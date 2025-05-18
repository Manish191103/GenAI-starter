# GenAI-starter: Modular AI Agent Framework

## Overview
GenAI-starter is a modular, extensible framework for building advanced AI agents. Inspired by modern agent architectures, it enables integration of tools, memory, planning, and action modules, making it easy to prototype and extend intelligent systems.

## Architecture
The framework is based on the following architecture:

```
[Tools] <--> [Agent] <--> [Memory]
   |             |            |
   v             v            v
[Action]     [Planning]   [Short/Long-term Memory]
```

- **Agent**: The central controller that orchestrates tool usage, memory, planning, and actions.
- **Tools**: External capabilities (e.g., Calendar, Calculator, Code Interpreter, Search) that the agent can use.
- **Memory**: Handles both short-term and long-term memory for context retention and learning.
- **Planning**: Responsible for reflection, self-critique, chain of thoughts, and subgoal decomposition.
- **Action**: Executes decisions and interacts with the environment or user.

*Refer to the architecture diagram for a visual representation.*

## Architecture Recommendations
Based on emerging LLM application stack patterns, the framework should incorporate:

```
                  [Embedding Models] <---> [Vector Databases]
                           |                      |
                           v                      v
[External APIs] <---> [Agent/Orchestration] <---> [Memory Systems]
       |                    |     |                    |
       v                    v     v                    v
  [Plugins]           [Planning] [Actions]     [LLM Cache]
                           |                      |
                           v                      v
                    [Validation] <---> [Logging/Monitoring]
```

- **Vector Databases**: For efficient semantic search of knowledge and context.
- **Embedding Models**: To convert text and other data types into vector representations.
- **LLM Cache**: Store and reuse responses to similar queries for better performance.
- **Validation**: Ensure inputs and outputs meet quality and safety standards.
- **Logging/Monitoring**: Track agent operations, performance metrics, and errors.
- **Cloud Provider Abstraction**: Support multiple LLM providers through a unified interface.

## Main Components
- `src/agent.py`: Main Agent class and orchestration logic.
- `src/tools.py`: Tool interface and example tool implementations.
- `src/memory.py`: Memory management (short-term and long-term).
- `src/planning.py`: Planning, reflection, and reasoning logic.
- `src/action.py`: Action execution logic.
- `src/a2a.py`: Agent-to-Agent protocol implementation.
- `src/embeddings.py`: Text and data embedding functionality.
- `src/vector_db.py`: Vector database integration for semantic search.
- `src/cache.py`: LLM response caching mechanisms.
- `src/validation.py`: Input/output validation utilities.
- `src/logging.py`: Observability and monitoring components.
- `src/providers.py`: Abstraction layer for different LLM providers.
- `main.py`: Entry point to run the agent.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd GenAI-starter
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the agent:**
   ```bash
   python main.py
   ```

## Usage Example
After running `main.py`, the agent will initialize its core modules and be ready to accept tasks, use tools, and demonstrate basic planning and memory capabilities. You can extend the agent by adding new tools or enhancing planning/memory logic.

## Extensibility
- **Add new tools:** Implement new classes in `src/tools.py` and register them with the agent.
- **Enhance memory:** Expand `src/memory.py` to use vector databases or other storage systems.
- **Improve planning:** Add advanced reasoning, reflection, or self-critique in `src/planning.py`.
- **Custom actions:** Implement new action types in `src/action.py`.
- **Vector search:** Connect to vector databases like FAISS, Chroma, or Pinecone.
- **Provider integration:** Add support for new LLM providers via the abstraction layer.
- **Enhanced observability:** Extend logging and monitoring capabilities.

## Agent-to-Agent (A2A) Protocol
GenAI-starter supports an Agent-to-Agent (A2A) protocol, enabling multiple agents to communicate, collaborate, and delegate tasks. The A2A protocol defines a standard message format and communication interface, making it easy to build distributed or collaborative agent systems.

**A2A Features:**
- Standardized message format for agent communication.
- Support for collaboration, task delegation, and knowledge sharing.
- Extensible to support local or networked agent communication.
- Foundation for building multi-agent, decentralized, or swarm intelligence systems.

**Extending A2A:**
- Implement new communication backends (e.g., HTTP, WebSocket, message queues).
- Add agent discovery, authentication, and trust mechanisms.
- Enable agents with specialized skills to work together on complex problems.

## License
MIT License