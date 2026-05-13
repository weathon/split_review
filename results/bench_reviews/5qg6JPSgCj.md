Now let me run calibration search while I read more of the paper:Now let me read a few key anchor papers:Now I have enough information to write the comprehensive final review. Let me synthesize everything.

---

## Summary

FPNN (Fokker-Planck Neural Network) proposes a score-based reformulation of the PDE residual loss for solving steady-state Fokker-Planck (SFP) equations. The core insight (Theorem 1) is that the plain PDE loss can be rewritten purely in terms of the score function of the unnormalized density, which is invariant to the partition function Z_θ. This decouples density-shape learning from normalization enforcement, allowing arbitrary network architectures (TNN and MLP) and computing Z_θ only once as a post-processing step. The method uses SDE simulation (SRK with strong order 1.5) to generate training samples from the invariant distribution, and demonstrates strong accuracy and parameter efficiency on 4D–20D SFP problems.

---

## Strengths

- **Algebraically clean score-based reformulation (Theorem 1):** The derivation that $p_\theta$ and $\tilde{p}_\theta$ share the same score function, allowing the PDE loss to be expressed purely in terms of the score (Eq. 5) without involving Z_θ, is a genuine and non-trivial insight. This resolves the normalization/collapse tension in PINN-style approaches without requiring soft penalty terms or specialized network architectures.

- **Concrete parameter and computational efficiency:** On the 4D Ring problem, MLP-FPNN achieves 11.36% MAPE with only 256 parameters in 4.8 minutes, versus TFFN's 33,792 parameters over 27.6 minutes with far worse results (Table 3, Figure 4a). These numbers are concrete and specific.

- **Efficient partition function via TNN tensor structure (Theorem 2):** The decomposition of the high-dimensional integral into a product of 1D Gauss-Legendre quadratures avoids Monte Carlo variance and is an efficient, principled contribution for TNN-parameterized densities.

- **Numerical stability of score loss across dimensions (Figure 5):** The score PDE loss consistently stays in the range $10^2$ to $10^{-1}$ across 4–20D problems, unlike plain PDE loss whose magnitude varies with dimensionality. This is verified empirically and is a meaningful diagnostic property.

- **Architecture-agnostic framework:** FPNN supports both TNN and MLP (and ResNet) parameterizations with comparable effectiveness (Table 5, Figure 8), demonstrating the generality of the score-based decoupling.

- **SRK-based adaptive domain selection (Algorithm 1):** Using SDE simulation to adaptively discover the high-probability support region is more principled than fixed-grid approaches and avoids wasting capacity on near-zero regions.

---

## Weaknesses

### Fatal
None. The paper's core contribution—the score-based FP loss decoupling—is mathematically valid, and the training procedure is clearly described.

### Major

- **Informational asymmetry in comparisons undermines the speedup and accuracy claims.** FPNN requires samples drawn from the true invariant distribution $p(x)$ (Section 3.2: "we need training data from the true distribution $p(x)$ of SFP equation, which can be sampled through the SDE simulation"). The baselines it outperforms—PINN, TFFN, normalizing flow methods—operate using only the PDE equation without access to samples from $p(x)$. This means FPNN is given strictly more information than the baselines. The accuracy improvements and the >20× speedup cannot be cleanly attributed to the score-based loss design; some or all of the advantage may come from this informational head-start. A critical missing ablation is comparing FPNN against vanilla score matching or a normalizing flow trained on the same SDE-generated data without the FP constraint. If those methods match FPNN's accuracy, the FP constraint adds nothing; if they don't, the FP constraint's value is demonstrated. This causal gap directly threatens the paper's core claim.

- **SDE simulation cost is excluded from all timing comparisons.** Section 4.2 attributes the 20× speedup to "improved optimization dynamics and post-process of normalization," but the time required to run Algorithm 1 (SRK simulation until convergence to the invariant distribution) is never reported. Baselines are timed from scratch without any pre-computation, while FPNN benefits from a pre-solved simulation stage. Until the full pipeline (SDE simulation + FPNN training) is timed against baselines on equal footing, the 20× figure is unsubstantiated.

### Minor

- **"Without labeled data" framing is potentially misleading.** The Abstract claims "Without any labeled data, FPNNs achieve MAPE of 11.36%..." While technically correct that the method uses no pointwise $(x, p(x))$ pairs, it does rely on samples from the true invariant distribution—which encodes the distributional structure of the solution. This framing creates a false impression that FPNN operates under the same information budget as PINN-type methods, which it does not. The paper should clearly distinguish what information is used versus what traditional "labeled data" means in the PDE context.

- **Partition function MC estimation degrades significantly in higher dimensions.** The paper honestly reports (Figure 7a, Section 4.2) that MLP-FPNN with the default $|\mathcal{D}_Z| = 20k$ yields MAPE of 58.66% on the 10D Gaussian mixture, improving to 18.38% only after increasing to 100k samples. While this is disclosed, no analysis is provided of how $|\mathcal{D}_Z|$ must grow with dimension d for fixed-accuracy estimation. This is relevant to the claimed scalability to 20D+ problems.

- **The 20D scalability experiment uses an isotropic Gaussian (Figure 10),** which is arguably the simplest possible high-dimensional density: fully factorized, no multi-modality, no ring structure, mode at origin. Success on this problem is expected and is weak evidence for general 20D scalability.

- **No analysis of the tolerance to SDE approximation error.** Section 3.2 states "we do not require the data points to exactly follow the true distribution $p(x)$, and our loss function offers a degree of tolerance and flexibility." This claim is never analyzed or tested experimentally. No bound on how much distributional mismatch the method can tolerate is given, and no experiment deliberately degrades simulation quality to probe this robustness.

- **MAPE metric choice.** MAPE is sensitive to near-zero probability regions and can give a misleading picture of accuracy for densities that approach zero over large portions of the domain. The choice of MAPE over $L^2$ error, KL divergence, or TV distance is not justified.

### Trivial

None.

---

## Nice-to-Haves

- Run SDE simulation + FPNN training vs. baselines end-to-end under the same hardware and time budget to give an honest speedup figure.
- Compare against vanilla score matching or normalizing flows trained on the same SDE-generated data (without the FP constraint) to isolate the value added by the FP constraint specifically.
- Provide a scaling analysis of $|\mathcal{D}_Z|$ with dimension for fixed MAPE tolerance.
- Add at least one 20D experiment with a non-trivial density (multi-modal or ring-like) to make the scalability claim more convincing.
- Clarify the "without labeled data" claim to explicitly describe what distributional information the method does use.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Missing sections (OCR artifacts, lines 432–485 of parsed text).** The parsed document contains bare line numbers (177–230) corresponding to the absent Section 4 and 4.1. Per the review rules, parser strips sections from the submission — these sections exist in the original. This criticism is a parser artifact and is removed.

- **Harsh Critic: Constant factor in Theorem 1 is unanalyzed.** The critic notes the "constant factor" ($\mathbb{E}[|\mathcal{L}p_\theta|]$) is not analyzed. Theorem 1 is a valid algebraic reformulation; the constant is part of the proof structure, and absence of a full convergence analysis is standard for empirical PINN-style papers. Removed as scope creep.

- **Harsh Critic: Power embedding not demonstrated for non-polynomial drift.** The ablation in Table 4 is referenced, and the paper explicitly scopes to polynomial-form drift in that context. The broader utility of PE is a nice-to-have, not a fatal flaw.

- **Harsh Critic: RealNVP and GMM comparison uses off-the-shelf models.** The paper's point is that hard-constraint architectures limit representation; comparing against standard implementations makes the point fair. The criticism that "purpose-built" flow solvers might do better is speculative. Removed.

- **Strength Finder: "This paper addresses an important problem"** — removed as generic.

- **Strength Finder: "Architecture-agnostic framework enables scalability"** — kept in filtered form above with concrete evidence.

---

## Novel Insights

The reviewer's most incisive observation is that the paper blurs the boundary between *solving a PDE* and *fitting a density to samples from its solution*. Since the SDE simulation already converges to the invariant distribution, FPNN is in effect applying score matching to those samples, with the FP constraint serving as an inductive bias rather than the primary information source. Whether that inductive bias (the score-based FP loss) meaningfully improves over unconstrained score matching on the same data is never tested. This question—how much does knowing the PDE equation help when you already have samples from its solution?—is actually the most interesting scientific question the paper raises, but does not answer. Clarifying this via ablation would transform the paper's contribution from "a faster PDE solver" into "a demonstration that PDE structure improves sample-efficient density learning," which would be a stronger and more principled claim.

---

## Suggestions

1. **Run the key ablation:** Train a standard score matching model (Hyvärinen 2005) and/or a normalizing flow directly on the SDE-generated data, without any FP constraint. Report MAPE against FPNN on the same benchmarks. If FPNN wins, the FP constraint is earning its keep. If it doesn't, the method reduces to SDE simulation + score matching.
2. **Report full pipeline timing:** Include SDE simulation time in every wall-clock comparison. This directly validates or invalidates the 20× speedup claim.
3. **Add a non-trivial high-dimensional experiment:** Replace or supplement the 20D isotropic Gaussian with a 10D+ ring or multi-modal problem to support the scalability claim.
4. **Provide a $|\mathcal{D}_Z|$-vs-dimension scaling curve:** Show how MC sample requirements for partition function estimation grow with d, so practitioners can judge feasibility.

---

## Score and Decision

**Anchor comparison:**

| Path | Avg Human Score | Comparison to this paper |
|---|---|---|
| `/uWHPW0sXFK.md` (PINF: CNF for Fokker-Planck) | 3.50 | Most directly related paper; rejected for missing baselines and unclear motivation. FPNN is clearly stronger: it has comprehensive baselines, a clean theoretical contribution, and solid empirical coverage. FPNN is well above PINF. |
| `/5sPgOyyjG5.md` (Feynman-Kac Estimator) | 3.00 | Rejected for vague contribution and unclear motivation. FPNN is stronger in every dimension. |
| `/EP09OGPRzk.md` (L-PINN: Langevin Dynamics) | 6.00 | Rejected despite 6.0 score; addresses PINN optimization dynamics with strong experiments. Comparable ambition to FPNN; FPNN has a cleaner theoretical contribution but the informational asymmetry issue is a comparability gap that L-PINN doesn't have. |
| `/ApjY32f3Xr.md` (PINNacle Benchmark) | 5.25 | Rejected; benchmark paper for PINNs. Less methodological novelty than FPNN but cleaner comparison. |
| `/wVADj7yKee.md` (SINGER: High-dim PDE) | 6.33 | Accepted. Solves high-dimensional PDEs with GNN, strong experiments across 5–20D. Similar scope to FPNN with a comparable theoretical contribution; SINGER does not have the informational asymmetry issue that FPNN does. |
| `/x4ZmQaumRg.md` (Active Learning for Neural PDE) | 7.00 | Accepted with high score; comprehensive benchmark study. Sets the bar for accept-level PDE solving work. FPNN's contribution is narrower. |
| `/fU8H4lzkIm.md` (PhyMPGN) | 8.00 | Accepted at top tier; strong theoretical + experimental package. FPNN is well below this level given the comparison gaps. |
| `/f3xXPDCh8Q.md` (Unisolver) | 5.50 | Rejected; ambitious universal PDE solver with methodological scope issues. Comparable situation to FPNN — strong idea but weaker-than-claimed experimental validation. |
| `/GkJCgUmIqA.md` (PINN Trust-region SQP) | 3.00 | Rejected; incremental PINN improvement with limited scope. FPNN is much stronger. |

**Assessment across axes:**

- *Originality*: High — the score-based decoupling for FP equations is genuinely novel and non-obvious.
- *Importance of research question*: High — high-dimensional FP equations are a real challenge with applications in physics, finance, and control.
- *Claim support*: Moderate — the algorithmic contribution is well-supported, but the speedup and accuracy advantages over baselines are confounded by the informational asymmetry (SDE samples not available to baselines, SDE cost not counted in timing).
- *Soundness of experiments*: Moderate — results are internally consistent and the method is clearly superior on the tested benchmarks, but the critical ablation (FPNN vs. score matching on same SDE data) is missing.
- *Clarity*: Good — the framework is explained clearly; the "without labeled data" framing creates some confusion.
- *Value to community*: Moderate-high — the score-based FP loss design is a useful building block, even if the speedup claims need recalibration.

FPNN sits between PINF (3.5, rejected, much weaker paper) and SINGER (6.33, accepted, stronger experimental rigor). The informational asymmetry in the comparison is a real and significant concern that prevents full acceptance — it is not fatal (the score-based contribution is real) but it is major enough that the speedup and accuracy claims require reframing. The paper is in borderline-reject territory at this stage, primarily needing the ablation and timing experiments before the comparison framework is credible.

**Final Score: 5.0**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>