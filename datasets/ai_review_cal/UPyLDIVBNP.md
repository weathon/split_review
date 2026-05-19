- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me construct the consolidated review.

---

## Summary

This paper proposes IDInit, an initialization method that uses padded identity-like matrices to maintain identity transition in both the main stem and sub-stem of residual networks. It addresses three practical obstacles: (1) rank constraints from zero-padding in non-square matrices (via padded identity), (2) the replica problem (via small noise), and (3) dead neurons in identity-control settings (via a subtraction trick with a tiny ε). Additional techniques address convolution reshaping (IDICτ) and dead-neuron fixes (IDIZCε). Experiments span CIFAR-10, ImageNet, text classification (SST2, TREC-6), and BERT pre-training.

## Strengths

- **Novel padded-identity design for non-square matrices with formal rank guarantee.** Theorem 3.1 provides a formal lower bound on residual-weight rank when all layers use IDI₁, and Figure 4(b) empirically shows padded identity achieves rank exceeding the input dimension while zero-padding caps below it. This directly addresses a known limitation of prior zero-padding schemes.

- **Consistently faster convergence across diverse settings.** On CIFAR-10 (Table 2), IDInit achieves the fewest epochs to 80% accuracy in all configurations. On ImageNet (Table 3), it accelerates convergence by 7.4 epochs on average to 60% accuracy. On BERT (Figure 9), it shows an 11.3% FLOPs reduction. This convergence benefit is the paper's most consistently supported empirical claim.

- **Generalization to text classification with strong results.** Table 5 shows IDInit achieves the highest accuracy on SST2 and TREC-6 across TextCNN, TextRNN, and Transformer backbones, with the smallest standard deviations, demonstrating applicability beyond vision.

- **Ablation confirms the two proposed techniques produce real gains.** Table 4 shows IDICτ improves accuracy by 3.42% and IDIZCε by 5.89% over a naive identity-initialization baseline on ResNet-20, and Figure 5 visually demonstrates that IDIZ₁ₑ₋₆ makes all elements trainable.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparisons to identity-control baselines on ImageNet and BERT.** On ImageNet (Table 3) and BERT (Figure 9), IDInit is compared only to each model's default initialization (Kaiming or random). Fixup, ZerO, SkipInit, and ReZero — the paper's own claimed prior work on identity-control initialization — are included on CIFAR (Table 2) but omitted at scale. This is a structural omission: the reader cannot assess whether IDInit's 0.55% average ImageNet improvement reflects an advantage over existing identity-control methods or simply the benefit of any identity-control scheme. This is the single most significant weakness because it leaves the paper's core comparative claim unsubstantiated at the largest scale. The paper text states IDInit can achieve "almost all the best performance" — this claim is unverifiable against the relevant baselines on ImageNet.

- **BERT experiment reports only training loss, no downstream task evaluation.** Figure 9 shows IDInit achieves lower training loss on Wikipedia+BookCorpus, but no GLUE or other downstream benchmark results are reported. Lower pre-training loss does not guarantee better fine-tuned performance. The 11.3% FLOPs reduction claim depends on reaching an unvalidated loss threshold.

### Minor

- **The CIFAR accuracy claim ("best in most cases") cannot be fully verified.** Table 2 is an image; the paper asserts IDInit "derives the best accuracies in most cases," while the harsh reviewer provides specific counter-numbers (e.g., ResNet-56 w/ BN: IDInit 93.68 vs. SkipInit 94.16, Fixup 93.87, Zero-γ 93.90). Without being able to read the table directly, this contradiction cannot be resolved from the text alone. At minimum, the accuracy advantage on CIFAR is not as clear-cut as the convergence advantage, and the paper should discuss any accuracy/convergence trade-off honestly.

- **Ablation starts from a known-failing baseline, not a strong one.** The "w/o both" condition in Table 4 is a naive partial-identity initialization that the paper itself acknowledges fails (Sec. 3.2). Showing 3.42% and 5.89% improvements over this is not surprising. The ablation would be more informative if it also compared to a strong baseline like Kaiming or to Fixup/ZerO on the same architecture.

- **The convergence problem section (Sec. 3.1) confirms expected behavior.** The paper shows that an identity-initialized network fails with pure SGD but succeeds with SGD+momentum, and acknowledges that "momentum is crucial in training deep networks." This is a valid observation but is presented as a contribution when it simply confirms standard practice. It does not reveal a problem that impeded prior work, since virtually all practical training uses momentum.

- **No statistical significance or error bars on ImageNet results.** Table 3 reports single-run numbers without standard deviations. Given the small average improvement (0.55%), variance could flip the conclusion. Single-run evaluation is common for ImageNet-scale experiments, but the paper does not acknowledge this limitation.

### Trivial

None that survive filtering.

## Nice-to-Haves

- A comparison to orthogonal initialization, which also preserves signal norm, would strengthen the positioning against this natural baseline.
- An analysis of hyperparameter sensitivity (ε = 1e-6, τ choices, noise magnitude) would improve reproducibility.
- A simpler alternative to IDIZε (e.g., setting the last layer to a small random constant) should be discussed or compared.

## Removed Points

- **Harsh critic Issue 4 (rank constraint critique)** — The critic claims Theorem 3.1's statement applies to "any full-rank initialization" and that training breaks rank for any method. This partially misreads the paper. Theorem 3.1 specifically addresses the *initial* rank in dimension-increasing layers where zero-padding caps rank at D₀; padded identity avoids this cap from the start. The critic's point about training changing rank is about a different claim the paper makes about later training steps. Removed as a partial misunderstanding of the paper.

- **Harsh critic: "dead neuron solution seems unnecessarily complicated" and suggestion to use small random values** — This is speculative. The paper provides a theoretical justification (Eq. 6) for why the subtraction trick yields zero-mean, small-variance output. The reviewer's alternative may or may not work; the paper cannot be faulted for not comparing to an unspecified alternative. Removed as speculative.

- **Harsh critic: Figure 4(b) improvement comes from noise, not from identity structure** — Figure 4(b) shows three curves: padding zero, padding identity (strict), and padding identity (loose). Both identity variants outperform zero-padding. The strict condition already breaks the rank constraint; the loose condition further improves it. The criticism that improvement "comes from noise" is inaccurate — noise helps but the core improvement is from the identity structure itself. Removed as factually inaccurate.

- **Harsh critic: "The paper claims to be the 'first successful trial' but ISONet already used a Dirac function"** — ISONet is discussed in the related work (line 68) as a framework that uses Dirac initialization but multiplies the residual stem by 0 (like Fixup) and lacks flexibility. The paper's claim is about maintaining identity in *both* main and sub-stems while breaking the rank constraint for non-square matrices, which is a distinct claim from ISONet. This criticism is too blurry to retain. Removed.

- **Strength Finder: "Convergence problem solved by standard momentum"** — This strength is overstated. Showing that a standard optimizer setting works is not a meaningful contribution or selling point. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper that the paper itself does not already contain or imply.

## Suggestions

1. **Add ImageNet comparisons to Fixup, ZerO, and SkipInit**, even on a single architecture (e.g., ResNet-50). Without this, the paper's central comparative claim is unverifiable at scale.
2. **Report downstream GLUE scores for the BERT experiment**, or at minimum acknowledge that only pre-training loss is shown.
3. **Clarify the CIFAR accuracy picture**: if IDInit converges faster but achieves lower final accuracy on some settings, discuss this trade-off transparently rather than claiming "best in most cases."
4. **Reframe Section 3.1** to position the convergence observation as a brief empirical note rather than a core contribution.
5. **Add error bars or multiple-run statistics** to ImageNet results, or acknowledge the limitation in the text.
