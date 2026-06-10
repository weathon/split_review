## Summary

This paper presents Zipformer, an efficient ASR encoder with four architectural innovations (U-Net-like aggressive downsampling with frame rates as low as 6.25 Hz, attention weight re-use via decomposed MHAW/SA/NLA modules, BiasNorm as a replacement for LayerNorm, and SwooshR/SwooshL activation functions) plus a new optimizer (ScaledAdam) that scales parameter updates by parameter RMS and explicitly learns parameter scales. Extensive experiments on LibriSpeech, Aishell-1, and WenetSpeech demonstrate that Zipformer achieves 2–3× FLOPs reductions over Conformer-L with better or competitive WER.

## Strengths

1. **Variable multi-resolution downsampling improves both efficiency and accuracy**: The U-Net structure with middle stacks operating at 6.25 Hz is more aggressive than Squeezeformer's fixed 2× downsampling. The ablation (Table 7, rows 369–370) proves this structure reduces parameters by 30% (65.6M vs 94.2M) while improving WER from 2.23/5.09 to 2.21/4.79 — a rare case where aggressive downsampling simultaneously reduces cost and improves quality.

2. **Attention weight re-use via MHAW/SA decomposition delivers large efficiency gains**: Decomposing MHSA into a single attention-weight computation (MHAW) shared by two Self-Attention modules and one Non-Linear Attention module saves ~63% FLOPs. The concrete evidence is in Table 2: Zipformer-L uses 107.7 GFLOPs vs Conformer-L's 294.2 GFLOPs (both pruned transducer) while achieving substantially better WER (2.06/4.63 vs 2.46/5.55).

3. **ScaledAdam provides substantial, principled gains**: The ablation (Table 7, row 386) shows replacing ScaledAdam with Adam degrades WER by 0.17% on test-clean and 0.72% on test-other — a very large margin from an optimizer change. The optimizer is principled: it scales updates by parameter RMS to equalize relative change across parameters of varying sizes, plus an explicit scale-learning term derived from a factored parameterization (Section 3.5).

4. **BiasNorm and Swoosh activations are validated by clean ablation evidence**: Each component is individually ablated with consistent positive signal: BiasNorm vs LayerNorm (2.29/4.97 → 2.21/4.79), SwooshL for "normally-off" modules vs SwooshR-only (2.32/5.21 → 2.21/4.79), and Swish (2.27/5.37 → 2.21/4.79).

5. **Strong multi-dataset validation**: Results on LibriSpeech (English, 1000h), Aishell-1 (Mandarin, 170h), and WenetSpeech (Mandarin, 10,000+ hours) consistently show Zipformer matching or outperforming baselines at substantially lower FLOPs, demonstrating robustness across languages and data scales.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Balancer and Whitener are mentioned but never described or ablated** (line 233). The paper states "We also employ the activation constraints including Balancer and Whitener to ensure training consistency and stability" but provides no definition, citation, or ablation. While these are not claimed as core contributions, the reader cannot assess whether they interact with the reported results. The authors should describe these techniques and ideally include them in the ablation.

2. **The ScaledAdam vs. Adam comparison is architecturally confounded** (lines 403–405). The Adam baseline requires "BiasNorm for each module" to avoid divergence, while the ScaledAdam setup does not — so the architectures differ. Notably, the confound likely favors Adam (more normalizations should help Adam if they help at all), meaning ScaledAdam's superiority is still credible; but the comparison does not cleanly isolate the optimizer's standalone effect.

3. **The NLA ablation result is partially oversimplified** (Table 7, rows 372–375). The paper states "Removing either NLA or Bypass leads to performance degradation," but No NLA improves test-clean (2.16 vs 2.21) while degrading test-other (4.97 vs 4.79). This mixed signal should be acknowledged.

4. **No variance or error bars reported**. All WER results are single-seed point estimates. Many ablation differences are 0.05–0.17%, which may be within run-to-run noise. While standard in ASR, the granular claims about each component's contribution would benefit from multiple seeds.

5. **"First to approach Conformer" claim is slightly overstated**. The standard Zipformer-L (50 epochs, 4 V100) achieves 2.06/4.63 vs original Conformer-L's 2.1/4.3 — test-clean surpasses but test-other lags. The stronger 2.00/4.38 result uses 8× A100s for 170 epochs, substantially more compute than the standard setup. The paper marks this with an asterisk, but the headline claim (line 25) blends the two without caveat.

### Trivial
None.

## Nice-to-Haves
- The paper could discuss limitations of the 6.25 Hz frame rate (~160 ms per frame) for tasks requiring fine-grained temporal resolution beyond ASR.
- Sensitivity to Eden schedule hyperparameters (α_base, α_start, t_warmup) could be discussed.
- FLOPs measurement details (encoder-only vs full model) could be clarified.

## Removed Points
These points were flagged by reviewers but removed after verification against the paper:

- **"No code release mentioned"** (harsh critic): Removed per instructions — do not question release status of cited references.
- **"Missing related works"** : Removed per instructions — cannot verify without external sources.
- **"Optimizer derivation h_t approximation needs more justification"** (harsh critic): Removed — the paper explicitly states the approximation and its justification ("since Adam is nearly invariant to changes in the gradient scale"). The reviewer's concern is speculative, not based on an error in the paper.
- **"Fatal methodological flaw" framing of Balancer/Whitener**: Demoted from the critic's implied fatal placement to Minor. These are mentioned as stability techniques, not claimed contributions; the main ablation studies focus on and validate the proposed innovations. This is an incompleteness of description, not a fatal flaw.
- **Generic/superficial strengths from Strength Finder** (e.g., "addressed an important problem"): Removed per instructions.
- **"Missing appendix/proofs"**: Removed per instructions — parser strips these; they exist in the original submission.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the need for transparency about Balancer/Whitener and the confound in the optimizer ablation, but these are standard methodological critiques rather than novel observations.

## Suggestions
1. Describe and ablate Balancer and Whitener — readers need to know what they are and whether they affect the core comparisons.
2. Run a controlled optimizer ablation: either train ScaledAdam with extra BiasNorm layers to match the Adam setup, or attempt Adam with the reduced-normalization configuration (with gradient clipping if needed) to verify divergence.
3. Acknowledge the mixed NLA signal (test-clean improvement vs test-other degradation) and discuss whether noise or a genuine trade-off.
4. Add multiple seeds for ablation experiments to establish whether small differences (e.g., 0.05–0.11% on test-clean) are systematic.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>