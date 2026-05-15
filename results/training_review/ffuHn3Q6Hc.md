Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper proposes selective weight reinitialization (SWR), which reinitializes low-utility individual weights, and systematically compares it to continual backpropagation (CBP), which reinitializes entire units. Through experiments in permuted MNIST and class-incremental CIFAR-100, the paper identifies two settings where weight-level reinitialization is more effective than unit-level reinitialization: (1) when the network has a small number of units, and (2) when the network includes layer normalization. The paper also provides mechanistic evidence (Table 1) for why unit reinitialization disrupts layer normalization statistics.

## Strengths

- **Systematic isolation of two failure modes for unit reinitialization.** The paper cleanly disentangles network size and layer normalization as distinct factors through a four-setting experimental design (Figure 2: large/small networks with/without layer norm). SWR maintains stable plasticity across all four settings, whereas CBP only succeeds in the large network without layer norm. The evidence is clear and well-presented.

- **Mechanistic insight into the layer normalization failure.** Table 1 quantifies the absolute change in activation statistics after a reinitialization step, showing that CBP produces substantially larger disruptions than SWR (e.g., in the small network, changes of 0.14–0.30 for CBP vs. 0.01–0.03 for SWR). This goes beyond speculation and provides a concrete diagnostic for why unit reinitialization fails with layer norm.

- **Transparency about limitations and contradictory results.** The paper honestly reports that CBP outperforms SWR on ResNet-18 (Figure 3a), that CBP + layer norm resetting matches SWR on ViTs, and that no single reinitialization strategy dominates across all settings. This candor strengthens the paper's credibility significantly.

- **Validation on modern architectures with real-world data.** The CIFAR-100 experiments on ResNet-18 and Vision Transformers (Figure 3) demonstrate that the findings extend beyond simple feed-forward networks. The observation that SWR maintains plasticity without privileged task-boundary information (unlike CBP+layer norm resetting) is a practical strength.

- **Computational granularity advantage is well-argued.** The paper correctly identifies that in small networks, reinitializing a single unit replaces 10% of weights, whereas SWR can modify a far smaller proportion. This granularity argument is clean and supported by the reinitialization-rate analysis (line 100).

## Weaknesses

### Major
None.

### Minor

- **No empirical comparison to dynamic sparse training (DST) baselines.** The paper acknowledges DST in the related work (Section 1.2) and notes parallels, but never empirically compares SWR to a DST algorithm such as SET or RigL. Since DST methods also prune and regrow weights, and Grooten et al. (2023) showed they are robust to distribution shift, an empirical comparison is needed to demonstrate that SWR's advantage is not simply inherited from a known family of algorithms. The paper's claim that weight reinitialization "had remained unexplored in the loss of plasticity literature" (Section 3) is strictly about that sub-literature, but the practical novelty of SWR would be better established with DST baselines.

- **The ViT experiment weakens the layer-norm claim more than the paper acknowledges.** In Figure 3b, CBP + layer norm resetting (a simple intervention) matches SWR's performance. The paper notes that this baseline requires privileged task-boundary knowledge, which is a meaningful distinction. However, the abstract states that reinitializing weights "is more effective… when the network includes layer normalization" without qualifying that a straightforward modification to unit reinitialization eliminates the gap. The claim is technically true for the base algorithms compared, but the practical takeaway is more nuanced than the abstract suggests.

- **ResNet-18 results favor CBP over SWR.** On ResNet-18 (Figure 3a), CBP achieves higher test accuracy than SWR over most tasks. The paper frames this as showing SWR is "a viable strategy," but the fact that the main competitor outperforms SWR on a standard architecture deserves more discussion. It limits the generality of the paper's central narrative ("reinitializing weights is more effective") to architectures with specific properties (layer norm, small hidden layers).

- **Missing analysis of computational cost.** SWR with gradient utility requires computing gradient magnitudes, while CBP uses activation statistics. The paper mentions both can be implemented with "little computational overhead" but provides no runtime or FLOP comparison. This is relevant for practitioners choosing between the two methods.

### Trivial

- The paper uses "loss of plasticity" interchangeably with "loss of generalizability" (line 40), which differs from other papers that measure trainability. This is a reasonable choice but should be flagged more prominently when comparing to prior work.

- The reinitialization-rate analysis (line 100) is valuable but descriptive — the paper notes the rate is "not entirely responsible" without probing further.

## Nice-to-Haves

- An ablation study showing performance as a function of reinitialization frequency/proportion for both SWR and CBP would strengthen the comparison and address concerns about hyperparameter fairness.
- Visualizing which weights/layers SWR selects for reinitialization over time would provide deeper insight into the utility function's behavior.

## Removed Points

- **"Missing comparison to DST invalidates novelty"** — REMOVED. The paper explicitly acknowledges DST in Section 1.2, distinguishes SWR's goal (maintaining plasticity, not learning sparsity), and scopes its novelty claim to the loss of plasticity literature. The critic's assertion that SWR is "essentially identical to a DST regrowth step" is inaccurate: DST algorithms aim to discover sparse subnetworks, while SWR operates on dense networks with no sparsity objective. The point is retained in weakened form as a minor weakness (DST comparison would strengthen the paper), but the claim of invalidated novelty is rejected.

- **"Inconsistent reinitialization strategy choice across experiments"** — REMOVED. The paper explicitly states "no single reinitialization strategy works best in all cases" as a known limitation (Section 6). Tuning per setting is standard practice. Both SWR and CBP were tuned per architecture via grid search. The reinitialization-rate comparison (8.35 vs 1) is already discussed in the paper.

- **"Hyperparameter transparency"** — REMOVED. The paper states "We used a grid search to tune the hyper-parameters of each learning system for each architecture" (line 86). This is standard and sufficient for a conference paper.

- **"Formatting/style nitpicks" and "typos"** — REMOVED per instructions; these are parser artifacts.

- **"Missing appendix/proofs"** — REMOVED per instructions; the parser strips these sections.

- Strength Finder strengths that are generic or conflict with verified weaknesses: None removed — the strengths listed are specific and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective or synthesis that the paper does not already articulates.

## Suggestions

1. **Add a DST baseline** (e.g., SET or RigL) to the permuted MNIST and CIFAR-100 experiments. This is the single most impactful addition: it would either demonstrate that SWR offers a distinct advantage over existing weight-reinitialization schemes, or honestly reveal the overlap. Either outcome improves the paper.

2. **Nuance the abstract and conclusion** to reflect the ViT result: reinitializing weights is more effective than *unmodified* unit reinitialization when the network includes layer normalization, but a simple augmentation (layer norm resetting) closes the gap at the cost of requiring task-boundary knowledge.

3. **Add a computational cost comparison** (training time or FLOPs) for SWR vs. CBP, especially since SWR with gradient utility requires backpropagating gradient information.

4. **Discuss the ResNet-18 result more directly** — acknowledge that on architectures without layer normalization, CBP can outperform SWR, and clarify the precise scope where SWR's advantage holds.

## Score and Decision

This paper makes a genuine empirical contribution: it systematically compares weight-level vs. unit-level reinitialization for maintaining plasticity, cleanly identifies two settings where the granularity of weight-level reinitialization matters (small networks and layer-normalized networks), and provides mechanistic evidence. The paper is well-written and transparent about its limitations. The most significant gap is the absence of any DST baseline, which would better position the contribution. The claims in the abstract are slightly overbroad given the ViT and ResNet-18 results, but the paper itself honestly reports the countervailing evidence.

The paper is a solid empirical contribution — not groundbreaking, but useful and reproducible. Worth accepting with minor revisions to address the DST comparison and nuance the claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>