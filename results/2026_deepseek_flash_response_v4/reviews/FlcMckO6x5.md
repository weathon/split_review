Now let me compile my complete analysis and write the final review.

## Round 1 — Bracketing Summary

I made three calibration_search queries to bracket the paper:

**Low band (score < 3.5):** Papers on general NTK theory (avg score 2.33–3.40). The current paper has far more theoretical substance and concrete contributions, so it clearly sits above this band.

**Middle band (score 3.5–7.5):** Papers on spectral bias preconditioning and NTK optimization (avg scores 4.75–6.25). The most relevant anchors are:
- "Inductive Gradient Adjustment for Spectral Bias in INRs" (avg 4.75, Reject) — directly on NTK-based preconditioning for spectral bias.
- "Preconditioning for PINNs" (avg 5.00, Reject) — preconditioning with theoretical analysis.
- "On the expressiveness and spectral bias of KANs" (avg 6.25, Accept) — approximation theory + spectral bias analysis for a novel architecture.

**High band (score > 7.5):** Papers on graph neural networks, graphon networks, etc. (avg scores 8.0). These are on entirely different topics and not comparable.

**Initial bracket:** [4.75, 6.25] — the current paper is clearly better than the 4.75 anchor (which had less theory) and comparable to the 6.25 anchor but with a notable overclaim issue.

## Round 2 — Narrowing

I queried for papers in (4.5, 6.5) and (5.5, 7.5) on related topics and read two key anchors in full:

- **"On the expressiveness and spectral bias of KANs" (avg 6.25, Accept):** Similar tripartite contribution (expressiveness proof + spectral bias analysis + experiments). The current paper has comparably novel theory but suffers from a verified overclaim ("provably" adjusting the NTK spectrum). The KAN paper did not have a comparable overclaim issue.

- **"Divergence of NTK in Classification Problems" (avg 5.75, Accept):** Pure NTK theory paper. The current paper has broader scope (theory + algorithm + experiments) and is slightly stronger.

The current paper sits between these two anchors — above 5.75 in breadth but below 6.25 due to the overclaim.

## Final Score and Decision

Score: **5.5**, Decision: **Reject**

The paper has genuine theoretical contributions (NTK two-regime analysis is the strongest part) and a practically motivated algorithm with real efficiency gains. However, the central claim that SepPGD "provably adjusts the NTK spectrum" is materially overstated: the body text uses hedged language ("can possibly be verified," "Suppose that," "We can ultimately show") and concludes "This is left for future research." This is a clear disconnect that needs to be resolved. The experimental evaluation also lacks error bars and higher-dimensional validation. With these issues fixed, the paper could become acceptable (≈6.0).

---

Now writing the final review:

## Summary
This paper makes three contributions to the theory of separable neural networks (SepNNs): (1) a universal approximation theorem for CP, TT, and Tucker SepNNs for any D≥2; (2) an NTK analysis characterizing two asymptotic regimes (deterministic under W→∞,R→∞; random under W→∞, fixed R); and (3) SepPGD, a preconditioned gradient descent method that leverages the separable structure to reduce preconditioner cost from O(n^D) to O(nD). The approximation theory and NTK analysis are solid contributions; the SepPGD efficiency gain is genuine. However, the paper significantly overclaims by asserting that SepPGD "provably adjusts the NTK spectrum" when the actual argument is hedged and explicitly deferred to future work. This disconnect between advertised and demonstrated contributions, together with limited experimental validation, prevents acceptance in the current form.

## Strengths
1. **Universal approximation theorem for SepNNs (Theorem 1) covering CP, TT, and Tucker decompositions for any D≥2.** Prior work (Cho et al., 2023) only proved this for the bivariate case (D=2). The proof via Stone-Weierstrass is clean and extends to all three decomposition types. The paper also clearly contrasts its simpler proof strategy with prior constructions (lines 84-85).

2. **Two-distinct-regime NTK analysis with explicit limiting kernels (Theorem 2 and Corollary 1).** The paper proves that the SepNN's NTK converges to a deterministic kernel when both width W→∞ and rank R→∞, but to a stochastic kernel when width→∞ with fixed rank. This is a genuine theoretical contribution that goes beyond standard NTK analysis by accounting for the rank parameter unique to separable architectures. The empirical validation in Figure 1(a)-(c) convincingly supports the theory, showing NTK difference decreasing toward zero only when width and rank jointly increase.

3. **SepPGD reduces preconditioner cost from O(n^D) to O(nD) (Table 1, Remark 4).** For n^D training samples on a D-dimensional grid, prior NTK-based PGD requires an n^D × n^D preconditioning matrix. SepPGD replaces this with D factor-level preconditioners of size n × n. The complexity comparison in Table 1 and Remark 4 is clearly presented: construction cost drops from O(n^{3D}+n^{2D}P) to O(D(n^3+n^2P)).

4. **Empirical performance gains demonstrated with specific numbers.** On image INR, SepPGD raises PSNR from 26.48 (unpreconditioned SepNN) to 33.30 — a 6.82 dB gain. On 3D surface representation, IoU improves from 0.983 to 0.992. The convergence curves in Figure 2 use wall-clock time (not iterations), fairly reflecting the claimed O(nD) speed advantage.

## Weaknesses

### Fatal
None.

### Major
1. **The paper claims SepPGD "provably adjusts the NTK spectrum" (abstract, line 9; contributions, line 50), but the supporting argument does not constitute a proof.** The abstract states that SepPGD "provably adjust[s] the eigenvalue distribution of NTK matrix, effectively alleviating spectral bias." However, the argument in Section 4 (lines 201-202) uses hedging throughout: "This can possibly be verified," "Suppose that...," "We can ultimately show," and concludes "This is left for future research." A sketch is provided (exploiting Kronecker product eigenvalue relationships and the closeness of the approximate NTK to the true NTK), but it is explicitly incomplete — the paper itself acknowledges that a proper convergence and consistency proof is deferred. Claiming "provably" in the headline contributions while deferring the proof to future work is a material overstatement that misrepresents what is actually demonstrated. This is fixable (drop the "provably" language and replace with "empirically demonstrated"), but in its current form it undermines the paper's presentation of its central algorithmic contribution.

### Minor
2. **No error bars or measures of statistical significance for the main experimental results (Figures 2-4).** The NTK theory section (Figure 1) includes variance bands over ten runs, but the KRR, image INR, surface representation, and PINN experiments report only single runs or point estimates without quantifying variability. Given the stochasticity inherent in finite-width, finite-rank SepNNs (which the paper's own NTK analysis identifies), some measure of variability is needed to assess whether the reported improvements are reliable.

3. **Experiments are limited to D=2 (images) and D=3 (surfaces, PINNs).** The primary complexity advantage of SepPGD — O(nD) vs. O(n^D) — grows exponentially with D. Showing results for D≥4 would make the computational benefit concrete and demonstrate the method's practical relevance beyond modest dimensions. The paper acknowledges the grid-based setting is a common training configuration for SepNNs, and grid data in higher dimensions is natural for scientific applications, so this gap is addressable.

4. **NTK analysis (Section 3) is developed only for CP SepNNs.** The paper states in a footnote that "we believe it can be readily extended to TT and Tucker SepNNs" (line 118), but no analysis or even a sketch of the extension is provided. Given that the approximation theorem covers all three types, a similar scope for the NTK analysis would strengthen the contribution.

5. **The equivalence in Lemma 2 is established only for D=2.** The extension to D>2 is stated as "It is believed that the result... can be readily extended" (line 202) without justification. Since the method is defined for arbitrary D in Definition 1, the theoretical grounding for D>2 is weaker.

6. **SepPGD's improvement over the next-best baseline on PINNs is modest.** The final MSE for SepPINN is 0.042 vs. SepPINN+SepPGD at 0.037 (Figure 4). While the convergence speed advantage is clearer from the time-vs-MSE curves, the final accuracy gain is small. The paper does not analyze whether this gap is meaningful.

### Trivial
None.

## Nice-to-Haves
- An ablation in the appendix comparing SepPGD to the cost of running standard (non-separable) PGD on SepNNs for a feasible small-scale problem would cleanly isolate the benefit of the separable preconditioner design.
- A discussion of regimes in which the Kronecker-sum preconditioner might be a poor approximation of the optimal full preconditioner would strengthen the paper.
- Reporting the effect of the rank R on SepPGD performance in the main text (currently deferred to an appendix table).

## Removed Points
These points from reviewers were removed with brief justification:

1. **"The equivalence between SepPGD and standard NTK-based PGD is misleadingly stated"** (Harsh Critic #2). Lemma 2 correctly establishes that SepPGD is equivalent to a PGD update with a Kronecker-structured preconditioner. The reference to Geifman et al. is contextual (establishing the form of the update), not claiming identity of the preconditioners. The paper does not misrepresent the relationship.

2. **"Missing ablation comparing SepPGD to standard PGD on SepNNs"** (Harsh Critic #3). The paper compares against SepNN+MSK, where MSK is a PGD variant. Running full (non-separable) PGD on SepNNs would cost O(n^D), which is computationally prohibitive. The MSK baseline with mini-batching is a reasonable proxy. This is a nice-to-have, not a missing critical baseline.

3. **"Missing comparison with K-FAC"** (Harsh Critic). K-FAC is a Hessian-based preconditioner; the paper's focus is NTK-based preconditioning. Table 1 already includes Hessian-based methods in the complexity comparison. This is scope creep.

4. **"Approximation theory is 'less surprising'"** (Harsh Critic). This is a subjective opinion, not a concrete weakness. The paper's proof is clean and correctly extends prior D=2 work to any D≥2 for three decomposition types.

5. **Several typos/presentation nitpicks** (removed per hard rules about parser artifacts and trivial formatting issues).

## Novel Insights
The harsh critic's sharpest observation — that the paper's abstract claims "provably" while the body defers proof to future work — is the key insight that emerged from the review synthesis. This is a genuinely useful finding for the authors: it is not that the SepPGD method is flawed (the efficiency gain is real and the Kronecker-structured preconditioner is well-motivated), but that the paper presents its central algorithmic contribution in a way that overstates what has been rigorously demonstrated. Separately, the comparison with the KAN spectral bias literature (from the calibration anchors) reveals that the current paper's NTK two-regime analysis is actually more novel than the approximation theorem: the latter is a clean application of Stone-Weierstrass to a new setting, while the former provides genuinely new architectural insight (that the rank parameter R determines whether the NTK is deterministic or random, a property unique to separable architectures). This distinction between the two theoretical contributions is not drawn sharply enough in the paper itself.

## Suggestions
1. **Fix the "provably" overclaim.** Replace "provably adjusts the NTK spectrum" in the abstract and contributions with language that accurately reflects what is shown: "empirically alleviates spectral bias, supported by theoretical analysis showing that the Kronecker-structured preconditioner improves the eigenvalue distribution of the factor-level NTK matrices." Keep the theoretical sketch in Section 4 but be explicit that a full convergence proof is future work.

2. **Add error bars to the main experiments.** Reporting means and standard deviations over at least 5 random seeds for the KRR, INR, and PINN results would significantly strengthen the empirical claims.

3. **Include at least one higher-dimensional experiment (D=4 or D=5).** A synthetic function approximation or PDE problem on a 4D grid would concretely demonstrate the O(nD) vs. O(n^D) advantage.

4. **Acknowledge scope limitations more prominently.** State explicitly that the NTK analysis is for CP SepNNs and the equivalence Lemma 2 is for D=2, rather than deferring extensions with "it is believed."

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>