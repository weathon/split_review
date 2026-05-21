Now I have all the information needed to write the consolidated review.

## Summary

This paper makes three substantial contributions to the theory and practice of separable neural networks (SepNNs): (1) a universal approximation theorem showing that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets, proven via Stone-Weierstrass; (2) a neural tangent kernel (NTK) analysis characterizing SepNN training dynamics, including convergence to a deterministic kernel under infinite width + infinite rank and a random kernel under fixed rank; and (3) an efficient separable preconditioned gradient descent method (SepPGD) that scales as O(nD) for n^D grid training samples by applying separate preconditioners to each factor network.

## Strengths

1. **Universal approximation theorem for multiple SepNN architectures (Theorem 1).** The proof combines the Stone-Weierstrass theorem with universal approximation of MLPs to show that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function. This is a clean, general result that subsumes prior bivariate-only results (Cho et al., 2023) and handles non-polynomial activations. The proof sketch is clear and the theorem is well-stated.

2. **Characterization of SepNN neural tangent kernel regimes (Lemma 1, Theorem 2, Corollary 1).** The paper derives the explicit NTK expression for CP SepNNs and proves convergence to a deterministic kernel under joint infinite width and rank, as well as convergence to a random (stochastic) kernel under fixed rank. These are the first principled results on SepNN training dynamics and spectral bias, and the empirical validation in Figure 1 supports the theoretical predictions. The distinction between infinite-rank (deterministic) and fixed-rank (random) NTK regimes is a nuanced and valuable contribution.

3. **Lemma 2 establishing equivalence to classical NTK-based PGD for D=2.** This lemma bridges the proposed SepPGD method with established preconditioning methods (Geifman et al., 2024; Shi et al., 2025) by showing equivalence to a Kronecker-sum preconditioner. This provides a clean theoretical connection that justifies why SepPGD should adjust the NTK spectrum, and also serves as an intuitive explanation of the method for the bivariate case.

4. **Empirical validation across diverse tasks.** The experiments span kernel ridge regression (noisy/noiseless), image representation and inpainting, 3D surface representation, and PINNs for PDEs. Across all tasks, SepPGD consistently achieves faster convergence and better final accuracy than baselines (MLP, SepNN without preconditioning, MSK). The visual results in Figures 3-4 show tangible improvements (e.g., PSNR from ~26.5 to 33.3).

## Weaknesses

### Fatal
None.

### Major

1. **The "provably" claim for spectral bias alleviation is overstated relative to what is actually shown.** The abstract and introduction state that SepPGD "provably adjusts the eigenvalue distribution of NTK matrix," but the theoretical support is incomplete in two ways. First, the argument for D=2 (the only case with a formal derivation) depends on the assumption that the Kronecker-sum NTK approximation K̃ is "close" to the true NTK matrix K, with the sense of "close" neither quantified nor proven in the available main text (Lemma 3 is referenced but its content and quantification of the approximation are not shown). Second, the extension to D>2 is only stated as "readily extended" without derivation or proof. While the D=2 case is well-justified through Lemma 2, these gaps mean the overall claim is better described as "heuristic with partial theoretical support" rather than "provable." The paper should either complete the proof for D>2, or scope the provability claim to D=2 with a clear caveat.

2. **The complexity analysis of SepPGD contains an inaccuracy and lacks a clear breakdown.** The paper claims O(nD) complexity for SepPGD in Table 1 and Remark 4, described as "by multiplying D n-by-n preconditioning matrices {M_d}." However, M_d is defined as ℝ^{R×n} (Equation 8), not n×n, and the construction of M_d involves a matrix product between an R × n^{D-1} matrix and an n^{D-1} × n matrix that naively costs O(R·n^D) — not O(n^{D-1}) as stated in Footnote 3. While this one-time (or every-10-iterations) construction cost is amortized and still far cheaper than the O(n^{3D}) cost of classical NTK-based PGD, the paper should provide a clean separation of (i) one-time preconditioner construction cost, (ii) per-iteration preconditioner application cost, and (iii) amortized cost with the update frequency. Without this, the advertised O(nD) figure is ambiguous and risks misleading readers about what the complexity claim covers.

3. **No iteration-count convergence plots to separate spectral bias alleviation from per-iteration cost effects.** The experiments plot MSE vs. wall-clock time, which conflates two sources of improvement: (a) cheaper per-iteration cost (O(nD) vs. O(n^D)) and (b) actual spectral bias reduction (better-conditioned dynamics per step). Since the paper claims the method "alleviates spectral bias," it should also show convergence in iterations (holding per-iteration cost constant by comparing against SepNN without preconditioning) to demonstrate that the improvement is not solely due to cheaper updates. This is especially important because SepPGD's faster wall-clock convergence could be driven entirely by the cheaper SepNN forward pass rather than by preconditioning.

### Minor

1. **The SepPGD definition (Equations 7-8) is notationally dense and hard to parse.** The combination of ⊕, ⊗, unfold, ×_d, and Einstein summation conventions in a single equation makes it difficult for readers to verify the correctness of the update or to reproduce it. While Lemma 2 clarifies the D=2 case, the D>2 formulation remains opaque. The paper would benefit from a simpler step-by-step derivation or a pseudocode description of the algorithm.

2. **The preconditioner update frequency (every 10 iterations) is stated without justification or sensitivity analysis.** The paper mentions that the preconditioner is updated every ten iterations "which is computationally expensive in previous methods," but provides no ablation or analysis of how this choice affects convergence. Since the preconditioner construction has non-trivial cost, this hyperparameter deserves some discussion or empirical investigation.

3. **Experiments do not include an ablation on the rank parameter R.** The theory relies on large R (infinite rank) for deterministic NTK, but the SepPGD experiments presumably use modest R. The paper should discuss or ablate how SepPGD's effectiveness varies with R.

### Trivial
- Remark 4 describes M_d as "n-by-n preconditioning matrices" but Equation 8 defines M_d ∈ ℝ^{R×n}.

## Nice-to-Haves
- A pseudocode summary of SepPGD alongside the tensor-notation definition would improve reproducibility.
- Comparing SepPGD against additional efficient preconditioning methods (e.g., KFAC applied to factor networks) would strengthen the method evaluation, though it is not required.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"NTK off-diagonal entries issue"** (Harsh Critic, Section 3): The critic stated that "the paper's final expression assumes no cross-terms between different r and s." This is factually incorrect — Lemma 1 explicitly defines 𝐊_{Θ_d}(x_d, x'_d) ∈ ℝ^{R×R} with elements indexed by (r,s), and Equation (4) uses a_d(x)^T 𝐊_{Θ_d}(x_d, x'_d) a_d(x'), which fully captures cross-terms.

- **"Lemma 3 not shown in main text"**: The hard rules state that parser-stripped appendix content should be assumed to exist. The criticism about Lemma 3 being absent from the main text is a formatting/presentation issue at most, not an evidential gap in the original submission.

- **"What is MSK?"**: The paper defines "modified spectrum kernel (MSK) (Geifman et al., 2024; Shi et al., 2025)" in the experiments section. This is clearly attributed to the cited works.

- **"Related work on KFAC tensor-train preconditioning is missing"**: The hard rules forbid mentioning missing related works due to lack of external verification capability.

- **Generic scope-creep criticisms** (e.g., "should test on more datasets," "should include more random seeds"): These are standard area-of-concern sweep items that do not identify any specific problem with the presented evidence.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight that emerges from the reviews is the tension between the paper's two strongest contributions. The approximation theory and NTK analysis are rigorous and well-scoped, establishing a firm theoretical foundation for SepNNs that did not previously exist. The SepPGD method, by contrast, is presented with claims ("provably," O(nD) without qualification) that outpace the actual theoretical support in the main text. This asymmetry is not uncommon in papers with both foundational theory and a proposed method, but the disconnect is particularly noticeable here because the theoretical sections set a high bar for rigor that the method section does not quite meet. A revision that brings the method claims into alignment with what is actually proven — while keeping the excellent approximation theory and NTK contributions — would substantially strengthen the paper.

## Suggestions

1. Tone down the "provably" language throughout: replace with "theoretically motivated" or "with a proof for the bivariate case (D=2)" and clearly state the D>2 case as a plausible extension with supporting empirical evidence.
2. Provide a clean complexity breakdown: (i) preconditioner construction: O(D·n^3 + D·n^2·P) for eigen-decomposition of factor NTK matrices + O(R·n^D) for M_d construction (amortized over update interval); (ii) per-iteration application: O(D·R·n + P) for factor gradient computation. Clarify that the O(nD) figure refers to the per-iteration cost.
3. Add convergence plots in iterations (not just wall-clock time) for SepNN vs. SepNN+SepPGD to isolate spectral bias alleviation from per-iteration cost advantages.
4. Include a pseudocode algorithm box for SepPGD to supplement the tensor-notation definition.

## Score and Decision

**Bracketing (Round 1):** Retrieved anchors in three score bands. Weak band (avg 2.33–3.00): papers with limited scope or flawed theory — this paper is clearly stronger. Middle band (avg 4.50–6.33): papers with solid contributions but notable gaps — WWlxFtR5sV (6.33, preconditioning for PINNs, accepted) and sawjxRnVpF (4.50, Lie-group preconditioners, rejected). Strong band (avg 7.60–8.00): polished papers with rigorous theory and thorough experiments. Initial bracket: **5.0–7.0**.

**Narrowing (Round 2):** Pulled additional anchors inside the bracket. SyVPiehSbg (7.50, ActNet, accepted spotlight) has a similarly structured contribution (novel architecture + UAP + experiments on scientific tasks) but is more polished in presentation and claim-scoping — the current paper is weaker on the method justification side. 3PWYAlAQxv (6.00, weight-permutation UAP, rejected) has clean theory but limited experiments — the current paper has broader scope and more experiments. eQggPqESBr (5.50, simplicity bias, rejected) has theory-light empirical analysis — the current paper has stronger theory. WWlxFtR5sV (6.33, preconditioning for PINNs, accepted poster) has a similar mix of theory + preconditioning + PINN experiments, with comparable weaknesses (limited experiments, strong claims with caveats).

**Final score determination:** Compared to the accepted anchors in the 6.0–6.5 range, this paper has stronger theoretical contributions (UAP + NTK analysis both well-proven, vs. primarily one theoretical result) but slightly weaker method validation (the "provably" overclaim and incomplete complexity breakdown). The paper sits comfortably above reject-level papers (3.0–5.0) and is comparable to marginal-accept papers (5.5–6.5). Given that the core theory is solid, the method is empirically effective even if overclaimed, and the issues are addressable in revision, the paper merits acceptance near the threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>