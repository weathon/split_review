Now I have all the information needed. Let me produce the final consolidated review.

## Summary

MARS proposes a federated learning backdoor defense that introduces "backdoor energy" (BE), a neuron-level measure meant to be more tightly coupled with backdoor intent than existing empirical statistical measures (norms, OOD scores, consistency). It extracts the top BE values per layer into a "concentrated backdoor energy" (CBE) vector and uses Wasserstein-distance-based K-Means clustering to separate benign from backdoored models. The paper evaluates against 3 SOTA attacks and 8 SOTA defenses across 3 datasets, reporting consistent superiority.

## Strengths

1. **Principled detection via backdoor energy**: Unlike prior defenses that rely on loosely coupled empirical statistics (norms, OOD detection, cosine consistency) which SOTA attacks can mimic, BE directly measures a neuron's association with the backdoor objective. The paper convincingly demonstrates (Figure 2) that existing statistical measures fail against 3DFed, while BE-based detection succeeds. The upper bound derivation (Theorem 1) provides a reasonable theoretical grounding for a practical, data-free approximation.

2. **Consistent and significant empirical superiority**: In Table 2, MARS outperforms all 8 existing defenses across 3 datasets (MNIST, CIFAR-10, CIFAR-100) and 3 SOTA attacks (MRA, CerP, 3DFed). The improvement is often dramatic — e.g., against 3DFed on CIFAR-10, MARS achieves 98.36% CAD while the best prior defense (FedCLP) reaches only 68.61%. No other defense maintains both high accuracy and low ASR across all attack–dataset combinations.

3. **Novel Wasserstein-distance clustering**: K-WMeans addresses the element-order sensitivity problem of Euclidean/cosine distances for CBE vectors. The toy example (Table 1) concretely demonstrates that Wasserstein distance correctly groups backdoor models together while standard metrics fail, providing clear intuition for the design choice.

4. **Principled cluster selection without majority assumption**: MARS selects the cluster with the smaller center norm rather than assuming benign clients are the majority, validated across attacker ratios from 0% to 95% (Table 5). The inter-cluster Wasserstein distance threshold handles the benign-only scenario by accepting both clusters when distances are small.

## Weaknesses

### Fatal
None.

### Major

1. **Cluster selection strategy has a contradiction with the threat model under adaptive attack.** The paper's threat model (Section 3.1) explicitly states attackers can constitute a majority. MARS's norm-based cluster selection (smaller center norm) works in standard settings. However, against the adaptive attack (high λ), BE values invert, and the paper switches to MARS*, which uses **majority-based selection**. This directly contradicts the "attackers can be a majority" assumption in the threat model: if attackers are the larger cluster and use the adaptive attack, MARS* selects the wrong cluster. The paper does not address this scenario or provide a unified selection strategy. This is not a minor oversight — it means the defense against adaptive attacks is only valid under the very assumption (attackers are minority) that the paper otherwise claims to avoid.

2. **Experimental results lack statistical rigor for extraordinary claims.** Table 5 reports TPR=100%, FPR=0% across every attacker ratio from 0% to 95%, including the extreme 95% case (only 5 out of 100 clients benign). These perfect scores are presented without variance estimates, confidence intervals, or any indication of how many independent trials (random seeds) were run. Given that non-IID data distributions cause natural variance in benign updates, the claim of zero false positives across all settings is extraordinary and requires replication-level evidence. Similarly, the main comparative results (Table 2) lack error bars. The absence of statistical validation undermines confidence that these results are reproducible rather than a single favorable run.

### Minor

1. **Limited non-IID evaluation.** Only a single Dirichlet α=0.9 is tested, which is a relatively mild non-IID setting. Stronger heterogeneity (α=0.1 or 0.5) could cause benign CBEs to have higher variance, making clustering harder and potentially increasing false positives. The paper claims "practicability" under heterogeneous data but does not substantiate this with experiments at more challenging heterogeneity levels.

2. **Hyperparameter sensitivity is unexamined.** The parameters κ (top 5%) and ε (clustering threshold 0.03) are fixed defaults with no ablation or sensitivity analysis. Small changes could affect detection performance, particularly across different attacks, datasets, or data heterogeneity levels. The paper would benefit from showing how robust MARS is to these choices.

3. **Missing standard experimental details for reproducibility.** The paper does not specify basic training details: learning rate, local epochs, batch size, total communication rounds, optimizer, or whether the global model reaches convergence before evaluation. While code release upon publication partially mitigates this, the current submission cannot be independently replicated from the text alone.

4. **The BE approximation is presented without clarifying its domain of validity.** The paper correctly argues that within a layer, relative BE ordering depends only on the neuron's Lipschitz constant (since other terms cancel). However, it does not explicitly state how the Lipschitz constant is computed from model parameters (for a ReLU neuron, this is the L2 norm of the incoming weight vector). The simplification from Equation (2) to Equation (3) is presented as a general result when it is valid only for within-layer comparisons, which is sufficient for the method (since top-κ% are extracted per layer) but could mislead readers about the generality of the approximation.

5. **The comparison with BackdoorIndicator does not clearly state which primary dataset was used.** The table caption references BackdoorIndicator's indicator datasets (GTSRB, CIFAR-100) but the FL task dataset is not explicitly stated. Since the main comparison (Table 2) already covers 3 datasets, this is a minor clarity issue rather than a substantive omission.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- **Stronger adaptive attack evaluation.** The only adaptive attack tested is a simple BE-minimization regularizer. A more sophisticated adversary could try to match the CBE distribution of benign models (e.g., via a generative approach or histogram matching) rather than simply minimizing BE. Evaluating against such attacks would strengthen claims of robustness.
- **Computational overhead analysis.** MARS requires computing per-neuron Lipschitz constants and running Wasserstein-distance-based K-Means. A brief comparison of runtime or communication cost against simpler defenses (e.g., Multi-Krum, FLAME) would help assess practical deployability.

## Removed Points

These points are flagged to be removed by review rules; treat them with caution:

- **Missing Section 7 / ImageNet evaluation.** The reviewer noted that "7 examines MARS's effectiveness on larger datasets such as ImageNet" is referenced but absent. This is a parser artifact — the appendix/supplementary material containing this section was stripped during PDF extraction; it exists in the original submission. **Removed per rule about missing appendix sections.**
- **"BE reduces to weight norms, not novel."** While the approximation does reduce to weight norms within a layer, the contribution is in the overall framework (BE definition + CBE extraction + Wasserstein clustering + norm-based cluster selection), not just the BE metric in isolation. **Removed per rule against strawman weaknesses.**
- **"No evaluation on larger-scale models."** Same as above — this exists in the appendix. **Removed.**
- **"Comparison with BackdoorIndicator uses only CIFAR-10."** The main evaluation (Table 2) covers 3 datasets; Table 4 is an additional comparison. The dataset is not clearly stated in the caption but this is a clarity issue, not a substantive missing comparison. **Downgraded to Minor weakness #5 above.**

## Novel Insights

The most insightful observation that emerges from the reviews — beyond what the paper itself claims — is the fundamental tension between the two cluster selection strategies (norm-based vs. majority-based) and what this reveals about the threat model coverage. The paper's norm-based selection is elegant for handling attacker-majority scenarios under standard attacks, but the fact that an informed adversary can invert BE values (forcing a retreat to majority-based selection) exposes a missing layer in the defense: there is no mechanism to detect *which regime* the system is in (normal BE ordering vs. inverted BE ordering) and automatically select the appropriate strategy. A defender who commits to one strategy a priori will fail under the other regime. This suggests that a more robust defense would need either (a) a third signal that disambiguates the two regimes without assuming majority, or (b) a provably ordering-invariant clustering criterion that works regardless of whether backdoor models have higher or lower BE than benign models.

## Suggestions

1. Address the cluster selection tension by either: (a) proposing a single selection rule that works regardless of BE ordering (e.g., using a reference distribution or statistical test), or (b) explicitly characterizing the detectable conditions under which each variant applies and providing a method to switch between them automatically.
2. Report all main experiments with at least 5 random seeds (data partition, client sampling, initialization) with mean and standard deviation for ACC, ASR, TPR, FPR.
3. Evaluate under stronger non-IID settings (e.g., Dirichlet α=0.1, 0.3, 0.5) to substantiate the "practicability" claim.
4. Include a hyperparameter sensitivity analysis for κ and ε.
5. Add standard training hyperparameters (learning rate, local epochs, total rounds, optimizer) for reproducibility.

## Score and Decision

The paper tackles an important problem and introduces genuinely novel ideas — the BE concept and Wasserstein-based clustering are interesting contributions backed by strong empirical results in standard settings. However, the cluster selection vulnerability under adaptive attacks (where MARS* contradicts the threat model's majority assumption), combined with the lack of statistical rigor for the extraordinary perfect-detection claims, prevents acceptance at a top venue. The paper's core claims are promising but not yet fully substantiated. Major revisions — particularly resolving the cluster selection contradiction and adding proper statistical evaluation — could make the contribution convincing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>