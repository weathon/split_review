## Summary

The paper proposes **Influence-Aligned Steering (IAS)**, a first-order framework claiming to unify activation steering and influence functions. The central claim is that both techniques are equivalent projections of the same underlying Jacobian sensitivity tensor: any steering vector can be written as a signed re-weighting over training data and vice versa. The framework yields a closed-form construction, an alignment diagnostic γ(x) that certifies feasibility, a spectral optimality recipe for choosing steering directions, and a Rademacher complexity bound for low-rank IAS.

---

## Strengths

- **Elegant geometric unification.** The paper correctly observes that both activation steering (Eq. 2) and influence functions (Eq. 1) are elements of the same first-order linear space and uses principal-angle analysis to quantify their overlap. The alignment diagnostic γ(x) is a practically computable quantity (two JVP/VJPs + small SVD) that provides a principled *steer-vs-retrain* decision rule.
- **No-Free-Lunch theorem (6.2) is clean and useful.** The impossibility result that, when γ(x) ≤ ρ, no activation perturbation can replicate more than a fraction ρ of the influence update's logit effect, gives a concrete criterion for when steering is fundamentally limited.
- **Layer-depth ablation (Section 7.3)** clearly corroborates Theorem 5.1: γ grows from 0.64 at L0 to 0.94 at L11 in GPT-2 Medium, providing actionable guidance on layer selection.

---

## Weaknesses

### Fatal

None that completely invalidate the theory. However, see the Major concerns below.

### Major

1. **IAS underperforms the simpler CAA baseline in its primary experiment.** Table 1 shows that IAS achieves toxicity 0.0164 and perplexity 13,701, while CAA achieves 0.0150 and 13,291 respectively—*both* metrics favor the untheorized baseline. The paper presents this without explanation. A theoretically principled method that is less effective than the hand-crafted alternative on its motivating task is a significant empirical shortcoming.

2. **Systematic slope of 1.50 in Figure 1 casts doubt on the first-order regime.** The paper frames the cosine of 0.978 as validating first-order equivalence, but the regression slope of 1.50 means the linear approximation *consistently underestimates* actual logit shifts by 50%. This is not a small perturbation artifact; it signals that the first-order framework operates outside the regime where it is self-consistent. The paper notes it is "consistent with the expected linear regime" but does not explain the systematic 50% bias.

3. **Corollary 1 (ℓ₁-minimality) proof is logically circular.** The argument is: "If another measure ν achieved the same shift with smaller ℓ₁ norm, one could scale ρ_s down and still match the shift, contradicting the definition of α as the steering magnitude." But scaling ρ_s down changes the steering magnitude and the corresponding shift; it does not reproduce the original shift. The proof does not establish that |α| is a lower bound on the ℓ₁ norm of any measure achieving Δy^SV.

4. **The key practical application—tracing causal training examples—is entirely unvalidated.** The paper's most compelling selling point (Corollary 1, Section 4.1) is that ρ_s pinpoints the most causally responsible training documents. No experiment measures whether the top-weighted examples under ρ_s genuinely correspond to the observed behavior (e.g., whether removing them reduces toxicity). This is a major gap between theory and practice.

5. **Generalization bound (Theorem 6.1) conflates activation steering with weight-space perturbation.** The bound is derived for ̃f = fθ + αUV^T, which is a rank-k *weight perturbation*, not an activation-level intervention. IAS adds a vector to intermediate activations at inference time, not a low-rank matrix to the weight tensor. The theorem from Pinto et al. (2024) applies to weight-space low-rank layers; applying it to inference-time activation additions requires an equivalence that is not established in the paper.

### Minor

- Lemma 5.4 (composability): The stated bound γ₁₂ ≥ γ₁γ₂ = √(1−(1−γ₁²)) · √(1−(1−γ₂²)) is trivially γ₁γ₂ by algebra, but the inequality γ₁₂ ≥ γ₁γ₂ for consecutive layers is not proved; it is stated without justification.
- The spectral optimality experiment (Section 7.4) only demonstrates that the spectral radius of the top eigenvector is statistically larger than random directions (z = 3.55). It does not show that using this direction for actual steering on ResNet-50 produces better class-activation outputs than alternatives. The experiment does not close the loop from theory to practical benefit.
- Experimental scope is narrow: only GPT-2 Medium (345M parameters) for language tasks, and a single classification class on ResNet-50 for vision. No validation on any model that practitioners actually use for alignment or interpretability work.

### Trivial

None worth noting beyond the hard rules.

---

## Nice-to-Haves

- A controlled causal attribution experiment: apply IAS to a toxic steering direction, extract the top-k training examples under ρ_s, remove them, fine-tune, and measure toxicity reduction compared to random removal.
- Analysis of the slope deviation in Figure 1: is the 1.5× factor a systematic artifact of the Tikhonov damping parameter λ? If so, the paper should calibrate λ or derive the correction factor analytically.
- Clarification or correction of the Corollary 1 proof; even a brief correct argument would suffice.

---

## Novel Insights

The principal-angle alignment diagnostic γ(x) as a computable, per-input scalar that certifies whether activation steering can faithfully substitute for weight-level influence updates is a genuinely useful formalization. The idea that the steer-vs-retrain decision can be made cheaply (two backward passes) before investing compute in either direction is a practical contribution to the interpretability workflow, independent of whether IAS itself outperforms simpler alternatives. The spectral optimality recipe (Theorem 5.3) for deriving a principled steering direction from Fisher-influence covariance rather than hand-crafted difference vectors is also a worthwhile conceptual step, though its empirical demonstration is incomplete.

---

## Suggestions

- Fix the Corollary 1 proof: consider establishing the ℓ₁ lower bound by showing that any measure ν achieving Δy^SV satisfies ‖ν‖₁ ≥ |α| via a dual argument on the norm of the steering perturbation.
- Add at least one causal attribution experiment—even on a small model or controlled synthetic task—to validate the most distinctive claim of the framework.
- Investigate and report the source of the slope = 1.5 in Figure 1; consider whether re-scaling IAS by this factor brings it in line with CAA or above.
- Either restrict Theorem 6.1 to the weight-perturbation setting (and label it accordingly) or provide the additional argument connecting inference-time activation injection to rank-k weight perturbation.

---

## Score and Decision

The theoretical framework is conceptually interesting and the geometric analysis is largely sound. However, the paper's main empirical task (detoxification) shows IAS *under*performing the simpler hand-crafted baseline; the first-order approximation has a 50% systematic slope error; the most distinctive claimed application (causal data attribution) is experimentally absent; and Corollary 1's proof appears logically flawed. The theoretical novelty is real but modest—connecting two linearizations of the same map via the chain rule, while framing the equivalence clearly, is not a deep result. The paper is better described as a clean reformulation that opens several questions than as a validated framework ready for community adoption.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>