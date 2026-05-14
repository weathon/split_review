Now I have read the paper thoroughly and examined the calibration anchors. Let me write the consolidated review.

## Summary

CausalNovo proposes a causality-informed framework for de novo peptide sequencing, formalizing the task with a Structural Causal Model (SCM) that distinguishes causal signal ions from non-causal noise. It derives two principles — independence (invariance of causal representations under noise intervention) and sufficiency (causal representations retain predictive information) — and implements them via a Causality Extraction Module (CEM) with contrastive and cross-entropy objectives. The framework is model-agnostic and is shown to improve three distinct baselines (CasaNovo, AdaNovo, π‑HelixNovo) across three public datasets at amino acid, peptide, and PTM levels.

## Strengths

- **Principled causal modeling grounded in an SCM.** The paper formalizes de novo sequencing with a Structural Causal Model (Section 3.2) that distinguishes causal factors C from non-causal factors S, yielding two actionable principles (independence and sufficiency) that guide the framework's design. This provides theoretical grounding beyond purely statistical approaches.

- **Consistent and substantial performance gains across multiple baselines and datasets.** CausalNovo improves amino acid precision by +2.4% to +14.2% over three state-of-the-art baselines (CasaNovo, AdaNovo, π‑HelixNovo) on three public datasets (Nine-species, Seven-species, HC-PT) at all evaluation levels (Tables 1 & 2). These gains hold uniformly — every baseline on every dataset shows improvement — and reach relative gains well above 10% on the challenging HC-PT dataset.

- **Thorough ablation and component validation.** Ablation studies (Tables 4 & 5) isolate the contribution of each design element (independence, purification, symmetric training, replace-based intervention), confirming that every component positively contributes. The analysis of peak distinguish strategies (Table 6) with 18 ion types further validates robustness to the peak-identification choice.

- **Cross-species generalizability.** Leave-one-out cross-species experiments (Table 3) demonstrate that CausalNovo improves CasaNovo on all eight species in the Nine-species dataset (average peptide precision gain of +2.6%), showing the framework generalizes to diverse biological sources.

- **Interpretable evidence of causal peak focus.** Attention analysis (Table 7) shows CausalNovo increases the proportion of predictions attending to all three top causal peaks from 19.26% to 32.87%, while decreasing predictions ignoring all causal peaks from 12.73% to 10.76%, providing direct evidence of the intended mechanism.

## Weaknesses

### Fatal
None.

### Major

- **Limited out-of-distribution robustness evaluation.** The central claim that CausalNovo learns "causal representations that generalize" is weakened by the fact that the robustness evaluation (Figures 1, 3, 4) uses the same definition of "noise" (proximity to the theoretical spectrum via Eq. 4) that is used during training. The vulnerability analysis replaces noise peaks with other noise peaks — exactly the perturbation the model was trained to be invariant to. This tests whether the training objective works as intended (which it does), but it does **not** demonstrate generalization to genuinely different noise distributions (e.g., from different instruments, different contamination patterns, or co-eluted peptides from unrelated species). The paper acknowledges this in the conclusion ("a priority for future work"), but this gap substantially limits the strength of the causal generalization claim. Without OOD evaluation under noise from a different generative process, the improvement could partially reflect fitting a label-aware noise statistic rather than discovering causal structure per se.

### Minor

- **The "causal" vs. "non-causal" peak distinction is a domain-knowledge heuristic, not a causally learned distinction.** The identification of causal peaks via proximity to the theoretical spectrum (Eq. 4) is a well-established statistical/matching heuristic from database search, not a causal discovery method. Calling these peaks "causal" is a rhetorical alignment with the SCM framework, but the actual peak-labeling depends on the tolerance threshold γ and the choice of which ion types to include (b, y, a). While the paper tests with 18 ion types and shows similar results (Table 6), it does not analyze the failure modes of this heuristic — e.g., cases where true signal ions fall outside the tolerance window or noise peaks fall inside it, and how gracefully CausalNovo degrades under such mislabeling.

- **Retrained baselines show large gains over original reported numbers.** The retrained baselines († in Table 1) already substantially outperform the original reported results (e.g., CasaNovo AA precision on HC-PT goes from 0.442 to 0.525; AdaNovo from 0.442 to 0.492). The comparison of CausalNovo against retrained baselines is fair and standard, but the paper does not discuss what drives these large retraining gains (better hyperparameters? longer training? different random seeds?). Understanding this could clarify how much of the CausalNovo improvement comes from the causal framework versus better overall training conditions.

- **Modest per-component ablation gains.** Each individual component in the ablation (Tables 4, 5) contributes 1–2% improvement. While the cumulative effect is meaningful, the gains from the independence principle (+1.2%), purification (+0.8%), and symmetric training (+0.4%) are individually small, making it difficult to rule out that simpler alternatives (e.g., a noise-masking baseline that discards identified noise peaks without the contrastive/sufficiency objectives) might achieve similar results.

### Trivial
None.

## Nice-to-Haves
- Evaluate CausalNovo on spectra from a different mass spectrometer or with synthetic contamination (e.g., spiked unrelated peptides) to test robustness to genuinely OOD noise distributions.
- Include a simple baseline that directly masks/discards peaks identified as noise (via the same heuristic) without the contrastive and sufficiency objectives, to isolate the value of the causal machinery.
- Provide concrete case studies with spectra where the baseline errs and CausalNovo corrects it, with attention heatmaps illustrating the mechanism.
- Discuss failure cases of the peak-distinction heuristic (Eq. 4) and whether CausalNovo degrades gracefully when the heuristic mislabels peaks.

## Removed Points
- **"Circular evaluation" characterization**: The critic claimed the evaluation is "circular" because the same heuristic identifies noise peaks in both training and evaluation. This overstates the issue — testing whether a model achieves invariance to the specific perturbation it was trained against is standard practice (analogous to testing robustness to the data augmentation used during training). The evaluation tests whether the training objective works, which is a valid test. The real concern is about limited OOD scope, not circularity. This point is subsumed under the first Major weakness above.
- **"Doesn't acknowledge other ion types"**: The paper directly addresses this in Section 4.4 ("Analysis of Peak Distinguish Strategies"), testing with 18 ion types (Table 6). Removed as factually incorrect.
- **"'Up to 10%' claim is about noise-sensitive evaluation"**: Checking Tables 1 and 2, the 10%+ relative improvements are also observed on standard (non-perturbed) evaluation (e.g., HC-PT: π-HelixNovo + CausalNovo achieves +12.4% relative AA precision improvement over retrained baseline). Removed as factually incorrect.
- **"SCM assumption that S only affects X"**: The SCM is a modeling choice explicitly stated. The critic acknowledges it is "plausible." This is not a weakness.
- **Pure formatting/style nitpicks**: Removed per instructions.
- **Missing appendix content**: Removed per instructions (parser artifact).

## Novel Insights
The reviews surface a substantive tension: CausalNovo has genuinely strong and consistent empirical performance across standard benchmarks, with a clean theoretical framework and thorough ablations — yet the headline claim about learning "causal representations that generalize" rests on a robustness evaluation that tests the same noise definition used during training. This pattern (strong in-distribution and same-distribution results, limited OOD validation) is common across papers adapting causal machinery to noisy biological domains. The paper's own acknowledgment of the limitation is commendable, but it also means the core causal claim is not fully proven here. The most valuable next step would be an OOD experiment (e.g., transferring across instruments or contamination regimes) that would either validate or bound the claim.

## Suggestions
- Add an experiment testing CausalNovo on spectra from a different instrument type or with real-world contamination (e.g., co-eluted peptides from a different species). Even a small-scale experiment would significantly strengthen the causal generalization claim.
- Include a baseline that simply zeros out or masks peaks identified as noise (using the same heuristic) before feeding to the baseline model. If this achieves similar gains to CausalNovo, it would suggest the causal machinery is unnecessary; if not, it would strengthen the paper's case.
- Discuss what happens when the theoretical-spectrum heuristic (Eq. 4) misclassifies peaks — i.e., true signal ions missed or noise peaks incorrectly labeled as signal — and whether CausalNovo degrades gracefully under such errors.

## Score and Decision

**Calibration anchors used (from batch retrieval):**

| Path | Avg Score | Comparison to CausalNovo |
|------|-----------|--------------------------|
| PeakNovo (0oqEBQA0UD) | 3.50 | Weaker: lacks theoretical framework, has fundamental issue with external DB dependency; CausalNovo is stronger on theory and experiments |
| PLMNovo (EKjt05WxMI) | 2.50 | Much weaker: negligible improvements, questionable motivation; CausalNovo has much larger and consistent gains |
| Pep2Prob (A5MPzwyq0H) | 3.50 | Different contribution (fragmentation prediction benchmark vs. sequencing method); CausalNovo has broader experimental validation |
| Causality-Inspired Robustness (kvzW81UtyH) | 4.50 | Weaker: limited experiments, weak empirical validation; CausalNovo has more thorough evaluation |
| Latent-Space Denoising for CRL (TfXpGqBNAQ) | 4.50 | Similar level: both have principled frameworks but limited empirical scope; CausalNovo has more extensive experiments |
| Causal Delta Embeddings (5d7prMWHNF) | 6.00 | Stronger: has OOD evaluation, cleaner causal theory; CausalNovo has more extensive experiments but weaker OOD evidence |
| PepBenchmark (NskQgtSdll) | 6.00 | Different contribution (benchmark vs. method); not directly comparable |

**Assessment**: CausalNovo presents a well-motivated framework with strong empirical results across multiple baselines, datasets, and evaluation levels. The ablation studies are thorough, and the cross-species validation is convincing. The primary limitation is that the central claim about "causal generalization" is not fully validated by the robustness evaluation, which tests the same noise definition used during training. The paper acknowledges this limitation. Relative to the anchors, CausalNovo is stronger than rejected papers in the same domain (3.5–4.5) but falls short of the stronger accepted causal ML papers (6.0) due to the OOD evaluation gap.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>