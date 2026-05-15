Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes NEPENTHE, an iterative unstructured pruning method that aims to reduce neural network depth by leveraging neuron-state entropy. The core idea is to compute a binary ON/OFF entropy per neuron, then use an entropy-weighted pruning budget that concentrates pruning on low-entropy layers, driving their average entropy to zero so they become linearizable and removable. The method is evaluated on ResNet-18, MobileNet-V2, and Swin-T across CIFAR-10, Tiny-ImageNet, and DomainBed datasets, showing that several layers can be removed with little or no accuracy loss compared to dense models and outperforming Layer Folding and iterative magnitude pruning.

## Strengths

- **Novel formulation of depth reduction via neuron-state entropy**: The paper introduces a clean framing where binary ON/OFF states of rectifier-activated neurons define a per-neuron entropy, and the method is designed to drive whole-layer average entropy to zero. This is a genuinely new way to connect unstructured pruning to architectural depth reduction (Section 3.1).

- **Effective empirical demonstration**: Table 1 (entropy trends) and the results discussion show that NEPENTHE achieves non-trivial layer removal — e.g., 3/17 layers on ResNet-18/CIFAR-10 with top-1 accuracy 92.55% vs the dense model's 91.66% — and performs favorably against Layer Folding. The neuron-state histogram (Fig. 4) provides visual evidence of the mechanism.

- **Clean ablation study**: Table 3 (ablation) isolates the contribution of each component (entropy weighting, don't-care state, neuron selection), showing monotonic improvement from 92.18% → 92.33% → 92.55%. This is well-structured and informative.

- **Robustness across activation functions**: Table 4 demonstrates that NEPENTHE removes 3/17 layers and maintains or improves accuracy across ReLU, SiLU, PReLU, LeakyReLU, and GELU, suggesting the method is not tied to a specific activation.

## Weaknesses

### Fatal
None. The core empirical contribution (the method works) is not invalidated by the issues below.

### Major

- **The theoretical derivation in Section 3.2 is mathematically unsound**: The paper models the pre-activation Z as the *product* of a single weight and a single input (Equation 5: f_Z(z,t) = (1/π)K₀(|z/q(t)|), which is the PDF of the product of two independent standard normals, citing Craig 1936). However, a neuron's pre-activation is the *sum* over N such products: z = Σ_{i=1}^N w_i x_i. Under the stated assumptions (large N, i.i.d. centered variables), the distribution of the sum converges to a *normal* distribution by the Central Limit Theorem, not the Bessel/Struve form presented. The derivation does not correctly model the quantity it claims to. The paper calls this "oversimplified" (line 222), but the issue is not oversimplification — it is modeling the wrong random variable. The intuitive claim that pruning reduces entropy is empirically validated in Table 1, so this error does not invalidate the method; however, presenting this as a "theoretical finding" (abstract, contributions bullet 2) overstates what is actually a plausibility argument with flawed mathematics.

- **No computational performance metrics are reported despite the computational motivation**: The paper's stated motivation is to "alleviate deep neural networks' computational burden" (abstract), reduce "the critical path" (Section 1), and have "practical impact even in computation on parallel architectures" (conclusion). Yet **zero** measurements of wall-clock speed, latency, throughput, or FLOPs are reported anywhere. Layer removal is a reasonable proxy, but the paper's own claims go beyond proxy reasoning. The missing measurements are a significant gap between the claimed contribution and the evidence provided.

### Minor

- **Layer removal mechanism is underspecified**: The paper states that layers with zero entropy "can be removed" (line 284) or "absorbed by the following layer" (line 179), but never specifies the exact procedure for doing so. For always-OFF neurons, pruning is straightforward. For always-ON neurons, the paper says the neuron "can in principle be absorbed" — but with GELU and SiLU, "always ON" does not mean the activation is the identity function (the paper acknowledges this in a footnote for GELU as "very close" but does not resolve it). For LeakyReLU, always-ON still applies a multiplicative slope. No algorithm steps or equations for layer folding/absorption are provided, and it is unclear how residual connections (present in ResNet-18) interact with layer removal.

- **Missing comparison to a closely related work**: The paper cites \cite{pmlr-v202-ali-mehmeti-gopel23a} (line 59) as "a similar channel-wise approach that enables significant reduction of more non-linear units" but does not include it as an empirical baseline. Given that this work pursues the same goal (reducing non-linear units / layers), its omission weakens the evaluation.

- **No statistical significance or variance reported**: All results appear to be from single runs. Pruning is known to be sensitive to initialization and random seeds. Without multiple trials and standard deviations, it is unclear whether the reported accuracy differences (e.g., ablation improvements of 92.18 → 92.33 → 92.55) are meaningful or noise.

### Trivial
None.

## Nice-to-Haves

- Reporting wall-clock inference time or FLOPs for the compressed models vs. dense baselines would substantially strengthen the practical claims.
- A concrete worked example showing how a zero-entropy layer is physically folded into its neighbor (with explicit linear transformation equations) would clarify the removal process.
- Sensitivity analysis for ζ (per-iteration pruning rate) would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Only NEPENTHE results are mentioned for DomainBed datasets"** (from Critical Issue 4): The reviewer states that "for the DomainBed datasets... only NEPENTHE results are mentioned — no baseline comparisons are reported in the available text." The reviewer acknowledges the main results table is missing from the extracted text. The paper text (line 347) states that the table shows results "for all the considered setups" and references IMP and Layer Folding performance in the surrounding discussion. This criticism is based on the absence of the table in the parser-extracted text, not on the paper's actual content. **Removed.**

2. **Claim that the theoretical error "invalidates the theoretical claim entirely"**: The reviewer asserts the derivation is "fundamentally wrong" and "invalidates the theoretical claim." While the derivation is indeed flawed (see Major weakness 1 above), the paper's core contribution is the NEPENTHE method and its empirical validation, which stand independently. The theory is presented as suggestion/oversimplification, not as a rigorous proof on which the method depends. The claim of total invalidation overstates the impact of this flaw. **Rephrased and downgraded to Major weakness 1 above.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations that the paper itself does not already articulate or imply.

## Suggestions

1. **Remove or substantially revise the theoretical derivation (Section 3.2)**: The current product-of-Gaussians argument is mathematically incorrect for the pre-activation sum. Either replace it with a correct derivation (e.g., showing that magnitude pruning reduces the variance of the pre-activation distribution, which for rectifier activations concentrates probability mass toward one state) or reframe it as an intuitive motivation supported by the empirical evidence in Table 1, removing the claim of a "theoretical finding."

2. **Report computational performance metrics**: At minimum, measure and report the inference FLOPs of the compressed models vs. dense baselines. Wall-clock latency on GPU would be even stronger.

3. **Specify the layer removal procedure**: Include algorithmic steps or equations showing how a zero-entropy layer is physically removed or folded for each activation type (ReLU, GELU, SiLU, LeakyReLU). Clarify how residual connections are handled.

4. **Add \cite{pmlr-v202-ali-mehmeti-gopel23a} as an empirical baseline**: Since this work is cited as closely related, a direct comparison would significantly strengthen the evaluation.

5. **Report results over multiple random seeds** with means and standard deviations for the main results.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>