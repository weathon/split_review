Now I have a thorough understanding of the paper and have verified all the reviewer's claims against the actual content. Let me produce the final consolidated review.

---

## Summary

This paper observes that neural network predictions on out-of-distribution (OOD) inputs tend to converge toward the Optimal Constant Solution (OCS) — the prediction that minimizes the training loss without seeing the input. The authors provide empirical evidence for this "reversion to the OCS" phenomenon across 8 datasets, three loss functions (cross-entropy, MSE, Gaussian NLL), and both CNNs and transformers. They propose a mechanistic explanation (feature norm collapse → bias domination → OCS approximation) with supporting empirical and theoretical analyses, and demonstrate a practical application to risk-sensitive decision-making via selective classification.

## Strengths

- **Generalizes OOD prediction behavior beyond softmax probabilities.** Prior work (Hendrycks & Gimpel 2016) noted that softmax confidence decreases on OOD inputs. This paper extends the observation to MSE and Gaussian NLL losses, showing that network outputs converge toward the OCS in general — not just lower softmax confidence. Fig. 3 shows this across 8 datasets with diverse distribution shifts, including both image (ResNet, VGG) and text (DistilBERT) modalities.

- **Proposes a concrete mechanistic explanation.** The paper identifies a plausible two-part mechanism: (1) OOD representations have smaller norms and align less with weight matrices in later layers (Fig. 4, columns 1-2), and (2) the accumulated bias terms in the network closely approximate the OCS (Fig. 4, columns 3-4). This explanation connects the empirical trend to a structural property of how information propagates through the network.

- **Demonstrates a practical application.** The selective classification experiments (Section 5, Figs. 5-6) show that when the OCS aligns with a cautious action (abstention), the model automatically becomes more cautious on OOD inputs — across 4 datasets. While imperfectly controlled, this serves as a compelling illustration of how the OCS insight could be leveraged in practice.

- **Solid empirical methodology for the core phenomenon.** The OOD score (low-capacity discriminator) and distance-to-OCS metrics are well-chosen, and the results show clean monotonic relationships with error bars over 5 runs. The breadth of settings (synthetic and natural shifts, both vision and NLP) strengthens confidence that the phenomenon is real and general.

## Weaknesses

### Fatal
None.

### Major

- **The mechanism evidence is correlational/counterfactual, not causal, and limited in scope.** The paper shows that (a) feature norms drop on OOD inputs and (b) accumulated bias constants approximate the OCS. But the link between (a) and (b) is inferred rather than directly demonstrated. The "accumulation of model constants" is computed by artificially zeroing an intermediate layer's representation — a hypothetical "what if" analysis, not evidence that the network actually uses this channel. Furthermore, this analysis (Section 4.1) is limited to just two small-scale settings: a 4-layer network on MNIST and a ResNet20 on CIFAR10. Extending the mechanism analysis to the other 6 datasets (e.g., Amazon for text) would substantially strengthen the claim of generality.

- **The theoretical analysis operates in a setting substantially different from the experiments, and key conditions are unverified.** The theory (Section 4.2) uses binary homogeneous ReLU networks with exponential loss under gradient flow — far from the multi-class CNNs, transformers, cross-entropy/MSE/Gaussian NLL used empirically. Proposition 4.3 shows that the learned bias approximates the OCS *only if* margin points have the same label marginal as the training set, but this condition is not empirically verified. The theory provides plausible intuition but does not substantially increase confidence that the mechanism holds in the practical settings studied.

- **The selective classification experiment conflates multiple differences and does not isolate OCS reversion as the causal factor.** The comparison contrasts MSE reward-prediction (whose OCS is abstention) with cross-entropy classification (whose OCS is the label marginal, never abstention). These approaches differ in loss function, training objective (regression vs. classification), and output structure — any of which could explain the OOD performance gap. The oracle baseline additionally uses temperature scaling on the OOD evaluation set (privileged information). The paper is transparent about its illustrative intent, but the experiment does not cleanly demonstrate that OCS reversion *causes* the improved OOD behavior. A cleaner test would compare two models with the same architecture and loss but different OCS (e.g., by manipulating training label distribution).

### Minor

- **The unverified condition for Proposition 4.3 weakens the theoretical-to-empirical connection.** The claim that accumulated biases approximate the OCS depends on margin points having label marginal similar to the training set. The paper does not check this condition in the experimental settings where it shows the bias-OCS alignment (Fig. 4, columns 3-4), leaving a gap between theory and observation.

- **Potential circularity of the OOD score is not discussed.** The OOD score is itself a neural-network-based discriminator output. If this discriminator also reverts to its OCS on the evaluation data, the OOD score could be systematically biased. This concern does not invalidate the results (the monotonic trends in Fig. 3 are clear), but it would strengthen the paper to address it.

- **No explicit failure cases or counterexamples are provided.** The paper acknowledges incompleteness in the conclusion but does not characterize *when* reversion to the OCS fails or degrades. A single counterexample (even a constructed one) would sharpen the boundaries of the phenomenon.

### Trivial
None.

## Nice-to-Haves

- Causal intervention experiments (e.g., artificially reducing intermediate representation norms and checking whether outputs approach the OCS) would directly test the claimed mechanism.
- Extending the mechanism analysis (feature norm collapse, subspace alignment) to at least one additional setting beyond MNIST/CIFAR10 — particularly the text domain (Amazon/DistilBERT) — would broaden confidence.
- A cleaner selective classification comparison: same architecture and loss, but with training label distribution manipulated to produce different OCS values.

## Removed Points

- **"Theoretical propositions are stated as informal, non-quantitative claims"** — Removed because this is factually incorrect. The paper presents formal mathematical bounds for all three theoretical statements (Proposition 1: line 150; Theorem 1: lines 162-163; Proposition 2: line 172). The reviewer appears to have been misled by the descriptive titles of the propositions/theorems.
- **Strength Finder's claim that theoretical analysis "adds rigor beyond purely empirical work"** — Removed because it conflicts with the verified weakness that the theory operates in a setting far from the experiments. The theory provides intuition but does not add rigorous support for the practical claims.

## Novel Insights

The reviews surface a consistent tension: the paper's most well-supported contribution is the empirical observation of OCS reversion, not the specific mechanistic explanation. The harsh critic correctly identifies that the mechanism evidence is correlational and limited in scope, while the strength finder correctly identifies that the core phenomenon is novel and well-documented. The interesting insight that emerges is that the phenomenon itself may be more robust and general than any one explanation of it — the paper's strongest contribution is the discovery and documentation of the pattern, and future work could productively focus on understanding the conditions under which it holds or fails, potentially leading to multiple complementary explanations rather than a single mechanism.

## Suggestions

1. Strengthen the mechanism analysis by adding a causal intervention experiment: artificially silence intermediate representations (e.g., zero out activations at a middle layer) and verify that outputs approach the OCS, thereby demonstrating that the bias accumulation channel *can* drive the behavior.
2. Extend the mechanism analysis (feature norm and subspace overlap measurements) to at least one additional dataset beyond MNIST/CIFAR10 — ideally the text domain (Amazon/DistilBERT) to show cross-modality generality.
3. For the selective classification experiments, add an ablation where the same reward-prediction architecture is trained with a modified reward structure whose OCS does *not* align with abstention, to better isolate the effect of OCS alignment from other differences between MSE and cross-entropy training.
4. Verify the theoretical condition from Proposition 4.3 empirically by checking whether margin points in the trained networks have label marginal similar to the training set.
5. Discuss the potential circularity of the OOD score discriminator and provide a validation that the OOD score is monotonic with true distribution shift for each dataset.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>