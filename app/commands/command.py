class Command:
    """Abstract base class for command implementations."""

    def execute(self, *args):
        """Executes the command with given arguments.
        
        Subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement this method.")
