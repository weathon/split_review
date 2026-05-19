- Decision: Accept
- Avg Score: 5.67
- Scores: 8, 6, 3
I have now thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper studies why large-learning-rate SGD improves neural network generalization. It proposes a feature-noise data model with strong features (large norm, present in a fraction of data) and weak features (small norm, present in all data), analyzes a two-layer CNN trained with SGD, and argues that oscillation of the network's predictions around the label does not cancel out but instead accumulates linearly — driving weak-feature learning. Theorem 5 shows that under an assumed oscillatory regime, weak features are learned to a constant scale, while Proposition 6 shows that small-LR training leaves weak features at initialization scale. Experiments on synthetic data and a CIFAR-10 motivation are provided.

## Strengths

1. **Novel mechanism: oscillation accumulation drives weak-feature learning.** Section 3 provides a careful decomposition (Equations (6)–(8)) showing that when the strong feature dominates, the sum of $(y f(\mathbf{x};\mathbf{W}^{(s)})-1)$ over oscillation periods has a determined sign and grows linearly in time (Equation (7)). This is a non-trivial insight that distinguishes the work from prior large-LR studies (e.g., Cohen et al., 2020) that observe oscillation but do not propose a mechanistic explanation for why it helps generalization.

2. **Formal comparative results under large vs. small learning rates.** Theorem 5 proves that under the oscillating regime the weak signal component reaches a constant scale $\delta/4$, while Proposition 6 bounds it at initialization scale $\widetilde{\mathcal{O}}(\sigma_0\|\mathbf{v}\|_2)$ under small-LR training. Together they directly establish a division in generalization (Section 4.2): large-LR trained NNs correctly classify weak test data, small-LR trained NNs do not.

3. **Targets a challenging and under-explored optimization regime.** The paper studies multi-pass SGD for a two-layer CNN with learning rate exceeding $m/(4\|\mathbf{u}\|_2^2)$, a regime where standard convex/strongly-convex convergence analysis does not apply. The careful tracking of strong-feature dynamics and the oscillation-accumulation argument is a technical advance over prior theoretical work that is largely restricted to small learning rates or linear models.

4. **Clean data model that isolates the core phenomenon.** The feature-noise model (Section 2) with strong features appearing only in a fraction of data and weak features present in all data cleanly captures the tension between learning dominant but non-generalizable patterns vs. weak but generalizable ones, enabling precise tracking of $\langle\mathbf{w}, \mathbf{u}\rangle$ and $\langle\mathbf{w}, \mathbf{v}\rangle$.

## Weaknesses

### Fatal
None.

### Major

1. **The paper assumes oscillation rather than deriving it from the learning rate, creating a gap between framing and proof.** Theorem 5 (and Theorem 2 in the single-data case) is conditional on Assumption 4, which simply *assumes* that $|y_{i_t} f(\mathbf{x}_{i_t};\mathbf{W}^{(t)}) - 1| \geq \delta$ for $\delta \in (0.2, 0.8)$ on strong data throughout training. The abstract states that "oscillation of the NN weights caused by SGD with large learning rates turns out to be beneficial," and the introduction frames oscillation as the engine driving learning (line 14: "the oscillation prevents the over-greedy convergence and serves as the engine"). However, the theory never establishes the causal chain LR $\to$ oscillation $\to$ benefit — it only proves the second link. The paper acknowledges this partially (lines 197–199 note that "Assumption 4 implicitly requires that the learning rate $\eta$ should be scaled properly" and that "the $\eta$ condition in Assumption 3 is only sufficient for boundedness and sign stability"), but this acknowledgment is buried in the assumptions section and does not appear in the abstract, introduction, or conclusion. The title ("Benign Oscillation of Stochastic Gradient Descent with Large Learning Rate") and the overall narrative imply a stronger end-to-end result than the mathematics supports. This is a genuine gap between the paper's claims and its proofs. The conditional analysis (oscillation $\to$ benefit) is still a meaningful contribution, but the paper overstates its scope.

### Minor

2. **The theoretical results depend on a specific constellation of conditions without discussion of which are essential.** Assumption 3 specifies the initialization scale $\sigma_0$, dimension $d = \Omega(n^2, \text{polylog}(m))$, $\|\mathbf{v}\|_2 \leq 0.1\|\mathbf{u}\|_2$, a narrow learning rate window $[m/(4\|\mathbf{u}\|_2^2),\, 2m/(5\|\mathbf{u}\|_2^2)]$, and a weak-data fraction constraint. While such conditions are standard in theoretical deep learning, the paper does not discuss which are structural and which are artifacts of the proof technique. For example, the dimension condition $d = \Omega(n^2)$ is quite restrictive relative to the small experiment ($d=64, n=16$ satisfies it only barely). This narrowness does not invalidate the results but limits their significance as stated.

3. **Experimental validation is on a very small scale with limited statistical rigor.** The synthetic experiments use $d=64$, $n=16$, $m=8$ with only 32 test points (4 weak). The test accuracy is averaged over 5 seeds, which is reasonable, but the internal dynamics plots (Figure 3) appear to be single-run trajectories with no variance information. The large test accuracy gap (99.38% vs. 93.75%) is consistent with the theory, but with only 4 weak test points, this difference represents at most 2–3 misclassifications, making the numbers coarse. For a theory paper these experiments serve as illustration, but more thorough validation would strengthen confidence.

4. **The claim that results "can be directly applied" to multi-feature, multi-patch, multi-class settings (line 50) is stated without justification.** This is a common but unsubstantiated assertion that the paper would be better without.

### Trivial
- The reference on line 41 has a broken citation anchor ("Ca0 et al." for Cao et al.).
- Line 67 contains a stray formatting character ("\Bar{x}").
- Line 94 contains garbled/duplicated text ("Thsoaqwdift").

## Nice-to-Haves

- **Prove that oscillation emerges from large LR under the data model**, or equivalently, derive Assumption 4 from the data model and learning rate choice. This would transform the paper from a conditional analysis into a complete end-to-end explanation and would justify the current framing.
- **If the above is not feasible**, reframe the title, abstract, and introduction to honestly scope the contribution as: "we prove that *if* oscillatory dynamics arise (as they do empirically), then weak-feature learning is guaranteed." This would eliminate the gap between claims and evidence.
- Report error bars or confidence intervals for the experimental results.
- Discuss which conditions in Assumption 3 are essential versus technical artifacts of the proof.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper uses only one random seed per learning rate."** — Factually incorrect. The paper states: "We repeat the testing evaluation over 5 random seeds and take the average" (line 244). The dynamics plots may be single runs, but this is standard for illustration in theory papers.
- **"The appendix is stripped, so we cannot verify the formal arguments."** — Per policy, missing appendix content is a parser artifact and should not be flagged as a weakness.
- **"Missing related works."** — Per policy, the reviewer cannot verify the existence of omitted references without external sources; this point is excluded.
- **General area sweeps** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?") — These are speculative concerns raised without specific evidence in the paper and are excluded.
- **Strengths that are generic** (e.g., "this paper addressed an important problem") — Removed as superficial; only concrete, paper-specific strengths are retained above.

## Novel Insights

The primary novel insight beyond the paper's own contributions is that the central weakness (assuming oscillation rather than deriving it) is partially but inadequately acknowledged within the paper. The paper states in lines 197–199 that the $\eta$ condition is only sufficient for "boundedness and sign stability" and that the dynamics could be more complex, but these caveats appear only in the assumptions subsection and are not reflected in the title, abstract, or conclusion. The net effect is a paper that has a real and novel theoretical contribution (the oscillation-accumulation mechanism and its formal analysis) packaged inside a narrative that promises more than it delivers. A reader who only reads the title, abstract, and conclusion would overestimate what has been proven. A reader who carefully reads Assumption 4 and the surrounding remarks would correctly understand the conditional nature. This discrepancy is the single most important issue to address in revision.

## Suggestions

1. **Reframe the contribution honestly.** If the authors cannot prove LR $\to$ oscillation, change the title to something like "Weak Feature Learning under Oscillating SGD with Large Learning Rates" and adjust the abstract and introduction correspondingly. The conditional analysis is still a publishable contribution; the overclaiming is what hurts the paper.

2. **Move the acknowledgment of the conditional nature from a buried remark (lines 197–199) to the introduction and conclusion.** Explicitly state: "We analyze the *consequences* of oscillation for feature learning; establishing that large LRs *cause* oscillation under our data model is a separate challenge that we leave for future work."

3. **Add a limitations paragraph** discussing that Assumption 4 is not derived, which conditions are essential vs. technical, and the small scale of the experiments.

4. **Report variance** for the synthetic experiments (at minimum, standard deviation over the 5 seeds for test accuracy).
