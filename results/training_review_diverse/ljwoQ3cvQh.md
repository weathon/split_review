I've now thoroughly read the paper and verified claims. Let me construct the final review.

---

## Summary

This paper makes the empirical observation that as inputs become increasingly out-of-distribution (OOD), neural network predictions tend to converge toward the Optimal Constant Solution (OCS) — the best constant prediction achievable without observing the input. The authors demonstrate this phenomenon across 8 datasets, 3 loss functions (cross-entropy, MSE, Gaussian NLL), and multiple architectures (ResNet, VGG, DistilBERT). They propose a mechanism (OOD features have smaller norms → output dominated by accumulated bias terms → bias approximates OCS), support it with both empirical analysis and theoretical results in a simplified setting, and illustrate a practical application to risk-sensitive selective classification.

## Strengths

- **Comprehensive empirical validation of the reversion-to-OCS phenomenon.** The paper demonstrates this behavior across 8 datasets with both synthetic and natural distribution shifts, 3 loss functions, both vision and text modalities, and CNNs and transformers. Figure 3 shows a clear monotonic relationship between an independent OOD score and prediction-OCS distance across all settings, with standard deviations over 5 runs. This breadth of evidence strongly supports the paper's central observational claim.

- **Generalization beyond prior work.** The paper extends earlier observations about softmax confidence decreasing on OOD inputs (Hendrycks & Gimpel, 2016) to arbitrary loss functions and continuous outputs. The Gaussian NLL case (where predicted variance *increases* OOD) is particularly compelling because it cannot be explained by a simple decrease in output magnitude, isolating the OCS reversion mechanism.

- **Clear, practical demonstration of how loss function choice affects OOD behavior.** The selective classification experiments cleanly illustrate that by designing the loss function so the OCS aligns with a cautious default action (abstention), the model automatically becomes more conservative on OOD inputs. This is a non-obvious design principle with direct practical relevance. The paper is appropriately measured, stating explicitly that the goal is not SOTA selective classification but illustrating the OCS effect.

## Weaknesses

### Major

1. **The evidence for the bias-approximates-OCS mechanism is limited.** The paper's mechanistic explanation has two parts: (i) OOD inputs produce smaller-magnitude layer activations, and (ii) accumulated bias terms approximate the OCS. Part (i) is reasonably supported (columns 1–2 of Figure 4, showing feature norm and subspace alignment decrease with shift). However, part (ii) is supported by only two data points: a single layer in two models (MNIST 4-layer net and CIFAR10 ResNet-20), for two loss functions (CE and MSE), shown in columns 3–4 of Figure 4. This is a narrow demonstration for what the paper frames as a general mechanism. The paper does not examine whether this approximation holds systematically across different architectures, layers, or depths. The theoretical result (Proposition 4.3) studies bias only in the *final* layer under exponential loss, and shows bias proportional to the sum of margin-point labels — which equals the OCS only when the margin points' label marginal matches the training marginal, a condition the paper acknowledges but does not verify empirically. While the paper is honest about incomplete understanding, the mechanism is presented in the abstract and introduction as a core contribution, making this gap significant.

### Minor

2. **The theory and empirics are not bridged.** The theoretical analysis (Section 4.2) studies deep homogeneous ReLU networks with exponential loss, gradient flow, and bias only in the final layer. The experiments use standard networks (ResNet, VGG, DistilBERT) with cross-entropy, MSE, or Gaussian NLL, biases at every layer, and SGD. The paper does not check whether the trained models satisfy the theoretical conditions (e.g., whether weight matrices are nearly rank-1 as predicted by theory for sufficiently deep/wide networks). Computing singular value distributions or subspace alignment for the CIFAR10 ResNet-20 would meaningfully connect the two analyses. As it stands, the theory is an isolated result about a different model class, and the paper would be strengthened by bridging this gap.

3. **The selective classification experiments, while valid for their stated purpose, would benefit from a non-oracle thresholded baseline.** The paper compares reward prediction (MSE) against standard classification (CE, which never abstains because its OCS is the label marginal) and an oracle (confidence-thresholded classifier calibrated on OOD data). The critic's claim that this is a "straw-man" is overstated — the paper's stated goal is to illustrate the OCS effect, not SOTA comparison, and the oracle is itself a thresholded classifier. However, including a standard confidence-thresholded classifier that selects its threshold on held-in validation data (without OOD access, unlike the oracle) would strengthen the comparison by showing that the reward prediction model's advantage is not merely a function of being able to abstain at all, but specifically of how the OCS drives OOD behavior.

4. **The OOD score discriminator is underspecified.** The paper says it trains "a low-capacity model to discriminate between the training and evaluation datasets" but does not specify the architecture, capacity, or training procedure. Since the OOD score is the independent variable in the paper's central figure (Figure 3), this detail matters for reproducibility.

5. **No quantification of how close predictions actually get to the OCS.** Figure 3 shows *relative* distance decreasing, but the y-axis is unnormalized. A normalized measure (e.g., distance to OCS divided by average in-distribution distance) would help assess the practical magnitude of the effect. The paper would also benefit from showing explicit examples where reversion fails.

### Trivial

6. The title "Deep Neural Networks Tend To Extrapolate Predictably" is bolder than the evidence supports — the paper does not study cases where reversion fails, and the empirical scope, while broad, does not guarantee generality. A title like "...Often Revert to the Optimal Constant Solution" would be more precise.

## Nice-to-Haves

- A discussion or explicit test of failure modes (e.g., adversarial perturbations, inputs from completely different modalities) to clarify boundary conditions.
- A normalized measure of distance-to-OCS to assess effect magnitude.
- Computing rank/singular-value distributions of weight matrices in the ResNet-20 to connect theory and empirics.

## Removed Points

- The critic's claim that the selective classification baseline is a "straw man" and that the paper should be faulted for comparing against a classifier that cannot abstain. **Removed because:** the paper includes an oracle (thresholded classifier with abstention) as a baseline, and the primary comparison is explicitly designed to contrast OCS effects, not to claim SOTA. The paper states this goal clearly. The criticism overstates the flaw.

- The critic's framing that Figure 4's bias-approximates-OCS evidence is "the [entire] support" for a central piece. **Weakened from fatal/major to major:** the criticism is factually correct about limited evidence, but the paper's primary contribution is the empirical observation (well-supported), and the mechanism is presented as a plausible explanation with partial validation, not as the sole result.

- The critic's suggestion that the theory is entirely disconnected. **Kept as minor (not major):** many ML papers use simplified theoretical settings, and the paper's theoretical results do provide formal bounds consistent with the empirical pattern. The gap is real but not structural — the paper could check rank conditions in its trained models to tighten the connection.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths and weaknesses without introducing a genuinely new framing or observation not already present in the paper.

## Suggestions

1. **Expand the bias-approximates-OCS evidence.** For the CIFAR10 ResNet-20 and other models, systematically sweep across layers and multiple OOD datasets, measuring the distance between accumulated bias output and the OCS. If the approximation holds broadly, this substantially strengthens the mechanism. If it does not hold at earlier layers, this reveals a boundary condition worth documenting.

2. **Bridge theory and empirics.** For the trained ResNet-20, compute the singular value distribution of weight matrices and check whether the low-rank / nearly-rank-one pattern predicted by Theorem 1 holds. Even a single sanity check would substantially increase coherence between Sections 4.1 and 4.2.

3. **Add a non-oracle thresholded classifier baseline.** Include a classifier that selects its abstention threshold on held-in validation data (without OOD access), to show that the reward prediction model's advantage is not simply a function of being able to abstain.

4. **Specify the OOD discriminator architecture and training details** for reproducibility.

5. **Add a normalized distance metric** in Figure 3 (e.g., distance-to-OCS divided by avg. in-distribution distance) to help readers assess effect magnitude.

## Score and Decision

This paper's core contribution — the empirical observation that neural network predictions on OOD inputs tend to revert toward the OCS — is well-supported, novel, and of genuine interest to the community. The paper generalizes a known classifier behavior to arbitrary loss functions, provides a plausible mechanism with partial validation, and illustrates a practical design principle. The weaknesses (thin mechanism evidence, theory-empirics gap, selective classification comparison could be tighter) are real but do not invalidate the central finding. With reasonable revisions, this is a solid paper.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**