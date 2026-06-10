## Summary

This paper introduces the $k$-multilinear extension for $k$-submodular functions (Definition 2.4) — a continuous relaxation over the domain $\Delta_k^n$ that generalizes the classic multilinear extension (recovered when $k=1$). Using this extension, the authors propose a unified Frank-Wolfe-type framework for constrained $k$-submodular maximization under matroid constraints, knapsack constraints, and their intersections. The main claimed results are: (1) an asymptotically tight $1/2$-approximation for monotone $k$-submodular maximization with $O(1)$ knapsack constraints or a single matroid, improving over the prior $1/3$; and (2) a $1/3$-approximation for non-monotone objectives under the same constraints, improving over the prior $\sim 0.245$—$0.317$.

## Strengths

**1. Novel definition of the $k$-multilinear extension with stated structural properties.** The paper formally defines $F(\mathbf{x}) = \mathbb{E}[f(\mathbf{s})]$ over $\Delta_k^n$ (Definition 2.4, lines 114–120) and identifies several analytical properties — multilinearity, element-wise non-positive Hessian (Eq. 3), approximate linearity (Ineq. 4), pairwise monotonicity (Lemma C.1) — that are individually cited in the algorithmic analysis. Extending the multilinear-extension toolkit from submodular ($k=1$) to $k$-submodular functions is a conceptually useful step, given the success of continuous methods in the submodular literature.

**2. Asymptotically tight $1/2$-approximation for monotone knapsack constraints.** The paper achieves $1/2-\varepsilon$ for $O(1)$ knapsacks, matching the $(k+1)/(2k)$ lower bound asymptotically in $k$ and eliminating the $d$-dependency that plagued the prior $1/(2(1+d))$ result (Gong et al., 2024). The analytic core (Lemma 3.3, line 198) uses a pseudo-convex-combination auxiliary point $\mathbf{o}(t) = \mathbf{x}(t) + (1-t)\mathbf{o}^\star$ to circumvent the closure issue of $\Delta_k^n$, a clean idea that is explained in the main text.

**3. Unified framework handling multiple constraint types.** The same continuous optimization stage (Algorithm 1) is claimed to accommodate monotone and non-monotone objectives, matroid constraints, $O(1)$ knapsack constraints, and their intersections. This contrasts with prior work that designed separate combinatorial algorithms for each setting and extends the constraint classes covered (e.g., $O(1)$ knapsacks with $b$ matroids, vs. prior work limited to a single knapsack with $b$ matroids).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

**1. The approximate linearity and pairwise monotonicity proofs are entirely deferred to the appendix, making the main text's core analytic steps opaque.** The paper's central inequalities — Ineq. (4) (approximate linearity, line 134–138) and the use of "pairwise monotonicity" for the non-monotone case (line 74) — are stated as properties of the $k$-multilinear extension, with the statement that they are "summarized in Lemma C.1" (line 140). For a theory paper whose claimed results depend entirely on these properties being provably true for $k>1$, the main text provides essentially no derivation or even a sketch of why the standard submodular proof techniques extend. A reader cannot assess whether the extension is straightforward (e.g., the expectation still factorizes across items, so Hessian calculations carry through) or whether subtle obstacles arise from the $\Delta_k^n$ domain. This is especially consequential for the non-monotone $1/3$ result (Theorem 1.2), whose entire justification is the pairwise monotonicity property and whose proof is only in Appendix F. *Why it matters*: The paper's core mathematical claims are unverifiable from what is presented in the main sections; the appendix would need to be correct for the paper to be sound.

**2. The $1/3$ non-monotone improvement over prior work is modest and the baseline framing in the abstract is selective.** The abstract highlights a $0.245 \to 1/3$ improvement for the non-monotone case, but Section 1.3 (line 85) acknowledges concurrent work (Xiao et al., 2023) achieving $0.317$ for the same single-knapsack setting. The actual improvement over the strongest prior result is $\sim 1.6$ percentage points ($0.317 \to 0.333$). While any improvement is legitimate, the abstract's framing (citing the weaker $0.245$ from Ha et al., 2024) overstates the advance. *Why it matters*: It inflates the perceived significance of the non-monotone results.

**3. The asymptotic optimality claim conflates asymptotic-in-$k$ optimality with optimality for all finite $k$.** The paper states the $(k+1)/(2k)$ lower bound (line 44, 56) and claims its $1/2$ result "aligns" with it and is "asymptotically tight." This is accurate as stated, but the paper does not clarify whether $(k+1)/(2k)$ is a hardness-of-approximation bound (no algorithm can exceed it for any $k$) or an algorithm-dependent bound — and for small $k$ (e.g., $k=2$ gives $3/4$), the gap between $1/2$ and $3/4$ is large. A sentence clarifying the status of this bound would prevent over-interpretation. *Why it matters*: The current framing could mislead readers into thinking a tighter result has been proven.

**4. The rounding scheme description is too brief to verify that it handles $k>1$ states rigorously.** The paper claims the rounding "is an extension of the approaches developed for submodular maximization" (line 192), and for the matroid case "the rounding procedure is directly applied to the output of FW" (line 192). Since constraints are defined on the support set (Definitions 2.1, 2.2), the rounding only needs to decide which elements are selected — plausible, but the paper does not argue why standard swap-rounding analysis (Călinescu et al., 2011) carries through when the fractional input is a $k$-multilinear extension solution rather than a standard multilinear extension solution. *Why it matters*: If the rounding loses the $\alpha$ guarantee for $k>1$, the overall approximation ratios fall.

**5. Query complexity for knapsack constraints is enormous ($O(k^{\text{poly}(1/\varepsilon)} n^{\text{poly}(1/\varepsilon)})$) and acknowledged but not contextualized.** The paper notes this complexity is larger than combinatorial methods (line 172) but does not discuss what $\text{poly}(1/\varepsilon)$ concretely means (e.g., degree of the polynomial) or how the constants compare with prior enumeration-based methods. *Why it matters*: For practical relevance, the gap between the asymptotic guarantee and actual computational cost matters.

### Trivial

- The non-monotone case assumes $k \geq 2$ (Theorem 1.2). The paper does not explain why $k=1$ is excluded — either the proof fails (which would be surprising) or the condition is an artifact.
- Eq. (3) (the Hessian expression) is garbled by parser artifacts; the intended mathematical content is clear from context.

## Nice-to-Haves

- A self-contained statement of what the $(k+1)/(2k)$ lower bound (Iwata et al., 2016) applies to (knapsack? matroid? general?) would greatly improve clarity.
- A brief explanation of why the approximate linearity inequality (Ineq. 4) follows from the Hessian bound and Taylor expansion — even a 3-line sketch — would make the main text self-contained enough to follow the proof of Lemma 3.3.

## Removed Points

- The harsh critic claimed the approximate linearity proof "is not established in the main text" and that its correctness is "unclear" — this is a standard deferral to the appendix for a theory paper; the property is stated (Ineq. 4) and attributed to Lemma C.1.
- The harsh critic claimed the rounding scheme "glosses over how the $k$ states per element are resolved" — the constraint definitions are support-set-based, and the paper explicitly mentions enumerating $k$ assignments for large elements (line 192). This is sufficient for a main-text overview.
- The harsh critic's claim that the Hessian property does not suffice for the approximate linearity inequality is incorrect: the inequality follows from bounding the quadratic Taylor remainder, not from concavity. The Hessian entries are bounded because $F$ is multilinear over a bounded domain.
- The harsh critic's complaints about Algorithm 1 not being displayed, missing derivation of query complexity, and generic conclusions — these are all standard scope choices for an 8-page theory paper.
- Complaints about "formatting artifacts" and "unreadable image" (Table 1) are parser issues, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a 3–4 line sketch in Section 2 showing why the approximate linearity inequality (Ineq. 4) follows from the Hessian bound (Eq. 3) and a second-order Taylor expansion. This would make the proof of Lemma 3.3 followable in the main text.
- Clarify the status of the $(k+1)/(2k)$ lower bound: is it a hardness bound (no algorithm can exceed it) or an algorithm-specific bound? State this explicitly.
- Add a sentence explaining why $k \geq 2$ is required for the non-monotone case.
- In the abstract, either cite the strongest prior bound (0.432/0.317 from Xiao et al., 2023) or qualify the improvement as "over the prior $1/3$ combinatorial result" to avoid selective baselining.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>