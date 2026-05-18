Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper addresses two limitations of Randomized Smoothed Conformal Prediction (RSCP): (i) its robustness guarantee is invalid when Monte Carlo sampling is used in practice (the concentration bound for the MC estimator is missing), and (ii) it produces excessively large (often trivial) prediction sets. The paper proposes \algoname, a new framework that uses the Monte Carlo estimator directly as the non-conformity score and provides a provable robustness guarantee via concentration inequalities. It then proposes Post-Training Transformation (PTT) and Robust Conformal Training (RCT) to reduce prediction set sizes. Experiments on CIFAR10, CIFAR100, and ImageNet show that the baseline produces trivial full-label-set predictions, while PTT/RCT boost efficiency by up to 4.36×, 5.46×, and 16.9× respectively.

## Strengths

1. **Clearly identifies a real theoretical gap in RSCP.** Section 3 explicitly points out that RSCP's guarantee is invalid in practice because it uses a Monte Carlo estimator without bounding the estimation error (Step 2 is missing). This is a sound logical argument supported by the paper's exposition: the theory assumes access to the intractable expectation $\scorers$, but practice uses $\hat{S}_{\text{RS}}$, and no bridge between them is provided. The paper then proposes \algoname to close this gap by using the MC estimator directly as the score and providing a concentration-bound-based guarantee (referenced as Theorem thm:MCScoreMainResultHoef).

2. **PTT and RCT yield dramatic and practically meaningful efficiency improvements.** Without these methods, the baseline produces trivial prediction sets (size = number of classes) that are useless. PTT (training-free) and RCT (training-based) reduce set sizes substantially — boosts of up to 4.36× on CIFAR10, 5.46× on CIFAR100, and 16.9× on ImageNet — turning an otherwise impractical method into a useful one.

3. **Principled theoretical motivation for efficiency improvement.** The paper provides a quantitative analysis linking the coverage gap to the slope of the score CDF via a linear approximation (Eq. 13–17), directly motivating the Sigmoid transformation in PTT. The two design conditions (slope reduction, monotonicity) are clearly stated and justified.

4. **Methods are orthogonal to the core framework and compatible with prior work.** The paper explicitly notes that PTT and RCT work not only with \algoname but also with the original RSCP, and provides additional results in the appendix. This demonstrates generality beyond the specific certification framework.

5. **Experimental validation across three standard benchmarks of varying scale.** Results are reported for CIFAR10, CIFAR100, and ImageNet, showing that the efficiency gains hold consistently. The analysis of the impact of Monte Carlo sample size $N_{\text{MC}}$ on set size (Figure 2) provides useful practical guidance.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **No empirical coverage verification.** The paper relies entirely on the theoretical guarantee (referenced Theorem thm:MCScoreMainResultHoef) and reports only average set sizes. While theoretical coverage guarantees are standard in conformal prediction and respect the "provably robust" claim, the paper's central motivation is fixing a practical flaw in RSCP (the missing MC error bound). Given this framing, a table reporting empirical coverage for all methods would strengthen reader trust that the efficiency gains do not inadvertently compromise coverage in practice. This is especially relevant because the concentration bound itself is an approximation (the bound is a high-probability statement, not exact).

2. **The PTT linear approximation, while well-motivated, has its core theoretical justification deferred to the appendix.** The main text (Eq. 13–17) provides the linear approximation $\covgap \approx \Phi'(\tau) \cdot M_\epsilon$, which is clearly explained, and the paper mentions that synthetic and empirical studies are in the appendix. However, a reader of the main text alone cannot assess how tight this approximation is or when it might fail. A brief discussion of the approximation error (e.g., a bound on the remainder of the first-order Taylor expansion) or at minimum a short intuitive description of when the approximation breaks down would make the main text more self-contained.

3. **The probability space of the robustness guarantee is not stated in the main text.** The theorem (thm:MCScoreMainResultHoef, thm:MCScoreContinuity_Hoef) is referenced but stated only in an input file stripped by the parser. The main text does not explicitly clarify the probability space (e.g., "with probability at least $1-\beta$ over calibration data and Monte Carlo randomness, for every test input and every adversarial perturbation of size $\leq \epsilon$, coverage $\geq 1-\alpha$"). A concise statement of this form in Section 3 would resolve ambiguity.

4. **The holdout set (size 500) for PTT ranking transformation is taken from the data and is disjoint from the calibration set, effectively reducing the calibration sample size.** The paper reports this size but does not analyze whether this reduction could affect coverage efficiency or how sensitive the method is to holdout set size. This is a modest concern but worth at least a brief discussion.

### Trivial

- The paper uses the placeholder `\algoname` throughout. This is standard for double-blind review and not a flaw, but should be replaced in a camera-ready version.

## Nice-to-Haves

- An ablation study on the holdout set size for PTT would help users understand the data requirement of the method.
- A brief discussion of the computational cost of \algoname (multiple MC draws per test point) and how PTT/RCT affect that cost would be useful for practitioners.
- Reporting the fraction of test examples where the ground truth is in the prediction set (empirical coverage) as a sanity check alongside the theoretical guarantee.

## Removed Points

The following points from the reviews are removed with justification:

- *"Insufficient justification that RSCP's guarantee is flawed"* — **Removed.** The paper clearly substantiates this claim. Section 3 states: RSCP uses MC estimation (Step 1) but omits the error bound (Step 2). The gap is explained: the theory relies on the intractable expectation $\scorers$, practice uses $\hat{S}_{\text{RS}}$, and without bounding this discrepancy the theoretical guarantee does not cover the practical implementation. This is a sound logical argument; a formal impossibility proof or empirical counterexample is not required to establish the gap.

- *"PTT relies on an unverified approximation" (as a fatal/major weakness)* — **Downgraded to Minor.** The paper acknowledges the approximation, provides the linear approximation equation, and explains that rigorous analysis is provided in the appendix (which was stripped by the parser). The main text gives the intuitive argument and two design conditions. This is not a fatal flaw.

- *"Probability space unclear" (as a critical issue)* — **Downgraded to Minor.** The theorem is in an input file. The main text could benefit from a one-sentence statement, but this is a presentation issue, not a structural one.

- *"\algoname placeholder indicates not fully camera-ready"* — **Removed.** This is standard practice for double-blind anonymous submission.

- *"Claim of being first should be toned down"* — **Removed.** The paper qualifies the claim with "To our best knowledge," which is appropriate.

- *"Perturbation magnitudes not justified"* — **Removed.** $\epsilon=0.125$ (CIFAR) and $\epsilon=0.25$ (ImageNet) are standard choices from the randomized smoothing literature (Cohen et al. 2019).

- *"Missing related works"* — **Removed.** As per instructions, the reviewer does not have external sources to confirm existence of missing references.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the existing reviews does not surface an insight about the paper that the authors themselves did not articulate.

## Suggestions

1. Add a table reporting empirical coverage (fraction of test examples where ground truth is in the prediction set) for all methods alongside set size. This directly addresses the most natural reader concern.

2. In Section 3, add a one-sentence statement of the form: "With probability at least $1-\beta$ over the calibration data and Monte Carlo draws, for every test input and every adversarial perturbation of $\ell_2$ norm $\leq \epsilon$, the coverage is at least $1-\alpha$."

3. In Section 4.1 (PTT), include a short discussion of the linear approximation error — e.g., a bound on the remainder term or a note on when the approximation may be loose — to make the main text more self-contained.

4. Discuss the impact of the holdout set size on calibration efficiency: e.g., how the effective calibration size changes and whether this affects the coverage guarantee.

5. Add a brief limitations paragraph in the conclusion, acknowledging that (a) PTT's linear approximation may be loose for some score distributions, (b) the guarantee depends on the number of Monte Carlo samples, and (c) the holdout set reduces effective calibration sample size.

**Score and Decision**

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>