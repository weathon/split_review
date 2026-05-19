Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

ShareLoRA proposes to reduce the number of trainable parameters in LoRA fine-tuning by sharing adapter weights across layers whose pre-trained representations are highly similar. The method computes cosine similarity between layer representations (using a small calibration set), applies a greedy algorithm to group layers into shareable sets, and reinvests the saved parameter budget into a slightly higher per-layer rank. Experiments are conducted on LLaMA-family models (commonsense reasoning) and LLaVA-1.5-7B (multimodal instruction following).

## Strengths

- **Naive sharing experiment (Table 1) provides compelling motivation**: The paper demonstrates that even a hand-crafted odd-even weight sharing of LoRA modules causes only minor performance degradation (e.g., BoolQ 69.4→69.2). This gives concrete, quantitative evidence that layer-level redundancy exists in LoRA adapters, which is the foundational observation for the work.

- **Clean matched-rank comparison on LLaVA (Table 3)**: The LLaVA experiment uses rank 64 for *both* LoRA and ShareLoRA, providing an unambiguous comparison. ShareLoRA achieves higher conversational scores (94.3 vs. 87.9) and overall performance while using ≈13% fewer trainable parameters. This is the strongest evidence for the method's effectiveness because it isolates weight sharing as the only variable.

- **Random-sharing ablation (ShareLoRA*) is informative**: The paper compares similarity-based ShareLoRA against a random adjacent-layer sharing baseline (ShareLoRA*). Across all three LLaMA models, similarity-guided sharing consistently outperforms random sharing (e.g., LLaMA-7B: 69.9 vs. 68.5 average accuracy), demonstrating that the similarity criterion provides meaningful signal beyond naive parameter reduction.

- **Concrete, reproducible algorithm**: The greedy algorithm for constructing shared-layer sets (Algorithm 1) is clearly specified, along with the rank-update formula, making the method implementable from the description.

## Weaknesses

### Fatal
None.

### Major

- **Confounded comparison in the primary LLaMA experiments (Table 2)**: The paper states explicitly that "we expand the original LoRA rank from 8 to 9" for ShareLoRA while comparing against LoRA at rank 8. This means ShareLoRA differs from the baseline in *two* ways: weight sharing *and* rank. A 12.5% increase in rank provides additional per-layer capacity, so any performance improvement or maintained performance could stem from the higher rank rather than from intelligent sharing. The random-sharing baseline (ShareLoRA*) also uses rank 9, but there is no rank-9 LoRA without sharing to compare against. Without a matched-rank comparison (both rank 8 or both rank 9), the paper's headline claim—"up to 23% reduction in trainable parameters" with "1.5% improvement"—cannot be cleanly attributed to the sharing mechanism. **Why this is major**: it is the paper's primary experimental evidence and the confound prevents interpreting the core causal claim.

### Minor

- **No variance or significance reporting for LLaMA experiments (Table 2)**: Only point estimates are reported for the eight commonsense reasoning tasks. The reported improvements are small (1.5% on LLaMA-7B), and without standard deviations or significance tests, it is impossible to assess whether the differences are statistically reliable. (The LLaVA experiments do report mean±std across three runs, which is better.)

- **The connection between representation similarity and adapter compatibility is asserted but not analyzed**: The paper shows that layer representations are similar and assumes this implies their LoRA adapters can be shared without loss. There is no analysis of whether the *trained* adapter weights (the B and A matrices) actually converge to similar values across shared vs. unshared layers, nor any analysis of whether layers with similar representations actually receive similar gradient updates. The naive-sharing result (Table 1) provides empirical evidence that sharing works, but the mechanism by which representation similarity translates to adapter compatibility remains a heuristic.

- **Different similarity thresholds used without justification**: The threshold is 0.85 for LLaMA-7B/LLaMA2-7B, 0.80 for LLaMA3-8B, and 0.9 for LLaVA. No rationale is given for these choices or for why they differ across models.

- **Rank-increase formula is presented without derivation or explanation**: The formula `floor(L / (L - sum|S_i| + |S|) * r)` is stated but not derived. It appears intended to keep total trainable parameters approximately constant after sharing, but this is not stated explicitly, making the design choice appear ad hoc.

- **No sensitivity analysis on the similarity threshold**: The paper uses one threshold per model without exploring how parameter savings vs. performance vary across a range of thresholds.

### Trivial
- "marinating a reasonably large batch size" — minor typo ("maintaining" intended).

## Nice-to-Haves
- Per-task accuracy breakdowns with standard deviations for the LLaMA commonsense reasoning tasks (8 tasks × multiple seeds) would significantly strengthen the empirical evidence.
- An analysis of the trained adapter weights (e.g., cosine similarity between B and A matrices of shared vs. unshared layers) would help ground the heuristic in the actual fine-tuning dynamics.
- Reporting wall-clock time and memory cost of the pre-computation step (256-sample inference + similarity calculation) relative to total fine-tuning time would help practitioners assess the overhead.
- Ablating which representation is used for similarity (final token vs. mean pooling vs. first token) would strengthen methodological grounding.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing ablation section 4.3"**: The parser stripped this section's content from the extracted text. Per policy, this section exists in the original submission and should not be treated as missing.
- **"No significance test" elevated to fatal**: This is a reporting gap but not fatal to the paper's claims; it is included as a Minor weakness above.
- **"Inconsistent claimed savings (13% vs. 23%)"**: Different models with different sharing patterns naturally yield different savings. The abstract says "up to 23%" and the conclusion says "80% of the trainable parameter budget" (a 20% reduction) — these are consistent across different configurations.
- **"The rank for Table 1 naive sharing is not specified"**: A valid presentation nitpick, but the naive-sharing experiment is a motivation, not a core result. This is moved to trivial-class presentation issues.
- **"Sensitivity to calibration dataset size"**: Request for additional experiments beyond the paper's stated scope. Nice-to-have but not a weakness.
- **"Pseudocode clarity" / "variable definitions ambiguous"**: Some formatting issues are due to PDF parsing artifacts; the algorithm is sufficiently clear for reproducibility.
- **"Missing comparison with alternative sharing strategies (CKA, mutual information)"**: The paper compares against a random-sharing baseline which is appropriate for the method's first demonstration. Requesting exhaustive alternative strategies is scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations converge on a central methodological point: the paper's primary evidence (LLaMA experiments) is confounded by a rank mismatch, while its cleaner evidence (LLaVA, matched rank) supports the method but covers only one model and one benchmark. The naive sharing result (Table 1) is perhaps the most under-exploited finding — it suggests that even trivial layer-sharing of LoRA adapters causes minimal degradation, which is a potentially broader observation about the low information content of per-layer LoRA updates in LLMs.

## Suggestions

1. **Add a matched-rank comparison for the LLaMA experiments**: Run ShareLoRA at rank 8 (same as the LoRA baseline) to isolate the effect of weight sharing from the effect of rank increase. If performance holds at rank 8, the claim is clean. (Optionally, also run a rank-9 LoRA without sharing to show that the method's gains are not simply due to higher rank.) This single addition would resolve the paper's most serious weakness.

2. **Report per-task accuracies with standard deviations** for the LLaMA experiments across at least 3 seeds.

3. **Add a threshold sensitivity plot** showing parameter savings vs. average accuracy across a range of similarity thresholds (e.g., 0.75 to 0.95) for at least one model.

4. **Clarify the rank-increase formula**: state explicitly that it aims to keep total trainable parameters approximately constant and show a worked example.

## Score and Decision

The paper addresses a worthwhile question and presents a clean, simple method. The LLaVA experiment provides credible evidence for the approach under matched-rank conditions. However, the primary LLaMA experiments — which carry the paper's strongest quantitative claims — are confounded by a rank mismatch between ShareLoRA (rank 9) and LoRA (rank 8), making the headline results uninterpretable as evidence for the benefit of sharing. This is a fixable methodological gap, but in its current form it undermines the paper's central empirical case.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>