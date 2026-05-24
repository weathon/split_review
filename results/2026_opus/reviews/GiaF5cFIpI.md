Based on my analysis, I have a clear picture. Let me verify the critical Eq. (8) issue one more time.## Summary
The paper proposes a real-time, modular pipeline for adaptive stimulation of latent neural dynamics, comprising (i) a novel streaming jPCA variant (sjPCA) plus parallel evaluation of proSVD/mmICA latent spaces, (ii) a nonparametric kernel-regression stimulus-response model that can track non-stationarities via a temporal kernel, and (iii) an optimization framework that designs high-dimensional stimuli to drive low-dimensional latents in a desired direction under non-negativity and sparsity-like constraints. Evaluation spans a toy circular LDS, calcium imaging from mouse visual cortex, and primate sensorimotor electrophysiology, all benchmarked at <100 ms end-to-end.

## Strengths
- **Real-time end-to-end runtime is concretely demonstrated.** Section 3 reports averaged latencies under 10 ms and a 100 ms ceiling on a single workstation (i9 + 3060 Ti), which is the appropriate hardware baseline for the targeted in-vivo regime.
- **Streaming sjPCA converges to its offline counterpart.** Figure 1a shows the sum of absolute principal angles to the true rotation plane dropping to the offline reference within ~10 s, at a rate comparable to proSVD; the Procrustes step per discovered plane is a sensible stabilizer for streaming jPCA.
- **Adaptive nonparametric stimulus-response model recovers from non-stationarities.** In the toy benchmark (Fig. 2e), after a 180° flip at t=25 s, one-step-ahead prediction error returns to pre-perturbation levels within ~15 s, while a stimulation-blind comparator stays elevated — concretely demonstrating that the temporal kernel $K_3$ in Eq. (7) actually buys what it claims.
- **Real-time differentiable optimization over high-dimensional stimuli.** Eq. (8) attempts to enforce non-negativity, box constraints, and a feasibility cap simultaneously, and the differentiability of the kernel regression $\hat S$ enables gradient-based search over the full $\mathbb{R}^N$ stimulus space rather than a small predetermined dictionary.
- **Two real neural modalities (calcium and electrophysiology).** Demonstrating the pipeline on Zong et al. calcium traces and O'Doherty motor-cortex spikes (Fig. 3) shows the streaming pieces handle different data rates and noise regimes.

## Weaknesses

### Fatal
None. The candidate "fatal" items (the synthetic-stimulation gap and the Eq. (8) sign issue) are serious but do not invalidate the framework as a streaming/optimization contribution; they are demoted to Major below.

### Major
- **The "real-data" experiments do not test the failure modes the model is designed to handle.** §4.1 ("Real data") explicitly defines the stimulus injected into the calcium and electrophysiology recordings as $y_t = r_t + a_t,\ a_t = 0.8 a_{t-1} + u_t$ — a linear additive AR(1) signal applied to pre-selected neurons. Under this construction, the true stimulus-response map is linear and additive, exactly the case §2.3 disclaims when it argues for the kernel model ("responses to stimulations are not robust nor faithful... a neuron may lack sufficient opsin... point-spread function is non-optimal..."). The headline biological failure modes — state dependence, off-target activation, plasticity — only appear in the toy model. §5 acknowledges the offline-vs-streaming caveat but does not flag that the stimulations themselves are synthetic linear additions. The contribution is therefore demonstrated on a much narrower regime than the motivation implies.
- **Equation (8) as written appears to reward density, not sparsity.** With $u\in[0,1]^N$ and $\|u\|_0^{\max}$ a fixed scalar cap, the penalty $\lambda_1(\|u\|_0^{\max}-\|u\|_1)$ is decreasing in $\|u\|_1$, so minimizing $\mathcal L$ pushes $\|u\|_1$ upward — the opposite of the prose at line 206 ("encourage a solution with the number of non-zero elements close to $n$") and the opposite of the sparse stimuli implied by Fig. 4b's Feasible case. This is almost certainly a transcription error (e.g., should be $\max(0,\|u\|_1-\|u\|_0^{\max})$ or an absolute value), but as written it undermines the central feasibility claim of §2.4 and the paper does not reconcile the equation with the reported behavior.
- **The strongest "Feasible" and "$Q_0$" results are partially tautological.** In Fig. 4b the >85% sub-1° optimization-error trials are obtained in the open-loop regime where the paper assumes $s(u)=Q^\top u$ (§4.2) and the target $v$ is constructed to lie in the column space of $Q^\top$ and to be reachable by <30 neurons. This is a useful sanity check on the optimizer but not direct evidence that the method designs useful stimuli when the forward map is unknown. The Random case in the same figure is the more informative comparison and shows a much wider error distribution, which the text does not emphasize.
- **No quantitative comparison against the cited prior stimulation-design literature.** The Introduction names Yang et al. 2021 (I/O dynamical), Minai et al. 2024 (Bayesian optimization), Wagenmaker et al. 2024 (active learning), and Draelos & Pearson 2020 (variational adaptive stimulation). The only quantitative baselines in §4 are random-single-neuron, random-multi-neuron, shuffled-self, and a Blind dynamical model — all weaker than the cited prior art. A reader cannot tell whether the proposed method advances over existing adaptive-stimulation work or merely beats random selection.

### Minor
- **The adaptive latent-space selection is described but never operationalized.** §2.2 / Fig. 1c introduce parallel evaluation of sjPCA/proSVD/mmICA and a per-timepoint selection of the most predictive subspace, and the abstract bills this as enabling "adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses." But no experiment in §4 uses this selection to change a stimulus or distinguish a hypothesis; it remains a visualization. The abstract slightly overclaims relative to what is shown.
- **Cosine-only objective ignores response magnitude.** The objective in Eq. (8) and the evaluation metrics in §4.2 are angle-based; Fig. 5b mentions magnitude but does not benchmark it. A stimulation producing a vanishingly small but well-aligned response is scored identically to one producing a large, well-aligned response — relevant for any downstream use that cares about effect size.
- **Kernel scaling in $u\in\mathbb{R}^N$ is not characterized.** Eq. (7) uses a product RBF kernel on $(x,u,t)$ with $N$ up to ~600 (calcium dataset). The paper claims a useful map within "roughly 10–20 stimulations" but does not show how this scales with $N$ or how the optional bandwidth tuning behaves in the high-dimensional regime. This is a real concern for the "10–20 stimulations" claim, though arguably out of scope for the current presentation.
- **Fig. 4c "lower bound" interpretation is loose.** "Predicted error functions as a loose lower bound on the observed error" (Fig. 4c) is partly an artifact: a model that predicts maximum error on infeasible targets trivially satisfies the inequality, and the negative-target case (~half of trials with observed < predicted) is consistent with that. The paper notes this but does not resolve it.

### Trivial
- None retained after filtering parser-related artifacts.

## Nice-to-Haves
- A stimulation simulator that injects at least one of the named failure modes (state-dependent gain, off-target leakage, opsin variability) and shows $\hat S$ tracks it on real recordings.
- One head-to-head comparison with a cited adaptive-stimulation baseline (Wagenmaker et al. 2024 is the most natural anchor) on either the toy LDS or one of the real datasets.
- A small experiment where the parallel sjPCA/proSVD/mmICA selection actually changes the chosen stimulus and that stimulus measurably outperforms a single-representation choice — converting §2.2 from visualization to capability.
- An additional row in Fig. 4b that draws random $v$ uniformly on the sphere without the <30-neuron feasibility construction, to deconfound "optimization works" from "target was constructible."
- Reporting effect magnitude alongside angle for all stimulation-optimization results.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **(Removed) Strawman framing of sjPCA novelty.** The harsh critic argues sjPCA "overstates novelty as a direct combination of proSVD + Sherman–Morrison + Procrustes." sjPCA is presented as a streaming variant, not a fundamentally new estimator; the convergence check (Fig. 1a) is what the contribution requires. This is editorial taste rather than a flaw.
- **(Removed) Strawman framing of the "Blind" comparator in Fig. 2e.** The criticism that a parametric drift-adaptive baseline (online ridge with forgetting) would also recover is speculative. The figure's claim is bounded to "modeling the stimulus beats ignoring it," which is what is shown. Nice-to-have, not a flaw.
- **(Removed strength) "Demonstration on two diverse real neural recording modalities" reads as a strength but the diversity is undercut by the synthetic-stimulation construction; merged into the Major weakness above so the disagreement resolves in favor of the weakness.
- **(Removed strength) "Validation that predicted error acts as lower bound" — this is concretely quantified but, per the Minor point on Fig. 4c, partly artifactual; downgraded rather than listed as a clean strength.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the gap between the kernel-regression model's stated capabilities (handling state-dependence, off-target activation, plasticity) and the linear-additive stimulation actually injected into real recordings — but this is a critique of the evaluation, not a new scientific insight.

## Suggestions
- Restate Eq. (8) to match the implementation: either $\lambda_1\max(0,\|u\|_1-\|u\|_0^{\max})$ as a hinge on the L1 budget, or $\lambda_1\,|\|u\|_1-\|u\|_0^{\max}|$ as a soft target, and report what was actually optimized in the experiments.
- Add a non-linear/state-dependent stimulation simulator on top of the real recordings (e.g., apply a saturating nonlinearity, a state-dependent gain on $a_t$, or a leakage matrix) and show that $\hat S$ outperforms the linear-additive baseline; this is the experiment that turns §2.3 from claim into demonstration.
- Add at least one prior adaptive-stimulation method as a quantitative baseline on the toy system; even Wagenmaker-style active learning over a discrete candidate set would let readers locate the contribution.
- Include a random-direction-uniform-on-sphere case in Fig. 4b without the feasibility construction, and sweep the sparsity cap, so the optimizer's success is decoupled from target constructibility.
- Operationalize the parallel-representation selection: a small case where the chosen subspace switches mid-experiment and the resulting stimulus is measurably better than the single-representation alternative.
- Add a magnitude metric (e.g., projected length of $s_{\text{obs}}$ onto $v$) alongside angles throughout §4.2.

## Evaluation against the Axes
- **Originality:** Moderate. sjPCA is a useful streaming variant; the integrated streaming-latent + kernel-response + differentiable-optimization pipeline is a real engineering contribution; the individual ingredients (proSVD, mmICA, KF/VJF/Bubblewrap, kernel regression, Sherman–Morrison) are existing tools combined sensibly.
- **Importance of research question:** High. Adaptive, latent-aware stimulation of neural dynamics is an open and clinically relevant problem.
- **Whether claims are well supported:** Partial. Streaming convergence (Fig. 1a) and non-stationarity recovery on the toy model (Fig. 2e) are well supported. The headline claim that the method enables stimulation experiments under realistic biological response conditions is not directly tested because every "real-data" experiment injects a synthetic linear additive stimulus.
- **Soundness of experiments:** Mixed. The optimization claim is partially tautological in its strongest cases (Feasible, $Q_0$) and the regularizer in Eq. (8) as written conflicts with the stated sparsity behavior. The "Random" direction case is the most informative and shows a wide error distribution.
- **Clarity of writing:** Generally clear; Algorithm 1 and Figures 1–5 read well.
- **Value to the research community:** Moderate as a system/engineering contribution; would be substantially higher with one realistic-stimulation experiment and one prior-art baseline.

## Score and Decision

**Anchors retrieved across rounds:**
- Round 1 (bracketing):
  - `xFvHcgj1fO.md` (avg 3.00, weak band) — online ML for anomaly detection; far less ambitious than this paper.
  - `NRRHkJE03w.md` (avg 3.00, weak band) — conservation principles discovery; not topically similar.
  - `fnO5h1CFyh.md` (avg 3.00, weak band) — Hebbian temporal memory; not similar.
  - `6Z8rZlKpNT.md` (avg 3.40, weak band) — normalizing flows OOD; not similar.
  - `4ltiMYgJo9.md` (avg 5.75, mid band) **[read]** — closed-loop EEG visual stimulus framework; same closed-loop spirit but different domain (image stimuli) and reviewers split 6/8/6/3. Comparable engineering ambition.
  - `FwW3jqchtY.md` (avg 5.00, mid band) **[read]** — interventional state-space models for neural dynamics; most directly comparable: same target problem of modeling neural responses to perturbations, with real perturbation data and an identifiability proof. Rejected.
  - `TVnkjz4MqV.md` (avg 5.50, mid band) — neural manifold regularization; mid-band tier.
  - `N83O2FcqzN.md` (avg 5.00, mid band) — time-dependent VAE on visual neural activity.
  - `kbjJ9ZOakb.md` (avg 8.00, strong band) — invariance manifolds in V1; markedly stronger.
  - `cmfyMV45XO.md` (avg 8.00, strong band) — feedback for neural ODEs; markedly stronger.
  - `Xo0Q1N7CGk.md` (avg 8.00, strong band) — conformal isometry hypothesis grid cells; markedly stronger.
  - `GRMfXcAAFh.md` (avg 8.00, strong band) — Oscillatory SSMs; markedly stronger.

- Round 1 bracket: **[4.5, 6.0]** — the paper is clearly above the avg-3 cluster and clearly below the avg-8 cluster, with the closest topical anchors at 5.00 (iSSM) and 5.75 (EEG closed-loop).

- Round 2 (narrowing within bracket):
  - `BYUdBlaNqk.md` (avg 5.25) — system identification of neural systems via video models.
  - `4AlNpszv66.md` (avg 4.75) **[read]** — Feedback Controllability Components Analysis; novel theory, modest empirical; mixed reviews (8/5/3/3); rejected.
  - `mV6cO4mGjH.md` (avg 4.50) — dynamics-based neural encoding with connectivity.
  - `pXPIQsV1St.md` (avg 5.25) — dynamical similarity analysis.
  - `ZwhHSOHMTM.md` (avg 6.67, accept) — dynamic functional connectome.
  - `WQwV7Y8qwa.md` (avg 5.80, accept) — switching nonlinear dynamical systems across brain regions.
  - `YIls9HEa52.md` (avg 6.60, accept) — infinite recurrent switching LDS.
  - `MREQ0k6qvD.md` (avg 6.33, accept) — one-hot GLM for switching brain state.
  - `HiTg16qhxp.md` (avg 5.50, accept) — dynamic neural response tuning.

**Comparison:** The paper is closest to `FwW3jqchtY` (iSSM, 5.00) and `4AlNpszv66` (FCCA, 4.75), both rejected, both with real methodological contributions but with empirical or theoretical gaps. Relative to iSSM, this paper has more engineering depth (real-time streaming pipeline, multiple latent spaces, multiple dynamical models) and broader scope, but a comparable or weaker empirical validation (iSSM used genuine perturbation datasets; this paper injects synthetic linear stimuli). Relative to FCCA, this paper has stronger empirical demonstrations but lacks FCCA's theoretical contribution. The accept-side anchors at 5.5–6.6 (`HiTg16qhxp`, `WQwV7Y8qwa`, `MREQ0k6qvD`) tend to have cleaner empirical claims or theoretical contributions that this paper does not match given the Eq. (8) inconsistency and synthetic-stimulation gap. Final placement: around iSSM, very slightly below to reflect the additional Eq. (8) concern and the un-operationalized adaptive-selection claim.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>