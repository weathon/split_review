Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper presents HyperHuman, a framework for hyper-realistic controllable human image generation. It makes three contributions: (1) **HumanVerse**, a 340M-image human-centric dataset with dense annotations (pose, depth, surface-normal); (2) a **Latent Structural Diffusion Model** that simultaneously denoises RGB, depth, and surface-normal via a shared backbone with replicated expert branches; and (3) a **Structure-Guided Refiner** that composes predicted structural conditions for high-resolution (1024×1024) synthesis with robust conditioning dropout. Experiments show strong quantitative results on MS-COCO 2014 validation human subset (FID 17.18, KID 4.11, pose accuracy metrics all exceeding prior methods).

## Strengths

- **Joint denoising of RGB, depth, and surface-normal in a unified network (Section 3.2, Fig. 2):** The paper proposes a principled architecture where expert branches (conv\_in, first DownBlock, last UpBlock, conv\_out) are replicated per modality while the backbone is shared, enforcing spatial alignment between appearance and structure. This addresses a genuine limitation of prior plug-in approaches (ControlNet, T2I-Adapter) that suffer from feature discrepancy between main and auxiliary branches.

- **HumanVerse dataset (Section 4):** At 340M images with dense structural annotations (pose via ViTPose-H, depth/surface-normal via Omnidata, outpainting for holistic structure), this is orders of magnitude larger than existing human-centric datasets (DeepFashion, SHHQ). The curation pipeline is thorough and well-documented, including human detection from LAION-2B and COYO with aesthetic and resolution filtering.

- **Improved noise schedule for structural maps (Section 3.2, Table 2):** The paper identifies that monotonous depth/normal maps leak low-frequency signals during training and addresses this with zero-terminal SNR and v-prediction. The ablation shows that different timesteps for different modalities degrade FID from 17.18 to 29.36, validating the same-timestep sampling strategy.

- **Ablation study that isolates key design choices (Table 2):** The ablation systematically evaluates the contribution of joint denoising targets (RGB only → 21.68 FID, RGB+Depth → 19.89, full → 17.18), the number of replicated expert layers, and the noise schedule. Critically, all ablated variants are trained on the same HumanVerse data, providing internal evidence that adding structural targets improves performance independent of the data advantage over baselines.

- **Structure-Guided Refiner with random conditioning dropout (Section 3.3):** The refiner composes multiple predicted conditions (depth, normal, skeleton, text) and applies random dropout during training to mitigate error accumulation from the two-stage pipeline — a practical design choice for robustness.

## Weaknesses

### Fatal
None.

### Major

- **Comparison with baselines conflates method advantage with data advantage.** The controllable baselines (ControlNet, T2I-Adapter, HumanSD) are used from their released checkpoints, trained on general LAION-2B or smaller subsets, while HyperHuman is trained on HumanVerse — a curated 340M-image human-specific dataset with rich structural annotations. The reported FID gap (17.18 vs. 23.54 for T2I-Adapter) could partly reflect the benefit of training on a cleaner, more specialized human dataset rather than the architectural contribution alone. This does **not** undermine the paper's core claim that joint denoising helps — the ablation in Table 2 controls for data and still shows meaningful gains from adding structural targets (RGB only: 21.68 → full: 17.18). However, the **headline SOTA claims** in Table 1 are weakened by this confound because the comparison is not controlled for training data.

### Minor

- **User study lacks essential methodological details (Table 3).** The paper reports preference ratios (89.24% over SD 2.1, 60.45% over SDXL, etc.) but provides no information about the number of participants, number of image pairs evaluated per comparison, whether the study was blind or randomized, what instructions users received, or any statistical significance measures. This limits the credibility of the claimed user preference as supporting evidence. The preference numbers themselves are reported, but without methodology the reader cannot assess their reliability.

- **No variance or confidence intervals reported for any metric.** FID, KID, CLIP, and pose accuracy are each reported as single numbers. Given that FID can be sensitive to sample size and random seeds, bootstrap estimates or multiple-run statistics would increase confidence in the numerical comparisons. While single-run evaluation is common practice in large-scale T2I evaluation, reporting uncertainty would strengthen the paper.

- **No computational cost comparison.** The paper does not compare parameters, training compute, or inference speed against baselines. Since the model has replicated expert branches (though only a few layers are replicated), it would be useful to know whether the quality gains come at substantially higher computational cost, or whether the joint denoising approach is efficient.

### Trivial

- The "normal only (without depth)" ablation variant is missing from Table 2. Adding depth alone improves FID from 21.68 to 19.89, and adding depth+normal further improves to 17.18. A depth-only vs. normal-only comparison would cleanly separate the contribution of each structural modality.

## Nice-to-Haves

- A controlled experiment retraining a competitive baseline (e.g., a ControlNet variant or a single-modality version of the proposed architecture) on a comparable subset of HumanVerse would cleanly disentangle the method's contribution from the data's contribution. This is standard practice for ablation but expensive for full-scale comparisons.
- Expanding the limitations section with concrete failure examples (e.g., finger/eye synthesis failures) would strengthen the paper's candid assessment of its own capabilities.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about dataset not being released:** The harsh critic notes the paper does not mention whether HumanVerse will be released and that this "limits its contribution to reproducibility." Per instructions, criticisms about release status of resources introduced by the paper are retained as soft points; however, this is at most a reproducibility concern, not a technical weakness. It does not affect the evaluation of the paper's contributions.
- **Criticism about missing 1024×1024 quantitative results:** The paper explicitly and sensibly uses the first-stage 512×512 output for quantitative comparison and the refiner for qualitative comparison only. This is a deliberate design choice, not a flaw.
- **Criticism about introduction not quantifying prior shortcomings on the same data:** This is a framing concern, not a substantive weakness.
- **Request for "normal-only" ablation variant moved to Trivial (handled above, not a core weakness).**

## Novel Insights

None beyond the paper's own contributions. The key tension surfaced by the reviews — that the method's advantage over baselines cannot be cleanly decomposed into architectural vs. data contributions — is already implicitly present in the paper's own design (the ablation table controls for data and does show architectural benefit). The reviews do not produce a genuinely novel observation that the paper fails to address.

## Suggestions

- In a rebuttal or revision, add a controlled experiment training a simpler baseline (or a single-modality version of the proposed model) on a HumanVerse subset of matching size to demonstrate the marginal gain from joint denoising independent of dataset curation.
- Report the user study methodology (number of participants, instructions, randomization procedure, significance test) to make the preference claims verifiable. Even brief details would substantially improve credibility.
- Add variance estimates (bootstrap or multiple-seed runs) for the main metrics in Table 1.

## Score and Decision

**Originality:** The joint denoising architecture with replicated expert branches for RGB, depth, and normal in a unified network is a novel design. The dataset is a significant scalability contribution.

**Importance of research question:** High — hyper-realistic human generation with structural control is an important and active area.

**Claims supported:** The core claim (joint denoising improves structural coherence) is supported by ablation. The SOTA claim is partially supported but weakened by the data confound in cross-method comparisons.

**Soundness of experiments:** Generally sound, with thorough ablation. The main weakness is the uncontrolled baseline comparison. The user study is underreported.

**Clarity of writing:** Clear and well-structured. Method description is detailed. Figures and tables are informative.

**Value to the community:** The dataset and architecture are valuable contributions. The approach is likely to influence future work on structure-aware generation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>