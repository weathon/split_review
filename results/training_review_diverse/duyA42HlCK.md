Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes HyperHuman, a unified framework for controllable human image generation. The key contributions are: (1) **HumanVerse**, a large-scale dataset of 340M human images annotated with pose, depth, and surface-normal maps; (2) a **Latent Structural Diffusion Model** that jointly denoises RGB, depth, and normal in a single network with shared backbone and structural expert branches; and (3) a **Structure-Guided Refiner** that composes predicted structural maps for higher-resolution (1024×1024) synthesis. Experiments show strong quantitative results on zero-shot MS-COCO evaluation, outperforming existing general T2I models and controllable generation methods.

## Strengths

- **Novel architecture for joint RGB-depth-normal denoising.** The paper proposes a unified network that simultaneously denoises three modalities with shared backbone and structural expert branches (Sec. 3.2). Unlike ControlNet/T2I-Adapter which treat structural maps as external input conditions, HyperHuman explicitly models the joint distribution of appearance and structure. The ablation confirms that joint denoising (FID 17.18) outperforms RGB-only (21.68) and RGB+depth (19.89) variants.

- **Large-scale HumanVerse dataset with comprehensive annotations.** At 340M images with pose, depth, surface-normal, and captions, HumanVerse is an order of magnitude larger than existing human-centric datasets (e.g., SHHQ, DeepFashion). The scale and diversity are critical for training a human generation foundation model, and the dataset is a clear community contribution.

- **State-of-the-art quantitative results on zero-shot evaluation.** On the MS-COCO human subset (Tab. 1), HyperHuman achieves 17.18 FID (25.2% improvement over SD 2.0 at 22.98), 4.11 KID (48.5% improvement), and highest pose accuracy (AP 30.38, AR 37.84). These results use only the first-stage model trained on HumanVerse (a subset of public LAION-2B and COYO), making them attributable to the proposed method rather than private data or post-processing.

- **Ablation covering multiple design dimensions.** The ablation study (Tab. 2) systematically examines the number of denoising targets, expert branch layer count, noise schedule (zero-terminal SNR vs. default), prediction target (ε-pred vs. v-pred), and timestep sampling strategy. The "Different Timesteps" variant (FID 29.36) convincingly demonstrates the importance of the same-timestep strategy for joint learning.

## Weaknesses

### Fatal
None.

### Major

1. **User study is insufficiently documented and has implausible preference ratios.** The user study (Tab. "User Preference Comparisons") reports only final preference percentages (89–99%) without specifying the number of participants, number of image pairs, randomization procedure, or presentation conditions. The 99.08% preference over HumanSD is extreme and suggests either cherry-picked examples, a small sample, or a biased protocol. As reported, this study does not constitute credible evidence for visual quality claims. This is a significant weakness because visual quality is a central claim of the paper.

2. **The second-stage refiner trained on an internal (non-public) dataset complicates the interpretation of qualitative comparisons.** The paper transparently discloses (Sec. 5) that the refiner uses an "internal dataset" and that quantitative metrics come from the first-stage model only. However, the user study and qualitative comparisons use the full pipeline including this refiner, while baselines use their own default configurations without a comparable refinement stage. The refiner's contribution to visual quality cannot be separated from the joint-denoising method's contribution, making the visual quality advantage (especially the extreme user study numbers) difficult to attribute to the core technical contribution. The paper would be stronger if it either (a) used a public dataset for refiner training, or (b) applied a comparable off-the-shelf refinement to all baselines.

### Minor

3. **The first two rows of the ablation table conflate architecture changes with training target changes.** The "Denoise RGB" and "Denoise RGB + Depth" rows change both the training target (how many modalities to denoise) and the model architecture (how many expert branches). An ablation that keeps the three-branch architecture fixed and varies only the training targets (e.g., all three branches predict RGB vs. two predict RGB + one predicts depth vs. one each for RGB/depth/normal) would cleanly isolate the benefit of joint structural denoising. The current comparison cannot rule out that part of the improvement comes from increased model capacity rather than joint learning.

4. **The zero-shot evaluation is not fully controlled for training data distribution.** HyperHuman is fine-tuned on HumanVerse (a human-centric subset of LAION-2B/COYO), while baselines like SD 2.0 are trained on the full LAION-2B. A baseline that fine-tunes SD 2.0 on HumanVerse with the same architecture but without joint denoising would help isolate whether the improvement comes from the method or simply from additional human-centric training. This is a common limitation in domain-specific generation papers, but acknowledging it would strengthen the claims.

5. **Missing details on inference cost.** The expert branches add parameters and computation. Reporting FLOPs, parameter count, or inference speed relative to SD 2.0 would help readers assess the practical trade-off.

### Trivial
None that survive filtering — the paper is generally well-written and the remaining formatting artifacts are parser issues.

## Nice-to-Haves

- A controlled ablation with fixed three-branch architecture varying only training targets (all RGB, two RGB+one depth, one each) would cleanly demonstrate the benefit of joint denoising.
- The FID_CLIP metric could be briefly explained or cited for readers unfamiliar with it.
- The outpainting step for annotation improvement (Sec. 4) is interesting but unvalidated — a small-scale analysis of when/why it helps would be informative.

## Removed Points

*(These criticisms were evaluated against the paper and found to be invalid, overblown, or based on misreading. They are listed here for transparency.)*

- **Criticism that the claim "one of the earliest attempts in human generation foundation model" is overstated.** The claim is qualified ("one of the earliest"), HumanSD is already cited as prior work, and the paper does not claim to be the first. This is a defensible characterization.
- **Criticism that the ablation comparison between "Default SNR with ε-pred" and full method "conflates three changes."** The ablation is about noise schedule and prediction target — the architecture and joint denoising loss are the same. Only two factors change (zero-terminal SNR, v-prediction), and these are cleanly attributed to the noise-schedule design choices the paper discusses.
- **Criticism about missing related works.** Without external sources to verify, this cannot be included.
- **Criticism about baselines not being fairly compared in the user study because they lack a refiner.** The paper states it uses each baseline's "officially provided best configurations" for qualitative comparison. This is standard practice; the refiner is part of HyperHuman's system, just as SDXL's own refinements are part of SDXL.
- **Criticism about the SDXL FID being "anomalously high."** The paper explicitly notes this is because SDXL generates artistic style at 512×512 and was resized. This is a known limitation acknowledged by the authors.
- **Various formatting/style nitpicks and reproducibility nitpicks.** These are parser artifacts or standard practice.

## Novel Insights

The harsh critic's observation about the data distribution confound (HumanVerse being human-centric vs. baselines trained on full LAION-2B) raises a genuinely important question about whether the quantitative improvements are driven by data curation rather than the joint denoising architecture. This is a subtle but significant point that the paper does not address. Additionally, the extreme user study numbers (99.08%) paired with minimal methodological reporting is a red flag that the broader community should take seriously when evaluating human generation papers. Beyond these, the reviews do not surface insights beyond what the paper already states.

## Suggestions

1. **Document the user study thoroughly** — number of participants, number of comparisons per method, randomization protocol, and whether first-stage or full-pipeline outputs were used. If the study was small, state this and treat the results as preliminary.
2. **Replace the internal refiner dataset with a public one**, or explicitly compare baselines with a common off-the-shelf refinement (e.g., a super-resolution model) to control for the effect.
3. **Add a controlled ablation** with fixed three-branch architecture varying only the training targets (all RGB, two RGB+one depth, one each) to cleanly demonstrate joint denoising's benefit.
4. **Include inference cost analysis** (FLOPs, parameters, or speed) so readers can evaluate the practical trade-off.

## Score and Decision

The paper presents a novel architecture for controllable human generation and a large-scale dataset that represent genuine contributions. The quantitative results from the first-stage model (trained on public data) are strong and convincing. However, the evaluation has two significant gaps: (1) the user study is insufficiently documented and its extreme numbers lack credibility, and (2) the second-stage refiner's private training data makes the qualitative/visual quality claims hard to fully evaluate. Neither gap invalidates the core technical contributions or the quantitative results, but they prevent the paper from being a clean accept.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>