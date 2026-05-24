## Summary

This paper proposes GAMA, a neural neighborhood search method for the Capacitated Vehicle Routing Problem (CVRP) that employs a graph-aware multi-modal attention encoder. The encoder uses dual graph convolutional networks to independently encode the problem instance and current solution, then models intra- and inter-modal interactions via stacked self-attention and cross-attention layers with a gated fusion mechanism. The resulting representation guides an RL-based operator selection policy. Experiments on CVRP20/50/100 and the Uchoa benchmark show that GAMA achieves marginally better costs than several neural and classical baselines.

## Strengths

- **Multi-modal encoding with gated fusion is a sensible architectural contribution.** The idea of treating the problem graph and solution graph as distinct modalities, processing them with dual GCNs, and then modeling their interactions through self-attention, cross-attention, and gated fusion is well motivated and technically sound. The design goes beyond the simple concatenation or summation used in prior L2I methods.

- **Ablation confirms the benefit of the proposed components.** Table 2 shows that GAMA outperforms GENIS (no cross-modal attention) and GAMA\_NG (sum fusion instead of gating) across all problem sizes, with Wilcoxon significance tests reported. On CVRP100, GAMA's mean cost (15.6510) is clearly better than GENIS (15.7441) and GAMA\_NG (15.7001). This provides direct evidence that both cross-modal attention and gated fusion contribute to performance.

- **Competitive zero-shot generalization.** On the Uchoa benchmark (100–1000 customers), GAMA achieves the best average optimality gap (4.956%) among neural baselines, edging out ReLD (5.018%) and substantially beating L2I (13.557%) and DACT (25.305%). This demonstrates that the learned state representation transfers across problem scales reasonably well.

## Weaknesses

### Major

- **Marginal improvements are described as "significant," unsupported by statistical evidence in the main comparison.** The abstract and introduction claim GAMA "significantly outperforms" neural baselines. However, the gains in Table 1 are very small: on CVRP20, GAMA's average (6.0810) differs from DACT(T=20k) (6.0811) and HGS (6.0812) by only 0.001–0.002 (<0.02%); on CVRP50 the gap to DACT(T=20k) is ~0.009 (<0.09%); on CVRP100 the gap to LKH3 is ~0.15% and to ReLD(A=8) ~0.05%. Crucially, **Table 1 reports no standard deviations, confidence intervals, or significance tests** for any method, so the reader cannot judge whether these tiny differences are statistically robust. The overclaim weakens the paper's credibility, and the lack of basic uncertainty reporting in the main results table is a significant methodological gap.

- **Runtime vs. solution quality trade-off is not addressed.** GAMA (T=20k) takes 19 minutes on CVRP100, while LKH3 (1.95 min) and HGS (59 sec) achieve nearly identical solution quality (15.6752 and 15.6994 vs. GAMA's 15.6510). The paper does not discuss when GAMA's large computational overhead would be justified, nor does it present any efficiency analysis (e.g., Pareto plots of cost vs. time). Given that the paper positions the method as an improvement over handcrafted heuristics, this omission is a significant gap.

- **Ablation is not fine-grained enough to isolate individual contributions.** The ablation compares GAMA against only two variants: GENIS (no cross-modal attention) and GAMA\_NG (sum fusion instead of gating). This does not isolate the effect of self-attention alone, cross-attention alone, or test alternative fusion strategies (concatenation, bilinear pooling). The paper claims "both the multi-modal attention mechanism and the gated fusion design play a key role," but the current experiments cannot separate which specific component contributes what, or whether the gains are simply due to increased model capacity.

- **GIRE is named as a baseline but never evaluated.** Section 4.2 lists GIRE (Ma et al., 2023) as a learning-to-improve baseline, but Table 1 contains no GIRE results. This is an unexplained omission that weakens the comprehensiveness of the comparison.

### Minor

- **High variance on CVRP100 (ablation).** In Table 2, GAMA's standard deviation on CVRP100 is 0.0215 — roughly 4–5× larger than GAMA\_NG (0.0042) and GENIS (0.0053). The paper does not discuss whether the gating mechanism sometimes leads to instability or whether a few outlier runs drive this variance.

- **Narrow y-axis range in Figure 2.** The box plots for CVRP50 use a y-axis range of 10.35–10.41, which exaggerates small differences. Reporting gap percentages relative to a strong baseline would give readers a better sense of absolute scale.

- **Small generalization margin over ReLD.** In Table 3, GAMA's average gap (4.956%) is only 0.062% better than ReLD (5.018%). No significance test is reported, so it is unclear whether this difference is reliable.

- **Underspecified details in the state representation.** Section 3.2 defines the state $s_t$ as including $\{ \mathcal{G}_{\text{dis}}, \mathcal{G}_{\text{sol}}, \mathcal{X}_t, a, e, \Delta, \eta\}$, but Section 3.3 only describes encoding of the two graphs and node features. How the scalar/indicator features $a$, $e$, $\Delta$, $\eta$ are embedded into the "optimization context vector" is not specified — the paper simply says they are "concatenated." This leaves a non-trivial implementation detail unclear.

- **Ambiguous timing notation.** The Table 1 caption says "run one instance average cpu time," but the experimental setup mentions both CPUs and A100 GPUs. For neural methods that presumably run on GPUs, whether the reported time is CPU or GPU time is ambiguous.

- **Broken reference to "Eq. ??".** The sentence introducing Table 1 contains a missing equation reference ("Eq. ??"), indicating incomplete proofreading.

### Trivial

- The reward assigns the same value to all operators within an improvement phase (inherited from L2I). The paper acknowledges this design choice but does not discuss its limitations. Any effect on policy learning is unclear but worth flagging.

## Nice-to-Haves

- A hyperparameter sensitivity analysis (number of attention layers, heads, GCN dimensions, learning rate) would strengthen the empirical characterization.
- Comparing with heuristic-initialized solutions (rather than random initial solutions, as currently used) could clarify whether GAMA's advantage holds across initialization strategies.
- A discussion of the limitations of coarse phase-level reward assignment would be welcome.
- Reporting results for GIRE and at least one more recent L2I method (e.g., from 2023–2025) would make the baseline set more contemporary.

## Removed Points

These points were flagged but are either incorrect, speculative, or not verifiable from the paper as written:

- **"Missing NeuOpt, N2S baselines"** — The reviewer names specific methods whose existence and relevance cannot be verified without external sources. The broader point about dated baselines is partially valid, but specific namedropping is removed. A toned-down version about the absence of very recent L2I methods is captured in Nice-to-Haves.
- **"GENIS omitted from main results table"** — The paper positions GENIS as an ablation baseline (Section 4.2: "To evaluate the contribution of the self-and-cross attention mechanism, we compare our GAMA encoder with GENIS"), which is a legitimate design choice. Not a weakness.
- **"Table 5 typo (GENIS → GAMA)"** — The text says "parameter settings of the proposed GENIS," which could mean settings used to run the GENIS baseline. Not clearly an error.
- **"Algorithm 1 line 8 conflation"** — The phrasing is somewhat informal but not incorrect; the encoder takes raw state and outputs representation.
- **"No limitations section"** — Many papers do not include a separate limitations section; this is not a standard requirement.
- **"Reproducibility concerns about supplementary appendix"** — The paper states code will be released upon acceptance and provides algorithmic details. Speculating about missing appendix content is not fair.

## Novel Insights

None beyond the paper's own contributions. The multi-modal encoder design is the key novelty, and the reviews do not surface any fundamentally new insight about the method or its behavior that the paper itself missed.

## Suggestions

1. **Add standard deviations (or more informative uncertainty estimates) to Table 1** for all methods, and report significance tests (paired Wilcoxon or similar) between GAMA and the top-3 baselines. This is essential for the reader to assess whether the small numerical advantages are reliable.
2. **Include a cost-vs-time plot** comparing GAMA (at multiple T budgets) against LKH3, HGS, and the best neural baselines. Discuss the scenarios where GAMA's extra computation is justified.
3. **Perform a finer-grained ablation:** e.g., remove self-attention only, remove cross-attention only, replace gating with concatenation. This would isolate which component drives the gains.
4. **Replace "significantly outperforms" with more measured language** in the abstract and conclusion, or provide the significance evidence to back it up.
5. **Report GIRE results** in Table 1 (or explain why GIRE is omitted).
6. **Clarify the embedding of $a, e, \Delta, \eta$** into the optimization context vector, and specify whether timing is CPU or GPU for neural methods.
7. **Fix the broken "Eq. ??" reference** and the narrow y-axis in Figure 2.

## Score and Decision

### Calibration

**Round 1 (Bracketing):**
- Weak-band anchors (score < 3.5): SrnTGdJKYG (avg 3.00), oGsR3MJvwS (avg 3.00), NIhRwzqhUz (avg 3.00). These papers had fundamental methodological flaws. GAMA is clearly stronger.
- Middle-band anchors (3.5–7.5): DKfcxPxunu (5.75, Reject), AMbIvaD4Rr (4.50, Reject), TbTJJNjumY (6.25, Accept), IA3wm5vwUl (3.67, Reject). GAMA sits between the weaker rejected papers and the stronger accepted ones.
- Strong-band anchors (>7.5): Non-VRP papers with very high scores. Not directly comparable.

Initial bracket: **4.0–6.0**

**Round 2 (Narrowing):**
- DPYPpC0cBC (4.25, Reject) — LRP paper with major methodological concerns. GAMA is stronger.
- AMbIvaD4Rr (4.50, Reject) — SHIELD paper with limited novelty and mixed reviews. GAMA is comparable.
- CFLEIeX7iK (5.75, Reject) — Neural solver selection, cleaner experiments but novelty concerns. GAMA is weaker.
- 4pRwkYpa2u (6.00, Accept) — ReLD paper with insightful analysis and clean experiments. GAMA is weaker.

**Final Score Determination:** GAMA has a genuine architectural contribution and reasonable experiments, but is held back by overclaimed results, missing uncertainty metrics in the main table, unaddressed runtime trade-off, limited ablation, and several presentation issues. It is stronger than the 3.5–4.5 papers (which had more fundamental problems) but clearly weaker than the accepted 6.0+ papers (which had stronger evaluation and clearer contributions). The most appropriate comparison is with the Neural Solver Selection paper (5.75, Reject) and the ReLD paper (6.00, Accept) — GAMA is closer to the former in overall quality. Score set at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>