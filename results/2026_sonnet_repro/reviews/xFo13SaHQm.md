Now let me run the bracketing calibration search.Now I have sufficient calibration data. Let me write the final review.

**Round 1 Bracket:** Based on the topically similar anchors (DreamBench++, Vec2Face, MS-Diffusion all at 6.0; EngagingImageNet at 6.75), I bracket this paper at **6.0–7.0**.

**Round 2 Narrowing:** WithAnyone is clearly stronger than MS-Diffusion (6.0) — it adds a large-scale dataset and formal benchmark on top of a method. It's stronger than DreamBench++ (6.0) which is benchmark-only. It's comparable to EngagingImageNet (6.75) in the dataset+model+benchmark structure, but more technically rigorous in its metric formulation and ablation. This places the paper around **6.5**.

---

## Summary

WithAnyone is a three-contribution paper: it introduces **MultiID-2M**, a large-scale dataset of 500k group photos with paired per-identity references; **MultiID-Bench**, a benchmark centered on the novel copy-paste (M_CP) metric that measures whether a generated face is anomalously close to the reference relative to the ground truth; and **WithAnyone**, a FLUX-based identity-customization model that employs GT-aligned ID loss, InfoNCE contrastive training with 4096 negatives, and a paired-tuning phase to break the previously universal trade-off between identity fidelity and copy-paste artifacts. The paper's most durable conceptual contribution is the insight that Sim(Ref) rewards trivial duplication, while Sim(GT) provides a fairer target — and that these two failure modes can be separated.

---

## Strengths

- **Novel and formally grounded M_CP metric** (Eq. 2): The angular-normalized copy-paste metric is mathematically clean and its motivation is well-articulated — using Sim(Ref) as the primary metric inadvertently rewards literal copying, while Sim(GT) penalizes it. The benchmark reveals a clear trade-off curve across all 12–14 evaluated baselines (Figure 5), validating M_CP's diagnostic value.

- **Large-scale paired dataset** (Section 3): MultiID-2M provides ~500k group photos with matched per-identity reference images across diverse poses, expressions, and hairstyles (~25k identities). This directly enables paired training strategies that are unavailable from prior datasets and is a genuine community resource.

- **GT-aligned ID loss** (Eq. 4, Figure 7): Aligning generated images using GT landmarks rather than noisy predicted landmarks enables reliable identity supervision at all noise levels (t ∈ [0, 1]). Figure 7 shows GT-Align consistently achieves lower ID loss and more informative gradient variance across all tested noise levels (0.2–0.8), a clear technical improvement over PortraitBooth (loss only at t < 0.25) and PuLID (expensive full denoising).

- **Contrastive loss with extended negatives** (Eq. 5, Table 3): Expanding the InfoNCE negative pool from 63 batch samples to 4096 identity-labeled images significantly improves identity discrimination: removing extended negatives drops Sim(GT) from 0.405 to 0.368 and nearly eliminates the CP reduction benefit.

- **Strong quantitative results on single-ID benchmark** (Table 1a, Figure 5a): WithAnyone achieves the highest Sim(GT) (0.460) with the second-lowest CP (0.144) among all 15 evaluated methods — including both face-customization specialists and powerful general VLMs. It is the only method that clearly breaks the regression curve observed across all competitors.

- **Comprehensive ablation** (Table 3): All four key components (Phase 3 paired tuning, GT-aligned ID loss, extended negatives, dataset quality) are ablated, with each contributing meaningfully and interpretably to the final performance.

---

## Weaknesses

### Fatal
None.

### Major

- **Co-design of training objective and primary evaluation metric**: Phase 3 (paired tuning) explicitly trains on paired instances where reference and target are different images of the same identity — this is precisely the condition on which M_CP is non-trivial and informative. The model is optimized to succeed on the exact situation the benchmark is designed to measure. While this is methodologically standard (identify a failure mode, design a method to address it, measure that failure mode), it means the benchmark results do not constitute fully independent validation. The OmniContext results (Table 1b) offer some independence, but they measure general prompt fidelity and scene correspondence rather than copy-paste specifically. This is an evidential limitation: the degree to which the method breaks the trade-off may be somewhat inflated by the aligned design choices, and the claims would be stronger with an independently constructed hold-out benchmark.

### Minor

- **Sim(GT) improvement is largely driven by copy-paste reduction, not cleaner identity preservation**: Table 3 shows that removing Phase 3 changes Sim(GT) by only 0.001 (0.406 → 0.405), while raising CP by 0.078 (0.239 → 0.161). This confirms that Phase 3's main contribution is CP reduction, not identity fidelity improvement. The paper accurately frames this as "maintaining state-of-the-art identity similarity while reducing copy-paste" (consistent with the ablation), but the abstract and introduction sometimes imply a broader identity-fidelity improvement that the ablation does not support.

- **Multi-ID results are less decisive than single-ID** (Table 2b): In the 3–4 person subset, DreamID achieves CP = 0.116 vs. WithAnyone's 0.171, albeit at lower Sim(GT) (0.311 vs. 0.414). The scatter plot (Figure 5b) still shows WithAnyone above the trade-off curve but less dramatically than in Figure 5a. The paper's "breaking the trade-off" claim is cleanest for single-ID; the multi-ID version deserves more careful discussion.

- **User study sample size**: Section 6.3 states "Ten participants were recruited." A ranking-based perceptual study with n = 10 evaluators across 230 image groups is underpowered. The paper notes statistical details are in Appendix H (stripped), but the main text should at minimum report a significance measure (e.g., Kendall's τ, inter-rater agreement).

- **M_CP metric stability near degenerate cases**: When the reference and ground truth are very similar (θ_tr ≈ 0), the denominator falls to ε and small numerator variations produce large M_CP swings. The Table 1 footnote applies an ad hoc Sim(GT) > 0.40 filter for CP ranking, but no sensitivity analysis of this threshold is provided. If WithAnyone systematically scores well on high-θ_tr cases (precisely the cases where paired training helps most), the CP ranking could be favorable by design.

### Trivial

- **BU (identity blending) metric is used in Table 2 but not defined in the main text**: Section 4 defers its definition to Appendix D. Since BU is Table 2's fourth column and is conceptually important for multi-ID generation (distinguishing identity confusion from identity preservation), at minimum a one-sentence informal definition should appear in the main text alongside the formal Sim(GT) and M_CP definitions.

---

## Nice-to-Haves

- A controlled decomposition of Sim(GT) cases would strengthen the paper substantially: for test cases where the GT prompt specifies a pose/expression change vs. cases where it does not, measuring whether WithAnyone's advantage concentrates in the former group would disentangle "better prompt-following" from "better identity preservation" and directly address the conflation concern.
- An analysis of M_CP as a function of θ_tr across benchmark cases would reveal whether WithAnyone's advantage is specifically in high-appearance-divergence cases (the theoretically correct behavior) and strengthen the sensitivity claim for the 0.40 CP-ranking threshold.
- The general-VLM gap on OmniContext (GPT-4o: 8.12, OmniGen2: 8.34 vs. WithAnyone: 6.52) deserves a brief discussion of what it implies for the long-term framing of face-customization as a distinct capability category.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Training–benchmark identity overlap** (Harsh Critic, Section 4): The paper explicitly states "no overlap to training data" and notes the verification procedure is in Appendix C. Per the hard rule, criticism of content in stripped appendices is not valid.
- **Appendix-deferred proofs and definitions** (BU in Appendix D, overlap in Appendix C, statistical analysis in Appendix H): The parser strips appendices; these are not absent from the submission.
- **DynamicID excluded from baselines** (Section 6, footnote 1): The paper explicitly notes "Excluded from our experiments due to unavailability of code and pretrained models." This is a valid exclusion reason; per the hard rule, questioning whether cited models exist or are available is not permitted.
- **Formatting artifacts in Table 2 and Table 3**: The apparent column alignment issues and merged row labels ("0.385 w/o GT-Align") are parser artifacts. The original submission does not have these issues.

---

## Novel Insights

The paper's most durable insight is the formal separation of *identity similarity to reference* (Sim(Ref)) from *identity similarity to ground truth* (Sim(GT)) as evaluation targets, and the rigorous demonstration that existing metrics inadvertently reward copy-paste. The M_CP metric operationalizes this distinction in a principled way (angular normalization by the reference–GT divergence). The ablation result that paired tuning primarily reduces CP without changing Sim(GT) (Δ = 0.001) is itself a meaningful finding: it shows that reducing copy-paste and improving identity fidelity are somewhat orthogonal objectives, and that the paper's method specifically addresses the former rather than naively claiming to improve both equally. This has implications for how future work should design and interpret identity-consistency metrics.

---

## Suggestions

- Add a one-sentence informal definition of BU (identity blending) in Section 4 before referring to it in Table 2.
- Include a brief sensitivity analysis of the Sim(GT) > 0.40 CP-ranking threshold (even just checking whether rankings change materially at 0.35 or 0.45) to establish robustness.
- Report the user study's inter-rater agreement or Kendall's τ in the main text alongside sample size.
- Add a decomposed analysis of Sim(GT) improvements by whether GT prompts specify appearance changes — this is the single most impactful addition that would directly validate the core claim about controllability.
- Soften the abstract's framing slightly to better align with what the ablation shows: the method primarily *reduces copy-paste while maintaining* identity fidelity rather than simultaneously improving both.

---

## Score and Decision

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NWvsm2VxAM (ID-Booth) | 3.0 | R1 | Rejected; weak method-only paper with no dataset/benchmark |
| 4GSOESJrk6 (DreamBench++) | 6.0 | R1 | Benchmark-only for personalized generation; WithAnyone adds dataset + model |
| RoN6NnHjn4 (Vec2Face) | 6.0 | R1/R2 | Face dataset + model for recognition; similar scale of contribution |
| 88Qm4fGWzX (Event-Customized) | 5.0 | R1 | Rejected; smaller contribution |
| PJqP0wyQek (MS-Diffusion) | 6.0 | R2 | Multi-subject personalization method without dataset/benchmark; WithAnyone clearly stronger |
| riieAeQBJm (UIFace) | 6.0 | R2 | Face recognition dataset generation; narrower contribution |
| ePOjNlOjLC (Diffusion in Diffusion) | 6.25 | R2 | Customization method only; comparable |
| TmCcNuo03f (EngagingImageNet) | 6.75 | R2 | Dataset + model + benchmark; similar structure, WithAnyone more technically rigorous |
| jZsN9zo8Qi (MEGA-like IITC) | 6.5 | R2 | Dataset + benchmark + model for VLMs; broadly comparable structure |

**Round 1 bracket: 6.0–7.0.**

**Round 2 narrowing:** WithAnyone is clearly above the 6.0 cluster (more comprehensive than any single-contribution paper at that level; MS-Diffusion, DreamBench++, Vec2Face all lack one or more of its three contributions). It sits around EngagingImageNet (6.75) in scope, but is more technically sound in metric formulation and ablation rigor. The major weakness (co-design of metric and training) prevents a score of 7.0+. Final score: **6.5**.

**Originality:** High — the M_CP metric and the Sim(GT)-vs-Sim(Ref) distinction are novel and will likely be adopted by subsequent work.  
**Importance:** Moderate-to-high — copy-paste artifacts are a widely-observed failure mode; quantifying and targeting them directly is practically valuable.  
**Claim support:** Good for single-ID; moderate for multi-ID; the ablation is clean and validates all components.  
**Experimental soundness:** Good; the 10-person user study is the weakest link.  
**Clarity:** Good overall; the BU metric omission and the subtle conflation in Sim(GT) framing are the main issues.  
**Community value:** High — open-sourced dataset, benchmark, and model benefit the entire ID-customization research community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>