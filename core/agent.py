import abc
import json
import asyncio
from typing import List, Dict, Any, Optional, Union, Callable
from pydantic import BaseModel, Field
from datetime import datetime

class AgentAction(BaseModel):
    """Represents a single action taken by an agent."""
    tool: str
    tool_input: Dict[str, Any]
    thought: str
    timestamp: datetime = Field(default_factory=datetime.now)

class AgentObservation(BaseModel):
    """Represents an observation resulting from an action."""
    content: Any
    timestamp: datetime = Field(default_factory=datetime.now)

class AgentMemory(BaseModel):
    """Manages the agent's short-term and long-term memory."""
    history: List[Union[AgentAction, AgentObservation, Dict[str, str]]] = Field(default_factory=list)
    context: Dict[str, Any] = Field(default_factory=dict)

    def add_action(self, action: AgentAction):
        self.history.append(action)

    def add_observation(self, observation: AgentObservation):
        self.history.append(observation)

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content, "timestamp": datetime.now().isoformat()})

    def get_full_history(self) -> List[Dict[str, Any]]:
        return [item if isinstance(item, dict) else item.dict() for item in self.history]

class AgentResult(BaseModel):
    """The final result of an agent's task execution."""
    output: str
    actions: List[AgentAction] = Field(default_factory=list)
    status: str = "success"
    metadata: Dict[str, Any] = Field(default_factory=dict)

class BaseAgent(abc.ABC):
    """Advanced base class for all Shards agents."""
    def __init__(self, name: str, role: str, goal: str, verbose: bool = True):
        self.name = name
        self.role = role
        self.goal = goal
        self.verbose = verbose
        self.memory = AgentMemory()
        self.tools: Dict[str, Dict[str, Any]] = {}

    def add_tool(self, name: str, func: Callable, description: str, schema: Optional[Dict[str, Any]] = None):
        """Registers a tool with the agent."""
        self.tools[name] = {
            "func": func,
            "description": description,
            "schema": schema or {}
        }

    @abc.abstractmethod
    async def run(self, task: str) -> AgentResult:
        """Executes the given task using the agent's reasoning logic."""
        pass

    def log(self, message: str, level: str = "INFO"):
        """Logs a message if verbose mode is enabled."""
        if self.verbose:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{self.name}] [{level}] {message}")

    async def call_tool(self, tool_name: str, tool_input: Dict[str, Any]) -> AgentObservation:
        """Safely calls a registered tool."""
        if tool_name not in self.tools:
            error_msg = f"Tool '{tool_name}' not found."
            self.log(error_msg, "ERROR")
            return AgentObservation(content=error_msg)

        self.log(f"Calling tool: {tool_name} with input: {tool_input}")
        try:
            func = self.tools[tool_name]["func"]
            if asyncio.iscoroutinefunction(func):
                result = await func(**tool_input)
            else:
                result = func(**tool_input)
            
            observation = AgentObservation(content=result)
            self.memory.add_observation(observation)
            return observation
        except Exception as e:
            error_msg = f"Error calling tool '{tool_name}': {str(e)}"
            self.log(error_msg, "ERROR")
            return AgentObservation(content=error_msg)

    def get_system_prompt(self) -> str:
        """Generates the system prompt for the agent."""
        tools_desc = "\n".join([f"- {name}: {info['description']}" for name, info in self.tools.items()])
        return f"""You are {self.name}, the {self.role}.
Your goal is: {self.goal}

Available Tools:
{tools_desc}

Reasoning Process:
1. Thought: Analyze the current state and decide the next step.
2. Action: Choose a tool and provide input.
3. Observation: Review the result of the action.
4. Repeat until the goal is achieved.
"""
