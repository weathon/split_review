Here is my consolidated final review.

## Summary
TimeKAN proposes a KAN-based multivariate time series forecasting model with a Multi-Scale Patching (MSP) module that uses FFT to determine patch sizes from data periodicity, and a hierarchical residual decomposition across blocks. The paper claims both state-of-the-art predictive performance and improved interpretability via symbolic regression of learned activation functions.

## Strengths
- **FFT-driven adaptive patch size selection**: The paper uses the amplitude spectrum to compute patch sizes \(p_j = \lfloor T/f_j \rfloor\) from the top-\(k\) frequencies (Section 3.3). This is a principled, data-driven alternative to manual tuning or fixed pyramid scales used in prior multi-scale approaches.
- **Incremental residual decomposition architecture**: Each TimeKAN block models only the residual not captured by prior blocks (\(Z_i = Z_{i-1} - S_i\)), enabling progressive extraction of finer-grained patterns. This design choice is clearly motivated.
- **Competitive results on standard benchmarks**: The paper reports quantitative improvements on six datasets across 27 settings, with specific gains noted (e.g., 3.4% MSE improvement over PatchTST on ETTh1 at the 336 horizon).

## Weaknesses

### Fatal
None.

### Major
- **Missing comparison against prior KAN-based forecasting methods.** The related work (Section 2) discusses T-KAN, MT-KAN (Xu et al., 2024), and RMoK (Han et al., 2024), characterizing them as "preliminary attempts." Yet none appear in the experimental comparison (Table 1). Without this comparison, the paper's implicit claim of advancing KAN-based forecasting for MTS is unsubstantiated. The reader cannot judge whether TimeKAN meaningfully improves upon the very line of work it situates itself within. This is the most significant structural gap in the evaluation.

- **Experimental setup is critically underspecified.** The experiments section reports no learning rate, optimizer, batch size, training epochs, early stopping criteria, train/val/test split details, hardware, or training time. Dataset statistics (size, dimensionality, sampling rate) are absent. The main results table and both ablation tables are embedded as images, preventing numerical verification from text. For a paper whose central claim is state-of-the-art predictive performance, these omissions mean the reported results cannot be properly assessed or reproduced.

- **Ablation results are selectively reported.** The text states "Some of the results are shown in Table 2" and "Some of the results are shown in Table 3" (lines 168, 174) without explaining which results were excluded or why. Selective reporting undermines confidence in the ablation evidence — if varying the number of MSP blocks from 1 to 6 was tested, why show only a subset? The same concern applies to the KAN-vs-MLP comparison.

- **Interpretability claim is asserted without rigorous demonstration.** The sole evidence is a single equation \(\ln(Y_i) = \cos(x_2) + \cos(x_3) + \sin(x_5)\) (Figure 1). The paper does not specify: which dataset produced this, what \(x_2, x_3, x_5\) correspond to (channels? time steps? patch indices?), how the symbolic regression was performed (algorithm/library), the fit quality (residual error), or whether such expressions generalize across patches/blocks/datasets. No systematic interpretability analysis is provided — this headline contribution is essentially unevidenced.

### Minor
- **"Kernel-based attention" phrase is inconsistent with the method.** Contribution bullet 1 (line 18) states "By utilizing kernel-based attention, TimeKAN effectively captures the nonlinear relationships" — yet the method section describes only KAN layers (spline-based univariate functions) and multi-scale patching. No attention mechanism, kernel-based or otherwise, appears in the architecture. This appears to be an error and undermines confidence in the paper's internal consistency.

- **KAN vs. MLP ablation does not control for model capacity.** The comparison uses "the same parameters except for the hidden layer parameters" (Table 3 caption) — this is contradictory. If hidden layer parameters differ, the two models have different capacities, and any performance difference may reflect capacity rather than the KAN architecture itself.

- **Tables are embedded as images** rather than text, preventing readers from extracting exact numerical values or performing independent verification.

### Trivial
None.

## Nice-to-Haves
- Report dataset statistics (size, dimensionality, sampling rate) for the six benchmarks.
- Report parameter counts for TimeKAN and all baselines to substantiate the claimed parameter efficiency.
- Include runtime/efficiency comparison, since KANs are known to be slower to train than MLPs due to spline computations.

## Removed Points
These points are flagged to be removed and should be treated with caution:
- **Missing appendix/proofs**: removed per instructions — the parser strips these sections from all papers; they exist in the original submission.
- **Training details presumably in appendix**: treated as parser artifact (fragment "1 for more details" is garbled text, not a substantive omission).
- **Code/reproducibility concerns about existence**: removed per hard rule — the paper provides a URL; questioning whether cited artifacts exist is disallowed.
- **Strength: "Controlled ablation showing KAN > MLP in identical architecture"** — removed because the verified weakness about contradictory capacity control ("same parameters except hidden layer parameters") conflicts with this claimed strength.
- **Strength: "Symbolic regression yielding interpretable mathematical expressions"** — removed because the verified weakness about insufficient interpretability demonstration conflicts with this claimed strength; the single unvalidated equation is too thin to count as a genuine strength.

## Novel Insights
None beyond the paper's own contributions. The reviews surface standard concerns about evaluation completeness but do not reveal any insight about the paper that the paper itself does not present.

## Suggestions
1. **Add T-KAN, MT-KAN, and RMoK as baselines** in the experimental comparison. This is the single most important improvement — without it, the paper's claim of advancing KAN-based forecasting is unsupported.
2. **Report full training hyperparameters**: learning rate, optimizer, batch size, epochs, early stopping, train/val/test splits, variance across seeds.
3. **Report complete ablation results** (all configurations tested, not a subset) with justification for any exclusions.
4. **Provide a properly validated interpretability example**: specify the dataset, what each input variable physically represents, the symbolic regression procedure, and the fit quality (e.g., \(R^2\) or residual error between symbolic expression and learned KAN activation).
5. **Remove or correct the "kernel-based attention" phrase** in the contribution list.
6. **For the KAN-vs-MLP ablation, either control for parameter count or explicitly discuss capacity differences** when interpreting the results.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>