Now let me run the calibration search to bracket the score.Initial bracket: **4–6**. The paper has genuine engineering contributions but limited empirical validation. Let me read a couple mid-range anchors and then narrow.Now I have enough to write the consolidated review. Let me compile the findings.

---

## Summary

This paper proposes a real-time adaptive framework for designing high-dimensional neural stimulations that perturb latent neural dynamics in specified directions. The system integrates three components: (1) a novel streaming jPCA algorithm (sjPCA) alongside existing proSVD and mmICA for real-time latent space construction, (2) a nonparametric kernel regression estimator $\hat{S}$ that maps stimulations to their effects on latent dynamics and adapts to non-stationarities, and (3) a constrained optimization (Eq. 8) that selects sparse, non-negative stimulation vectors maximally aligned with a target direction in latent space. The method is validated on a toy circular dynamical system and on two real neural datasets (calcium imaging and intracortical electrophysiology) with simulated stimulations injected via an AR(1) additive model.

---

## Strengths

- **Real-time feasibility is genuinely demonstrated**: Section 3 reports end-to-end computation averaging <10 ms per timepoint and always below 100 ms, confirming pipeline compatibility with future in-vivo closed-loop experiments. This is a concrete, verifiable, and non-trivial engineering result.

- **Kernel regression adapts to non-stationary stimulus-response mappings**: On the toy model (Fig. 2c–e), $\hat{S}$ converges to the ground-truth $S$ within ~20 stimulations, and recovers after both a 180° flip and a continuous rotation of the underlying mapping, outperforming the blind baseline. The state-dependent toy model $S_\theta$ (Eq. 9) is genuinely nontrivial—it varies with the current latent position $(x_1, x_2)$—so these results do reflect learning a nonlinear map.

- **Designed stimulations outperform random and shuffled baselines on observed outcomes (Fig. 4a)**: The angle between $s_\text{obs}$ and $v$ is substantially lower for the optimization-designed stimuli than for single random neurons, multi-neuron random groups, or shuffled versions of the designed stimuli. This validates the optimization's practical utility at least under the conditions tested.

- **Response delay modeling is validated**: The framework handles a fixed response delay $d$ (Section 2.3) and the calcium imaging experiments introduce a 0.2 s delay at $t=304\text{s}$ (Fig. 3a), with the method maintaining lower prediction error than the blind baseline before and after the delay switch.

- **Parallel streaming over multiple latent representations**: Running sjPCA, proSVD, and mmICA in parallel and selecting the best-performing space per timepoint (Fig. 1c) is a practically useful capability for hypothesis-driven neuroscience experiments.

---

## Weaknesses

### Fatal
None.

### Major

- **Real-data experiments use only simulated, linear stimulations**: Section 4.1 explicitly states that all stimulations on real data are generated via $a_t = 0.8 \cdot a_{t-1} + u_t$, $y_t = r_t + a_t$—an AR(1) additive model. When projected into the learned latent space, this reduces to essentially a linear, state-independent, stationary map. The paper's central argument for the nonparametric $\hat{S}$ with state conditioning and temporal discounting is that stimulus responses can be nontrivial, state-dependent, and nonstationary. But the one condition where that complexity actually exists—the toy model—is by construction not the real-data condition. The paper never tests whether $\hat{S}$ provides value over a simpler baseline in any condition with real neural circuitry. The Discussion (Section 5) acknowledges offline execution but does not acknowledge that stimulations themselves are simulated with a trivially learnable model.

- **Baseline comparison is too weak to evaluate the kernel regression's contribution**: In every quantitative comparison (Sections 4.1 and 4.2), the only baseline is a "blind" model that receives no information about stimulation times. Any method that conditions on stimulation times—including simple linear regression—would outperform this baseline. The paper does not compare against ridge regression, OLS, or GP regression as a stimulus-response model. As a result, it is impossible to determine whether the specific nonparametric design choices in $\hat{S}$ (RBF kernels over latent state, stimulus, and sample age) provide value over a simpler informed alternative, or whether the improvement is entirely attributable to the tautology of including stimulation timing.

### Minor

- **The primary optimization metric in Fig. 4b is tautological**: The optimization problem (Eq. 8) directly minimizes the angle between $s(u) = \hat{S}(x_t, u, t)$ and $v$. Reporting that 517/600 feasible optimizations achieve <1° of predicted misalignment demonstrates that the optimizer can minimize its own objective, not that delivered stimulations will produce the desired effects. The more informative observed metric (angle between $s_\text{obs}$ and $v$, Fig. 4a) is shown only under simulated AR(1) stimulations where the mapping is trivially learnable. The relationship between predicted and observed error (Fig. 4c) is characterized as a "loose lower bound" without statistical quantification of when it fails.

- **sjPCA convergence is slower than proSVD and its advantage for stimulation design is undemonstrated**: Figure 1a shows sjPCA converging more slowly to the correct rotation plane than proSVD converges to the PCA subspace. The stimulation results in Section 4.2 use proSVD/$Q_0$. The paper does not show that sjPCA subspaces yield better stimulation outcomes than proSVD subspaces, which would justify the additional complexity of the Sherman-Morrison + Procrustes pipeline.

- **The parallel latent-space selection feature is never evaluated in the stimulation context**: The abstract promises "the opportunity for adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses" as a contribution, but all stimulation experiments use a single fixed latent space (proSVD). No demonstration—even on the toy model—shows stimulation design adapting across latent hypotheses.

### Trivial

- The claim in Section 5 that "our real data experiments were performed offline, though in a realistic streaming setting" understates the actual gap: it is not just that experiments are offline but that the stimulations themselves are synthetic and do not reflect real neural circuit dynamics.

---

## Nice-to-Haves

- A biologically realistic (though fully synthetic) stimulus-response model—e.g., a recurrent linear network or coupled leaky integrate-and-fire system where stimulating a subset of neurons propagates through the network and produces state-dependent, nonlinear effects—would let the authors demonstrate nontrivial $\hat{S}$ learning and closed-loop gains without requiring actual optogenetic hardware.

- A ridge regression baseline for $\hat{S}$ (linear in $x$ and $u$, with exponential forgetting) would clarify how much of the improvement over the blind model is attributable to the kernel structure versus simply conditioning on stimulation timing.

- A unified table or figure reporting both predicted and observed alignment across all experimental conditions (toy model, calcium, electrophysiology; open loop, closed loop) would substantially improve interpretability.

- A demonstration of the adaptive latent-space selection (Fig. 1c) influencing stimulation design—even on the toy model—would substantiate the parallel-evaluation contribution claimed in the abstract.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"sjPCA contribution is merely incremental"**: The reviewer frames the Sherman-Morrison solve and Procrustes alignment as "standard tools," implying the contribution is trivial. The combination into a streaming jPCA estimator is novel in application, and the convergence comparison in Fig. 1a provides honest quantitative evidence. Removed as overclaiming incremental-ness; demoted to minor.

- **"Assumption that stimulations are 'somewhat sparse' is unquantified"**: The reviewer asks how sparse is sufficient. This is a parameter sensitivity concern that applies to all regression models trained on non-overlapping subsets; it is not a structural flaw in the method. Removed as a speculative gap.

- **"Variance/statistical tests for optimization results absent"**: Violin plots and counts (e.g., 517/600 optimizations) are reported. The request for formal hypothesis tests across restart conditions is standard-practice critique, not a methodological flaw. Moved to nice-to-have.

- **Strength: "The strongest piece of evidence is closed-loop with nontrivial mapping (Fig. 5b)"**: The strength finder characterizes Fig. 5b as the strongest evidence. On inspection, Fig. 5b shows magnitude aligned with $v$ (not angle) in the toy model—the comparison is between open-loop (trivial mapping) and closed-loop (nontrivial mapping). This does show the kernel regression enabling a genuine gain, but it is on the toy model, not real data. Retained as a supporting strength but not elevated to core.

---

## Novel Insights

The most important insight from this review—not made explicit in the paper—is that the feasibility of the overall framework rests on a largely untested premise: that the AR(1) additive stimulation model used for real-data validation is representative of the complexity that $\hat{S}$ is designed to handle. If the latent effect of real optogenetic stimulation is approximately linear and stationary (as the validation assumes), much of the method's sophistication is unnecessary. If it is genuinely nonlinear and state-dependent (as the motivation argues), the method has never been tested in that regime. Closing this gap—either with a biologically realistic synthetic network or by running the pipeline on actual optogenetically stimulated data—would substantially clarify the paper's contribution. The streaming jPCA derivation and the parallel latent evaluation heatmap are the two components that feel most genuinely novel; the rest of the system is a principled but not uniquely surprising engineering integration.

---

## Suggestions

1. Introduce a recurrent network synthetic ground truth (e.g., a 100-neuron ring attractor or linear network with off-diagonal coupling) where stimulating 10 neurons causes a genuinely state-dependent, propagated response; validate $\hat{S}$ convergence and stimulation design quality against this.
2. Add a ridge-regression baseline for $\hat{S}$ (linear in concatenated $[x; u]$ with exponential forgetting) in all figures that currently compare against the blind model.
3. Separate the optimization evaluation into two clearly labeled sub-figures: (a) the optimizer's self-assessed predicted error (Fig. 4b), and (b) the actually observed latent response error (Fig. 4a), and include both for every condition.
4. Either demonstrate adaptive latent-space selection affecting stimulation choice in at least one experiment, or remove it from the abstract's list of contributions.
5. In Section 5, add an explicit sentence: "Furthermore, the stimulations applied to real data were simulated via an AR(1) model and do not reflect actual circuit-mediated responses; future work should test $\hat{S}$ under real delivered stimulations."

---

## Score and Decision

**Round 1 bracket: 4–6**

*Anchors retrieved (Round 1):*
- `/BBldjKEBlJ.md` (QuantFormer, avg 3.0) — significantly weaker; narrow contribution and poor methodology
- `/NPzuN3Rxi8.md` (TAVRNN, avg 3.0) — weaker; limited scientific contribution
- `/LNp7KW33Cg.md` (Stabilized Neural Dynamics/HDA, avg 5.0) — comparable in topic; paper under review has more novel components but weaker empirical grounding
- `/FwW3jqchtY.md` (iSSM, avg 5.0) — close comp; iSSM uses real stimulations, has identifiability theory; paper under review has real-time engineering advantage but weaker validation
- `/eR1119aUlL.md` (MRINE real-time multiscale, avg 4.25) — comparable; paper under review has more novel system design but similar validation gaps
- `/wCUw8t63vH.md` (Spectral learning of shared dynamics, avg 6.8) — stronger; rigorous analytical methods with stronger theory
- `/cNmu0hZ4CL.md` (Optimal transport for neural dynamics, avg 8.0) — clearly stronger; novel metric with strong theory and evaluation
- `/cmfyMV45XO.md` (Feedback neural ODEs, avg 8.0) — different domain; clearly stronger
- `/RWJX5F5I9g.md` (Brain Bandit, avg 8.0) — different topic

**Round 2 narrowing (4.5–6.0):**
- `/4ltiMYgJo9.md` (Closed-loop EEG visual stimulation, avg 5.75) — delivers real stimuli in a real closed-loop with human EEG; paper under review has more sophisticated latent-space machinery but doesn't close the loop in practice; **paper under review is weaker**
- `/4AlNpszv66.md` (FCCA controllable subspaces, avg 4.75) — novel dimensionality reduction with theory and real data; scores low due to reviewer disagreement; paper under review is comparable in novelty and validation quality
- `/TVnkjz4MqV.md` (Neural Manifold Regularization, avg 5.5) — evaluated on real data with real behavioral outcomes; paper under review has more ambitious claims but comparable evidence level
- `/PdZkfSttGK.md` (Nonparametric covariance regression, avg 5.25) — comparable technical sophistication, real data

Compared to these round-2 anchors: the paper under review is roughly comparable to the 4.75–5.25 range. It has real engineering originality (sjPCA, the joint kernel regression + constrained optimization pipeline, real-time feasibility) but the evaluation gap—that no condition with a genuinely nontrivial, real-circuit stimulus-response mapping is tested—prevents a higher placement. The weak baselines compound this. The paper lands slightly below iSSM (5.0) because iSSM at least validates against real delivered stimulations. Score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>