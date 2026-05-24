Now I have sufficient context. Let me produce the consolidated review.

## Summary

This paper makes three contributions to separable neural networks (SepNNs): (1) a universal approximation theorem showing that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function, (2) an NTK analysis characterizing SepNN training dynamics under infinite/finite width and rank, including spectral bias, and (3) an efficient separable preconditioned gradient descent (SepPGD) that speeds convergence with O(nD) complexity on n^D grid samples — exponentially cheaper than prior NTK-based PGD methods. Empirical results on KRR, image/surface INRs, and PINNs demonstrate qualitative improvements.

## Strengths

1. **Universal approximation theorem for multivariate SepNNs (Theorem 1, Section 2).** The proof uses Stone-Weierstrass combined with universal approximation, cleanly extending prior work (Cho et al., 2023) from D=2 to arbitrary D and to CP, TT, and Tucker forms simultaneously. The proof sketch is clear and the reliance on classical tools makes it verifiable.

2. **NTK analysis of SepNNs with practical asymptotic regimes (Lemma 1, Theorem 2, Corollary 1, Section 3).** Lemma 1 derives the NTK of a CP SepNN; Theorem 2 shows convergence to a deterministic kernel under infinite width + rank; Corollary 1 characterizes the random kernel regime under fixed rank. The result in Figure 1 provides empirical validation of these regimes with variance reported across ten seeds, lending credibility to the theory.

3. **SepPGD algorithm with dramatic complexity reduction (Definition 1, Lemma 2, Table 1, Section 4).** The core algorithmic idea — building D factor preconditioners of size n×n rather than one n^D×n^D preconditioner — is elegant and yields a genuine complexity improvement from O(n^D) to O(nD). Lemma 2 shows exact equivalence to classical NTK-based PGD for D=2 via Kronecker product structure, proving that the efficiency gain does not sacrifice theoretical grounding in that case. The complexity comparison in Table 1 is informative and clearly positions the contribution.

4. **Broad empirical demonstration across multiple tasks (Figures 2–4, Section 5).** The method is tested on four distinct problem types (KRR, image INRs, surface INRs, PINNs), consistently showing faster convergence in wall-clock time. This breadth strengthens the claim of practical relevance.

## Weaknesses

### Fatal
None.

### Major

1. **Claim-audit mismatch on "provably" for SepPGD (Abstract, Introduction, Section 4).** The abstract and introduction state that SepPGD "provably adjusts its NTK spectrum." The formal proof (Lemma 2) is established only for D=2. For D>2 — the regime actually used in the surface representation and PINN experiments — the paper states "it is believed that the result can be readily extended" and "this is left for future research" (line 208). The spectral argument following Lemma 2 also uses hedging language ("This can possibly be verified," "Suppose that..."). While the D=2 proof is valid and useful, the "provably" claim across the full scope claimed in the abstract is overstated relative to what is established in the paper. This is the most significant weakness because it inflates the paper's central advertised contribution.

2. **Experimental results lack statistical reporting for the main convergence claims (Figures 2–4, Section 5).** Only Figure 1 (NTK verification) reports variance across multiple seeds. Figures 2–4 present single convergence curves and single PSNR/IoU values with no error bars, standard deviations, or indication of number of replicates. Given that neural network training is stochastic, it is not possible to assess whether the observed improvements are statistically significant or represent variability across runs. This is a meaningful gap in empirical rigor for a paper whose third contribution is an optimization method.

### Minor

3. **Missing direct comparison with the full NTK-based PGD (Geifman et al., 2024) applied to SepNN.** The paper compares SepPGD against "SepNN (MSK)" (modified spectrum kernel, itself a preconditioning method). A head-to-head comparison with the full PGD method on a small-scale problem (where full PGD is tractable) would disentangle whether SepPGD's improvement comes from better preconditioning or simply from applying a different preconditioner. The complexity argument motivates why full PGD is expensive, but even a single small-scale comparison would strengthen the empirical evaluation.

4. **The spectral argument connecting SepPGD to NTK eigenvalue improvement is heuristic for D>2.** The paper's reasoning for D>2 (line 208) relies on an assumed closeness between the true NTK K and the Kronecker-structured approximation K̃, with the conclusion ultimately based on "can possibly be verified." The paper is transparent about this limitation, but it means the "provably adjusts its NTK spectrum" claim depends on the D=2 case only. A clear framing of this boundary would improve the paper.

### Trivial
None.

## Nice-to-Haves

- A small-scale comparison with the full NTK-based PGD (Geifman et al., 2024) on a bivariate problem would substantially strengthen the empirical case for SepPGD without incurring O(n^D) cost at scale.
- The choice of the eigenvalue cutoff parameter k for the preconditioners {S_d} is not discussed; a brief note on how k is selected or its sensitivity would help reproducibility.
- The paper could add a short remark clarifying the "stochastic kernel" terminology in Corollary 1.

## Removed Points

- **Missing experimental details (appendix stripped):** The harsh critic flagged that experimental settings are in Appendix A.12, which was removed by the parser. This is a parser artifact — the original submission contains these details. The paper explicitly cites Appendix A.12, confirming they exist in the full submission. **Removed.**

- **"The connection between SepPGD and SepNN's NTK spectrum is not as clean as suggested" — pseudo NTK matrix criticism:** The harsh critic argues that the sum-of-logits NTK reduction loses structural information, but the paper acknowledges it uses a "pseudo NTK matrix" and the empirical results (Figure 1(d)) confirm that the spectral bias characterization is meaningful. The paper's approach follows standard practice from Mohamadi et al. (2023) and Geifman et al. (2024). **Removed** as the paper does not claim the pseudo NTK is the full true NTK; it is a well-motivated design choice.

- **Convergence guarantee and NTK condition number bound:** The harsh critic demands a convergence bound for SepPGD akin to Geifman et al. (2024). The paper explicitly states this is left for future research (line 208). Criticizing a paper for not doing something it explicitly scopes out is not fair. **Removed.**

- **Missing TT/Tucker proof sketch:** The harsh critic asks for more detail on the TT/Tucker extension. The paper provides a proof sketch for CP and states the detailed proof is in the appendix. The Stone-Weierstrass argument is general enough to apply to all forms; singling this out as a weakness is scope creep. **Removed.**

- **"Stochastic kernel" terminology not defined:** The term is standard in the kernel methods literature (a kernel whose value is a random variable). **Removed.**

- **Missing discussion of rank R and parameter k selection:** These are implementation details that would be in the appendix (Section A.12). **Removed** as parser artifact.

- **Complexity comparison with Hessian-based methods in Table 1:** The harsh critic argues the comparison is not apples-to-apples. The table is clearly labeled with the gradient formulation for each method; the reader can judge the comparison on its own terms. No error in the paper. **Removed.**

- **Strengths from Strength Finder that are generic or conflict with verified weaknesses:** Several strengths were generic ("broad empirical evaluation," "empirical validation") and conflict with the verified weakness about missing error bars. These are **Removed** per the instruction that when a strength and weakness disagree, the weakness wins.

## Novel Insights

The harsh critic and strength finder inputs are largely aligned on the core assessment, though the harsh critic over-penalizes the paper for not including elements explicitly deferred to future work or appendices. The most valuable observation emerging from the synthesis is that the paper's three contributions sit at different levels of maturity: the approximation theorem and NTK analysis are complete and well-supported, while the SepPGD contribution — which the paper prominently advertises — has a theory-claim gap (proved for D=2, used for D>2) and an empirical-rigor gap (no statistical reporting on main experiments). This unevenness means the paper's overall score is pulled down by the weakest link in its presented evidence. A version that either (a) scales back the "provably" language to match the D=2 scope, or (b) adds error bars and statistical rigor to the main experiments, would move the paper solidly into the accept range.

## Suggestions

1. Tone down the "provably" language in the abstract and introduction to match what is proved (D=2 case with a spectral heuristic for D>2).
2. Add error bars or variance reporting to the convergence curves in Figures 2 and 4 at minimum; report mean and standard deviation for the final metrics in Figure 3.
3. Consider adding a single small-scale comparison with the full NTK-based PGD to demonstrate the empirical advantage more directly.
4. Clarify the choice of the eigenvalue cutoff parameter k used in constructing S_d.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| CXlsqTAf1E | PGD toward rich learning regime | 5.00 | 1,2 | Similar theoretical depth; present paper has broader scope but weaker experiments |
| P2m7gvtfrE | Preconditioning guides feature learning | 4.50 | 1 | Present paper is stronger (more concrete algorithm, real-task experiments) |
| U6SnDgI3gG | NTK vs CNTK spectral differences | 6.00 | 1,2 | Comparable level; present paper broader but experiments less rigorous |
| YzjS4jcfmS | Muon's spectral design | 5.00 | 2 | Similar level; both have theory + empirical components with gaps |
| bP6eScSxm2 | Spectral algorithms / ESD | 5.33 | 2 | Present paper is stronger (more practical relevance, empirical validation on real tasks) |

**Round-1 bracket:** Between ~3.5 and ~7.5. The weak-band anchors (1.5–3.0) are clearly weaker papers (rejected, limited scope). The strong-band anchors (8.0+) address different problems and communities.

**Round-2 narrowing:** Comparing against the 4.5–6.5 bracket anchors, the paper sits above the 4.50 anchor (rejected, synthetic-only) and comparable to the 5.00 poster anchors. It is slightly below the 6.00 poster anchors due to the experimental rigor gap and the claim-audit mismatch on "provably."

**Final score:** The paper's approximation theory and NTK contributions are solid and novel. The SepPGD algorithm is genuinely efficient and practically motivated, but the experimental evaluation lacks statistical rigor and the "provably" claim is inflated for D>2. Placing the paper relative to the anchors — between the 5.00 Poster and 6.00 Poster level — I assign **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>