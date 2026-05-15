Now I have all the evidence needed. Let me synthesize the final consolidated review.

## Summary

This paper develops a deep $\alpha$-stable kernel process (D$\alpha$-KP) as the infinite-width limit of deep Bayesian neural networks whose weights have infinite-variance elliptical priors. The key idea is that a common positive $\alpha/2$-stable random scale per layer factors out of the sum over incoming weights, leaving a finite-variance term to which the classical CLT applies, yielding a conditionally Gaussian representation with $\alpha$-stable marginals. The conditional covariance kernels are linked recursively via Cho & Saul (2009) formulas, enabling tractable MCMC posterior inference. The method bypasses the exponential computational bottleneck of prior stable-process inference (Loria & Bhadra) and demonstrably provides feature learning (stochastic kernel) without artificial noise injection. Experiments on discontinuous functions and UCI benchmarks show competitive or superior predictive performance.

## Strengths

- **Novel theoretical extension of Cho & Saul recursion to infinite-variance priors.** Theorem 1 generalizes the deterministic Cho & Saul (2009) recursive kernel formulas to deep BNNs with elliptical infinite-variance weights, yielding a *stochastic* kernel that remains positive definite with probability 1. This is the first recursive kernel formula for deep non-Gaussian ($\alpha$-stable) processes, directly enabling conditionally-Gaussian posterior inference.

- **Principled feature learning without artificial noise injection.** Proposition 2 proves that for $\alpha<2$ the posterior of the features depends on the observations (genuine representation learning), whereas $\alpha=2$ (the GP limit) yields a deterministic kernel with no learning. Figure 2 confirms heavy-tailed, non-Gaussian learned features on the Boston dataset. This cleanly distinguishes the method from DIWP (Aitchison 2021), which requires ad-hoc artificial noise.

- **Elimination of the exponential computational bottleneck.** The paper explicitly identifies that Loria & Bhadra's method has complexity $O(n^{I+2})$ due to feature-space enumeration, while the kernel-space approach avoids this entirely. Table 1 shows that the Stable method is "not available for more than 2 dimensions" while D$\alpha$-KP runs in ten dimensions, and timing results in the supplementary provide direct evidence of the speedup.

- **Strong predictive performance on discontinuous functions.** On the ten-dimensional discontinuous simulation (Table 1), D$\alpha$-KP achieves RMSE 8.08 (SD 0.38) versus the best GP-based method at 8.32. On the Energy and Yacht UCI datasets (Table 3), it yields the lowest RMSE/MAE (0.46/0.32 and 0.31/0.16 respectively), showing clear advantage when the truth contains jumps that GPs cannot model.

## Weaknesses

### Fatal
None. The harsh critic's central claim — that the $M_\ell^{-1/2}$ scaling in Theorem 1 is mathematically incompatible with convergence to a non-degenerate $\alpha$-stable distribution — is based on a misunderstanding of the weight construction. The paper constructs $w_{ij}^{(\ell)} = (s_+^{(\ell)})^{1/2} \tilde{w}_{ij}^{(\ell)}$ where $s_+^{(\ell)}$ is a **single** random scale shared across all $i$ in layer $\ell$. This common factor factors out of the sum: $\frac{1}{\sqrt{M_\ell}}\sum_i \sqrt{s_+^{(\ell)}}\tilde{w}_{ij}^{(\ell)} f_i^{(\ell)} = \sqrt{s_+^{(\ell)}} \cdot \frac{1}{\sqrt{M_\ell}} \sum_i \tilde{w}_{ij}^{(\ell)} f_i^{(\ell)}$. The $1/\sqrt{M_\ell}$ scaling applies to the $\tilde{w}$ terms, which have finite variance (conditional on the features and scales). The classical CLT applies to this inner sum, yielding a Gaussian, and the $\sqrt{s_+^{(\ell)}}$ factor then gives an $\alpha$-stable limit via the Gaussian scale-mixture representation. This is a standard and well-understood construction in the stable-process literature; it does not contradict any known limit theorem.

### Major
None. The paper's central claims are theoretically sound and supported by experiments.

### Minor
- **No ablation varying $\alpha$.** All experiments fix $\alpha=1$. Without a comparison across $\alpha \in \{0.5, 1, 1.5, 2\}$ on at least one synthetic task, the claim that *non-Gaussianity* (rather than some other aspect of the model) drives the performance gains is partially unsubstantiated. An $\alpha=2$ case would recover the deterministic GP kernel, directly testing the benefit of heavy tails.

- **Theorem 1 lacks an intuitive sketch in the main paper.** While proofs may reside in a supplementary section (stripped by the parser), the main text could benefit from a 2--3 sentence explanation of why the $1/\sqrt{M_\ell}$ scaling works despite the weights having infinite variance, emphasizing that the common scale factor is the key enabler. The current presentation states the result without building intuition.

- **UCI improvements are modest on some datasets.** On Boston (Table 3), D$\alpha$-KP (RMSE 2.59, SD 0.73) essentially ties with GP Bayes (2.58, SD 0.75). This is not a weakness of the method per se, but the paper's claim of "superior predictive performance" is overstated for this specific dataset.

- **Depth analysis (Table 2) is presented without investigation.** The finding that depth from 2 to 16 layers makes little difference is reported honestly, but the paper offers only a brief conjecture (one hidden layer suffices). A more thorough discussion of why this occurs would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- An ablation study varying $\alpha$ (as noted above) would strengthen the core claim about heavy-tailed priors driving performance.
- An empirical check that increasing depth *does* matter in problems with more complex structure (e.g., hierarchical discontinuities) would round out the depth analysis.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Theorem 1 uses incorrect scaling; $M_\ell^{-1/2}$ is incompatible with $\alpha$-stable convergence."**  
   *Reason for removal:* Factually wrong. The critic treats the weights as i.i.d. with infinite variance, ignoring that $s_+^{(\ell)}$ is a *common* scale factor shared across all $i$ in layer $\ell$, which factors out and leaves a finite-variance sum to which the classical CLT applies. The construction is standard and valid.

2. **"Missing connection to prior stable-limit literature (Der & Lee 2005, Peluchetti, Favaro, etc.)."**  
   *Reason for removal:* The paper explicitly cites all these works at lines 20--21, stating: "The first non-Gaussian limit result of its kind was given by \citet{DerLee2005}... Recent extensions to deep feedforward networks are by \citet{Peluchetti}, \citet{favaro} and \citet{lee2023deep}."

3. **"Those works all use $n^{1/\alpha}$ scaling; the scaling discrepancy is a serious inconsistency."**  
   *Reason for removal:* Those works use $n^{1/\alpha}$ because they treat i.i.d. infinite-variance weights without a common scale factor. The paper's construction is deliberately different — the common scale factors it out — so the $n^{1/2}$ scaling is appropriate and not inconsistent.

4. **"Theorem statement provides no proof or even a sketch."**  
   *Reason for removal:* The paper references a supplementary section (line 138), and the hard rules require removing criticisms about missing proofs in the appendix, as the parser strips those sections from all papers.

5. **"The depth result 'may be an artifact of the model rather than a property of a properly derived stable process.'"**  
   *Reason for removal:* This is speculation, not a concrete weakness, and is predicated on the (incorrect) assumption that the theoretical derivation is flawed.

6. **"Experiments do not validate the infinite‑width limit claim."**  
   *Reason for removal:* The infinite-width limit is a mathematical statement, not an empirical claim that experiments could "validate" in the sense the critic demands. The paper uses the limit to *motivate* the kernel process, and the experiments validate the *resulting method*.

## Novel Insights

None beyond the paper's own contributions. The reviews do not reveal insights about the paper that the authors themselves did not articulate.

## Suggestions

1. **Add an $\alpha$ ablation.** Run D$\alpha$-KP with $\alpha \in \{0.5, 1, 1.5, 2\}$ on at least the 1-d discontinuous function (Section 3.2) to directly demonstrate that the non-Gaussianity drives performance gains. This is the single most impactful addition.

2. **Include a brief intuitive explanation in Section 2** of why the $1/\sqrt{M_\ell}$ scaling works despite infinite-variance weights. The sentence "[because] $s_+^{(\ell)}$ is shared across all $i$ and thus factors out of the sum, leaving a finite-variance term to which the CLT applies" would preempt the very confusion that arose in review.

3. **Temper the claim on the Boston dataset** (Table 3) from "best" to "competitive," since D$\alpha$-KP ties with GP Bayes within one standard deviation.

4. **Add a discussion of why depth has little effect** (Table 2) — even a brief reference to the relevant theory on trainable depth (Schoenholz et al. 2017, already cited) would strengthen the interpretation.

## Score and Decision

The paper makes a genuine contribution: a theoretically sound, computationally tractable extension of deep kernel processes to infinite-variance (stable) priors, with demonstrated benefits on discontinuous functions and real benchmarks. The harsh critic's main criticism is based on a misunderstanding of the weight construction and does not hold. The paper's weaknesses are minor and addressable.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>