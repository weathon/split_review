Now I have verified all the key claims against the paper. Let me produce the final consolidated review.

Here is my analysis of the critical issues:

**1. 183% error**: VERIFIED. Spearman: RDE-Net. = 0.24, PPIformer = 0.44. True relative improvement = (0.44-0.24)/0.24 ≈ 0.83 = 83%. The paper's claim of 183% is indeed wrong.

**2. 5 held-out PPIs**: The paper mentions "non-leaking cross-validation split" but the reported results focus on 5 PPIs (these are described as "outliers set aside to obtain 5 additional distinct test folds"). The cross-validation results likely appear in the appendix (stripped). So this weakness is partially addressed but the reported headline results are on only 5 PPIs.

**3. Baseline retraining**: Not explicitly stated in the main text. Valid concern.

**4. iDist validation against iAlign**: The paper does provide a sensitivity analysis of the threshold (the 1.5× relaxation experiment). This partially addresses the concern about threshold choice.

**5. Pre-training ablation**: No such experiment in the paper. Valid concern.

---

## Summary

This paper makes three contributions: (1) PPIRef, the largest and first non-redundant dataset of 3D protein-protein interfaces (322K structures, 46K unique interfaces); (2) iDist, a fast algorithm for PPI deduplication achieving 480× speedup over iAlign with 99% precision and 97% recall; and (3) PPIformer, an SE(3)-equivariant transformer pre-trained on PPIRef via masked modeling and fine-tuned via a log-odds ratio for ΔΔG prediction. The paper also identifies substantial data leakage in existing PPI benchmarks and evaluates on non-leaking splits.

## Strengths

1. **Largest non-redundant PPI dataset**: PPIRef (322K structures, 46K unique interfaces) is 5–8× larger than prior datasets like DIPS (40K/9K) and MaSIF-search (6K/5K), as shown in Table 1. The deduplication via iDist removes redundancy that plagued earlier efforts, and the scale enables large-scale pre-training.

2. **iDist algorithm enables previously infeasible deduplication**: iDist achieves 480× speedup over the gold-standard iAlign while retaining 99% precision and 97% recall on near-duplicate detection (Section 3.1). This is what makes PPIRef's construction feasible and also enables systematic detection of data leakage in existing PPI splits — a finding that has independent methodological value.

3. **Non-leaking evaluation reveals overestimation in prior work**: The paper quantifies that 53–88% of test examples in standard DIPS splits have near-duplicates in training data (Section 3.2), and constructs non-leaking splits. On these splits, many ML methods' performance drops considerably, while PPIformer shows more robust generalization.

4. **Strong practical performance on case studies**: PPIformer achieves perfect P@1 (top rank for a favorable mutation) on the SARS-CoV-2 antibody dataset (Table 3) and identifies 2/6 strongly favorable staphylokinase mutations as top-2 candidates, with P@5% of 75% vs. 50% for RDE-Network (Table 4). These go beyond synthetic benchmarks into realistic design scenarios.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation isolating the pre-training contribution**: The paper presents PPIRef pre-training as a core contribution (it is the first letter of the paper's title), yet no experiment compares PPIformer (a) without pre-training, (b) pre-trained on a smaller dataset like DIPS, or (c) with a different masking/pretraining strategy. Without this, it is impossible to attribute test-set performance to the PPIRef pre-training rather than to the Equiformer architecture or fine-tuning protocol. The comparison against RDE-Network (which also uses structure-based pre-training) helps but does not isolate the effect of PPIRef's scale. This omission is significant given how prominently pre-training is featured.

### Minor

1. **Numerical error in headline claim**: The paper states "a 183% relative improvement in mutation ranking compared to the state-of-the-art supervised RDE-Network, as measured by Spearman correlation." From Table 2, Spearman values are 0.24 (RDE-Network) and 0.44 (PPIformer). The true relative improvement is (0.44−0.24)/0.24 ≈ 83%, not 183%. This overstates the advantage by a factor of two. The 83% improvement is still respectable and worth reporting accurately.

2. **Main SKEMPI evaluation rests on only five held-out PPIs**: The headline results in Table 2 averages over 5 PPIs set aside as outliers. While the paper mentions a non-leaking cross-validation split (likely in the appendix), the subset reported in the main text is very small. Standard deviations for PPIformer (Spearman ±0.03) suggest variability, and no variances are reported for baselines. A more comprehensive evaluation — even a summary of the full cross-validation — would substantially strengthen the generalization claim.

3. **Unclear whether supervised baselines were retrained on the same non-leaking splits**: The paper does not state whether RDE-Network (a primary ML baseline) and other supervised methods were retrained on the paper's new non-leaking split or used published weights trained on leaky splits. If the latter, the comparison may unfairly penalize these methods. This should be clarified.

4. **Pre-training–fine-tuning connection is motivated but not validated**: The paper connects the log-odds ratio to ΔΔG (Section 4.4) and argues that pre-training learns correlates of binding energies. This is presented as a "key insight" but is not validated (e.g., by checking whether pre-training loss correlates with known ΔG values). The paper could proceed without this motivational framing, but the physics-informed language overstates what is actually an empirical design choice.

### Trivial

1. **Slightly imprecise dataset size claim**: The paper describes PPIRef as "one order of magnitude larger" than alternatives. Raw counts: 322K vs 40K (DIPS) ≈ 8×, unique interfaces: 46K vs 9K ≈ 5×. Neither is quite a full order of magnitude (10×). The phrasing should be tightened.

2. **Staphylokinase case study contrast with MSA Transformer**: The paper emphasizes PPIformer prioritizing 2/6 favorable mutations as top-2, but MSA Transformer achieves the same P@1 (100%) and identical recall at top ranks for some mutations. The advantage is real at higher cutoffs (P@5%, P@10%) but the contrast is less sharp than the summary suggests.

## Nice-to-Haves

- A pre-training ablation (random init → fine-tune vs. PPIRef pre-train → fine-tune) would directly validate the value of PPIRef.
- A sensitivity analysis showing how downstream performance varies with the iDist deduplication threshold.
- Reporting baseline variances for the 5-PPI evaluation, even if computed via bootstrap.

## Removed Points

- **"iDist validation against iAlign is circular"**: Removed. The paper is benchmarking iDist's approximation of a well-established similarity measure (iAlign/TM-score), which is standard practice. The paper also provides a threshold sensitivity analysis (relaxing threshold 1.5× changes DIPS connectivity), partially addressing threshold-choice concerns. The question of whether iAlign's threshold is the "right" one for deduplication is a domain question the paper cannot fully resolve, and the criticism misunderstands what the benchmark is designed to show.
  
- **"Missing limitations section"**: Removed. The paper explicitly discusses that flex ddG outperforms ML methods ("this non-leaking evaluation reveals that traditional force field simulators... still outperform machine learning methods"). The reviewer's suggestion for a formal "Limitations" section is a stylistic preference, not a substantive gap.

- **"Reproducibility: iDist details insufficient"**: Removed per hard rules — the appendix (stripped by the parser) likely contains implementation details. The paper described the algorithm conceptually (SE(3)-invariant representations via message passing), which is appropriate for the main text.

- **"Missing related works"**: Removed per instructions.

- **"Formatting/typo complaints"**: Removed per instructions.

## Novel Insights

The review surfaces a tension that the paper does not fully resolve: the pre-training on PPIRef and the iDist deduplication are presented as enabling each other (you need deduplication to build PPIRef, and you need PPIRef to pre-train), yet without an ablation, there is no evidence that the deduplication-driven scale of PPIRef matters more than simply having any large (even redundant) set of PPI structures. This loop — dedup enables dataset, dataset enables model — is the paper's core narrative, and the missing ablation leaves it unclosed. A clean comparison of PPIformer pre-trained on PPIRef50K vs. PPIRef300K (the non-deduplicated version) would be particularly informative and is a sharper experimental test than a random-init baseline.

## Suggestions

1. Correct the 183% claim to the true 83% relative improvement.
2. Add a pre-training ablation: compare PPIformer (random init → fine-tune) vs. PPIformer (PPIRef pre-train → fine-tune). Even better, compare PPIRef50K vs. PPIRef300K pre-training to isolate the value of deduplication.
3. Clarify whether all supervised baselines were retrained on the paper's non-leaking splits or used published weights.
4. Report cross-validation results (not just the 5 held-out outliers) in the main text or supplement available for review.

---

**Overall Assessment**: The paper's dataset (PPIRef) and deduplication tool (iDist) are solid contributions with clear value to the PPI community regardless of the model results. The PPIformer model is a sensible application of existing equivariant architectures and demonstrates genuine improvements in generalization on non-leaking splits and practical case studies. The main weakness is the absence of a pre-training ablation, which prevents attributing gains to PPIRef's scale/deduplication vs. the architecture itself. The numerical error (183%) should be corrected. The paper's contributions are sufficient for publication, but the pre-training claims would be substantially strengthened by the recommended ablation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>