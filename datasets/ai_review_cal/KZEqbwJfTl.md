- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 6, 8, 5
Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper studies agnostic conditional (selective) classification under Gaussian marginals: given a distribution over labeled examples with standard normal $\mathbf{x}$-marginals, find a classifier and a halfspace selector such that the classification error on the selected subset is minimized. The paper provides (i) a polynomial-time algorithm for **homogeneous** halfspace selectors achieving an $\tilde{O}(\sqrt{\mathrm{opt}})$ approximation guarantee (Theorem 3.1), with an extension to sparse linear classifiers via list learning (Theorem 3.5), and (ii) hardness results showing that for **general** (non-homogeneous) halfspaces, approximating the conditional classification loss to small additive error is computationally hard under the sub-exponential cLWE assumption (Theorem 4.3), via a reduction showing conditional classification is at least as hard as agnostic classification (Proposition 4.5, Claim 4.7).

## Strengths

- **First polynomial-time algorithm for agnostic conditional classification with a provable approximation guarantee.** Theorem 3.1 shows that under standard normal marginals, Algorithm 1 achieves conditional classification error $\tilde{O}(\sqrt{\epsilon})$ when the optimal error is $\epsilon$, using $\tilde{O}(d/\epsilon^6)$ samples and time. This is the first such result for halfspace selectors, giving a concrete non-trivial approximation to a previously open problem.

- **Hardness result establishing a separation between homogeneous and general halfspaces.** Theorem 4.3 proves that, under the sub-exponential cLWE assumption, no polynomial-time algorithm can achieve even a small additive error for conditional classification with general halfspaces under Gaussian marginals. This establishes that the homogeneous case (the positive result) is genuinely easier.

- **Reductions connecting conditional and agnostic classification in both additive and multiplicative forms.** Proposition 4.5 shows that any additive-error algorithm for conditional classification implies an additive-error algorithm for agnostic classification (with a $6\epsilon$ factor), and Claim 4.7 gives an analogous multiplicative reduction. These formalize the relative difficulty of the two problems.

- **Extension to sparse linear classifiers via list learning.** Theorem 3.5 shows the algorithm generalizes to infinite classes of classifiers (e.g., sparse linear classifiers with $s=O(1)$) by combining with a robust list-learning oracle, achieving the same $\tilde{O}(\sqrt{\epsilon})$ guarantee in polynomial time.

## Weaknesses

### Fatal
None.

### Major

- **Initialization gap in the algorithmic analysis.** Lemma 3.4 and the inductive argument that drives the positive result explicitly require $\theta(\mathbf{v},\mathbf{w}^{(0)}) \in [0,\pi/2)$ — the initial weight vector must have angle less than $90^\circ$ to the unknown optimal selector $\mathbf{v}$. The paper does not specify how $\mathbf{w}^{(0)}$ is chosen (Algorithm 2 takes it as input; Algorithm 1 does not describe how to set it) nor provide any strategy to guarantee this condition. A random unit vector would succeed with probability at most $1/2$, and the paper offers no argument that multiple restarts or some other initialization scheme yields the condition in polynomial time. Because Theorem 3.1 is stated unconditionally (no initialization requirement appears in its statement), the claimed guarantee is not fully established by the analysis as presented. This is a concrete gap — the proof of the algorithm's correctness relies on an unaddressed assumption.

### Minor

- **Limited scope of the positive result.** The algorithm only works for homogeneous halfspaces (which always select exactly $1/2$ of the data under the standard normal) and requires Gaussian $\mathbf{x}$-marginals. The authors honestly acknowledge these limitations in Section 5, but they do reduce the practical significance. The homogeneous restriction in particular prevents the selector from choosing a minority subset — which is often the motivation for selective classification.

- **Structure of the hardness reduction is sketched rather than fully detailed in the main text.** Proposition 4.5 (the additive reduction from agnostic to conditional classification) is described in prose rather than with a formal derivation of the $6\epsilon$ factor. While the full details likely reside in the appendix (stripped by the parser), the main text's compressed treatment makes it harder for a reader to verify the factor's correctness without reconstructing the argument.

### Trivial
None.

## Nice-to-Haves

- An explicit discussion of how the initialization condition $\theta(\mathbf{v},\mathbf{w}^{(0)}) \in [0,\pi/2)$ could be guaranteed (e.g., random initialization with multiple restarts, or a warm-start argument) would resolve the main weakness cleanly.

- A brief synthetic experiment (e.g., low-dimensional Gaussian data with known optimal halfspace) would help demonstrate the algorithm's practical behavior and catch hidden assumptions, though this is not expected for a theory paper.

## Removed Points

**These points are flagged to be removed; treat them with caution:**

- *Weakness about Proposition 4.5's proof being "too sketchy to assess correctness"* — The full proof is in the appendix, which was stripped by the parser. The main text provides the logical structure (Lemma 4.4 → interval sweeping → $6\epsilon$ bound) consistent with a theory paper's presentation norms.

- *Weakness about sample complexity for the reduction and failure probabilities compounding* — The technical details of the interval discretization and union bounds are standard and would appear in the appendix.

- *Weakness about missing experimental validation* — Acknowledged by the reviewer as "not required for a theory paper."

- *Weakness about the homogeneous-halfspace assumption being a limitation* — Moved to Minor weaknesses instead, since the authors explicitly acknowledge it in Section 5 and it is a tradeoff, not an oversight.

- *Strength about the paper addressing an important problem* — Generic; removed per filtering rules.

- *Strength about the reductions being "supporting strengths"* — These are kept as strengths since they are concrete and specific to the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews primarily surface the initialization gap (genuine but likely fixable) and confirm the paper's stated contributions. The most interesting observation emerging from the synthesis is that the positive result and the negative result operate at fundamentally different levels: the hardness result targets general halfspaces and small additive error, while the algorithmic result targets homogeneous halfspaces and multiplicative $\tilde{O}(\sqrt{\mathrm{opt}})$ error. The paper would be strengthened by a more explicit discussion of whether the initialization gap is the only obstacle to extending the algorithmic result beyond homogeneous halfspaces, or whether deeper structural barriers remain.

## Suggestions

1. **Address the initialization gap.** Provide either (a) an explicit initialization strategy that guarantees $\theta(\mathbf{v},\mathbf{w}^{(0)}) \in [0,\pi/2)$ with high probability (e.g., random initialization with $\log(1/\delta)$ repetitions), or (b) restate Theorem 3.1 and Lemma 3.4 to explicitly include the initialization condition as a requirement, making transparent that the algorithm requires a warm start. Either resolution would close the gap described above.

2. **Expand the sketch of Proposition 4.5 in the main text** to show how the $6\epsilon$ additive error accumulates from interval discretization and the complement-handling step. Even a short derivation would significantly improve verifiability.

3. **Clarify the relationship between Theorem 3.1 and Lemma 3.4** by stating whether the initialization condition is assumed in Theorem 3.1 or derived within the algorithm.
