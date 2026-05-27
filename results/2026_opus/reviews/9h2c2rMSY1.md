Now I have enough calibration to write the final review.

## Summary
The paper studies conformal prediction (CP) for time-dependent PDE surrogates, where calibration and test samples come from different times and are not exchangeable. It proves (Theorem 4.1) that for the 1D heat equation with a specific Gaussian initial condition, the laws at any two distinct times are mutually singular in function space (TV distance = 1), and (Theorem 4.2) that for spatially-discretized linear PDEs with Gaussian (or location-scale) initial conditions, the discretized solution is Gaussian with closed-form mean and covariance, enabling exact density-ratio weights in weighted split CP. Empirical validation uses one synthetic 1D linear-PDE family $u_t + a u_{xx} + b u_x + c u = 0$ and a brief pulsed-thermography (heat-equation) example.

## Strengths
- **Closed-form weights for weighted CP in a well-defined regime (Theorem 4.2 + §4.4).** Once the discretized linear-Gaussian setting is taken for granted, the density ratio in eq. (1) is exact, so weighted CP delivers formal coverage without estimating weights — a clean methodological move. Remark 4.3 extends the construction to the location-scale family.
- **Honest reporting of "refusal to predict."** Table 1 reports $n_\infty$ (fraction of samples for which WCP emits infinite bands), and the paper explicitly argues that producing trivial bands is preferable to silent undercoverage in safety-critical settings. This transparency about the method's degenerate mode is a positive.
- **Empirical separation against the chosen baselines.** Figure 3 / Table 1 show that as the PDE becomes more unstable ($a$ more negative), naive CP and LSCI undercover earlier and more severely, while WCP either holds 90% coverage or correctly switches to trivial bands. WCP is also reported to run in seconds versus ~40 minutes for LSCI.
- **Theorem 4.1 sharpens the motivation for the discretized treatment.** Even if it is essentially a Feldman–Hájek instantiation (the paper itself cites Hairer), formalizing TV = 1 for the heat-equation pushforward is a clean way to justify abandoning the function-space framing for CP. The paper explicitly notes this is "not necessarily problematic for practical CP" on discretized data.

## Weaknesses

### Fatal
None — the underlying method is correct and honestly implemented within its stated scope.

### Major
- **Scope mismatch between motivation and contribution.** §1 motivates with weather, climate, stock-market crashes, and financial modeling — phenomena that are nonlinear, often non-Gaussian, and not described by linear PDEs with Gaussian initial conditions. Theorem 4.2 requires (i) linearity of $\mathcal{L}_x$, (ii) Gaussian (or location-scale) IC, and (iii) knowledge of $\mathbf{A}$ and $\mathbf{r}(t)$ sufficient to compute the matrix exponential and covariance in closed form. The discussion (§6) admits nonlinear PDEs are "future work," but the motivating use cases are precisely the ones outside scope. The abstract's claim that the method provides "exact coverage guarantees through reweighting calibration scores" for time-dependent PDEs should be qualified to linear, Gaussian-IC, known-operator settings.
- **Trajectory-level CP not used as a baseline.** §2 discusses Moya et al. (2025), Gray et al. (2025), and Gopakumar et al. (2025) — methods that calibrate at the trajectory level and provide valid coverage when trajectories are i.i.d. (which is precisely how the synthetic experiments are constructed). These methods are dismissed for not extending beyond the calibrated horizon, but they are an obvious within-horizon comparator with formal guarantees. Comparing only against naive split CP (which the paper itself flags as having "no formal guarantees") and LSCI (which the paper expects to fail under their setup) makes the headline "WCP is the only method providing formal guarantees" weaker than the writing suggests. Including a trajectory-level baseline would let the reader see what per-time-step WCP buys.
- **The regime where WCP differs from naive CP is also where it refuses to predict.** Table 1 shows at $a=-0.0075$: $n_\infty=86.4\%$ at $t=15$ and $100\%$ at $t=20$; at $a=-0.01$: $35.4\%$ at $t=10$ and $100\%$ at $t=15$. In every row where naive CP and LSCI visibly undercover, WCP responds with infinite bands. The paper frames this as a feature, and it defensibly is — but the upshot is that the empirical claim collapses to "WCP correctly recognizes when it has nothing to say." A characterization of the horizon at which WCP becomes vacuous as a function of system properties (e.g., spectral gap of $\mathbf{A}$, KL between $\mathcal{P}_{t+\delta}$ and $\mathcal{P}_t$) would convert this finding into a deployment criterion rather than a coverage trivium.
- **Unexplained sub-nominal coverage at $a=-0.005, t=15{-}20$.** Table 1 shows WCP coverage of 0.88 ($t=15$) and 0.85 ($t=20$) at the 90% nominal level, with $n_\infty = 0.0\%$ and $0.2\%$, so roughly 5000 and 4990 samples remain. The paper attributes coverage drops to "higher stochastic noise" when "very few samples remain," but that explanation does not apply to these rows — with 5000 samples the standard error on empirical coverage is $\approx 0.004$, so 0.85 is several SEs below the 0.90 target. Either the weighted-quantile computation has noticeable numerical error or the formal-guarantee narrative needs a tighter empirical match. The paper's blanket claim that WCP "consistently meets its coverage guarantees" should be reconciled with these specific rows.

### Minor
- **Narrow synthetic evaluation.** A single PDE family (constant-coefficient $u_t + a u_{xx} + b u_x + c u = 0$ with $b=-0.5$ in the main table) is studied. Even within the linear regime, no advection-diffusion-reaction with spatially varying coefficients, no wave equation, no 2D synthetic, and no non-trivial source term $\mathbf{r}(t)$. The generality claimed for Theorem 4.2 deserves at least a small-scale demonstration on another linear operator.
- **Real-world example is one paragraph and inside the closed-form sweet spot.** Pulsed-thermography cooldown follows the heat equation, exactly the regime where the closed-form construction trivially applies. Calling this "demonstrating applicability in real-world scenarios" without any nonlinear, noisy, or model-mismatched setting somewhat oversells the empirical reach.
- **The connection between weighted CP and the temporal setup deserves a paragraph in §4.4.** Standard weighted CP results apply when reweighting is on the conformal-score input distribution. Here the test "covariate" $\mathbf{u}_t$ at the future time is itself random with a known law, and the calibration and test samples come from the same trajectory distribution at different times. The argument for why standard weighted CP transfers cleanly to this setting (rather than the more usual fixed-test-$x$ covariate shift) is implicit; making it airtight would help.
- **Idealized data-generating process.** §4.1 assumes calibration data are obtained by simulating the *known* PDE from sampled ICs — no observational noise, no model–data mismatch. For real measurements (such as the thermography example), the calibration distribution will not exactly equal the Gaussian density used in the weight. The paper does not test robustness of WCP under operator/IC misspecification, which is the most pressing question for any practical adoption.

### Trivial
None of weight.

## Nice-to-Haves
- A horizon study quantifying how $n_\infty(t)$ scales with the spectrum of $\mathbf{A}$ (or with $D_{\mathrm{KL}}(\mathcal{P}_{t+\delta}\,\|\,\mathcal{P}_t)$), giving practitioners a guideline for the maximum horizon at which non-trivial bands are obtainable.
- A robustness ablation: how does coverage degrade when $\mathbf{A}$, $\boldsymbol{\Sigma}_0$, or boundary terms are estimated from data with error rather than assumed exactly?
- Direct comparison with a trajectory-level CP baseline (Moya et al. 2025; Gray et al. 2025) on the same synthetic family, showing where WCP wins, ties, or loses by horizon.
- At least one experiment outside the linear-Gaussian-known-operator triad (even an approximate one) to show a path toward the motivating use cases.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *"If $\mathbf{A}$ is known and $\mathbf{u}_0$ is Gaussian, one can read off marginal/joint intervals analytically without any surrogate."* — This is a valid observation but it conflates the role of the surrogate (which is a fast approximation for downstream prediction tasks) with the role of CP (which is the uncertainty layer on the surrogate's residuals). The paper's setup is that one uses a neural-operator surrogate for speed and then calibrates its residuals with WCP; the closed-form Gaussian law is used only for the weight, not as a substitute predictor. Demoted from "fatal/major methodological gap" to a removed framing point.
- *"Theorem 4.1 is a Feldman–Hájek strawman."* — The paper itself acknowledges the result is representative of a broader phenomenon (citing Hairer) and explicitly says it is "not necessarily problematic for practical CP." The theorem is correctly positioned as a motivating observation, not a deep theoretical contribution; framing it as a "strawman" overstates the criticism. The substantive part of this critique — that the theorem doesn't actually attack practical neural-operator CP methods which work on discretized grids — is fair but does not invalidate the result and is already conceded in §4.2.
- *Strength: "addresses an important problem."* — Generic; dropped per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The combination of "use the closed-form Gaussian law of a linear-PDE discretization to drive weighted CP with exact density ratios" is the paper's own observation, and the synthesis here does not surface additional novel insight beyond it.

## Suggestions
- Rewrite §1 and the abstract to scope the contribution to discretized linear PDEs with Gaussian/location-scale ICs and a known operator; move the weather/climate/finance motivation to a "broader future direction" framing or qualify it explicitly.
- Add a trajectory-level CP baseline (e.g., Moya et al. 2025) to Figure 3 / Table 1 so the comparison set includes a method with formal guarantees.
- Add a horizon characterization: plot $n_\infty(t)$ against a system property (spectral gap of $\mathbf{A}$ or analytic KL/TV between $\mathcal{P}_t$ and $\mathcal{P}_{t+\delta}$ from Theorem 4.2 + Remark 4.4) and use this to define the operational horizon.
- Provide a misspecification ablation (estimated vs true $\mathbf{A}$, non-Gaussian IC, observation noise) to quantify how brittle the closed-form-weights argument is.
- Reconcile the $a=-0.005, t \in \{15,20\}$ rows in Table 1 with the "consistently meets coverage" claim — either tighten the wording or explain the residual gap.

## Evaluation against own community standards
- **Originality:** Modest. The Feldman–Hájek-style observation is well-known in PDE-on-Hilbert-space contexts; the closed-form Gaussian for linear ODE systems is textbook. The novel combination is plugging these into weighted CP — a clean but incremental synthesis.
- **Importance of the research question:** Real. Uncertainty quantification for time-dependent PDE surrogates is a live problem and exchangeability genuinely breaks here.
- **Are the claims well-supported?** Partially. The formal claim (weighted CP with closed-form Gaussian ratios) is supported. The framing claim ("exact coverage guarantees for PDEs without limiting assumptions on their time-dependent behavior") is not — the assumptions are quite restrictive, and one row in the main table dips below nominal without an adequate explanation.
- **Soundness of experiments:** Narrow. One PDE family, three values of one parameter, a brief real-world example inside the closed-form regime, baselines stacked toward methods the authors expect to fail.
- **Clarity:** Generally good. The exposition is readable and the figures are clear.
- **Value to the community:** Modest. A clean baseline construction for a niche regime; would gain substantial value with the trajectory-level comparison and a horizon characterization.

## Score and Decision

**Calibration anchors and how they compare:**

Round 1 (bracketing):
- `fzZfju8y0g.md` — In-Context Neural PDE, avg 3.40, Reject. Different topic (PDE learning, not CP).
- `LwAG269lIq.md` — PDE discovery via adjoint method, avg 3.00, Reject. Different topic.
- `v8RDgaEtE2.md` — CP under bias, avg 2.50, Reject. CP topic; this paper is clearly stronger.
- `GkJCgUmIqA.md` — Trust-region PINNs, avg 3.00, Reject. Different.
- `cF6OoaYcRa.md` — Calibrated Physics-Informed UQ (CP for neural PDEs), avg 4.50, Reject. Very close topic; reviewers complained about minor extension and limited evaluation.
- `XxxKHiy9Gw.md` — CoCo-PINNs, avg 4.33, Reject. Different.
- `vcX0k4rGTt.md` — Gauss-Newton approximate full-CP, avg 5.75, Accept. More technically novel than this paper.
- `WwQdcQROmb.md` — Safe physical control, avg 4.00, Reject. Different.
- `5KqveQdXiZ.md` — Constrained PDE learning, avg 5.25, Accept. Different.
- `bWcnvZ3qMb.md` — FITS, avg 8.00, Accept. Off-topic (time series).
- `xriGRsoAza.md` — MILLET, avg 8.00, Accept. Off-topic.
- `A3YUPeJTNR.md` — Cost of waiting, avg 8.00, Accept. Off-topic.
- `EUSkm2sVJ6.md` — Data usage inference, avg 7.60, Accept. Off-topic.

Round-1 bracket: between 3.5 and 6, closest to the 4.5 reject anchor (Calibrated Physics-Informed UQ) and the 5.75 accept anchor (Gauss-Newton CP).

Round 2 (narrowing):
- `4vPVBh3fhz.md` — PAC Prediction Sets Under Label Shift, avg 6.40, Accept. More involved methodology (importance-weight CIs) than this paper.
- `j511LaqEeP.md` — Non-Exchangeable Conformal Risk Control, avg 6.00, Accept. Reviewers noted "combines previous work in a relatively straightforward way" — similar character to the present paper but broader scope and more general framework. This paper is narrower.
- `Nfd7z9d6Bb.md` — Probabilistic CP with Approximate Conditional Validity, avg 6.00, Accept. Stronger theory.
- `AKAz88zYLB.md` — CP for Dose-Response with Continuous Treatments, avg 5.80, Reject. Applies weighted CP via propensity scores; reviewers complained about reliance on propensity-quality assumptions and synthetic-only experiments — close in character to this paper.
- `aJ3tiX1Tu4.md` — Wasserstein-Regularized CP, avg 6.67, Accept. More theoretically novel.
- `33XGfHLtZg.md` — Conformal Risk Control, avg 7.00, Accept. More substantive contribution.
- `cho9iE9POr.md` — Low-Budget SBI, avg 5.50, Reject. Less relevant.
- `Q9OGPWt0Rp.md` — PINN parametric solve, avg 5.25, Reject. Different.

**Where the paper lands:** The closest comparators are the rejected 4.50 ("Calibrated Physics-Informed UQ" — CP for neural PDEs, minor extension, limited evaluation) and the rejected 5.80 ("Dose-Response CP with Continuous Treatments" — applies weighted CP with closed-form-ish ratios, methodology novel but evaluation limited and synthetic). The present paper is similar in character to both: a clean but narrow weighted-CP construction with a real but circumscribed contribution, framing that overpromises, and a baseline set that doesn't include the most directly relevant prior work. It is weaker than the 6.00 accept anchor ("Non-Exchangeable Conformal Risk Control"), which has a broader framework and stronger general theorem, and clearly weaker than the 6.40+ accept anchors.

I place this paper just below the rejected 5.80 anchor: the methodology is honest but the scope-mismatch with the motivation, the missing trajectory-level baseline, and the unaddressed undercoverage at $a=-0.005$ are real drags. Calibrated score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>