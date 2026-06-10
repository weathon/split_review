## Summary

This paper proposes HART, a hypernetwork training method for generating PEFT parameters (prefixes) for language models. HART introduces two technical innovations: (1) **autoregressive layerwise parameter generation** — the decoder generates hidden states sequentially, with each state conditioned on its predecessor and mapped to a distinct layer's PEFT parameters — and (2) **local consistency regularization**, which penalizes large changes in generated hidden states across consecutive training iterations to stabilize training. Experiments on T5-Large and T5-XL across S-NI and P3 benchmarks show improvements over the authors' re-implementation of the prior HyperTuning method.

## Strengths

- **Attention analysis validates the layerwise-dependency hypothesis (Figure 1, Section 1).** The paper trains a bidirectional decoder and visualizes its attention map, demonstrating that each layer primarily attends to its immediate predecessor. This diagnostic directly motivates the autoregressive design and is absent from prior hypernetwork work (Phang et al., 2022; Ivison et al., 2022), which generates all layers' parameters from a single shared hidden state.

- **Ablation study cleanly isolates the contribution of each proposed component (Table 6, Section 5.1).** The ablation decomposes gains step by step: autoregressive generation contributes over one point on both benchmarks, and local consistency regularization adds approximately 0.5 points. This decomposition confirms that both components independently improve performance.

- **Convergence-speed evidence shows the autoregressive scheme produces better-fitted parameters (Figure 3).** The loss curves comparing autoregressive vs. non-autoregressive generation (holding all else equal) show faster convergence to a lower loss, providing mechanistic evidence beyond final test accuracy.

- **Loss-variance evidence shows consistency regularization stabilizes training (Figure 4).** The regularized training alleviates loss spikes and reduces variance, directly supporting the paper's stated motivation of addressing training instability caused by high input diversity.

- **Weight-untying enables leveraging stronger auxiliary models (Table 2, Section 4.1).** By initializing the hypernetwork with Flan-T5-Large while keeping the main model as T5-Large, HART improves by 2.8 points over the basic HART and surpasses full fine-tuning. This demonstrates a unique advantage over weight-sharing approaches like HINT.

## Weaknesses

### Fatal

None.

### Major

- **Framing mismatch between the abstract and the actual comparison (Abstract, Section 4.1).** The abstract claims that "HART notably outperforms [Phang et al., 2022] on both T5-Large and T5-XL models." However, the primary experimental comparison is against **"HyperTuning"** — the authors' own re-implementation of Phang et al.'s HyperTuning-PT **from which the hypernetwork pre-training stage has been removed** (line 178: "HyperTuning is our re-implementation of HyperTuning-PT where we remove the hypernetwork pre-training"). The paper does distinguish between these in Section 4.1, but the abstract and introduction (line 28: "HART outperforms HyperTuning (Phang et al., 2022)") present the comparison as directly against the original published method. Since the gap between HART and the stripped-down re-implementation (1.6 points on S-NI, 3.6 on P3 T5-XL) is larger than what would be expected against the full HyperTuning-PT (which includes pre-training and whose performance the paper does not report in comparable settings), this framing is misleading. The paper would be significantly stronger if it directly compared against the full HyperTuning-PT and scoped its claims accordingly.

### Minor

- **No statistical significance information (Section 4).** No error bars, confidence intervals, or multi-run variance are reported. Hypernetwork training involves stochasticity at multiple levels (task sampling, demonstration sampling, query sampling). Given that several comparisons hinge on improvements of 0.5–1.6 points, the absence of variance information makes it impossible to assess whether these differences are meaningful.

- **Key regularization hyperparameter α not specified (Section 4).** The paper states "We select α ∈ {1, 10, 20}" (line 156) but does not report which specific value was used for the main results. This is a reproducibility gap, and it also prevents readers from assessing the sensitivity of results to this choice.

- **No direct comparison against the full HyperTuning-PT (with pre-training) in the results tables.** The paper mentions HyperTuning-PT as a baseline (line 176) and discusses it in the comparison table (Table 1), but the numerical results tables compare against "HyperTuning" (without pre-training). The ablation (Table 6) shows that removing pre-training causes a substantial performance drop, and adding fusion-in-decoder recovers some of it — but the paper never reports how HART (with autoregressive generation + consistency regularization but without pre-training) compares to the original HyperTuning-PT (with pre-training but without these innovations). This omission weakens the evidence for the core claim.

### Trivial

- The term "autoregressive" is used somewhat loosely — the decoder applies the same parameters recurrently at each step (h₁ = H_dec(z), h_l = H_dec(h_{l-1})) rather than performing causally-masked multi-step transformer decoding. The paper clearly defines the mechanism, but a more precise term like "recurrent" or "sequential" would be less ambiguous. This does not affect the technical validity of the method.

## Nice-to-Haves

- **Analysis of the generated parameters themselves.** The paper argues that autoregressive generation produces more "expressive" parameters, but the only supporting evidence is lower training loss (Figure 3). Visualizing or quantitatively analyzing the structure of generated prefixes across layers would strengthen this claim.

- **Inference cost analysis.** The paper's framing emphasizes "extremely efficient task adaptation," but provides no FLOPs, latency, or memory analysis for the hypernetwork forward pass (which is itself an 8-layer Transformer for T5-XL).

- **Sensitivity analysis for α.** Reporting how results vary across the {1, 10, 20} range would improve reproducibility and understanding of the regularization's behavior.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that the comparison is "against a weakened re-implementation" with specific numeric values (0.0, -0.4, +0.7, +1.7) for HyperTuning-PT.* **Removed because:** The specific numbers for HyperTuning-PT (32.2 on S-NI T5-Large, 57.0 on P3 T5-Large, etc.) are not present in this paper — they come from an external comparison with the original Phang et al. paper. The framing issue (abstract vs. actual comparison) is retained as a Major weakness, but the critic's precise numerical cross-paper comparison is not verifiable from this paper alone.

- *Criticism that "fusion-in-decoder is a borrowed technique whose benefit is conflated with HART's own contributions."* **Removed because:** The paper transparently acknowledges the origin of fusion-in-decoder (line 154), both HART and the HyperTuning baseline include it, and the ablation (Table 6) separately controls for it. The controlled comparison is fair.

- *Criticism that the "autoregressive" mechanism is "more precisely a recurrent process" and that using the same decoder parameters limits expressiveness.* **Removed because:** The paper clearly defines the mechanism (Eq. 6-7), and the critic's speculation about limited expressiveness from recycling parameters is not supported by any evidence in the paper or the review. No experiment demonstrates this is a problem.

- *Strength about "consistent gains across model scales and benchmarks" from the Strength Finder.* **Kept with caveat** — the gains are real against the comparable baseline (HyperTuning re-impl). The qualification about which baseline is used is handled above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the primary comparison.** Compare HART directly against the full HyperTuning-PT (with pre-training) as a baseline, and report whether gains hold. If pre-training is incompatible with HART for computational reasons (as stated on line 182), then the comparison should be explicitly scoped against methods with comparable compute budgets. Adjust the abstract accordingly.

2. **Report variance.** Even 3 runs with different seeds would allow readers to assess whether the 0.5–1.6 point improvements are significant.

3. **Specify the α value** used for main results, and ideally report sensitivity across the {1, 10, 20} range.

4. **Add an analysis of generated parameter structure** (e.g., measuring diversity of prefixes across layers, comparing autoregressive vs. non-autoregressive generations) to directly support the claim that the method produces more "expressive" parameters.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>