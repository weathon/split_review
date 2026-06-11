Now let me write the final consolidated review.

## Summary
This paper identifies a theoretical flaw in HiResCAM explanations—they admit an arbitrary additive shift that leaves probability predictions unchanged (Theorem 3.2)—and proposes ContrastiveCAMs (pairwise HiResCAM differences) that are provably invariant to this shift (Theorem 3.5). Using ContrastiveCAMs, the authors observe that standard cross-entropy training encourages reliance on non-core (spurious) regions, and propose Core-Focused Cross-Entropy (CFCE) to penalize non-core contributions during training. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and Pascal VOC demonstrate improvements in feature alignment metrics.

## Strengths
1. **Theorem 3.2 (non-uniqueness of HiResCAMs)**: The paper proves that HiResCAMs admit an arbitrary additive matrix M that changes every class-level explanation yet leaves probability predictions unchanged—a genuine theoretical flaw in a widely-used explanation method that prior work (including Draelos and Carin, 2020, who introduced HiResCAM) did not identify. The proof follows cleanly from softmax shift-invariance amplified to the spatial dimension via Eq. (3).

2. **ContrastiveCAMs are provably M-invariant (Theorem 3.5) and directly express probabilities (Proposition 4.1)**: Definition 3.3 constructs ContrastiveCAMs as pairwise differences of HiResCAMs; Theorem 3.5 shows the spurious M cancels exactly. Proposition 4.1 goes further, proving that softmax probabilities can be expressed as a direct function of ContrastiveCAMs alone (Eq. 11) when the classifier bias is zeroed. This establishes a formal correctness guarantee connecting the explanation to actual predicted probabilities—a property not held by HiResCAM itself.

3. **Core-Focused Cross-Entropy is theoretically grounded (Definition 4.5, Theorem 4.6)**: The paper first decomposes cross-entropy into core and non-core contributions (Proposition 4.2), showing that CE does not inherently differentiate between them. CFCE (Eq. 15) replaces the non-core term with a positive penalty. Theorem 4.6 proves that CFCE is classification-calibrated w.r.t. the core-constrained risk—a strong consistency guarantee.

4. **Substantial empirical gains across multiple alignment metrics**: On Hard-ImageNet (Table 2), CFCE+KL achieves 93.39% ContrastiveCAM IoU (vs. 30.27% for CE w/ Arch) and 51.52% GradCAM IoU (vs. ~18% for CE baselines). Core-region ablation accuracy drops dramatically (Gray Mask: 45.49% vs. 75.94% for CE—lower is better, indicating less reliance on ablated regions). RFS shifts from -0.18 (CE) to +0.236 (CFCE+KL), indicating the model becomes genuinely sensitive to foreground/core regions.

5. **Robustness to coarse or auto-generated masks (Section 5.2)**: CFCE with SAM-generated masks achieves IoU of 83.95% (binary validation) and 85.26% (multiclass validation), close to the ground-truth-mask performance (82.92%/88.16%). Even bounding-box supervision gives competitive results (79.13%/84.61%), demonstrating practical applicability.

6. **Downstream segmentation transfer (Section 5.3)**: Backbones trained with CFCE+KL improve segmentation IoU across most PASCAL VOC classes compared to CE-trained initializations, showing that the induced feature alignment transfers to dense prediction tasks.

## Weaknesses

### Fatal
None.

### Major
1. **Incomparable IoU metrics across methods in the headline experiment (Table 2)**: The paper's central quantitative claim of dramatically improved "feature alignment" is supported by ContrastiveCAM IoU for the proposed methods (89.22%, 93.39%) but only GradCAM IoU for the baselines (~18-20%). The paper acknowledges this in a footnote, noting that GradCAMs "have been shown to present unfaithful explanations," but this does not resolve the comparability concern. The paper does report GradCAM IoU for all methods—on this comparable metric, CFCE achieves 18.88 (essentially tied with CE's 18.44) while CFCE+KL achieves 51.52 (a clear improvement). So there IS some comparable evidence, but the paper's presentation emphasizes the non-comparable ContrastiveCAM numbers. Additionally, the IoU metric in Tables 3 and 4 (Pets, Pascal VOC) is unspecified—it is not stated whether it is GradCAM-based, ContrastiveCAM-based, or something else, making cross-table comparisons difficult.

2. **Anomalous "CE w/ Arch" baseline behavior on Pets (Table 3)**: The "CE w/ Arch" baseline achieves 38.58% IoU on training vs. 78.37% for plain cross-entropy—a ~40-point degradation from adding "interpretability-motivated modifications" (detailed in Appendix C, which was stripped). This is a massive drop that is unexplained in the main text. While the architectural modifications are described in the (stripped) appendix, the anomalous numbers themselves raise questions about whether the modifications encode inductive biases rather than the loss, or whether there is a confound. Readers cannot assess the fairness of this comparison from the main text alone.

### Minor
1. **No analysis of mask quality sensitivity**: The paper shows results with GT masks, SAM masks, and bounding boxes, and notes that "KL regularization must not be applied when bounding boxes are used" (Section 5.2), hinting at sensitivity. However, there is no systematic study of how mask quality degradation (e.g., noise, boundary errors, false positives/negatives) affects downstream performance. This would help practitioners understand when the method can be applied.

2. **Un-ablated accuracy trade-off not characterized**: CFCE models show ~4% lower un-ablated accuracy on Hard-ImageNet (90.53% vs. 94.25% for CE). The paper mentions this trade-off but does not analyze it (e.g., via a sweep of the non-core penalty to show a pareto frontier). Similarly, on Pets, CFCE validation accuracy is sometimes slightly below CE (92.96% vs. 94.41% multiclass).

3. **Missing error bars for Hard-ImageNet baselines (Table 2)**: Standard deviations are reported for the proposed methods and "CE w/ Arch" but not for baselines (CORM, DFR, CORM+DFR). While these may be from prior work without multiple runs, the asymmetry makes comparison less informative.

4. **Segmentation results lack variance or significance (Section 5.3)**: The segmentation bar chart shows per-class IoU improvements but reports no error bars or statistical significance, making it hard to assess the reliability of the reported gains.

5. **Gradient flow through CAM computation not discussed**: The CFCE loss is defined in terms of ContrastiveCAMs. With the assumed GAP + linear classifier, ∇_{A_j} f_c is constant w.r.t. activations, keeping the loss first-order differentiable. However, the paper does not explicitly state this simplification or discuss whether the "interpretability-motivated modifications" (Appendix C) preserve it. Clarification would help readers assess training feasibility.

### Trivial
- The IoU metric in Tables 3 and 4 should specify which CAM method it is based on, for clarity.

## Nice-to-Haves
- A pareto frontier analysis of the accuracy-alignment trade-off as the non-core penalty strength is varied.
- A systematic study of mask quality degradation (e.g., adding spatial noise to GT masks at varying levels) to characterize practical robustness.
- Reporting computational overhead of computing ContrastiveCAMs during training relative to standard forward/backward passes.
- Error bars on the segmentation results.

## Removed Points
The following points from the reviewers are removed (kept here for completeness):

- **"Positive RFS is unusual / unexplained"**: Removed because the critic misread RFS. Positive RFS means corrupting foreground *hurts* performance (the expected/desired behavior for a model that relies on core regions). CE's negative RFS (-0.18) is the unusual case—corrupting foreground *improves* performance, indicating reliance on background. The paper correctly interprets this.
- **Criticism about Theorem 3.2's practical significance**: Removed because the critic argued the theorem is about reverse mapping, not forward computation. The theorem's framing (non-uniqueness of explanations given probability predictions) is precisely the relevant framing for why ContrastiveCAMs provide more faithful explanations—the point is that there exist infinitely many HiResCAMs consistent with the same prediction, so the one you compute may be misleading.
- **"Missing training details are fatal"**: Removed per rule on stripped appendices. Hyperparameters (λ₁, λ₂, λ₃, optimizer settings, etc.) are likely in Appendix B/C which was stripped by the parser. The λ values are noted as a minor concern but not a fatal omission.
- **"Related work is thin"**: Removed per the rule about not citing missing related work without external sources to verify what exists in the literature.
- **Formatting, typo, and presentation nitpicks**: Removed per instructions on parser artifacts.
- **"Method requires near-perfect masks" overstatement**: Removed because the paper already demonstrates competitive performance with SAM and bounding-box masks, directly contradicting this claim.

## Novel Insights
The reviews surface a tension in the paper's empirical strategy that is worth highlighting: the paper presents two distinct contributions (ContrastiveCAMs as a better explanation method, and CFCE as a training method that leverages them), but the evaluation partially conflates them. The headline IoU improvements on Hard-ImageNet combine both contributions—ContrastiveCAM provides the better metric, and CFCE produces the better models—but the metric itself comes from the authors' own method, creating a circularity concern. The paper partially mitigates this by also reporting GradCAM IoU for all methods, but the contrast between the modest GradCAM IoU improvement (18.88 vs. 18.44 for CFCE alone) and the dramatic ContrastiveCAM IoU improvement (89.22) would benefit from explicit discussion. A cleaner evaluation would report both CAM types for all methods where possible. Despite this, the non-IoU metrics (RFS, ablation accuracy drops, downstream segmentation) provide independent converging evidence that CFCE genuinely improves feature alignment.

## Suggestions
1. **For the rebuttal/next version**: In Table 2, explicitly state "GradCAM IoU" and "ContrastiveCAM IoU" as separate columns and report ContrastiveCAM IoU for baseline methods where the pre-trained models are available. If not available, note this limitation explicitly.
2. **In Tables 3 and 4**: Specify which CAM method underlies the reported IoU metric.
3. **Report λ₁, λ₂, λ₃ values** used in the main experiments (these may already be in the stripped appendix but should be in the main text given their direct impact on results).
4. **Add error bars to the segmentation results** (Section 5.3, Figure 4 / bar chart).
5. **Acknowledge the un-ablated accuracy trade-off** more explicitly and, if possible, characterize it with a sweep.

## Score and Decision

### Calibration Anchors
**Round 1 (Bracketing):**
- Low band (<3.5): e.g., "Conceptualize Any Network" (3.00), "Counterfactual Image Generation" (2.50), "Grad-TopoCAM" (3.00), "Patch Ranking Map" (2.50), "COMiX" (3.25) — purely empirical CAM papers with limited theoretical contributions. The paper under review is substantially stronger.
- Middle band (3.5–7.5): e.g., "Interpretable Transformer" (6.00), "How to Probe" (6.25), "InterpGN" (6.60), "QPM" (6.67), "Factor Graph-based Interpretable NN" (6.20), "On Generalization of Gradient-based Interpretations" (4.00). This is the appropriate comparison band.
- High band (>7.5): e.g., "Cross-Entropy Is All You Need to Invert" (8.00), "Learning and aligning single-neuron invariance" (8.00). Papers on different topics with cleaner evaluations; not directly comparable.

**Round 2 (Narrowing within 4.5–7.0):**
- "Faithful Vision-Language Interpretation via CBM" (6.25): Concept bottleneck stability; stronger evaluation but different problem.
- "Respect the model: SRD" (6.00): New XAI method with extensive experiments but presentation issues. Comparable to this paper—both propose better explanations—but SRD has cleaner evaluation while this paper has stronger theoretical grounding and a training component.
- "ContraLSP" (5.75): Contrastive time series explanations. Similar mixed evaluation quality (some unclear claims, imprecise presentation). This paper has stronger theory.
- "How to Probe" (6.25): Clean empirical study of how training affects explanations. This paper has more theoretical depth but messier evaluation.

**Relative placement:** The paper under review has stronger theoretical contributions than any anchor in rounds 1–2 (Theorems 3.2, 3.5, 4.6 are genuine and non-trivial) and a more extensive methodological pipeline (explanation method + training method). However, its evaluation is weaker than most ~6.0 anchors due to the IoU comparability issue and the unexplained CE w/ Arch baseline. It is stronger than ContraLSP (5.75) in both theory and empirical breadth. It is slightly weaker than "Respect the model" (6.00) in evaluation cleanliness but has more theoretical depth. Overall, the paper sits between 5.5 and 6.0—a solid borderline paper with genuine contributions that are somewhat undermined by evaluation presentation issues.

**Round 1 bracket:** 3.5–7.5
**Round 2 narrowing:** compared against anchors at 5.75–6.25, the paper's theory is stronger but its evaluation is weaker → score near the middle/bottom of this band.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>