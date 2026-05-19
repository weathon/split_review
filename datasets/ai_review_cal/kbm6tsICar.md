- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have all the information I need. Let me produce the final review.

## Summary

This paper proposes **direct semantic modeling** as a conceptual shift from the traditional two-step pipeline (discover a closed-form ODE, then analyze it) to directly predicting a semantic representation of a dynamical system's behavior from data. The authors formalize semantic representation as a **(composition, properties)** pair, where composition is a sequence of motifs describing trajectory shape and properties are quantitative parameters. They instantiate this for 1D systems as **Semantic ODE**, consisting of a semantic predictor \(F_{\text{sem}}\) (which predicts compositions via a piecewise-constant classifier and properties via branch-specific univariate functions) and a trajectory predictor \(F_{\text{traj}}\) (which maps semantic representations back to trajectories using cubic splines). The paper demonstrates advantages including intuitive semantic inductive biases, direct model editing, and flexibility to model non-ODE systems (delay differential equations, integro-differential equations).

## Strengths

- **Direct semantic modeling bypasses post-hoc analysis.** The architecture guarantees that \(F_{\text{sem}}\) is the semantic representation of the model by construction (Section 5: "by definition, the semantic predictor is the semantic representation of \(F\)"). This means users can inspect model behavior (e.g., "for small initial conditions the trajectory increases then decreases") without analyzing equations, directly addressing the paper's central claim.

- **Semantic inductive biases are intuitive and concretely contrasted with syntactic alternatives.** Table 1 (Section 6.1) gives a side-by-side comparison: SINDy biases concern library terms and sparsity, while Semantic ODE biases include "allowed motifs" and "horizontal asymptote range." This is a concrete, domain-expert-friendly way to encode prior knowledge that is not available in equation-discovery methods.

- **Model editing is shown quantitatively to reduce extrapolation error.** Section 6.3 reports that editing the property map to set the horizontal asymptote to 0 drops the extrapolation error to levels "comparable with the in-domain error" (Table 2). This is a direct, quantitative demonstration of an advantage that is cumbersome with closed-form equations.

- **Flexibility to model non-ODE systems is empirically demonstrated.** Table 3 shows Semantic ODE successfully models a delay differential equation (Mackey-Glass) and an integro-differential equation, where SINDy-based methods (which assume closed-form ODE structure) perform poorly. This supports the claim that direct semantic modeling does not require compact symbolic representations.

- **Formal definition of semantic representation is clear and operational.** Section 4 provides Definitions 1 and 2, a well-specified motif set (10 motifs), and a structured property schema. This formalization enables systematic construction of both the semantic predictor and the trajectory predictor.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation does not directly measure semantic predictor accuracy.** The only reported metric is trajectory RMSE (Table 3). While the architecture guarantees \(F_{\text{sem}}\) is the semantic representation if \(F_{\text{traj}}\) is faithful, the paper never reports composition classification accuracy (precision/recall of \(C_F\)) or property prediction error (e.g., MAE on transition point coordinates, asymptote values). Without these, it is impossible to tell whether \(F_{\text{sem}}\) has learned meaningful semantics or whether the trajectory predictor's flexibility is absorbing semantic errors. This is a significant gap relative to the paper's core claim that the model produces a human-accessible semantic representation.

- **The piecewise-constant composition map assumption is untested.** The paper models \(F_{\text{com}}\) as a partition of \(\mathbb{R}\) into intervals, each mapped to one composition. For the logistic growth example this is verifiable (3 branches), but the paper provides no evidence that this assumption holds for the other systems in Table 3 (general DE, DDE, integro-DE). It does not discuss how compositions vary with initial conditions for these systems, nor how the user-selected parameter \(I\) (maximum branches) is chosen. If the actual composition map varies more continuously, the model's capacity is structurally limited.

### Minor

- **The procedure for extracting ground-truth semantic representations from training trajectories is underspecified.** The paper states that \(F_{\text{com}}\) and \(F_{\text{prop}}\) are trained on data but never describes how raw trajectory observations \((t_n, y_n)\) are converted into the (composition, properties) labels needed for supervised training. For synthetic experiments the ground-truth system is known, so this is tractable, but the paper should state this explicitly. The gap becomes critical for real-world applications where derivative estimation and motif assignment under noise are nontrivial.

- **Editing demonstration is a single case study without error quantification.** The editing experiment (Section 6.3) reports a single extrapolation error reduction. There are no error bars, no comparison of editing difficulty (time, number of properties changed), no evaluation of whether editing generalizes to other systems or composition maps with many branches. The claimed ease of editing is plausible but not systematically validated.

- **No ablation study on inductive biases.** Table 1 lists semantic biases as an advantage, but the paper does not measure their effect — e.g., does restricting allowed motifs hurt RMSE? Does providing a horizontal asymptote range help? Without an ablation, the claim that semantic biases are beneficial remains qualitative.

- **C² trajectory predictor fallback rate not reported.** The paper states that if the \(C^2\) solver fails, it defaults to \(C^0\) (Section 5.2.1), but never reports how often this fallback is triggered. If the fallback is frequent, the claimed \(C^2\) smoothness is not reliably achieved.

### Trivial
None.

## Nice-to-Haves
- Reporting composition classification accuracy and property prediction error alongside trajectory RMSE would substantially strengthen the paper's core claims.
- An ablation study removing or varying the semantic inductive biases would quantify their contribution.
- Testing on real-world noisy data (e.g., sparse pharmacokinetic measurements with actual measurement noise) would increase practical relevance beyond synthetic benchmarks.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

1. **"The paper does not report results for the pharmacokinetic model in Table 3"** — Removed because the paper explicitly lists the pharmacokinetic model among the systems in Table 3 (Section 6.4: "a multidimensional ODE where only one dimension is observed (pharmacokinetic model)").

2. **"Straight-line motifs are excluded and this is not acknowledged as a limitation"** — Removed because the paper explicitly acknowledges this: "Note that we excluded the three original motifs describing straight lines to simplify the modeling process. If necessary, they can be approximated by other motifs with infinitesimal curvature" (Section 4).

3. **"Baselines may not be competitive on non-ODE systems; needs more flexible neural surrogates"** — Removed because the paper already compares against Neural ODE, Neural Laplace, and DeepONet (three flexible black-box neural approaches) in Table 3. The comparison is broader than the critic implies.

4. **"Missing comparison with a method that directly predicts trajectory values without semantics"** — Removed because Neural ODE, Neural Laplace, and DeepONet are exactly such methods (they predict trajectories directly without intermediate semantic representations).

5. **General speculative concerns about the method's applicability** (e.g., "assuming Y is the case…", "could the metric be measuring a proxy?") — Removed per the filtering rule: speculation without a specific, anchored problem in the paper text does not constitute a verifiable weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report direct semantic accuracy metrics.** Add columns to Table 3 (or a separate table) showing composition classification accuracy (e.g., F1-score) and property prediction error (e.g., normalized MAE on transition points and asymptote values) on held-out initial conditions. This directly tests whether \(F_{\text{sem}}\) has learned the intended semantics.

2. **Validate the piecewise-constant composition map assumption.** For each system in Table 3, show how the ground-truth composition varies with the initial condition, and discuss whether the piecewise-constant model is appropriate. Report how the branch count \(I\) was chosen for each system.

3. **Add an ablation for the semantic inductive biases.** Run Semantic ODE with and without the biases listed in Table 1 and report the effect on RMSE and semantic accuracy.

4. **Report the C² fallback rate.** State the percentage of test trajectories where \(F_{\text{traj}}^2\) succeeded vs. fell back to \(F_{\text{traj}}^0\).

5. **Describe the semantic label extraction pipeline.** Briefly explain how compositions and properties are obtained from training data (even if it is "for synthetic data, we compute them analytically from the known ground-truth system").
