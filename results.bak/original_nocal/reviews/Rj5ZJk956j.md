Now I have a thorough understanding of the paper's content. Let me construct the consolidated final review.

---

## Summary

This paper introduces a weight-based method for analyzing gated neurons (SwiGLU/GeGLU) in transformers: computing cosine similarities between a neuron's input, gate, and output weight vectors to characterize its read-write (RW) functionality. Applying this method across 9–12 LLMs, the authors discover a class of "weakening" neurons (cos(w_in, w_out) ≈ -1) that are few in number but activate frequently and have outsized influence on model behavior. A conditional ablation method further suggests that some of this influence stems from activations where the gate value is negative — challenging the common view that negative Swish values only aid training dynamics.

## Strengths

1. **Simple, scalable, cross-model method.** The weight-cosine-similarity analysis requires no activation data and can be applied to any gated model. Figure 1(a) convincingly shows that the median cos(w_in, w_out) transitions from positive (strengthening) in early layers to negative (weakening) in later layers across nine LLMs of diverse families and sizes (2B–9B). This is the first demonstration of this consistent temporal shift for gated neurons and is the paper's strongest empirical finding.

2. **Discovery of a small neuron class with disproportionate influence.** Figure 3(a) shows that zero-ablating only 243 weakening neurons in OLMo-7B measurably reduces attribute rate from layer ~10 onward, whereas ablating the same number of random neurons from the same layers has no effect. This causal evidence that a tiny class of neurons has outsized influence on factual recall is genuinely surprising and worth investigating further.

3. **Conditional ablation identifies a novel mechanism involving negative gate values.** Figure 3(b) shows that the entropy-sharpening effect of weakening neurons is largely recapitulated by the subset of activations where x_gate < 0 and x_in < 0 (case iii). The paper is among the first to demonstrate that negative SwiGLU gate values encode functionally important behavior, and it explicitly acknowledges concurrent work (Kong et al., 2025).

4. **Activation-frequency analysis strengthens the case.** Figure 4 shows a strong negative correlation (r = -0.97, p < 0.01) between activation frequency and cos(w_in, w_out) for OLMo-7B layer 15. This extends prior findings from GELU models (Gurnee et al., 2024) to gated architectures and quantitatively supports the claim that weakening neurons activate far more often than strengthening ones.

5. **Novel taxonomy for gated neurons.** Table 1 defines six prototypical RW functionalities based on weight cosine thresholds. This provides a reusable framework that goes beyond prior work analyzing neurons only by activation contexts (Voita et al., 2024) or output weights (Gurnee et al., 2024).

## Weaknesses

### Fatal
None.

### Major

1. **The most striking finding — functional importance of negative gate values — rests on a single model with no statistical rigor.** The conditional ablation experiment (Section 6.2) is performed only on OLMo-7B. The results are presented as raw histograms (Figure 3b) with no confidence intervals, no significance tests, and no quantification of variance. The text states "≈10 nats" decrease in entropy, but the histograms span -10 to 10 and the visual asymmetry is modest. Without error bars or replication on at least one additional model (e.g., Llama-3.2-3B), the reader cannot assess whether this effect is robust or an artifact of this specific model/dataset. The paper acknowledges the single-model limitation for ablations ("to save resources") but does not caveat it as a limitation of the negative-gate claim.

2. **No evidence that negative-gate importance is specific to weakening neurons.** The conditional ablation is only applied to weakening neurons. If other RW classes (strengthening, conditional strengthening) also show comparable entropy effects from negative-gate activations, the claim that this is a weakening-neuron-specific mechanism or a "newly discovered read-write functionality" is unsupported. The paper does not perform this control experiment, leaving the specificity of the finding unestablished.

### Minor

3. **Category distributions supporting "universality" are only shown for one model in the main text.** Figure 1(a) convincingly shows the median cos(w_in, w_out) trend across 9 models. However, the finer-grained category-by-layer distribution (Figure 1b) is shown for Llama-3.2-3B only, with a reference to Section J ("see section J for other models") for other models. Since the "universality" claim about where specific RW classes appear depends on these category distributions, their absence from the main text weakens the claim. A single bar chart for a second model in the main text would substantially strengthen the paper.

4. **The "weakening" label is defined by weight geometry but functional behavior depends on activation signs.** A neuron classified as "weakening" by weight cosines (cos(w_in, w_out) ≈ -1) can functionally *strengthen* when x_gate < 0 and x_in < 0 (as the paper itself discovers in Section 6.2). The paper acknowledges this and explains it, but the taxonomy's naming creates an internal tension: the "weakening" class is defined statically from weights, yet the paper's headline discovery is that these neurons sometimes *strengthen* via negative gate values. This could be clarified by more precise framing (e.g., "weight-weakening" vs. "function-weakening").

5. **No sensitivity analysis for the cosine threshold (τ = ±0.5).** The choice of 0.5 as the threshold for classifying neurons into prototypical RW classes is acknowledged but never varied. Different thresholds could produce different category distributions (Figure 1b), and the robustness of the downstream findings (ablation effects, activation frequencies) to this choice is unknown.

6. **Activation-frequency correlations across all layers, and quantitative summary of conditional ablation, are reported as text only.** The paper states correlations are "at least -0.71 in all layers except the last two" but provides no table or figure showing this across all layers (only Figure 4 for layer 15). Similarly, the conditional ablation results could benefit from a bar-chart summary with effect sizes rather than only histograms.

### Trivial

None.

## Nice-to-Haves

- Extend the conditional ablation experiment to at least one additional model (e.g., Llama-3.2-3B) to demonstrate generality.
- Add a control experiment: apply the same conditional ablation to strengthening/conditional strengthening neurons to test whether negative-gate effects are specific to weakening neurons.
- Provide a table of effect sizes with bootstrap confidence intervals for the conditional ablation conditions.
- Vary the cosine threshold (τ = 0.3, 0.5, 0.7) and report stability of category distributions and ablation results.

## Removed Points

- **"First to observe negative gate mechanism is overstated due to Kong et al."** — Removed because the paper explicitly states "concurrently with Kong et al. (2025) who focus on a different phenomenon." The claim is appropriately qualified.
- **"Ablation lacks control: no comparison against other RW classes"** — Removed because the paper states in the Figure 3 caption that results for other classes are shown in appendix figures 14–16 and are "indistinguishable from the clean line." This does exist in the paper (though in the appendix).
- **"Missing related works"** — Removed per instructions (cannot verify from external sources).
- **"Presentational issues"** (typos, figure caption clarity, etc.) — Removed per instructions as parser artifacts.
- **Various speculative concerns** (e.g., "the entropy effects in Figure 3(b) are visually small") — Removed as subjective interpretation without specific anchor to an error in the paper.

## Novel Insights

The reviews do not surface any genuinely novel observation beyond the paper's own contributions. The harsh critic's observation that the taxonomy's "weakening" label is at odds with the paper's own finding about negative-gate strengthening is a valid framing tension, but it is essentially pointing out a limitation the paper partially acknowledges rather than a new insight.

## Suggestions

1. **Run the conditional ablation on a second model.** Even if resources are limited, replicating the experiment on a smaller model (e.g., OLMo-1B or Llama-3.2-3B) would dramatically strengthen the negative-gate claim.
2. **Add a control conditional ablation for strengthening neurons.** This would establish that the negative-gate mechanism is specific to weakening neurons, not a general property of gated activations.
3. **Replace or supplement the entropy histograms with a bar chart** showing mean entropy change per condition with bootstrapped 95% confidence intervals for both weakening and random baselines.
4. **Show category distributions for at least one additional model in the main text** (moving from appendix to main) to support the universality claim beyond median trends.
5. **Re-frame the taxonomy** to clarify that the "weakening" label refers to a weight-geometric property (the direction of w_out relative to w_in) and that the actual functional effect depends on activation signs — reducing the tension between the taxonomy and the negative-gate findings.
6. **Add a brief sensitivity analysis** showing that the category distribution and ablation results are qualitatively stable across different cosine thresholds.

## Score and Decision

This paper makes a genuine contribution: a simple, activation-free method for analyzing gated neurons that yields a striking cross-model pattern (strengthening-to-weakening transition across layers) and discovers a small neuron class with outsized influence. The weaknesses are real but not fatal — the main concerns are the single-model basis for the headline negative-gate claim and the absence of a control conditional ablation for other RW classes. These are addressable with additional experiments. The core methodological contribution and the cross-model median trend (Figure 1a) are solid.

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**