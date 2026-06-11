## Summary
This paper presents a detailed critical re-analysis of "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024), a high-visibility ICLR 2025 Oral paper. The authors systematically re-examine all four lines of evidence (human evaluations, NLP benchmarks, LLM-as-a-Judge, community adoption) and demonstrate that each fails to support min-p sampling's claimed superiority. The paper also introduces a "Best-of-N" methodology for fair hyperparameter-controlled comparison and derives general lessons for research rigor.

## Strengths
- **Thorough documentation of omitted data (Section 2.1):** The authors identify that one-third of collected human evaluation data (scores for basic sampling) were excluded from the original paper without mention or justification, publicly confirmed with the original authors. Figure 2 shows basic sampling was actually the most preferred by human evaluators (21 evaluators vs. 12 for min-p).
- **Novel Best-of-N methodology for fair hyperparameter-controlled comparison (Section 3.1):** The subsampling-based method (repeated 150 times) that equalizes hyperparameter search volume before comparing peak performance is a genuinely useful methodological contribution applicable beyond this case study. Supported by ~6,000 A100-hours across 9 models, 4 samplers, and extensive hyperparameter grids (Figures 4–5).
- **Rigorous statistical re-analysis with proper corrections (Section 2.2, Table 1):** Conducts 12 one-sided paired t-tests, applies Bonferroni correction, and additionally applies an Intersection-Union Test appropriate for the "consistently outperforms" claim. After correction, only 1 of 12 comparisons remains significant, directly contradicting the original paper's single pooled t-test.
- **Documentation of selective reporting in LLM-as-a-Judge (Section 4.3):** A specific, verifiable instance where Table 3(b) reported the higher of two min-p scores (52.01 for p=0.05) but the lower of two top-p scores (50.07 for p=0.9), with data available from a public GitHub repository (Figure 6).
- **Exposure of unsubstantiated community adoption claims and their influence on peer review (Section 5):** The claimed "54,000 GitHub repositories" and "1.1 million stars" were retracted by the original authors. Critically, 3 of 4 ICLR reviewers cited these retracted numbers as their main justification for strong endorsement — a striking meta-level finding about how unverified claims can corrupt peer review.

## Weaknesses

### Fatal
None

### Major
- **Single-benchmark limitation of hyperparameter sweeps (Section 3.1):** The Best-of-N analysis — the paper's most novel methodological contribution — was conducted only on GSM8K CoT, despite the original paper also evaluating on GPQA. Line 150 states "Due to our compute budget, we only evaluated GSM8K CoT." If min-p were superior on GPQA, the general conclusion "samplers perform approximately equally when given equal hyperparameter tuning" would be weakened. The authors acknowledge this but present the GSM8K results as settling the question more than the evidence warrants.

- **"Blueprint" framing overstates the contribution's generality:** The paper claims to provide "a blueprint for conducting more meticulous science" (abstract) and lists six general lessons (Section 6) that are sound but well-established best practices. The genuine contribution is the demonstration of these principles in a high-stakes real-world case study, plus the Best-of-N methodology. Repositioning as "a detailed case study in research rigor" would be more honest and, paradoxically, more impactful, because the specificity of the case is what makes it compelling.

### Minor
- **Inconsistent statistical language — conflation of "not proven better" with "proven not better":** The paper correctly states "insufficient evidence to support the claim that min-p consistently outperforms" (Table 1 caption), but elsewhere uses stronger language: "min-p is largely indistinguishable from other samplers" (lines 23, 165), "min-p offers no apparent advantage" (lines 112, 117). Failing to reject the null is not the same as demonstrating equivalence, which is inconsistent with the paper's own stated commitment to statistical rigor.

- **Qualitative annotation without blinding (Section 2.3):** The authors manually annotated human evaluators' qualitative preferences themselves without blinded annotation or inter-annotator reliability (e.g., Cohen's κ). For a paper whose central argument is about rigor, this is a notable gap — the coding of preferences involves subjective judgment. The authors did publicly post their annotations, which partially mitigates this.

- **Selective reporting evidence relies partly on informal channels (Section 4.3):** The primary evidence is a "Telegram link" shared by the original paper's first author (line 193). While the data is also available from a public GitHub repository (Figure 6 caption), the paper would benefit from providing reproducible code showing which hyperparameter configurations yield which scores, rather than leaning on the informal channel.

### Trivial
None

## Nice-to-Haves
- A sensitivity analysis of the Best-of-N methodology — how robust are results to hyperparameter grid composition, subsample size, and number of repetitions?
- More explicit discussion of practical implications: does the finding that samplers perform equally with equal tuning mean practitioners should prefer basic sampling (no tuning needed)?
- Use equivalence testing (e.g., TOST) rather than just "fail to reject null" when claiming samplers are "indistinguishable."
- Acknowledge that the Best-of-N analysis may understate basic sampling's practical appeal since basic has no hyperparameters beyond temperature — not needing tuning is itself an advantage.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh Critic's concern about basic sampling having fewer hyperparameters as a fairness issue: The paper explicitly acknowledges this at lines 133–134 ("Basic sampling has only a temperature hyperparameter, and is thus swept to a lesser extent") and the Best-of-N methodology already controls for this by subsampling equal numbers of hyperparameters.

## Novel Insights
The paper's genuinely novel contribution is the "Best-of-N" subsampling methodology (Section 3.1) for fair comparison under unequal hyperparameter tuning — a pervasive but under-addressed problem in empirical ML evaluation. The repeated subsampling approach (150 repetitions) provides a statistically grounded way to equalize hyperparameter search volume. The meta-level finding that 3 of 4 ICLR reviewers cited subsequently-retracted community adoption numbers as their main justification is also a genuinely novel and important observation about how unverified claims can corrupt peer review.

## Suggestions
- Reposition the paper as "a detailed case study in research rigor" rather than "a blueprint" — the case study is the real contribution.
- Add a brief formal treatment of the Best-of-N methodology: assumptions, sensitivity analysis, guidance on choosing N.
- Use equivalence testing (e.g., TOST) when claiming samplers are "indistinguishable."
- Add blinded annotation or compute inter-annotator agreement for Section 2.3 qualitative coding.
- More explicitly acknowledge the single-benchmark limitation when stating general conclusions.

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| nSDOkm0SKo.md | 1.00 | 1 | Completely unrelated financial/NN paper |
| Uj0h13lVrR.md | 1.00 | 1 | GFlowNets paper with fundamental flaws |
| P49gSPmrvN.md | 1.00 | 1 | UMAP visualization paper, no rigor |
| 8QTpYC4smR.md | 1.00 | 1 | Generic LLM survey, no contribution |
| qcyn7ESaM8.md | 2.50 | 1 | PCA/NN class bias, weak claims |
| 1gqR7yEqnP.md | 2.20 | 1 | "Pan for gold" paper, overclaimed |
| hv8l922Ad7.md | 3.40 | 1 | Correcting disentanglement metrics; similar theme but much less thorough |
| GbEmJmnQCz.md | 4.40 | 1 | "Is Memorization Necessary" re-analysis; closest comparator but less thorough |
| lf8QQ2KMgv.md | 3.75 | 1 | Same re-analysis paper, different reviews |
| kiwyQsZIGP.md | 5.00 | 1 | "Evaluating the Evaluators"; evaluation critique, less impactful |
| X8XQOLjLX6.md | 4.50 | 1 | Autoencoders unreliable; overgeneralized conclusion |
| GlPVnuL66V.md | 6.00 | 1 | Provable privacy attacks; different topic |
| RW37MMrNAi.md | 5.60 | 1 | Class-wise autoencoders; different topic |
| g16vmAtJ8x.md | 6.00 | 1 | Privacy metrics critique; shows existing metrics flawed |
| 20oxNYWQl9.md | 5.75 | 1 | Sensitivity sampling; different topic |
| EUSkm2sVJ6.md | 7.60 | 2 | "How much of my dataset"; novel methodology |
| h8yg0hT96f.md | 7.33 | 2 | Bayesian experimental design; novel method |
| uqWM9hBDAE.md | 7.33 | 2 | "How Much is Unseen"; theoretical contribution |
| vi3DjUhFVm.md | 7.25 | 2 | Diffusion alignment; different topic |
| Q2bJ2qgcP1.md | 6.00 | 2 | CATE benchmark showing methods fail; closest comparator, accepted at 6.0 |
| icTZCUbtD6.md | 6.20 | 2 | "Dissecting Sample Hardness"; analysis/benchmark paper |
| K9zedJlybd.md | 6.00 | 2 | Implicit degree bias in link prediction; shows benchmark is flawed |
| JnRStoIuTe.md | 5.20 | 1 | Repeated random sampling; different topic |
| juZNRYRMPn.md | 4.75 | 1 | Truth-guided negative sampling; different topic |
| n7qGCmluZr.md | 6.00 | 2 | PQMass probabilistic assessment; different topic |
| yQUbpAHbIZ.md | 6.00 | 2 | Post-nonlinear causal; different topic |
| ZQ9SF5eUHZ.md | 5.67 | 2 | Dynamic data pruning; different topic |

**Round 1 Bracket:** 5.5–7.5. The paper is substantially more thorough than re-analysis papers in the 3.75–5.0 range ("Is Memorization Necessary" at 3.75–4.40, "Correcting Flaws" at 3.40), with ~6000 A100-hours of compute, a novel Best-of-N methodology, and concrete verifiable findings including retracted claims. It is comparable to the CATE benchmark paper (6.0, Accept) which also showed methods fail through extensive experimentation.

**Round 2 Narrowing:** 6.0–7.0. The paper has more novel methodology and more concrete findings than the CATE paper (6.0), but its narrower focus (one paper vs. a class of methods) and framing issues prevent it from reaching 7.0+. **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>