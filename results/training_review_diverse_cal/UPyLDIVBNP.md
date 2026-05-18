Now I have thoroughly reviewed the paper. Let me produce the final consolidated review.

## Summary

This paper introduces Fully Identical Initialization (IDInit), a set of initialization techniques for neural networks that use identity-like matrices to preserve identity transition in both main and sub-stem layers of residual networks. The core proposals are: (1) IDIτ, a padded identity scheme for non-square weight matrices that addresses rank constraints; (2) IDICτ, a patch-maintain strategy for convolutional layers that reshapes kernels to fuse spatial information; and (3) IDIZε, a technique that replaces exact zeros with tiny values to mitigate dead neurons in residual stems. The paper validates these methods across CIFAR-10, ImageNet, text classification, and BERT pre-training, reporting consistent improvements.

## Strengths

1. **Dead neuron solution with clear empirical evidence.** The IDIZε method replaces strict zeros in the last sub-stem layer with small numerical values (ε = 1e-6) while keeping output variance near zero. The ablation in Table 4 shows IDIZCε alone improves ResNet-20 accuracy by 5.89% (from 87.01% to 92.90%), and Figure 5 visually demonstrates that nearly all weight elements become trainable versus >50% dead neurons in Fixup. This addresses a genuine practical problem in identity-control initialization that prior work (Fixup, ZerO) did not resolve.

2. **Patch-maintain convolution improves feature diversity.** IDICτ reshapes a 4-D convolution kernel into a 2-D matrix, applies IDIτ, then reshapes back — fusing spatial information rather than keeping identity only along channels (as ZerO does). The ablation shows IDICτ alone improves accuracy by 3.42% (from 87.01% to 90.43%), and combined with IDIZCε gives the best result (93.91%). This is a simple but effective idea.

3. **Consistent gains on large-scale benchmarks.** On ImageNet (ViT-B/32, ResNet-50/152, Se-ResNet-50), IDInit achieves an average 0.55% accuracy improvement and accelerates convergence by 7.4 epochs to 60% accuracy over default initialization (Table 3). On BERT-Base pre-training, IDInit reduces computational cost by 11.3% in FLOPs (Figure 9). These results demonstrate practical utility at scale.

## Weaknesses

### Major

1. **Overclaimed theoretical contribution from Theorem 3.1.** The paper states that IDInit "breaks the rank constraint problem" via Theorem 3.1, but the theorem only proves rank(θ̂^(k)) ≥ D₀ — a lower bound that is consistent with ZerO's upper bound of ≤ D₀ (together implying ≈ D₀ at initialization, not > D₀). The paper then falls back on the claim that "after training for several steps, an IDInit initialized network can break this constraint," which is supported empirically by Figure 4(b). However, the theorem itself does not establish what the paper claims it does, and the central theoretical framing is inflated relative to what is actually proved. The empirical evidence for rank growth during training is real, but it should be honestly presented as an empirical observation rather than claimed as a proven theoretical result.

2. **Missing identity-control baselines on ImageNet.** On CIFAR-10 (Table 2), the paper compares IDInit against Fixup, SkipInit, ReZero, Kaiming, Zero γ, and ZerO — a reasonable set. But on ImageNet (Table 3), only "Default" initialization is used as a baseline. Since Fixup, ZerO, and SkipInit are the paper's stated primary competing identity-control methods, their absence on the most important large-scale benchmark is a significant gap. Without these comparisons, it is difficult to assess whether IDInit's ImageNet gains are attributable to identity-control in general or to IDInit's specific innovations. The CIFAR-10 results suggest IDInit is competitive, but the ImageNet results are the main claim of practical advantage.

### Minor

1. **Convergence analysis is a useful verification, not a substantive contribution.** Section 3.1 confirms that SGD without momentum fails for identity-initialized networks with negative target eigenvalues (Bartlett et al., 2019), and that adding momentum resolves the issue. Since momentum is standard in virtually all deep learning optimizers, this shows the concern is not a practical barrier — which is a useful empirical note — but the framing as IDInit "solving" a problem is inflated. No analysis is provided of *why* momentum resolves the issue (e.g., eigenvalue conditioning, gradient bias correction), which limits insight.

2. **IDIτ for non-square matrices does not preserve identity.** For D_{i+1} > D_i, IDIτ produces a repetition pattern (replicating input features) rather than an identity map. The paper acknowledges a "replica problem" and adds noise (τ ∼ N(τ, ε_τ)) as a mitigation, but calling this "fully identical initialization" overstates what is achieved for non-square layers. The method may be a useful heuristic, but the naming and framing conflate what is achieved (favorable training dynamics) with what is claimed (identity transition).

3. **Missing downstream evaluation for BERT.** The BERT pre-training experiment (Figure 9) reports FLOPs reduction (11.3%) and final loss (1.46), but does not report downstream task performance (e.g., GLUE scores). Faster pre-training convergence is only compelling if it translates to better or comparable fine-tuned quality.

4. **No error bars or multiple seeds in the ablation.** Table 4 reports single accuracy numbers for each ablation setting without variance estimates. Given the 3–6% differences claimed, it would be important to confirm these are not due to random seed variation.

### Trivial

1. **Technical definitions lack full precision.** Eq. (3)'s indexing convention (row m, column j) is standard but never explicitly stated. The IDIZε description uses colon notation and modulo conditions that are understandable but could be clearer with a short pseudocode block or figure annotations. This does not prevent understanding but makes exact reproduction harder than necessary.

## Nice-to-Haves

- Include Fixup, ZerO, and SkipInit as ImageNet baselines (the most impactful improvement the paper could make).
- Report GLUE scores (or similar downstream metrics) for the BERT pre-training experiment.
- Add a brief analysis of why momentum helps with identity initialization (e.g., effective condition number, gradient covariance).
- Add error bars or multi-seed results for the ablation study.
- Include a brief limitation discussion (the section header exists but is empty): e.g., IDInit is tailored to residual-like architectures; its benefit for non-residual or more complex normalization schemes is unclear; the non-square extension introduces replica artifacts.

## Removed Points

- **ISONet novelty criticism (Critic Point "Other Observations", third bullet):** The critic claims ISONet already does what IDInit does. However, the paper explicitly discusses ISONet in related work (line 68) and positions its contribution as breaking rank constraints, which ISONet (using zero-padding) does not do. This is a misreading of the paper's claim. Removed as strawman.

- **"Any reasonable initialization" would also break the rank constraint (Critic Point 1, sub-argument):** The critic states that "that is true of essentially any reasonable initialization that breaks symmetry; it is not a property specific to IDIτ." However, Figure 4(b) experimentally shows that zero-padding (a commonly used approach in identity-control methods) remains bounded at rank 768 even after training, while IDInit achieves ranks well above 768. So the property is empirically specific to IDInit's initialization structure. This sub-argument is factually incorrect. The main thrust of the criticism (Theorem 3.1 is weaker than claimed) is kept above.

- **"Framing convergence as IDInit 'solves' a problem is misleading" (Critic Point 2, strong version):** The paper's text says "we find that the convergence problem can be solved by adding a moment in an optimizer" — this describes an empirical observation about a standard optimizer feature, not a claim of inventing momentum. The framing is slightly imprecise but not misleading. However, the underlying point (that this section adds little beyond confirming standard behavior) is valid and kept above in Minor.

- **Formatting/style nitpicks and typos:** Not present in original paper.

## Novel Insights

The harsh critic observes an interesting tension not articulated in the paper: the very property that makes IDIτ work — the identity structure that allows gradient flow — also creates the replica problem for non-square layers that must be fixed by adding noise. This tension between "preserving identity" and "avoiding replication" is the fundamental design challenge of the method, and the paper would benefit from a more explicit discussion of this trade-off rather than treating the replica problem as an afterthought. The critic also correctly identifies that the paper's strongest evidence is empirical (dead neuron resolution, ablation gains) rather than theoretical — a reframing that would better serve the contribution.

## Suggestions

1. Reframe the theoretical narrative: honestly present Theorem 3.1 as establishing a rank guarantee rather than a "breakthrough," and rely on the empirical evidence (Figure 4b) to demonstrate the practical rank advantage.
2. Add Fixup/ZerO/SkipInit comparisons on ImageNet — this is the single most impactful experiment you can add.
3. Add a short pseudocode block or algorithmic description for IDIτ, IDICτ, and IDIZε to resolve clarity concerns.
4. Report downstream GLUE scores for the BERT experiment.
5. Include standard deviations or multi-seed results in the ablation table.
6. Rename or qualify "fully identical initialization" to acknowledge that non-square layers use an identity-like repetition pattern, not a true identity map.

## Score and Decision

**Originality:** Medium. The IDIτ padding scheme is a reasonable extension of identity initialization to non-square matrices; IDICτ (reshape-and-initialize) and IDIZε (small nonzero values for dead neurons) are useful heuristics. The individual ideas are incremental but their combination is novel.

**Importance:** Medium. Initialization is a foundational component of deep learning, and practical improvements are valuable.

**Claims support:** Below average. The central theoretical claim (breaking rank constraint via Theorem 3.1) is not actually proven by the theorem presented. The empirical results support the practical value, but missing ImageNet baselines against competing identity-control methods weaken the main claim of superiority.

**Soundness:** Fair. Experimental methodology is reasonable, but the single-seed ablation, missing error bars, and absence of key baselines on ImageNet are notable gaps.

**Clarity:** Below average. Technical definitions are imprecise in places, and the framing consistently oversells theoretical contributions while understating limitations.

**Value:** Moderate. The empirical toolkit (IDIτ + IDICτ + IDIZε) is likely useful to practitioners working with residual networks, and the dead neuron solution addresses a real practical problem.

Overall, the paper proposes useful initialization heuristics backed by reasonable empirical evidence, but the theoretical framing is overclaimed, the experimental comparison on ImageNet is incomplete, and several presentation issues reduce clarity. With substantial revisions — particularly re-framing the theoretical claims honestly and adding the missing baselines — the paper could be a solid empirical contribution. In its current form, the weaknesses outweigh the strengths.

**Score:** 4.5

**Decision:** Reject

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>