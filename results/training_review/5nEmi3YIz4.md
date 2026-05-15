Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

ProtoNMF proposes a post-hoc, two-step method (NMF prototype discovery + convex classification head reconstruction with a residual) that converts any trained black-box image classifier into a form that provides prototype-based explanations. The key claimed contribution is that, unlike prior prototype-based models (e.g., ProtoPNet) that trade accuracy for transparency, ProtoNMF guarantees recognition accuracy equal to the original black box by reconstructing its classification head and accounting for any error through a residual prototype that is then distributed across the NMF prototypes. The method is evaluated on CUB-200-2011 and ImageNet with CNNs, ViTs, and CoC.

## Strengths

- **Novel reverse-direction approach to prototype-based interpretability**: Unlike prior prototype-based models (ProtoPNet and variants) that build interpretability into the architecture from scratch via complex multi-stage training, ProtoNMF starts from a trained black box and *converts* it into a form that supports prototype-based reasoning. This "reverse direction" (Section 1, line 14) is a genuine departure from the literature and opens a new path for retrofitting existing high-performance models with interpretability without retraining.

- **Guaranteed accuracy preservation via explicit reconstruction**: Because the method exactly reconstructs the black box's classification head (with the residual distributed across prototypes), ProtoNMF achieves identical accuracy to the original black box. Tables 2 and 3 demonstrate this: on ImageNet with ResNet34, ProtoNMF matches the black box at 75.1% top-1 accuracy, whereas ProtoPNet drops to 65.5%. This property—however achieved—is genuinely novel: no prior prototype-based model or explanation method offers this guarantee.

- **NMF yields diverse, parts-based prototypes with empirical evidence of comprehensiveness**: The paper shows quantitatively (Table 1) that NMF-derived prototypes serve as better basis vectors for reconstructing class features than ProtoPNet's selected prototypes, with consistently lower reconstruction error. Qualitatively (Figure 2), the prototypes correspond to distinct body parts (head, belly, wing) that remain stable across training cycles, while ProtoPNet's prototypes become redundant. The use of NMF's non-negativity constraint to force additive, parts-based representations is well-motivated (Section 3.1, line 66).

- **Applicability across diverse architectures**: ProtoNMF works on CNNs (ResNet34), Vision Transformers (ViT-base), and CoC-tiny without architectural modification (Section 4.2, Figure 3), demonstrating generality beyond the CNNs with ReLU activations that prior prototype methods are typically limited to. The handling of negative features (zeroing negatives) is simple but empirically effective.

## Weaknesses

### Fatal
None. No single error invalidates the paper's core claims or results. The method is technically sound as presented.

### Major

- **No quantitative evaluation of interpretability—the paper's core claim is unmeasured**. The paper asserts that ProtoNMF "discovers meaningful prototypes" and offers "transparent reasoning," yet provides no direct interpretability evaluation. The evidence consists entirely of:
  - Qualitative heatmap visualizations (Figures 2–4) — subjective by nature.
  - Feature reconstruction error (Table 1) — a compression metric, not an interpretability metric.
  - A case study of coefficients for the "sled dog" class (Section 4.2) — anecdotal.
  
  There is no human study, no comparison with ground-truth part annotations (e.g., bird body parts in CUB), no concept coherence/completeness metric from the concept-based explainability literature, and no user study demonstrating that the resulting explanations improve human understanding or facilitate debugging. For a paper whose *entire purpose* is interpretability, this is a critical evidential gap. The paper cannot support its primary motivation without it.

- **Misleadling comparisons with inherently interpretable models**. Table 2 compares ProtoNMF's accuracy (74.8%, exactly matching ResNet34) against ProtoPNet's accuracy (70.7–73.0%), presented as ProtoNMF "outperforming" prior prototype-based models. This is an apples-to-oranges comparison: ProtoPNet is an *inherently interpretable model* that trades accuracy for transparency (its prediction is entirely based on prototype comparisons), whereas ProtoNMF *reconstructs* the black box's classification head. The accuracy advantage is a direct consequence of the reconstruction, not a methodological improvement. The paper acknowledges this indirectly ("we do not claim to outperform all prior prototype based models in all aspects," line 46) but the table and surrounding text strongly imply superiority. This framing is misleading and should be replaced with a fair comparison against other post-hoc explanation methods or a clear acknowledgment that the two approaches have fundamentally different trade-offs.

- **The residual handling is ad-hoc and its interpretability is unvalidated**. The "transparent reasoning" claim is undermined by two issues:
  1. The "NMF only" accuracy is substantially lower than the black box (e.g., 57.8% vs. 75.1% for ResNet34 on ImageNet, Table 3), showing that the interpretable NMF prototypes alone carry far less discriminative signal. The residual accounts for the gap.
  2. The formula for distributing the residual across the NMF prototypes (Eq. 8: \(b_i + R^c / \sum a_i\)) has no principled justification. Why divide by the sum of coefficients? Why distribute equally? The resulting "augmented" prototypes mix the interpretable NMF component with the uninterpretable residual, potentially distorting both. The paper asserts the augmented prototypes "are both discriminative and interpretable" (line 182) but provides no evidence that the augmentation preserves semantic meaning.

### Minor

- **Zeroing negative features for ViT/CoC is a simplification with unexamined consequences**. The paper acknowledges this (Section 3.1, line 80) but provides no quantitative analysis of information loss. Given that the "NMF only" accuracy is already low for CNN architectures, the impact on ViT/CoC could be more severe. A simple ablation (e.g., comparing NMF with semi-NMF or convex-NMF alternatives) would strengthen confidence.

- **The residual's content is not systematically analyzed**. The paper visualizes the residual via heatmap optimization (Eq. 6) and notes it is "mostly present in the foreground, offering insights such as there are still undiscovered discriminative patterns" (line 105). But this is a qualitative observation without systematic evaluation. Showing examples of residual heatmaps and analyzing whether the residual captures meaningful missed concepts or noise would strengthen the contribution.

- **Missing explicit text stating the accuracy of the augmented NMF model**. Table 3's column header "NMF+residual/Aug. NMF" exists, but the paper's text surrounding Table 3 does not explicitly state the numerical accuracy of the augmented NMF prototypes. The reader must infer from the column (rendered as an image) that the augmented NMF recovers the full accuracy. This should be stated explicitly in the text.

### Trivial
None.

## Nice-to-Haves

- A human evaluation study (e.g., prototype naming task, part localization accuracy) would directly support the interpretability claims.
- A comparison with other post-hoc concept discovery methods (e.g., clustering + linear probe, TCAV-style concept vectors) would better situate the method in the post-hoc explanation literature, which is where it naturally belongs.
- A systematic analysis of how the number of prototypes affects both accuracy recovery and human interpretability (beyond the reconstruction error curves in Figure 5) would be useful for practitioners.
- Demonstrating the promised test-time intervention (e.g., suppressing a biased prototype and confirming the prediction changes as expected) would show practical value beyond explanation.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The paper does not report the accuracy of the augmented NMF prototypes"** (from Harsh Critic Issue 3): Factually wrong. Table 3 has a column "NMF+residual/Aug. NMF" that reports this information. The column header is present in the text (line 192), and the values are rendered in the table image.
- **"The paper never clearly states the inference procedure"** (from Harsh Critic Issue 3): Factually wrong. Section 3.3 (line 107–127) explicitly describes the inference process, including the decomposition equation and the residual distribution strategy, with reference to an illustrative figure in Appendix A.3.
- **"Mischaracterization as a prototype-based model rather than a post-hoc method" as a fatal flaw**: The paper explicitly states "our model can be categorized to both a prototype based model and a post-hoc method" (Section 2, line 31). It acknowledges the "reverse direction" throughout. While the framing is ambitious and could be tempered, this is not a fatal misrepresentation—it is clearly disclosed.
- **"The negative coefficients for background are a consequence of linear decomposition, not a sign that the model learned them"**: The paper does not claim the model "learned" these coefficients during training. It interprets them as revealing the model's reasoning (line 196), which is standard and valid for linear decomposition weights.
- **Pure formatting/style nitpicks and claims about missing appendix content**: Removed per instructions — these are parser artifacts.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a tension at the heart of the work: ProtoNMF offers a "guarantee" of accuracy that is technically trivial (it's a reconstruction) but practically novel (no prior prototype-based approach could match black-box accuracy). The crucial question the paper sidesteps is whether the resulting "transparent reasoning" is genuine or illusory. The residual distribution (Eq. 8) forces the interpretable prototypes to absorb uninterpretable signal, which may produce explanations that appear plausible but are actually contaminated. This tension—between fidelity to the original model and faithfulness of the resulting explanations—is a known challenge in post-hoc interpretability (Rudin, 2019), and the paper would benefit from engaging with it directly rather than asserting that the augmented prototypes "are both discriminative and interpretable" without evidence. The reviews also highlight that the paper's real contribution—a post-hoc decomposition that yields global, parts-based explanations without accuracy loss—is obscured by its insistence on being framed as a "prototype-based model" competing with inherently interpretable approaches.

## Suggestions

1. **Reframe the contribution honestly**: Reposition ProtoNMF as a *post-hoc explanation method* that provides global, prototype-based decompositions of a black box's decision boundary with guaranteed fidelity, rather than as a "prototype-based model" competing directly with ProtoPNet. The reverse-direction framing is novel enough to stand on its own merits.

2. **Add interpretability evaluation**: At minimum, (a) measure prototype alignment with ground-truth part annotations (e.g., CUB body parts), (b) conduct a human evaluation where participants identify the semantic concept each prototype represents, and (c) compare against a simple baseline (e.g., k-means feature clustering + linear probe) on the same interpretability metrics.

3. **Report the augmented NMF accuracy explicitly in the text** and clarify that the residual distribution enables exact reconstruction — but also acknowledge that the "interpretable" part (NMF prototypes alone) carries substantially less discriminative signal.

4. **Replace or qualify the apples-to-oranges comparison** (Table 2) with a clearer distinction: one column for inherently interpretable models (ProtoPNet variants) and one column for post-hoc decomposition methods. Explicitly state that the accuracy advantage follows from reconstruction, not from superior prototype learning.

5. **Provide principled justification or alternatives for the residual distribution formula** (Eq. 8), or at minimum discuss why this choice was made and what alternatives were considered. Show that the augmented prototypes remain interpretable (e.g., by demonstrating that their heatmaps remain semantically coherent).

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>