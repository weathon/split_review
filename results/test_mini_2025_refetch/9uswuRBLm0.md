Now I have all the calibration I need. Let me synthesize the final review.

**Final bracket analysis:**
- **Round 1 bracket**: 3.5–5.0 (below the 7.5+ Oral papers, below the 5.75 accepted poster, comparable to rejected papers in the 4.0–5.5 range)
- **Round 2 narrowing**: Comparing to Trifecta (5.0, rejected: better experiments but less novelty), GIFF (4.0, withdrawn: similar experiment quality, comparable issues), and LCN (5.5, rejected: better experiments but similar missing comparisons), the current paper's uncontrolled parameter count confound is a more fundamental issue than these comparators faced. The paper has genuine conceptual novelty but its central experimental claim is not properly validated.
- **Final score**: **4.0** — an interesting idea with insufficiently rigorous experimental support.

Now writing the review.

---

## Summary

This paper proposes Cyclic Neural Networks (Cyclic NN), a new architecture paradigm that removes the Directed Acyclic Graph (DAG) constraint from neural networks, allowing neurons to be connected in arbitrary graphs including cycles. The authors instantiate this as Graph Over Multi-Layer Perceptron (GOMLP), trained with localized Forward-Forward (FF) objectives, and evaluate it on MNIST, NewsGroup, and IMDB across multiple graph topologies (Chain, Cycle, Watts-Strogatz, Barabási-Albert, Complete). The paper claims that cyclic/graph-structured networks outperform DAG architectures and that this is the first instance of FF training surpassing Back-Propagation.

## Strengths

1. **Conceptually novel paradigm.** The paper challenges a fundamental and largely unquestioned design principle of ANNs — the DAG constraint — and proposes an alternative where computation flows over arbitrary graph structures. This is a genuinely thought-provoking departure from layer-by-layer designs and opens up a new axis of architectural exploration.

2. **First empirical evidence that FF can beat BP on some datasets.** Table 1 shows that FF-Complete achieves 1.54% error on MNIST (vs. 1.74% for the best BP model) and 38.26% on NewsGroup (vs. 38.85% for BP). This is a noteworthy milestone given that previous FF implementations (Hinton, 2022) lagged substantially behind BP.

3. **Systematic exploration of graph topologies.** The paper tests Chain, Cycle, Watts-Strogatz, Barabási-Albert, and Complete graphs, showing a clear trend where richer connectivity correlates with better performance. This goes beyond a single architecture and provides evidence that graph structure matters.

4. **Useful ablation and sensitivity analysis.** Table 2 confirms that both the neuron-level local loss (ℒ<sub>N</sub>) and the readout loss (ℒ<sub>Readout</sub>) contribute to performance. Figure 4 provides practical guidance on the propagation steps T (optimal ~3–4) and threshold θ.

## Weaknesses

### Major

- **Uncontrolled parameter counts invalidate the central comparison.** This is the most critical issue. The paper's core claim — that cyclic/graph-structured neural networks outperform chain-structured (DAG) networks — cannot be properly evaluated because model capacity is not controlled. In GOMLP, each neuron receives the concatenated outputs of all its pre-synapse neurons (Equation 4). Under the Complete graph, each neuron receives input from *all other neurons* (n−1=3 pre-synapse neurons plus the input feature), making each weight matrix of dimension d_out × (d_input + 3·d_out). Under the Chain graph, each neuron only receives input from the previous neuron plus the original input, yielding much smaller weight matrices (d_out × (d_input + d_out)). The paper states "We keep 4 computation neurons for all methods during the experiments" (Section 4.1), but keeping the *number of neurons* fixed does not keep the *number of parameters* fixed. Without controlling for total parameter count or FLOPs, the observed performance gains of FF-Complete over FF-Chain could be trivially explained by increased model capacity rather than the presence of cycles or graph topology. A fair comparison would require either matching parameter counts (e.g., widening or deepening the chain to match the Complete graph's parameter count) or ablating where the Complete graph's advantage persists under matched capacity. This is not provided, and it undermines the paper's main experimental conclusion.

### Minor

- **"First FF to beat BP" claim is only partially supported.** Examining Table 1: FF-Complete beats the best BP model on MNIST (1.54 vs. 1.74) and NewsGroup (38.266 vs. 38.85), but *loses* on IMDB (17.58 vs. 17.16 for BP-Chain\*). The claim is technically correct only if one cherry-picks datasets and baselines. On IMDB, BP still outperforms FF. The framing as "first to beat BP" (abstract, Section 1, conclusion) is overstated and should be qualified.

- **Missing comparison to recurrent/iterative baselines.** The cyclic architecture with T propagation steps is structurally analogous to an RNN unrolled for T iterations over a fixed set of hidden states. The paper does not compare against any RNN or iterative message-passing baseline trained with local FF losses (or even BP). Without this comparison, it is unclear whether the benefit comes from the graph structure, the iterative propagation (which an RNN also provides), or the specific combination. The claim in Section 3.6 that cycles increase effective depth is similarly true for any recurrent architecture.

- **Limited evaluation scale.** All experiments use only 4 computational neurons and three small datasets (MNIST, NewsGroup, IMDB). MNIST and NewsGroup are near-saturated benchmarks where even small models achieve <2% error. The paper does not demonstrate scalability to larger models (more neurons), harder problems (CIFAR-10, ImageNet), or more complex tasks. This makes it difficult to assess whether the paradigm has practical relevance beyond the toy setting.

- **Biological plausibility claim overstates the implementation.** The paper motivates "computational neurons" by citing Beniaguev et al. (2021), which shows a single biological neuron is as computationally powerful as a shallow MLP. However, the actual implementation (Equation 3) is a single linear layer with ReLU — far weaker than an MLP. The paper also invokes biological parallels for local learning and arbitrary connectivity, but these are functional analogies, not faithful models of biological learning. The biological framing should be toned down to match what is actually implemented.

### Trivial

- The complexity analysis in Section 3.5 is informal: the reduction from O(T·|E|·|V|) to O(|E|) via parallel updates conflates wall-clock time with asymptotic complexity and does not account for the internal dimension-dependent cost of each neuron's linear layer.

## Nice-to-Haves

- Compare FF-Complete against a wider chain or deeper chain with the same total parameter count to isolate the effect of graph topology from capacity.
- Compare against an RNN or GGNN trained with FF (or BP) to isolate what the fixed-graph architecture adds beyond recurrence.
- Include a random graph (Erdős–Rényi) baseline to test whether specific graph properties (small-world, scale-free) matter beyond simple connectivity.
- Report parameter counts and FLOPs for every model in Table 1.
- Test on a larger-scale dataset (e.g., CIFAR-10) with more neurons to demonstrate scalability.

## Removed Points

- **Criticism that the method is "essentially a GNN":** The graph in GOMLP is the model architecture (fixed across inputs), whereas GNNs operate on data graphs (varying per input). This is a meaningful distinction. The paper's related work discussion could be improved, but this is not a fatal weakness.
- **Claim that the goodness function has a normalization bug:** The critic initially raised a concern about the output norm being constrained, then acknowledged it was not. This is not an actual issue.
- **MLP-Ensemble is a "poor baseline":** The paper deliberately uses small models (4 neurons/4 MLPs) for comparability. The low absolute accuracy on MNIST is because models are tiny, not because the baseline is poorly chosen.
- **Complexity analysis is conflating concepts:** The analysis is informal but directionally reasonable for the parallel setting. Not a significant weakness.
- **Missing Erdos-Renyi graph:** A reasonable suggestion but not a required baseline.
- **Missing related works references:** The paper adequately covers GNNs, RNNs, and local learning. I cannot verify missing citations.
- **Formatting/style nitpicks, reproducibility concerns (undisclosed hyperparameters), missing appendix content:** These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The core observation — that removing the DAG constraint and training with local FF objectives is feasible and can yield competitive results — is the paper's genuine contribution. The reviews surface no unclaimed insight.

## Suggestions

1. **Control for parameter count.** This is essential: rerun the comparison between FF-Complete and FF-Chain with matched total parameters (by widening the chain or increasing its depth). Report parameter counts and FLOPs for all models in the table.

2. **Add an RNN baseline.** Compare GOMLP against an RNN unrolled for T steps with local FF losses. This isolates what the graph structure adds beyond iterative propagation.

3. **Qualify the "first FF to beat BP" claim.** Acknowledge that this holds on 2 of 3 datasets and specify which BP baseline is being compared against.

4. **Expand the evaluation.** Test with more neurons (e.g., 8, 16) and on a slightly larger dataset (Fashion-MNIST, CIFAR-10) to demonstrate that the approach scales.

5. **Tone down biological plausibility.** The current implementation uses linear layers and binary classification losses. The biological analogy is functional, not structural. This should be stated explicitly.

---

**Round 1 bracket**: 3.5–5.0 (the paper sits below strong posters at 5.75 and above clearly weak papers at 3.0)

**Round 2 anchors consulted**: 
- `wcKGK0tRHD.md` (avg 5.0, Reject) — Trifecta FF improvements. Better experiments (CIFAR-10, multiple architectures) but less conceptual novelty. The current paper is weaker due to the parameter confound.
- `wUKVia7J10.md` (avg 4.0, Withdrawn/Reject) — GIFF. Similar scale experiments, similar unfair comparison issues. The current paper has more novelty but a more fundamental methodological flaw.
- `qMUtej58Pc.md` (avg 5.5, Reject) — LCN. Bio-inspired architecture with better experiments (CIFAR-10). The current paper is less convincing experimentally.
- `r2ve0q6cIO.md` (avg 4.25, Reject) — GNN-async. Stronger theory but limited experiments. Comparable overall weakness in supporting claims.
- `cUFIil6hEG.md` (avg 5.75, Accept Poster) — NiNo. More thorough experiments, accepted. The current paper is clearly below this bar.
- `NJ6nyv3XWH.md` (avg 3.0, Reject) — GNN for fine-grained classification. Weaker novelty and insight. The current paper is above this.

**Final score**: **4.0** — The paper presents a genuinely interesting architectural paradigm, but the central experimental comparison is confounded by uncontrolled parameter counts. The evaluation is limited to tiny models and small datasets, and the "first FF to beat BP" claim is only partially supported. The core idea has merit and could form the basis of a strong paper with properly controlled experiments and broader evaluation, but in its current form the evidence does not support the claims made.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>