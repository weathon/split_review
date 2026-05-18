Now I have all the evidence needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes a library-based relearning framework for continual learning. The core idea is to store a large, unbiased "library" of past data (beyond the small replay buffer), detect when shortcut learning causes information loss via an "active quiz" that tests task-id prediction on the library, and then select a small informative subset from the library for targeted relearning. Experiments on CIFAR10, CIFAR100, and TinyImageNet show that the approach improves several strong baselines (especially CLOM) by 1–4% accuracy.

---

## Strengths

1. **Novel library-based relearning architecture.** The idea of maintaining a larger, unbiased library that serves both as a testbed for detecting shortcut learning (via the active quiz) and as a source for selective relearning is a genuinely new contribution to the continual learning literature. The separation between library (large, unbiased, for quizzing/selection) and library buffer (small, for actual training) is clearly articulated and distinct from standard replay buffers.

2. **Consistent empirical gains on main benchmarks (Table 1).** Applying relearning to the CLOM baseline yields the highest accuracy on all five dataset/task configurations (e.g., 87.5% vs. 83.8% for CLOM+c on CIFAR10-5T, 76.3% vs. 72.9% on TinyImageNet-10T). The performance gap generally widens as the number of tasks increases, which is consistent with the paper's motivating story about cumulative shortcut learning.

3. **Active quiz reduces computation cost (Table 3).** The selective relearning mechanism (triggered only when the worst-task difficulty count exceeds λ=100) demonstrably reduces the number of relearning rounds while maintaining most of the accuracy gain, providing practical evidence of efficiency.

4. **Orthogonal applicability demonstrated.** The method is shown to improve baselines from different categories (regularization-based, replay-based, task-ID-based) in Table 2, suggesting the framework is a general augmentation strategy rather than a narrow fix.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison: total stored data is not controlled.** The library stores 5000 samples (|L_T|) in addition to the library buffer (|C_T^L| = 200 for CIFAR10, 2000 for CIFAR100/TinyImageNet), for a total of 5200–7000 stored samples. Standard replay baselines store only the buffer (200–2000 samples). No ablation compares CLOM (or other baselines) with an enlarged replay buffer of equivalent total size to isolate whether the improvement comes from the sample selection algorithm or simply from having access to more past data. The paper's claim that "Even when the baseline uses the same size of replay-buffer... the replay-buffer is not enough" (Section 5.1) addresses buffer-to-buffer training cost, not total storage advantage. This is a significant evidential gap that prevents disentangling the method's core contribution (the selection mechanism) from a simple data quantity effect.

2. **Difficulty score computation is unspecified for non-task-ID methods (DER++, BiC).** The difficulty score D_t^i (Eq. 4) is defined in terms of inter-task logits p_{t'}^i and within-task logits p_t^i, which presupposes per-task classifiers. For methods like DER++ and BiC that use a single classification head, there are no per-task logit vectors. The paper says "For Der++ and BiC, we use fixed replay buffer and library buffer size m=500 for all datasets" (Section 5.1) but never explains how Eq. 4 is applied to single-head classifiers. Without this information, the results in Table 2 cannot be interpreted or reproduced. This undermines a significant part of the empirical claims about orthogonality.

### Minor

3. **No variance or standard deviations reported.** The paper reports single accuracies without standard deviations across runs. CL results can vary across seeds, and the 1–4% improvements may not be statistically significant without this information. This is the single most important missing experimental detail.

4. **Mutual information estimation details missing for Figure 1b.** The paper presents Figure 1b as empirical support for the IB analysis, showing that I(X_1;H) drops during shortcut learning and recovers after relearning. However, no estimator, number of bins, or any technical detail is given for how mutual information was computed. The axes appear unlabeled in the figure. This makes the figure uninterpretable as evidence and weakens the empirical grounding of the theoretical motivation.

5. **Hyperparameter sensitivity not studied.** Two key parameters of the proposed method receive no sensitivity analysis: (a) λ = 100 for the active quiz threshold (Table 3, set without justification), and (b) c in the transformation function (Eq. 5), which controls the peak of the difficulty score transformation. The paper notes that c ∈ [1.5, 2.5] but provides no ablation on how different values of c or λ affect results.

6. **Computational cost comparison is qualitative.** The paper provides an asymptotic complexity analysis (O notation) but no wall-clock time or FLOPs comparison against baselines. Since the method requires loading the full library (5000 samples) for scoring and 100 extra epochs of training for the classifier heads, a quantitative cost comparison would strengthen the claim of "comparable computational cost."

### Trivial
None.

---

## Nice-to-Haves

- Add an ablation where the library buffer is selected **randomly** from the library (same size) and compare to the difficulty-based selection to isolate the contribution of the selection algorithm.
- Report a brief limitations paragraph discussing cases where the method might fail (library too small, difficulty score not correlating with shortcut loss, relearning causing forgetting of the new task).
- Clarify whether the difficulty score computation for non-task-ID methods requires assuming task boundaries during memory selection, which may not be available in strict class-incremental settings.

---

## Removed Points

These points were flagged by reviewers but removed from the main weaknesses after cross-checking against the paper:

- **"Missing related work discussion"** — The harsh critic suggests deeper discussion of shortcut types in CL and comparison with OnPro. The paper does briefly distinguish itself from OnPro ("Our approach stems from the information bottleneck perspective, and our techniques differ from the prototype learning strategy"). Missing related works cannot be confirmed without external sources. **(Removed per hard rule about missing related works.)**

- **"Missing hyperparameters (batch size, learning rate, optimizer)"** — The paper states "We follow a similar augmentation technique as (Kim et al., 2022a;c)" and references prior work for experimental details. The critic's request for training hyperparameters is a standard concern but falls under the hard rule to remove nitpicks about reproducibility details that can be recovered from cited references. **(Removed per hard rule.)**

- **"IB theory is unmoored from method / should be removed"** — The harsh critic argues the theoretical connection is too loose. However, the paper explicitly uses IB as a **conceptual motivation** (Section 3), not as a formal optimization objective. The method's contrastive learning step is connected to MI maximization via the lower bound (Khosla et al., 2020). Many papers use conceptual frameworks without formal optimization; this is a stylistic choice, not a flaw. The specific valid concern about missing MI estimator details is already captured in Weakness #4. **(Removed as it overstates the severity of the theory-practice gap.)**

---

## Novel Insights

The most insightful observation that emerges from synthesizing the reviews is that the paper's core claim has a **confound that is explicitly visible but unaddressed**: the method's advantage may come from simply storing more data (the library), and the carefully engineered difficulty-score transformation and active quiz mechanism may contribute less than the paper implies. This confound is fixable (an ablation with random library selection and an enlarged replay buffer baseline) but acknowledging it changes how seriously one takes the theoretical framing. A second insight is that the difficulty score (Eq. 4) implicitly assumes task-ID-based architectures, which the paper extends to non-task-ID methods without explaining the adaptation — this suggests the "orthogonal applicability" claim is weaker for replay-only methods than for task-ID methods. Neither observation invalidates the paper's contribution, but both point to specific experiments that would substantially strengthen it.

---

## Suggestions

1. Add a control experiment where the library buffer is selected **randomly** from the library (same size as the difficulty-based selection). If difficulty-based selection outperforms random, the selection algorithm is validated. If not, the benefit is from having more stored data.
2. Add a baseline where CLOM (or a simpler replay method) is given a replay buffer of size equal to the total stored samples (library + library buffer), to isolate the effect of the selection mechanism from the data quantity advantage.
3. Explicitly state how the difficulty score (Eq. 4) is computed for single-head classifiers (DER++, BiC). If task boundaries must be assumed during selection, state this assumption and its limitations.
4. Report all main results with at least 3 random seeds (mean ± std) to establish statistical significance.
5. Provide details of the mutual information estimator used in Figure 1b, or remove the quantitative MI claim and keep Figure 1b as a qualitative illustration.
6. Include a sensitivity analysis for the key hyperparameters c (Eq. 5) and λ (active quiz threshold) over a small range.

---

## Score and Decision

**Originality:** 7/10 — The library concept and active quiz are novel, though the theoretical framing (IB) is standard and loosely connected.
**Importance of research question:** 8/10 — Shortcut learning in continual learning is a timely and underexplored problem.
**Claims support:** 5/10 — The main claim is supported by Table 1, but the fairness confound and missing methodological details weaken the evidence.
**Soundness of experiments:** 5/10 — Missing variance, uncontrolled storage comparison, and underspecified application to non-task-ID methods are significant gaps.
**Clarity of writing:** 7/10 — The main ideas are communicated clearly, though the IB section is dense and the MI figure lacks details.
**Value to community:** 7/10 — The library-based relearning framework is a practical idea that other CL researchers could build upon.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>