import asyncio
from agents.shards_agents import KernelAgent, RevenueAgent, OrchestratorAgent, NemotronAgent, NemoClawAgent
from tools.mcp_client import MCPClient

async def run_demo():
    print("\n--- Initializing Shards AI Agent System Demo ---")

    # Initialize specialized agents
    kernel_agent = KernelAgent()
    revenue_agent = RevenueAgent()
    nemotron_agent = NemotronAgent()
    nemoclaw_agent = NemoClawAgent()
    
    orchestrator_agent = OrchestratorAgent(agents=[kernel_agent, revenue_agent, nemotron_agent, nemoclaw_agent])

    # Initialize MCP client
    mcp_client = MCPClient(server_url="https://mcp.shards.foundation")
    await mcp_client.connect()

    # Register MCP tools to agents (example for KernelAgent)
    for tool in mcp_client.get_tools():
        kernel_agent.add_tool(
            name=tool.name,
            func=mcp_client.call_tool,
            description=tool.description
        )
    
    print("\n--- Running individual agent tasks ---")

    # Example task for KernelAgent
    kernel_task = "Perform a security audit on kernel \'K-alpha-7\'."
    print(f"\n[DEMO] KernelAgent processing: {kernel_task}")
    kernel_result = await kernel_agent.run(kernel_task)
    print(f"[DEMO] KernelAgent Result: {kernel_result.output}")

    # Example task for RevenueAgent
    revenue_task = "Generate Q1 2026 revenue report and identify growth opportunities."
    print(f"\n[DEMO] RevenueAgent processing: {revenue_task}")
    revenue_result = await revenue_agent.run(revenue_task)
    print(f"[DEMO] RevenueAgent Result: {revenue_result.output}")

    # Example task for NemotronAgent
    nemotron_task = "Analyze market trends for Q1 2026 and predict Q2 growth."
    print(f"\n[DEMO] NemotronAgent processing: {nemotron_task}")
    nemotron_result = await nemotron_agent.run(nemotron_task)
    print(f"[DEMO] NemotronAgent Result: {nemotron_result.output}")

    # Example task for NemoClawAgent
    nemoclaw_task = "Deploy a new workflow for automated customer support ticket routing."
    print(f"\n[DEMO] NemoClawAgent processing: {nemoclaw_task}")
    nemoclaw_result = await nemoclaw_agent.run(nemoclaw_task)
    print(f"[DEMO] NemoClawAgent Result: {nemoclaw_result.output}")

    print("\n--- Running orchestrated workflow ---")

    # Example complex task for OrchestratorAgent
    orchestration_task = (
        "Orchestrate the Q1 financial closing process, ensuring kernel integrity, "
        "generating a comprehensive revenue analysis report, and deploying a new customer support workflow."
    )
    print(f"\n[DEMO] OrchestratorAgent processing: {orchestration_task}")
    orchestration_result = await orchestrator_agent.run(orchestration_task)
    print(f"[DEMO] OrchestratorAgent Result: {orchestration_result.output}")

    print("\n--- Demo Complete ---")

if __name__ == "__main__":
    asyncio.run(run_demo())
