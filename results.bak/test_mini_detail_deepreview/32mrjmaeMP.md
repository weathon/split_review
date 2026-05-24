Now let me construct the final consolidated review.

---

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a method that regularizes task-vector fine-tuning to reduce cross-task interference without requiring access to external task data. The key insight is to reformulate representation-drift regularization as a quadratic form of the Jacobian Gramian, connect it to the generalized Gauss-Newton matrix, and approximate it via KFAC. A Kronecker-factor accumulation heuristic keeps memory and compute costs constant in the number of tasks. Experiments on vision (CLIP ViT-B/32, B/16, L/14 across 8 datasets) and language (T5-base on 6 NLP tasks) show that TAK achieves state-of-the-art or competitive performance on both task addition and negation, while being dataless, robust to scaling coefficients, and computationally efficient.

## Strengths

1. **Novel connection between representation-drift regularization and KFAC curvature approximation.** The paper cleanly derives representation drift under linearization (Eq. 2–3) as a quadratic form of the Jacobian Gramian, identifies this as an instance of the GGN matrix (Section 3.2), and leverages KFAC — a well-studied approximation from second-order optimization — to make it tractable. This theoretical bridge is principled and distinguishes TAK from prior dataless methods (e.g., diagonal GGN in Porrello et al., 2025) that use coarser approximations.

2. **Strong empirical results across task addition and negation, with practical advantages over data-dependent methods.** TAK matches or exceeds the data-dependent method τJp despite requiring no cross-task data during regularized fine-tuning. On ViT-L/14 task addition (Table 1), TAK with α=1 achieves 91.6 absolute accuracy vs. τJp's 90.9. On task negation (Table 2), TAK achieves substantially lower target accuracy (3.4 vs. 6.7 on ViT-B/32) while maintaining higher control accuracy (62.4 vs. 60.8). These gaps are consistent across model scales and modalities.

3. **Robustness to task-vector rescaling, eliminating held-out tuning.** Figure 4a shows TAK maintains high accuracy across a wide range of α (0 to 2), while competing methods peak sharply. This is a practical advantage: practitioners can use α=1 without grid search, which is critical when validation data from other tasks is unavailable.

4. **Thorough computational and ablation analysis.** The paper reports training time, memory overhead (Figure 6), KFAC estimation cost (≈4 minutes for 8 tasks), the effect of the Kronecker accumulation heuristic (Table 3 shows marginal gaps), KFAC compression strategies (Figure 7b achieves 87% memory reduction with ~1-point accuracy drop), and scheduling of the regularization loss (Figure 8). This level of detail is uncommon and significantly strengthens the paper's practical claims.

5. **Demonstration of task localization.** Figure 5 shows that TAK forces the Jacobian-vector norm ‖J_θ f(x,θ₀) τ_t‖₂² to be near zero for inputs outside task t's distribution, empirically verifying the weight-disentanglement property that the regularizer is designed to encourage.

## Weaknesses

### Fatal
None.

### Major

1. **No variance estimates on main results.** Tables 1, 2, and 3 report only point estimates without error bars or standard deviations. Given the sensitivity of task arithmetic to initialization and training stochasticity, it is unclear whether small differences between methods (e.g., ViT-B/16 τJp 88.6 vs. TAK 88.3 at best α) are significant. The paper itself observes "variance across seeds increasing as the number of MC samples grows" (Section 4, KFAC estimation paragraph), confirming that stochasticity is present. This is the most impactful evidential gap: the conclusions are likely correct, but the evidence is weaker than it should be.

2. **The Kronecker-factor accumulation heuristic (Eq. 8) lacks theoretical grounding.** The paper merges per-task KFAC factors by summing Kronecker factors separately, which is not mathematically equivalent to the sum of Kronecker products. The authors acknowledge this is a heuristic and validate it empirically (Table 3), where gaps are indeed marginal. However, no theoretical justification or discussion of conditions under which the approximation is accurate is provided. Given that this heuristic is central to the constant-complexity claim, the absence of analysis on when/why it might fail is a gap.

### Minor

3. **The "dataless" claim requires qualification.** TAK avoids using cross-task data *during regularized fine-tuning* — the regularizer only accesses pre-computed KFAC factors. However, computing those factors still requires forward-backward passes through each task's data (Section 3.3; Figure 7 experiments use 128–256 examples per task). The paper presents this as a reasonable one-time pre-computation cost (≈4 minutes), and the body (Section 3.1: "after initial pre-computation – does not require further data access") clarifies this. But the title, abstract, and "dataless" framing could mislead readers into thinking the method requires *no task data at all*. This is a presentation issue, not a methodological flaw.

4. **The non-linear regime extension is heuristic.** The regularizer is derived under the linearized model (Eq. 2–3), and the paper's best absolute results come from the linearized regime. The extension to non-linear fine-tuning relies on pairing TAK with attention-only fine-tuning, which "implicitly induces kernel-like behavior" (Jin et al., 2025). The paper is transparent about this ("although our regularization is not theoretically exact in the non-linear regime"), but the justification is empirical and the non-linear results (e.g., Attn. Only FT + TAK at α=1 for ViT-B/16: 59.0 vs. the linearized TAK 88.3) are substantially weaker. The paper would benefit from a clearer delineation of where the theory holds vs. where the method is a heuristic.

5. **Squared loss vs. cross-entropy GGN is not ablated.** The paper uses the squared-loss GGN (i.e., the unweighted Jacobian Gramian, Eq. 3) rather than the GGN weighted by the Hessian of the actual training criterion (e.g., cross-entropy). The justification ("output-space Euclidean distance is appropriate for representation drift") is reasonable, but an ablation comparing the two choices would be informative.

### Trivial
None.

## Nice-to-Haves
- Report results with error bars on the main benchmarks (Tables 1 and 2). The paper already has the infrastructure for multiple runs (the MC analysis uses multiple seeds), so this is feasible.
- Ablate the choice of loss for the GGN (squared loss vs. cross-entropy) to clarify whether the output-space Euclidean distance is the right measure for representation drift.
- Discuss the privacy implications of sharing KFAC factors. While aggregate covariances leak less information than raw data, a brief discussion would strengthen the privacy motivation.

## Removed Points

- **Weakness about the method being designed for linearized regime but tested in non-linear regime.** The paper explicitly acknowledges this limitation ("although our regularization is not theoretically exact in the non-linear regime") and pairs TAK with attention-only fine-tuning as a reasonable bridge. The non-linear results are presented as an extension, not a core claim. The critic's framing that "best absolute performance on vision is in the non-linear regime" misreads Table 1 (linearized TAK at 88.3 for ViT-B/16 actually outperforms non-linear TAK at 84.3). Removed as partially misreading the paper.

- **"Constant complexity is slightly oversold" criticism.** The paper is transparent about pre-computation being O(T) (Figure 6b shows total pre-computation time). The abstract's "constant complexity" refers to the regularizer's cost during training. The body clarifies this. This is accurate, not oversold.

- **Strength: "data-free regularization achieves state-of-the-art performance" — the Strength Finder claimed TAK matches τJp on some metrics but this is slightly overstated.** In task negation, TAK clearly outperforms τJp (3.4 vs 6.7 on ViT-B/32). In task addition, TAK is competitive and sometimes ahead. Retained as a genuine strength but rephrased.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's substance and differ mainly in tone.

## Suggestions

1. Add means and standard deviations (≥3 seeds) to Tables 1 and 2 for the main comparisons. If computation is prohibitive, at minimum report for the key comparison (TAK vs. τJp across model sizes).
2. Add an ablation comparing the squared-loss GGN (used in the paper) against the cross-entropy-weighted GGN on at least one setting (e.g., ViT-B/32, 8 Vision).
3. Add a brief theoretical analysis or discussion of when the Kronecker accumulation heuristic (Eq. 8) is expected to be accurate (e.g., when curvature structures are similar across tasks, or when input/output distributions have low variance).
4. Qualify the "dataless" framing in the abstract/introduction to clarify that one-time KFAC pre-computation uses task data, after which no further access is needed.

## Score and Decision

**Calibration analysis.** All anchors listed below were retrieved from `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`.

**Round 1 (bracketing):**
- Weak anchors (score < 3.5): `WM5G2NWSYC.md` (2.00, task arithmetic unrelated), `HCCkCjClO0.md` (3.00, continual learning), `OW5Gf4cse1.md` (3.00, LLM emergent abilities), `fUz6Qefe5z.md` (3.00, NTK theory). These are clearly weaker papers — the current paper is orders of magnitude more complete.
- Middle anchors (3.5–7.5): `1VwWi6zbxs.md` (6.00, τJp paper — the main baseline), `dj0TktJcVI.md` (6.25, Attention-Only FT paper), `SkF7NZGVr5.md` (5.50, curvature & plasticity), `eeyhnqYbxw.md` (4.80, geometry of attention).
- Strong anchors (>7.5): `STUGfUz8ob.md` (7.60, transformer reasoning), `gc8QAQfXv6.md` (9.00, continual instruction tuning), `PdaPky8MUn.md` (8.00, long-sequence models), `1aF2D2CPHi.md` (8.00, data-free knowledge distillation).

**Preliminary bracket: 5.5–7.5.**

**Round 2 (narrowing inside bracket):**
- `1VwWi6zbxs.md` (6.00, τJp paper): This is the closest competitor. The τJp paper's main weaknesses were: (a) requires data from other tasks, (b) no runtime/computational cost reporting, (c) limited to image classification. TAK addresses all three: it is dataless, reports detailed computational analysis, and evaluates on both vision and language. TAK is clearly stronger than this anchor.
- `dj0TktJcVI.md` (6.25, Attention-Only FT): Had reviewer 2 claiming "naive combination of prior work" with score 3/10. TAK has a more novel core contribution (connecting representation drift to KFAC). TAK also has more thorough evaluation. TAK is stronger.
- `1v7SRWsYve.md` (6.33, MAP): Had presentation issues and limited comparison to baselines. TAK is more thorough and cleaner in presentation. TAK is stronger.
- `7D9X2cFnt1.md` (7.00, EFC): Very positive reviews (8,8,6,6) with generally minor weaknesses. The EFC paper is well-written and has SOTA results in its subfield. TAK is comparable in thoroughness but in a less mature subfield (task arithmetic). The main difference is that TAK has the variance-reporting gap which the EFC paper does not. TAK is slightly weaker than this anchor.

**Final score:** The paper is clearly stronger than the ~6.0–6.33 anchors but has more notable evidential gaps than the 7.0 anchor (EFC). The core contribution is novel and well-executed, the experimental evaluation is comprehensive, and the practical advantages (dataless, constant complexity, robustness to α) are clearly demonstrated. The main weakness — missing variance estimates — is significant but addressable. **Score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>