Now I have a thorough understanding of both the paper and the reviewers' claims. Let me produce the consolidated review.

---

## Summary

This paper studies active learning on heterophilic graphs. It identifies that existing graph active learning (GAL) methods produce training sets whose local homophily distribution is homophilic even on heterophilic graphs, explaining their poor performance. The paper proposes KyN, built on a "Know Your Neighbors" principle — label nodes together with their neighbors via subgraph sampling using ℓ₁-Lewis weights. Experiments on six heterophilic datasets show consistent improvements over baselines.

## Strengths

- **Problem diagnosis is novel and well-supported.** The analysis in Section 3.1 (Figure 2) demonstrates concretely that prior GAL methods select training sets with a left-skewed (homophilic) local homophily distribution on the heterophilic Roman-empire dataset, while the ground truth distribution is right-skewed. This reframes the problem of heterophilic GAL in a way that directly motivates the solution.

- **Consistent and substantial empirical improvements.** Table 1 shows KyN outperforms all prior GAL methods across six heterophilic datasets, with improvements over the best baseline reaching up to 12.1% (Roman-empire). Unlike prior methods, KyN consistently beats random sampling across all budgets and datasets.

- **Principled algorithm design.** The "Know Your Neighbors" principle is clearly motivated by Theorem 3.2 (labeling neighbors improves local homophily estimates), and the implementation via subgraph partitioning + ℓ₁-Lewis-weight sampling is a novel and well-reasoned instantiation for the graph active learning setting.

- **Robustness across heterophilic GNN backbones.** Table 2 shows KyN works with FAGCN and M2M-GNN as backbones, not just SAGE-Mean, demonstrating that the benefit comes from the training set selection rather than a particular encoder.

- **Scalability demonstrated.** Table 3 shows KyN completes on snap-patents (2M+ nodes) in reasonable time, while several baselines exceed 24 hours.

## Weaknesses

### Fatal

None.

### Major

None that are truly structural — the paper's core claims are supported by evidence. However, the following issues are worth careful attention.

### Minor

- **Abstract overstates the failure of prior work relative to the paper's own evidence.** The abstract and conclusion claim that prior GAL methods "fail to outperform the naive random sampling on heterophilic graphs." However, the results section uses the more measured phrasing "fail to consistently outperform" (line 189), and Table 1 shows that some prior methods do beat random on several datasets (e.g., DOCTOR and GreedyET on Amazon-ratings at 10C/20C; GraphPart on Tolokers at 20C; ALG on Texas at 10C). The genuine and still-interesting finding — that many GAL methods are inconsistent on heterophilic graphs and KyN improves over all — does not require the stronger claim. This is a presentation issue that should be corrected.

- **The theoretical guarantee (Theorem 3.6) does not cover the experimental setup.** The theory is stated for a *one-layer* SAGE-Mean encoder (line 133), with the caveat that "the results are similar on any multi-layer linear GNNs." The experiments, however, use a *three-layer* SAGE-Mean with ReLU activations (line 185), which is non-linear. The paper acknowledges this simplification ("For simplicity, we use a one-layer SAGEMean encoder") but the mismatch between the theory (linear, one-layer) and practice (non-linear, three-layer) means the stated coreset guarantee does not formally apply to the empirical results. Since the paper markets itself as having "solid theoretical guarantees," this gap should be acknowledged more explicitly. A practical mitigation would be to include a small experiment with a one-layer linear encoder to demonstrate the guarantee in the regime where it holds.

- **Hyperparameter sensitivity is higher than claimed.** The paper claims "KyN is robust to the choice of c" (Figure 5, line 198), but the reported variation spans roughly 5–15% on several datasets (e.g., Texas at 20C drops from ~88% to ~78% across the c range). Additionally, the recommended heuristic c ≈ |V|/C is not followed in the main experiments (e.g., for Roman-empire, |V|/C ≈ 4532 but c = 1500). While the method works well across a range, the "robust" characterization and the recommendation-in-practice deserve more careful reconciliation.

- **Budget truncation could introduce selection bias.** The procedure samples subgraphs until the labeled node count exceeds the budget B, then keeps the first B nodes (line 143). Nodes from the tail of the last selected subgraph are discarded. The paper does not analyze whether this truncation systematically affects the homophily distribution of the final training set.

- **Proposition 3.1 adds little beyond intuition.** The inequality in Proposition 3.1 is a straightforward bound linking prediction accuracy to the accuracy of estimated local homophily. It is not wrong, but it is presented as a formal necessity result when the real evidence for the paper's diagnosis comes from the distributional analysis in Figure 2. The paper could downplay the proposition without loss.

### Trivial

- Some references to figures/tables contain garbled text likely from PDF parsing — this does not affect the original submission.

## Nice-to-Haves

- An ablation comparing the two "Know Your Neighbors" schemes (sample-then-expand vs. partition-then-sample) on at least one dataset would strengthen the design justification beyond the intuition and toy example.
- An experiment on a homophilic dataset (e.g., Cora, Citeseer) would demonstrate that KyN does not degrade performance when the graph is homophilic, showing its range of applicability.
- Statistical significance tests (e.g., paired t-tests) for cases where KyN's margin over the best baseline is small (e.g., Amazon-ratings at 5C) would help assess whether the improvement is meaningful.

## Removed Points

These points are flagged for removal; treat them with caution.

- **Criticism that the "sample then select k-hop" dismissal is unsubstantiated (Harsh Critic, Issue 3).** The paper provides a clear, well-motivated argument (neighbor explosion leads to a single large connected component) and a visual illustration (Figure 3). This is a reasonable design justification; an ablation would be nice but is not required. Moved to Nice-to-Haves.

- **Criticism about missing appendix / missing proofs.** Per instructions, the appendix exists in the original submission. The mathematical concern about CE loss satisfying the nice hinge function conditions is a valid question but cannot be evaluated without the appendix content. Not included as a standalone weakness.

- **Complaint that Proposition 3.1 is "trivial" / "almost tautological."** While the proposition is indeed a simple inequality, the paper does not present it as a major theoretical contribution — it is a supporting formalization. The real diagnostic evidence is Figure 2. This observation does not constitute a weakness of the paper.

- **Missing comparison on homophilic graphs.** The paper explicitly scopes itself to heterophilic graphs; demanding homophilic experiments is scope creep. Moved to Nice-to-Haves.

- **Large-scale OOT baselines are "not a fair comparison."** Reporting OOT is standard and legitimate — it reflects a practical limitation of those methods. The remaining baselines that do finish provide a fair comparison, and KyN outperforms them.

- **Demand for statistical significance tests.** Not standard practice in this benchmarking area; impractical on 10 runs.

## Novel Insights

Beyond the paper's own contributions, the reviews offer no genuinely novel insight. The harsh critic's observation that Proposition 3.1 is a simple bound rather than a deep theoretical result is accurate but not novel. The critic's identification of the abstract/results inconsistency is a valid editorial point.

## Suggestions

1. **Reconcile the abstract with the evidence.** Change "fail to outperform" to "fail to consistently outperform" or "often underperform" in the abstract and introduction to match the measured language in Section 5.2.
2. **Acknowledge the theory-experiment gap explicitly.** Add a sentence: "The theoretical guarantee (Theorem 3.6) applies to one-layer linear encoders; extending it to multi-layer non-linear encoders is left for future work."
3. **Add a small-scale experiment with a one-layer linear SAGE encoder** to demonstrate that the coreset guarantee holds empirically in the regime covered by the theory.
4. **Analyze the budget truncation procedure.** Report the mean/median number of discarded nodes and verify that their features/labels are not systematically different.
5. **Clarify the hyperparameter guidance.** Explain the discrepancy between the recommended c ≈ |V|/C and the values used in the main experiments, and provide clearer guidance on selecting c.

## Score and Decision

The paper makes a substantive contribution: it identifies a genuine problem in heterophilic GAL with clear evidence, proposes a well-motivated algorithm, and demonstrates consistent empirical improvements on multiple datasets and backbones. The weaknesses are real but addressable — the abstract overstatement is a presentation fix, the theory-experiment gap is acknowledged and common in ML papers, and the remaining issues are minor. The core contribution is solid and the empirical results are convincing.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>