Now I have all the information I need. Let me produce the consolidated review.

## Summary

The paper introduces WARP (Weight-space Adaptive Recurrent Prediction), a sequence model that uses the weights of a small MLP ("root network") as its recurrent hidden state, driven by input differences Δxₜ rather than direct inputs. The hidden state θₜ serves double duty as both the recurrent state and the parameters of a non-linear decoder that produces outputs. The architecture supports dual training modes (convolutional and recurrent), gradient-free adaptation at test time, injection of physical priors, and in-context learning. Empirical evaluation spans image completion, energy/traffic forecasting, dynamical system reconstruction, UEA time series classification, and ICL tasks.

## Strengths

- **Novel architectural combination.** WARP is the first model to explicitly cast the weights of an auxiliary MLP as the hidden state of a linear RNN, combining linear recurrent dynamics (hardware-efficient, parallelizable) with non-linear decoding through the root network. This is a genuine design innovation over standard linear RNNs/SSMs, which use a fixed linear readout C·hₜ.

- **Input-difference-driven recurrence.** Using Δxₜ = xₜ − xₜ₋₁ rather than xₜ directly is an underexplored design choice in discrete-time RNNs. The paper provides a reasonable rationale (proportional updates for slow vs. fast changes, connection to continual learning) and this choice demonstrably works across diverse tasks.

- **Broad and ambitious empirical evaluation.** The paper evaluates across multiple modalities (images, univariate/multivariate time series, dynamical systems, synthetic ICL) and multiple task types (forecasting, classification, reconstruction, adaptation). This breadth is unusual and demonstrates the flexibility of the architecture. WARP achieves best or near-best results on several benchmarks (EthanolConcentration, Heartbeat classification; energy forecasting on ETT; competition with SSMs on image completion).

- **Physics-informed variant shows genuine promise.** On MSD and MSD-Zero, WARP-Phys achieves an order-of-magnitude improvement over the black-box WARP, demonstrating that the weight-space framework can meaningfully incorporate domain knowledge.

- **Gradient-free ICL demonstration.** The paper shows that WARP can learn linear mappings from context without gradient updates during inference, and that the final root network θ_{T-1} can be extracted for subsequent queries — a genuine computational advantage over transformer-based ICL.

## Weaknesses

### Major

- **PEMS08 result is extraordinary and insufficiently justified.** The paper reports MAE 6.59 vs. STDCN's 13.45 — a 51% improvement on a well-studied benchmark with years of specialized graph-based methods. The only hint of explanation in the main text is "we preprocess the input sequence with a non-causal convolution, as detailed in Appendix D." Non-causal convolution on traffic data can introduce data leakage if it allows the model to see future information during training. This result is so anomalously good that it raises immediate red flags. The paper would need to demonstrate (a) exact same train/test splits, (b) that the non-causal preprocessing does not leak future information across the train/test boundary, and (c) ideally, reproduce this on another traffic benchmark. Without this, the result undermines confidence in all other reported numbers.

- **WARP-Phys on SINE* is trivial curve-fitting, not a meaningful demonstration.** The paper embeds τ ↦ sin(2πτ + φ̂) in the root network, where the ground-truth function is τ ↦ sin(2πτ + φ). The model *contains the exact ground-truth functional form as a subcomponent*, with only φ predicted by an MLP. The "order of magnitude" improvement over baselines that lack this prior is entirely expected and proves nothing about WARP's architecture. The more interesting result is on MSD (where the physical prior is unspecified in the main text), but the presentation groups MSD and SINE* together with the same "order of magnitude" claim, conflating a genuine achievement with a trivial one.

- **"Weight-space learning" framing is inflated.** The paper repeatedly frames WARP as "unifying weight-space learning with linear recurrence" and as operating "directly within the weight space of neural networks." However, the standard weight-space learning literature (e.g., [85], [91], [28], [24]) processes the weights of *already-trained models* as input data. WARP does not do this: it generates θₜ on-the-fly as a recurrent state that happens to be reshaped into MLP parameters. This is better described as "using MLP parameters as a high-dimensional hidden state with a non-linear decoder" rather than weight-space learning in the established sense. The paper's footnote 1 (citing [106]) attempts to redefine the terminology, but the gap between the paper's framing ("transformative paradigm") and what it actually does is significant and will mislead readers.

### Minor

- **Classification results are more modest than the narrative suggests.** The paper claims "top three in 4 out of 6 datasets," which is technically correct, but on EigenWorms (the longest sequence at ~18k timesteps), WARP achieves 70.93% vs. LinOSS at 95.0% — a 24-point gap and 8th place out of 11. On SCP1, WARP ranks 4th (83.53% vs. 87.8%). The paper acknowledges long-sequence difficulty in its limitations, but the abstract and introduction give a different impression.

- **No controlled baseline isolating the weight-space contribution.** The paper never compares WARP against a simple ablated baseline: a linear RNN with the same hidden dimension D_θ but a standard non-linear readout (e.g., yₜ = MLP_ψ(hₜ, τ) where ψ are learned parameters, not the hidden state itself). This would test whether the "self-decoding" (θₜ as both state and decoder parameters) is the source of improvement, or whether any large linear RNN with a non-linear decoder would work as well.

- **Negative BPD on CelebA without discussion.** WARP achieves BPD = -0.043 and -0.162 on CelebA. While negative BPD is possible for continuous density models with very small predicted variance, this is unusual and the paper offers no explanation. Combined with the fact that baselines show absurd BPD values (e.g., LSTM at 3869, GRU at 24.14), the CelebA evaluation appears unreliable.

- **The ICL experiment is a non-standard setup.** Standard ICL for linear regression (e.g., von Oswald et al., Garg et al.) presents key-value pairs followed by a query and evaluates whether the model learns the underlying mapping. WARP uses a cumulative-sum transformation and predicts the *entire* output sequence (including training targets) rather than just the query. While this may be reasonable, it deviates from the established protocol, making direct comparison to prior ICL results difficult.

- **Missing ablation on the necessity of high-dimensional D_θ.** The paper uses large θₜ (millions of parameters). An ablation varying D_θ while keeping the root network shape fixed would clarify whether performance comes from the high-dimensional linear dynamics or from the weight-space reformulation.

### Trivial

- The ETT heatmap (Figure 3b) does not report error bars or statistical significance for the comparisons.
- The paper claims "infinite-dimensional" hidden states (Conclusion), which is a mathematical overstatement — a linear RNN with dimension D_θ is D_θ-dimensional, regardless of reshaping.

## Nice-to-Haves

- Compare WARP against a controlled baseline: a linear RNN with the same D_θ and a non-linear readout MLP with learned parameters (not the hidden state itself). This would isolate the benefit of the self-decoding design.
- Validate the PEMS08 result on at least one additional traffic benchmark and clarify whether the non-causal convolution leaks information across train/test splits.
- For WARP-Phys on MSD, clearly specify the physical prior injected into the root network (the main text says only "physical constraints").
- Show visualizations of θₜ evolution over time to support the claim that the weight-space representation captures meaningful structure.

## Removed Points

These points were flagged by reviewers or automatically detected but are removed with justification:
- **"WARP does not actually perform weight-space learning as claimed"** — The paper defines its terminology clearly in Footnote 1 (citing [106] for the convention). While the framing is inflated (kept as a weakness above), the claim that the model does "not" perform any form of weight-space processing is too strong given the paper's stated definitions.
- **"Identity initialization of A is not novel"** — The paper cites [58] for this, so there is no claim of novelty for this specific initialization.
- **"Missing related works"** — Cannot confirm this without external sources. Per instructions, do not mention missing related works.
- **Formatting/typo/grammar nitpicks** — Parser artifacts, not author errors.
- **"Missing appendix content"** — Appendix is stripped by the parser; cannot penalize for this.
- **"WARP-Phys on LV marked X is unexplained"** — The paper explicitly states in Section 3.2 that "this particular evaluation protocol is incompatible with the WARP-Phys variant due to the deliberate introduction of artificial discontinuities."

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's framing and its actual mechanism, but the fundamental observations about what the model does and does not do are already present in the paper's method section (though obscured by the weight-space terminology).

## Suggestions

1. **Downplay the "weight-space learning" framing** and instead describe the model honestly: "a linear RNN whose hidden state is reshaped into the parameters of a non-linear decoder MLP." This is still interesting and novel.
2. **Investigate the PEMS08 result thoroughly.** Either provide strong evidence that the comparison is fair (exact splits, no leakage from non-causal convolution, verified against other reproductions) or remove the result and the "over 50%" claim. An extraordinary claim requires extraordinary evidence.
3. **Reposition WARP-Phys on SINE*** explicitly as a proof-of-concept for the physics-injection mechanism, not as a competitive result — since the model knows the exact functional form.
4. **Add the controlled ablation** comparing WARP against a standard linear RNN + non-linear readout at matched hidden dimension and parameter count.
5. **Be more precise in the abstract/intro about classification performance.** Note that WARP excels on shorter sequences but struggles on very long ones (>10k steps).

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human-reviewed corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `4ygElzj772.md` (Weight-space learning from hubs) | 4.0 / Reject | Similar quality level; that paper has a clearer experimental setup but narrower scope. This paper has broader experiments but more framing issues. |
| `fF72TYOKjZ.md` (Improved state mixing in LRNNs) | 4.0 / Reject | Both papers propose novel linear RNN architectures. The LRNN paper only evaluates on synthetic tasks; this paper evaluates on real-world data, which is stronger, but has more questionable results (PEMS08). |
| `ptfu9Pr3dk.md` (Symmetries in weight-space learning) | 4.0 / Reject | Solid theory paper. This paper has more empirical breadth but less theoretical rigor. Comparable overall quality. |
| `9uChwgWHX9.md` (Design principles for sequence models) | 4.0 / Reject | Theoretical framework with synthetic validation only. This paper has a genuine architectural contribution and real-world evaluation, placing it slightly above. |
| `7WLtbB0pay.md` (Don't Pay Attention) | 3.5 / Withdrawn | Novel architecture but weak empirical results. This paper has stronger empirical validation. |
| `YDl4vqQqGP.md` (MambaSL) | 6.0 / Accept Poster | Strong, rigorous empirical paper on time series classification with 30 UEA datasets. This paper has broader scope (multiple modalities) but is less rigorous on classification (6 datasets) and has questionable results. Below this anchor. |
| `l54TZ88nFD.md` (WaveletGPT) | 2.5 / Reject | Major methodological flaws including unreliable citations. This paper is clearly above this anchor. |

**Score: 4.5** — The paper proposes a genuinely novel architecture and evaluates it broadly across multiple domains. However, the framing is inflated (not weight-space learning in the established sense), one headline result (PEMS08) is extraordinary and insufficiently justified, and one key demonstration (WARP-Phys on SINE*) is essentially trivial curve-fitting. These issues collectively prevent acceptance but do not invalidate the core architectural contribution. A major revision with honest reframing and verification of the suspicious result could make the paper competitive.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>