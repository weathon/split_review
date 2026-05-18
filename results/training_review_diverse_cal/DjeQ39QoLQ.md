Now I have a thorough understanding of the paper and can evaluate all the reviewer claims against the actual text. Let me produce the consolidated final review.

## Summary

This paper analyzes the diagonal initialization used in S4D/S5 state-space models, proving theoretically that while the diagonal initialization converges to the S4 (DPLR) initialization pointwise for fixed smooth inputs (linear rate in n), it does **not** converge uniformly in the operator norm — leading to instabilities at specific Fourier frequencies. To address this, the authors propose a "perturb-then-diagonalize" (PTD) methodology that adds a small optimized perturbation to the non-normal HiPPO matrix before diagonalizing, yielding an approximate diagonalization that stays uniformly close to the robust DPLR system. They introduce S4-PTD and S5-PTD models and evaluate them on LRA benchmarks and a robustness test on sCIFAR.

## Strengths

- **Rigorous theoretical characterization of S4D's non-robustness.** Lemma 1 derives an exact closed-form expression for the transfer function difference between S4 (DPLR) and S4D (diagonal) systems. Theorems 1 and 2 then prove that while fixed smooth inputs converge at O(n⁻¹), the operators do **not** converge in the operator norm — the persistent spikes in Figure 2 directly confirm this non-uniformity. This is a genuine and well-executed theoretical contribution that illuminates a previously undiagnosed failure mode.

- **PTD methodology with a provable error bound.** Theorem 3 bounds the transfer function deviation between the perturbed-diagonal and DPLR systems by (2 ln n + 4)ε + O(√(log n)ε²), which is linear in the perturbation size and depends only logarithmically on the state dimension. This provides a theoretical guarantee that the PTD initialization stays uniformly close to the robust HiPPO initialization.

- **Empirical demonstration of improved robustness.** On the sCIFAR task (Figure 4), S4D fails dramatically when inputs are contaminated with Fourier-mode noise derived from the theoretical transfer function spikes, while S4-PTD maintains high accuracy. This directly validates the theoretical prediction and is the paper's strongest empirical contribution.

- **Competitive LRA accuracy.** On the Long-Range Arena benchmark (Table 1), S4-PTD averages 86.58% (improving over S4D's 84.89% by +1.69%), while S5-PTD reaches 87.61% (versus S5's 87.46%). These results demonstrate that the PTD initialization does not sacrifice — and in some cases improves — standard task accuracy while adding robustness.

- **Controlled ablation study confirming the perturbation trade-off.** Figure 4(c) plots accuracy versus ‖E‖/‖A_H‖, showing a clear sweet spot between 10⁻² and 1, with the eigenvector condition number following a 1/ε trend that corroborates Theorem 4. This provides practical guidance for selecting the perturbation size.

- **Synthetic frequency-domain experiment linking theory to practice.** Figure 3 shows that S4D predicts negative amplitudes for frequencies near the transfer function spikes (e.g., s > 80 in extrapolation), while S4-PTD remains accurate. This isolates the failure mode in a controlled setting and makes the non-robustness concrete and reproducible.

## Weaknesses

### Major

None.

### Minor

- **The theoretical bound in Theorem 3 is not empirically verified for the actual perturbations used.** The paper states a bound on |G_Pert(s) − G_DPLR(s)| but never computes this quantity for the optimized perturbations used in the experiments. Without this verification, the reader cannot tell whether the bound is pessimistic or whether the actual transfer function error is small for the chosen ε (~10⁻¹ relative to ‖A_H‖). Reporting the actual maximum deviation over a range of frequencies for the perturbations in the ablation study would clarify the practical meaning of Theorem 3 and the trade-off being optimized.

- **Improvements on LRA are modest, and the main benefit (robustness) is demonstrated only on a worst-case, contrived noise setting.** S4-PTD improves over S4D by 1.69% on average, while S5-PTD essentially ties with S5 (+0.15%). The robustness experiment (Figure 4) uses 10% sinusoidal noise at frequencies derived from the theoretical spikes of the S4D transfer function — the authors explicitly call this a "worst-case" setup. While demonstrating robustness against worst-case perturbations is meaningful, the practical relevance to natural distribution shifts or real-world noise is not established. A complementary experiment on a natural long-sequence task (e.g., an LRA task with structured noise) would strengthen the claim.

- **No comparison against a simpler baseline: random perturbation.** Theorem 4 suggests that a random Ginibre perturbation of appropriate size should also reduce the eigenvector condition number. The paper does not compare the optimized PTD perturbation against this simpler alternative. Without this control, it is unclear whether the optimization (Equation 8) provides meaningful improvement over a zero-shot random perturbation with the same norm — or whether the benefits of PTD come primarily from perturbing at all rather than from optimizing the specific perturbation.

- **Somewhat overstated scope of generality.** The abstract claims a "general solution for this and related ill-posed diagonalization problems in machine learning" and the text states the method "can be used to diagonalize many SSM initialization schemes." However, the experiments exclusively test the HiPPO-LegS matrix. While testing on HiPPO is the most relevant case for SSMs, the generality claim is not supported by experiments on other initializations or matrices.

### Trivial

- The paper is truncated in the extracted version (missing conclusion, references, and appendix), but per the instructions this is a parser artifact and not an author error. No trivial formatting issues are discernible from the extracted text.

## Nice-to-Haves

- An empirical comparison to a **random Gaussian perturbation** (Ginibre matrix) of the same norm would clarify whether the gradient-based optimization in Equation 8 is necessary or whether simple random perturbation suffices.
- Computing and plotting the actual ‖G_Pert − G_DPLR‖_∞ for the perturbations used in the ablation study, alongside the theoretical bound from Theorem 3, would make the connection between theory and practice concrete.
- A robustness experiment on a natural long-range task (e.g., injecting structured noise at vulnerable frequencies into one of the LRA benchmarks) would strengthen claims of practical relevance beyond the sCIFAR worst-case test.
- The paper could test PTD on a second non-HiPPO initialization (e.g., a random non-normal matrix or another SSM initialization) to substantiate the claimed generality.

## Removed Points

These points are flagged to be removed per the meta-reviewer instructions; treat them with caution.

1. **Harsh Critic Point 1 (PTD methodology insufficiently specified for reproducibility):** The critic claims the core algorithm is under-specified because the paper states only "We implement a solver to this optimization problem using gradient descent" without detailing gradient computation, optimizer choice, or iteration count. Removed per rule: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references" — the paper defers hyperparameter details to Appendix sections (e.g., Sec. experimentdetail) that are stripped by the PDF parser. The original submission contains these details.

2. **Sub-criticism that normalizations in Theorem 3 are "not obviously achievable simultaneously":** This is factually incorrect. The normalizations (‖Ṽ_H B_Pert‖ = ‖V_H B_DPLR‖ = ‖C_Pert Ṽ_H⁻¹‖ = 1) are achievable by simultaneously scaling B and C — since G(s) = C(sI−A)⁻¹B + D is invariant under B → αB, C → (1/α)C, these are simple scaling choices, not constraints that restrict feasibility.

3. **Complaint about the bound in Theorem 3 being "too weak":** The critic argues that (2 ln n + 4)ε is large for n=1000 and ε/‖A_H‖≈0.1. This misreads the theorem: the logarithmic dependence on n is actually favorable (the bound grows only logarithmically, not polynomially or exponentially, in the state dimension). A bound of O(ε log n) for this type of non-normal perturbation problem is standard and competitive. The real issue (kept above) is that the bound is not empirically verified, not that it is theoretically weak.

4. **Criticism that minimizing κ(Ṽ_H)+γ‖E‖ is a "proxy not obviously connected to the final transfer function error":** Theorem 3 directly connects the two: the transfer function error is bounded by (2 ln n+4)ε + O(...). Minimizing ‖E‖ (subject to keeping κ small) directly controls this bound. This connection is explicit in the paper, making the criticism unfounded.

5. **Various formatting/style nitpicks and requests for domain-coverage breadth:** Removed as scope-creep or per the formatting/style rules.

## Novel Insights

The strongest insight emerging from the interaction between the reviewers' perspectives is that the paper has a somewhat asymmetric contribution profile: the theoretical analysis of S4D's non-convergence in operator norm (Theorems 1–2, Lemma 1) is genuinely rigorous and stands as a meaningful contribution independently of the PTD method. The PTD method itself, while well-motivated by pseudospectral theory, delivers modest empirical gains whose attribution to the specific optimization (versus simpler random perturbation) is not fully disentangled. This suggests the paper could be strengthened most by either (a) directly comparing against a random perturbation baseline to demonstrate the value of the optimization, or (b) reframing the contribution toward the theoretical diagnosis of the problem, with PTD presented as a plausible (rather than uniquely optimal) remedy.

## Suggestions

1. Add an empirical baseline where the HiPPO matrix is perturbed with a random Gaussian matrix of the same norm (as suggested by Theorem 4), and compare its LRA accuracy and robustness against the optimized PTD perturbation. This would isolate the benefit of the optimization from the benefit of perturbing at all.

2. Empirically verify Theorem 3 by computing the actual maximum of |G_Pert(is) − G_DPLR(is)| over a range of frequencies for the perturbations used in the ablation study, and plot it alongside the theoretical bound. This would make the practical meaning of ε clear and validate the theoretical guarantee.

3. Add a note in the text (or the conclusion, which is stripped) clarifying that the generality claim for PTD is established theoretically (Theorem 3 works for general A with appropriate modifications) but empirically validated only on HiPPO — or test on a second initialization to support the claim.

4. Consider running the robustness experiment on one LRA task (e.g., Text or Image) by injecting structured noise at the identified vulnerable frequencies, to demonstrate that the robustness benefit extends beyond the sCIFAR worst-case scenario to natural long-sequence tasks.

## Score and Decision

**Originality:** 7/10 — The theoretical analysis of non-convergence is novel; the PTD method adapts known ideas from pseudospectral theory (Davies, Banks) to SSMs, which is a well-executed application but not a conceptually new algorithmic paradigm.

**Importance of research question:** 8/10 — Understanding and fixing non-robustness in widely-used SSM initializations is practically important for the long-sequence modeling community.

**Claims well-supported:** 6/10 — The core theoretical claims are well-supported. The empirical claims about PTD's benefits are adequately but not strongly supported: LRA gains are modest, the robustness test is worst-case/contrived, and the bound in Theorem 3 is not empirically verified.

**Soundness of experiments:** 6.5/10 — The experiments are mostly sound but lack a critical control (random perturbation baseline) and do not verify the key theoretical bound empirically.

**Clarity of writing:** 7/10 — The writing is clear and well-structured in the extracted portion. The theoretical sections are particularly well-organized.

**Value to the community:** 7/10 — The theoretical diagnosis of S4D's non-robustness is valuable. The PTD method provides a practical workaround, though its incremental benefit over simpler approaches needs sharper characterization.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>