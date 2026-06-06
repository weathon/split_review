## Summary
The paper proposes a first-order unifying framework—Influence-Aligned Steering (IAS)—that formally connects activation steering and training-data influence functions as projections of the same underlying Jacobian sensitivity tensor. The central theoretical contribution is a closed-form duality between steering vectors and signed measures over training data (Theorem 4.2), a scalar alignment diagnostic γ(x) that characterizes when perfect equivalence is achievable (Theorem 5.1), generalization bounds for low-rank steering (Theorem 6.1), and a spectral recipe for choosing optimal steering directions (Theorem 5.3). Experiments on GPT-2 Medium and ResNet-50 serve as empirical illustrations.

---

## Strengths

- **γ(x) is a computable and empirically grounded feasibility diagnostic.** Figure 2 shows that the median principal-angle cosine rises monotonically from 0.64 at layer 0 to 0.94 at layer 11 in GPT-2 Medium. This directly validates Theorem 5.1's prediction that deeper layers provide better subspace overlap. The diagnostic requires only two JVPs—a cost comparable to a single backward pass—making it practically deployable as a pre-screening step.

- **The unified Jacobian framing is genuine and novel.** Both steering (Eq. 2) and influence functions (Eq. 1) are written as products of the same family of Jacobians, and IAS (Theorem 5.2) is the minimum-norm solution to the induced linear system. This closed-form bridge between two previously disconnected interpretability tools is a concrete, constructive result. The chain-rule factorization (Lemma 4.1) is elementary, but the assembly into a unified first-order theory is a real contribution.

- **Generalization bound for low-rank steering (Theorem 6.1) is formally derived.** The Rademacher complexity increase from a rank-k IAS correction at a layer of width d is bounded by αL√(2k/dn), scaling favorably with d and n. This provides a formal backing for the practitioner's preference for low-rank, small-magnitude interventions—something that was previously a heuristic.

- **Directional accuracy of first-order predictions is strong.** Over 5,000 prompt-token pairs (Figure 1), predicted and actual logit shifts achieve cosine similarity 0.978, confirming that the first-order linearization captures the correct direction of change very well.

---

## Weaknesses

### Fatal
None.

### Major

- **IAS strictly underperforms CAA on both metrics in Table 1, with no explanation.** CAA achieves toxicity 0.0150 and perplexity 13,291; IAS achieves 0.0164 and 13,701, while the unadjusted baseline sits at 0.0195 and 14,333. If IAS is the principled minimum-norm optimal steering direction derived from influence information, it is internally inconsistent that a simpler hand-crafted mean-difference direction (CAA) dominates it on both reported metrics. The paper is entirely silent on this discrepancy. Possible explanations—influence function instability, small contrastive set (50 examples), implementation choices, layer selection—are not explored. This undermines the practical workflow claim in contribution 4 (Section 1).

- **The proof sketch of Corollary 1 is incorrect.** The sketch reads: "If another measure ν achieved the same shift with smaller ℓ₁ norm, one could scale ρ_s down and still match the shift, contradicting the definition of α as the steering magnitude." Because the map ν ↦ Σ_z ν(z) I(z→x) is linear, scaling ρ_s down scales the induced logit shift proportionally—a scaled-down ρ_s would therefore *not* reproduce the same logit shift. The argument is logically invalid. The ℓ₁-minimality claim may be provable under the stated affine-independence assumption (Section 2, assumption iii), but no correct argument is given. This is a structural flaw in one of the corollaries used to back the data-attribution workflow.

- **The claimed "equivalence" is materially qualified but the abstract/title framing obscures this.** The feasibility condition Im(J_{θ→y}) ⊆ Im(J_{h→y}) is stated as an assumption "when stated" (Section 2), but the abstract asserts the techniques are "equivalent" with no qualification. Figure 2 shows γ = 0.64 at layer 0, meaning the feasibility condition is substantially violated at early layers—the approximate residual bound (Eq. 3) would allow up to √(1−0.64²) ≈ 77% relative logit-space error. While the paper does provide the γ diagnostic to handle the non-ideal case, the unqualified "equivalence" framing throughout the abstract and introduction overstates what the theorems actually guarantee.

### Minor

- **The slope of 1.50 in Figure 1 indicates a systematic 50% underestimate of logit shift magnitudes.** The paper calls this "consistent with the expected linear regime," but for a framework whose theoretical apparatus is predicated on first-order accuracy, a slope 50% above the identity is notable. Corollary 2 provides an O(α²) remainder bound without reporting α, so it is not possible to judge whether the magnitude is within the theoretical tolerance. The directional accuracy (cosine 0.978) is impressive, but the magnitude mismatch should be acknowledged and analyzed rather than subsumed under "consistent with linearity."

- **The data-attribution workflow (Implication after Theorem 4.2) is entirely unvalidated.** The paper claims ρ_s "pinpoints the fewest training examples to relabel/remove/examine." No experiment tests whether ρ_s actually recovers causally responsible training documents. A natural proof-of-concept—insert a known-causal document, apply the steering→data mapping, check if ρ_s recovers it—is absent.

- **Basu et al. (2021) on influence-function fragility in deep networks is cited but never discussed.** Since IAS inherits its fidelity directly from influence-function estimates, the documented instability of those estimates at the Hessian level is a relevant threat to IAS's reliability in practice. The paper cites this work but does not address the implication.

- **The "billion-parameter models" scalability claim (Section 1) is not supported by experiments.** The only language model evaluated is GPT-2 Medium (~350M parameters). The claim that the method "scales to billion-parameter models" requires at least one experiment at or near that scale to be credible.

### Trivial

- **Lemma 5.4's displayed equality is tautological.** The equality case written as "√(1-(1-γ₁²))√(1-(1-γ₂²))" trivially simplifies to γ₁γ₂ by inspection; presenting it as a separate equality alongside the bound adds no information.

- **Theorem 6.2's "No-Free-Lunch" label oversells a direct corollary of the definition of γ.** The bound ‖J_{h→y}Δh‖/‖J_{θ→y}Δθ‖ ≤ γ(x) follows immediately from the definition of the smallest principal angle between the two subspaces. It is useful to state explicitly, but calling it a theorem with a named label is a packaging choice, not a derivational achievement.

---

## Nice-to-Haves

- **Larger-model evaluation.** Measuring γ and IAS accuracy on a 7B-class LM would address the scalability claim and test whether the monotone depth-dependence of γ observed in GPT-2 generalizes.
- **Diagnosis of the IAS vs CAA gap.** Ablating the contrastive set size (50 → 500 → 5,000 examples) and the Hessian approximation quality would help determine whether the gap is a data-quantity issue or a more fundamental problem with the influence-based direction.
- **End-to-end attribution experiment.** Validating that ρ_s recovers known-causal training documents would convert Corollary 1's "practical payoff" claim from assertion to evidence.
- **ImageNet comparison with a non-random baseline.** Comparing the spectral direction from Theorem 5.3 against a CAA-style mean-difference direction on the vision task would be a stronger validation than the random baseline currently used.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Section 3 "inflates" a pseudoinverse projection into a primal–dual framework.** Removed: The primal–dual framing is a legitimate pedagogical device to motivate the IAS derivation and introduce the dual multiplier λ* as a diagnostic. That it rests on classical constrained optimization does not make the packaging inappropriate.

- **Harsh Critic: Theorem 5.3 (Spectral Optimality) is "the standard spectral norm bound for bilinear forms."** Removed: While the underlying linear algebra is classical, identifying the correct matrix Σ (the influence covariance projected into activation space) and providing the power-iteration recipe in the context of steerable LLMs is a useful contribution. The "standard" label would apply to many applied-math theorems; the novelty here is the problem setup.

- **Harsh Critic: Theorem 6.2 is a "direct consequence of the definition of γ" and should not be called a theorem.** Partially removed: Retained only as a Trivial note on labeling, since the underlying content is still useful to state explicitly even if it follows directly from definitions.

- **Strength Finder: "Minimal-ℓ₁ data re-weighting derived from steering" (Corollary 1 as strength).** Removed: The proof sketch is incorrect (as established above); the strength depends on a flawed argument and cannot be credited as a confirmed result until the proof is corrected.

- **Strength Finder: "First-order equivalence verified at scale: remarkably accurate."** Partially removed: Directional accuracy (cosine 0.978) is retained as a strength; the characterization of slope 1.50 as "remarkably accurate" is removed because a 50% magnitude discrepancy is not accurate.

---

## Novel Insights

The most genuinely novel observation in this paper—one that neither reviewer fully articulates—is that γ(x) is not merely a static feasibility flag but a *layer-selection oracle*: because γ increases monotonically with depth (Figure 2), the practitioner can compute γ at a small set of candidate layers on a micro-batch and pick the earliest layer where γ ≥ threshold, trading off computational locality against representational fidelity. This is a concrete, principled answer to the otherwise-heuristic question of "which layer should I steer?" that existing activation-steering work handles entirely by trial-and-error. The result could stand alone as a practical contribution independent of the broader duality claims, and deserves more prominence than it currently receives.

---

## Suggestions

1. **Fix the proof of Corollary 1.** The correct argument should proceed through the affine-independence assumption: under affine independence the representation of the logit shift as a linear combination of influence vectors is unique (up to the affine constraint), so ρ_s is the unique measure achieving the shift with ‖ρ_s‖₁ = |α|. A brief but correct proof sketch is needed.
2. **Report the steering magnitude α used in Figure 1 and verify it is consistent with the O(α²) remainder bound.** This would clarify whether the slope 1.50 is within theoretical tolerance or signals a regime violation.
3. **Address the IAS vs CAA gap explicitly**, even if just with an ablation over contrastive-set size. Silence on this point reads as ignoring a contradictory result.
4. **Qualify "equivalent" in the abstract and introduction** to "equivalent to first order when Im(J_{θ→y}) ⊆ Im(J_{h→y}), with bounded approximation error otherwise," to align the framing with the actual theorems.
5. **Replace the random-direction baseline in Figure 3** with a CAA-style baseline to make the spectral direction's advantage actionable.

---

## Axis Evaluation

**Originality:** Moderate. The connection between activation steering and influence functions through a shared Jacobian structure is a genuine new observation. The individual components (pseudoinverse projections, principal-angle geometry, Rademacher bounds) are classical; the assembly is the contribution.

**Importance of research question:** High. Bridging controllability and data attribution is a pressing need in LLM safety and interpretability. The γ diagnostic in particular addresses a practical gap.

**Claims supported:** Weak-to-moderate. The γ diagnostic is well-supported by Figure 2. The first-order directional accuracy is well-supported by Figure 1 (cosine 0.978). The practical improvement over CAA is not supported (IAS is worse). The attribution claim is unsupported. One corollary has a flawed proof.

**Soundness of experiments:** Weak. One experiment (Table 1) shows the proposed method is dominated by a simpler baseline. One experiment (Figure 3) uses only a random baseline. Only Figure 2 straightforwardly supports a key claim.

**Clarity of writing:** Good overall, but the abstract's unqualified use of "equivalent" is misleading given the conditional nature of the equivalence.

**Value to research community:** Moderate. The γ diagnostic and the unified framework have real value. The IAS algorithm as a practical tool is not yet demonstrated to be useful.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>