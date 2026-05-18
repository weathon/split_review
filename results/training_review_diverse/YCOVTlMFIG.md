Now I have all the evidence I need. Let me compile the final consolidated review.

## Summary

This paper proposes Slerp+, extending the Slerp approach (Jang et al. 2024a) from composed image retrieval to a joint image-video setting. The key idea is to fine-tune a BLIP vision-language model on both image-caption and video-caption pairs simultaneously, using the same Slerp spherical interpolation at inference to compose visual and text embeddings. A new video benchmark (Activitynet-CoVR) is also introduced. The main finding — supported by the ablation study — is that joint training on both modalities mutually improves performance on both image and video composed retrieval tasks. Results on CIRR, FashionIQ, WebVid-CoVR, and Activitynet-CoVR show competitive or state-of-the-art zero-shot performance.

## Strengths

- **First demonstration that joint training on image-caption and video-caption pairs mutually benefits both composed image retrieval (CoIR) and composed video retrieval (CoVR).** The ablation study (Table 5, rows f,g) directly shows that training on both modalities improves image retrieval (CIRR) and video retrieval (WebVid-CoVR) compared to training on either modality alone. This synergistic effect is the paper's most concrete contribution and is demonstrated empirically.

- **Simple, parameter-efficient zero-shot method that achieves strong results across multiple benchmarks.** Slerp+ uses standard VTC and VTM losses with LoRA fine-tuning (<0.32% of parameters), requires no compositional triplets or complex projection modules, yet outperforms prior zero-shot methods and even the supervised CoVR approach on WebVid-CoVR-Test (R@1 19.3 vs. 14.9), CIRR (R@1 25.5), and FashionIQ (R@1 27.3). The simplicity of the approach is a genuine strength.

- **Introduction of Activitynet-CoVR, a more challenging video evaluation benchmark.** While the characterization is limited, the benchmark provides a useful additional testbed with longer, more complex text modifications, and Slerp+'s strong performance on it (Table 2) demonstrates generalization beyond the training distribution, outperforming even the supervised CoVR model.

- **Qualitative results** (Figures 3, 4) corroborate the quantitative findings and help build intuition for how the method works.

## Weaknesses

### Major

- **The "unified" framing substantially overstates what is actually demonstrated.** The paper repeatedly claims a system where "a query, composed of either an image or video accompanied by user modification text, can retrieve corresponding images and/or videos" (Figure 1 caption) with a gallery comprising both images and videos (Section 3.3). However, all experiments evaluate same-modality retrieval only (image→image, video→video). No cross-modal experiment (image+text→video or video+text→image) is conducted, nor is there any mixed-gallery evaluation. The paper's actual contribution is a single model trained jointly on both modalities that performs better on separate modality-specific benchmarks, which is a weaker claim. The claims should be scaled back to match what is evaluated, or cross-modal experiments should be added.

- **The comparison to prior Slerp (Jang et al. 2024a) is confounded by backbone choice.** In the main results tables (Tables 3, 4), Slerp+ (BLIP backbone, joint training) is compared against "Slerp TAT" (CLIP backbone). The improvements could be substantially driven by the stronger BLIP backbone rather than the joint training scheme. While the ablation in Table 5 (row f vs. row a) does compare BLIP-only training vs. BLIP+video training, this comparison is only in the ablation table rather than the main results, and the paper never directly compares a BLIP-based Slerp (without any video data) against CLIP-based Slerp TAT to disentangle backbone effects. A clean baseline — fine-tuning BLIP on image-caption pairs only (no video), then evaluating with Slerp on CoIR benchmarks alongside the CLIP-based baselines — would be needed to isolate the contribution of adding video data.

### Minor

- **The choice of Slerp over early-fusion is not empirically justified on the same model.** The paper dismisses early-fusion as "not intended to compose" (Section 3.3) but provides no experiment comparing Slerp vs. early-fusion inference using the same trained Slerp+ model. The ablation (row c) only compares Slerp against simple averaging of frame and text embeddings, not against early-fusion with cross-attention. Given that the model's text encoder already has cross-attention layers (from BLIP), a direct empirical comparison would strengthen the technical argument for Slerp as the composition method of choice.

- **Hyperparameter sensitivity of the Slerp balancing scalar *t* is not discussed.** The paper uses *t*=0.6 for video and *t*=0.7 for image without justification or sensitivity analysis. Since Slerp performance can vary with *t*, a sweep on a validation set is expected.

- **Training for a single epoch** is noted in the paper but not justified with convergence curves. Given that only 0.32% of parameters are trainable, the model may be underfit. Showing validation curves or discussing convergence would address this.

- **Video embedding via averaging frame-level [CLS] tokens** is a simple design choice that is not ablated. Alternatives (e.g., temporal attention pooling, averaging patch tokens) exist and could affect performance.

- **The claimed advantage of BLIP's cross-attention** (Section 3.2: "especially advantageous for understanding the complex relationship between visual data and text") is asserted rather than demonstrated. A comparison against a CLIP-style dual encoder under the same joint training setup would substantiate this claim.

- **Activitynet-CoVR is under-characterized.** The paper provides its construction pipeline (intra/inter-pair creation, LLM prompting, human filtering) but no distributional analysis (caption lengths, modification types, difficulty vs. WebVid-CoVR). As a secondary contribution, this limits its value as a benchmark resource.

### Trivial

- None of substance beyond what is captured above.

## Nice-to-Haves

- A sensitivity analysis for the Slerp balancing scalar *t* (e.g., a plot of R@1 as a function of *t* on a validation set).
- Cross-modal retrieval experiments (image query→video target, video query→image target) to validate the "unified" framing.
- An ablation comparing Slerp vs. early-fusion inference on the same trained Slerp+ model.
- A direct comparison in the main result tables of "Slerp+ (BLIP, images only)" against prior CLIP-based methods to isolate backbone effects.

## Removed Points

- **Availability/release status of Activitynet-CoVR** — The reviewer criticized the paper for not stating whether the dataset will be released and implied the contribution is unverifiable without it. Per policy, this is removed: the dataset is cited as existing in the paper; questioning release status is not a valid weakness.
- **"Slerp w/ only image (row f) still uses the joint training procedure on the image-only subset—it is not a baseline that mirrors Jang et al.'s exact setup"** — This specific sub-point is factually misleading: row (f) trains on images only with VTC+VTM+LoRA, which IS a valid ablation for isolating the effect of video data. The underlying concern (no CLIP→BLIP backbone comparison in main tables) is kept above in the Major section.
- **Criticism about missing appendix / missing proofs / missing references** — Parser-stripped content; paper likely contains them in the original submission.

## Novel Insights

None beyond the paper's own contributions. The finding that joint training on images and videos produces mutual improvement is itself the main novel observation.

## Suggestions

1. **Temper the "unified" claims** to accurately reflect what is demonstrated: a single model jointly trained on image and video data that improves task-specific retrieval, rather than a system tested on cross-modal or mixed-gallery retrieval.
2. **Add a clear baseline** in the main results: Slerp+ with BLIP fine-tuned on image-caption pairs only (no video), evaluated on the CoIR benchmarks. This would cleanly separate the BLIP backbone effect from the joint-training effect and strengthen the controlled comparison in Tables 3 and 4.
3. **Add a cross-modal experiment** (image+text→video and video+text→image) even if results are modest — this would validate whether the system's embedding space truly supports unified retrieval.
4. **Include a sensitivity analysis** for the Slerp scalar *t* and consider showing training convergence (even a single loss curve).

## Score and Decision

The paper presents a useful empirical finding (joint image-video training mutually benefits both composed retrieval tasks) with a simple, well-executed method and solid results across four benchmarks. Its main weaknesses are (a) overstated framing relative to what is actually evaluated and (b) a confounded comparison to the prior Slerp method that is not fully disentangled from the backbone change. These issues are substantive but addressable. The contribution is incremental but positive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>