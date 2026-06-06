## Summary

DelRec introduces the first surrogate gradient learning (SGL)-based method to train axonal or synaptic transmission delays in **recurrent** connections of spiking neural networks (SNNs). The method employs a differentiable triangle-interpolation scheme (Eqs. 9–11) with a progressively sharpened spread parameter σ, allowing real-valued delay optimization during training and clean rounding to integers at inference. Using simple LIF neurons, DelRec achieves new state-of-the-art accuracy on SSC (82.58±0.08%, 3 seeds) and PS-MNIST (96.21%, 1 seed) and includes a controlled ablation on SHD that characterizes the relative benefit of recurrent versus feedforward delay learning.

---

## Strengths

- **Genuine methodological novelty**: DelRec is, to the best of the literature's knowledge (confirmed in Section 1), the first SGL-compatible method for learning recurrent delays. The differentiable interpolation (Eqs. 9–11) with decreasing σ is principled and cleanly handles the discrete–continuous transition, building cleanly on the DCLS feedforward framework.
- **Strong SSC result with proper statistical treatment**: 82.58±0.08% across 3 seeds with 0.37M parameters surpasses all prior models in the comparison class, including those with more complex adaptive neuron dynamics (SE-adLIF at 80.44±0.26%, RadLIF at 77.4%, etc.), and the variance is narrow enough to make the margin credible.
- **Informative and methodologically honest SHD ablation**: The paper uses 20% of training data as a held-out validation set and reports over 10 seeds, explicitly noting that accuracy differences above 93% are likely not statistically significant given the 2264-sample test set. This level of calibration is rare in the SNN literature and directly supports the comparative phase findings in Figure 3B/3C.
- **Efficient scheduling**: The finite-support argument (Eqs. 12–13) combined with the pointer mechanism (Algorithm 1) ensures the scheduling matrix has bounded memory proportional to the maximum delay rather than O(T²), making the approach practical for long sequences.
- **Clean training-to-inference transition**: σ is reduced to 0 across training epochs, yielding linear interpolation between the two nearest integer delays at the end of training (Fig. 2C), followed by deterministic rounding — a well-defined deployment path.
- **Broad compatibility and reproducibility**: Implementation in SpikingJelly with full hyperparameters in Tables 2–3 and an anonymous repository makes the method accessible and reproducible.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **PS-MNIST SOTA claim rests on a single seed with a thin margin.** Table 1 shows DelRec at 96.21% versus ASRC-SNN's reproduced 95.77%, a gap of 0.44%. The paper justifies single-seed evaluation by noting "all the previous state-of-the-art models on the dataset" followed this convention (Section 3.1). While this aligns with field norms, it means the margin is indistinguishable from plausible run-to-run variance. The SSC SOTA claim (3 seeds, narrow SE) is much better evidenced; the PS-MNIST claim should be presented with more caution or backed by additional seeds.

- **Unexplained regression when combining delay types on SSC.** Table 1 shows "DelRec (only Rec. delays)" at 82.58±0.08% outperforming "DelRec (Rec. and Ff. delays)" at 82.19±0.16%. The paper does not explain this reversal. The conclusion mentions "we believe that further improvements could be obtained by … better combining DelRec with feedforward delays" but offers no explanation for why the combination currently underperforms. The SHD ablation (Fig. 3B) shows the same pattern in small models ("Learned feedforward and recurrent delays" ≈ 75%, below either type alone at ≈80–82%). The paper acknowledges the tradeoff exists but does not provide a hypothesis or ablation targeted at SSC to illuminate it. This complicates the paper's framing that the two delay types are complementary.

- **Gradient-flow motivation is not empirically grounded.** The introduction (Section 1 and Figure 1B) presents reduced vanishing/exploding gradient risk as a distinct functional advantage of recurrent delays, via temporal skip connections. Figure 3C shows that fixed random recurrent delays outperform the vanilla RSNN, which is consistent with this claim but confounds gradient flow improvement with generic temporal processing benefits. No experiment measures gradient norms, gradient propagation depth, or training stability. The mechanistic claim therefore remains illustrative rather than demonstrated.

### Trivial

- The text at line 98 refers to "Eq. 15" while the equation being discussed appears to be Eq. 11 in the body text — likely a numbering artifact from appendix equations that were stripped during parsing. Worth checking in the final submission.

---

## Nice-to-Haves

- A controlled SSC ablation (plain RSNN → RSNN with fixed recurrent delays → DelRec) at matched parameter counts would directly quantify how much recurrent delay learning contributes to the SSC SOTA (vs. having recurrent connections at all), and would help explain the combined-delay regression.
- A simple diagnostic plotting mean gradient norm as a function of time-step depth for vanilla RSNN vs. DelRec would empirically ground the gradient-flow motivation in Figure 1B.
- Running 3 seeds on PS-MNIST (matching the SSC protocol) would make that SOTA claim as defensible as the SSC one, at modest additional cost.
- A brief qualitative analysis of inference-time memory overhead for the scheduling matrix as a function of maximum delay would strengthen the neuromorphic hardware deployment motivation cited in the abstract.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — Eq. 15/11 numbering as a substantive reproducibility issue**: The critic raises this as a concern about gradient flow documentation. The reference to "Eq. 15" in the body likely refers to an appendix equation; the appendix is stripped by the parser. This is a parsing artifact, not an author error.
- **Harsh Critic — ASRC-SNN asterisk insufficiently prominent**: Criticism that readers may miss the methodological asterisk in Table 1 is a minor presentation nitpick that does not affect the scientific content.
- **Harsh Critic — feedforward vs. recurrent parameterization heterogeneity (axonal vs. synaptic) as a flaw**: The paper explicitly acknowledges this difference in Section 3.2: "it is worth noting that we are comparing synaptic feedforward delays (one delay per synapse), with axonal recurrent delays (one delay per neuron)." The comparison is heterogeneous, but its limitations are stated. Removed as the concern is already addressed.
- **Strength Finder — "broad applicability" and "important problem" as generic strengths**: Removed per filtering rules. The retained strengths are the concrete, paper-specific ones.
- **Strength Finder — "SHD comparison demonstrates recurrent delays outperform feedforward delays across the board"**: Partially conflicts with the verified weakness that the combined-delay condition underperforms either type alone in small models; the statement is overgeneralized. Removed.

---

## Novel Insights

The paper's most interesting empirical finding — beyond confirming the value of trainable delays — is the **inverted performance ordering when combining delay types**: on both SHD small models (Fig. 3B) and SSC (Table 1), having only recurrent delays outperforms having both. This is not predicted by the "complementary temporal processing" framing and suggests a potential interference effect or optimization difficulty when both delay types are jointly trained. If this is a reproducible phenomenon, it would have practical implications for delay-learning architecture design. A second insight, supported by Fig. 3C (bottom), is the **energy/performance tradeoff between delay types**: feedforward delays achieve equivalent accuracy at a lower mean firing rate, suggesting that the choice of delay type is not just a performance question but an energy-budget question — relevant for neuromorphic deployment where energy is the primary cost.

---

## Suggestions

1. Report PS-MNIST with at least 3 seeds; state explicitly whether the SOTA claim is seed-robust.
2. Add an explanatory hypothesis — or a targeted ablation — for why combining recurrent and feedforward delays regresses on SSC. Even a qualitative discussion would strengthen Section 3.2.
3. Consider adding a gradient-norm diagnostic for the vanilla RSNN vs. DelRec comparison to empirically support the temporal skip-connection motivation in Figure 1B.
4. Clarify the SSC combined-delay result in the conclusion; the current framing ("we believe further improvements could be obtained by better combining DelRec with feedforward delays") sidesteps the observed regression rather than explaining it.

---

**Evaluation:**

| Axis | Assessment |
|---|---|
| **Originality** | High — first SGL method for recurrent delays; principled differentiable approach |
| **Importance** | High — recurrent delays are biologically grounded and underexplored in the SNN literature |
| **Claims Supported** | Mostly well-supported; SSC (3 seeds) strong, PS-MNIST (1 seed) weaker |
| **Soundness** | Sound method, rigorous SHD ablation, appropriate statistical caveats |
| **Clarity** | Good — well-organized with clear figures, tables, and architecture descriptions |
| **Community Value** | High — implements in SpikingJelly, opens the recurrent-delay research direction, establishes new SOTA on key benchmarks |

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>