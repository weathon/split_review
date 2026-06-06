Now I have enough context from the paper to write a thorough consolidated review. Let me synthesize everything.

---

## Summary

The paper introduces a real-time, adaptive framework for designing high-dimensional neural stimulations that perturb low-dimensional latent neural dynamics in desired directions. The system integrates three components: (1) streaming latent space construction (a novel streaming jPCA method, proSVD, and mmICA run in parallel), (2) an adaptive nonparametric kernel regression estimator Ŝ of the stimulus-response mapping conditioned on latent state, stimulus, and time, and (3) a constrained optimization problem that selects stimuli aligned with a target latent direction under non-negativity and sparsity constraints. The system is validated on a toy circular dynamical system, simulated stimulations applied to calcium imaging data, and electrophysiological recordings, with runtimes below 100 ms.

---

## Strengths

- **Stimulus-response mapping learns rapidly and adapts to instabilities on the toy model**: The kernel regression estimator Ŝ converges to low estimation error within ~20 stimulations on the toy circular system (Fig. 2c), and adapts to both a 180° flip and a continuously rotating ground-truth S (Fig. 2d–e), outperforming the blind baseline during and after instability events. The toy model's S (Eq. 9) is genuinely state-dependent (depends on x₁, x₂ position on the manifold), making this a non-trivial learning demonstration.

- **Optimization produces observed improvements over random alternatives**: In Figure 4a, designed stimulations produce observed responses s_obs more aligned with the target direction Q₀ than random single-neuron activations, random multi-neuron activations, or shuffled versions of the designed stimuli. This is the key empirical comparison: it uses *observed* (not predicted) misalignment.

- **Closed-loop outperforms open-loop on nontrivial mapping (Fig. 5b)**: The paper demonstrates that using the adaptive Ŝ estimator in closed-loop achieves a larger proportion of s_obs magnitude aligned with v than the open-loop (identity S(u) = Q^T u) baseline, on the toy model with a genuinely complex S. This directly validates the paper's core argument that modeling the stimulus-response mapping provides value.

- **Real-time feasibility is credibly demonstrated**: End-to-end computation averages <10 ms and is always below 100 ms (Section 3), which is a concrete and verifiable engineering contribution enabling compatibility with in vivo neural data rates.

- **Handling of response delays and nonstationarity is well-motivated and tested**: The delayed response model is empirically validated on calcium imaging data (Fig. 3a–c, delay introduced at 304 s), and the temporal kernel discounting (K₃) is shown to enable recovery from instabilities (Fig. 2e) — a realistic and important design consideration.

---

## Weaknesses

### Fatal
None.

### Major

- **Real-data experiments use only trivially learnable stimulus-response mappings**: The paper simulates stimulations on all real datasets using a simple AR(1) additive model: `y_t = r_t + a_t, a_t = 0.8 · a_{t-1} + u_t` (Section 4.1). The effect of u on the latent state is Q^T a_t ≈ Q^T u (temporally scaled), which is essentially the "open-loop identity mapping" the paper identifies in Section 4.2: "The above experiments assumed that the result of a stimulation u was simply its projection into the latent space S(u) = Q^T u. Because this requires no feedback, or information about the result of the stimulation, we call it open loop mode." The key advantage of the full kernel regression Ŝ — state-dependence, nonstationarity adaptation, genuine nonlinearity — is never exercised on real data. This means the outperformance over the "blind" baseline on real data is expected of any method that knows when stimulations occurred, not evidence for the added value of the nonparametric form. The paper's Discussion only acknowledges that experiments were "performed offline, though in a realistic streaming setting" (Section 5), without noting that the stimulations themselves are trivially modeled.

- **Weak baseline for the kernel regression Ŝ**: The only comparison model throughout Sections 4.1 and 4.2 is a "blind" model that does not receive stimulation timing information. Any method conditioning on stimulation times — including linear regression — would outperform this baseline. The paper does not compare Ŝ to simpler alternatives (OLS, ridge regression on latent state × stimulus, GP regression) that would isolate the contribution of the nonparametric, state-conditioned, time-discounting kernel design. This makes it impossible to evaluate whether the kernel machinery adds value beyond simply including stimulation information.

### Minor

- **Primary optimization metric in Fig. 4b is nearly tautological**: The reported metric of 517/600 feasible-direction optimizations achieving <1° of predicted misalignment (angle between s(u) and v) quantifies how well the optimizer minimizes its own objective (Eq. 8), not whether the designed stimulations will work. The more informative diagnostic — observed misalignment between s_obs and v — is shown only for the Q₀ comparison in Fig. 4a. A unified reporting of both metrics across all conditions would clarify how much the optimization's self-assessed performance diverges from actual outcomes.

- **Parallel latent-space selection is never evaluated in stimulation experiments**: The abstract and introduction claim that parallel evaluation of latent spaces "allows for direct comparison between different latent representations and the opportunity for adaptive selection of stimulations to best distinguish amongst neural subspace hypotheses." However, all stimulation experiments use a fixed proSVD/Q₀ space. The mechanism shown in Fig. 1c is only demonstrated for tracking/prediction quality, not for stimulation design.

- **sjPCA convergence is slower than proSVD** (Fig. 1a), yet the paper does not show that jPCA subspaces produce better stimulation outcomes. If sjPCA's rotational structure does not translate into stimulation benefits, the added complexity over proSVD is unjustified given its slower convergence.

### Trivial
- The paper does not report variance or statistical significance for the closed-loop vs. open-loop comparison in Fig. 5b. Violin plots or standard error bands are shown in other figures, but Fig. 5b only shows solid lines (averaged values).

---

## Nice-to-Haves

- A biologically realistic (but fully synthetic) stimulus-response model — such as a recurrent network where stimulating one unit propagates effects through the network — would bridge the gap between the toy model and real data. This would demonstrate that Ŝ provides meaningful value in conditions more complex than the AR(1) simulated stimulation, without requiring actual optogenetic experiments.

- Even a simple ridge regression of S (linear in latent state and stimulus, with exponential time decay) as an additional baseline would clarify how much the nonparametric kernel structure contributes relative to just conditioning on stimulation information.

- A unified table/figure reporting both predicted and observed misalignment across all experimental conditions (Negative, Dense, Random, Feasible, Q₀) would make it straightforward to assess the gap between optimizer performance and actual outcome.

- Demonstration that the adaptive latent selection (Fig. 1c) can be used to adaptively choose stimulations across representations, even on the toy model, would substantiate the abstract's claim about this feature.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "sjPCA never justified for stimulation experiments."** The critic notes that stimulation results all use proSVD/Q₀. This is true but is already captured as a Minor weakness. The broader claim that sjPCA's existence as a contribution is unjustified is too strong — it is a genuine streaming algorithm and stands independently as a method. Retained as a minor sub-point only.

- **Harsh Critic: "The paper's description of S in the abstract overstates experimental validation."** The critic says the abstract claims evaluation on "real neural data" without disclosing that stimulations are simulated. This is a presentation concern and is already covered by the Major weakness on simulated stimulations. Not retained as a separate criticism.

- **Strength Finder: "mmICA converges quickly."** Fig. 1a shows mmICA converges more slowly than proSVD and sjPCA. This strength is contradicted by the paper's own data. Removed.

- **Strength Finder: "Streaming latent-space construction converges quickly."** Only proSVD converges quickly in Fig. 1a; sjPCA is slower, and mmICA is substantially slower. This generic claim is removed; real-time feasibility is retained for proSVD specifically.

---

## Novel Insights

The most genuinely useful observation to emerge from the review process is that the paper tacitly conflates two validation goals: (1) demonstrating that the kernel regression machinery learns nontrivial stimulus-response maps (tested only on the toy model), and (2) demonstrating that the framework operates correctly in the face of real neural data complexity (tested on real data, but with trivially linear stimulations). These goals require different experimental conditions, and the paper conflates them by applying the real-data experiments as if they validate both. Disentangling these two claims — and providing at least one experiment that satisfies both simultaneously (e.g., a synthetic network embedded in real-data noise, or a more complex stimulation model applied to real data) — would substantially change the strength of evidence. As it stands, the closed-loop advantage over open-loop (Fig. 5b) is the paper's most important result and the one most directly supporting its central claim, but it resides entirely on the toy model.

---

## Suggestions

1. **Add a synthetic network stimulation model**: Replace or supplement the AR(1) stimulation with a model where neurons in a small recurrent network are stimulated, causing downstream activity changes. This produces a nontrivial S where network structure determines the latent-space effect, making the kernel regression's state-dependence actually necessary.

2. **Add a linear regression baseline**: Report performance of a simple ridge regression of S (regressing s_obs on [x_t; u_t] with temporal decay) alongside the kernel regression in Fig. 2c and 3c, to isolate what the nonparametric kernel design adds.

3. **Unify observed vs. predicted metrics**: Create a single figure or table that reports both observed angle (s_obs vs. v) and predicted angle (s(u) vs. v) for all experimental conditions, making the optimizer's calibration transparent across all targets.

4. **Use the adaptive latent selection in at least one stimulation experiment**: Even a simple demonstration that switching between proSVD and sjPCA based on Fig. 1c's heuristic changes stimulation outcomes would validate the abstract's claim about this feature.

---

## Evaluation on Key Axes

- **Originality**: Moderate-to-high. The combination of streaming latent spaces, adaptive nonparametric stimulus-response mapping, and constrained optimization is novel as an integrated system, even if individual components draw on existing tools.
- **Importance of research question**: High. Adaptive control of latent neural dynamics is a pressing challenge for both basic neuroscience and brain-machine interfaces.
- **Whether claims are well supported**: Moderate. Core claims (learning Ŝ, closed-loop advantage, real-time feasibility) are supported, but the support for real-data applicability rests on trivially linear simulated stimulations.
- **Soundness of experiments**: Moderate. Toy model experiments are careful and informative. Real-data experiments demonstrate integration but not the key contribution.
- **Clarity of writing**: Good overall. Algorithm 1 is clear, methods are well-described, though the open/closed-loop distinction in Section 4.2 could be introduced earlier and more prominently.
- **Value to the research community**: Moderate-to-high. The framework addresses a real need, is computationally feasible, and is likely to be useful to the neuroscience/BMI community even in its current form.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>