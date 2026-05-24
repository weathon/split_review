Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the review.

## Summary of calibration

**Round 1 bracket**: Low band (<3.5) — papers scoring 2.5–3.4; Middle band (3.5–7.5) — papers scoring 4.25–6.75; Strong band (>7.5) — papers scoring 8.0. The paper clearly sits in the middle-to-upper-middle band. Narrowing the bracket: somewhere between 5.5 and 7.0.

**Round 2 narrowing**: Comparable papers in the 4.5–6.5 range (DRL: 5.75/Accept, Gradients AD: 5.75/Reject, OOD Paradox: 5.67/Reject, Zero-shot OD: 5.75/Reject) and the 6.0–7.5 range (MCM: 6.67/Accept, AnoLLM: 6.75/Accept, Diffusion AD: 7.00/Accept, Kernelised Flows: 6.75/Accept).

The current paper is stronger than the 5.75 group (more comprehensive empirical evaluation, rigorous theoretical results) but does not match the strongest 7.0 papers. It is comparable to the 6.67–6.75 Accept papers. Its main empirical strengths (47 datasets, no selection bias, strong theoretical backing) are offset by the incomplete operationalization of its own definition and the lack of a controlled image comparison. Final score: **6.0**.

---

## Final Review

## Summary

This paper investigates whether the counterintuitive phenomenon observed in image anomaly detection—where normalizing flows assign higher likelihoods to out-of-distribution data than to in-distribution data—also occurs in tabular data. The authors propose a domain-agnostic definition of this phenomenon (Definition 3.3) based on relative AUROC compared to other detection models, and conduct extensive experiments on 47 tabular and 10 CV/NLP embedding datasets from ADBench with 12 baselines. Their normalizing flow model (NF-SLT) achieves the highest average AUROC (0.8575), best average rank (3.43), and a very low fail ratio (0.02). The paper further provides theoretical analysis (Theorem 5.4, Corollary 5.6) linking dimensionality to likelihood inversion, and empirical analysis using intrinsic dimension to show that tabular data has weaker feature correlations than images. The central conclusion is that the counterintuitive phenomenon is rare in tabular data, and that simple likelihood-based detection with normalizing flows is a reliable approach for tabular anomaly detection.

## Strengths

1. **Comprehensive and unbiased empirical evaluation.** The paper uses all 47 tabular datasets from ADBench without selection bias (citing Shwartz-Ziv & Armon, 2022), plus 10 CV/NLP embedding datasets, comparing against 12 baseline models spanning both shallow and deep methods. NF-SLT achieves the highest average AUROC (0.8575), average rank (3.43), top2 ratio (0.45), and a fail ratio of only 0.02 (Table 1). This provides strong evidence that the simple likelihood test works well across diverse tabular settings.

2. **Theoretical analysis of dimensionality's role.** Theorem 5.4 proves that under an independent-feature assumption, the expected likelihood gap between normal and anomalous data has a lower bound that decreases linearly with dimension \(d\). Corollary 5.6 shows that the maximum achievable AUROC is inversely related to \(d\) when the likelihood gap is negative. These results provide a formal explanation for why lower-dimensional tabular data (Fact 1.1) is less susceptible to the counterintuitive phenomenon. The ICA dimensionality reduction experiments in Table 2 (e.g., CIFAR-100/SVHN AUROC improving from 0.0843 at 1024 dims to 0.3490 at 30 dims) directly validate the theoretical prediction.

3. **Feature correlation analysis via intrinsic dimension.** The paper introduces the \(d\) Ratio (intrinsic/ambient dimension) to quantify feature correlation. Table 4 and Figure 1 show that image datasets have \(d\) Ratio ≈ 0.01 (CIFAR-10: 0.003), while tabular datasets have much higher values (magicgamma: 0.70, waveform: 0.81). The log-scale scatter plot (Figure 1, right) shows tabular points clustered near the identity line while image points are far below it. This provides a principled, quantitative explanation for why tabular data's heterogeneous features (Fact 1.2) mitigate the phenomenon.

4. **Domain-agnostic definition of the counterintuitive phenomenon.** Definition 3.3 formalizes the phenomenon in terms of relative AUROC performance compared to other models, moving beyond the vague "likelihood inversion" framing. This provides a clear framework for consistent evaluation across domains, which was previously lacking in the literature.

5. **Reproducibility focus.** The paper provides code, hyperparameter search details, and sensitivity experiments (Appendix F), enabling independent verification.

## Weaknesses

### Major
None identified that threaten the core claims of the paper.

### Minor

1. **Definition 3.3 is not fully operationalized.** The paper introduces thresholds \(\beta\) and \(\gamma\) in Definition 3.3 but never specifies concrete values or applies the definition systematically across the 47 datasets to determine how many exhibit the phenomenon. The empirical evaluation instead relies on aggregate metrics (average AUROC, fail ratio, top2 ratio) and a single case study (yeast). While these metrics convincingly support the paper's claim, the stated definition is treated as a conceptual framework rather than an evaluative tool, creating a disconnect between the formalism and the experiments. The "fully rigorous formulation" deferred to Appendix B cannot be checked. Setting reasonable defaults (e.g., \(\beta=0.5, \gamma=0.05\)) and reporting the proportion of datasets satisfying Definition 3.3 would substantially tighten the argument.

2. **Controlled image comparison is absent.** The paper claims the phenomenon "occurs far less often in tabular settings" than in images, but no parallel experiment is conducted on image data using the same evaluation protocol and baseline set. The only image evidence cited is a single AUROC value (6.4%) from prior work using a different model (Glow) and different baselines. The paper's own image experiments (Tables 2, 3) focus on the dimensionality effect rather than a systematic comparative evaluation. While the image-domain counterintuitive phenomenon is well-established in prior literature, the paper's comparative claim would be stronger with a controlled apples-to-apples comparison.

3. **The definition shifts the meaning of "counterintuitive phenomenon."** The original phenomenon (Nalisnick et al., 2019a) specifically concerns likelihood inversion—OOD data receiving higher likelihoods than in-distribution data. Definition 3.3 instead captures cases where the generative model underperforms relative to other methods, which is a broader notion. The paper acknowledges this shift and provides justification (the simple AUROC<0.5 criterion is too strict and conflates dataset difficulty with the phenomenon), but the conceptual change is under-discussed. Notably, the paper never reports the proportion of datasets where NF-SLT achieves AUROC below 0.5 (the direct indicator of likelihood inversion), which would bridge the original and proposed definitions.

4. **Hyperparameter selection favors robustness over per-dataset optimality.** The paper selects a single hyperparameter configuration that maximizes average AUROC across all datasets. This is an unconventional but defensible choice; however, its impact on relative performance comparisons is not discussed. Some baselines (e.g., DeepSVDD) are known to benefit significantly from per-dataset tuning, which could change relative rankings.

5. **Independence assumptions in the theoretical analysis.** Theorem 5.4 assumes independent features in both \(P\) and \(Q\), which does not hold for real tabular data. The paper acknowledges this implicitly but does not discuss how violations of independence might affect the theoretical conclusions. The connection between theory and the tabular setting is argued qualitatively rather than formally.

### Trivial
- The paper refers to an appendix ("fully rigorous formulation... provided in Appendix B") that is not available to reviewers, but this is a parser artifact.
- Minor notation issues: \(\mathbb{H}(P) > \mathbb{H}(Q)\) condition in Theorem 5.4 is discussed but the exact condition from the theorem statement uses \(\mathbb{H}(P) - \mathbb{H}(Q) > D_{KL}(Q||P)\), which requires clarification in the main text.

## Nice-to-Haves

- Apply Definition 3.3 explicitly: choose reasonable \(\beta\) and \(\gamma\) values (or a range for sensitivity analysis) and report the number of datasets (out of 47) that satisfy both conditions. This would turn the main claim from an impression to a precise quantitative result.
- Run a parallel experiment on a representative set of image datasets using the same baselines and evaluation protocol to support the "far less often" comparative claim.
- Report the proportion of tabular datasets where NF-SLT's AUROC falls below 0.5 (direct likelihood inversion), which would connect the analysis to the original phenomenon definition.

## Removed Points

These points from the reviewers are removed after cross-checking against the paper:

- **"Baselines include models known to be weak on tabular data (e.g., OCSVM, DAGMM), which makes it easier for NF-SLT to appear relatively strong."** — The paper uses the complete ADBench suite without selection bias, which is a stated strength. The baseline set includes both strong methods (IF, LOF, ICL, MCM) and weak ones, which is standard practice for comprehensive benchmarks. The asymmetry is not a weakness; the point is removed.

- **"The claim that the phenomenon is less frequent than in images is not empirically compared."** — Weakened to Minor (see Weakness #2). The original framing as a fatal flaw is rejected because the image-domain phenomenon is well-established in prior work, and the paper provides some image experiments (Tables 2, 3) showing the effect.

- **"Definition conflates likelihood inversion with relative underperformance" as a fatal flaw.** — The paper explicitly justifies this shift in the introduction (the simple likelihood-inversion definition is contradictory because any result below 100% AUROC would qualify) and provides a reasoned argument for the broader definition. The criticism is retained as Minor (Weakness #3) but the characterization as a fatal conceptual error is removed.

- **"The paper does not report the proportion of datasets where NF-SLT achieves AUROC below 0.5 (direct indicator of likelihood inversion)."** — This is a reasonable suggestion but not a weakness, as the paper explicitly argues that AUROC < 0.5 is too strict a criterion (it would consider any imperfect detection as counterintuitive). Moved to Nice-to-Haves.

- **"The sensitivity of Definition 3.3 to the choice of β and γ is not analyzed."** — Subsumed by Minor Weakness #1.

- **Pure formatting/style nitpicks and parser artifacts** are removed per guidelines.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's formal definition of the counterintuitive phenomenon and its actual evaluation strategy. The paper introduces Definition 3.3 (with \(\beta\), \(\gamma\) thresholds and a "fully rigorous formulation" in the appendix) as a novel contribution, but the empirical evaluation falls back on aggregate performance metrics that do not instantiate the definition. This disconnect suggests that the definition may be more useful as a conceptual framework than as an operational tool in its current form. A genuinely novel insight would be whether explicit application of Definition 3.3 with reasonable thresholds would confirm or qualify the paper's conclusion that the phenomenon is rare. The intrinsic dimension analysis (Section 5.2) offers a compelling and testable explanation for why tabular data resists the phenomenon, and extends naturally to the CV/NLP embedding results—this is perhaps the paper's most distinctive analytical contribution, as it provides a continuous measure (the \(d\) Ratio) that correlates with detection difficulty even within the tabular domain (Table 4 bottom). None beyond the paper's own contributions in the theoretical and empirical analysis.

## Suggestions

- **Specify \(\beta\) and \(\gamma\) values and explicitly apply Definition 3.3.** Choose reasonable thresholds (e.g., \(\beta=0.5\) meaning most baselines outperform the model, \(\gamma=0.05\) or 0.1 for a meaningful gap), apply them to the 47 datasets, and report counts. This would take seconds given the existing data and would eliminate the gap between the definition and the evaluation.
- **Add a controlled image comparison experiment.** Apply the same evaluation protocol (same baselines, same definition, multiple datasets) to a set of image datasets. Even a smaller-scale experiment (5-10 image datasets) would substantially strengthen the comparative claim.
- **Report AUROC < 0.5 statistics.** As a bridge to the original phenomenon definition, report how many tabular datasets show NF-SLT AUROC below 0.5. This simple statistic complements the relative-performance framing.
- **Discuss the impact of the independence assumption** in Theorem 5.4 on the applicability of the theoretical results to real tabular data.
- **Include a sensitivity analysis** of how the conclusions would change under different \(\beta\) and \(\gamma\) choices.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- 6Z8rZlKpNT (3.40) — NF for OOD via Latent Density Estimation. Much weaker; limited experiments. Current paper stronger.
- rcmhydaEJp (3.00) — Flow-based imputation. Different topic. Not comparable.
- i28ZjVxl81 (2.50) — OOD in prediction problems. Very weak.
- 3qDhqj6qfu (3.00) — TabKANet. Tabular classification, not AD. Not comparable.
- 7QDIFrtAsB (5.75) — Gradients AD (tabular, NCSN). Extensive experiments but limited novelty. Current paper comparable or slightly stronger.
- jQ596tXT3k (5.67) — OOD Paradox explanation (images). Current paper stronger in both theory and empirical scope.
- 7VkHffT5X2 (6.75) — AnoLLM (LLMs for tabular AD). Current paper weaker in methodological novelty but stronger in analysis depth.
- Vi6p2TeujL (4.25) — PTAD. Current paper stronger.
- cJs4oE4m9Q (8.00) — Deep Orthogonal Hypersphere Compression. Much stronger overall.
- ZCOwwRAaEl (8.00) — Latent Bayesian Optimization. Different topic.
- I5lcjmFmlc (8.00) — Robust Classification via Diffusion. Different topic.
- k38Th3x4d9 (8.00) — Root Cause Analysis. Different topic.

**Round 2 (Narrowing):**
- CJnceDksRd (5.75, Accept) — DRL (tabular AD method). Current paper slightly stronger (more datasets, tighter theory).
- gRXLa6LS3J (5.75, Reject) — Zero-shot OD via Transformers. Different approach, comparable score band.
- lNZJyEDxy4 (6.67, Accept) — MCM (tabular AD). Current paper similar quality, different contribution type.
- lR3rk7ysXz (7.00, Accept) — Diffusion AD (DTE). Stronger overall (clever idea, thorough evaluation).
- iTFdNLHE7k (6.75, Accept) — Kernelised Normalising Flows. Different topic, comparable score.

**Final bracket**: Round 1 placed the paper between 5.5 and 7.0. Round 2 anchors at 5.75, 6.67, 6.75, 7.00 placed it between the 5.75 group (which it exceeds) and the 6.67–7.00 group (which it approaches but does not match in methodological novelty). The paper's rigorous theoretical analysis and comprehensive unbiased benchmark are its strongest assets; the incomplete operationalization of its own definition and lack of controlled image comparison prevent it from reaching the 6.67+ tier. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>