Now I have all the information needed to write the consolidated review.

---

## Summary

This paper proves that neural networks with a wide first layer, pyramidal topology, smooth activations, and at least two linear layers, trained by gradient descent with weight decay, provably exhibit neural collapse. The key theoretical innovation is a modular framework: Theorem 3.1 gives sufficient conditions (approximate interpolation + approximate balancedness of linear layers + bounded representations) for NC1, NC2, and NC3. The paper then shows these conditions are satisfied by GD training with weight decay for NC1 (Theorem 4.2), and gives two conditional scenarios for NC2/NC3: near-global optimality or stability under large learning rates. This moves substantially beyond the unconstrained features model (UFM) that dominated prior theoretical work on neural collapse.

## Strengths

1. **First end-to-end proof of NC1 for deep networks with at least two linear layers.** The paper moves beyond the data-agnostic UFM and shows that within-class variability collapse emerges from actual GD training dynamics, not just from optimization over free features. The abstract and intro clearly contrast with prior work relying on UFM or shallow architectures (lines 17–18, 45–53).

2. **Modular sufficient conditions for neural collapse.** Theorem 3.1 provides clean, interpretable conditions — approximate interpolation, approximate balancedness, bounded representations — under which NC1, NC2, and NC3 provably hold. The bounds (Eqs. 1–4) quantify the collapse in terms of error parameters, making the result applicable to any training method meeting these conditions.

3. **Provable satisfaction of NC1 conditions by GD with weight decay.** Theorem 4.2 (main GD result) shows that for networks satisfying Assumptions 1–3, gradient descent with appropriate learning rate and regularization achieves the required approximate interpolation and balancedness. The two-phase proof (exponential convergence via a shifted PL inequality, then balancedness emergence) links training dynamics directly to neural collapse.

4. **Two concrete scenarios for NC2 and NC3.** Section 5 shows that near-global minimizers (Theorem 5.1) and parameters stable under large learning rates (Proposition 5.2) both yield a well-conditioned last weight matrix, implying the full collapse. The large-LR argument connects the edge-of-stability phenomenon to conditioning of the linear layers, offering a novel perspective.

5. **Experimental validation of depth-dependent NC2 and balancedness trends.** Figure 2 shows NC2 improves as the linear head deepens, consistent with the theory. Figure 1 tracks balancedness showing exponential decrease, and Figure 4 shows deeper non-linear layers become more balanced and more linear. Results span MLPs and ResNets on MNIST and CIFAR-10.

## Weaknesses

### Fatal
None.

### Major

None. No verified weakness undermines the paper's core claims. The concerns raised about the PL argument are addressed below (Removed Points).

### Minor

1. **The large-LR sufficient condition is partly heuristic.** The paper's Proposition 5.2 is a valid conditional result (if the NTK is bounded and the network approximately interpolates, then some linear layer has bounded conditioning). However, the link from "large learning rate" to "bounded NTK" relies on the edge-of-stability phenomenon, which the paper explicitly states "remains difficult to prove" and "has been proved theoretically for simple models" (lines 291–294). The paper writes "Now, *assuming* the 'edge of stability' phenomenon" (line 322, emphasis added), which is transparent. Nevertheless, the abstract and intro present this as one of the two sufficient conditions without noting that the link from large LR to bounded NTK is not proven. The presentation slightly overstates what is proved versus what is conjectural.

2. **The NC1 proof relies on restrictive assumptions.** The theoretical guarantee for NC1 (Theorem 4.2) requires: (i) a pyramidal topology with the first layer wider than the number of samples, (ii) smooth activations (Assumption 2, excluding ReLU), (iii) a nontrivial initialization condition (Assumption 3), and (iv) small learning rate and weight decay satisfying multiple interdependent bounds (Eq. 23). The paper acknowledges these limitations (lines 137, 155–159) and the smooth activation approximates ReLU uniformly (Eq. 5), but the cumulative restrictiveness means the result covers a narrower class of networks than standard practice. This is typical for first theoretical results but limits the immediate practical applicability.

3. **The bounds in Theorem 3.1 are complex with coupled constants.** The ε in Eq. (4) has a denominator that depends on ϵ₁, ϵ₂, r, L₁, L₂, and ‖X‖_{op}. The bound is positive only when ϵ₂ is sufficiently small relative to other quantities. The paper does not explicitly discuss when this positivity condition holds. Similarly, the r in Theorem 4.2 (Eq. 25) depends on ϵ₁ and λ in a way that may be nontrivial to tune jointly. These couplings make the bounds less clean than one might hope.

4. **Experiments do not validate the specific theoretical conditions.** The experiments use ReLU activations (not smooth), large learning rates (not small), and architectures that may not satisfy the pyramidal width condition (ResNet20 widths are not specified). The paper is upfront about this (the experiments "confirm the insights coming from the theory" rather than test the assumptions), but an explicit check of whether the PL inequality holds, whether iterates stay within the ball, or whether the learning rate satisfies Eq. (23) would increase confidence. This is not required for a theory paper, but it would strengthen the empirical connection.

### Trivial

- The labeling of Proposition 5.2 uses `\label{thm:large_learning_rates}` while it is a proposition, a minor inconsistency.
- The paper would benefit from a simplified corollary for the scaling regime (e.g., N fixed, n₁ → ∞) to help readers parse the rates in Theorem 4.2.

## Nice-to-Haves

- A lemma or explicit construction showing that Assumption 3 (initial conditions) is satisfiable for concrete architectures would improve concreteness.
- Reporting final numerical values of NC1/NC2/NC3 metrics alongside the plots would allow quantitative comparison.
- An ablation checking whether the second phase (balancedness emergence) occurs under the learning rate bounds prescribed by the theory would be informative.

## Removed Points

These points were raised by reviewers but are removed or downgraded after verification against the paper:

1. **"Circularity in the PL inequality argument."** — Removed. The reviewer claimed a circularity: the iterates must stay in the ball for the PL to apply, but staying in the ball relies on convergence. This is a standard GD induction that is not circular. Proposition 1 shows that with η < 1/(2β₁), the GD iterates satisfy ‖θ_{k₁} − θ₀‖₂ ≤ 8√(C_λ(θ₀)/α) ≤ r₀ (Eq. 30). This is proven via a descent lemma + PL induction (standard in optimization), not by circular reasoning. The reviewer's concern stems from misunderstanding how these proofs work.

2. **"Proof of Proposition 4.1 (shifted PL) is only sketched."** — Removed. The paper states Proposition 1 as a restatable proposition; its proof (with the shifted PL inequality) is standard and would appear in the appendix, which is stripped by the parser.

3. **"The ε in equation (8) could become negative."** — Downgraded to minor (folded into Weakness #3 above). The denominator positivity is implicitly ensured because ϵ₂ is assumed small (approximate balancedness). This is standard for perturbation bounds.

4. **"First end-to-end proof claim needs more qualification."** — Removed. The paper *does* qualify this claim in the related work (lines 50–53), explaining that prior works (Xu et al. 2023, Rangamani et al. 2022) make the strong assumption of symmetric quasi-interpolation, which the paper does not require. The claim is properly contextualized.

5. **"The initialization assumption (Assumption 3) may be impossible to satisfy."** — Downgraded. The paper sketches a constructive argument (lines 173–175) showing it can be satisfied by choosing a small second layer and large others. A full lemma would be nice but the argument is plausible.

6. **"Weights might grow before regularizing."** — This concern (about the bound on representations/weights in Theorem 4.2 relying on r defined in Eq. 25) overlooks the two-phase structure: the first phase already brings the loss below ϵ₁², and the descent lemma ensures monotonic loss decrease, so weights cannot grow arbitrarily. The paper's analysis handles this.

## Novel Insights

The key insight that is genuinely novel and emerges from the review process is that the paper's modular architecture — separating NC1 guarantees (requiring only interpolation + balancedness) from NC2/NC3 guarantees (requiring additionally well-conditioned linear product) — is a powerful design principle for neural collapse proofs. Prior work collapsed these into monolithic assumptions (quasi-interpolation, UFM optimality). By breaking the problem into independent sufficient conditions, the paper creates a framework where future work can replace the GD proof for NC1 with one using weaker assumptions (e.g., ReLU, minimal overparameterization) without redoing the NC2/NC3 analysis, and vice versa. This modularity is the paper's most lasting contribution.

## Suggestions

1. **Clarify the large-LR section's logical status.** Explicitly separate the *proven* conditional statement (Proposition 5.2: if bounded NTK + interpolation + bounded weights, then bounded conditioning) from the *heuristic* link between large LR and bounded NTK. The current abstract could be read as claiming more than is proven. A sentence like "While Proposition 5.2 is proven, whether large learning rates actually yield bounded NTK for these networks is not yet proven; we provide the edge-of-stability intuition as motivation" would resolve this.

2. **Add a simplified corollary.** Provide a corollary of Theorem 4.2 for a specific scaling (e.g., N fixed, n₁ → ∞, ϵ₁, ϵ₂ → 0 with appropriate rates) to help readers see the qualitative behavior.

3. **Discuss the denominator positivity in Eq. (4) explicitly.** A brief note on when the ε in the NC2 bound is well-defined (what regime of ϵ₂ relative to other quantities) would improve rigor.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>