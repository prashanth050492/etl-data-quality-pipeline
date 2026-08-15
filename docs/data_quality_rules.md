# Data Quality Rules

| Rule | Check | Expected result |
|---|---|---|
| DQ-001 | Order ID uniqueness | No duplicate order IDs |
| DQ-002 | Order date completeness | No NULL order dates |
| DQ-003 | Amount validity | Amount must be greater than 0 |
| DQ-004 | Referential integrity | Every order customer_id must exist |
| DQ-005 | Status standardization | Status must be Completed, Pending, or Cancelled |
| DQ-006 | Row-count reconciliation | Loaded counts must match expected source counts |

## Testing approach

For each rule, capture:
- Test condition
- Records affected
- Pass/Fail status
- Root cause
- Corrective action

The included source data intentionally creates failures so the checks can be demonstrated.
