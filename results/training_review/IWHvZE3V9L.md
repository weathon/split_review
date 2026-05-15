Now I have a thorough understanding of the paper. Let me compile the final consolidated review, carefully verifying each reviewer claim against the actual paper text.

---

## Summary

ProPicker proposes a promptable 3D segmentation model for universal particle picking in cryo-ET. The architecture uses a frozen TomoTwin encoder to extract a 32-dim feature vector from a user-provided sub-tomogram prompt, which then conditions a 124M-parameter 3D U-Net to segment the target particle class. The paper demonstrates that ProPicker achieves competitive F1 scores with the state-of-the-art universal picker TomoTwin while being 5–10× faster, generalizes to unseen particles and real-world tomograms with zero additional training, and can be efficiently fine-tuned on as few as one annotated tomogram.

## Strengths

- **Convincing speed–accuracy trade-off over the SOTA universal picker.** Figure 2 shows ProPicker-C with stride=32 matches TomoTwin stride=4 on most of 100 training-set particles while being >5× faster, and ProPicker-TM with stride=56 yields a 10× throughput increase with only minor performance loss. Throughput is quantified concretely (tomograms/hour on a single L40 GPU), making the comparison verifiable.

- **Demonstrated universality on unseen particles.** Table 1 reports best-case F1 scores on 8 particles excluded from training. ProPicker-C (stride=32) performs on par with TomoTwin (stride=2) across all eight classes. The paper is transparent that CryoSAM is evaluated on clean ground-truth data (its best-case scenario) and still underperforms both methods, strengthening the case for domain-specific training.

- **Data-efficient fine-tuning with practical impact.** Figure 5 shows that fine-tuning ProPicker on a single tomogram (~150 instances per particle) lifts F1 from near zero to 0.5–0.8, outperforming single-class DeepFinder at all data amounts and multi-class DeepFinder in the low-data regime (1–2 tomograms). This quantifies a genuine practical benefit for cryo-ET practitioners with limited annotation budgets.

- **Real-world transfer with no additional training.** On EMPIAR 10045 (purified ribosomes) and EMPIAR 10988 (in-cell ribosomes), ProPicker-C trained exclusively on synthetic data produces plausible segmentation masks. On EMPIAR 10988, it achieves F1=0.61 (denoised) vs. TomoTwin's 0.60, confirming the approach transfers to experimental data.

- **Novel promptable architecture for cryo-ET.** The conditioning mechanism — feeding a frozen TomoTwin embedding into a 3D U-Net — is a concrete architectural contribution that bridges template-matching representations with efficient segmentation, distinct from both non-universal segmentation pickers (DeepFinder, DeePiCt) and template-based universal pickers (TomoTwin).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Ambiguity in real-world preprocessing (Section 4.1.3).** The paper reports "ProPicker-C achieves 0.61 on the denoised tomogram and 0.55 on the raw, un-denoised tomogram" while "TomoTwin achieves a best-case F1 of 0.60." It is not explicitly stated whether TomoTwin was evaluated on the denoised or raw tomogram. If TomoTwin was run on raw data while the 0.61 for ProPicker uses denoised input, the comparison is not controlled. The paper should clarify this and ideally report both conditions for TomoTwin. (Note: the claim of unfair advantage is weakened by the fact that ProPicker's *raw* F1 of 0.55 is still close to TomoTwin's 0.60, so this does not invalidate any core conclusion — but the ambiguity is a reporting flaw.)

2. **Limited evaluation scale for core generalization claims.** The generalization to unseen particles (Section 4.1.2) is evaluated on a single tomogram containing 8 particle types with no repeated runs or variance estimates. The real-world quantitative evaluation (Section 4.1.3) similarly rests on a single F1 score from one tomogram. While this is not unusual for the field, the lack of statistical confidence measures limits how strongly the claims can be stated.

3. **Missing ablation of the conditioning mechanism.** The paper does not include an experiment that removes the prompt conditioning (e.g., using a fixed/random prompt vector or a randomly initialized prompt encoder) to quantify the contribution of the promptable design versus the U-Net's baseline segmentation capability. Without this, it is difficult to assess how much the frozen TomoTwin encoder adds over a simpler conditioning approach.

4. **Fine-tuning setup differs from the main model.** The fine-tuning experiments (Section 4.2) use a *re-trained* ProPicker (with the 8 test particles excluded from both ProPicker's and TomoTwin's training). This is a valid control, but it means the fine-tuning results are not directly comparable to the prompt-based results in Sections 4.1.1–4.1.3, which use the originally trained model. The paper should note this more explicitly to avoid confusion.

### Trivial

- The training duration (number of epochs, convergence criteria) is not reported. While not critical for reproducibility of a published model, it would help practitioners gauge training cost.
- F1 scores are reported as "best-case" with thresholds optimized on test data throughout. While the paper acknowledges this follows common practice (Rice et al., 2023), it inflates absolute scores relative to what could be achieved without ground-truth access at inference time.

## Nice-to-Haves

- A controlled experiment applying CryoSAM to denoised versions of the synthetic tomograms (rather than only clean ground-truth) would provide a more complete picture, though the current asymmetric comparison already favors the baseline.
- An analysis of sensitivity to prompt quality (e.g., mis-centered prompts, different instances of the same particle) would strengthen the practical usability claims.
- A few concrete failure case visualizations on real-world data (the paper acknowledges failures exist) would help users understand the method's limitations.

## Removed Points

These points were raised by reviewers but are removed (with justifications) as per guidelines:

1. **"Unfair CryoSAM comparison"** — The paper states: *"CryoSAM is unable to pick particles in the noisy tomogram. Therefore, we applied CryoSAM to the clean ground truth tomogram... to probe the best-case performance."* The asymmetry favors the baseline (CryoSAM gets easier input), not the proposed method. Per hard rule: remove criticisms about unfair comparison when asymmetry favors the baseline.

2. **"Overclaiming 'universal' based on 113 protein types"** — The paper defines universal as the ability to pick *unseen* particles from a single prompt, which is demonstrated experimentally (Table 1). The claim is precisely scoped and supported by evidence.

3. **"Missing comparison to DeePiCt/DeepETPicker in fine-tuning"** — The paper explicitly selects DeepFinder as a representative non-universal baseline and explains why (lines 148–149). Criticizing the absence of every available method is scope creep; the chosen baseline is appropriate.

4. **"Re-training ProPicker as a confound"** — The paper explicitly states: *"we re-trained ProPicker and its TomoTwin prompt-encoder, and excluded the 8 particles from both training sets."* This is a proper experimental control to ensure the particles are truly unseen, not a confound.

5. **"CryoSAM's best-case evaluation invalidates conclusions"** — The paper's conclusion is that CryoSAM *even on clean data* underperforms, which strengthens the argument that domain-specific training is necessary. This is valid reasoning, not a flaw.

## Novel Insights

The most interesting finding beyond the paper's own framing is the effectiveness of a frozen TomoTwin encoder (trained via deep metric learning for template matching) as a prompt conditioner for dense 3D segmentation. The 32-dim embedding space learned for similarity search apparently retains sufficient spatial and structural information that a U-Net can decode it into per-voxel segmentation masks for the target particle. This suggests that the TomoTwin embedding space is more informative than a mere "similarity score" representation — it captures particle-specific features that can be spatially grounded. This bridging of metric-learning embeddings and dense segmentation is a useful design pattern that could generalize to other cryo-ET tasks beyond particle picking (e.g., membrane segmentation, organelle identification). The data efficiency of fine-tuning (usable results from one tomogram) further supports the value of the pretrained representation.

## Suggestions

1. **Clarify the real-world preprocessing.** Explicitly state whether TomoTwin was applied to raw or denoised tomograms in Section 4.1.3, and ideally report both conditions for all methods.
2. **Add a conditioning ablation.** Include a baseline that replaces the TomoTwin prompt encoder with a learned embedding (or removes conditioning entirely) to quantify the contribution of the promptable design.
3. **Add error bars or repeated runs.** For the generalization experiments (Sections 4.1.2, 4.1.3, 4.2), even a small number of repeated evaluations with different train/test splits would substantially strengthen the statistical grounding of the claims.
4. **Report the training schedule.** Adding the number of epochs and convergence criteria would improve reproducibility for practitioners.

## Score and Decision

The paper presents a novel, well-motivated architecture with a clearly demonstrated speed advantage (5–10×) over the SOTA universal picker, competitive performance on unseen particles and real-world data, and practically useful fine-tuning efficiency. The weaknesses are real but limited to evaluation depth and reporting clarity — they do not invalidate the core contributions. The paper is a solid contribution to the cryo-ET particle picking literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>