---

## Summary

This paper re-examines the robustness of Chinchilla's compute-optimal scaling laws to parameter-count ambiguity. The authors uncover that three different interpretations of model parameters are possible from Chinchilla's Table A9 (reported, standard-formula, and best-fit), with discrepancies up to 15.2%. They show that key Chinchilla results—the fitted scaling-law parameters and the ~20-to-1 tokens-per-parameter ratio—are robust to which interpretation is used. They then conduct a systematic perturbation analysis, injecting four types of structured errors (multiplicative, additive, systematic bias, log-normal noise) into the parameter counts and re-running the Chinchilla fitting pipeline. The analysis reveals that robustness depends on perturbation type: multiplicative and noise perturbations preserve the flat trend of the optimal ratio, while additive and systematic perturbations can alter it. The paper contributes a careful sensitivity analysis that clarifies which parameter-count errors matter and which do not.

## Strengths

- **Discovery of parameter-count ambiguity and demonstration of robustness (Section 2):** The paper identifies that Chinchilla's Table A9 supports three distinct parameter-count interpretations with up to 15.2% relative error (Figure 1), then shows through refitting that all three yield essentially unchanged scaling-law coefficients and a constant ~20-to-1 tokens-per-parameter ratio (Figure 2). This is a concrete, well-validated finding that directly addresses a known source of uncertainty in the scaling-law literature.

- **Systematic perturbation framework (Section 3):** The four perturbation types—multiplicative, additive, systematic bias, and log-normal noise—are well-motivated and clearly defined (Equations 6–9, Figure 3). Re-running the full Chinchilla fitting pipeline under each perturbation and mapping the resulting fit parameters (Figure 4) and optimal ratios (Figure 5) provides a comprehensive stress test that quantifies robustness boundaries rather than merely asserting them.

- **Analytical derivations that explain observed trends:** The paper provides theoretical derivations (referenced to Appendix C, summarized in main text) that predict how each perturbation type affects the fit parameters—for instance, that an additive constant causes $\hat{\alpha}$ to increase linearly and $\hat{A}$ to grow exponentially (Section 3.2), matching the empirical observations in Figure 4. This adds explanatory depth beyond pure empirical reporting.

- **Connection to real-world discrepancies:** The paper explicitly links its additive-perturbation results to the findings of Porian et al. (2024) and Pearce & Song (2024) on embedding-parameter inclusion/exclusion (Section 3.2), validating that the perturbation framework captures meaningful sensitivity relevant to prior scaling-law debates.

- **Reproducibility via open-source code:** All refitting uses the open-source code from Besiroglu et al. (2024), making the analysis straightforward to replicate.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Framing slightly overstates robustness relative to the nuanced findings:** The abstract and discussion use language like "renewed confidence" and "durable guide," and the contribution is framed as a "powerful confirmation" (Section 5). While the paper *is* transparent that additive and systematic perturbations can qualitatively change the trend of the optimal ratio (the abstract, Section 1, and Section 3.2 all explicitly acknowledge this), the overall narrative could be more carefully calibrated. A reader who skims only the abstract and conclusion might miss that two of the four perturbation types break the constancy of the ratio—the very property the paper sets out to defend. The conclusions would be stronger if they directly stated: multiplicative errors and noise do not disrupt the key scaling relationships, but additive and systematic errors *can*, and this matters because additive offsets correspond to known embedding-parameter reporting differences. This is a framing issue, not a methodological flaw; the underlying evidence is honestly presented.

- **Choice of standard-formula parameters as the perturbation baseline is not justified:** Section 3 perturbs the standard-formula model parameters without explaining why these—rather than the reported or best-fit parameters—serve as the anchor for the stress test. Given that Section 2 shows all three interpretations are equivalent for the key results, this choice is defensible, but a brief justification would strengthen the link between the perturbation study and the real-world ambiguity that motivated it.

### Trivial

- **Scope not explicitly bounded:** The paper tests robustness only along one dimension (model-parameter counts). Other potential sources of fragility—loss-measurement noise, scaling-law functional form, optimizer details—are not tested, which is reasonable for a focused paper, but a brief statement acknowledging this scope boundary would prevent any impression of overbreadth. The future-directions paragraph hints at this but does not explicitly say what the current paper does *not* cover.

## Nice-to-Haves

- Mapping the additive-perturbation parameter $c_a$ more directly onto real-world embedding-inclusion differences (e.g., showing the resulting trend for the specific parameter-count differences between the three interpretations from Section 2) would strengthen the practical relevance of the perturbation framework, though it is not strictly required.

- The paper could strengthen its contribution by framing itself as a diagnostic—clarifying *which kinds* of parameter-count errors are benign and which are consequential—rather than as a blanket confirmation. This reframing would align the narrative more precisely with the evidence already presented.

## Removed Points

These points were flagged by reviewers but are not included in the main review for the reasons given.

- **"The central claim is inconsistent with its own evidence—the paper promises confirmation it does not deliver" (Harsh Critic):** Removed. The paper explicitly and repeatedly acknowledges that additive and systematic perturbations qualitatively change the trend of the optimal ratio (abstract: "alter the otherwise flat trend"; Section 1: "can qualitatively change the compute-optimal scaling strategy"; Section 3.2: "becomes less constant"). The paper's overall claim that Chinchilla "withstands sizable perturbations" is supported by the evidence: multiplicative and noise perturbations preserve the ratio's flatness, and even under additive/systematic perturbations the ratio remains in a reasonable range for realistic perturbation magnitudes. The harsh critic's assertion of inconsistency misreads the paper's own transparent reporting.

- **"The paper should acknowledge scope" as a major weakness:** Demoted to Trivial and rephrased. The paper's scope is narrow by design; this is not a methodological flaw.

- **Formatting/presentation nitpicks:** None present in the harsh critic or strength finder inputs beyond what's covered above.

## Novel Insights

None beyond the paper's own contributions. The paper's key novel insight is already well-articulated in the work itself: that Chinchilla's parameter-count ambiguity, while real (up to 15.2% discrepancy), does not meaningfully affect the fitted scaling-law coefficients or the compute-optimal ratio. A secondary insight is the structured mapping of *which types* of parameter-count errors affect the constancy of the ratio and which do not—this is a useful diagnostic framework.

## Suggestions

- **Recalibrate the narrative:** Frame the contribution as a diagnostic that distinguishes benign perturbations (multiplicative, noise) from consequential ones (additive, systematic), rather than a blanket confirmation. This would align the conclusions with the evidence without requiring new experiments.

- **Justify the baseline:** Add one sentence in Section 3 explaining why the standard-formula parameters are used as the anchor for the perturbation study (e.g., they are the most natural derivation from the architectural hyperparameters provided in Table A9, and Section 2 demonstrates they produce equivalent results to the other interpretations).

- **Add a brief scope statement:** In Section 5, explicitly note that the analysis covers robustness to parameter-count errors and that robustness to other factors (functional form, optimizer settings, loss noise) remains an open question, previewing the future-directions paragraph.

## Score and Decision

**Calibration summary:**

*Round 1 bracketing* placed the paper between roughly 5.0 and 7.5. The weak-band anchors (avg 3.0) covered unrelated topics and were clearly below this paper. The middle-band anchors included "A Hitchhiker's Guide to Scaling Law Estimation" (5.20) and "PolyPythias" (6.50). The strong-band anchors included "Small-scale proxies for large-scale Transformer training instabilities" (8.00) and "Scaling Laws for Precision" (8.00).

*Round 2 narrowing* pulled anchors in the 4.5–7.5 range. The most comparable anchor is "(Mis)Fitting Scaling Laws: A Survey of Scaling Law Fitting Techniques" (5.75, scores: 5,5,8,5), which surveys scaling-law methodologies and includes a replication study. The paper under review is more focused and executes its core analysis more cleanly than this anchor. "Language models scale reliably with over-training and on downstream tasks" (6.50) trains 104 new models and extends scaling laws to new regimes—more ambitious in scope. "PolyPythias" (6.50) trains 45 new runs and studies training stability—comparable in spirit but trains new models, which this paper does not.

*Anchor comparison:*
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| xGM5shdGJD (Hitchhiker's Guide) | 5.20 | 1 | Paper under review is cleaner and more focused |
| xI71dsS3o4 (MisFitting Scaling Laws) | 5.75 | 2 | Paper under review has a clearer, better-executed contribution |
| bmrYu2Ekdz (PolyPythias) | 6.50 | 1 | Comparable quality; PolyPythias is more resource-intensive (trains models) |
| iZeQBqJamf (LM scale reliably with over-training) | 6.50 | 1 | More ambitious (trains 104 models); our paper is narrower but well-executed |
| d8w0pmvXbZ (Small-scale proxies) | 8.00 | 1 | Clearly stronger—more novel findings, practical guidance, broader ablations |
| wg1PCg3CUP (Scaling Laws for Precision) | 8.00 | 1 | Clearly stronger—extends scaling laws to a new dimension |

The paper is better than the 5.20–5.75 anchors (cleaner execution, more focused contribution). It is comparable in quality to the 6.50 anchors but narrower in scope (no new model training, a single robustness dimension). It is clearly below the 8.00 anchors, which provide broader practical insights and more novel findings. **Score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>