Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper introduces CausalNovo, a model-agnostic framework for *de novo* peptide sequencing that leverages causal reasoning to learn representations focusing on signal fragment ions while suppressing spurious noise peaks. Grounded in a Structural Causal Model with independence and sufficiency principles, the framework uses a Causality Extraction Module with information-theoretic objectives (contrastive learning for invariance and cross-entropy losses for prediction) to disentangle causal from non-causal representations. Experiments across three public datasets (Nine-species, Seven-species, HC-PT) and three baseline architectures (CasaNovo, AdaNovo, π-HelixNovo) show consistent improvements of up to 10–14% in amino acid, peptide, and PTM-level metrics.

## Strengths

- **Consistent and substantial performance gains across multiple baselines and datasets.** Table 1 shows CausalNovo improves amino-acid precision over retrained baselines by 2.2–14.2 percentage points across all three datasets. On the Seven-species dataset, CasaNovo precision rises from 0.357 to 0.477 (+12.0 points). Peptide-level precision and AUC also improve across all settings, and CausalNovo outperforms SearchNovo on several metrics (e.g., peptide precision 0.564 vs. 0.550 on Nine-species).

- **Demonstrated robustness to noise perturbations** via vulnerability analysis (Figures 1 and 3, Table 6). Baseline models degrade substantially when noise peaks are replaced, while CausalNovo maintains higher precision, achieving up to 28.5% relative improvement (HC-PT, threshold=1). This directly confirms the method relies on causal signal peaks rather than spurious correlations.

- **Model-agnostic framework with broad applicability.** CausalNovo improves *all three* baselines on *every* metric in Tables 1, 2, and 5, demonstrating general-purpose enhancement. Cross-species leave-one-out experiments (Table 3) show gains on all nine species (+2.6% average peptide precision improvement), ruling out overfitting to a single organism's spectra.

- **Interpretable attention shift** (Table 7) provides mechanistic evidence: the fraction of predictions where the model's top‑3 attended peaks are all causal rises from 19.26% (baseline) to 32.87% (CausalNovo), directly supporting the claim that the model focuses on signal fragment ions.

- **Component ablation** (Table 4) cleanly validates each design choice (independence +1.2%, purification +0.8%, symmetric training +0.4%), confirming that the gains come from the proposed objectives.

## Weaknesses

### Major

- **The contrastive loss does not match the claimed theoretical objective.** The paper derives the independence principle as *max I(z_c; z_c′ | C)*, replaces unobserved *C* with label *Y* (giving *I(z_c; z_c′ | Y)*), and then implements Eq. (5) as a standard InfoNCE loss with batch negatives. This standard InfoNCE approximates unconditional *I(z_c; z_c′)*, not the conditional *I(z_c; z_c′ | Y)* — the conditioning on *Y* is never operationalized. The loss is instance-level discrimination between different spectra, not class-conditioned invariance. While the practical effect (encouraging perturbation-invariant representations) is reasonable and the empirical results are strong, the theoretical narrative as written overclaims what the loss provably enforces. This matters because it is the centerpiece of the paper's causal framing. **Resolution**: either reformulate the loss (e.g., within-class negatives, conditional contrastive objective) or revise the theoretical narrative to transparently characterize the loss as instance-level invariance rather than conditional mutual information.

- **No comparison with simpler noise-robust alternatives.** The paper does not compare against data augmentation, spectral denoising methods (e.g., Noise2Vec, MSDenoiser), or peak filtering baselines. These would clarify whether the benefit comes from causal modeling specifically, or from any form of noise-invariant training. This is not fatal — the ablation studies control for components — but it weakens the claim that the causal framing is the source of improvement.

### Minor

- **The purification objective** (*max I(z_s; Y)*) is described as "indirectly lead[ing] to the purification of z_c" without formal justification. The intuition is plausible and the ablation confirms it helps (+0.8%), but the theoretical claim about purification is speculative rather than proven. The paper should either provide a formal argument or present the objective more honestly as a helpful auxiliary loss.

- **Retrained baselines differ substantially from published values** (e.g., CasaNovo AA recall on Nine-species: 0.696 published vs. 0.740 retrained). The paper says "retrained with the same configurations" but does not explain the source of these discrepancies. Since CausalNovo's improvements are measured relative to the retrained versions (not the published ones), the gap warrants at least a brief discussion (e.g., different hardware, random seeds, data preprocessing). The relative improvements within the controlled setup are valid, but the lack of explanation raises questions about reproducibility.

- **Missing standard deviations or confidence intervals** for all main results. This is common in the field but still limits the reader's ability to assess result stability, especially given the large retraining differences noted above.

- **Training time** is mentioned as "approximately 2.3x" but is not quantified with any concrete data (table, figure, or precise number). A quantitative statement (e.g., "CasaNovo baseline trains in X hours; CausalNovo in Y hours") should be provided.

- **The RCCP justification** is slightly imprecise: the paper states "C ⟂ S" as part of the structural equations derived from RCCP, but RCCP does not directly imply independence between causal and non-causal factors — it is a modeling assumption, not a consequence of the principle. This is a minor clarity issue.

### Trivial

- Missing standard deviations throughout (noted above; trivially fixable).
- "approximately 2.3x training time" should be accompanied by concrete numbers.

## Nice-to-Haves

- An evaluation on a more challenging out-of-distribution benchmark (e.g., MassIVE-KB or a different-instrument dataset) would strengthen claims about generalization under distribution shift. The paper explicitly acknowledges this is a priority for future work; adding even one such experiment would be impactful.
- Ablation on hyperparameters (α, τ, γ) would improve completeness.
- Visualization of the learned attention mask M (which peaks receive high importance) would strengthen the interpretability analysis.

## Removed Points

These points from the inputs are removed with justification:

- **"Evaluation protocol does not reflect the most challenging settings" (harsh critic's #2)** → The paper explicitly acknowledges this limitation in the Conclusion ("our evaluation follows the NovoBench setting, whereas recent methods (e.g., ContraNovo, RankNovo) adopt a more realistic protocol… is a priority for future work"). A gap noted and owned by the authors is not a hidden weakness; it becomes a nice-to-have. Demoted accordingly.
- **"The perturbation uses the same noise-identification method as the training intervention"** → This is by design: the intervention during training mirrors the test-time perturbation to create a consistent evaluation. The paper provides a secondary analysis in Table 6 with a more comprehensive 18-ion-type set, which serves as a robustness check. The criticism is not a genuine weakness.
- **The training time complaint ("no quantitative evidence")** → The paper states "approximately 2.3x training time" and though it lacks a precise number, this is acknowledged as a limitation. Kept as a minor weakness but noted as requiring concrete data.
- **Strength Finder's generic strengths** ("the paper addresses an important problem", "the paper is well-motivated") → Removed as generic. Only evidence-backed strengths are retained.
- **"No analysis of the learned mask M"** → The paper provides attention analysis in Table 7, which serves essentially this purpose. Partially addressed.
- **"Hyperparameter sensitivity"** → Reasonable request but standard for this type of paper; demoted to nice-to-have.
- **"Missing comparison with denoising baselines"** → Retained as a Major weakness because it would help attribute the source of improvement.

## Novel Insights

None beyond the paper's own contributions. The core insight — that applying causal disentanglement principles to peptide sequencing via a model-agnostic module with contrastive and cross-entropy objectives yields robust gains — is clearly stated and demonstrated. The reviews surface no additional synthesized insight not already in the paper.

## Suggestions

1. **Fix the independence objective gap**: Either reformulate the loss to explicitly condition on *Y* (e.g., supervised contrastive learning with same-class negatives) or revise the theoretical narrative to describe the loss as instance-level invariance rather than conditional mutual information. This is the single most impactful improvement for theoretical soundness.

2. **Explain the retrained baseline differences** — even a brief sentence about hardware/software/environment changes that caused discrepancies from published values would substantially improve reproducibility.

3. **Add standard deviations or confidence intervals** to the main results tables.

4. **Quantify training time** with a concrete number or small table.

5. **Consider adding one evaluation on a more challenging OOD benchmark** to directly support the generalization claims, even if relegated to the appendix.

## Score and Decision

**Round-1 bracket**: I queried three bands: weak (<3.5), middle (3.5–7.5), strong (>7.5). Weak anchors (avg 3.0) were rejected papers with significant theoretical or empirical gaps. Middle anchors (4.25–6.0) included causal representation learning papers with partial empirical support. Strong anchors (8.0) were accepted papers in protein design with comprehensive evaluation. The paper clearly sits in the middle band.

**Round-2 narrowing**: I queried within (4.5, 7.5) for domain-specific papers. **ReNovo** (6.50, accept) is the closest comparison: same subfield, similar empirical rigor, but ReNovo's main weakness is missing comparisons while CausalNovo's main weakness is a theoretical framing gap. **RankNovo** (5.50, reject) has less extensive empirical support. Based on these comparisons, the paper is slightly weaker than ReNovo (6.50) due to the theoretical gap but notably stronger than RankNovo (5.50) due to more comprehensive validation.

**Final score**: 6.0. This reflects a solid empirical contribution with clear strengths (consistent gains, robustness validation, model-agnostic design, interpretability evidence) weighed against a genuine but non-fatal theoretical gap in how the central independence objective is justified.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>