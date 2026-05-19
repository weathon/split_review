- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 3, 8
Now I have verified the paper's content against the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes UniTST, a Transformer for multivariate time series forecasting that flattens all patches from every variate into a single sequence and applies unified self-attention (with a dispatcher mechanism for memory efficiency) to simultaneously capture both inter-variate and intra-variate temporal dependencies. The key ideas are: (1) flattening patches from all variates into a unified sequence to enable direct cross-time cross-variate attention, and (2) a dispatcher module of k learnable tokens that reduces complexity from O(N²p²) to O(kNp) via two cross-attention steps. Experiments on 9 long-term and 4 short-term datasets show strong results against 11 baselines.

## Strengths

- **Unified attention on flattened patch tokens.** UniTST flattens patches from all variates into one sequence and applies single self-attention, enabling simultaneous modeling of cross-time cross-variate dependencies that prior two-stage/parallel attention designs (iTransformer, Crossformer, CARD) cannot capture at the patch level. This design is conceptually clean and directly addresses a real limitation. (Section 4.1, Figure 1)

- **Dispatcher mechanism with practical memory savings.** By using k learnable dispatcher tokens with cross-attention, the model reduces memory from O(N²p²) to O(kNp). The ablation (Table 3) demonstrates that on Traffic (N=862) and ECL (N=321) the naive flattened version runs out of memory on a 40GB GPU while the dispatcher version uses 22.87GB and 13.32GB respectively. This makes the unified-attention approach feasible on large-variate datasets.

- **Strong empirical results across diverse benchmarks.** UniTST achieves best or second-best MSE on 7 of 9 long-term datasets (Table 1) and wins 14 of 16 metrics on PEMS short-term forecasting (Table 2), often by sizable margins (up to ~13% relative improvement). The comparison covers 11 strong baselines including iTransformer, PatchTST, and Crossformer.

- **Real-data motivation for cross-time cross-variate dependencies.** The paper defines a patch-level correlation coefficient (Eq. 1) and visualizes it on real solar data (Figure 3), showing that strong correlations exist between patches from different variates at different time offsets. This provides empirical grounding for the unified attention design over approaches that cannot capture such fine-grained cross-variate cross-time patterns. (Section 3, Figure 3)

## Weaknesses

### Fatal
None.

### Major

- **The core claim — that unified (simultaneous) attention is superior to sequential/parallel two-stage attention — is not directly tested.** The ablation in Table 3 compares the model with vs. without dispatchers, which tests the efficiency mechanism, not the core architectural choice. A controlled comparison is missing: keep the same patching, dispatcher design, and model capacity, but replace unified attention with two separate attention modules (time-wise then variate-wise, or vice versa) as in Crossformer/CARD. Without this experiment, the paper cannot attribute the performance gains to *simultaneity* of attention rather than to other factors (patching, dispatcher regularization, better optimization). The comparison against Crossformer in Table 1 is informative but confounded by many other architectural differences (encoder-decoder vs. encoder-only, different patching strategies, etc.). The authors should either run this controlled ablation or soften the causal claim about simultaneity.

### Minor

- **The claim of "directly" modeling dependencies is overstated.** The dispatcher mechanism compresses all Np tokens into k learnable dispatchers via cross-attention and then expands back. The resulting effective interactions between any two patches are mediated through the dispatchers, producing a low-rank approximation (rank k) of the full Np×Np attention matrix. This is not the same as full all-pair attention. The paper should acknowledge that the method captures cross-variate cross-time dependencies *through a compressed representation*, which is still more direct than prior two-stage mechanisms but not equivalent to unrestricted pairwise attention. The complexity-vs.-expressivity tradeoff should be discussed more explicitly (the number-of-dispatchers ablation in Table 5 partially addresses this, but the "directly" language in the abstract and discussion is too strong).

- **No variance or confidence intervals reported.** All results (Tables 1–4) are point estimates without standard deviations or multiple-seed averages. Several gaps are small (e.g., ETTm2: UniTST MSE 0.280 vs. RLinear 0.286; Traffic MSE: UniTST 0.439 vs. iTransformer 0.428). Without error bars, it is difficult to assess whether these improvements are statistically significant. While single-run reporting is common in this literature, the paper's strongest claims (SOTA, up to 13% improvement) would be substantially strengthened by variance estimates, especially on the closer benchmarks.

- **The Traffic dataset (N=862) is a notable counterexample with no discussion.** On Traffic, iTransformer beats UniTST on MSE (0.428 vs. 0.439) despite UniTST winning on most other datasets. Traffic has the largest number of variates among the benchmarks. The paper does not analyze why this occurs — whether the dispatcher bottleneck is too severe for this setting, whether variate-wise attention (iTransformer) is sufficient for Traffic's structure, or whether some other factor is at play. Since this is the dataset where the method's complexity advantage matters most, the omission is notable.

### Trivial

- Table 5 (number of dispatchers) reports MSE values (e.g., Weather 0.1575) that differ from Table 1 (Weather 0.242). The caption states "prediction length as 96," explaining the discrepancy since Table 1 averages over four prediction lengths. This should be stated more prominently in the caption or table notes.

## Nice-to-Haves

- A comparison or at least a discussion relating the dispatcher mechanism to other low-rank/inducing-point attention methods (Perceiver, Linformer, Nyströmformer) would help contextualize the design choice.
- An analysis of why UniTST performs particularly well with short lookback lengths (Figure 4) — e.g., attention visualizations for short vs. long lookback — could strengthen the understanding of the method's behavior.
- Explicitly stating in the camera-ready version that code will be released would improve reproducibility confidence.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Baseline fairness and reproducibility — it is not clear whether results were obtained from original papers or re-run"**: Removed. The paper follows the standard experimental protocol of the field (iTransformer setting, lookback 96, prediction lengths 96/192/336/720). Citing results from original papers is standard practice in MTSF. The reviewer's concern is speculative and not anchored to any specific discrepancy in the paper.

- **"Abstract claim that 'previous models cannot capture these dependencies' is too strong — Crossformer and CARD can capture some cross-time cross-variate information"**: Removed. The paper consistently qualifies this with "directly and explicitly" and "simultaneously" (abstract: "cannot directly and explicitly learn"; Section 3: "indirect and unable to explicitly learn"). The paper's claim is about *direct/simultaneous* capture, not about *any* capture. The critic misreads the qualifier.

- **"Section 3 motivation could provide a statistical test"**: Removed. The correlation visualization is illustrative and sufficient to motivate the design. Requesting a formal statistical test is scope creep for a motivation figure.

- **"Section 4.1 dispatcher description is under-specified about layer norms"**: Removed. This is a trivial implementation detail standard in Transformer blocks; the paper states "passed to a BatchNorm Layer and a feedforward layer with residual connections" (line 145). No meaningful reproducibility issue.

- **"Missing complexity comparison table"**: Removed. The paper provides the key complexity analysis (O(N²p²) vs. O(kNp)) in the main text. A separate table is not necessary.

- **"Attention visualization claim not rigorously supported"**: Removed. The paper presents the histogram as an observation ("may suggest"), not as a rigorous proof. The claim is appropriately hedged.

- All "Strengthening the Paper on Its Own Terms" and "Missing Parts" items that overlap with the above: Removed as duplicative or scope-creep.

## Novel Insights

The most interesting observation from the cross-review is the conjunction of two results: (1) the dispatcher ablation shows that on ETTm1 (7 variates), the compressed version actually slightly *improves* MSE over full attention (0.379 vs. 0.385), suggesting the bottleneck may act as a beneficial regularizer rather than just a cost-saving approximation; (2) on Traffic (862 variates), where the compression is most needed, the method underperforms iTransformer. Together these suggest the dispatcher's effect is dataset-dependent and interacts with the number of variates in non-trivial ways — a pattern worth deeper investigation that neither review fully explores.

## Suggestions

1. **Run a controlled ablation comparing unified (flattened) attention vs. two-stage sequential attention (time-wise then variate-wise) with all else equal** — same patching, same dispatcher design, same model capacity. This would directly test whether simultaneity is the operative mechanism behind the gains, which is the paper's central claim.

2. **Report results averaged over at least 3 seeds with standard deviations** for the main tables (or at minimum for the closer benchmarks like ETTm2, Traffic, ETTh1). This would significantly strengthen the evidential value of the empirical comparison.

3. **Acknowledge the low-rank nature of the dispatcher mechanism** in Section 4.1. Replace or supplement "directly" with "through a compressed representation that still enables simultaneous cross-time cross-variate interactions" to accurately reflect the architecture's properties.

4. **Analyze the Traffic underperformance.** Given that Traffic has the largest N (862), this is the setting where the dispatcher's compression is most aggressive. Discussing whether the bottleneck is responsible or whether the data's structure favors variate-only attention (iTransformer) would add valuable insight.
