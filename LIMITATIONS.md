# Limitations

1. **Academic lab scope.** Small VM/node counts and educational workloads do not represent production scale.
2. **Separate environments.** The modules were not one integrated production platform.
3. **Self-signed TLS.** The Nginx TLS exercise verifies encryption mechanics, not public PKI trust.
4. **Replication terminology.** The report uses historical MySQL “Master–Slave” wording. This portfolio prefers **primary/replica** except when referring to exact report terminology/output.
5. **Redis result.** The ~19× improvement belongs to one lab run and should not be generalized as a benchmark.
6. **Kubernetes size.** A two-node learning cluster is useful for orchestration fundamentals but does not provide production control-plane HA.
7. **HAProxy validation.** Round-robin distribution was verified; failure detection, failover recovery time, session persistence, and load tests were not comprehensively benchmarked.
8. **Monitoring.** Metrics collection and visualization were validated, but production alerting/SLOs/on-call workflows were outside the retained evidence.
9. **Raw artifacts.** Some screenshots are intentionally absent from the public mirror because they contain identifiers or environment-specific information.