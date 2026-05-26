Now I have sufficient context. Let me write the final consolidated review.

## Final Review

## Summary
This paper proposes a streaming framework for adaptive stimulation of latent neural dynamics. It combines streaming dimensionality reduction (including a novel sjPCA algorithm), dynamical state-space modeling, nonparametric kernel regression for stimulus-response mapping, and constrained optimization to design high-dimensional stimulation patterns that drive low-dimensional latent activity along desired directions. The method is demonstrated on a toy model, two real neural datasets with synthetically injected stimulation effects, and benchmarked for real-time computational feasibility.

## Strengths

1. **sjPCA converges to offline jPCA subspace in real time.** Figure 1a shows sjPCA error rapidly converging to the offline reference across 10 runs, supporting the claim that real-time latent space construction can match a standard batch method.

2. **Adaptive kernel-regression model recovers from non-stationary stimulus-response mappings.** Figure 2e demonstrates that after a 180° flip (t=25 s) and a continuous rotation (t=45 s), the 1-step-ahead prediction error recovers within ~15 s, while a stimulation-blind baseline does not. This is direct evidence that the temporal kernel discounting mechanism works as intended.

3. **Designed stimuli achieve high alignment with target latent directions.** Figure 4a shows that optimized stimuli (median angle <10°) substantially outperform random single-neuron, random-group, and shuffled stimuli (all >80°), demonstrating that the overall pipeline can effectively drive latent dynamics along specified vectors.

4. **End-to-end computation stays below 100 ms worst-case, ~10 ms average** (Section 3), supporting the real-time feasibility claim.

5. **Predicted error from the optimization provides a conservative lower bound on observed error** (Figure 4c: <6% of non-Negative optimizations have observed error below predicted error, Section 4.2), a useful property for safe experimentation.

## Weaknesses

### Major

1. **The sparsity constraint in the optimization (Equation 8) is formulated incorrectly.** The penalty term λ₁(‖u‖₀^max − ‖u‖₁) with a positive weight λ₁ minimizes making ‖u‖₁ as large as possible (dense), which is the *opposite* of sparsity. The paper states the intention is to "encourage a solution with the number of non-zero elements close to n," but the term as written incentivizes all entries toward 1. This is either a sign error (should be +λ₁‖u‖₁ or λ₁|‖u‖₁ − n|) or a mis-specified objective. Since limiting the number of simultaneously targeted neurons is a stated core constraint (Discussion: "limit on the number of total targets in a single stimulation"), this error undermines a key claimed capability. The paper also does not verify the actual L0 count of optimized solutions, so it is unclear whether the empirical results respect the experimental feasibility constraints the framework claims to enforce.

2. **The "real data" experiments use only synthetic stimulation responses, not actual neural responses to stimulation.** Section 4.1 states: "For each of the real datasets, we simulated stimulations using an autoregressive function… a_t = 0.8·a_{t-1} + u_t." This is a trivial linear injection — the ground-truth stimulus-response map is known, linear, and additive. Real optogenetic or electrical stimulation involves nonlinear, state-dependent, and off-target effects that this model does not approximate. The paper therefore provides no evidence that the method can learn a realistic, unknown stimulus-response mapping from real data. The abstract claims "demonstrate our approach on both simulated and real neural data," which is technically true but potentially misleading because the *stimulation effects* are entirely synthetic. The paper acknowledges this only in passing (Discussion: "real data experiments were performed offline") without noting this as the central limitation of the empirical evidence.

3. **Comparisons are against trivial baselines only; no existing stimulation design method is used for comparison.** The paper compares against: (i) a "blind" model that ignores stimulation, (ii) random single-neuron stimulation, (iii) random group stimulation, and (iv) shuffled designed stimuli. While these show that the optimized stimuli are better than random, they do not demonstrate an advantage over existing approaches that the paper itself cites — Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), input-output dynamical modeling (Yang et al., 2021). Even a simple heuristic like selecting neurons with the largest loadings on the desired latent direction would be a more informative baseline. Without such comparisons, it is impossible to assess whether the proposed method offers practical advantages over the state of the art.

### Minor

1. **No ablation study isolating key components.** The pipeline combines streaming latent spaces, three dynamical models, kernel regression with temporal discounting, and constrained optimization. It is unclear which components drive the observed performance. For instance: (i) how much does the learned Ŝ improve over assuming an identity stimulus-response mapping (open-loop)? (ii) does sjPCA meaningfully outperform running offline jPCA on a sliding window? (iii) does the parallel multi-space selection mechanism actually improve predictions compared to any single space? Ablations addressing these questions would substantially strengthen the paper.

2. **Several components are underspecified.** The online tuning of kernel length scales via "stochastic coordinate descent at each new observation" is mentioned without algorithmic details or safeguards against instability. The optimization solver for the non-convex objective in Equation (8) is not specified (gradient descent? L-BFGS? proximal method?), nor is the initialization strategy for u. The delayed-response model introduces coefficients β without specifying how many are used or how they are fit.

3. **No statistical tests for key comparisons.** Figure 4 presents violin plots comparing alignment angles across methods, but no confidence intervals, p-values, or effect sizes are reported. The statements about "significantly lower error" are unsupported by statistical testing.

4. **The Kalman filter is used for all main experiments without justification** or comparison against the other two dynamics models (VJF, Bubblewrap). The paper mentions these alternatives but does not evaluate whether using them changes the results.

### Trivial

- Figure 5's description is unclear ("Closed non-trivial" definition, trial number axis). The proportion of aligned magnitude comparison in Figure 5b is based on only 10 experiments without error bars on the individual conditions.

## Nice-to-Haves

- Comparison against at least one existing method (e.g., Bayesian optimization for stimulus selection, or a greedy heuristic selecting neurons by loading magnitude) to contextualize the contribution.
- Verification of the actual L0 count (number of non-zero entries) in optimized stimulus vectors to confirm that sparsity constraints are satisfied.
- A more realistic generative model for stimulation effects on real data (nonlinear, state-dependent) to test the method under conditions that better approximate actual optogenetic or electrical stimulation.
- Ablation studies isolating the sjPCA streaming method, the adaptive kernel regression, and the closed-loop Ŝ from open-loop identity mapping.

## Removed Points

**Removed weaknesses from the harsh critic that do not survive verification:**

- *"The description of sjPCA is too brief to be reproducible"* — The paper provides the Sherman-Morrison solution sketch and Orthogonal Procrustes stabilization; code is promised in the supplementary material. Adequate for a methods paper at this length.
- *"No justification of Kalman filter choice"* — The paper states that all three models are "well suited for modeling a linear dynamical system" and that VJF/Bubblewrap are "preferred for higher noise regimes." This is adequate justification.
- *"Optimization algorithm not specified"* — Box-constrained minimization is standard; the precise solver is a minor implementation detail.
- *"Toy model is extremely simple"* — Toy models are intended as simple proof-of-concept demonstrations. This is not a weakness.
- *"No convergence analysis on real data"* — Convergence is shown on simulated data (Figure 1a), which is the standard approach for methods papers.
- *No style/typo/formatting criticisms* — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments surface the structural flaw in the sparsity formulation and the gap between the claimed and demonstrated validation, but these are critical observations rather than novel insights.

## Suggestions

1. **Fix the sparsity penalty in Equation (8).** Replace λ₁(‖u‖₀^max − ‖u‖₁) with λ₁‖u‖₁ (standard L1 regularization) or λ₁|‖u‖₁ − n| (target L1 norm), or use a projected-gradient approach to enforce ‖u‖₀ ≤ n directly. Verify empirically that the optimized solutions are indeed sparse and report the distribution of L0 counts.

2. **Add at least one meaningful baseline comparison.** On the toy model, compare against a simple heuristic (e.g., select neurons with largest absolute loadings on the desired latent direction) or against Bayesian optimization (Minai et al., 2024) for the same objective.

3. **Strengthen the real-data validation.** Either (a) use a dataset that contains actual stimulation-evoked neural responses (many public optogenetic datasets exist), or (b) build a substantially more challenging simulation of stimulation effects that includes nonlinearity, state dependence, and heterogeneous neural responses. In either case, clarify in the abstract that the stimulation effects are modeled, not experimentally evoked.

4. **Add ablations** for the key components: (i) learned Ŝ vs. identity mapping (Figure 5 comparison is a start but could be more rigorous), (ii) sjPCA vs. offline jPCA on a sliding window, (iii) temporal discounting vs. a static kernel.

5. **Report confidence intervals or uncertainty estimates** for the alignment angles and prediction errors in Figures 4 and 5.

## Score and Decision

**Calibration anchor summary:**

| Anchor | Path | Avg Score | Source | Comparison to this paper |
|---|---|---|---|---|
| Identifying neural dynamics using iSSM | FwW3jqchtY | 5.00 | R1-topic-mid | Stronger: real stimulation data, rigorous identifiability proof; weaker in same areas (missing baselines). Our paper scores lower. |
| When predict can also explain | SyPrLti4PG | 5.67 | R1-topic-mid | Stronger: better experiments, theoretical analysis of co-smoothing. |
| Dynamical modeling for real-time inference | eR1119aUlL | 4.25 | R1-topic-mid / R2 | Comparable quality level, similar issues (limited experiments, missing comparisons) but no mathematical error. |
| FCCA - Feedforward/Feedback subspaces | 4AlNpszv66 | 4.75 | R2 | Had serious derivation issues similar to our formulation error; harshly reviewed. |
| Closed-loop EEG stimulation | 4ltiMYgJo9 | 5.75 | R1-weakness | Better validation, real EEG data; different modality. |
| Graph-based optimization (sparsity) | uZVDJfV2Ex | 3.67 | R1-weakness | Different topic but sparsity formulation concerns. |
| TAVRNN | NPzuN3Rxi8 | 3.00 | R1-topic-low | Weaker: presentation issues, limited contribution. Our paper is stronger. |
| Sparsity beyond TopK | UbLvSPMvMA | 1.67 | R1-weakness | Fundamentally flawed approach; our paper is stronger. |

**Round-1 bracket:** 3.0 – 5.0 (based on topic mid-band and low-band anchors plus weakness queries).

**Round-2 narrowing:** Anchors inside (3.5, 5.5) and (2.5, 5.0) confirmed the bracket. The iSSM anchor (5.00) is the closest topical match but a clearly stronger paper (real stimulation, rigorous proofs). The FCCA anchor (4.75) had derivation issues of comparable severity and was treated harshly. The dynamical modeling anchor (4.25) had similar evaluation weaknesses but no mathematical error.

**What the low-band anchors failed at:** Papers scoring ≤3.5 in the topic band generally suffered from unclear contributions, poor presentation, insufficient validation, or fundamental flaws. The sparsity-error paper (3.67) and TAVRNN (3.00) exemplify these failure modes. Our paper shares the insufficient-validation problem and has a mathematical error, placing it closer to the low-mid boundary than the mid range.

The paper cannot be scored above 4.0 because (a) the iSSM paper at 5.00 had stronger validation on real stimulation data *and* rigorous theoretical results, and our paper lacks both; (b) the sparsity formulation error is a concrete mathematical mistake in a core equation that undermines a claimed constraint; (c) the absence of any meaningful baselines prevents assessment against the state of the art.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>