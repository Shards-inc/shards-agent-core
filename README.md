# Shards AI Agent System (shards-agent-core)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![NVIDIA NemoClaw Compatible](https://img.shields.io/badge/NVIDIA-NemoClaw--Ready-green.svg)](https://www.nvidia.com/en-us/ai-data-science/generative-ai/)

> **The Foundational Operating System for Autonomous Enterprise Intelligence.**

The **Shards AI Agent System** is a modular, high-performance framework designed for **Shards Inc / Shards Foundation**. It provides the infrastructure to build, deploy, and orchestrate specialized autonomous agents that integrate seamlessly with the **NVIDIA NemoClaw** ecosystem and **Shards Kernels**.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Core Architecture](#-core-architecture)
- [The "Claw" Ecosystem Integration](#-the-claw-ecosystem-integration)
- [Specialized Agents](#-specialized-agents)
- [Multi-Agent Orchestration](#-multi-agent-orchestration)
- [Installation & Setup](#-installation--setup)
- [Usage & Examples](#-usage--examples)
- [Security & Governance](#-security--governance)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

In the rapidly evolving landscape of 2026, AI is shifting from static models to **autonomous agents**. The Shards AI Agent System is built to capture this shift by providing a robust runtime layer for enterprise-grade agents.

### Key Capabilities:
- **Deterministic Control**: Integration with Shards Kernels for precise, verifiable operations.
- **Advanced Reasoning**: Powered by NVIDIA Nemotron models for complex, multi-step problem solving.
- **Enterprise Orchestration**: A sophisticated workflow engine that manages state across multiple specialized agents.
- **MCP Native**: Built-in support for the Model Context Protocol (MCP) to connect with any external tool or service.

---

## 🏗 Core Architecture

The system follows a layered architecture designed for scalability, security, and modularity.

```text
Application Layer (Enterprise Workflows)
    │
Orchestration Layer (WorkflowOrchestrator)
    │
Agent Layer (Kernel, Revenue, Nemotron, NemoClaw Agents)
    │
Core Engine (BaseAgent, Memory, Reasoning)
    │
Infrastructure Layer (MCP, NIM, Shards Kernels)
```

### Components:
- **`core/`**: The heartbeat of the system. Contains the `BaseAgent` with integrated memory management and tool-calling logic.
- **`agents/`**: Specialized agent implementations with domain-specific logic.
- **`workflows/`**: State management and orchestration logic for multi-agent tasks.
- **`tools/`**: Standardized connectors, including the production-ready `MCPClient`.

---

## 🦞 The "Claw" Ecosystem Integration

The Shards AI Agent System is fully compatible with the NVIDIA "Claw" ecosystem, enabling enterprise-scale deployment and high-performance inference.

| System | Integration Level | Focus |
| :--- | :--- | :--- |
| **NemoClaw** | Platform Native | Enterprise agent platform and NIM container orchestration. |
| **Nemotron** | Reasoning Engine | Advanced reasoning, coding, and multi-step logic. |
| **NIM** | Inference Runtime | High-performance, containerized microservices for agent deployment. |
| **NeMo** | Toolkit Integration | Leveraging NVIDIA's agent toolkit for enhanced capabilities. |

---

## 🤖 Specialized Agents

The system includes a suite of pre-built agents, each optimized for specific enterprise functions:

1. **KernelAgent**: Manages Shards Foundation kernels. Focuses on deterministic control and security audits.
2. **RevenueAgent**: The financial brain. Analyzes ERP data, identifies growth drivers, and optimizes revenue workflows.
3. **NemotronAgent**: The logic specialist. Decomposes complex tasks and provides high-accuracy reasoning.
4. **NemoClawAgent**: The platform integrator. Manages agent lifecycles within the NVIDIA enterprise ecosystem.
5. **OrchestratorAgent**: The conductor. Coordinates the other agents to complete end-to-end business processes.

---

## 🎼 Multi-Agent Orchestration

Orchestration is handled by the `WorkflowOrchestrator`, which manages a `WorkflowState` across multiple steps.

### Example: Financial Closing Workflow
1. **RevenueAgent** pulls and analyzes Q1 data.
2. **NemotronAgent** predicts Q2 growth based on Q1 results.
3. **KernelAgent** verifies the integrity of the ledger on the Shards Kernel.
4. **NemoClawAgent** deploys the final executive report to the enterprise dashboard.

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Access to Shards Foundation MCP servers (optional for local testing)
- NVIDIA NIM API keys (for production deployment)

### Local Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Shards-inc/shards-agent-core.git
   cd shards-agent-core
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the demo**:
   ```bash
   python main.py
   ```

---

## 📖 Usage & Examples

### Creating a Custom Agent
```python
from core.agent import BaseAgent, AgentResult

class MyCustomAgent(BaseAgent):
    async def run(self, task: str) -> AgentResult:
        self.log(f"Processing: {task}")
        # Your custom logic here
        return AgentResult(output="Task completed", status="success")
```

### Executing a Workflow
```python
from workflows.orchestration import WorkflowOrchestrator
from agents.shards_agents import RevenueAgent, NemotronAgent

orchestrator = WorkflowOrchestrator(agents=[RevenueAgent(), NemotronAgent()])
state = await orchestrator.run_enterprise_closing()
print(f"Workflow Status: {state.status}")
```

---

## 🛡 Security & Governance

Security is baked into the core of the Shards AI Agent System:
- **Sandboxed Execution**: Agents operate in restricted environments.
- **Deterministic Oversight**: Integration with `Kloc-kernel-level-oversight-council` for policy enforcement.
- **Audit Logging**: Every thought, action, and observation is logged with timestamps for full traceability.
- **Access Control**: Enterprise-grade authentication for all MCP and NIM connections.

---

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:
- [**Shards Agent Guide**](docs/Shards_Agent_Guide.md): Comprehensive system overview.
- [**API Reference**](docs/API_Reference.md): Detailed class and method documentation.
- [**Deployment Guide**](docs/deployment_guide.md): Instructions for local, Docker, and Cloud (NIM) deployment.
- [**NemoClaw Integration**](docs/NemoClaw_Integration.md): Deep dive into the NVIDIA ecosystem.
- [**Nemotron Integration**](docs/Nemotron_Integration.md): Leveraging advanced reasoning models.

---

## 🤝 Contributing

We welcome contributions from the community! Please see our [**CONTRIBUTING.md**](CONTRIBUTING.md) for guidelines on how to get started. All contributors are expected to adhere to our [**CODE_OF_CONDUCT.md**](CODE_OF_CONDUCT.md).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

© 2026 Shards Inc / Shards Foundation. Built with precision by **Manus AI**.
