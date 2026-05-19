Now I have enough information. Let me compose the final consolidated review.

## Summary

This paper proposes Cyclic Neural Networks (Cyclic NN), a paradigm that removes the Directed Acyclic Graph (DAG) constraint from neural network design, allowing arbitrary cyclic connections between "computational neurons" trained with localized Forward-Forward objectives. The authors instantiate this in the GOMLP model and compare it against 4-neuron chain-based baselines on MNIST, NewsGroup, and IMDB. The core empirical finding is that an FF-trained fully-connected cyclic graph (FF-Complete) outperforms a BP-trained chain (BP-Chain*) on NewsGroup, and matches or slightly exceeds it on the other two datasets.

## Strengths

1. **Novel and thought-provoking core idea.** Removing the DAG constraint from ANN design is a genuinely underexplored direction that challenges a fundamental assumption. The biological motivation (connectome structure, local Hebbian-style learning) is well-articulated in Sections 1–2, and the conceptual departure from layer-by-layer stacking is clearly framed.

2. **Systematic graph topology comparison.** Table 1 shows a monotonic relationship between graph complexity and performance under FF training (FF-Cycle → FF-WSGraph → FF-BAGraph → FF-Complete), with error on MNIST dropping substantially (e.g., from FF-Cycle to FF-Complete). This provides direct evidence that richer non-DAG connectivity helps under local FF training, independent of the training-algorithm confound.

3. **Theoretical analysis of cyclic expressiveness.** Section 3.6 connects the cyclic structure to increased effective depth (growing with propagation steps T) without adding parameters, and the hyperparameter analysis (Figure 4) confirms that a small T (~3–5) is optimal. This gives a principled reason why cycles might help.

4. **Ablation study confirms both loss components are necessary.** Table 2 shows that removing either the neuron-level goodness loss (ℒ_N) or the readout loss (ℒ_Readout) causes significant degradation (e.g., MNIST error rises from 1.78% to 12.53% when ℒ_N is removed), validating the two-part local optimization design.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded evaluation design.** The headline comparison (FF-Complete vs. BP-Chain*) varies both the graph structure (complete graph vs. chain) and the training algorithm (FF vs. BP) simultaneously. This makes it impossible to attribute the observed advantage to the cyclic structure per se rather than to the change in architecture or training method. The missing critical baseline is **BP-Complete** (a cyclic/complete graph trained with BP, possibly by unrolling cycles for backprop). Without it, the paper cannot isolate the effect of cycles from the effect of FF training. This fundamentally weakens the central claim that cyclic structure is responsible for the performance gain.

2. **Overclaiming relative to evidence.** The paper claims that Cyclic NN demonstrates "superiority over current layer-by-layer DAG neural networks" (abstract) and that "the Forward-Forward training algorithm also firstly outperforms the current Back-Propagation algorithm" (abstract). The evidence only supports that a specific FF-trained cyclic model (FF-Complete) beats one specific BP-trained chain model (BP-Chain*) on three small datasets—with margins of ≤0.1% on two of them. The claim about outperforming "the BP algorithm" as a general method is not supported by comparisons against BP-trained cyclic networks, deeper BP networks, or modern architectures (CNNs, Transformers). These claims should be calibrated to the actual scope of the evidence.

3. **No statistical reliability.** All results in Table 1 are reported as single numbers without variance, confidence intervals, or significance tests. Given that the margins on MNIST and IMDB are very small (≤0.1% absolute according to the reported numbers), the observed differences could easily flip under different random seeds or initializations. The paper does not demonstrate that its findings are statistically stable.

4. **Limited experimental scope.** The paper tests on only three small datasets (MNIST, NewsGroup, IMDB), uses only 4 computational neurons in all experiments, and compares only against minimal chain-based baselines. There is no evaluation on larger-scale datasets (CIFAR-10/100, ImageNet subset), no scaling study with more neurons, and no comparison against any architecture with practical relevance (deeper MLPs, CNNs, or Transformers). For a paper claiming a "transformative" new design paradigm, this scope is too narrow to establish generality.

### Minor

1. **No comparison with other local learning methods on the same cyclic structure.** The paper claims to be "the first to beat global BP training with pure localized learning algorithm based on cyclic structure" (Section 5.2), but does not experimentally compare FF-Complete against alternatives such as Feedback Alignment, Equilibrium Propagation, or layer-wise BP training on the same cyclic graph. This would strengthen the attribution of success to the FF/local approach specifically.

2. **Stability analysis is missing.** While the paper mentions over-smoothing for large T (Section 4.3), it does not analyze whether the iterative propagation in cyclic networks converges, oscillates, or diverges. This is relevant since recurrent computation over T steps with no gradient gating could amplify noise or settle into trivial fixed points.

3. **The "computational neuron" design conflates two changes.** Each GOMLP neuron is parameterized as a linear layer (rather than a scalar neuron), which is motivated by biological evidence (Beniaguev et al., 2021). However, this change in neuron capacity is a separate design variable from the cyclic connectivity. The experiments do not isolate whether the performance gain comes from cycles, from increased per-neuron capacity, or from their combination.

### Trivial
None.

## Nice-to-Haves

- Adding visualizations or post-hoc analysis of what individual computational neurons learn during cyclic propagation would strengthen the biological plausibility narrative.
- A discussion of how Cyclic NN relates to recurrent neural networks (RNNs) and reservoir computing, which also involve cyclic/feedback connections, would help position the contribution.

## Removed Points

The following weaknesses from the inputs are removed with justification:

- **"BP-Chain* is poorly described"** (Harsh Critic): The paper states "BP-Chain*: Layer-by-layer networks trained with BP as depicted in Figure 2(a)" and distinguishes it from BP-Chain (Figure 2(b)). This is an adequate description; the reviewer's difficulty likely stems from parser-stripped figures.
- **"No analysis of what the cycles actually learn"** (Harsh Critic): This is a nice-to-have enhancement, not a weakness. The paper's primary goal is to establish feasibility and comparative performance, not to provide mechanistic interpretability.
- **"Pure formatting/style nitpicks" / parser artifacts** (Harsh Critic): Removed per hard rules.
- **Strength about "first FF outperforming BP"** (Strength Finder): While the empirical observation stands, this strength partially conflicts with the verified confounded-comparison weakness. Retaining it without qualification would be misleading, so it is moved here. The underlying observation that FF-Complete beats BP-Chain* on NewsGroup is treated as part of the paper's descriptive results, not as a validated strength supporting the causal claim.
- **Generic strength about the problem being "important"** (Strength Finder): Removed as generic/superficial per filtering instructions.

## Novel Insights

The most interesting observation emerging from the intersection of the two reviews is that **the paper's strongest evidence (monotonic improvement with graph complexity under FF training) is actually independent of the BP comparison.** The fact that FF-Cycle → FF-WSGraph → FF-BAGraph → FF-Complete shows consistently decreasing error rates under the same training algorithm is a clean, unconfounded result supporting the value of richer connectivity. Meanwhile, the paper's flagship claim about "beating BP" rests on the weakest experimental footing (confounded comparison, single-run numbers, minimal baseline). This asymmetry suggests the paper would be more convincing if it repositioned its contribution around the expressiveness advantage of cyclic/local training combinations rather than positioning itself as a BP-defeating result.

## Suggestions

1. **Add the BP-Complete baseline.** Train the same complete graph structure using BP (unrolling cycles for backprop or using truncated BPTT). This is the single most important experiment needed to attribute the observed gains.
2. **Report means and standard deviations over at least 5 random seeds.** This is essential given the small margins on MNIST and IMDB.
3. **Scale up.** Test with more computational neurons (e.g., 8, 16, 32) and at least one larger dataset (e.g., CIFAR-10) to demonstrate that the approach generalizes beyond toy-scale problems.
4. **Calibrate the claims.** Tone down the language from "outperforms BP" / "transformative paradigm" to claims commensurate with the evidence: e.g., "we show that cyclic connectivity improves expressiveness under local FF training and can match or exceed a simple BP-trained chain baseline on small-scale tasks."
5. **Include at least one other local learning method** (e.g., Feedback Alignment or layer-wise BP) on the complete graph to isolate whether the benefit is specific to FF or general to local training of cyclic networks.

## Score and Decision

The paper proposes a genuinely novel and thought-provoking direction — removing the DAG constraint from ANN design — and provides a concrete instantiation with some supporting experiments. However, the evaluation suffers from a confounded comparison that undermines the central claim, overclaiming relative to the evidence, no statistical rigor, and very limited experimental scope. These are addressable in a revision but are significant as presented.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>