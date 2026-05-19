- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 5, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces a new setting, Multi-Model Source-Free Video Domain Adaptation (MSFVDA), where a target user has access to multiple pre-trained source video models (with diverse architectures, from multiple source domains) but not the source data. The authors propose the MSVMA framework with two key modules: (1) Multi-level Instance Transferability Calibration (MITC), which refines uncertainty-based instance-level transferability estimates by incorporating group-level and dataset-level scale information, and (2) Instance-level Multi-Video Model Aggregation (IMVMA), which uses the calibrated transferability to guide a path generation network that assigns instance-specific weights for unsupervised aggregation. Experiments on three video domain adaptation benchmarks (Daily-DA, UCF-Sports1M, UCF-HMDB_full) show consistent improvements over existing SFDA, MSFDA, and SFVDA methods.

## Strengths

- **Novel problem formulation with practical relevance.** The MSFVDA setting is a natural and underexplored extension of SFVDA that reflects real-world scenarios where multiple pre-trained models from different sources are available. The paper is the first to address this setting in the video domain, and the problem framing is clear and well-motivated.

- **Strong empirical evidence for improved transferability estimation.** Table 1 shows that MITC achieves substantially higher Spearman rank correlation with target-domain cross-entropy loss than existing distribution-induced and uncertainty-based methods (e.g., +0.268 on Daily-DA, +0.033 on UCF-HMDB_full over the best prior method). This directly validates the core claim that multi-level calibration enables more accurate cross-model instance-level transferability estimation.

- **Consistent state-of-the-art adaptation accuracy.** The full MSVMA framework outperforms all compared baselines (SHOT, STHC, DECISION, CAiDA, KD3A) across benchmarks. On the challenging Daily-DA dataset, it achieves a 4.29% average accuracy improvement over the second-best method and 21.84% over the average of individual source models (Table 2). On UCF-Sports1M and UCF-HMDB_full, it improves over the best aggregation model by 0.55% and 3.69% respectively.

- **Instance-level aggregation surpasses the best single model (Oracle).** Table 4 demonstrates that instance-specific path weights guided by MITC outperform the best individual source model by up to 8.52% on M→A and 6.25% on A→H tasks. This is stronger than a fixed-weight multi-model baseline and goes beyond what any single pre-trained model can achieve, confirming the value of instance-level aggregation.

- **Systematic ablation and analysis of design choices.** The paper ablates the multi-level calibration structure (Table 3), the effect of path selection and weight correction (Table 4), the number of aggregated models (Figure 4b), and shows MITC's robustness across different uncertainty metrics (entropy, temporal consistency, spatial consistency in Figure 3a).

## Weaknesses

### Fatal
None.

### Major
- **No variance or uncertainty reporting for experimental results.** All results in Tables 1–4 and ablation studies are reported as single numbers without standard deviations, confidence intervals, or replication across multiple runs. This is particularly problematic for evaluating the reliability of modest improvements (e.g., +0.022 Spearman on Sport-DA, +0.09 average gain from group-level calibration in Table 3). The one case where a very large improvement appears (M→A: 33.24→49.70 in Table 2) is especially difficult to assess without variance. While single-run evaluation is common in this field, the absence of any statistical grounding weakens confidence in the claimed improvements.

### Minor
- **Baseline adaptation procedures are underspecified.** The paper lists SHOT, STHC, DECISION, CAiDA, and KD3A as primary baselines but does not explain how single-model methods (SHOT, STHC) are configured for the multi-model setting (e.g., applied per-model then selected/aggregated, and if so, how). For the MSFDA methods (DECISION, CAiDA, KD3A) that require source data, how they are adapted to the source-free setting is not clarified. This gap makes it difficult to assess whether comparisons are fair or whether the proposed method benefits from the comparison design.

- **Calibration function form lacks justification and ablation.** The specific function Φ(a,b) = (a/a_norm)(1+ln(1+b)) (Equation 1) is proposed without comparison to alternative forms (e.g., multiplicative-only scaling, linear combination, different non-linearities). While the multi-level structure is ablated (Table 3), the choice of the functional form itself is not validated, leaving the question of whether the particular expression is critical or incidental.

- **Group-level transferability formulation is thinly validated.** Group-level transferability is defined as the maximum distance between a sample and its k nearest neighbors in feature space, justified in one sentence as reflecting class separation. No analysis, visualization, or sanity check is provided to confirm that this quantity behaves as claimed across models with different architectures. Given that the full MITC depends on this intermediate level, the lack of validation weakens trust in the overall calibration pipeline.

- **Per-task degradations are acknowledged but not explained.** In Table 3, adding group-level calibration actively hurts performance on three tasks (H→A, H→M, M→H). In the H→M task of Table 2, the full MSVMA is worse than the version without instance-level weighting (24.60 vs. 27.60). The paper acknowledges these cases but provides only high-level speculation ("fine-grained transferability estimation is crucial") rather than mechanistic analysis of why group-level information backfires on certain domain pairs.

- **Hyperparameter sensitivity is not analyzed.** Key hyperparameters (τ for the SUTE rejection threshold, k for top-k model selection, k for group-level nearest neighbors, θ₁ for loss trade-off) are introduced without any sensitivity study. Figure 4b shows that performance varies with the number of aggregated models, yet no analysis shows whether the chosen values (top-3 selection, top-2 activation) are robust across domains.

### Trivial
- Some figure references in the text are imprecise (e.g., "Figure 3(b)" references a model count plot in what is captioned as Figure 4), and the D→A task abbreviation is inconsistently introduced.

## Nice-to-Haves

- A controlled baseline where model weights are set uniformly (1/k) but with the same top-k selection as MITC-guided aggregation (Table 4 currently compares MITC-guided weighting against fixed-weight/no-selection variants but not against uniform weighting of the top-k).
- Qualitative analysis of the path generation network's behavior, showing examples where different source models are activated for different instances and arguing why the assigned weights are sensible.
- Synthetic experiments where ground-truth instance-level transferability is known (e.g., corrupting specific source models on specific instance types) to directly validate the calibration function independent of the downstream aggregation task.

## Removed Points

These points were flagged by reviewers but are excluded from the main evaluation for the following reasons:

- **Ground-truth transferability proxy in Table 1 is "questionable"** (Harsh Critic Point 3). The critic argues that cross-entropy loss conflates "performance" with "transferability." However, using cross-entropy loss on the target domain as a ground-truth evaluation signal is a standard protocol in transferability estimation literature. The critic's concern about "complementary errors" is speculative and not grounded in any evidence or citation. Removed as a misunderstanding of standard evaluation methodology.

- **Missing implementation details / appendix content.** Criticisms about implementation details being deferred to supplementary materials, and about "Tables 1 and 2 in the supplementary materials" causing confusion. The PDF parser strips supplementary sections; these details exist in the original submission. Removed per hard rules.

- **Kinetics exclusion "poorly explained."** The paper states: "We excluded Kinetics from our experiments AS the pre-trained models we used from the mmaction2 framework were pre-trained on Kinetics-400." This is a clear justification — a model pre-trained on Kinetics-400 cannot be evaluated on Kinetics as a target domain due to data overlap. Removed.

- **"MSFVDA conflates multiple models with multiple source domains"** (from Section-by-Section). The paper explicitly defines the setting as having multiple source domains, each providing a zoo of models. The critic's concern about the setting "equally applying to multiple models from the same source domain" does not contradict the paper's framing. Removed as scope creep.

- **Pure formatting/style nitpicks** and grammar complaints. These are parser artifacts, not author errors. Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful observations about gaps in experimental rigor (no error bars, underspecified baselines) but do not identify any fundamentally novel angle on the problem that the paper itself misses.

## Suggestions

1. **Report error bars.** Re-run all experiments at least 3 times with different random seeds and report mean ± std. This is critical for the modest improvements and for the one anomalously large gain (M→A: 33.24→49.70).

2. **Specify baseline adaptation protocols.** Clearly state how each baseline method (especially single-model SFVDA methods like SHOT, STHC) is adapted to the multi-model setting, and how MSFDA methods (DECISION, CAiDA, KD3A) operate without source data.

3. **Ablate alternative calibration function forms.** Compare the proposed Φ against simpler alternatives (e.g., a/a_norm only, or a linear combination a/a_norm + b/b_norm) to justify the specific logarithmic design.

4. **Add hyperparameter sensitivity analysis.** Report performance over a range of values for τ, k (top-k selection), and θ₁ to demonstrate robustness.

5. **Explain per-task failures.** Provide analysis (e.g., feature space visualization, per-class accuracy breakdown) for the cases where group-level calibration or the full framework underperforms simpler variants (H→A, H→M, M→H).
