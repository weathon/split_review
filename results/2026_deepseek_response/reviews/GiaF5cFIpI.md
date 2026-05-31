Now I'll write the final consolidated review.

## Summary

This paper proposes a real-time adaptive stimulation framework for driving latent neural dynamics, combining: (1) streaming latent space construction including a novel sjPCA method, (2) nonparametric kernel regression for modeling the stimulus-response mapping with temporal discounting to handle nonstationarity, and (3) constrained optimization to design high-dimensional stimulation patterns respecting non-negativity, box, and sparsity constraints. The method is validated on a toy model and on real neural recordings (calcium imaging, electrophysiology) with simulated stimulation effects.

## Strengths

1. **Novel streaming sjPCA method with Orthogonal Procrustes stabilization** (Section 2.1, Equation 2): Introduces a streaming version of jPCA that explicitly stabilizes each discovered plane of rotation independently. Figure 1a shows convergence to the offline fit within seconds, enabling real-time tracking of rotational neural dynamics — something prior streaming methods like proSVD do not target. This is a genuine methodological contribution to online dimensionality reduction for neuroscience.

2. **Nonparametric kernel regression with temporal discounting for stimulus-response mapping** (Section 2.3, Equation 7): Models the effect of stimulation as a function of latent state, stimulus, and sample age via a product of RBF kernels. The time-dependent kernel allows the model to recover from abrupt flips (~15s recovery in Figure 2e) and track continuous drift in the underlying mapping, addressing real-world nonstationarities like photobleaching, plasticity, or probe shifts that would break non-adaptive alternatives.

3. **Constrained optimization targeting arbitrary latent directions** (Section 2.4, Equation 8): Formulates a differentiable optimization with non-negativity, box constraints, and an L1 sparsity penalty, leveraging the kernel model's differentiability. For feasible target directions, 517/600 optimizations achieve <1° alignment (Section 4.2), and Figure 4c shows the predicted error serves as a reliable lower bound. This goes substantially beyond prior work that selects from predetermined stimulus sets or ignores realistic constraints.

4. **Real-time feasibility demonstrated** (Section 3): Reports end-to-end runtimes averaging <10ms and always below 100ms on a standard workstation for a full timepoint including streaming dimensionality reduction, dynamics prediction, and stimulus optimization. This is critical for future *in vivo* closed-loop experiments.

## Weaknesses

### Major

- **Insufficient baselines for the optimization framework**: The optimization is compared only against random single-neuron stimulation, random multi-neuron stimulation, and shuffled versions of the designed stimuli (Figure 4a). The paper cites prior work addressing the same or similar problems — Minai et al. (2024) with Bayesian optimization, Wagenmaker et al. (2024) with active learning, Draelos & Pearson (2020) with Bayesian variational inference — but does not compare against any of them. Even a simple alternative such as linear regression of stimulation effects followed by constrained quadratic programming with the same constraints (non-negativity + sparsity) is absent. Without at least one nontrivial baseline, the paper demonstrates only that "nonrandom is better than random," which is insufficient to support the claim that the nonparametric kernel regression + L1-regularized optimization offers a meaningful advantage.

### Minor

- **sjPCA contribution is under-integrated**: The novel streaming sjPCA (Section 2.1, listed as a contribution) is validated for convergence to offline fit (Figure 1a) but is not used in the stimulation-response or optimization experiments — those use proSVD (Section 4.1). The parallel multi-space evaluation (Figure 1c) is interesting but is not connected to stimulation design; the paper does not demonstrate that sjPCA or adaptive space switching improves stimulation targeting outcomes. This component feels like a separate contribution rather than an integrated part of the framework.

- **Real-data validation uses simulated stimulations with untested assumptions**: The paper is transparent about this (Section 4.1 explicitly says "simulated stimulations using an autoregressive function"), but the abstract's framing ("real neural data") could lead readers to expect closed-loop optogenetic/electrical stimulation experiments. The stimulation model ($a_t = 0.8 a_{t-1} + u_t$) uses a fixed decay coefficient, assumes additive effects with no noise in the stimulation effect, and is never varied to test robustness. The method's ability to handle the unknown, nonlinear, and often failure-prone effects of real stimulation remains unvalidated.

- **No sensitivity analysis for key hyperparameters**: The L1 penalty weight $\lambda_1$ in Equation (8) and the kernel length scales in Equation (7) lack ablation or sensitivity analysis. The time kernel's role is described verbally ("if the system is stable, it can ignore the time feature") but its impact is never isolated or ablated in experiments. This makes it difficult to assess how much the method's performance depends on careful hyperparameter tuning.

- **Electrophysiology results not displayed**: The electrophysiology dataset (O'Doherty, 2024, 130 units, 30 Hz) is described in Section 4.1, but the stimulation-response and optimization results shown are from the calcium dataset only. No corresponding figure or quantitative summary for the electrophysiology data appears in the main text (the appendix is stripped, so results there cannot be evaluated).

### Trivial

- **Figure 5 shaded regions**: The caption states "solid lines are average values across experiments" but does not specify what the shaded regions represent (standard deviation? confidence interval?).

## Nice-to-Haves

- Add at least one nontrivial optimization baseline (e.g., ridge-regression estimate of $S$ followed by a quadratic program with the same constraints) to establish the value of the nonparametric approach.
- Ablate the kernel regression model: compare (a) full kernel with time kernel, (b) kernel without time kernel, (c) a simple linear model for $S$.
- Integrate sjPCA into the stimulation experiments, for example by testing whether stimulation targeting differs when the latent space is constructed via sjPCA vs. proSVD, or by demonstrating adaptive space switching in a nonstationary scenario.
- Provide sensitivity analysis for $\lambda_1$ and kernel length scales.
- Add error quantification (standard deviations or confidence intervals) for the optimization results in Figure 4a and the closed-loop results in Figure 5.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No error bars/confidence intervals for Figure 4 violin plots"** (Harsh Critic): Violin plots inherently show the full distribution of data, not summary statistics. This criticism misunderstands the visualization. REMOVED.

2. **"L1 penalty does not enforce L0 sparsity"** (Harsh Critic): The paper explicitly acknowledges this limitation at line 148 ("Rather than employ the $L_0$ constraint on the number of neurons, which would make the problem NP hard in general, we use an $L_1$ constraint"). This is standard practice in optimization and is not a flaw. REMOVED.

3. **"Evaluation on real neural data is misleading — stimulation effects are simulated"** framed as a Critical Issue: The paper is transparent about this in Section 4.1 ("simulated stimulations using an autoregressive function"). The abstract correctly describes using "real neural data" (the recordings are real), with simulated stimulation effects. There is no deception. However, the limitation of simulated stimulation is real, and that is retained as a Minor weakness above. The "misleading" framing is removed. REMOVED.

4. **"No comparison to existing stimulation optimization methods"** framed as fatal: This is valid and is retained as the Major weakness above. However, the harsh critic's assertion that the paper's "central claim [is] unverifiable" is too strong — the paper does show that its method can target arbitrary latent directions with high precision, which is a nontrivial algorithmic result even without baselines. The framing is softened. PARTIALLY RETAINED as Major.

5. **Strength Finder generic claims**: Strengths like "addressed an important problem" or "targeted an interesting question" are removed as generic. Kept only concrete, evidence-grounded strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the paper that the authors' own discussion does not already cover.

## Suggestions

The single highest-leverage improvement is to replace one random baseline with a simple but credible alternative: collect the same initial 10–20 stimulation-response observations, fit a linear (or ridge) regression to estimate $S$, then solve a quadratic program with the same non-negativity and L1-mimicking constraints. Compare closed-loop performance. This would directly test whether the nonparametric form matters and give readers a meaningful sense of the advantage. Second, ablate the time kernel from Equation (7) to isolate its contribution to handling nonstationarity. Third, move the sjPCA results from Figure 1 into an ablation showing whether switching latent representations improves stimulation targeting — or, if this is infeasible, reframe the contribution to separate sjPCA from the core stimulation pipeline.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| BBldjKEBlJ.md (QuantFormer) | 3.00 | R1-low | Much weaker — no framework for stimulation design, purely predictive |
| NPzuN3Rxi8.md (TAVRNN) | 3.00 | R1-low | Much weaker — no closed-loop or optimization component |
| fnO5h1CFyh.md (DHTM) | 3.00 | R1-low | Unrelated; much weaker |
| nwDRD4AMoN.md (Kuramoto neurons) | 9.00 | R1-low-outlier | Much stronger — accepted paper, very different topic |
| 4ltiMYgJo9.md (Closed-loop EEG) | 5.75 | R1-mid | Comparable — similar validation gaps but different domain (visual stimuli) |
| FwW3jqchtY.md (iSSM) | 5.00 | R1-mid | Similar domain, slightly weaker — this paper has more novel components |
| MFCjgEOLJT.md (Locomotion control) | 5.75 | R1-mid | Comparable — accepted despite baseline gaps |
| LNp7KW33Cg.md (HDA) | 5.00 | R1-mid | Related (neural dynamics) but different problem; comparable quality |
| cNmu0hZ4CL.md (Optimal transport) | 8.00 | R1-high | Much stronger — polished evaluation, clearly different domain |
| cmfyMV45XO.md (Feedback NODEs) | 8.00 | R1-high | Much stronger — rigorous, clear |
| Xo0Q1N7CGk.md (Grid cells) | 8.00 | R1-high | Much stronger — focused, well-executed |

**Round 2 — Narrowing:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| FwW3jqchtY.md (iSSM) | 5.00 | R2 | Slightly weaker — current paper has more novel components (sjPCA, kernel model, optimization), though both share weak-baseline issues |
| LNp7KW33Cg.md (HDA) | 5.00 | R2 | Less relevant domain; comparable quality |
| WQwV7Y8qwa.md (MR-SDS) | 5.80 | R2 | Similar space, different problem (multiregion); stronger evaluation |
| TVnkjz4MqV.md (NMR) | 5.50 | R2 | Comparable — interesting technical contribution, similar validation gaps |
| 3usdM1AuI3.md (BRAID) | 6.25 | R2 | Stronger — better evaluation (baselines, ablations, error bars), similar domain |
| 4UXIGATUTj.md (Forecasting whole-brain) | 6.33 | R2 | Different domain; stronger on evaluation |
| LbgIZpSUCe.md (Nonlinear multiregion) | 7.33 | R2 | Stronger — accepted, more rigorous |
| DkYQHewNcp.md (Constrained filters) | 6.33 | R2 | Different domain, similar evaluation level |

**Round 1 Bracket**: 4.0–6.5
**Round 2 Narrowing**: The paper sits between iSSM (5.00) and BRAID (6.25), closest to NMR (5.50). It is stronger than iSSM because its framework addresses a harder problem (stimulation *design* rather than just modeling intervention effects) with more novel components, but notably weaker than BRAID which has proper baselines, ablations, and error quantification.

### Final Score

The paper proposes a well-motivated framework for a genuinely important problem — real-time adaptive stimulation of latent neural dynamics. The individual components (sjPCA, kernel regression for stimulus-response mapping, constrained optimization) are technically sensible and together form a novel contribution. However, the empirical validation has significant gaps: only trivial baselines, simulated rather than real stimulation effects on the neural data, an under-integrated sjPCA contribution, and missing sensitivity analyses. These issues are fixable without new wet-lab data, but as presented, the evidence does not convincingly establish that the method improves upon simple alternatives or will work under real experimental conditions.

**Score**: 5.5

**Decision**: Borderline — the core ideas are novel and well-motivated, but the evaluation needs substantial strengthening to support the claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>