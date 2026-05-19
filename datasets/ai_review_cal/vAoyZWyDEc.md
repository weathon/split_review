- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 1, 3
Now I have thoroughly verified the paper's content against the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper studies the computability of approximating global optima of non-convex functions in an oracle model (where function values are obtained through queries). It attempts to prove that (1) computing an ε-approximation to the global optimum is not computable, (2) gives a necessary and sufficient condition for approximability expressed via a predicate Q, and (3) presents an algorithm that converges when a "basin of attraction" size is known, with numerical experiments. The paper's central contribution is the noncomputability claim, which it frames as "much stronger" than NP-hardness.

## Strengths

- **Clear problem framing and real-world motivation.** The oracle model is explicitly described (Section 1.3), and the paper draws connections to practical problems where functions are only known through queries (portfolio optimization, chemical process optimization, neural network training). The distinction between NP-hardness and incomputability is a valid and interesting framing.

- **Awareness of the need for global properties.** The paper correctly identifies that additional global knowledge (Lipschitz constant, basin of attraction size, etc.) can make the otherwise intractable problem of global optimization computable, and attempts to formalize this via Theorem 3.4.

## Weaknesses

### Fatal

- **The proof of the main noncomputability result (Theorem 2.6) has an unbridgeable gap; the central claim is not established.**  

  Theorem 2.6 claims that no algorithm can compute an ε-approximation to the global optimum. Its proof relies on Lemma 2.4 (undecidability of deciding whether a given point is an ε-approximation), which in turn attempts a reduction from the undecidable "identically zero" problem (Lemma 2.3).  

  The proof of Lemma 2.4 (lines 116–118) reads in full:  
  > "Now consider the problem of deciding if a (non-convex) negative function f is identically zero. This problem is unsolvable by Lemma 2.3. Since the function is negative, it is identically zero if and only if the global minimal value is zero. Similarly the function f'(x) = max{0, f(x) + ε} is identically zero if and only if the ε-approximation to the global minimal value is zero. Thus, we have a reduction from the problem of deciding if a function is identically zero to the problem of deciding if the global minimal value is zero. Thus our problem is unsolvable by Lemma 2.3."

  **The gap:** The lemma's statement is about "deciding if a point x_k is an ε-approximation to the global optima." But the proof reduces the identically-zero problem to a different problem — "deciding if the global minimal value is zero" — and never connects this to the specific claim about deciding membership of a particular point. The step from "global minimum value is zero" to "this specific point is/is not an ε-approximation" is absent. Lemma 2.5 merely says "the proof is similar" without filling this gap. Since Theorem 2.6 depends on Lemma 2.4 (via a contradiction argument), the paper's central contribution is unsupported by the reasoning provided.

  This is not a minor presentational issue — the core claim the paper advertises ("much stronger than NP-hardness") is not properly proved.

### Major

- **Theorem 3.4 (the characterization of when global optima are computable) is not rigorous and does not constitute a meaningful contribution.**  

  The proof (lines 161–163) makes several unjustified leaps:  
  - It states that "inverse of a surjective recursive function is recursive" and uses this to claim that from y₀ and ζ one can compute an x₀ satisfying P^f(x₀, y₀) = Q(ζ, x₀, y₀). No mechanism is given for how such an x₀ would be computed in a continuous domain, nor is the connection to "surjective recursive function" explained in context.  
  - It asserts that the constructed sequence {x_k} converges to the global optimum x^* because "P^f(x,y) defines a partial order with f(x_k) ≤ f(x_{k-1})." Monotonic decrease alone does not guarantee convergence to the global minimum.  
  - The second direction ("if the global optimizer is computable then there exists such a predicate") is trivial: choosing ζ = ||x^*|| and Q(ζ, x, y) as some function depending on ζ does not yield a substantive characterization.

  The section attempts to give a necessary and sufficient condition but the reasoning is too vague to be considered a theorem. This contribution as written does not advance the paper's goals.

- **Lemma 5.2's proof assumes the minimum over all non-global local minima of the gap δ is well-defined and positive, without justification.**  

  The proof (line 219) defines δ = min_{\tilde{x}} δ_{\tilde{x}} over all local minima that are not global. For a general continuous non-convex function on a compact domain, there may be infinitely many local minima; the minimum of their gaps may not be attained or could be 0 (e.g., if local minima accumulate toward the global minimum). The proof does not address this, and the lemma's conclusion — that the algorithm's iterates eventually remain in an arbitrarily small ball around x^* — is not established on the basis of the reasoning given.

- **The algorithm in Section 4 provides no discussion of how the critical parameter m (basin of attraction size) could be obtained in practice.**  

  The paper acknowledges that knowing m is a strong assumption, but the numerical experiments (Section 6) simply list m values for each test function (e.g., m=2 for Beale, m=10 for Rastrigin) without any justification. The experiments therefore amount to gradient descent initialized from a grid point tuned to be inside the basin — a standard multi-start method — and do not validate the paper's claims about computability. No baseline comparisons (e.g., random multi-start, gradient descent alone) are provided.

### Minor

- **The algorithm description (Section 4) is vague.** No pseudo-code is given; the description (lines 186–188) states the algorithm "finds the point z_k where the function takes a minimum amongst all points at a distance of m from each other and does a gradient descent step" but does not specify how the grid search and gradient descent are interleaved, stopping criteria, or how the grid resolution relates to m.

- **Lemma 2.3's proof (line 114) is a standard adversarial argument but is too brief to be satisfying in a formal setting.** It does not specify how the counterexample function g' is constructed (e.g., via a bump function) to be continuous and agree with g on all queried points while differing elsewhere.

### Trivial

- The paper would benefit from a pass to clean up minor notation issues (e.g., the overbar formatting in Lemma 2.4's f' appears garbled).

## Nice-to-Haves

- A proper noncomputability proof would likely require a constructive adversarial argument (e.g., constructing a family of functions that differ only in a small unqueried region around the optimum). The paper might benefit from adopting such a direct approach rather than the attempted reduction.
- A more thorough review of related work on black-box complexity and no-free-lunch theorems would help contextualize the noncomputability claim.
- The experiments would be strengthened by comparisons with baselines (gradient descent alone, random restart) and by sensitivity analysis with respect to the assumed m value.

## Removed Points

- Criticisms about "missing related works" — hard rule prohibits mentioning missing related works without external sources.
- Criticisms about "typos, formatting, garbled characters" — these are parser artifacts, not paper problems.
- Criticisms about reproducibility of trivial implementation details (e.g., undisclosed hyperparameters) — hard rule removes.
- The claim that "the assumption of finite-precision numbers is not justified in detail" — the paper does provide a justification (Section 1.2; Remark 2.10) so this criticism is strawman.
- Several speculative concerns about Lemma 5.2's assumptions being "not guaranteed by the algorithm" — these are partially conflated with the real issue about δ not being guaranteed to exist, which is kept in Major.
- Strength Finder's claimed strength #1 ("reduction from undecidable identity problem") — this reduction is the flawed part; it is not a real strength as the reduction is incomplete.
- Strength Finder's claimed strength #2 ("characterization of when global optima are computable") — the section is not rigorous and does not constitute a genuine contribution as written.

## Novel Insights

None beyond the paper's own contributions. The paper's core idea — that global optimization is not computable in an oracle model — is not new in spirit (e.g., the well-known difficulty of black-box optimization, adversarial constructions for zeroth-order methods), and the attempted formal proof is incomplete. The characterization in Section 3 and the algorithm in Section 4 do not produce any insight beyond what is already known (e.g., that Lipschitz continuity or knowledge of a basin of attraction can make optimization tractable).

## Suggestions

1. **Repair or replace the noncomputability proof.** The current reduction from the "identically zero" problem to the membership problem for ε-approximation is incomplete. Either fix the reduction (making explicit how checking an oracle query's response connects to undecidability) or adopt a direct adversarial construction: for any finite query budget, construct a function that differs from zero only in a small ball around the global optimum, which the algorithm cannot detect.
2. **Remove or substantially rewrite Section 3.** The current "necessary and sufficient condition" (Theorem 3.4) is not a rigorous result. Either replace it with a concrete, well-known sufficient condition (e.g., Lipschitz continuity with known constant) properly proven, or remove it entirely.
3. **Provide a clear, implementable pseudo-code for the algorithm** and discuss how the basin size m could be estimated or bounded in practice.
4. **Strengthen the experiments** by including baseline comparisons (random initialization, gradient descent alone, random multi-start), and by showing how sensitive convergence is to the chosen m value.
