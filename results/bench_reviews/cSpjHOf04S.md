Here is the final consolidated review.

---

## Summary

This paper proposes gen2seg, a method that fine-tunes generative models (Stable Diffusion and MAE) for category-agnostic instance segmentation using a simple instance coloring loss. Trained on only a narrow set of object types (indoor furnishings and cars from synthetic data), the models exhibit surprising zero-shot generalization to unseen object types and image styles (art, x-rays, fine structures, egocentric scenes), approaching or exceeding SAM on some datasets despite never seeing masks of those categories. The paper argues that generative pretraining encodes an inherent grouping mechanism that transfers across categories and domains.

## Strengths

- **Novel and well-motivated approach**: The core idea of repurposing generative models for instance segmentation via a per-pixel coloring loss (treating segmentation as image-to-image translation) is clean, elegant, and architecturally agnostic. Avoiding task-specific mask predictors and instead keeping the entire generative model as the segmenter is a principled way to preserve the generative prior. (Section 3)

- **Compelling evidence of generalization with limited training diversity**: Table 2 is a highlight of the paper. Fine-tuning on just 10 or even 5 object classes from Hypersim yields nearly the same zero-shot performance as the full dataset (e.g., SD with 10 classes: 56.1 COCO_exc^L vs. 57.6 with full data). This strongly supports the claim that the generative prior, not category diversity, drives generalization.

- **Strong controlled comparison via SimpleClick vs. MAE-B**: The paper provides a clean comparison where both models use the same MAE-B backbone and the same training data. SimpleClick (with a standard ViTDet mask predictor) catastrophically fails (1.4 mIoU on COCO_exc^L), while gen2seg (MAE-B) achieves 44.6. This directly demonstrates that the generative architecture (encoder+decoder) is responsible for the generalization, not the backbone or data. (Table 1)

- **Superior boundary quality**: The paper shows that generative models produce crisper boundaries than SAM (93.4 vs. 79.0 Edge AP on BSDS500), an effect that persists even when fine-tuned on polygonal COCO masks (89.7 Edge AP). This suggests the boundary precision stems from the generative prior itself. (Table 6, Figure 6)

- **Comprehensive ablation suite**: The paper systematically varies training data domain (synthetic Hypersim, real COCO, simple ClevrTex shapes), category diversity (5, 10, or 33+ classes), and model scale (MAE-B, MAE-H, SD). The consistent pattern across ablations bolsters the core claims. (Table 2)

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison in the DINO+VAE baseline limits the claim about discriminative models.** The DINO-B baseline uses a *frozen* VAE decoder (from Stable Diffusion) while MAE fine-tunes its decoder end-to-end. As stated in the paper: "we attach DINO to a frozen VAE decoder" (line 193). This means the DINO baseline cannot adapt its decoder to the segmentation task, while MAE can. Since the VAE decoder itself is generatively pretrained (by Stable Diffusion), the correct controlled experiment would fine-tune the VAE decoder as well (or freeze the MAE decoder). Without this control, the DINO comparison cannot cleanly attribute the gap to the encoder's pretraining paradigm (generative vs. discriminative) rather than decoder flexibility. This weakness primarily affects the claim that "discriminatively pretrained models fail to generalize" — the SimpleClick vs. MAE-B comparison (same backbone, different architecture) is cleaner and independently supports the core thesis about generative architectures.

2. **The paper overclaims that discriminative models "fail to generalize."** The abstract states that "discriminatively pretrained models fail to generalize," but DINO-B achieves 35.0 mIoU on COCO_exc^L (Table 1) — this is far from total failure, though it trails generative models. SimpleClick does fail (1.4 mIoU), but SimpleClick is a promptable segmentation *architecture*, not a discriminatively pretrained model per se. The paper would benefit from more precise language about what exactly fails and why, acknowledging the DINO-B result as partial (not total) failure.

### Minor

3. **Edge detection metric is non-standard.** The paper evaluates BSDS500 using AP only for recall < 20% (Table 6). While the paper states this choice is explained in Appendix B (removed by the parser), standard BSDS500 evaluation uses F-measure at optimal dataset scale (ODS) or optimal image scale (OIS). The narrow recall range favors models with high-precision, sparse edges (which generative models produce) and penalizes models with more comprehensive edge maps. The gap between SD (93.4) and SAM (79.0) may be inflated by this choice. Full precision-recall curves or standard F-measures would allow for clearer comparison with the edge detection literature.

4. **No strong discriminative baseline at larger scale.** The paper tests DINO-B (ViT-B) but omits DINOv2 (which is available in ViT-L/g variants). DINOv2 is the current state-of-the-art discriminative self-supervised model and would provide a stronger test of whether the claimed generalization is truly exclusive to generative models. Given that DINO-B already achieves non-trivial performance (35.0), it remains plausible that a larger discriminative model with comparable decoder fine-tuning would narrow or close the gap.

5. **Small-object analysis is missing.** The paper acknowledges small-object limitations (line 227) and attributes them to pretraining biases, but provides no quantification or breakdown by object size. Table 1 already shows the gap is largest on small objects (COCO_exc^S: SD 8.5 vs. SAM 56.9), but a systematic analysis would strengthen the paper and guide future work.

### Trivial

- The timestep choice t=999 for Stable Diffusion is cited from prior work (Garcia et al., 2024) but is not ablated. A brief ablation would confirm this choice is not critical.
- Training resolution is reported for most models but is not stated consistently for DINO-B.

## Nice-to-Haves

- **Ablate decoder fine-tuning for the DINO baseline**: Compare DINO-B with frozen VAE decoder vs. DINO-B with fine-tuned VAE decoder (or MAE-B with frozen decoder) to disentangle the effect of encoder pretraining from decoder adaptability.
- **Full BSDS500 evaluation with ODS/OIS F-measure**: This would make the edge detection results more comparable to the literature and address concerns about metric selection.
- **Test on more out-of-distribution domains** (e.g., medical or satellite imagery) to probe the limits of the claimed generalization.
- **Analyze failure cases** with breakdown by object size to substantiate the claimed small-object limitation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"DINO+VAE decoder issue is fatal to the paper's core claim"** — This overstates the impact. The core claim is supported by the SimpleClick vs. MAE-B comparison (same backbone, different architecture) and the category-diversity ablations, both of which are clean. The DINO comparison is secondary evidence for the claim about discriminative pretraining specifically, and the confound weakens but does not invalidate that subsidiary claim.
- **"Missing related works (DIFT, Hector)"** — The paper does cite relevant diffusion-for-perception work (Tang et al., 2023; Ke et al., 2024; etc.). The reviewer's suggestion of specific missing citations is not verifiable.
- **Generic or superficial strengths from the Strength Finder** (e.g., "comprehensive evaluation across diverse domains") — This is genuine but already subsumed by the specific cited strengths above.
- **"Training resolution not specified for DINO-B"** — Minor presentation point that does not affect evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the confound in the DINO+VAE baseline and the non-standard edge metric, but neither reviewer identifies a novel pattern or insight about the method that the paper itself does not already articulate. The most interesting unresolved question — why exactly generative representations are more equivariant than discriminative ones — remains an open direction the paper raises but does not fully explain.

## Suggestions

1. **Clean up the DINO baseline**: Run an additional experiment with DINO-B where the VAE decoder is also fine-tuned, or freeze the MAE decoder as a controlled comparison. This would either strengthen or temper the claim about discriminative models and remove the confound.
2. **Add DINOv2-Large with fine-tuned decoder** as an additional discriminative baseline. This would provide a stronger test of the claim that generative pretraining is uniquely suited for this task.
3. **Report standard BSDS500 metrics** (ODS/OIS F-measure) alongside the current AP@recall<20% metric, or show the full precision-recall curves (already promised in the removed appendix).
4. **Tone down the "fail to generalize" language** for discriminative models — DINO-B achieves 35.0 mIoU, which is non-trivial. The paper's story is stronger as "generative models generalize *better*" rather than "discriminative models fail."
5. **Add a breakdown by object size** to quantify the small-object limitation and provide a concrete target for future work.

## Score and Decision

### Calibration Anchors

| Paper (Path) | Avg Human Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/gNgyV2dPAK.md` (Open-Set Domain Generalization for Semantic Segmentation) | 2.80 | Much weaker: combination of common techniques with unclear contribution. gen2seg is far more novel and the empirical results are stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/H8UFAU9gJ2.md` (NOCTIS) | 4.00 | Weaker: incremental combination of off-the-shelf models. gen2seg has a genuinely novel method (instance coloring loss) and cleaner experimental design. |
| `/home/wg25r/review_agent/human_reviews_2026/QVzb9c3VCy.md` (COLER) | 3.50 | Weaker: heuristic improvements on N-cut pipeline. gen2seg's contribution is more novel and the results more striking. |
| `/home/wg25r/review_agent/human_reviews_2026/fEZ6DqfwTR.md` (Training-Free Reference-Based Instance Seg.) | 5.33 | Comparable, but gen2seg has a more original method (not just combining off-the-shelf models) and addresses a more interesting research question about generative priors. |
| `/home/wg25r/review_agent/human_reviews_2026/DYjyFDn8K7.md` (Fine-Tuning Diffusion Models via Intermediate Distribution Shaping) | 3.33 | Weaker: unclear contributions and poorly structured. gen2seg is cleaner and more focused. |
| `/home/wg25r/review_agent/human_reviews_2026/yKC3CaFg8K.md` (GenRep) | 6.00 | Comparable: both papers explore generative models for perception. GenRep has some theoretical concerns about MC approximation; gen2seg has cleaner experiments but a narrower scope. |
| `/home/wg25r/review_agent/human_reviews_2026/oeWqDrTb38.md` (OC-ZSS) | 6.00 | Comparable: both are solid zero-shot segmentation papers with clear contributions and well-designed experiments. OC-ZSS has more comprehensive baselines; gen2seg has a more surprising and interesting finding. |

**Score rationale**: The paper presents a genuinely novel idea (repurposing generative models for instance segmentation via coloring loss) with compelling evidence of cross-category generalization from limited data. The Table 2 ablation is particularly strong. The main weaknesses are (1) a confounded DINO baseline that weakens but does not invalidate the core claim (which is independently supported by the SimpleClick vs. MAE-B comparison), and (2) some overclaiming in the abstract. These are addressable issues. The paper is comparable in quality to accepted poster papers like GenRep (6.00) and OC-ZSS (6.00), and clearly stronger than papers scoring in the 3-4 range.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>