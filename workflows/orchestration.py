import asyncio
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from agents.shards_agents import BaseAgent, AgentResult

class WorkflowStep(BaseModel):
    """Represents a single step in a multi-agent workflow."""
    agent_name: str
    task: str
    status: str = "pending"
    result: Optional[AgentResult] = None
    timestamp: datetime = Field(default_factory=datetime.now)

class WorkflowState(BaseModel):
    """Manages the state of a multi-agent workflow."""
    workflow_id: str
    steps: List[WorkflowStep] = Field(default_factory=list)
    global_context: Dict[str, Any] = Field(default_factory=dict)
    status: str = "initialized"

    def add_step(self, agent_name: str, task: str):
        self.steps.append(WorkflowStep(agent_name=agent_name, task=task))

    def update_step(self, index: int, result: AgentResult):
        self.steps[index].result = result
        self.steps[index].status = result.status
        self.steps[index].timestamp = datetime.now()

class WorkflowOrchestrator:
    """
    Advanced workflow orchestrator for Shards AI Agent System.
    Manages complex, multi-step agent interactions and state.
    """
    def __init__(self, agents: List[BaseAgent], verbose: bool = True):
        self.agents = {agent.name: agent for agent in agents}
        self.verbose = verbose
        self.active_workflows: Dict[str, WorkflowState] = {}

    def log(self, message: str, level: str = "INFO"):
        if self.verbose:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [Orchestrator] [{level}] {message}")

    async def execute_workflow(self, workflow_id: str, steps_config: List[Dict[str, str]]) -> WorkflowState:
        """
        Executes a predefined multi-agent workflow.
        """
        self.log(f"Initializing workflow: {workflow_id}")
        state = WorkflowState(workflow_id=workflow_id)
        
        for step in steps_config:
            state.add_step(step["agent"], step["task"])
        
        self.active_workflows[workflow_id] = state
        state.status = "running"

        for i, step in enumerate(state.steps):
            agent = self.agents.get(step.agent_name)
            if not agent:
                error_msg = f"Agent '{step.agent_name}' not found for step {i}."
                self.log(error_msg, "ERROR")
                state.status = "failed"
                return state

            self.log(f"Executing step {i+1}/{len(state.steps)}: {step.agent_name} -> {step.task}")
            
            # Inject global context into agent task if needed
            task_with_context = f"{step.task}. Context: {state.global_context}"
            
            try:
                result = await agent.run(task_with_context)
                state.update_step(i, result)
                
                # Update global context with agent result metadata
                if result.status == "success":
                    state.global_context.update(result.metadata)
                else:
                    self.log(f"Step {i+1} failed. Stopping workflow.", "WARNING")
                    state.status = "failed"
                    break
            except Exception as e:
                self.log(f"Error in step {i+1}: {str(e)}", "ERROR")
                state.status = "failed"
                break

        if state.status != "failed":
            state.status = "completed"
            self.log(f"Workflow {workflow_id} completed successfully.")
        
        return state

    async def run_enterprise_closing(self) -> WorkflowState:
        """
        Example: High-level enterprise financial closing workflow.
        """
        steps = [
            {"agent": "RevenueAgent", "task": "Analyze Q1 revenue data and identify key drivers."},
            {"agent": "NemotronAgent", "task": "Predict Q2 growth based on Q1 analysis and market trends."},
            {"agent": "KernelAgent", "task": "Verify ledger integrity on Shards Kernel for the reported period."},
            {"agent": "NemoClawAgent", "task": "Deploy the final report to the enterprise dashboard via NIM."}
        ]
        return await self.execute_workflow("enterprise_closing_2026", steps)
