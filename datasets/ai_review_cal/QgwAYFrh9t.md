- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 8, 5
Now I have a thorough understanding of the paper and all the inputs. Let me produce the final consolidated review.

## Summary

The paper studies learning hierarchical polynomials of the form $h = g \circ p$ (with degree-$k$ feature $p$ and degree-$q$ link $g$) using three-layer neural networks trained via layerwise gradient descent. The main result shows that for a structured subclass of polynomials $p$, the learner achieves test error $\widetilde O(d^{-\alpha})$ with $\widetilde O(d^k)$ samples and polynomial time — a strict improvement over kernel methods ($\widetilde\Omega(d^{kq})$ samples). When $p$ is quadratic ($k=2$), the algorithm matches the information-theoretically optimal $\widetilde O(d^2)$ sample complexity, improving over the prior $\widetilde\Theta(d^4)$ result. The key technical innovation is an approximate Stein's lemma showing that the degree-$k$ Hermite projection of $h$ is approximately proportional to $p$.

## Strengths

- **Sample complexity improvement for general-degree hierarchical polynomials**: The paper proves that three-layer networks learn $h = g \circ p$ in $\widetilde O(d^k)$ samples, improving over the $\widetilde\Omega(d^{kq})$ lower bound for kernel methods. This is a clear step beyond prior work that was restricted to quadratic features. (Evidence: Abstract lines 4–5; Section 1.2 "Our Results" at line 22.)

- **Information-theoretically optimal rate for quadratic features**: When $p$ is quadratic, the algorithm achieves $\widetilde O(d^2)$ samples, matching the information-theoretic lower bound and improving over the prior $\widetilde\Theta(d^4)$ result of Nichani et al. (2023). (Evidence: Abstract; Corollary \ref{cor:quad} at line 228; Section \ref{sec:sample_complexity_improvement} at lines 335–342.)

- **Approximate Stein's Lemma as a novel technical tool**: The paper introduces and proves Lemma \ref{lem:approximate_stein}, which bounds $\|\mathcal P_k h - \mathbb E[g'(z)] p\|_{L^2} = O(d^{-1/2})$ and $\|\mathcal P_{<k} h\|_{L^2} = O(d^{-1/2})$, generalizing Stein-type arguments from the quadratic-only setting to arbitrary degree $k$. This is clearly stated as the paper's main technical contribution. (Evidence: Lemma \ref{lem:approximate_stein} at line 262; Section \ref{sec:approximate_stein} at lines 295–321.)

- **Clean modular proof structure**: The training algorithm (Algorithm \ref{alg:layerwise}) is precisely specified with sample splitting, weight decay, and two separate stages. The proof cleanly separates feature learning (Stage 1) from link learning (Stage 2), with each stage analyzed via convex kernel arguments, making the conditions for success transparent. (Evidence: Algorithm \ref{alg:layerwise}; Lemma \ref{thm:kernel_stage1}; Lemma \ref{lem:stage_2}.)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The information exponent assumption ($\mathbb E[g'(z)] = \Theta(1)$) is non-trivial and its restrictiveness is not discussed.** The paper requires $g$ to have a nonzero first Hermite coefficient (Assumption \ref{assumption: zero expectation and information exponent}, line 201–203). This excludes natural link functions such as even polynomials (e.g., $g(z) = z^2$, where $\mathbb E[g'(z)] = 0$). While the assumption is transparently stated and standard in the single-index literature, the paper does not acknowledge this as a limitation or discuss whether the analysis could extend to higher information exponents (e.g., by projecting onto higher-degree Hermite components). Given that the paper aims to show three-layer networks can learn hierarchical polynomials broadly, this restriction deserves explicit discussion. (Evidence: Assumption at line 201–203; the paper's only mention is the phrase "The assumption on $g$, in the single-index model literature … is referred to as $g$ having an information exponent of 1" at line 200.)

- **The characterization of the feature class (Assumption \ref{assumption: on feature p in main text}) is not fully explored.** The assumption requires $p$ to decompose into $L = \Theta(d)$ orthogonal components with balanced coefficients. While two illustrative examples (orthogonally decomposable tensor, sum of sparse parities) are provided, it is unclear how much broader this class is and whether the key insight (that the low-degree Hermite content of $g\circ p$ reveals $p$) extends to more general degree-$k$ polynomials that do not have this orthogonal decomposition. The Future Work section (line 351) acknowledges generalizing to all degree-$k$ polynomials as an open direction, but a more precise characterization of the subclass — even conjecturally — would help readers gauge the scope of the contribution. (Evidence: Assumption \ref{assumption: on feature p in main text} at lines 163–170; remarks at lines 171–198; Future Work at line 351.)

### Trivial
None.

## Nice-to-Haves

- **Stage 2 approximation sketch**: The paper could briefly outline in the main text how $m_2 = d^\alpha$ random ReLU features in one dimension approximate a degree-$r$ polynomial with error $O(d^{-\alpha})$, to give readers intuition for Lemma \ref{lem:stage_2}. (The full proof is in the appendix.)
- **Sensitivity to hyperparameters**: The algorithm requires many hyperparameters set as specific functions of $d, m_1, m_2, n, \alpha, \delta$. A note on whether simpler choices (e.g., no weight decay in stage 2) would suffice would be helpful for practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism about Stage 2 approximation guarantee being unsubstantiated / stronger than typical rates** — The harsh critic questioned Lemma \ref{lem:stage_2}'s claim that $m_2 = d^\alpha$ random ReLU features can achieve $O(d^{-\alpha})$ error, asserting this is stronger than "typical" random feature rates. **Removed because:** (a) The proof of this lemma is in the appendix, which the parser stripped — per the review rules, criticisms that depend on missing appendix content must be removed. (b) The critic's mathematical objection relies on generic Monte Carlo rates for Lipschitz/Sobolev classes, but the target here is a polynomial (degree $r$, infinitely smooth in 1D), so standard lower bounds for non-smooth functions do not directly apply. A polynomial of any fixed degree can be approximated at fast rates by appropriate 1D basis functions; whether random ReLU features achieve the specific rate claimed is a technical question addressed in the appendix proof. Speculating that the proof is unsound without seeing it does not constitute a verified weakness.

2. **Strength about assumptions being "well-motivated"** — The Strength Finder claimed Assumption 3.1 is well-motivated with concrete examples. This is retained in the main review but downgraded from a core strength to supporting context; it is already partially reflected in the "strengths" above.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs did not surface any novel insight about the paper that the paper itself does not already articulate.

## Suggestions

- Add a brief paragraph in Section 4 (Proof Sketch) discussing the information exponent assumption — specifically, acknowledge that $g$ with $\mathbb E[g'(z)] = 0$ is not covered, and state whether the technique could extend to higher Hermite coefficients or whether this is a fundamental barrier.
- In the remarks following Assumption \ref{assumption: on feature p in main text}, add a sentence characterizing the size of the subclass more precisely (e.g., "this includes all degree-$k$ polynomials with $\mathcal P_k p = p$ whose Hermite coefficient tensor has a rank-$L$ decomposition with $L=\Theta(d)$ and bounded spectral norm").
