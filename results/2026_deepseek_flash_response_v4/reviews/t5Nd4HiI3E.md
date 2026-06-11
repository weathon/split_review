## Summary

This paper identifies high gradient variance from stochastic trace sampling as a key bottleneck for aligning Large Reasoning Models (LRMs) with human preferences, and proposes BVPO. The method combines a high-variance trace-based gradient with a low-variance "empty-trace" gradient (computed by disabling reasoning) via a convex combination \(g_c = \alpha g_t + (1-\alpha) g_e\). The paper provides theoretical analysis (variance reduction, MSE-optimal mixing, tighter SGD convergence bounds) and empirical results on three LRM families showing consistent gains over DPO and SimPO on Arena-Hard (up to +6.8 points) and AlpacaEval 2 (up to +7.8 points), with an additional bonus of improved math reasoning performance despite training only on general conversational data.

---

## Strengths

1. **Consistent and strong empirical gains across all settings (Table 1).** BVPO outperforms the best baseline (DPO or SimPO) in every one of 18 reported conditions (3 model sizes × 2 inference modes × 3 metrics). No other method wins in even a single cell. This consistency directly supports the paper's core claim that managing the bias-variance trade-off yields better alignment.

2. **Reasoning improvement is a non-obvious finding (Table 2).** BVPO, trained exclusively on general conversational data, raises average math reasoning performance over the base model by up to 4.0 points (R1-Qwen-7B: 60.5→62.3; R1-Qwen-1.5B: 44.7→48.7; R1-0528-Qwen3-8B: 74.7→76.1). This suggests the method's benefits extend beyond alignment quality and that reducing trace variance has positive side effects on reasoning capability.

3. **Clean theoretical variance-reduction guarantee (Theorem 1).** Proves \(\text{Var}(g_c) = \alpha^2 \text{Var}(g_t) < \text{Var}(g_t)\) for any \(\alpha \in (0,1)\) where \(\text{Var}(g_t) > 0\). This is unconditional on any assumptions about the data distribution and provides a clear mathematical foundation for the method.

4. **MSE domination guarantee (Theorem 2 + Corollary 1).** Proves \(\text{MSE}(g_c(\alpha^*)) \leq \min\{\text{MSE}(g_t), \text{MSE}(g_e)\}\) — the combined estimator is provably never worse than the better of its two components, and strictly better under mild conditions. This is a meaningful formal guarantee for a convex-combination method.

5. **Simplicity and generality.** The approach is a convex combination of two loss terms (Equation 2) that can be layered on top of any preference optimization objective. The paper instantiates it with DPO, but the gradient estimator \(g_c = \alpha g_t + (1-\alpha)g_e\) is algorithm-agnostic, making the contribution easy to adopt and extend.

---

## Weaknesses

### Fatal
None.

### Major

1. **Hyperparameter \(\alpha\) not reported and no sensitivity analysis.** The mixing coefficient \(\alpha\) is BVPO's only hyperparameter, and the paper devotes an entire theoretical section (Section 4.2) to deriving its optimal closed-form value. Yet the main experiments never state what \(\alpha\) was used, whether it was held constant across models, or how sensitive results are to its choice. This is a significant reproducibility gap — the practical contribution depends entirely on how this hyperparameter is set, and the reader cannot assess the method's robustness from the reported results.

2. **No direct empirical evidence that variance reduction is the mechanism of improvement.** The paper's central narrative is that trace sampling induces high gradient variance and BVPO reduces this variance, which in turn improves alignment. Yet no plot, table, or statistic directly measures gradient variance during training for either the baselines or BVPO. The paper cites Appendix B for evidence about log-probability variance — but this is about the variance of log-probabilities, not gradients, making it only an indirect proxy. Without direct variance measurements (e.g., trace of gradient covariance, gradient norm dynamics over training steps), the causal claim connecting variance reduction to improved alignment is partially circumstantial.

3. **No statistical significance or error bars.** All results in Tables 1 and 2 are point estimates with no uncertainty quantification. Given the paper's central claim is about *variance* — and that stochasticity is a core challenge — reporting single-seed results without confidence intervals or multiple-seed standard deviations is a conspicuous gap. This is especially important because the gains, while consistent, are sometimes modest (e.g., 71.5 vs. 69.2 on Arena-Hard for R1-0528-Qwen3-8B Thinking).

### Minor

4. **Closed-form \(\alpha^*\) depends on intractable quantities.** Theorem 2's formula for \(\alpha^*\) (line 149) depends on bias vectors \(b_t = \mathbb{E}[g_t] - \mu\) and \(b_e = \mathbb{E}[g_e] - \mu\), where \(\mu = \nabla_\theta \mathcal{L}_m(\theta)\) is the marginal gradient that the paper itself acknowledges is "computationally intractable" (line 71). The theoretical \(\alpha^*\) therefore cannot be computed in practice. This is common in optimization theory (optimal quantities often depend on unknown true values), but the abstract's phrasing — "provides a closed-form choice of the mixing weight" (line 9) — overstates practical applicability. The paper should be clearer that this is a formal characterization rather than a recipe practitioners can directly apply.

5. **Nature of the empty-trace gradient could be discussed more carefully.** The empty-trace loss \(\mathcal{L}_e\) uses \(\pi_\theta(r=\emptyset, y|x)\), which is the joint probability of a fixed empty trace and the answer — a qualitatively different object from the marginal probability \(\pi_\theta(y|x)\) that the ideal loss targets. While the paper correctly notes "potentially higher bias" (line 95), the formal treatment treats \(b_e\) as a benign bias that can be compensated by mixing, without discussing the possibility that \(g_e\) may point toward a fundamentally different optimum. The bias in this context is not just a scalar shift but a structural difference. Adding a brief discussion would strengthen the framing.

6. **Theorem 4's \(\eta L = 1\) condition is restrictive.** The key result linking MSE-optimality to SGD convergence (Theorem 4) requires \(\eta L = 1\). For neural network training, the smoothness constant \(L\) is typically unknown and varies across the optimization trajectory, making it difficult to verify this condition. The paper should acknowledge this limitation in the main text rather than only in the theorem statement.

### Trivial

7. **Notation inconsistency on line 21.** The combined estimator is introduced as \(g_e(\alpha)\) (likely a typo for \(g_c(\alpha)\)), inconsistent with the notation \(g_c\) used throughout the rest of the paper.

---

## Nice-to-Haves

- A brief discussion of alternative approaches to variance reduction in gradient estimation (e.g., control variates, importance sampling) and why the convex-combination approach was chosen.
- An investigation of whether the optimal \(\alpha\) changes over the course of training (the paper mentions adaptive \(\alpha_k\) in Section 4.3 but does not experiment with it).
- Evaluation of BVPO with other preference optimization backbones (e.g., SimPO as the base, not just DPO) to demonstrate algorithm-agnosticity empirically.

---

## Removed Points

These points from the input reviews are flagged for removal; they should be treated with caution:

- **Harsh critic's claim that the paper overstates novelty about "no systematic study" of LRM alignment (line 31).** The paper explicitly acknowledges DeepSeek-R1's PPO work ("limited to brief remarks in technical reports") and correctly distinguishes its contribution as a systematic treatment rather than claiming to be the first-ever attempt. The cited text says "there is no systematic study" — this is accurate as the existing discussions are brief subsections in technical reports.
- **Harsh critic's criticism about Appendix B being "impossible to evaluate."** The parser strips appendices from all papers; they exist in the original submission. Per the meta-reviewer instructions, missing-appendix criticisms should be removed.
- **Harsh critic's framing of the empty-trace gradient concern as a "structural" issue that undermines the bias-variance formalism.** The paper already acknowledges the bias (line 95), and the bias-variance formalism is mathematically sound for handling this — the bias term \(b_e\) captures exactly this structural difference. Retained as Minor weakness 5 above but the "structural"/"fatal" framing is removed.
- **Strength Finder's generic or superficial strengths** (e.g., "this paper addressed an important problem," "the paper targets an interesting question"). These lack specific content anchored to the paper's concrete contributions and are removed per instructions.
- **Strength Finder's claim about Theorem 4's "direct link between statistical optimality and SGD convergence"** is retained as a real strength, but note the \(\eta L = 1\) condition makes it less general than it first appears (Minor weakness 6).

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Report the \(\alpha\) value(s) used in the main experiments** and include a sensitivity analysis (e.g., sweep over \(\alpha \in \{0, 0.25, 0.5, 0.75, 1.0\}\)) showing how alignment metrics vary with this choice.
2. **Add confidence intervals or standard deviations** to Tables 1 and 2 using at least 3 random seeds.
3. **Provide empirical measurements of gradient variance** — e.g., track \(\text{Var}(g_t)\), \(\text{Var}(g_e)\), and \(\text{Var}(g_c)\) during training for a representative setting, or at minimum plot gradient norms over training steps for BVPO vs. DPO.
4. **Clarify in the abstract and introduction** that the closed-form \(\alpha^*\) is a formal theoretical result (which provides the domination guarantee) but the formula depends on the intractable true marginal gradient, so \(\alpha\) must be selected as a hyperparameter in practice.
5. **Add training hyperparameters** (learning rate, number of epochs, batch size, \(\beta\) value for DPO) to the main text rather than deferring entirely to the appendix.

---

## Calibration Anchors

**Round 1 — Bracketing:** Narrowest plausible range = [5.0, 7.0]. Papers below 3.5 (general DPO variants scoring 2.5–3.4) are clearly weaker — they lack theory, have inconsistent or small improvements, or are purely incremental. Papers above 7.5 are strong comprehensive contributions with deeper analysis (e.g., 8.0 papers on reward modeling or multi-value alignment). BVPO sits between these.

**Round 2 — Narrowing:** Anchors used to position within the bracket:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qBKA2844I4.md (HyperDPO) | 5.50 | R2 | Weaker: incremental combination of known techniques, less consistent results |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ToWKyjwDqO.md (Direct Judgement PO) | 5.00 | R2 | Weaker: narrower scope, mixed reviewer opinions |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/h71cSd2loX.md (Extending DPO to Ties) | 5.50 | R2 | Weaker: modest extension, limited empirical breadth |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/TU5ApbbeDZ.md (Learning Loss Landscapes) | 5.00 | R2 | Weaker: narrow scope (MuJoCo environments only) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/O0sQ9CPzai.md (TPO) | 6.33 | R2 | Comparable: similar DPO+reasoning contribution, but TPO evaluated on only one model family (Qwen); BVPO has broader empirical scope |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9Hxdixed7p.md (3D-Properties) | 6.25 | R2 | Slightly stronger: deeper analysis of DPO limitations, though novelty questioned; BVPO's method contribution is more novel |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/twtTLZnG0B.md (α-SVRG, accepted) | 6.25 | R2 | Comparable: both propose a simple α-weighted combination for variance reduction with theory + experiments; BVPO has broader model scope but weaker experimental rigor (no error bars, no α report) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/StYc4hQAEi.md (Sliced Wasserstein) | 6.50 | R2 | Slightly stronger: more thorough empirical validation with error analysis, well-received by reviewers |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/uaMSBJDnRv.md (Unintentional Unalignment) | 7.00 | R2 | Stronger: deeper theoretical and empirical analysis of DPO behavior |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/GBWqZNoeIk.md (Generalizing Stochastic Smoothing) | 5.00 | R1 | Weaker: mixed reviews, insufficient novelty |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/EVZnnhtMNX.md (Scalable Preference Learning) | 3.00 | R1 | Much weaker: limited results, weak novelty |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/aYYZBPoSHb.md (Multi-Objective ORPO) | 3.40 | R1 | Much weaker: incremental, limited empirical evidence |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rfdblE10qm.md (Rethinking Reward Modeling) | 8.00 | R1 | Stronger: deeper theoretical contribution, comprehensive analysis |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NN6QHwgRrQ.md (MAP) | 8.00 | R1 | Stronger: more comprehensive framework for multi-value alignment |

BVPO is clearly above the 5.0–5.5 anchor papers (which are incremental or have narrow scope) and sits comparably to the 6.25–6.5 level. It is slightly below the 7.0 paper (Unintentional Unalignment) and well below the 8.0 papers. The missing experimental rigor (α unreported, no error bars, no variance measurements) prevents it from reaching the 6.5+ level despite its strong and consistent empirical breadth.

---

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**