from dataclasses import dataclass, field
from threading import Lock

@dataclass
class IDManager:
    """
    IDManager is a class that manages the ID in a thread-safe manner.

    Attributes:
    ----------
    current_id: int
        The current ID.
    step: int
        The step size.
    _lock: Lock
        A threading lock to ensure atomic operations.
    """
    current_id: int = 0
    step: int = 1
    _lock: Lock = field(default_factory=Lock, init=False, repr=False)

    def __post_init__(self):
        """
        Validate the IDManager after initialization.

        Raises:
        -------
        ValueError
            If the step size is 0.
        """
        if self.step == 0:
            raise ValueError("step must be not 0")

    @property
    def next_id(self) -> int:
        """
        Get the next ID and increment the current ID.
        This property is thread-safe.

        Returns
        -------
        int
            The next ID.
        """
        with self._lock:
            next_val = self.current_id
            self.current_id += self.step
            return next_val

    def reset(
        self, 
        start: int = 0
        ) -> None:
        """
        Reset the IDManager to a specific start value.
        This method is thread-safe.

        Parameters
        ----------
        start : int, optional
            The start ID. Default is 0.
        """
        with self._lock:
            self.current_id = start

    def __str__(self):
        return f"IDManager(current_id={self.current_id}, step={self.step})"

    def __repr__(self):
        return self.__str__()
