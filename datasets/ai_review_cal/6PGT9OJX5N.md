- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 3, 1
Now I have all the evidence I need. Let me verify the remaining key claim about whether all baselines use the re-labeling method.

**Key verification: Table 1 caption explicitly says "Comparison of baselines and the proposed RoP by using PreAct ResNet-18 and re-labeling method (SOP+)"** — meaning KCenter + SOP+ is already a baseline. The harsh critic's claim that the paper doesn't compare with KCenter + re-labeling is factually wrong.

Now I'll compose the final review.

---

## Summary

This paper proposes a two-stage data pruning method (RoP) for noisy-label scenarios. The first stage computes a Neighboring Label Inconsistency Score (NLI-Score) by constructing a local KNN graph, applying feature and label propagation to correct neighboring predictions, and measuring JS divergence between a sample's label and its neighbors' predictions. The second stage selects samples based on NLI-Score, applies density-based coverage sampling to balance easy/hard samples, and re-labels the selected subset with SOP+. Experiments on CIFAR-10N, CIFAR-100N, WebVision, and ImageNet-N show consistent improvements over baselines.

## Strengths

1. **NLI-Score measurably reduces noisy sample selection.** Table 3 shows that RoP's selected subset contains only 4.8% noisy labels on CIFAR-10N (20% selection) versus ≈17% for competing methods. This is direct, concrete evidence that the proposed metric effectively discriminates clean from noisy samples—arguably the paper's strongest empirical result.

2. **Consistent SOTA across multiple benchmarks.** RoP_B outperforms 10 baselines on CIFAR-10N, CIFAR-100N (Table 1), WebVision (Figure 4), and ImageNet-N (Table 4), with a 1.5% improvement over the sub-optimal method on CIFAR-10N Worst at 20% pruning. Performance is demonstrated across both real-world and synthetic noise.

3. **Ablations validate the two-stage design.** Table 6 confirms that feature+label propagation improves over no propagation, and that re-labeling is critical especially at low pruning rates. Figure 6 shows the method is stable for K ∈ [10,15] across pruning rates. The empirical correlation between NLI-Score and re-labeling accuracy (Figure 3) provides a principled justification for the selection strategy.

4. **Competitive selection efficiency.** Figure 5 shows RoP's selection time on ImageNet-N is comparable to GraNd (~10 seconds), whereas KCenter is orders of magnitude slower—an important practical consideration for large-scale deployment.

## Weaknesses

### Fatal
None.

### Major

1. **Missing full-dataset reference point for SOP+.** The paper compares pruning methods against each other but does not report the test accuracy of SOP+ trained on the *entire* noisy dataset (0% pruning). Without this upper bound, the reader cannot assess how much accuracy pruning costs relative to using all available data. For example, on CIFAR-10N Worst at 20% pruning, RoP_B achieves the best result among pruning methods—but is this close to the full-data SOP+ accuracy or substantially below it? This affects the interpretation of every table. Figure 1 shows "Full" (entire noisy dataset), but it is unclear whether this uses the same SOP+ re-labeling pipeline, and it is not included in the main comparison tables. This is the single most impactful missing piece of evidence.

2. **No measures of statistical uncertainty.** All tables report only averages over 3 runs without standard deviations or confidence intervals. Many improvements over the next-best method are in the 1–2% range, and without variance it is unclear which differences are robust across seeds. This is a recurring evidential weakness that should be addressed in all main tables (Tables 1, 4, 5, 6).

### Minor

1. **No systematic analysis of how the pre-trained model's quality (affected by noise) impacts the NLI-Score.** The method relies on a model trained on the noisy dataset itself (θ\_̃D) for both features and the classifier weights used in label propagation. If the initial model overfits to noisy labels, feature neighbors could be contaminated and propagation could amplify errors. The ablation on K (Figure 6) and the propagation ablation (Table 6) partially address this, but a direct stress test—varying noise level and measuring NLI-Score's ability to identify clean samples—would strengthen the evidence for robustness.

2. **Single-step feature propagation not justified.** Equation 5 applies (I+E)V, which is a single smoothing step. The paper does not discuss why one round is sufficient or whether iterative propagation would improve or harm the NLI-Score. This is a methodological detail that could affect results.

3. **Density-based coverage pruning insufficiently explained.** The coverage sampling component (CCS, referenced to Zheng et al. 2022b) has a non-trivial effect (RoP vs. RoP_B differences in Table 1), but the paper does not describe how CCS operates on NLI-Scores or justify its application in this setting beyond a one-sentence reference. A brief explanation of the mechanism would aid understanding.

4. **Computational complexity analysis omitted.** The method requires computing a KNN graph for the entire dataset (O(n²) naive). The paper should discuss how this scales to larger datasets (e.g., 1.2M ImageNet-N). Figure 5 shows wall-clock time is competitive, but an explicit complexity analysis would be valuable.

5. **Table 3 only at one selection ratio (20%).** Showing the noisy-sample ratio at multiple pruning rates would strengthen the claim that NLI-Score consistently selects cleaner subsets. The K ablation (Fig. 6) is only on CIFAR-10N; results on another dataset would strengthen generalizability claims.

### Trivial
None.

## Nice-to-Haves
- A systematic noise-rate sweep (e.g., 10%, 30%, 50% synthetic noise) to characterize the method's breaking point.
- Extending Table 3 (noisy sample ratio) across multiple pruning rates.
- Ablation of K (neighbor count) on at least one additional dataset beyond CIFAR-10N.

## Removed Points

- **"KCenter + re-labeling not compared"** — REMOVED. Factually incorrect. Table 1 caption states all baselines use SOP+ re-labeling. KCenter + SOP+ is already a baseline in every table.
- **"Full-dataset baseline in Fig. 1 doesn't clarify if it uses SOP+"** — PARTIALLY RETAINED as Major #1 (the full-data SOP+ baseline is missing from tables). The specific complaint about Fig. 1's "Full" baseline being unclear is removed because Fig. 1 is a motivation figure, not the main results table.
- Various formatting/style/presentation nitpicks — REMOVED per instructions (parser artifacts).
- **"Related work thin on joint noise+pruning methods"** — REMOVED. Missing related works should not be mentioned per instructions.
- **"Reproducibility details incomplete (architecture, epochs, etc.)"** — REMOVED per hard rules. The paper provides code and states the architecture (PreAct ResNet-18). Training protocol details commonly appear in appendices (stripped by parser).
- **"Why one step of propagation"** — DEMOTED from the harsh critic's framing as a major concern to Minor #2. It is a reasonable question but does not threaten the core claims.
- **Strength Finder's generic/superficial strengths** — REMOVED. Only dropped the ones that are generic (e.g., "addresses an important problem") or contradicted by verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface a perspective on the method that the paper itself does not articulate.

## Suggestions

1. **Add a full-data baseline**: Report the performance of SOP+ trained on the entire noisy dataset (0% pruning) in Tables 1, 4, and 5. This single addition would dramatically strengthen the paper's evidential value.
2. **Add standard deviations** to all main tables, or at minimum indicate which differences are robust across seeds.
3. **Add a sensitivity experiment** varying the noise rate (e.g., 10%, 30%, 50% synthetic noise on CIFAR-10) to show how NLI-Score's discriminative power degrades with increasing noise.
4. **Justify the single-step propagation** or show (even briefly) that more iterations do not help.
5. **Expand the description of CCS** to at least one paragraph explaining how coverage sampling operates on NLI-Scores.
