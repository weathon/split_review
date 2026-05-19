Now let me run calibration searches to anchor the score.Let me read a couple of the mid-range anchor papers to establish a clearer bracket.Initial bracket: **5.5–7.0**. Real3D is better than GTR in novelty (new training paradigm, not just architecture) and has cleaner ablations. Let me narrow within this range.Now I have sufficient information to write the final review. Let me also check the exact WILD dataset table to verify the FID number cited by the harsh critic.

Based on my paper reading, I can confirm:
- Table 2 (WILD) shows TripoSR FID 128.5 → Real3D 106.5 ✓
- Training data (WILD3D) includes MVImageNet images (line 175) ✓
- Section 3.2 on data curation is exactly 2 sentences ✓  
- Ablation Table 4 shows 18.60 for clean data (slightly below 18.63 raw) ✓
- The "seemingly endless" language appears in the Conclusion ✓

---

## Summary

Real3D proposes the first Large Reconstruction Model (LRM) framework that can be trained using single-view in-the-wild images, removing the dependency on multi-view supervision. The method introduces two unsupervised self-training losses—a cycle-consistency rendering loss with stop-gradient and curriculum learning, and a CLIP-based semantic loss with hard-negative mining—together with an automatic data curation pipeline that filters 3M to 300K high-quality unoccluded instances. Experiments across four diverse benchmarks show consistent ~0.74 PSNR improvements over TripoSR, with gains exceeding those of LRM* which uses multi-view real data, supporting the paper's claim that single-view self-training is a superior use of real-world data for scaling LRMs.

---

## Strengths

- **Novel self-training framework enabling LRM training on single-view real images**: The cycle-consistency loss (Eqs. 1–4) with stop-gradient and progressive curriculum, and the CLIP semantic loss with hard-negative mining (Eqs. 5–7), are both specifically designed for the absence of ground-truth novel views. The ablation (Table 4) shows that each component contributes meaningfully: properly-applied semantic guidance (row 2: 18.81 vs. naive 17.89 PSNR), stop-gradient (row 3: 19.18 vs. 17.78 end-to-end), and curriculum learning (row 3: 19.18 vs. 18.63 without curriculum).

- **Consistent out-of-domain improvements with clean evaluation**: Tables 3 and 4 report standard NVS metrics against held-out ground-truth novel views on CO3D and OmniObject3D—datasets not in training. Real3D gains +0.74 PSNR over TripoSR on both, while the comparable LRM* (trained with multi-view real data) gains only +0.51 and +0.33 PSNR respectively. This is the paper's most compelling evidence: single-view self-training is more effective than multi-view supervised training on real data.

- **Δours vs. ΔLRM* comparison as a genuinely novel finding**: The paper demonstrates that training on single-view real images via self-training surpasses adding multi-view supervised real data (LRM*) across all four evaluation settings. For example, in Table 1 (MVImageNet), Δours = +2.08 PSNR (Self-Consistency) vs. ΔLRM* = +1.28. This is a practically significant finding for the 3D reconstruction field's data collection strategy.

- **Empirical scalability evidence**: Figure 5 shows monotonically increasing performance as more real images are added to training (up to ~300K images), supporting the claim that the method can benefit from further scaling.

---

## Weaknesses

### Fatal
None.

### Major

- **Metric circularity on the WILD test set (Table 2)**: The paper's WILD evaluation has no ground-truth novel views, so all reported metrics in Table 2 are custom proxy metrics: "Semantic Similarity" (CLIP, LPIPS, FID between rendered novel views and the input) and "Self-Consistency" (cycle-consistency round-trip to original viewpoint). Structurally, these are functionally identical to the two proposed training objectives $\mathcal{L}^R_\text{sem}$ and $\mathcal{L}^R_\text{pix}$. The headline result in Table 2—FID dropping from 128.5 (TripoSR) to 106.5 (Real3D), a 17% relative gain—is essentially measuring the objective that Real3D is trained to optimize. This does not invalidate the paper's contribution (the out-of-domain NVS results in Tables 3 and 4 remain clean and independent), but the paper presents Table 2 prominently and draws on it to substantiate broad generalization claims. The text at line 298 says "Results in Table 2 also highlight the advantage of our self-training method by using a broader data distribution," which overstates what Table 2 can legitimately support.

- **MVImageNet domain overlap between training and evaluation**: WILD3D is collected from "a set of datasets from diverse domains" including MVImageNet (Section 3, "Datasets", line 175). MVImageNet is also used as the benchmark in Table 1, which the paper labels as "in-domain." Because the model has been trained on single-view images drawn from MVImageNet, improvements in Table 1 cannot be cleanly attributed to general 3D reconstruction improvement versus domain-specific adaptation. The paper does not acknowledge or discuss this confound. The partially independent evidence from CO3D and OmniObject3D (Tables 3–4) mitigates but does not eliminate the concern.

### Minor

- **Data curation method lacks sufficient description in the main body**: Section 3.2 describes the curation pipeline in two sentences (lines 165–167)—stating that unoccluded instances are selected via "the synergy between instance segmentation and single-view depth estimation"—without specifying the segmentation model, depth model, the decision rule, or any failure analysis. Given that the 90% rejection rate (3M → 300K) is central to the self-training performance (ablation row: clean data contributes to reaching 19.18 vs. 18.79 PSNR), the curation is a meaningful component and deserves more detail in the main paper, even if an appendix exists.

- **Minor inconsistency in data quality ablation worth acknowledging**: In Table 4 row (1), adding clean data (18.60 PSNR) versus raw data (18.63 PSNR) shows a slight decrease within noise. The paper does not comment on this. While statistically negligible, it slightly weakens the standalone narrative about data quality being essential—the gains from clean data only become clear once the cycle-consistency loss is also active. The paper's claim that data curation improves performance would be more precisely stated as: *curation is necessary for the cycle-consistency loss to work properly*.

### Trivial

- The conclusion uses "seemingly endless" (line 378) to describe the data scaling potential, which is speculative extrapolation from a single benchmark curve covering up to ~300K images. The scaling analysis would be stronger with even a brief discussion of expected diminishing returns.

---

## Nice-to-Haves

- Providing human perceptual evaluation (e.g., preference study) for the WILD test set would give Table 2 independent validation, since standard NVS metrics are unavailable there. Without ground truth, a human study is the natural alternative.
- An analysis of what geometric properties cycle-consistency training induces—beyond NVS metrics—would sharpen the paper's geometric contribution. A shape-level evaluation (Chamfer distance) on the subset of benchmarks with ground-truth meshes would distinguish photometric consistency from actual 3D accuracy.
- A brief investigation into whether combining multi-view real data (LRM*) with the proposed self-training losses yields further improvements would directly address the paper's main thesis about data collection strategy.
- The curriculum learning schedule (from 15° to 90° azimuth over training) is clearly described, but the sensitivity to the specific parameters ($\theta_\text{min}, \theta_\text{max}$, etc.) is not ablated. Even a brief comment on robustness would strengthen this component.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Ablation inconsistency (18.60 < 18.63) undercuts the data quality narrative (Major)"**: Retained as Minor only. The difference is within noise and the paper's overall ablation structure is sound—the practical claim that clean data is needed for cycle-consistency to work is supported. Elevating this to Major misrepresents the severity.
- **Harsh Critic: "Scalability to 'seemingly endless' data (Fatal/Major)"**: Demoted to Trivial. The scaling curve is indeed limited to one benchmark and one scale range, but the conclusion's "seemingly endless" phrasing is a standard rhetorical claim in this literature rather than a falsified empirical statement. The scaling evidence within the paper is genuine.
- **Strength Finder: "Data curation is well-described as a strength"**: Removed. The ablation does support that clean data matters, but the curation method itself is a weakness in description (2 sentences). The claimed strength does not survive the verified weakness.
- **Harsh Critic: "Semantic loss self-reinforcing because CLIP is both training guidance and evaluation metric"**: The paper does acknowledge CLIP "lacks spatial awareness" (line 60), but the deeper issue—that CLIP-based evaluation metrics and CLIP-based training loss are self-reinforcing—is a valid framing of the metric circularity weakness. This is merged into the Major weakness on WILD evaluation circularity rather than kept as a separate point.

---

## Novel Insights

The most genuinely novel finding in this paper is the empirical comparison between single-view self-training (Δours) and multi-view supervised training (ΔLRM\*) across four diverse evaluation settings. The consistent pattern—single-view self-training outperforms multi-view supervised real-data augmentation—challenges the implicit assumption in the 3D reconstruction field that more supervision is always better. The paper suggests that the domain gap introduced by the normalization requirements of multi-view real-world capture pipelines may actually impede generalization more than the lack of explicit supervision does. This observation, if confirmed in larger-scale studies, has meaningful implications for how training data should be prioritized in future LRM development.

---

## Suggestions

1. **Restructure the presentation of Table 2 to clarify what it does and does not prove**: Explicitly note that WILD metrics are proxy measures aligned with training objectives, not independent validation. Move the strongest evidence (Δours vs. ΔLRM\* comparison across Tables 3–4) to the front of the discussion.
2. **Expand Section 3.2** with at least the key specifics: which segmentation and depth estimation models are used, the decision rule for occlusion detection, and the approximate false positive/negative rates. This is needed for reproducibility of a component the paper presents as a contribution.
3. **Acknowledge the MVImageNet overlap** in the experimental setup. Even a single sentence noting that WILD3D training images include MVImageNet samples—and that CO3D/OmniObject3D results are therefore the cleanest generalization benchmarks—would preempt reviewer concern.
4. **Reframe the ablation discussion** to clarify that clean data's benefit is conditioned on the cycle-consistency loss being present, not unconditional.

---

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Scaled Inverse Graphics | GSckuQMzBG.md | 3.00 | R1 | Much weaker; lacks clear contribution and consistent results |
| Self-Evolving NeRF | TW0MVSflg5.md | 4.75 | R1 | Thematically related (self-training NeRF) but per-scene optimization setting, lower impact |
| Long-LRM | meOELl7HRf.md | 5.33 | R1 | LRM extension, rejected; less novel problem formulation than Real3D |
| GTR | Oxpkn0YLG1.md | 5.60 | R1/R2 | Accepted; architecture-focused LRM improvement, more limited novelty than Real3D |
| MeshLRM | R1rNN22IoP.md | 6.25 | R2 | Rejected; LRM-to-mesh extension, comparable ambition but missing key baselines and limited novelty |
| PRM | AkL2ID5rRV.md | 6.25 | R1/R2 | Rejected; novel LRM training paradigm but with writing and evaluation gaps |
| STORM | M2NFWRPMUd.md | 6.50 | R2 | Accepted; extends LRM to dynamic outdoor scenes, good novelty with some clarity gaps |
| Cycle Consistency Object Discovery | f1xnBr4WD6.md | 6.75 | R2 | Accepted; uses cycle consistency for 3D, comparable technical depth |
| NoPoSplat | P4o9akekdf.md | 8.00 | R1 | Accepted; stronger technical contribution, unposed multi-view reconstruction |

**Round 1 bracket:** 5.5–7.0. Real3D is clearly above GTR (5.60) in novelty (new training paradigm vs. architecture tweaks), and above the low-middle band.

**Round 2 narrowing:** Real3D vs. STORM (6.50, accepted): Both are accepted-tier LRM papers extending reconstruction to new data regimes. STORM has more novel technical scope (dynamic outdoor), but also larger clarity gaps in its methodology. Real3D is more focused but has genuine Major weaknesses (metric circularity, domain overlap). Real3D vs. PRM/MeshLRM (both 6.25, rejected): Real3D's core contribution is more impactful (enabling in-the-wild training vs. photometric stereo or mesh extraction). Real3D has cleaner evaluation on out-of-domain data and a better-supported central claim.

**Positioning:** Real3D sits at or slightly above STORM (6.50). The core contribution is genuinely novel and well-supported by clean out-of-domain experiments. The Major weaknesses (metric circularity on WILD, domain overlap) are real but do not undermine the central finding. The data curation underdescription is a Minor concern given likely appendix elaboration. I place the paper at **6.5**.

**Axis assessment:**
- *Originality*: High — first LRM trained on single-view real images, novel self-training framework.
- *Importance of research question*: High — data scaling bottleneck for LRMs is a recognized, important problem.
- *Claims well supported*: Partially — out-of-domain results (CO3D, OmniObject3D) are strong and clean; WILD evaluation is compromised by metric circularity.
- *Soundness of experiments*: Good overall, with a well-structured ablation; weakened by MVImageNet overlap concern.
- *Clarity of writing*: Adequate; data curation section is underdescribed.
- *Value to research community*: Good — the Δours > ΔLRM\* finding has broader implications for data collection strategy in 3D reconstruction.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>