- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper addresses the stochastic k-server problem on graphs by formulating it as an MDP and learning policies via deep Q-learning with a graph convolutional network backbone. The main novelty is a decomposition of the action-value function into a global term (depending on the full state) and a local term (depending only on the L-hop neighborhood of the chosen server). This decomposition enables inference-time scalability because the optimal action depends only on the local term, so large graphs can be handled by processing small subgraphs. The paper evaluates on grids, trees, and two real-world transportation networks (Sioux Falls, Eastern Massachusetts), and demonstrates that a generalist policy trained on diverse instances can transfer across graph topologies and arrival distributions, sometimes outperforming instance-specific policies.

## Strengths

- **Novel global–local action-value decomposition (Section 3.2, Eq. 9):** Unlike dueling DQN (state-value vs. advantage), this decomposition ties the local term to only an L-hop subgraph around the chosen server's node. This architectural choice enables inference on arbitrarily large graphs by evaluating only local subgraphs (Eq. 9, line 118–121), directly supporting the scalability and transferability claims.

- **Generalist policy with demonstrated cross-topology and cross-distribution transfer (Tables 1, Figures 2–3):** The paper trains a single GCN DQN on diverse random instances and evaluates it on unseen graphs of different sizes and structures. Table 1 shows Generalist GCN DQN outperforming graph-specific GCN DQN and all baselines on most graph types. Figure 3 provides a well-designed zero-shot experiment: a generalist trained on exponential arrival probabilities performs nearly as well on lognormal, Poisson, and Bernoulli arrivals as specialist policies trained on those distributions. This is a genuinely novel demonstration of transfer for the k-server problem.

- **Constant parameter count independent of graph size (Section 4.3):** The GCN architecture uses 228,866 parameters for all graph sizes, whereas MLP DQN's parameter count grows from 13,608 (9 nodes) to over 1.5 million (100 nodes). This makes the approach structurally scalable, and the paper provides concrete numbers.

- **Direct MDP formulation without problem transformation (Section 2.2):** The state (tuple of server locations + request location) and action (server index) are a natural, minimal encoding. The paper acknowledges prior MDP-based approaches (e.g., Lins et al. 2019a, which uses a visual transformation) and correctly distinguishes its own "direct" formulation.

- **Empirical comparison against strong baselines including WFA on multiple graph classes:** The paper benchmarks against Greedy, Harmonic, Balance, MLP DQN, and WFA (a state-of-the-art online algorithm). The inference time comparison (GCN DQN: 198.4s vs. WFA: ~30 hours for 40k steps on the EM graph) highlights a practical advantage of the learning-based approach.

## Weaknesses

### Fatal

None.

### Major

1. **Scalability claim for 1024-node graphs is unsubstantiated.** The paper states (Section 4.3, evaluation paragraph) that experiments were conducted on graphs of size 1024 but presents **no numerical results, no figure, and no table** reporting the outcomes. The only baseline mentioned is Greedy, yet no comparison is shown. Since scalability is one of the two central contributions (alongside transferability), this omission directly undermines a core claim. Either the results should be provided, or the scalability claims should be scaled back.

2. **Global-value architecture is incompletely specified (Section 3.4, Eq. 10).** The global value is defined as `Q^{global}(s) = MLP^{global}(H^{(L)})`, where `H^{(L)}` is the *n×d* node embedding matrix output by the GCN. An MLP requires a vector input, so some aggregation (pooling, flattening, graph-level readout) over the *n* nodes is necessary, but none is described. This is not a minor detail — it determines whether the architecture can handle variable-size graphs during training (when the global term is needed for the loss) and whether inference truly requires only local information. Without this specification, the method as written is not fully reproducible. (The figure likely shows the intended design, but the text alone is insufficient.)

3. **Lack of statistical rigor in all reported results.** All performance numbers (Tables 1, Figures 2–3) are presented as point estimates without confidence intervals, standard deviations, or significance tests. The paper states 10 episodes per problem instance are used, yet only single values are reported. Given the inherent stochasticity (random graph generation, random arrival sequences, random training seeds), the reader cannot assess whether reported improvements — especially the claim that Generalist GCN DQN outperforms graph-specific GCN DQN — are meaningful or within noise.

### Minor

4. **WFA comparison has an information asymmetry that is acknowledged but not controlled.** The RL methods access the true arrival probability vector **p** as input, while WFA receives only 100 burn-in requests from which to estimate the distribution. The paper notes a separate experimental setup where both sides use estimated arrival rates (footnote, line 147–148), but all main tables compare the *true-distribution* RL methods against the *estimated-distribution* WFA. The asymmetry biases the comparison in favor of RL and should be clearly flagged in the main results.

5. **Offline optimal cost computation is not described.** The paper reports performance "with respect to an optimal offline algorithm" (Section 4.3) but never specifies how the offline optimum is computed for each instance. Was it computed via network flow over the exact request sequence? This is necessary to interpret the "relative to offline" metric and to assess the quality of the scale.

6. **Probability-to-rate conversion lacks ablation (Section 3.3).** The paper converts probabilities to arrival rates (`λ_v = p_v * n`) and claims this is "necessary (as we verified empirically)" but provides no ablation study comparing performance with and without this transformation. The reader cannot evaluate whether this engineering choice is critical or incidental.

7. **No discussion of over-smoothing with 12-layer GCN (Section 3.4).** The GCN uses 12 residual layers, which is deep for message-passing networks and risks over-smoothing (node embeddings becoming indistinguishable). The paper does not comment on whether this was observed or whether shallower networks were explored.

8. **Distance metric limited to unweighted hop count (Section 2.2).** The paper measures distance as number of edges (hops), which is a simplification. Real road networks typically have edge weights (travel times, distances). The paper acknowledges real-world applicability needs further testing (Section 4.5), but this limitation should be stated earlier and more explicitly.

### Trivial

- The input dimension for `W^{init}` in `H^(0) = S * W^{init}` (Section 3.4) is not explicitly stated — a reader must infer that it maps the 3 input features to the hidden dimension *d*.

## Nice-to-Haves

- An ablation study testing whether the global term `Q^{global}(s)` is actually needed. Since the optimal action depends only on `Q^{local}` (Eq. 9), one could train a model with `Q^{global} = 0` to validate the decomposition's utility empirically.
- Sensitivity analysis for the number of servers *k* (fixed to `⌊n/6⌋` throughout).
- Analysis of the computational cost of subgraph extraction at inference time.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

- **"First MDP modeling claim is overstated" (Harsh Critic #Abstract/Intro):** The paper explicitly acknowledges prior MDP-based approaches (Lins et al. 2019a, Even-Dar et al. 2009) and qualifies its claim as "first effort to *directly* model (i.e., without any transformations)". This is a reasonable, scoped claim, not an overstatement. **Removed.**

- **"Comparison is not at equal compute for MLP DQN vs GCN DQN" (Harsh Critic, Section 4.3 notes):** The critic notes MLP DQN receives more training steps. But this asymmetry *favors the baseline* (MLP DQN gets more training), yet GCN still outperforms it. This point actually strengthens, not weakens, the paper's case. **Removed.**

- **Training steps confound:** Same reasoning as above. **Removed.**

- **Various formatting nitpicks and reproduction-perfection demands:** Requests to include complete training logs, hyperparameter search details beyond what is provided, etc. These exceed the standards expected in a conference submission. **Removed.**

- **Strengths from Strength Finder that are generic or sycophantic:** Dropped generic strengths such as "addressing an important problem" — retained only concrete, evidence-backed strengths. **Removed.**

## Novel Insights

The harsh critic's observation that the global-value architecture is dimensionally underspecified (requiring aggregation from *n×d* matrix to a vector for MLP input) is a concrete, actionable finding that goes beyond the paper's own description. Conversely, an insight that emerged from cross-referencing the two reviews is that the *inference-time* claim (Eq. 9 shows the optimal action depends only on the local term) is actually well-supported by the architecture as described — the underspecification only affects training, where the global term contributes to the loss. This means fixing the global-branch specification is important for reproducibility but does not invalidate the core inference-time scalability claim.

## Suggestions

1. **Provide the missing 1024-node results** in a table or figure. Even a simple comparison of Generalist GCN DQN vs. Greedy on these large graphs would substantiate the scalability claim.
2. **Specify the global-value aggregation** explicitly in Section 3.4. If global pooling (mean, sum, max, or attention-based readout) is used, state which. If no aggregation is used, explain how the MLP handles the variable-size matrix input.
3. **Add confidence intervals or standard deviations** to all reported results (at minimum over the 10 evaluation episodes and ideally over multiple training seeds).
4. **Describe the offline optimal computation** in the evaluation section. State whether it is the network-flow solution over the exact request sequence, and cite the specific algorithm used.
5. **Clarify the WFA comparison** by moving the discussion of the information asymmetry from the footnote into the main results text, or by including a table column for the "ablated" condition where RL methods also use estimated arrival rates.
6. **Consider an ablation of the probability-to-rate conversion** and a brief comment on over-smoothing for the 12-layer GCN.
