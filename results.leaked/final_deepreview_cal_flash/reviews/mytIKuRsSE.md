## Summary

This paper reveals and formalizes the Dual-level Noisy Correspondence (DNC) problem in multi-modal entity alignment, where both intra-entity (entity-attribute) and inter-graph (entity-entity and attribute-attribute) correspondences contain noise. The authors propose RULE, a multi-component framework that estimates correspondence reliability via a two-fold principle (uncertainty + consensus), uses these estimates for robust attribute fusion and inter-graph discrepancy elimination during training, and employs a chain-of-thought MLLM-based reasoning module at test time to uncover hidden attribute connections. Experiments across five benchmarks with seven baselines under inherent and injected noise (20%–50%) show consistent and often large performance margins (e.g., 58.2% H@1 vs. 43.9% best baseline on ICEWS-WIKI Non-name with 50% DNC).

## Strengths

1. **Novel problem formulation with strong empirical justification.** The paper is the first to formalize DNC in MMEA — a practical problem where both entity-attribute noise and cross-graph alignment noise coexist. The real-world statistics (Appendix B, over 50% noise in ICEWS benchmarks) and the controlled experiments in Fig. 1(b) convincingly demonstrate that existing methods degrade under both noise types, motivating the work.

2. **Consistent and substantial SOTA results across all settings.** Tables 1 and 2 show RULE outperforms seven existing methods on all five datasets under inherent DNC, 20% DNC, and 50% DNC. The margins are often large — on ICEWS-WIKI Non-name with 50% DNC, RULE achieves 58.2% H@1 versus the best baseline at 43.9% (MEAformer). This pattern holds across both Non-name and All-attributes protocols, providing strong evidence that the design is effective.

3. **Every proposed component contributes meaningfully in ablation.** Table 3 shows that removing any module (DRL, DRF, TTR, or reducing to Only Unc. or Only Cons.) causes clear performance drops. On Non-name 50% DNC, w/o DRL collapses H@1 from 58.2% to 31.6%, confirming that all three training-phase innovations are necessary for the observed robustness.

4. **Principled two-fold reliability estimation with theoretical grounding.** Theorem 1 formally proves that uncertainty alone is insufficient to guarantee correct correspondence, motivating the addition of consensus. Fig. 3(b) and Fig. 4 provide visual confirmation that the resulting reliability scores cleanly separate clean from noisy pairs, and that the three subsets ($\mathcal{S}_U$, $\mathcal{S}_I$, $\mathcal{S}_C$) are well-separated in uncertainty-consensus space.

5. **Practical code release.** Code is provided at GitHub, aiding reproducibility and future work.

## Weaknesses

### Major

1. **Greedy marginal-contribution strategy (Sec. 2.2.2) is introduced but never integrated into the pipeline.** This strategy is presented as a way to estimate the correct correspondence $y_i$ when the annotated label is unavailable (i.e., at inference). However: (a) during training the annotated $y_i$ is used directly; (b) during pair division ($\mathcal{S}^{TP}$ definition) the annotated $y_i$ is used; (c) the test-time TTR module (Sec. 2.5) uses a fundamentally different MLLM-based approach. The paper never specifies whether or how the greedy strategy produces the test-time reliability weights $\hat{w}_i^m$ in Eq. 15, or whether it computes the consensus $c_i$ at inference when $y_i$ is unavailable. This leaves a notable coherence gap in the exposition. The paper should either clarify the connection (e.g., tie the greedy estimate to $\hat{w}_i^m$) or remove the description to avoid confusion.

2. **Test-time reliability weights $\hat{w}_i^m$ (Eq. 15) are left unspecified.** The TTR module computes refined similarity scores as $\hat{s}_i = \sum_{m \in M} \hat{w}_i^m \cdot \hat{s}_i^m$, but the paper only states that $\hat{w}_i^m$ "denotes the corresponding reliability weight" without explaining how it is obtained — whether from the uncertainty-consensus framework (using the greedy estimate of $y_i$), from the MLLM's output, or elsewhere. This undermines reproducibility of the test-time module and should be clarified.

### Minor

3. **No variance or standard deviation reported for any result.** All tables report single numbers without multiple-run statistics. Entity alignment evaluations can be sensitive to random seeds, data splits, and the noise injection procedure. Without variance estimates, the reader cannot assess whether the reported margins are statistically reliable. Adding averages and standard deviations over at least 3 runs would strengthen the empirical claims.

4. **Ablation study conducted on only one dataset (ICEWS-WIKI).** Table 3 is limited to a single benchmark. Showing similar ablation trends on at least one additional dataset (e.g., ICEWS-YAGO or DBP15K) would increase confidence that the component contributions generalize.

5. **Pair division thresholding uses the model's own predictions for $\mathcal{S}^{TP}$.** The thresholds $\beta_u, \beta_c$ are computed from $\mathcal{S}^{TP} = \{i \mid \arg\max(s_i) = \arg\max(y_i)\}$, which depends on the model's current (potentially noisy early-training) predictions. The paper does not analyze whether this self-adaptive thresholding is stable across training iterations or how sensitive performance is to the hyperparameter $\beta$. A brief analysis would strengthen the method's justification.

### Trivial

6. A few minor presentation issues: the ICEWS-WIKI dataset citation is not provided in the main text; Fig. 1(b) bar charts lack explicit numerical labels, making precise comparison difficult from the figure alone; some notations (e.g., $w_i$ vs $w_i^m$, $s_i$ vs $s_i^m$) could be more systematically disambiguated.

## Nice-to-Haves

- Discuss the computational overhead of the 72B MLLM (Qwen2.5-VL) used for TTR, and note that the training-only version (w/o TTR) already achieves SOTA. This would contextualize the practical cost of the test-time module.
- Include experiments under different backbone architectures beyond CLIP to demonstrate backbone-agnostic robustness.
- Extend the ablation to include the effect of varying the hyperparameter $\beta$ on the pair division quality and downstream performance.

## Removed Points

These points are flagged to be removed or downgraded from the original reviewer inputs; treat them with caution:

- **Criticism about Fig. 1(b) being described only in vague terms.** The figure caption provides a thorough description of the bar charts and their takeaways. The claim is overly strict — the figure visually conveys the data, and the caption explains the key observations adequately.
- **Criticism about baselines not being re-tuned for noisy settings.** The paper states that the same backbone (CLIP) is used for all methods for fair comparison, which is standard practice. Re-tuning each baseline's hyperparameters for every noise level would be unusual and could introduce unfair advantages.
- **Criticism about the paper not addressing whether the model overfits to low-consensus pairs.** This is a plausible concern but is a speculative claim with no evidence in the review of actual overfitting behavior. The ablation results (Table 3) show that the DRL module provides large gains, indirectly addressing this.
- **Some generic claims from the Strength Finder** (e.g., "this paper addressed an important problem") are removed because they lack specific, concrete anchors in the paper's evidence.
- **The concern about "missing related works"** is removed per protocol — I cannot verify missing citations externally.
- **Several minor formatting/style nitpicks** from the section-by-section notes are removed as they are parser artifacts or trivial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a concrete exposition gap (the orphaned greedy strategy and unspecified $\hat{w}_i^m$) that the authors should address, but do not contribute a fundamentally new perspective on the method or results.

## Suggestions

- Explicitly state how $\hat{w}_i^m$ in Eq. 15 is derived — whether from the greedy marginal-contribution estimate, from the uncertainty-consensus framework using that estimate, or from the MLLM directly.
- Either connect the greedy marginal-contribution strategy (Sec. 2.2.2) to a concrete use in the pipeline (e.g., computing $\hat{w}_i^m$ or estimating $c_i$ at inference), or remove it in a revision to avoid misleading readers.
- Add standard deviations to all main tables (Tables 1–3) from at least 3 independent runs.
- Provide ablation results on a second benchmark to verify that the component contributions generalize.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- Low band (< 3.5): `a4O528mek9` (3.00), `YrxhSkfHh0` (3.33), `rwdeKOdAwY` (3.00), `AAZ3vwyQ4X` (2.50), `ky2JYPKkml` (3.00), `pLvh9DTyoE` (2.50) — all rejected, substantially weaker than RULE.
- Middle band (3.5–7.5): `NNUiUwQWx6` (NeuSymEA, 5.75, Reject), `z3dfuRcGAK` (GEEA, 6.67, Accept), `er7VhmqZEA` (4.00, Reject), `kE1TVeolWv` (4.25, Reject), `MCUvAc1GTg` (5.50, Reject), `a69zct3BkY` (4.67, Reject). RULE is clearly stronger than all Reject papers in this band and comparable to the Accept paper (GEEA 6.67).
- Strong band (7.5+): `9Cu8MRmhq2` (Norton, 8.00, Accept), `TPZRq4FALB` (READ, 8.00, Accept) — very polished papers with unanimous 8s; RULE is not at this tier due to exposition gaps.

**Round 1 bracket:** 6.0 – 7.5

**Round 2 — Narrowing:**
- `z3dfuRcGAK` (GEEA, 6.67, Accept) — similar entity alignment topic; RULE has stronger empirical scope (5 datasets vs 3, more baselines) and more novel problem formulation, but weaker exposition clarity. RULE is slightly stronger overall.
- `ue1Tt3h1VC` (Multi-heads mixture, 6.60, Accept) — MMKG representation paper; RULE has more extensive evaluation and clearer task definition. RULE is slightly stronger.
- `ftGnpZrW7P` (GRAM, 7.00, Accept) — multimodal alignment paper with novel Gramian measure; similar quality level, GRAM slightly ahead on mathematical elegance, RULE ahead on practical impact and experimental breadth.
- `QQYpgReSRk` (MOFI, 6.25, Accept) — large-scale vision model; RULE has stronger methodological novelty and more rigorous evaluation.

**Round 2 comparison:** RULE sits between the 6.6–6.7 anchors (weaker exposition but stronger scope) and the 7.0 anchor (comparable overall). The exposition gaps (orphaned greedy strategy, unspecified $\hat{w}_i^m$) prevent it from reaching the 8.0 tier.

**Final score: 7.0** — A solid paper with a novel problem, well-designed method, and strong empirical support. The main weaknesses are expositional gaps that are addressable in revision rather than fundamental methodological flaws.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>