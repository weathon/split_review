Now I have a clear picture of the paper and all the claims. Let me write the final consolidated review.

## Summary

This paper proposes a method for joint audio-video generation by integrating two frozen pre-trained diffusion models (AnimateDiff for video, AudioLDM for audio) with lightweight trainable connectors and self-attention blocks. Two mechanisms are introduced: (1) timestep adjustment to align the noise schedules across modalities, and (2) CMC-PE (Cross-Modal Conditioning as Positional Encoding), which injects cross-modal features as positional encodings rather than via cross-attention. Experiments on GreatestHits, Landscape, and VGGSound datasets evaluate video quality (FVD), audio quality (FAD), and cross-modal alignment (AV-Align, ImageBind scores).

## Strengths

1. **Timestep adjustment is clearly motivated and empirically validated.** The paper identifies a real problem — misaligned noise schedules between video and audio diffusion models — and provides concrete evidence (Figure 2's loss distributions, Table 1's AV-Align improvements from 0.256 to 0.268 and FAD from 1.29 to 0.60 with γ=1.5). The mechanism is simple and well-reasoned.

2. **CMC-PE is a clean architectural contribution with practical advantages.** On GreatestHits (Table 1), replacing cross-attention with CMC-PE improves AV-Align (0.250→0.256) and FAD (2.35→1.29). The idea of injecting cross-modal information as positional encodings rather than through attention keys/values is novel and provides a stronger inductive bias for temporal alignment.

3. **Strong quality metrics on benchmark datasets.** On VGGSound (Table 3), the proposed method achieves FVD=333 vs. TempoToken's 2473, and FAD=1.46 vs. SpecVQGAN's 5.08 and DiffFoley's 5.72. On Landscape (Table 2), FVD=1122 vs. MM-Diffusion's 1689 and FAD=6.63 vs. 16.4. These substantial improvements in generation quality are valuable.

4. **Training efficiency is a practical strength.** Keeping pre-trained U-Net parameters frozen and only training the connectors and self-attention blocks (Section 3.1) makes the method accessible and cost-effective. This aligns with the paper's stated goal of a "simple baseline."

## Weaknesses

### Fatal
None.

### Major

1. **The comparison with sequential approaches (T2A2V, T2V2A) is not a clean evaluation of joint vs. sequential generation.** The paper feeds the proposed method's audio output into TempoToken (T2A2V) and the proposed method's video output into SpecVQGAN/DiffFoley (T2V2A). This tests how well sequential models can *fix* one modality given the joint model's output, not how a text→audio→video or text→video→audio pipeline would perform starting from scratch. A fairer comparison would run, e.g., text→AudioLDM→audio→TempoToken→video and text→AnimateDiff→video→DiffFoley→audio independently. As structured, the comparison conflates the sequential models' own quality with their sensitivity to artifacts from the joint model's outputs. The paper's claim that "the proposed method achieved the best quality...except for FVD in Landscape and IB-AV in VGGSound" is too sweeping given this design issue. *(Supported by lines 268–271, which describe the pipeline feeding the joint model's outputs into sequential models.)*

### Minor

1. **Factual error about FVD improvement with CMC-PE alone.** The paper states: "Replacing cross-attention with CMC-PE improves the AV-Align score as well as FVD and FAD" (line 209). Table 1 shows the cross-attention baseline achieves FVD=379, while CMC-PE without timestep adjustment (γ=1) gives FVD=393 — *worse*, not better. The AV-Align and FAD improvements are real, but the FVD claim is factually incorrect for the direct comparison. (CMC-PE with timestep adjustment at γ=1.75 achieves FVD=374, which is better, but that reflects the combined effect of both mechanisms, not CMC-PE alone.)

2. **No ablation of the proposed mechanisms on benchmark datasets.** The ablation study (Table 1) is conducted only on the custom GreatestHits dataset. On Landscape and VGGSound, only the full method is compared against baselines, without ablating CMC-PE or timestep adjustment. Since the base models themselves (AnimateDiff+AudioLDM) are strong, it is unclear how much of the benchmark improvement comes from the mechanisms vs. the base models. An ablation on at least one benchmark would strengthen attribution.

3. **Missing architectural details for reproducibility.** The paper does not specify: (a) the connector architecture (number of layers, output dimension, which U-Net block(s) it reads from), (b) at which U-Net levels the inserted self-attention blocks operate, (c) whether they share parameters across modalities, and (d) the exact interpolation method for matching audio and video temporal dimensions (line 164 mentions "interpolated and broadcast" without specifying how). These are necessary for reproducing the method.

4. **No variance or confidence intervals reported.** FVD and FAD are known to be noisy with limited sample sizes, yet all tables report only point estimates without standard deviations or confidence intervals. The paper also does not state how many videos were generated for evaluation on each benchmark.

5. **Overclaiming in the abstract.** The abstract states the method "outperforms existing methods" (line 4). On VGGSound IB-AV (Table 3), the proposed method scores 0.155 vs. TempoToken's 0.168 and DiffFoley's 0.159 — worse on both. On Landscape IB-AV (Table 2), the score is 0.192 vs. MM-Diffusion's 0.191 — essentially tied. The introduction (line 17) uses the more careful phrasing "on par with or better than," which is more appropriate. The abstract should match this precision.

6. **The timestep adjustment hyperparameter γ is not validated across datasets.** The paper sets γ=1.5 "unless otherwise noted" based on GreatestHits results (Section 3.2.2, line 132), but does not test whether this value transfers to Landscape or VGGSound, which have very different temporal dynamics (natural scenes, diverse sound classes vs. percussion strikes). Sensitivity to γ may vary by dataset.

7. **Unsupported claim about Xing et al. (2024).** The paper states that Xing et al.'s "guidance based approach...heavily limits the capability of the model to generate temporally aligned samples" (line 77) without providing evidence or citation. This should be supported or softened.

### Trivial
- The paper uses both "timestep alignment" and "timestep adjustment" interchangeably (line 17 vs. Section 3.2 title). Consistent terminology would help.

## Nice-to-Haves
- A discussion of compute cost (training time, number of added parameters, inference speed) would contextualize the "simple baseline" claim.
- Qualitative examples from the benchmark datasets (Landscape, VGGSound) showing alignment improvements would strengthen the presentation.
- Automated search or adaptive selection of γ would address the sensitivity concern. The paper acknowledges this as future work, which is appropriate.

## Removed Points

1. **"CMC-PE improves FVD" error (from Strength Finder).** The Strength Finder incorrectly says CMC-PE "holds FVD nearly constant" (379→393 is not "nearly constant" — it is a 3.7% degradation). This strength claim is filtered because it conflicts with verified data; the underlying strength (CMC-PE improves alignment) is kept in the main review.

2. **Harsh critic's concern about AV-Align metric tuning fitting the dataset.** The paper states hyper-parameters were tuned using "annotated timestamps in the Greatest Hits dataset" (line 193). Without evidence that this used the test split, this concern is speculative. The paper explicitly follows the original train/test split (line 197), so the concern is unsubstantiated. (Removed as factually unsupported.)

3. **Harsh critic's claim that "the paper does not discuss alternative mappings" for timestep adjustment.** The paper clearly describes the mapping (Eq. 6) and provides a sensitivity analysis over γ values. The claim that no alternatives are discussed is true in the strict sense, but this is a design choice, not a flaw — proposing one simple, effective mapping is standard. (Moved to Nice-to-Haves.)

4. **"No discussion of MM-Diffusion being unconditional/class-conditional vs. text-conditional."** The paper uses class names as text conditions (line 259). MM-Diffusion's official pretrained models on Landscape are class-conditional, making the comparison reasonable. The reviewer's concern is not a material mismatch. (Removed.)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the method or results that the authors themselves did not identify.

## Suggestions

1. Correct the factual error on line 209 — CMC-PE alone (γ=1) does not improve FVD (393 vs. 379). Restate to reflect the correct pattern: CMC-PE improves AV-Align and FAD; adding timestep adjustment further improves both and brings FVD in line with or slightly below the cross-attention baseline.

2. Restructure the sequential comparison: either (a) run clean text→AudioLDM→audio→TempoToken→video and text→AnimateDiff→video→DiffFoley→audio pipelines, or (b) reframe the existing comparison as a *robustness test* rather than a head-to-head superiority claim.

3. Add an ablation on at least one benchmark dataset (e.g., Landscape) showing (i) cross-attention baseline, (ii) CMC-PE only, (iii) CMC-PE+timestep adjustment. This would directly attribute benchmark gains to the mechanisms.

4. Provide missing architectural details (connector design, insertion layers, interpolation method) in the paper or appendix to ensure reproducibility.

5. Tone down the abstract to match the introduction's more measured language ("on par with or better than").

## Score and Decision

**Overall assessment:** The paper proposes a sensible method with two well-motivated mechanisms (timestep adjustment and CMC-PE). The GreatestHits ablation convincingly shows both mechanisms improve temporal alignment. The benchmark results demonstrate strong generation quality, especially on FVD and FAD. However, the evaluation is weakened by a flawed sequential comparison that overstates the case for joint generation, an absent benchmark ablation, and a factual error in one result statement. These issues are addressable in revision and do not invalidate the core contribution, but they do reduce confidence in the paper's strongest claims as written.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>