Now I have enough calibration data. Let me finalize my analysis.

**Round 1 bracket**: 6.0 – 7.5. The paper is clearly stronger than all rejected papers in the 3.4–5.75 range (NF OOD paper at 3.40, PTAD at 4.25, OOD paradox paper at 5.67, NCSNAD at 5.75) and comparable to accepted papers in the 6.5–6.75 range (ImageNet-OOD at 6.50, MCM at 6.67, AnoLLM at 6.75), but not as strong as the 8.0 papers (Deep Orthogonal Hypersphere Compression).

**Round 2 narrowing**: Comparing directly:
- Better than NCSNAD (5.75, reject): stronger theory, more comprehensive evaluation (57 vs fewer datasets), no methodological issues
- Comparable to AnoLLM (6.75, accept): more comprehensive evaluation and theoretical grounding, but less novel methodologically
- Better than ImageNet-OOD (6.50, accept): more comprehensive evaluation, stronger empirical demonstration
- Outperforms MCM (6.67, accept) empirically with deeper analysis

**Final score**: 7.0 — the paper sits comfortably above the 6.5–6.75 accepted anchors due to its uniquely comprehensive evaluation (all ADBench datasets), novel d-Ratio analysis, and theoretical contributions, while its weaknesses (underspecified definition thresholds, single architecture in main text) keep it from the 7.5+ range.

---

## Summary

This paper investigates whether the well-known counterintuitive phenomenon in image-domain anomaly detection—where deep generative models assign higher likelihoods to out-of-distribution data—also occurs in tabular data. The authors propose a formal domain-agnostic definition (Definition 3.3), conduct comprehensive experiments with NICE-based NF-SLT across all 57 ADBench datasets against 12 baselines, and provide theoretical (Theorem 5.4, Corollary 5.6) and empirical (intrinsic dimension / d-Ratio analysis) explanations linking the rarity of the phenomenon to lower dimensionality and weaker feature correlation in tabular data.

## Strengths

- **Comprehensive evaluation without selection bias**: All 47 tabular and 10 CV/NLP embedding datasets from ADBench are used, against 12 baselines (6 shallow, 6 deep) with 10 repeated experiments each (Table 1). NF-SLT achieves best average AUROC (0.8575), best rank (3.43), highest top-2 ratio (0.45), and lowest fail ratio (0.02). This explicitly addresses Shwartz-Ziv & Armon (2022)'s critique of dataset selection bias and far exceeds prior work (Kirichenko et al., 2020) which tested on only 2 datasets.

- **Novel intrinsic dimension / d-Ratio analysis**: Table 4 and Figure 1 show image datasets have d-Ratio ≈ 0.2–1.9% while tabular datasets have d-Ratio of 38.9–81%, directly linking feature heterogeneity to NF-SLT success. Table 4 (bottom) shows that among 25 datasets where NF-SLT ranks ≥3, 92% have d-Ratio below 0.7, providing a concrete quantitative bridge between theoretical arguments and empirical performance.

- **Controlled dimensionality experiments**: Table 2 (ICA + RealNVP) and Table 3 (resize + Glow) provide empirical support for the dimensionality claim. Notably, Table 3 shows AUROC exceeding 0.5 for CelebA vs SVHN when resizing to 8×8 (from 0.1541 at 32×32 to 0.7037), demonstrating that simple dimensionality reduction partially alleviates the counterintuitive phenomenon in images.

- **Simple yet practically significant finding**: The demonstration that a straightforward NICE flow with standard hyperparameters outperforms 12 carefully designed baselines is practically valuable. NF-SLT's 0.02 fail ratio means it essentially never catastrophically fails, which is a strong practical guarantee.

- **Multi-pronged analysis**: The paper combines formal definition, theoretical analysis (Theorem 5.4 extending Caterini & Loaiza-Ganem's entropy framework to incorporate dimensionality), and empirical validation (d-Ratio, controlled experiments), giving depth beyond a pure benchmark study.

## Weaknesses

### Fatal
None

### Major

- **Definition 3.3 thresholds (β, γ) are never instantiated**: The definition's two conditions (Equations 2–3) use free parameters β and γ that are never assigned concrete values. In Section 4, the definition is applied informally—"the yeast dataset... minimum performance difference... is 0.02; hence, we cannot assume... counterintuitive phenomenon" (lines 124–125) and "on the 'imdb' dataset... the difference in performance... is very small" (line 125)—but without fixed thresholds. This undermines the paper's first claimed contribution ("a domain-agnostic definition that enables consistent detection and evaluation"), as the definition cannot be applied consistently without post-hoc threshold choices. The qualitative conclusion is likely robust (gaps are indeed small compared to the 6.4% vs 90%+ image case), but the formalization should commit to specific values or provide a sensitivity analysis.

- **Main results rely on a single flow architecture**: All main results in Table 1 use NICE (a 2015 architecture with fixed-volume coupling layers). The paper mentions "results of applying other flows to NF-SLT are included in Appendix G" (line 122), but the main text never surfaces these results. The core claim—"the counterintuitive phenomenon is rare in tabular data"—is about the domain, not a specific architecture. A more expressive flow might fit training distributions more tightly, potentially changing the likelihood landscape. Moving a summary of multi-architecture results into the main text would significantly strengthen the domain-level claim.

### Minor

- **Two theoretical explanations not clearly reconciled**: Theorem 5.4 assumes independent distributions (P = ∏p_i(x_i)), essential for linear-in-d scaling. Section 5.2 then argues feature correlation is the key distinguishing factor. The paper presents these as complementary "perspectives" but does not clarify their interaction. The d-Ratio analysis shows tabular data's effective dimensionality is close to ambient dimension (high d-Ratio), which actually *helps* likelihood-based detection—suggesting the two explanations are not independent but rather that correlation modulates effective dimensionality. A brief unifying discussion would strengthen the theoretical contribution.

- **Global hyperparameter selection protocol deserves explicit discussion**: The paper selects "the hyperparameter combination with the highest average AUROC for all datasets" (line 122). This is a defensible regularization strategy, but it potentially disadvantages comparison models that benefit more from dataset-specific tuning (e.g., DAGMM with its mixture components). This asymmetry should be acknowledged.

### Trivial
None

## Nice-to-Haves
- Present multi-architecture NF-SLT results (Appendix G) in the main text as a summary table.
- Provide a sensitivity analysis of Definition 3.3 across ranges of β and γ.
- Discuss whether NICE's expressiveness is sufficient to properly fit tabular distributions (e.g., examining training likelihoods) to rule out underfitting artifacts.
- Frame the CV/NLP embedding results and tabular results as a unified finding about dimensionality/correlation rather than two separate observations.

## Removed Points
These points are flagged to be removed, treat them with caution.

- "Theorem 5.4's independence assumption creates fundamental tension with the correlation analysis" — The paper explicitly presents these as complementary perspectives (Section 5.1 and 5.2 titles). The tension is a reconciliation/presentation issue rather than a contradiction. Demoted to Minor and reframed above.

## Novel Insights

The paper's most genuinely novel contribution is the d-Ratio analysis connecting intrinsic dimensionality to the absence of the counterintuitive phenomenon. The finding that 92% of datasets where NF-SLT ranks ≥3 have d-Ratio below 0.7 (Table 4, bottom) provides a concrete, quantitative bridge between abstract theoretical arguments about dimensionality/correlation and empirical performance. This extends beyond a simple benchmark study by offering a measurable predictor of when simple likelihood-based anomaly detection will succeed, and the controlled experiments (Tables 2 and 3) provide causal evidence for the dimensionality mechanism.

## Suggestions
- Commit to concrete β and γ values (e.g., β=0.5, γ=0.05) and show sensitivity analysis across plausible ranges. This directly addresses the first claimed contribution.
- Surface a summary of Appendix G's multi-architecture results in the main text (even a single sentence with key numbers would help).
- Add a brief paragraph in Section 5 reconciling the dimensionality and correlation explanations under a unified framework (e.g., showing that correlation reduces effective dimensionality, which is the true driver).

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| NF for OOD via Latent Density | 6Z8rZlKpNT.md | 3.40 | 1 | Much weaker — limited novelty, evaluation issues; paper under review clearly superior |
| OOD Detection Paradox / Likelihood Peaks | jQ596tXT3k.md | 5.67 | 1,2 | Similar topic but less comprehensive; paper under review has stronger empirical evidence and broader scope |
| NCSNAD Tabular Anomaly Detection | 7QDIFrtAsB.md | 5.75 | 1,2 | Similar scope but limited novelty; paper under review has deeper theoretical contribution |
| PTAD Tabular Anomaly Detection | Vi6p2TeujL.md | 4.25 | 1 | Weaker — complex framework without clear novelty; paper under review substantially better |
| Double Descent Meets OOD | eN0RyRVbSm.md | 6.50 | 2 | Similar theoretical depth for OOD; paper under review has more comprehensive empirical grounding |
| ImageNet-OOD | VTYg5ykEGS.md | 6.50 | 2 | Similar analytical contribution; paper under review has more comprehensive evaluation |
| Graph AD/OOD Benchmark | g90RNzs8wX.md | 6.50 | 1 | Different domain but similar unifying-benchmark contribution; paper under review has stronger theory |
| Swift Hydra Anomaly Detection | P7t2niLbvw.md | 6.50 | 2 | Different focus; paper under review has more thorough evaluation |
| MCM: Masked Cell Modeling | lNZJyEDxy4.md | 6.67 | 2 | Paper under review empirically outperforms MCM and provides deeper analysis |
| AnoLLM Tabular Anomaly Detection | 7VkHffT5X2.md | 6.75 | 1,2 | Paper under review is more comprehensive (57 vs 36 datasets) and more theoretically grounded |
| Deep Neural Networks Extrapolate Predictably | ljwoQ3cvQh.md | 7.00 | 2 | Similar quality insight contribution; paper under review has comparable depth |
| Deep Orthogonal Hypersphere Compression | cJs4oE4m9Q.md | 8.00 | 1 | Stronger — novel theoretical contributions across multiple data types; paper under review is below this level |

**Round 1 bracket**: 6.0 – 7.5. **Round 2 narrowed to**: 6.5 – 7.0. Paper sits above the 6.5–6.75 accepted anchors due to uniquely comprehensive evaluation and novel d-Ratio analysis, but below 7.5+ due to underspecified definition and single-architecture limitation.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>