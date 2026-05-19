Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper studies neural collapse (NC) in deep networks trained end-to-end with weight decay, moving beyond the unconstrained features model (UFM). The key contributions are: (1) a generic theorem (Theorem 3.1) showing that approximate interpolation, balancedness, and bounded conditioning imply NC1–NC3; (2) a proof that gradient descent with weight decay on a class of networks with a wide first layer, pyramidal topology, and smooth activations provably achieves low training error and approximate balancedness, thus establishing NC1 (within-class variability collapse) under GD dynamics — the first such end-to-end guarantee for deep networks; and (3) two sufficient conditions for the bounded conditioning needed for NC2/NC3 — global optimality (Section 5.1) and stability under large learning rates (Section 5.2). Experiments on MLPs and ResNets illustrate the theoretical predictions.

## Strengths

- **First end-to-end NC1 guarantee under GD.** Theorem 4.1 (mainGD) proves that for a nontrivial class of deep networks with a wide first layer and pyramidal topology, gradient descent with weight decay yields approximate interpolation and balancedness, leading to vanishing within-class variability. This is the first proof of NC1 for deep networks trained end-to-end via GD, moving meaningfully beyond the UFM.

- **Clean sufficient-condition framework (Theorem 3.1).** The generic theorem cleanly decomposes neural collapse into three verifiable conditions (approximate interpolation, balancedness, bounded conditioning), providing a modular template for future analyses. The proof sketch in lines 122–131 is conceptually clear.

- **Global minimizer result for NC2/NC3 (Theorem 5.2).** Shows that any global minimizer of the ℓ₂-regularized loss automatically satisfies bounded conditioning of the linear part, provided the nonlinear part can fit the labels. This gives a clean sufficient condition for full neural collapse (NC1–NC3) without analyzing GD dynamics for the linear head depth.

- **Large-learning-rate connection (Proposition 5.3).** Connects large learning rates / edge of stability to bounded NTK and controlled conditioning of linear blocks, linking an empirically observed phenomenon to NC2/NC3 guarantees. While conditional, this opens an interesting theoretical direction.

- **Technical lemma (Proposition 4.2).** The shifted Polyak–Łojasiewicz inequality for the regularized loss is a clean technical contribution that enables the exponential convergence argument in Theorem 4.1.

- **Experiments support qualitative trends.** Figure 2 shows that NC2 improves with deeper linear heads across MLP and ResNet20, and balancedness decreases exponentially during training (Figure 1), consistent with the theoretical predictions.

## Weaknesses

### Fatal
None.

### Major

1. **Title overclaims the scope of the proof.** The title states that wide networks "provably exhibit neural collapse," but NC2 (orthogonality of class means) and NC3 (alignment with weights) are not proven under the same GD dynamics as NC1. The paper's abstract and introduction (lines 20–22) are actually careful about this distinction — "we provide the first end-to-end proof of within-class variability collapse (NC1)" and "we give rather weak sufficient conditions... for solutions to exhibit [NC2/NC3]" — but the title obscures this. The NC2/NC3 results in Section 5 are conditional: the global-minimizer argument (Theorem 5.2) assumes existence of parameters fitting labels in the nonlinear part (a reasonable but external assumption), and the large-LR argument (Proposition 5.3) is conditional on NTK bounds that are not proven to hold under GD. The paper's contributions would be better served by a title that reflects what is actually proved under GD (NC1) versus what is established under additional conditions.

2. **NC2/NC3 results are not closed under the same GD dynamics.** The Section 5 results are genuinely valuable as sufficient conditions, but they do not complete a proof that GD with weight decay drives networks toward full neural collapse. The global-minimizer argument (Section 5.1) requires the nonlinear part to exactly fit labels — the paper cites approximation results for this (line 276), but this is not a consequence of the GD dynamics analyzed in Section 4. The large-LR argument (Section 5.2) is explicitly conditional on NTK bounds ("assuming the 'edge of stability' phenomenon," line 322) and does not prove that GD enforces this bound. These limitations are disclosed in the paper's body but the narrative framing ("provably exhibit neural collapse") papered over them.

### Minor

3. **Restrictive assumptions on the network class.** Theorem 4.1 requires: pyramidal topology with n₁ ≥ N, smooth activations with σ′ bounded away from zero and one-Lipschitz (which excludes ReLU), and a specific initialization condition (Assumption 3.3). The paper acknowledges this (lines 28, 137) and notes that ReLU is ruled out but extensions are expected. These are standard for theory papers building on prior work (QuynhMarco2020), but they narrow the gap between the theory and the experiments, which use ReLU networks. The paper would benefit from a dedicated limitations paragraph discussing what it would take to relax each assumption.

4. **Complex bounds limit interpretability.** The bounds in Theorem 4.1 (equations 11–14) involve numerous interdependent parameters (λ, η, β₁, m_λ, r₀, α, ε₁, ε₂, L, L₁, L₂, etc.), making it difficult to gauge tightness. While the paper provides qualitative interpretation (lines 200–201), a simplified corollary for the ideal case (e.g., exact interpolation, perfect balancedness, large L₂) would help readers see the essence of the result through the heavy notation.

### Trivial
None.

## Nice-to-Haves

- A dedicated limitations section discussing the gap between assumptions (smooth activation, pyramidal topology, specific initialization) and practice would calibrate reader expectations and improve the paper's honesty.
- For the large-LR argument, simulations checking whether the NTK bound holds at convergence for the networks studied would make the conditional result more compelling, even though it would not constitute a proof.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:

- **Harsh critic's claim that "the bound on r in (11) seems to grow with 1/√λ" and that "The statement that r is 'of constant order' is not obviously justified."** This is factually incorrect. The paper's own constraint (11) requires λ ≤ ε₁²/(18(‖θ₀‖₂+λ_F/2)²), so ε₁/√λ is O(1) and r is indeed constant-order as the paper explicitly states in lines 200–201. Removed due to being factually wrong (Hard Rule 2).

- **Harsh critic's claim that "Theorem 3.1 does not explicitly state the minimal assumptions needed for NC2/NC3 bounds."** The theorem does state the additional assumption explicitly (line 101: "If we additionally assume that the linear part of the network is not too ill-conditioned, i.e., κ(W_{L:L₁+1}) ≤ c₃"). The critic's follow-up that "this is precisely what needs to be proven" is an observation about the result structure, not a weakness of the paper. Removed as a misunderstanding (Hard Rule 2).

- **Harsh critic's generic complaint about bounds being "hard to gauge how tight or meaningful" and the bound on κ(W_L) being "hard to interpret."** These are subjective impressions without a specific technical error. The paper provides interpretation (lines 117–120, 200–201). Removed as noise (Filtering Discipline).

- **Harsh critic's complaint about "missing appendix" or "missing proofs."** The parser strips appendices; they exist in the original submission. Removed per Hard Rule 9.

- **Harsh critic's speculation that the bounds blow up as λ→0.** The paper's constraints ensure this does not happen (see above). Removed per Hard Rule 2.

- **Strength Finder's supporting strength about "Proposition 1 (Proposition 2) derives a shifted PL inequality."** While accurate, this is a minor technical lemma, not a strength that supports the paper's main claims about neural collapse. Demoted to Nice-to-Haves territory.

## Novel Insights

The reviews' main cross-cutting insight is that the paper's framing (especially the title) creates an expectation of a complete proof of all three NC properties under GD, whereas NC2/NC3 require additional assumptions not proven to arise from GD dynamics. This gap between framing and substance is the central tension: the paper has a genuine and valuable contribution (NC1 under GD) but packages it with conditional NC2/NC3 results in a way that could mislead readers. Neither reviewer identified a specific mathematical error — the issue is one of scope calibration. A secondary insight, implicit across both reviews, is that the modular sufficient-condition framework (Theorem 3.1) is arguably the paper's most reusable contribution, as it decouples the analysis of NC into independently verifiable sub-problems that future work could satisfy under weaker assumptions.

## Suggestions

1. **Revise the title.** Consider something like "Wide Neural Networks Trained with Weight Decay Provably Exhibit Within-Class Variability Collapse" or "Provable Neural Collapse in End-to-End Training of Deep Networks: NC1 Guarantees and Sufficient Conditions for NC2/NC3."

2. **Restructure the narrative to be upfront about the GD vs. conditional distinction.** The current abstract and intro are fairly careful, but the title dominates first impressions. Adding a short "Caveat" paragraph early in the paper (or in the introduction) that explicitly states "our GD guarantee covers NC1; NC2/NC3 are shown under the additional sufficient conditions in Section 5" would eliminate any ambiguity.

3. **Add a simplified corollary to Theorem 3.1** for the ideal case (ε₁=ε₂=0, κ bounded) to make the main intuition transparent before presenting the perturbed bounds.

4. **Include a limitations paragraph** in the conclusion or introduction discussing the gap between assumptions (smooth activation excluding ReLU, pyramidal topology, initialization conditions) and common practice, along with speculation on which are fundamental vs. artifacts of the proof technique.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>