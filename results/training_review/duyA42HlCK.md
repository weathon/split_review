Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the consolidated review.

---

Actually, let me check one more thing about the "Denoise RGB" and "Denoise RGB + Depth" settings to understand the architecture used.

The paper says in the ablation:
- "Denoise RGB, that only learns to denoise an image."
- "Denoise RGB + Depth, which also predicts depth."

These are described under the section "Simultaneous Denoise with Expert Branch" and compared against different expert branch configurations. The way it's structured:

1. Denoise RGB - baseline
2. Denoise RGB + Depth - another baseline
3. Half DownBlock & UpBlock - expert branch variant
4. Two DownBlocks & UpBlocks - expert branch variant
5. Full model

The question is whether (1) and (2) use the expert branch architecture or a standard UNet. Since they're in the section about expert branches, they might use expert branches too. But "Denoise RGB" with one branch is essentially the same as a standard UNet.

For "Denoise RGB + Depth": if it uses two expert branches (one for RGB, one for depth), it's still an expert branch architecture. If it uses a single UNet with two output heads, it's the baseline the reviewer asks for.

The description is ambiguous, but I think it's more likely that "Denoise RGB + Depth" uses the same expert branch framework with 2 branches (RGB and depth) rather than 3. This is consistent with the ablation setting: "we explore... how many layers to replicate" - the first two rows test which target modalities to use with expert branches, and the next two test architectural specifics of the branches.

If this interpretation is correct, then there IS no "single UNet with three output heads" baseline. The reviewer's point stands.

OK, I think I have enough information now. Let me write the final review.Now I have thoroughly verified every claim against the paper. Let me produce the final consolidated review.

## Summary

HyperHuman proposes a unified framework for hyper-realistic controllable human image generation. Its core technical novelty is a Latent Structural Diffusion Model that jointly denoises RGB, depth, and surface-normal via structural expert branches with a shared backbone, coupling appearance and multi-level spatial geometry within a single network. The paper also introduces HumanVerse (340M human images with pose/depth/normal/caption annotations) and a second-stage Structure-Guided Refiner for high-resolution output. Extensive experiments on MS-COCO show large improvements over prior controllable generation methods (ControlNet, T2I-Adapter, HumanSD) and general T2I models.

## Strengths

- **Joint denoising of RGB, depth, and normal in a unified network with expert branches.** The design of replicating input-proximal and output-proximal layers while sharing the middle backbone is technically clean and well-motivated. The ablation (Table 2) shows this architecture yields spatially-aligned structure maps (lowest L2 errors for depth and normal) while improving FID (17.18 vs. 21.68 for RGB-only on the same data), demonstrating that the joint learning of appearance and structure genuinely helps.

- **HumanVerse dataset is a substantial resource.** At 340M in-the-wild human images with pose, depth, normal, and caption annotations, this is far larger and richer than existing human-centric datasets (e.g., SHHQ, DeepFashion). The curation pipeline — YOLOS detection, aesthetic filtering, MiDaS/Omnidata for depth/normal, MMPose for pose, and outpainting to improve structure annotation — is clearly described in Section 4.

- **Noise schedule improvements are well-motivated and empirically validated.** The paper identifies that monotonous structure maps (depth/normal) leak low-frequency information under standard schedules and shows (Table 2) that zero-terminal SNR with v-prediction and same-timestep sampling across modalities yields substantial gains (FID 29.36 for different timesteps → 17.18 for same timestep with improved schedule). The "same timestep" argument about sampling sparsity (1-in-10^9 chance under independent sampling) is a concrete, non-obvious insight.

- **Quantitative results show large margins on a standard benchmark.** On the MS-COCO human subset, HyperHuman achieves FID 17.18 vs. second-best 22.98 (25.2% relative improvement), KID 4.11 vs. 7.98 (48.5% relative), and best pose accuracy metrics across all controllable methods. The FID-CLIP vs. CLIP curves over multiple CFG scales (Figure in Table 2) further show consistent dominance.

## Weaknesses

### Fatal
None.

### Major

1. **The second-stage Structure-Guided Refiner is not quantitatively evaluated.** The paper states it is trained on "an internal dataset" (line 147) and that its outputs "are merely utilized for visual comparison" (line 144). There is no FID, KID, user study, or ablation measuring whether the refiner improves quality over the Stage 1 output. The random dropout scheme for robust conditioning — while plausible — is not ablated or validated. Since the refiner is listed as a core contribution (contribution 2 in the introduction), the lack of any quantitative evidence supporting it is a significant gap. The "internal dataset" also makes this part of the pipeline non-reproducible.

2. **Pose accuracy metrics use an unnamed pose estimator that may overlap with the annotation pipeline.** The paper annotates HumanVerse with ViTPose-H (MMPose) and evaluates pose accuracy using a "state-of-the-art pose estimator" (line 187) without naming it. If the same estimator family is used for both training annotation and evaluation, the results could be biased toward the model's learned annotation distribution. This is not discussed or mitigated (e.g., by verifying with an independent estimator like OpenPose). Given that pose accuracy is a headline result (best AP/AR across all methods), this oversight weakens confidence.

### Minor

1. **The main comparison (Table 1) conflates method and data.** HyperHuman is trained on 340M human-specific images from HumanVerse, while baselines use their pre-trained weights (trained on different data: general LAION-5B for SD, LAION-2B+COCO for ControlNet, etc.). The paper does not retrain any baseline on HumanVerse. **However**, the ablation study in Table 2 controls for data by varying only method components on HumanVerse, showing that the proposed architecture improves FID from 21.68 (RGB-only) to 17.18 (full method) — about a 4.5 FID gain attributable to methodology. This partially addresses the concern, but the magnitude of the improvement over baselines in Table 1 (e.g., 17.18 vs. ControlNet's 27.16) likely has a non-trivial data component that is never disentangled. The paper should acknowledge this explicitly as a limitation.

2. **The expert branch design is not fully isolated from capacity/multi-task effects.** The ablation compares "Denoise RGB" and "Denoise RGB + Depth" against the full model, but does not include a "single UNet with three output heads (no replicated branches) trained on RGB+Depth+Normal" baseline. Such a control would isolate whether the benefit comes from the specific branch replication or simply from the added parameters and multi-task objective. The existing ablations on branch configuration (Half DownBlocks, Two DownBlocks) partially address architectural sensitivity, but the missing "single UNet, three outputs" baseline is a clear gap.

3. **User study lacks methodological detail.** Table 3 reports 89–99% preference for HyperHuman over baselines, but the paper provides no information on number of participants, image selection process, or whether the study was blind. The extreme preference rates (98–99% over HumanSD and T2I-Adapter) hint at possible confounds (e.g., resolution differences, cherry-picked examples). This weakens the otherwise supportive qualitative evidence.

4. **The outpainting step for annotation improvement is not evaluated.** The paper uses SD-Inpaint to outpaint images for better structure estimation (Section 4), but does not verify whether this actually improves annotation quality or introduces artifacts that the model later inherits.

5. **Choice of depth+normal as structural targets is not justified against alternatives.** The paper motivates depth and normal as complementary structural representations (Section 3.2) but does not compare against other structural representations (e.g., segmentation maps, edge maps) to show these are the best choices.

### Trivial
- None beyond standard formatting issues that are parser artifacts.

## Nice-to-Haves
- Reporting confidence intervals or variance estimates for FID/KID across multiple runs, though single-run evaluation is the norm for large-scale diffusion training.
- Retraining at least one baseline (e.g., HumanSD or ControlNet) on HumanVerse to directly measure the data contribution, though this is a massive undertaking.
- Ablating the refiner's impact by comparing Stage 1 output vs. Stage 2 output with quantitative metrics on a human subset at 1024×1024.

## Removed Points

Points flagged for removal, treated with caution:

- **"No mention of concurrent work like Realistic Vision"** — Removed per Hard Rules (cannot verify unreviewed community models; also, the paper compares against peer-reviewed published methods, which is appropriate).
- **"The paper claims state-of-the-art but evidence conflates method and data advantage"** — The reviewer's strongest phrasing of this criticism is overly harsh. The paper *does* provide data-controlled evidence via Table 2 ablation, which weakens (not eliminates) the concern. Moved to Minor tier after verification against the paper.
- **"FID_CLIP is non-standard"** — FID_CLIP (using CLIP features instead of Inception features) is a known variant (used by e.g., DALL-Eval, Parti). Not a standard flaw. Removed.
- **"Different timesteps baseline likely under-trained"** — Speculative; no evidence in the paper that training was not fully converged. Removed.
- **"No confidence intervals"** — Standard for large-scale diffusion model evaluations; moved to Nice-to-Haves.
- **"as one of the earliest attempts in human generation foundation model overstates novelty"** — The paper acknowledges HumanSD as prior work and correctly notes the scale difference. This is a reasonable claim, not overstatement. Removed.
- **"random dropout is a known technique, not cited"** — The technique is different from classifier-free guidance; the paper does not claim novelty here. Minor omission not worth highlighting as a weakness.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviews surfaces one non-obvious tension: the paper's strongest *evaluation* asset (data-controlled ablations in Table 2) and its weakest evaluation liability (the untouched refiner) coexist in the same submission. The ablations convincingly show that the joint denoising architecture improves FID by ~4.5 points on fixed data, yet the paper buries this evidence alongside a main-table comparison where the data advantage is uncontrolled. This asymmetry suggests the paper could strengthen its core methodological claim simply by elevating the data-controlled evidence and being more circumspect about the refiner.

## Suggestions

1. **Quantitatively evaluate the refiner.** Compute FID/KID on a human subset at 1024×1024, comparing Stage 1 (upsampled) vs. Stage 2 output. Ablate the random dropout scheme. Report these numbers or drop the refiner as a claimed contribution.
2. **Disclose the pose estimator used for evaluation and verify with an independent estimator** (e.g., OpenPose) to rule out annotation-estimator overlap bias. Even a brief discussion acknowledging this concern would improve transparency.
3. **Add a "single UNet with three output heads" baseline** to the ablation to isolate the expert branch design from capacity/multi-task effects.
4. **Provide user study details** (N participants, selection procedure, blinding protocol) in the appendix.
5. **Acknowledge the data confound explicitly** in the limitations section and note that Table 2 provides data-controlled evidence for the method's contribution.

## Score and Decision

The paper presents genuinely useful contributions: the HumanVerse dataset, the joint denoising architecture with expert branches, and technically sound noise schedule improvements. The core methodological claims are supported by data-controlled ablations. However, the paper is weakened by the unevaluated refiner (a claimed contribution that is effectively not tested), the undisclosed evaluation pose estimator, and the absence of a clean architectural control for the expert branch design. These issues are addressable but limit confidence in the paper's full set of claims. The strengths are solid enough to justify a qualified acceptance with a clear path to addressing the gaps.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>