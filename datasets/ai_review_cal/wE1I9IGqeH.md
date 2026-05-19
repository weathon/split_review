- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes a two-system architecture for continual learning in open-vocabulary image classification, inspired by complementary learning systems (CLS) theory. The slow system is a frozen CLIP model preserving zero-shot ability; the fast system is an exemplar-based model that can be efficiently updated. Two main contributions are presented: (1) **Tree Probe** — a hierarchical clustering of exemplars with per-leaf linear classifiers achieving near-constant update time and accuracy competitive with full linear probing; (2) **Adaptive Instance Marginalization (AIM)** — using CLIP's zero-shot confidence over exemplar labels to adaptively weight predictions from the two systems. Experiments across data-incremental, class-incremental, task-incremental, and flexible inference scenarios show strong performance and substantial training speedups (6–25×) over linear probe and fine-tuning baselines, including state-of-the-art results on the ZSCL benchmark.

## Strengths

1. **Tree-probe achieves near-linear-probe accuracy with dramatically faster training** — In task-incremental learning (Fig. 3), TreeProbe (50k) obtains target-task accuracy comparable to LinProbe while reducing cumulative training time by 25×; TreeProbe (100k) matches LinProbe with a 6× speedup. This directly substantiates the paper's central efficiency claim.

2. **AIM improves both seen and unseen class accuracy under class-incremental learning** — Fig. 2(b) shows AIM-Emb maintains reasonable unseen-class accuracy (~50% at 40% of classes) while outperforming Avg-Emb on overall accuracy at all stages. This demonstrates that adaptive weighting using CLIP's zero-shot confidence enables effective open-vocabulary continual learning, not just task-incremental performance.

3. **State-of-the-art results on the ZSCL benchmark without per-task hyperparameter tuning** — Table 2 shows TreeProbe (50k) outperforms ZSCL on Average, Average+Novel, and Transfer metrics while using less GPU memory. The paper explicitly notes it did not perform per-task hyperparameter selection, strengthening the practical utility claim.

4. **Fused system maintains zero-shot performance throughout continual learning** — In task-incremental learning (Fig. 2c), CLIP+LinProbe (AIM-Emb) consistently exceeds CLIP zero-shot on target tasks without degrading zero-shot accuracy across all stages. This operationalizes the paper's goal of achieving all three desiderata (flexible inference, continual improvement, efficient learning) simultaneously.

5. **Scalability to larger CLIP models** — Table 3 shows TreeProbe improves target-task accuracy over CLIP zero-shot for ViT-B/32, ViT-L/14, and ViT-H/14 (e.g., +3.8% on targets for ViT-L/14) with negligible change on zero-shot tasks, demonstrating generality across model sizes.

## Weaknesses

### Fatal
None.

### Major

1. **AIM-Prob vs. AIM-Emb inconsistency between method description and experiments** — Section 3.3 introduces AIM-Prob (Eq. 3) as the "final" fusion method, which multiplies and renormalizes the zero-shot and exemplar probabilities. Yet all experiments in Section 5 use the embedding-based AIM-Emb (adaptive α applied to Eq. 2). AIM-Prob is never evaluated, and no rationale is given for choosing one variant over the other. While the core adaptive-weighting idea is validated through AIM-Emb, this discrepancy undermines the coherence between the claimed contribution and the evidence. The authors should (a) clarify which variant is used and why, (b) provide an ablation comparing AIM-Prob, AIM-Emb, and fixed-weight baselines, or (c) commit to one as the primary method with justification.

2. **Missing ablation of tree probe's ensembling mechanism** — The paper states (line 157) that tree probe uses an ensemble of classifiers from the *k* nearest neighbors' leaf nodes "to avoid non-smooth predictions near cluster boundaries," but never ablates this choice against the simpler single-leaf assignment. The value of *k* is also never specified. Without this, it is unclear how much of tree probe's accuracy is due to the hierarchical structure vs. the ensembling step. An ablation varying *k* and comparing single-leaf vs. ensemble would clarify the contribution of each component.

### Minor

1. **Flexible inference only evaluated after task-incremental training** — The well-motivated flexible inference scenarios (Zero-shot, Union+Zero-shot, Mix+Zero-shot) are only tested in the task-incremental setting (Section 4, line 234). Since AIM's adaptive weighting is most critical when label coverage varies — which happens in data-incremental and class-incremental settings — evaluating flexible inference in those scenarios would strengthen the generality claims.

2. **Reproducibility gaps in tree probe details** — The following are not specified: (a) the value of *k* used for the tree probe nearest-neighbor ensemble and for KNN baselines; (b) the distance metric and KMeans initialization used for tree node splits; (c) the number of KMeans iterations. These details affect both reproducibility and the precise complexity analysis.

3. **No error bars or variance estimates** — Results are reported as single-point estimates without standard deviations across runs or data splits. Given variability in continual learning schedules, this omission weakens the precision of the reported comparisons.

### Trivial

- The paper uses "LinProb" (line 254) and "LinProbe" (line 254, elsewhere) interchangeably, which is minor but could cause confusion.

## Nice-to-Haves

- Ablation comparing AIM-Prob vs. AIM-Emb vs. uniform averaging vs. learned weighting would directly strengthen the central claim about the fusion mechanism.
- Analysis of when AIM's adaptive weighting fails (e.g., when CLIP's *p*(*y*∈**Y**ₑ|*I*) is miscalibrated, or on classes with very few exemplars) would deepen understanding of the method's failure modes.
- Comparison with more recent CLS-inspired continual learning approaches such as DualNet or CLS-ER on the same benchmarks would help contextualize the advantages of the proposed architecture.
- Results with a non-ViT backbone (e.g., ResNet-based CLIP) would assess generality across encoder architectures.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Claim that AIM was only tested with LinProbe** (Harsh Critic #3, first sentence) — **FACTUALLY WRONG**. Section 5.2 explicitly states: "we perform a thorough analysis of different complementary models using AIM on their performances and efficiency: CLIP+KNN, CLIP+LinProbe and CLIP+TreeProbe" (line 272–273). AIM is evaluated with all three backends in Fig. 3.

2. **Claim that ZSCL per-task hyperparameter tuning disadvantages ZSCL in the comparison** (Harsh Critic, Section-by-section notes) — The paper openly acknowledges that ZSCL used per-task tuning (line 286–287) while the proposed method did not. Since the proposed method still outperforms ZSCL, this is a strength, not a weakness.

3. **Critique of the efficiency complexity analysis** (Harsh Critic #2) — The paper's claim of O(ψ + log *n*) per-insertion complexity is correct. Split costs (O(ψ) per split event, occurring every ψ insertions amortized) do not change the asymptotic per-insertion analysis. The paper's characterization is reasonable.

4. **Question about ZSCL performance degradation** (Harsh Critic, Experimental Results section) — The paper shows ZSCL's degradation as an empirical finding (Fig. 2c, line 263). This is an observation about the baseline, not a weakness of the proposed method.

5. **Critique about tree probe novelty claim** (Harsh Critic, Section-by-section notes) — The paper already hedges by saying "we are not aware of this specific method being proposed" (line 39) and connects to the lazy learning literature. This claim is appropriately scoped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the AIM-Prob/AIM-Emb inconsistency**: Either rename the "final" method to AIM-Emb and relegate AIM-Prob to a discussed variant, or evaluate both and justify the choice. This is the most pressing fix.

2. **Add tree probe ensembling ablation**: Compare single-leaf assignment vs. *k*-NN ensemble with different *k* values. This would clarify how much of the accuracy gain comes from ensembling vs. the hierarchical structure itself.

3. **Specify missing reproducibility details**: Report the *k* value for both KNN and tree probe, the distance metric and KMeans settings for node splits, and ideally provide hyperparameters in a single table.
