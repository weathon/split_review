Now I have all the information needed to write an authoritative consolidated review.

---

## Summary

This paper proposes Swift-FedGNN, a mini-batch sampling-based federated GNN algorithm that reduces communication and sampling overhead by having all clients perform efficient local training in most iterations, while only a randomly selected subset of clients periodically conducts expensive cross-client training. The key contributions are: (1) a periodic cross-client training scheme with random client selection that avoids storing cross-client neighbor information and uses two-stage aggregation (remote clients → server → training client) for privacy; (2) rigorous convergence analysis bounding stochastic gradient errors from neighbor sampling and missing cross-client neighbors *without* assuming unbiased or consistent gradients (Lemmas 5.4, 5.5); and (3) a convergence rate of O(T^{-1/2}) matching SOTA sampling-based GNNs despite the more challenging federated setting.

## Strengths

- **Rigorous convergence theory without unrealistic assumptions.** Lemmas 5.4 and 5.5 bound the errors from neighbor sampling and missing cross-client neighbors without resorting to the unbiased or consistent stochastic gradient assumptions used in prior work (Chen et al., 2018; Chen & Luss, 2018). Theorem 5.6 establishes a convergence rate of O(T^{-1/2}) to a neighborhood of the exact solution, matching the SOTA rate of sampling-based GNN methods despite operating in the more challenging federated setting. This is a genuine theoretical contribution.

- **Clean algorithmic design directly motivated by measured bottleneck.** The paper measures that cross-client training is ~5× slower than local training (Figure 2, with per-iteration time breakdown on Amazon product data). The algorithmic response — primarily local training, periodic cross-client training on a random client subset (Algorithms 1–3), and two-stage aggregation (remote clients → server → training client) — directly addresses this bottleneck while helping preserve data privacy by avoiding raw feature transfer between clients.

- **Empirically demonstrated efficiency gains.** The paper shows (Section 6) that while FedGNN-G (full cross-client training every iteration) achieves slightly higher accuracy (e.g., 87.93% vs. 87.73% on ogbn-products), Swift-FedGNN converges faster (Figure 4) with dramatically lower overhead: cross-client training takes <200ms vs. >5000ms for LLCG on ogbn-products. The computation-to-communication ratio is significantly reduced compared to FedGNN-G, FedGNN-PNS, and LLCG (Figure 5).

- **Uses the largest dataset in the federated GNN literature.** The paper evaluates on ogbn-products, which it correctly notes is the largest dataset used in federated GNN research, alongside Reddit, which is known for its density. These provide complementary coverage of scale and density.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that Swift-FedGNN achieves comparable accuracy to full cross-client training while being substantially more efficient — are supported by the evidence presented. The weaknesses below are addressable in a revision and do not threaten the main contribution.

### Minor

- **Baseline final accuracy numbers not reported in text.** The paper states the final validation accuracies for Swift-FedGNN (87.73% ogbn-products, 95.60% Reddit) and FedGNN-G (87.93%, 96.03%) but does not explicitly report the final accuracies of LLCG and FedGNN-PNS. While Figure 4 visually shows convergence curves for all methods (so a reader can roughly read off values), the text itself omits these numbers, making a side-by-side accuracy comparison incomplete. The authors should state all baseline accuracies directly.

- **Limited evaluation breadth.** The experiments use two datasets, 10–20 clients (small by FL standards where 100+ clients is typical), and a single partitioning method (METIS). The paper justifies the datasets (largest in literature, dense) and client counts are common in federated GNN papers, but adding even one more dataset (e.g., a citation graph with different structural properties) and varying the number/partitioning of clients would strengthen confidence in generalizability.

- **Hyperparameter sensitivity on a single dataset with a single metric.** The sensitivity analysis (Figure 6, ogbn-products only) reports only the computation-to-communication ratio, not actual wall-clock training time to a target accuracy or the accuracy impact of varying \( I \) and \( K \). The trade-off between efficiency and accuracy is the central claim of the paper, so showing how accuracy varies with \( I \) and \( K \) would directly support it. This is a missed opportunity.

- **No wall-clock time to target accuracy comparison.** The paper reports per-iteration timings (Figure 2) and computation-to-communication ratios (Figure 5), but the most practically relevant efficiency metric — total wall-clock time to reach a given accuracy — is not provided. This would directly substantiate the "low communication and sample [overhead]" claim.

### Trivial
- The paper states "For instance, when training the ogbn-products dataset, LLCG takes over 5000ms to perform cross-client training on the server, whereas Swift-FedGNN completes cross-client training within 200ms" — this is a per-iteration figure and could be misinterpreted as end-to-end time if read quickly. Clarifying this in the text would help.

## Nice-to-Haves

- A formal communication complexity analysis (e.g., total bits transferred per round for Swift-FedGNN vs. baselines) would strengthen the title's appeal to "low ... complexities," though the empirical ratios already convey the practical message.
- Ablation on how accuracy changes with different values of \( I \) and \( K \) (not just how the efficiency ratio changes).

## Removed Points

These points were flagged by reviewers but are removed with justifications:

1. *"The experimental evaluation is not strong enough to support the paper's central claims"* — Removed as an overbroad assessment. The experiments do show comparable accuracy to FedGNN-G and faster convergence with significantly less overhead. The paper's central claims are supported, though the evaluation could be broader.

2. *"The paper's title promises 'low communication and sample complexities' but provides no quantification"* — Removed. The paper provides empirical quantification: per-iteration timing breakdowns (Figure 2), computation-to-communication ratios (Figure 5), and specific cost comparisons (5000ms vs. 200ms for cross-client training). The title uses "complexities" informally to mean overhead, not as a formal complexity class.

3. *"Comparisons are incomplete: convergence curves and final accuracies for these baselines are not reported"* — Partially removed. The convergence curves *are* in Figure 4 (visible to the reader). Only the omission of explicit final accuracy numbers for LLCG and FedGNN-PNS from the text is retained as a minor weakness (see above).

4. *Strengths about "this paper addressed an important problem" or similar generic statements* — Removed as they lack specific, grounded evidence.

## Novel Insights

The most striking observation from the review is the gap between the paper's theoretical rigor and the comparative thinness of its experimental evaluation. The theoretical analysis genuinely advances the state of the art by bounding stochastic gradient biases without the unrealistic unbiased/consistent assumptions used in prior GNN convergence proofs. This is a non-trivial contribution that could benefit the broader GNN theory community independently. Yet the experiments, while positive, are confined to a scope (2 datasets, 10–20 clients, single partitioner) that is narrower than what would be expected to fully substantiate the practical effectiveness of a systems-efficiency claim. The theory is the paper's strongest asset; the experiments are adequate but could be stronger.

## Suggestions

1. Report the final validation accuracies for **all** baselines (LLCG, FedGNN-PNS, FedGNN-G) in the text alongside Swift-FedGNN's.
2. Provide wall-clock training time to reach a target accuracy (or to converge) for all methods — this is the most interpretable efficiency metric.
3. Add at least one more dataset with different structural properties (e.g., a citation graph like ogbn-arxiv, or a smaller but structurally different graph) and experiment with varying client counts (e.g., 50, 100).
4. In the hyperparameter sensitivity analysis, show how accuracy (not just the efficiency ratio) varies with \( I \) and \( K \), making the accuracy-efficiency trade-off explicit.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>