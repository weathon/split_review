Now I have thoroughly read and verified the paper against the reviewer claims. Let me construct the final review.

## Summary

This paper introduces β-calibration, a group-conditional generalization of standard calibration for generative QA, where the calibration guarantee is conditioned on a partition β of question-answer pairs. The authors propose two posthoc calibration schemes — β-binning and hierarchical scaling-β-binning — and prove a distribution-free approximate β-calibration guarantee for both. Experiments across 5 QA datasets with Mistral and Gemma show that the proposed methods substantially reduce β-calibration error compared to standard calibration baselines, and in some settings improve selective QA performance.

## Strengths

1. **Well-motivated generalization of calibration.** The paper identifies a fundamental limitation of average-case calibration for generative QA — it can be misleading for individual user groups or topic clusters — and formalizes this with a clear counterexample (Example 1, Table 1). The notion of β-calibration (Definition 3) directly addresses this by conditioning on a partition of the QA space, and it recovers standard calibration as a special case when β is constant. This is the paper's central conceptual contribution and is clearly articulated.

2. **Distribution-free guarantee with explicit bounds.** Theorem 1 provides a finite-sample, high-probability bound on the conditional β-calibration error for both proposed schemes. The bound has a simple closed form (ε = √(log(2N/bα)/(2(b−1))) + ν), depends only on the bin size b and misspecification ν, and holds for any discrete β. The paper also provides practical guidance (Figure 2) for choosing b based on target ε and dataset size.

3. **Consistent and large improvements in β-calibration error.** Across all settings in Table 2 (MMLU and BigBench with Mistral and Gemma), the proposed methods (especially HS-BB) achieve substantially lower β-calibration error than all baselines. For example, on MMLU Verb1s-Top1 with Mistral, CE(h;β) drops from 0.639 (None) to 0.149 (HS-BB), a 77% reduction. On BigBench Ling1S-Top1 with Mistral, it drops from 0.245 to 0.138. The improvements are consistent and far exceed what could be attributed to the baselines being "unsuited" for the metric — the gap is too large to be explained away.

4. **Principled instantiation of β via kd-tree embeddings.** Using DistilBERT [CLS] embeddings with a kd-tree provides an efficient, adaptive, and semantically meaningful partitioning of QA pairs. The instantiation is well-justified: it generalizes standard calibration at depth d=0, produces cohesive groups, and is computationally efficient. The paper's methods work with any β, but this concrete instantiation makes the framework reproducible.

5. **Robust handling of data scarcity via hierarchical scaling.** The scaling-β-binning method uses hierarchical logistic regression with random intercepts and slopes (partial pooling), allowing information sharing across partitions. This directly addresses the practical challenge of partitions with few data points — a realistic concern for fine-grained β — and the experiments confirm that HS-BB consistently outperforms the fully-pooled S-BB.

6. **Comprehensive experimental design.** The evaluation spans 5 datasets, 2 LLMs, 2 confidence elicitation prompts, and 4 strong baselines. The 4-way data split (20:60:10:10 for kd-tree construction, calibration training, hyperparameter tuning, and testing) is a careful protocol that strengthens reliability.

## Weaknesses

### Fatal
None.

### Major
None. While the paper has limitations (discussed below), none invalidate its core claims or contributions.

### Minor

1. **The theoretical guarantee's assumptions are not operationalized in experiments.** Theorem 1 requires that every partition s ∈ S have at least b calibration points (n_s ≥ b). The paper's hyperparameter search ensures this by construction — it selects depths such that each partition admits 3–10 bins, implying n_s ≥ 3b — but it never explicitly reports the fraction of test points that fall into partitions satisfying n_s ≥ b. Since the root fallback (used for test points in unseen partitions) does not carry the same guarantee, reporting this coverage statistic would meaningfully connect theory to practice. The authors should add this to strengthen the paper; without it, the empirical connection to the theorem is implicit rather than verified.

2. **CM(h;β) estimation procedure is underspecified for continuous scores.** Definition 4 defines the β-calibration error at the population level, but computing it from finite samples requires binning along both the confidence scale and β-induced groups. For methods that output continuous scores (e.g., the "None" baseline), the inner conditional expectation must be approximated via discretization. The paper does not specify how this estimation is done — e.g., what binning scheme is used for the confidence dimension when computing CM(h;β) for None, Platt scaling, etc. Since different binning choices can affect the reported error, this should be clarified.

3. **Proxy labels introduce unquantified misspecification.** The ground truth proxy is generated by Llama 3.1 (line 610), introducing a misspecification factor ν in the theoretical framework. The paper mentions that ν could be estimated using a hold-out set with true labels (line 308), but does not provide such an estimate. As a result, the reported CM(h;β) and AUAC values reflect calibration to the proxy, and the gap between proxy and true correctness is unknown. A rough empirical bound on ν, even on a small subset with human-verified labels, would strengthen the connection between theory and evidence.

4. **Hyperparameter sensitivity to kd-tree depth d is not explored.** The depth d, which controls the granularity of β partitions, is selected by optimizing AUAC on a held-out set. The paper states that the optimal d is never 0 (line 373), but does not show how CM(h;β) or AUAC vary with d, nor whether the optima are sharp. Given that d is arguably the most important design choice in the β instantiation, an ablation would help practitioners understand the trade-off between partition granularity and statistical reliability.

5. **Selective QA gains are modest in several settings.** While the paper claims "up to 30% increase in selective answering performance," the AUAC gains are inconsistent across settings. In several cases (e.g., MMLU Ling1s-Top1 Mistral: 0.269 vs. 0.269; BigBench Ling1S-Top1 Mistral: 0.690 vs. 0.684), the proposed methods are essentially tied with the None baseline within confidence intervals. The claim is technically accurate with the "up to" qualifier (a 33.7% gain occurs for MMLU Verb1s-Top1 Gemma BB), but the selective QA benefits are not as universal as the β-calibration error improvements.

### Trivial
- The paper uses "Table 1" and "Table 2" inconsistently in the text (line 370 references "Table 2" but the main results table is labeled Table 1 in the embedded caption). This should be harmonized.

## Nice-to-Haves
- A breakdown of CM(h;β) per β-group for at least one dataset, illustrating which groups are most miscalibrated and how the methods improve them.
- A brief discussion of computational cost (wall-clock time) for scaling-β-binning, since the hierarchical logistic regression scales with the number of partitions.
- Sensitivity analysis with alternative β functions (e.g., random partitioning, topic-model-based groupings) to demonstrate generality.

## Removed Points
These points were removed from the critic's input as they were either factually wrong, based on misunderstanding the paper, or violated the review guidelines:

- **"Unfair baseline comparison" (Critical Issue 3):** The reviewer proposed adding a "partition-specific baseline that applies UMD independently to each β-induced group" to isolate the benefit of β-grouping. This is exactly what β-binning (BB) already does — it applies UMD independently per partition. The comparison B (pooled UMD) vs. BB (per-partition UMD) already isolates this effect. The reviewer's criticism reflects a misunderstanding of the paper's own method. Factually incorrect; removed.

- **"Inflated performance claims" (Critical Issue 2) — specifics re: CE(h;β):** The reviewer claimed the β-calibration improvements are only "10-40%." In reality, the improvements over None are often 50-77% (e.g., from 0.639 to 0.149 on MMLU Verb1s-Top1 Mistral). The paper's stated "10-40%" range is actually conservative for the β-calibration metric, not inflated. Removed the CE-specific sub-claim; kept the AUAC nuance as Minor #5.

- **"Inflated performance claims" (Critical Issue 2) — AUAC specifics:** The reviewer claimed "many other entries contradict" the "up to 30%" AUAC claim and singled out BigBench Ling1S-Top1 Mistral (0.690 vs. 0.684). However, "up to 30%" means the maximum observed gain, not the average. The BB method on MMLU Verb1s-Top1 Gemma achieves a 33.7% relative AUAC improvement over None, supporting the claim. The paper is not claiming that every setting achieves 30% gains. Overstated criticism; kept only the qualified version in Minor #5.

- **Criticism about "line 399" and "line 564" references:** These line numbers refer to the original LaTeX, not the parsed text; the content referenced (fallback to root calibrator) is present and discussed in the paper (Algorithms 1-3, lines 200-226). Not a valid weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews identify useful suggestions for strengthening the empirical validation but do not surface a fundamentally new perspective on the work.

## Suggestions

1. Report, for each experimental setting, the fraction of test points that fall into partitions with n_s ≥ b (where Theorem 1's guarantee holds) versus those handled by the root fallback. This directly connects the theory to practice.
2. Clarify the finite-sample estimation procedure for CM(h;β) — specifically, how the inner conditional expectation is binned for methods that output continuous confidence scores.
3. Provide an empirical estimate of the misspecification factor ν on a small subset with human-labeled ground truth, even if approximate.
4. Add an ablation showing how CM(h;β) and AUAC vary with kd-tree depth d for at least one dataset/model combination.
5. Qualify the selective QA claim slightly by noting that AUAC gains are most pronounced on MMLU compared to BigBench, rather than presenting a single universal number.

## Score and Decision

The paper makes a well-motivated conceptual contribution (β-calibration), provides practical algorithms with a clean theoretical guarantee, and demonstrates large and consistent improvements on its target metric across diverse settings. The weaknesses are minor and addressable — none undermine the core claims. The writing is clear, the experimental design is thorough, and the work has clear practical value for deploying generative QA systems with reliable confidence scores.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>