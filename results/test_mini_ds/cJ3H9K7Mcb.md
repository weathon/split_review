Now I'll compose the final consolidated review.

## Summary

This paper studies how model robustness behaves under different *degrees* of the same type of distribution shift. Through experiments on NoisyMNIST, RotatedMNIST, LowLightCIFAR10, and ImageNet subsets, it demonstrates that (1) models performing well at one shift degree can fail at slightly higher or lower degrees, (2) this pattern is task-dependent (noise vs. rotation), and (3) even large pre-trained models like CLIP can be surprisingly brittle to unfamiliar downstream shifts when adapted via linear probing. The paper does not propose a new method; it argues for more thorough evaluation protocols that cover a range of shift degrees.

## Strengths

- **Concrete quantitative evidence of brittleness (Table 1)**. ERM on CNN drops from 77.8% at D₄ to 47.7% at D₅ (38.7% relative drop) and 26.5% at D₆ (66.0% drop) when models are selected at D₄. These numbers cleanly support the claim that conclusions drawn from a single shift degree can be misleading. The same pattern holds across multiple DG algorithms and architectures.

- **Contrasting task-dependent generalization curves (Figure 3)**. On NoisyMNIST, training on strong shifts improves robustness to all milder shifts. On RotatedMNIST, training on strong rotations *harms* performance at milder rotations. LowLightCIFAR10 falls somewhere between. This finding is non-trivial and challenges the assumption that high-degree robustness transfers downward.

- **GradCAM visualizations provide mechanistic insight (Figure 2, right)**. The paper shows that ERM relies on local pixel features that are corrupted by noise, while CAD uses global structures. This explains *why* the brittleness surfaces as noise intensity increases, connecting quantitative drops to a qualitative difference in learned representations.

- **CLIP brittleness under rare distribution shifts (Figure 4)**. Despite matching randomly-initialized models on clean data, CLIP adapted via linear probing suffers a >40% larger accuracy drop from D₀ to D₁ on NoisyMNIST. This extends the paper's findings beyond small-scale training to large pre-trained models, though only for linear probing.

## Weaknesses

### Fatal
None.

### Major
- **The CLIP finding is established only for linear probing, but the abstract and introduction state it as a general claim about CLIP models.** The abstract (lines 9–10) states "large-scale pre-trained models, such as CLIP, are sensitive to even minute distribution shifts" without qualifying the adaptation strategy. The experiments (Section 5) only evaluate linear probing (line 277). The paper itself includes a `\comment{}` block (lines 310–313) noting that fine-tuning significantly outperforms linear probing on NoisyMNIST, but these results are not in the main paper. The conclusion (line 324) does mention linear probing, but the abstract and intro create a broader impression. This needs to be scoped explicitly in the abstract.

### Minor
- **The paper uses "brittleness" to cover two distinct phenomena without separating them.** Section 4.1 (Figure 2 left) shows *model selection instability* — the best model at D₄ is different from the best model at D₆. Table 1 shows *within-model performance degradation* — the same model (e.g., the best ERM model at D₄) collapses at D₅/D₆. These have different implications: the former suggests evaluation should consider multiple candidate models, the latter that a single model's robustness curve is deceptive. The paper frames both as "brittleness" without distinguishing the two lessons. Separating them would strengthen the evaluation recommendations.

- **The actionable recommendation is vague.** The paper concludes by "encourag[ing] future research to conduct evaluations across a broader range of shift degrees whenever possible" (lines 55, 328). After showing that even a one-step increase in noise can cause collapse, the paper could offer a heuristic: how many degrees to sample, how to space them, or at minimum a suggested protocol. This is a missed opportunity to operationalize the findings.

- **The CLIP experiments use only synthetic distribution shifts (Gaussian noise, rotation, low resolution).** The paper hypothesizes that CLIP's brittleness is due to Gaussian noise being rare in pre-training data (line 295), but this is not verified. While a full investigation is not expected, the datasets remain synthetic — CLIP's behavior on natural distribution shifts of downstream tasks (e.g., texture, background, style shifts) is not tested, which limits the generality of the CLIP finding.

### Trivial
None.

## Nice-to-Haves
- **Show a real analog of Figure 1.** The motivating illustration shows two crossed generalization curves. Picking two real models from the experiments whose curves cross would make the motivating example more concrete.
- **Offer a hypothesis for why rotation behaves differently from noise.** The paper notes the contrast (lines 231–233) but offers no explanation. Even a speculative account (e.g., rotation preserves local pixel patterns while noise destroys them) would add depth.
- **Include at least one DG algorithm in Figure 3.** The paper notes "DG algorithms are helpful but only to a limited extent (see Fig. A.4)" — referencing an appendix that was stripped. Including one DG algorithm in the main figure would strengthen the claim that the pattern generalizes beyond ERM.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Missing hyperparameters (learning rate, batch size, etc.)* — The paper states models are trained "with different initializations and hyperparameters" (line 159). Exact hyperparameters may be in the stripped appendix. Following meta-review instructions, this type of reproducibility nitpick is removed.
- *"Degree ordering underspecified for LowLightCIFAR10"* — The paper defines degrees by the combined effect of brightness and shot-noise intensity, which are correlated in real low-light photography. The ordering is well-defined as an intensity parameter. This criticism is overly speculative.
- *"CLIP Gaussian noise claim not verified"* — The paper explicitly says "We hypothesize" (line 295), not that it's a conclusion. The criticism misreads the paper.
- *"Section 4.2 only shows ERM"* — The paper references an appendix figure (Fig. A.4) for DG algorithm results. The parser strips appendices.
- *"Best model selection from D₀ and D₁ only"* — The paper explicitly states this training regime (line 158) and justifies it (line 147: "Data under strong distribution shifts are usually very rare"). This is a deliberate design choice, not an oversight.
- *"Figure 1 never returned to with real data"* — A nice-to-have improvement, not a weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface observations that the paper itself does not already make.

## Suggestions
1. **Scope the CLIP claim in the abstract.** Replace "CLIP models are sensitive to even minute distribution shifts" with "CLIP models adapted via linear probing are sensitive to even minute distribution shifts." This small change prevents the paper from overclaiming.
2. **Separate the two senses of brittleness.** Add a sentence in Section 4.1 distinguishing model-selection brittleness (Figure 2 left) from within-model brittleness (Table 1), and note what each implies for evaluation design.
3. **Add a concrete evaluation heuristic.** Even a simple rule-of-thumb ("recommend testing at ≥3 degrees spanning the expected severity range, with at least one degree beyond the training distribution") would make the recommendation actionable.
4. **Acknowledge the synthetic-dataset limitation more explicitly in the conclusion.** The paper currently notes this briefly in Section 3 but should restate it in the conclusions to prevent readers from over-extrapolating.

## Score and Decision

**Anchors used:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7LZjuA4AB2.md` (avg 3.00, R1 low) — weaker paper on pre-training & distribution shifts; our paper is clearly stronger
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/64vO8qoJfb.md` (avg 3.00, R1 low) — generic robustness study; our paper has more focused contribution
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RxhOEngX8s.md` (avg 4.25, R1 mid) — OOD detection benchmark with flawed method; our paper is stronger
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VTYg5ykEGS.md` (avg 6.50, R1 mid) — OOD benchmark paper with dataset contribution; our paper has weaker contribution (no new resource)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/w0jk3L3IjV.md` (avg 5.67, R2 narrow) — OOD detection-generalization tradeoff paper; our paper has cleaner findings but no method
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qDFpNXnuYK.md` (avg 5.00, R2 narrow) — empirical study on early training & OOD with marginal results; our paper's findings are stronger and clearer
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AhMEkBSdIV.md` (avg 5.33, R2 narrow) — OOD generalization prediction framework; our paper is comparable but different focus
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oKglS1cFdb.md` (avg 5.67, R2 narrow) — OOD generalization feasibility study; our paper has crisper empirical contributions
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ljwoQ3cvQh.md` (avg 7.00, R2 narrow) — strong empirical+theoretical paper on OOD extrapolation; our paper is weaker (no theory, simpler datasets)
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pEGSdJu52I.md` (avg 6.00, R2 narrow) — empirical+theoretical paper on training variance; our paper has comparable empirical rigor but no theory
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zPHra4V5Mc.md` (avg 7.00, R2 narrow) — theoretical+empirical paper on feature averaging; our paper is less ambitious in scope

**Round 1 Bracket:** [5.0, 6.5]. The paper is clearly above reject-level weak papers (2.6–3.0) and clearly below top papers with method+theory contributions (7.0–9.0).

**Round 2 Narrowing:** Compared against anchors at 5.0–7.0, the paper sits around 5.5. It is stronger than "Early Period of Training" (5.0, Reject) which had marginal improvements and missing baselines. It is comparable to "LCA-on-the-Line" (5.33, Reject) in overall quality. It is weaker than "On the Variance of NN Training" (6.0, Accept) which includes theoretical analysis, and clearly weaker than "Extrapolate Predictably" (7.0, Accept) which covers 8 datasets, includes theory, and provides practical guidance. The paper's main limitation relative to the 6.0+ anchors is the lack of a reusable resource (dataset/method) and reliance on simple synthetic datasets.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>