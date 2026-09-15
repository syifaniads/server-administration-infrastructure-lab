# Prometheus, Node Exporter & Grafana

## Monitoring pipeline

```mermaid
flowchart LR
  N[Node Exporter\n:9100] -->|scrape| P[Prometheus\n:9090]
  P --> G[Grafana\n:3000]
  P --> API[cURL / Python API queries]
```

## Verified results
- Node Exporter exposed CPU, memory, disk and network metrics.
- Prometheus scraped Node Exporter successfully.
- Prometheus Targets UI showed Node Exporter as **UP**.
- Grafana connected to Prometheus and rendered the Node Exporter Full dashboard.
- Prometheus API queries were tested with cURL and Python and returned JSON metric data.

## Production extensions
This lab proves telemetry collection/visualization. A production observability platform should add alert rules, Alertmanager/on-call routing, SLOs, retention planning, authentication/TLS, backup, and access control.