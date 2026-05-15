Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper introduces Self-TPT, a test-time prompt tuning framework that uses text-only self-supervised contrastive learning (Contrastive Prompt Tuning, CPT) to adapt prompts on class names rather than per-image computation. Stage 1 co-trains CPT with the classification objective (plus a gradient matching loss), and Stage 2 adapts prompts on new class names via CPT alone, enabling direct zero-shot prediction on test images without per-sample backward passes. This yields dramatic efficiency gains (25× FPS, 30× memory reduction over PromptAlign) while maintaining competitive accuracy on cross-dataset, base-to-new, and domain generalization benchmarks.

## Strengths

- **Drastically improved inference efficiency**: Self-TPT achieves 146.7 FPS and 0.32GB GPU memory on CLIP-B/16 (vs. PromptAlign's 5.3 FPS, 11.2GB) — a genuine 25× speedup and 30× memory reduction. This is an unambiguous practical contribution for deploying prompt tuning in resource-constrained settings. (Table 1)

- **Novel text-only adaptation paradigm**: Shifting test-time adaptation from per-image computation to class-name preprocessing (Eq. 3, Stage 2) is a conceptually clean and underexplored approach. The method converts a major computational bottleneck into a negligible one, decoupling prompt refinement from test-image processing.

- **Gradient correlation insight with principled GM loss**: Figure 3b empirically demonstrates positive cosine similarity between CPT and classification gradients across 10/11 datasets, providing an intuitive explanation for why CPT serves as a useful proxy. The gradient matching loss (explicitly maximizing this similarity) yields consistent gains of ~0.5–1.0% in ablation (Table 5c), supporting the causal claim.

- **Broad and systematic evaluation**: The paper evaluates across three benchmarks (11 datasets), five model backbones (RN50 through L/14), a different VLM (EVA-CLIP), and includes data-efficiency and class-diversity ablations. The consistent improvement across all backbones (Table 7a) and on EVA-CLIP (Table 7b) demonstrates generalizability beyond CLIP-B/16.

- **Clean ablation decomposition**: Table 5a-5c cleanly isolates the contributions of Stage-1 CPT, Stage-2 TTA, GM loss, and each contrastive view, providing clear evidence that each component contributes positively.

## Weaknesses

### Fatal
None.

### Major

- **The domain generalization benchmark reveals a framing mismatch that overstates the method's TTA capabilities.** In the domain generalization setting (Table 4), the four target datasets (ImageNet-V2, -Sketch, -A, -R) share the *exact same 1000 class names* as the source dataset (ImageNet). Self-TPT's Stage 2 adaptation operates on class names only — since the class names are unchanged, the adaptation does not introduce visual-domain information and cannot be understood as adapting to distribution shifts. The paper claims Self-TPT demonstrates "robustness to domain shifts and adaptability to varying image distributions" (Line 373), but the method never sees a single test image during adaptation. The +1.82% gain must come from Stage 1 co-training (which produces better source prompts), not from test-time adaptation. The paper should reframe this: Self-TPT is not adapting to domain shifts; it is leveraging better source training that happens to transfer well.

- **The SOTA claims mix two different inference regimes without sufficient transparency.** The three headline improvements (+0.93%, +1.59%, +1.82%) are all based on **Self-TPT-v** (which uses 63 augmented images at inference with ensemble), not the efficient unaugmented Self-TPT. The unaugmented Self-TPT achieves smaller margins (+0.80% cross-dataset, +1.13% base-to-new) and is **not even reported** in the domain generalization table (Table 4). The abstract and introduction state "state-of-the-art performance" without specifying which variant, creating ambiguity. Since the efficiency claim (Table 1) uses the unaugmented version while the accuracy claim often uses the augmented version, the paper conflates two different operating points. It should be transparent about which variant supports each claim.

- **Missing variance reporting across seeds undermines confidence in the modest gains.** All results are averaged over three seeds but no standard deviations or confidence intervals are reported anywhere. Given that prompt learning benchmarks typically exhibit 1–2% variance across seeds, and the claimed margins are 0.93–1.82%, the improvements could easily lie within noise. For example, EuroSAT in cross-dataset (52.94) trails WaffleCLIP (55.07) and VisDesc (54.84) — these per-dataset underperformances are not discussed. The paper should either report variance or demonstrate consistency (e.g., directional improvement across all seeds/datasets).

- **Self-TPT and TPT/PromptAlign solve different sub-problems, making direct comparison misleading without caveat.** Self-TPT adapts prompts on class names only (text-only); TPT/PromptAlign adapt per image, incurring high cost. The efficiency comparison (Table 1) is valid, but the accuracy comparison (Tables 2–4) pits a text-only method against methods that address the harder problem of visual distribution shifts. The paper correctly includes prompt-learning baselines (CoOp, CoCoOp, etc.), but the narrative emphasizes the TPT comparison to claim "SOTA" while the gains over non-TTA methods are more modest. A clearer discussion of what the relevant comparison regime is would strengthen the paper.

### Minor

- **Self-TPT (unaugmented) is absent from the domain generalization table (Table 4).** Only Self-TPT-v appears. Without this data, readers cannot assess how the core efficient method performs on domain shifts, nor can they determine how much of the 1.82% improvement comes from augmentation vs. the core method. This missing result should be reported.

- **The gradient similarity analysis (Figure 3b) is computed on source data.** This is appropriate for motivating the GM loss (which is applied during Stage 1 training), but the paper does not analyze whether CPT gradients align with classification gradients on *new* class names. Since Stage 2 relies entirely on CPT operating on new class names, analyzing this directly (e.g., for base-to-new splits where labels exist) would strengthen the claim.

- **On several individual datasets, Self-TPT underperforms simpler baselines.** EuroSAT (cross-dataset): Self-TPT 52.94 vs. WaffleCLIP 55.07 and VisDesc 54.84 — a gap of ~2%. In base-to-new, Self-TPT lags PromptSRC on Pets, Food101, and Aircraft. These per-dataset regressions are not discussed and suggest the method is not uniformly superior.

### Trivial
- The paper uses "state-of-the-art" in the abstract without immediate qualification (e.g., "among efficient TTA methods").
- Table numbering in the text references may not match the actual floating placement (e.g., the domain gen table is labeled Tab. 4 in the wrap table but referenced somewhat loosely).

## Nice-to-Haves
- Adding standard deviations or confidence intervals for all main tables.
- Reporting Self-TPT (unaugmented) results for domain generalization.
- Analyzing gradient similarity on new (target) class names where test labels exist (e.g., base-to-new setting).
- A brief limitations section acknowledging that the method does not handle visual distribution shifts during test-time adaptation and is best characterized as "label-space adaptation."

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Stage 2 adaptation is vacuous on same class names"** — Overstated. CPT on identical class names still refines the text embedding space via contrastive learning (pushing different classes apart, pulling same-class views together). This is not "vacuous," though it is not adapting to visual shifts either.
- **"GM loss transfer to new classes is unknown"** — The GM loss is applied during Stage 1 training only, and its effect on final prompts is validated by the ablation (Tab. 5c) and the overall benchmark improvements. This is a standard training-time technique; requiring per-class-name gradient analysis on test classes is not a standard expectation.
- **"Comparison to non-TTA methods is unfair"** — The paper includes both prompt learning and TTA baselines in the same tables, which is standard practice. Self-TPT outperforms both categories, so the comparison is not misleading by inclusion.
- **Generic strengths from Strength Finder** (e.g., "addressed an important problem") — Dropped due to lack of specific evidence or conflict with verified weaknesses.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a fundamentally new interpretation of the method or results that the paper itself does not already present.

## Suggestions

1. **Separate the two regimes explicitly.** Reframe Stage 2 as "class-set adaptation" or "label-space refinement" rather than "test-time adaptation." Reserve test-time adaptation claims for settings where the method actually handles visual distribution shifts (which it does not).
2. **Report unaugmented Self-TPT for domain generalization.** Without this, the +1.82% claim is incompletely supported.
3. **Add variance estimates** (standard deviations over seeds) to all main tables, or provide a consistency analysis showing directional improvement across seeds.
4. **Clarify in the abstract and introduction** that the SOTA accuracy claims are based on the Self-TPT-v variant (with augmentation + ensemble). Distinguish this from the efficiency claims.
5. **Discuss per-dataset weaknesses** (e.g., EuroSAT) to provide a balanced assessment of where the method excels vs. underperforms.
6. **Show gradient similarity on new class names** (using base-to-new partitions) to directly validate the transfer of the gradient correlation insight to the test-time setting.

## Score and Decision

The paper makes a real contribution: text-only prompt adaptation that achieves dramatic efficiency gains is practically important, and the CPT + GM design is well-motivated. However, the framing overreaches — the method is presented as general test-time adaptation when it only handles new class names, not visual distribution shifts. The variance reporting gap and the conflation of augmented/unaugmented variants weaken the empirical claims. These are addressable issues. The paper should not be accepted in its current form, but a revision addressing these structural framing issues could make a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>