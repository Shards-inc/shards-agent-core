import pytest
import asyncio
from agents.shards_agents import KernelAgent, RevenueAgent, DataAnalysisAgent, SecurityAgent

@pytest.mark.asyncio
async def test_kernel_agent():
    agent = KernelAgent()
    result = await agent.run("Test task")
    assert result.status == "success"
    assert "KernelAgent" in result.output

@pytest.mark.asyncio
async def test_revenue_agent():
    agent = RevenueAgent()
    result = await agent.run("Test task")
    assert result.status == "success"
    assert "RevenueAgent" in result.output

@pytest.mark.asyncio
async def test_data_analysis_agent():
    agent = DataAnalysisAgent()
    result = await agent.run("Test task")
    assert result.status == "success"
    assert "DataAnalysisAgent" in result.output

@pytest.mark.asyncio
async def test_security_agent():
    agent = SecurityAgent()
    result = await agent.run("Test task")
    assert result.status == "success"
    assert "SecurityAgent" in result.output
