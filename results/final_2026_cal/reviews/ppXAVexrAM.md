Now I have all the information I need. Let me write the consolidated review.

## Summary

ARSS introduces the first decoder-only autoregressive transformer (GPT-style) for novel view synthesis from a single image, conditioned on camera trajectories. It uses a video tokenizer for temporally consistent discrete tokens, a camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and a hybrid token permutation strategy that preserves temporal causality while enabling bi-directional spatial context. Evaluated on RealEstate10K, ACID, and zero-shot DL3DV, ARSS achieves competitive or superior results compared to diffusion-based and feed-forward NVS baselines, with particularly strong evidence from error accumulation analysis showing slower degradation along camera trajectories.

## Strengths

- **First causal autoregressive framework for NVS with camera control.** The paper is the first to apply a decoder-only AR transformer to novel view synthesis with explicit camera trajectory conditioning (Abstract, Section 1, Section 3). The related work section confirms the absence of prior work in this specific paradigm. This is a genuinely novel direction.

- **Well-designed hybrid token permutation strategy with clean ablation evidence.** Section 3.2.3 defines a permutation that shuffles spatial tokens within each frame while preserving temporal order. Table 2 and Figure 7 provide convincing quantitative and qualitative evidence that this hybrid strategy outperforms both raster (no permutation) and full spatial+temporal permutation across all four metrics, and avoids the geometric distortion and temporal inconsistency of the alternatives.

- **Video tokenizer ablation shows clear, large-margin improvements.** Table 3 demonstrates that adopting a video tokenizer (VidTok) instead of per-frame VQ improves FVD by ~62% (137.68 → 52.56), with substantial gains in PSNR (+3.53), SSIM (+0.128), and LPIPS (−0.204). This directly supports the claim that temporal consistency matters and validates the design choice.

- **Error accumulation analysis provides the strongest evidence for the paper's core causal-AR thesis.** Figure 6 plots per-frame metrics across 16 frames and shows ARSS maintaining the highest scores with markedly flatter degradation slopes than all baselines (LVSM, MotionCtrl, RayZer, ViewCrafter). This is a clean, direct demonstration of the claimed advantage — causal generation accumulates less error over long trajectories.

- **Competitive quantitative and qualitative results across multiple benchmarks.** Table 1 shows ARSS leads on PSNR (19.02) and LPIPS (0.269) on RealEstate10K, best LPIPS (0.265) on ACID, and best zero-shot LPIPS (0.347), FID (84.96), and FVD (91.25) on DL3DV. The qualitative figures (3, 4, 5) show compelling visual quality across in-domain and out-of-distribution scenes.

## Weaknesses

### Fatal
None.

### Major

1. **The camera autoencoder — a core module — is neither validated nor ablated.** This is the most significant gap in the paper. Section 3.2.2 introduces a dedicated camera autoencoder that compresses Plücker raymaps into latent tokens serving as explicit 3D positional guidance, inserted at every spatial position interleaved with visual tokens. However, the paper provides:
   - No reconstruction accuracy metrics for the autoencoder (e.g., mean angular error on ray directions, dot-product consistency on the Plücker coordinates).
   - No analysis of how errors in camera tokens propagate to the autoregressive generator.
   - No ablation removing camera tokens, replacing them with simpler conditioning (e.g., per-frame camera embedding as a global token), or varying the loss weights λ₁–λ₄ to isolate the contribution of each geometry constraint.
   
   Without this evidence, it is unclear whether the camera autoencoder is genuinely beneficial, redundant, or even harmful. Given that camera tokens are paired with every visual token and are the primary mechanism for camera control, evaluating their fidelity is essential to the paper's claims.

2. **Baseline comparison fairness is not fully documented.** The paper does not state whether baselines (SEVA, ViewCrafter, MotionCtrl, Genwarp, LVSM, RayZer) were evaluated using their official checkpoints at their native resolutions, fine-tuned to 256×256, or otherwise adapted. The paper acknowledges that "SEVA benefits from large-scale, high-resolution training data" while ARSS is "trained from scratch...with relatively low resolution" (Section 4.2, Discussion), which suggests asymmetric training conditions. However, without explicit documentation of the evaluation protocol for each baseline — including resolution, frame count, and any adaptation steps — the reader cannot assess whether the quantitative advantages (e.g., +1.1% PSNR, −21% LPIPS on Re10K) reflect genuine methodological superiority or artifacts of a mismatched evaluation setup. This weakness tempers but does not invalidate the claims, since the zero-shot DL3DV results and error accumulation analysis provide independent evidence.

### Minor

3. **Missing inference cost analysis.** AR methods typically involve sequential token-by-token decoding, which can be substantially slower than feed-forward or single-shot diffusion approaches. The paper does not report per-view generation time, throughput, or any efficiency comparison with baselines. This is important context for evaluating the practical trade-offs of the proposed approach.

4. **No statistical significance or confidence intervals.** Table 1 reports point estimates without error bars. Several metric gaps are small (e.g., FVD on ACID: 53.69 SEVA vs. 54.60 ARSS; PSNR on Re10K: 18.73 SEVA vs. 19.02 ARSS), and without variance estimates it is unclear whether these differences are meaningful.

5. **"Parallel decoding" advantage stated but not demonstrated.** Section 3.2.3 mentions that random shuffling enables parallel decoding, citing Pang et al. (2025), and that "the system has the capacity to predict multiple tokens at one time." However, the paper never demonstrates parallel decoding in practice, reports no speedup from it, and the inference procedure is described as "iteratively sampling the target tokens using a next-token prediction manner." This claim should either be demonstrated or removed to avoid confusion.

6. **Error accumulation analysis limited to 16 frames.** Figure 6 stops at frame 16. For world-model applications where trajectories of 50–100+ frames are relevant, extending this analysis would substantially strengthen the paper's central claim about causal AR reducing long-horizon error accumulation.

### Trivial
None.

## Nice-to-Haves

- Validate the camera autoencoder internally (reconstruction error on Plücker rays, unit-norm and orthogonality compliance) and ablate it against simpler camera conditioning baselines.
- Document the evaluation protocol for each baseline (checkpoint source, resolution adaptation, frame count matching) in the main paper or appendix.
- Report inference speed (seconds per view) for ARSS and key baselines, with and without potential parallel decoding.
- Provide error bars or confidence intervals for all quantitative metrics (e.g., across multiple random seeds or dataset splits).
- Extend the error accumulation plot to 32+ frames.
- Ablate the four loss terms in Eq. (5) to demonstrate the contribution of each geometry constraint.

## Removed Points

These points from the inputs were removed with justifications:

- **Token sequence design is "underspecified" and "ambiguous"** — Removed. Eq. (6) clearly shows the interleaved π-x structure with spatial permutation indices. The Figure 2 caption explicitly describes "an interleaved sequence of visual and camera tokens (v0, x0, v1, x1, ...)." The phrase "camera tokens are inserted before visual tokens" (Section 3.2, Figure 2) is clarified by the equation and figure; it means each camera token immediately precedes its paired visual token. The permutation is defined as shuffling spatial positions within each frame while keeping π-x pairs together, which is unambiguous from the notation P_i(j) applied to both tokens.

- **Criticism that "CE" is used without definition** — Removed. Lines 203-205 define CE as cross-entropy loss immediately after Eq. (3).

- **Criticism about camera autoencoder architecture details being omitted** — Removed as a repro/nitpick. The paper states it uses "stacked 3D convolutional and downsampling blocks" and symmetric upsampling, with the output having matching spatial/temporal dimensions to the visual tokens (5×32×32). Complete architecture tables for every submodule are not expected in a main paper of this length.

- **Strength Finder's generic/superficial strengths** — The Strength Finder includes generic claims like "first causal autoregressive model" which is rephrased as a concrete verified strength above. Vague supporting strengths about "quantitative results that match or exceed diffusion-based methods" are merged into the verified strengths above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the camera autoencoder.** This is the single most important addition. Report reconstruction accuracy on Plücker coordinates (mean angular error, unit-norm violation, orthogonality error). Add an ablation replacing camera tokens with a per-frame camera embedding as a global condition token. If the camera autoencoder provides no benefit over this simpler baseline, the design should be reconsidered; if it does, the evidence will substantially strengthen the paper.

2. **Document baseline evaluation protocol.** In the experimental setup or an appendix table, state for each baseline: (a) whether official checkpoints were used, (b) resolution at evaluation, (c) whether any fine-tuning or adaptation was applied, and (d) number of frames matched. If resolution differences exist, discuss how they affect the comparison.

3. **Report inference speed.** Add a simple table showing per-view generation time (seconds) for ARSS vs. at least 2–3 baselines, to contextualize the quality-efficiency trade-off. If parallel decoding is implemented, report the speedup over sequential decoding.

4. **Add confidence intervals or error bars** for the main quantitative results (Table 1), at minimum for the methods trained by the authors.

---

**Calibration Report:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| EL1esipMln | 3.00 | 1 (low) | Context-Aware AR multi-conditional image gen; less rigorous eval, withdrawn |
| IeqzZmCG9y | 3.00 | 1 (low) | AR video autoencoder; different task, rejected |
| imblpbUryY | 2.67 | 1 (low) | Sparse NVS with 3DGS; different paradigm, withdrawn |
| guUaZN0kyC | 2.50 | 1 (low) | Single-image dynamic scene gen; rejected |
| PZQHihJlfm | 5.00 | 1 (mid) | **ArchonView** — first AR (next-scale VAR) for object-centric NVS. Most similar anchor. ARSS has better evaluation breadth (error accumulation + ablations + zero-shot) but shares similar gaps (missing baseline documentation). ARSS is somewhat stronger. |
| 8A4AQyJO9m | 4.50 | 1 (mid) | AR4D — AR 4D generation from monocular video; different task (4D), withdrawn |
| 3XxoBwMusJ | 5.00 | 1 (mid) | 3DScenePrompt — camera-controllable video gen with 3D memory; diffusion-based, similar evaluation concerns |
| fIPng6j4eM | 4.50 | 1 (mid) | **Kaleido** — seq2seq generative neural rendering; diffusion-based, criticized for missing comparisons. ARSS has stronger novelty (first AR NVS) and better ablations. |
| kI27Niy4xY | 8.00 | 1 (high) | Text-to-3D stitching; different task, much stronger paper |
| DTQIjngDta | 8.00 | 1 (high) | Permutation-equivariant geometry learning; different task |
| kkBOIsrCXh | 8.00 | 1 (high) | Embodied navigation foundation model; different task |
| DM0Y0oL33T | 8.00 | 1 (high) | Generative universal verifier; different task |
| yx3g4sF70y | 5.00 | 2 (narrow) | **SHARP** — feed-forward 3D Gaussian regression NVS. Strong zero-shot but different paradigm (feed-forward, not generative AR) |
| 2wSORykWAc | 5.50 | 2 (narrow) | **Faithfulness NVS** — training-free diffusion NVS. Similar rigor/gaps; Reject. ARSS has stronger novelty but similar evaluation concerns. |
| aJJppqAm6r | 6.00 | 2 (narrow) | **XFactor** — self-supervised NVS with transferability. Stronger evaluation framework (new metric, ablations). ARSS has broader contribution (first AR NVS) but weaker evaluation rigor. |
| QXc2NBJFHr | 6.00 | 2 (narrow) | Less3Depend — NVS without 3D knowledge. Different paradigm (feed-forward, not generative) |
| BR2ItBcqOo | 6.00 | 2 (narrow) | Rotary Ray Embedding for NVS; different paradigm |
| NQq9JLMfNN | 6.00 | 2 (narrow) | Unified 3D scene understanding; different task |

**Round-1 bracket:** 4.5–6.5. **Round-2 narrowing:** Placed above ArchonView (5.00) and comparable to Faithfulness NVS (5.50) but below XFactor (6.00). Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>