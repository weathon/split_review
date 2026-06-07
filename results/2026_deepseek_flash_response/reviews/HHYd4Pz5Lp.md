## Summary

DelRec introduces the first surrogate-gradient-based method to learn per-neuron (axonal) delays in recurrent connections of spiking neural networks. The approach uses a differentiable triangle-function interpolation with an annealed spread parameter σ to handle real-valued delays during training, rounding to integer delays at inference. Experiments on SSC (82.58±0.08%), PS-MNIST (96.21%), and SHD show competitive or SOTA results within the class of simple LIF-based models. A functional study on SHD with ~10k-parameter models systematically demonstrates that learned recurrent delays outperform learned feedforward delays under low-parameter constraints.

## Strengths

1. **First SGL-based method for learning per-neuron delays in recurrent SNN connections** — The paper correctly identifies that prior recurrent-delay work either learns a single shared delay per layer via softmax selection (Xu et al.) or relies on EventProp (Mészáros et al., 2025). DelRec is genuinely the first to learn per-neuron delays in recurrent connections using surrogate gradients. The differentiable triangle-function interpolation (Eq. 9) with annealed σ is a natural and technically sound extension of DCLS (Hammouamri et al., 2024) to the recurrent case.

2. **Systematic ablation study isolating the benefit of recurrent delays** — Section 3.2 (Fig. 3B–C) is the paper's strongest empirical contribution. At ~10k parameters, learned recurrent delays achieve ~82% on SHD vs. ~80% for learned feedforward delays, ~78% for fixed random recurrent delays, and ~60% for vanilla SNN. The accuracy-vs-parameter count curves show recurrent delays degrade less steeply as network size shrinks, directly demonstrating that recurrent delays improve parameter efficiency for temporal processing.

3. **Transparent handling of dataset saturation on SHD** — The paper explicitly acknowledges SHD is saturated (line 176), uses a proper train/validation split (20% of training set), reports results over 10 seeds with Bayesian confidence intervals, and recommends SHD only for proof-of-concept validation. This methodological rigor strengthens confidence in the SSC/PS-MNIST results.

4. **Clean, reproducible implementation** — The method is implemented in SpikingJelly, provides detailed hyperparameters in the appendix, and is compatible with any neuron model fitting the Eqs. 1–3 formalism.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **PS-MNIST result lacks variance information** — The paper reports 96.21% on PS-MNIST from a single seed, with a ~0.44% gap over the prior best (95.77%). The paper states "we only test one seed as all the previous state-of-the-art models on the dataset" (line 132), but this does not justify the absence of variance for the authors' own result. A 0.44% gap could fall within run-to-run variation. This weakens the SOTA claim on PS-MNIST.

2. **Unexplained Rec.+Ff. performance discrepancy on SSC** — On SSC (Table 1), the combined Rec.+Ff. delays configuration achieves 82.19±0.16%, while the simpler Rec.-only configuration achieves 82.58±0.08% — i.e., combining both delay types *hurts* performance. On SHD (Table 2), the pattern reverses (combined: 93.73±0.69% vs. recurrent-only: 93.39±0.45%). The paper presents combining both delay types as a contribution ("our study is the first to combine the optimization of feedforward delays... and delays in recurrent connections," line 36) but does not discuss this inconsistency. This raises questions about whether the interaction between the two mechanisms is well understood.

3. **No analysis of what delays are actually learned** — The paper never shows a histogram or distribution of the learned delay values \(d_j\) across neurons or layers. Such an analysis would directly illustrate whether the optimization discovers meaningful structure (e.g., spread of delays, clustering at certain values, differences across layers) and would be the single most informative addition within the paper's own framing.

4. **No discussion of computational overhead** — The scheduling matrix has dimension \(N \times \dim(\tilde{\mathbb{E}}(\sigma, D))\), which scales with the maximum learned delay. The paper does not discuss the memory or wall-clock time costs of this mechanism, which is relevant given that SNN research often motivates energy efficiency.

### Trivial
None.

## Nice-to-Haves
- Ablation of σ annealing schedule sensitivity (initial σ value, rate of decrease).
- Testing the synaptic delay variant (one delay per synapse) to validate the claimed compatibility.
- Additional comparisons on other standard neuromorphic datasets (e.g., DVS-Gesture, N-MNIST) would broaden the empirical support.

## Removed Points
- **SOTA claim lacking qualification**: The abstract states "using only vanilla Leaky-Integrate-and-Fire neurons with stateless (instantaneous) synapses," which qualifies the comparison class. The models with higher raw accuracy (Zheng et al. 82.46%, Wang et al. 83.69%) use multi-compartment neurons, attention, or GRU mechanisms — not LIF. Footnote 1 is transparent about these exclusions. The claim is properly scoped.
- **"Eliminates the need to predefine a maximum delay range" vs. Eq. 13**: The buffer dimension in Eq. 13 depends on learned \(d_j\) values, not a predefined maximum. The method genuinely avoids requiring the user to choose a fixed range beforehand, unlike softmax-based selection from a discrete set. The harsh critic's concern here stems from a misunderstanding.
- Various formatting/style nitpicks and missing-appendix concerns (parser artifacts).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Run PS-MNIST with at least 3 seeds and report mean ± std, or explicitly acknowledge the limitation and provide justification (e.g., stability analysis across training runs showing low variance on this task).
2. Discuss the Rec.+Ff. vs. Rec.-only discrepancy on SSC — whether it is a statistical fluctuation, an optimization difficulty (e.g., interference between the two delay optimization mechanisms), or a genuine interaction. If the combined version is not reliably beneficial, the claim about combining them should be softened.
3. Include histograms or summary statistics of the learned delay values \(d_j\) across layers and seeds.
4. Report training time and memory footprint of the scheduling mechanism versus baseline models without recurrent delays.

## Score and Decision

**Calibration anchors consulted (all rounds):**

| Anchor | Path | Avg Score | Round | Comparison to DelRec |
|--------|------|-----------|-------|---------------------|
| Delay Neural Networks (DeNN) | pIJR9uPjy3.md | 4.50 | R1 | DelRec is stronger: clearer exposition, sounder method, more thorough ablation |
| Forward Gradient Training (FGT) | yBP36xQhZl.md | 5.00 | R2 | DelRec is stronger: more novel contribution, better empirical rigor |
| Temporal Flexibility in SNNs | RmQAKu1wCe.md | 5.00 | R2 | Comparable; DelRec has more novel method but narrower evaluation |
| ST-DANO | eN4g4cjFX1.md | 5.75 | R2 | DelRec has more novel contribution but narrower experimental scope; slightly weaker overall |
| Layer Synchronization | 6iM7mmVhXh.md | 5.75 | R1/R2 | Comparable quality; DelRec has better clarity but less fundamental topic |
| DeepTAGE | drPDukdY3t.md | 6.25 | R2 | DelRec is weaker: DeepTAGE has broader evaluation (ImageNet-scale) and was accepted |

**Round 1 bracket**: 4.5–6.0  
**Round 2 narrowing**: Compared against DeNN (4.50), FGT (5.00), ST-DANO (5.75), DeepTAGE (6.25). DelRec is clearly above 4.50 and 5.00 anchors, comparable to but slightly below the 5.75 anchors, and below the 6.25 accepted paper.  
**Final score**: 5.0 — solid contribution with genuine novelty, but the experimental validation has gaps (PS-MNIST single seed, unexplained Rec.+Ff. discrepancy, no delay analysis, no overhead discussion) that collectively prevent it from meeting the acceptance bar at ICLR in its current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>