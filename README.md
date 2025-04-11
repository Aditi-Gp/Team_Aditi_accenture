# Team_Aditi_accenture

An intelligent multi-agent system to optimize retail inventory using on-prem Ollama-based LLMs
# 🧠 Retail Inventory Optimization with Multi-Agent AI System

I built a **Multi-Agent AI System** to optimize retail inventory using **Ollama-powered local LLMs**, **embedding-based reasoning**, and **real-time data insights**. This platform delivers intelligent recommendations across **demand forecasting**, **inventory monitoring**, **customer segmentation**, and **pricing optimization**.

---

## 🌟 What Makes My Approach Stand Out

### ✅ LLM-Powered Multi-Agent Reasoning  
I orchestrated **4 functional agents** — *Demand, Inventory, Pricing,* and *Customer* — each equipped with ML tools and custom logic. These agents collaborate through a reasoning layer powered by an **on-premise LLM**, which interprets their insights and generates adaptive action plans — emulating real-world decision-making.

### ✅ Privacy-Preserving Deployment  
All LLM operations run **locally via Ollama**, ensuring data privacy and enterprise-grade compliance — a key differentiator from cloud-only solutions.

### ✅ Integration of Custom Tools  
Each agent leverages **custom APIs**, **web scrapers**, **ML models**, and **FAISS-based embeddings** for enhanced decision-making, enabling rich personalization beyond rule-based systems.

### ✅ Scalable, Modular Architecture  
The system uses **SQLite** for unified data storage and is built on a **FastAPI** backend with a **React** frontend — delivering real-time interaction and seamless visualization.

### ✅ Render Deployment with Mock LLM Fallback  
To accommodate cloud hosting constraints, I deployed the system on **Render** with a **mock LLM fallback**, preserving pipeline behavior and making the solution demo-friendly.

---

## ⚙️ Tech Stack

| Component     | Tech Used                          |
|---------------|------------------------------------|
| 🧠 Local LLM   | Ollama (LLaMA3 / Mistral)          |
| 🔁 Agent Logic | Python modules, custom orchestration |
| 📊 ML/Embeddings | Scikit-learn, FAISS, NumPy       |
| 🛠️ Tools       | Custom APIs, Web Scrapers          |
| 🗃️ Database     | SQLite                            |
| 🧩 Backend      | FastAPI                            |
| 🌐 Frontend     | React.js                          |
| ☁️ Hosting      | Render + Mock LLM Fallback         |

---

## 📌 Bonus Highlights

- **Seamless extensibility:** Add new agents (e.g., supplier, logistics) or plug into real-time inventory systems.
- **Modular and explainable:** Each agent logs its decisions; the LLM provides a human-readable rationale.
- **Production-conscious:** Designed with real-world constraints in mind — latency, edge deployment, and core retail KPIs.

---

## 🚀 Get Started

> Want to run the system or explore the demo?  
> Refer to the [`/docs`](./docs) folder for setup instructions, architecture, and agent configurations.
