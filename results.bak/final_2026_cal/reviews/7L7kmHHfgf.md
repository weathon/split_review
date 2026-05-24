Now I have sufficient anchors for calibration. Let me compile my final review.

**Calibration Summary:**
- **Round 1 bracket**: 5–7
  - Weak anchors (score < 3.5): FewGAD (3.0), TAGAD (3.0) — different domains, poorly scored.
  - Middle anchors (3.5–7.5): UIP-AD (4.0, Withdrawn) — highly topically similar (prototype-based MAD), but had missing ablations, citation errors, weak comparison control. PIRN is clearly stronger.
  - Strong anchors (7.5+): Unrelated topics (multimodal reasoning, text-to-3D) — not comparable.
- **Round 2 narrowing**: 
  - FoundAD (6.0, Poster): Few-shot AD with frozen foundation encoder. Clean, simple method. Scored 6, 8, 4. PIRN tackles a harder problem (multimodal) with more thorough evaluation. Slightly stronger than FoundAD.
  - ProMoS (5.5, Reject): Graph anomaly detection — different domain.
- **Round 3**: No topically relevant anchors in the 6–7.5 range for multimodal industrial AD.

**Final score**: 6.0. PIRN is stronger than UIP-AD (4.0) and somewhat stronger than FoundAD (6.0) in scope and thoroughness, but the backbone-concern and lack of variance reporting prevent a higher score.

Here is the consolidated review:

---

## Summary

This paper proposes **PIRN**, a prototype-driven intra-modal reconstruction framework for few-shot multimodal anomaly detection (MAD). It integrates three components: (1) **Balanced Prototype Assignment (BPA)**, which uses balanced optimal transport to prevent codebook collapse; (2) **Adaptive Prototype Refinement (APR)**, which dynamically updates prototypes at inference via a GRU to bridge the train-test distribution gap; and (3) **Multimodal Normality Communication (MNC)**, which exchanges high-level normal cues across RGB and surface-normal modalities. Experiments on MVTec-3D-AD, Eyecandies, and Real-IAD show consistent improvements over baselines in few-shot settings, with substantial efficiency gains over the SOTA method FIND.

## Strengths

- **Well-motivated and clearly articulated framework.** The paper identifies three concrete challenges in few-shot MAD (codebook collapse, static prototypes, lack of cross-modal communication) and designs one component per challenge. The architecture diagram (Fig. 2) and the flow from APR → BPA → MNC within each decoder layer are clearly presented and easy to follow.

- **Strong empirical results across multiple benchmarks and shot settings.** Table 1 shows consistent gains over all baselines on MVTec-3D-AD and Eyecandies at 5, 10, and 50 shots. The improvement over INP-Former (controlled with the same ViT-B/14 backbone) at 5-shot on MVTec-3D-AD (+3.9 AUROC_I) is the most meaningful comparison, as it isolates the contribution of PIRN's decoder design from the backbone.

- **Comprehensive ablation studies.** Tables 2, 3, 5, 6, and 7 systematically validate each design choice: the contribution of each module (BPA, APR, MNC), the optimal prototype count (K=10), decoder depth (L=2), and the superiority of balanced OT over alternative aggregation strategies in APR. Table 3 convincingly demonstrates that MNC's cross-modal communication provides clear additive value over single-modality variants.

- **Substantial computational efficiency.** Table 4 shows PIRN achieves the best AUROC_I (0.922) while requiring only 103.36G FLOPs and 17.49ms latency — 85% fewer FLOPs and 4.35× faster than FIND (728.46G, 76.09ms). This is practically significant for deployment.

- **Multi-benchmark validation including a challenging real-world dataset.** Beyond the standard MVTec-3D-AD and Eyecandies, the paper evaluates on Real-IAD D3, achieving the best overall anomaly localization (AUROC_P 0.961) in 13 out of 20 categories, despite using fewer modalities than the top-performing competitor D³M.

## Weaknesses

### Major

- **Backbone controlled for only one baseline.** The paper adapts INP-Former with the same ViT-B/14 DINOv2 backbone (a fair comparison). However, the other baselines (BTF, AST, M3DM, CFM, 3D-ADNAS) are not re-run with the same backbone, and their original implementations use different feature extractors (ResNets, smaller ViTs, etc.). Since DINOv2 ViT-B/14 is a very strong frozen encoder, a non-trivial fraction of the reported gains may come from the backbone rather than the proposed BPA/APR/MNC modules. The paper would benefit from either (a) re-running the most competitive baselines with the same DINOv2 backbone, or (b) including a simple ablation baseline — DINOv2 encoder + a basic reconstruction loss (no prototypes, no cross-modal communication) — to quantify the added value of PIRN's decoder design.

- **No variance reporting for few-shot results.** Few-shot (5, 10, 50-shot) experiments are inherently high-variance due to which specific normal samples are drawn. The paper reports only point estimates (AUROC, AUPRO) without standard deviations, confidence intervals, or multi-seed trials. For example, the +3.9 AUROC_I gain at 5-shot could fall within the noise range of a different sample selection. Reporting mean±std over 3–5 random seeds would substantially strengthen the paper's central claims.

### Minor

- **APR's robustness to large or full-image anomalies is not empirically validated.** The paper argues that anomalous tokens contribute weakly to prototype updates because they are "diffusely assigned" by the OT plan. This is theoretically plausible, but no controlled experiment (e.g., injecting synthetic anomalies of varying sizes) verifies that prototype codebook corruption does not occur when a large region — or the entire image — is anomalous. A brief experiment would increase confidence in APR's safety.

- **Failure modes on Real-IAD are not discussed.** On certain Real-IAD categories (e.g., `miniature_filling_sensor` with 0.604 AUROC_J, `frontline_head` with 0.717 AUROC_J), PIRN underperforms multiple baselines. The paper does not analyze why the method fails on these categories. A brief discussion of failure modes would improve credibility.

- **Component contribution table (Table 2) has a formatting issue and a typo.** The column header reads "BFA" instead of "BPA," and all rows display the same checkmark pattern, which is inconsistent with the caption ("the baseline model (first row) excludes all proposed modules"). While likely a parser artifact, this needs clarification.

### Trivial

- The claim of being "the first multimodal AD framework to integrate a vector-quantized prototype codebook into a ViT encoder-decoder" is narrow enough to be accurate but could be toned down to focus on the few-shot regime as the primary novelty.

## Nice-to-Haves

- Ablation on prototype count K in the few-shot setting (Table 5 ablates only in the all-shot setting; the optimal K may differ under 5 or 10 shots).
- Simple two-stream reconstruction baseline (DINOv2 encoder + element-wise cosine reconstruction loss, no prototypes) to further isolate the backbone effect.
- KL divergence or AUC of normal/anomaly score distributions to quantify the "clearer separation" shown qualitatively in Fig. 3.
- Discussion of why PIRN struggles on specific Real-IAD categories.

## Removed Points

The following points from the reviewers were assessed and removed:

1. **"Missing code release or reproducibility statement"** (Harsh Critic) — Removed per Hard Rules: questioning the availability of artifacts cited in the paper. The paper references code, models, and datasets that are assumed to exist.
2. **"Overclaimed 'first' claim"** (Harsh Critic) — Removed. The claim is "first multimodal AD framework to integrate VQ codebook into ViT encoder-decoder," which is specific and verifiable. INP-Former does this for 2D AD only, so the multimodal extension is not simply incremental.
3. **"Missing baseline: simple two-stream reconstruction"** (Harsh Critic) — Partially kept as a Nice-to-Have, not a weakness.
4. **"K=10 justification"** and **"statistical significance test for K"** (Harsh Critic) — Demoted to Removed. The paper provides ablation on K (Table 5) showing the trend, which is sufficient for an empirical paper.
5. **"Gating mechanism in MNC uses a single scalar, limiting expressiveness"** (Harsh Critic) — Removed. This is speculation without evidence that a vector gate would improve performance.
6. **"2D INP-Former adaptation details are sparse"** (Harsh Critic) — Removed. The paper states both branches use the same ViT-B/14 backbone and input resolution, with element-wise fusion. This is sufficient for reproducibility.
7. **"Qualitative analysis not quantified"** (Harsh Critic) — Demoted to Nice-to-Have. The qualitative figures are illustrative and the paper makes no quantitative claim from them.
8. **"FIND efficiency comparison feels tangential"** (Harsh Critic) — Removed. The efficiency comparison is relevant to show practical advantages.
9. **"Missing ablation: frozen vs. trainable backbone"** (Harsh Critic) — Demoted to Nice-to-Have. The paper uses a frozen encoder following standard practice in this field.
10. **Numerous strength-finder strengths about "the problem being important"** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate the paper's claims rather than offering novel cross-cutting observations.

## Suggestions

1. **Controlled backbone comparison**: Add a simple baseline: DINOv2 encoder + a lightweight reconstruction head (no prototypes, no cross-modal communication) trained with the same loss. This would isolate the value of BPA/APR/MNC from the backbone.
2. **Multi-seed variance reporting**: Report mean±std over 3–5 random seeds for all few-shot results. This is especially important for the 5-shot setting where sample selection variance is highest.
3. **APR robustness experiment**: Construct a test with synthetic anomalies covering 25%, 50%, 75%, 100% of the image and compare APR vs. a naive averaging baseline to demonstrate that OT-based filtering prevents prototype corruption.
4. **Fix Table 2 formatting**: Ensure the checkmark pattern correctly reflects which modules are enabled per row, and correct "BFA" → "BPA."
5. **Failure case analysis**: Include a brief discussion of why PIRN underperforms on specific Real-IAD categories (e.g., `miniature_filling_sensor`).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>