Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper introduces β-calibration, a generalization of average-case calibration that conditions on groups of question-answer pairs defined by a function β. The authors propose two posthoc calibration algorithms (β-binning and scaling-β-binning) that achieve this grouped notion of calibration, provide a distribution-free theoretical guarantee, and instantiate β concretely via kd-tree on DistilBERT embeddings. Experiments on 5 QA datasets with 2 LLMs show that the proposed methods substantially reduce β-calibration error and improve or match selective QA performance.

## Strengths

1. **Well-motivated new calibration target.** The paper identifies a genuine limitation of average-case calibration for generative QA — that it can mask systematic miscalibration for subgroups of QA pairs. Example 1 (Section 2.2) cleanly illustrates this, and β-calibration formalizes the intuitive requirement that calibration should hold conditional on groups. This is a principled and useful generalization.

2. **Distribution-free guarantee with practical guidance.** Theorem 1 provides a high-probability bound on β-calibration error that depends on interpretable quantities (bin size b, per-bin sample count, misspecification ν) and Figure 2 translates this directly into hyperparameter choices. Such actionable theoretical guidance is rare in the LM calibration literature.

3. **Consistent empirical gains on β-calibration error.** On both datasets and both LLMs, the proposed methods (especially HS-BB) achieve dramatically lower CE(h;β) than all baselines — e.g., from ≈0.53–0.64 (None) down to ≈0.15–0.18 (HS-BB) on MMLU (Table 2). The gap is large and consistent across settings.

4. **Hierarchical scaling addresses sparse partitions.** Scaling-β-binning's use of hierarchical logistic regression (random intercepts and slopes per partition, Equation 4) is a principled solution to the key practical challenge that fine-grained partitions may have few data points, allowing information sharing across groups.

5. **Framework generalizes standard calibration.** Setting kd-tree depth d=0 recovers average-case calibration, making β-calibration a true generalization. The hyperparameter d is chosen by optimizing downstream AUAC, providing a practical tuning strategy.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is missing a formal union bound over partitions for the "for all s∈S" condition.** The conditional β-calibration definition (Definition 3) requires the bound to hold simultaneously for all s∈S and all p∈range(h). However, the algorithm trains separate UMD calibrators per partition, each on n_s points. The stated bound ε = √(log(2N/bα)/(2(b-1))) + ν does not include any dependence on |S| (the number of partitions), which would be needed for a union bound over partitions to guarantee the "for all s" condition. Using N (total data) instead of n_s (partition size) is conservative and therefore safe, but the missing union bound over |S| is a genuine gap. This is fixable (adding a log|S| term via standard union bound), but the theorem as stated does not logically follow from the per-partition UMD guarantees as applied. This undermines the claim of a rigorous distribution-free guarantee.

2. **Evaluation uses a proxy for ground truth labels for both training and testing.** The paper uses Llama 3.1 to assess semantic equivalence between generated answers and gold answers, and the AUAC metric is computed "based on a ground truth proxy of y" (line 366). While this semantic-equivalence proxy is standard in generative QA evaluation (following Tian et al. 2023), using the same proxy for both training and evaluation without quantification of its agreement with human judgment creates the risk that results reflect the proxy's biases rather than true calibration quality. The paper should either (a) evaluate on human-verified gold labels for at least one dataset to validate the proxy, or (b) report the proxy's agreement rate with human judgment.

### Minor

3. **Primary metric (CE(h;β)) favors the proposed methods by construction.** The paper acknowledges this ("While the first result, in itself, may not be surprising as our proposed schemes aim to minimize CE(h;β)", Section 5), which is appropriate. However, the selective QA (AUAC) results — the more objective measure — show that the "None" baseline is competitive in some settings (e.g., MMLU Ling1s-Top1 Mistral: HS-BB 0.269 vs. None 0.269, overlapping confidence intervals). The claimed "up to 30% increase in selective answering performance" is not uniformly supported across all settings.

4. **Gap between the motivating example and the actual instantiation.** The paper's running example (User 1 vs. User 2, topical groups like geography/politics/medicine) motivates β as a user-specified topic function. But the instantiation uses a kd-tree on DistilBERT embeddings, producing partitions that are not interpretable to an end user ("group 7 of the kd-tree"). The paper does not address how users could specify or interpret groups relevant to their decision-making.

5. **Limited reporting of sensitivity and diagnostic statistics.** The paper does not report: (a) how many test points fall outside the bounded kd-tree space and thus use the root calibrator, (b) the proportion of partitions that have very few points and how often they are used, (c) the effective number of partitions used after filtering empty/small ones, or (d) the tuned kd-tree depths. These would help assess how much of the β-calibration machinery is actually operational.

### Trivial
- Only 2 of 5 datasets appear in the main table; results for TriviaQA, SciQ, and OpenBookQA are relegated to the appendix. A brief summary of those results in the main text would strengthen the paper.
- The data split (20:60:10:10) is unusual but adequately explained.

## Nice-to-Haves
- An ablation on the choice of embedding model (DistilBERT vs. Sentence-BERT vs. last-layer LM embeddings) for the kd-tree.
- A comparison on standard ECE to verify that β-calibration gains do not come at the cost of average-case miscalibration.
- Qualitative examples showing QA pairs that fall into the same kd-tree leaf, to help ground the interpretability claim.
- Statistical significance testing (e.g., win/loss counts across all datasets×prompts×LLMs) for the AUAC comparisons.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism that Theorem 1 uses N instead of n_s (partition size).** Using N ≥ n_s is conservative (produces a larger ε), so this direction does not invalidate the bound. Removed because it is factually not a flaw — the bound is looser but still valid.

- **Claim that "None is competitive or even better in several cases" on AUAC.** Comparing the best proposed method per setting against None: across all 6 rows in Table 2, the proposed method is either strictly better or tied — never worse. Removed because it is factually wrong.

- **"The bound does not follow from the underlying UMD guarantee."** The UMD bound per partition depends on partition-specific quantities, but the theorem's use of N is a conservative upper bound. The real issue is the missing union bound (captured in Major weakness 1), not the use of N. Removed because this phrasing is imprecise.

- **Concern about proxy labels being an "evidential issue" that could "inflate results."** While the proxy concern is real (Minor weakness 2), the framing as an "evidential issue" is overstated — using a separate LM for semantic-equivalence checking against gold answers is standard practice in generative QA evaluation (Tian et al. 2023, cited by the paper), and the cited entities (Llama 3.1, the benchmark datasets) exist and are properly referenced.

- **"DistilBERT choice is arbitrary, no ablation."** The choice is explained (smaller/faster, rich semantic embeddings — Section 2.3), and an ablation across embedding models would be a nice-to-have but is not a structural weakness. Removed from weaknesses; moved to Nice-to-Haves.

- **"Only 2 of 5 datasets in main table."** The paper clearly states that additional results are in the appendix (Tables S1, S2). Given space constraints, this is within normal practice. Retained as Trivial.

- **Formatting/style nitpicks.** Removed per hard rules.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective on β-calibration that the paper itself does not already articulate.

## Suggestions
1. **Fix Theorem 1** by adding a formal union bound over partitions. The corrected bound should include dependence on |S| (or the total number of bins across all partitions, which is bounded by N/b). Show that log|S| enters logarithmically, so the impact is small in practice.
2. **Validate the proxy.** Evaluate on at least one dataset using the original human-verified gold labels (checking exact match or using a held-out human evaluation) to confirm that results are not artifacts of the Llama 3.1 proxy.
3. **Report diagnostic statistics:** number of test points using the root calibrator, distribution of partition sizes, tuned kd-tree depths, and how often the fallback root calibrator is invoked.
4. **Address the interpretability gap** by either (a) providing qualitative examples of kd-tree leaves, or (b) discussing how a practitioner could define a custom β for their domain.

## Score and Decision

The paper makes a genuine contribution: β-calibration is a principled generalization of calibration that addresses a real need in generative QA. The algorithms are sound, the hierarchical scaling approach is thoughtful, and the empirical results on β-calibration error are striking. The main concern is the theoretical guarantee missing a union bound over partitions — but this is fixable (the log|S| correction is typically small) and does not invalidate the core ideas or the empirical findings. The proxy-label evaluation is standard practice but warrants a sanity check. The AUAC results, while more modest than the CE(h;β) gains, still consistently favor the proposed methods.

This is a solid paper that would benefit from a cleaned-up theoretical statement and a proxy validation. The weaknesses are addressable and do not undermine the paper's overall contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>