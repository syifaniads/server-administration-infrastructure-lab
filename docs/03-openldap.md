# OpenLDAP Centralized Identity

## Components
- OpenLDAP (`slapd`, `ldap-utils`)
- LDAP Account Manager (LAM)
- LDAP client using NSS/PAM integration

## Directory structure
The lab created organizational units for functional groups and populated Unix users/groups beneath the directory base DN.

## Client path

```mermaid
flowchart LR
  U[Linux login] --> PAM[PAM]
  PAM --> NSS[NSS / LDAP integration]
  NSS --> LDAP[OpenLDAP server]
  LDAP --> DIR[(Directory tree)]
```

## Troubleshooting evidence

A client initially could not log in using an LDAP user. The report attributes the problem to the client-side identity/authentication integration and resolves it by correcting the LDAP-backed name-service configuration, enabling home-directory creation, and restarting the relevant service.

## Production notes

For a real environment, prefer TLS-protected LDAP, restrict directory bind privileges, avoid default passwords, centralize secrets, and document account lifecycle/offboarding.