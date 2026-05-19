I have verified all claims against the paper. Let me now construct the final consolidated review.

---

## Summary

This paper proposes DA-CLIP, a framework that adapts a frozen CLIP image encoder for image restoration by training a lightweight controller (inspired by ControlNet). The controller predicts degradation embeddings (which classify corruption type) and hidden controls that modify the CLIP encoder to produce high-quality content embeddings from corrupted inputs. These are integrated into restoration networks (IR-SDE, NAFNet) via cross-attention and prompt learning. A 10-degradation-type dataset with BLIP-generated captions is constructed. The method achieves strong perceptual metrics (LPIPS, FID) on both degradation-specific and unified restoration tasks.

## Strengths

1. **Accurate degradation classification.** The controller achieves near-perfect classification: 9 out of 10 degradation types are predicted perfectly, and blurry reaches 91.6% accuracy (line 306). In contrast, the original CLIP scores ≤2% on noisy/raindrop and 0% on inpainting. This directly validates the core claim that DA-CLIP can predict real degradation types from corrupted inputs.

2. **Consistent perceptual improvement across all tasks.** In the degradation-specific setting (Table 1), DA-CLIP+IR-SDE achieves the best LPIPS and FID on all four tasks (deraining: 0.031/11.79 vs IR-SDE 0.047/18.64; low-light: 0.083/34.03 vs IR-SDE 0.129/47.28; deblurring: 0.058/6.15 vs IR-SDE 0.064/6.32; dehazing: 0.030/5.52 vs IR-SDE 0.060/8.33). For deraining, it even achieves superior scores across all four metrics (PSNR, SSIM, LPIPS, FID).

3. **Integration demonstrated in both diffusion and non-diffusion architectures.** Beyond IR-SDE (a diffusion model), DA-CLIP is integrated into NAFNet (an MSE-based network), improving it above PromptIR across all metrics (Table 2: NAFNet+DA-CLIP LPIPS 0.145, FID 47.94 vs PromptIR 0.147/48.26). This broadens the applicability claim beyond a single backbone.

4. **Best perceptual results in the unified setting.** DA-CLIP achieves LPIPS 0.127 and FID 34.89 across 10 degradation types (Table 2), outperforming AirNet (0.182/64.86) and PromptIR (0.147/48.26), which are methods specifically designed for unified restoration.

## Weaknesses

### Fatal
None.

### Major

1. **Incomplete manuscript preparation: placeholder section and duplicated content.** Section 7 ("Related Work," line 452–458) consists only of "Text text text... TODO!" and a note to merge it with the Background section. While Section 2 ("Background and Related Work") already provides substantive related work discussion, the presence of a separate, empty section with a TODO marker is unprofessional and signals an unpolished draft. Additionally, there are two "Discussion and Analysis" sections — one as a subsection of Experiments (line 377) and another as a standalone section (line 429) — with overlapping content and reused figures (Fig. 5 subfigures duplicated in lines 314–376 and lines 398–425, with different captions). This organizational disarray impairs readability and suggests the manuscript was assembled from multiple drafts without a final cleaning pass.

2. **Claims of "state-of-the-art" are metric-dependent and not uniformly supported.** Across the four degradation-specific tasks (Table 1), DA-CLIP achieves SOTA on *perceptual* metrics (LPIPS, FID) on every task, and SOTA on *all* metrics only for deraining. For deblurring, PSNR (30.88) trails MAXIM (32.86); for dehazing, PSNR (30.16) trails DehazeFormer (30.29) and SSIM (0.936) trails DehazeFormer (0.964). In the unified setting (Table 2), average PSNR (27.01) is *below* PromptIR (27.14) and SSIM (0.794) is substantially below PromptIR (0.859). The paper's narrative (title, abstract) frames the contribution as advancing SOTA broadly, but the actual advantage is concentrated in perceptual quality. The paper does acknowledge this implicitly (line 148, 302) but the framing remains overly broad.

3. **Ablation analysis relies on training curves without numerical values.** The "Discussion and Analysis" sections argue for the effectiveness of individual components (degradation embedding, HQ content embedding, ground-truth oracle) using only line plots (Fig. 5, Fig. 14, Fig. 15 in the text). No final numerical values for LPIPS, FID, PSNR, or SSIM are reported for any ablation configuration. The reader cannot quantify how much each embedding contributes, or determine the gap between predicted and oracle embeddings from the prose alone. The single quantifiable claim — >91.6% classification accuracy — appears as a sentence (line 306) without a supporting confusion matrix or per-class breakdown table.

4. **Evaluation coverage is thin.** (a) Only one dataset per task is used in the degradation-specific setting (Rain100H for deraining, LOL for low-light, GoPro for deblurring, RESIDE-6k for dehazing). (b) Test set sizes for several degradation types in the unified setting are very small (JPEG: 29, Low-light: 15, Noisy: 68, Raindrop: 58), which raises reliability concerns for the reported averages. (c) No variance, confidence intervals, or multiple-run statistics are reported anywhere, making it impossible to assess whether gaps between methods (e.g., NAFNet+DA-CLIP PSNR 27.22 vs NAFNet+Degradation 27.02) are significant.

### Minor

1. **"NAFNet + Degradation" baseline is not clearly defined.** The term "Degradation" in Table 2 (line 273) is not explained — is it the DA-CLIP degradation embedding, a one-hot encoding of the true label, or something else? The text (line 304) says "adding our degradation context" but does not specify what this baseline consists of.

2. **Per-task breakdown in the unified setting is qualitative only.** Radar plots (Fig. 6) give an overview but no numerical table of per-degradation PSNR, SSIM, LPIPS, FID is provided. The paper notes that JPEG and noise have lower distortion metrics (line 302) but does not quantify this.

3. **The two Discussion sections contain a self-contradictory statement.** Line 385 says: "increased model complexity and computational cost. The test-time computational cost (FLOPs and runtime) is however virtually unaffected." If model complexity increases, it is unclear how test-time cost is unaffected; this needs clarification.

### Trivial

- None beyond the structural issues noted above (the presentation problems are covered in Major #1).

## Nice-to-Haves

- A confusion matrix or per-class accuracy table for the 10 degradation types would strengthen the classification claim.
- Tabular per-task breakdown of all metrics for the unified setting (not just radar plots).
- Error bars or results from multiple seeds for the main comparisons.
- Ablation with zero-initialization disabled, to confirm its necessity (following ControlNet practice).

## Removed Points

*These points were considered but moved here because they do not survive verification against the paper.*

- **"Missing related works"** (harsh critic's suggestion to compare with "more recent unified restoration methods"). Per policy, I cannot judge what is missing from the related works section without external knowledge; the paper already cites AirNet (2022), PromptIR (2023), Restormer (2022), MAXIM (2022), and others.
- **"Dataset quality assessment needed for BLIP captions"** (harsh critic suggests human evaluation). This is speculative — there is no evidence the captions are inaccurate, and the method is not fundamentally contingent on caption perfection.
- **"Ablation on zero-initialization strategy"** (harsh critic requests this ablation). A reasonable suggestion but not a core weakness; moved to Nice-to-Haves.
- **Generic formatting/style nitpicks** (the critic's complaints about "duplicated figures with the same captions" are partially inaccurate — the figures are reused with *different* captions, but the content overlap is real and already addressed in Major #1).
- **Strength Finder's generic strength about "superior unified restoration performance"** — retained but qualified; the claim is accurate for perceptual metrics but the wording in the original strength was broader than the evidence supports. It has been integrated into Strength #4 with appropriate caveats.

## Novel Insights

The two reviews converge on a significant observation: the paper's main empirical advantage is concentrated in perceptual metrics (LPIPS, FID), while distortion metrics (PSNR, SSIM) often fall below existing methods — sometimes substantially (e.g., unified SSIM 0.794 vs PromptIR 0.859). This pattern is not accidental: it likely reflects a property of the DA-CLIP approach itself. By injecting CLIP-derived high-quality content embeddings into the restoration network, the method biases the output toward perceptually naturalistic images, which may trade off pixel-level fidelity. This is a genuine and potentially valuable tradeoff — many applications prioritize visual quality over exact reconstruction — but the paper does not articulate it as a deliberate design choice. An interesting open question is whether the SSIM gap could be closed by tuning the relative weighting of the contrastive loss components, or whether it is an inherent limitation of using VLM features for low-level vision.

## Suggestions

1. **Complete the manuscript.** Remove or fill the placeholder Section 7. Merge or delete the duplicate Discussion section and remove redundant figures.
2. **Add a tabular ablation table** reporting final PSNR/SSIM/LPIPS/FID for each component setting (no embedding, content only, degradation only, both, ground-truth oracle) on a held-out validation split.
3. **Add a per-task numerical table** for the unified setting (all 10 degradation types × 4 metrics), including test set sizes.
4. **Clarify the "NAFNet + Degradation" baseline** in Table 2 and the corresponding text.
5. **Add error bars** (at minimum from 2–3 seeds) for main comparisons, especially where gaps are small.
6. **Calibrate the language** about "state-of-the-art" to specify the metric and setting (perceptual metrics; deraining for all metrics).

## Score and Decision

The paper presents a well-motivated idea and demonstrates real improvements on perceptual metrics across a diverse set of restoration tasks. However, the manuscript is not in a publishable state due to a placeholder section, duplicated content, and lack of quantitative rigor in the ablations. The evaluation, while showing a clear pattern, is thin (one dataset per task, no variance, small test sets for several degradation types). The contribution is promising and the core results are credible, but substantial cleanup and additional rigor are needed before the paper meets publication standards.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>