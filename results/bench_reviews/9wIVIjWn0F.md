Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA), a method that replaces the standard entropy-based view selection in CLIP test-time adaptation with a learned regression mapping from view logits to a pseudo cross-entropy loss. The key insight—demonstrated through ceiling experiments—is that ground-truth label cross-entropy selects views far better than entropy. RTA trains a lightweight LightGBM regression tree once on pseudo-labeled ImageNet data to predict loss from logits, then uses this tree at test time to select confident views across arbitrary downstream tasks without parameter updates. The method achieves new state-of-the-art results on single-label, multi-label, and cross-domain benchmarks.

## Strengths

- **Compelling ceiling experiments:** Tables 1–2 convincingly show that oracle view selection via true-label cross-entropy (LCE) yields dramatic accuracy gains over entropy-based selection (e.g., ViT-B/16 with 64 views on ImageNet-A: 90.2% LCE vs. 64.3% entropy). This clearly motivates seeking better view-selection signals than entropy and is a genuinely useful finding for the community.

- **Consistent state-of-the-art across diverse settings:** RTA achieves new best results on single-label ImageNet variants (Table 3: OOD average 65.84% for ViT-B/16, surpassing Zero's 65.03%), cross-domain benchmarks (Table 4: highest average accuracy for both RN50 and ViT-B/16), and multi-label datasets (Tables 5–6: up to 3.18% mAP improvement over ML-TTA on NUSWIDE). The breadth and consistency of these gains are impressive.

- **Practical and efficient design:** The method requires only a single offline training pass on 1,000 pseudo-labeled samples using LightGBM, followed by zero-parameter-update inference at test time. This avoids the backpropagation, memory banks, or iterative optimization required by most prior TTA methods, making it genuinely lightweight.

- **Cross-domain generalization without per-task retraining:** The regression tree is trained once on ImageNet-based data and applied directly to ten cross-domain datasets and multi-label tasks with strong results, demonstrating practical transferability.

## Weaknesses

### Major

- **Missing direct-computation baseline:** The regression tree is trained to predict pseudo-LCE computed as \(-\log(\max_j \text{softmax}(s)_j)\) for high-confidence samples (confidence ≥ 0.8), because the pseudo-label is the argmax class in these cases. A natural and important baseline is to simply use \(-\log(\max \text{softmax})\) on the same 1000 ImageNet-class logits as a view-selection score, requiring no training at all. The paper never reports results for this baseline, leaving unclear whether the learned regression tree adds value beyond a trivial deterministic computation. Since the tree partitions the full logit space rather than only using the maximum, it *could* capture useful distributional patterns beyond the scalar max, but this needs to be demonstrated. This is the most significant methodological gap in the current submission.

- **Class-set specification for non-ImageNet tasks is ambiguous:** Section 4.3 and Algorithm 2 do not explicitly state which class labels are used to compute the logit inputs to the regression tree during test-time adaptation on cross-domain or multi-label tasks. The most plausible reading is that the tree always takes 1000 ImageNet-class logits regardless of the target task, but this critical design choice is never stated, and the papers notation reuses \(L\) and \(\mathbf{t}_j\) without disambiguation. This makes the cross-domain and multi-label experiments difficult to reproduce from the description alone and should be clarified.

### Minor

- **Pseudo-LCE to true-LCE gap not validated:** The paper motivates the entire approach with ceiling experiments using ground-truth LCE (Tables 1–2) and shows that logit features correlate with true LCE (Figures 2–3). However, the regression tree is trained on *pseudo*-LCE from CLIP's own predictions—not true LCE—and the paper provides no direct measurement of how well the trees predicted pseudo-loss correlates with true label loss on downstream tasks. A Spearman correlation between predicted loss and true loss on test tasks would bridge this important gap. The strong downstream results provide indirect evidence, but a direct validation would substantially strengthen the contribution.

- **No analysis of why the tree outperforms entropy:** The paper shows that the tree-based selection outperforms entropy, but never analyzes *why*. Is it because the tree leverages cross-class information in the full logit vector? Because it captures non-linear interactions? Because the mapping generalizes better across distributions? An ablation or qualitative analysis would help readers understand what the tree is learning that entropy misses.

### Trivial

- Notation inconsistency in Eq. (8): the superscript uses \(x_i^{\text{reg}}\) in a section describing test-time adaptation, where \(x_i^{\text{test}}\) would be expected. This is a minor typographical issue but adds to the ambiguity about whether the test stage uses the same class set as regression training.

## Nice-to-Haves

- **Side-by-side view selection examples:** Showing which views are selected by RTA vs. entropy vs. the direct-computation baseline on a few test images would make the method's behavior more interpretable.
- **Sensitivity to the confidence threshold (0.8):** The paper analyzes sensitivity to sample size but not to the critical confidence threshold that determines the regression target formulation.
- **Comparison with training on lower-confidence pseudo-labels:** Showing results when training with lower confidence thresholds (where the pseudo-label is not trivially the argmax) would help justify the regression approach over the direct computation.

## Removed Points

These points were raised by the Harsh Critic but are flagged for removal, as they are either incorrect, overly harsh, or misinterpret the paper:

- **"The regression mapping is unnecessary and the methodological contribution is hollow."** While the missing direct-computation baseline is a valid concern (kept as a Major weakness), the Harsh Critic's conclusion that the method is therefore hollow overstates the case. The regression tree uses the full 1000-dimensional logit vector as input, not merely the maximum softmax value, and its decision-tree structure can capture non-linear interactions across logit dimensions that a scalar max-softmax cannot. The empirical results show the method working across diverse settings. The baseline is needed but its absence does not make the method hollow.

- **"Cross-domain and multi-label results are not reproducible and their validity is in doubt."** The Harsh Critic claims the method cannot work because the tree expects a fixed-dimensional input. However, the paper's design implies the tree always takes the 1000 ImageNet-class logits (the classes used during regression training) regardless of the downstream task. This is a reproducible design—it just needs to be stated clearly. The downstream task predictions use task-specific classes separately. This is a clarity issue, not a fatal reproducibility problem.

- **"The logits-loss visualization and Spearman analysis do not validate the regression target."** The Harsh Critic correctly notes these analyses use true-label loss while the tree is trained on pseudo-loss, but this is a limitation in validation strength (already captured as a Minor weakness), not an invalidation. The analyses still demonstrate that logit structure carries information about view quality, which is the core motivation.

- **"The paper should remove the regression model and use the direct formula."** This contradicts the critic's own acknowledgment that the method achieves SOTA results. Whether the tree can be replaced by a simpler formula is an empirical question the baseline would answer—not a reason to reject a working method outright.

## Novel Insights

The paper's genuinely novel insight is the empirical discovery that view quality can be predicted from logit vectors via a simple regression mapping trained on out-of-domain pseudo-labeled data, without requiring any target-domain labels, parameter updates, or memory banks. This challenges the prevailing assumption in the TTA literature that view selection must rely on instance-level signals (entropy, reward models, etc.) and opens a new direction: pre-computing general-purpose view-quality estimators that transfer across tasks. This is conceptually distinct from both entropy-based methods and prior loss-prediction work (Kim et al., 2020), which required in-domain training.

## Suggestions

- Add the \(-\log(\max \text{softmax})\) baseline computed on the same 1000 ImageNet-class logits. If RTA outperforms this baseline, it demonstrates the tree adds value; if not, the insight simplifies to an even more elegant finding. Either outcome is publishable and useful.
- Explicitly state in Section 4.3 that the regression tree always receives logits computed against the 1000 ImageNet class prompts (the same class set used in regression training), regardless of the downstream task's label space.
- Report Spearman or Pearson correlation between the tree's predicted loss and true label loss on at least one held-out test task to bridge the motivation-to-method gap.

## Score and Decision

### Anchor Comparison

- **CLUvRxQXtf (CLIP-TTA): avg 4.67, Reject** — An incremental method (adds two losses to CLIP-OT), missing key baselines, limited to one backbone. RTA is stronger: broader experimental coverage, more novel paradigm (regression vs. entropy), SOTA margins are larger.

- **S90g7NE88b (FGA): avg 5.00, Accept (Poster)** — A well-motivated method with theoretical analysis but requires labeled training data, has theoretical gaps flagged by reviewers, and narrower experimental scope. RTA has broader benchmarks, requires no labeled data, and achieves clearer SOTA. RTA is somewhat stronger.

- **HeGMugkCOH (C-TTA): avg 3.00, Reject** — Confusing terminology, sensitive hyperparameters, missing CTTA experiments. RTA is substantially stronger in both methodology and evaluation.

- **dHj8hC081K (ADTE): avg 4.50, Accept (Poster)** — Replaces SE with TE plus bias correction; incremental over existing entropy frameworks, modest gains. RTA proposes a fundamentally different paradigm with larger gains. RTA is stronger.

- **nErnNhJx2o (SOBA): avg 4.00, Reject** — Training-free TTA via geometric transformation. RTA has more comprehensive evaluation and stronger results.

- **rClkte0ZTp (Efficient Test-Time Scaling): avg 5.00, Accept (Poster)** — Test-time augmentation and adaptation for small VLMs. Comparable quality level; RTA's broader benchmarks give it a slight edge.

- **7kLNGaAHaw (PEA): avg 5.50, Accept (Poster)** — Backprop-free TTA via embedding alignment, strong theoretical framing. RTA lacks theory but has more extensive multi-label and cross-domain evaluation.

The paper's core strengths (compelling ceiling experiments, consistent SOTA across many benchmarks, efficient design) outweigh its weaknesses (missing baseline, clarity issue on class set, unvalidated pseudo-to-true loss gap). The missing baseline is the most significant concern but is addressable and does not invalidate the contribution. The paper falls in the Accept (Poster) range, comparable to or stronger than the 5.0–5.5 anchors.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>