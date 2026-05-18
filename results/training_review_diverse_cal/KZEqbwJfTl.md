Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

---

## Summary

This paper studies agnostic conditional classification with halfspace selectors under Gaussian marginals. It provides two main contributions: (1) a polynomial-time algorithm achieving an \(\tilde{O}(\sqrt{\mathrm{opt}})\) approximation guarantee for **homogeneous** halfspace selectors with finite classifier classes (Theorem 3.1), extended to sparse linear classifiers via list learning (Theorem 3.5), and (2) a hardness result showing that for **general** halfspaces, approximating the conditional classification loss within small additive error is computationally hard under the sub-exponential cLWE assumption (Theorem 4.3). The hardness is established via a reduction showing conditional classification is at least as hard as agnostic classification in both additive (Proposition 4.5) and multiplicative forms (Claim 4.7).

## Strengths

1. **First polynomial-time PAC algorithm for agnostic conditional classification with provable approximation.** Theorem 3.1 gives the first guarantee of its kind for this problem. The paper explicitly identifies this as a first result (Section 1.3), and the evidence for the claim is clearly laid out through the combination of Proposition 3.2 (geometric condition linking suboptimality to gradient signal), Proposition 3.3 (convergence of projected SGD), and Lemma 3.4 (inductive argument).

2. **Novel hardness reduction connecting conditional and agnostic classification.** Proposition 4.5 and Claim 4.7 show that any approximation algorithm for conditional classification yields one of the same quality for standard agnostic classification. Combined with known cLWE-based hardness of agnostically learning halfspaces (Lemma 4.6, citing Diakonikolas et al., 2023), this yields Theorem 4.3. This formalizes the intuition that conditional classification is at least as hard as ordinary classification.

3. **Technically interesting use of a ReLU surrogate loss tailored to the one-sided nature of conditional classification.** The paper defines \(\mathcal{L}_{\mathcal{D}}(\mathbf{w}) = \mathbb{E}[y \cdot \max(0, \langle\mathbf{x},\mathbf{w}\rangle)]\) and shows (Proposition 3.2) that when a homogeneous halfspace is suboptimal, the projected negative gradient has a non-negligible component pointing toward the optimal direction. This insight is key to making projected SGD work for the one-sided loss, and the paper's honest discussion of how this differs from prior analyses (lines 67–68) is a sign of careful scholarship.

4. **Clear acknowledgment of limitations.** Section 5 honestly discusses all three major limitations: the restriction to homogeneous halfspaces, the Gaussian marginal assumption, and the sub-optimal \(\tilde{O}(\sqrt{\mathrm{opt}})\) rate. This candor strengthens rather than weakens the paper.

## Weaknesses

### Fatal

None.

### Major

None. While the paper has meaningful limitations, none of the identified issues rise to the level of invalidating its core claims.

### Minor

1. **The gap between positive and negative results (homogeneous vs. general halfspaces) is noted but not interrogated.** The positive result (Theorem 3.1) targets homogeneous halfspaces; the hardness result (Theorem 4.3) targets general halfspaces. The paper acknowledges this in Section 5, but it does not discuss whether the hardness reduction could be adapted to the homogeneous case specifically. If it cannot (and the paper does not argue either way), then the two results address different problem variants, and the narrative that they jointly characterize the problem's difficulty is incomplete. *Severity: minor — the paper is explicit about what each result covers, but the framing could be tightened.*

2. **The convergence analysis of Algorithm 2 (Proposition 3.3) is presented in a way that invites confusion.** The paper states (line 65) that "the goal of Algorithm 2 is not minimizing \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\), but the norm of the projected gradient \(\|\mathbb{E}[g_{\mathbf{w}}]\|_2\)." This is technically true in terms of what is directly bounded, but it obscures the fact that \(g_{\mathbf{w}}\) is precisely the projection of \(\nabla_{\mathbf{w}}\mathcal{L}_{\mathcal{D}}(\mathbf{w})\) onto \(\mathbf{w}^\perp\) — i.e., the Riemannian gradient of \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\) on the unit sphere. The algorithm is therefore doing standard Riemannian SGD on \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\), and convergence of the gradient norm is the standard nonconvex guarantee. The paper's own phrasing makes the connection appear more opaque than it is, which could (and did, in this case) lead a reader to question whether the analysis is sound. The sketch of Proposition 3.3 in the main text is brief but identifies the correct technical challenges (boundedness of \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\) and almost-Lipschitz continuity of the gradient under Gaussian anti-concentration). The full proof is in the appendix (as indicated by references to Theorem A.1), which the parser has removed. *Severity: minor — the concern is about presentation, not correctness; the algorithmic idea is standard once the connection to Riemannian SGD is recognized.*

3. **The polynomial bounds for sparse linear classifiers (Theorem 3.5) are stated only as "poly" without explicit exponents.** While this is common in theory papers that prioritize feasibility over exact rates, the paper would benefit from stating the exponents explicitly, especially since the sample complexity \(\tilde{O}(d/\epsilon^6)\) for the finite-class case (Theorem 3.1) is already specific. *Severity: trivial — does not affect the validity of the result.*

4. **The extra \(\epsilon\) additive term in the multiplicative reduction (Claim 4.7) is acknowledged but could be discussed more directly.** The paper notes it can be made polynomially small, which is acceptable, but the discrepancy between the clean additive reduction (Proposition 4.5, factor 6\(\epsilon\)) and the "near-multiplicative" reduction is slightly under-emphasized when the paper claims both forms. *Severity: trivial.*

### Trivial

- The induction argument in Lemma 3.4 could be described more explicitly to improve reader confidence, though the high-level logic (contrapositive of Proposition 3.2 + angle contraction) is conveyed.

## Nice-to-Haves

- A discussion of whether the \(\tilde{O}(\sqrt{\mathrm{opt}})\) rate is improvable or information-theoretically optimal, perhaps via a lower bound for the conditional classification problem.
- A brief discussion of whether the hardness reduction can be adapted to homogeneous halfspaces specifically, to clarify whether the gap in the paper's scope is intrinsic or merely technical.

## Removed Points

The following points from the Harsh Critic review were removed or downgraded per the filtering rules:

- **"The convergence analysis of Algorithm 2 is not adequately justified and may be flawed."** — Removed as stated. The reviewer's claim that \(g_{\mathbf{w}}\) "is not the gradient of any obvious potential" reflects a misunderstanding: \(g_{\mathbf{w}}\) is the projection of \(\nabla\mathcal{L}_{\mathcal{D}}(\mathbf{w})\) onto \(\mathbf{w}^\perp\), i.e., the Riemannian gradient of \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\) on the sphere. The algorithm is doing standard Riemannian SGD. The paper's own confusing phrasing ("goal is not minimizing \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\)") is a presentation issue, not a flaw in the algorithm or its analysis. The substance of this concern is retained in Minor Weakness #2 above, downgraded from "fatal" to "minor presentation issue."

- **"Significance of the positive result — \(\tilde{O}(\sqrt{\mathrm{opt}})\) is weak compared to constant-factor approximations for standard agnostic classification."** — This compares apples to oranges. Conditional classification is a fundamentally harder problem (the paper shows it is at least as hard as agnostic classification), and the paper is explicit that this is the first result of its kind. Retaining this as a weakness would be an unfair cross-problem comparison.

- **"The proof of Proposition 3.3 is not sketched in enough detail"** — The full proof exists in the appendix (stripped by the parser). The main text sketch, while brief, identifies the correct technical challenges and references the relevant proof technique.

- **"The induction argument in Lemma 3.4 is only briefly described"** — The paragraph explaining the induction (lines 121–122) is actually reasonably complete for a main-text sketch. The logic (contrapositive of Proposition 3.2 → angle contracts → invariant maintained) is conveyed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not already articulate.

## Suggestions

1. Revise lines 63–67 to clarify the relationship between \(g_{\mathbf{w}}\), \(\nabla\mathcal{L}_{\mathcal{D}}(\mathbf{w})\), and the Riemannian gradient on the sphere. A sentence like "Since Algorithm 2 normalizes \(\mathbf{w}\) to the unit sphere at each step, the relevant gradient is the projection onto \(\mathbf{w}^\perp\); the update therefore performs Riemannian SGD on \(\mathcal{L}_{\mathcal{D}}(\mathbf{w})\)" would resolve the confusion.
2. Add a brief discussion (perhaps in Section 5 or a remark after Theorem 4.3) addressing whether the hardness reduction can be adapted to homogeneous halfspaces, or whether homogeneous halfspaces are plausibly strictly easier.
3. Provide the explicit exponent in the polynomial bound for Theorem 3.5 (sparse linear classifiers), as is done for Theorem 3.1.

## Score and Decision

This paper makes a solid theoretical contribution to a well-motivated problem. The positive result is the first of its kind, the negative result is well-connected to existing hardness, and the limitations are honestly discussed. The main concern raised by the harsh reviewer — about the convergence of Algorithm 2 — stems from a misunderstanding that the paper's own phrasing inadvertently invites; it is not a genuine flaw in the analysis. The homogeneous/general halfspace gap is real but acknowledged, and does not invalidate either result on its own terms.

**Originality:** Good — first algorithm for agnostic conditional classification with provable guarantees, plus a novel hardness reduction.  
**Importance:** Moderate — conditional/selective classification is an active area with practical relevance.  
**Claims supported:** Yes, assuming the appendix proofs are correct.  
**Soundness:** The algorithmic framework is sound (Riemannian SGD with a ReLU surrogate).  
**Clarity:** Generally clear; one passage about the algorithm's objective is confusing and should be rewritten.  
**Value:** A meaningful step forward for the theory of selective classification.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>