- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a Visibility Prediction Network (VPN) that is trained concurrently with a NeRF to predict the visibility of any 3D point from any training camera. From the predicted visibility vector across cameras, it derives a per-point reliability score using an effective sample size formulation. The paper demonstrates two post-training applications: (1) filtering low-visible near-range points during rendering to remove floaters, yielding a 0.6 dB average PSNR gain across 62 real-world scenes (58/62 improve); and (2) selecting additional training views via a visibility-based index to improve re-training quality. The core idea — that visibility from training cameras correlates with rendering reliability at novel views — is well-motivated and practically relevant.

## Strengths

- **Efficient concurrent training of VPN alongside NeRF (Sec. 3.1):** The VPN is trained via binary cross-entropy loss with stop-gradient on the NeRF's ground-truth visibility, using the same ray-sampling pattern as NeRF training. This design adds minimal training overhead and cleanly separates visibility learning from radiance learning. The architecture (hash grid + small MLP) follows efficient NeRF practices.

- **Large-scale quantitative evaluation on 62 challenging real-world scenes (Table 1, Fig. 3):** The filtering application improves PSNR on 58/62 scenes with an average gain of 0.6 dB. The ObjectScans benchmark spans 6 different environments with real-world challenges (motion blur, varied lighting, reflective materials, low texture). This is substantially larger and more diverse than typical NeRF artifact-removal evaluations.

- **Second downstream application demonstrating broader utility (Table 2, Sec. 4.2):** Beyond artifact removal, the paper shows that the visibility analysis can guide data acquisition — selecting 10 additional views via the proposed visibility index improves re-training quality over random selection across 6 datasets. This showcases the VPN as a general-purpose post-training analysis tool, not a one-trick filter.

- **Preliminary extension to inpainting (Fig. 5):** The paper provides a concrete example of using the visibility mask to guide NeRF inpainting with Stable Diffusion 2.0, suggesting broader applicability beyond the two main experiments.

## Weaknesses

### Fatal
None.

### Major

- **Filtering application lacks comparison against simpler baselines (Sec. 4.1).** The method resets σᵢ = 0 when τ(n_pred) < 0.9 and depth < 1, but never compares against a baseline that uses the NeRF's *own density* or *transmittance along the novel ray* to achieve similar filtering. For example, skipping near-range points with low density (σ < ε) or low accumulated transmittance would be a trivial, VPN-free baseline. Without this comparison, we cannot determine whether the VPN is necessary for the observed 0.6 dB gain, or whether a cheaper heuristic suffices. Since the VPN is the paper's core contribution, this is a significant evidential gap.

- **View selection experiment is underpowered and insufficiently controlled (Sec. 4.2, Table 2).** (a) Only 6 of 62 datasets are used, without justification for the subset. (b) The "random selection" baseline appears to be a single draw per dataset — no multiple random trials with variance reporting, so statistical significance cannot be assessed. (c) No comparison against alternative selection heuristics (e.g., farthest-point sampling of camera poses to maximize diversity), which would isolate whether the *visibility-specific* component of C_I adds value beyond pose diversity. The paper calls this a "proof-of-concept" (line 140), but the evidence is too thin to support the claimed superiority of visibility-based selection.

- **VPN prediction accuracy on unseen points is not validated (Sec. 3.1).** The VPN is trained on points sampled along training-view rays. The paper claims it predicts visibility of "any" point (abstract), but never evaluates prediction accuracy on a held-out set of points. A straightforward experiment — hold out a fraction of training views, compute ground-truth visibility for points along those views' rays using the pre-trained NeRF, and compare against VPN predictions (e.g., using classification metrics like precision/recall or AUC) — would directly validate this central claim. Without it, the reliability of VPN predictions in the regimes where it is actually used (novel-view rays) is an unverified assumption.

### Minor

- **Scoring function choices not ablated (Sec. 3, Eq. 4; Sec. 4.1).** The chain of transformations — ESS n_p → τ(n) bias-correction (Eq. 4) → threshold at 0.9 — uses specific functional forms without sensitivity analysis. While τ(n) is a known statistical function from bias correction for normal standard deviation estimation, the paper does not test whether simpler alternatives (e.g., using n_p directly, 1 − 1/n, a sigmoid) produce similar results, or whether the 0.9 threshold is robust (e.g., 0.7 or 0.95). This weakens confidence that the specific formulation is essential.

- **"Too close" distance in view selection rules not defined (Sec. 4.2).** Rules 1 and 2 state that views "too close" to existing/selected views are skipped, but no distance threshold is specified. This makes the view selection experiment difficult to reproduce exactly.

- **Runtime and memory overhead not reported (Sec. 3.1, 4).** The paper claims "small overheads" (line 15) but provides no numbers for VPN training time relative to base NeRF, rendering time with vs. without filtering, or memory cost of the FoV grid predictor (up to 128³ × K ≈ 100M floats). This information is needed for practitioners to assess the tool's practical deployability.

- **No analysis of failure cases by scene characteristics (Sec. 4.1, Fig. 3).** Four scenes show degradation. The paper does not analyze what properties these scenes share (e.g., textureless surfaces, specularity, sparse camera coverage), which would help practitioners understand when the method should or should not be applied.

### Trivial

- The FoV grid predictor resolution (64³ vs. 128³) is mentioned but no ablation or guidance is given on choosing between them (Sec. 3.1).
- Table 2 shows LPIPS/SSIM trends that are less consistent than PSNR (e.g., Dataset 6 shows SSIM drop with visibility-based selection), which is not discussed.

## Nice-to-Haves

- **Validate VPN accuracy directly** — hold out a small fraction of training views and compare VPN predictions against ground-truth visibility computed from the pre-trained NeRF for points along those views' rays.
- **Add sensitivity analysis** for the τ threshold (0.7, 0.8, 0.9, 0.95) and depth cutoff in the filtering heuristic.
- **Run multiple random trials** (≥5) for the view-selection baseline and report mean ± std.
- **Compare against a diversity-maximizing baseline** (e.g., farthest-point sampling of camera poses) for Task 2.
- **Report runtime/memory overhead and per-scene SSIM/LPIPS** scatter plots in addition to PSNR.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Criticism about dataset release status** ("The paper does not state whether ObjectScans will be made publicly available") — removed per hard rule: papers are not required to state release plans, and this speculates about future availability.
2. **Criticism about "1Ω²" as an unclear unit** — this is a PDF parser artifact; the original submission does not contain this garbled character. The underlying concern about the depth threshold value (1 unit) not being justified is retained in the scoring-function weakness above.
3. **Strength #4 from Strength Finder ("theoretically grounded scoring function")** — removed because it conflicts with a verified weakness (scoring function choices not ablated). The function τ(n) is a known statistical formula, but its application here is not empirically justified or ablated, so claiming theoretical groundedness as a strength is not warranted.
4. **Criticism about the introduction being "vague" / "hand-waving"** ("the statement 'this phenomenon is well understood from a machine learning perspective' is vague") — this is a presentation-style judgment, not a specific, verifiable weakness about the paper's claims or evidence.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs provide thorough coverage of the paper's strengths and gaps but do not synthesize any fundamentally new observation about the method beyond what was already present in the paper.

## Suggestions

1. **Add a direct comparison against a density-based baseline for Task 1.** For example, implement a variant that skips near-range points with σᵢ < ε (or points below a transmittance threshold along the novel ray) and report PSNR changes. If the VPN-free baseline matches the VPN's 0.6 dB gain, the paper's core claim is weakened; if the VPN significantly outperforms it, the contribution is strengthened. Either outcome would be informative.

2. **Validate VPN prediction accuracy directly** by holding out a small set of training views (e.g., 5%), computing ground-truth visibility v^(k)(p) for points sampled along those views' rays using the pre-trained NeRF, and comparing against VPN predictions using binary classification metrics (precision, recall, AUC). This would directly support the claim that the VPN generalizes to arbitrary points.

3. **Run multiple random trials** for the view-selection baseline (Task 2) and report mean ± std, enabling statistical comparison. Also include a diversity-maximizing heuristic as an additional baseline.

4. **Ablate the τ threshold** (e.g., 0.7, 0.8, 0.9, 0.95) and depth cutoff on a subset of ObjectScenes to show robustness. Similarly, test whether using n_p directly or a simple sigmoid mapping changes results.

5. **Report per-scene SSIM/LPIPS scatter plots** analogous to Fig. 3, and analyze the 4 degrading scenes to identify common failure characteristics.

6. **Report the "too close" distance threshold** used in Rules 1 and 2 (Sec. 4.2) and the runtime/memory overhead of VPN training and inference.
