- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper studies class-incremental continual learning for multi-view clustering (MVC)—a novel problem formulation where multi-view data with new semantic classes arrive sequentially and the model must cluster all seen classes without task identifiers at test time. The authors propose CCMVC, which operates in two phases: Multi-view Cluster Search (MCS) learns GMM-based clusters for the current task with cross-view contrastive losses, and Multi-view Cluster Consolidation (MCC) performs continual component expansion plus self-supervised data replay and a cross-view synchronous loss to mitigate forgetting and asynchronous view convergence. Experiments on six datasets show large improvements over adapted baselines.

## Strengths

- **First dedicated solution for a meaningful, underexplored problem.** The paper convincingly demonstrates (Figure 1a) that existing MVC methods suffer catastrophic forgetting when applied to class-incremental scenarios, and that single-view continual clustering methods cannot handle multi-view heterogeneity. Formulating this problem and providing a proof-of-concept method is a genuine contribution.

- **Well-motivated architectural design with complementary components.** The two-phase design (MCS for within-task clustering, MCC for cross-task consolidation) is clearly motivated by the two challenges (catastrophic forgetting, asynchronous view convergence). The cross-view dual-anchor contrastive losses (sample-anchor and cluster-anchor, Eqs. 3–8) are a principled way to align generative probabilities across views using GMM outputs as features.

- **Cross-view synchronous loss shows clear empirical benefit.** The ablation study (Table 4) demonstrates that removing \(\mathcal{L}_{syn}\) causes substantial performance drops (e.g., Fashion A₅ from 0.479 to 0.418), and Figure 1(b) provides visual evidence that the loss maintains feature alignment across views during continual learning.

- **Empirical gains are large and consistent across six datasets.** CCMVC outperforms all baselines on every dataset, with improvements on the final task ranging from +0.089 (Caltech-2V) to +0.358 (Fashion) over the second-best method. Per-task accuracy heatmaps (Figure 3) show that gains are concentrated on earlier tasks, confirming that the replay mechanism mitigates forgetting.

## Weaknesses

### Fatal
None.

### Major

- **No measures of variance reported, making gains uninterpretable.** The paper states results are "mean accuracy ... of 10 runs" (Section 5.2), but no standard deviations, confidence intervals, or significance tests are provided anywhere. Given the stochasticity of clustering initialization, GMM optimization, and replay buffer sampling, variance could be substantial. Without it, the reader cannot assess whether the observed margins are robust—especially for moderate gaps (e.g., Caltech-4V: 0.760 vs. 0.662, Δ≈0.1).

- **Implausibly large gaps on some datasets without evidence that baselines are properly tuned.** On Fashion (10 classes), CCMVC scores A₅=0.479 while the strongest replay-equipped baseline (JCT+EWC+replay) scores 0.121—barely above random (10%). On MNIST-USPS, the gap is 0.214 (0.698 vs. 0.484). These baselines use "the same task memory in our CCMVC" (Section 5.2), so the near-random performance of replay-based methods is suspicious and suggests either poor hyperparameter tuning or a mismatch between the baseline architecture and the multi-view setting. The paper reports no hyperparameter search or tuning procedure for any baseline, so the reader cannot assess whether the comparisons are fair. A method claiming to improve accuracy from 12% to 48% in a 10-class problem bears a heavy burden of proof.

- **Cross-view synchronous loss lacks diagnostic validation of its core assumption.** Equation (12) (ℓ_syn) uses a supervised contrastive loss where positive pairs are determined by pseudo-labels from memory. The paper provides no analysis of pseudo-label quality, no tracking of agreement rates between pseudo-labels and ground truth over tasks, and no study of how label errors propagate through the synchronous loss during continual learning. The ablation shows the loss helps empirically, but the claimed mechanism—"balancing learning rhythm across views"—is not directly evidenced. Without diagnostic analysis (e.g., tracking feature alignment across views with/without ℓ_syn over the task sequence), the mechanism remains plausible but unverified.

- **Critical experimental details missing, harming reproducibility and assessment of difficulty.** The paper does not specify: (a) the number of tasks per dataset, (b) how many classes each task contains, (c) the values of hyperparameters (τ_s, τ_c, τ_v, N', learning rate, optimizer, epochs per task), or (d) the memory replacement policy (only "randomly push N' samples" is stated). These omissions make it impossible to reproduce the results or assess the difficulty of the continual learning scenario.

### Minor

- **Memory replacement policy is underspecified.** The paper states samples are "randomly push[ed]" into memory (Section 4.2), but does not describe the eviction policy when the memory budget is reached. Since baselines use the same memory setup, this ambiguity affects fairness assessment.

- **How |C_t| (number of clusters per task) is determined is not stated.** In class-incremental learning this is typically given by the protocol, but the paper should state it explicitly for reproducibility.

- **CVS baseline's poor performance is explained but not verified.** The paper attributes CVS's poor performance to "neglect of view heterogeneity" (Section 5.3). However, it is unclear whether CVS was adapted for multi-view data (e.g., by concatenating features or processing per view). A brief clarification of the adaptation procedure would strengthen confidence in the comparison.

- **Ablation study is standard but could be more informative.** While the component-level loss ablation (Table 4) confirms each term's contribution, the paper would be strengthened by ablating higher-level design choices (e.g., using a fixed vs. expanding component pool, or removing the cross-view synchronous loss during MCS). The current ablation does not isolate whether the key novelty (class-incremental MVC with view synchronization) drives the gains or whether a simpler combination of existing techniques could match performance.

### Trivial
None.

## Nice-to-Haves

- A diagnostic study tracking average feature similarity between views over tasks with and without ℓ_syn would directly validate the claimed synchronization mechanism.
- Reporting pseudo-label accuracy on the memory buffer across tasks would address concerns about error propagation.
- Varying the number of tasks or memory size would demonstrate robustness under different resource constraints.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Privacy motivation inconsistency"** (Harsh Critic): The paper mentions privacy as one motivation among several for limited data access, then uses a memory buffer. This is a standard framing in rehearsal-based continual learning and not an actual inconsistency. (Minor framing choice, not a weakness.)
- **"Joint Training clarification needed"** (Harsh Critic): The paper already states Joint Training "is trained from scratch on all past training sets jointly, using the model and loss as the same as our multi-view cluster search." This is sufficiently clear.
- **"Ablation study is too narrow"** (Harsh Critic's framing): The paper's ablation already covers all loss components (including the cross-view contrastive losses in MCS and the replay/synchronous losses in MCC). The critic's specific examples (no cross-view contrastive in MCS, no memory) are already tested by w/o L_con^sa, w/o L_con^ca, and w/o L_rpl. The ablation is standard and adequate for a component analysis. I have included a softened version (wishing for higher-level ablations) under Minor.
- **"Single-view continual clustering methods not discussed in enough detail"** (Harsh Critic): The paper cites and discusses the key single-view continual clustering works (Rao et al., 2019; Kumar et al., 2021a; Korycki & Krawczyk, 2021) in Section 2. The level of coverage is appropriate for a paper focused on multi-view clustering.
- **"Could the metric be measuring a proxy?"** (implied speculative critique): No concrete evidence for this speculation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report standard deviations for all main results.** This is the single highest-leverage improvement—without it the reported gains are statistically uninterpretable.
2. **Strengthen baseline credibility.** Either report the hyperparameter search procedure used for each baseline, or include an additional strong baseline (e.g., DER+replay adapted to multi-view via feature concatenation) and show that tuning does not close the gap.
3. **Add diagnostic analysis for the cross-view synchronous loss.** Track average cosine similarity between view features for same-class samples across tasks with and without ℓ_syn. This would directly validate the claimed "balancing" mechanism.
4. **Provide full experimental details in a supplementary table:** task splits (classes per task, number of tasks), all hyperparameter values (τ_s, τ_c, τ_v, N', learning rate, optimizer, epochs), and memory management protocol (selection and eviction policy).
