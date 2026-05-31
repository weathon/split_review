## Summary

This paper introduces the *Dynamic $\ell_p$-Lewis Weight Projection Maintenance* problem, a generalization of the classical projection maintenance data structure (for $\sqrt{W}A$) to matrices of the form $W^{1/2-1/p}A$. The authors propose a deterministic data structure that supports sublinear amortized update and query times, and they extend their approach to the differential privacy setting. The problem is motivated by applications in linear programming, interior-point methods, and leverage-score-based sampling.

## Strengths

- The problem definition is novel and naturally generalizes the widely studied $\sqrt{W}A$ projection maintenance, opening the door to applications involving $\ell_p$ Lewis weights.
- The stated goal—achieving sublinear amortized updates while handling diagonal weight changes—is important and practically relevant for modern convex optimization algorithms.
- The inclusion of a differential privacy extension shows awareness of contemporary data-protection concerns and broadens the potential impact.

## Weaknesses

### Fatal

- **Core claims are unsupported.** The paper provides no rigorous analysis or complete proof of the main result (Theorem 4.1). Key lemmas (Lemma 4.3, 4.4, 4.5, 4.6) are either stated as informal versions, rely on “proof identical to” previous work without adaptation, or are deferred to a missing appendix. The false precision of runtime expressions (e.g., Lemma 4.5: “$O(r g, n^{2+o(1)})$” is meaningless) and the absence of any derivation of amortized bounds make the claimed guarantees impossible to verify.
- **The algorithm description is incomplete and ambiguous.** The UPDATE and QUERY procedures (Algorithms 2 and 3) use variables (e.g., $R_{l,*}$, $R_{*,l}$, $Q_{*,l}$) whose definitions are unclear or inconsistent with the INITIALIZE pseudocode. The role of the sketching matrices $R_{1,*},\dots,R_{L,*}$ is not explained, and the QUERY algorithm computes a result that is never related back to the original projection $P(W)h$ in a precise way.
- **Incoherence between deterministic and randomised guarantees.** The data structure is described as deterministic (“If the input is deterministic, so is the output and the runtime”), yet Theorem 4.1 states an *amortized expected time* that depends on stochastic conditions on the update sequence (involving $\mathbb{E}[\ln w_i]$ and $\text{Var}[\ln w_i]$). The paper never explains how a deterministic data structure can exploit such stochastic assumptions to achieve sublinear expected amortized cost, nor does it provide the necessary probabilistic analysis.

### Major

- **The differential privacy part is a placeholder.** Section 5 lists a series of lemmas (5.3–5.11) all marked as “informal version” and without any proof or concrete instantiation. The DP guarantees are not connected to a specific algorithm with explicit privacy parameters; instead, the section reads like an unmotivated outline. The paper does not demonstrate that the combined DP mechanism yields meaningful privacy–utility trade-offs when composed with the data structure.
- **Dependence on missing appendices.** The paper repeatedly references Appendix C, D, and E for essential technical details (correctness, runtime, sensitivity, utility). Without these, the main text is a hollow shell. A paper must stand on its own at the time of submission; wholesale omission of the proofs invalidates the submission.
- **Self-citations to non-public/unverifiable works.** The DP analysis heavily cites “(Gao et al., 2023b)”, “(Gu et al., 2025)”, and other anonymous references that are not part of the current submission. These are not accessible to reviewers, making it impossible to judge whether the claimed results follow.

### Minor

- The paper lacks a clear comparison with prior projection maintenance data structures (e.g., Cohen et al., 2021b; Lee et al., 2019) that would contextualize the improvement. The novelty is asserted but not quantified: what concrete runtime gains does the $\ell_p$ generalization offer over existing $\sqrt{W}A$ methods?
- Some variable names are inconsistent (e.g., $A$ is $\mathbb{R}^{n\times n}$ in Definition 1.2 but $\mathbb{R}^{d\times n}$ in Theorem 4.1; $m$ appears in Definition 1.2 without clear relation to $n,d$).

### Trivial

- The paper contains a few typographical errors (e.g., “amortized expected time<sup>1</sup>” with footnote out of place) but these are not counted against the contribution.

## Nice-to-Haves

- A concrete instantiation of the DP mechanism with explicit $\epsilon,\delta$ bounds and a comparison with non-private baselines would strengthen the paper considerably.
- An intuitive explanation of the sketching matrices $R_{i,*}$ and why the query algorithm takes $n^{1+b+o(1)}+n^{1+a+o(1)}$ time.

## Novel Insights

None beyond the paper’s own contributions. The problem definition is the main novelty, but the technical depth is insufficient to judge whether any new algorithmic insight emerges.

## Suggestions

- Rewrite the paper so that the main theorem is proven in the main body, at least for the core deterministic part, with explicit amortization arguments. The stochastic/expected extension can be a separate section.
- Remove or properly cite all references that are not publicly available or that are anonymous self-citations to other works under review.
- Clarify the data structure: define the sketching matrices $R_{l,*}$ precisely, specify how $Q$ is maintained, and give a self-contained correctness proof for the QUERY operation.
- Either separate the DP extension entirely (it is currently too sketchy to evaluate) or develop it fully with complete privacy and utility proofs.

## Score and Decision

MY FINAL SCORE: <score>1</score>  
MY FINAL DECISION: <decision>Reject</decision>