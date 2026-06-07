Now I have enough calibration context. Let me write the final review.

## Summary
This paper investigates whether the "counterintuitive phenomenon" (generative models assigning higher likelihood to anomalous/OOD data than normal data, well-documented in images) occurs in tabular anomaly detection. The authors propose a formal definition (Definition 3.3) based on relative model performance, conduct extensive experiments across all 47 ADBench tabular datasets with 12 baselines showing NF-SLT (normalizing flow with simple likelihood test) achieves top performance (AUROC 0.8575, Fail Ratio 0.02), and provide theoretical/empirical analysis linking the phenomenon's rarity to tabular data's lower dimensionality and weaker feature correlations.

## Strengths
1. **Comprehensive benchmark with no selection bias**: Table 1 evaluates NF-SLT against 12 baselines across all 47 ADBench tabular datasets and 10 embedding datasets, motivated by concerns about selection bias (Shwartz-Ziv & Armon, 2022). NF-SLT achieves AUROC 0.8575 vs. next-best 0.8208 (ICL) and Fail Ratio 0.02 vs. 0.23+, making this the most thorough evaluation of likelihood-based tabular AD to date.

2. **d-Ratio analysis provides a principled quantification of feature correlation**: The intrinsic/ambient dimension ratio (Table 4, Figure 1) convincingly shows tabular data preserves more of its ambient dimensionality (d-Ratio 0.389–0.810) than image data (0.002–0.019), directly connecting feature correlation differences to the observed performance asymmetry. The toy Gaussian experiment (Figure 1, left/center) validates the relationship between correlation strength and ID reduction.

3. **ICA dimensionality reduction experiments validate theoretical predictions**: Table 2 directly tests Theorem 5.4 by reducing image dimensionality via ICA — when ℍ(P) > ℍ(Q), AUROC improves substantially as dimension drops (e.g., CIFAR-100/SVHN: 0.0843 → 0.3490), providing concrete empirical support for the theoretical mechanism.

4. **Honest treatment of conflicting results**: The paper acknowledges that the SVHN→CelebA resize experiment (Table 3) "conflicts with the theorems in Appendix D" (line 176) and offers a plausible explanation (bilinear interpolation strengthening pixel correlations), which strengthens scientific credibility.

## Weaknesses

### Major
1. **Definition-Question Mismatch**: The paper motivates its investigation with the original literature phenomenon (likelihood inversion: OOD data gets higher likelihood than in-distribution data, documented in Nalisnick et al. 2019a, Serrà et al. 2020). However, Definition 3.3 replaces this with a criterion based on relative model ranking — the phenomenon occurs when most comparison models outperform the generative model by a meaningful margin. This conflates two distinct questions. Under Definition 3.3, a model with perfectly ordered likelihoods could be flagged as "counterintuitive" if most baselines outperform it (Scenario A), while a model with genuinely inverted likelihoods (AUROC < 0.5) would NOT be flagged if the baselines are even worse (Scenario B). The paper's central claim — "the counterintuitive phenomenon is rare in tabular data" — may be true under Definition 3.3, but the definition is structured so that a model performing well relative to others cannot, by construction, exhibit the phenomenon. Since NF-SLT achieves the best average AUROC, the conclusion becomes partly tautological. The paper does not directly test whether the original likelihood-inversion phenomenon occurs in tabular data — no analysis of likelihood distributions, no likelihood ratios, no systematic check of how many datasets have AUROC < 0.5. This mismatch between framing and methodology weakens the paper's main narrative.

2. **No per-dataset AUROC results or uncertainty reporting**: Only aggregate metrics (average AUROC, rank, top2/fail ratios) are reported for the 47 tabular datasets in Table 1. Individual dataset AUROC values are not shown, making it impossible to assess the distribution of outcomes — e.g., whether any individual dataset shows genuine likelihood inversion (AUROC << 0.5) even if the average is high. Despite 10 repeated runs, no standard deviations, confidence intervals, or any variance measure are reported, so the statistical significance of performance differences is unknowable.

### Minor
3. **β and γ thresholds deferred to appendix**: The thresholds that operationalize Definition 3.3 (the paper's central definition) are not stated in the main text. The empirical discussion of yeast (gap 0.02) and imdb (gap 0.0385) implicitly relies on these thresholds, but the reader cannot evaluate whether these gaps are meaningful without knowing β and γ. The paper refers to Appendix B for the "fully rigorous formulation" (line 77), but these parameters are central enough to the main argument to require main-text disclosure.

4. **Strong theoretical assumptions**: Theorem 5.4 assumes P and Q are product distributions over independent dimensions — an assumption violated by essentially all real data, including tabular data. Corollary 5.6 requires assumptions about moment scaling (n-th absolute central moment scaling as O(d^k) with k < n) that cannot be verified for real data. These are acknowledged but limit the theory's applicability to real-world settings.

### Trivial
5. **Ambiguous hyperparameter selection description**: Line 122 states "the hyperparameter combination with the highest average AUROC for all datasets is selected." This could mean a single hyperparameter configuration per model is chosen to maximize average AUROC across all 47 datasets simultaneously, which is an unusual design that could mask substantial cross-dataset variance. Clarification is needed.

## Nice-to-Haves
- Report per-dataset AUROC values (or at minimum a histogram) for the 47 tabular datasets
- Add standard deviations or confidence intervals for the 10 repeated runs
- Conduct direct analysis of likelihood distributions (not just AUROC) to test for likelihood inversion
- Separate the paper's two distinct claims: (Q1) does likelihood inversion occur in tabular data? and (Q2) is NF-SLT an effective tabular AD method?

## Removed Points
- **Criticism about Fact 1.1's generality**: The critic noted that Fact 1.1 ("tabular data generally have lower dimensionality") is contradicted by the paper's later acknowledgment of high-dimensional tabular domains. The paper directly addresses this at line 35 ("Although there are datasets in the tabular domain that have higher dimensions than images or strong correlation... these have very different characteristics"), providing adequate nuance. **Removed** — paper already handles this.
- **Criticism about Assumption 3.1 embedding contestable claims**: The critic argued the assumption that "most comparison models should outperform the generative model" embeds unstated assumptions about baseline suitability. These are explicitly presented as assumptions of the definition, not hidden claims. **Removed** — this is what the definition is; contesting it is contesting the definition itself, which is covered by Weakness 1.
- **Criticism about 50% training data split**: The critic noted the Zong et al. (2018) protocol uses only 50% of normal data for training. This is a standard protocol in the field, not a flaw. **Removed**.
- **Strength Finder's generic/superficial strengths**: Removed generic strengths such as "the paper addresses an important problem" or "the paper is well-organized." Only concrete, evidenced strengths are retained.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Restructure the paper around two clearly separated questions**: (Q1) Whether the original likelihood-inversion phenomenon occurs in tabular data requires direct evidence (likelihood distribution analysis, prevalence of AUROC < 0.5 across datasets). (Q2) Whether NF-SLT is an effective tabular AD method is already well-supported by Table 1. The paper should either (a) reframe the contribution around Q2 and present Definition 3.3 as a methodological contribution for defining "failure" in context, or (b) add the missing evidence for Q1.
2. **State β and γ thresholds in the main text** and justify the choice.
3. **Add per-dataset results** (at minimum a histogram or violin plot of AUROC values across the 47 datasets) and standard deviations.
4. **Clarify the hyperparameter selection procedure**: Was one configuration per model used for all 47 datasets? If so, discuss the rationale and limitations.

## Score and Decision

**Calibration anchors consulted:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| jQ596tXT3k (OOD Paradox Likelihood Peaks) | 5.67 | R1 | Stronger technical contribution (LID estimation), rejected for approximation concerns. Current paper has broader empirical scope but a more consequential framing issue. |
| 7QDIFrtAsB (Anomaly Detection by Estimating Gradients) | 5.75 | R1 | Extensive tabular AD benchmark, rejected for limited novelty. Current paper has more novelty (definition + theory) but a clearer structural weakness. |
| RxhOEngX8s (BROAD OOD) | 4.25 | R1 | Benchmark paper, rejected. Current paper is stronger in both scope and analysis. |
| hlijRgXTDK (Pathologies of OOD Detection) | 4.75 | R2 | Critique paper lacking new technical contributions. Current paper has more concrete contributions. |
| LjygLD0AkT (Rethinking Test-time Likelihood) | 5.00 | R2 | Theoretical OOD detection work with strong assumptions. Similar pattern to current paper — useful contributions undermined by framing/assumption issues. |
| Vi6p2TeujL (PTAD) | 4.25 | R2 | Tabular AD method paper, rejected. Current paper has broader scope and more novel contributions. |

**Round 1 bracket**: [4, 6] — The paper is clearly above papers scoring 3-4 (which have fundamental technical flaws or minimal contributions) and below papers scoring 7+ (which are ICLR-worthy contributions with clean execution). Within the middle band, the paper falls between the 4.25-4.75 range (papers with modest contributions) and the 5.67-5.75 range (papers with stronger technical contributions but execution issues).

**Round 2 narrowing**: Compared against anchors at 4.25 (PTAD), 4.75 (Pathologies), and 5.00 (Rethinking Test-time Likelihood), this paper sits above PTAD and Pathologies due to its more extensive empirical scope and novel analysis (d-Ratio), but is comparable to or slightly below the 5.00 anchor due to the framing issue which is more fundamental than the assumption-issues in that paper.

**Final score**: 5.0 — The paper has genuine contributions (extensive benchmark, d-Ratio analysis, formal definition) that would make it a solid paper after revision, but the central definition-question mismatch prevents acceptance at a top venue in its current form. The paper needs structural reframing and additional evidence before it meets the ICLR bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>