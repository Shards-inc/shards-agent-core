import asyncio
from typing import List, Dict, Any
from agents.shards_agents import KernelAgent, RevenueAgent, NemotronAgent, NemoClawAgent
from workflows.orchestration import WorkflowOrchestrator
from tools.mcp_client import MCPClient

async def main():
    print("\n" + "="*60)
    print("   SHARDS AI AGENT SYSTEM - ENTERPRISE ORCHESTRATION DEMO")
    print("="*60 + "\n")

    # 1. Initialize Specialized Agents
    kernel_agent = KernelAgent(verbose=True)
    revenue_agent = RevenueAgent(verbose=True)
    nemotron_agent = NemotronAgent(verbose=True)
    nemoclaw_agent = NemoClawAgent(verbose=True)

    # 2. Initialize MCP Client and Connect
    mcp_client = MCPClient(server_url="https://mcp.shards.foundation")
    await mcp_client.connect()

    # 3. Register MCP Tools to Agents
    # For example, register kernel control to KernelAgent
    for tool in mcp_client.get_tools():
        if "kernel" in tool.name:
            kernel_agent.add_tool(
                name=tool.name,
                func=mcp_client.call_tool,
                description=tool.description,
                schema=tool.input_schema
            )
        elif "revenue" in tool.name:
            revenue_agent.add_tool(
                name=tool.name,
                func=mcp_client.call_tool,
                description=tool.description,
                schema=tool.input_schema
            )
        elif "nemotron" in tool.name:
            nemotron_agent.add_tool(
                name=tool.name,
                func=mcp_client.call_tool,
                description=tool.description,
                schema=tool.input_schema
            )

    # 4. Initialize Workflow Orchestrator
    agents = [kernel_agent, revenue_agent, nemotron_agent, nemoclaw_agent]
    orchestrator = WorkflowOrchestrator(agents=agents, verbose=True)

    # 5. Execute Enterprise Workflow: Financial Closing 2026
    print("\n" + "-"*60)
    print("   EXECUTING ENTERPRISE WORKFLOW: FINANCIAL CLOSING 2026")
    print("-"*60 + "\n")
    
    workflow_state = await orchestrator.run_enterprise_closing()

    # 6. Display Workflow Results
    print("\n" + "="*60)
    print(f"   WORKFLOW {workflow_state.workflow_id} STATUS: {workflow_state.status.upper()}")
    print("="*60 + "\n")

    for i, step in enumerate(workflow_state.steps):
        print(f"Step {i+1}: {step.agent_name}")
        print(f"  Task: {step.task}")
        print(f"  Status: {step.status}")
        if step.result:
            print(f"  Output: {step.result.output[:100]}...")
        print("-" * 30)

    print("\n" + "="*60)
    print("   SHARDS AI AGENT SYSTEM - DEMO COMPLETE")
    print("="*60 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
