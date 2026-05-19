- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3, 3, 3, 5
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes DIFAIR, a method for learning representations where each dimension of the feature vector is associated with a specific class, aiming to improve interpretability and open-set recognition (OSR). The approach defines fixed class anchors in feature space with multiple dimensions per class, uses a thresholded Euclidean distance loss (with a hypersphere radius) to cluster instances near their class anchor, and evaluates OSR performance on the Neal et al. (2018) benchmark. The paper honestly analyzes learned representations and identifies that intra-class features are duplicated across dimensions rather than differentiated — a central limitation it explicitly acknowledges.

## Strengths

- **Clear and well-motivated hypothesis.** The paper clearly articulates (Section 1, Figure 1) the desired property: each representation dimension should signal the presence/absence of a class-specific feature, and unknown instances should exhibit low activation across dimensions or activate features from multiple classes. This hypothesis is used to derive the loss function design rather than being merely stated.

- **Novel loss formulation with thresholded Euclidean distance.** Equation 2 defines a loss that is zero inside a hypersphere around each class anchor, allowing intra-class variation and tolerance for activation of other-class features while still enforcing clustering. This concretely differentiates DIFAIR from CAC (which adds a triplet loss for separation) and from standard cross-entropy.

- **Honest and informative representation analysis.** Section 5.1 uses Hinton diagrams (Figure 3a) and weight convergence plots (Figure 3b) to show that DIFAIR-learned features duplicate across dimensions of the same class rather than differentiating distinct visual features — a flaw the paper identifies and discusses transparently. This provides concrete diagnostic evidence for future work.

- **Fair baseline re-implementation.** The paper retrains CAC and cross-entropy baselines using the same improved training protocol (600 epochs, RandAugment, learning rate schedule) as Vaze et al. (2022), enabling controlled comparison despite different random splits in the original papers.

- **Ablation of OSR scoring method.** The paper systematically compares distance-to-anchor versus Maximum Output Score (MOS) for OSR detection (DIFAIR vs. DIFAIR† in Table 1), showing that MOS yields substantially better results and providing insight into how unknown instances activate features at lower magnitudes.

## Weaknesses

### Fatal

None. The paper is transparent about what it does and does not achieve; its claims are not falsified, and the method does partially succeed at associating dimensions with classes, even though the differentiation goal is incomplete.

### Major

- **The method's core objective — differentiated, non-duplicated per-class features — is not achieved, as the paper itself documents.** Section 5.2 states: *"Instead of intra-class feature duplication, it would be preferable to observe feature duplication over other classes … this behavior has not emerged from the optimization."* Figure 3b shows that class weights converge to near-identical values. The loss function (Equation 2) only penalizes distance to the class anchor; it contains no mechanism to encourage diversity among dimensions of the same class. Consequently, the interpretability claim is weakened: associating dimensions with classes is trivial if all dimensions for a class carry the same information. The paper's honest reporting is commendable, but for a methods paper, a loss function that does not produce its intended representational structure is a fundamental limitation that significantly diminishes the contribution's value.

- **OSR results are not competitive with simpler alternatives.** On the Neal et al. (2018) benchmark, DIFAIR (even with MOS) is substantially below state-of-the-art methods like ARPL+CS and DCHS. More critically, the MLS baseline from Vaze et al. (2022) — a standard cross-entropy model without any representation regularization — outperforms DIFAIR on most settings. Compared to the closely related CAC, results are essentially tied, and on CIFAR+10, CAC† exceeds DIFAIR†. The paper argues this is a trade-off for semantic richness, but no evidence demonstrates that this semantic richness benefits any downstream task or changes the pattern of errors. For a paper whose evaluation is entirely OSR-based, the lack of clear advantage over the baseline is a substantial weakness.

- **No quantitative evaluation of interpretability is provided.** Interpretability is a core motivation, yet the only evidence is visual inspection of mean representations (Figure 3a). No user study, interpretability metric (e.g., sparsity, dimension orthogonality, faithfulness to image content), or quantitative analysis of feature semantics is offered. The visual analysis itself reveals feature duplication, which arguably makes the representation *less* interpretable than standard representations (where features may be distributed but are not provably redundant by construction). Without a validated measure, the paper's central interpretability claim cannot be assessed.

### Minor

- **Missing closed-set accuracy.** The paper does not report closed-set accuracy. Given the finding by Vaze et al. (2022) that closed-set accuracy correlates with OSR AUROC, reporting closed-set performance would help contextualize whether DIFAIR's OSR results reflect a genuine trade-off or simply weaker underlying representations.

- **No hyperparameter sensitivity analysis.** The choices (𝒩=5, α=10, r=0.4×√(2Nα²)) are described but not ablated. A sensitivity study for at least one key dataset would clarify how robust the method is.

- **No analysis of individual test instances.** Only mean representations are shown (Figure 3a). Visualizing activation patterns for individual known and unknown test images would directly test the hypothesis that unknown instances produce different activation signatures.

- **No failure analysis.** When DIFAIR misclassifies an unknown as known (or vice versa), the representation is not examined. This could directly test the paper's hypothesis about "which features are activated."

- **No standard deviations reported.** Results are averaged over 5 splits without confidence intervals or standard deviations, making it difficult to assess whether observed differences between methods are meaningful.

### Trivial

- None that survive filtering (the paper is competently written and presented).

## Nice-to-Haves

- A redesign of the loss function to encourage diversity among dimensions of the same class — e.g., a decorrelation penalty, variance maximization, or a sparsity-inducing term. The paper identifies this as future work; addressing it would substantially strengthen the contribution.
- Incorporating MOS-like magnitude scoring directly into the loss (as the paper mentions in Section 5.2 as ongoing investigation).

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

- **"The paper does not engage with prior definitions of interpretability / does not mention ProtoPNet or concept bottleneck models."** Removed: This is a missing-related-work critique. The paper is about OSR, not general-purpose interpretability, and the critic does not demonstrate how these specific works are essential to DIFAIR's argument.

- **"The paper does not discuss the connection to broader interpretability literature."** Removed: Same rationale — scope creep beyond the paper's OSR framing.

- **"The chosen r=0.4 of inter-anchor distance is arbitrary."** Demoted to minor (hyperparameter sensitivity). The paper actually provides a rationale: it allocates 40% of the inter-anchor distance to each hypersphere, leaving 20% for unknown data (line 123). The real issue is the lack of ablation, not arbitrariness.

- **"Missing appendix / missing proofs in appendix."** Removed per instructions: appendix content is stripped by the parser and exists in the original submission.

- **Strength Finder: "Clear hypothesis linking feature presence to OSR."** Kept as a core strength. However, the associated "Figure 1 provides a schematic of this desired behavior" detail is noted; the figure does visually articulate the goal.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any interpretation of the paper's results that the authors themselves did not already articulate (the feature duplication issue is discussed in Sections 5.1–5.2, and the trade-off between OSR performance and semantic flexibility is discussed in Section 4). The main novel observation from the reviews — that the loss function lacks any differentiation incentive — is implicit in the paper's own admission but made more explicit by the critic.

## Suggestions

1. **Address the feature duplication problem directly** before claiming differentiated representations. This could involve adding a variance-maximization or decorrelation term across dimensions of the same class, or reformulating the loss to encourage sparse, one-hot-like activation patterns within a class's allocated dimensions.

2. **Add at least one quantitative interpretability metric** — e.g., within-class dimension correlation, sparsity (fraction of near-zero dimensions per instance), or alignment with human-annotated visual concepts. Without this, the interpretability claim remains untestable.

3. **Report closed-set accuracy** and include standard deviations over the 5 splits to allow readers to assess statistical reliability.

4. **Provide per-instance visualizations** of representations for known and unknown test images to qualitatively validate the hypothesis about feature activation patterns.
