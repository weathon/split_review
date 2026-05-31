## Summary

Gen2Seg introduces a finetuning method that repurposes pretrained generative models (Stable Diffusion 2 and MAE) for category-agnostic instance segmentation. The core idea is to treat instance segmentation as image-to-image translation and train with a novel instance coloring loss exclusively on a narrow synthetic domain (indoor furnishings and cars), then demonstrate strong zero-shot generalization to unseen object categories and image styles. The paper argues that generative pretraining inherently encodes equivariant, boundary-aware representations that discriminative pretraining fails to produce.

## Strengths

- **Clean causal ablation isolating generative pretraining**: The comparison of MAE-B vs. DINO-B under identical finetuning conditions (same loss, same limited data) is the strongest evidence for the core claim. MAE-B achieves 44.6 mIoU vs. DINO-B's 35.0 on COCO_exc^L and 28.9 vs. 14.8 on EgoHOS, directly attributing the improvement to the generative prior rather than architecture or data.

- **Edge detection corroborates the core hypothesis**: The BSDS500 evaluation independently validates that generative models learn fine boundary representations. SD achieves 93.4 edge AP vs. SAM's 79.0, and crucially, even when finetuned on noisy polygonal-edged COCO annotations, SD (COCO) still reaches 89.7—roughly 11 points above SAM—demonstrating that the boundary quality comes from pretraining, not annotation format.

- **Thoroughness of domain diversity ablations**: Table 2 is genuinely informative. The 5-class experiment (books, chairs, lamps, tables, pillows) achieving non-trivial zero-shot generalization, and the minimal gap between 10-class and 33+-class training, provide concrete evidence that the generalization arises from the generative prior rather than finetuning data coverage.

- **Compelling resource asymmetry**: The SD model achieves performance near SAM's on large objects (57.6 vs. 57.0) while trained on 4 GPUs with 3.7M masks of a narrow domain, vs. SAM's 256 A100s and 1.1B masks of diverse categories. This is a practical insight for the community about leveraging generative pretraining.

- **Principled loss design**: The instance coloring loss avoids color permutation ambiguity through a variance/separation formulation that is architecture-agnostic and supports direct evaluation of raw learned features without a specialized mask decoder, making the feature quality claim cleaner.

## Weaknesses

### Fatal
None.

### Major

- **Small-object performance gap is severe**: On COCO_exc^S, gen2seg SD achieves 8.5 mIoU vs. SAM's 56.9—a 48-point gap. The paper attributes this to resolution (480×640 vs. 1024×1024) and pretraining biases, which is plausible, but the gap is large enough to limit practical applicability. No experiment investigates whether simply increasing resolution during finetuning would recover a significant fraction of this performance, making it unclear whether the limitation is architectural or fixable.

- **Promptable segmentation decoder is not comparable to SAM's**: The simple color-distance thresholding with bilateral filter is intentionally lightweight to "showcase raw feature quality," but it conflates two distinct things: feature quality and the prompting mechanism quality. SAM's mask decoder is learned and designed for multi-scale upsampling. The mIoU comparison in Table 1 bundles both effects. Showing a comparison where only SAM's decoder is swapped for the same simple prompting mechanism—or providing a lightweight learned decoder for a more apples-to-apples comparison—would strengthen or weaken the feature quality claim considerably.

### Minor

- **Qualitative part-compositionality claim lacks quantitative support**: Figure 3's demonstration of hierarchical part grouping is compelling anecdotally but is not quantified. Without a benchmark or metric for part-level grouping, the claim that "generative models learn hierarchical scene representations" remains illustrative only.

- **SAM2 is mentioned but not included as a baseline**: SAM2 is cited as SAM's "recent successor" but not evaluated. Given that SAM2 improves on SAM significantly, its omission makes the high-water mark comparison potentially outdated.

### Trivial

- The Gaussian weighting standard deviation for the query vector ($0.01 \cdot (W, H)$) is stated but not ablated. Given the simple nature of the prompting mechanism, a brief sensitivity analysis would be reassuring.

## Nice-to-Haves

- An experiment varying inference resolution (e.g., finetuning SD at 1024×1024) specifically targeting the small-object gap would clarify whether the limitation is fundamental or easily closed.
- A light learned projection head on top of the color feature map for promptable segmentation, trained on the same limited domain, would provide a fairer mid-point comparison with SAM.
- Quantitative evaluation of part-level compositionality using an established part segmentation benchmark (e.g., PartImageNet) to back the hierarchical representation claim.

## Novel Insights

The paper's most genuinely novel contribution is the empirical demonstration that generative pretraining—even at the scale of ImageNet-1K alone (MAE)—encodes equivariant, boundary-aware object grouping priors that transfer without category-diverse supervision. The controlled MAE vs. DINO comparison under identical finetuning conditions is methodologically clean, and the convergence of two independent evaluations (promptable segmentation and edge detection) on the same conclusion strengthens confidence. The finding that finetuning on only five object classes suffices for broad zero-shot generalization points toward a practically important asymmetry: generative models may require far less annotated diversity to bootstrap generalizable perception than discriminative paradigms do, which has implications for low-resource perception in medical imaging and robotics where diverse labeled data is scarce.

## Suggestions

- Provide at least one experiment varying inference/finetuning resolution for SD to quantify how much of the small-object gap is resolution-limited versus intrinsic.
- Include a per-category breakdown of COCO_exc^L results to assess whether gains over DINO-B are uniform or driven by specific visual properties (e.g., texture-rich vs. shape-defined objects).
- Consider adding a lightweight learned projection head for prompting that trains on the same limited data—the goal would be to cleanly separate feature quality from the prompting mechanism's quality.

## Score and Decision

The paper addresses an important question (what do generative models learn for perception, and can it substitute for diverse supervision?), presents a clean experimental design with a good causal ablation, and delivers consistent findings across multiple evaluation axes. The instance coloring loss is simple and principled. The main limitation—severe small-object underperformance and an uncontrolled prompting comparison—are real but do not invalidate the central claims about zero-shot generalization from narrow supervision. The contribution is above the average ICLR submission in novelty and empirical rigor.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>