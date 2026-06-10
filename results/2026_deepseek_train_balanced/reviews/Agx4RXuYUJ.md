## Summary
This paper investigates temperature scaling for sigmoid-based logit distillation in multi-label learning. It proposes Tempered Logit Distillation (TLD), which introduces a temperature parameter τ into the sigmoid activation function. Through theoretical gradient analysis, the paper shows that τ<1 produces a hardness-aware distillation effect, focusing student learning on challenging samples. The method is evaluated across image classification, object detection, and instance segmentation on COCO, PASCAL-VOC, and NUS-WIDE, consistently outperforming KL and BCE baselines and achieving competitive results with feature-based KD methods.

## Strengths

1. **Clean theoretical analysis linking τ to hard-sample mining (Section 3.2, Eq. 7).** The gradient derivation ∂ℒ_TLD/∂z_i^s = τ(p̃_{i,τ}^s − p̃_{i,τ}^t) is simple yet insightful. It formally connects temperature in sigmoid to penalty weighting: τ<1 concentrates gradient on samples with large teacher–student discrepancy. This is not merely a restatement but a genuine theoretical contribution that explains why τ behaves oppositely for sigmoid (τ<1 optimal) versus softmax (τ>1 optimal).

2. **Comprehensive multi-task, multi-dataset evaluation (Tables 2–9).** The paper evaluates across three datasets (COCO, PASCAL-VOC, NUS-WIDE) and three distinct tasks (multilabel classification, object detection, instance segmentation) using multiple architectures (ResNet18/34/50, GFocal, SOLOv2). TLD consistently beats both KL and BCE baselines in every configuration. The finding that a simple logit-only method can be competitive with feature-based methods (Tables 8, 9) is genuinely interesting and practically useful.

3. **Systematic τ ablation revealing opposite optimal regimes (Table 10).** Varying τ from 0.25 to 10 shows that TLD performs best at τ<1 (robust even at τ=0.25) while KL requires τ>1, with the opposite trends clearly documented. This clean empirical result strongly supports the paper's central thesis and is the strongest piece of evidence for the contribution.

4. **Visual evidence corroborating the hard-mining mechanism (Figures 3, 4, 5).** The loss distribution visualizations show TLD with τ<0.5 producing highly sparse loss concentrated on semantically meaningful regions (hands, edges, objects), while KL distributes loss broadly across the image. These figures directly support the theoretical claim and are more convincing than numbers alone.

5. **Self-KD results and compatibility with feature-based methods (Tables 11, 2, 8, 9).** TLD still yields substantial gains in self-KD (+2.54% mAP classification, +1.1% detection), showing the mechanism does not depend on a capacity gap. It also combines additively with FitNet, MGD, and PKD, demonstrating practical flexibility.

## Weaknesses

### Fatal
None.

### Major

1. **Some overclaiming in the conclusion relative to empirical margins.** The paper states that TLD "outperforms state-of-the-art KD methods designed specifically for the corresponding tasks." In detection (Table 8), TLD (42.1 mAP) beats MGD (41.9) by only +0.2% mAP — a margin that could fall within run-to-run variation. In segmentation (Table 9), TLD alone (38.2) actually trails MGD (38.6) and PKD (38.3). While TLD+FitNet/TLD+MGD achieve the best overall segmentation results (39.0, 39.2), the claim that TLD alone "outperforms" dedicated feature-based methods is not uniformly supported by the reported numbers. This overreach should be scoped more carefully in a revision but does not invalidate the core contribution.

2. **The foundational motivation (Table 1) comparing sigmoid vs. tempered softmax lacks the statistical support needed for its role as a linchpin claim.** The paper opens by asserting that prior work's conclusion — that sigmoid is more suitable than tempered softmax — "is not entirely correct." Table 1 is the primary evidence that removing confounding factors makes sigmoid's advantage "substantially disappear." This is a negative finding (two activation functions are not meaningfully different), and negative findings require some indication of stability across runs to be persuasive. Without error bars or multiple seeds, the reader cannot distinguish between genuine equivalence and hyperparameter- or seed-specific results. This weakness is confined to the motivational framing and does not cascade into the core contribution (TLD vs. fixed-τ baselines), but it is notable given the weight the paper places on the refutation.

### Minor

1. **No error bars or variance estimates for any reported result.** This is a concern because many reported gains in detection and segmentation are modest (1–2% mAP, or as small as +0.2%). While single-run reporting is common practice in computer vision at top venues, the paper would be substantially strengthened by adding at minimum 3-run mean±std for its main comparisons (Tables 6–9) and for the τ ablation (Table 10). This is the single highest-leverage improvement the authors could make.

2. **No discussion of how τ=0.5 was selected for the main experiments.** The paper uses τ=0.5 for most experiments but does not state whether this was chosen via a validation set, from Table 10's ablation, or heuristically. Since the paper's practical recommendation is τ<1 and performance varies across τ values, the selection procedure should be disclosed.

3. **The τ→0 analysis (Section 3.2) lacks precision.** The paper states that "when τ→0, the p̃_{i,τ}^t starts resembling the ground-truth [1,0]." More precisely, τ→0 makes sigmoid approach a step function, producing hard binary values — the teacher's probabilistic predictions collapse to deterministic labels, which is a qualitatively different regime from the soft probability-based intuition the paper relies on. The direction of the analysis is correct, but this nuance should be acknowledged.

### Trivial
- "Astonishingly performant" and "remarkable performance" in the abstract are promotional and not commensurate with empirical gains that, while solid, are in the typical range for KD improvements.

## Nice-to-Haves
- **Ablation isolating the effect of tempered sigmoid from the loss function.** The paper compares TLD (tempered sigmoid + binary KL) against KL (tempered softmax + multiclass KL) and BCE (sigmoid + BCE). An experiment with tempered sigmoid + BCE would isolate whether the benefit comes from the activation function itself, the binary KL formulation, or their combination.
- **A direct comparison plugging tempered sigmoid into the full L2D/BCKD pipelines** (i.e., L2D/BCKD with their re-weighting and advanced distance functions, but swapping vanilla sigmoid for tempered sigmoid). This would definitively isolate the contribution of τ in the context of prior methods.
- **Adaptive/learned temperature for sigmoid-based multi-label KD** is a natural extension mentioned in related work but not applied. This is explicitly future work and not a required comparison.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Criticism that "L2D and BCKD never claimed that sigmoid alone was superior" and that the paper's refutation is of a claim prior work did not make.* Removed because the paper correctly paraphrases L2D/BCKD's claims that tempered softmax is unsuitable for multi-label KD and that sigmoid is more suitable. The refutation (Table 1) specifically tests the activation function in isolation, which is precisely the claimed basis for their preference. This is a valid scientific comparison.
- *Criticism that "the paper does not compare against adaptive or learned temperature methods applied to sigmoid-based multi-label KD."* Removed because it asks the paper to solve an open problem beyond its stated scope. The paper's contribution is introducing τ to sigmoid with a fixed value; adaptive methods are a natural extension, not a required comparison.
- *Generic strengths about "important problem" or "well-written"* — superficial and lacking specific evidence, removed.
- *Criticism about missing related works.* Removed per instructions (cannot verify existence of external works).

## Novel Insights
None beyond the paper's own contributions. The key insight — that τ<1 in sigmoid provides hardness-aware distillation, opposite to the τ>1 optimal for softmax — is already well-articulated in the paper itself. The reviews do not add genuinely novel observations beyond this.

## Suggestions
1. Add 3-run mean±std for all main tables (especially Tables 1, 6–10) to establish the reliability of gains, particularly those under 2% mAP.
2. Soften the language around outperforming specialized KD methods; the current claim in the conclusion exceeds what the margins consistently support.
3. Clarify how τ=0.5 was chosen (validation set, ablation result, or heuristic) and consider a cross-task sensitivity analysis of τ.
4. Expand the τ→0 analysis to explicitly note the step-function limit and its implications for the hardness-aware mechanism.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>