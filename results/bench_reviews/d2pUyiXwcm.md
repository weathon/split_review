Now I have a comprehensive understanding of the paper and the calibration landscape. Let me synthesize the final review.

---

## Summary

This paper introduces SCaSML, a framework that corrects pre-trained PDE surrogate models at inference time without retraining. The key insight is the "Structural-preserving Law of Defect": subtracting the surrogate's approximately-satisfied PDE from the original PDE yields a new semi-linear PDE describing the exact error, which can be solved via Multilevel Picard (MLP) Monte Carlo simulation. The authors prove that the final error is bounded by the *product* of surrogate and simulation errors (Theorem 2.5), yielding an accelerated convergence rate (Corollary 2.6). Experiments on PDEs up to 160 dimensions (linear convection-diffusion, viscous Burgers, HJB, diffusion-reaction) show SCaSML reduces error by 20–80% over base PINN and GP surrogates.

## Strengths

- **Novel conceptual contribution with theoretical backing.** The Structural-preserving Law of Defect (Fact 2.3) is a genuinely insightful observation: the error of a surrogate solution satisfies a semi-linear PDE with the same structure as the original, enabling Feynman–Kac-based Monte Carlo correction. This is clean and non-obvious. Theorem 2.5 formalizes the synergy by bounding final error as the *product* of surrogate and simulation errors — if rigorous, this is a meaningful theoretical result.

- **Strong empirical error reduction across diverse, challenging PDEs.** Table 1 consistently shows SCaSML achieving the lowest error across L², L∞, and L¹ metrics on five PDE families (up to d=160), with reductions of 20–80% over base surrogates. The method succeeds on the HJB (LQG) problem where naive MLP fails entirely (MLP L² error ~5.6 vs. SCaSML ~0.055 at d=100). Figure 3a confirms tightened pointwise error distributions.

- **Plug-and-play with heterogeneous surrogates.** SCaSML works with both PINNs and Gaussian Processes (Table 1, VB-PINN and VB-GP rows), demonstrating genuine flexibility without requiring surrogate-specific tuning of the correction mechanism.

- **Inference-time scaling behavior.** Figure 3b shows error monotonically decreasing as more Monte Carlo samples are allocated at inference, validating the "elastic compute" paradigm at a qualitative level.

## Weaknesses

### Fatal

None.

### Major

- **Budget-controlled efficiency comparisons are deferred to the appendix, leaving the central convergence-rate claim empirically undersupported in the body.** Corollary 2.6 claims that with *total* budget 2m (m training + m inference), error improves from O(m^{-γ}) to O(m^{-γ-1/2}). However, Figure 4 plots error vs. training points m on a log-log scale and shows SCaSML with steeper slope than the GP surrogate — but SCaSML uses *additional* inference samples beyond m, so the steeper slope is confounded by higher total compute. The caption states "By balancing the computational budget," but the plot does not demonstrate budget-normalized superiority. Table 1's runtimes (e.g., LCD-10d: SR 0.45s vs. SCaSML 13.31s) also show SCaSML costs substantially more total time. The body text points to fixed-budget comparisons in Appendix G.7, but the paper's headline empirical claim would be strengthened by bringing key budget-controlled results into the main text.

- **Assumption 2.4 is strong and unverified.** The assumption bounds both the surrogate's L∞ residual and its W^{1,∞} error by the same quantity e(û). For surrogates like PINNs or GPs in high dimensions, residual magnitudes can far exceed true solution error, and the W^{1,∞} norm of the error may scale differently. The theoretical scaling law (Corollary 2.6) depends on this assumption holding, yet no experimental verification of Assumption 2.4 is provided. This weakens confidence that the predicted rate improvement materializes under realistic surrogate behavior.

- **Different clipping thresholds between MLP and SCaSML in 3 of 4 problem families.** For Burgers (VB): MLP threshold = 1.0, SCaSML = 0.01. For LQG: MLP = 10, SCaSML = 0.1. For DR: MLP = 10, SCaSML = 0.01. The paper justifies this by the defect's smaller magnitude, but the tighter thresholds may independently reduce SCaSML error by suppressing simulation instability. No ablation on clipping threshold sensitivity is provided, making it difficult to attribute error reduction solely to the defect-correction mechanism. (The LCD problem uses identical thresholds for both methods, which partially mitigates this concern.)

### Minor

- **The "first physics-informed inference-time scaling" framing slightly overclaims.** The paper uses LLM inference-time scaling as an analogy and claims to be "the first inference-time scaling algorithm that enhances the learned surrogate solution during inference without requiring fine-tuning or retraining." While the specific combination (defect PDE + MLP correction at inference) appears genuinely novel, the broader idea of using surrogates as control variates in Monte Carlo PDE solvers has precedent (e.g., neural control variates for BSDEs), and the authors do not clearly distinguish their contribution from this lineage.

- **The product error bound's behavior when e(û)→0 is correct but counterintuitive, and the main text does not explain why.** Theorem 2.5 predicts zero error when the surrogate is perfect — which is actually correct (the defect PDE would have zero source term and zero terminal condition, yielding exact zeros). However, the paper's proof sketch does not clarify this, leaving readers to wonder whether the bound is overly optimistic. A brief remark would preempt this confusion.

### Trivial

- Figure 4 caption states "By balancing the computational budget" without specifying the exact budget allocation used to generate the SCaSML points, making the plot harder to interpret.

- The conclusion's use of "rigor" could be qualified since the guarantees are probabilistic (Monte Carlo), not deterministic.

## Nice-to-Haves

- An automated or heuristic method for choosing the balance between surrogate training effort and inference samples to minimize total cost for a target accuracy would strengthen the "elastic compute" narrative and enhance practical usability.

- Pointwise error maps (e.g., 2D projections for high-dimensional problems) would help illustrate whether SCaSML correction primarily reduces uniform bias or targets large local errors.

- A discussion of computational complexity beyond the asymptotic rate — e.g., how the constant factors in the MLP solver's E(M,N) term scale with dimension d — would help practitioners estimate real-world cost.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The paper lacks comparisons against surrogates trained with the same total computational budget."** — Softened and kept above as the Major weakness about budget-controlled comparisons, but with the caveat that Appendix G.7 (invisible due to parser stripping) is claimed to contain such comparisons. The removal of the *absolute* form of this criticism is because the paper does reference these comparisons, just not in the visible body.

- **Harsh Critic: "The Appendix (unseen) may contain some budget comparisons, but the body of the paper provides no evidence."** — This is fundamentally an appendix-visibility complaint. Per instructions, the parser strips appendices from all papers; they exist in the original submission. The criticism is reframed above as a presentation concern about the body text.

- **Harsh Critic: "The derivation of the defect PDE is standard algebraic manipulation; calling it a 'Structural-preserving Law of Defect' overstates the contribution."** — The derivation IS algebraically straightforward, but the *insight* that it preserves semi-linear structure (enabling Feynman–Kac solvers) is the contribution. This is not an error in the paper.

- **Harsh Critic: Section 2.2/2.3 "MLP methodology is taken from existing work."** — The paper is candid that MLP methods are from prior work (E et al., 2021; Hutzenthaler et al., 2020a, 2021) and explicitly cites them. Applying MLP to the defect PDE is the contribution, not inventing MLP.

- **Strength Finder: "Rigorous theoretical guarantee"** — Tempered above; the theory is meaningful but the "rigorous" label is strong given the unverified Assumption 2.4.

- **Harsh Critic: "Claims of 'rigor' are inconsistent with the fully stochastic nature of the simulation step."** — Moved to Trivial. Probabilistic guarantees ARE rigorous; stochastic methods can deliver rigorous convergence rates.

- **Harsh Critic: "The paper does not quantify the variance of SCaSML correction across multiple random seeds."** — The body text points to Appendix G.4 for statistical significance tests (p ≪ 0.001). Per instructions, missing-appendix concerns are removed. The paper reports point estimates but claims statistical validation exists.

- **Strength Finder: Generic claims like "this paper addressed an important problem"** — Dropped as overly generic.

- **Harsh Critic: Missing related work on neural control variates for deep BSDEs** — Per instructions, I do not flag missing related works as I cannot confirm their existence or relevance.

## Novel Insights

The review process highlights a tension common to hybrid ML-simulation methods: the product-form error bound (Theorem 2.5) is theoretically elegant, but its empirical validation is confounded by the practical difficulty of disentangling synergy from simple compute addition. The paper's core idea — that a better surrogate makes the defect PDE "easier" to simulate because variance scales with residual magnitude — is genuinely novel and well-motivated by the spectral bias of neural surrogates. The key challenge for the authors going forward is not to prove that SCaSML reduces error (Table 1 does that convincingly) but to demonstrate that the specific *rate improvement* (O(m^{-γ-1/2}) vs. O(m^{-γ})) materializes under budget-controlled conditions, which requires careful experimental design beyond what the main text currently shows.

## Suggestions

- Bring one or two key budget-controlled comparisons from Appendix G.7 into the main text — e.g., a plot of error vs. total function evaluations for SCaSML, pure MLP, and a larger surrogate trained with the same total budget. This would directly address the most significant concern about the empirical validation.

- Add an ablation study varying the clipping threshold for SCaSML on at least one problem (e.g., VB-PINN or DR) to demonstrate that the error improvement persists across a reasonable range, confirming it stems from the defect correction rather than threshold tuning.

- Clarify Figure 4 by specifying exactly how many inference samples were used for each SCaSML data point and whether total budget is matched to the GP baseline.

- Add a brief remark after Theorem 2.5 explaining why the bound vanishing when e(û)→0 is correct (perfect surrogate → trivial defect PDE → zero correction needed), to preempt the natural concern about irreducible simulation error.

## Anchor Comparisons

- **`3VdSuh3sie.md` (7.00, Oral)**: Frozen-PINN — stronger overall: more polished, cleaner experiments, no budget-confounding issues. SCaSML is a notch below in presentation completeness.
- **`7G0L4cj452.md` (6.67, Poster)**: ∂∞-Grid — comparable quality; novel architecture, strong empirical results. SCaSML has better theoretical backing but weaker empirical validation of its central rate claim.
- **`KWWfLgkySm.md` (6.00, Poster)**: NGD for PINNs — theory-heavy, restrictive assumptions (2-layer). SCaSML has broader empirical scope and a more immediately applicable idea.
- **`96fJALwotm.md` (5.50, Poster)**: AIS complexity analysis — theory paper with significant presentation issues. SCaSML is stronger empirically.
- **`BZnnIeeQox.md` (4.50, Poster)**: AI4S-RL framework — limited empirical validation. SCaSML has substantially more experimental evidence.
- **`zJ2kJyO6Ww.md` (4.50, Reject)**: PDEDIFF — weaker experiments and limited comparisons. SCaSML is clearly stronger.
- **`7noPldewfE.md` (2.50, Reject)**: Projective Symbolic Regression — conceptual flaws and weak scope. SCaSML is far stronger.
- **`fdjGPp1KPR.md` (1.33, Withdrawn)**: Adaptive activation functions — poorly executed, minimal novelty. Not comparable to SCaSML.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>