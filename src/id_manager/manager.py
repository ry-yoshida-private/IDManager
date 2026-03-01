
class IDManager:
    """
    IDManager is a class that manages the ID.

    Attributes:
    ----------
    current_id: int
        The current ID.
    step: int
        The step size.
    """
    def __init__(
        self, 
        start: int = 0,
        step: int = 1
        ):
        """
        Initialize the IDManager.
        
        Parameters
        ----------
        start : int, optional
            The start ID. Default is 0.
        step : int, optional
            The step size. Default is 1.
        """
        if step == 0:
            raise ValueError("step must be not 0")
        self.current_id = start
        self.step = step
     
    def get_next_id(self) -> int:
        """
        Get the next ID.
        
        Returns
        -------
        int
            The next ID.
        """
        next_id = self.current_id
        self.current_id += self.step
        return next_id

    def reset(
        self, 
        start: int = 0
        ) -> None:
        """
        Reset the IDManager.
        
        Parameters
        ----------
        start : int, optional
            The start ID. Default is 0.
        """
        self.current_id = start
    
    def __str__(self):
        return f"IDManager(current_id={self.current_id}, step={self.step})"

    def __repr__(self):
        return self.__str__()
