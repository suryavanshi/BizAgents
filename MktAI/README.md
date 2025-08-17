# MktAI

This is a monorepo for the MktAI MVP. It contains a FastAPI backend with a LangGraph agent and a Next.js frontend chat interface.

## Structure
- `apps/backend` – FastAPI service exposing `/run_graph`
- `apps/frontend` – Next.js application with a simple chat UI

## Development

Use `pnpm` for managing workspaces and `docker-compose` for running services locally.

```bash
pnpm install
docker-compose up --build
```
