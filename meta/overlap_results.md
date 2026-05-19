# Weakness Overlap Results

Each row reports the rate at which weakness items in review-of-paper-A reappear as similar items in review-of-paper-B, with both reviews written by the same agent (or same-style human reviewer). Lower = more paper-specific, less templated.

| method | n_pairs | mean_overlap | median_overlap | mean_items |
|---|---:|---:|---:|---:|
| ours_wo_search | 801 | 0.415 | 0.333 | 5.70 |
| human | 801 | 0.442 | 0.333 | 3.63 |
| v1_DeepReviewer_14B_TXT | 800 | 0.509 | 0.500 | 3.24 |
| v2_API_DeepSeek_PDF | 801 | 0.513 | 0.500 | 7.58 |
| v1_DeepReviewer_7B_TXT | 801 | 0.559 | 0.500 | 3.55 |
| v2_Local_Qwen_PDF | 801 | 0.566 | 0.600 | 4.64 |
