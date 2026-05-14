Now I have all the information I need to write the consolidated review.

## Summary

This paper investigates whether the "counterintuitive phenomenon" (where deep generative models assign higher likelihoods to OOD data than in-distribution data, first documented in images) also occurs in tabular anomaly detection. The authors propose a domain-agnostic formal definition of this phenomenon based on relative underperformance against other models, then conduct a large-scale benchmark (47 tabular + 10 embedding datasets from ADBench, 12 baselines) showing that simple likelihood testing with normalizing flows (NF-SLT) rarely underperforms other methods, and often outperforms them. They further provide theoretical analysis linking dimensionality to the likelihood gap (Theorem 5.4) and empirical analysis via intrinsic dimension ratios to explain why tabular data is less susceptible to the phenomenon than images.

## Strengths

- **Comprehensive, unbiased benchmark.** The paper tests all 47 tabular and 10 CV/NLP embedding datasets from ADBench against 12 diverse baselines, following the criticism of dataset cherry-picking (Shwartz-Ziv & Armon, 2022). This is a substantial experimental effort. NF-SLT achieves the best AUROC (0.8575), lowest fail ratio (0.02), and best average rank (3.43) among all methods.

- **Robustness of NF-SLT's leading position.** Per-dataset optimal hyperparameter results (Table 15) confirm NF-SLT still leads (0.8691 AUROC) even when all models are individually tuned, and hyperparameter sensitivity analysis (Table 12) shows NF-SLT is the least sensitive model — the results are not artifacts of tuning choices.

- **Theoretical analysis linking dimension to likelihood degradation.** Theorem 5.4 shows that under independent-feature assumptions, the lower bound of the likelihood expectation gap decreases linearly with dimension when entropy differences exceed KL divergence. Corollary 5.6 extends this to AUROC upper bounds. The ICA dimensionality-reduction experiments on images (Table 2) provide empirical support, showing AUROC improving from ~0.23 to ~0.47 as dimension drops.

- **Intrinsic dimension analysis provides a concrete, measurable explanation.** The d_Ratio (ID/ambient dimension) cleanly separates tabular (0.39–0.81) from image (~0.002–0.019) data, and the analysis of NF-SLT failure cases (rank ≥ 3) shows these occur predominantly on datasets with low d_Ratio. This connects feature correlation to detection performance in a quantifiable way.

## Weaknesses

### Major

- **The paper's central claim — that the counterintuitive phenomenon is rare in tabular data — is never directly tested via the paper's own definition.** Definition 3.3 operationalizes the phenomenon via two thresholded conditions (β and γ), but the paper never specifies concrete values for β or γ, never computes condition (2) (fraction of outperforming models > β) or condition (3) (minimum gap > γ) across the 47 datasets, and never reports the fraction of datasets where the phenomenon occurs by this definition. Instead, the paper argues indirectly: NF-SLT has a low fail ratio (0.02) and a small gap on the "yeast" dataset (0.02), therefore the phenomenon must be rare. This is a reasonable proxy argument but not a substitute for applying the definition. The headline claim about the counterintuitive phenomenon is thus supported by circumstantial evidence rather than direct measurement.

- **Definition 3.3 shifts the meaning of the phenomenon from likelihood inversion (AUROC < 0.5, the original finding in Nalisnick et al. 2019a) to relative underperformance against other models, without adequately justifying this reconceptualization.** These are genuinely different phenomena: a model could exhibit severe likelihood inversion (AUROC far below 0.5) but the definition would not flag it if all baselines are also weak (condition (2) fails). Conversely, a model with AUROC=0.6 could be flagged if baselines achieve 0.9. The paper's claim that the counterintuitive phenomenon is "rare in tabular data" conflates two distinct claims: (a) likelihood inversion rarely happens, and (b) NF-SLT rarely underperforms other methods. Claim (b) is well-supported; claim (a) is not directly tested. The paper acknowledges this tension in Section 2 but never resolves it.

- **Hyperparameter selection procedure is unusual and, while mitigated by per-dataset results, still clouds interpretation.** The paper selects a single hyperparameter combination per model by maximizing average AUROC across *all* 47 datasets simultaneously (Section 4, Appendix F). This could advantage models less sensitive to hyperparameters (like NF-SLT, Table 12) over models that benefit more from per-dataset tuning. The per-dataset optimal results (Table 15) partially address this — NF-SLT still leads — but the gap to the second-best method (ICL) narrows from 0.0367 to 0.0199. The main results (Table 1) are based on the fixed-hyperparameter setting, and the paper's claims should be evaluated with this caveat in mind.

### Minor

- **The theoretical analysis (Theorem 5.4, Corollary 5.6) relies on strong assumptions (independent features, perfect model limit, specific moment scaling) that do not hold for real data.** The paper acknowledges this (images do not satisfy independence) and provides dimensionality-reduction experiments as validation, but the results are mixed — some trends go in the expected direction, others are absent or reversed (Tables 3, 5, 6). The explanations offered for discrepancies (e.g., "bilinear interpolation strengthens correlations") are heuristic. The theory connects to the likelihood gap, not directly to Definition 3.3, creating an additional inferential gap.

- **The analysis of the counterintuitive phenomenon on CV/NLP embedding datasets (Table 1, bottom) undermines the domain-specific framing.** NF-SLT outperforms other models on 9/10 embedding datasets. If the phenomenon were truly domain-specific to images versus tabular data, embeddings of images should behave like images, not like tabular data. The paper provides a post-hoc explanation (embeddings have higher d_Ratio than raw pixels) which is reasonable but blunts the force of the main domain-contrast narrative.

- **Only one concrete dataset example ("yeast", gap 0.02) is discussed for failure-case analysis.** The paper would benefit from reporting the distribution of AUROC gaps across all datasets, and from checking whether the handful of datasets where NF-SLT ranks poorly satisfy Definition 3.3 under reasonable (β, γ) values.

### Trivial

- Table formatting in the extracted text is distorted; the original submission likely has proper formatting.
- The paper uses "conterintuitive" (typo) in the introduction text.

## Nice-to-Haves

- **Direct test for likelihood inversion (AUROC < 0.5).** A simpler and more direct claim would be to report how often NF-SLT's AUROC falls below 0.5 across ADBench datasets. (From Table 17, yeast appears to be the only case.) This would connect to the original paradox literature without relying on the relative-performance definition.
- **Histogram or table of min_i (AUROC_i – AUROC_0) across all 47 datasets**, so readers can assess whether gaps are generally small without relying on a single example.
- **Investigation of the datasets where NF-SLT ranks ≥ 3** (which Table 4 bottom links to low d_Ratio), checking whether they satisfy Definition 3.3 — this would directly connect the feature-correlation analysis to the phenomenon claim.

## Removed Points

- *"The paper never specifies what values of β and γ are used"* → This is actually a valid weakness, kept in Major. But the harsh critic's claim that the paper's central claim "collapses into a tautology" is removed as an overstatement — the fail-ratio argument is a reasonable proxy even if it doesn't directly operationalize the definition.
- *"Unfair comparison with other methods"* → The paper's own per-dataset results (Table 15) show NF-SLT still leads even when others are individually optimized. The harsh critic's framing that this "may inflate NF-SLT's relative performance" is weakened by the paper's own robustness checks. Moved to Minor.
- *"The definition is also domain-agnostic in name only—it depends entirely on the set of comparison models"* → Kept as part of the Major weakness about definition shift, but the "domain-agnostic" critique is inherent to any relative definition and not unique to this paper.
- *"The paper should report results with per-dataset validation-based tuning or provide a stronger justification"* → The paper already reports per-dataset optimal results (Table 15), so this specific demand is already addressed.
- Various formatting/style nitpicks removed per instructions.
- The Strength Finder's claim that the definition "enables consistent detection and evaluation across different data modalities" conflicts with the verified weakness that the definition was never operationalized — the weakness wins, so this strength is dropped.
- Strength Finder's claim about "directly addressing the criticism of dataset cherry-picking" — kept.
- Strength Finder's claim about "novel domain-agnostic definition" — retained with caveat.

## Novel Insights

An interesting tension emerges across the reviews: the paper's strongest contributions (comprehensive benchmarking, intrinsic dimension analysis, dimensionality theory) actually support a claim that is *different from* — though related to — the advertised headline. The paper convincingly shows that NF-SLT is a strong anomaly detector for tabular data and provides mechanistic explanations in terms of dimension and feature correlation. But whether this constitutes "the counterintuitive phenomenon rarely occurs" depends on which definition one adopts. Under a strict likelihood-inversion definition (AUROC < 0.5), the phenomenon seems genuinely rare in ADBench. Under the paper's own relative-performance definition, the claim is never formally tested. This disconnect between the framing and the actual experimental design is the paper's central weakness, but resolving it would likely strengthen rather than weaken the overall contribution.

## Suggestions

1. **Operationalize Definition 3.3.** Pick at least one plausible (β, γ) pair (e.g., β=0.5, γ=0.05 or β=0.5, γ=0.1) and report the fraction of datasets where both conditions hold. This directly tests your central claim.
2. **Disambiguate the two meanings of "counterintuitive phenomenon."** Add a parallel analysis using the straightforward likelihood-inversion criterion (AUROC < 0.5) and discuss how often each definition flags each dataset. This would clarify what claim is being made.
3. **Report the distribution of min_i(AUROC_i – AUROC_0) across all datasets** (a histogram or table) rather than only the yeast example.
4. **Tone down the framing** to better match what is actually demonstrated: "Simple likelihood testing with normalizing flows performs strongly on tabular anomaly detection benchmarks and rarely underperforms other methods, unlike in the image domain where it often fails."

## Score and Decision

**Calibration anchors (from batch retrieval):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/JdbqDiguyO.md` (NRDE, tabular AD + normalizing flows) | 3.33 (Reject) | Weaker: poor writing, partial code, unvalidated assumptions. Our paper is much more thorough empirically and analytically. |
| `/home/wg25r/review_agent/human_reviews_2026/Ct3MmgpOki.md` (LATTE, tabular AD) | 3.00 (Reject) | Weaker: smaller benchmark, no theoretical analysis of the phenomenon. Our paper's scope is broader. |
| `/home/wg25r/review_agent/human_reviews_2026/73QNa7rAgm.md` (TCAD, tabular AD) | 4.00 (Reject) | Comparable in scope but less theoretical depth. Our paper provides stronger mechanistic analysis. |
| `/home/wg25r/review_agent/human_reviews_2026/UFwgg44VZq.md` (ReTabAD, tabular AD benchmark) | 5.50 (Accept Poster) | Stronger in clarity of contribution (clear benchmark contribution). Our paper is more ambitious but the central claim is less cleanly substantiated. |
| `/home/wg25r/review_agent/human_reviews_2026/Eu25AOvORb.md` (UniOD, universal OD) | 6.00 (Accept Poster) | Stronger theoretical contribution and cleaner experimental design. Our paper is weaker on operationalizing its core definition. |
| `/home/wg25r/review_agent/human_reviews_2026/nCsF3Bsn2n.md` (kernel method, unrelated topic) | 8.00 (Oral) | Different topic, very high score for clean theoretical + empirical contribution. Not comparable in domain. |
| `/home/wg25r/review_agent/human_reviews_2026/wunWpzNKfl.md` (AGNI, tabular AD) | 3.00 (Withdrawn/Reject) | Weaker overall: narrower method proposal without the analytical depth of this paper. |

**Final assessment:** The paper has a strong empirical core and interesting theoretical/analytical contributions, but the central framing overstates what is demonstrated. The headline claim about the "counterintuitive phenomenon" relies on a definition that is never directly operationalized, and the relationship to the original likelihood-inversion literature is not adequately resolved. The empirical finding that NF-SLT outperforms 12 baselines on a full ADBench benchmark is genuine and valuable, and the intrinsic dimension analysis provides a concrete explanation. The paper sits between a sound empirical contribution that would benefit from reframing and a more ambitious conceptual contribution that is incompletely tested. Relative to the anchors, this is stronger than the typical rejected tabular AD papers (3-4 range) but has a gap in its central claim that prevents it from reaching the cleaner contributions scoring 6+.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>