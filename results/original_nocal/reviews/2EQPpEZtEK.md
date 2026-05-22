## Summary

DiSTAR proposes a zero-shot text-to-speech framework that couples an autoregressive language model drafter with a masked diffusion refiner, operating entirely within a discrete RVQ code space. The approach factorizes generation into patch-level units: a causal AR LM produces a compact hidden sketch for the next patch, then a discrete masked diffusion Transformer completes the patch in parallel. This design avoids continuous latent representations (addressing fragilities of prior work like DiTAR) while providing patch-level parallelism, inference-time RVQ layer pruning, and elimination of duration predictors. The paper reports competitive WER, speaker similarity, and UTMOS on LibriSpeech and Seed-TTS benchmarks.

## Strengths

1. **Novel architecture for discrete-space patch-level speech generation.** The paper cleanly formalizes (Section 3.1) a coupling of AR drafting with masked diffusion in RVQ code space, using a patchified view (Eq. 1, Figure 1) that jointly models time and depth dependencies. This is a genuine architectural contribution that extends ideas from DiTAR and LLaDA into a fully discrete setting while retaining blockwise parallelism.

2. **Strong empirical results on WER.** Table 1 shows DiSTAR-medium (0.3B) achieves 1.66 % WER on LibriSpeech test-clean and 1.32 % on Seed-TTS test-en — the lowest among all compared systems, including the larger DiTAR (0.6B) and even the human reference on Seed-TTS (1.47 %). These results demonstrate genuinely robust synthesis.

3. **Inference-time flexibility without retraining.** Stochastic layer truncation during training (Section 3.4) enables pruning of upper RVQ layers at test time, trading compute/bitrate for quality. Figure 2 verifies that retaining only 6 of 9 layers maintains low WER while speaker similarity degrades gracefully. This is a practical contribution for deployment scenarios with varying latency budgets.

4. **Parameter efficiency.** DiSTAR-medium (0.3B) and DiSTAR-base (0.15B) outperform or match several larger baselines (DiTAR at 0.6B, IndexTTS at 0.5B), suggesting the discrete-space design is parameter-efficient.

5. **Effective decoding heuristics.** The paper identifies and addresses a "tail-first" bias in the non-autoregressive decoder using layer-wise and position-wise temperature shaping plus a hybrid sample/greedy schedule (Section 3.4). Table 3 shows these heuristics improve WER from 2.11 % (unshaped sampling) to 1.91 % (shaped greedy).

6. **Elimination of duration predictor and forced alignment.** The fully discrete setting with [EOS] tokens removes the need for auxiliary duration predictors or stop heads (Section 3.1.2), simplifying the pipeline relative to continuous-flow systems.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguous baseline comparability weakens the SOTA claim.** The paper states "All models are trained on Emilia" (Section 4.1), but DiTAR results are explicitly marked as coming from the original paper (Table 1 caption: ♦ denotes scores reported in DiTAR paper), meaning DiTAR was not retrained on the same data. For other baselines (E2TTS, IndexTTS), it is not stated whether they were retrained on Emilia or numbers are taken from their original papers. This ambiguity means the claimed "state-of-the-art" status is not fully controlled for training data. The paper should (a) clarify exactly which baselines were retrained on Emilia and (b) ideally retrain DiTAR on the same data for a fair comparison, since DiTAR is the most directly comparable continuous-patch counterpart.

2. **Core architectural contribution is not ablated.** The paper claims the hybrid AR+drafted masked diffusion design is beneficial, yet provides no ablation comparing against either component alone — e.g., a pure AR model that predicts all RVQ layers within a patch autoregressively, or a pure masked diffusion model without the AR drafter. The only ablation (Table 3) compares decoding strategies (greedy vs. sampling), which tests inference heuristics, not the core architecture. Without such ablations, there is no direct evidence that the coupling of AR and diffusion outperforms simpler alternatives. This is the most significant evidential gap.

3. **Loss function in Equation 2 is non-standard and unsubstantiated.** The masked diffusion loss uses a \(1/t\) weighting factor. This is unlike standard masked diffusion formulations (D3PM/Austin et al. 2021; LLaDA/Nie et al. 2025), which use uniform weighting or schedule-dependent weights derived from a valid ELBO. The paper claims the weight "recovers an upper bound on the sequence negative log-likelihood" but provides no derivation or citation for this specific form. As \(t \to 0\), the weight diverges, giving large importance to nearly clean inputs where few tokens are masked. The derivation may reside in the (stripped) appendix, but in the main text the loss appears ad-hoc. The authors should provide a clear justification — or correct the equation.

### Minor

1. **Subjective evaluation methodology is under-described.** Table 2 reports SMOS and CMOS with confidence intervals, but the paper gives no details on the number of listeners, how test samples were selected, whether listeners were native English speakers, or whether they were screened for hearing ability. These details are standard for subjective listening tests.

2. **Ablation study lacks statistical significance testing.** Table 3 reports small WER differences (e.g., 1.91 vs. 1.99 vs. 2.11) without any confidence intervals or significance tests. The differences may be within variance, and the paper does not show they are reliable.

3. **Non-monotonic WER behavior in RVQ layer pruning is unexplained.** Figure 2 shows WER slightly increasing at 8 RVQ layers (2.04 %) compared to 6 layers (1.88 %) and 9 layers (1.98 %). The paper offers no explanation for this non-monotonic pattern, which is unusual if higher layers encode only "acoustic detail."

4. **The rationale for averaging only the last \(S\) tokens in the aggregator (Section 3.2) is not analyzed.** The paper states that overlapping patches use pooling over the last \(S\) tokens of each patch, but does not explain why this choice is preferred over pooling all \(P\) tokens or using a different aggregation strategy.

### Trivial
- The paper uses "aggregator" to describe a component that both aggregates and encodes — the naming could be more precise.

## Nice-to-Haves
- An empirical comparison between the discrete masked diffusion component and a continuous diffusion variant (analogous to DiTAR) on the same data and architecture would directly substantiate the claim that discrete space is advantageous.
- A scaling study (log-log loss vs. compute) would strengthen the contribution by showing whether the approach benefits from increased capacity beyond the two sizes tested.
- Visualizing the mask evolution over decoding steps (showing which positions are resolved early vs. late) would provide intuition for the "tail-first" bias and how temperature shaping corrects it.

## Removed Points

These points from the reviewers were evaluated and removed with justification:

1. **"Unfair comparison — IndexTTS, E2TTS, F5TTS not retrained on Emilia"** — The paper states "All models are trained on Emilia" (Section 4.1). F5TTS's original paper used Emilia, making the comparison fair. Only DiTAR is explicitly flagged (♦) as using original-paper scores. The remaining ambiguity about E2TTS and IndexTTS is retained as the Major weakness above, but the sweeping claim that "every improvement could be due to data scale" is removed as overstated.

2. **"Patchified view notation is confusing"** — The notation \(\mathbf{C}^{(k)}\) and \(\dot{\mathbf{C}}^{(k)}\) (Section 3.1.1) is clearly defined with explicit indexing. The left-padded extension is a standard boundary-handling technique.

3. **"Training details missing from main text"** — The paper provides key details (cut cross entropy, fused Adam, RMSNorm, RoPE via Liger kernels) and states "Further details are provided in the Appendix B.1." The appendix is stripped in this review format; the main text contains adequate implementation summary.

4. **"Stochastic layer truncation might be too aggressive"** — Dropping top layers uniformly from \(\{0,\dots,L-1\}\) is the intended design: the model must learn to handle truncated inputs. This is not a flaw but the mechanism itself.

5. **"UTMOS can be unreliable"** — This is a generic concern about any predicted MOS metric, not specific to this paper. It applies equally to every TTS paper using UTMOS.

6. **"Continuous latents fragility claim lacks empirical evidence"** — The paper's critique of continuous approaches is a literature-motivated motivation, not an empirical claim requiring proof in this paper.

7. **"Missing related works"** — I cannot verify missing citations without external sources.

8. Various typo/formatting nitpicks — these are parser artifacts, not author errors.

## Novel Insights

Both reviews converge on the central tension: the paper's architecture is novel and principled (AR drafting + discrete masked diffusion in RVQ space is a natural combination of ideas from DiTAR and LLaDA), but the empirical validation has a notable gap — the core design choice is not directly ablated, and the baseline comparison is not fully controlled. The loss function's \(1/t\) weighting is flagged as unusual by the harsh critic, but this is a matter the authors can address in rebuttal; the paper's empirical success suggests either the derivation is correct (in the appendix) or the practical impact of the weighting is minor. The most distinctive strength — inference-time RVQ layer pruning — is well-supported and practical.

## Suggestions

1. **Clarify baseline comparability.** Explicitly state which baselines were retrained on Emilia and which use published numbers. If DiTAR was not retrained, acknowledge this limitation and, ideally, retrain it on the same data for a controlled comparison.

2. **Add ablations of the core architecture.** The most important missing experiment is a comparison between (a) the full DiSTAR and (b) a variant without masked diffusion (completing patches purely through AR at the token level) and (c) a variant without the AR drafter (using only masked diffusion with conditioning on raw history). Even a simplified comparison would substantially strengthen the evidence for the hybrid design.

3. **Justify or revise the \(1/t\) weighting in Eq. 2.** Provide a brief derivation showing how this weight arises from a variational bound, or adopt the standard uniform weighting used in LLaDA. If the derivation is in the appendix, reference it clearly.

4. **Add subjective evaluation methodology details** (number of listeners, screening criteria, sample selection protocol).

## Score and Decision

**Rationale:** The paper presents a well-motivated architecture with genuine novelty (coupling AR drafting with discrete masked diffusion in RVQ space, enabling patch-level parallelism while remaining fully discrete). The empirical results are strong, especially on WER where DiSTAR achieves the lowest error rates across two benchmarks. The inference-time controllability via RVQ layer pruning is a practical contribution. However, the paper has three significant weaknesses: (1) the baseline comparison is not fully controlled — DiTAR's scores are taken from a different training setup and it is unclear which other baselines were retrained, weakening the SOTA claim; (2) the core architectural contribution (AR + diffusion coupling) is not ablated against either component alone, leaving a gap in the evidence for the design choice; (3) the loss function uses a non-standard \(1/t\) weighting with no justification provided in the main text. These issues are addressable in rebuttal and revision but prevent unconditional acceptance in the current form. The paper's contributions are real, and the problems are not fatal — they are about clarity and completeness of evidence rather than fundamental invalidity.

**MY FINAL SCORE:** <score>6.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>