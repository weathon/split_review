Now let me run calibration searches to properly score this paper.Round 1 bracket: **5.0–7.0**. Most relevant comparator is `jQ596tXT3k` (OOD paradox via LID, 5.67) and `7VkHffT5X2` (AnoLLM, 6.75 accept). Let me narrow further.Now let me read the 7QDIFrtAsB anchor briefly to sharpen the score comparison:Now I have enough to write the final review.

---

## Summary

This paper studies whether the well-known counterintuitive likelihood phenomenon in image out-of-distribution detection—where generative models assign higher likelihoods to anomalous/OOD data than to normal data—also manifests in tabular anomaly detection. The authors introduce a domain-agnostic operational definition of the phenomenon (Definition 3.3), conduct a comprehensive benchmark across all 47 tabular and 10 CV/NLP embedding datasets in ADBench against 12 baselines, and show that vanilla normalizing-flow likelihood thresholding (NF-SLT) rarely exhibits this phenomenon in tabular settings. They further provide a two-factor theoretical and empirical explanation attributing this rarity to tabular data's lower dimensionality (Theorem 5.4 / Corollary 5.6) and weaker feature correlation (d Ratio analysis, Table 4).

---

## Strengths

1. **Comprehensive, unbiased benchmark**: The evaluation uses *all* 47 tabular and 10 CV/NLP embedding datasets in ADBench—explicitly motivated by avoiding the selection bias documented by Shwartz-Ziv & Armon (2022)—with 12 baselines and 10 repeated experiments. Table 1 shows NF-SLT achieving avg rank 3.43, fail ratio 0.02, and top-2 ratio 0.45, all substantially better than any baseline. This is a robust empirical finding, not a cherry-picked result.

2. **d Ratio analysis connecting feature correlation to NF-SLT performance**: Section 5.2 defines the d Ratio (intrinsic dimension / ambient dimension) as a proxy for feature correlation, validates its behavior on Gaussian synthetic data (Figure 1, left/center), and compares real tabular datasets (d Ratio ≈ 0.39–0.81) to image datasets (d Ratio ≈ 0.002–0.019) in Table 4. Table 4 (bottom) further shows that among the 25 datasets where NF-SLT does not rank first, the fraction with d Ratio below a threshold grows monotonically, directly linking correlation to NF-SLT underperformance. This is the paper's most direct and concrete mechanistic evidence.

3. **Dimensional analysis extending prior theoretical work**: Theorem 5.4 and Corollary 5.6 extend the entropy-based likelihood-gap expression of Caterini & Loaiza-Ganem (2022) to incorporate dimensionality, showing the lower bound of the expected log-likelihood gap decreases linearly with d under independence. The ICA dimensionality-reduction experiment (Table 2) confirms the qualitative prediction for CIFAR-100/SVHN (AUROC rises from 0.0843 at 1024 dims to 0.3490 at 30 dims) and CelebA/SVHN (0.1207 → 0.4711), providing direct empirical support in the expected-violation domain (images).

4. **Consistent results on CV/NLP embedding datasets**: Table 1 (bottom) shows NF-SLT is best or near-best on all 10 embedding datasets; the one underperforming case (imdb, gap = 0.0385) is shown to not satisfy Definition 3.3's gap condition. The d Ratio explanation is coherent here too: embeddings have intrinsic dimension 18–23 in ambient space of 1000, yielding a much higher d Ratio than raw pixels.

---

## Weaknesses

### Fatal
None.

### Major

- **β and γ not stated in the main text, preventing verification of the central claim.** The paper's central empirical claim is that "the phenomenon rarely occurs" as measured by Definition 3.3. However, Section 3 states only that "The fully rigorous formulation of Definition 3.3 is provided in Appendix B" without disclosing the actual values of β and γ. Without these thresholds, a reader cannot assess whether (a) the thresholds are calibrated meaningfully against the CIFAR-10/SVHN reference case (AUROC 6.4%), (b) the definition is trivially easy to avoid triggering, or (c) the conclusion of "rarity" is robust to threshold variation. This is not a formatting concern—it is a material gap in the paper's core evidentiary chain that should appear in the main text.

- **Theorem 5.4 assumes dimension-wise independence, but the paper applies it to explain behavior in correlated tabular data, without bridging this gap.** Theorem 5.4 explicitly states: "Let P = ∏ pᵢ(xᵢ) and Q = ∏ qᵢ(xᵢ) be independent d-dimensional distributions." The independence assumption allows entropy to factor into a sum of marginal entropies, making the dimension d appear as a linear multiplier. The paper then invokes this theorem as the theoretical account of why tabular data succeeds, yet Section 5.2 documents that tabular datasets have d Ratio values ranging from 0.39 to 0.81—clearly not approximately independent. The paper acknowledges this only in passing ("although there are datasets in the tabular domain that have higher dimensions than images or strong correlation"), but does not provide any extension, bound, or qualification of Theorem 5.4 for the partially-correlated case. The independence assumption is the load-bearing premise of the theorem; invoking the theorem where that premise is violated leaves the theoretical scaffolding incomplete.

### Minor

- **The entropy condition H(P) > H(Q) is the trigger for the counterintuitive phenomenon in Theorem 5.4 and Corollary 5.6, but is never empirically verified for any of the 47 tabular datasets.** Section 5.1 uses this condition extensively to interpret the image experiments in Table 2 (identifying which side of the "bold vertical line" each pair falls on), but never applies this check to the tabular datasets where NF-SLT succeeds. If most tabular anomaly tasks satisfy H(P) < H(Q) by construction (e.g., anomalies are rarer, more diverse, and thus higher entropy), the theoretical explanation via dimensionality would be secondary to a favorable entropy relationship, not the mechanism the paper emphasizes. Checking this condition even approximately (via histogram or k-NN entropy estimator on a few tabular datasets) would ground the theoretical discussion substantively.

- **Table 2 offers mixed support for Corollary 5.6.** The CIFAR-10/SVHN case—the canonical image failure mode—does not improve as dimensionality decreases (1024 dims: AUROC 0.3311; 30 dims: AUROC 0.3143, a slight *decrease*). The paper's explanation that CIFAR-10/SVHN's failure to improve is due to "complexity of pixel correlations violating independence" is post-hoc and not independently verified. The prediction holds for CIFAR-100/SVHN and CelebA/SVHN, providing 2 of 3 confirmatory cases, but the most prominent case does not behave as predicted.

- **The choice of minimum in Equation 3 (gap condition) is not well motivated.** Equation 3 requires the *minimum* AUROC gap among better-performing models to exceed γ, rather than the average or median. This is the same statistic used both to declare the phenomenon present and to exonerate NF-SLT on "yeast" (minimum gap 0.02). Using the minimum makes the presence condition easy to satisfy (a single outlier model suffices) while also making the exculpatory test easy to pass. The paper does not discuss this design choice or compare it to alternatives.

### Trivial
None.

---

## Nice-to-Haves

- **State β and γ explicitly in the main text and include a brief sensitivity analysis** (e.g., does the conclusion "rare" hold if thresholds are varied by ±20%?). This would make the definitional choices transparent and confirm robustness.
- **Extend the d Ratio analysis to all 47 tabular datasets** rather than four illustrative examples, and plot per-dataset NF-SLT AUROC against d Ratio directly. Table 4 (bottom) gestures at this via bucketed thresholds but the full scatter would be the most convincing version of the Section 5.2 argument.
- **Provide at least approximate entropy estimates for a sample of tabular datasets** to verify whether the H(P) > H(Q) condition applies there. This would either strengthen the theoretical account or correctly attribute the rarity to the entropy relationship rather than dimensionality.
- **Motivate the minimum gap statistic** in Equation 3, or compare to results using average or median gap, as a robustness check.
- **Discuss or relax the independence assumption** in Theorem 5.4 for the correlated case. Even stating "Theorem 5.4 bounds behavior under independence; the correlated tabular case is explained empirically by Section 5.2" would clarify the relationship between the two explanatory threads.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic – Table 2 "provides only weak support" (cited primarily from CIFAR-10/SVHN)**: The critic characterizes the ICA experiment as providing only weak support by focusing on the one case (CIFAR-10/SVHN) where AUROC does not improve. The other two cases (CIFAR-100/SVHN, CelebA/SVHN) show substantial improvement (0.0843→0.3490, 0.1207→0.4711). Retained as *Minor* rather than *Major* with appropriate caveats.

- **Harsh Critic – hyperparameter selection being unfair**: The paper states that for all models, "the hyperparameter combination with the highest average AUROC for all datasets is selected." This is a global selection (across all 47 datasets), not per-dataset, which reduces overfitting. The critic's concern that NF-SLT might receive privileged treatment is not substantiated by the text. Removed.

- **Harsh Critic – Definition is "circular"**: The critic argues the definition conflates "likelihood inversion" with "comparative AUROC ranking." The paper explicitly argues (Section 3, opening paragraph) that simply checking whether anomalies receive higher likelihoods than normals is an insufficient operationalization because intrinsic dataset difficulty can produce the same result. The comparative definition is a deliberate and justified design choice, not a circular one. Removed.

- **Strength Finder – CIFAR-10/SVHN showing improvement in Table 2**: The Strength Finder states "for CIFAR-10 vs. SVHN, AUROC rises from 0.33 to 0.31" as evidence. This misreads the table—AUROC actually decreases slightly (0.3311→0.3143). The correct supporting cases are CIFAR-100/SVHN and CelebA/SVHN. Removed from strengths as stated; the broader dimensionality claim is still supported by those two cases.

- **Harsh Critic – AUROC integrating over score distribution could hide sample-level likelihood inversions**: While this is a philosophically valid distinction, it applies to virtually all comparative AUROC benchmarks and is precisely why the paper's definition (motivated in Section 3) is adopted. Without specific evidence that sample-level inversions are occurring in tabular data despite good AUROC, this concern is speculative. Removed.

---

## Novel Insights

The paper's most analytically novel observation is that feature correlation—quantified as the ratio of intrinsic to ambient dimension (d Ratio)—explains performance variation *within* the tabular domain: even among tabular datasets, those with low d Ratio (high correlation) tend to undermine NF-SLT. This "within-tabular" heterogeneity analysis goes beyond the image-vs-tabular dichotomy and provides a more principled handle on when likelihood-based anomaly detection can be trusted. The finding that some tabular datasets (e.g., genomics) behave image-like due to high correlation is a useful nuance that points toward a correlation-indexed rather than domain-indexed view of the phenomenon.

---

## Suggestions

1. Move the explicit values of β and γ from Appendix B into Section 3, and add a one-paragraph sensitivity analysis showing that the "rare" conclusion is stable across a range of threshold values.
2. In Section 5.1, add a brief empirical check (histogram-based or k-NN entropy estimation) for the H(P) > H(Q) condition on a representative subset of the 47 tabular datasets to ground the theoretical discussion.
3. Clarify the scope of Theorem 5.4 explicitly: state that it applies under independence and that the correlated tabular case is handled empirically by Section 5.2. This removes the apparent contradiction between the theorem's premise and its application.
4. Extend the d Ratio computation to all 47 tabular datasets and include a scatter plot of NF-SLT AUROC vs. d Ratio to strengthen the mechanistic claim beyond the four examples in Table 4.
5. Discuss the CIFAR-10/SVHN non-improvement in Table 2 more directly rather than attributing it post-hoc to pixel correlations without further evidence.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `6Z8rZlKpNT.md` (NF for OOD via latent density) | 3.40 | R1 | Weak, much narrower scope, no tabular study |
| `i28ZjVxl81.md` (OOD tabular, basic) | 2.50 | R1 | Much weaker, no theory |
| `rcmhydaEJp.md` (Flow imputation) | 3.00 | R1 | Different task, no benchmark breadth |
| `7QDIFrtAsB.md` (NCSN tabular AD, rejected 5.75) | 5.75 | R1/R2 | Proposes novel method + large benchmark; rejected. Paper under review lacks novel method but is more theoretically grounded |
| `jQ596tXT3k.md` (OOD paradox via LID, rejected 5.67) | 5.67 | R1/R2 | Most topically similar; proposes new LID method + explanation; rejected. Paper under review has more empirical breadth but similar theoretical issues |
| `Vi6p2TeujL.md` (PTAD, rejected 4.25) | 4.25 | R1 | Proposes new method, weaker results |
| `hlijRgXTDK.md` (OOD pathologies, rejected 4.75) | 4.75 | R2 | Critique paper, less empirical content |
| `falBlwUsIH.md` (OOD without labels, accepted 6.33) | 6.33 | R2 | Stronger theory, cleaner information-theoretic proof |
| `lNZJyEDxy4.md` (MCM tabular AD, accepted 6.67) | 6.67 | R2 | Novel masking method, accepted; paper under review has no new method |
| `7VkHffT5X2.md` (AnoLLM, accepted 6.75) | 6.75 | R1/R2 | Novel LLM-based method, accepted; paper under review lacks novel method |
| `cJs4oE4m9Q.md` (Hypersphere AD) | 8.00 | R1 | Much stronger methodology, clear theoretical novelty |
| `CJnceDksRd.md` (DRL tabular AD, accepted 5.75) | 5.75 | R2 | Novel method + good empirics; comparable breadth |

**Round-1 bracket**: 5.0–7.0

**Round-2 narrowing**: The paper under review sits closest to `jQ596tXT3k` (5.67, rejected) and `7QDIFrtAsB` (5.75, rejected). Both of those papers propose new methods—this paper does not. The empirical scope is comparable or slightly broader (47 vs. ~50+ datasets in 7QDIFrtAsB, but 12 vs. 49 baselines). The theoretical contribution (Theorem 5.4/Corollary 5.6) is real but burdened by the unverified independence and entropy premises. The d Ratio analysis is original and well-executed. Compared to accepted papers in this range (`lNZJyEDxy4` at 6.67, `7VkHffT5X2` at 6.75), those papers propose novel methods with clean ablations—the paper under review's primary novelty is the benchmark study and definition, not a new algorithm.

The paper is comparable to the 5.67–5.75 rejected papers. It is slightly more interesting than `jQ596tXT3k` in terms of empirical breadth and the d Ratio analysis, but weaker in that it proposes no new model. The theoretical gaps (missing β/γ in main text, independence assumption, unverified entropy condition) are material. Final score: **5.5**.

**Originality**: Moderate. The definition is novel; the empirical study is comprehensive; the theoretical extension to dimensionality extends prior work rather than breaking new ground.  
**Importance**: Moderate-high. Demonstrating that simple likelihood tests work reliably across 47 tabular datasets is practically useful and addresses a real community concern.  
**Claim support**: Moderate. The core empirical claim is well-supported by Table 1. The theoretical claims are partially supported but rest on unverified premises.  
**Experiment soundness**: Good on the benchmark side; moderate on the theoretical validation side.  
**Clarity**: Good overall, though Definition 3.3 is insufficiently transparent without β/γ.  
**Value to community**: Moderate. The benchmark study is immediately useful; the theoretical explanation would be more valuable with the independence gap closed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>