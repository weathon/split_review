Now I have a thorough understanding of the paper and calibration anchors. Let me write the final consolidated review.

## Summary

The paper presents a streaming framework for adaptive stimulation of latent neural dynamics, combining: (i) a novel streaming jPCA (sjPCA) method for real-time latent space construction, (ii) a kernel regression model that maps (latent state, stimulation, time) to neural responses while adapting to non-stationarities, and (iii) a constrained optimization procedure that designs high-dimensional stimulation patterns to drive dynamics along a desired latent direction under sparsity and non-negativity constraints. The method is evaluated on a synthetic toy model and on two real neural datasets (calcium imaging, electrophysiology) with simulated stimulation effects, demonstrating sub-10ms average runtime.

## Strengths

1. **Novel streaming jPCA (sjPCA) that converges to an offline fit.** Section 2.1 introduces sjPCA with an Orthogonal Procrustes stabilization step (Equation 2). Figure 1a demonstrates convergence of sjPCA error to the offline reference within seconds, providing a genuinely new real-time capability beyond the original batch jPCA.

2. **Nonparametric stimulus-response model that adapts to non-stationarities.** Section 2.3 uses kernel regression with a time feature (Equation 7) to handle changing stimulus-response mappings. Figure 2d–e shows that after a 180° flip or continuous drift in the ground-truth mapping, the model recovers within 15s (flip) and continuously tracks drift, significantly outperforming a blind baseline.

3. **Constrained optimization framework for designing high-dimensional stimulations.** Section 2.4 formulates stimulation design as a tractable optimization (Equation 8) with non-negativity and sparsity constraints. Figure 4a shows designed stimuli produce significantly smaller angles to the target latent direction than random single, multiple, or shuffled stimuli, demonstrating that the learned mapping and optimization together achieve targeted perturbations.

4. **End-to-end runtime below 100ms (average <10ms).** Section 3 reports concrete timing benchmarks, providing evidence of real-time feasibility — a critical prerequisite for any future *in vivo* use.

## Weaknesses

### Major

1. **The central claim — adaptive stimulation of real neural dynamics — is not validated with real stimulation data.** The paper's title, abstract, and introduction frame the contribution as a method for adaptive stimulation of neural activity. However, every experiment on real neural data uses **simulated stimulations**: an autoregressive function adds an artificial response to recorded traces (Section 4.1: "For each of the real datasets, we simulated stimulations using an autoregressive function"). The ground-truth stimulus-response mapping is therefore known and controlled. The method never interacts with a real biological system whose response is unknown, noisy, and non-stationary. The paper acknowledges this in the Discussion ("real data experiments were performed offline") but the framing throughout overstates what was demonstrated. Without validation on real closed-loop stimulation — or at minimum a significant reframing as an algorithmic toolkit with explicit caveats — the evaluation does not match the central claim.

2. **The optimization problem is underspecified, preventing reproducibility.** Equation (8) defines a non-convex optimization over a high-dimensional vector \(u \in [0,1]^N\) (up to \(N=592\)). The paper states only that the optimization is solved with "box constraints" and that runtime is under 100ms. No details are provided about the optimization algorithm (gradient descent? L-BFGS? projected gradient?), initialization strategy, number of iterations, convergence criterion, or sensitivity to the hyperparameter \(\lambda_1\). Given the non-convexity, it is not clear that good solutions can be found reliably within the claimed time budget. This is a methodological gap that prevents reproducibility of a core component.

3. **Weak baselines and incomplete comparisons.** The primary comparison for the response model is against a "blind" model that ignores stimulation altogether (Figures 2e, 3c). This is a weak comparison: any model that accounts for stimulation will naturally outperform one that does not. The paper does not compare against alternative stimulus-response models (e.g., linear regression with input features, Gaussian process regression) to justify the choice of kernel regression. Similarly, the optimization comparisons in Figure 4 evaluate only random stimulation strategies against designed stimuli, but not other adaptive stimulation methods (e.g., Bayesian optimization, active learning, greedy selection).

4. **Multiple latent representations are introduced but never integrated into the stimulation loop.** Section 2.1 introduces sjPCA alongside proSVD and mmICA. Section 2.2 lists KF, VJF, and Bubblewrap. Figure 1c presents heatmaps of predictive probability for each latent space. However, in the real-data stimulation results (Figures 3, 4, 5), only proSVD and KF are used. The claimed "parallel evaluation across multiple latent space representations" and "adaptive selection" are described but never demonstrated in the context of actual stimulation performance — the heatmaps in Figure 1c are disconnected from the stimulation experiments.

### Minor

1. **Cluster of unspecified methodological details.** The kernel scaling constants are "optionally tuned by stochastic coordinate descent" but the procedure is not described. The \(\|u\|_0^{\max}\) term in Equation (8) is used without explicit definition (presumably the maximum allowed number of active neurons). The interaction between the scale-invariant cosine similarity and the \(\ell_1\) penalty is not discussed.

2. **Synthetic toy model is low-dimensional.** The toy model uses binary stimulation (\(u_t \in \{0,1\}\)) and a simple \(S\) that depends only on angle (Equation 9). The method is not demonstrated on high-dimensional \(u\) with a complex \(S\) in a controlled setting where ground truth is known, making it harder to separate the contribution of each component.

3. **Sensitivity analysis missing.** The paper does not analyze sensitivity to key hyperparameters: the kernel length scales, the time discount factor, and the sparsity penalty \(\lambda_1\). Ablation studies on the temporal kernel, non-negativity constraint, and sparsity penalty would strengthen the claims.

### Trivial

- None.

## Nice-to-Haves

- Comparison against a linear regression or Gaussian process stimulus-response baseline would strengthen the case for kernel regression's nonparametric flexibility.
- Integrating the streaming latent space selection (Figure 1c) into the stimulation loop would demonstrate the "adaptive selection across multiple representations" claim.
- An ablation showing the effect of removing the temporal kernel, non-negativity constraint, or sparsity penalty would help isolate the contribution of each component.
- Statistical significance tests (confidence intervals) for key comparisons would strengthen the quantitative claims.

## Removed Points

The following points from the reviewers were removed with justification:

1. **"The paper claims to 'evaluate across multiple latent space representations and multiple models of dynamics in parallel' but this is not demonstrated in the stimulation experiments."** — Partially kept as a Major weakness (#4), but the harsh critic overstated this. The paper clearly describes the parallel evaluation framework and shows the heatmaps; the issue is that this capability is not integrated into the stimulation loop, not that it doesn't exist.

2. **"The sjPCA method is novel and the convergence results in Figure 1a are reasonable. However, the paper does not explain why sjPCA is needed given that proSVD is used in the main experiments."** — This is a minor concern that is better framed as a "nice-to-have." The paper presents sjPCA as an alternative latent representation, not as a required component of the pipeline. Multiple representations are offered for flexibility.

3. **"Stochastic coordinate descent is mentioned but not described."** — Kept as a minor weakness about underspecified details.

4. **"The paragraph about Figure 1c is confusing: 'Heatmaps are estimates of where that space is most likely to give the best predictive probability (modeled using Bubblewrap)'—Bubblewrap is a dynamical model, not a model for selecting latent spaces."** — The paper is actually clear here: Bubblewrap is used as the dynamical model to compute predictive probabilities, and those probabilities are used to compare latent spaces. This is not a confusion; the sentence structure could be clearer but the content is correct.

5. **Strength Finder claims about "Parallel evaluation across multiple latent representations and dynamics models with adaptive selection"** — Demoted; the experiment shows parallel evaluation and selection potential but never uses this in the stimulation loop, so the strength as stated was overstated.

6. **Strength Finder's generic claims** ("The paper addresses a relevant and timely problem") — removed as generic.

7. **"The paper does not specify how the kernel scaling constants are tuned"** — Mentioned briefly; kept as a minor methodological detail gap.

8. **Strengths about modeling delayed responses** — This is real (Section 2.3 discusses delay \(d\) and coefficients \(\beta\)), but it's a standard feature, not a standout strength. Moved to minor supporting point.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same assessment: the framework is well-motivated and the algorithmic components are novel, but the evaluation is insufficient for the claims made.

## Suggestions

1. **Reframe the contribution.** Either (a) conduct a real closed-loop stimulation experiment to validate the full pipeline, or (b) reframe the paper clearly as a stimulation-response modeling toolkit with algorithmic contributions (sjPCA, kernel regression, constrained optimization) and explicit acknowledgment that real stimulation validation remains future work.

2. **Specify the optimization algorithm.** Provide the solver, initialization, convergence criteria, and hyperparameter selection. Show runtime breakdowns for latent space update, kernel regression update, and optimization as a function of \(N\).

3. **Add stronger baselines.** Compare the kernel regression stimulus-response model against simpler alternatives (linear regression, GP regression). Compare the optimization against basic adaptive methods (greedy selection, Bayesian optimization).

4. **Demonstrate the full claimed pipeline.** Use the parallel latent space evaluation (Figure 1c) to actually select representations during stimulation experiments, and show that this selection improves stimulation performance.

## Score and Decision

**Calibration anchors:**
- **Round 1 (bracketing):** Weak (avg <3.5): zbIS2r0t0F (3.40), z2QdVmhtAP (3.00); Middle (3.5–7.5): wCUw8t63vH (6.80), FwW3jqchtY (5.00), 9kFaNwX6rv (6.25), TVnkjz4MqV (5.50); Strong (>7.5): agPpmEgf8C (8.00), bcTjW5kS4W (7.50). **Initial bracket: 4–6.**

- **Round 2 (narrowing):** Middle-low (3.5–6.0): b7DsNJYmeo (4.67, real-time calcium imaging, withdrawn/reject), 3sfOGsBh85 (4.75), ulMXGO1fdH (4.33); Middle-high (6.0–8.0): bcTjW5kS4W (7.50, accept spotlight), 9kFaNwX6rv (6.25, accept poster), W8S8SxS9Ng (6.25, accept poster).

**Comparative analysis against key anchors:**
- **FwW3jqchtY (iSSM, avg 5.00, reject):** Most topically similar — both target causal manipulation of neural dynamics. iSSM had real stimulation data (mouse photostimulation, macaque microstimulation) but was rejected for strong assumptions and lack of baseline comparisons. The current paper has weaker evaluation (no real stimulation at all) but more algorithmic novelty and better baselines (at least a blind comparison). Comparable quality; current paper is slightly more transparent about limitations.
- **b7DsNJYmeo (realSEUDO, avg 4.67, withdrawn/reject):** About real-time processing for closed-loop neuroscience. This paper accumulated more algorithmic innovation (sjPCA + kernel regression + optimization vs. implementation tweaks on top of SEUDO) and hence is slightly stronger.
- **9kFaNwX6rv (SIMPL, avg 6.25, accept poster):** A cleaner, well-scoped contribution (EM algorithm for neural latent variable identification) with thorough validation. The current paper is broader in scope but weaker in validation, explaining the gap.

The paper has genuine algorithmic novelty and the runtime numbers are compelling. However, the evaluation gap between the central claim (adaptive stimulation of real neural dynamics) and what was actually demonstrated (simulated stimulations on recorded data) is significant. The optimization component is underspecified. The paper falls between 4.5 and 5.5, comparable to or slightly above the iSSM paper (5.00) but below the better-validated SIMPL paper (6.25).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>