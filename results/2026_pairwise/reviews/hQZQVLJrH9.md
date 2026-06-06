Now I've read the paper carefully. Let me synthesize the draft review before running calibration searches.Now running 5 calibration searches across all bands:Now let me read a few of the most comparable calibration papers to select anchors:Now I have everything I need to write the final consolidated review.

---

## Summary

This paper proposes Influence-Aligned Steering (IAS), a first-order framework that unifies activation steering and training-data influence functions by identifying both as projections of the same underlying Jacobian sensitivity tensor. The central theoretical contribution is a constructive duality: any steering vector can be represented as a signed measure over training data and vice versa (Theorem 4.2), with the scalar γ(x)—the cosine of the smallest principal angle between two Jacobian image subspaces—quantifying when this equivalence is achievable. Supporting results include generalization bounds for low-rank steering, a spectral recipe for optimal directions, and a no-free-lunch impossibility result. Proof-of-concept experiments on GPT-2 Medium and ResNet-50 provide partial empirical grounding.

---

## Strengths

- **Constructive first-order duality with closed-form formulas**: Theorem 4.2 and the IAS construction (Section 3.2, Eq. 2) provide an explicit algebraic bridge—not merely a conceptual analogy—between activation steering and influence functions. The paper is, to the best of the reviewers' knowledge, the first to provide this constructive map with accompanying error bounds.

- **γ as a principled, computable feasibility diagnostic**: The scalar γ(x) (smallest principal-angle cosine between Im(J_{h→y}) and Im(J_{θ→y})) functions both as an upper bound on steering fidelity (Theorem 5.1: relative error ≤ √(1−γ²)) and as the basis for a no-free-lunch lower bound (Theorem 6.2). Figure 2 shows it rising monotonically from 0.64 to 0.94 across GPT-2 Medium layers, making it concretely actionable. This is a useful tool for the steer-vs-retrain decision that neither line of prior work provides.

- **Generalization bound for low-rank steering (Theorem 6.1)**: The Rademacher complexity increment αL√(2k/dn) — vanishing as layer width d and sample size n grow — provides formal learning-theory backing for the low-rank steering recommendation. This bridges the controllability and generalization perspectives cleanly.

- **Spectral optimality recipe with empirical validation**: Theorem 5.3 identifies the top eigenvector of Σ (Fisher-influence matrix) as the maximum-logit-change direction under an ℓ₂ budget; Figure 3 confirms it lies in the far tail of the null distribution (z=3.55, p=0.00498) on ResNet-50.

---

## Weaknesses

### Fatal
None.

### Major

- **IAS is strictly dominated by CAA on both metrics in Table 1, with no explanation.** Table 1 (Section 7.1) shows IAS achieves mean toxicity 0.0164 vs. CAA's 0.0150, and perplexity 13701 vs. 13291—losing to CAA on both reported metrics. The paper presents IAS as a minimum-norm, principled, influence-optimal steering direction, yet the hand-crafted contrastive direction (CAA) performs strictly better. No ablation or analysis is offered: not on the quality of the influence Hessian approximation, not on whether 50 contrastive examples suffice for a reliable influence signal, not on layer choice sensitivity. This is not a minor limitation to note in passing—it is the primary downstream experiment, and the result contradicts the paper's claim of principled improvement over existing steering. A paper whose main practical claim (IAS improves on ad-hoc steering) is falsified in its own experiment requires either an explanation that restores coherence or a significantly more modest framing of the practical contribution.

- **The Corollary 1 proof is wrong as written.** The "idea of the proof" (Section 4.1) states: "If another measure ν achieved the same shift with smaller ℓ₁ norm, one could scale ρ_s down and still match the shift, contradicting the definition of α as the steering magnitude." This argument is invalid: since the map ν ↦ ∑ ν(z)I(z→x) is linear, scaling ρ_s down scales the logit shift proportionally, so a scaled-down ρ_s would no longer reproduce the same shift. The ℓ₁-minimality claim may still hold under the stated affine-independence assumption (e.g., via a uniqueness argument), but the given proof sketch is structurally incorrect and must be replaced.

- **The slope of 1.50 in Figure 1 is inconsistently characterized as "consistent with the linear regime."** Section 7.2 reports cosine 0.978 (directions match well) but slope 1.50 (magnitudes are systematically underestimated by 50%). For a paper whose entire apparatus—IAS construction, error bounds, Corollary 2—rests on first-order Taylor accuracy, a 50% systematic underestimate of the realized shift magnitude is not negligible. The paper does not report the perturbation magnitude α, making it impossible for readers to assess whether the tested setting genuinely qualifies as "small." The cosine alone is not sufficient to validate a first-order approximation framework that also makes magnitude predictions.

### Minor

- **Limited experimental scale contradicts the claim of billion-parameter applicability.** Section 1 states that "all quantities reduce to Jacobian-vector products and pseudo-inverses" and that the method scales to billion-parameter models. All language-model experiments use GPT-2 Medium (~345M parameters), and Figure 2's γ-depth analysis is restricted to this one architecture. Whether the monotone increase in γ with depth generalizes to larger models, and whether IAS vs. CAA performance relationships persist at scale, are open questions that the paper does not address.

- **The abstract's use of "equivalent" without qualification overstates generality.** The paper correctly lists the feasibility condition Im(J_{θ→y}) ⊆ Im(J_{h→y}) as Assumption (i) in Section 2, but the abstract reads "we prove that, to first order, these techniques are *equivalent*" without this caveat. Without feasibility, only the approximate bound of Theorem 5.1 applies. More careful scoping in the abstract and introduction would improve accuracy.

### Trivial

- Lemma 5.4 displays the equality γ₁γ₂ = √(1−(1−γ₁²))·√(1−(1−γ₂²)), which algebraically reduces to γ₁γ₂ and adds no content. The equality is a tautological rewrite that takes up display space without illuminating anything.

---

## Nice-to-Haves

- **Validation of the steering→data attribution direction.** A natural experiment would insert a known-causal training document inducing a specific behavior, apply the steering→ρ_s mapping, and verify ρ_s assigns high weight to that document. Without this, the attribution claim ("pinpoints the fewest causal training examples") is entirely theoretical.
- **Diagnosing the IAS vs. CAA gap** via ablation: larger contrastive sets, better Hessian approximations, or layer sweeps. Even if IAS underperforms, diagnosing *why* would make the paper internally coherent and useful for practitioners.
- **γ distribution at larger scales** (7B, 70B LMs) to determine whether the monotone depth increase is architecturally general or a GPT-2 artifact.
- **Discussion of influence-function fragility** (Basu et al. 2021, cited in references) and its implications for IAS reliability, since IAS inherits the faithfulness of the underlying influence estimates.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **[REMOVED — Strength Finder] "First-order equivalence verified at scale."** The 5000 pairs on GPT-2 Medium is not "at scale," and the slope of 1.50 partially undermines the claim. Conflicts with a verified weakness; dropped.

2. **[REMOVED — Strength Finder] "Minimal-ℓ₁ data re-weighting derived from steering" as a confirmed strength.** The proof of Corollary 1 is wrong as written; this cannot be counted as a validated strength until the proof is corrected.

3. **[REMOVED — Harsh Critic] "Theorem 6.2 is trivial—a direct consequence of the definition of γ."** The proof is indeed immediate, but the practical framing (a computable diagnostic for when to abandon steering) is a contribution beyond proof novelty. Retained only at Trivial level (packaging/labeling), not as a substantive weakness.

4. **[REMOVED — Harsh Critic] "The primal–dual framing inflates a pseudoinverse projection."** While arguably grandiose, the framing is not wrong, and stylistic framing choices are not weaknesses.

5. **[REMOVED — Harsh Critic] "Basu et al. (2021) showed influence functions are fragile—this threatens IAS."** The fragility concern is real but: (a) the paper cites Basu et al. in its references; (b) the paper uses damped Hessian inversion specifically for stability; (c) fragility in influence estimation is a known limitation of the whole field, not a specific flaw of this paper. Moved to Nice-to-Haves.

6. **[REMOVED — Harsh Critic] Speculation that the appendix proof is missing.** The parser strips appendices; missing appendix material cannot be treated as absent from the original submission.

7. **[REMOVED — Harsh Critic] "The practical workflow is undemonstrated end-to-end."** True, but this is appropriately scoped as future work / Nice-to-Have rather than a fatal flaw of a theoretical paper.

---

## Novel Insights

The most genuinely novel contribution is γ(x) as a cross-tool feasibility diagnostic: it provides, in a single computable number derived from two small SVDs, a principled answer to the question "can steering substitute for weight-space editing on this input?" This framing—of Jacobian subspace geometry as a decision criterion for algorithm selection—does not appear in either the activation-steering or the influence-function literature. The layerwise composability bound (Lemma 5.4), suggesting multiplicative alignment degradation across layers, is a useful structural observation. Together, these results give practitioners a geometric vocabulary for reasoning about the relationship between weight-space and activation-space interventions, which is genuinely new.

---

## Suggestions

1. **Fix the Corollary 1 proof.** Under the stated affine-independence assumption, a valid argument proceeds via uniqueness: affine independence of {I(z→x)} implies the decomposition is unique, hence ρ_s with ‖ρ_s‖₁ = |α| is the sole solution and trivially ℓ₁-minimal. State this explicitly.
2. **Report α (steering magnitude) in Section 7.2** and the range of perturbation sizes explored, so readers can assess whether the tested regime qualifies as "small" and why a 1.50 slope rather than ~1.0 arises.
3. **Address the IAS vs. CAA gap in Table 1** with at least a diagnostic ablation, or reframe the practical contribution more modestly (IAS as a principled attribution tool rather than a practical performance improvement over CAA).
4. **Add at least one experiment on a 7B-class LM** to support the billion-parameter scalability claim.
5. **Moderate the abstract** to note that the "equivalence" is conditional on the feasibility assumption Im(J_{θ→y}) ⊆ Im(J_{h→y}), consistent with Section 2's Assumption (i).

---

## Evaluation on Key Axes

- **Originality**: High. The constructive first-order duality between activation steering and influence functions, and the γ principal-angle diagnostic, are new contributions not present in either prior literature strand.
- **Importance of research question**: High. Connecting steering and data attribution is a meaningful problem for interpretability and AI safety.
- **Claims well-supported**: Mixed to poor. The γ diagnostic is supported by Figure 2. But the primary practical claim (IAS improves on CAA) is directly falsified by Table 1, and the slope discrepancy in Figure 1 is inadequately addressed.
- **Soundness of experiments**: Weak. Only GPT-2 Medium evaluated for the main claim; the single downstream task shows IAS losing; the validation experiment (Figure 1) is against random directions only.
- **Clarity of writing**: Good. The paper is well-organized and the geometric intuition is communicated clearly.
- **Value to the research community**: Moderate. The γ diagnostic and duality framework have real value; however, the experimental shortcomings prevent establishing whether IAS is practically useful.

---

## Score and Decision

The paper occupies the upper end of the 4–5 range: it has genuine theoretical novelty (γ diagnostic, first-order duality) that places it above marginal or weak submissions, but is pulled down by a falsified main experiment (IAS strictly dominated by CAA), a wrong proof (Corollary 1), a poorly explained slope discrepancy (1.50 in Figure 1), and overstated billion-parameter claims. Among comparable calibration anchors, "From Steering Vectors to Conceptors" (score 5.0, Reject)—a theoretical steering paper with formal results but weak empirical validation—is the closest comparator. The paper under review has comparable theoretical depth but a more damaging empirical situation (its own experiment contradicts its practical claim).

**Score: 4.5 / Reject**

---

# Selected Anchors

<related>["z1yI8uoVU3", "fdvSCcB7i8", "qJkCEcd50n", "9wjGUN65tY", "egHptuv7hx", "jZw0CWXuDc", "OLtD2vDF5X", "wozhdnRCtw", "8WQ7VTfPTl", "Hf17y6u9BC"]</related>

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>