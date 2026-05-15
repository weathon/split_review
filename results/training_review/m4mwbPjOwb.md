Now I have all the information needed. Let me compose the consolidated review.

## Summary

The paper proposes Simple-TTS, a latent diffusion model for text-to-speech that operates in the latent space of a pre-trained EnCodec autoencoder, conditioned on byte-level ByT5 representations. It adapts the U-ViT image diffusion architecture to 1D audio sequences via a U-Audio Transformer (U-AT) and modifies the noise schedule to improve text-speech alignment. The system requires no phonemizers, forced aligners, or separate duration/pitch predictors—unlike prior diffusion TTS models. It achieves a WER of 2.4% (text-only) and 3.4% (speaker-prompted), outperforming VITS variants, YourTTS, and the closed-source Vall-E on intelligibility.

## Strengths

- **First end-to-end diffusion TTS without external alignment components**: The paper demonstrates that latent diffusion with byte-level conditioning eliminates the need for phonemizers, forced aligners, duration predictors, and pitch predictors required by prior diffusion TTS systems (NaturalSpeech2, VoiceBox). Table 1 clearly contrasts the system complexity. This is a genuine architectural simplification.

- **Strong intelligibility competitive with or exceeding closed-source systems on comparable data**: Simple-TTS (44.5k hours) achieves 3.4% WER vs. Vall-E's 5.9% WER (trained on ~60k hours of LibriLight), i.e., *with less training data*. This is the cleanest comparison in the paper and provides meaningful evidence that the simplified approach does not sacrifice quality.

- **Character-aware byte-level conditioning is demonstrated to be critical**: The ablation (Table 4) shows that replacing ByT5-Large with T5-Large increases WER by 4.4×. While confounded by model size (1.2B vs. 770M parameters), the magnitude of the gap strongly suggests that byte-level representations contribute to phonetic precision—a practically useful finding for TTS system design.

- **Clean, reproducible design using publicly available components**: The system uses public EnCodec, public ByT5, and a single 243M-parameter diffusion model trained on public MLS data. The commitment to open-source strengthens reproducibility and practical impact.

- **Statistically significant subjective improvements over the strongest open-source baseline**: The human study (Table 3) shows +0.52 QMOS and +1.46 SMOS over YourTTS with non-overlapping confidence intervals, confirming that objective gains translate to perceptible quality.

## Weaknesses

### Fatal
None.

### Major

- **Data-scale confound undermines text-only comparisons with VITS baselines**: The paper's text-only WER comparisons pit Simple-TTS (trained on 44,500 hours of MLS) against VITS-LJ (~24 hours of LJ Speech) and VITS-VCTK (~44 hours of VCTK). This is a ~1000× difference in training data. The claim that "simplicity drives performance" cannot be validated from these comparisons—the results are equally (or more) plausibly explained by data volume. The paper does not acknowledge this as a limitation or attempt any data-matched control. This weakens the central narrative of the paper.

- **The T5 vs. ByT5 ablation confounds architecture with model capacity**: ByT5-Large (~1.2B parameters) and T5-Large (~770M parameters) differ by ~56% in parameter count. The paper attributes the 4.4× WER gap entirely to "character-awareness," but capacity differences alone could produce a large gap. An ablation controlling for model size (e.g., ByT5-Base vs. T5-Base) would be needed to isolate the effect of byte-level vs. subword tokenization.

- **Human evaluation is limited to a single, data-mismatched baseline**: The subjective study compares Simple-TTS only to YourTTS (trained on ~600 hours). This is confounded by the same data-scale issue (~74× more data for Simple-TTS). While the paper correctly notes that Vall-E and VoiceBox are closed-source, a controlled comparison against a VITS model trained on MLS (even a subset) would have addressed the confound and strengthened the subjective claims.

### Minor

- **Ablation studies are trained for only 50k steps (¼ of the final model's 200k steps)**: While the relative comparisons between ablation conditions are valid, the paper does not verify that the ablation conclusions hold at convergence. It is possible that the T5-conditioned model catches up with more training, or that the noise schedule matters less at convergence. Reporting final-model ablations or showing learning curves would strengthen the conclusions.

- **No analysis of why the noise schedule modification improves alignment**: The paper attributes the improvement to Balaji et al. (2022)'s observation about text-conditioned diffusion at high noise levels, but provides no analysis (e.g., cross-attention visualization, guidance utilization across timesteps) that the model actually relies more on conditioning under the s=0.5 schedule. The ablation shows the *what* but not the *why*.

- **No diversity analysis despite claiming diverse durations**: The paper states that Simple-TTS generates diverse durations (vs. NaturalSpeech2's deterministic duration model) but provides no quantitative diversity metrics (e.g., duration variance, number of distinct realizations per text).

- **Speaker similarity scores reported without variance**: Table 2 reports cosine similarity of 0.514 (Simple-TTS) vs. 0.337 (YourTTS) without confidence intervals or variance, making it impossible to assess the reliability of the difference.

### Trivial
None.

## Nice-to-Haves

- Train a data-matched VITS or YourTTS on a subset of MLS (e.g., 5k hours) and compare under equal data conditions. This would directly address the primary confound. *(Beyond what is standard for a conference paper but would substantially strengthen the claims.)*

- Ablate the U-AT architecture (e.g., replace U-Net encoder-decoder with a standard transformer using stride-based downsampling) to isolate the benefit of the U-Net design.

- Ablate EnCodec latent vs. mel-spectrogram or raw waveform inputs to justify the latent diffusion choice.

- Report performance on shorter (<4s) and longer (>10s) utterances, since many TTS applications require these regimes.

## Removed Points

These points are flagged for removal—treat them with caution.

- **"Simple-TTS has a slight data advantage over Vall-E (44.5k vs 60k)"** — REMOVED (factually incorrect). Simple-TTS uses 44.5k hours of MLS data; Vall-E uses ~60k hours of LibriLight. 44.5k < 60k, so Simple-TTS has *less* data than Vall-E yet achieves better WER (3.4% vs. 5.9%). This actually *supports* the paper's claims. The critic reversed the inequality.

- **"End-to-end claim is loose"** — REMOVED (misunderstands paper's definition). The paper defines "end-to-end" in context: "without the need for phonemizers, forced aligners, or complex multi-stage pipelines" (Abstract) and visualizes the system boundaries in Table 1. Using pre-trained components (EnCodec, ByT5) is standard practice and does not violate the stated definition.

- **Criticism that ablation studies "undermine the claimed contributions"** — WEAKENED to minor. The ablations are consistently trained for 50k steps, making relative comparisons valid. The critic's framing that they "undermine" rather than "insufficiently probe" the claims is overstatement.

- **"No ablations of U-AT architecture, EnCodec vs. mel, or classifier-free guidance"** — MOVED to Nice-to-Haves. The paper does ablate noise schedule, text encoder, and guidance (Figure 3). Additional ablations would strengthen but are not missing core experiments.

- **"Filtering test set to 4–10 seconds could bias results"** — REMOVED. The paper follows the exact evaluation protocol of prior work (Borsos et al., 2023; Wang et al., 2023; Le et al., 2023), enabling direct comparison. This is standard practice, not a bias.

- **"VITS is not a 'complex model that relies on explicit alignment components'"** — PARTIALLY RELEVANT but kept as part of the data-scale confound discussion. The paper's narrative about "complex models with alignment components" is aimed at NaturalSpeech2/VoiceBox (Table 1), while the WER comparison includes VITS. The mapping is somewhat loose but not a fatal flaw.

- **Various missing-experiment requests (data-matched baseline, U-AT ablation, EnCodec vs. mel ablation)** — MOVED to Nice-to-Haves. These go beyond what is standard for a conference paper.

## Novel Insights

The most informative tension emerging from the combined reviews is that the paper's *strongest evidence* and *weakest evidence* occupy opposite sides of the same comparison. The paper's most compelling result—outperforming Vall-E with less data (44.5k vs. 60k hours)—is also the most data-matched comparison, yet the paper burying this under comparisons with VITS variants trained on three orders of magnitude less data. The Vall-E comparison directly supports the simplicity claim: a diffusion model without alignment components beats an autoregressive model with a multi-stage pipeline, using less data. The VITS/YourTTS comparisons, by contrast, are dominated by data scale. A revision that pivots to emphasize the Vall-E comparison and honestly caveats the VITS comparisons would be substantially more persuasive.

## Suggestions

1. **Acknowledge the data-scale confound explicitly.** The paper should add a limitations paragraph noting that the text-only WER comparison with VITS is confounded by data volume and that the strongest evidence for the simplicity claim comes from the speaker-prompted Vall-E comparison (where Simple-TTS uses ~25% *less* data).

2. **Control for model size in the ByT5 vs. T5 ablation.** Compare ByT5-Base vs. T5-Base (similar parameter counts) in addition to the Large variants, or at least acknowledge the capacity confound.

3. **Add diversity metrics for duration.** Provide variance or entropy measures for generated durations to support the claim of non-deterministic generation.

4. **Include confidence intervals for automated speaker similarity scores** in Table 2, consistent with standard reporting practice.

## Score and Decision

This paper makes a real contribution: demonstrating that a latent diffusion model with byte-level conditioning can produce intelligible speech without the external alignment components required by prior diffusion TTS systems. The Vall-E comparison (with less data, better WER) is genuinely impressive. However, the paper oversells its evidence by comparing text-only WER against VITS baselines trained on ~1000× less data without acknowledging the confound. The ablation studies are informative but shallow in key respects. The paper is clearly above the acceptance threshold but would benefit from more measured claims and deeper analysis.

**Overall**: Originality 7/10, Importance 7/10, Claims Support 5/10, Soundness 6/10, Clarity 7/10, Value to Community 7/10.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>