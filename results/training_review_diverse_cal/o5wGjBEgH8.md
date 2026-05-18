Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper introduces Novel View Acoustic Parameter Estimation (NVAPE), a task that predicts spatially distributed acoustic parameters (C50, T30, DRR, EDT) across a scene from only a 2D binary floormap and a single reference RIR. The authors propose a U-Net-based model that treats the problem as image-to-image translation, construct the MRAS dataset (1000 multi-room apartment scenes, ~4M RIRs), and demonstrate results on both a new task and an existing within-scene interpolation benchmark. The work also extends to directionally-dependent (beamformed) parameter prediction.

## Strengths

1. **Well-motivated task with practical value**: NVAPE reframes the NVAS problem by targeting perceptually meaningful acoustic parameters rather than full RIRs, requiring only a 2D floormap and a single reference RIR as input (Section 3.1). This directly addresses the impracticality of needing detailed 3D meshes with material properties for on-device AR/VR applications.

2. **The MRAS dataset fills a clear gap**: The authors generate 1,000 algorithmically designed multi-room apartment scenes with varying geometries, materials, and door widths, yielding ~4 million RIRs (Section 4.2). This is a substantial resource for studying complex reverberation in coupled-room environments — a regime poorly covered by existing datasets like SoundSpaces. The dataset is publicly released.

3. **Clear results on energy-ratio parameters**: On the new NVAPE task, the model achieves strong results on C50 and DRR, outperforming all baselines by 0.5–1 dB on both Replica and MRAS (Table 1). On MRAS, C50 error is 1.87 dB vs. the best baseline at 2.23 dB. These parameters are the ones that exhibit meaningful spatial variation, which the model successfully captures.

4. **First extension to directionally-dependent prediction**: The model handles beamformed C50 for five fixed azimuth directions by incorporating a pose channel, achieving 1.94 dB error vs. 3.09 dB for the best baseline (Table 2, Ours+pose). This is a genuinely novel capability for the NVAS literature.

5. **Methodologically thoughtful preprocessing**: The masked average pooling with Gaussian filtering (Section 3.2) produces smooth, continuous heatmap labels without the hard transitions of Voronoi-based approaches. The data augmentation strategy (random rotations & translations that preserve directional information) is non-trivial and correctly implemented.

## Weaknesses

### Major

1. **The "state-of-the-art on existing tasks" claim is not adequately qualified.** Contribution (4) states the model "achieves state-of-the-art benchmarks on existing tasks," referring to the within-scene interpolation comparison (Table 3) against INRAS and NAF. The problem is that the proposed model has a fundamentally different information budget than INRAS/NAF: it receives a *reference RIR from the same scene* as input, while INRAS/NAF take only spatial coordinates and must learn scene acoustics from training data alone. The paper acknowledges this is a "different task" (line 326) but does not list the reference RIR as the crucial difference — instead it cites "frequency dependent acoustic parameters" as the key difference, which is secondary. A reader could easily conclude the model is algorithmically superior in a direct comparison, when in reality the reference RIR provides scene-specific acoustic context that the baselines lack. The Ours+split30/70 result (0.55 dB C50 vs. INRAS 0.6 dB, Table 3) is a fairer comparison point since it uses less data, and it does corroborate the trend — but the claim should be explicitly caveated that the model operates with additional acoustic conditioning not available to INRAS/NAF. This weakens the headline "state-of-the-art" framing.

### Minor

2. **Missing ablation: contribution of the reference RIR.** The model uses both a floormap *and* a reference RIR as input. There is no experiment that removes the reference RIR (the spectrogram channel and source/receiver marker maps) to isolate how much performance comes from geometric reasoning vs. acoustic conditioning. This is especially important because the "input rir" baseline (using the reference RIR as a uniform map) already achieves 3.82 dB C50 on Replica, and the full model reduces this to 1.73 dB — a real but not enormous improvement. An ablation without the reference RIR would clarify whether the U-Net is genuinely learning geometry-to-acoustics mappings or primarily extrapolating the reference RIR's characteristics with minor geometric modulation.

3. **Abstract overstates the results.** The abstract claims the method "outperforms statistical baselines significantly," while the paper body honestly reports (line 191) that "for reverberation time metrics (T30, EDT) the model is slightly worse than the best baseline." On Replica, the model's T30 error is 10.77% vs. the best baseline (scene avg map) at 5.86%; on MRAS it is 16.59% vs. 11.50% (Table 1). The model clearly excels on energy-ratio parameters (C50, DRR) but is *worse* on decay-time parameters. The abstract should reflect this mixed outcome rather than implying uniform dominance.

4. **T30/EDT errors exceed the perceptual JND.** The paper references a 10% JND for decay times (Section 5.2), yet the model's T30 errors are 10.77% on Replica and 16.59% on MRAS. The task motivation is that these parameters will condition reverberators for plausible auralization. The Limitations section (line 387) mentions that "further perceptual validation can be conducted" but does not directly address whether T30 errors above JND would produce perceptible artifacts in the rendered output. This is a gap in the argument connecting the reported metrics to the claimed application.

5. **Limited evidence of generalization to real-world data.** The MRAS dataset, while large and acoustically diverse, is generated algorithmically by connecting shoe-box rooms in line/grid patterns. The model may exploit regularities in this synthetic structure (e.g., rooms of similar shape, doors at predictable locations) that would not transfer to real apartments with irregular layouts, furnishings, and material variations. The Limitations section (line 387) acknowledges the desire to extend to measured data, but the paper does not discuss *how* the synthetic-to-real gap might affect performance or what steps could mitigate it.

### Trivial

None.

## Nice-to-Haves

- **Per-source error analysis**: The paper reports pixel-wise aggregated metrics. Showing the distribution of errors across different source positions (e.g., does the model fail for sources in small rooms or near boundaries?) would give insight into failure modes.
- **Qualitative heatmaps for the directional task**: Figure 4 shows visual results for omnidirectional parameters; a comparable figure for the beamformed case would help the reader understand what the model captures vs. misses.
- **Model efficiency reporting**: Model size, inference time, and GPU memory requirements would be useful given the stated motivation of on-device AR/VR applications.
- **Ablation without reference RIR**: As noted in Weakness (2), this would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Baselines for directional experiment may use omnidirectional data"** — Factually wrong. Table 2 lists all baselines as using "2nd-order" (i.e., beamformed) ambisonic data, matching the proposed model's input. The paper is clear on this. REMOVED.

2. **"0.077 dB error is implausibly low; model may be memorizing"** — Speculative and unsupported. The held-out receiver split (different receivers within the same scene) prevents scene-level memorization. The Ours+split30/70 result (0.55 dB) corroborates the trend with less data and still beats INRAS (0.60 dB). The real issue is comparison fairness (covered in Weakness 1), not data leakage or implausibility. REMOVED.

3. **"Paper does not discuss real-world behavior"** — The Limitations section (line 387) explicitly states: "we expect to extend this work to real-world measurement data." The paper acknowledges this; however, the underlying concern about synthetic-to-real transfer is retained in Weakness 5 with reframed scope. REMOVED as stated.

## Novel Insights

The reviewer's most incisive observation is that the SOTA claim on the within-scene interpolation task conflates *architectural superiority* with *information advantage*. INRAS/NAF and the proposed model are solving related but distinct tasks: INRAS/NAF infer RIRs from coordinates alone, while the proposed model gets scene-specific acoustic grounding from a reference RIR. This is not a flaw in the paper's method but in its framing — the same U-Net without the reference RIR would likely underperform INRAS on the interpolation task, meaning the claimed SOTA status should be attributed to the *combination* of geometry + acoustic sample rather than to the architecture itself. This distinction matters for future work that might try to build on the claimed SOTA result.

## Suggestions

1. **Qualify the SOTA claim**: In both contribution (4) and the abstract, explicitly state that the within-scene comparison operates with a different input setup (reference RIRs) than prior methods, and present the 30/70 data split result as a more directly comparable baseline.

2. **Reconcile the abstract with the results**: Replace "outperforms statistical baselines significantly" with a more precise claim such as "outperforms baselines on energy-ratio parameters (C50, DRR) and achieves competitive performance on decay-time parameters."

3. **Add the RIR-removal ablation**: Even a small-scale version would substantially strengthen the paper by isolating the contribution of geometric input.

4. **Discuss T30/JND implications**: Explicitly state whether T30 errors of 10–16% are acceptable for auralization given the JND of 10%, and under what conditions (e.g., late reverberation being less perceptually critical than early reflections).

5. **Provide at least one qualitative figure for the directional task** to support Table 2 visually.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>