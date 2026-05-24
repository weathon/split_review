Now I have a solid calibration basis. Let me synthesize my final review.

**Round 1 bracket:** 4.5 – 7.0 (the paper is stronger than SG-Adapter at 5.50 but has experimental confounds that keep it below the 7+ range).

**Round 2 narrowing:** The SG-Adapter anchor (5.50, Reject) is the most directly comparable but clearly weaker (309-image dataset vs 540K). SlotAdapt (6.25, Accept), Davidsonian SG (6.00, Accept), and Hydra-SGG (6.33, Accept) are similar-caliber papers. The current paper sits between 5.50 and 6.25 — its dataset contribution is substantial and the within-SG-model controlled comparisons are solid, but the missing text-only fine-tuning baseline and evaluation circularity are real weaknesses. Placing it at **6.0**.

---

## Summary

This paper introduces LAION-Comp, a 540K-image dataset with scene graph annotations (objects, attributes, relations) built by prompting GPT-4o on LAION-Aesthetics V2 images. Alongside the dataset, the authors train four SG-conditioned baselines (SDXL-SG, SD1.5-SG, SD3.5-SG, FLUX-SG) using a GNN-based scene graph encoder, and introduce CompSGen Bench, a 20,838-sample benchmark for evaluating complex multi-object generation. The key evidence is that SG-conditioned models trained on LAION-Comp outperform the same models trained on COCO-Stuff and Visual Genome across SG-IoU, Entity-IoU, and Relation-IoU.

## Strengths

- **Large-scale, verified scene graph dataset.** LAION-Comp provides 540K+ images with structured annotations — an order of magnitude larger than existing SG datasets (COCO-Stuff, Visual Genome). The annotation pipeline uses GPT-4o with careful prompt engineering, and partial human verification (300 samples) reports 98.8% object, 97.5% attribute, and 95.7% relation accuracy (Sec. 3.1, Table 1). No prior SG dataset achieves this scale with verified annotations.

- **Controlled within-model comparison shows dataset quality advantage.** Table 2 demonstrates that the same SDXL-SG model trained on LAION-Comp achieves higher SG-IoU (0.558 vs 0.497/0.546), Entity-IoU (0.884 vs 0.842/0.813), and Relation-IoU (0.856 vs 0.833/0.800) than when trained on COCO or Visual Genome. This comparison is properly controlled — same architecture, same training procedure, only the training dataset varies — and directly attributes the gains to LAION-Comp's annotation quality and scale.

- **Monotonic improvement with data scale.** The ablation (Table 4) shows consistent gains from 10% to 100% of LAION-Comp data: SG-IoU rises from 0.530 to 0.558, Entity-IoU from 0.874 to 0.884, Relation-IoU from 0.837 to 0.856. Notably, even at 10% scale (smaller than VG), the model already matches or exceeds VG-trained performance, indicating annotation quality matters beyond raw volume.

- **Diverse, non-spatial relation coverage.** LAION-Comp's relation distribution is dominated by non-spatial relations (77.48%) like "holding," "wearing," "supporting," in contrast to Visual Genome's spatial skew (58.02% spatial). This targets precisely the interaction types where T2I models struggle most (as noted in T2I-CompBench and MMRel).

- **Multi-backbone adaptation.** The SG encoder is successfully integrated across diffusion (SDXL, SD1.5) and flow-matching (SD3.5, FLUX) backbones, showing the structural annotations' benefits transfer across fundamentally different generative frameworks.

## Weaknesses

### Major

- **Missing text-only fine-tuning control baseline.** The paper's headline comparisons pit SG-conditioned models (*fine-tuned* on LAION-Comp) against off-the-shelf T2I models (*not* fine-tuned on the same data, Table 2, Table 3). This confounds two variables: (1) the structured conditioning itself, and (2) additional training on the LAION-Aesthetics image distribution. The claim in the abstract that models "outperform their original prompt-only counterparts" cannot be attributed to structured conditioning without a controlled experiment that fine-tunes the same backbones on LAION-Comp using text-only conditioning (serialized scene graphs or original captions) for the same number of steps. This does not invalidate the paper's core dataset contribution — the controlled within-model comparisons (LAION-Comp vs COCO vs VG in Table 2) are properly designed — but it weakens the claim that structured annotations per se are what drive the improvement over text-only models.

- **CompSGen Bench ground truth shares annotation pipeline.** The CompSGen benchmark (20,838 samples) uses ground-truth scene graphs from the same GPT-4o pipeline that generated the training annotations. The SG-IoU/Entity-IoU/Relation-IoU metrics therefore reward reproducing the GPT-4o annotation style rather than necessarily reflecting true visual composition accuracy. The paper partially mitigates this with T2I-CompBench results (Appendix A.6), COCO evaluation (CLIP scores), and a user study (Appendix A.3), but these are deferred to the appendix and the main paper's primary evaluation remains on the self-constructed benchmark.

### Minor

- **Annotation accuracy substantiation is thin in the main text.** The claimed 98.8%/97.5%/95.7% accuracies are supported only by a brief mention of "partial human verification" on 300 samples (Table 1). The human verification protocol, inter-annotator agreement, and sample selection criteria are relegated to the stripped appendix (Sec. A.5). While the appendix likely contains these details, the main text provides insufficient evidence to fully trust these high numbers given known GPT-4o hallucination issues.

- **Statistical significance/variance not reported.** Quantitative results in Tables 2–4 lack confidence intervals or standard deviations across runs. Given that some differences (e.g., Entity-IoU 0.884 vs 0.813 for VG) are large, this is not a fatal issue, but it limits the reader's ability to assess result stability.

- **No out-of-distribution generalization experiment.** The paper evaluates LAION-Comp-trained models on LAION-Comp's test set and on T2I-CompBench, but does not test whether these models generalize to COCO or VG test sets (which have different image distributions). Such a test would be a stronger signal of the dataset's generalization benefits.

### Trivial

- The paper claims "first to propose a compositional generation benchmark based on scene graphs" (§2, line 177) — a slight overstatement given that existing SG2IM works evaluate on COCO-Stuff and VG, though these are not specifically designed as compositional generation benchmarks.

## Nice-to-Haves

- A text-only fine-tuning baseline on LAION-Comp (serialized SG → text prompt) would cleanly isolate the effect of structured conditioning vs. additional training on the dataset. This is the single most impactful addition to strengthen the paper's claims.
- Human evaluation of generated images (pairwise preference between SG-conditioned and text-only fine-tuned models) would break the circularity concern with CompSGen Bench.
- Reporting standard deviations across multiple training runs would strengthen the quantitative evidence.

## Removed Points

Strengths marked as removed: None.

Weaknesses marked as removed:
- *"The paper does not compare LAION-Comp to contemporaneous annotation efforts like SPRIGHT/Chen et al. 2024b"* — The paper does briefly mention both (Sec. 2, lines 161-168). A detailed comparison is a nice-to-have, not a weakness.
- *"Method details deferred to appendix"* — Standard practice for long papers with page limits. The main paper gives the core design; the appendix provides details.
- *"Editing framework not in main text"* — The paper explicitly states the editing framework is introduced in Sec. A.1 due to space limits and mentions qualitative and quantitative experiments. This is scope-appropriate.
- *"No limitations section"* — A fine suggestion but not a weakness. Most conference papers do not require a separate limitations section.
- *"Overclaiming novelty in §1"* — The paper's claim about being the first SG-based compositional generation benchmark is arguable but not incorrect; existing datasets were not designed as compositional generation evaluation benchmarks.
- *"Annotation accuracy is too high to believe"* — This is a speculation about the numbers rather than a verified error. The paper reports partial human verification with a sample size and the appendix presumably contains the protocol. Demoted from unresolved suspicion to Minor.
- Generic formatting/presentation nitpicks: removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a text-only fine-tuning baseline.** Fine-tune SDXL and FLUX on LAION-Comp using the scene graph serialized as natural language (or the original LAION caption). Keep training steps and hyperparameters identical. If the SG-conditioned models still outperform, the structured-conditioning claim becomes airtight.
2. **Report human evaluation results** (user study from Appendix A.3) in the main paper rather than the appendix, especially pairwise preference between SG-conditioned and text-only models on CompSGen Bench samples.
3. **Report accuracy on a human-corrected subset** of CompSGen Bench as a secondary ground truth, to break the circularity concern.
4. **Add confidence intervals or standard deviations** to the key quantitative tables (Tables 2–4).

## Score and Decision

**Score: 6.0**

**Decision: Accept**

**Calibration Summary**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| SG-Adapter (KCYDpqSpqg) | 5.50 | R1/R2 | Directly comparable SG2IM paper; current paper is significantly stronger (540K vs 309 images, more backbones, broader evaluation) |
| DSG Eval (ITq4ZRUT4a) | 6.00 | R2 | Evaluation benchmark paper; similar quality, different focus |
| SlotAdapt (kZvor5aaz7) | 6.25 | R2 | Object-centric + diffusion for compositional generation; comparable tier, similar strengths/weaknesses balance |
| Hydra-SGG (tpD1rs25Uu) | 6.33 | R2 | Scene graph generation; comparable quality |
| COGT (haJHr4UsQX) | 6.67 | R1/R2 | Compositional understanding; stronger empirical rigor but addresses different problem |
| ISG (rDLgnYLM5b) | 7.20 | R1/R2 | Higher-tier benchmark paper; more thorough evaluation methodology |

**Round 1 bracket:** 4.5 – 7.0 (stronger than weak anchors at 3.0–3.5 range; not as clean as top-quartile papers at 7.5+.)

**Round 2 narrowing:** The paper is clearly better than SG-Adapter (5.50) — larger scale, more thorough, better-controlled within-SG comparisons. It is comparable to SlotAdapt (6.25, Accept) and Davidsonian SG (6.00, Accept). The missing text-only fine-tuning control and benchmark circularity are real but not fatal (the core dataset contribution and the properly controlled LAION-Comp vs COCO/VG comparisons survive). Score set at 6.0, positioned between the SG-Adapter reject tier and the stronger papers in the 6.25–6.67 range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>