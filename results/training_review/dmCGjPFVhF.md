Here is my synthesized final review.

---

## Summary

The paper introduces FACTS (FACTored State-space), a recurrent framework for world modelling that treats both the latent state and input features as sets of nodes. It uses an attention-based routing mechanism to dynamically assign input features to latent factors, and the state update is designed to be permutation-invariant with respect to input features (R.P.I.) and permutation-equivariant with respect to the latent factors (L.P.E.). The paper provides theoretical analysis of these invariance properties, derives a linearised formulation that enables parallel computation, and evaluates FACTS on multivariate time series forecasting, object-centric video prediction, and graph-based traffic prediction, achieving competitive or superior results against specialised baselines.

## Strengths

- **Provable permutation invariance/equivariance with strong empirical validation.** The paper formally defines L.P.E. and R.P.I. properties (Definitions 1, 2) and proves them for the FACTS dynamics (Theorems 1, 2). This is directly corroborated by Figure 2, where FACTS maintains stable prediction error under random test-time input permutations while iTransformer and S-Mamba degrade severely (e.g., S-Mamba's MSE on Traffic increases more than threefold). This combination of theory and targeted experiment is the paper's strongest piece of evidence.

- **Competitive performance across diverse tasks.** Despite being a general-purpose framework, FACTS achieves top-2 MAE on 7 out of 9 MTS forecasting datasets (Table 1), the lowest LPIPS (0.09) on CLEVRER object dynamics (Table 2), and a MAPE of 9.08% on METR-LA traffic prediction versus the prior best of 9.67% from TESTAM (Table 3). The breadth of evaluation across three distinct modalities strengthens the claim of generality.

- **Linearised variant with demonstrated empirical efficiency.** The paper derives a closed-form expansion (Equations 17–20) that replaces the non-linear dependency on \(Z_{t-1}\) in the routing with the initial memory \(Z_0\), enabling parallel computation. Figure 3 shows that the parallel version performs nearly identically to the fully recurrent version across segment window sizes on the Electricity dataset, validating the practical utility of the approximation.

- **General theoretical condition for future SSM design.** Theorem 2 establishes that any dynamics of the form in Equation 10 inherits L.P.E. and R.P.I. properties provided the selective parameters \(\bar{A}, \bar{B}, U\) satisfy these properties. This provides a clean design principle for developing other permutation-invariant state-space models beyond FACTS.

## Weaknesses

### Fatal
None.

### Major
- **The linearised formulation weakens the "dynamic routing" claim in practice.** The paper motivates FACTS by the need to dynamically assign input features to factors based on the evolving state \(Z_{t-1}\) (Section 3, Figure 1). However, the linearised version used for parallel computation substitutes \(Z_{t-1}\) with the fixed initial memory \(Z_0\) inside the routing functions \(\bar{A}, \bar{B}, U\) (lines 119–127). While the paper is transparent about this substitution and segments can be used to refresh \(Z_0\), within each segment the routing is not conditioned on the evolving memory. The paper claims (line 26) that "FACTS dynamically assigns input features to distinct latent state-space factors," but the implemented model only does so partially: the per-segment routing depends on \(X_t\) but not on the moment-to-moment changes in \(Z_{t-1}\). The authors acknowledge the linearisation but never discuss this discrepancy, and the parallel–recurrent comparison (Figure 3) is only on Electricity, leaving the cost of linearisation on tasks with stronger temporal dynamics (e.g., object-centric video) unexamined. This gap between motivation and implementation is the paper's most significant weakness.

### Minor
- **Statistical uncertainty is not reported for main results.** Tables 1, 2, and 3 report only point estimates (MSE, MAE, LPIPS, MAPE) without standard deviations, confidence intervals, or number of seeds. Given that performance differences between top methods are often small (e.g., 0.066 vs 0.065 in Table 1), it is impossible to assess whether FACTS is significantly better, equivalent, or worse than the baselines. Figure 2 does provide error bars (5 seeds, ±2σ), and the paper would benefit from extending this practice to all main tables.

- **The MTS baseline comparison may be confounded by architectural asymmetry.** The paper states (line 183) that it replaces the standard TSLib pre- and post-processing modules with "set functions to accommodate the output structure of FACTS," while baselines (iTransformer, S-Mamba, etc.) use their standard linear projections. Any observed improvement could partly stem from these better-suited set functions rather than the core FACTS routing mechanism. A control experiment — equipping baselines with similar set-based embedders or showing FACTS with standard linear projections performs similarly — would strengthen the comparison.

- **Missing ablations of key components.** Several design choices are not isolated through ablation experiments: (a) the attention-based routing vs. a fixed or random assignment of input features to factors; (b) the inclusion of \(Z_{t-1}\) in \(U_t\) vs. using only \(X_t\) (as in standard SSMs); (c) the impact of the number of latent factors \(k\) on performance. Without these, it is difficult to attribute the empirical results to the specific claimed innovations rather than to general model capacity.

- **Ambiguity about which model variant produced each result.** The paper presents two distinct versions: the general recurrent FACTS (Equation 10, routing depends on \(Z_{t-1}\)) and the linearised FACTS (Equations 17–20, routing depends on \(Z_0\)). The main experimental sections (Tables 1, 2, 3) do not explicitly state which variant is evaluated, nor whether segmentation was used. The reader has to infer from context (e.g., the parallel–recurrent discussion in Section 4.1.1, where "window size of 96 corresponds to fully parallel FACTS") that the linearised variant was likely used. The paper should state this upfront for each experiment.

- **Unsupported claim about learning "statistical independence factors."** Line 185 states that FACTS "encourages better learning statistical independence factors," but no evidence is provided (e.g., mutual information, disentanglement metrics, or qualitative factor analysis). This claim is speculative in its current form.

- **The graph-prediction experiment is thin.** Table 3 reports results on a single dataset (METR-LA) with one metric set, providing limited evidence for the claim that FACTS handles graph-structured data.

### Trivial
- None.

## Nice-to-Haves

- **Analysis of factor consistency over time.** In the object-centric setting, visualisations showing whether the same factor (object) is consistently tracked across frames under permutations would visually confirm the invariance claim.
- **Recurrent vs. linearised comparison on object-centric tasks.** Repeating the Figure 3 analysis on CLEVRER or MOVi-A would reveal whether the linearisation cost varies by task difficulty.
- **Sensitivity analysis for the number of latent factors \(k\).** This hyperparameter is likely important but is not explored.
- **Qualitative comparisons of predicted frames.** LPIPS numbers are useful, but example predictions from FACTS vs. SlotFormer would help interpret the visual quality difference.

## Removed Points

These points were flagged by reviewers but are removed as per the meta-review guidelines:

- **"Missing proof in main text / appendix deferred."** The full proofs were stated to be in the appendix; the parser strips appendix content from all papers. This criticism reflects a parser artifact, not a paper deficiency. (Hard Rule: REMOVE)
- **"Missing PSNR/SSIM for object dynamics."** The paper explicitly justifies using LPIPS over PSNR/SSIM ("stronger alignment with human perception," line 218), citing the baseline's own practices. This is a deliberate design choice, not an omission.
- **"Only three models tested in permutation experiment."** The experiment focuses on top-performing models from Table 1 (FACTS, iTransformer, S-Mamba). Adding more baselines would be welcome but the current selection is sufficient to demonstrate the claimed effect.
- **"Model size / efficiency not compared."** The paper focuses on prediction accuracy; efficiency is addressed via the linearisation (Figure 3). A full efficiency analysis is a natural extension but not a core requirement.

## Novel Insights

None beyond the paper's own contributions. The reviews surface predictable tensions (linearisation vs. dynamic routing, missing ablations) but do not identify a new angle or reinterpretation that the authors themselves missed.

## Suggestions

1. **Explicitly state which variant (recurrent or linearised) is used in each experiment**, and clarify whether and how segmentation is applied. This alone would resolve much of the ambiguity.
2. **Add at least one ablation**: compare learned attention-based routing against random/fixed assignment on one dataset (e.g., Electricity or CLEVRER) to isolate the routing mechanism's contribution.
3. **Report standard deviations** for Tables 1 and 2 over multiple seeds, or cite prior convention if single-run reporting is standard for the benchmark.
4. **Include a controlled baseline experiment** for MTS forecasting that either uses standard linear projections for FACTS or adds set-based embedders to the competing baselines.
5. **Add a brief discussion** acknowledging the gap between the general recurrent formulation (dynamic routing via \(Z_{t-1}\)) and the linearised implementation (routing via \(Z_0\)), explaining the practical implications and the conditions under which the approximation is likely to hold.
6. **Remove or qualify** the unsupported claim about "statistical independence factors" (line 185), or provide supporting analysis.

---

**MY FINAL SCORE: <pineapple>6.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**