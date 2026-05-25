## Summary

This paper identifies and formalizes Dual-level Noisy Correspondence (DNC) in multi-modal entity alignment—a practical problem where both intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) correspondences are corrupted. The authors propose RULE, a framework that (1) estimates correspondence reliability via a two-fold principle combining evidential uncertainty and consensus, (2) applies tailored robust losses and adaptive fusion to mitigate intra-entity and inter-graph noise, and (3) leverages an MLLM with chain-of-thought prompting for test-time correspondence reasoning. Experiments on five benchmarks with seven SOTA baselines under inherent and synthetic noise show consistent and substantial gains.

## Strengths

1. **Novel problem formulation (DNC).** The paper reveals and formalizes a genuinely practical problem—that both intra-entity and inter-graph correspondences in MMEA are simultaneously noisy—which prior work implicitly assumes away. Evidence: Section 1 (Figure 1b shows performance degradation from noise) and the formal definition in Section 2.1. The claim that real-world benchmarks contain substantial DNC (e.g., >50% in ICEWS) is supported by statistics cited in Appendix B.

2. **Two-fold reliability estimation with theoretical motivation.** The method combines evidential uncertainty (Eq. 3) and consensus (Eq. 5) to estimate correspondence reliability. Theorem 1 proves that uncertainty alone is insufficient, motivating the dual design. This principle is validated visually: Figure 3b shows clean vs. noisy pair separation by reliability, and Figure 4 shows the three subsets S_U / S_I / S_C are clearly separated in the uncertainty-consensus plane.

3. **Strong, consistent empirical gains.** RULE achieves SOTA on five datasets under both inherent and injected noise. Under inherent DNC in the Non-name setting (Table 1), RULE surpasses PMF by 5.2 H@1 on average (73.8 vs. 68.6). At 50% injected DNC, RULE achieves 64.3 avg H@1 while the best baseline (MEAformer) reaches 54.0. These gains are consistent across datasets (ICEWS-WIKI, ICEWS-YAGO, DBP15K ZH/JA/FR) and across noise levels (Figure 3a), demonstrating genuine robustness.

4. **Ablation confirms necessity of each component.** Table 3 shows that removing DRL drops H@1 by 26.6 points (31.6 vs. 58.2) on the Non-name setting, removing DRF drops 7.8 points, and removing TTR drops 1.7 points. The "Only Unc." and "Only Cons." variants each underperform the full method, confirming the two-fold principle is necessary.

## Weaknesses

### Major

- **No variance or statistical significance reported in any table.** Tables 1–3 report point estimates without standard deviations, confidence intervals, or significance tests. For an empirical paper making comparative claims across 5 datasets and 3 noise levels, this makes it impossible to assess whether the reported gains are statistically reliable or could be driven by a single run. While single-run reporting is common in this field, the gap between RULE and the best baseline is narrow in some cases (e.g., All-attributes, Table 2, inherent DNC: 98.8 vs. 97.0 for MEAformer), where error bars could affect the conclusion.

### Minor

- **Lack of analysis on the consensus bootstrapping mechanism.** The greedy strategy (Eq. 6–7) for estimating correspondence via marginal contribution uses a fixed initial subset size |π₀| = ⌊M/2 + 1⌋ and a hard threshold (> 0). The paper provides no sensitivity analysis on these choices or on how the bootstrapping behaves when initial estimates are wrong. The ablation shows "Only Cons." (48.3 H@1) substantially underperforms "Only Unc." (53.5), suggesting the consensus estimation is the weaker of the two principles. The paper would benefit from analyzing when and why the two principles interact to produce the full method's 58.2 H@1 result.

- **"Deep reasoning" claim for TTR is inflated relative to the evidence.** The paper states that the TTR module "performs deep reasoning to uncover the underlying attribute-attribute connections" (Section 2.5) and presents the "Cristiano Ronaldo vs. Mexico" vignette as a motivating example. However, the only evidence provided is aggregate H@1 improvement in Table 3 (56.5 → 58.2). This does not distinguish genuine chain-of-thought reasoning from a powerful but shallow re-ranking by a 72B MLLM. Qualitative examples showing the CoT trace, intermediate reasoning steps, and cases where only CoT succeeds would substantially strengthen this claim.

- **No computational cost analysis for the 72B MLLM.** The TTR module uses Qwen2.5-VL-72B-Instruct at inference time. The paper does not report inference time, GPU memory, or any cost comparison to the baselines. Given the substantial gap in model scale (72B vs. the much smaller encoder-based baselines), this is a practical concern for deployment and a necessary trade-off to acknowledge.

- **Parameter sensitivity for the threshold β not examined in the main text.** The hyperparameter β directly controls the partition into S_C, S_I, S_U via the self-adaptive thresholds (Eq. 8), yet the paper fixes β=0.3 across all experiments without analyzing its effect. A sensitivity analysis is standard practice for a hyperparameter that defines the central data partition of the method.

### Trivial

- No explicit limitations section. The paper would benefit from acknowledging the dependency on a large MLLM, the synthetic noise injection protocol, and the scope of the benchmarks.

## Nice-to-Haves

- A qualitative gallery of TTR reasoning traces (as suggested by the harsh critic), showing the specific prompt, intermediate CoT steps, and the final change in similarity ranking for cases where direct similarity fails.
- An analysis tracking the distribution of S_C, S_I, S_U over training epochs to verify that the bootstrapping stabilizes rather than diverges.
- Error bars (3–5 seeds) at least for the main results (Tables 1–2) to support the comparative claims.

## Removed Points

These points were considered but removed after cross-checking against the paper:

1. "Consensus estimation is a self-training loop" — The consensus during training uses the *annotated* correspondence y_i directly (Eq. 5), not the model's own predictions. The greedy strategy (Eq. 7) is proposed specifically for inference when y_i is unavailable. The critic's framing of a "self-training loop" mischaracterizes the architecture. The sensitivity concern about the greedy strategy's parameters is kept (see Minor weaknesses), but the "self-training" characterization is removed.

2. "Missing standard deviations" — The Strength Finder's praise about "Strong empirical results" is kept despite this weakness; the two are independent observations. This is a genuine gap and is listed as a Major weakness.

## Novel Insights

The key structural insight from the reviews is that the paper's claimed synergy between uncertainty and consensus (two-fold principle) would be substantially more convincing if the interaction were analyzed dynamically. The ablation shows that the two components individually underperform their combination, but the paper does not explain *how* the interaction resolves the bootstrapping fragility that the "Only Cons." variant reveals. This is a concrete open question for follow-up work: under what distributional conditions does the greedy consensus estimate fail, and how does the uncertainty filter correct it?

## Suggestions

- Add standard deviations (3–5 seeds) to the main result tables.
- Include a brief analysis (one paragraph + one figure) showing how the S_C / S_I / S_U subset sizes evolve during training and whether the composition stabilizes.
- Present 2–3 qualitative TTR vignettes with the full CoT trace to support the "reasoning" claim, or alternatively reframe the claim as "MLLM-assisted re-ranking."
- Add a computational cost analysis for the TTR module (inference time, GPU memory relative to baselines) and discuss the practical trade-off.
- Add a sensitivity experiment for the threshold β (Eq. 8) over a range (e.g., 0.1–0.5) showing H@1 on ICEWS-WIKI.

## Score and Decision

**Calibration:** I retrieved anchors from three topic bands (low: ≤3.5, mid: 3.5–7.5, high: ≥7.5) plus weakness-anchored queries. The mid-band topic anchors most relevant are: z3dfuRcGAK (6.67, accepted EA paper with comparable empirical scope but stronger theory), ue1Tt3h1VC (6.60, accepted MMKG paper with similar experiment quality), and NNUiUwQWx6 (5.75, rejected EA paper with weaker experiments and missing complexity analysis). The weakness-anchored papers most relevant are 6w2HEMxzq7 (5.50, graph matching with noisy correspondence—limited experiments) and PD8JVDg8mB (4.25, annotation bootstrapping—limited analysis of bootstrapping dynamics). The paper under review is substantially stronger than the low-band and weakness-anchored papers, comparable to the mid-band accepted papers, but weaker than the high-band benchmarks.

**Round-1 bracket:** [5.5, 7.0]. **Narrowing:** The paper shares the missing-dynamics-analysis weakness with PD8JVDg8mB (4.25) but addresses it to a greater degree through empirical validation (Fig. 4, Table 3). The paper shares the missing-complexity-analysis weakness with NNUiUwQWx6 (5.75) but has stronger experiments and a clearer problem contribution. The paper is comparable in experiment quality to z3dfuRcGAK (6.67) and ue1Tt3h1VC (6.60) but has addressable gaps (no error bars, overclaimed TTR framing, limited bootstrapping analysis) that the accepted anchors do not share to the same degree.

**What the low-band and weakness-anchored papers failed at:** Low-band anchor a4O528mek9 (3.00) failed at writing quality, method clarity, and experiment scope—the paper under review does not share these failures. Weakness-anchored PD8JVDg8mB (4.25) failed to analyze the dynamics of its bootstrapping mechanism—the paper under review partially shares this gap (no analysis of consensus estimation convergence or sensitivity), but provides extensive empirical validation (ablation, visualizations) that the weaker paper lacked.

**Final score: 6.5. Decision: Accept.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>