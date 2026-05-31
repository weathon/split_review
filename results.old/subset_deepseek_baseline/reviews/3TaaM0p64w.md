## Summary

This paper proposes Fed-MADS, a federated active learning (FAL) framework for explainable federated learning (XFL). The method leverages the information bottleneck (IB) principle to derive a minimax data selection objective that identifies unlabeled samples exhibiting large divergence between local and global models in both latent representations and final predictions. The variational distributions in the IB objective are implemented using the global model, making the approach naturally suited to XFL. Experiments on four benchmark datasets show that Fed-MADS consistently outperforms existing FAL methods in model accuracy, rule accuracy, and rule fidelity.

## Strengths

- **Principled theoretical grounding**: The paper derives the data selection criterion from the information bottleneck principle, providing a clear information-theoretic motivation for selecting samples where local and global models disagree. This goes beyond heuristic uncertainty-based methods.
- **Strong empirical results**: Fed-MADS achieves the best or near-best performance across all four datasets on all three metrics (accuracy, rule accuracy, rule fidelity). The learning curves show consistent improvement over baselines, often with fewer labeled samples.
- **Well-motivated for XFL**: The method explicitly targets explainable FL by considering both latent representation divergence and prediction divergence, which aligns with the goal of learning semantically-rich representations. The use of the global model as the variational distribution is a natural fit for the federated setting.
- **Comprehensive evaluation**: The paper compares against six baselines, including recent FAL methods (FedAL, LoGo, KSAS), and reports not only model accuracy but also rule accuracy and rule fidelity—metrics that directly measure explainability. An ablation study on the trade-off parameter β is also provided.

## Weaknesses

### Fatal
None.

### Major
- **Limited novelty relative to KSAS**: The KSAS method (Cao et al., 2023) also selects samples based on KL-divergence between local and global model predictions. The paper claims KSAS uses “mean outputs” but does not clearly explain how Fed-MADS differs beyond adding a latent representation divergence term. The IB derivation is presented as the main theoretical contribution, but the resulting selection score (KL divergence on latent + cross-entropy on predictions) is a straightforward combination of two existing ideas. The paper would benefit from a more explicit comparison and a discussion of what the IB lens adds beyond the heuristic used in KSAS.
- **Theoretical justification of the minimax objective**: The derivation from the IB upper bound (Eq. 8) to the minimax data selection objective (Eq. 13) is not fully rigorous. The paper states that minimax is a common technique in active learning, but the connection between the upper bound and the specific maximization over a batch of samples is heuristic. The claim that the minimax formulation “unifies” learning and data selection is not strongly supported. A clearer argument or a more direct derivation would strengthen the paper.
- **Lack of non-i.i.d. experiments**: The paper explicitly assumes i.i.d. data across clients (Section 3.1), but many real-world FL scenarios are non-i.i.d. The method’s reliance on global model quality may be particularly sensitive to data heterogeneity. Without experiments on non-i.i.d. partitions, the practical applicability of Fed-MADS is unclear.

### Minor
- **No error bars on learning curves**: Figure 2 shows learning curves without any indication of variance (e.g., shaded regions). The paper reports mean and standard deviation of the learning curve values in Table 1, but it is unclear whether the curves in Figure 2 are from a single run or averaged. Adding error bars or clarifying the number of runs would improve reproducibility.
- **Incomplete ablation study**: The ablation only varies β, which removes the prediction divergence term when β=0. There is no ablation that removes the latent divergence term (e.g., using only s2). Such an experiment would help isolate the contribution of each component.
- **Computational cost not empirically measured**: The paper claims O(|U_i|) complexity for data selection, but does not report actual runtime or compare it with baselines. For large unlabeled pools, computing KL divergence on latent representations may be non-trivial, especially if the latent space is high-dimensional.

### Trivial
- The paper states “the global model gathers the information of every client and thus becomes more accurate” (Section 3.3). This is true under i.i.d. assumptions but may not hold under heterogeneity; the paper later acknowledges this as a limitation.

## Nice-to-Haves
- Experiments on non-i.i.d. data partitions would significantly strengthen the paper.
- A variant that uses only the prediction divergence term (s2) would help disentangle the contributions of the two terms.
- Reporting the number of communication rounds or total labeling budget used in the experiments would provide context for the learning curves.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions
- Clarify the relationship with KSAS more explicitly, including a direct comparison of the selection criteria and a discussion of what the IB derivation adds.
- Provide a more rigorous derivation of the minimax objective from the IB upper bound, or at least state clearly that it is a heuristic inspired by the bound.
- Add non-i.i.d. experiments to demonstrate robustness.
- Include error bars or confidence intervals on the learning curves.
- Report empirical runtime of the data selection step.

## Score and Decision

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>