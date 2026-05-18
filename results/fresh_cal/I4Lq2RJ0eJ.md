Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper studies unlearnable examples (UEs) — perturbations added to training data to prevent models from learning. It makes three contributions: (1) an empirical finding that existing UEs fail to maintain unlearnability in multi-task settings (Taskonomy, Fig. 1); (2) a loss-landscape-based explanation of UEs via the proposed Sharpness-Aware Learnability (SAL), which quantifies parameter-level sharpness during training; and (3) the Unlearnable Distance (UD) metric, which measures data unlearnability as the ratio of "learnable" parameters in poisoned vs. clean models, abstracting away from task-specific test accuracy. The paper benchmarks multiple UE methods, defenses, and architectures using UD.

---

## Strengths

1. **First demonstration that existing UEs fail in multi-task settings** (Fig. 1, §3.4). The paper shows that on Taskonomy (scene classification, keypoints, depth, segmentation), models trained on UEs from EM, OPS, and AR achieve task metrics nearly indistinguishable from clean training. This challenges the implicit assumption that UEs generalize across tasks and opens a concrete new research direction. The finding is clearly presented and well-motivated.

2. **Loss-landscape-based explanation of unlearnability via SAL** (§3.1–3.3, Definition 1). The paper provides a training-phase perspective on UEs by showing that models trained on UEs converge to flatter regions of the loss landscape, and that SAL (the max loss change within an epsilon-ball around parameters) drops sharply for most parameters under UEs while remaining high under clean training. This mechanistic account goes beyond prior shortcut-based or overfitting-based explanations and offers a more intrinsic view.

3. **The UD metric provides a task-agnostic evaluation tool** (§4, Definitions 2–3, Algorithm 1). UD measures unlearnability without relying on downstream test accuracy — it quantifies how many model parameters actually stop learning. This is a genuinely different evaluation paradigm. The metric correctly identifies TAP (adversarial examples) as distinct from true UEs (UD > 1), and the benchmarking in Tables 1–3 demonstrates UD's consistency with known results while surfacing new observations (e.g., ViT is harder to poison).

4. **Systematic benchmarking across datasets, defenses, and architectures** (Tables 1–3). The paper evaluates UD across CIFAR-10, CIFAR-100, ImageNet-100; three defenses (JPEG, UEraser, adversarial training) and two augmentations (MixUp, CutOut); and architectures including ResNet-18/50, SENet-18, and ViT. This provides practical insights (e.g., JPEG compression best restores learnability, stronger models are harder to poison).

---

## Weaknesses

### Fatal
None.

### Major

1. **Multi-task evidence is thin relative to the strength of the claim.** The paper repeatedly frames "We are the first to uncover that existing unlearnable methods fail to maintain unlearnability in multi-task models" as a central contribution. However, the supporting experiment uses only a single dataset (Taskonomy tiny), one backbone (ResNet), one training procedure (ModSquad), and four tasks. No alternative multi-task architectures or datasets are tested. The paper's own §3.4 acknowledges that multi-task learning naturally suffers from task conflicts, which makes the failure somewhat expected. The finding is genuine but the evidence base is too narrow to support the weight placed on it.

2. **UD metric lacks ablation and ground-truth validation.** Several critical design choices go unjustified: (a) the K-means threshold on SAL values assumes a bimodal distribution but no SAL distribution is shown; (b) the choice of epsilon for SAL, the number of iterative steps (10), and the epoch-averaging scheme are not ablated; (c) K-means initialization effects are not studied. More fundamentally, UD is correlated with test accuracy (Tables 1–3), but correlation does not validate a metric. The paper does not construct a controlled experiment with known unlearnability (e.g., mixing clean and random labels at varying ratios) to demonstrate that UD orders datasets correctly or reveals insights that accuracy cannot. Without such validation, UD remains a plausible but unverified heuristic.

3. **Framing-evaluation disconnect: multi-task hook, single-task UD evaluation.** The introduction motivates the need for better metrics by showing that UEs fail in multi-task settings. Yet UD is evaluated and benchmarked entirely on single-task classification (CIFAR-10/100, ImageNet-100). The multi-task analysis (§3.4, Fig. 5) uses cosine similarity of SAL vectors, not UD. The only UD values in the multi-task setting are a few labels in Figure 5(b), noted as "time-consuming." This leaves a significant gap between the motivating problem and the actual evaluation. The paper does not demonstrate that UD solves the problem it was introduced to address.

4. **Incomplete experiments and missing statistical rigor.** Table 1 contains entries marked "p indicates pending" — this is inappropriate for a submission; all experiments should be complete. No error bars or standard deviations are reported for any of the tabular results. Given that training from scratch on poisoned data can exhibit high variance, single-run reporting is insufficient to establish reliability.

### Minor

1. **No ablation of SAL/UD design choices.** The paper does not study sensitivity to the epsilon parameter in SAL, the number of K-means clusters (fixed at 2), the threshold computation (mean of cluster centers vs. median vs. fixed percentile), or the epoch averaging scheme. These design decisions could significantly affect the metric's behavior.

2. **Multi-task analysis (§3.4) is superficial.** Figure 5 shows cosine similarity of SAL vectors between tasks for clean vs. EM training, with the observation that similarity patterns are similar. This analysis does not connect to why UEs fail in multi-task settings beyond stating that task conflicts exist, nor does it use SAL/UD to propose a remedy or diagnostic tool for multi-task unlearnability.

3. **SAL closely resembles existing sharpness measures from SAM.** Definition 1 is essentially the standard sharpness measure used in SAM (Foret et al., 2020) and related work. The paper does not compare SAL against existing UE explanations (e.g., linear separability of perturbations, Yu et al. 2022) to show what SAL uniquely reveals that prior explanations cannot. The paper would benefit from a direct comparative analysis.

4. **No discussion of computational cost.** Computing SAL for each layer at each epoch requires 10 steps of inner optimization. This could be prohibitively expensive for large models or long training runs; the paper should report runtime or propose a cheaper approximation.

### Trivial
- The claim "we are the first to uncover" should be softened given the thin evidence base.
- No dedicated limitations section is present.
- Figure 2's PCA-based visualization of DNN parameters compresses millions of dimensions to two — the paper should report variance explained.

---

## Nice-to-Haves
- **Validate UD against a ground-truth dataset** with artificially controlled unlearnability (e.g., varying label noise ratios, perturbation strengths) and show that UD orders settings correctly, ideally revealing insights that test accuracy misses.
- **Bridge the multi-task gap**: either apply UD to multi-task training by defining a joint SAL over all tasks, or explicitly limit the paper's scope to single-task and adjust the narrative accordingly.
- **Provide a taxonomy of UD values**: what does UD < 0.1, ~0.5, > 1.0 mean in practical terms?
- **Discuss whether UD can be used as an optimization objective** to generate better UEs, or if it is purely an evaluation tool.

---

## Removed Points
These points were removed from the main review with justification:

1. **"The interpretation that defenses increase UD and thereby disrupt unlearnability is circular"** — REMOVED. This is not circular; it is a consistency argument. The paper uses UD to measure unlearnability and finds that defenses increase UD, which is exactly what one would expect if defenses work. The missing piece is independent verification of task performance alongside UD, which is already covered by other weaknesses.

2. **"The paper does not discuss whether UD can be used as a defense objective"** — REMOVED. This is scope creep; the paper presents UD as an evaluation tool, not an optimization objective. Criticizing it for not doing something it never claims to do is unfair.

3. **"No standard deviation" criticism reframed as "missing statistical rigor"** — KEPT as major weakness #4, as the "p" entries and missing error bars are genuine issues.

4. **"SAL is essentially just SAM's sharpness"** — WEAKENED to minor weakness #3. The harsh critic overstated the novelty concern; applying sharpness analysis to UE training is a new application. However, the lack of comparison with existing UE explanations remains a valid gap.

---

## Novel Insights
None beyond the paper's own contributions. Both reviews cover overlapping ground: the paper's core ideas (multi-task failure, loss-landscape explanation, UD metric) are acknowledged as interesting but insufficiently validated. No reviewer observation surfaced a fundamentally new perspective not already present in the paper.

---

## Suggestions
1. Add at least one controlled validation experiment for UD (e.g., dataset with known unlearnability via label noise).
2. Run the multi-task experiment with at least one additional architecture/dataset to strengthen the central claim.
3. Provide error bars (multiple seeds) for all tabular results; complete the "pending" entries.
4. Add ablation studies on the epsilon parameter, K-means vs. fixed threshold, and epoch averaging for UD.
5. Add a limitations section and discuss when UD might fail or be misleading.

---

## Score and Decision

The paper identifies a real gap (need for intrinsic UE metrics) and proposes a plausible direction. The multi-task finding, while limited, is genuinely novel. However, the UD metric is presented as a major contribution without ground-truth validation, ablation, or multi-task evaluation — a significant gap between claims and evidence. The lack of error bars and the presence of incomplete ("pending") experiments further weaken the empirical support. Revisions could substantially strengthen the paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>