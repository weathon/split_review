## Summary

This paper develops a general framework for constructing equivariant machine learning architectures that map tuples of tensors to tensors, exploiting symmetries under the orthogonal group O(d), the indefinite orthogonal/Lorentz group O(s,d−s), and the symplectic group Sp(d). The key theoretical result (Theorem 1, Corollary 1 for O(d); Theorem 2, Corollary 3 for the generalizations) characterizes all equivariant polynomial functions via isotropic tensors, providing a practical recipe that avoids Clebsch–Gordan decompositions. Three experimental domains—stress–strain tensors in materials science, path signature estimation, and sparse vector estimation—validate the approach.

---

## Strengths

- **Universal, constructive equivariant parameterization across a broad family of groups**: Theorem 1 and Corollary 1 provide explicit equivariant parameterizations for O(d), while Theorem 2 and Corollary 3 generalize to O(s,d−s) (Lorentz) and Sp(d). This goes meaningfully beyond prior work (e.g., e3nn, escnn) restricted to SO(d) and O(d) for small d=2,3 and relying on Clebsch–Gordan coefficients, which are unavailable in closed form for non-compact or symplectic groups.

- **Strong empirical performance on path signatures with the Lorentz group (Table 2)**: "Ours" achieves a test error of 0.005 vs. 0.186 for the augmented MLP baseline. The comparison is against same-width, same-parameter, and augmented MLPs, so the gain is not a capacity artifact. This is the paper's most compelling experimental result.

- **Materials science results (Table 1)**: The equivariant model achieves test errors 5–10× lower than TFENN (the prior specialized method) across all dataset sizes, demonstrating that the Corollary 2 architecture (permutation-equivariant function of eigenvalues) provides a substantial practical improvement.

- **Sparse vector estimation outside the SoS regime**: Under Accept/Reject with Random covariance, "Ours" achieves ⟨v,v̂⟩² = 0.938 versus SoS's 0.610 (Table 3), showing the learned equivariant model can succeed where existing theoretical methods fail — directly supporting the paper's thesis that enforcing symmetry improves generalization when distributional assumptions are violated.

- **Correct and careful handling of pseudovector parity**: The formulation explicitly includes parity p in the group action (Equation 1, Definitions 1–2) and accounts for pseudotensors via the Levi-Civita isotropic tensor (Lemma 3), capturing physically relevant transformation laws often ignored elsewhere.

---

## Weaknesses

### Fatal
None.

### Major

- **Symplectic group is present in the title and abstract but has zero experimental validation.** Theorem 2 and Corollary 3 cover Sp(d), and Section 5 explicitly confirms: "We use Corollaries 1 and 3 which characterize the O(d)- and Lorentz-equivariant functions…" — no symplectic experiment is included. The abstract states "we showcase our results on three problems" framed as covering all three symmetry groups, which is not accurate. The title "Tensor Learning with Orthogonal, Lorentz, and **Symplectic** Symmetries" commits to a scope that the experiments do not cover. Either a synthetic symplectic experiment should be added or the title/abstract must be scoped back to reflect what is actually demonstrated.

- **Underperformance of the full O(d)-equivariant model under Identity covariance is unexplained.** In Table 3, "Ours" scores 0.190, 0.342, and 0.197 for Accept/Reject, Bernoulli-Gaussian, and Corrected BG under Identity covariance — all substantially below "Ours (Diag)" (0.351, 0.908, 0.239 respectively) and, in the BG-Identity row, far below the MLP baseline (0.342 vs. MLP's 0.196 being very close at top). Under Identity covariance the noise is isotropic and O(d)-equivariance should be the ideal inductive bias; this is precisely where the model should have the largest advantage. The table caption explains why SoS wins ("SoS assumptions are met"), but never explains why the full equivariant model underperforms its own "Diag" ablation or, in some rows, approaches random performance. This is not merely a missing discussion — it calls into question what the cross inner-product features are actually contributing.

### Minor

- **"Ours (Diag)" ablation is more informative than the text acknowledges.** "Ours (Diag)" outperforms "Ours" in 6 of 12 settings in Table 3, and the 6 cases all cluster at Diagonal and Identity covariances. This pattern — cross inner products help under Random covariance but hurt or are neutral under structured covariance — is a substantive finding about when the richer equivariant features contribute value versus potentially overfitting. It is mentioned only by its presence in the table; no paragraph in the main text discusses it.

- **The Discussion's claim "equivariant models outperform all non-equivariant baseline models" is imprecise.** Reading Table 3 directly: for Accept/Reject Identity, "Ours" scores 0.190 while "MLP baseline" scores 0.196 — the equivariant model does not outperform the non-equivariant one. The sentence in Section 6 is an overstatement and should be qualified (e.g., "in most settings" or "when the Random covariance condition holds").

### Trivial

- **"Universally expressive" in the abstract is slightly oversold.** Remark 1 already acknowledges uncertainty: "We are unsure if a characterization of this sort can be stated for all continuous O(d)-equivariant functions." The word "universally" in the abstract should be qualified or cross-referenced to Remark 1.

---

## Nice-to-Haves

- A brief empirical runtime or memory comparison with e3nn or escnn on a standard task would substantiate the claim that Corollaries 1 and 3 are "comparable" in efficiency to Clebsch–Gordan methods. The theoretical equivalence is argued but not measured.
- Investigation into varying the spacetime dimension or applying the Lorentz path signature model to real particle physics data would considerably deepen the contribution.
- A short cross-reference from the end of Section 4 to Corollary 3's concrete bilinear form instantiation would help readers connect the abstract character χ to the specific experiments.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — Corollary 2 is well-known from the spectral theorem**: The authors do not overclaim novelty for Corollary 2; the spectral-theorem reduction is used correctly as a structural result to justify the materials science architecture. The architecture's superiority over TFENN could be explained more fully, but this is a nice-to-have, not a weakness. Removed as a strawman (the authors never claim Corollary 2 is novel in isolation).

- **Harsh Critic — Section 4 presentational gap re: characters χ**: This is a minor exposition preference; the cross-reference would help readability but does not constitute a weakness in the technical content. Moved to Nice-to-Haves.

- **Strength Finder — "Empirical superiority across diverse tasks"**: As stated ("consistently outperform"), this is overstated. The materials science and path signature results are strong, but the sparse vector results are mixed. Retained only with appropriate qualification.

- **Strength Finder — "Effective operation outside theoretical guarantees"**: Valid only for the Random covariance condition; inflated to cover all of Table 3 by the Strength Finder. Retained with narrowed scope.

---

## Novel Insights

The most genuinely novel insight from this review synthesis is that the "Ours (Diag)" ablation — which uses only per-vector norms rather than all pairwise inner products — systematically *outperforms* the full equivariant model under Diagonal and Identity covariances while underperforming under Random covariances. This covariance-dependent inversion of the cross-product features' utility suggests a non-trivial interaction between the covariance structure of the input distribution and the utility of off-diagonal equivariant features. This is richer than a simple overfitting story and could be a productive direction for theoretical work on when richer equivariant features help versus hurt — but the paper currently leaves this entirely unanalyzed.

---

## Suggestions

1. **Most impactful**: Add even a minimal synthetic experiment for the symplectic group (e.g., a toy Hamiltonian dynamics prediction task), or explicitly retract the symplectic claim from the title and abstract. The current gap between the title's promise and the experimental scope is the paper's biggest credibility risk.
2. Add a dedicated paragraph in Section 5 analyzing the covariance-dependent behavior of "Ours" vs. "Ours (Diag)" — specifically why cross inner-product features help under Random covariance but hurt under Diagonal/Identity covariance. Connecting this to variance estimation or identifiability arguments would turn a mixed result into a positive contribution.
3. Qualify the Discussion's claim "equivariant models outperform all non-equivariant baseline models" to reflect that this holds in most but not all rows of Table 3.
4. Qualify "universally expressive" in the abstract to point to Remark 1's caveat about Stone–Weierstrass approximation.

---

## Score and Decision

**Originality**: Strong — the invariant-theory route to equivariant parameterization is distinct from Clebsch–Gordan methods and is the first to cover Lorentz and symplectic groups in a machine learning framework at this generality.
**Importance**: Moderate-to-high — groups like the Lorentz group are foundational in physics and underserved in equivariant ML.
**Claims supported**: Partially — O(d) and Lorentz claims are well-supported; symplectic claims are not experimentally demonstrated; sparse vector generalization claim is overstated in the Discussion.
**Soundness**: Good — theory is correct and the main experimental results (path signatures, materials science) are convincing and carefully controlled.
**Clarity**: Good overall; the sparse vector analysis section leaves important questions unanswered.
**Community value**: High for physics ML and geometric deep learning communities.

The paper makes real, verifiable contributions and should be accepted. The symplectic experimental gap and the unexplained sparse vector behavior are the two issues authors must address in revision; neither invalidates the central theoretical contribution or the strong Lorentz/materials science results.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>