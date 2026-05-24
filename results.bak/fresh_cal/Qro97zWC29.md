Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes NeCo (Patch Neighbor Consistency), a self-supervised dense post-pretraining loss that enforces patch-level nearest-neighbor ordering consistency between a student and teacher model using differentiable sorting. Applied as a lightweight post-pretraining step (19 GPU-hours on COCO) on top of existing vision transformers, NeCo yields substantial gains across frozen clustering (+14.5% over CrIBO), in-context segmentation (4–13% over DINOv2-R and CrIBO), linear segmentation, full finetuning, and 3D multiview consistency, setting new state-of-the-art results on several benchmarks.

## Strengths

1. **Novel use of differentiable sorting for dense feature learning.** The paper replaces binary contrastive signals (attract/repel) with a richer, continuous ordering signal by applying differentiable sorting (Petersen et al., 2021) to patch-level nearest-neighbor distances between student and teacher. This is a clean conceptual departure from prior dense SSL methods like CrIBO and Hummingbird, which operate on pooled image- or object-level features (Section 3, Eqs. 2–4).

2. **Consistent and substantial gains across six different pretrained backbones demonstrate generality.** Table 3 shows that NeCo improves DINO, iBOT, Leopart, TimeT, CrIBO, and DINOv2-R by roughly 4–30% on frozen clustering and linear segmentation. Notably, it even improves CrIBO — a method already trained with a dense SSL objective — indicating that the ordering signal adds value beyond generic dense training.

3. **New state-of-the-art in in-context semantic segmentation, especially in low-data regimes.** On the nearest-neighbor retrieval benchmark (Balazevic et al., 2023), NeCo outperforms prior methods by 4–13% on Pascal VOC and ADE20k, with the gap widening at smaller training fractions (1%, 5% of data). This directly supports the paper's claim that the method produces higher-quality patch-level representations (Figure 2).

4. **Efficient post-pretraining (19 hours, single GPU) that improves even massive models like DINOv2-R.** Despite DINOv2-R being trained on 142M images with multiple losses, NeCo fine-tunes it for a fraction of the compute and surpasses it on full-finetuning segmentation (Table 4) and linear segmentation (Table 2). This efficiency is a practical strength.

5. **Improvements in 3D understanding (multiview feature consistency) demonstrate broader impact beyond segmentation.** Table 5 shows NeCo boosts DINO models by roughly 10% on SPair-71k (recall@0.01), demonstrating that the method improves spatial and geometric feature quality, not just semantic discreteness. This evaluation is not aligned with the training objective, strengthening the generality claim.

6. **Ablation studies validate key design choices.** Table 6 systematically ablates patch selection, teacher-student EMA, nearest neighbor source, training dataset, sorting algorithm, batch size, and number of neighbors, providing empirical justification for design decisions.

## Weaknesses

### Major

1. **The contribution of the sorting-based loss is not fully isolated from the confound of additional COCO training data.** NeCo is applied as a post-pretraining step on COCO (118k images). Baselines (CrIBO, DINOv2-R, etc.) are taken as released without additional dense training on the same data. This conflates two factors: (a) the proposed sorting-based loss, and (b) the benefit of any additional dense training on a dataset (COCO) that is semantically aligned with the downstream evaluation tasks. Table 3 partially addresses this by showing NeCo improves CrIBO (which already had dense SSL training), but a controlled experiment — comparing NeCo against a baseline that receives the same COCO post-pretraining with a simpler dense loss (e.g., patch-level contrastive or patch-level MSE consistency to the teacher) under identical compute and data conditions — is needed to attribute the gains definitively to the ordering signal. Without this, the core claim that differentiable sorting is responsible for the improvements is less strongly supported than the paper implies.

### Minor

1. **Metric alignment between training and the in-context evaluation.** The training objective explicitly enforces nearest-neighbor ordering consistency, and the benchmark reporting the largest margins (Figure 2) is itself a nearest-neighbor retrieval evaluation. This creates direct alignment between what the model is optimized for and what it is tested on. The paper mitigates this by showing strong results on non-aligned tasks (linear segmentation, full finetuning, 3D understanding), and the critic acknowledges this mitigation. However, the paper should acknowledge this alignment explicitly and discuss whether the in-context benchmark may over-react to the training signal, especially since improvements on unrelated tasks (3D understanding, ~10%) are smaller than on the in-context tasks (>10% on average in clustering). Not a fatal concern, but worth tempering claims of broad "scene understanding" improvements.

2. **Key hyperparameters (reference fraction \(f\) and temperature \(\beta\)) are not reported.** The method section defines the fraction \(f \ll 1\) of sampled reference patches (line 48) and the inverse temperature \(\beta\) in the differentiable sorting relaxation (line 62), but neither value is specified. The fraction \(f\) directly affects memory footprint (permutation matrices of size \(R \times R\)) and neighbor quality, while \(\beta\) controls the hardness of the sorting relaxation. These values are important for reproducibility and practical adoption.

3. **The "no sorting" ablation is mentioned but not presented with numerical results in the main paper.** The text states "Additionally, we investigate the absence of a sorting component, which leads to deteriorated performance" (line 241), with a footnote referencing supplementary tables. For a point that directly supports the central claim — that the sorting mechanism is necessary — the main paper should include this result or at least clearly describe what replaces the sorting component (e.g., random ordering, standard contrastive loss). Without this, the reader cannot evaluate whether the ordering signal is truly necessary or whether a simpler consistency loss would suffice.

4. **Results are reported without error bars or significance tests.** Given that some comparisons involve differences of <1% (e.g., sorting algorithm variants in Table 6), it is unclear which results are reliable. While single-run evaluation is common for large-scale benchmarks in this field, reporting standard deviations or confidence intervals would strengthen the evidence, especially for claims of incremental improvements.

### Trivial

- The paper does not explicitly state that COCO (training set) does not overlap with Pascal VOC or ADE20k validation sets. A brief statement would address a natural concern about evaluation fairness.

## Nice-to-Haves

- An analysis of the learned neighbor orders (e.g., "are the top-5 nearest neighbors semantically meaningful for a given patch?") would deepen the intuition for why the ordering signal works.
- Reporting the wall-clock time or compute requirements of baselines under the same evaluation conditions would contextualize the efficiency claim.
- An analysis of how the effective reference pool size \(R\) (determined by \(f\), batch size, and number of patches) impacts memory and performance.

## Removed Points

These points from the reviewers were removed with brief justifications:

- **"Standard deviations / error bars" (moved from potential Major to Trivial):** Single-run evaluation on large-scale segmentation benchmarks is standard practice in this subfield; the absence is a minor presentation concern, not a structural weakness.
- **"Compute comparison against baselines" (moved to Nice-to-Have):** Requesting wall-clock time for all baselines under identical conditions is a useful addition but not standard practice, and the paper already provides its own compute budget.
- **"Dataset overlap concern" (moved to Trivial):** A minor clarification the authors could add in one sentence.
- **"Metric alignment could invalidate results" (retained as Minor after filtering):** The paper provides extensive counter-evidence (linear seg, full finetuning, 3D), so this is not a fatal concern; kept as a minor caveat.
- **Generic strength statements from Strength Finder (e.g., "addresses an important problem", "targets an interesting question"):** These lack specific evidence anchored in the paper and do not add value beyond the concrete strengths already listed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard critical analysis for a paper of this type (data confound in post-pretraining, metric alignment, ablation clarity) but do not identify a new research direction or unexpected implication of the method.

## Suggestions

1. **Run a controlled experiment isolating the loss function:** Take a strong dense SSL baseline (e.g., CrIBO or DINOv2-R), apply a post-pretraining phase on COCO using an alternative dense loss (e.g., patch-level contrastive attract/repel, or patch-level MSE consistency to the teacher) with identical compute, batch size, augmentations, and EMA framework, and compare against NeCo trained under the same conditions. This is the cleanest test of whether the ordering signal — and not just any dense post-training on COCO — is responsible for the gains.

2. **Report the numerical values of the "no sorting" ablation in the main paper and specify what replaces the sorting component** (e.g., random permutation, identity ordering, or standard contrastive loss).

3. **Report the specific values of \(f\) (reference fraction) and \(\beta\) (sorting temperature)** used in all experiments, as these are critical for reproducibility.

4. **Acknowledge the metric alignment between training objective and in-context evaluation** explicitly, and discuss why improvements on non-aligned tasks (linear segmentation, 3D) support the generality claim despite this alignment.

## Score and Decision

This paper proposes a conceptually clean and technically sound method with strong empirical results across diverse evaluations. The main weakness — incomplete isolation of the loss function from the data confound — is real but addressable, and the paper provides partial mitigating evidence (Table 3 improves dense SSL baselines; Table 4 beats DINOv2-R trained on 142M images). The contribution is novel and the results are practically significant. I recommend acceptance with a request to address the controlled experiment and reporting gaps in a revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>