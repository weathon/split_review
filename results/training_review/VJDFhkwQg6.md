Now I have all the evidence needed. Let me synthesize the final review.

## Summary

The paper introduces FC-GFlowNet, the first principled framework for federated learning of GFlowNets, where the target distribution is a product of (potentially sensitive) reward functions held by different clients. The approach is a single-round divide-and-conquer strategy: clients train local GFlowNets, send their policies to a server, and the server aggregates them via the proposed *federated balance* (FB) condition (Theorem 1). Along the way, the paper introduces *contrastive balance* (CB), a new training criterion for standard GFlowNets that avoids estimating the partition function or state flows, with a theoretical connection to variational inference (Theorem 3). Experiments on grid-world, multiset, sequence, and phylogenetic inference tasks show that FC-GFlowNet closely matches a centralized oracle and dramatically outperforms a simple categorical-product baseline (PCVI).

## Strengths

- **First principled framework for federated GFlowNets:** The paper identifies a clear gap — no prior work addresses federated settings for GFlowNets — and fills it with a clean, theoretically grounded solution. The divide-and-conquer approach and single-round communication protocol are elegant and practically appealing.

- **Sound theoretical core:** Theorem 1 provides a necessary and sufficient condition (federated balance) for the correctness of the aggregation step. Theorem 2 quantifies how errors in locally trained GFlowNets propagate to the federated model via a bound on Jeffrey divergence, with a clean connection to the catastrophic failure phenomenon known in parallel MCMC. The bound correctly degenerates when a local model is poorly trained (β_n → ∞ or α_n → 1).

- **Novel contrastive balance (CB) condition:** The CB loss (Equation 10) eliminates the need to parameterize the partition function (as in TB) or state flows (as in DB), reducing model complexity. Theorem 3 shows that on-policy gradients of the CB loss equal the gradient of the KL divergence between forward and backward policies, establishing a direct variational interpretation. The empirical results in Figure 6 suggest CB can converge faster on certain tasks (multiset generation, phylogeny).

- **Consistent empirical results across diverse tasks:** Table 1 shows FC-GFlowNet achieves L1 distances and top-800 average rewards that are statistically indistinguishable from a centralized GFlowNet (within one standard deviation across all four tasks), while the PCVI baseline is often orders of magnitude worse. The phylogenetic inference experiment (L1 error 0.088) demonstrates applicability to real scientific inference.

## Weaknesses

### Fatal
None.

### Major

- **Limited baseline comparison weakens empirical support for the method's practical benefits.** The paper compares FC-GFlowNet only against PCVI (product of independent categoricals) and a centralized oracle. PCVI is a natural strawman — it cannot capture any dependencies and is expected to fail on structured output spaces — so outperforming it does not demonstrate that the federated balance loss provides meaningful advantages over other plausible aggregation strategies. A natural missing baseline is **FedAvg-style parameter averaging**: the server averages the weights of the local forward (and backward) networks and tests whether the resulting GFlowNet samples from the product of rewards. Without such a comparison, a reader cannot tell whether the complex federated balance loss is necessary or if a simpler approach would suffice. The phylogeny experiment omits PCVI entirely, stating it yields "invalid topologies," but provides no quantitative evidence of this failure mode.

- **Theoretical correctness guarantee depends on a condition (Equation 4) whose relationship to local training is undertreated.** Theorem 1's "if and only if" statement assumes local GFlowNets have marginals proportional to their rewards. However, the condition in Equation 4 involves trajectory-level ratio products ∏ p_F/p_B that are not guaranteed to be well-behaved when local models are trained with DB or other losses that do not enforce trajectory-level constancy. If local models have correct marginals but their per-trajectory ratios vary (which can happen without TB/CB), the condition in Eq. 4 becomes trajectory-dependent in a way whose practical implications are not analyzed. The paper acknowledges this through Remark 1 and Theorem 2 (bounded error for imperfect local models), but the gap between the "perfect" theoretical guarantee (which implicitly requires local models to satisfy TB/CB-level conditions) and the actual practical setup (where models are trained with DB/TB objectives that may not achieve this) is significant. The abstract's claim that FB "provably ensures the correctness" would more accurately read "provably ensures correctness conditional on local models achieving trajectory-level balance."

### Minor

- **The CB loss evaluation (Section 4.5) lacks sufficient experimental rigor.** The paper states that CB outperforms TB/DB/FL on two tasks but does not report error bars for these comparisons, specify the number of runs, describe the learning rates tested (beyond "all rates we have tested"), or detail the training budget (the x-axis in Figure 6 is labeled "steps" without indicating total budget or how trajectory pairs were sampled per update). Given the known variance in GFlowNet training, these results are suggestive but not conclusive. The paper's own caveat ("A rigorous understanding... is still lacking") is appropriate but does not excuse the missing details.

- **The experimental scope is limited to small-scale, low-dimensional problems.** The grid-world is 18×18 with exhaustive enumeration possible; the multiset task uses 8 elements from a dictionary of 10; the sequence task has unspecified maximum length; the phylogeny task uses constant branch lengths (topology only). While these are appropriate for validating the core idea, they do not stress-test the method on the high-dimensional, combinatorial spaces where GFlowNets are most valuable (e.g., molecule generation with QM9/ZINC, biological sequence design, or causal DAG discovery). The paper's contributions would be substantially strengthened by at least one task of realistic scale.

- **The number of clients is limited (up to 5) across all experiments.** Theorem 2's bound grows linearly with N (sum of log terms), and it is unclear how performance degrades with more clients. A sensitivity analysis with 10–20 clients would help characterize practical limitations.

### Trivial
- None.

## Nice-to-Haves
- An ablation showing how the quality of the aggregated model varies with the choice of local training objective (TB vs. DB vs. CB) would reveal whether the method is robust to the local balance condition.
- A controlled experiment with deliberately undertrained local GFlowNets (varying α_n, β_n) would test whether Theorem 2's bound captures observed error qualitatively.
- Extending the method to weighted products R(x) = ∏ R_n(x)^{w_n} is mentioned in the supplementary material but not empirically demonstrated, which would broaden applicability.
- Example trajectories from the aggregated model vs. local models would build intuition about how the FB loss combines trajectory-level decisions.

## Removed Points

The following points from the harsh critic are removed per the review guidelines:

- **"Corollary 1 loss is garbled / both terms identical"** — This is a PDF parsing artifact; the original submission has superscript (i) on the local policies inside the sum, which was stripped during text extraction. Per the hard rules, parser artifacts are not author errors.
- **"Abstract overstates 'provably ensures the correctness'"** — The abstract refers to the aggregation step being provably correct given an assumption of locally correct models. This is standard language for federated methods and not an overstatement. Remark 1 and Theorem 2 transparently address the imperfect local inference case.
- **"None of the experiments involve sensitive data or measure data leakage"** — The paper never claims to provide formal privacy guarantees; it identifies privacy as one motivation. Criticizing the absence of experiments that are outside the paper's stated scope is scope creep.
- **"Centralized GFlowNet baseline is an oracle upper bound, not a competitor"** — This is exactly how it is presented: as an upper bound on achievable performance. The paper never claims to beat the centralized oracle; it aims to match it without sharing rewards, which the experiments show it does.
- **"The bound in Equation 8 depends on worst-case per-trajectory ratios that are not controlled"** — This is the nature of a theoretical bound: it provides a guarantee in terms of worst-case quantities. The bound is useful precisely because it characterizes the worst-case impact of local errors. This is a feature, not a weakness.
- **Weakness about missing appendix content** — The parser strips supplementary material from all papers; it exists in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews add no additional insight not already stated more precisely in the paper.

## Suggestions

1. **Add a FedAvg-style parameter averaging baseline** — Average the weights of the local forward networks and test whether the resulting GFlowNet samples from the product of rewards. This is the simplest conceivable baseline and directly tests whether the federated balance loss is beneficial over naive averaging.

2. **Strengthen the CB loss evaluation (Section 4.5)** — Report the number of independent runs, include error bars/shading on the L1 curves, specify the learning rates tested and the trajectory-pair sampling procedure, and state the total training budget. This is essential for reproducibility and for substantiating the claim that CB outperforms TB/DB.

3. **Add at least one larger-scale experiment** — Even a standard GFlowNet benchmark (e.g., molecule generation on a subset of the QM9 dataset, or biological sequence design) would significantly increase confidence that the method scales beyond small synthetic domains.

4. **Clarify the theoretical relationship between Equation 4 and local training objectives** — Either prove that models trained with standard losses (TB/DB/CB) satisfy the necessary trajectory-level ratio properties, or add a discussion making explicit that the ideal correctness guarantee assumes local models achieve trajectory-level balance (not just correct marginals), and characterize the approximation gap for models trained with DB.

5. **Study sensitivity to number of clients** — A simple simulation with 10, 20, and possibly 50 clients on the grid-world or multiset task would demonstrate whether the method degrades gracefully as predicted by Theorem 2.

## Score and Decision

The paper introduces a genuinely novel problem and a clean, theoretically grounded solution. The theoretical contributions (federated balance, contrastive balance, error propagation bounds) are sound, and the empirical results consistently show the method matches a centralized oracle. The main weaknesses are: (1) insufficient baselines — the paper compares only against a weak strawman (PCVI) and excludes the natural FedAvg baseline; (2) the theoretical guarantee has a gap between the idealized assumptions of Theorem 1 and the practical training setup (partially acknowledged but worth deeper treatment); (3) the CB loss experiments lack statistical rigor; (4) the scope is limited to small-scale tasks. These are addressable weaknesses that do not undermine the core contribution. I recommend acceptance with a request for strengthening the baselines and experimental rigor in a final version.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>