Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

This paper makes three contributions: (1) PPIRef, the largest non-redundant dataset of 3D protein–protein interfaces (46K unique interfaces); (2) PPIformer, an SE(3)-equivariant transformer pre-trained via masked modeling on PPIRef; and (3) a thermodynamically motivated fine-tuning procedure for ΔΔG prediction using log-odds ratios that naturally enforces antisymmetry. The paper convincingly demonstrates that existing PPI benchmarks suffer from severe structural leakage, and constructs a clean evaluation setup. The experimental results show PPIformer outperforming ML baselines on non-leaking splits of SKEMPI and two case studies.

## Strengths

1. **PPIRef dataset construction.** The paper builds the largest non-redundant PPI dataset (PPIRef50K, 46K unique interfaces), exceeding DIPS (9K) and MaSIF-search (5K) by a wide margin (Table 1). The exhaustive mining from 202K PDB entries and careful deduplication yields a resource that enables large-scale pre-training not previously possible.

2. **iDist algorithm for scalable deduplication.** iDist is 480× faster than the standard iAlign while achieving 99% precision and 97% recall on near-duplicate detection (Section 3.1). This is a well-validated algorithmic contribution that makes large-scale structural deduplication feasible, and the validation against iAlign on 1,646 PPIs (2.7M pairwise comparisons) is thorough.

3. **Exposure of data leakage in existing benchmarks.** Using iDist, the paper shows that 53–88% of test examples in standard PPI dataset splits have near-duplicates in the training set (Section 3.2). This is a significant finding that identifies a critical flaw in prior evaluations and motivates the need for non-leaking evaluation.

4. **Thermodynamically motivated ΔΔG prediction.** Equation (8) derives ΔΔG from the log odds ratio of wild-type and mutant probabilities, naturally enforcing the antisymmetry property ΔΔG_{wt→mut} = −ΔΔG_{mut→wt}. Prior methods either ignored this symmetry or required two forward passes (Section 4.4). This is conceptually elegant and principled.

5. **Honest assessment of limitations relative to force fields.** The paper openly reports that flex ddG (physics-based) achieves Spearman 0.55 vs. PPIformer's 0.44 and states that "traditional force field simulators...still outperform machine learning methods in terms of predictive performance" (Section 5). This transparency strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

- **The primary test set is small and lacks statistical rigor for strong claims.** The main benchmark (Table 1) evaluates on only 5 held-out PPIs from SKEMPI v2.0. Spearman correlations on 5 complexes can swing substantially depending on which complexes are chosen. The paper reports 3-seed variance for PPIformer but provides no variance for any baseline method, making it impossible to assess whether observed differences between methods are statistically significant. The 183% relative improvement in Spearman (0.24 → 0.44) sounds dramatic, but without confidence intervals or significance tests for baselines, the robustness of this margin is uncertain. The two case studies provide complementary evidence but involve very small numbers of favorable mutations (5 and 6), limiting their statistical weight. This weakens the paper's central claim of "enhanced generalization."

### Minor

- **No ablation of pre-training contribution.** The paper never isolates the contribution of PPIRef pre-training by comparing against a randomly initialized PPIformer fine-tuned directly on SKEMPI. Without this experiment, it is unclear whether the performance gains come from the large-scale pre-training (the paper's stated thesis), the architecture design, the coarse-grained representation, or the thermodynamic fine-tuning objective. Given the small test set, this is a missed opportunity to demonstrate the value of PPIRef directly.

- **Baseline comparisons are informative but not fully controlled.** It is not stated whether ML baselines (e.g., RDE-Network) were retrained on the same non-leaking SKEMPI subsets used for PPIformer. For the SARS-CoV-2 case study, baseline values are explicitly "reproduced from" prior work (Table 2 caption). This confounds model architecture with training data distribution: baselines trained on leaking splits may underperform on non-leaking test data, making the comparison partially about split design rather than model quality. The paper's claim of "superiority" is therefore not as cleanly isolated as it should be. (The paper's honest acknowledgment that flex ddG still outperforms all ML methods partially mitigates this.)

- **No variance reported for any baseline method.** The table reports standard deviations only for PPIformer. Without knowing baseline variance (e.g., from different random seeds or train/test splits), it is impossible to determine whether PPIformer's improvements over GEMME (0.44 vs. 0.38 Spearman) or other baselines are statistically meaningful.

- **The log-odds estimator assumes unchanged backbone geometry.** The method feeds the same wild-type complex structure for both wild-type and mutant predictions (masking the mutated residue). This assumes backbone geometry is unchanged upon mutation, which can be inaccurate for mutations that induce structural rearrangements. While the coarse-grained representation is designed for robustness, this limitation is not discussed or tested (e.g., by comparing with methods that allow side-chain repacking).

### Trivial

- **The iDist threshold value** used for deduplication is described as "estimated to approximate iAlign" but the numerical threshold is not reported in the main text (likely deferred to a figure or appendix stripped by the parser).

## Nice-to-Haves

- Expand the benchmark via cross-validation folds that respect PPI-level non-redundancy, producing a larger test set and enabling bootstrapped confidence intervals.
- Retrain all ML baselines on the same non-leaking training folds for a controlled comparison.
- Perform an ablation: fine-tune PPIformer from random initialization (no PPIRef pre-training) to quantify the contribution of the pre-training dataset.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. *"The 100 PDB code sample comes from DIPS—which is itself biased. A more convincing validation would sample from the full PDB."* — DIPS is the standard PPI dataset; using it for validation of iDist against iAlign is appropriate. The critic offers no specific evidence of bias that would affect the validation. **Removed.**

2. *Criticism about missing appendix details (hyperparameters, training steps, etc.)* — The parser strips appendix content from all papers; these details exist in the original submission. **Removed per hard rule.**

3. *"The values for the SARS-CoV-2 case study show PPIformer detects only 2/5 favorable mutations in top-10% while RDE-Network detects 3" as a weakness* — The paper transparently reports this and discusses it honestly ("PPIformer is superior in prioritizing favorable mutations among random ones but does not prioritize 5 annotated mutants as high as..."). This is not a weakness the paper hides. **Removed.**

4. *"Random chance could place a favorable mutation at rank 1 with probability roughly 5/494 ≈ 1%"* — This conflates the probability of any favorable mutation being rank 1 (5/494) with getting a specific favorable mutation at rank 1, and ignores that the model achieves this consistently across different settings (also P@1=100% on staphylokinase). The paper's P@1 result is legitimate evidence. **Removed.**

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-cutting observation from the reviews is the tension between the paper's two main claims: (a) that leakage inflates prior ML scores, and (b) that PPIformer achieves superior generalization. Claim (a) is very well supported. But the evidence for (b) is partially confounded because the baselines whose scores are "deflated" by the non-leaking test may simply have been trained on different (leaking) data. The paper would benefit from explicitly separating these claims and designing experiments that isolate each.

## Suggestions

1. **Run a pre-training ablation** — fine-tune PPIformer from random initialization on the same SKEMPI non-leaking splits and compare performance. This directly quantifies the benefit of PPIRef pre-training.
2. **Retrain RDE-Network (or equivalent) on the exact same non-leaking SKEMPI subsets** used for PPIformer, or clearly specify why this was not done and how it would affect conclusions.
3. **Report variance for all baselines** — if multiple runs are not feasible (e.g., for published results), at minimum report per-complex breakdowns and bootstrap confidence intervals.
4. **Discuss the structural change limitation** explicitly — the assumption of unchanged backbone geometry upon mutation, and how the coarse-grained representation mitigates or fails to mitigate it.
5. **Report the iDist threshold value** in the main text or a centralized table for reproducibility.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>