Now I have all the evidence I need. Let me produce the consolidated final review.

## Summary

This paper identifies a fundamental ambiguity in the standard definition of "semantic shift" for OOD detection: whether a shift counts as "semantic" depends on the granularity of the training labels. The authors formalize this by defining a **Semantic Space** (span of differences between ID class means) and a **Covariate Space** (its orthogonal complement). They prove that, under a Gaussian-linear setting, a trained classifier's output becomes identical for any two distributions whose projections onto the Semantic Space coincide, rendering post-hoc OOD detection intractable. They propose a **"Tractable OOD"** definition requiring a minimum Semantic-Space distance, and validate their theory on both synthetic Gaussians and a carefully crafted ImageNet-dog experiment where breed-specific features shift from Semantic to Covariate space depending on training label aggregation.

---

## Strengths

- **Precise, actionable formalization of Semantic and Covariate Spaces (Definitions 1, 2, Proposition 1).** Prior work uses "semantic shift" informally. This paper ties Semantic Space directly to ID class-mean differences, giving a rigorous decomposition. Proposition 1 shows that Covariate-Space components of all ID class means are constant, which grounds the intuition that variations in that subspace should not affect classification.

- **Theorem 1 provides a clean theoretical explanation for a real failure mode.** It proves that, under Gaussian distributions with identity covariance and a linear classifier, if two distributions have identical Semantic-Space projections, their output distributions (via softmax) have zero KL divergence. This connects a formal mathematical condition to the practical observation that certain OOD classes become undetectable — e.g., novel dog breeds under aggregated training.

- **The "Tractable OOD" definition (Definition 4) replaces a vague notion with a measurable condition.** Instead of requiring a minimum Euclidean distance in input space (which can be satisfied by Covariate-Space shifts that are undetectable), it requires a minimum distance *in Semantic Space*. Table 1 (synthetic) and Table 2 (ImageNet) validate that this condition tracks actual detectability.

- **The ImageNet-dog experiment (Table 2) is well-designed and convincing.** It uses 10 different post-hoc methods (MSP, ODIN, EBO, GradNorm, RMDS, KNN, DICE, ASH, Relation, SCALE) across two training setups. Under breed-separated training, AUROCs on OOD-breed reach ~70-75%; under breed-aggregated training, every method drops to ~50% (chance). Under breed-aggregated training, the same methods still achieve ~77-82% on OOD-object. This clean within-experiment control elegantly isolates the role of training-label granularity.

---

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claim — that OOD detection can become intractable when the shift lies entirely in the Covariate Space defined by training-label structure — is well-supported by both theory and experiments. The limitations are acknowledged and partially addressed empirically.

### Minor

- **Corollary 1 overclaims relative to what Theorem 1 proves.** The corollary states that if the OOD representative feature vector matches an ID class's in Semantic Space, "it becomes intractable for *any* post-hoc OOD detection method to identify the class." Theorem 1 only proves that the *classifier's softmax output distribution* is identical — which directly covers score-based methods (MSP, EBO, ODIN, etc.) but does not theoretically cover methods that operate on penultimate-layer features (KNN, RMDS). The remark after Corollary 1 correctly qualifies this to "methods based on the classifier's output," but the Corollary statement itself is unqualified. This is a minor framing issue: the *experiments* show KNN and RMDS do fail (Table 2: ~48-50% AUROC), so the empirical claim holds, but the theoretical framing slightly overreaches.

- **The theoretical analysis assumes Gaussian distributions with *identity* covariance, which equates class covariances.** The Semantic Space is defined purely from class-mean differences. In realistic settings where class covariances differ, the optimal classifier (or a deep network) can exploit covariance structure that has nonzero components in the Covariate Space. This means the "tractable" condition (Definition 4, requiring only Semantic-Space distance) may be neither necessary nor sufficient under non-isotropic covariances. The authors acknowledge this in the limitations paragraph, but the paper's formal definitions do not address it, and the experiments (ImageNet) do not directly test whether covariance differences could be exploited to detect OOD samples that are indistinguishable by their means alone.

- **The breed-separated baseline achieves only ~70-75% AUROC, not near ceiling.** While the critical comparison is the *drop* to ~50% under breed-aggregated training, the fact that even the "good" setup leaves substantial room for improvement is worth brief discussion. The paper does not comment on whether this reflects inherent difficulty of the task or limitations of the methods — a sentence would help readers calibrate expectations.

### Trivial

None.

---

## Nice-to-Haves

- Include FPR95 or AUPR in addition to AUROC for the ImageNet experiment (standard in safety-critical OOD evaluation).
- Show the same phenomenon with at least one additional backbone (e.g., ViT) or dataset (e.g., CIFAR-100 with coarse/fine labels) to further demonstrate generality beyond ResNet-18 / ImageNet.
- Provide a practical algorithm to estimate the Semantic Space rank *r* from a trained model (e.g., PCA on class-mean differences), and verify that for the ImageNet breed-aggregated setup the OOD-dog means indeed have near-zero Semantic-Space projection.

---

## Removed Points

These points were flagged for removal; treat with caution:

1. **"Definition numbering jumps from 2 to 4."** This is almost certainly a parser artifact (Definition 3 existed in the original submission's appendix, which the parser strips). Per the hard rules, formatting artifacts from PDF extraction are not paper errors.
2. **"The breed-separated baseline only achieves ~73-75%, not 100%."** The paper never claims the baseline should be 100%. The relevant comparison is the *relative* drop to ~50% under breed-aggregated training. This is an observation, not a weakness.
3. **Missing related works, extra architectures/datasets as "missing" (beyond what was noted in Nice-to-Haves).** The paper scopes itself appropriately; demanding a broader scope is outside its stated goals.
4. **Criticisms about missing appendix content or deferred proofs.** The parser strips appendix sections; they exist in the original submission.

---

## Novel Insights

The reviews surface one insight the paper itself does not fully articulate: the Semantic/Covariate decomposition is *label-dependent* in a way that interacts with dataset construction practices. Many existing OOD benchmarks (e.g., CIFAR-100 vs. SVHN, or ImageNet-1K vs. textures) may unintentionally place the OOD shift in Semantic Space simply because the training and test classes are from entirely different domains. The paper's analysis suggests that the hardest — and perhaps most practically relevant — OOD scenarios are those where the OOD classes *share a supercategory with ID classes* (novel dog breeds, new car models, unseen bird species), because these shifts may land in Covariate Space depending on how the ID labels are defined. Future benchmark design should account for this.

---

## Suggestions

1. **Qualify Corollary 1** to read "any post-hoc OOD detection method *that operates on the classifier's output scores*." The experiments already cover feature-based methods, so the practical claim is unchanged.
2. **Add a short discussion** acknowledging that under non-isotropic covariances, class-mean differences alone may not fully characterize detectability, and that Definition 4 assumes isotropic covariances for tractability.
3. **Briefly comment** on why the breed-separated baseline is ~70-75% rather than near-perfect — even a sentence noting this is likely due to the inherent difficulty of fine-grained breed discrimination helps readers interpret results.
4. **Optionally include FPR95** in the ImageNet experiments as a supplementary metric.

---

## Score and Decision

This is a conceptually clean, well-written paper that identifies a real flaw in OOD detection definitions, formalizes it rigorously, and validates the formalization with carefully designed experiments. The theoretical assumptions are acknowledged simplifications, and the empirical work credibly shows the phenomenon extends beyond those simplifications. The weaknesses are minor framing issues and acknowledged limitations, none of which threaten the core contribution.

**Score: 8.0**

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>