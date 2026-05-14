Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper investigates whether the "counterintuitive phenomenon" — where deep generative models assign higher likelihood to OOD/anomalous data than to in-distribution data — occurs in tabular anomaly detection as it does in image domains. The authors: (1) propose a domain-agnostic formal definition of the phenomenon based on relative AUROC performance against comparison models; (2) conduct a large-scale empirical study across all 47 tabular and 10 CV/NLP embedding datasets from ADBench, benchmarking NF-SLT (NICE flow + simple likelihood test) against 12 baselines; and (3) offer explanatory analysis linking the phenomenon's rarity in tabular data to lower dimensionality and weaker feature correlation, quantified via intrinsic dimension estimation. The central finding is that NF-SLT achieves the highest average AUROC (0.8575), best average rank (3.43), and a fail ratio of only 0.02, convincingly demonstrating that the counterintuitive phenomenon is rare in tabular settings.

## Strengths

- **Comprehensive empirical demonstration (Table 1):** The evaluation across all 47 tabular and 10 CV/NLP embedding datasets from ADBench, with no selection bias, compared against 12 shallow and deep baselines, is thorough and convincing. NF-SLT achieves highest AUROC (0.8575), AUPRC (0.6398), best average rank (3.43), highest Top2 Ratio (0.45), and lowest fail ratio (0.02). The use of 10 repeated experiments per dataset and per-hyperparameter combination adds statistical rigor.

- **Intrinsic dimension analysis for feature correlation (Section 5.2, Figure 1, Table 4):** The quantification of overall feature correlation via the ratio of intrinsic dimension to ambient dimension (_d_ Ratio) is a genuinely novel empirical contribution. The paper demonstrates that tabular datasets have _d_ Ratio values substantially higher than image datasets (e.g., landsat at ~0.39 vs. CIFAR-10 at ~0.003), and shows that NF-SLT tends to underperform on tabular datasets with very low _d_ Ratio. The synthetic Gaussian experiments (Figure 1, left/center) elegantly validate the correlation-ID relationship.

- **Domain-agnostic definition (Definition 3.3):** The formalization of the counterintuitive phenomenon requiring both a proportion _β_ of comparison models to outperform the generative model and a minimum AUROC gap _γ_ is a conceptual advance. It moves beyond vague prior characterizations (e.g., mere likelihood overlap) and enables consistent cross-domain evaluation. The definition is applied qualitatively to interpret the results — e.g., the "yeast" dataset's 0.02 gap fails the second condition.

- **Robustness across data types:** Appendix E demonstrates strong NF-SLT performance across clustered, global, and dependency anomaly types and on categorical-feature-heavy datasets (InternetAds, campaign, census, nsl-kdd), confirming general applicability beyond continuous-feature settings.

- **Practical message clearly communicated:** The paper delivers an actionable finding: a simple NICE flow with a likelihood test is a reliable, practical approach for tabular anomaly detection, outperforming many specialized baselines without requiring complex architectural modifications.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical analysis rests on unverified assumptions (Theorem 5.4, Corollary 5.6):** The dimensionality explanation assumes feature-wise independence and an entropy–KL condition H(P) − H(Q) > DKL(Q||P). Neither condition is verified on real tabular or image data in the paper. The theorem demonstrates that *if* these conditions hold, dimension exacerbates likelihood inversion, but it does not establish that real tabular data inherently satisfy or avoid them. The paper acknowledges the independence limitation for the resize experiment (Section 5.1: "the theorem presented in Appendix D cannot be applied"), but this candor also exposes the gap between the theory and the empirical claims. The theoretical contribution provides a plausible mechanism rather than a validated explanation.

- **Flow architecture limited to NICE and RealNVP:** The main experiments use only NICE, and Appendix G shows RealNVP underperforms NICE slightly (AUROC 0.8480 vs. 0.8575). The paper's title and claims refer to "normalizing flows" broadly, but only two volume-preserving or affine coupling architectures are tested. More expressive flows (e.g., neural spline flows, residual flows) are not evaluated. While the paper acknowledges this in the conclusion as future work, the generalization claim is somewhat overbroad given the evidence. That said, the RealNVP result does mitigate the concern somewhat — it shows NICE is not a singular outlier.

### Minor

- **Definition 3.3 is not operationally instantiated with concrete thresholds:** The paper never specifies explicit values for _β_ or _γ_. The empirical analysis instead relies on the "fail ratio" heuristic (rank ≥ 9 out of 13) and a per-dataset example (yeast, gap = 0.02) to implicitly argue the definition's conditions are unmet. The definition serves its conceptual purpose adequately — the heuristic and gap analysis clearly show the phenomenon is rare — but a more rigorous instantiation would strengthen the paper's formal contribution.

- **Correlation analysis is correlational, not causal (Section 5.2):** The observation that low _d_ Ratio correlates with worse NF-SLT performance is well-supported, but the paper does not manipulate correlation experimentally (e.g., by adding synthetic correlated features to tabular data) to test whether the phenomenon then emerges. The paper's language is appropriately cautious ("we conclude that one factor behind..."), so this is a limitation of scope rather than an overclaim.

- **Dimensionality-reduction experiments conflate effects (Table 3):** The resize experiment acknowledges that bilinear interpolation strengthens pixel correlation while reducing dimension, so dimension and correlation effects are confounded. The paper candidly notes this (Section 5.1: "it is difficult to confirm the effect of dimension on AUROC through the methodology"), but the experiment provides limited independent support for the dimensionality hypothesis.

### Trivial

- The parser-extracted tables (Tables 2, 3, 5, 6 in the review copy) show identical values across all dimension columns. This is a PDF extraction artifact, not an author error, but it makes verification of the claimed dimension-AUROC trends impossible from this copy. The paper text describes the trends clearly.

- The phrase "counterintuitive phenomenon of likelihood" is used as the paper's central concept but is somewhat awkward; "likelihood inversion" or "likelihood paradox" are more standard terms.

## Nice-to-Haves

- A direct manipulation experiment altering feature correlation in tabular data (e.g., injecting synthetic correlated features) to test whether the counterintuitive phenomenon emerges would strengthen the causal claim.
- Testing more expressive modern flow architectures (spline flows, residual flows) would broaden confidence in the "normalizing flows" generalization.
- Side-by-side log-likelihood distribution plots comparing a tabular vs. image OOD pair would provide intuitive illustration of the phenomenon's domain dependence.
- A practical diagnostic tool predicting, from dimension and _d_ Ratio, when a dataset is at risk of likelihood inversion would be a valuable practitioner takeaway.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Table 2 appears to duplicate identical numbers across all column headers, making it impossible to verify the claimed trend"** — This is a PDF parser artifact. The original submission has distinct values per column; the parser simply failed to extract them. The text (Section 5.1, lines 427-432) describes the trends clearly, and the appendix provides additional tables (Tables 5-6) with independent verification. Removed as a parser issue, not an author error.

- **"The theorem only shows that if the condition holds... it does not demonstrate that tabular data inherently avoid this condition"** — Partially retained (major weakness) but softened, since the paper is transparent about its assumptions and does not claim the theorem directly applies to real tabular data.

- **"The paper does not test any modern, expressive flow"** — Retained as a major weakness, but softened since RealNVP is in fact tested in Appendix G and the paper frames this as a first demonstration rather than a comprehensive architecture survey.

- **"No experiment manipulates correlation in tabular data"** — Retained as minor weakness, since the paper uses appropriately cautious language and does not claim causality.

- **"The definition is decorative and does not drive the paper's claims"** — Removed. The definition is applied qualitatively: the fail ratio and yeast gap analysis directly operationalize its two conditions, and the text explicitly links Table 1 results back to Definition 3.3. The definition provides the conceptual framework for the entire empirical evaluation.

## Novel Insights

The most genuinely novel insight from this paper is the use of intrinsic dimension ratio (_d_ Ratio) as a quantitative bridge between the abstract concept of "feature correlation" and the empirical success/failure of likelihood-based anomaly detection. The demonstration that tabular datasets cluster near the identity line in log-scale ambient-vs-intrinsic dimension plots (Figure 1, right), while image datasets are far displaced, provides an elegant, measurable explanation for why the counterintuitive phenomenon is domain-dependent. The observation that even within tabular data, NF-SLT performance degrades on low-_d_ Ratio datasets (Table 4, bottom) suggests a continuum rather than a binary domain split, which is a subtle but important refinement of the paper's own narrative.

## Suggestions

- **Operationalize Definition 3.3 concretely:** Choose specific β and γ values (e.g., β = 0.5, γ = 0.05) and report per-dataset occurrence in a table. This would make the definition falsifiable and strengthen the formal contribution.
- **Add a synthetic correlation manipulation:** Even a simple experiment adding correlated Gaussian features to an existing tabular dataset and observing whether the counterintuitive phenomenon emerges would substantially strengthen the causal argument.
- **Tone down the "normalizing flows" generalization** in the title/abstract to reflect that only NICE and RealNVP are evaluated. "Likelihood-based detection with volume-preserving flows" would be more precise.
- **Move the typicality test comparison (Appendix H) to the main paper**, as it directly addresses an alternative explanation for NF-SLT's success and strengthens the paper's argument.

## Score and Decision

**Originality:** The paper is original in its large-scale empirical investigation of a known image-domain phenomenon in the tabular setting, its formal definition, and its intrinsic-dimension-based explanatory framework. The combination of comprehensive benchmarking with explanatory analysis is novel.

**Importance:** Understanding when and why likelihood-based anomaly detection fails is a practically important question. The finding that simple NICE works well on tabular AD provides actionable guidance.

**Claims supported:** The core empirical claim (the phenomenon is rare in tabular data) is well-supported by Table 1. The theoretical explanation is plausible but not rigorously validated. Claims are generally appropriately scoped.

**Soundness:** Experimental methodology is sound — comprehensive dataset coverage, hyperparameter tuning, 10-repeat experiments, multiple baselines. The theoretical analysis has acknowledged limitations.

**Clarity:** The paper is well-structured and the narrative is clear. Some theoretical sections are dense but intelligible.

**Value to community:** High. Practitioners gain confidence in using simple flow-based detection for tabular AD. Researchers gain the intrinsic dimension ratio as a diagnostic tool and the formal definition as a framework for future comparisons.

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `XOPH34Extq` (TabStruct) | 7.00 (Accept Oral) | Stronger: more polished benchmark contribution with novel evaluation metric and broader generator coverage |
| `UFwgg44VZq` (ReTabAD) | 5.50 (Accept Poster) | Comparable scale; this paper has stronger empirical findings and theoretical analysis |
| `jCQVjd4vrX` (Likelihood Paradox) | 4.00 (Reject) | Same topic area; this paper has much stronger empirical grounding and clearer contribution |
| `JdbqDiguyO` (NRDE) | 3.33 (Reject) | Both use normalizing flows for tabular AD; this paper has more comprehensive experiments and clearer claims |
| `0eEtTsnmyo` (USF) | 4.00 (Reject) | Both connect theory to normalizing flows for AD; this paper has substantially stronger empirical validation |
| `73QNa7rAgm` (TCAD) | 4.00 (Reject) | Tabular AD method; this paper's empirical scope (47 datasets, 12 baselines) is broader |
| `jbGGPSI9aO` (AdaSCALE) | 4.67 (Reject) | OOD detection method; this paper provides stronger benchmarking |

The paper under review sits clearly above the 4.0-range rejects. It has a solid empirical contribution comparable to accepted poster-level work, with a more comprehensive benchmark than ReTabAD (5.50) but without the theoretical polish of TabStruct (7.00). The theoretical limitations and narrow flow architecture evaluation prevent an oral-level score, but the empirical contribution and novel intrinsic dimension analysis merit acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>