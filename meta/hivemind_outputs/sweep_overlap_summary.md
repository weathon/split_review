# Sweep Hivemind Overlap Summary

Source: `meta/hivemind_outputs/sweep_overlap_results.jsonl`
Completed records: 450

Lower overlap means the weaknesses are less reused across different papers by the same sweep.

| method | n_records | n_unique_pairs | mean_overlap | median_overlap | item_weighted_overlap | mean_items | matched/items |
|---|---:|---:|---:|---:|---:|---:|---:|
| `sweep_v1` | 90 | 90 | 0.396 | 0.333 | 0.386 | 6.01 | 209/541 |
| `sweep_v3` | 90 | 90 | 0.431 | 0.400 | 0.414 | 5.12 | 191/461 |
| `sweep_v4` | 90 | 90 | 0.458 | 0.400 | 0.454 | 5.66 | 231/509 |
| `sweep_v6` | 90 | 90 | 0.465 | 0.429 | 0.437 | 6.00 | 236/540 |
| `sweep_v5` | 90 | 90 | 0.480 | 0.400 | 0.431 | 5.29 | 205/476 |

Best by mean overlap: `sweep_v1` (0.396).
Best by item-weighted overlap: `sweep_v1` (0.386).