Now let me produce the final consolidated review.

## Summary

This paper introduces DelRec, a method for learning per-neuron axonal (or per-synapse synaptic) delays in recurrent connections of spiking neural networks using surrogate gradient learning. The method extends differentiable triangle-function interpolation (from DCLS) to the recurrent setting via a scheduling matrix with a pointer mechanism. DelRec achieves 82.58% on SSC and 96.21% on PS-MNIST using only simple LIF neurons, outperforming prior methods that rely on more complex neuron models. A controlled ablation on SHD demonstrates that recurrent delays improve temporal processing in the low-parameter regime.

## Strengths

1. **New SOTA on SSC and PS-MNIST using only LIF neurons.** Table 1 shows DelRec (only Rec. delays) achieves 82.58±0.08% on SSC and 96.21% on PS-MNIST, surpassing prior best methods including SiLIF (82.03%) and ASRC-SNN (95.77%). The LIF column in Table 1 confirms that DelRec uses vanilla LIF neurons while all higher-ranked competitors in prior work use adaptive, resonant, or state-space neuron models. This is concrete quantitative evidence for the method's effectiveness.

2. **Controlled 6-model ablation isolating the benefit of recurrent delays.** Figure 3 systematically compares vanilla SNN, vanilla RSNN, feedforward delays, fixed random recurrent delays, learned recurrent delays, and combined delays — all at matched parameter counts on SHD. This disentangles the benefit of learning delays from merely having delays, and compares recurrent vs. feedforward delays under equal compute budgets. The inclusion of fixed random recurrent delays as a baseline is a good methodological control.

3. **First SGL-based method for per-neuron delays in recurrent connections.** The literature review correctly identifies that prior recurrent-delay methods either learn a single delay per layer (Xu et al.) or use EventProp exact gradients (Mészáros et al., 2025), while SGL is the dominant paradigm for these benchmarks. DelRec is differentiated by bringing per-neuron axonal delay learning via SGL to recurrent connections, which the ablation confirms is beneficial.

4. **Methodological rigor on SHD.** The paper uses a clean 20% validation split, reports Bayesian confidence intervals acknowledging that the small test set (2264 samples) makes high-accuracy comparisons statistically noisy, and trains on 10 seeds. This is more transparent than many prior SNN papers on this benchmark.

## Weaknesses

### Major

None.

### Minor

1. **Abstract's SOTA claim is unqualified.** The abstract states "new state-of-the-art (SOTA) on two challenging temporal datasets" without qualification. However, Wang et al. (2024) report 83.69% on SSC using attention-based neurons — higher than DelRec's 82.58%. While the paper's footnote 1 and main text explain these are excluded because they use more complex neuron models, the abstract does not convey this scope limitation. A qualification like "SOTA among LIF-based models" would be more precise and prevent misleading readers.

2. **"Recurrent delays outperform feedforward" claim is too broad.** The abstract states this as a general finding, but the evidence comes from the low-parameter regime (Figure 3, ~10k params) where comparisons are at matched parameter counts. On large SHD models (Table 2), DCLS (feedforward-only delays) achieves 93.77±0.68% while DelRec (recurrent-only) achieves 93.39±0.45% — the feedforward model performs better by mean accuracy. The paper should scope this claim to the low-parameter regime and discuss the interesting reversal at scale.

3. **Combined model underperforms recurrent-only on SSC without discussion.** In Table 1, DelRec with both recurrent and feedforward delays (82.19±0.16%, 0.55M params) underperforms DelRec with only recurrent delays (82.58±0.08%, 0.37M params). The combined model has ~50% more parameters yet does worse. This puzzling reversal on the paper's flagship dataset is never discussed, which undermines confidence in the combined training procedure and leaves readers questioning whether optimization interference is at play.

4. **No analysis of learned delay values.** The paper learns per-neuron delays but never shows what values are learned, whether they converge to interpretable patterns, or how they distribute across neurons. A histogram or analysis for the SSC model would provide insight into whether the method learns diverse delays or collapses to a few values. This is a natural and expected analysis for a delay-learning paper.

5. **Computational cost not discussed.** The scheduling matrix has dimension N × dim(Ẽ(σ, D)), which grows with the maximum delay and σ. At early epochs (σ=5), this buffer can be substantial. The memory and per-step computational overhead compared to a vanilla RSNN of equal size is never quantified, making it difficult for practitioners to assess deployability. Reference to Algorithm 1's pointer mechanism partially addresses efficiency but does not quantify the overhead.

6. **PS-MNIST result from a single seed.** The paper reports 96.21% on PS-MNIST from one seed, justifying this by noting "all the previous state-of-the-art models on the dataset" use one seed. This justification is circular — running baselines on one seed does not justify running your method on one seed. Without variance information, the improvement over ASRC-SNN's 95.77% may or may not be meaningful.

### Trivial

None.

## Nice-to-Haves

- A controlled comparison against a per-layer delay baseline (Xu et al. variant) with matched architecture would isolate the benefit of finer-grained delay allocation.
- The "SHD is saturated" argument could be strengthened by showing near-ceiling performance across many diverse methods, rather than relying solely on the small-test-set argument.

## Removed Points

- **"Xu et al. partially undercuts 'first SGL-based method' claim":** The paper's claim is about *per-neuron* (axonal/synaptic) delays specifically, which Xu et al. did not do. The paper already acknowledges Xu et al.'s approach and the distinction is per-neuron vs per-layer. Weakness removed per rule against strawman misunderstandings.
- **"SHD saturation claim is a non sequitur":** The paper's argument about SHD saturation is based on the small test set (2264 samples) with overlapping Bayesian confidence intervals, citing prior work (Mészáros et al., 2025). This is reasonable evidence, not a non sequitur. The critic's objection is not well-grounded.
- **Generic formatting/style nitpicks, missing appendix content, reproducibility concerns about hyperparameters, etc.:** Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Qualify the SOTA claim in the abstract (e.g., "SOTA among LIF-based models").
2. Scope the "recurrent delays outperform feedforward" claim to the low-parameter regime, and discuss why the trend reverses at scale.
3. Add a paragraph discussing why the combined model underperforms recurrent-only on SSC — optimization interference, overfitting, or something else.
4. Include a histogram or analysis of learned delay values (e.g., for the SSC model).
5. Report multi-seed results for PS-MNIST, or at minimum state the limitation transparently rather than relying on the circular justification.
6. Quantify the computational overhead (training time, memory) of the scheduling buffer relative to a vanilla RSNN.

## Score and Decision

**Calibration anchor table:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| fnO5h1CFyh (Hebbian Temporal Memory) | 3.00 | R1-weak | The paper is substantially stronger |
| 7eYmijcuqO (RNN Dynamics) | 3.00 | R1-weak | Much weaker than DelRec |
| SI6zocV2SS (Continually Adapting) | 1.50 | R1-weak | Much weaker |
| XMaPp8CIXq (Sparse Training) | 3.00 | R1-weak | Much weaker |
| pIJR9uPjy3 (Delay Neural Networks) | 4.50 | R1-mid | Very topically similar but weaker — DeNN uses only delays (no weights), has unclear exposition and weaker benchmark results |
| A6K4aqReoF (Binary Activation Recurrent) | 3.75 | R1-mid | Weaker |
| 6iM7mmVhXh (Layer Synchronization) | 5.75 | R1-mid | Comparable tier but DelRec has cleaner method and stronger results |
| vq75kRCYuY (SOLO) | 4.00 | R1-mid | Weaker |
| yBP36xQhZl (Forward Gradient SNN) | 5.00 | R2 | Weaker |
| mJ4mgYjDru (QIF Neuron) | 4.60 | R2 | Weaker |
| ZN8BaYVFkx (Adversarially Robust SNN) | 5.50 | R2 | Comparable tier, DelRec has stronger benchmark results |
| eN4g4cjFX1 (Spatio-Temporal Dependency) | 5.75 | R2 | Similar quality level |
| drPDukdY3t (DeepTAGE) | 6.25 | R2 | Comparable — both are solid incremental SNN methods with SOTA results; DeepTAGE accepted |
| 9HsfTgflT7 (Temporal Flexibility) | 6.20 | R2 | Comparable — both are solid incremental contributions; Temporal Flexibility accepted |
| XrunSYwoLr (Spatio-Temporal Approximation) | 7.00 | R2 | Stronger — addresses the harder ANN-to-SNN conversion problem for Transformers |
| RWJX5F5I9g (Brain Bandit) | 8.00 | R1-strong | Stronger — has theory + biological grounding |
| Xo0Q1N7CGk (Grid Cells) | 8.00 | R1-strong | Stronger — theoretical contribution |
| GRMfXcAAFh (Oscillatory State-Space) | 8.00 | R1-strong | Stronger — theory + universality proof |
| cNmu0hZ4CL (Neural Population Dynamics) | 8.00 | R1-strong | Stronger |

**Round 1 bracket:** 4.5 – 7.0

**Round 2 narrowing:** Compared to accepted papers at 6.2–6.25 (DeepTAGE, Temporal Flexibility), DelRec has comparable method quality and stronger empirical results (actual SOTA on two benchmarks) but suffers from framing overclaims and missing analyses that the accepted papers handled better. Compared to rejected papers at 5.0–5.75 (Forward Gradient, Layer Synchronization), DelRec is clearly stronger — its method is cleaner, ablation is more thorough, and results are more convincing. The paper sits between these groups.

**Final score: 6.0** — A solid paper with a clean incremental contribution. The method (extending differentiable delay interpolation to recurrent connections) is well-motivated and clearly described. The ablation study is informative and the SOTA results on two benchmarks are genuine. However, the abstract overclaims (unqualified SOTA, unqualified outperformance claim), the puzzling combined-model underperformance on SSC goes undiscussed, and the lack of delay-value analysis and single-seed PS-MNIST result leave clear gaps. These issues are all fixable with text revisions and one additional analysis, making the paper a solid candidate for acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>