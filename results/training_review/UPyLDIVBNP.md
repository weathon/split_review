Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

## Summary

This paper proposes Fully Identical Initialization (IDInit), an initialization method that extends identity-based initialization to non-square weight matrices using padded identity-like matrices (IDI_τ). It addresses rank constraints from zero-padding, convergence issues via momentum, and introduces two additional techniques: patch-maintain convolution (IDIC_τ) for feature diversity and IDIZ_ε to mitigate dead neurons in residual blocks. Experiments span CIFAR-10, ImageNet, text classification, and BERT pre-training.

## Strengths

- **Broad experimental validation across diverse architectures and tasks**: IDInit is tested on non-residual ConvNets (AllConv), residual ConvNets (ResNet-56/110, RN-50/152, Se-ResNet-50), Vision Transformers (ViT-B/32), text models (TextCNN, TextRNN, Transformer), and BERT pre-training. This breadth supports the claim of general applicability. Results consistently show IDInit matching or exceeding baselines on CIFAR-10 (Table 2) and improving over default initialization on ImageNet by an average of 0.55% (Table 3).

- **Ablation study cleanly isolates the two proposed modifications**: Table 4 quantifies the individual contributions of patch-maintain convolution (+3.42%) and the dead-neuron fix (+5.89%) on ResNet-20/CIFAR-10, providing clear evidence that each component adds value beyond the base identity initialization.

- **Novel approach to non-square identity initialization**: Prior identity-control methods (Fixup, ZerO) initialize the non-zero weight W₁ with random or Hadamard matrices. IDInit's core idea — padding an identity-like matrix rather than zeros to handle non-square weights — is a natural and principled extension. The empirical rank analysis in Figure 4(b) supports that this padding scheme achieves higher rank than zero-padding.

## Weaknesses

### Fatal

None. While the paper has significant issues, none outright invalidate every contribution.

### Major

- **Theorem 3.1 is internally contradictory and unsupported for the claimed scenario.** The theorem claims that initializing all weights with IDI₁ yields rank(θ̂^(k)) ≥ D₀ for middle layers (k ∈ {1,...,L-2}), where θ̂^(k) = θ^(k) − I and θ^(k) ∈ ℝ^{D_h × D_h}. For these square middle layers, IDI₁ reduces to the standard identity (m ≡ j (mod D_h) ⇒ m=j), giving θ^(k) = I, so θ̂^(k) = 0 with rank = 0, which contradicts rank ≥ D₀ > 0. The paragraph immediately following the theorem further compounds the confusion: it states that ZerO's contrary claim (ranks limited to D₀) "is tenable in the initial state" — which directly undermines Theorem 3.1, which is supposed to describe the initial state. The paper then says the constraint is broken "after training for several steps," but the theorem as stated refers to initialization. This theoretical contradiction weakens the paper's core justification for the padding scheme over ZerO's approach.

- **Missing comparison to identity-control baselines on ImageNet.** The paper's central narrative critiques Fixup, ZerO, SkipInit, and ReZero for their handling of non-zero weights and dead neurons, yet the ImageNet experiments (Table 3) compare IDInit only to "Default" (standard Kaiming/Xavier initialization). The CIFAR-10 results (Table 2) do include these baselines, but the margins are small (e.g., ResNet-56 w/o BN + SGD: IDInit 93.68 vs. Fixup 93.66) and sometimes IDInit is slightly worse (e.g., ResNet-110 w/ BN + Adam: IDInit 93.50 vs. Fixup 93.69). Without direct ImageNet comparisons to the very methods IDInit claims to improve upon, the paper's central claim — that IDInit outperforms prior identity-control methods — is only partially supported.

### Minor

- **The convergence "solution" is a known property of momentum, not a novel finding.** Section 3.1 demonstrates that SGD without momentum fails on a tiny 3-layer, 10-dim problem with target −I, while SGD with momentum succeeds. The paper frames this as addressing Bartlett et al. (2019)'s convergence concern. However, momentum is standard in virtually all modern deep learning training, so this experiment merely confirms a known fact. The experiment is also too small (3 layers, 10 dimensions) to establish that IDInit avoids the slow escape problem in realistic settings. This does not invalidate the paper but the framing overstates what is shown.

- **Derivation of τ values for activation functions is not provided.** The paper states that τ_ReLU = 1/2 and τ_sigmoid = 1 are "calculated by considering the activation function" but gives no derivation, analysis, or citation connecting these values to variance propagation or dynamical isometry. Incorrect τ values could cause signal explosion/vanishing, and the lack of derivation is a gap for practitioners who might need τ for other activations (e.g., GELU).

- **Dead neuron problem prevalence is not quantified.** Figure 5 shows weight distributions from a single trained ResNet, and Table 4 shows a large 5.89% improvement from IDIZ_ε. However, the paper does not quantify how often or severely dead neurons occur with standard Fixup/ZerO setups. Zhang et al. (2019) and Zhao et al. (2021) reported successful training without such a fix, raising the question of whether the dead neuron problem is specific to the paper's particular training pipeline (e.g., BN with learnable scale set to 0). The ablation's base setting (87.01%) may not be equivalent to the Fixup/ZerO configuration that performs well in Table 2.

- **11.3% FLOPs reduction claim for BERT is unsubstantiated.** The paper reports that IDInit yields an "11.3% acceleration ratio in terms of FLOPs" but does not define how this is computed (fewer FLOPs to reach a target loss? FLOPs saved over the full training run?), nor provide error bars or comparison to other init methods. The loss curves (Figure 9) show faster convergence, which is a qualitative observation, but the specific FLOPs metric needs clarification.

- **Limitations section is empty.** The paper has a "Limitation" heading with no content (line 289). Key limitations worth acknowledging include: the reliance on standard momentum (already standard), the lack of theoretical guarantees for non-square weights after training begins, potential sensitivity to hyperparameters ε and τ, and the absence of identity-control baselines on ImageNet.

### Trivial

- The paper references a non-existent Figure number "Theorem 3.1.3" on line 114 (likely a formatting artifact).

## Nice-to-Haves

- **Error bars on ImageNet results**: While single-run ImageNet evaluations are standard practice, providing error bars or multiple seeds would strengthen the 0.55% average improvement claim.
- **Larger-scale experiments**: Extending IDInit to deeper models (e.g., ResNet-200, ViT-Large) would strengthen claims about scalability.
- **Visualization of the IDI_τ matrix for non-square FC and patch-maintain conv layers**: A figure would clarify the structure, which is not obvious from the mathematical description alone.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"No comparison to state-of-the-art identity-control methods on ImageNet"** — This point was moved to Major weaknesses (it is valid and substantive, not removed).

2. **"Implausibly large convergence gaps on ImageNet"** (Critic claim about Epochs to 60% Acc gaps straining credibility) — Removed. This is the critic's speculation without evidence. Improvements in convergence speed are exactly what better initialization should provide. The 89.4 epochs for RN-50 default on a 90-epoch schedule is unusual but not impossible; default initialization can indeed converge slowly.

3. **"Section 2 residual network formulation is unconventional"** — Removed. The formulation x^(i+1) = a(I + θ^(i,0)θ^(i,1))x^(i) is a reasonable simplification for theoretical analysis. Many ResNet analyses use equivalent forms.

4. **"Patch-maintain convolution is underspecified and unreproducible"** — Removed. The paper specifies: reshape c (k×k×c_in×c_out) → C (c_out × kkc_in), apply IDI_τ, reshape back. This is a standard reshape operation that is fully reproducible in any deep learning framework.

5. **"Figure 2 comparison is unrealistic because W₁ is almost always non-square in practice"** — Weakened and merged into the general assessment. The figure uses a square case for illustration, which is standard pedagogical practice. The non-square case is explicitly handled in Section 3.2.

6. **Strength Finder's Point 2 ("Empirical resolution of Bartlett et al. convergence problem")** — This was kept in Minor weaknesses (the convergence discussion is noted but as a minor issue rather than a strength, since the "solution" is just using standard momentum).

7. **The critic's claim that "no error bars on ImageNet" is a major issue** — Moved to Nice-to-Haves. Single-run ImageNet evaluations are standard practice in the field due to computational cost. This is not a weakness that carries weight in evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine flaw in the theoretical framing (Theorem 3.1 contradicts itself for square middle layers) and note the gap in ImageNet comparisons to identity-control baselines, but these are criticisms, not novel insights.

## Suggestions

1. **Correct or remove Theorem 3.1.** The claim that rank(θ̂^(k)) ≥ D₀ at initialization is false for square middle layers initialized with IDI₁ (which gives θ^(k) = I, hence θ̂^(k) = 0). Either restate the theorem to refer to the entire weight matrix θ^(k) rather than the residual component θ̂^(k), or clarify that it applies only after training begins. The paragraph following the theorem must be reconciled — it currently contradicts what the theorem asserts.

2. **Add Fixup, ZerO, SkipInit, and ReZero baselines on ImageNet for at least one architecture (e.g., RN-50).** This is the most critical missing experiment for supporting the paper's central claim. Without it, the community cannot assess whether IDInit improves over prior identity-control methods at scale.

3. **Provide a derivation or citation for τ values** (τ_ReLU = 1/2, τ_sigmoid = 1), connecting them to variance propagation or dynamical isometry analysis.

4. **Quantify the dead neuron problem** across multiple runs and configurations, comparing to standard Fixup/ZerO pipelines, to justify the IDIZ_ε fix and explain why other methods train successfully without it.

5. **Define the FLOPs acceleration metric** for the BERT experiment and consider reporting loss vs. wall-clock time.

6. **Fill the Limitations section** with a candid discussion of scope and potential sensitivities.

## Score and Decision

Based on my assessment: the paper addresses a worthwhile problem and presents broadly positive empirical results across diverse settings. However, the theoretical foundation (Theorem 3.1) contains a clear internal contradiction that undermines a key claimed advantage over prior work. The missing ImageNet comparison to identity-control baselines further weakens the central narrative. These are substantial issues that cannot be fully resolved in a rebuttal and would require a major revision. The paper's empirical breadth and the ablation study provide genuine value, but the core claims are not adequately supported in the current form.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>