Now I have all the information needed. Let me construct the final review.

## Summary

The paper identifies that standard "filter-based" Concept Activation Vectors (CAVs)—derived from linear classifiers optimizing class separability—capture distractor signals and diverge from the true concept direction. To address this, the authors introduce "pattern-based CAVs" computed by regressing latent activations on concept labels (Eq. 4), which directly estimates the concept signal while discarding distractor components. Experiments across VGG16, ResNet18, and EfficientNet-B0 on ISIC2019, Pediatric Bone Age, and FunnyBirds datasets show that pattern-CAVs achieve higher alignment with ground-truth concept directions, improve TCAV reliability, and enhance model correction (ClArC) for shortcut removal.

## Strengths

1. **Identifies a genuine, overlooked problem in a widely used methodology**: The paper formally demonstrates that filter-based CAVs optimize class-separability and thereby capture distractor directions unrelated to the concept signal. This critique is novel and well-supported by the 2D toy experiment (Section 3.3, Figure 1), where filter-CAVs diverge under distractor scaling and rotation while pattern-CAVs remain aligned.

2. **Introduces a principled, theoretically grounded solution**: Pattern-CAVs are derived by reversing the regression direction (regressing activations on concept labels rather than labels on activations), grounded in established neuroimaging literature (Haufe et al., 2014). This formulation (Eq. 4, Section 3.2) inherently discards distractor components and has a closed-form solution requiring no hyperparameter tuning.

3. **Empirically demonstrates superior alignment with true concept directions across multiple architectures and datasets**: Figure 3 shows pattern-CAVs consistently achieve higher cosine similarity with ground-truth concept directions across all 13 Conv layers of VGG16 for three controlled datasets, with standard errors reported. Figure 4 further shows pattern-CAVs are invariant to feature preprocessing, while filter-CAVs vary substantially.

4. **Shows clear downstream benefits in two applications**: (a) TCAV experiments (Figures 5 and 6) demonstrate that pattern-CAVs yield TCAV scores reflecting the model's true concept sensitivity, while filter-CAVs produce arbitrary scores varying with distractor orientation. (b) Model correction with RRClArC (Table 1, Figure 7) shows pattern-CAVs consistently reduce artifact sensitivity while maintaining accuracy, with strong qualitative evidence (Figure 7) where pattern-CAVs drastically reduce artifact attribution while filter-CAVs barely help.

5. **Honest and appropriate limitations section**: The paper explicitly acknowledges that filter-CAVs may be superior for tasks where class-separability matters (e.g., post-hoc concept bottleneck models), providing a nuanced contribution rather than claiming pattern-CAVs universally replace filter-CAVs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Table 1 (model correction results) lacks variance estimates.** The paper reports standard errors for the alignment experiments (Figure 3) and for AUC using the Wilcoxon-Mann-Whitney statistic, but the main model correction table reports only point estimates for accuracy, artifact relevance, and ΔTCAV with no indication of variability across runs or seeds. Since the paper's core claims about downstream utility rest partly on these numbers, the omission reduces confidence. This is addressable in revision (adding error bars from multiple seeds or bootstrap intervals), and the converging evidence from the layer-by-layer plot (Figure 6) and qualitative results (Figure 7) mitigates the concern, but it remains a gap.

2. **The ground-truth concept direction is operationalized as an additive shift without discussion of when this assumption might fail.** The definition $\bh_{\text{gt}} = \ba(\bx^+) - \ba(\bx^-)$ (Section 4.2) assumes the concept manifests as an additive, linear effect in latent space. This is valid for the controlled datasets (timestamp overlays, brightness changes), but the paper does not discuss whether more complex real-world concepts (e.g., compositional or contextual features) could violate additivity. The claim that pattern-CAV better estimates the "true concept direction" is relative to this operationalization. Adding a short discussion of this assumption and its scope would strengthen the paper.

3. **The ResNet18 TCAV result (all CAVs achieve perfect scores) is noted but not explained.** Line 292 observes "interestingly, all CAV variants achieve a perfect score for ResNet18" in the FunnyBirds TCAV experiment, but no hypothesis is offered (e.g., ResNet18's residual connections making concept directions more robust to distractor influence, or architectural differences in feature distributions). The paper does not need a full analysis, but acknowledging and briefly speculating on why directional divergence matters less for this architecture would help readers understand the method's scope.

4. **The formal connection between pattern-CAV invariance to feature preprocessing and Pearson correlation is implicit but not mathematically stated.** The paper states that pattern-CAV's invariance to centering and scaling (Figure 4) is "attributed to the fact that Pearson correlation is not affected by the scale and translation of variables" (line 223), but Eq. (4) defines pattern-CAV using covariance, not correlation. While the connection holds after z-score normalization (covariance becomes proportional to correlation), the paper does not make this step explicit. Minor clarity issue.

### Trivial

None.

## Nice-to-Haves

- **Add an oracle baseline in model correction**: Using the ground-truth direction $\bh_{\text{gt}}$ itself in RRClArC would show how close pattern-CAVs come to the optimal correction, providing a valuable upper bound.
- **Report computational cost or fitting time**: The paper claims pattern-CAVs are "more computationally efficient" because they require no hyperparameter tuning (line 225), but provides no runtime measurements. A brief comparison would support this claim.
- **Statistical significance for artifact relevance reductions**: For the model correction results where effect sizes are small (e.g., ResNet18 band-aid), bootstrapping across samples could confirm whether reductions are significant.

## Removed Points

These points are flagged to be removed; treat them with caution.

- The harsh critic's comment that "controlled datasets use very simple concepts (overlays, brightness)" and that "one could argue that these are too easy." This is partially addressed by the real-artifact experiments (band-aid, ruler, skin marker), and the use of controlled settings is a deliberate design choice to enable ground-truth computation. The paper already acknowledges this structure.
- The critic's suggestion that "the paper does not discuss whether the ground truth direction itself may also change under pre-processing." The critic acknowledges this is likely fine ("presumably yes"). This was raised as a question, not a confirmed weakness.
- The critic's framing of the additivity assumption as potentially undermining "what is established." The downstream experiments (TCAV, model correction) demonstrate practical utility regardless of whether the additive assumption holds universally. The paper's claims about alignment with $\bh_{\text{gt}}$ are appropriately qualified as applying to the controlled setting.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent subtext: the paper's central contribution is about *directional accuracy* versus *class separability* as competing desiderata in concept representation. This framing—that different CAV applications require different properties from the concept vector—is already articulated in the paper's limitations section and is the paper's core insight.

## Suggestions

1. **Add variance estimates to Table 1.** Re-run model correction with at least 3 random seeds and report mean ± std for all metrics. If computational cost is prohibitive, provide bootstrapped confidence intervals for the artifact relevance and ΔTCAV metrics.

2. **Add a brief paragraph in Section 4.2 or the Limitations discussing the additivity assumption** underlying $\bh_{\text{gt}}$. Acknowledge that this operationalization is valid for controlled settings with known, localized concepts, and note that real-world concepts with complex or nonlinear effects may require more nuanced ground-truth definitions.

3. **Briefly hypothesize why all CAVs achieve perfect TCAV scores on ResNet18** (e.g., architectural properties such as residual connections that distribute concept information more robustly, or differences in the last-layer feature space).

## Score and Decision

The paper makes a clear, well-motivated methodological contribution: identifying directional divergence in standard CAVs and proposing a principled fix grounded in the neuroimaging literature. The experiments are carefully designed across multiple architectures (VGG16, ResNet18, EfficientNet-B0), datasets (ISIC2019, Bone Age, FunnyBirds), and applications (TCAV, ClArC), with results consistently supporting the claims. The limitations are honestly discussed. The remaining weaknesses—missing variance estimates in Table 1, the undiscussed additivity assumption, and the unexplained ResNet18 result—are all addressable in revision and do not undermine the core contribution. The converging evidence from multiple experiments (alignment metrics, TCAV, qualitative/quantitative model correction) makes the paper's claims robust despite the minor gaps.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>