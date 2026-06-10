## Summary

This paper proposes a quantum algorithm for sparse online learning based on Langford, Li, and Zhang's truncated gradient descent framework, with applications to logistic regression, SVM, and least squares. The core idea is to use quantum subroutines (inner product estimation, amplitude estimation) to avoid explicitly storing and updating the full O(d)-dimensional weight vector at each iteration, instead computing entries on demand. The paper claims a time complexity of $\tilde O(T^{5/2}\sqrt{d})$ versus the classical $O(Td)$ while maintaining $O(1/\sqrt{T})$ regret, yielding a quadratic speedup in the dimension $d$ at the cost of a worsened $T$-dependence.

## Strengths

1. **Novel and well-motivated algorithmic connection.** The paper makes a creative link between quantum computation and sparse online learning. The observation that in truncated gradient descent the prediction is a single scalar while the update requires O(d) work — and that quantum subroutines can exploit this asymmetry — is genuinely insightful and opens a new direction (lines 85–90).

2. **Explicit update rules for three problems.** Lemma 3.5 (lines 221–231) concretely specifies how each coordinate update is computed for logistic regression, SVM, and least squares within the quantum framework. These are not abstract claims — they give the exact arithmetic expressions that the unitary must implement.

3. **Regret bounds with error accounting.** The theorems (4.1–4.3) explicitly incorporate the estimation errors $\epsilon_{\mathrm{IP}}$ and $\epsilon_{\mathrm{norm}}$ into the regret bound, showing that setting them to $\Theta(1/\sqrt{T})$ preserves the $O(1/\sqrt{T})$ rate. This is a nontrivial step beyond stating an idealized bound.

4. **Comparisons with prior quantum offline algorithms.** The paper provides concrete quantitative comparisons against prior work (Shao 2019 for logistic regression, Li et al. 2019 for SVM), claiming improved parameter dependence in the offline conversion (lines 269, 284).

## Weaknesses

### Fatal
None. The paper's core idea is not invalid; the issues below are fixable with substantial revision.

### Major

1. **Incomplete complexity accounting: query complexity conflated with time complexity, and the per-query cost of weight-vector access is not tracked.** The abstract (line 5) and body refer to a "time complexity of $\tilde O(T^{5/2}\sqrt{d})$," but the theorems (lines 265, 280, 304) formally state only *query* complexity. The paper's own definition (lines 121–122) distinguishes query complexity from time complexity (queries + gates). The central subroutine (Lemma 3.5) costs $O(T)$ per entry of $w^{(t)}$. The inner product estimation (Lemma 3.4) makes $O(\|u\|_\infty\|v\|_1\sqrt{d}/\epsilon)$ queries to its input oracles, and whenever $w^{(t)}$ is one of the vectors, each oracle call requires computing an entry on the fly at $O(T)$ gate cost. This per-query $O(T)$ factor is not multiplied through in the stated complexity, and the paper does not bound $\|w^{(t)}\|_\infty$ either. A complete accounting would need to track both the per-query cost of $w^{(t)}$-oracle calls and the norm factors, and it is unclear whether the claimed speedup survives after this accounting.

2. **The norm dependence in Lemma 3.4 is not tracked through the analysis, threatening the $\sqrt{d}$ speedup claim.** The inner product estimation lemma (line 216) has complexity $O(\|u\|_\infty\|v\|_1\sqrt{d}/\epsilon)$. For $v = x^{(t)}$, Assumption 1(iii) gives $\|x^{(t)}\|_1 \leq C\sqrt{d}$, so the complexity is $O(\|w^{(t)}\|_\infty \cdot C \cdot d / \epsilon)$ — an $O(d)$ dependence, not $O(\sqrt{d})$. The paper neither bounds $\|w^{(t)}\|_\infty$ nor discusses how the $d$-dependence from $\|x^{(t)}\|_1$ interacts with the $\sqrt{d}$ factor in the lemma. Without this analysis the claimed quadratic speedup in $d$ is not substantiated.

3. **Lemma 3.5 — the central computational primitive — lacks sufficient detail to verify its claimed resource costs.** The lemma asserts existence of a unitary that computes any entry $w^{(t)}_j$ in $O(T)$ queries and $O(T+\log d)$ gates, but provides no circuit construction, decomposition, or argument for how the sequential, history-dependent truncated gradient updates (which depend on $\tilde y^{(1)},\dots,\tilde y^{(t-1)}$) can be unrolled into a unitary of depth $O(T)$ operating coherently on each coordinate independently. The paper references generic quantum arithmetic circuits, but for a top venue the core enabling primitive needs substantiation commensurate with its importance.

4. **Offline conversion costs are understated.** The stated offline complexities (e.g., $\tilde O(C^{10}\|u^*\|_2^{10}\sqrt{d}/\epsilon^5)$) do not include the $\tilde O(T^2)$ extra cost acknowledged in Footnote 1 (line 96) for accessing the averaged vector $\bar w$. Since $T = \Theta(1/\epsilon^2)$ for these applications, this adds a factor of $\Theta(1/\epsilon^4)$ that could dominate the stated complexity. The offline complexity claims are therefore incomplete.

### Minor

1. **Regret is bounded for predictions using $\tilde y^{(t)}$, not the true inner product $\hat y^{(t)}$.** The theorems (e.g., lines 262–263) bound regret in terms of loss evaluated at the *estimated* inner product $\tilde y^{(t)}$, whereas the classical algorithm's regret is in terms of $\hat y^{(t)}$. For logistic and hinge loss the gap is $O(\epsilon_{\mathrm{IP}}) = O(1/\sqrt{T})$ (both are 1-Lipschitz), preserving the $O(1/\sqrt{T})$ rate, but this bridge argument is not made explicit. For square loss, the constant-bounded prediction error assumption handles it. The paper should state this reasoning.

2. **SVM learning rate differs dramatically from logistic regression with no explanation.** The SVM uses $\eta = 1/(C^2 T^2)$ (line 275) while logistic regression uses $\eta = 1/(C^2\sqrt{T})$ (line 260). The $1/T^2$ decay means updates become negligible after very few iterations. The paper does not explain why this different rate is needed or how it affects the comparison with the classical algorithm.

3. **The $d \geq \tilde\Omega(T^5)$ regime is acknowledged but its practical implications are not discussed.** For the offline applications proposed ($T = \Theta(1/\epsilon^2)$), the condition becomes $d \gtrsim \epsilon^{-10}$, which is far beyond any realistic dataset. The paper correctly notes this is a limitation (lines 54, 316) but does not give any concrete example or discuss whether any practical high-dimensional learning problem satisfies this condition.

### Trivial
None.

## Nice-to-Haves
- A more detailed derivation of how the $T^{5/2}\sqrt{d}$ complexity arises from the individual subroutine costs would improve readability.
- A bound on $\|w^{(t)}\|_\infty$ under the truncated gradient updates would help clarify the norm-dependent complexity.

## Removed Points
The following points from the input reviews were removed with justification:
- **"Loss functions are not globally Lipschitz"** (Harsh Critic Point 3): Removed as factually incorrect. Logistic loss and hinge loss are both 1-Lipschitz in their argument. The critic's broader concern about bridging the $\tilde y^{(t)}$ vs. $\hat y^{(t)}$ regret gap is valid and kept as a Minor weakness, but with correct justification.
- **"$T^{5/2}\sqrt{d}$ derivation appears internally inconsistent"** (Harsh Critic): The reviewer speculated about the derivation without accounting for all terms the paper might be using. Kept in spirit via the incomplete accounting weakness but removed as a standalone criticism since the derivation is incomplete rather than provably wrong.
- **"Speedup only materializes in nonexistent regime" framing as a fatal weakness**: The paper acknowledges this condition (lines 54, 316) very explicitly. Acknowledged limitations are not fatal flaws. Downgraded to Minor (point 3 above).
- **Several generic/lens-sweep concerns** (speculation about confounders, possible issues with offline comparisons): Removed as unsubstantiated speculation not anchored to specific paper content.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the complexity accounting gap as the most serious issue, which the paper's own framing did not adequately address.

## Suggestions
1. **Separate query complexity and time complexity clearly.** State both in every theorem. Track the $O(T)$ per-query cost of weight-vector access through the inner product estimation subroutine explicitly.
2. **Bound $\|w^{(t)}\|_\infty$** and account for $\|x^{(t)}\|_1 \leq C\sqrt{d}$ in the complexity analysis. Determine whether the $\sqrt{d}$ speedup holds after this accounting, or honestly report the corrected $d$-dependence.
3. **Provide a detailed construction or more rigorous argument for Lemma 3.5.** This is the core enabling primitive; an extended treatment in the appendix is expected at a top venue.
4. **Include the $\tilde O(T^2)$ average-vector access cost** in the stated offline complexities, or qualify the offline claims clearly.

## Score and Decision

**Score:** 4.0 — Weak reject for current form. The idea is novel and interesting, but the complexity analysis has significant gaps (incomplete per-query cost accounting, unaccounted norm dependence, underspecified central lemma) that prevent verification of the core speedup claim. These are fixable with major revision.

**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>