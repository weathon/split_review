Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper introduces Activation Transport (AcT), a framework for steering activations in generative models using affine optimal transport maps. The method provides a unifying theoretical perspective showing that prior activation-steering methods (ActAdd, CAA, ITI, etc.) are special cases of linear transport that only shift the mean, while AcT also scales activations to preserve target distributions. The authors propose a simple linear estimator (Linear) with a strength parameter λ ∈ [0,1] and demonstrate consistent effectiveness at λ=1 across five tasks (toxicity mitigation, concept induction, truthfulness augmentation, style control, concept negation) on LLMs (Gemma-2B, Llama-8B) and T2I models (SDXL, FLUX), outperforming or matching baselines with minimal inference overhead.

## Strengths

- **Unifying theoretical framing under optimal transport**: The paper demonstrates that ActAdd, CAA, ITI, MassMean, and other activation-steering methods are all special cases of linear transport maps (Table 1, §2.3). This provides a principled explanation for why mean-shift methods fail to preserve activation distributions when source and target variances differ (Figure 2, §2.1), and clearly situates the proposed Linear estimator as the natural generalization.

- **Consistent optimal λ=1 across all tasks and modalities**: Across toxicity mitigation (Table 2), concept induction (Figure 4), truthfulness (Table 3), style control (Figure 5a), and concept negation (Figure 5b), Linear achieves its best performance at λ=1 (full transport) without per-task tuning. No baseline method achieves such consistency—ITI requires λ=8 for toxicity, λ≈5 for concept induction, and λ=2 for SDXL style control. This empirical regularity directly validates the optimal transport theory.

- **Strong quantitative results**: On Gemma-2B toxicity mitigation, Linear achieves 7.5× toxicity reduction (4.17% → 0.56% CLS toxicity) with +0.81 PPL increase, outperforming Aura (2.0×) and ITI (5.6×). On Llama-8B truthfulness, Linear improves TruthfulQA MC1 by +7.76% while decreasing MMLU by only –0.57%, substantially better than ITI (+4.65% MC1, –0.64% MMLU). These gains are achieved at λ=1 without per-task tuning.

- **Modality-agnostic transfer without architectural modification**: The same Linear estimator applied to LLM activations and diffusion model UNet/transformer activations achieves state-of-the-art results in style control (~95% style presence at λ=1 on SDXL) and concept negation, without per-modality adaptation (§5). This is, to the authors' knowledge, the first inference-time intervention method shown to work simultaneously on both modalities.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The "without any hyperparameter tuning" claim is slightly overstated.** The paper states (line 93) that Linear "without any hyperparameter tuning, matches or outperforms existing \ii{}" on LLM tasks. While λ=1 indeed requires no tuning, the method still involves selecting which layers to intervene upon (Post-LN vs. Attention vs. All-LN across experiments), and this selection varies by model (e.g., Gemma-2B toxicity uses Post-LN; Llama-8B toxicity uses Attention). The paper does provide a general finding that "LN layers were the most suited" (line 327), and all baselines also undergo layer selection, which levels the playing field. However, the phrasing could mislead readers into thinking absolutely no decisions are needed. The paper should either calibrate the claim to specify "without tuning the strength parameter λ" or provide a principled, data-driven criterion for layer selection that a new user could follow without empirical search.

2. **Computational cost of the causal estimation procedure is not reported.** The sequential estimation (§2.2) requires one forward pass per layer with interventions applied, meaning L passes through the model over n sentence pairs. While the paper correctly notes no overhead at *inference* time (maps compose with existing linear layers), the *estimation* cost (wall-clock time, FLOPs) for learning maps on the largest models (Gemma-2B, Llama-8B, FLUX) is not reported. This is relevant for practitioners deciding whether to use the method. Additionally, the comparison with the simultaneous (non-causal) estimation variant is deferred to the appendix, leaving readers unable to verify whether the extra cost of causal estimation is justified from the main paper alone.

3. **The truthfulness evaluation uses an asymmetric matched-utility criterion.** The paper selects λ for each baseline such that MMLU stays within ±0.1 of Linear's MMLU before comparing MC1 accuracy (Table 3 caption). This is defensible as a "matched-utility" comparison that controls for general capability degradation, but it does not reflect the natural operating point of each method. The paper could more clearly explain that this comparison shows "at comparable general capability cost, which method achieves higher truthfulness" rather than leaving readers to infer that Linear's reported MC1 advantage is its advantage at its own natural λ.

### Trivial

- The "off-the-shelf" terminology for the T2I experiments (lines 94, 379) could be read as implying no design choices at all, when in fact the method requires selecting source/target datasets, pooling operators, and transport support. The paper does specify these choices in context, but the phrasing is slightly loose.

## Nice-to-Haves

- Report activation histograms from actual tasks (toxic vs. non-toxic, concept vs. generic) to directly visualize the distribution-preservation argument, rather than the current toy example (Figure 2) and standard deviation plot (Figure 3).
- Present the causal vs. simultaneous estimation comparison in the main paper, as it directly validates a key methodological design choice.
- Show the pooling operator ablation (mean vs. max vs. last-token) in the main paper rather than the appendix.
- Add error bars or repeat-run variance to T2I CLIPScore plots for rigor.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **ITI adaptation criticism (Harsh Critic's Critical Issue 3)**: The reviewer claims the ITI adaptation for T2I is unfair because "the authors do not test the original ITI formulation." However, the original ITI is designed for LLM attention heads and cannot be directly applied to T2I UNet/transformer architectures. The paper's adaptation (same spatial mean pooling as AcT, applied per-position) is transparent, reasonable, and treats both methods equally. The claim that "ITI may perform better with a different adaptation" is speculative and unverifiable. The paper's characterization of ITI "failing" at concept negation is supported by the data (ITI's CLIPScore drops into the semantic-loss region). **Removed as factually unsupported.**

- **"Off-the-shelf" terminology concern (Other Observations)**: The reviewer claims the term "off-the-shelf" is misleading. The paper uses it to mean "the same method without per-modality modification," which is accurate given the paper's explicit description of the method's components. **Removed as overly pedantic.**

- **First work claim verification request**: The paper uses the phrase "to the best of our knowledge," which is appropriately cautious. **Removed as not a genuine weakness.**

## Novel Insights

The reviewer's most insightful observation is that the causal sequential estimation procedure, while methodologically justified, creates a dependency structure where later-layer maps are optimized to correct distortions introduced by earlier maps on specific in-sample activations. This raises a legitimate question about out-of-sample generalization that the paper does not fully address. The simultaneous vs. causal comparison (deferred to appendix) is precisely the right experiment to resolve this concern. Additionally, the point about the matched-utility comparison in the truthfulness experiments is well-taken: the paper's evaluation protocol is fair, but its framing could better distinguish between "best operating point" comparisons and "matched-utility" comparisons.

## Suggestions

1. Calibrate the "without any hyperparameter tuning" claim to specify "without tuning the strength parameter λ" and add a brief discussion of how layer types can be selected (e.g., using the heuristic that LN layers work best across tasks, or providing a small validation procedure).
2. Report wall-clock estimation time for the causal procedure on the largest models tested, and include the causal vs. simultaneous comparison in the main paper.
3. Clarify the truthfulness evaluation as a matched-utility comparison in the main text, not just the table caption.
4. Add variance bars or multi-seed results to the T2I CLIPScore plots for improved rigor.

## Score and Decision

This is a strong paper with a clear theoretical contribution (unifying prior work under optimal transport), a simple and effective method, and extensive experiments across two modalities and five tasks. The weaknesses are minor and addressable—primarily presentation calibration and missing analysis of estimation cost. The core claims are well-supported.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>