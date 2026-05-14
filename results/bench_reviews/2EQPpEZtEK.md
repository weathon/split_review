Now I have all the calibration material I need. Let me write the consolidated review.

## Summary

DISTAR proposes a zero-shot text-to-speech framework that operates entirely in the discrete RVQ code space, coupling an autoregressive language model (for drafting patch-level tokens) with a masked diffusion transformer (for intra-patch parallel infilling). The approach builds on the patch-wise factorization of DiTAR but replaces continuous diffusion with discrete masked diffusion (inspired by LLaDA), and is evaluated on LibriSpeech-PC and Seed-TTS benchmarks against strong baselines including DiTAR, F5TTS, E2TTS, and IndexTTS.

## Strengths

- **Strongest WER among compared systems.** DISTAR-medium achieves 1.66% WER on LibriSpeech test-clean (beating the human baseline of 1.80%) and 1.32% on Seed-TTS test-en — the best reported among all baselines in Table 1, including F5TTS (2.02%), DiTAR (2.39%), and IndexTTS (2.57%). These WER improvements are substantial in absolute terms (0.73% absolute / ~30% relative over DiTAR) and are not "tiny" as one reviewer claimed.

- **Practical engineering contributions that work.** The RVQ-specific decoding heuristics (layer-wise temperature shaping, position-wise temperature shaping, hybrid sampling) are well-motivated by the observed "tail-first bias" and Table 3 shows they yield measurable gains: greedy decoding with temperature shaping achieves 1.91% WER vs 2.11% for uniform sampling. The embedding transplantation trick for initializing from codebook vectors is a useful practical idea for stabilizing training.

- **Inference-time RVQ layer pruning without retraining.** Enabled by stochastic layer truncation during training, DISTAR supports variable bitrate and controllable compute at test time. Figure 2 demonstrates a monotonic quality improvement as more RVQ layers are retained, with WER stabilizing around 6 layers while SIM continues to improve — a genuinely useful capability for deployment under latency/bandwidth constraints.

- **Strong results under purely greedy decoding.** DISTAR achieves competitive WER (1.91%) under fully deterministic greedy decoding (Table 3), demonstrating inherent robustness that reduces sensitivity to sampling hyperparameters. This is a practical advantage over systems that require careful stochastic sampling for acceptable quality.

- **Scaling behavior is consistent and well-documented.** DISTAR-medium (0.3B) improves over DISTAR-base (0.15B) on all metrics and both benchmarks, validating that the architecture scales positively with model capacity. The patch-size ablation (Table 6) provides clear design guidance: P=4 achieves best WER (1.85%) and UTMOS (4.33), while P=2 suffers from insufficient context (4.50% WER).

## Weaknesses

### Major

- **NFE mismatch undermines the primary WER comparison with DiTAR.** DiTAR is reported at NFE=10 (taken from the original paper) while DISTAR uses NFE=24. E2TTS and F5TTS are evaluated at NFE=32. If DiTAR were run at NFE=24 or 32 (its architecture supports variable NFE), its WER would likely improve substantially, narrowing the reported gap. The paper does not provide DiTAR results at matched compute, nor does it justify why 10 NFE is the "correct" setting for DiTAR while 24 is appropriate for DISTAR. This is the single most significant weakness because the paper's central quantitative claim (WER superiority over DiTAR) rests on an apples-to-oranges comparison.

- **DiTAR is conspicuously absent from the subjective evaluation (Table 2).** The paper's core framing is that DISTAR improves over the "continuous next-patch diffusion" paradigm of DiTAR, yet DiTAR is not included in the human listening tests. The SMOS (3.31 ± 0.25) and CMOS (0.22 ± 0.13) are compared against FireRedTTS, CosyVoice 2, E2TTS, and F5TTS — none of which use the same patch-wise architecture. Without DiTAR in subjective evaluation, the paper's claim of subjective superiority over its most directly comparable baseline is unsubstantiated.

- **"State-of-the-art speaker similarity" claim is directly contradicted by the paper's own data.** In Table 1, E2TTS achieves higher SIM on both LibriSpeech (0.70 vs 0.67) and Seed-TTS (0.71 vs 0.66). The Abstract states DISTAR surpasses "state-of-the-art zero-shot TTS systems in robustness, naturalness, and speaker/style consistency." The SIM data does not support this. The UTMOS claim is also debatable: IndexTTS achieves 4.35 vs DISTAR-base 4.29 on LibriSpeech, and DiTAR (4.15) beats DISTAR-base (3.93) on Seed-TTS. The paper should distinguish between metrics where it truly leads (WER, subjective SMOS) and those where it is competitive but not best (SIM, UTMOS).

### Minor

- **The paper never ablates the core architectural claim: the benefit of coupling AR with masked diffusion.** DISTAR combines an AR LM (for patch-level drafting) with a masked diffusion model (for intra-patch infilling). The paper claims this "tight coupling" is superior to either component alone, but it never trains a pure-AR variant (no diffusion, AR predicts all intra-patch tokens) or a pure masked-diffusion variant (no AR, condition directly on text + history codes) with matched data and compute. Without this ablation, we cannot attribute the results to the AR-diffusion coupling rather than to the high-quality codec, training data scale, or hyperparameter choices. The decoding strategy ablations (Table 3) and patch-size ablations (Table 6) do not address this.

- **Decoding heuristics lack individual ablation and sensitivity analysis.** The paper introduces three decoding tricks (layer-wise temperature, position-wise temperature, hybrid sampling) to address "tail-first bias." Table 3 shows their combined effect but does not ablate each trick individually. The hyperparameters (T_layer=0.8, T_time=0.95, 50/50 split) appear hand-tuned with no sensitivity analysis. A per-trick ablation would clarify which component drives improvement, and a sensitivity analysis would show how robust the method is to parameter choices.

- **The "tail-first bias" is described but not analyzed.** Section 3.4 gives a plausible intuition for why the bias occurs ("later positions are easier, leading to overconfidence") but provides no quantitative evidence — no plot of per-position confidence across decoding iterations, no comparison of mask patterns under different schedules. A simple visualization would strengthen the motivation for the proposed heuristics.

### Trivial

- The paper's technical novelty is incremental — DISTAR combines DiTAR's patch factorization with LLaDA's discrete masked diffusion, using a MAGICODEC-based RVQ codec. The individual components are established, and the contribution lies in their specific combination and the engineering to make it work. This is not a fatal flaw but should be reflected in how the contribution is framed.

## Nice-to-Haves

- Running DiTAR at NFE=24 or 32 and including it in Table 1 (matched compute comparison) would resolve the most significant evaluation concern.
- Adding DiTAR to the subjective evaluation (Table 2) would substantiate the central claim of superiority over continuous next-patch diffusion.
- A controlled ablation removing the AR module (pure masked diffusion + text conditioning) and removing the diffusion module (pure AR with same codec) would validate whether the coupling is necessary.
- Reporting statistical significance for the subjective metrics (SMOS/CMOS differences) would strengthen the evaluation.
- Individual ablation of the three decoding tricks would clarify their relative contributions.

## Removed Points

These points from the source reviews are flagged for removal; treat them with caution:

1. **Parameter count ambiguity** (Harsh Critic #1 second bullet): The paper clearly separates the codec (0.3B, Section 3.5.1) from the generative model (0.15B/0.3B, Table 1). This is standard practice in TTS. The table header "#Params" refers to the generative model parameters, consistent with how baselines report theirs. The ambiguity claim is unfounded.

2. **WER improvements are "tiny"** (Harsh Critic #1 third bullet): 0.73% absolute and ~30% relative WER improvement over DiTAR is substantial, not tiny. DISTAR-medium also beats human WER (1.66% vs 1.80%). This criticism is factually incorrect.

3. **Training loss is not novel** (Harsh Critic #4 second bullet): The paper does not claim novelty for the masked diffusion objective. It explicitly cites MaskGIT (Chang et al., 2022) for the cosine schedule and LLaDA (Nie et al., 2025) for the formulation. This is a strawman.

4. **English-only despite multilingual framing** (Harsh Critic Section-by-Section notes): The Limitations section (Appendix A) explicitly states "we trained our model solely on a around-50k-hour English corpus." The paper is transparent about this. References to multilingual systems appear in the context of related work, not as a claim about DISTAR.

5. **Figure 2 RVQ layer axis ambiguity** (Harsh Critic Section-by-Section notes): The x-axis is labeled "RVQ Layers" ranging 2-9, which clearly means retaining layers 1 through ℓ. The finding about upper layers encoding acoustic detail is a well-known result, but reporting it is not a weakness of the paper.

6. **Core innovation is "straightforward combination"** (Harsh Critic #4): While the novelty is incremental, this framing is overly dismissive. Many accepted papers at top venues make contributions through effective combinations of existing ideas. The engineering to make the combination work at scale (64 A100s, 0.6M steps, Cut Cross-Entropy, Liger kernels) and the specific design choices (aggregator design, embedding initialization, stochastic layer truncation) are non-trivial.

7. Several generic strengths from the Strength Finder were generic/did not survive comparison with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run DiTAR at matched NFE (24 or 32)** and replace the cited DiTAR scores with your own measurements. This is the single most impactful thing the authors can do to make the WER comparison fair and convincing. The gap may narrow but DISTAR's WER advantage (1.66% vs ~2.0-2.4%) is large enough that it could still hold.

2. **Include DiTAR in subjective evaluation.** Without this, the paper's central narrative — that discrete-space AR+diffusion coupling beats continuous-space counterparts — lacks perceptual validation.

3. **Tone down the SOTA claims for speaker similarity.** The SIM numbers are clear: E2TTS outperforms DISTAR on both benchmarks. Reframe the contribution as "competitive or best on WER and subjective similarity, with strong performance on other metrics" rather than claiming across-the-board SOTA.

4. **Add an ablation of the AR module and the diffusion module.** Even a small-scale experiment on a subset of the data would help validate the core design choice. The field has strong pure-AR (VALL-E 2) and pure-diffusion (MaskGCT) baselines; a direct comparison under the same codec and data would be informative.

5. **Provide individual ablations of the three decoding tricks** and sensitivity analysis for T_layer and T_time to demonstrate robustness and clarify which trick matters most.

## Score and Decision

### Calibration Anchors

| Path | Avg Human Score | Comparison to This Paper |
|------|----------------|--------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/e3XLWHFrnr.md` | 4.40 (Accept Poster) | Similar hybrid AR+NAR architecture for speech. Had missing SOTA comparisons and no human eval — DISTAR has stronger evaluation but similar overclaim issues. Roughly comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/h5KLpGoqzC.md` | 5.20 (Accept Poster) | Stronger novelty (differentiable FSQ bottleneck), end-to-end, more careful claims. DISTAR has better WER but less novelty and overclaims. Slightly weaker paper. |
| `/home/wg25r/review_agent/human_reviews_2026/FaGDopTTTC.md` | 2.50 (Withdrawn) | Weak baselines, evaluation issues, implausible claims. DISTAR is substantially stronger in experimental rigor and results. |
| `/home/wg25r/review_agent/human_reviews_2026/im2a2MHoke.md` | 2.50 (Reject) | Cherry-picked test sets, unreliable comparisons. DISTAR is much more rigorous. |
| `/home/wg25r/review_agent/human_reviews_2026/zjaV5zmlkl.md` | 5.50 (Accept Poster) | Different task (speech-to-speech). Stronger novelty and more comprehensive evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/juM14y0caI.md` | 6.00 (Accept Poster) | Different domain (VQ codebook training). Strong theory + experiments. Not directly comparable. |

### Decision Rationale

This paper presents a well-engineered zero-shot TTS system with genuinely strong WER results (1.66%, beating human at 1.80%) and useful practical contributions (decoding heuristics, RVQ pruning). However, the evaluation has significant gaps: the NFE mismatch with DiTAR makes the primary quantitative comparison unfair; DiTAR is missing from the subjective evaluation; and the "state-of-the-art speaker similarity" claim is factually wrong given the paper's own SIM numbers. The core architectural novelty (AR+diffusion coupling) is not validated by ablation. These issues are addressable but real. The paper's contributions are solid enough to warrant acceptance conditionally, with the understanding that the claims must be revised and the missing comparisons addressed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>