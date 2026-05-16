Now I have a thorough understanding of the paper. Let me produce the final review.

## Summary

This paper proposes CONTROL, a framework that adds three contrastive losses (supervised, nearest-neighbor, unsupervised) to existing BCE-based open-world semi-supervised learning methods like ORCA and NACH. The authors claim a theoretical justification that contrastive losses are more robust to misaligned pairs than BCE loss, and that uniformity in contrastive learning prevents representation collapse. Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show improvements over the base methods, with the largest gains on CIFAR-100 (+6.4% unseen classes).

## Strengths

- **Significant and consistent empirical gains on CIFAR-100**: Table 1 reports a 6.4% improvement in unseen-class accuracy and 2.1% all-class accuracy when CONTROL is added to NACH, and 11.8% unseen-class / 9% all-class improvement over ORCA. These are nontrivial improvements on a standard benchmark that demonstrate practical value.

- **Mechanistic analysis linking the method to its hypothesized effect**: Table 4 directly measures that CONTROL increases the ratio of unseen-unseen nearest-neighbor pairs (+2.35%) and the ratio of unseen-class predictions (+2.77%). This provides a concrete explanation for why feature-level alignment translates to better unseen-class classification—a stronger form of analysis than typical ablation studies.

- **Ablation study validating individual loss components**: Table 3 shows that each of the three contrastive losses contributes to the overall improvement, with the combination of L_SupSeen + L_SimAll yielding +2.7% unseen classes and adding L_SupNN further boosting unseen classes by 2.6%. This decomposition supports the design choice.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical analysis in Section 4.1 is not mathematically rigorous and does not support the paper's central claims.** The derivation contains unjustified steps that undermine both the BCE-loss analysis and the contrastive-loss analysis:
  - **BCE analysis**: The paper claims that under independent samples, $g(\phi(x))^\top g(\phi(v)) = 0$ and therefore $M \to -\infty$. This is not generally true. For softmax probability vectors (which $g$ outputs), the inner product of independent random vectors is not zero; under a uniform predictor it would be approximately $1/C$, giving a finite value. The paper provides no justification for why these vectors would be orthogonal.
  - **Contrastive analysis**: The derivation claims that $\mathbb{E}_{x\sim P_X}\mathbb{E}_{v^+\sim P_V}[-\phi(x)^\top\cdot\phi(v^+)/\tau] + \mathbb{E}_{x\sim P_X}\mathbb{E}_{v^-\sim P_V}[\log\sum\exp(\phi(x)^\top\cdot\phi(v^-)/\tau)]$ simplifies to $\log(|\mathcal{N}(x)|)$ "because $\phi(x), \phi(v^+), \phi(v^-)$ are independent." Independence alone does not make the first term vanish (the expected inner product of independent unit vectors is not zero in general) nor does it make the log-sum-exp collapse to $\log(|N|)$. The simplification requires strong assumptions (uniformity of features on the sphere, equal logits for all negatives) that are not stated and do not hold during training.
  
  Because the paper frames this theoretical argument as its central motivation ("we theoretically prove that optimization of contrastive learning at the feature level benefits unseen classification" — abstract, contributions), this flaw is a structural weakness rather than a missing detail.

- **Claims of broad generality are not supported by the experiments.** The abstract states CONTROL is "compatible with a broad range of existing open-world semi-supervised learning algorithms," and Section 4.4 describes a "replaceable open-world semi-supervised learning module." However, experiments only combine CONTROL with two BCE-based methods (ORCA and NACH). No results are shown with the non-BCE methods the paper itself discusses (OpenLDN, TRSSL) or with OpenCON used as the base module. Without broader validation, the paper reads as a targeted improvement for BCE-based methods rather than a general framework, and the compatibility claim is unsubstantiated.

### Minor

- **The paper makes an unsubstantiated claim about OpenCON.** At line 31, the paper states OpenCON "is incapable of sustaining continuous optimization of representations during the process of semi-supervised learning" without providing any citation, analysis, or experimental evidence. OpenCON uses contrastive learning throughout training, so this assertion needs support or should be removed.

- **The empirical gains are inconsistent across settings, and the method adds meaningful complexity.** On CIFAR-10, the improvement over NACH is only +0.4% all classes and +0.3% for ORCA—gains that are small enough to be within run-to-run variation (no error bars are reported). On ImageNet-100, the gains are modest (+0.7% all classes for NACH). The method adds three extra losses with three λ hyperparameters, a temperature parameter, and a nearest-neighbor lookup mechanism, yet the paper provides no sensitivity analysis for these hyperparameters. The practical significance of small gains given this added complexity is unclear.

- **The paper has no discussion of limitations.** There is no section or paragraph discussing when CONTROL might fail, whether it requires larger batch sizes, how it affects training time, or whether certain dataset characteristics make it more or less effective. This omission makes the paper less useful as a reference for practitioners.

- **The claim that "performance improvement for all class classifications primarily comes from the uniformity component" (Section 5.2) is not directly supported by the ablation.** The ablation in Table 3 combines L_SupSeen (supervised contrastive, which provides both alignment and uniformity) with L_SimAll (unsupervised contrastive, also providing both). The improvement could come from alignment effects, and the study does not isolate the uniformity mechanism separately (e.g., by adding only a uniformity regularizer without alignment).

### Trivial

- **BCE loss notation ambiguity**: In Section 3.2, $p(x)$ is used in the BCE loss formula $-\log(p(x)^\top p(\tilde{x}))$ without clarifying whether $p$ represents softmax probabilities or logits. The notation is resolved later in Section 4.1 with $g(\cdot)$ for logits, but the earlier usage could confuse readers.

## Nice-to-Haves

- A hyperparameter sensitivity analysis for the three λ weights and the temperature $\tau$ would help assess whether the reported gains are robust or fragile.
- Error bars or standard deviations in all tables would help assess significance, especially for the small CIFAR-10 gains.
- Additional ablation isolating the uniformity effect from alignment (e.g., using the decomposition from Wang & Isola 2020 directly as a loss term).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing experimental details (batch size, epochs, learning rate)"**: Per instructions, hyperparameter implementation details stripped by the parser are assumed to exist in the original submission.
- **"The method is a straightforward combination of existing contrastive losses" / "incremental contribution"**: While this is a fair opinion on novelty level, it overlaps with other verified weaknesses and is too subjective to carry weight as a standalone criticism; the paper's empirical results indicate genuine practical value beyond what is trivial.
- **Strength Finder's "Theoretical justification" claim**: This conflicts with the verified weakness that the theory is not rigorous; per rules, when strength and weakness disagree, weakness wins.
- **Strength Finder's "Generality and compatibility" claim**: This conflicts with the verified weakness about narrow empirical scope.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful meta-point: when a paper's theoretical derivation relies on distributional assumptions that are not checked against actual training dynamics (e.g., independence of features, zero inner-product of independent softmax outputs), the claimed theoretical motivation can be more of a rhetorical device than a genuine proof. The paper's empirical contribution—that adding contrastive regularizers helps BCE-based open-world SSL—may well be valid independently of the theory, but the paper would be stronger and more honest if presented as an empirical finding rather than a theoretically grounded framework. The mechanistic analysis in Table 4 (showing increased unseen-unseen pair ratios) is actually the most compelling support for the method's effectiveness, and it doesn't depend on the flawed theory at all.

## Suggestions

1. Remove or substantially rewrite the theoretical analysis in Section 4.1. The current derivation cannot be salvaged by clarifications; the key claims about BCE loss diverging to $-\infty$ and contrastive loss simplifying to a constant are simply not provable under the stated assumptions. Consider either (a) presenting the method as an empirically motivated approach without theoretical guarantees, or (b) replacing the flawed analysis with a correct argument (e.g., noting that contrastive loss is bounded while BCE loss on probability vectors is not, or providing a properly derived bound).
2. Scale back the generality claims. Either replace "broad range of existing algorithms" with "BCE-based methods such as ORCA and NACH," or add experiments with at least one non-BCE method (e.g., OpenLDN) to substantiate the claim.
3. Add a limitations paragraph discussing computational cost, hyperparameter sensitivity, and settings where the method may not help.
4. Add error bars/standard deviations to all tables.
5. Remove or substantiate the unsupported claim about OpenCON's limitations.

## Score and Decision

The paper has genuine empirical value—the CIFAR-100 gains are notable, and the mechanistic analysis in Table 4 is well-designed. However, the theoretical analysis that the paper presents as a central contribution is not mathematically sound, and the claims of broad generality are overstated relative to the evidence. These are not minor issues; they directly affect how the paper's contributions should be evaluated. The paper would need substantial revision (fixing the theory or dropping it, broadening the experiments, scaling back the claims) to meet the standard for a competitive venue. In its current form, it does not meet that standard.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>