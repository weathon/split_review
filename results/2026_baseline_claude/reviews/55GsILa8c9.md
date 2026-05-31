Now I have enough content to write a thorough review. Let me compose it.

---

## Summary

CausalNovo is a model-agnostic causal-inference framework for *de novo* peptide sequencing from tandem mass spectra. It formalizes the task through a Structural Causal Model (SCM) grounded in Reichenbach's Common Cause Principle, derives two learning principles (independence and sufficiency), and instantiates them via a Causality Extraction Module (CEM) that disentangles causal signal-fragment representations from spurious noise-peak representations in latent space. Applied on top of three strong baselines (CasaNovo, AdaNovo, π-HelixNovo) and evaluated on three public benchmarks, CausalNovo delivers consistent improvements of up to ~14% in amino-acid, peptide, and PTM-level metrics and demonstrably reduces model reliance on non-causal peaks.

---

## Strengths

- **Well-motivated problem with empirical evidence.** Figure 1 is a compelling "smoking gun": simply replacing noise peaks in a well-trained model drops amino-acid precision by up to ~15%, and the drop grows as the m/z tolerance tightens. This concretely justifies the causal motivation before any methodology is introduced.
- **Principled SCM formulation.** Using RCCP to derive C ⊥ S and Y = g(C) is elegant; it cleanly maps to the independence and sufficiency objectives and gives the method a coherent theoretical backbone rather than just an ad-hoc regularization.
- **Model-agnosticism with consistent gains.** CausalNovo is verified on three architecturally distinct baselines across three datasets and three evaluation granularities (AA, peptide, PTM). The fact that improvements are positive in every single cell of Tables 1–3 is strong evidence against cherry-picking.
- **Comprehensive ablation.** Table 4 (component ablation) and Table 5 (intervention design ablation) isolate each design choice. The attention analysis (Table 7) provides mechanistic evidence: the fraction of predictions where the model attends to 3 causal peaks nearly doubles (19% → 33%), directly supporting the causal grounding story.
- **Negligible inference overhead.** The framework adds <1% inference cost, making deployment practical; the only real cost is training time (2.3×).

---

## Weaknesses

### Fatal
None.

### Major

1. **The "causal" identification of peaks is supervised by ground-truth labels.** The non-causal ions are localized using the theoretical spectrum derived from the ground-truth peptide sequence (Eq. 4). This means the independence objective and causal intervention are both conditioned on knowing Y, collapsing the framework to domain-knowledge-guided regularization (focus on b/y/a ions, ignore the rest) rather than causal discovery in the strict sense. This is not wrong as an engineering choice, but the paper frames it as a general causal framework while the actual mechanism is closer to "use the theoretical spectrum as a teacher signal." Acknowledging this distinction more explicitly would sharpen the scientific contribution claim.

2. **The mutual information–cross-entropy equivalence is stated too loosely.** Section 3.4.2 asserts "Maximizing mutual information is equivalent to minimizing cross-entropy loss," citing Boudiaf et al. This equivalence holds only in the limit of infinite model capacity and is an upper-bound approximation in practice. The same approximation is applied to both I(z_c; Y) and I(z_s; Y). Because the decoder ρ has finite capacity and z_s is a masked-out complement of z_c, applying the same CE loss to z_s can cause the model to smuggle label-predictive information into the "non-causal" pathway, partially defeating the purification goal. The paper acknowledges this qualitatively (Section 3.3) but does not measure or bound the information leakage empirically.

3. **Missing comparisons under the same protocol.** ContraNovo, RankNovo, and π-PrimeNovo are mentioned in Related Work but excluded from Tables 1–2 because they use a different, more realistic training protocol (large external corpora + OOD test sets). This exclusion is disclosed and the paper commits to this as future work, which is appropriate. However, since SearchNovo is included and it also extends beyond vanilla supervised training, it would strengthen the paper to at least situate CausalNovo relative to ContraNovo/RankNovo with a qualitative discussion of why the protocol difference makes comparison infeasible here.

### Minor

1. **Vulnerability evaluation creates a favorable test condition for CausalNovo.** The "vulnerability evaluation" (Figures 1, 3; Table 6) replaces noise peaks, which is exactly the transformation used during CausalNovo's training. It is not surprising that a model trained with noise-peak replacement is more robust to noise-peak replacement at test time. A genuinely adversarial evaluation—e.g., replacing causal peaks, adding synthetic noise with a different distribution, or testing on real spectra with measured contamination—would provide stronger evidence of causal invariance beyond domain-matched augmentation.

2. **Sensitivity of the CEM architecture is unreported.** The CEM uses 3 Transformer layers followed by an MLP head, but no ablation on the number of layers or the head design is provided. For a module that computes a continuous importance mask M over peaks, even layer count can matter considerably.

3. **NSR distribution in test sets is not analyzed.** Figure 4 shows per-NSR improvements but does not report the NSR histogram of the test set. If most spectra fall in the low-NSR regime, aggregate metric gains may be driven by factors other than noise robustness.

### Trivial

- Table 4 appears to have duplicate checkmark columns due to parser formatting; the content is readable but the visual presentation is confusing.

---

## Nice-to-Haves

- Evaluating CausalNovo under the ContraNovo/RankNovo protocol (large corpora + OOD test) would significantly broaden the impact claim.
- A dedicated experiment replacing or corrupting causal peaks (rather than noise peaks) would establish a tighter negative control.
- Reporting per-sample or per-species NSR statistics alongside the NSR generalization analysis would help readers interpret Figure 4.

---

## Novel Insights

The most genuinely novel insight in CausalNovo is the attention-attribution analysis (Table 7): after training with the causal framework, the distribution of model attention over signal vs. noise peaks shifts dramatically—from 19% of predictions fully attending to causal peaks to 33%. Combined with the finding (Appendix Table 14) that for error-to-correct transitions the fraction of predictions with zero causal-peak attention drops from 14% to 5%, the paper establishes a mechanistic causal story that goes beyond aggregate metrics. This is a concrete, measurable, and underreported property of how causal regularization actually changes model behavior at the representation level, and it offers a template for auditing spurious-correlation reliance in other spectrum-to-sequence tasks in computational biology.

---

## Suggestions

- Add an experiment replacing/corrupting signal (causal) peaks to establish a proper negative control alongside the noise-peak perturbation results.
- Quantify the information leakage into z_s empirically (e.g., measure I(z_s; Y) with a linear probe after training) to validate the purification claim.
- Include a CEM depth ablation (1 vs. 3 vs. 5 Transformer layers) to help future users configure the module.
- Provide a brief qualitative comparison with ContraNovo/RankNovo protocols to clarify scope.
- Clarify the relationship between the causal framing and domain-knowledge-based signal/noise separation more explicitly, to avoid overstating the generality of causal discovery.

---

## Score and Decision

The paper tackles a real and practically important problem in computational proteomics, motivates it rigorously, and delivers consistent, reproducible improvements across three datasets and three baselines. The causal framing is principled even if its operationalization is partly supervised by ground-truth labels, and the attention-attribution analysis provides genuine mechanistic insight. The major weaknesses (supervised peak identification vs. causal discovery, loose MI–CE equivalence, favorable test conditions) are real but do not invalidate the core empirical contribution. The 2.3× training overhead and the inability to compare with the most recent training protocol are acknowledged honestly. This is a solid paper with a clear contribution to a niche but growing area.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>