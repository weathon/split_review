Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper identifies a fundamental problem in the widely used Concept Activation Vector (CAV) framework: linear classifiers (filters) used to compute CAVs optimize class separability, which causes them to conflate concept signals with distractor directions. The authors introduce pattern-based CAVs, derived from the neuroimaging literature (Haufe et al., 2014), which directly estimate the signal pattern via covariance between activations and concept labels rather than optimizing separability. Through controlled experiments on ISIC2019, Bone Age, and FunnyBirds datasets across VGG16, ResNet18, and EfficientNet-B0 architectures, they demonstrate that pattern-based CAVs achieve consistently better alignment with true concept directions and improve downstream applications (TCAV and ClArC-based model correction).

## Strengths

1. **Principled derivation from a signal-distractor decomposition**: The paper formalizes the limitation of filter-based CAVs by connecting to established work in neuroimaging (Haufe et al., 2014), showing why optimizing separability conflates signal and distractor patterns. The pattern-based CAV is derived via a simple regression formulation (Eq. 2–4) that directly estimates the signal pattern rather than the separating hyperplane, providing a clean theoretical foundation.

2. **Consistently superior alignment across architectures, layers, and datasets**: In controlled experiments with known ground-truth concept directions, pattern-based CAVs achieve significantly higher cosine similarity to the true direction across all 13 convolutional layers of VGG16 on ISIC2019, Bone Age, and FunnyBirds datasets (Fig. 3). This directly supports the core claim that pattern-based CAVs more precisely estimate concept signal directions.

3. **Demonstrated practical impact on TCAV and ClArC applications**: Pattern-based CAVs lead to correct TCAV scores invariant to distractor rotation in 2D toy experiments (Fig. 5), while filter-based CAVs produce arbitrary scores. In model correction with RR-ClArC, pattern-based CAVs consistently achieve higher accuracy on biased test sets and lower artifact relevance across three architectures for both controlled and real-world artifacts (Table 1).

4. **Invariance to feature preprocessing and no hyperparameter tuning**: Figure 4 demonstrates that pattern-based CAVs maintain high alignment regardless of centering, max-scaling, or no preprocessing, while filter-based CAVs are sensitive to these choices. Pattern-based CAVs also require no regularization parameter tuning, making them more robust and efficient in practice.

5. **Honest discussion of limitations and task-dependent suitability**: The paper explicitly acknowledges (Sec. 4.3.3) that for applications requiring class separability (e.g., post-hoc concept bottleneck models), filter-based CAVs may be preferable. This balanced treatment strengthens the credibility of the contribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ground-truth concept direction is an imperfect target that conflates signal with insertion artifacts.** The paper defines $\mathbf{h}_{\text{gt}} = \mathbf{a}(\mathbf{x}_{\text{att}}) - \mathbf{a}(\mathbf{x})$ as the difference between latent activations of attacked and original samples (line 336). This difference captures not only the intended conceptual signal but also incidental activation changes caused by the insertion mechanism — edge artifacts from text overlays, global brightness shifts, or interactions between the inserted feature and existing features. The paper treats this as pure ground truth without acknowledging that it is itself a potentially noisy proxy. While this does **not** invalidate the relative comparison (pattern outperforms filter on this proxy), and the downstream TCAV/ClArC results provide independent validation, the paper should explicitly caveat this. *Relevant: lines 207–208, 336.*

2. **The ResNet18 anomaly in the TCAV experiment is mentioned but not discussed.** The paper states (line 292): "Interestingly, all CAV variants achieve a perfect score for ResNet18." This observation — that filter-based CAVs already achieve near-optimal TCAV scores on ResNet18, unlike VGG16 and EfficientNet-B0 — raises important questions about architecture-dependent benefit. Possible explanations (different latent space geometry, more separable concept representations, or layer choice effects) are not explored. This is a missed opportunity to either strengthen the paper's argument or qualify its scope. *Relevant: lines 291–292, Fig. 6 caption.*

3. **The assumption of uncorrelated distractors is not tested or discussed.** The pattern-CAV derivation (Eq. 2) uses OLS to recover the signal pattern under a model $A = p_s t + \text{distractor}$. The OLS estimate $\hat{p}_s = \text{cov}[A, t] / \sigma_t^2$ is unbiased only when the distractor is uncorrelated with $t$. If distractors (including features of other concepts) are correlated with $t$ — a common situation in real data — the covariance estimate absorbs that correlated component into the pattern estimate. The paper acknowledges (line 108) that "any information unrelated to concept label $t$ is considered a distractor," but does not probe the regime where distractors are correlated with $t$. A controlled experiment varying distractor-label correlation would clarify the method's boundary conditions. *Relevant: lines 114–136.*

4. **Computational efficiency claim lacks quantitative support.** The paper states (line 225) that pattern-CAVs are "more computationally efficient" but provides no wall-clock time or iteration counts. A simple comparison of fitting time per CAV across methods would quantitatively support this claim. *Relevant: line 225.*

### Trivial

- The standard error estimation for the alignment metric (cosine similarity) is not described. The paper (lines 215–216) explains standard error estimation for AUC scores (via Wilcoxon-Mann-Whitney) but not for the alignment measure in Fig. 3/4. Clarification would help.

## Nice-to-Haves

- **Analysis of pattern-CAV stability under low-data regimes**: The paper notes filter-CAV sensitivity to regularization and seeds with few samples but does not evaluate pattern-CAV's behavior under the same conditions. Since the pattern-CAV estimate is a sample covariance, its variance scales as $1/n$, and a small experiment varying concept sample size would be informative.

- **Discussion of nonlinear concept representations**: Both CAV types rely on linear separability. While the paper mentions this in related work (line 70–71), a brief caveat about what happens when concepts are not linearly encoded (e.g., living on a nonlinear manifold) would strengthen the paper. This is a shared limitation and does not affect the relative comparison.

- **Evidence for the post-hoc bottleneck model claim**: The limitations section argues (lines 387–390) that filter-CAVs are preferable for post-hoc concept bottleneck models because the linear classifier can handle directional divergence. This reasoning is logical but stated without supporting evidence or citation. Even a reference to prior empirical work would strengthen the discussion.

- **The ClArC gains on real-world artifacts are marginal**: The paper acknowledges this (lines 348–349: "all CAVs yield similar accuracy scores") but a more nuanced statement would be appropriate: pattern-CAV shows consistent directional benefits, but on weak artifacts these translate into only marginal empirical gains.

## Removed Points

- **"Standard errors not described"**: The critic claimed standard errors in Fig. 4 are not described. However, the paper states they are included (line 215: "including standard errors, for both CAV alignment [...] and separability"). The estimation method is described for AUC but the error bars themselves are present. This is a misreading of the paper. *Removed as factually incorrect.*

- **"The paper should also cover correlated distractors more extensively"**: Some aspects of this criticism are downgraded from the critic's framing as a major issue. The correlated-distractor concern is a valid theoretical point but the relative comparison (pattern vs. filter) is robust to it — both methods would be affected, and the paper's experiments span realistic settings where pattern-CAV still outperforms filter-CAV. Kept as a minor weakness rather than a major one.

- **"The paper should add more datasets / domains"**: This would turn the paper into a broader survey rather than a stronger methods paper. The three datasets and three architectures already provide sufficient evidence for the core claim. *Removed as scope creep.*

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight that the paper itself does not already articulate.

## Suggestions

1. Add an explicit caveat in Section 3.2 (or Section 4) that $\mathbf{h}_{\text{gt}}$ is an approximate target that may capture incidental changes from the insertion mechanism, and that the downstream TCAV/ClArC results provide complementary validation.

2. Add a brief discussion of the ResNet18 result: speculate on possible reasons (e.g., differences in latent space geometry, whether ResNet18 learns more separable concept representations at the last conv layer) and note that the benefit of pattern-CAV may be architecture-dependent.

3. Provide a simple diagnostic or heuristic (e.g., the alignment ratio between filter and pattern CAVs on a held-out set) that practitioners can use to predict whether switching to pattern-CAV will matter for their setting.

4. Include a small experiment or at minimum a more detailed discussion of what happens when distractors are correlated with the concept label, clarifying the boundary conditions of the method.

5. Add wall-clock fitting time comparison to support the efficiency claim.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>