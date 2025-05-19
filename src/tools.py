"""
Tool interface and example tool implementations for GenAI-starter framework.
"""

class Tool:
    """
    Base class for all tools used by the agent.
    """
    
    def __init__(self, name):
        """
        Initialize a new tool instance.
        
        Args:
            name (str): The name of the tool
        """
        self.name = name
        
    def execute(self, *args, **kwargs):
        """
        Execute the tool's functionality.
        
        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            The result of the tool execution
        """
        raise NotImplementedError("Tool subclasses must implement execute method")
        
        
class Calculator(Tool):
    """
    Example calculator tool that can perform basic arithmetic operations.
    """
    
    def __init__(self):
        """Initialize a new calculator tool."""
        super().__init__(name="Calculator")
        
    def execute(self, expression):
        """
        Evaluate a mathematical expression.
        
        Args:
            expression (str): The expression to evaluate
            
        Returns:
            The result of the evaluation
        """
        # This is a simple implementation - in a real tool you'd want proper validation and error handling
        try:
            # Using eval is not recommended for production, but this is just a placeholder example
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}" 