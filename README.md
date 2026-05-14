# Architecting Event-Driven Agentic Systems  
## REST API vs Model Context Protocol (MCP)

This repository contains hands-on demonstrations for understanding the architectural differences between **Traditional REST APIs** and the **Model Context Protocol (MCP)** in modern AI-driven systems.

The demo shows how:

- **REST APIs** require human-written integration logic.
- **MCP** enables autonomous AI agents to dynamically discover and execute capabilities.
- **REST + MCP (Hybrid)** allows AI agents to interface with legacy REST APIs via an MCP wrapper.

---

# 🧠 Architectural Concepts

## Traditional REST API

REST (**Representational State Transfer**) is the standard architecture used in modern web applications.

REST works using:

- HTTP Methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`)
- Predefined URLs / Endpoints
- Stateless request-response communication

Example:

```http
GET /api/devices/edge_node_1
POST /api/devices/edge_node_1/restart
```

### REST Characteristics

✅ Standardized  
✅ Lightweight  
✅ Easy for frontend/backend integration  

### REST Limitations for AI Systems

❌ No runtime capability discovery  
❌ No conversational memory  
❌ Every workflow must be manually hardcoded  
❌ AI must know endpoints in advance  

---

## Model Context Protocol (MCP)

MCP (**Model Context Protocol**) is an open standard designed for AI-native communication.

Unlike REST, MCP allows AI agents to:

- Discover tools dynamically
- Maintain session context
- Execute multi-step reasoning
- Interact using JSON-RPC

Example:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "get_device"
  }
}
```

### MCP Advantages

✅ Runtime tool discovery  
✅ Stateful sessions  
✅ JSON-RPC communication  
✅ AI-driven orchestration  

---

## REST API + MCP (The Hybrid Approach)

When you already have a mature REST API and want to expose it to an AI agent, you don't need to rebuild it from scratch. You can build an **MCP Wrapper**.

The MCP Wrapper acts as a bridge:
1. It exposes **MCP Tools** to the AI agent.
2. When the AI agent calls an MCP Tool, the Wrapper translates it into standard **HTTP REST calls** to your existing backend.

This gives you the best of both worlds: maintaining your existing REST architecture for frontends while enabling dynamic AI discovery.

---

# 📁 Project Structure

```text
Demo/
├── 01_rest_api/
│   ├── server.py
│   └── client.py
│
├── 02_mcp/
│   ├── mcp_server.py
│   └── client.py
│
├── 03_rest_plus_mcp/
│   ├── mcp_wrapper.py
│   └── client.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Environment Setup

## 1. Create Virtual Environment

```bash
conda create -n demo python=3.12 -y
conda activate demo
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Demo

---

## Part 1: Traditional REST Demo

This demo shows how a developer manually writes integration logic using HTTP methods and URLs.

### Terminal 1 — Start REST Server

```bash
cd 01_rest_api
python server.py
```

Server runs at:

```text
http://127.0.0.1:8700
```

Swagger docs:

```text
http://127.0.0.1:8700/docs
```

---

### Terminal 2 — Run REST Client

```bash
cd 01_rest_api
python client.py
```

### What happens?

The client manually performs:

1. GET Device Status  
2. GET Device Logs  
3. POST Restart Device  
4. PUT Update Device  
5. PATCH Partial Update  
6. DELETE Device  

---

## Part 2: MCP Demo

This demo shows how an AI agent dynamically discovers capabilities using MCP.

### Terminal 1 — Start MCP Server

```bash
cd 02_mcp
python mcp_server.py
```

Server runs at:

```text
http://localhost:8200
```

SSE endpoint:

```text
http://localhost:8200/sse
```

---

### Terminal 2 — Run MCP Agent

```bash
cd 02_mcp
python client.py
```

---

### What happens?

The AI agent performs:

#### 1. Initialize Connection

```json
{
  "jsonrpc": "2.0",
  "method": "initialize"
}
```

---

#### 2. Discover Tools

```json
{
  "jsonrpc": "2.0",
  "method": "tools/list"
}
```

Available tools:

- `get_device`
- `get_logs`
- `restart_device`
- `update_device`
- `patch_device`
- `delete_device`

---

#### 3. Execute Tools Dynamically

Example:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "get_device"
  }
}
```

---

## Part 3: REST + MCP (Hybrid) Demo

This demo shows how to wrap an existing REST API using an MCP server, bridging legacy endpoints with modern AI agents.

### Terminal 1 — Start Existing REST Server

```bash
cd 01_rest_api
python server.py
```

### Terminal 2 — Start MCP Wrapper Server

```bash
cd 03_rest_plus_mcp
python mcp_wrapper.py
```

### Terminal 3 — Run MCP Agent

```bash
cd 03_rest_plus_mcp
python client.py
```

### What happens?

The AI agent connects to the MCP wrapper and discovers capabilities dynamically. When it decides to execute a tool (e.g., `restart_device`), the MCP wrapper translates that request into a standard `POST /api/devices/{device_id}/restart` HTTP request and forwards it to the existing REST API. The response is then routed back to the AI.

---

# 🧠 MCP Primitives Used

## Tools

Executable functions exposed to the AI.

Examples:

- `get_device()`
- `restart_device()`
- `delete_device()`

---

## Resources

Contextual data provided to the AI.

Example:

```text
resource://system/info
```

---

## Prompts

Reusable prompt templates for structured AI interactions.

Example:

```python
infrastructure_report_template()
```

---

# REST vs MCP Comparison

| Feature | REST API | MCP | REST + MCP Wrapper |
|---------|----------|-----|--------------------|
| Communication | HTTP | JSON-RPC | Client -> JSON-RPC -> Wrapper -> HTTP -> Backend |
| Discovery | Static Documentation | Runtime Discovery | Runtime Discovery |
| Context | Stateless | Stateful | Stateful (at Wrapper level) |
| Workflow | Human Written | AI Driven | AI Driven |
| Integration | Endpoint Based | Capability Based | Capability Based for AI, Endpoint Based for Backend |

---

# Final Takeaway

## REST

> REST exposes endpoints.

## MCP

> MCP exposes capabilities.

Modern AI systems don't just need data access—they need **reasoning, context, and dynamic execution**.

That is where MCP becomes powerful, and by wrapping existing REST endpoints into MCP tools, you can seamlessly bring legacy systems into the agentic era!

---

# Useful Resources

- MCP Documentation: https://modelcontextprotocol.io
- FastMCP Framework: https://gofastmcp.com
- MCP Server Registry: https://github.com/modelcontextprotocol/servers
