Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper studies the effect of noise injection in deep learning models through the lens of information entropy. It defines "task complexity" via joint entropy between labels and features, classifies noise into "positive" (reducing task complexity) vs. "harmful" (increasing it), and proposes NoisyNN — injecting linear transform noise (circular shift) into the latent space of CNNs and ViTs. The paper claims experimental results including 89.99% on ImageNet with ViT-B (+5.66% gain) and 95.65% using a theoretically derived "optimal quality matrix."

## Strengths

- **Ablation study on noise strength and injection layer** (Fig. 2): The paper systematically varies the noise parameter α and the injection layer depth across both CNN and ViT families, showing clear trends that deeper layers and moderate noise strengths yield better results. This provides useful empirical guidance for practitioners.

- **Validation on diverse architectures and tasks**: The positive noise (circular shift) is tested across multiple ResNet scales (18/34/50/101), ViT scales (T/S/B/L), ViT variants (DeiT, Swin, BEiT, ConViT), and extended to domain adaptation benchmarks (Office-Home, VisDA2017) with consistent improvements. This breadth suggests the phenomenon is not architecture-specific.

- **Clear differentiation from related work**: The paper explicitly distinguishes NoisyNN from Manifold MixUp (label interpolation vs. label-preserving) and positions it relative to Li2022Positive (extending from image-space to embedding-space), giving the reader a clear sense of what is new.

## Weaknesses

### Fatal

**1. The optimal Q matrix produces a degenerate transformation that would make classification impossible, yet is claimed to yield 95.65% accuracy.**

The derived optimal quality matrix (Eq. 374) is:

\[
Q_{\text{optimal}} = \operatorname{diag}\!\left(\frac{1}{k+1}-1, \ldots, \frac{1}{k+1}-1\right) + \frac{1}{k+1} \mathbf{1}_{k\times k}
\]

where the paper explicitly states \(k\) is the number of data samples (~1.2M for ImageNet). The corresponding transformation \((I+Q)\boldsymbol{Z}\) applied to the data matrix \(\boldsymbol{Z}\) (size \(k \times d\)) yields:

\[
((I+Q)\boldsymbol{Z})_i = \frac{1}{k+1}\boldsymbol{Z}_i + \frac{k}{k+1}\operatorname{mean}(\boldsymbol{Z})
\]

For \(k = 1.2\times 10^6\), the coefficient \(1/(k+1) \approx 8\times 10^{-7}\). Every single training sample's embedding becomes approximately the global mean vector — all discriminative information is obliterated. It is **theoretically impossible** for this transformation to support 95.65% ImageNet top-1 accuracy. The paper provides no explanation of how this Q was implemented at ImageNet scale (a full \(k\times k\) matrix is \(\sim 10^{12}\) entries), nor any reconciliation between the mathematical form of the optimal Q and the claimed result. This alone invalidates the paper's central experimental claim.

**2. The "task complexity" framework conflates feature compression with task difficulty, and the sign of the theory is at odds with the intended interpretation.**

The paper defines task complexity as \(H(\mathcal{T};\boldsymbol{Z}) = H(\boldsymbol{Y};\boldsymbol{Z}) - H(\boldsymbol{Z})\), where \(H(\boldsymbol{Y};\boldsymbol{Z})\) is the joint entropy (despite the semicolon notation being non-standard and never explicitly defined). Crucially, after noise injection, the definition keeps \(H(\boldsymbol{Z})\) fixed (Eq. 139 uses \(H(\boldsymbol{Z})\), not \(H(\boldsymbol{Z}+Q\boldsymbol{Z})\)).  

This definitional choice leads to \(\Delta S = -\log|I+Q|\) — a quantity that depends **only** on the transformation matrix \(Q\) and not at all on the relationship between features \(\boldsymbol{Z}\) and labels \(\boldsymbol{Y}\). The paper's classification of noise as "positive" (\(\Delta S > 0\)) or "harmful" (\(\Delta S \leq 0\)) is therefore independent of the actual prediction task. A noise that compresses the feature space (making \(|\!I\!+\!Q\!| < 1\)) is called "positive" regardless of whether it helps or hurts classification. The paper never acknowledges this conceptual issue or provides a justification for why feature compression alone should correspond to reduced task difficulty. The claimed mechanism — that positive noise "reduces task complexity" — conflates two distinct quantities (feature entropy change and conditional predictive uncertainty) without disentangling them.

### Major

**3. The experimental gains are extraordinary and presented without sufficient detail for verification.**

The reported improvements — ResNet-50 +11.32% (Table 1), ViT-B +5.66% (Table 2), and especially the 95.65% with optimal Q (Table 6) — are far beyond anything reported in the literature for similar model scales. Yet the paper provides none of the following: optimizer choice, learning rate schedule, number of epochs, batch size, weight decay, or training/validation protocol. For ViT models, data augmentation settings are unspecified. The ResNet experiments are stated to use "no data augmentation," which produces baselines (70.00% for ResNet-50) well below standard reported numbers (~76%), making the relative gains misleading. Without these details, the experimental claims cannot be independently assessed.

**4. The circular-shift noise and the optimal Q derivation are disconnected.**

The paper's actually implemented method (circular shift, Eq. 247) is a heuristic construction introduced after the theoretical derivation. There is no argument or proof that the circular shift satisfies the optimization constraints (Eq. 190–198) or that it is a practical approximation of the optimal Q. The paper does not explain why shifting each embedding toward its immediate neighbor constitutes "positive" noise under the theory, or how the hyperparameter \(\alpha\) relates to the derived entropy bound. The experiments therefore float free of the theoretical framework: the theory says nothing about circular shifts, and the circular shifts contribute nothing to validating the theory.

### Minor

- **Non-standard notation**: The notation \(H(\boldsymbol{Y};\boldsymbol{Z})\) (with semicolon) is never defined in the preliminary section. From context it is used as joint entropy, but the paper defines \(H(x,y)\) for joint entropy (which would be standard) and never bridges the two notations. This creates ambiguity.

- **Moderate Model Assumption (line 104)**: Introduced but never operationalized. No experiment tests whether the model is "overfitting" before deciding whether positive noise should be applied. It reads as a post-hoc hedge.

- **Inconsistent baseline comparisons**: Table 3 (ViTcompare) compares NoisyViT-B at 384×384 against models trained at various resolutions with different pretraining data (including private JFT). The paper notes that JFT is private but does not control for equal training conditions.

### Trivial

- Typo in Eq. 184: \(\boldsymbol{\Sigma_{XY}}\) should likely be \(\boldsymbol{\Sigma_{ZY}}\) for consistency.
- The text references "section 4.4" (line 355) in a way that doesn't clearly correspond to any section in the main paper.

## Nice-to-Haves

- Compare against standard noise-based regularizers (dropout, Gaussian dropout, stochastic depth) under the same training setup to isolate whether the gains are truly from "positive noise" or from any regularizing perturbation.
- Evaluate on small synthetic datasets where the Gaussian assumptions actually hold to validate the theory before scaling to ImageNet.
- Train baselines under identical conditions (same optimizer, resolution, augmentation) for fair comparison.
- Clarify whether \(k\) in the optimal Q formula could instead be the embedding dimension or batch size, and if so, how the experimental results were obtained with the corrected interpretation.

## Removed Points

*The following points from the reviews were removed with justification:*

- **"The theoretical derivation (Eq. 184–186) is algebraically incorrect"** (Harsh Critic, item 1). The derivation is algebraically consistent with the paper's stated definitions (keeping \(H(\boldsymbol{Z})\) fixed post-noise). The specific claim that the conditional covariance cancellation is unjustified is factually wrong: for invertible \((I+Q)\), \(\Sigma_{Y|(I+Q)Z} = \Sigma_{Y|Z}\) is a standard result. The real problem is a *conceptual* definitional issue (see Fatal Weakness 2), not an algebraic error.
- **"Gaussian noise derivation's Box-Cox transform is invoked without justification"** (Harsh Critic, item 4). The paper cites Box (1964) and Feng (2014) — standard references for normalizing transformations. This is sufficient justification in context.
- **"Moderate Model Assumption is never used"** (Harsh Critic, Other Observations). This is true but is a minor omission, not a structural weakness. Moved to Minor.
- **"Notation inconsistency between Eq. 1 and Eq. 5"** (Harsh Critic, Other Observations). Eq. 1 (\ref{MI}) does not use semicolon notation at all — it writes \(MI(x,y) = H(x) - H(x|y)\). The critic misread the equation.
- **Several generic formatting/style nitpicks** and claims about "missing appendix content" removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. While the decomposition of noise effects via entropy change is a framing borrowed from Li2022Positive, and the circular-shift heuristic is a practical construction, the paper does not produce a genuinely novel theoretical insight that withstands scrutiny. The key conceptual problem (that the "positive noise" criterion is independent of the label-feature relationship) is not discussed, let alone resolved.

## Suggestions

1. **Re-examine the task complexity definition**: The choice to keep \(H(\boldsymbol{Z})\) fixed after noise (Eq. 139) needs rigorous justification, or the framework should be rebuilt around a more standard information-theoretic objective (e.g., directly maximizing \(I(\boldsymbol{Z};\boldsymbol{Y})\) or minimizing \(H(\boldsymbol{Y}|\boldsymbol{Z})\) under a capacity constraint).

2. **Provide a practical, feasible implementation of the optimal Q or acknowledge its impracticality**: If \(k\) in Eq. 374 is the number of data samples, the resulting transformation is degenerate for large-scale datasets and the 95.65% claim cannot stand without a detailed and plausible implementation. If the paper intended a different interpretation of \(k\), this must be clarified immediately.

3. **Release full training configurations and code**: The extraordinary empirical claims (+11% on ResNet-50, 95.65% on ImageNet) require open, reproducible experimental setups to be taken seriously by the community.

4. **Bridge the theory-experiment gap**: Show analytically that the circular-shift construction satisfies the optimization constraints (Eq. 190–198), or present an alternative experiment that directly tests the theoretical predictions (e.g., on small controlled data where the Gaussian assumptions hold).

## Score and Decision

The paper has a fatal structural problem: the derived optimal Q produces a transformation that, when analyzed algebraically, destroys discriminative information yet is claimed to yield state-of-the-art results. Additionally, the theoretical framework conflates feature compression with task difficulty in a way that is not acknowledged or justified. The experimental gains are extraordinary and lack the basic details needed for verification. These issues are not addressable through a rebuttal — they require either fundamentally reworking the theory or providing a completely new set of explained, reproducible experiments. The paper should not be accepted in its current form.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>