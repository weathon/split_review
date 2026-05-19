- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
I now have a complete picture. Let me produce the consolidated review.

## Summary

This paper proposes SpikeLLM, a framework that uses spiking neural network dynamics as an alternative quantizer for large language models (7B–70B parameters). The core ideas are: (1) a Generalized Integrate-and-Fire (GIF) neuron that merges L binary spiking steps into one step with L quantization levels, balancing encoding steps and per-step bit-width; (2) an Optimal Brain Spiking framework that detects salient activation/weight channels via first/second-order Taylor expansion and allocates more spiking steps to those channels. The method is integrated into OmniQuant and GPTQ pipelines, achieving substantial perplexity and zero-shot accuracy improvements in low-bit settings (e.g., W4A4, W2A8, W2A16) and enabling fully additive linear layers via ternary spiking.

## Strengths

1. **First scaling of spiking dynamics to 70B‑parameter LLMs.** The paper demonstrates SpikeLLM on LLaMA‑2‑70B (Table 1, Table 2), achieving viable perplexity and zero-shot accuracy with a small increase in operations. This is the first demonstration of SNN-style dynamics at this parameter scale.

2. **Large, consistent improvements over OmniQuant in very low‑bit settings.** For LLaMA‑2‑7B W4A4, SpikeLLM reduces WikiText2 perplexity from 15.25→11.36 (Table 2) and raises average zero‑shot accuracy from 47.58%→50.65% (Table 1). At W2A8 and W2A16, the perplexity improvements are even more dramatic (e.g., 287.64→22.13 for W2A8 on LLaMA‑2‑7B).

3. **Fully additive linear layers via ternary spiking, outperforming PB‑LLM.** Using the ternary GIF neuron (Remark 1), SpikeLLM achieves 100% additive operations while PB‑LLM reaches only 80–95%. At a similar "equal steps" cost (~1.4), SpikeLLM averages 52.10% accuracy vs. PB‑LLM's 46.93% (Table 3, Figure 4).

4. **Empirical validation that OBS saliency selection outperforms random allocation.** Figure 3 (Mid, Right) shows that targeting channels via the proposed first/second‑order saliency consistently outperforms random channel selection at the same computational cost.

5. **Empirical justification for per‑channel (not per‑token) saliency.** Figure 2 demonstrates that first‑order gradient saliency is significant along the channel dimension but not the token dimension, supporting the per‑channel spiking design of Eq. (espike2).

6. **Compatibility with existing quantization pipelines.** The method is plugged into both OmniQuant (for weight‑activation quantization) and GPTQ (for weight‑only ternary quantization), showing it can be integrated without redesigning the training loop.

## Weaknesses

### Major

- **Activation saliency derivation in Theorem 1 is not rigorous as presented.** The proof in Eq. (s1) replaces ∂ℒ/∂(WX) with WX without justification. For the stated layerwise loss ‖WX − 𝒬(W)𝒬(X)‖²₂, the gradient would be 2(WX − 𝒬(W)𝒬(X)), not WX. The claimed activation saliency formula X ∘ W⊤WX does not follow from the stated assumptions in a mathematically sound way. This is a genuine gap in the theoretical presentation. However, the approach is empirically validated (Figure 3 demonstrates OBS saliency outperforms random), so the gap weakens the paper's theoretical foundation without invalidating the empirical results.

### Minor

- **The GIF neuron equation (Eq. espike) has a notation inconsistency.** The same index variable `t` is used both as the left-hand-side time step and as the summation index ∑_{t=1}^{L}, making the definition technically ambiguous. The intended meaning (merge L IF sub‑steps into one GIF step) is understandable from context, but the notation should be cleaned up.

- **Uncertainty about baseline reproduction.** The paper states "our primary baseline in OmniQuant and we keep the same training settings" and the Table 2 caption says "Comparisons between SpikeLLM and OmniQuant in the same pipeline." This strongly implies the authors ran OmniQuant themselves, but this could be stated more explicitly. The zero‑shot OmniQuant results in Table 1 were not reported in the original OmniQuant paper, so clarifying that they were reproduced would strengthen confidence.

- **No sensitivity analysis for the saliency threshold.** The saliency rate (0.10 for W4A4, 0.05 for W2A8) is reported without analysis of how performance varies as this hyperparameter changes. A simple sweep would improve reproducibility understanding.

- **No actual runtime or energy measurements.** The paper claims energy efficiency inspired by biological plausibility but provides only ACE (operation count) as a proxy. Real runtime/energy measurements would significantly strengthen the efficiency claims.

- **No discussion of limitations.** Potential limitations (variable-step hardware deployment difficulty, reliance on calibration data, ACE metric not accounting for all overheads) are not discussed.

### Trivial

- Several minor typos: "preplexity" → "perplexity", "Meraging" → "Merging", "Effiency" → "Efficiency", "differentation" → "differentiation", "subsect" → "subtract", "WikeText2" → "WikiText2".

## Nice-to-Haves

- A pseudo-code or algorithmic specification of the per-channel variable-step spiking forward pass would aid reproducibility.
- For the W2A8 setting where OmniQuant collapses (287.64 perplexity), a brief explanation of why the baseline fails would help contextualize the dramatic improvement.
- The "Equal Steps" operation metric used for ternary spiking comparison (Table 3) is defined non-standardly; a more standard metric or a worked example would help.

## Removed Points

These points were flagged by reviewers but are removed as they are either factually incorrect, not verifiable from the paper, or based on speculation:

- *"The ternary spike connection to GIF is not established"* — The paper explicitly states in Remark 1 that the ternary spike is a special case of GIF formed by merging positive and negative IF neurons. The connection is clearly stated.
- *"The paper does not adequately differentiate from SpikeGPT"* — The paper discusses SpikeGPT and prior work in Section 2 (Related Work), noting that language-oriented SNNs are "almost less than 1 billion parameters." The differentiation is adequate.
- *"OmniQuant comparison may not be under identical conditions"* — The paper states it uses the same pipeline and settings. While more explicit language would help, the claim that the comparison is insufficiently controlled is not supported by evidence.
- *"The IF-to-uniform-quantization equivalence is asserted without derivation"* — The paper cites prior ANN-SNN conversion works (bu2021optimal, li2021free) that established this equivalence, which is standard practice.
- *"The ACE metric is not clearly tied to the proposed method"* — The paper defines ACE as M×N and reports it for each setting. For the variable-step case, the computation (T×M×N for T-step channels) follows naturally from the definition, even if not spelled out in exhaustive detail.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the authors themselves do not make.

## Suggestions

1. **Fix the activation saliency derivation.** Either (a) provide a rigorous derivation from a specific loss, or (b) clearly state the formula as a heuristic motivated by the OBS framework and defend it empirically (which you already do in Fig. 3). This would resolve the paper's most significant rigor concern.
2. **Clean up notation in Eq. (espike)** — disambiguate the summation index from the GIF step index.
3. **Explicitly state that OmniQuant baselines were reproduced** using the authors' own code, and report whether results match the original paper.
4. **Add a brief sensitivity analysis** (e.g., a small table or plot) for the saliency rate parameter.
5. **Fix typos** throughout.
