- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have thoroughly examined the paper. Let me construct the final review.

## Summary
This paper proposes applying the information bottleneck (IB) principle to understand masked autoencoders (MAEs), and introduces MI-MAE, a method that adds mutual information maximization (via InfoNCE) and minimization (via CLUB) losses to the standard MAE reconstruction loss. The core idea — that MAEs can be improved by explicitly controlling information flow in the latent space through IB-guided losses — is novel and potentially valuable.

## Strengths
1. **Novel application of IB theory to MAEs**: The paper identifies a relevant gap — prior understanding of MAEs is largely post-hoc and contrastive-based, lacking a principled optimization framework. Applying the IB lens to MAEs is a genuinely new direction that could yield theoretical insights (Section 4.1).

2. **Concrete, actionable losses derived from information-theoretic principles**: Rather than stopping at a qualitative analysis, the paper translates the IB framing into two specific loss terms: a mutual information maximization loss (InfoNCE between latent features of different masks, Eq. 5–6) and a mutual information minimization loss (CLUB upper bound between latent and input, Eq. 9–10). This gives practitioners a clear recipe to implement (Section 4.2).

3. **Multiple orthogonal mask sampling**: The idea of generating multiple mutually orthogonal masks per image and treating their latent features as positive pairs is a clean and principled way to create the contrastive signal needed for the IB-derived objective, without requiring additional augmentations (Section 4.2, Assumption 3 line 103).

## Weaknesses

### Fatal
None.

### Major
1. **The theoretical derivation (Section 4.1) is unclear and contains unjustified leaps.** This is the paper's central claimed contribution — a "systematic and comprehensive framework" for understanding MAEs via IB — but the presentation does not support this. Specifically: (a) The notation is confusing and inconsistently used: the overbrace notation `\overbrace{X\cdot(1-m)}^{}` appears without definition (line 73), and `\widetilde{X}` is used on line 87 as "the complexity of X·(1-m)" while `X\cdot\widetilde{(1-m)}` is used differently on line 73. (b) Theorem 2 asserts `\hat{z}=X\cdot(1-m)+r` without any justification (lines 81-82) — the claim that "the latent feature is the information bottleneck for the MAE" is stated rather than derived, and the additive bias form is assumed without argument. (c) The bound in Theorem 2 (Eq. 3) is presented without derivation or citation, and the term `-I(\hat{z};X\cdot m|r)` whose optimization is later claimed crucial is never connected to any practical training objective. A reader familiar with the standard IB formulation (`min I(X;Z) - β I(Z;Y)`) will find the mapping to the paper's Lagrangian (Eq. 2) unclear. **Why this matters**: The paper's main novelty claim rests on this theoretical framework; if it does not cohere, the paper is left with a method that is only weakly grounded in the presented theory.

2. **The leap from Corollary 4 to the specific loss functions is asserted rather than derived.** Corollary 4 (lines 105-111) gives a bound on `I(ˆz_k;z_k)` involving multiple terms, and states three conditions for maximization. From this, the paper directly adopts InfoNCE (Eq. 5) for condition (1). However, there is no analysis showing that maximizing `I(ˆz_k;ˆz_i)` via InfoNCE is the dominant factor in the bound, or that the other two conditions are simultaneously satisfied — the paper simply asserts that optimizing Eq. 10 (the CLUB loss) satisfies the third condition (line 140). The connection between the abstract inequality and the final loss is therefore a logical gap. **Why this matters**: The paper positions the losses as "derived from theory," but the derivation is not a formal consequence — it is a heuristic selection of one term from a multi-term bound.

3. **The experimental results are not present in the visible text.** Section 5 contains only pre-training hyperparameters and the start of Algorithm 1, then jumps to the conclusion. Despite strong empirical claims in the abstract and introduction ("our 400-epoch model achieves 83.9% accuracy on ImageNet-1K, surpassing the 1600-epoch MAE by 0.5%"), there are **no tables, no comparisons to baselines (MAE, SimMIM, BEiT, etc.), no ablation studies, and no detection/segmentation results**. The paper as provided cannot be evaluated on its empirical claims. (Note: This may be a parser truncation artifact; if so, the full submission should be re-evaluated with results included.)

4. **The paper criticizes contrastive approaches for providing only "implicit insights" and performing "on par with the original MAE" (line 46), but then proposes a contrastive InfoNCE loss as its own core contribution — without adequately distinguishing itself.** The paper does not explain why its contrastive loss is fundamentally different from the prior work it critiques. This creates an unresolved tension in the paper's narrative.

### Minor
1. **Missing implementation details** that are needed to assess the method: (a) No weight coefficients are given for combining the three loss terms (`L_rec`, `L_max-mi`, `L_min-mi`). (b) The architecture of the variational approximation network V (used for the CLUB loss) is not described. (c) The "mutually orthogonal masks" concept (line 103) is not explained — for binary patch masks, what does orthogonality mean? (d) The loss balancing is not discussed.

2. **The claim that the CLUB-based loss also satisfies the third condition in Corollary 4 (line 140) is asserted without any analysis or evidence.** This linkage is crucial to the claim that all three conditions are met, but no reasoning or experiment supports it.

3. **The approximation network is trained via negative log-likelihood (Eq. 8) but the paper does not discuss whether this approximation is accurate enough for the CLUB upper bound to be valid.** If the variational posterior is a poor approximation, the CLUB bound may not hold, and minimizing it may not achieve the intended information compression.

### Trivial
- Figure 1's caption contains garbled text and unclear variable references (line 63), making the figure difficult to interpret.

## Nice-to-Haves
- An ablation study isolating the contribution of each loss term (max-mi only, min-mi only, both) would be the most effective way to validate the method, even beyond baseline comparisons.
- A description of how orthogonal masks are constructed in practice (e.g., are they predefined or sampled per batch?) would aid reproducibility.
- A discussion of the computational overhead introduced by the additional masks (4× more encoder forward passes) and whether the reduced training epochs compensate for it would help practitioners assess the method's efficiency.

## Removed Points
These points were raised by reviewers but are removed from the main weaknesses list for the following reasons:

1. **"The CLUB-based loss deviates from the standard CLUB formulation without explanation."** — REMOVED. The paper's Eq. 10 matches the standard CLUB estimator (Cheng et al., 2020): `log q(ˆz_j|X_j) - (1/N) Σ_k log q(ˆz_k|X_j)`. The second term averages over all latents conditioned on the same input, which is exactly how CLUB is defined. The estimator includes the diagonal term (k=j), which is standard. This criticism is factually incorrect.

2. **"The definitions use inconsistent and undefined notation"** (the specific claim that variables are "impossible to reconcile" with standard IB). — WEAKENED and merged into Major weakness #1 above with concrete examples. The extreme framing ("impossible to reconcile") is removed, but the valid core (unclear notation, missing derivations) is retained.

3. **"Missing proof of Theorem 2"** — REMOVED per instructions: missing proofs that would go in an appendix are parser-stripped content.

4. **Several generic "strengthening" suggestions** (e.g., "clean up the theoretical section," "validate through ablation") — MOVED to Nice-to-Haves or removed as they are not specific weaknesses.

5. **"Reproducibility: The variational network architecture is not described"** — WEAKENED and moved to Minor weakness #1c.

6. **"Hyperparameter details: Temperature τ=0.07 is given, but no weight coefficients for the three loss terms"** — MOVED to Minor weakness #1a.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an angle or implication that the paper itself does not already claim, though they correctly flag that the execution does not match the ambition of the claims.

## Suggestions
1. **Revisit the theoretical section with precision.** Define every variable and notation explicitly. Show, step-by-step, how the standard IB formulation (min I(X;Z) - β I(Z;Y)) maps to the MAE setting. Provide a concrete derivation (even in the supplement) for Theorem 2 from first principles. Without this, the "IB framework" claim cannot be evaluated.

2. **Either strengthen the derivation from Corollary 4 to the losses, or re-frame the paper as empirically motivated.** If the connection cannot be made rigorous (showing that InfoNCE optimizes the dominant term in the bound, and that the other conditions are effectively satisfied by the reconstruction loss and CLUB loss), then acknowledge the losses as heuristics inspired by the IB perspective rather than derived from it. This would be an honest and still useful contribution.

3. **Include the complete experimental results** (tables, baselines, ablations) in any resubmission, with error bars where applicable. The claims of state-of-the-art performance are the strongest practical argument for the method, and they must be verifiable.

4. **Address the contrastive-learning tension explicitly.** Acknowledge that the max-mi loss is a contrastive objective, explain how its specific formulation or its pairing with the min-mi loss goes beyond prior contrastive MAE analyses, and compare to the most relevant prior work (U-MAE, Kong & Zhang 2023).
