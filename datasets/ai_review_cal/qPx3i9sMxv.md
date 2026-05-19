- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8
Now I have everything I need. Here is the consolidated final review.

---

## Summary

This paper tackles controllable spatial audio generation from text and images. It contributes BEWO-1M, a large-scale (1M+ samples, 2.8k hours) simulated binaural audio dataset with GPT-generated spatial captions; SpatialSonic, a diffusion-based one-stage model that uses coarse-to-fine azimuth state matrices to provide explicit spatial guidance; and new spatial evaluation metrics (FSAD, GCC MAE, CRW MAE). Experiments on the simulated test sets show that SpatialSonic substantially outperforms fine-tuned mono-generation baselines on spatial metrics.

## Strengths

- **First large-scale dataset with spatial audio captions (BEWO-1M).** At over 1M audio-text pairs and 2.8k hours, BEWO-1M is orders of magnitude larger than prior stereo audio datasets (e.g., SinIs2Spk) and is the first to pair stereo audio with explicit spatial descriptions (lines 8–10, 50–52, 124; Table 1). The semi-automated pipeline combining Pyroomacoustics/gpuRIR simulation with GPT-based attribute induction is clearly described (§3, Fig. 2).

- **Novel azimuth state matrix for precise spatial guidance.** The coarse (Gaussian-based, Eq. 4) and fine (discrete one-hot, Eq. 5) azimuth matrices encode continuous direction and movement over time based on physical principles (Eq. 3). The ablation (Tab. 8, referenced on line 275) confirms that both matrix variants significantly improve FSAD — e.g., coarse guidance reduces FSAD from 50.71 to 10.98 in T2A — directly validating the core design choice.

- **Proposed spatial evaluation metrics.** The paper introduces FSAD (Fréchet Stereo Audio Distance, replacing VGGish with StereoCRW) and two TDOA-based errors (GCC MAE, CRW MAE) to fill the gap in spatial audio evaluation (lines 249–254). These metrics capture spatial alignment that mono-channel metrics (FAD, CLAP) miss.

- **Regional-perception image encoder for spatial I2A.** The detection-model-based region embedding (§4.2) outperforms global CLIP-based encoders — Table 9 (referenced on line 275) shows regional perception improves CLAP from 14.20 to 15.31 and FSAD from 9.47 to 4.58, demonstrating the value of spatial-aware visual encoding.

- **Interactive audio generation via clicks/bboxes.** Using SAM to select RoIs, the model supports interactive control (lines 232–235). Table 7 (referenced on line 270) reports competitive results (MOS-Direction ~3.8–3.96), demonstrating controllability beyond text/image inputs.

## Weaknesses

### Fatal
None.

### Major

- **Real-world validity is asserted but not demonstrated.** The abstract and introduction claim the paper conducts "subjective and objective evaluations on simulated and real-world data" (line 14). A "real-world recorded subset" is mentioned as being manually constructed and annotated (line 52), yet **no quantitative or qualitative results on this real-world subset appear anywhere in the paper text.** All reported results (Tabs. 5, 7, 8, 9 as described in §5) are on BEWO-1M test sets, which are simulated (human-checked, but still within the simulator's distribution). This is a significant evidential gap for a paper that pitches its contributions toward VR/AR and embodied AI applications. Readers cannot assess whether the model produces spatial audio that generalizes beyond the simulator's assumptions (e.g., no head shadow, idealized RIR).

- **GPT-based azimuth extraction during inference is not evaluated.** During inference, the paper relies on GPT to extract azimuth parameters (K, μ_begin, μ_end, T) from natural language descriptions (line 152). The main experiments use ground-truth azimuth directly from simulation. The paper presents **no study of GPT's accuracy at this task** — no accuracy rate, no error analysis, no sensitivity analysis of how GPT errors propagate to generation quality. Since the controllability-from-text claim directly depends on this pipeline step being reliable, this is a critical missing validation. As presented, the paper only shows that SpatialSonic can follow an azimuth matrix *if given the correct one*.

- **No empirical comparison to cascaded/stereo-conversion baselines.** The paper motivates the one-stage design by arguing that two-stage approaches (mono generation + spatial simulator) incur "high computational costs and potential error accumulation" (line 43). However, the baseline comparisons (§5) include only fine-tuned mono models (AudioLDM2, etc.) adapted to output stereo. The most directly relevant prior work — Dagli et al. (2024)'s cascaded pipeline, or mono-to-stereo conversion methods (Zhou 2020, Parida 2022) — is discussed in §2 but **never compared empirically.** Without this comparison, the claimed advantage of the one-stage design is asserted but unsubstantiated.

### Minor

- **The "first attempt/exploration" framing is imprecise.** The paper uses "first attempt" (line 8), "first exploration" (line 45), and "first time" (line 81) to describe its contributions. While qualified with "to the best of our knowledge" and while the paper does cite related cascaded and mono-to-stereo work, these claims would be more accurate and less vulnerable to skepticism if phrased as "first end-to-end controllable spatial audio generation model" or similar. The oversweeping framing is unnecessary because the actual contributions (dataset, azimuth matrices, metrics) are strong enough to stand on their own.

- **FSAD metric not validated against human spatial perception.** FSAD replaces VGGish with StereoCRW (a network trained for spatial audio localization) as the feature extractor for Fréchet Distance (line 254). This changes what the metric measures — it may over-weight localization accuracy and under-weight audio content quality. The paper reports no correlation study between FSAD and human spatial judgments (e.g., MOS-Direction), leaving the metric's validity as a general-purpose spatial audio quality measure unestablished.

- **Confusing/redundant text in the ablation description.** Line 275 states "coarse guidance is more suitable for the T2A task, while fine guidance is necessary for the T2A task." One of these should clearly be "I2A" based on the surrounding context (which discusses coarse guidance in I2A being unstable). This typographical error makes the ablation results ambiguous and needs correction.

- **Detection model not identified.** The image encoder pre-training (§4.2) uses "a detection model along with the CLIP model" (line 163) but never names which detection model (e.g., Faster R-CNN, DETR). This is a minor reproducibility gap.

- **Subjective evaluation uses a small panel with no confidence/inter-rater metrics.** The MOS evaluation (line 255) uses 15 experts. While not unusually small for audio evaluation, no confidence intervals or inter-rater agreement metrics (e.g., Fleiss' kappa) are reported, making it hard to assess the reliability of the subjective scores.

- **Cross-attention design choice in AFM is not justified.** Eq. 4 (line 199) uses the azimuth state matrix as the *query* in cross-attention with text/image embeddings as keys/values. This is an unconventional formulation — typically conditioning signals serve as keys/values. The paper acknowledges the equation is simplified (line 208) but does not justify this design choice or clarify the full implementation with projections.

### Trivial
- Two instances of the same conference/workshop name appear differently in citations (none found — the paper's formatting is clean given parser limitations).

## Nice-to-Haves
- Evaluate the model on the real-world subset that was already constructed. Even a subset of 50–100 samples with quantitative and qualitative results would substantially strengthen the claims.
- Run a controlled study of GPT-based azimuth extraction accuracy on 50–100 natural language descriptions and report how often errors exceed perceptual thresholds (e.g., >30° offset).
- Add a cascaded baseline: a strong mono model (e.g., AudioLDM 2) followed by binaural rendering via simulated HRTF or Pyroomacoustics, and compare against SpatialSonic on the same metrics.
- Validate FSAD against human perception via a small listening test correlating FSAD scores with MOS-Direction ratings.
- Provide a diagram of how the state matrix is reshaped and concatenated with the latent in the diffusion backbone (Eq. 6).

## Removed Points
These points were removed from the main review with justification:

1. **"Missing/absent tables (e.g., Table 2)"** — The paper uses \input{tabs/...} commands; these tables exist in the original submission and were stripped by the PDF parser. The paper references and discusses them in text (line 122: "Tab. ref{tab:caption_quality} shows that our automated pipeline can generate decent captions").
2. **"Missing appendix/proofs"** — Standard parser artifact. Appendices exist in the original submission.
3. **"No head shadow effect"** — The paper explicitly states "To make the dataset general, we do not consider the shadow effect of the head and leave the head adaptation achieved by future fine-tuning" (line 119). This is a deliberate design choice, not an omission.
4. **"Missing related works"** — Per instructions, the reviewer cannot verify whether cited works exist or whether related works are missing.
5. **"Formatting/style nitpicks" and "typos/grammar"** — These are parser artifacts from PDF extraction, not author errors.
6. **Weaknesses about reproducibility of trivial details (complete training logs, etc.)** — The paper provides the main training configuration (8×RTX 4090, 500K steps, learning rate 2e-5, batch size 128; line 246).
7. **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") were dropped as they lack specific citations to the paper's content.

## Novel Insights
None beyond the paper's own contributions. The reviews surface three structural gaps (real-world validation, GPT pipeline evaluation, cascaded baseline comparison) that the paper's own framing already partially acknowledges but does not address. The most incisive observation across the reviews is that the paper's practical controllability claim has two stages — (1) text → azimuth parameters (via GPT, unvalidated), and (2) azimuth parameters → spatial audio (validated). The paper presents evidence only for the second stage, which the reviews correctly identify as a significant omission regardless of whether one finds it fatal or fixable.

## Suggestions
1. Run the model on the already-constructed real-world subset and report results — even if the model degrades, documenting where and why would strengthen the paper.
2. Add a systematic evaluation of GPT-based azimuth extraction accuracy (precision/recall at various angular tolerances) and a sensitivity analysis showing how azimuth errors propagate to generation quality.
3. Implement a simple cascade baseline: a mono generator (e.g., AudioLDM 2) followed by binaural rendering via the same simulator used for BEWO-1M, and compare on FSAD and MOS.
4. Calibrate the "first" claims to match what is actually first — "first end-to-end controllable spatial audio generation model" is more precise and still impactful.
5. Report confidence intervals for MOS scores and include a correlation analysis of FSAD against human direction judgments.
6. Fix the text on line 275 where one "T2A" should likely read "I2A."
7. Name the detection model used for regional perception in §4.2.
