# Provenance record

Create `provenance.json` with:

```json
{
  "project": "new-skill-name",
  "upstreams": [
    {
      "url": "https://github.com/owner/repository",
      "revision": "commit-or-tag",
      "license": "MIT",
      "usage": "idea | adapted | verbatim",
      "components": ["workflow concept"],
      "changes": "Original implementation with validation and tests"
    }
  ],
  "original_contributions": ["observable new capability"]
}
```

Use `verbatim` only when the license permits it and the repository preserves required notices. Descriptions must be specific enough that a reviewer can locate the relevant upstream material.
