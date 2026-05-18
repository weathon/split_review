Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a library-based relearning framework for continual learning that addresses shortcut learning. It stores a larger dataset (the "library," ~5000 samples) from past tasks, uses a difficulty-score-based selection mechanism with a sine transformation to select a small informative subset (the "library buffer"), and relearns classifier heads on that subset. An active quiz mechanism decides whether relearning is needed. Experiments on CIFAR10/100 and TinyImagenet show 2–5% improvements over strong baselines like CLOM, DER++, and BiC.

---

## Strengths

**1. Library-based relearning framework delivers consistent empirical gains.** Table 1 shows that applying relearning to the strongest baseline (CLOM+c) improves final accuracy by +3.3% on CIFAR100-10T (68.3→71.6) and +2.4% on TinyImagenet-10T (58.6→61.0). The gap widens as the number of tasks increases, consistent with the paper's claim that shortcut learning compounds across tasks.

**2. Orthogonality to multiple CL method categories.** Table 2 demonstrates that relearning improves DER++ (+4.6% on TinyImagenet-10T), BiC, and CLOM, showing the framework is not tied to a single model architecture or training paradigm. This is the strongest evidence that the library buffer selection mechanism delivers value beyond the base method's own replay buffer.

**3. Active quiz for selective relearning.** Table 3 shows that using the library as a testbed with threshold λ=100 achieves 97.1% accuracy (vs. 97.3% for always-relearning) while skipping relearning on several tasks, validating the computational efficiency claim. This is a practical and well-motivated mechanism.

**4. Ablation on library size and difficulty level.** Figure 5 provides empirical backing that a moderate library size (5000–10000) and moderately difficult samples give the best performance, and that extreme difficulty or very large libraries harm performance due to outlier selection. This supports the design choices in the transformation function.

---

## Weaknesses

### Fatal
None.

### Major

**1. The contribution of the selection mechanism is not isolated from the benefit of having a larger selection pool.** The method stores a library of 5000 samples (a larger pool from which to select), while baselines select their replay buffers incrementally from individual task data. Although the library buffer used for *training* is the same size as baselines' replay buffers (controlled in Table 2), the method has access to a much larger pool to score and choose from. The paper lacks a controlled experiment where a baseline also draws from a pool of 5000 past samples but selects uniformly at random (or via another simple strategy). Without this, it is unclear whether the improvement comes from the specific difficulty-score + sine-transformation selection or simply from having a larger, more representative pool to sample from. The paper claims that "simply increasing replay buffer size is not feasible" (Section 4.1) due to computation cost, but this conflates storage with training: the library is stored but not trained on fully — the same could be done for baselines as a controlled comparison. This is the most significant gap in the evaluation.

**2. No standard deviations or confidence intervals reported for any experimental result.** This is a common shortcoming in CL papers but makes it impossible to assess whether the reported gains (2–5%) are statistically significant, especially for smaller improvements on CIFAR10-5T.

### Minor

**3. The information bottleneck analysis is presented as a theoretical contribution but is informal and does not yield testable predictions specific to the proposed method.** Equations (3)–(4) restate standard IB concepts with heuristic notation (representing X_t by a set of features H). The conclusion that the replay buffer is insufficient because |C_t| << |X_t| is straightforward and does not require the IB formalism. The analysis does not explain why the library is the correct remedy over alternatives (larger replay buffer, generative model). The paper would be better served by treating this as intuitive motivation rather than a formal contribution.

**4. Mutual information estimation in Figure 1b is not specified.** The paper reports "the value of mutual information" for Task 1 data but does not describe the estimator used. Mutual information between high-dimensional continuous variables (images and hidden representations) is notoriously difficult to estimate reliably. Without specifying the estimator, assumptions, and any approximations, Figure 1b cannot be interpreted or reproduced. This weakens the empirical evidence offered for the theoretical claim.

**5. Active quiz threshold λ (=100) is used without sensitivity analysis.** The paper sets λ to 100 for CIFAR10-5T (Table 3) but provides no ablation varying λ or showing how performance and computational cost trade off. The method's claim of "effectively detect[ing] shortcut learning" depends on this threshold.

**6. The transformation function (Equation 5) is a heuristic with no comparison against alternatives.** The sine-based function is chosen from a Fourier series search space but is not compared against simpler alternatives (e.g., selecting top-k by raw difficulty score, Gaussian weighting, uniform random from the library). Without this comparison, the specific design choice is not empirically justified.

**7. No comparison with OnPro** — the only prior work on shortcut learning in CL cited by the paper. While OnPro uses a different approach (prototype learning), including it as a baseline would contextualize the contribution against the most directly related method.

**8. No ablation on the choice of difficulty scoring function** (Equation 4). The score uses `max(p_t' - max(p_t))`. Alternatives such as entropy, margin, or loss-based difficulty are not explored, so the design remains ad hoc.

### Trivial

- The paper does not discuss limitations (e.g., when the library might hurt performance, scalability to ImageNet-scale datasets, or distribution shift within tasks).
- Actual training time comparisons with baselines are not reported, despite the computational cost analysis in Section 4.2.

---

## Nice-to-Haves

- A controlled experiment comparing difficulty-based selection vs. uniform random selection from the same 5000-sample library pool. This would directly validate whether the selection mechanism (and not just the larger pool) drives the improvement.
- Sensitivity analysis for λ (active quiz threshold) on at least one dataset.
- Comparison against OnPro (Wei et al., 2023) as the most directly related prior work on shortcut learning in CL.
- Ablation comparing the sine transformation against simpler weighting schemes (e.g., Gaussian, top-k).

---

## Removed Points

- **"Writing is disjointed" (Harsh Critic, Other Observations):** Pure style/presentation nitpick. Removed per hard rules on formatting/style.
- **"The claim that the function is derived from a Fourier series is misleading" (Harsh Critic, Point 5, partial):** The paper explains the Fourier series connection explicitly (Section 4.2): a sine is a valid first-harmonic member of the Fourier series family. The characterization is not misleading. Removed.
- **"The library buffer selection...does not analyze how scaling affects selection" (Harsh Critic, Other Observations, last bullet):** Too granular; belongs at the level of the transformation function choice (already covered in Weakness #6 above).
- **Strength: "Theoretical insight from information bottleneck" (Strength Finder, point 1):** Dropped because it conflicts with verified Weakness #3 (the theory is informal and does not yield testable predictions). The weakness wins per instructions.

---

## Novel Insights

The reviews surface a tension that the paper itself does not fully address: the library concept is intuitively appealing (store more data, select intelligently), but the paper conflates two potential sources of improvement — having a larger, more representative pool to draw from vs. the specific difficulty-score selection mechanism. A controlled decomposition (random selection from an equally large pool vs. difficulty-based selection) would not only strengthen this paper but provide a useful methodological baseline for future work on selective replay in continual learning. Additionally, the paper's framing of shortcut learning as a distinct phenomenon from catastrophic forgetting (rather than a sub-cause) is a useful conceptual contribution that could influence how future CL work diagnoses and attributes performance drops.

---

## Suggestions

1. **Add a controlled experiment comparing difficulty-based selection vs. uniform random selection from the same library pool.** This is the single most impactful addition: it isolates whether the selection mechanism itself adds value beyond having a larger representation of the past data distribution.

2. **Specify the mutual information estimator used in Figure 1b** (or acknowledge that the figure is an approximate visualization). If the estimator is non-standard, include its details.

3. **Report standard deviations** (at least over 3–5 runs) for the main results in Tables 1 and 2 to establish significance.

4. **Add sensitivity analyses** for the threshold λ (active quiz) and the transformation parameter c on at least one dataset.

5. **Consider comparing against OnPro** or at minimum discuss why the comparison is omitted (different task setting, incompatible architectures, etc.).

6. **Add a limitations section** discussing when the library might not help (e.g., few-shot tasks, within-task distribution shift, very large-scale datasets like ImageNet).

---

## Score and Decision

The paper addresses a real problem (shortcut learning in continual learning) with a practical, well-motivated framework that shows consistent improvements across multiple datasets and baseline categories. The library concept and active quiz mechanism are novel and sensible. However, the evaluation has a significant confound: the method benefits from a larger selection pool (the 5000-sample library) that baselines do not have, and the paper does not isolate whether its specific selection mechanism drives the gains or simply having more data to choose from. This gap is addressable with additional controlled experiments. The remaining weaknesses (informal theory, missing sensitivity analyses, no standard deviations) are standard issues in the CL literature but collectively detract from the rigor. The core contribution is promising but not yet fully validated.

**Score:** 6.0 — A solid paper with a meaningful contribution and generally well-executed experiments, but the main evaluative confound prevents stronger acceptance. With the controlled experiment suggested above, this could become a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>