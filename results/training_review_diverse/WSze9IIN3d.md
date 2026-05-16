Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

This paper introduces Progressive Autoregressive Video Diffusion (PA-VD) models, which assign progressively increasing noise levels across frames within the attention window during denoising. This design enables existing pre-trained video diffusion models to generate long videos (up to 1 minute / 1440 frames) autoregressively with large attention-window overlaps and without quality degradation. The method is architecture-agnostic (demonstrated on UNet-like and DiT-based backbones) and can work training-free on models with masked pre-training. Experiments on video extension show that PA-VD outperforms replacement-based baselines in terms of motion dynamics, aesthetic quality, and imaging quality while maintaining temporal coherence.

---

## Strengths

- **Progressive noise scheduling is a clean, well-motivated idea that enables natural autoregressive extension.** The core insight — gradually increasing noise levels across frames rather than assigning a single noise level — allows the attention window to overlap by up to F-1 frames without extra computational cost (Section 3.1, Eq. 3). This directly addresses the gap between "replacement-with-noise" (which smooths transitions but loses motion dynamics) and "replacement-without-noise" (which preserves dynamics but causes abrupt scene changes). The paper provides both intuitive justification (fine-grained conditioning, smooth temporal transitions) and algorithmic detail.

- **Architecture-agnostic and applicable with minimal changes.** The method works on both UNet-based and DiT-based backbones, demonstrated on two distinct models (Open-Sora v1.2 and a modified variant). The only modification required is to the noise level embedding computation (Section 3.3), and the method can work training-free on models already trained with per-frame independent noise levels (e.g., Open-Sora's masked pre-training, Section 4.1). This universality is a genuine advantage over approaches like StreamingT2V that require task-specific cross-attention modules.

- **Practical engineering insights (chunk-by-chunk denoising, clean-frame retention) are honestly documented and ablated.** The paper identifies that naive progressive scheduling causes divergence from 3D VAE chunking artifacts and temporal jittering, then provides concrete fixes: treating each VAE chunk as a single latent (lines 232–237) and keeping a chunk of clean latents in the attention window (lines 239–244). These are documented and qualitatively ablated (Figure 5, Ablations 1 and 2), giving readers useful implementation guidance.

- **Training-free variant demonstrates generalizability.** PA-Open-Sora-base works without any finetuning and still improves over the RN-Open-Sora-base baseline in dynamic degree, aesthetic quality, imaging quality, and scene change count (Table 1). This shows the method can leverage capabilities already present in pre-trained models, reducing the computational barrier to adoption.

- **Strong qualitative results and video examples.** The supplementary website provides side-by-side comparisons that visually demonstrate PA-VD's advantage over baselines in maintaining frame quality and motion consistency over the full 60-second duration. The qualitative evidence is consistent with and reinforces the quantitative findings.

---

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent test sets across compared models undermine the quantitative comparison.** The paper states (line 261) that PA-\internalmodel was evaluated on only 24 text prompts (48 videos) and StreamingSVD on 40 prompts (40 videos), while other models were evaluated on 40 prompts (80 videos). Because metrics are averaged over different prompt subsets with varying difficulty, the reported numbers are not directly comparable. This weakens the central quantitative claim that PA-\internalmodel achieves "state-of-the-art" results — while the gap appears large (e.g., substantially better aesthetic and imaging quality), the comparison is potentially biased. The paper does not acknowledge this caveat when interpreting the results in lines 283–293. **Why it matters:** The paper explicitly pits PA-\internalmodel against RW-\internalmodel, StreamingSVD, SVD-XT, etc. With mismatched test sets and no per-prompt matching or re-weighting, the reader cannot determine whether the better numbers reflect the method or easier prompts. This is the single most impactful weakness.

### Minor

- **Full text-to-video pipeline is not evaluated despite the paper's broad framing.** The introduction and method (Section 3.2) describe initialization and termination stages designed to handle text-only inputs without conditioning frames. However, all experiments condition on initial frames from real videos (video extension). The paper acknowledges this scope (line 264: "we focus on the video extension capability"), but the abstract and introduction claim "long video generation" without this qualification, and the initialization/termination stages remain untested loose ends. The contribution as demonstrated is "state-of-the-art video extension," not full text-to-long-video generation.

- **Ablation study is limited to qualitative comparison.** The two central design choices — chunk-by-chunk denoising and keeping clean frames — are ablated only qualitatively (Figure 5). While Ablation 2 (divergence within seconds) makes quantitative metrics infeasible, Ablation 1 (absent clean frames causing degradation) could and should be evaluated with standard quantitative metrics (e.g., VBench scores, scene-change count) to quantify the magnitude of the degradation. Without this, the paper cannot demonstrate *how much* each component contributes to the overall performance.

- **No confidence intervals or variance estimates.** The test set is small (80 videos at most, fewer for some models), and metrics could have high variance across prompts. Reporting standard deviations or confidence intervals would substantially increase confidence in the comparisons, especially given the test-set inconsistency issue above.

- **Inference time / compute cost not analyzed.** The paper claims "the additional computational cost at inference time is minimal" (line 40) and that the method has "large overlaps between the attention window" without extra computation (Section 3.1), but no concrete numbers are provided. For a method requiring 30 or 50 denoising steps per autoregressive shift, the total cost across hundreds of shifts for a 1-minute video could be large. A quantitative analysis of wall-clock time or FLOPs relative to baselines would help readers assess the practical trade-off.

### Trivial

- Naming inconsistency: line 261 refers to "\internalmodel-PA" while the rest of the paper uses "PA-\internalmodel."
- The claim that the method "can be easily implemented" (line 37) is an oversimplification given the training requires 1M videos + 2.3B images (line 215). This is not "easy" for most practitioners and should be qualified.

---

## Nice-to-Haves

- **Failure case analysis:** The paper would benefit from discussing what kinds of prompts or motions cause PA-VD to degrade (fast camera motion, complex scene changes, etc.), helping users understand limitations.
- **Standard deviations for metrics in Table 1:** Given the test set size and the partial coverage of some models, confidence intervals would significantly strengthen the quantitative evidence.
- **A single text-to-video demonstration using the initialization stage:** Even one qualitative example of starting from noise (no conditioning frames) and extending to a long video would validate the full pipeline described in Section 3.2.
- **Inference wall-clock time or step-count comparison:** Quantifying the computational cost of the autoregressive process vs. baselines would substantiate the "minimal additional cost" claim.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure references in text are placeholders"** — The figures are loaded via \input{} commands that reference separate files; they exist in the original submission. This is a parser artifact from the review format, not an author error.
- **"Missing appendix or missing proofs"** — The paper is an empirical systems paper, not a theoretical one. The parser strips appendix sections from the extracted text; they exist in the original submission.
- **"Missing related works"** — Per instructions, this cannot be verified without external sources and is not included.
- **"Naive progressive scheme doesn't work without chunk-by-chunk and clean-frame tricks"** — The paper is transparent about needing these modifications and documents them honestly. This is a strength (practical engineering insight), not a weakness.
- **"Unfair comparison because baselines use different architectures"** — The paper includes controlled baselines on the *same* base models (RW-\internalmodel, RN-\opensora-base), which directly isolate the benefit of the progressive noise schedule. SVD-XT and StreamingSVD are additional external baselines, not the primary comparison.
- **"Dynamic degree is not a quality metric"** — Dynamic degree is a standard VBench metric measuring motion amount. The paper reports it alongside aesthetic quality, imaging quality, and scene changes, not as a standalone quality measure. This is standard practice in the long-video generation literature (c.f. StreamingT2V).

---

## Novel Insights

None beyond the paper's own contributions. The reviews identify the test-set inconsistency as the primary concern but do not surface any unexpected findings about the method itself. The core insight — that progressive noise levels enable stable autoregressive extension — remains the paper's novel contribution, and the reviews do not challenge its validity; they challenge the strength of the evidence supporting it.

---

## Suggestions

1. **Recompute all comparisons on a common test set.** Report metrics on the intersection of prompts evaluated by all models (24 prompts, 48 videos) so that the quantitative comparison is apples-to-apples. If the full 40-prompt results show the same trends, this will substantially strengthen the paper.
2. **Add quantitative metrics for the ablation study.** For Ablation 1 (absent clean frames), compute VBench scores and scene-change counts. For Ablation 2 (no chunk-by-chunk), report that quantitative metrics are infeasible due to early divergence, and state this explicitly.
3. **Reframe the paper's scope or add a text-to-video experiment.** Either include at least one qualitative example of the full text-to-long-video pipeline (using the initialization stage), or adjust the abstract/introduction to clearly state the contribution as "long video *extension*."
4. **Report standard deviations or confidence intervals** for all metrics in the main table.
5. **Add an inference cost analysis** (wall-clock time or step count) comparing PA-VD to the baselines.

---

## Score and Decision

**Originality:** The progressive noise scheduling idea is novel and well-motivated, extending Diffusion Forcing to the specific challenge of autoregressive video generation with practical engineering contributions.

**Importance of research question:** Long video generation is a timely and important problem. The paper addresses a real limitation of current video diffusion models.

**Whether claims are well supported:** Partially. The strongest claim — state-of-the-art results — is undermined by the inconsistent test set issue. The qualitative and training-free results provide supporting evidence, but the quantitative comparison needs fixing.

**Soundness of experiments:** Reasonable design but weakened by the test-set mismatch and lack of variance estimates. The ablation is only qualitative.

**Clarity of writing:** Clear and well-structured. The method is explained logically with good use of formal notation.

**Value to the research community:** High. The method is architecture-agnostic, relatively simple to implement (conceptually), and the practical engineering insights are valuable to practitioners.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>