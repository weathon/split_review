## Summary
The paper introduces TAAE, a predominantly transformer-based neural speech autoencoder scaled to ~950M parameters, paired with a modified Finite Scalar Quantization (FSQ) bottleneck that supports a novel post-hoc residual decomposition (using the L = 2ⁿ+1 level construction). On LibriSpeech test-clean, TAAE achieves SOTA across objective metrics at 400 and 700 bps and dominates a MUSHRA subjective test, approaching ground-truth quality.

## Strengths
- **Novel post-hoc residual FSQ (§3.2.1, Eq. 3–4).** Training a single FSQ bottleneck with L = 2ⁿ+1 levels and then decomposing it at inference into an RVQ-like hierarchy (via the Minkowski-sum / scale-halving construction) is genuinely new and useful for downstream generative modeling that prefers hierarchical tokens.
- **Practical hybrid quantizer-emulation recipe (§3.2).** Bernoulli-mixing of straight-through estimation, uniform-noise emulation, and unmodified latents, plus random selection over level counts, is a clean and reusable training trick that supports both discrete and continuous (no-quant) operating points.
- **Substantive architectural engineering at scale.** The combination of ViT-style patching, sliding-window self-attention with RoPE, QK-norm, LayerScale, and a large LN ε is concretely described (§3.1, §4.2), and the within-family scaling study (App. A.2) supports that the architecture benefits from increased parameter count up to 1B.
- **Strong empirical results.** Tab. 2 shows TAAE at 400/700 bps beating all baselines on SI-SDR, Mel, STFT, PESQ, STOI, and MOSNet at comparable or lower bitrates; Fig. 2 shows MUSHRA scores near ground truth at 700–800 bps, well above Mimi/SemantiCodec/SpeechTokenizer.
- **Useful continuous-latent operating point.** The "no quant." row in Tab. 2 makes the bottleneck directly usable for latent-diffusion settings.

## Weaknesses

### Fatal
None.

### Major
- **The "scaling transformers" thesis is not isolated by the experiments (§4.5, §4.6).** The headline comparison in Tab. 2/Fig. 2 confounds architecture (transformer vs. convolutional), parameter count (~950M vs. baselines roughly an order of magnitude smaller), quantization scheme (FSQ vs. RVQ), training data, and sample rate. The within-family ablation in App. A.2 shows that TAAE scales, but does not show that the *transformer* (vs. a same-scale convolutional codec) or FSQ (vs. same-architecture RVQ) is the driver of SOTA. A matched-scale convolutional or matched-architecture RVQ baseline is the single most important missing experiment, and its absence weakens the central scientific claim.
- **FSQ vs. RVQ is asserted but never directly ablated at matched scale and bitrate.** §1 and §3.2 motivate FSQ as solving RVQ codebook-utilization and hierarchical-stream issues, but the paper does not run TAAE-with-RVQ at the same parameter count and bitrate. The single-token vs. residual FSQ rows in Tab. 2 are nearly identical (PESQ 2.96 vs. 3.09), which weakens any claim that the residual decomposition is empirically important — though it is still useful as an inference-time option.
- **MUSHRA protocol deviations limit the strength of the subjective claim (§4.3).** The paper explicitly states the test follows "the MUSHRA format without hidden anchor." Removing the low-quality anchor is a real protocol deviation (MUSHRA's calibration depends on it), so scores cannot be directly compared with other MUSHRA results in the literature. Combined with 24 self-selected online listeners from public forums, no reported screening, and no confidence intervals, the "significant margin" claim in §4.5 is less robust than presented. The paper does cite precedent (Zhang et al. 2023b; Défossez et al. 2022) for this variant, but a CI / per-utterance distribution would substantially strengthen the result.

### Minor
- **Sample-rate mismatch in evaluation (§4.4).** Encodec and Mimi (24 kHz native) are evaluated by upsampling to 24 kHz, reconstructing, and downsampling back to 16 kHz. This resampling chain can bias SI-SDR/STFT/PESQ/STOI in ways unrelated to coding quality. A matched-sample-rate evaluation, or at least a control quantifying the cost of the resampling chain, would help.
- **In-distribution test set (§4.1, §5).** Train and test are both English clean audiobooks (LibriLight + MLS English / LibriSpeech test-clean). Limitations §5 acknowledges that the model is likely to struggle on out-of-domain speech, but no out-of-domain (noisy, spontaneous, overlapping) evaluation is reported, while several baselines were trained on broader corpora. App. A.5 shows generalization to other languages, which partly mitigates this.
- **Discriminator changes deferred to appendix.** Three "major changes" to the discriminator (§3.3) are introduced and shown to drive perceptual gains via feature-matching loss (Eq. 7), but no main-text ablation isolates their individual contributions — App. B.5 is referenced but the contribution relative to a standard Encodec discriminator is not quantified in the main results.
- **Quantification of out-of-range residual-FSQ latents is missing.** §3.2.1 notes that "rare combinations" produce latents outside the trained range, handled by clipping; the empirical frequency and the reconstruction cost of clipping are not measured.
- **Mimi comparison (§4.4) is non-causal vs. streaming.** Mimi is a streaming/causal codec; the main-table TAAE is non-causal. The causal-TAAE comparison is deferred to App. A.4. This is partly justified by the paper's stated scope (generative modeling rather than streaming) but is worth flagging.

### Trivial
- The framing of 105k hours of English audiobook speech as a "modest amount" (§5) is rhetorically inconsistent — this is a sizable corpus by codec standards.

## Nice-to-Haves
- A same-architecture RVQ baseline at matched parameter count and bitrate, and a same-parameter convolutional codec baseline, both on the same test set.
- MUSHRA re-run with a hidden anchor, listener screening, confidence intervals, and per-utterance distributions.
- Out-of-domain evaluation (noisy / spontaneous / multi-speaker) and a matched-sample-rate protocol to remove the up/downsample chain for 24 kHz baselines.
- Quantitative measurement of how often the post-hoc residual FSQ exceeds its trained range, and the reconstruction degradation incurred by clipping.
- Move the discriminator ablation (App. B.5) into the main paper.

## Removed Points
These points are flagged as removed; treat them with caution.
- "Framing 105k hours as a limitation while baselines used different data is rhetorical." — Already covered as a minor framing nit; not a methodological flaw.
- Harsh critic implied unfair-comparison concerns where the asymmetry actually disadvantages TAAE (e.g., domain match favors TAAE but parameter count vs. smaller baselines is asymmetric in TAAE's favor — yet the paper is upfront in Tab. 12 and the scope statement in §4.4 about size and data differences). The blanket "evaluation systematically favors TAAE" framing is partially true but partly addressed by the paper's transparency.
- Strength Finder's "generalisation to unseen languages and lengths" was kept implicitly through App. A.5/A.6 references; it is real but secondary and not central to the paper's claims, so not separately highlighted.
- Generic "important problem" type strength — dropped as superficial.

## Novel Insights
None beyond the paper's own contributions. The most insight-bearing contribution is the post-hoc residual FSQ decomposition tied to the L = 2ⁿ+1 level construction, which is the paper's own.

## Suggestions
- Add a same-architecture, matched-parameter RVQ-bottleneck TAAE row to Tab. 2 to isolate the FSQ contribution.
- Add a matched-scale convolutional baseline (e.g., scaled-up DAC) at ~1B parameters to support the "scaling transformer" claim, or soften the claim to "a 1B-parameter transformer codec with FSQ achieves SOTA."
- Re-run MUSHRA with a hidden anchor, screening, and CIs; include per-utterance score distributions and significance tests for the "significant margin" claim.
- Evaluate on at least one out-of-domain corpus (e.g., spontaneous / noisy speech) and report a control for the 24 kHz baseline up/downsample chain.
- Promote the discriminator ablation (App. B.5) and a clipping-frequency analysis for post-hoc residual FSQ to the main text.

## Axis Evaluation
- **Originality**: Above-average — the post-hoc residual FSQ construction and the recipe for a predominantly transformer codec at 1B parameters are concrete novel contributions.
- **Importance**: High — low-bitrate speech tokenization is a load-bearing component for current speech LMs.
- **Claim support**: Mixed — the "SOTA at 400/700 bps" claim is well supported by both objective and subjective evidence; the "scaling transformers is what produces SOTA" framing is partly supported (within-family scaling) but not isolated against confounds (architecture, FSQ, data, sample rate).
- **Soundness of experiments**: Reasonable but with real protocol gaps (MUSHRA without anchor, no CIs, in-distribution test set, resampling chain for 24 kHz baselines, missing matched-scale ablations).
- **Clarity**: Generally clear; methodology and architecture are described with enough detail to reproduce.
- **Value to the community**: High — code/model release, the FSQ residual trick, and the continuous-latent operating point are directly useful for downstream generative speech work.

## Score and Decision
Calibration anchors used:
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/uxDFlPGRLX.md — FlowDec (avg 7.0, Accept): another low-bitrate full-band codec with strong empirical results. TAAE is comparable in empirical strength but has more confound concerns in its central scaling claim.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/868masI331.md — HALL-E (avg 6.4, Accept): hierarchical codec LM with novel bottleneck restructuring; similar in spirit (bottleneck construction + scale).
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ofzeypWosV.md — CLaM-TTS (avg 6.4, Accept): probabilistic RVQ; comparable empirical/methodological positioning.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/LfDUzzQa3g.md — RepCodec (avg 5.5, Reject): borderline; TAAE has stronger empirical headline result than this.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/C53xlgEqVh.md — Vec-Tok (avg 5.2, Reject): weaker borderline; TAAE clearly above.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/UFwefiypla.md — DM-Codec (avg 3.0, Reject): low anchor; TAAE far above this.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/nhgTmx1TZJ.md — UniAudio (avg 3.0, Reject): low anchor for codec/audio generation paper with weak ablations.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/JFPaD7lpBD.md — Jamba (avg 6.25, Accept): high anchor for "strong empirical SOTA + reviewers flag confounded scaling comparisons"; the confounded-claim concern in TAAE has not historically prevented similar papers from being accepted around 6.0–6.5.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/9WD9KwssyT.md — Zipformer (avg 7.5, Accept): considered but TAAE has weaker ablation rigor than Zipformer.

TAAE has strong empirical results (clear SOTA on both objective and subjective metrics), a genuinely novel technical contribution (post-hoc residual FSQ), an open code/model release, and well-described engineering — placing it in the FlowDec / HALL-E / CLaM-TTS range. The main detractor — that the "scaling transformer" framing is not isolated from FSQ/data/scale confounds, and that the MUSHRA protocol has real deviations — pulls it slightly below FlowDec but above the borderline-reject anchors.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>