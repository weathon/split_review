Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper introduces IDInit (Fully Identical Initialization), a method that preserves identity transition in both main- and sub-stem layers of residual networks. The core technical contributions are: (1) a padded identity-like matrix (IDI_τ) that handles non-square weight matrices while avoiding rank constraints that plague zero-padding approaches; (2) an empirical demonstration that the known convergence problem of identity initialization is resolved by standard momentum optimizers; (3) a patch-maintain convolution strategy (IDIC_τ) for higher-order weights; and (4) a small-noise technique (IDIZ_ε) to mitigate dead neurons in identity-control settings. Experiments span CIFAR-10, ImageNet, text classification (SST2, TREC-6), and BERT pre-training, showing consistent improvements over baselines.

## Strengths

- **Practical identity-like initialization for non-square matrices**: The IDI_τ scheme (Eq. 3) provides a simple, principled way to extend identity initialization to rectangular weight matrices, which is a genuinely practical problem. Figure 4(b) empirically confirms that this scheme achieves higher rank than zero-padding, supporting the claimed advantage.

- **Consistent empirical improvement across architectures and tasks**: On ImageNet (Table 3), IDInit achieves an average 0.55% top-1 accuracy improvement over default initialization across ResNet-50/152, Se-ResNet-50, and ViT-B/32, with 7.4 epochs faster convergence to 60% accuracy. On BERT-Base pre-training (Figure 9), it yields an 11.3% FLOPs reduction and reaches a lower final loss. These results demonstrate broad applicability.

- **Clean ablation study isolating the two key techniques**: Table 4 quantifies the individual contributions of IDIC_τ (+3.42%) and IDIZC_ε (+5.89%) on ResNet-20/CIFAR-10, validating that both modifications independently improve over the baseline identity initialization.

- **Strong performance against identity-control baselines on CIFAR-10**: Table 2 compares IDInit against Fixup, SkipInit, ReZero, Zero-γ, ZerO, and Kaiming across ResNet-56/110 with/without BN and both SGD/Adam optimizers. IDInit achieves the best accuracy in most settings and consistently reaches 80% accuracy in the fewest epochs.

- **Stable text classification results with lowest variance**: Table 5 shows IDInit achieves highest accuracy across all six TextCNN/TextRNN settings on SST2 and TREC-6, and consistently obtains the smallest standard deviation, supporting claims of training stability.

## Weaknesses

### Fatal

None.

### Major

- **Theorem 3.1 is mathematically imprecise and potentially incorrect as stated**: The theorem claims that initializing all weights with IDI₁ yields rank(θ̂⁽ᵏ⁾) ≥ D₀ for middle square layers (θ̂⁽ᵏ⁾ = θ⁽ᵏ⁾ − I). However, for the middle square weights θ⁽ᵏ⁾ ∈ ℝ^{D_h × D_h}, IDI₁ produces the identity matrix I, making θ̂⁽ᵏ⁾ = I − I = 0, whose rank is 0 — not ≥ D₀ (assuming D₀ > 0). The paper's own post-statement clarification acknowledges that ZerO's rank-constraint claim "is tenable in the initial state" and that "after training for several steps, an IDInit initialized network can break this constraint." This means the theorem as written is either false (if interpreted as an initialization guarantee) or vacuous (if interpreted as a post-training claim about dynamics that are not proven). Since the rank constraint argument is the paper's main motivation for the IDI_τ padding scheme, this inconsistency undermines the theoretical framing. The empirical evidence (Figure 4) still supports the practical claim, but the theorem needs substantial correction or removal.

- **Missing identity-control baselines on ImageNet**: On ImageNet (Table 3, Figure 8), IDInit is compared only against "Default" (Kaiming) initialization. Fixup, ZerO, SkipInit, and ReZero — the directly relevant identity-control methods discussed at length in Section 2 and compared on CIFAR-10 (Table 2) — are absent from the largest-scale experiments. Without these comparisons, the paper cannot substantiate its claim that IDInit is superior to existing approaches in its own class on the most important benchmark. The CIFAR-10 comparisons are a useful sanity check, but ImageNet is the standard for evaluating practical initialization methods, and this omission is a decisive gap.

### Minor

- **The dead neuron analysis is correlational rather than causal**: The paper shows that IDIZ_ε improves accuracy by 5.89% (Table 4) and that weights in a trained ResNet look more "alive" with IDIZ_ε (Figure 5). However, it never verifies that the baseline (Fixup/ZerO) actually suffers from zero-gradient dead neurons under the specific training conditions used, nor does it establish that the accuracy gain is causally linked to resolving dead neurons rather than other side effects of adding small noise. The 5.89% improvement is a real ablation result, but the claimed mechanism is not rigorously demonstrated.

- **The convergence experiment is too limited to fully resolve the theoretical concern**: Section 3.1 tests only a 3-layer network with 10×10 weights on synthetic data with 4000 samples. While this demonstrates that momentum helps SGD converge from identity initialization under the specific condition Bartlett et al. (2019) identified, the paper then broadly asserts that "momentum is crucial in training deep networks" and treats the problem as solved for all settings. The gap between this toy setup and the deep, wide networks used in later experiments is significant. This does not invalidate the method (since all experiments use momentum), but the "solution" to the convergence problem is presented with weaker evidence than it merits.

- **Overclaim on novelty relative to ZerO**: The paper states "IDInit is the first successful trial to maintain identity in both main- and sub-stems by breaking the rank constraints." ZerO (Zhao et al., 2021) also breaks rank constraints (using Hadamard matrices) and maintains identity in the main stem via the Dirac function. The genuine novelty of IDInit is using identity-like periodic patterns (IDI_τ) rather than Hadamard matrices for the non-square case, and maintaining identity in sub-stem weights — but the "first to break rank constraints" framing is misleading given prior work.

### Trivial

- The modulo condition in Eq. (3) (m ≡ j mod D_i) would benefit from explicit index ranges (m ∈ [0, D_{i+1}-1], j ∈ [0, D_i-1]) and clarification of 0-vs-1 based indexing, though the convention is inferable.

## Nice-to-Haves

- Adding Fixup/ZerO baselines on ImageNet under the same training recipe would greatly strengthen the paper's central claim.
- A controlled analysis of the dead neuron mechanism (gradient flow measurements, ablations isolating the effect of ε noise from the identity structure) would turn a heuristic into a well-understood fix.
- The ablation (Table 4) uses ResNet-20 on CIFAR-10; repeating this on a larger model (e.g., ResNet-50) would increase confidence in the findings.

## Removed Points

These points were identified but removed because they are factually incorrect, misunderstand the paper, or violate the filtering rules:

- **Criticism about "convergence problem is not established for deeper networks" (Harsh Critic, overblown)**: The paper's claim is modest — momentum solves the Bartlett et al. convergence problem under the specific condition that motivated it. All experiments use momentum. The reviewer's demand for testing on "deeper, wider networks" as proof of concept is disproportionate to the paper's intended scope of this subsection. The paper is not claiming a new convergence theory.

- **Criticism about "the paper never verifies that dead neurons actually occur in the compared baselines" (Harsh Critic, partially invalid)**: Figure 5(a) visually demonstrates untrained weights in the baseline. The ablation (Table 4) shows the technique improves accuracy. A rigorous causal chain would be stronger, but the paper provides reasonable (if correlational) evidence.

- **Notation nitpicks about modulo indexing and "padded identity-like matrix" not being formally defined (Harsh Critic, Other Observations)**: The IDI_τ definition in Eq. (3) and Figure 3 formally define the construction. The modulo convention is standard in matrix indexing. These are parser/stylistic nitpicks that do not impede understanding.

- **Strength Finder strengths that conflict with verified weaknesses**: The strength about "Theorem 3.1 proves rank ≥ D₀" is retained in substance (the empirical rank improvement is real) but qualified in the Weaknesses section by the theorem's imprecision.

## Novel Insights

Beyond the paper's own contributions, a notable observation from the cross-review is that the paper inadvertently highlights a gap in the identity-control literature: prior methods (Fixup, ZerO, SkipInit, ReZero) each handle identity in the sub-stem by setting the last layer to zero, but none address what happens to that zero-initialized weight when downstream normalization layers or downsampling operations produce zero gradients. This failure mode — where zero initialization interacts pathologically with modern architectural components — is genuinely underexplored, and the paper's IDIZ_ε solution, while simple, draws attention to a real vulnerability in the identity-control paradigm. The paper would benefit from leaning into this observation more explicitly as a contribution.

## Suggestions

1. **Fix Theorem 3.1**: Either (a) restate it as a claim about the rank achievable *after training* from IDI₁ initialization, with empirical backing from Figure 4, or (b) remove the theorem entirely and rely on the empirical rank measurements as motivation. The current formulation is mathematically incorrect for square middle layers and confuses the paper's theoretical narrative.

2. **Add ImageNet results for at least Fixup and ZerO** under the same training setup used in Table 3. If cost is prohibitive, explicitly acknowledge the gap and frame the ImageNet contribution as a comparison against "standard initialization" rather than against identity-control methods.

3. **Strengthen the dead neuron analysis** by adding gradient norm measurements (or a simple probe) that show the baseline's zero-initialized weights receive near-zero gradients while IDIZ_ε's do not. This would convert a plausible claim into a verifiable one at minimal experimental cost.

4. **Tone down the "first" claim** regarding breaking rank constraints and instead emphasize the specific novelty: using identity (rather than Hadamard) matrices for non-square weight initialization, and maintaining identity across *both* stems.

## Score and Decision

**Originality**: 6/10 — The identity-like padding scheme is a practical twist on existing ideas (ZerO, DiracNet), not a paradigm shift. The dead neuron fix and patch-maintain convolution are incremental but useful.

**Quality**: 5/10 — Experiments are generally well-designed and cover multiple tasks, but the theoretical flaw and missing ImageNet baselines reduce rigor. The ablation study is a highlight.

**Clarity**: 6/10 — The core ideas are communicated clearly, but the theoretical section (Theorem 3.1) is confusing and the notation has minor imprecisions.

**Significance**: 6/10 — A simple, practical initialization method that works across architectures and tasks has clear value to the community. The improvements are modest but consistent.

**Overall**: The paper proposes a simple and practical initialization method with broad empirical validation across vision and language tasks. However, the central theoretical claim (Theorem 3.1) is mathematically imprecise and potentially incorrect for the setting it describes, and the paper lacks the direct ImageNet comparisons against identity-control baselines needed to substantiate its claimed advantages over prior work in its own class. These are fixable issues, but in their current form they significantly weaken the contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>