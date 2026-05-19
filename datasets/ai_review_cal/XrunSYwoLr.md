- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have all the information needed. Let me compose the consolidated review.

## Summary

This paper proposes Spatio-Temporal Approximation (STA), the first pipeline to convert a pretrained ANN Transformer into a purely event-driven SNN without training on the target dataset. Two novel modules are introduced: Universal Group Operators (UGOs), which use small groups of IF neurons trained on synthetic data to approximate complex non-linearities (GELU, sqrt, etc.), and a Temporal-Corrective Self-Attention Layer (TCSA), which handles non-causal spike multiplications in self-attention via an estimation-correction mechanism with proven quadratic convergence. The pipeline is validated on ViT-B/32 from CLIP, demonstrating zero-shot classification and standard classification performance with faster simulation (T=32–64) than CNN-based conversion methods.

## Strengths

- **First conversion pipeline targeting pretrained Transformers to event-driven SNNs.** The paper clearly identifies two Transformer-specific obstacles (complex non-linearities, variable-variable multiplications in self-attention) that prior conversion methods cannot handle, and provides principled solutions (UGOs and TCSA) rather than ad-hoc patches. This addresses a genuine gap: all existing ANN-to-SNN conversion methods are limited to CNNs.

- **Theoretical error analysis for both modules.** Theorem 1 decomposes the UGO approximation error into empirical, parameterization, and quantization gaps that are used to guide concrete design choices (layer-specific regularization, hyperparameter selection). Theorem 3 proves that the temporal estimation error in TCSA decreases quadratically with time steps. These analyses go beyond heuristic design and provide provable guarantees for the conversion quality.

- **Demonstration on a large-scale pretrained model (ViT-B/32 from CLIP, 87.8M parameters).** The paper converts a real, widely-used model and evaluates it on zero-shot benchmarks (CIFAR-10/100, ImageNet-200, distribution-shifted variants) and standard classification. The converted SNN inherits CLIP's zero-shot capabilities and achieves competitive accuracy with fewer simulation steps (T=32–64) than existing CNN-based conversion methods (which typically need T≥128).

- **Ablation studies isolating each component.** The paper reports that removing either UGO or the estimation-correction mechanism significantly degrades performance on CIFAR-100, empirically validating that both spatial and temporal approximations are necessary.

- **Energy analysis with per-module savings.** The paper provides quantitative SOP/FLOP comparisons, reporting 41% savings for UGOs over GELU and up to 75% savings for the sparsest attention modules via TCSA, with explicit formulas for the estimates.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "training-free" framing conflates two different meanings.** The paper repeatedly uses "training-free" in the title, abstract, and contributions, but the UGOs require training a small ANN on synthesized data (Section 4.1, Construction Step 2). While "training-free" in the conversion literature conventionally means no training on the target dataset — and the paper is transparent about the synthetic-data training — the term will mislead readers expecting zero training of any kind. This is a framing mismatch, not a technical flaw, but it affects how the contribution is positioned relative to truly training-free (Diehl et al., 2015) and training-dependent conversion methods. The paper could say "no training on the target task" or "synthetic-data-driven approximation" without diminishing its novelty.

- **The zero-shot evaluation's primary baseline is cross-architectural (ViT vs. ResNet-50).** Table 1 compares the converted ViT to converted ResNet-50 from the same CLIP model. This comparison says more about the relative strength of the base architectures than about the efficacy of the STA conversion pipeline. Although the paper mentions "much lower accuracy drop after conversion" for ViT (Section 6.2), explicit tabulation of *absolute* conversion gaps (ANN ViT accuracy minus converted SNN accuracy) for the zero-shot setting would more directly support the claim that STA preserves the source model's capabilities. The paper does report ANN-ViT comparisons for standard classification (Section 6.3: "remaining small accuracy gap to ANN ViT"), which partially addresses this concern.

- **The energy estimation assumes firing rates rather than reporting measured ones.** Section 6.4 uses an "empirical firing rate" η≈9.1% for UGOs and η∈[3%,13%] for attention modules, but these values appear to be assumed averages rather than actual spike counts measured from the converted network. Since the whole energy argument depends on these rates, reporting the actual firing statistics observed during inference would substantially strengthen the claims. The paper also notes that the latest hardware supports hybrid floating-point/event-driven computation, which somewhat undercuts the claim of purely event-driven efficiency.

- **Hardware overhead of TCSA's time-dependent divisions is not addressed.** The Q(t) update in Definition 3 involves scaling by 1/t and 1/(1−t). The paper claims these can be "pre-integrated into the linear layers W before inference," but the time-dependent scaling factors change at each step t, making literal pre-integration into a single weight matrix non-trivial. A concrete mapping onto event-driven hardware or an acknowledgment of the overhead (e.g., per-step scalar multipliers) is needed.

- **Theorem 3's assumptions are strong and their violations are undiscussed.** The convergence proof assumes spiking sequences follow a "stationary independent process" with a fixed number of emitted spikes — a stochastic model that does not match the deterministic threshold-based encoding used in actual conversion. The paper does not analyze how violations of this assumption (e.g., temporal correlations in spike trains, variable firing rates across layers) affect the practical convergence behavior.

- **No comparison to existing spiking Transformers.** The paper correctly notes that models like Spikformer (Zhou et al., 2022, 2023) are trained from scratch and structurally different from ANN Transformers. Nevertheless, reporting their accuracy on the same benchmarks (even as secondary context) would help readers calibrate whether the conversion route recovers competitive accuracy. Without this, the paper's "state-of-the-art" claim (Section 6.3) refers only to the conversion literature, which is exclusively CNN-based.

- **Conclusion makes speculative claims about LLM applicability.** Section 7 extends the pipeline broadly to "Large Language Models, as our subsequent work" without any evidence. This is unnecessary and undermines the otherwise measured tone.

### Trivial

None.

## Nice-to-Haves

- A direct (ablation-like) comparison: convert a ViT using the closest available alternative (e.g., replace GELU with ReLU, skip temporal correction) and show how much UGO and TCSA each recover. The paper mentions this ablation (Fig. 6) but numerical values are not in the extractable text.
- Reporting actual membrane potential traces or firing rate histograms from the converted network to visually validate the "residual potential accumulation" motivation for TCSA.
- A discussion of the memory/parameter cost of inserting UGOs (each is a 2-layer network with N neurons) into every non-linear operation in the Transformer.

## Removed Points

These points were raised by reviewers but are removed per the filtering rules:

- **Missing Table.G.2 / Figure 6 / appendix content:** The text-extracted version omits these (parser artifact). The original submission includes them.
- **"No discussion of how to determine 𝒟 for a given target model without training data":** The paper explicitly states that LayerNorm constrains the input range empirically and gives a concrete example (𝒟=[−10,10] for GELU). The reviewer's hypothetical concern about unknown ranges across all layers is not supported by the paper's methodology.
- **"The comparison in Table 1 doesn't say anything about conversion preserving strength":** The paper reports accuracy drops ("much lower accuracy drop after conversion"), which directly compares conversion efficacy. The critic overlooked this.
- **"No statistical significance or variance reported":** Single-run evaluation on standardized benchmarks is the norm in this field; this is not a meaningful omission.
- **"The integration of prior techniques is mentioned but not described":** The paper briefly describes MMSE, signed neurons, and burst spikes with citations (Section 6.1). Full re-description of prior techniques is unnecessary.
- **"Theorem 1 constants depend on function class and network size but are not discussed":** The paper provides the error decomposition structure, which is the intended contribution. Bounding the individual constants for specific functions is a separate exercise.
- **Formating nitpicks, typos, and grammar complaints:** Parser artifacts, not author errors.

## Novel Insights

The harsh critic and strength finder both identify that the paper's core division — spatial approximation via UGOs and temporal approximation via TCSA — is sensible and addresses a genuine gap. The most interesting observation not fully developed in the paper or reviews: the UGO framework transforms the conversion problem from "how to express Transformer operations exactly in spikes" to "how to approximate them with controlled error." This re-characterization is more significant than any single module, because it opens the door to treating conversion as an approximation problem with explicit trade-offs between neuron count N, time steps T, and precision. The temporal estimation-correction mechanism (TCSA) is a clever insight that the naive temporal split preserves equality but produces unstable intermediate dynamics — the innovation is recognizing that the *intermediate* behavior matters for downstream SNN functionality even when the *final* sum is correct.

## Suggestions

1. **Reframe "training-free"** to "training on synthetic data only" or "no training on the target dataset" to match what the method actually does.
2. **Show ANN ViT accuracy alongside converted SNN accuracy** in the zero-shot results table, and compute the absolute conversion gaps explicitly. This directly answers the main evaluation concern.
3. **Report measured firing rates** from the converted model (per layer, per module) to ground the energy analysis in empirical data rather than assumed ranges.
4. **Acknowledge the TCSA time-dependent scaling overhead** honestly. Either provide a concrete mapping onto neuromorphic hardware (e.g., a per-step scalar multiplier that can be implemented with low overhead) or state that the energy estimates exclude this cost.
5. **Add a paragraph discussing limitations of Theorem 3's assumptions** and how violations (temporal correlations, non-stationary firing) would affect convergence in practice.
6. **Drop the speculative LLM generality claim** in the conclusion, or replace it with a concrete description of what a conversion of a text model would require.
