"""
Main entry point for the GenAI-starter framework.
"""

from src.agent import Agent
from src.tools import Calculator

def main():
    """Initialize and run the agent."""
    
    # Create a new agent
    agent = Agent(name="GenAI")
    
    # Register some tools
    agent.register_tool("calculator", Calculator())
    
    # Run the agent with a task
    result = agent.run("Calculate 2 + 2")
    
    # Print the result
    print(result)
    
    # Add more functionality later
    print("GenAI-starter framework initialized.")
    print("Ready to add your custom agent functionality!")
    

if __name__ == "__main__":
    main() 