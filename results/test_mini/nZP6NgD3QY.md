Now I'll write the final consolidated review.

---

## Summary

This paper proposes AdaMerging, an unsupervised method that learns per-task or per-layer merging coefficients for task-vector-based model merging via entropy minimization on unlabeled multi-task test data. The approach addresses the sensitivity of existing task arithmetic methods to a single global merging coefficient λ. Experiments on eight image classification tasks (VTAB-1k style) with ViT-B/32 and ViT-L/14 show that Layer-wise AdaMerging improves average accuracy by 11% over Task Arithmetic and 8.7% over Ties-Merging, with additional experiments demonstrating generalization to unseen tasks and robustness to distribution shifts.

## Strengths

- **Significant and consistent performance gains over SOTA task-vector methods.** On ViT-B/32, Layer-wise AdaMerging achieves 80.1% vs. Task Arithmetic's 69.1% and Ties-Merging's 72.4% (Table 1). Gains are consistent across both architectures and on the ViT-L/14 setting (90.8% vs. Task Arithmetic's 84.5% and Ties-Merging's 86.0% in Table 2). Task-wise AdaMerging (single coefficient per task) shows more modest gains (71.1%—slightly below Ties-Merging), indicating the key innovation is the layer-wise granularity rather than merely allowing per-task coefficients.

- **Stronger generalization to unseen tasks.** When merging six task vectors and testing on two unseen tasks, AdaMerging achieves 4.4–9.1% higher average accuracy than Task Arithmetic and Ties-Merging (Table 3). This is the cleanest experiment in the paper because the unseen tasks were never part of coefficient optimization, providing a more rigorous evaluation.

- **Interpretable learned coefficients reveal differential layer importance.** The analysis of learned layer-wise coefficients (Figure 3) shows that shallow layers consistently rely more on pre-trained weights (smaller λ), while deep layers depend more on task vectors (larger λ). This aligns with representation learning intuitions and provides a principled explanation for why layer-wise merging outperforms task-wise merging.

- **Established correlation between entropy and test loss.** The Spearman correlation of 0.87 between entropy and prediction loss across eight tasks (Figure 2) provides empirical justification for using entropy minimization as a proxy objective — a non-trivial finding that the paper verifies rather than assumes.

- **Robustness to distribution shifts.** AdaMerging consistently outperforms Task Arithmetic across seven corruption types (motion blur, impulse noise, Gaussian noise, pixelate, spatter, contrast, JPEG compression) with average improvements of 5.8–11.2% per corruption type (Table 4).

## Weaknesses

### Major

1. **Evaluation protocol does not clearly separate adaptation and evaluation sets (structural).** The method optimizes merging coefficients via entropy minimization on batches of unlabeled test samples (Eq. 1, line 150). The paper then reports accuracy on "the test set" without specifying what fraction of test samples were used for adaptation versus held out for evaluation. The statement that "even if only 0.1% or 1% of unlabeled tests are available, our method can have significant performance improvements" (line 154) is presented as a generic claim without actual results showing this. Without knowing whether evaluation samples overlap with adaptation samples, the reported numbers in Tables 1–4 could be optimistically biased. This is the most consequential weakness because it affects the interpretation of all main results. (The paper's own generalization experiments in Table 3 partially mitigate this concern since unseen tasks were never adapted on, but the seen-task numbers in the same table suffer from the same ambiguity.)

2. **Missing ablation studies on coefficient optimization.** The paper does not report the optimizer, learning rate, number of iterations, batch size, initialization scheme, or convergence behavior for the coefficient learning procedure (line 154 merely notes "This is trivial with automatic differentiation tools like Pytorch"). Without these details the method cannot be independently reproduced. Furthermore, there is no ablation showing how performance varies with the number of optimization steps, the amount of test data used for adaptation, or the sensitivity to random seeds. The claim that "0.1% or 1% of unlabeled tests" works is stated but never empirically demonstrated.

### Minor

3. **Robustness experiments omit Ties-Merging baseline.** Table 4 compares AdaMerging only against Task Arithmetic for robustness to corruptions, despite Ties-Merging being a central baseline in the main results. Since a detailed per-task analysis would be informative (e.g., EuroSAT under Impulse Noise where AdaMerging scores 30.8% vs. Task Arithmetic's 49.1%), including Ties-Merging would give a more complete picture of robustness trade-offs.

4. **Unfair comparison confounds adaptation with coefficient flexibility.** The baselines (Task Arithmetic, Ties-Merging) use a single global λ searched on validation data, while AdaMerging uses test-time adaptation with per-layer coefficients. This conflates two factors: (a) the benefit of per-coefficient flexibility and (b) the benefit of test-time adaptation. A control baseline that applies entropy- based test-time adaptation to the merged Task Arithmetic model (without per-coefficient flexibility) would help isolate the source of improvement. The generalization experiments (Table 3) partially address this by testing on unseen tasks, but the main results remain confounded.

5. **Task-wise AdaMerging underperforms Ties-Merging.** In Table 1, Task-wise AdaMerging (71.1%) actually scores lower than Ties-Merging (72.4%), and Task-wise AdaMerging++ (73.7%) only matches it. This weakens the claim that adaptive coefficients broadly improve performance — the improvement is specific to the layer-wise variant. The paper should discuss this limitation more explicitly.

### Trivial

- None beyond those listed above.

## Nice-to-Haves

- Evaluate with a proper hold-out protocol: adapt coefficients on a subset (e.g., 50%) of each task's test samples and evaluate on the remaining held-out portion for both AdaMerging and baselines given test-time adaptation access.
- Include baselines that also use entropy-based test-time adaptation: (a) Task Arithmetic with λ tuned via entropy minimization, (b) a simple "entropy minimization on the merged model" without reweighting, to separate the effect of per-coefficient adaptivity from the effect of test-time adaptation.
- Report per-task accuracy in all tables to expose cases where improvements are concentrated or drops occur (e.g., EuroSAT under corruption).

## Removed Points

- **"Correlation analysis does not validate entropy minimization as a surrogate" (Harsh Critic point 3):** REMOVED. The critic claims this analysis is "circular" because the correlation is computed on test data. This is a misunderstanding. The paper establishes that entropy and prediction loss are correlated (Spearman ρ=0.87) on the test distribution, which straightforwardly justifies entropy as a proxy objective for loss minimization on that distribution. This is not a causal claim about held-out generalization — it is a correlational validation of a surrogate objective, which does not require a hold-out set. The analysis is sound for its intended purpose.

- **"Claim about bridging the gap is not supported" (Critic, Introduction note):** REMOVED. The paper says AdaMerging "greatly reduces the gap" (line 218)—which is factually supported (80.1% vs. 88.9% traditional MTL, vs. 69.1% Task Arithmetic). The critic mischaracterizes this as claiming the gap is fully bridged.

- **Various formatting/style nitpicks and minor presentation issues:** REMOVED per instructions (parser artifacts, not author errors).

- **Strength Finder's generic strengths (e.g., "addresses an important problem"):** REMOVED. These are superficial and not specific to the paper's contributions.

## Novel Insights

None beyond the paper's own contributions. The key novel elements — using entropy minimization to optimize merging coefficients without training data, and the interpretable layer-wise coefficient patterns — are well-described in the paper itself.

## Suggestions

1. **Most important: clarify the evaluation protocol.** Specify exactly what fraction of test samples per task were used for coefficient adaptation, whether evaluation was on the same samples or a held-out portion, and report results under both settings (including with 0.1%, 1%, 10% of test data). This single change would most improve the credibility of the empirical claims.

2. **Add optimization details.** Report the optimizer (Adam/SGD?), learning rate, number of gradient steps, batch size per task, and initialization of λ values. Show a convergence curve (entropy vs. iteration) to demonstrate that the optimization is not overfitting.

3. **Add a test-time adaptation baseline.** Apply entropy minimization directly to the merged Task Arithmetic model (without per-layer reweighting) as a control. This would isolate whether the gains come from per-layer flexibility or simply from test-time adaptation.

4. **Include Ties-Merging in the robustness table** and discuss per-task trade-offs more honestly (e.g., EuroSAT drops).

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison to AdaMerging |
|--------|-----------|--------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lNtio1tdbL.md` (ATM) | 3.00 | Much weaker — ATM misaligns with model merging goals by requiring joint training. AdaMerging works on independently-trained models. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/q3ztjJRQuJ.md` (TATR) | 5.75 | Similar topic. TATR is training-free, but AdaMerging has stronger empirical results. AdaMerging is slightly stronger overall. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1v7SRWsYve.md` (MAP) | 6.33 | Both accepted. MAP focuses on Pareto fronts. AdaMerging has more extensive experiments (generalization, robustness) and clearer novelty. Comparable quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eaTqsptDPL.md` (SAM) | 5.75 | Both about improving model merging. AdaMerging has stronger experimental results and more dimensions of evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/D7KJmfEDQP.md` (GradMatch) | 6.00 | Good theoretical grounding, but experiments are weaker than AdaMerging's. AdaMerging has more comprehensive empirical validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/McqVjmwdPe.md` (Weight Multitask) | 5.75 | Rejected. AdaMerging has a clearer contribution and better experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/plflYGf23L.md` (CABS) | 4.75 | Rejected. AdaMerging has stronger results and a more novel approach. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lIdc5DUplq.md` (SUPERMERGE) | 4.33 | Rejected. AdaMerging is better positioned and has clearer evaluation. |

### Assessment

The paper presents a well-motivated, novel idea with strong empirical results across multiple dimensions (accuracy, generalization, robustness, interpretability). The layer-wise coefficient analysis provides genuine insight. The main weakness is structural: the evaluation conflates adaptation and testing (no clear hold-out), and the method's optimization details are underspecified. These are addressable but real concerns. The paper is stronger than the rejected anchors in its topic area (ATM 3.00, CABS 4.75, SUPERMERGE 4.33) and comparable to the accepted ones (TATR 5.75, MAP 6.33, GradMatch 6.00).

**Score: 6.0** — A solid paper with genuine contributions. The evaluation protocol concern prevents a higher score but does not invalidate the contribution, given that the generalization experiments (unseen tasks) partially address it.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>