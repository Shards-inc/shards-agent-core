# Shards AI Agent System API Reference

This document provides a detailed reference for the core classes and methods in the Shards AI Agent System.

## 1. Core Module (`core/agent.py`)

### `BaseAgent`
The abstract base class for all Shards agents.

| Method | Description |
| :--- | :--- |
| `__init__(name, role, goal)` | Initializes a new agent with a name, role, and goal. |
| `add_tool(name, func, description)` | Registers a tool that the agent can use. |
| `run(task)` | Abstract method to execute a task. Returns an `AgentResult`. |
| `log_thought(thought)` | Logs the agent's internal reasoning process. |
| `log_action(action)` | Logs an action taken by the agent. |

### `AgentAction`
A Pydantic model representing an action taken by an agent.

| Field | Type | Description |
| :--- | :--- | :--- |
| `tool` | `str` | The name of the tool to be used. |
| `tool_input` | `Dict[str, Any]` | The input arguments for the tool. |
| `thought` | `str` | The reasoning behind taking this action. |

### `AgentResult`
A Pydantic model representing the result of an agent's task execution.

| Field | Type | Description |
| :--- | :--- | :--- |
| `output` | `str` | The final output or response from the agent. |
| `actions` | `List[AgentAction]` | A list of actions taken during execution. |
| `status` | `str` | The status of the execution (e.g., "success", "failure"). |

## 2. Agents Module (`agents/shards_agents.py`)

### `KernelAgent`
Specialized agent for managing Shards Foundation kernels.

### `RevenueAgent`
Specialized agent for autonomous revenue generation and analysis.

### `NemotronAgent`
Agent leveraging NVIDIA Nemotron models for advanced reasoning.

### `NemoClawAgent`
Agent for integrating with the NVIDIA NemoClaw enterprise platform.

### `OrchestratorAgent`
Agent for coordinating multi-agent workflows.

## 3. Workflows Module (`workflows/orchestration.py`)

### `WorkflowOrchestrator`
Manages complex, multi-step agent interactions and state.

| Method | Description |
| :--- | :--- |
| `execute_enterprise_workflow(name, data)` | Executes a predefined enterprise workflow. |

## 4. Tools Module (`tools/mcp_client.py`)

### `MCPClient`
Client for interacting with Model Context Protocol (MCP) servers.

| Method | Description |
| :--- | :--- |
| `connect()` | Connects to the specified MCP server and discovers tools. |
| `call_tool(name, args)` | Calls a specific tool on the MCP server. |
| `get_tools()` | Returns a list of discovered MCP tools. |
