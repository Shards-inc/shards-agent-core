import abc
import json
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AgentAction(BaseModel):
    tool: str
    tool_input: Dict[str, Any]
    thought: str

class AgentResult(BaseModel):
    output: str
    actions: List[AgentAction] = Field(default_factory=list)
    status: str = "success"

class BaseAgent(abc.ABC):
    def __init__(self, name: str, role: str, goal: str):
        self.name = name
        self.role = role
        self.goal = goal
        self.memory: List[Dict[str, Any]] = []
        self.tools: Dict[str, Any] = {}

    def add_tool(self, name: str, func: Any, description: str):
        self.tools[name] = {"func": func, "description": description}

    @abc.abstractmethod
    async def run(self, task: str) -> AgentResult:
        pass

    def log_thought(self, thought: str):
        print(f"[{self.name}] Thought: {thought}")
        self.memory.append({"role": "thought", "content": thought})

    def log_action(self, action: AgentAction):
        print(f"[{self.name}] Action: {action.tool}({action.tool_input})")
        self.memory.append({"role": "action", "content": action.dict()})
