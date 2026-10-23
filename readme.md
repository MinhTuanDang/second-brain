# Second Brain

## Technology

- **API:** Python 3.12, FastAPI, Pydantic, SQLAlchemy, Alembic
- **Storage:** PostgreSQL with pgvector, Redis
- **AI:** OpenAI-compatible providers, embeddings, tiktoken
- **Observability:** OpenTelemetry, Prometheus
- **Python SDK:** `src/client/secondbrain`
- **TypeScript SDK:** `src/client/secondbrain-ts` with TypeScript, Zod and Jest
- **Go SDK:** `src/client/secondbrain-go` with Go 1.22+
- **MCP server:** FastMCP
- **Infrastructure:** Docker Compose
- **Documentation:** MDX and OpenAPI

## Project structure

```text
src/client/secondbrain       Python SDK
src/client/secondbrain-ts    TypeScript SDK
src/client/secondbrain-go    Go SDK
src/mcp                   MCP server
src/server                API server and Docker Compose
assets                    Examples and tutorials
docs                      Documentation and benchmarks
```

## Run the server

```bash
cd src/server
cp api/config.yaml.example api/config.yaml
docker compose up --build
```

The API is exposed on the port configured by `API_EXPORT_PORT`.

## Python SDK

```bash
pip install -r requirements.txt
```

## TypeScript SDK

```bash
cd src/client/secondbrain-ts
npm install
npm run build
npm test
```

## Go SDK

```bash
cd src/client/secondbrain-go
go test ./...
```

## Checks

```bash
python -m pytest src/client/tests -q
```

The SDK integration tests require a running API server.
