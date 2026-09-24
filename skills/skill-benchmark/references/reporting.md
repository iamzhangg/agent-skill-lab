# Reporting

The report should state:

1. Target Skill and revision.
2. Environment and runner version.
3. Passed/total assertions and blocking failures.
4. Per-case failures with the smallest useful diagnostic.
5. Changes from the previous baseline, if any.
6. Scope limitations and untested risks.

Recommend release only when every blocking assertion passes and the configured score threshold is met. Never hide skipped cases inside the pass count.
