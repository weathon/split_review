Here is my consolidated review after carefully verifying each claim against the paper text.

---

## Summary

This paper identifies and systematically studies intra-modal misalignment in CLIP-style models — the phenomenon where image-image or text-text similarities from frozen encoders are poorly calibrated despite strong inter-modal (image-text) alignment. The authors propose using optimization-based modality inversion (OTI for image→text, OVI for text→image) to convert intra-modal retrieval tasks into inter-modal ones, yielding consistent gains across 15 image retrieval datasets and 5 model variants. Multiple control experiments (zero-shot classification reversal, SLIP analysis, modality gap manipulation, drift analysis) provide convergent causal evidence that the improvement stems from exploiting CLIP's inter-modal alignment rather than from the inversion process itself.

## Strengths

- **Controlled quantification of the problem (Section 2).** The "Dogs vs Cats" filtering experiment cleanly isolates intra-modal misalignment: after ensuring perfect inter-modal alignment, image-to-image mAP is only 81.4% and R-Precision 71.5%, directly showing the issue even in a simple two-class setup. This is a concrete, reproducible demonstration.

- **Consistent improvement across 15 datasets × 5 models (Table 1).** Image-to-image retrieval with OTI-inverted features outperforms intra-modal baselines across all 15 datasets and all 5 models tested (OpenAI CLIP B/32, L/14; OpenCLIP B/32, L/14; SigLIP B/16). The inclusion of SigLIP shows the finding extends beyond the softmax contrastive loss to sigmoid-based training.

- **Elegant causal control via zero-shot classification reversal (Table 2 right).** Applying the same OTI process to the inherently inter-modal task of zero-shot classification *decreases* accuracy. This symmetric experiment rules out the concern that modality inversion universally improves features — the benefit is specific to converting intra-modal tasks to inter-modal ones, directly supporting the paper's central claim.

- **Causal evidence through pre-training intervention (Tables 3 & 4).** SLIP (which adds an intra-modal SimCLR loss during pre-training) reduces OTI's advantage, and fine-tuning to close the modality gap (high temperature) eliminates it. These experiments provide converging causal support that intra-modal misalignment originates from the contrastive training objective and the resulting modality gap.

- **Inversion dynamics analysis (Section 6.4, Figure 3c).** The paper shows that OTI features (R=1, 150 steps) have similarity statistics closer to text-image pairs than to image-image pairs, confirming they remain in the text manifold. The drift analysis (as loss→0, performance reverts to baseline) further strengthens the mechanistic explanation.

## Weaknesses

### Fatal
None.

### Major

- **Missing a direct control: simpler inter-modal mapping.** The paper claims the performance gain "stems from inter-modal alignment and not the modality inversion process itself" (Section 1), yet the only method tested for obtaining inter-modal features is the specific iterative optimization (OTI/OVI). A direct control would compare against a simpler single-step mapping — e.g., a linear projection from image→text embedding space trained on a held-out set of image-caption pairs and applied per query at test time. If such a linear mapping also outperforms the intra-modal baseline, the claim about inter-modal representations being superior (independent of the inversion method) is strongly confirmed. If it does not, then the iterative, token-level optimization may be a necessary component. The existing evidence (zero-shot reversal, drift analysis, SLIP, modality gap) is convergent and convincing, but it does not fully exclude the possibility that properties of the optimization process (beyond crossing the modality gap) contribute to the gains. Adding this control would substantially strengthen the paper's central causal claim.

### Minor

- **OVI evaluation is thin with marginal gains.** Text-to-text retrieval (Table 2 left) covers only 4 datasets, and several gains are very small (e.g., ~0.05 mAP on Flickr30K). The paper itself notes that text-to-text is not a typical CLIP use case. No variance or significance measures are reported, so it is unclear whether these tiny margins are meaningful. A more discriminating evaluation (e.g., non-caption text pairs where the intra-modal baseline is further from ceiling) would strengthen the generality claim.

- **No variance reporting anywhere.** Optimization with random initialization (OTI/OVI), model fine-tuning (modality gap experiment), and pre-training variants (SLIP) all involve stochastic components, yet the paper reports only single-run point estimates. Error bars or multiple-run statistics would give confidence that the reported improvements are not artifacts of initialization, especially for the smaller-margin cases.

- **Template sentence not ablated.** OTI uses "a photo of" as the fixed template (Section 5.1). Since the template contributes to the text-side representation during inversion, the sensitivity of results to this choice is not explored. A brief ablation (or justification) would improve rigor.

### Trivial
None.

## Nice-to-Haves

- The linear projection control experiment (described under Major) as a way to further nail down the source of improvement.
- Reporting variance over multiple OTI/OVI runs (e.g., 3–5 seeds).
- Evaluating OVI on non-caption text pairs where the intra-modal baseline is not near-ceiling.
- Ablation of alternative template sentences for OTI.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

- **"Missing comparison to other single-feature inversion methods"** — The paper already systematically compares different numbers of pseudo-word tokens (R=1, 2, 4, 8) in Section 6.4 (Figures 3a–b), which covers this comparison.
- **"OVI interpolation scheme is unclear"** — The paper provides a detailed mathematical description of the nearest-neighbor interpolation with the expansion formula (Section 5.2), which is sufficiently clear for reproduction.
- **"Code release not mentioned"** — This is a reproducibility nitpick; the primary review guidelines instruct not to penalize for format/reproducibility items of this type. If code is a concern, it would be addressed post-acceptance.
- **"Missing related works"** — Cannot be verified without external sources.
- **Claims about appendix/proof being missing** — The parser strips appendices; they exist in the original submission.
- **Pure formatting/style nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key synthesis from the reviews is that the paper's evidence is strongest on the image-to-image retrieval front (15 datasets, consistent gains, multiple models) and somewhat thinner on text-to-text retrieval, but the control experiments (zero-shot reversal, SLIP, modality gap) form a coherent causal chain that meaningfully advances understanding of why intra-modal CLIP features are suboptimal.

## Suggestions

1. Add a linear-projection inter-modal mapping baseline (trained on COCO train or similar) for image-to-image retrieval. This directly tests whether inter-modal *representations* (not the specific optimization) drive the improvement.
2. Report variance (at least min/max or std over 3 runs) for the main OTI and OVI experiments, particularly where margins are small.
3. Consider evaluating OVI on a text retrieval task with captions from non-VLM domains where the intra-modal baseline is weaker, making the comparison more discriminating.
4. Briefly ablate or justify the "a photo of" template choice for OTI.

## Score and Decision

The paper makes a well-motivated, clearly argued, and empirically substantial contribution. The central observation — that CLIP intra-modal features are systematically suboptimal and that converting to inter-modal representations helps — is convincingly demonstrated across a wide evaluation. The control experiments are clever and rule out the most obvious confounds. The weaknesses identified are about strengthening already-supported claims, not about fundamental flaws. The paper is honest about its computational limitations and does not over-claim practical utility.

My final decision is to **Accept**. The paper would benefit from the suggested additions, particularly the linear-projection control, but the contribution stands on its existing evidence.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>