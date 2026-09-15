# Linux Users, Groups & Permissions

The local identity lab covered:

- `adduser` vs `useradd`;
- home-directory creation;
- sudo-group membership;
- group creation/membership;
- Unix ownership and permission modes;
- validating access boundaries.

## Verified scenarios

- A normal account was promoted to administrative capability through the sudo group and verified with `sudo whoami`.
- Separate developer/designer scenarios exercised `chown`, group ownership, and permission bits.
- Access to `/etc/shadow` from a normal account was correctly denied.

## Security lesson

The lab reinforces least privilege: administrative rights and file permissions should be granted intentionally instead of using broad world-writable access.