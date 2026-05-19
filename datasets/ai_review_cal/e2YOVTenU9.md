- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 8, 3
Now I have all the evidence needed. Let me compose the final consolidated review.

## Summary

This paper proposes ArchLock, a NAS-based method that searches for architectures that perform well on a source task but poorly on target tasks, as a defense against unauthorized model transfer at the architecture level. It uses a binary predictor trained with zero-cost proxy labels and simulated target task embeddings to enable efficient cross-task search. Experiments on NAS-Bench-201 and TransNAS-Bench-101 show that architectures found by ArchLock have reduced rank percentiles on target tasks while maintaining source-task performance within 2% degradation.

## Strengths

- **First architecture-level defense against unauthorized transfer**: The paper identifies that prior defenses operate at the weight level (which can be circumvented via fine-tuning) and instead proposes reducing transferability at the architecture level. This is a genuinely new direction for model protection (Section 1; contribution list).

- **Demonstrated quantitative reductions on benchmarks**: On TransNAS-Bench-101, ArchLock-TK reduces the architectural rank percentile of the searched architecture on target tasks substantially (e.g., SS→SC from 81.81% to 40.48%) while source-task rank percentile remains within 2% of the source-only baseline (Tables 1–2). The pattern holds across multiple source-target pairs on both NB-201 and TNB-101.

- **Zero-cost binary predictor with meta-learning**: The predictor uses seven complementary zero-cost proxies (fisher, flops, grad-norm, grasp, jacov, nwot, snip) to generate training labels, avoiding expensive architecture training. By incorporating task embeddings as additional input, the predictor aims to generalize to unseen tasks (Section 3.2, Section 4.3).

- **Simulated task embeddings avoid dataset generation**: Rather than simulating full target datasets, the paper generates target task embeddings via Fisher Information Matrix manipulation (Eq. 8, Section 3.1), enabling cross-task search without knowing the attacker's data.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation tests standalone architecture performance, not the claimed transfer scenario**: The paper's threat model concerns an attacker who obtains a pre-trained model (weights + architecture) and fine-tunes it to a target task. However, the evaluation uses benchmark-provided validation accuracy — which measures performance when architectures are **trained from scratch** on each task independently (Section 4, line 140: "Performance evaluation is based on the validation performance provided by the benchmarks"). The paper does not pre-train on the source task and fine-tune on target tasks, nor does it vary the amount of data available to the attacker. The claim that the defense works "regardless of the amount of data available to the attacker" (line 18) is not tested. While the architecture-level results are informative — an architecture that ranks poorly on a task when trained from scratch is unlikely to excel under fine-tuning — the current evaluation does not directly support the stated threat model. The paper should either test the fine-tuning scenario or more precisely scope its claims.

- **Binary predictor is not validated**: The predictor is a core component — it guides the entire search — yet the paper reports no metrics on its accuracy or ranking quality. There are no Spearman/Kendall correlations between predictor rankings and true performance, no binary accuracy or AUC on held-out tasks, and no ablation that replaces the predictor with ground-truth rankings. The paper uses zero-cost proxy labels (which have known limitations in cross-task settings) as ground truth for training (Section 4.3), but does not validate whether the ensemble voting scheme yields correct pairwise comparisons. Without this, the reader cannot assess whether ArchLock's results stem from meaningful architecture selection or from noise in the predictor.

### Minor

- **Simulated task embeddings lack validation baselines**: The method for generating target task embeddings (Eq. 8) is a geometric construction based on the source task's Fisher Information Matrix. The ablations in Section 5.2 show sensitivity to the similarity hyperparameter *d* and the number of embeddings, which is useful, but the paper does not compare simulated embeddings against simpler alternatives: (a) using the actual target task embedding (available in TNB-101), (b) random embeddings of the same dimension, or (c) a null model that omits the embedding. This makes it difficult to attribute the observed reductions to the embedding mechanism rather than to the regularisation effect of having multiple objectives.

- **Ambiguous calculation of claimed reduction percentages**: The abstract claims "up to 30% and 50%" reduction in transferability, but the derivation of these figures from the reported rank percentile values (Tables 1–2) is not clearly explained. The paper would benefit from stating explicitly whether these are absolute reductions, relative reductions, or refer to specific source-target pairs.

### Trivial
None.

## Nice-to-Haves

- Reporting standard deviations or variability estimates for the results (the paper mentions "average of multiple runs" but does not report the number of runs or variance).
- Ablation on the balancing parameter λ in the fitness score (Eq. 9; the paper uses λ=2 without sensitivity analysis).
- A discussion comparing ArchLock to existing weight-level defenses (e.g., adversarial training's effect on transferability) to clarify the complementary nature of the approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- The harsh critic's characterization of the evaluation gap as "fatal" and "invalidating the paper's central claim" is overstated. The paper's central claim — that architecture-level properties can be selected to degrade cross-task performance — IS supported by the evaluation (training from scratch on each task is the standard in NAS benchmarks). The gap is between the threat model (fine-tuning) and evaluation protocol, not between the problem formulation and evaluation. This gap is a real concern but does not invalidate the paper's core findings.
- The harsh critic's call for "comparison to weight-level defenses" is removed as scope creep — the paper explicitly focuses on the architecture level and notes that weight-level defenses are a complementary direction (Section 1).
- The harsh critic's request for "statistical reporting" (standard deviations, number of runs) is downgraded to a nice-to-have, as single-run evaluation on large NAS benchmarks is the community norm.
- The strength finder's more generic statements about the problem being important or interesting are removed per the filtering instructions.

## Novel Insights

The harsh critic's core observation — that the evaluation protocol (training from scratch on each task) does not match the stated threat model (fine-tuning from a pre-trained source) — is a genuinely insightful critique that goes beyond a surface-level reading. This tension is not standard in NAS papers, which typically evaluate architecture performance by training from scratch on benchmarks. The paper's defense of architecture-level protection implicitly assumes that poor standalone task performance implies poor transferability, but this assumption — while plausible — is neither stated nor tested. A second insight that emerges across the reviews is that the paper's technical machinery (ZCP-based binary predictor + simulated embeddings) is clever but lacks component-level validation, making it impossible to attribute the overall result to any specific design choice. These observations together suggest that the paper's real contribution may be in posing the architecture-level defense problem rather than in the specific solution it implements.

## Suggestions

1. **Test the actual transfer scenario**: Pre-train the searched architectures on the source task, fine-tune on target tasks, and report final accuracy. Compare against standard architectures to show that the architecture-level degradation persists after fine-tuning. This would directly support the threat model.
2. **Validate the binary predictor**: Report Spearman rank correlation between predictor rankings and true performance on held-out tasks. Compare against individual ZCPs and a random baseline. Show that the ensemble voting improves over single proxies.
3. **Add baselines for task embedding simulation**: Compare ArchLock-TU using simulated embeddings against using (a) the actual target task embedding and (b) random embeddings. This would isolate the contribution of the embedding mechanism.
4. **Clarify the reduction calculation**: State explicitly how the 30% and 50% figures in the abstract are derived from the tables.
