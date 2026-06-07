Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

CausalNovo is a model-agnostic framework for de novo peptide sequencing that augments existing models (CasaNovo, AdaNovo, π-HelixNovo) with a Causality Extraction Module (CEM). The CEM learns per-peak importance scores through an attention mechanism, then applies a replacement-based perturbation to noise peaks (identified using known fragmentation patterns from ground-truth labels) and uses contrastive learning to make the "causal" representation invariant under such perturbations. The framework is grounded in a Structural Causal Model that motivates independence and sufficiency objectives. Evaluated on three benchmark datasets (Nine-species, Seven-species, HC-PT), CausalNovo achieves consistent but modest improvements at amino acid, peptide, and PTM levels across all baselines, with the strongest improvement shown under high-noise conditions.

## Strengths

- **Consistent gains across three baselines, three datasets, and three metric levels (Tables 1, 2).** CausalNovo improves every baseline on almost every metric — no baseline is harmed on any dataset. For example, π-HelixNovo + CausalNovo raises amino acid precision from 0.765 to 0.787 on Nine-species and from 0.465 to 0.536 on Seven-species. The consistency across 3 model architectures rules out model-specific artifacts.

- **Vulnerability analysis (Table 6, Figures 1, 3) provides direct evidence that CausalNovo reduces reliance on noise peaks.** Under the tightest perturbation threshold (γ=1), CasaNovo's peptide precision drops to 0.397 on Nine-species and 0.156 on HC-PT, while CausalNovo retains 0.482 and 0.352 — a relative improvement of 10.3% and 28.5%. This directly measures the claimed behavior change.

- **Attention analysis (Table 7) gives mechanistic interpretability evidence.** CausalNovo increases the proportion of predictions attending to all three top causal peaks from 19.26% to 32.87%, while decreasing the proportion attending to zero causal peaks from 12.73% to 10.76%. This goes beyond aggregate metrics to show the model's attention is shifting toward signal ions.

- **Cross-species validation (Table 3) shows no species degrades.** Across all nine species in leave-one-out evaluation, CausalNovo improves CasaNovo's peptide precision (e.g., +2.4% on Human, +3.9% on Mouse, +3.9% on Tomato), ruling out the possibility that gains are driven by a particular test distribution.

- **Principled derivation from the SCM (Section 3.2).** The independence and sufficiency properties are clearly derived from the SCM equations and directly motivate the contrastive and cross-entropy objectives. This provides a clean conceptual framework for what would otherwise be ad-hoc regularization.

## Weaknesses

### Major

- **Two critical hyperparameters (α and γ) are not reported.** The fraction α of noise peaks replaced during the intervention (Section 3.4.1) and the tolerance threshold γ for identifying non-causal ions (Eq. 4) are defined but never given specific values anywhere in the paper (verified by text search). α controls how aggressive the perturbation is; γ defines what counts as a signal peak. These are not minor implementation details — they define the method's core operations. Without them, the experiments cannot be reproduced from the paper alone, and the sensitivity of results to these values is unknown. (The harsh critic notes that the ablation in Table 5 mentions "20% of noise peaks" for the drop variant but never states α used for replacement.)

- **The paper's core claim about improved generalization to distribution shift is not tested.** The paper motivates the method by arguing that standard models fail because they learn spurious correlations under distribution shift (contaminants, instrument variation, etc.). Yet the evaluation follows the standard NovoBench protocol (training and testing on the same dataset with held-out species splits from the same distribution). The authors explicitly acknowledge this in the conclusion (line 295-299): "our evaluation follows the NovoBench setting, whereas recent methods adopt a more realistic protocol that trains on large-scale external corpora and evaluates on out-of-distribution test sets. Assessing CausalNovo under this protocol... is a priority for future work." This is an honest admission, but it means the paper's central claim — that causal representations improve robustness and generalization under distribution shift — remains unvalidated. The cross-species validation (Table 3) is a step in this direction but stays within the same dataset.

### Minor

- **No statistical significance or variance estimates for any result.** Every number in Tables 1–7 and Figures 1–4 is reported as a single point estimate. Many improvements are small in absolute terms (e.g., +0.4% from the symmetric objective in Table 4; +0.6% from the replace operation in Table 5). Without confidence intervals, standard deviations, or significance tests, it is impossible to determine whether these differences reflect genuine improvements or random variation. This is a standard concern in proteomics benchmarks (as noted in reviews of ReNovo and RankNovo), but it weakens the evidential value of the reported numbers.

- **Retrained baselines differ substantially from published results.** In Table 1, the retrained CasaNovo (†CasaNovo) achieves 0.741/0.740 on Nine-species, while the published CasaNovo scores 0.697/0.696 — a ~6% absolute difference. Similarly, AdaNovo retrained (0.681) is lower than published (0.698). These discrepancies raise the question of whether the retraining configuration (e.g., hyperparameters, early stopping criteria, data preprocessing) differs from the original papers in ways that could favor or disfavor CausalNovo. While the comparison between retrained baselines and CausalNovo is internally fair (same training setup), the large gap from published results suggests the setup is not calibrated to the original models' optimal configurations.

- **The causal framing is somewhat decorative.** The method uses ground-truth peptide labels to compute theoretical fragment spectra, then labels any peak within tolerance γ of those theoretical masses as "causal." This is label-guided feature engineering with domain knowledge, not causal discovery. The SCM equations and do-operator language (Reichenbach's Common Cause Principle, intervention, etc.) provide a conceptual motivation, but the algorithm can be described more directly as: "use known fragmentation patterns to identify signal peaks, learn an attention mask that focuses on them via contrastive regularization, and train on the masked representation." Readers familiar with the causal representation learning literature (Chen et al., 2022; Kaddour et al., 2022) will recognize this as a valid application of causal principles to representation learning — the paper is transparent about using Y as a proxy for C — but the framing overstates the methodological novelty. This is a presentational issue, not a fatal flaw.

### Trivial

- **Table 4 and 5 have presentation issues in the extracted text** (all checkmarks appear identical across rows due to parser artifacts; the accompanying text clarifies which components are active per row). This does not affect the paper's substance.
- **The attention analysis (Table 7) evaluates the model on whether it attends to peaks defined as "causal" by the same criterion used during training.** The metric is thus aligned with the training objective. The independent evidence of effectiveness comes from the downstream performance gains (Tables 1–3), not from this analysis.

## Nice-to-Haves

- Reporting α and γ values plus a sensitivity analysis for each would significantly strengthen reproducibility and show whether performance is robust to these choices.
- An out-of-distribution experiment (e.g., train on Nine-species, test on HC-PT, or train on one instrument type and test on another) would directly test the paper's core generalization claim.
- Adding variance estimates (e.g., 3 random seeds with standard deviations) would allow readers to assess the reliability of the reported improvements.

## Removed Points

These points were flagged but removed with justifications:

- **"Causal framing is a fatal overclaim"** (harsh critic point 1): Removed because the paper transparently states it uses Y as a proxy for C (line 181) and never claims to discover causal structure de novo. It applies causal representation learning principles (Chen et al., 2022) to proteomics — a perfectly standard use of SCMs as a design framework. The criticism that "the algorithm would look essentially the same without causal vocabulary" is true but not fatal; many papers in causal ML use SCMs as conceptual motivation. This is a minor presentational weakness, as noted above.

- **"C ⟂ S independence assumption is unjustified"**: Removed. The paper explicitly derives this from RCCP as a modeling assumption. Causal representation learning papers routinely make such assumptions.

- **"Statistical vs causal false dichotomy"**: Removed. The paper provides empirical evidence (Figure 1) that baselines rely on noise peaks, which motivates the need for methods that focus on signal peaks. This is a well-supported problem statement, not a philosophical claim.

- **"Attention analysis is circular"** elevated from being treated as a major issue: The analysis simply verifies that the model behaves as intended; the independent evidence comes from downstream task performance.

- **"Missing related works"**: Removed per instruction - external knowledge cannot confirm their existence.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same assessment: the method is sound and the experiments are extensive, but the paper overstates its causal framing and lacks key rigor elements (hyperparameter reporting, variance estimates, OOD evaluation).

## Suggestions

1. Report the specific values used for α (noise replacement fraction) and γ (tolerance threshold) in Section 3.4.1 or 4.2, and include a sensitivity analysis showing how results vary with these parameters.
2. Add variance estimates: run each experiment at least 3 times with different random seeds and report mean ± std.
3. Include at least one genuine out-of-distribution experiment (e.g., train on Nine-species → evaluate on HC-PT, or train on one instrument type and test on another) to substantiate the generalization claim.
4. Temper the causal framing in the title and abstract by characterizing the method as "causality-inspired" or "causality-informed" (as it already does in the title) rather than claiming the discovery of causal representations. The empirical contributions stand on their own.

---

**Calibration anchors (all rounds):**

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| TorSeq | G536mmC2HL | 3.00 | R1 (low) | Much weaker; unrelated domain, rejected |
| CypST | ZyAwBqJ9aP | 2.00 | R1 (low) | Much weaker; unrelated domain, rejected |
| ReNovo | uQnvYP7yX9 | 6.50 | R1 (mid), R2 | Stronger: more novel contribution (first RAG for de novo); similar rigor gaps |
| RankNovo | 87B3zDRMjv | 5.50 | R1 (mid), R2, R3 | Comparable: both are framework contributions with modest improvements and similar rigor issues |
| CrossNovo (Distill) | I2ZYngkRW6 | 4.25 | R1 (mid) | Weaker: engineering-heavy, limited novelty |
| PepHAR | jqmptcSNVG | 6.20 | R3 | Different task (peptide design), but comparable evaluation rigor |
| CL-MFAP | fv9XU7CyN2 | 5.75 | R2, R3 | Different task (antibiotic prediction), similar level |
| MADGEN | 78tc3EiUrN | 6.00 | R2, R3 | Different task (molecular generation), similar evaluation depth |
| Protein Discovery (D-WJS) | zMPHKOmQNb | 8.00 | R1 (high) | Much stronger; foundational method, rigorous evaluation |

**Round 1 bracket**: 4.5–6.5 (clearly above the 2–3 proteomics-adjacent papers; below the 7.5+ papers on protein generation which have entirely different scope and rigor).

**Round 2 narrowing**: The paper is closest to RankNovo (5.5, Reject) in type and quality — both are frameworks wrapping existing models with modest improvements. It is weaker than ReNovo (6.5, Accept) which has a more original core idea. It is comparable to MADGEN (6.0, Accept) in evaluation thoroughness but MADGEN addresses a harder problem (molecular structure generation).

**Final score: 5.5** — a solid empirical contribution with consistent results, held back by the missing hyperparameter reporting, lack of OOD evaluation for the core generalization claim, and an inflated causal framing that invites more skepticism than the experiments can resolve. The paper would benefit from addressing these gaps; in its current form it is a borderline submission.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>