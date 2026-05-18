Now I have a thorough understanding of the paper and all the reviewer inputs. Let me construct the final consolidated review.

## Summary

**Paper:** NeRM introduces a two-stage generative framework combining variational Implicit Neural Representations (INRs) with latent diffusion for high-framerate human motion synthesis. The key insight is representing motions as continuous fields over temporal coordinates, which allows training directly on datasets with varied native framerates (20–250 fps) without discarding or downsampling data. The first stage learns per-sequence variational latent codes via a coordinate-conditioned decoder with a Codebook-Coordinate Attention (CCA) mechanism; the second stage learns a diffusion model over these latents. NeRM achieves state-of-the-art FID on HumanML3D (0.180 vs. next best 0.427) and demonstrates high-framerate generation that avoids interpolation artifacts like foot sliding.

## Strengths

- **Novel approach to a real, underexplored problem.** NeRM is, to my knowledge, the first generative motion model that handles varied native framerates directly during training — a practical bottleneck that prior work sidesteps by downsampling and discarding data. The core idea (continuous motion field via INR + latent diffusion) is well-motivated and the two-stage decomposition is architecturally sound.

- **Substantial empirical results on standard benchmarks.** NeRM achieves state-of-the-art FID on HumanML3D (0.180, vs. next best MLD at 0.427) and KIT (0.429, vs. next best 0.502) for text-to-motion, competitive results on action-to-motion (best Accuracy and Diversity on UESTC, Table 3), and best FID on unconditional AMASS (Figure 5). These results are presented with confidence intervals and represent a clear advance.

- **Meaningful high-framerate generation with direct evidence.** Table 2 shows NeRM achieving clip-FID scores far below interpolated baselines at 60, 90, and 120 fps (e.g., 0.216 at 90 fps vs. 2.588 for interpolated MLD). Figure 4b provides visual confirmation that NeRM avoids foot sliding artifacts that appear under SLERP interpolation of baseline outputs.

- **Abundant conditioning flexibility.** The same variational INR decoder supports text (via CLIP), action labels (via learned embeddings), and unconditional generation within a unified diffusion framework — demonstrated across three distinct experimental settings.

## Weaknesses

### Fatal
None.

### Major

- **No ablation studies for individual components.** The paper introduces at least four distinct design choices — variational INR (optimizing latent distributions vs. deterministic latents), Codebook-Coordinate Attention (CCA vs. plain Fourier features), progressive multi-framerate training, and the two-stage diffusion-over-latents pipeline — but never isolates their contributions. The sole ablation is "NeRM (fixed-framerate train)" which controls for raw-data benefit. Without ablations, readers cannot tell whether the codebook, variational formulation, progressive schedule, or diffusion stage actually drive the improvements, or whether simpler alternatives would suffice. This undermines the attribution narrative built around each component, even though the full system's effectiveness is clear from the SOTA results. **Impact:** The paper's claims about which specific designs matter are unsupported.

### Minor

- **Codebook pre-training details are unspecified.** The paper states the codebook is "pre-trained" (line 86) but does not specify on what data, using what objective, or whether it is frozen or fine-tuned during INR training. While CoCo-NeRF is cited, the adaptation to motion data is non-trivial and requires specification for reproducibility and to rule out the concern that the codebook memorizes training structure that inflates reconstruction metrics.

- **Framerate encoding into the decoder is underspecified.** The paper states that framerate \(s\) is fed into the decoder \(f_\theta\) (Figure 2 caption, line 46) but never specifies how — as a scalar, an embedding, or concatenated with normalized coordinates. This detail affects whether the decoder truly conditions on framerate as a continuous variable, which is central to the any-framerate claim.

- **High-framerate evaluation uses only SLERP as a baseline.** The baselines (MLD, MDM, etc.) cannot natively generate high-framerates, so interpolation is a natural comparison. However, comparing against at least one simple learned upsampling network would provide a stronger test of whether NeRM's INR-based upsampling genuinely outperforms reasonable alternatives, not just linear blending. The lack of this comparison weakens but does not invalidate the claim.

- **Clip-FID metric is introduced but not validated.** The paper proposes clip-FID as a metric sensitive to local details like foot sliding (line 145) but provides no evidence — no correlation with human judgments, no analysis of what it captures beyond standard FID, and no specification of the clip sampling parameters (number of clips, clip size \(m\), sampling strategy). For a new metric used in core evaluation, this is a gap.

- **Continuous framerate claim is demonstrated only at discrete points.** The model is described as learning a continuous field, yet evaluation is limited to 20, 60, 100, and 250 fps — all within the training distribution. No results are shown at framerates not seen during training (e.g., 33, 75, 150 fps) or at non-integer timestamps, which would directly validate the "any-framerate" claim and rule out overfitting to training framerates.

- **No runtime or memory measurements.** The paper claims NeRM is "memory-friendly" and "highly efficient even when generating high-framerate motions" (abstract), but provides no runtime comparisons, memory profiling, or latency measurements against baselines. Given that INRs can be computationally expensive to evaluate at many points, this claim needs quantitative support.

- **Key hyperparameters for the multi-framerate sampling are missing.** The maximum duration \(l_{max}\), clip size \(m\), number of clips per training step, and the progressive training schedule (iteration counts, learning rate changes) are not reported. These are non-trivial choices that likely affect performance and are needed for reproducibility.

### Trivial
None.

## Nice-to-Haves

- A simple learned temporal upsampling baseline (e.g., a small MLP or linear layer that upsamples low-framerate poses) would strengthen the high-framerate evaluation without requiring re-architecting the baselines.
- Quantifying the temporal sub-sampling property (Figure 4c) — e.g., measuring pose consistency when skipping frames — would turn a qualitative demonstration into a quantitative one.
- Validating clip-FID against human perceptual judgments on a small set of examples would establish the metric's credibility.

## Removed Points

- **Missing related works (HuMoR, EDGE).** The harsh critic mentions these under "Other Observations" — removed per instructions to not mention missing related works.  
- **Criticism that the high-framerate comparison uses "extremely weak" baselines.** The critic describes SLERP as an "extremely weak competitor." However, the baselines literally cannot generate high-framerates, so SLERP is a natural and reasonable comparison. The paper's comparison is not unfair. Downgraded to Minor and reframed.
- **"Weakness" about "unfair comparison" framing** — not applicable; no such framing exists in the review.
- **Generic phrasing about "should also cover Y in addition to X"** — limited to the one related-works instance above.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's strong SOTA results and its lack of component-level attribution. The paper shows an impressive FID of 0.180 on HumanML3D — nearly 2.4× better than the next best method — while also enabling high-framerate generation. Yet without ablations, it is unclear whether this gain comes from the INR formulation, the codebook, the variational latents, the progressive training, the diffusion stage, or simply the benefit of using more training data (i.e., not discarding low-framerate sequences). Disentangling these would substantially elevate the paper's contribution from "the system works well" to "here is why each piece matters." The review process highlights that in a paper with multiple architectural novelties, evaluating the whole system is necessary but not sufficient — readers need to understand what each component buys.

## Suggestions

1. **Add component-level ablation studies** as the top priority: (a) CCA vs. plain Fourier features, (b) variational INR vs. deterministic per-sequence latents, (c) progressive training vs. one-stage multi-framerate training, (d) latent diffusion vs. direct sampling from the variational prior without diffusion. Even a single table with these ablations on one dataset (e.g., HumanML3D FID and clip-FID) would dramatically strengthen the paper's causal claims.

2. **Specify codebook pre-training details**: dataset, objective (VQ-VAE? k-means?), frozen or updated during INR training, number of codes \(N\) and dimension \(d\).

3. **Clarify how framerate \(s\) is encoded** into the decoder \(f_\theta\).

4. **Report hyperparameters** for the multi-framerate clip sampling (\(l_{max}\), \(m\), clips per step) and the progressive training schedule.

5. **Provide runtime and memory measurements** to substantiate the efficiency claims.

6. **Validate clip-FID** by reporting its parameters (clip size, number of clips, sampling strategy) and ideally correlating it with a small human evaluation on foot sliding vs. smooth motion.

7. **Include at least one additional high-framerate baseline** (e.g., a lightweight learned temporal upsampler applied to baseline low-framerate outputs) to strengthen the comparison beyond SLERP.

## Score and Decision

**Originality:** 7/10 — the specific combination of variational INR + latent diffusion for motion with native-framerate training is novel, though each individual technique is established.  
**Importance of research question:** 8/10 — handling varied-framerate data and generating high-framerates addresses a genuine practical limitation.  
**Claims supported:** 5/10 — the system-level results support the overall effectiveness, but component-level claims are unablated and underspecified.  
**Soundness of experiments:** 6/10 — methodology is appropriate, evaluation covers multiple tasks and datasets, but missing ablations and limited high-framerate baseline weaken the validation.  
**Clarity of writing:** 7/10 — well-structured and readable, though several implementation details are missing.  
**Value to community:** 6/10 — the approach and SOTA results are valuable, but missing reproducibility details and ablations limit immediate impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>