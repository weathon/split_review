Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes the first feed-forward method for generating clothing-disentangled 3D characters from a single image. The approach operates in two stages: (1) a multi-part diffusion model with a novel multi-part attention mechanism disentangles the input image into separate body and clothing part images in 2D, and (2) a multi-view diffusion model with a combination attention mechanism generates multi-view images for each part, which are then fed into an off-the-shelf feed-forward reconstructor (LGM) for 3D Gaussian models. The paper also contributes a large VRoid-based anime character dataset with over 10k models and 11 clothing combinations each. Ablations demonstrate that both the multi-part attention and the special condition image for combination improve over simpler alternatives.

## Strengths

- **First feed-forward pipeline for clothing-disentangled character generation, with clean two-stage design.** The paper identifies a genuine gap — existing methods rely on per-scene optimization (hours per character) — and proposes a learned alternative. The two-stage decomposition (2D disentanglement first, then multi-view generation) is well-motivated: separating disentanglement from multi-view consistency simplifies each subproblem. The multi-part attention mechanism that allows cross-part information flow during 2D disentanglement is shown to improve PSNR by ~1.5–2.3 dB per part over independent generation (Table 2, Figure 4).

- **Novel combination attention with special condition image.** Integrating part composition into the multi-view diffusion model (rather than adding a separate external network) is a clean design choice. The ablation in Table 1 shows this outperforms direct feature fusion without the special condition image, providing evidence that the design contributes.

- **Large disentangled character dataset.** The dataset of >10k VRoid anime characters with 11 clothing combinations each (totaling >110k distinct clothed models) is a substantial resource. Prior datasets in this area are much smaller (<1,000 subjects), and this dataset enables training the feed-forward pipeline and will be useful for future research.

- **Quantitative improvement over adapted baseline.** The method consistently outperforms an adapted Wonder3D baseline on PSNR, SSIM, and LPIPS across all part categories (body, upper clothing, lower clothing, shoes) in Table 1, and the qualitative results in Figure 3 show cleaner decomposition.

## Weaknesses

### Fatal

None.

### Major

- **The final 3D output is never quantitatively evaluated, leaving a gap between the paper's claims and its evidence.** The paper's title, abstract, and contribution list all emphasize "3D character generation," yet every quantitative metric (PSNR, SSIM, LPIPS in Tables 1 and 2) measures only 2D multi-view image quality. No 3D geometry metrics (Chamfer distance, normal consistency, F-score) are reported for the reconstructed Gaussian models. No evaluation of whether the body and clothing layers are correctly separated in 3D space — e.g., inter-penetration rates, surface alignment quality — is provided. The 3D composition optimization (Eq. 3) is evaluated only qualitatively (Figure 5, right). While the 3D reconstruction uses an off-the-shelf method (LGM), the paper nevertheless frames the contribution as 3D generation, and the reader cannot assess whether the pipeline actually produces usable, correctly layered 3D models. This is the single most important missing evaluation.

- **The paper claims dramatic speed improvements ("hours to seconds") without reporting any runtime numbers.** The efficiency argument is central to the paper's motivation: optimization-based methods are "time-consuming and not scalable," while the proposed method runs in "seconds." Yet no wall-clock times are reported for any stage of the pipeline or for the full end-to-end process. No runtime comparison against any baseline is provided. The claim that LGM runs "in 1 second" is cited, but this covers only one module. Without measured runtime data, the paper's core value proposition — feed-forward efficiency — is unsubstantiated.

- **The "special condition image" used for the combination module is never defined or specified, making the approach irreproducible as described.** Section 3.2 states: "we propose to introduce a special condition image specifically for part combination" and describes its role in allowing the network to learn combination separately from multi-view generation, but never explains what this image contains, how it is constructed, or how it is derived from the input. This is not a minor implementation detail — it is a core design element of the combination attention mechanism. Without this specification, the method cannot be reproduced.

### Minor

- **The method is evaluated exclusively on anime characters, and the paper does not discuss whether the approach generalizes to realistic humans.** The dataset (Section 4.1) is explicitly VRoid anime, and the limitations section (4.6) discusses dataset size but not domain specificity. The multi-part attention, multi-view diffusion, and LGM reconstruction components may not transfer to photorealistic humans with different clothing topologies, body shapes, or material properties. The paper should either acknowledge this limitation honestly or provide evidence of cross-domain applicability.

- **The optional 3D part composition optimization (Eq. 3) is shown only qualitatively; no quantitative alignment improvement is reported.** Figure 5 (right) shows a visual comparison, but metrics such as mean surface distance between body and clothing parts before/after optimization, intersection volume, or rendering alignment error are missing.

### Trivial

None.

## Nice-to-Haves

- A failure analysis reporting the fraction of test cases where part decomposition fails (e.g., body leaking into clothing or vice versa) would help establish robustness.
- Renderings of the 3D models from viewpoints beyond the four training views would help demonstrate that the reconstruction is genuinely correct, not merely interpolating.
- A runtime breakdown (2D disentanglement, multi-view generation per part, LGM reconstruction per part, 3D optimization) would be informative even without a baseline comparison.

## Removed Points

Several criticisms from the reviewer inputs were removed or downgraded:

- **Optimization-based comparison (GALA, Cloth2Tex, Feng et al.):** The reviewer faults the paper for not comparing against GALA (takes a clothed 3D mesh input), Cloth2Tex (takes text descriptions), and Feng et al. (takes monocular video). These methods have fundamentally different input modalities and solve different tasks. Comparing against them would require adapting them to a different setting, not running them on the same benchmark. Removed as evaluating against the wrong class of expectations.

- **Ablation fairness concern:** The reviewer questions whether the "w/o special condition image" ablation is fair because the baseline "may have been trained without a combination condition at all." This is precisely what an ablation tests — the presence of a specific design element. The comparison is standard and the concern reflects a misunderstanding of ablation methodology. Removed.

- **"Optional" 3D optimization criticism:** The reviewer suggests the 3D composition optimization should not be called optional. The paper clearly describes it as optional (Section 3.3: "we propose an optional 3D part model optimization algorithm") and acknowledges it is used to improve alignment. The classification is not a weakness. Removed.

- **Missing appendix / missing proofs:** Not applicable; the parser strips these sections from all papers. Any such criticism would be a parser artifact, not an author error.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any unexamined implications, connections to broader trends, or methodological insights that the paper itself does not already articulate.

## Suggestions

1. **Report 3D evaluation metrics.** At minimum, compute Chamfer distance and normal consistency between the reconstructed 3D Gaussians and the ground-truth 3D models from the test set, for each part individually and for the composed character. Also report inter-penetration rates between body and clothing layers. If rendering is used for evaluation, render multi-view images of the reconstructed 3D models and compare to ground-truth renders using PSNR/SSIM/LPIPS.

2. **Report end-to-end runtime** in seconds, broken down by pipeline stage, and compare against at least one optimization-based method on a common subset.

3. **Define the "special condition image" explicitly.** State what it contains (e.g., a specific composition template, a blank canvas, a learned embedding visualized as an image), how it is constructed, and how it is fed into the model. This is essential for reproducibility.

4. **Acknowledge the anime-domain limitation** in the limitations section and discuss prospects or barriers for extending to realistic humans.

5. **Provide quantitative results for the 3D composition optimization** (Eq. 3): report surface alignment error or rendering consistency before and after optimization.

## Score and Decision

The paper presents a novel and well-motivated contribution — the first feed-forward pipeline for clothing-disentangled character generation — with clean ablations validating its key design choices and a substantial dataset contribution. However, the evaluation has two significant gaps: the final 3D output is never quantitatively assessed (despite "3D generation" being the headline claim), and the efficiency argument ("seconds vs. hours") is made without a single runtime measurement. The special condition image, a core design element, is underspecified to the point of non-reproducibility. These gaps are addressable but non-trivial. The core technical contribution is solid, and with proper evaluation the paper would be a strong submission.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>