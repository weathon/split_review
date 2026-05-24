Now I have all the data I need. Let me produce the final consolidated review.

**Calibration Summary (all rounds):**

**Round 1 (Bracketing):**
- Low anchor (<3.5): SF-PE (2.67, Reject), SPARTA (2.50, Withdrawn) — no ImageNet, fatal code-theory mismatch
- Mid anchor (3.5-7.5): Positional Encoding for Spiking Transformers (4.50, Reject), TP-Spikformer (4.50, Accept Poster), STAS (4.00, Withdrawn)
- High anchor (>7.5): Not SNN-relevant (language models, quantum, navigation)

**Round 2 (Narrowing, bracket 4.0-6.0):**
- SMixer (5.00, Accept Poster) — clean execution, limited novelty
- SpikeDet (4.00, Withdrawn) — strong results but vague mechanism, missing ablations
- Gradient Checkpointing for SNNs (5.50, Accept Poster) — practical, well-executed, limited novelty

**Final comparison:** The paper has better problem diagnosis and more novel contributions (LRF in SSA) than the 4.0-4.5 anchors, but has vaguer methodological exposition than the 5.0-5.5 papers. Score: 4.5.

Now let me produce the review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- Concrete, specific strengths backed by evidence.
- Not generic.

## Weaknesses
### Fatal
None.

### Major
Issues that would weigh against acceptance.

1. LRF-Dyn derivation is insufficiently specified
2. No actual memory measurements reported
3. Table 2 inconsistency

### Minor
1. Theorems rely on assumed functional forms

### Trivial
None.

Let me now write it properly.

Actually, I need to be careful about the LRF-Dyn criticism. Let me re-examine what the paper says:

Section 5.2:
- Eq. 8 is the LRF-SSA formulation
- Eq. 11 rewrites it causally: sattn'_n[t] = q_n[t] × Σ_{j=1}^{n-1} k_j[t]^T v_j[t] + Σ_{d,i,j∈Ω_d} r_{ij}^d v_{ρ_k}[t]
- Text says: "It closely parallels the charge-fire-reset dynamics of spiking neurons, where the first term represents membrane potential information and the second term represents presynaptic input."
- Then Eq. 12: X_n[t] = A ⊙ X_{n-1}[t] + Γ Token_n[t], sattn'_n[t] = X_n[t] + Σ_{d,i,j∈Ω_d} r_{ij}^d · X_{ρ_k}[t]

The mapping is:
- Eq 11 first term: q_n[t] × Σ_{j=1}^{n-1} k_j[t]^T v_j[t] → this is like a "memory potential"
- Eq 12 first eq: X_n[t] = A ⊙ X_{n-1}[t] + Γ Token_n[t] → recurrent dynamics
- Then sattn'_n[t] = X_n[t] + LRF_term

These are not obviously equivalent. The paper says "it closely parallels" but doesn't derive how A, Γ, and Token relate to q, k, v. This IS a valid concern.

Let me check if the paper addresses this: "Inspired by other softmax-free attention... LRF-SSA can be reformulated through causal inference to significantly reduce memory consumption." So they rewrite LRF-SSA in causal form (Eq. 11), then observe it resembles neuron dynamics (text after Eq. 11), then propose LRF-Dyn (Eq. 12). The connection is analogical, not derived.

But then Eq. 13 defines A and Γ in dendritic form. These don't obviously connect back to the q, k, v from Eq. 11. So how does LRF-Dyn actually compute attention? The paper says "Owing to the time-invariant property of the A matrix, the neuron can be trained efficiently following the (Chen et al., 2024)." But this doesn't explain how the output relates to attention.

So yes, the harsh critic's criticism about LRF-Dyn being vague is valid. The paper asserts a correspondence but doesn't establish it rigorously.

However, the harsh critic said "The method as described is not reproducible." This is a strong claim. Given that the paper does present equations and references Chen et al. 2024 for training, "not reproducible" may be too strong. But the method's relationship to attention computation IS unclear.

Let me also check: does the paper say which version (Eq. 12 vs Eq. 15) is used? Section 5.3 presents Eq. 15 as the "dynamics of LRF-Dyn" using Fourier transforms. Eq. 12 is also presented as the dynamics. Neither is specified as "the one used in experiments." This creates confusion.

OK, now let me write the final review carefully.## Summary

This paper identifies two key limitations in Spiking Transformers — poor local modeling due to the absence of softmax in SSA, and high memory overhead from storing attention matrices — and proposes LRF-Dyn to address both. The method proceeds in two steps: (1) LRF-SSA, which injects dilated depthwise convolutions into spiking self-attention to strengthen local receptive fields, and (2) LRF-Dyn, which aims to approximate the resulting attention computation via neuronal charge-fire-reset dynamics to eliminate explicit attention-matrix storage. Experiments on ImageNet classification and ADE20K segmentation across three spiking Transformer backbones (Spikformer, QKFormer, SDT-V3) show consistent gains of 0.44–1.24% top-1 accuracy with the LRF-SSA variant.

## Strengths

1. **Well-diagnosed problem with quantitative evidence.** Section 4.1 and Figure 2 directly quantify SSA's limited local modeling: only 20.31% of SSA attention falls within Manhattan distance 5 (vs. 76.68% for VSA), and SSA's attention entropy is 0.5637 (vs. VSA's 0.1777). This measurement-based diagnosis is concrete and provides a clear motivation for the proposed LRF injection.

2. **Consistent accuracy gains across architectures and tasks.** Table 1 shows LRF-SSA improves top-1 accuracy on all three backbones (Spikformer: +1.24%/0.85%, QKFormer: +0.44%/0.48%, SDT-V3: +0.92%/0.51%). Table 2 shows +2.6% MIoU on ADE20K semantic segmentation. The gains are consistent across multiple architectural families and parameter scales, supporting the generality of the approach.

3. **Ablation study confirms the source of improvement.** Table 3 systematically varies the LRF kernel count (Ω ≤ 1, 3, 5) and shows monotonic accuracy gains for both LRF-SSA and LRF-Dyn on CIFAR-100, isolating the LRF module as the source of improvement rather than an artifact of other changes.

4. **ERF visualizations corroborate the theoretical claim.** Figure 5(a) shows effective receptive field heatmaps where LRF-SSA and LRF-Dyn produce substantially more localized ERFs than SSA, consistent with the intended effect of the LRF injection.

## Weaknesses

### Fatal
None.

### Major
1. **LRF-Dyn derivation is insufficiently specified.** The paper's second core contribution — approximating attention via neuronal dynamics — lacks a clear, step-by-step mapping. The text states that Eq. 11 "closely parallels the charge-fire-reset dynamics" and then presents Eq. 12 as the dynamical system, but the transition is analogical rather than derived. The parameters 𝒜 and Γ in Eq. 13 are presented with unclear dimensionality (a scalar row vector times a matrix that is then used in a Hadamard product), and it is not explained how they relate to the query/key/value quantities in the original attention formulation. Furthermore, two distinct formulations are presented (Eq. 12's recurrent dynamics and Eq. 15's Fourier-convolution operator) without stating which is used in the experiments or how they relate. Readers cannot determine how to implement LRF-Dyn from the description alone.

2. **No absolute memory measurements reported.** Despite the paper's title and contributions emphasizing reduced memory, no actual peak GPU memory figures (MB/GB) are reported. The only quantitative evidence is the sentence in Section 6.2 that LRF-Dyn "reduces memory usage by 49.4%" under Spikformer-8-512 — but this percentage is presented without a derivation, without a baseline absolute value, and without a table comparing memory across all model configurations. The theoretical complexity notation (𝒪(kd) vs. 𝒪(d²)) is necessary but not sufficient; absolute measurements are expected for a claimed advantage central to the paper's narrative.

3. **Table 2 contains a numerical inconsistency.** In the segmentation results (Table 2), the baseline SDT-V3 large model is listed as "18.99 + 1.4" parameters, but the SDT-V3 + LRF-SSA large row shows "10.0 + 1.4" — a *decrease* in backbone parameters despite LRF-SSA adding convolutional kernels. Table 1 reports the same model as 19.25M total parameters. The "10.0" is clearly erroneous (likely a typo for ~19.25). This undermines confidence in the table's accuracy and needs correction.

### Minor
4. **Theorems assume specific attention functional forms without justification.** Theorems 1 and 2 posit that VSA attention decays exponentially with Manhattan distance and SSA attention decays linearly (α − βΔ)_+. These forms are asserted rather than derived from attention distributions. As a result, the theorems' conclusions (that LRF-SSA's expected receptive field is smaller and its entropy lower) follow from the assumed premises rather than from the actual behavior of the models. The paper would benefit from either justifying these forms empirically (which Figure 2 partially does for the decay trends) or reframing the discussion as intuitive characterization rather than formal proof.

### Trivial
None.

## Nice-to-Haves
- Measure and report actual peak GPU memory (MB) for all models in Tables 1–2 to substantiate the memory-reduction claim.
- Include an ablation varying the number of dendrites k in LRF-Dyn to show the memory-accuracy trade-off explicitly.
- Report computational cost in terms of synaptic operations (SOPs) or AC/MAC energy estimates, which is standard practice in the SNN literature.
- Provide a comparison with other memory-efficient attention mechanisms (linear attention, FlashAttention) to contextualize the relative benefit.

## Removed Points

These points from the harsh critic were considered and removed with justification:

- *"No runtime or energy measurements are provided, which would normally be expected for SNN papers."* — Reasonable but moved to Nice-to-Haves. The paper's core memory claim is the primary focus; energy and runtime were not positioned as core contributions.
- *"The paper does not provide the proofs in the main text and expects the reader to accept the statements as rigorous."* — **REMOVED (hard rule).** The parser strips appendices; proofs exist in the original submission.
- *"No training or inference procedure is specified for the new parameters (dendrite weights, decay factors, membrane capacitance)."* — Mitigated by the paper's reference to Chen et al. (2024) for training procedure. Overstated as a fatal omission.
- *"No comparison with other memory-efficient attention schemes (e.g., linear attention, Performer, FlashAttention)."* — Moved to Nice-to-Haves. Not part of the paper's stated scope; SSA-based methods are the comparison baseline.
- *"The theorems add little credibility"* and *"The entropy inequality in Theorem 2 uses an undefined αᵢ, making the proof circular."* — The harsh critic's claim about αᵢ being undefined in the main text is correct, but the proof is deferred to the (stripped) appendix. The fundamental concern about assumed functional forms is retained as a Minor weakness; the circular-proof accusation cannot be verified without the appendix.
- *"Overclaimed theoretical results"* — softened from "overclaimed" to a factual description: the theorems rely on assumed forms. The "false impression of mathematical support" language is removed as it is a judgment call beyond verifiable facts.
- *"Method as described is not reproducible"* — downgraded to "insufficiently specified" because equations are presented, even if the mapping is incomplete. "Not reproducible" is too strong given the equations and the reference to Chen et al. for training.
- Strength Finder's claimed strength about "memory reduction with accuracy gain" (item 2) — retained with the caveat that only the 49.4% number (without absolute values) is reported. The strength exists but is weakened by the missing absolute measurements.

## Novel Insights

The primary novel observation emerging from the review — beyond what the paper itself states — is the asymmetry between the two proposed components. LRF-SSA (adding dilated depthwise convolutions to SSA) is a simple, clear, and empirically validated engineering contribution that consistently improves performance across backbones. LRF-Dyn, by contrast, attempts a more ambitious theoretical bridge between attention computation and neuronal dynamics, but the exposition lacks the precision needed to evaluate whether the bridge is real or merely asserted. The paper's empirical success therefore rests almost entirely on the LRF-SSA component, which is a worthwhile but modest architectural improvement. Whether LRF-Dyn actually implements attention through dynamics or is better understood as a separate recurrent mechanism with LRF-inspired structure remains unresolved.

## Suggestions

1. **Clarify LRF-Dyn.** Provide an explicit derivation showing how Eq. 11 maps to Eq. 12 — or state clearly that the correspondence is approximate/inspirational rather than exact. Specify which formulation (Eq. 12 or Eq. 15) was used in experiments, and describe the training and inference procedures for the dynamical parameters (𝒜, Γ, number of dendrites).

2. **Add absolute memory measurements.** Report peak GPU memory in MB for all configurations in Table 1, ideally at the same batch size and sequence length, so the 49.4% reduction claim can be verified.

3. **Fix Table 2.** Correct the "10.0 + 1.4" entry for the large LRF-SSA model to its proper value (~19.25 + 1.4) and ensure all parameter counts in Table 2 are consistent with Table 1.

4. **Reframe Theorems 1–2.** Either provide empirical justification for the assumed attention forms (using the data already collected for Figure 2) or present the results as intuitive illustrations rather than formal theorems with unchecked premises.

5. **Separate the two contributions more clearly in the narrative.** The paper would be stronger if it acknowledged that LRF-SSA and LRF-Dyn are at different stages of maturity — the former is a finished architectural contribution, while the latter is a promising direction that requires further theoretical and empirical development.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>