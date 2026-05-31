## Summary

This paper presents a real-time adaptive framework for designing neural stimulations that perturb latent neural dynamics along desired directions. The method integrates three components: (1) streaming latent space construction including a novel streaming jPCA algorithm (sjPCA), (2) adaptive kernel regression for stimulus-response modeling with temporal decay to handle non-stationarities, and (3) a constrained optimization problem that selects high-dimensional stimulation patterns to drive low-dimensional neural dynamics in a target direction. The system is evaluated on a simulated circular LDS, a calcium imaging dataset (mouse visual cortex), and an intracortical electrophysiology dataset (nonhuman primate), with all stimulations synthetically applied to real recordings. End-to-end runtimes are reported below 10 ms on average.

---

## Strengths

- **Novel sjPCA streaming algorithm with theoretical motivation.** The streaming formulation of jPCA using the Sherman-Morrison formula for online updates combined with a per-plane Orthogonal Procrustes stabilization step (Eq. 2) is a technically sound and genuinely new contribution. The convergence to offline solutions is empirically validated (Fig. 1a), and the method fills a practical gap since jPCA is widely used in systems neuroscience.

- **Well-motivated kernel regression formulation for adaptive stimulus-response modeling.** Equation (7) elegantly captures state-dependence, stimulus identity, and temporal non-stationarity in a single nonparametric estimator. The demonstration that the model recovers within ~15 s after a 180° jump discontinuity and continuously tracks rotating maps (Fig. 2d–e) is convincing and directly relevant to real experimental instabilities such as probe shifts or photobleaching.

- **Constrained optimization framework matching realistic experimental conditions.** The optimization problem (Eq. 8) explicitly imposes non-negativity (excitation-only opsins), a sparsity-promoting penalty, and a box constraint, which matches practical limitations of holographic optogenetics. The ablations across feasible vs. infeasible target directions (Fig. 4b) illustrate that the framework correctly identifies what is and is not achievable, with 508–517/600 optimizations achieving <1° misalignment for feasible targets.

- **Multi-representation, multi-model parallel evaluation with adaptive switching.** Running proSVD, sjPCA, and mmICA in parallel and using predictive probability heatmaps (Fig. 1c) to adaptively select the best representation at each location is a practically useful feature not found in prior streaming neural pipeline work. This could be especially valuable for experiments with complex multi-regime dynamics.

- **Real-time feasibility rigorously benchmarked.** Reporting sub-10 ms average end-to-end latency and sub-100 ms worst-case on commodity hardware provides strong evidence of practical deployability, which is a prerequisite for the envisioned in vivo applications.

---

## Weaknesses

### Fatal
None. The core claims are internally consistent and supported by the presented experiments.

### Major

1. **All real-data experiments use synthetically simulated stimulations.** The paper explicitly states: "For each of the real datasets, we simulated stimulations using an autoregressive function." The AR stimulation model ($y_t = r_t + a_t$, $a_t = 0.8 a_{t-1} + u_t$) is deterministic and linear, which may dramatically underestimate the complexity and variability of actual optogenetic responses (network-mediated effects, opsins variability, out-of-focus excitation). The paper's central claim is a method for adaptive closed-loop stimulation of latent dynamics, yet the only closed-loop validation is simulation-within-simulation. While acknowledged in Section 5, this gap is substantial for a venue that expects empirical claims to be backed by appropriately realistic experiments.

2. **No quantitative comparison against competing algorithmic approaches.** The paper mentions Bayesian optimization (Minai et al., 2024) and active learning approaches (Wagenmaker et al., 2024) as related work for stimulus design, but neither appears in any experiment. The baselines used—randomly stimulating single neurons, random groups, and shuffled versions of the designed stimuli—are weak. A comparison with a BO-based approach (even in the toy or simulated setting) would substantively strengthen the claim that the proposed kernel-regression + gradient-optimization pipeline is preferable. Similarly, the "blind" dynamical model is a natural baseline for the prediction error task, but not a state-of-the-art one.

3. **Optimization objective (Eq. 8) lacks clarity and analysis.** The term $\|u\|_0^{\max}$ is not defined in the main text, leaving the L0-L1 penalty $\lambda_1(\|u\|_0^{\max} - \|u\|_1)$ ambiguous. Using a difference between the L0 pseudo-norm upper bound and L1 norm as a sparsity surrogate is non-standard, and no analysis is given for whether this relaxation reliably recovers sparse solutions or what the effect of $\lambda_1$ is on the solution quality. The sensitivity of stimulation quality to this hyperparameter is not ablated.

### Minor

1. **Streaming model selection component is underspecified in the main text.** The mechanism for adaptively switching between latent spaces (Section 2.2, Fig. 1c) is described in one paragraph without a formal algorithm, update equations, or complexity analysis. It is unclear how predictions from incompatible latent spaces (proSVD vs. mmICA) are placed on the same scale for comparison.

2. **Scalability analysis is absent.** Experiments involve 592 neurons (calcium imaging) and 130 units (electrophysiology). The kernel regression in Eq. (7) has $O(N_{obs})$ cost per query where $N_{obs}$ is the number of observed stimulations. For long experiments or large populations, this could become a bottleneck. The paper does not discuss how performance or runtime degrades as the number of observations or neurons grows.

3. **No statistical tests on experimental comparisons.** Figures 4 and 5 rely on violin plots and smoothed averages to establish differences between methods. Without significance tests, it is unclear whether differences observed (e.g., between Designed and Shuffled stimulations in Fig. 4a) are robust or depend on initialization choices.

### Trivial
None.

---

## Nice-to-Haves

- Including at least one experiment comparing the proposed optimization strategy against Bayesian optimization on the toy or simulated real-data setting, even with a small number of stimulations, would substantially strengthen the stimulation design claims.
- A sensitivity analysis on the kernel bandwidth tuning (the stochastic coordinate descent procedure) and its impact on stimulus-response learning speed would help practitioners deploy the method.
- Scaling experiments (runtime vs. number of neurons, number of observed stimulations) would clarify applicability to modern large-scale recording settings.

---

## Novel Insights

The most genuinely novel insight is the streaming jPCA formulation (sjPCA): by reformulating the skew-symmetric linear system identification step via Sherman-Morrison and stabilizing per-rotation-plane subspaces via Orthogonal Procrustes, the paper enables a representation specifically suited for rotational neural dynamics to be computed in real time. This is non-trivial because jPCA involves eigendecomposition of a dynamically updated matrix, and naïve streaming of this is unstable. The second notable insight is that a nonparametric kernel regression with a temporal forgetting kernel handles both stable and non-trivially time-varying stimulus-response mappings at similar convergence rates, precisely because it makes minimal structural assumptions—this "easy because assumption-free" property is practically important and empirically supported. The parallel multi-representation selection framework offers a principled way to detect regime changes in neural state, which could be broadly applicable beyond the stimulation design use case.

---

## Suggestions

- Validate at least one key component (stimulus-response learning or optimization quality) against a competitive baseline (e.g., Gaussian process / BO-based stimulus selection) to establish the method's position in the landscape more convincingly.
- Provide a complete algorithmic description (pseudocode or equation-level) for the adaptive latent space selection procedure, analogous to Algorithm 1 for the full pipeline.
- Define $\|u\|_0^{\max}$ explicitly and provide either a theoretical guarantee or an ablation study showing that the L1 penalty reliably promotes the desired level of sparsity across the experimental conditions.
- Test robustness under a more realistic (e.g., Poisson-sampled, network-mediated) stimulation response model in the toy setting to bridge the gap to actual in vivo conditions.

---

## Score and Decision

The paper presents a technically sound, well-motivated framework that integrates several novel components (sjPCA, adaptive kernel regression with temporal decay, constrained optimization for latent-space stimulation). The problem is important and practically relevant for neuroscience and brain-machine interfaces. However, for ICLR, the paper has two significant gaps: the entire real-data validation relies on synthetically applied stimulations rather than actual closed-loop experiments, and there are no comparisons with algorithmically competitive alternatives (BO, active learning) that are explicitly cited as related work. The optimization formulation also has a non-standard, underanalyzed component. Taken together, the paper is interesting and methodologically meaningful but not yet at the standard of experimental rigor expected for acceptance at a top ML venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>