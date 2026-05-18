Now I have a complete understanding of the paper and can verify each claim. Let me write the consolidated review.

## Summary

The paper investigates the limitations of existing Unlearnable Examples (UEs) and reveals that they fail to maintain unlearnability in multi-task settings. To move beyond test-accuracy-based evaluation, the authors propose Sharpness-Aware Learnability (SAL)—a per-parameter measure of loss landscape sharpness—and Unlearnable Distance (UD), a data-level metric that aggregates SAL to quantify how unlearnable a dataset is. They benchmark existing unlearnable methods using UD across multiple datasets, architectures, and defenses.

## Strengths

- **First empirical demonstration of UE failure in multi-task settings**: The paper evaluates UEs (EM, OPS, AR) on Taskonomy with a ResNet backbone and shows that performance on tasks like semantic segmentation and depth estimation is nearly indistinguishable from vanilla training (Figure 1). This negative result challenges the prevailing single-task assumption and identifies a meaningful open problem.

- **Loss-landscape-based analysis of UE training dynamics at the parameter level**: Using 2D projections of the loss landscape (Figure 2), the paper demonstrates that clean and poisoned models differ primarily in a small subset of "key parameters" that fail to converge under UEs. This offers a different perspective from existing explanations (e.g., linear separability of perturbations) and grounds the analysis in the training process itself.

- **SAL and UD as training-phase metrics for unlearnability**: SAL (Eq. 3) quantifies per-parameter sensitivity by measuring loss variation under weight perturbations. UD (Eq. 5) aggregates this into a single score. The framework correctly identifies TAP as an adversarial example rather than a true UE (UD > 1), clarifying a known confusion in the literature between availability attacks and true unlearnability.

- **Systematic benchmarking across diverse settings**: The paper evaluates UD on CIFAR-10, CIFAR-100, and ImageNet-100; ResNet-18/50, SENet-18, and ViT; and three defenses plus two augmentations (Tables 1–3). This breadth reveals that stronger models (ViT) have higher UD and are harder to poison, validating the metric's sensitivity.

- **Identification that TAP is qualitatively different from true UEs**: The paper provides converging evidence (SAL visualization, learnable parameter counts, UD > 1) that TAP impairs accuracy through continued learning of wrong features rather than stalled learning—a genuinely useful conceptual distinction.

## Weaknesses

### Fatal

None. The weaknesses identified below do not invalidate the paper's core contributions.

### Major

1. **SAL's explanatory claim rests on correlation, not causation.** The paper presents SAL as an "explanation" for how UEs work (contributions: "put forward an explanation for the effectiveness of unlearnable examples"). However, the evidence is entirely correlational: poisoned models have lower SAL and also lower test accuracy. No controlled experiment manipulates SAL independently while keeping other factors fixed. As acknowledged in the paper itself, a low-SAL parameter in a flat region could still learn over many steps if gradients are small but non-zero. Without causal evidence, the claim that SAL *explains* unlearnability is speculative, even if SAL remains useful as a descriptive metric.

2. **The Learnable Threshold (LT) via K-means is arbitrary and unvalidated.** The threshold separating "learnable" from "unlearnable" parameters is computed by running K-means with two clusters on the SAL values of the *clean* model, then taking the mean of the two cluster centers (Eq. 4). The paper provides no justification for why the SAL distribution should be bimodal, no sensitivity analysis for the number of clusters, no analysis of K-means initialization sensitivity, and no analysis of the choice of ε (perturbation radius). Since UD depends entirely on this threshold, its reliability is unclear. A percentile-based threshold or a density-based alternative could serve as a robustness check, but none is provided.

3. **UD's value-add over conventional test accuracy is not convincingly established.** The paper claims UD is "more intrinsic" and does not "rely on the specific form of downstream tasks." Yet in Table 1, UD rankings largely mirror what one would expect from test accuracy. The clearest exception is TAP (UD > 1, which correctly flags it as not a true UE), and OPS shows an anomalous pattern on ImageNet-100 that the paper itself says it "leaves for future discussions." Missing error bars or confidence intervals on all reported UD values (Tables 1–3) make it impossible to assess whether differences between methods are significant or just noise. Without demonstrating that UD predicts something test accuracy does not (e.g., cross-task transferability, robustness to unseen defenses, or stability across seeds), its practical advantage remains unclear.

### Minor

1. **The multi-task finding—the paper's motivating observation—rests on thin evidence.** The experiment uses one dataset (Taskonomy tiny), one backbone (ResNet), and three unlearnable methods, one of which ("AR") is **never defined or referenced in the paper**. The paper acknowledges in Section 3.4 that "it is time-consuming to perform SAL analysis for multi-task models," but the fundamental discovery claim deserves broader validation. As presented, it is an interesting observation rather than a robustly established phenomenon.

2. **A dangling observation in the introduction is never revisited.** Line 18 states "we observed that the model parameters trained on clean datasets have higher values than those trained on UEs," but this claim is never quantified, shown in a table, or meaningfully discussed again. This undermines the precision of the paper's motivating narrative.

3. **No uncertainty quantification on any quantitative result.** All UD values in Tables 1–3 and all SAL visualizations appear to come from single runs. Given that the OPS result on ImageNet-100 shows an "opposite trend" that the paper cannot explain, the possibility that this is a random fluctuation rather than a meaningful signal cannot be ruled out.

4. **The loss landscape visualization (Section 3.1) uses a toy linear classifier (12×10 parameters).** The paper acknowledges this limitation, noting that "the fewer the model parameters, the more accurate the estimation." However, the transition from the toy model to full ResNet-18 experiments is abrupt, and the connection between the two is asserted rather than argued. The claim that "only a few key parameters" matter in deep networks is plausible but not directly supported by the toy experiment.

5. **Missing ablation on ε (the perturbation radius in SAL).** Setting ε = 0.05 for all layers and datasets is plausible, but no analysis shows how UD changes with ε. If UD rankings are sensitive to this hyperparameter, the metric is not robust. This is especially important because SAL is evaluated layer-by-layer with frozen other layers, so the choice of ε could interact with layer-specific gradient scales.

6. **Related work does not compare SAL with existing explanations on common ground.** The paper discusses the linear separability explanation (Yu et al., 2022) and shortcut learning as competing accounts, but does not evaluate whether SAL subsumes, contradicts, or is orthogonal to these explanations on the same datasets. This weakens the claim that SAL provides a "better explanation."

### Trivial

- The method "AR" is used in the multi-task experiment (line 12) but never defined or cited anywhere in the paper.
- The phrase "employe" appears in the figure caption for Figure 2 (a parser artifact).

## Nice-to-Haves

- Providing test accuracy alongside UD in Tables 1–3 would allow readers to directly compare the new metric against the standard one and would strengthen the claim that UD adds value.
- A sensitivity analysis on the number of K-means clusters (2 vs. 3 vs. automatic methods like silhouette score) and on ε would greatly increase confidence in the UD metric.
- A controlled experiment showing that artificially reducing SAL (e.g., via weight perturbation or explicit regularization) impairs generalization would transform the correlational story into a causal one.
- Computing SAL on a representative subset of layers or at sparser epoch intervals, with a demonstration that the ranking is preserved, would address the computational cost concern the paper itself raises about multi-task analysis.

## Removed Points

- **Criticisms about missing figures or references to figures (Figure 1 not visible, Figure 11 missing, etc.):** These are parser artifacts; the original submission has them. Removed per hard rules.
- **Criticism about missing appendix/proofs:** The parser strips these sections. Removed per hard rules.
- **Typos/formatting nitpicks ("employe" etc.):** Parser artifacts. Removed per hard rules.
- **"The paper tries to cover too many disparate contributions":** The paper's structure (observation → explanation → metric → benchmark) is a coherent narrative, not arbitrarily disparate. This is a subjective preference, not a demonstrated flaw. Downgraded to removed.
- **"Algorithm 1 is essentially a recipe, not a methodological contribution":** Algorithm descriptions are standard in papers that introduce computational procedures. This is not a weakness.
- **The claim that the paper doesn't show SAL subsumes existing explanations:** The paper's contribution is introducing a new perspective, not systematically comparing or disproving prior explanations. This expectation overreaches the paper's scope.

## Novel Insights

The human reviews do not surface a genuinely novel insight that goes beyond the paper's own contributions. The tension between the papers—that UD is interesting as a training-phase metric but its advantage over test accuracy is yet to be proven—is already present in the review analysis.

## Suggestions

1. **Strengthen the multi-task evidence** by either expanding it (more datasets, backbones, methods) or explicitly reframing it as a preliminary observation that motivated the SAL/UD framework rather than as a core contribution.

2. **Replace or supplement the K-means threshold** with a more principled alternative (e.g., a percentile of the clean model's SAL distribution) and show that UD rankings are robust to this choice. Add sensitivity analysis for ε.

3. **Run all UD experiments with at least 3 random seeds** and report mean ± std. This is essential for establishing that differences between methods are real, especially given the anomalous OPS result on ImageNet-100.

4. **Clearly distinguish the explanatory claim from the metric contribution.** The paper's strongest offering is the SAL/UD framework as a tool for evaluation and comparison, not as a causal theory of unlearnability. Framing it as such would reduce overclaiming while preserving the contribution's value.

5. **Define "AR"** and add it to the list of methods in Section 5, or replace it with a properly cited method if the abbreviation is non-standard.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>