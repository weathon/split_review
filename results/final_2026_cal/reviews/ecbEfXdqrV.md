Now I have all the information needed to write the final consolidated review. Let me compile it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Let me now compute calibration anchors properly.

For the calibration report:

**Round 1 — Bracketing**
- Weak anchors (high_score=3.5): Papers 3.0-3.33 — rejected tabular AD papers (JdbqDiguyO 3.33, Ct3MmgpOki 3.00, AQSeiBXWwd 3.00, wunWpzNKfl 3.00)
- Middle anchors (3.5-7.5): Papers 4.0-6.0 — likelihood paradox mitigation (jCQVjd4vrX 4.00, rejected), Certificate of Trust (2RuSWLQK82 5.33, accepted), Dissecting Mahalanobis (HuuCWjlJuQ 4.29, withdrawn), Fisher-Rao (GEtOzC4MIi 6.00, accepted)
- Strong anchors (low_score=7.5): Papers 8.0 — unrelated topics (nCsF3Bsn2n, 248ysaRatx, Ahdsg2nkNH, yRtgZ1K8hO)

Round 1 bracket: 4.5 to 6.0

**Round 2 — Narrowing**
- (4.5-6.0): ReTabAD (UFwgg44VZq 5.50, accepted), MAPE (jRP5nlqhnW 4.67, rejected), TimeRCD (Z4T26VztkU 5.00, rejected), Foundation Models TSAD (H27kvyG4qf 5.00, accepted)
- (5.0-7.0): Fisher-Rao (GEtOzC4MIi 6.00, accepted), SCOPED (TMLiG9Rk2J 5.50, accepted), GradPCA (7rvMexIZA1 5.60, accepted), SGFlow (C1bkDPqvDW 5.50, accepted)

Final score: 5.5Now I'll produce the final consolidated review.

## Summary

This paper empirically investigates whether the counterintuitive phenomenon in which deep generative models assign higher likelihoods to anomalous data—well-documented in the image domain—also occurs in tabular anomaly detection. It proposes a domain-agnostic definition of the phenomenon (Definition 3.3), then conducts an extensive evaluation across all 47 ADBench tabular datasets and 10 CV/NLP embedding datasets, benchmarking normalizing-flow-based simple likelihood testing (NF-SLT) against 12 baselines. NF-SLT achieves the highest average AUROC (0.8575) and a fail ratio of only 0.02, demonstrating that the phenomenon rarely occurs in tabular settings. The paper further provides theoretical analysis linking dimensionality to the likelihood gap (Theorem 5.4, Corollary 5.6) and empirical analysis connecting feature correlation (via intrinsic dimension estimates) to detection performance.

## Strengths

- **Comprehensive evaluation without selection bias**: The paper tests on all 47 ADBench tabular datasets and 10 CV/NLP embedding datasets against 12 baselines. Table 1 shows NF-SLT achieves the highest average AUROC (0.8575), AUPRC (0.6398), lowest average rank (3.43), and lowest fail ratio (0.02). This directly addresses the selection bias critique (Shwartz-Ziv & Armon, 2022) and provides the most thorough empirical investigation of flow-based likelihood testing in tabular AD to date.

- **Theoretical extension linking dimensionality to likelihood gap**: Theorem 5.4 extends the Caterini & Loaiza-Ganem (2022) entropy-based likelihood gap decomposition by proving that under independence assumptions and the entropy condition ℍ(P) > ℍ(Q), the lower bound of the expected likelihood gap decreases linearly with dimension d. Corollary 5.6 further shows an inverse relationship between the maximum achievable AUROC and dimensionality. This formalizes an intuition present in prior work but not previously proven.

- **Controlled dimensionality experiments supporting the theory**: Tables 2 and 3 systematically reduce image dimension (via ICA and bilinear interpolation) and show that when ℍ(P) > ℍ(Q), AUROC increases as dimension decreases—e.g., CelebA vs. SVHN rising from 0.1207 (1024 dims) to 0.4711 (30 dims). These controlled experiments provide credible causal evidence for the dimension-based explanation.

- **Intrinsic dimension analysis linking feature correlation to performance**: Section 5.2 uses MLE and TwoNN estimators to show that tabular datasets have substantially higher d Ratio (intrinsic/ambient dimension)—e.g., MagicGamma d Ratio 0.700 vs. CIFAR-10 d Ratio 0.003—and that low d Ratio strongly predicts poor NF-SLT performance (Table 4 bottom: at d Ratio threshold 0.1, only 16% of poorly performing datasets; at 0.8, 100%). This provides a concrete correlate of feature heterogeneity that explains the domain difference.

## Weaknesses

### Major

- **Definition 3.3 does not directly capture the phenomenon described in the paper's title and abstract**. The paper's motivating literature (Nalisnick et al., 2019a) concerns generative models assigning *higher likelihoods to anomalies than to normals* (likelihood inversion). However, Definition 3.3 operationalizes the phenomenon as the generative model being *outperformed by many comparison models by a large margin*. These are different things: a model could have no likelihood inversion (AUROC > 0.5) yet be beaten by stronger baselines, or it could exhibit true likelihood inversion (AUROC < 0.5) but rank well among weak baselines. The paper acknowledges the limitations of the simpler definition (Section 1, "this view is contradictory since the argument would consider any result outside 100% AUROC as counterintuitive") and proposes Definition 3.3 as an alternative, but this shift means the headline claim—"Why Is the Counterintuitive Phenomenon of Likelihood Rare in Tabular Anomaly Detection"—is answered using evidence about relative model rankings rather than direct likelihood comparisons. The paper's own empirical evidence mitigates this: NF-SLT achieves mean AUROC 0.8575, which *directly* implies anomalies tend to receive lower likelihood (no inversion), but the paper's analytical framing (fail ratio, Top2 ratio) emphasizes the relative-ranking definition rather than this direct evidence.

- **Theoretical analysis rests on assumptions not satisfied by real tabular data**. Theorem 5.4 assumes P and Q are independent product distributions and that P₍θ₎ approximates P perfectly. Real tabular features exhibit weak to moderate correlations, and learned flows are never perfect density estimators. Moreover, the theorem requires the condition ℍ(P) − ℍ(Q) > D_KL(Q‖P) to apply, but the paper never verifies whether this condition holds for any of the 47 tabular datasets used. The ICA experiments (Table 2) attempt to test the dimension effect, but ICA only linearizes correlations and does not enforce full independence, and the entropy condition is asserted rather than measured. The bilinear interpolation experiments (Table 3) are explicitly acknowledged as not satisfying the independence assumption, and some results "conflict with the theorems" (line 180). While the qualitative trend (lower dimension helps) is plausible, the theoretical support is too fragile to carry the paper's explanation of *why* the phenomenon is rare.

### Minor

- **The analysis emphasizes relative model rankings rather than the direct likelihood ordering**. The paper's results section focuses on fail ratio (proportion of datasets where NF-SLT's rank is 9th or lower) and Top2 ratio rather than on the simple question: "for each dataset, what fraction of anomalies receive higher likelihood than the median normal sample?" While the average AUROC of 0.8575 implicitly answers this (anomalies are ranked below normals), the paper does not report per-dataset AUROC distributions or the count of datasets where NF-SLT actually exhibits AUROC < 0.5 (which would indicate true likelihood inversion). The 'yeast' dataset is mentioned as a case of relatively low performance, but its actual AUROC is not given.

- **Hyperparameter selection procedure may asymmetrically affect baselines**. The paper selects a single hyperparameter configuration per model by maximizing average AUROC across *all* 47 datasets simultaneously. While this avoids per-dataset cherry-picking, it may favor models (like NF-SLT with NICE) that are robust to one-size-fits-all tuning, while methods like DeepSVDD or ICL that typically benefit from per-dataset adjustments may be disadvantaged. The paper does not show that the same conclusions hold when models are tuned per dataset.

- **Definition 3.3's thresholds β and γ are not concretely specified or applied**. The definition requires two thresholds (proportion of outperforming baselines, minimum AUROC gap), but the paper never states what values of β and γ are used, nor does it directly apply Definition 3.3 by counting datasets that satisfy both conditions. Instead, the paper uses proxies (fail ratio, Top2 ratio, the yeast/imdb examples) to argue about the phenomenon. The full formulation is deferred to Appendix B (stripped by the parser), but operationalization in the main text would strengthen the connection between definition and evidence.

### Trivial

- The phrase "9th or lower" for fail ratio is defined with rank 9+ but k=12 baselines → this means being in the bottom 1/3 of models. A clearer justification for this threshold would help.

- Table 1 does not report standard deviations or statistical significance (e.g., Wilcoxon signed-rank across datasets) despite 10 repeated experiments being performed.

## Nice-to-Haves

- **Directly measure likelihood ordering**: For each dataset, report the proportion of anomalies with likelihood exceeding the median normal likelihood. This would connect directly to the image-domain literature and require no definitional indirection.

- **Verify the entropy condition**: Estimate ℍ(P) and ℍ(Q) for a subset of tabular datasets using nearest-neighbor entropy estimators to check whether ℍ(P) > ℍ(Q) holds, which would confirm that the theoretical dimension argument applies.

- **Include VAE-based likelihood estimation**: The paper focuses on normalizing flows, but the phenomenon was observed for likelihood-based models generically. A VAE with ELBO-based scoring would clarify whether the results are flow-specific or apply to all tractable likelihood methods.

## Removed Points

These points were considered but removed from the main weaknesses, as they are not valid upon verification against the paper:

- "The paper never directly tests for likelihood inversion" — **Removed**. This is factually incorrect. The paper reports AUROC for NF-SLT (0.8575), and AUROC directly measures whether anomalies are ranked above or below normals. AUROC > 0.5 means anomalies have lower likelihood (no inversion). The paper directly provides this evidence.

- "The theory's dimension dependence is uninterpretable because the entropy condition is not verified" — **Downgraded from Fatal to Major**. The entropy condition is indeed unverified for tabular data, but the controlled experiments (Tables 2, 3) provide empirical support for the dimension effect even without verifying the condition on tabular datasets. The paper acknowledges which experiments violate the theorem's assumptions.

- Criticisms about missing appendix content (Appendix B formulation, Appendix F hyperparameter spaces) — **Removed per hard rules**. The parser strips appendix sections; they exist in the original submission.

- "The embedding datasets blur the boundary between tabular and image domains" — **Removed**. The paper transparently separates tabular results (Table 1 top) from CV/NLP embedding results (Table 1 bottom) and provides a dedicated analysis (Section 5.2) explaining why embeddings behave differently.

- "No theoretical contribution, just correlation evidence for intrinsic dimension" — **Removed**. The paper provides Theorem 5.4 and Corollary 5.6, which are genuine theoretical contributions extending prior work. The ID analysis is explicitly framed as correlational ("one factor," not a causal claim), which is appropriate.

## Novel Insights

The most interesting insight that emerges from combining the reviews is that the paper's primary empirical contribution (NF-SLT works well on tabular data) is robust regardless of which definition of "counterintuitive phenomenon" one adopts, but the paper's *framing* using Definition 3.3 creates unnecessary tension with the literature it cites. The paper would be better positioned as a comprehensive empirical demonstration that likelihood-based anomaly detection with normalizing flows is practically reliable for tabular AD, with the theoretical and intrinsic-dimension analyses as supporting explanations—rather than centering on a novel definition that redefines the phenomenon being studied. The contrast between the clean, controlled dimension-reduction experiments (Tables 2, 3) and the messy, correlational intrinsic-dimension analysis (Table 4, Figure 1) is also instructive: it highlights that we understand the *dimension* effect reasonably well (through theory and controlled experiments) but have a weaker handle on the *feature correlation* effect, which is likely the more important factor for tabular data.

## Suggestions

1. **Re-center the narrative**: Reframe the paper around "Normalizing flow-based likelihood testing is practically reliable for tabular anomaly detection" rather than "the counterintuitive phenomenon is rare." This avoids the definitional disconnect and aligns the evidence (high AUROC, low fail ratio) directly with the claim.

2. **Operationalize Definition 3.3**: If the definition is to remain central, specify concrete β, γ values and apply the definition to count how many datasets satisfy both conditions. This would make the definition actionable rather than decorative.

3. **Report per-dataset AUROC**: Add a figure showing the full distribution of AUROC values across the 47 datasets (e.g., a scatter plot or boxplot with dataset labels). Flag any dataset where NF-SLT's AUROC is below 0.5 (true likelihood inversion) and discuss these cases explicitly.

4. **Verify the entropy condition**: Estimate ℍ(P) and ℍ(Q) for a diverse subset of tabular datasets to confirm that ℍ(P) > ℍ(Q) holds—or discuss what happens if it doesn't. This would strengthen the connection between Theorem 5.4 and the empirical results.

5. **Add statistical significance**: Report standard deviations from the 10 repeated experiments and include a statistical test (e.g., Wilcoxon signed-rank across datasets) comparing NF-SLT to the best-performing baseline.

---

My round-1 bracket was 4.5–6.0 based on comparisons with anchors scoring 3.0–3.33 (rejected tabular AD papers), anchors at 4.0–6.0 (mixed accept/reject), and anchors at 8.0 (strong accepts, but on unrelated topics). Round 2 narrowed this by comparing against ReTabAD (5.50, Accept Poster), GradPCA (5.60, Accept Poster), SCOPED (5.50, Accept Poster), and SGFlow (5.50, Accept Poster). The paper under review is of comparable quality to these anchors: it has broader empirical scope and theoretical ambition than ReTabAD but shares a similar definitional-concern weakness; it has weaker theory than GradPCA but broader and more directly applicable results. Placing it at 5.5 reflects that the paper's contributions (comprehensive benchmark, theoretical analysis, intrinsic dimension insights) are real and above the acceptance bar, but the Definition 3.3 disconnect and unverified theoretical conditions prevent it from reaching the 6+ range occupied by the cleanest papers.

**Calibration anchors used (all rounds)**:

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| JdbqDiguyO | 3.33 | R1 (weak) | Rejected tabular AD paper; this paper is clearly stronger |
| Ct3MmgpOki | 3.00 | R1 (weak) | Rejected tabular AD paper; this paper is stronger |
| AQSeiBXWwd | 3.00 | R1 (weak) | Rejected; OOD for conditional generation; different topic |
| wunWpzNKfl | 3.00 | R1 (weak) | Withdrawn tabular AD; this paper is stronger |
| jCQVjd4vrX | 4.00 | R1 (mid) | Rejected likelihood paradox paper; this paper's contribution is stronger |
| 2RuSWLQK82 | 5.33 | R1 (mid) | Accepted poster; OOD for scientific AI; comparable quality |
| HuuCWjlJuQ | 4.29 | R1 (mid) | Withdrawn; Mahalanobis analysis; this paper has stronger empirical contribution |
| GEtOzC4MIi | 6.00 | R1 (mid) | Accepted poster; Fisher-Rao OOD; this paper has weaker theory but broader scope |
| nCsF3Bsn2n | 8.00 | R1 (strong) | Unrelated topic; not comparable |
| 248ysaRatx | 8.00 | R1 (strong) | Unrelated topic; not comparable |
| Ahdsg2nkNH | 8.00 | R1 (strong) | Unrelated topic; not comparable |
| yRtgZ1K8hO | 8.00 | R1 (strong) | Unrelated topic; not comparable |
| UFwgg44VZq | 5.50 | R2 | Accepted poster; ReTabAD benchmark; comparable quality, different strengths |
| Z4T26VztkU | 5.00 | R2 | Rejected; TSAD foundation model; this paper is somewhat stronger |
| jRP5nlqhnW | 4.67 | R2 | Rejected; graph AD; this paper is stronger |
| H27kvyG4qf | 5.00 | R2 | Accepted poster; TSAD critique paper; comparable but different domain |
| TMLiG9Rk2J | 5.50 | R2 | Accepted poster; SCOPED diffusion OOD; comparable |
| 7rvMexIZA1 | 5.60 | R2 | Accepted poster; GradPCA OOD; comparable but narrower scope |
| C1bkDPqvDW | 5.50 | R2 | Accepted poster; flow models; not directly comparable |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>