Here is my final consolidated review.

---

## Summary

This paper proposes selective weight reinitialization (SWR), an algorithm that reinitializes low-utility individual weights to maintain plasticity in continually learning neural networks. It systematically compares weight-level reinitialization (SWR) against unit-level reinitialization (continual backpropagation, CBP) across four feed-forward architectures on permuted MNIST, plus ResNet-18 and vision transformers on incremental CIFAR-100. The paper identifies two concrete settings where weight reinitialization is more effective: (1) small networks and (2) networks with layer normalization. The central finding — that reinitializing weights maintains plasticity in a wider variety of architectural settings than reinitializing units — is well-supported by the experimental evidence.

## Strengths

- **SWR maintains plasticity across a broader range of architectures than CBP (Figure 2).** Figure 2 is the linchpin of the paper: SWR with initial-distribution reinitialization sustains stable online accuracy in all four tested settings (large/small networks, with/without layer normalization), whereas CBP maintains plasticity only in the large-network-without-layer-norm setting. This directly supports the paper's claim that weight-level reinitialization is more robust across architectural variations.

- **Provides a mechanistic explanation for why unit reinitialization fails in certain settings (Table 1).** Table 1 quantifies the absolute change in activation statistics after reinitialization. In small networks, reinitializing a single unit causes up to an order-of-magnitude larger change in sample average and standard deviation than reinitializing a weight. This provides a concrete, measurable reason why CBP underperforms when the network has few units or uses layer normalization — linking the failure mode to disruption of normalization statistics.

- **Systematic ablation of design choices (Figure 1).** The paper evaluates four combinations of utility functions (magnitude vs. gradient) and reinitialization strategies (to-mean vs. initial-distribution), showing that gradient utility coupled with initial-distribution reinitialization is required for full plasticity. This ablation goes beyond a simple method-vs-baseline comparison and builds understanding of *why* SWR works.

- **Rigorous experimental methodology.** All experiments use 10–30 independent runs with standard errors reported. Hyperparameters are tuned via grid search per architecture. The use of both the controlled permuted MNIST setting and the more realistic incremental CIFAR-100 (with ResNet-18 and ViT) provides complementary evidence at different scales.

- **Honest, appropriately scoped claims.** The paper explicitly states that "no single reinitialization strategy works best in all cases" (Section 6) and acknowledges the ResNet-18 results where CBP achieves better generalization. This transparency strengthens the credibility of the contribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No comparison against dynamic sparse training (DST) baselines.** The paper acknowledges that SWR "has parallels to dynamic sparse training algorithms" (Section 1.2) and cites Grooten et al. (2023) showing DST is robust to distribution shift. Yet no DST method (e.g., SET, RigL) is included in the experiments. Since DST also reinitializes weights (through pruning and regrowth), the paper would be significantly strengthened by including at least one DST baseline on permuted MNIST to contextualize where SWR adds value beyond existing methods that operate at the weight level.

- **Hyperparameter details not reported.** The paper states "We used a grid search to tune the hyper-parameters of each learning system for each architecture" (Section 4) but provides no grid ranges, number of trials, or final selected values. For CBP, the replacement rate and maturity threshold are critical; for SWR, the reinitialization frequency *τ* and proportion *p* are similarly important. Without these details, the experiments cannot be reproduced and the fairness of tuning across methods cannot be assessed.

- **No discussion of optimizer state handling during reinitialization.** The CIFAR-100 experiments use SGD with momentum of 0.9. When a weight is reinitialized, its momentum buffer is presumably stale — reinitializing without resetting the buffer could cause instability. The paper does not mention whether momentum buffers (or other optimizer state) are reset upon reinitialization.

- **Partial comparison on vision transformers.** CBP is applied only to feed-forward layers in ViT because "an extension of continual backpropagation for attention layers has yet to be proposed" (Section 5). This is transparently stated, but it means the ViT comparison is asymmetric — SWR operates on all parameters while CBP operates on a subset. A reader cannot rule out that extending CBP to attention layers (e.g., by treating attention weight matrices as sets of linear layers) might close the gap.

- **Asymmetric reinitialization schedule in the ViT layer-norm resetting baseline.** The CBP+layer-norm-resetting baseline resets layer norm parameters at task boundaries (privileged information), while SWR operates continuously without task boundaries. The paper acknowledges this asymmetry, but it means the statement "continual backpropagation matches the performance of selective weight reinitialization" conflates the reinitialization scheme (units vs. weights) with the reinitialization schedule (task-triggered vs. continuous). A cleaner comparison would also evaluate a variant of SWR that reinitializes only at task boundaries, or CBP that reinitializes continuously.

### Trivial

- The ResNet-18 result (Figure 3a) is presented as both methods "maintaining plasticity," with CBP showing higher accuracy. This is consistent with the paper's claims, but the framing could more explicitly distinguish between "maintaining plasticity" (the ability to learn new tasks at the level of a freshly initialized network) and "achieving better generalization." A short clarifying sentence in Section 5 would prevent misinterpretation.

## Nice-to-Haves

- A controlled ablation that equalizes the number of weights reinitialized per update between SWR and CBP would strengthen the argument that the granularity level (weights vs. units), not just the reinitialization rate, drives the performance difference.
- A runtime/flops comparison would help practitioners choose between methods.
- Statistical significance tests (e.g., paired permutation tests) for the key comparisons in Figures 2c vs. 2d would further solidify the conclusions.

## Removed Points

These points are flagged for removal; treat them with caution.

1. **"Mixed experimental evidence undermines central claim"** — The reviewer claims the ResNet-18 result contradicts the paper's central claim. This is incorrect: the paper's claim is that weight reinitialization *maintains plasticity* in more settings, not that it always achieves higher accuracy. In ResNet-18, both methods maintain plasticity (as the paper states), which is consistent with the claim. The paper deliberately says "equally effective at maintaining plasticity" for large networks without layer norm. The ViT layer-norm-resetting comparison is transparently discussed with its asymmetry acknowledged.

2. **"Biological plausibility discussion is padding"** — This is a few sentences at the end of a related-work paragraph. It is not "half a paragraph" and serves as reasonable motivation for why weight-level (synaptic) reinitialization is biologically grounded. Disagreement on taste, not a weakness.

3. **"Correlation vs. causation in Table 1"** — The paper says the statistics "partially explain" the performance drop, which is appropriately cautious language. No causal claim is made.

4. **"Reinitialization rate argument is thin"** — The paper provides concrete counter-evidence (small network with layer norm where CBP reinitializes 0.084 weights/update vs. SWR's 0.687), which directly supports their claim that rate is "not entirely responsible." The reviewer's reading misses this evidence.

5. **"Absolute accuracy numbers should be reported"** — The paper uses relative accuracy (difference from a freshly trained network), which is the standard and appropriate metric for isolating plasticity loss from other confounds.

6. **General formatting/style nitpicks, missing appendix, and hyperparameter detail demands that exceed typical standards** have been removed per the review guidelines.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add at least one DST baseline** (e.g., SET or RigL) on the permuted MNIST architectures to contextualize where SWR's weight-level approach adds value beyond existing weight-level reinitialization in sparse training.
2. **Report the tuned hyperparameter configurations** (grid ranges, final values for *τ*, *p*, replacement rate, maturity threshold) for each architecture in an appendix.
3. **Clarify optimizer state handling** — state explicitly whether momentum buffers and other optimizer state are reset when weights are reinitialized.
4. **Add a clarifying sentence** in Section 5 explaining that in ResNet-18, both methods maintain plasticity (achieve near-fresh-network accuracy), but CBP achieves higher *generalization* — reinforcing the distinction between plasticity maintenance and accuracy maximization.

## Score and Decision

This paper makes a clear, empirical contribution to the loss of plasticity literature. It proposes a practical algorithm (SWR), systematically compares weight-level vs. unit-level reinitialization, identifies two concrete architectural conditions where the distinction matters, and provides a mechanistic explanation (disruption of normalization statistics). The experiments are well-designed (multiple seeds, standard errors, controlled and realistic benchmarks) and the claims are appropriately scoped. None of the identified weaknesses undermine the core thesis that weight reinitialization maintains plasticity in a wider variety of settings than unit reinitialization. The paper would benefit from DST baselines and hyperparameter transparency, but these are addressable in revision and do not threaten the validity of the core findings.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>