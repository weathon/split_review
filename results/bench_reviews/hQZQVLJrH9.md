Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

This paper establishes a first-order theoretical bridge between activation steering and influence functions, proving that any steering vector corresponds to a signed re-weighting of training data (and vice versa). The framework yields practical tools: (i) an Influence-Aligned Steering (IAS) vector computable in two Jacobian-vector products, (ii) a scalar diagnostic ω (cosine of the smallest principal angle between Jacobian subspaces) that predicts when steering can fully substitute for weight-space editing, and (iii) a spectral recipe for choosing optimal steering directions. Experiments on GPT-2 Medium demonstrate IAS for detoxification, validate the first-order approximation (cosine 0.978), and confirm ω increases with layer depth.

## Strengths

- **Novel conceptual bridge.** The paper is, to my knowledge, the first to explicitly connect activation steering and influence functions through a shared Jacobian structure. Theorem 4.2 provides a constructive, invertible mapping between any steering vector and a signed data re-weighting — a genuinely fresh perspective that unifies two previously disconnected threads of interpretability research.

- **Practical diagnostic with empirical support.** The ω metric (Theorem 5.1) gives practitioners a cheap, principled answer to "should I steer or should I retrain?" — computing it costs only two JVPs. Figure 2 validates that ω increases monotonically with layer depth on GPT-2 Medium (0.64 → 0.94), providing actionable guidance for layer selection.

- **Principled direction selection.** Theorem 5.3 replaces hand-crafted steering vectors (e.g., difference-in-means) with the top eigenvector of a Fisher-influence matrix. Figure 3 demonstrates this spectral direction lies far in the tail of a null distribution on ResNet-50 (p=0.00498), confirming its utility beyond language models.

- **First-order approximation validated.** Figure 1 reports cosine similarity of 0.978 between IAS-predicted and actual logit shifts over 5000 prompt–token pairs, confirming the linear theory holds with high fidelity in a real transformer.

## Weaknesses

### Fatal

None.

### Major

- **The steer–influence equivalence is never demonstrated end-to-end.** The paper's central claim is that a steering vector can replicate the effect of an influence re-weighting and vice versa. Yet no experiment takes a computed influence update, builds the corresponding IAS vector, applies it, and verifies that the resulting model behavior matches the behavior obtained by actually implementing that influence update (e.g., via data re-weighting or fine-tuning on up-weighted examples). The detoxification experiment (Section 7.1) compares IAS against CAA — another steering method — not against any influence-based intervention. Figure 1 validates the *first-order Taylor expansion* (i.e., that the local linear approximation is accurate), which is a sanity check on the theory's assumptions, not a test of the equivalence construct itself. Without an end-to-end equivalence demonstration, the paper's headline contribution remains a formal statement whose practical significance is unverified.

- **Causal language is unwarranted and unsupported.** Corollary 1 and surrounding text (Section 4.1) claim that the measure ϱ_s isolates "the *most causal* training documents" (emphasis in paper). What the math actually proves is ℓ₁-minimality among first-order representations — i.e., ϱ_s is the sparsest signed measure *in the basis of influence vectors* that reproduces the first-order logit shift. This is a representational property, not a causal one. Influence functions for deep networks are known to be fragile (Basu et al., 2021, cited in the paper), and no experiment removes or relabels the top-weighted examples to test whether they are genuinely responsible for the steered behavior. The causal framing significantly overstates what the theory supports.

### Minor

- **Narrow experimental scope.** Only one model (GPT-2 Medium) and one task (toxicity reduction) are evaluated for the complete IAS pipeline. This is adequate for a theory-forward paper but insufficient to support the claimed "integrated workflow for debugging, auditing, and aligning" — a claim that implies broader applicability. Adding a second model family (e.g., Llama) or a second behavioral axis (e.g., bias, factuality) would substantially strengthen the practical contribution.

- **No comparison with parameter-space editing methods.** The ω diagnostic is presented as a decision rule: when ω is small, practitioners should switch from steering to weight-space editing. Yet the paper never demonstrates this decision rule in practice — e.g., showing that on a prompt where ω is low, steering fails while a parameter-space method (ROME, MEMIT, or even LoRA fine-tuning) succeeds. This limits the practical value of what is otherwise the paper's most actionable contribution.

- **The ℓ₁-minimality interpretation is weaker than presented.** Corollary 1 claims ϱ_s uses the "fewest training examples" to reproduce a steering effect. This interpretation treats influence vectors as if they were an orthogonal dictionary, which they are not. The ℓ₁-minimal solution in a correlated basis may distribute weight across many nearly-collinear examples rather than isolating a few genuinely distinct ones. The paper should acknowledge this limitation.

### Trivial

- The running toy example referenced in Section 2 is deferred to an appendix (Appendix C), removing helpful intuition from the main text.

## Nice-to-Haves

- A demonstration of the full workflow: (i) use IAS to steer, (ii) compute ϱ_s to identify candidate training examples, (iii) remove/relabel those examples and show the behavior changes — would dramatically strengthen the paper's practical narrative.
- Sensitivity analysis of ϱ_s to Hessian damping and Gauss–Newton approximation choices, since influence functions for deep networks are sensitive to these parameters.
- Qualitative inspection of top-weighted training examples for a known steering vector to assess whether they are plausibly related to the steered behavior.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The core theoretical contribution is a repackaging of elementary linear algebra."** Removed. While the mathematical tools (pseudoinverses, principal angles, Rayleigh quotients) are indeed standard, the *connection* between activation steering and influence functions is genuinely novel — no prior work has established this duality. The value is in the insight and its practical consequences (ω diagnostic, spectral recipe), not in inventing new linear algebra. This is comparable to how the "Belief Dynamics" paper (score 4.50) used Bayesian updating — a standard tool — to connect ICL and steering in a novel way.

2. **"Theorem 4.2 proof sketch is hand-wavy; ℓ₁-minimality ignores that influence vectors are not orthogonal."** Partially removed — the "hand-wavy" characterization is a presentation nitpick. The ℓ₁-minimality concern is retained as a minor weakness above, since the practical interpretation is overstated.

3. **"The Rademacher-complexity bound is imported from Pinto et al. with minimal modification."** Removed. Combining existing bounds to characterize a new intervention is standard and valid theoretical practice. The bound is correctly cited and the contribution is the application to IAS, not a new Rademacher bound.

4. **"No ablations on steering magnitude."** Removed as a separate point. The detoxification experiment compares at matched ℓ₂ magnitude, and steering magnitude is not central to the theoretical claims.

5. **"Missing experiments on causal data attribution test, sensitivity of signed measure, top-weighted training examples."** These are addressed in Nice-to-Haves rather than Weaknesses, since they concern the practical workflow claim rather than the core theoretical contribution.

6. **Formatting/parser artifacts (garbled symbols, broken text).** Removed — these are parser artifacts, not author errors. The original submission does not have these issues.

7. **"Several symbols appear without clear definition."** Removed. While true that the parser output is garbled, the original submission presumably defines symbols properly. The core notation (Jacobians, Hessian, influence function) is standard and used consistently.

8. **"The paper never discusses the known fragility of deep-network Hessian approximations."** Removed. The paper explicitly mentions using a damped inverse with Tikhonov regularization (Section 2: "We use a damped inverse (H_ω + φI)^(-1) for stability") and acknowledges the Gauss–Newton approximation. The fragility concern is partially addressed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add an experiment that closes the loop: compute an influence update for a small set of up-weighted toxic prompts, construct the IAS vector, and show that applying IAS produces logit shifts matching the influence update (beyond the first-order sanity check of Fig. 1). Even on a small scale, this would substantiate the paper's central claim.
- Tone down the causal language in Corollary 1 and Section 4.1. Replace "most causal training documents" with "training documents whose influence vectors best explain the steering direction in the first-order sense," and acknowledge that this is correlational rather than interventional.
- Test ω as a decision rule on at least one example where ω is low — show that steering indeed fails while a simple parameter-space intervention (even LoRA on a small subset) succeeds.

## Score and Decision

### Calibration anchors used:

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `EDPvNhTOLK.md` (Directional Influence Function) | 6.00 | More technically sophisticated theory (VI-based), similar experimental limitations (MNIST + regression). This paper's theory is less deep but more directly practical. |
| `wMtS3brldm.md` (Dynamically Scaled Activation Steering) | 5.00 | Better experiments (2 models, Pareto-front analysis), method-focused rather than theory. This paper has novel theory but weaker empirical validation. |
| `guSVafqhrB.md` (Fine-Grained Activation Steering) | 4.67 (Accepted) | More comprehensive experiments across models/tasks, empirical contribution. This paper's theory is its differentiator. |
| `XyQ5ui62mm.md` (Belief Dynamics) | 4.50 | Most similar: theoretical bridge between two control paradigms, 5 tasks, 3 models. Comparable novelty but this paper has thinner experiments. |
| `ETT804iVAt.md` (Momentum Steering) | 4.67 | Practical method with moderate novelty. This paper has stronger theoretical contribution. |
| `I3IeAZvxB4.md` (Painless Activation Steering) | 3.33 | Purely empirical, limited novelty. This paper clearly surpasses it on theoretical contribution. |
| `MTlBNELM9S.md` (GLOSE) | 2.00 | Poorly motivated, multiple fundamental issues. This paper is substantially stronger. |

**Assessment:** This paper makes a genuinely novel theoretical connection between activation steering and influence functions, provides concrete practical tools (ω diagnostic, IAS vector, spectral recipe), and validates the first-order assumptions empirically. However, the headline equivalence claim lacks end-to-end empirical validation, the causal language is oversold, and experiments are narrow for a paper that claims a practical workflow. These issues place it below the stronger theory papers (DIF at 6.00) and the stronger empirical papers (DSAS at 5.00, Fine-Grained AS at 4.67), but above purely empirical papers with limited novelty (PAS at 3.33). The paper is most comparable to "Belief Dynamics" (4.50), which also proposed a theoretical bridge with limited-to-moderate experiments, but the current paper's weaknesses (unvalidated equivalence, oversold causal claims) pull it slightly below.

**Score:** 4.5 — Weak Reject. The theoretical contribution is genuine and the tools are useful, but the gap between what the paper claims and what it empirically demonstrates is too large for acceptance in its current form. The paper would need at minimum a direct equivalence experiment and toned-down causal language to become a solid accept.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>