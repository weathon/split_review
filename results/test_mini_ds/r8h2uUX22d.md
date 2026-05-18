Now I have sufficient calibration context. Let me compose the final review.

## Summary

This paper provides an analysis of the MLP-Mixer architecture by showing that its mixing layers can be expressed as a wide MLP with sparse, Kronecker-product-structured weights. The authors derive the effective width (m = SC) and sparsity characteristics of the Mixer, establish a connection to Monarch matrices, and empirically demonstrate that maximizing sparsity (by setting the token-mixing and channel-mixing dimensions S and C close to each other) systematically improves performance across CIFAR-10/100, STL-10, and ImageNet. They also introduce the PK family of architectures (including RP-Mixer) as a generalization that destroys the block structure while preserving the sparsity and spectral properties.

## Strengths

1. **Clean theoretical derivation of effective expression (Proposition 1).** The vectorization of mixing layers into an MLP with Kronecker-product weight matrices (Eq. 11) is a simple but missing-in-the-literature insight that clearly establishes the effective width m=SC and the per-weight sparsity ratios (1/S and 1/C). This is the paper's foundational contribution and is correctly derived.

2. **Consistent experimental validation that optimal S=C maximizes performance.** Figures 4(a)–(d) show that test error for both normal and RP Mixers is minimized near C=S across four datasets (CIFAR-10, CIFAR-100, STL-10, ImageNet). This directly supports the sparsity-maximization argument derived in Section 4.1 and is the paper's strongest empirical contribution.

3. **Spectral analysis explaining why Mixers can exploit extreme width while SW-MLPs cannot.** Section 4.2 provides a quantitative argument that the maximal singular value of Mixer weights remains bounded (~1+√γ) while that of unstructured sparse MLPs grows linearly with width. This explains the divergence in Figure 2 (right) and is a genuine insight not present in prior work.

4. **Novel PK family and RP-Mixer as a controlled ablation.** The random-permuted Mixer destroys the block-diagonal structure while preserving sparsity and singular values. The fact that RP-Mixers show similar trends (Figures 4, 5) provides the cleanest evidence that sparsity, not just the Kronecker structure per se, is driving performance.

5. **ImageNet-scale results.** The experiment in Figure 5(d) and Table 1 (Mixer-B-W) demonstrate that the sparsity-maximization principle carries to large-scale settings, increasing the paper's practical relevance.

## Weaknesses

### Major

- **The "implicit sparse regularization" claim (Proposition 2) is overframed.** The paper states that the inequality between the Frobenius-regularized Kronecker-product objective and an L1-regularized dense objective constitutes "implicit regularization" or an "implicit bias towards sparsity." In the deep learning literature, "implicit regularization" typically refers to a dynamical property of gradient descent (e.g., Neyshabur 2014, Woodworth 2020), not a static lower bound on two different optimization problems. Proposition 2 shows a structural similarity (the Kronecker parameterization induces an L1-type bound), which is a mathematically correct and useful observation, but the paper would be stronger if it simply presented this as a structural property rather than framing it as implicit regularization. The references to Hadamard-product parameterization (hoff2017lasso, yasuda2022sequential) justify the connection to L1, but the paper should clarify that this is about objective-function equivalence, not training dynamics.

- **The β-LASSO comparison in Table 1 is uncontrolled.** The paper states that Mixer-SS-W ("under the same number of total connections") beats β-LASSO on CIFAR-10/100, but it does not specify whether the β-LASSO results were reproduced under identical training conditions (same optimizer, schedule, augmentation, epochs) or cited from Neyshabur et al. (2020). Without this information, the comparison is not apples-to-apples. This does not invalidate the paper's core claims, but if the authors want to assert superiority over β-LASSO, the comparison needs to be properly controlled or removed.

### Minor

- **The evidence that sparsity is the "key mechanism" is correlational, not causal.** The paper's strongest evidence is (i) CKA similarity with sparse MLPs, (ii) the trend of improved performance with increased effective width, and (iii) the optimal S=C result. The RP-Mixer experiment is the cleanest attempt at isolation, but its sparsity pattern (each row has exactly n₂ non-zeros, a uniform row-degree) still differs from the binomial distribution of SW-MLP. The paper acknowledges this ("seemingly become much closer") but does not quantify the gap. The claim that sparseness is "the key mechanism" (abstract, conclusion) slightly overstates what the evidence can establish — the Kronecker structure, balanced factorization, and favorable eigenvalue statistics likely all contribute.

- **The derivation of optimal width (Eq. max_width) uses an averaged Ω across layers.** The paper averages the token-mixing and channel-mixing connections (Ω = γ(CS² + C²S)/2) to derive C*=S*=(Ω/γ)^{1/3}. This is acceptable as a heuristic, but the actual per-layer Ω varies between token and channel layers, so the derivation does not apply exactly to deep networks with heterogeneous layers. The experiments nonetheless confirm the prediction, which somewhat mitigates this gap.

- **Transition from linear S-Mixer to non-linear deep networks is not fully bridged.** The theory (Proposition 1, Proposition 2, Corollary 1) is developed for the linear-activation S-Mixer, but the experiments use deep networks with non-linear activations, skip connections, and layer norm. The paper states "their inclusion does not detract from the fundamental outcomes," which is reasonable but relies on empirical consistency rather than a formal connection.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Quantify how close the RP-Mixer's sparsity pattern is to that of an unstructured sparse matrix (e.g., using Kolmogorov–Smirnov distance on row-degree distributions).
- Run β-LASSO in the same experimental pipeline as the Mixer variants, or remove the comparison row and simply compare Mixer-SS-W to Mixer-SS/8.
- Discuss whether matching the row-degree distribution of SW-MLP in a PK variant changes performance.

## Removed Points

- **Criticism about "Proposition 1 is close to trivial."** The vectorization identity is mathematically elementary, but its application to reveal the MLP-Mixer's effective width and sparsity is precisely the paper's contribution — stating an elementary identity in a new context can be insightful. This is a matter of opinion, not a verifiable flaw, and the value is borne out by the experiments that follow.

- **Criticism about missing appendix content and reproducibility details.** The appendix is stripped by the parser; these sections exist in the original submission per the submission instructions.

- **Criticism about "the CKA sparsity level p = (1/S + 1/C)/2 is somewhat arbitrary."** The paper explains this choice as the average of the two sparsity ratios from the Mixer's left and right multiplications. This is a reasonable, transparent design choice.

- **Criticism about the Monarch matrix experiment being based on "a single small experiment."** The Monarch connection is presented as a theoretical observation (Corollary 1) backed by a sanity-check experiment; the paper does not claim this experiment as a primary evidence pillar.

- **Various formatting/style nitpicks and grammar complaints** — these are parser artifacts, not author errors.

## Novel Insights

The most interesting observation from combining the two reviews is that the harsh critic's strongest concern (overclaimed implicit regularization) and the strength finder's strongest point (effective width derivation) are two sides of the same coin: the paper does a genuinely good job of deriving and empirically testing the sparsity properties of the Mixer, but packages some of its mathematical observations with rhetoric that exceeds what the results can strictly support. The RP-Mixer experiment, which both reviews identify as important, is under-discussed in the paper itself — it could be elevated to the primary evidence piece rather than playing a supporting role. The spectral analysis (Mixer weights stay bounded while SW-MLP weights diverge) is the paper's most underappreciated strength; it explains a real practical advantage of Mixers over unstructured sparsity that goes beyond the core sparsity hypothesis.

## Suggestions

1. Reframe Proposition 2 and Section 3.2: replace "implicit regularization/implicit bias" language with "structural bias" or "objective-function lower bound suggesting a preference for sparse solutions." Acknowledge clearly that this is not a statement about gradient descent trajectories.
2. Either re-run β-LASSO under identical conditions or remove the β-LASSO row from Table 1.
3. Elevate the RP-Mixer discussion and quantify how its sparsity pattern differs from SW-MLP.
4. Add error bars / confidence intervals to Figure 5 (optimal S=C plots).

## Score and Decision

Round 1 bracket: I identified this paper as sitting between 5.0 and 7.0 based on initial retrieval (SCHEME at 5.0 on the low end, Scaling Laws for Sparsely-Connected at 7.0 on the high end).

Round 2 narrowed this to 6.0 by comparing against:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SCHEME | U4ekUAOLsM | 5.00 | R1 | Weaker — engineering-focused, less theoretical insight; this paper is clearly stronger |
| Learning Param Sharing | tGsumqfOUk | 4.75 | R1 | Weaker — incremental contribution; this paper has more originality |
| Improving MLP Module | I8pdQLfR77 | 4.75 | R1 | Weaker — marginal improvements, limited scope |
| DNN Init w/ Sparsity Activations | uvXK8Xk9Jk | 6.50 | R2 | Stronger in theoretical rigor, but narrower in scope; this paper is comparable overall |
| Expressivity Random Weights | 5xwx1Myosu | 6.50 | R2 | Stronger theoretical proofs, but this paper has broader experimental validation |
| MLPs Learn In-Context | MbX0t1rUlp | 6.20 | R2 | Similar level of insightfulness; this paper has more extensive experiments |
| How Sparse Can We Prune | FT4gAPFsQd | 6.00 | R2 | Comparable — both have a mix of theory and experiments with some methodological gaps |
| Scaling Laws Sparsely-Connected | i9K2ZWkYIP | 7.00 | R2 | Stronger — more comprehensive and tightly controlled; this paper is a notch below |

The paper has genuine contributions (the effective expression, the optimal S=C prediction, the spectral analysis), solid empirical support, and an interesting generalization (PK family). However, the overframing of "implicit regularization," the uncontrolled β-LASSO comparison, and the correlational nature of the sparsity evidence prevent it from reaching the 6.5–7.0 tier of papers with tighter claims and more controlled experiments. It is clearly above the 4.75–5.0 tier of incremental or purely engineering contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>