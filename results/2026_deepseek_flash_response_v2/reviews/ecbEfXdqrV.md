Now let me write the final consolidated review with the score and decision.

**Calibration Report:**

**Round 1 (Bracketing):**
- Low band (< 3.5): Papers like "Normalizing Flows For OOD Detection" (3.40), "Dealing with OOD in Prediction" (2.50) — clearly weaker than current paper
- Middle band (3.5–7.5): "Anomaly Detection by Estimating Gradients" (5.75), "Explaining the OOD Detection Paradox" (5.67), "AnoLLM" (6.75), "PTAD" (4.25) — current paper sits in this range
- High band (> 7.5): "Deep Orthogonal Hypersphere Compression" (8.00), "Latent Bayesian Optimization" (8.00) — clearly stronger

**Round 2 (Narrowing within 4.5–7.5):**
- "Explaining the OOD Detection Paradox through Likelihood Peaks" (5.67, Reject) — same phenomenon, but only 8 image pairs. Current paper is stronger (47 datasets, comprehensive).
- "DRL" (5.75, Accept) — novel method for tabular AD, 40 datasets. Current paper comparable but different contribution type.
- "MCM" (6.67, Accept) — novel method, 20 datasets, clean experiments. Current paper is weaker as an analysis paper with framing issues.
- "AnoLLM" (6.75, Accept) — novel LLM method, accepted. Current paper has less novelty.

**Final position:** Between 5.75 (DRL) and 6.67 (MCM). The paper's comprehensive evaluation and interesting analytic findings place it above DRL; its framing mismatch, unclear hyperparameter protocol, and absence of variance reporting place it below MCM.

---

## Summary

This paper investigates why the "counterintuitive phenomenon" (where deep generative models assign higher likelihoods to anomalous/OOD data than to in-distribution data, as observed in images) is rare in tabular anomaly detection. The authors propose a domain-agnostic formal definition of the phenomenon based on relative AUROC performance (Definition 3.3), then conduct extensive experiments on all 47 ADBench tabular datasets + 10 CV/NLP embedding datasets, comparing NF-SLT (normalizing flow with simple likelihood test) against 12 baselines with 10 repeated runs. NF-SLT achieves the best average AUROC (0.8575), best average rank (3.43), and lowest fail ratio (0.02). The paper further provides theoretical analysis (Theorem 5.4 linking dimensionality to likelihood gap) and empirical feature correlation analysis (via intrinsic dimension ratio) to explain why tabular data differs from images.

## Strengths

1. **Comprehensive, selection-bias-free evaluation across the full ADBench benchmark (Section 4, Table 1).** The paper uses all 47 tabular datasets and 10 embedding datasets without exclusion, comparing against 12 baselines. NF-SLT's AUROC 0.8575 (vs. next-best ICL at 0.8208), Top2 Ratio 0.45 (vs. ICL at 0.32), and Fail Ratio 0.02 (an order of magnitude below all competitors) provide strong evidence that simple likelihood-based detection is effective on tabular data. This directly addresses Shwartz-Ziv & Armon (2022)'s criticism of dataset cherry-picking.

2. **Formal operationalization of the counterintuitive phenomenon (Definition 3.3, Section 3).** Prior work described the phenomenon only qualitatively. The authors provide a quantitative definition with two conditions (proportion of outperforming baselines exceeds β, minimum performance gap exceeds γ), enabling consistent cross-domain comparison. The definition is validated against the known CIFAR-10-vs-SVHN case (AUROC 6.4% vs. comparison models >90%).

3. **Theoretical result linking dimensionality to likelihood gap (Theorem 5.4, Corollary 5.6, Section 5.1).** The paper extends Caterini & Loaiza-Ganem (2022)'s likelihood-gap expression and proves that under independence, when H(P) - H(Q) > D_KL(Q||P), the expected likelihood gap's lower bound decreases linearly with dimension d, and the AUROC upper bound is inversely related to d. This provides formal grounding for the intuition that lower-dimensional tabular data is less susceptible to likelihood inversion.

4. **Controlled dimensionality-reduction experiments validating the theory (Table 2, Section 5.1).** Using ICA to reduce image dimensionality, the paper shows AUROC systematically improves as dimension decreases when H(P) > H(Q) (e.g., CIFAR-100/SVHN from 0.0843 at 1024 dims to 0.3490 at 30 dims). This isolates the effect of dimensionality from architectural changes, providing clean empirical support.

5. **Feature correlation analysis via intrinsic dimension ratio (Section 5.2, Table 4, Figure 1).** The paper introduces the d Ratio (intrinsic/ambient dimension) as a proxy for overall feature correlation, shows image datasets have d Ratio ~0.002–0.019 while tabular datasets have much higher values (e.g., waveform at 0.810), and demonstrates a monotonic relationship between d Ratio threshold and NF-SLT success rate. The controlled Gaussian toy experiment convincingly establishes that stronger correlation reduces estimated ID.

## Weaknesses

### Major

- **Hyperparameter selection protocol is unusual, ambiguously described, and potentially biasing (Section 4, line 122).** The paper states: "For each dataset, after experimenting with all combinations in the hyperparameter searching space with 10 repeated experiments, the hyperparameter combination with the highest average AUROC for all datasets is selected." The phrasing is ambiguous — it is unclear whether hyperparameters are selected per-dataset (contradicted by "highest average AUROC for all datasets") or globally. A global selection that maximizes average AUROC across all datasets could advantage models whose performance is more robust across diverse distributions rather than models that are simply better. The hyperparameter sensitivity analysis is relegated to Appendix F (stripped by the parser), so the main text does not demonstrate robustness to this choice. This is the paper's most significant methodological concern and warrants careful clarification.

### Minor

- **Framing mismatch between the paper's title/abstract and Definition 3.3.** The title and abstract refer to the "counterintuitive phenomenon of likelihood" (the Nalisnick et al. observation that OOD data receives higher likelihood), but Definition 3.3 operationalizes it as relative AUROC underperformance. As the paper acknowledges (lines 25–27), likelihood inversion can arise from dataset difficulty rather than the phenomenon itself. However, the converse is also true: a model could exhibit genuine likelihood inversion (anomalies scoring higher on average) yet still achieve reasonable AUROC because AUROC measures separability, not correctness of direction. The definition cannot distinguish these cases. The paper's positive finding (NF-SLT works well on tabular data) is valuable independently, but the specific claim about the "counterintuitive phenomenon of likelihood" is not directly measured — it is inferred from relative AUROC rankings.

- **No variance/confidence intervals reported for Table 1 despite 10 repeated runs.** The paper reports only averages for AUROC and AUPRC. Without standard deviations or confidence intervals, the reader cannot assess whether NF-SLT's advantage over ICL (0.8575 vs. 0.8208) or NeuTraLAD (0.8081) is statistically significant.

- **Theorem 5.4 assumes independence, limiting its explanatory scope for real correlated data.** The theorem requires P and Q to be product distributions over independent dimensions. The paper acknowledges this (line 164) for the image resize experiments. However, the theorem is invoked more broadly to explain why tabular data avoids the phenomenon. Real tabular data has correlations, so the theorem does not directly explain the empirical results without additional justification about why the independence approximation is reasonable.

- **Limited explanation for why only 6 of 13 models were compared on CV/NLP embedding datasets (Table 1 bottom).** The shallow models (PCA, LOF, IF, OCSVM, COPOD, ECOD) and DAGMM are excluded without explicit justification. Since these embeddings are part of the empirical support, the omission should be explained.

- **β and γ thresholds in Definition 3.3 are not specified in the main text.** The paper states the full formulation is in Appendix B (stripped). The main text should state the chosen values and ideally include a sensitivity analysis. The discussions of 'yeast' (gap 0.02) and 'imdb' ("very small" gap) reference these thresholds implicitly without connecting them to formal γ values.

### Trivial

- Table 1 would benefit from a note explaining why fewer models are used for embedding datasets vs. tabular datasets.

## Nice-to-Haves

- Direct measurement of likelihood inversion (e.g., what fraction of anomalies receive higher likelihood than the median normal sample) would connect the findings more directly to the original Nalisnick et al. phenomenon and resolve the framing mismatch.
- Reporting full d Ratio results for all 47 ADBench datasets (not just the 4 shown in Table 4) would strengthen the feature correlation analysis.
- A sensitivity analysis comparing global hyperparameter selection vs. per-dataset tuning vs. fixed defaults would address concerns about evaluation fairness.

## Removed Points

- **β/γ thresholds as a "critical issue":** The harsh critic's claim that thresholds are "never specified" is softened — they are referenced in the paper's reference to Appendix B (stripped by parser). The point about main-text specification is retained as a Minor weakness rather than a critical issue.
- **CIFAR-10-vs-SVHN "not apples-to-apples":** Removed — the paper uses this only as an illustrative example of Definition 3.3, not as a controlled experiment.
- **"Reframe the paper" suggestion:** Moved to Nice-to-Haves as a stylistic framing suggestion rather than a concrete weakness.
- **Theorem 5.4 as "tenuous" with "contradictory" empirical results:** The critic overstated this. The paper acknowledges the independence limitation and reports results that are "conflicting with the theorems" in the interpolation case (which is explicitly discussed as testing the no-independence scenario). Retained as Minor (independence limits scope), not as a structural flaw.
- **Generic "evaluation lacks rigor" type complaints** from the critics: Removed because they lack concrete anchors. Only specific, verifiable concerns are retained.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem"): Removed. Only specific, evidence-grounded strengths are kept.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the hyperparameter selection protocol** in the main text: state explicitly whether hyperparameters are selected per-dataset or globally, and include a sensitivity analysis showing results are robust to this choice.
2. **Add standard deviations or confidence intervals** to Table 1 to enable assessment of statistical significance.
3. **Specify the β and γ values** used in Definition 3.3 in the main text and include a robustness check showing the conclusion holds across reasonable threshold choices.
4. **Explain why only 6 models** were compared on the CV/NLP embedding datasets.
5. **Consider adding a direct measure of likelihood inversion** (e.g., fraction of anomalies with likelihood above the median normal likelihood) to supplement the relative AUROC-based definition, bridging the gap to the original Nalisnick et al. phenomenon.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 6Z8rZlKpNT.md (NF for OOD) | 3.40 | R1 | Weaker — narrower scope, less comprehensive eval |
| i28ZjVxl81.md (OOD in Prediction) | 2.50 | R1 | Much weaker — limited experiments |
| rcmhydaEJp.md (Flow Imputation) | 3.00 | R1 | Weaker — different task, small data |
| 3qDhqj6qfu.md (TabKANet) | 3.00 | R1 | Weaker — different approach, classification |
| 7QDIFrtAsB.md (NCSN Gradients) | 5.75 | R1,R2 | Similar domain, rejected for novelty/fairness; current paper has less severe fairness issues |
| jQ596tXT3k.md (OOD Paradox) | 5.67 | R1,R2 | Most topically similar; current paper stronger (47 datasets vs 8 pairs) |
| 7VkHffT5X2.md (AnoLLM) | 6.75 | R1,R2 | Stronger novelty (LLM method); current paper slightly weaker |
| Vi6p2TeujL.md (PTAD) | 4.25 | R1 | Weaker — less comprehensive |
| cJs4oE4m9Q.md (Orthogonal Hypersphere) | 8.00 | R1 | Clearly stronger — novel method, strong results |
| ZCOwwRAaEl.md (Latent BO) | 8.00 | R1 | Different topic, stronger |
| I5lcjmFmlc.md (Robust Diffusion) | 8.00 | R1 | Different topic, stronger |
| k38Th3x4d9.md (Root Cause Analysis) | 8.00 | R1 | Different topic, stronger |
| CJnceDksRd.md (DRL) | 5.75 | R2 | Similar domain, novel method but theoretical gaps; current paper comparable |
| gRXLa6LS3J.md (FoMo-0D) | 5.75 | R2 | Different approach, similar quality |
| lNZJyEDxy4.md (MCM) | 6.67 | R2 | Stronger as method paper; current paper has more methodological concerns |

Round 1 bracket: Between 3.5 and 7.5. Round 2 narrowed to between 5.75 (DRL) and 6.67 (MCM). The paper's comprehensive evaluation and interesting analytic findings place it above DRL (5.75); its framing mismatch, unclear hyperparameter protocol, and absence of variance reporting place it below MCM (6.67).

**Final Score:** 6.0

**Decision:** Accept

The paper makes a genuine empirical contribution — the comprehensive demonstration that simple likelihood-based anomaly detection with normalizing flows works well across the full ADBench benchmark is novel, non-trivial, and practically useful. The analysis linking this to dimensionality and feature correlation is thoughtful. However, the framing mismatch between the paper's headline claim (about the "counterintuitive phenomenon of likelihood") and the actual operationalization (relative AUROC performance), combined with an unclear hyperparameter selection protocol and absent variance reporting, prevent the paper from being a stronger accept. These issues are addressable with clarifications and additions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>