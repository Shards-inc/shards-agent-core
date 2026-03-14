import asyncio
from agents.shards_agents import KernelAgent, RevenueAgent, NemotronAgent, NemoClawAgent, OrchestratorAgent, DataAnalysisAgent, SecurityAgent
from tools.mcp_client import MCPClient

async def run_demo():
    print("\n--- Initializing Shards AI Agent System Demo ---")

    # Initialize specialized agents
    kernel_agent = KernelAgent()
    revenue_agent = RevenueAgent()
    nemotron_agent = NemotronAgent()
    nemoclaw_agent = NemoClawAgent()
    data_analysis_agent = DataAnalysisAgent()
    security_agent = SecurityAgent()
    
    orchestrator_agent = OrchestratorAgent(agents=[kernel_agent, revenue_agent, nemotron_agent, nemoclaw_agent, data_analysis_agent, security_agent])

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
    kernel_task = "Perform a security audit on kernel 'K-alpha-7'."
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
    nemoclaw_task = "Orchestrate data synchronization between ERP and CRM systems."
    print(f"\n[DEMO] NemoClawAgent processing: {nemoclaw_task}")
    nemoclaw_result = await nemoclaw_agent.run(nemoclaw_task)
    print(f"[DEMO] NemoClawAgent Result: {nemoclaw_result.output}")

    # Example task for DataAnalysisAgent
    data_analysis_task = "Analyze customer feedback data from Q4 2025 and identify key sentiment trends."
    print(f"\n[DEMO] DataAnalysisAgent processing: {data_analysis_task}")
    data_analysis_result = await data_analysis_agent.run(data_analysis_task)
    print(f"[DEMO] DataAnalysisAgent Result: {data_analysis_result.output}")

    # Example task for SecurityAgent
    security_task = "Perform a vulnerability scan on the agent deployment environment."
    print(f"\n[DEMO] SecurityAgent processing: {security_task}")
    security_result = await security_agent.run(security_task)
    print(f"[DEMO] SecurityAgent Result: {security_result.output}")

    print("\n--- Running orchestrated workflow ---")

    # Example complex task for OrchestratorAgent
    orchestration_task = (
        "Orchestrate the Q1 financial closing process, ensuring kernel integrity, "
        "generating a comprehensive revenue analysis report, analyzing market trends, "
        "synchronizing data, and performing a security audit."
    )
    print(f"\n[DEMO] OrchestratorAgent processing: {orchestration_task}")
    orchestration_result = await orchestrator_agent.run(orchestration_task)
    print(f"[DEMO] OrchestratorAgent Result: {orchestration_result.output}")

    print("\n--- Demo Complete ---")
