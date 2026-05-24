Now I have a solid understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

CausalNovo is a model-agnostic training framework for de novo peptide sequencing that aims to make models robust to noise by focusing on signal (causal) fragment ions rather than spurious noise peaks. It introduces a Causality Extraction Module (CEM) that splits latent representations into causal and non-causal components, and trains with three objectives: a contrastive loss for independence from noise, a cross-entropy loss on causal representations for sufficiency, and a cross-entropy loss on non-causal representations for purification. Noise peaks are identified using the theoretical spectrum derived from ground-truth labels and are replaced during training as a form of data augmentation. Experiments across three baselines (CasaNovo, AdaNovo, π-HelixNovo), three datasets, and multiple metrics show consistent improvements, with strong robustness demonstrated under noise perturbations and varying noise-signal ratios.

## Strengths

- **Comprehensive and consistent empirical validation across diverse settings.** The method is tested on three different baseline architectures (CasaNovo, AdaNovo, π-HelixNovo), three public benchmark datasets (Nine-species, Seven-species, HC-PT), and evaluated at amino acid, peptide, and PTM levels. Gains are consistent across all combinations (e.g., +2.4% to +14.2% amino acid precision), providing strong evidence that the framework genuinely improves performance rather than fitting to one particular model or dataset (Tables 1–2).

- **Convincing robustness evidence through vulnerability analysis and NSR evaluation.** When non-causal noise peaks are systematically replaced, baseline models degrade sharply while CausalNovo retains significantly higher precision, with relative improvements up to 15.7% (Figures 1, 3). Similarly, CausalNovo maintains higher precision across varying Noise Signal Ratios (Figure 4). These analyses directly test the paper's core claim—that the method reduces reliance on spurious noise correlations.

- **Attention analysis confirms the mechanism works as intended.** Table 7 shows that CausalNovo substantially increases the fraction of predictions that fully attend to all three causal peaks (19.26% → 32.87%) and reduces predictions that ignore causal peaks entirely (12.73% → 10.76%). Analysis of error-correction cases (Appendix Table 14) further shows a drop from 14.18% to 5.44% in ignoring causal peaks on corrected predictions.

- **Incremental ablation studies isolate contributions.** Table 4 shows that independence, purification, and symmetric contrast each add incremental value beyond the baseline. Table 5 shows that the replace-based perturbation improves over baseline and that the enhance (theoretical spectrum injection) further helps. These ablations give a reasonably clear picture of which components matter.

- **Cross-species generalization supports the invariance claim.** Leave-one-out cross-species validation (Table 3) shows consistent gains averaging +2.6% peptide precision across all eight held-out species, supporting the claim that the learned representations transfer across domains.

## Weaknesses

### Fatal

None. The method produces genuine empirical improvements that are well-supported by the evidence presented.

### Major

- **The causal SCM framing is physically inaccurate and not genuinely causal.** The paper constructs an SCM where "causal factors" C act as a common cause of both the spectrum X and the peptide Y (Eq. 2, Figure 2A), with X = f(C,S) and Y = g(C). In the actual physical process of mass spectrometry, the peptide Y is fragmented and its fragment ions are measured as X—so Y is a cause of X, not a co-effect of a shared latent C. The "causal intervention" (Section 3.4.1) is not an intervention in any causal model but is simply a data augmentation pipeline that uses the ground-truth label Y to identify noise peaks (via the theoretical spectrum) and replace them. The paper's claim to be doing "causal representation learning" substantially overstates what is actually a supervised, domain-informed training strategy. The practical method—using label-derived signal-peak information for noise-robust training—is sound and effective, but it does not require or justify the causal SCM that the paper builds its theoretical narrative around. The paper would be stronger if it presented the SCM as a loose conceptual analogy rather than claiming it as a formal causal model of the data-generating process.

- **No capacity-controlled baseline to isolate the causal mechanism.** CausalNovo adds a Causality Extraction Module with 3 Transformer layers (a ~33% parameter increase over the 9-layer baseline encoder) plus multiple new training signals (contrastive loss, purification loss, data augmentation). The ablation studies in Tables 4–5 show incremental value from each component, but they do not include a baseline that matches CausalNovo's parameter count and data augmentation without the causal objectives—e.g., a CasaNovo variant with an equivalent 3 extra Transformer layers and the same replace+enhance augmentation but trained only with standard cross-entropy. Without this control, some fraction of the observed gains could be attributed to additional model capacity rather than the causality-inspired design. The robustness analyses (Figures 1, 3, 4) provide converging evidence that the mechanism works, but a capacity-controlled baseline would substantially strengthen the causal claim.

### Minor

- **Key hyperparameters α (fraction of replaced noise peaks) and γ (m/z tolerance for noise identification) are not reported in the main text.** These appear only as symbols in Eq. (4) and the description of the replace-based perturbation (Section 3.4.1) without concrete values, which impedes reproducibility. The specific replacement values used in the vulnerability perturbation experiments are also not described.

- **No variance estimates or significance tests for any results.** Tables 1–7 report single-point estimates without standard deviations, confidence intervals, or statistical tests. Given the magnitude of some reported gains (e.g., +0.6% from the replace intervention in Table 5), it is difficult to assess whether differences are meaningful or within run-to-run variation. This is a common limitation in the peptide sequencing literature (several baselines also report single-point results), but the paper should still provide variance estimates given the number of claims made.

- **The attention analysis (Table 7) has a mild circularity concern.** "Causal peaks" are defined by proximity to the theoretical spectrum—the same criterion used to construct the training supervision signal. It is therefore not surprising that the model trained to focus on these exact peaks does so more after training. The analysis still shows the mechanism is working, but the interpretation should acknowledge this circularity.

### Trivial

- The paper reports a ~2.3× training time overhead; a wall-clock comparison would be useful context for practitioners weighing the cost-benefit tradeoff.
- The perturbation protocol details (what values are substituted for noise peaks in the vulnerability experiments, and whether the same m/z tolerance is reused from training) could be described more explicitly.

## Nice-to-Haves

- A comparison against a baseline that concatenates a binary mask of theoretical peaks to the spectrum input (or uses the theoretical spectrum as an auxiliary reconstruction target) without the contrastive and purification losses. This would help isolate whether the loss design specifically, rather than just additional domain knowledge, drives the gains.
- A discussion of how the framework behaves when the ground-truth-based noise identification is imperfect (e.g., when theoretical spectrum coverage is incomplete due to uncommon ion types or PTMs).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The causal model is physically mis-specified and therefore the paper's central thesis is unsupported" (from Harsh Critic, framed as fatal):** While the SCM framing is loose and the paper oversells the causal angle (retained as a Major weakness), the practical method is well-motivated and the empirical evidence for its effectiveness is strong. The core contribution—a domain-informed training strategy that makes models noise-robust—is supported by the experiments. The SCM issue downgrades the theoretical contribution but does not invalidate the empirical one.

- **"The retraining alone yields large differences from originally published numbers, which is a red flag about hyperparameter sensitivity" (from Harsh Critic):** The paper transparently reports both original and retrained numbers. Retraining differences are common across ML papers and do not indicate a problem—the retrained baseline is the appropriate comparison point since CausalNovo builds on it. The retrained numbers for π-HelixNovo are very close to the originals, and for CasaNovo they are higher than originals (suggesting the retraining is well-tuned, not under-tuned).

- **"The comparison with SearchNovo uses numbers from NovoBench that were not obtained under the same retraining setup" (from Harsh Critic):** The paper clearly marks which numbers are retrained (†) and which are from NovoBench. Retraining all methods under identical conditions would be ideal but is impractical for a paper that already retrains three baselines. The paper compares fairly against its own retrained baselines and reports NovoBench numbers for broader context.

- **"These issues cannot be repaired by simply adding experiments; the framing and core argument need to be rethought" (from Harsh Critic):** This overstates the problem. The paper can be strengthened by reframing the causal narrative as a conceptual motivation rather than a formal model, and by adding a capacity-controlled baseline—both addressable revisions.

- **Strength Finder claim about "model-agnostic, causality-driven improvement":** Retained but reframed without the "causality-driven" language, since the causal mechanism is not isolated. The model-agnostic nature of the improvement is a genuine strength.

- **"The purification objective is given only a hand-wavy justification" (from Harsh Critic, removed as a separate weakness):** The justification—maximizing I(z_s; Y) indirectly purifies z_c by pushing predictive information through the causal branch—is brief but logically coherent and grounded in prior work (Chen et al., 2022). Merged into the broader concern about theoretical looseness.

- **"No standard deviations or significance tests are reported for any result, making it impossible to judge whether differences are meaningful" (from Harsh Critic):** Retained as a Minor weakness. However, the claim that this makes it "impossible to judge" is overstated—the consistency across three baselines, three datasets, and multiple metrics provides cross-validation that single-run variance cannot easily explain away.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface genuinely novel observations that the paper itself does not already contain.

## Suggestions

- **Reframe the causal narrative.** Present the SCM as a conceptual motivation or loose analogy rather than as a formal causal model of the data-generating process. The method's actual contribution—using label-derived theoretical spectra to identify noise peaks and training with contrastive invariance objectives—stands on its own without requiring the SCM to be physically accurate. A reframing like "supervised peak-attention training" or "theoretical-spectrum-guided contrastive learning" would be more honest and no less compelling.

- **Add a capacity-controlled baseline.** Train a CasaNovo variant with an equivalent 3 extra Transformer layers in the encoder and the same replace+enhance data augmentation, but using only standard cross-entropy loss (no contrastive or purification objectives). This would isolate how much of the gain comes from the specific loss design versus extra capacity and data augmentation.

- **Report α, γ, and include variance estimates** (standard deviations across at least 3 seeds for key results in Tables 1, 4, and 5).

- **Acknowledge the mild circularity in the attention analysis** and consider a complementary analysis using an orthogonal definition of signal peaks (e.g., from an independent database search tool rather than the theoretical spectrum).

## Score and Decision

**Calibration anchors considered across rounds:**

*Round 1 (bracketing):*
- AvXrppAS2o (score 3.00): Causal structure learning for outcome prediction — much weaker, rejected.
- TRHyAnInUC (score 3.25): Causal discovery with diffusion models — much weaker, rejected.
- Q0s6kgrUMr (score 6.67): Robust causal/anticausal relation discovery — theoretical contribution, accepted. CausalNovo has weaker theory but stronger empirical validation.
- 7oT1X8xjIk (score 5.80): Identifiability of nonlinear representation learning — rejected, more theoretical. CausalNovo has stronger empirical results.
- 3cuJwmPxXj (score 8.00): Identifying representations for intervention extrapolation — accepted, rigorous theory + experiments. CausalNovo has less theoretical rigor.

*Round 2 (narrowing):*
- uQnvYP7yX9 (ReNovo, score 6.50): De novo peptide sequencing with retrieval — accepted, same domain. CausalNovo has more comprehensive experiments (3 baselines, better ablations, more analysis dimensions) and is model-agnostic, but shares similar concerns about theoretical framing and missing controls. CausalNovo is slightly stronger.
- ym7pr83XQr (DenoiseVAE, score 7.00): Learnable noise distributions for molecular pre-training — accepted. Comparable in having some theoretical looseness with strong empirical validation. DenoiseVAE's theory is cleaner; CausalNovo's empirical validation is more thorough.
- MADGEN (score 6.00): Mass-spec molecular generation — accepted, clearly weaker than CausalNovo in comprehensiveness and evaluation quality.

**Bracket:** Round 1 placed the paper between 5.80 and 8.00. Round 2 narrowed this to 6.50–7.00, with ReNovo (6.50) as a close lower bound and DenoiseVAE (7.00) as a close upper bound.

CausalNovo is stronger than ReNovo due to more comprehensive experiments (3× baselines, more analysis dimensions, model-agnostic), but shares the theoretical looseness concern. It is comparable to DenoiseVAE in overall contribution quality—DenoiseVAE has a cleaner theoretical motivation (VAE), CausalNovo has more thorough empirical validation. The paper falls slightly below the 8.0 causal theory papers that provide rigorous identifiability results. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>