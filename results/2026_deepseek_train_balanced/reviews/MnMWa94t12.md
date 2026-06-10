Here is my consolidated review.

---

## Summary

The paper proposes DyST (Dynamic Scene Transformer), a model that learns latent neural scene representations from monocular video with disentangled control over camera pose and scene dynamics. The key technical innovation is a Latent Cycling Scheme (LCS) applied during training on a custom synthetic dataset (DySO) that forces camera and dynamics information through separate latent bottlenecks. The model is co-trained on synthetic DySO and real Something-Something v2 (SSv2) videos to transfer the disentanglement to real data.

## Strengths

- **Latent Cycling Scheme (LCS) induces measurable disentanglement**: The paper's core technical contribution is clearly articulated and quantitatively verified. With LCS, the contrastiveness metric reaches R^cam=0.06 (16.7× closer for matching vs. non-matching views in camera latent space) and R^dyn=0.42 (2.4× closer), versus R^cam=0.72 and R^dyn=1.26 without LCS (Sec. 5.2, Eqs. 7–8, ablation Sec. 5.4). This cleanly isolates the effect of the training scheme on latent separation.

- **Co-training strategy for sim-to-real transfer**: The paper identifies that LCS requires a structured multi-view multi-dynamics dataset unavailable for real video, and proposes a practical co-training solution (Sec. 3.4): alternating between synthetic batches with latent swapping and real-video batches with self-estimation. Qualitative results on SSv2 (PCA, distance matrices, video manipulation) suggest the separation transfers to real data, demonstrating the feasibility of the approach.

- **Contrastiveness metric for evaluating latent disentanglement**: The metric defined in Eq. 7 provides a principled, interpretable measure of how well camera and dynamics information are separated, going beyond qualitative inspection. This is a useful methodological contribution for the community.

- **Downstream control demonstrations**: Motion freezing ("bullet-time" effect) and video-to-video motion transfer are demonstrated on real SSv2 videos (Sec. 5.3), providing behavioral evidence that the latent representation is genuinely factored and can be used for practical control tasks even with out-of-distribution latents.

## Weaknesses

### Major

- **No comparison against any baselines**: The paper surveys relevant methods (NeRF-VAE, SRT, RUST, MonoNeRF, NerFPlayer, RoDynRF, etc.) but provides no quantitative or qualitative comparison against any of them. Without baselines, the reader cannot calibrate whether DyST advances the state of the art, whether modeling dynamics actually helps reconstruction quality, or whether the disentanglement is superior to alternative approaches. At minimum, a static-scene model (e.g., SRT/RUST) on SSv2 would establish a reference PSNR and clarify the value of modeling dynamics. The ablation study (Sec. 5.4) is informative but is an internal comparison, not a substitute for external baselines.

- **No quantitative evaluation on real-world videos**: The paper's central claim involves learning representations from *real-world videos*, yet PSNR/SSIM/LPIPS are reported only on synthetic DySO. On SSv2, only qualitative results are shown (Sec. 5.1: a single cup-manipulation video and still frames; Sec. 5.2: PCA; Sec. 5.3: manipulation examples). Given that real videos use the trivial self-estimation path (Eq. 6) rather than the LCS swap, the critical question of how well the model actually performs on held-out real data is left unanswered. Quantitative metrics on SSv2 would directly substantiate the sim-to-real transfer claim.

### Minor

- **Disentanglement metric computed only on synthetic data**: The contrastiveness metric (R^cam, R^dyn) is computed only on DySO where ground-truth labels exist. On real videos, the paper relies on qualitative evidence (distance matrices, PCA). A proxy metric on real data (e.g., measuring background consistency when freezing the camera latent, or tracking consistency when freezing the dynamics latent) would strengthen the transfer claim from suggestive to quantified.

- **Only one real-world dataset evaluated (SSv2)**: SSv2 has relatively constrained camera motion and object-centric dynamics. Testing on a more challenging dataset (e.g., DAVIS, or in-the-wild YouTube videos) would strengthen claims of generality. The paper acknowledges this as future work, but in its current form the evidence for real-world applicability is narrow.

- **Ablations performed only on synthetic data**: The ablation study (Sec. 5.4: no swap, 50% swap, averaging) is insightful but restricted to DySO. An ablation on real data showing, e.g., whether reducing the synthetic training fraction degrades real-world separation, would strengthen the analysis of how robustly the transfer works.

### Trivial

- Training compute budget, runtime, and model size are not reported. For a method trained for 4M steps with batch size 256 on 170K videos plus 1M synthetic scenes, these are practically useful details.

## Nice-to-Haves

- A quantitative proxy for disentanglement on real data (e.g., flow consistency under latent freezing).
- Analysis of failure cases: when does the L2 loss cause blur, and how do large camera displacements or fast object motion affect quality?
- An ablation removing the architectural difference between CE and DE (learned token vs. GAP) to further isolate the contribution of LCS vs. architecture.

## Removed Points

These points are flagged as removed; treat them with caution.

- **"Quantitative DySO results referenced but not present"** (from Harsh Critic): Removed because the tables are included via `\input{}` commands (standard LaTeX). The figures exist in the original submission and were stripped by the PDF text extraction. This is a parser artifact, not a paper flaw.
- **"Both CE and DE share a single transformer, creating a weak architectural inductive bias"**: The paper explicitly acknowledges this design choice for efficiency (Sec. 3.4) and shows via ablation that without LCS, separation collapses entirely — confirming LCS is the intended mechanism, not architecture. This is a design choice, not a weakness.
- **"The LCS scheme's reliance on synthetic data is under-analyzed"**: Demoted from major to nice-to-have. The paper acknowledges the limitation (Sec. 3.4), the co-training strategy is clearly described, and reframing it as a "methodological gap" overstates the issue. Additional sensitivity analysis would strengthen but is not a core flaw.
- **"Only one real-world dataset (SSv2)" from Strength Finder**: Not a strength — it's a realistic scope choice, not a positive contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a baseline comparison: at minimum, compare against a static-scene model (e.g., SRT or RUST) on the same SSv2 data to establish whether modeling dynamics improves reconstruction.
- Report PSNR/SSIM/LPIPS on held-out frames of SSv2 to provide quantitative evidence for the real-world transfer claim.
- Develop a proxy metric for disentanglement on real data without ground-truth labels (e.g., measure background consistency when freezing the camera latent across frames).
- Include training time and compute budget for practical context.

## Score and Decision

The paper presents a genuinely clever idea (Latent Cycling Scheme) and provides solid quantitative evidence for disentanglement on synthetic data. The method is clearly described, the co-training strategy is practical, and the qualitative demonstrations are compelling as a proof of concept. However, the evaluation is critically incomplete for a top-venue paper: there are **no baseline comparisons** and **no quantitative results on real-world videos**. The evidence does not currently meet the bar for acceptance at ICLR. The core ideas are worth developing further with stronger empirical validation.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>