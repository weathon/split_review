## Summary

This paper proposes Parameter Expanded SGMCMC (PX-SGMCMC), a technique that reparameterizes each weight matrix in a neural network as a product of matrices (PVQ decomposition with additional expanded matrices). The method aims to improve the diversity of posterior samples drawn by SGMCMC without requiring tempering or multiple chains, and without increasing inference cost. The paper provides a theoretical analysis of the induced preconditioning dynamics and presents empirical results on CIFAR-10/CIFAR-100, distribution shifts, OOD detection, and a comparative study with Hamiltonian Monte Carlo.

## Strengths

- **Lemma 3.1 is a clean theoretical contribution**: The derivation of the exact preconditioning matrix \(P_{\mathbf{X}(t)}\) induced by the matrix-product expanded parametrization is novel and goes beyond prior work on deep linear neural networks, which focused on optimization rather than sampling dynamics. This lemma clarifies how EP structurally modifies the gradient dynamics.

- **Empirical validation that PX-SGHMC approaches gold-standard HMC diversity (Section 5.3, Table 5, Figure 4)**: Starting from HMC burn-in checkpoints (Izmailov et al., 2021), PX-SGHMC achieves ensemble ambiguity and prediction variance comparable to HMC, while vanilla SGHMC falls short. The loss landscape analysis (Figure 4a) shows PX-SGHMC crosses substantially larger barriers than SGHMC, and the 2D subspace visualization (Figure 4b) supports that its posterior coverage approaches HMC. This is the strongest evidence that the method actually solves the diversity problem it targets.

- **Causal chain from EP depth → singular value dynamics → sample diversity is empirically confirmed (Figure 2, Table 4)**: The paper validates the mechanistic pathway: as the number of expanded matrices \(e\) increases, (i) maximum singular values rise and minimum singular values drop, (ii) both unnormalized and normalized Euclidean distances between consecutive samples grow monotonically, and (iii) ensemble ambiguity (AMB) increases (Table 4). This connects the theoretical prediction to observable outcomes.

- **Zero inference-cost overhead (Section 1, line 22; Section 3.1, lines 90–92)**: The expanded matrices P, V, Q can be reassembled into the original weight matrix W after training, so inference runs at exactly the same speed and memory cost as standard SGMCMC. This distinguishes PX-SGMCMC from deep ensembles (which multiply inference cost by ensemble size) or preconditioning approaches requiring auxiliary computations at test time.

- **Efficient convolutional reparameterization (Section 3.3, Eqs. 16–17)**: For convolutions, the paper restricts P and Q to operate on channel dimensions only, reducing parameter overhead from 3× to \((1 + 2/k^2)\)× (e.g., ~1.125× for 3×3 kernels). This engineering contribution makes the method feasible for modern architectures.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 3.2 does not logically support the diversity claim**: The theorem derives an *upper bound* on the expected Euclidean distance between consecutive SGLD samples that grows with EP depth \((c+d+1)\) and maximum singular value \(M\). The paper argues (lines 156–158, 249) that because the bound gets larger with depth, the method achieves better exploration. This reasoning is logically flawed: an upper bound becoming looser does not imply that the *actual* distance grows — it is equally consistent with the distance remaining unchanged or even shrinking. The paper acknowledges the gap ("Although the bound in Theorem 3.2 is not necessarily the maximum distance…") but does not resolve it. To establish increased exploration from the bound, a *lower bound* or direct estimate is needed, not a looser upper bound. The paper's own hedging ("suggests", "may improve") underscores that the theoretical argument as presented does not bear the weight placed on it. The empirical results (Figure 2, Table 4) independently support the diversity claim, but the theoretical framing as presented overclaims what has been proven.

- **Deep Ensembles — the paper's primary motivation — are never compared in any experiment**: The introduction (lines 12–13) explicitly frames the paper's significance around SGMCMC's failure to match deep ensembles (DE), stating "When training time is not a concern, DE usually outperforms SGMCMC in terms of both accuracy and uncertainty estimation." Yet DE is never included as a baseline in Tables 1, 2, 3, or 5. Without this comparison, the reader cannot assess whether PX-SGMCMC closes the gap that the paper itself identifies as the central problem. If PX-SGMCMC still underperforms DE, the practical significance of the contribution is unclear; if it matches or exceeds DE, that would be a strong result. Either way, the omission is a significant evidential gap relative to the paper's own framing.

- **Training overhead is acknowledged but never quantified**: The paper states (line 280) that EP "requires additional training resources in terms of memory and computation" but provides no concrete numbers. The abstract's claim of improvements "within the same computational budget" is ambiguous without specifying the budget (number of iterations vs. FLOPs/parameters vs. wall-clock time). For a ResNet20 with FRN, adding square P and Q matrices per layer increases the parameter count — by how much? What values of \(c\) and \(d\) were used in the main experiments? What is the wall-clock time overhead per iteration? These quantities should be reported.

### Minor

- **Toy experiment (Section 5.1) uses HMC, not SGMCMC**: The mixture-of-Gaussians experiment runs HMC (full gradients, no stochastic noise, no minibatches) with EP, not SGHMC or SGLD. The paper acknowledges this, but the experiment is presented as supporting evidence for the SGMCMC claim. The dynamics of HMC are qualitatively different from SGMCMC (stochastic gradients, injected noise, cyclical step sizes). This experiment demonstrates that parameter expansion helps in a deterministic setting, but it does not directly speak to the stochastic-gradient regime that is the actual object of study. The main SGMCMC experiments in Sections 5.2–5.3 are what carry the weight, making this a minor inconsistency rather than a fatal flaw.

- **All experiments use cyclical step size schedules, leaving the interaction between EP and the schedule uncontrolled**: The paper states (line 194) that "Unless otherwise specified, all the SGMCMC methods utilize the cyclical step size schedule." This means both PX-SGHMC and its baselines use the same schedule, so the comparison is fair. However, it is unclear whether PX-SGHMC's gains are additive to or dependent on the cyclical schedule. A control experiment without cyclical step sizes would clarify whether EP's benefits are independent.

- **"EP converges faster than SP" claim (line 247) is supported only by qualitative trace plots**: Figure 3 shows training/validation error curves but no quantitative comparison (e.g., epochs to reach a given validation accuracy). The claim would be stronger with numerical evidence.

- **Figure 2 (distance and singular value plots) lacks error bars**: The paper averages over 4 trials for the main tables but does not show variability in the exploratory analysis of Figure 2.

- **CIFAR-100 results (Table 3) are not discussed in the prose**: The caption mentions CIFAR-100 but the main text does not analyze or interpret these results.

### Trivial
None.

## Nice-to-Haves

- Add Deep Ensembles as a baseline in at least one experiment (e.g., CIFAR-10) to directly address the motivational framing.
- Include a control experiment without cyclical step sizes to isolate EP's contribution.
- Quantify training overhead: parameter counts, wall-clock time per iteration, and memory usage for the settings used.
- Provide a lower bound on the expected distance (or a mixing-rate bound) in the theoretical analysis if possible; otherwise, reframe the theory section as informal intuition and let the experiments carry the full argument.
- Add error bars to Figure 2 and report quantitative convergence metrics for Figure 3.

## Removed Points

These points were flagged for removal; treat them with caution.

- *"Reproducibility details are absent from the main text"* — This is a standard criticism that applies to virtually all conference papers, as implementation details are routinely deferred to appendices (which are stripped by the PDF parser). Removed per the rule against nitpicks about undisclosed hyperparameters and implementation details that are impractical to include in the main submission.

- *"The paper assumes the appendix covers [details]"* — Removed per the rule that missing appendix content should not be flagged since the parser strips appendices.

- *Strength 1 (from Strength Finder) as originally stated* — Included Theorem 3.2 as a strength, but this conflicts with the verified weakness about Theorem 3.2's flawed logic. The Lemma 3.1 portion is retained as a separate strength; the Theorem 3.2 portion is removed per the rule that when a strength and weakness disagree, the weakness wins.

- *"No error bars on distance/singular value plots"* — Moved to Minor (was in Strengthening section); kept but demoted.

- *"The bound in Theorem 3.2 focusing on SGLD while experiments use SGHMC"* — This is a reasonable point but standard in SGMCMC literature where theoretical analysis often focuses on SGLD for simplicity. Removed as an overreach.

- *"DE would multiply inference cost"* mentioned as a strength of PX-SGMCMC — This was noted by the Strength Finder as a supporting strength; retained in Strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not produce a synthesis that identifies a pattern or connection the paper itself did not already articulate.

## Suggestions

1. **Fix the theoretical framing**: Either provide a correct argument (e.g., a lower bound on expected distance, or a bound on the spectral gap) or demote the theoretical section to informal motivation. As written, Theorem 3.2's upper bound does not support the diversity claim, and the paper should not claim it does.

2. **Add Deep Ensembles as a baseline**: This directly addresses the paper's motivational framing and would substantially strengthen the practical significance of the results. Even a single comparison (e.g., CIFAR-10 test accuracy/NLL) would be informative.

3. **Quantify training overhead**: Report the actual increase in parameter count, per-iteration wall-clock time, and memory usage for the values of \((c,d)\) used in the main experiments.

4. **Run a control experiment without cyclical step sizes**: This would clarify whether EP's benefits are independent of the cyclical schedule or interactive with it.

5. **Provide quantitative convergence metrics for Figure 3** (e.g., epochs to reach a threshold validation error) rather than relying solely on qualitative trace plots.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>