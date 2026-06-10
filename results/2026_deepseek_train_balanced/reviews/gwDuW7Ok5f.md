## Summary

DAEFR proposes a dual-branch encoder architecture for codebook-based blind face restoration. The key idea is to train a dedicated low-quality (LQ) encoder alongside the standard high-quality (HQ) encoder, align them via a patch-level association stage (similar in spirit to CLIP), and fuse the two feature streams via multi-head cross-attention before code prediction. The method achieves competitive results, particularly on real-world benchmarks where it obtains best FID on WIDER-Test and BRIAR-Test.

## Strengths

1. **Best FID on multiple challenging real-world datasets.** On WIDER-Test, DAEFR achieves FID 36.720 vs. 38.798 (CodeFormer, second-best), and on BRIAR-Test FID 90.032 vs. 91.653 (GPEN, second-best). These are real-world benchmarks with severe, varied degradation. This concretely demonstrates that the dual-encoder design provides a practical benefit over prior single-encoder codebook methods in realistic settings.

2. **Ablation study isolates each component's contribution.** Table 3 systematically decomposes the design into separable decisions (dual vs. single encoder, with/without association, linear vs. MHCA fusion). This allows the reader to trace which design choice drives which metric improvement — e.g., the MHCA module (Exp. d→e) improves LMD from 4.197 to 4.019 and NIQE from 4.290 to 3.815, while the association stage (Exp. c→d) improves LPIPS from 0.349 to 0.343. This granularity is valuable even when the trade-offs are mixed (see weaknesses).

3. **Downstream face recognition validation.** Table 5 shows DAEFR consistently outperforms CodeFormer on ArcFace verification under atmospheric turbulence degradation (a type unseen at training time), with the gap widening as degradation severity increases (73.78% vs. 71.67% at the most severe level). This provides practical validation beyond image-quality metrics.

4. **Monotonic improvement with increasing LQ feature contribution.** Table 4 (tab:fuse_lq) shows that as the LQ feature scalar increases from 0 to 1.0, LPIPS, PSNR, and SSIM all improve monotonically. This directly supports the paper's central premise — that LQ-domain features carry useful information that a single-encoder design discards.

## Weaknesses

### Fatal
None.

### Major

1. **Claim-evidence mismatch: "superior performance" is not supported by the synthetic benchmark.** The abstract (line 10) and contributions (line 38) claim "superior performance," but on the synthetic CelebA-Test (Table 1b), DAEFR achieves **zero best scores** across all seven metrics (FID, LPIPS, NIQE, IDA, LMD, PSNR, SSIM). It places second on four metrics and third on three. The paper itself describes these results as "competitive" (line 249), which is accurate, but the abstract and contributions use "superior" — a mismatch that overstates the evidence. On real-world datasets (Table 1a), DAEFR does achieve best FID on WIDER-Test and BRIAR-Test and best NIQE on LFW-Test (3 best out of 6), which is a stronger showing, but the blanket "superior" framing across all settings is not justified.

2. **The full architecture regresses LPIPS relative to simpler variants, and this is not discussed.** In the ablation (Table 3), the full method (Exp. e) achieves LPIPS of **0.351**, which is *worse* than: a single HQ encoder (Exp. a: 0.344), a single LQ encoder (Exp. b: 0.343), and the dual-encoder setup with association and linear fusion (Exp. d: 0.343). The paper highlights that the dual-encoder setup "yields better performance" based on NIQE, and that the MHCA module improves LMD and NIQE, but never acknowledges the LPIPS regression. This is selective reporting of a real trade-off. Understanding why the full method harms perceptual similarity while helping identity preservation (LMD) and perceptual quality (NIQE) would significantly strengthen the paper.

3. **Selective comparison in the face recognition experiment.** Table 5 compares DAEFR against only CodeFormer on the downstream recognition task. Other baselines (GFP-GAN, GPEN, VQFR, RestoreFormer, DR2) are excluded without explanation. Since CodeFormer is the strongest baseline on several synthetic metrics (LPIPS, IDA, LMD, PSNR), this single comparison is not a convincing demonstration of superiority. This weakens what would otherwise be a strong supplementary experiment.

### Minor

1. **Marginal gains from the association stage.** The association stage (Exp. c vs. d in Table 3) improves LPIPS by 0.006 (1.7%), LMD by 0.061 (1.4%), and NIQE by 0.007 (0.2%). These improvements are directionally positive but very small, and a single dataset is insufficient to establish the general effectiveness of the association mechanism. The paper's claim that association "effectively enhances the encoder's capability" (line 265) would benefit from additional evidence (e.g., cross-dataset validation or feature-space visualizations).

2. **The CLIP analogy is loose and potentially misleading.** The paper states the association stage is "similar to CLIP" (lines 33, 118). CLIP aligns representations across *different modalities* (image and text) via large-scale contrastive learning. Here, the alignment is between two feature representations of the *same image* from two encoders within the same modality, using a diagonal-maximization objective on a similarity matrix. The description would be more precise if it simply described the mechanism without invoking the CLIP analogy.

3. **MHCA query/key/value assignment is underspecified.** The fusion equation $Z^{A}_{f} = \text{MHCA}(Z^{A}_{h},Z^{A}_{l})$ (line 139) does not specify which feature serves as query and which as key/value. This matters for reproducibility, as the choice determines whether HQ features attend to LQ features or vice versa.

### Trivial
None.

## Nice-to-Haves
- Reporting confidence intervals or error bars for FID (known to be noisy at moderate sample sizes) would strengthen the quantitative claims.
- A limitations paragraph discussing cases where DAEFR underperforms (e.g., the LPIPS regression on synthetic data) would improve the paper's completeness.

## Removed Points
*These points were identified by reviewers but are removed after cross-checking against the paper.*

1. **"Core motivation undermined by method's own design"** — The reviewer claimed DAEFR contradicts its own critique because it also uses the HQ encoder to encode LQ images. However, the paper's critique (lines 6–7) is that prior work relies on a *single* encoder pre-trained on HQ data, *disregarding* the domain gap. DAEFR does not claim never to use the HQ encoder on LQ data; it adds a dedicated LQ encoder and associates the two. The distinction is about having *only* an HQ encoder vs. having *both* HQ and LQ encoders. The criticism is removed because it mischaracterizes the paper's actual claim.

2. **"Association stage training details underspecified"** — The paper states that $y_{i,j}$ is the ground-truth label and that $N=C$ (the number of patches). The diagonal-maximization objective is implicit but standard for this type of feature alignment; the formulation in Eq. 4 is sufficient for reproducibility.

3. **"No failure cases"** — While a limitations discussion would improve the paper, this is a common formatting constraint for conference papers, not a weakness in the method itself. Moved to Nice-to-Haves.

4. **Various formatting/style nitpicks and requests for equipment-release or repository details** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
1. **Recalibrate the claims** to match the evidence. The synthetic results (zero best scores, Table 1b) support "competitive" framing; the real-world results (3 best out of 6, Table 1a) support a stronger but qualified claim. Acknowledging the mixed landscape would be more persuasive than blanket "superior" language.
2. **Analyze and discuss the LPIPS regression.** The full method worsens LPIPS while improving LMD and NIQE. This is an interesting trade-off worth understanding and reporting, not suppressing. A dedicated analysis (e.g., does the MHCA module introduce high-frequency artifacts that help identity but hurt perceptual similarity?) would be the single most valuable addition.
3. **Extend the face recognition comparison** (Table 5) to at least 2–3 additional baselines (e.g., GFP-GAN, VQFR) to make the result convincing.
4. **Specify query/key/value assignment** in the MHCA equation for reproducibility.
5. **Evaluate the association stage on multiple datasets** or provide feature-space visualizations (e.g., t-SNE of pre- vs. post-association features) to demonstrate its effect beyond a single-table comparison.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>