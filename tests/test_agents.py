import unittest
import asyncio
from agents.shards_agents import KernelAgent, RevenueAgent, NemotronAgent, NemoClawAgent

class TestShardsAgents(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_kernel_agent_initialization(self):
        agent = KernelAgent()
        self.assertEqual(agent.name, "KernelAgent")
        self.assertEqual(agent.role, "Deterministic Control Plane Manager")

    def test_revenue_agent_initialization(self):
        agent = RevenueAgent()
        self.assertEqual(agent.name, "RevenueAgent")
        self.assertEqual(agent.role, "Autonomous Revenue Generation Specialist")

    def test_nemotron_agent_initialization(self):
        agent = NemotronAgent()
        self.assertEqual(agent.name, "NemotronAgent")
        self.assertEqual(agent.role, "Nemotron-powered Reasoning Specialist")

    def test_nemoclaw_agent_initialization(self):
        agent = NemoClawAgent()
        self.assertEqual(agent.name, "NemoClawAgent")
        self.assertEqual(agent.role, "Enterprise AI Agent Platform Integrator")

    def test_agent_run(self):
        agent = KernelAgent()
        result = self.loop.run_until_complete(agent.run("Test task"))
        self.assertEqual(result.status, "success")
        self.assertIn("KernelAgent processed: Test task", result.output)

if __name__ == "__main__":
    unittest.main()
