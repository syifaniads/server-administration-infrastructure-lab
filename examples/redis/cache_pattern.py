"""Conceptual cache-aside pattern.

This is a sanitized portfolio example, not the original coursework source.
"""

def get_records(cache, database, key="employees"):
    cached = cache.get(key)
    if cached is not None:
        return cached

    rows = database.query("SELECT * FROM employees")
    cache.set(key, rows, ttl_seconds=60)
    return rows
