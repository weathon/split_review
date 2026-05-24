Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

---

## Summary

CausalNovo introduces a model-agnostic causal representation learning framework for *de novo* peptide sequencing from tandem mass spectra. Grounded in a Structural Causal Model, it operationalizes two principles—*independence* (causal representations should be invariant to noise perturbations) and *sufficiency* (causal representations should retain predictive power for the peptide sequence)—via a replace-based causal intervention and information-theoretic objectives. On three benchmark datasets (Nine-species, Seven-species, HC-PT), CausalNovo yields consistent, large-margin gains (up to +14.2% amino acid precision, +15.1% PTM precision) across three state-of-the-art baselines (CasaNovo, AdaNovo, π-HelixNovo). Vulnerability analysis, cross-species validation, NSR generalization experiments, and attention interpretability analysis collectively support the claim that the framework reduces reliance on non-causal noise peaks.

## Strengths

- **Consistent, large-margin improvements across all baselines and datasets.** CausalNovo boosts amino acid precision on Seven-species by +12.0% for CasaNovo, +5.0% for AdaNovo, and +9.1% for π-HelixNovo (Table 1). Gains are uniform across three independent benchmarks at amino acid, peptide, and PTM levels—not cherry-picked for a single setting.

- **Vulnerability analysis directly validates the core causal claim.** When noise peaks are systematically perturbed at varying thresholds, baseline models degrade sharply while CausalNovo variants maintain significantly higher precision, achieving average relative improvements of +14.9%, +15.7%, and +13.5% on HC-PT (Figures 1 and 3). This provides direct evidence that the framework actually reduces reliance on non-causal signal, beyond just improving predictive accuracy.

- **Generalization across species, noise levels, and peak-labeling strategies is well-demonstrated.** Cross-species leave-one-out validation (Table 3) shows consistent improvement across all eight species (avg. +2.6% peptide precision). Figure 4 shows sustained gains across varying noise-signal ratios (avg. +10–12%). Table 6 shows robustness even when using 18 ion types for causal peak identification. These collectively rebut concerns of dataset-specific overfitting.

- **Attention analysis provides interpretable evidence of mechanism shift.** Table 7 shows that the proportion of predictions where all top-three attended peaks are causal rises from 19.26% (baseline) to 32.87% with CausalNovo, while predictions attending to zero causal peaks drop from 12.73% to 10.76%. This bridges the gap between abstract causal objectives and observable model behavior.

- **Model-agnostic design with honest limitation reporting.** The framework is demonstrated on three distinct architectures (CasaNovo, AdaNovo, π-HelixNovo) with consistent improvements. The paper transparently notes the ~2.3× training overhead and the evaluation protocol limitation (NovoBench versus large-scale external training), which is commendable.

## Weaknesses

### Major
- **The contrastive loss is claimed to approximate $I(z_c; z_c' \mid Y)$ but implements an unconditional NT-Xent loss.** Equation (5) states:

  $$I(z_c; z_c' \mid Y) \approx \log \frac{\exp(\text{sim}(z_c, z_c')/\tau)}{\exp(\text{sim}(z_c, z_c')/\tau) + \sum_{z_c'' \in \mathcal{N}} \exp(\text{sim}(z_c, z_c'')/\tau)},$$

  and the negatives are described as "simply use the current training batch (excluding $z_c'$) as $\mathcal{N}$" — without any conditioning on $Y$ in the negative sampling. The NT-Xent / InfoNCE loss with batch negatives is a known lower bound on *unconditional* mutual information $I(z_c; z_c')$, not $I(z_c; z_c' \mid Y)$. Conditioning on $Y$ would require either supervised contrastive sampling (positives share the same $Y$) or a different formulation. This gap does **not** invalidate the empirical results, because (a) the positive pair is always the same spectrum pre/post-perturbation, and (b) the sufficiency objective simultaneously forces $z_c$ to predict $Y$, so the combined effect may still approximate the intended behavior. Nevertheless, the theoretical justification as written is incorrect, and the authors should either revise the derivation to honestly reflect an unconditional contrastive objective (and justify why it suffices under the SCM) or modify the implementation to truly condition on $Y$.

### Minor
- **No variance or uncertainty reported.** All results are reported as point estimates without standard deviations or confidence intervals. Given the stochasticity from both training (random seed) and the replacement-based intervention, multiple runs would strengthen the reliability of the reported gains. This is a shortcoming in an otherwise thorough empirical section.
- **The purification objective's mechanism is heuristic and lacks formal justification.** The paper argues that maximizing $I(z_s; Y)$ indirectly purifies $z_c$ by drawing overlapping predictive signal into $z_s$ (Section 3.3). While the ablation (Table 4) confirms it works empirically, the reasoning is not formalized with information-theoretic inequalities or a decomposition of the joint mutual information. A more rigorous treatment would strengthen the conceptual contribution.
- **The SCM framing is abstract relative to the downstream application.** The structural equations $X = f(C, S)$ and $Y = g(C)$ (Eq. 2) are standard for causal representation learning but do not specify how $C$ and $S$ map onto concrete properties of the mass spectrum (e.g., whether $C$ encodes fragment ion patterns, intensities, or both). Making this connection more explicit would help readers assess the faithfulness of the SCM to the actual mass spectrometry physics.

### Trivial
- Figure 3 x-axis labels appear truncated/rendered incorrectly ("16, 2, -10" suggests a parsing artifact from the PDF extraction). The text description indicates thresholds 16, 12, 8, 4, 2 as in Figure 1, so the figure itself is likely fine in the original submission.

## Nice-to-Haves
- A brief discussion of failure cases (e.g., very short peptides, high charge states, or spectra with extremely dense noise) would add useful practical depth.
- Direct measurement of the independence property (e.g., computing mutual information between predicted importance scores and noise level during training) would further corroborate the causal claim beyond the indirect vulnerability analysis evidence.
- Including the slightly heavier variant retrained with all 18 ion types (referenced in Appendix Table 12) in the main results would be informative.

## Removed Points
*The following points from the input reviews were removed for the reasons stated:*

- **"Table 1 PointNovo Pep.Prec=0.022 is very low"** → This is a factual observation about PointNovo's documented performance on that dataset, not a weakness of the paper.
- **"Figure 3 x-axis labels are confusing"** → This is a PDF parsing artifact, not an author error.
- **"Missing related works"** → Prohibited by hard rules (cannot verify from external sources).
- **Several formatting/style nitpicks** → Prohibited by hard rules (removed as parser-level issues).
- **"The SCM does not make explicit how C relates to mass spectrum peaks"** → Softened to a minor weakness above rather than a standalone fatal critique; the paper provides structural equations and an intervention design grounded in known ion physics.

## Novel Insights

The most insightful observation from synthesizing the reviews is that the paper's *empirical validation strategy* is actually stronger than its *theoretical packaging*. The vulnerability analysis (Figures 1, 3), NSR generalization (Figure 4), and attention analysis (Table 7) form a coherent chain of evidence that directly demonstrates the mechanism the framework is designed to achieve — reduced reliance on non-causal peaks — independent of whether the contrastive loss label ($I(z_c; z_c' \mid Y)$ vs. $I(z_c; z_c')$) is precisely right. This means the core contribution (a practical, model-agnostic method for causal disentanglement in noisy spectral data) is well-supported even if one corrects the theoretical framing. The paper would be stronger if it leaned into this evidence chain rather than over-claiming the theoretical derivation.

## Suggestions
- **Revise the contrastive loss theoretical justification.** Either (a) drop the conditional $Y$ notation and derive the unconditional InfoNCE bound directly from the independence principle, justifying why invariance across perturbed copies suffices when coupled with the sufficiency loss; or (b) implement a supervised contrastive variant where positive pairs share the same $Y$ (and include it as an ablation).
- **Report variance across multiple seeds** (at least 3 runs) for the main results in Tables 1–3.
- **Add a formal information diagram** showing how $I(z_c; Y)$, $I(z_s; Y)$, and $I(z_c; z_c')$ relate under the decomposition $\mathbf{z} = \mathbf{z}_c + \mathbf{z}_s$, to ground the purification argument.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Three queries targeting score bands: weak anchors (<3.5), middle (3.5–7.5), and strong (>7.5). Retrieved anchors:
- Weak band: All score 3.0 (AvXrppAS2o, yIRtu2FJvY, qi5dkmEE91, vVlNBaiLdN) — rejected papers on biological ML with causal elements. CausalNovo is clearly far stronger.
- Middle band: ReNovo (6.5, Accept), RankNovo (5.5, Reject), Distilling Non-Autoregressive (4.25, Reject), MADGEN (6.0, Accept) — de novo sequencing and related MS papers. CausalNovo is strongest in this cohort empirically.
- Strong band: All score 8.0 (xByvdb3DCm, 3cuJwmPxXj, Nx4PMtJ1ER, k38Th3x4d9) — causal discovery/theory papers of a fundamentally different type. Not directly comparable.

**Round 1 bracket:** 5.5–7.0.

**Round 2 (Narrowing):** Queried inside (5.0, 7.5) focused on robust/denoising peptide sequencing and causal representation learning. Retrieved:
- ReNovo (6.5, Accept) — same task, same benchmarks. CausalNovo shows larger and more consistent empirical gains but has a theoretical gap ReNovo does not. *Comparable overall.*
- RankNovo (5.5, Reject) — CausalNovo is clearly stronger empirically.
- DenoiseVAE (7.0, Accept) — different domain (molecular pre-training). CausalNovo is slightly below this anchor in execution rigor due to the theoretical gap.
- MADGEN (6.0, Accept) — related MS domain. CausalNovo has stronger evidence chain.

**Round 2 positioning:** CausalNovo sits between 6.0 and 6.5, slightly above MADGEN and on par with ReNovo. It is clearly stronger than RankNovo (5.5) but below the 7.0+ threshold due to the verifiable theoretical gap.

**Final score: 6.5.** This is an Accept-level paper with a novel framework, strong empirical validation, and one verifiable but fixable theoretical issue.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>