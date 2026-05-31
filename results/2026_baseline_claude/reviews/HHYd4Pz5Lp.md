## Summary

DelRec is a surrogate gradient learning (SGL)-based method for optimizing axonal/synaptic transmission delays in recurrent spiking neural network (RSNN) connections. The core technique is a differentiable triangle-function interpolation that spreads scheduled spikes over neighboring time steps during training (with a progressively decreasing width σ → 0), enabling gradient-based optimization of continuous delay parameters that are subsequently rounded to integers at inference. Using simple LIF neurons, DelRec achieves new state-of-the-art accuracy on the Spiking Speech Commands (SSC) and Permuted Sequential MNIST (PS-MNIST) benchmarks, and matches the SOTA on the saturated Spiking Heidelberg Digits (SHD) dataset.

---

## Strengths

- **First SGL-based method for recurrent delay learning with a clear technical gap addressed.** Prior work on learnable recurrent delays (Mészáros et al., 2025) used EventProp, which has scalability limitations. All SOTA SNN methods use SGL, making this a natural and practically significant extension. The scheduling matrix + pointer mechanism is an elegant engineering solution.

- **Compelling empirical results with simple neurons.** Achieving new SOTA on SSC (82.58±0.08%) and PS-MNIST (96.21%) using vanilla LIF neurons—rather than adaptive, resonant, or multi-compartment models used by competing approaches—powerfully isolates the contribution of learnable recurrent delays and demonstrates their representational power.

- **Meaningful ablation study.** Section 3.2 carefully disentangles the roles of delay type (feedforward vs. recurrent), delay learning (fixed random vs. learned), and recurrent connections (vanilla RSNN vs. delayed RSNN) under matched parameter budgets. The finding that learned recurrent delays dominate at small parameter counts, while feedforward delays achieve competitive accuracy at lower firing rates (better energy efficiency), is a genuinely useful practical characterization.

- **Strong efficiency story.** SOTA results at 0.37M parameters, competitive with or better than models using 3–5× more parameters, strengthens the argument that recurrent delays are a high-value inductive bias for temporal processing.

---

## Weaknesses

### Fatal
None.

### Major

1. **Restricted architecture scope.** All experiments use small, fully-connected networks (64–256 neurons per layer). There is no evaluation on convolutional, depthwise, or attention-based SNN architectures, nor on larger-scale sequence tasks. It is unclear whether DelRec's advantage persists in architectures with spatially structured connectivity, where the interaction between spatial and temporal delays is non-trivial.

2. **SOTA framing is selective.** Table 1 deliberately excludes multi-compartment neurons (Chen et al., 2024 achieves 97.78% on PS-MNIST vs. this paper's 96.21%), attention-based methods (Wang et al., 2024 achieves 83.69% on SSC), and multi-compartment methods (Zheng et al., 2024 achieves 82.46% on SSC, comparable to DelRec's 82.58%). While the justification for these exclusions is reasonable, the SOTA claim is specific to a sub-class of models. The paper's phrasing of "new state-of-the-art" without qualification in the abstract and conclusion overstates the scope.

3. **No memory/compute overhead analysis.** The scheduling matrix grows with the maximum delay and with σ during training, creating overhead relative to a standard RSNN. The paper does not quantify memory or wall-clock overhead as a function of maximum delay or sequence length, which is critical information for assessing scalability and for the neuromorphic deployment claim.

### Minor

1. **Single seed on PS-MNIST.** The 0.44% improvement over the prior SOTA (96.21% vs. 95.77%) is reported on a single seed, citing precedent. Without variance estimates, the statistical significance of this margin is unclear.

2. **Sensitivity of σ schedule not ablated.** The decreasing-σ curriculum is central to the method, but no ablation shows sensitivity to the initial value of σ or to the schedule shape. It would be informative to know whether performance degrades significantly with different annealing strategies.

3. **Learned delay distributions not shown.** No histogram or visualization of the converged delay values is provided. Understanding the emergent delay distribution (e.g., whether delays cluster near particular values, span a wide range, or co-adapt with weights) would strengthen the mechanistic interpretation.

4. **Neuromorphic deployment claim is unsupported.** The conclusion and abstract repeatedly cite neuromorphic hardware deployment as motivation and potential impact, but no hardware experiments, latency estimates, or hardware-specific design constraints are discussed.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A runtime and memory benchmark comparing DelRec to standard RSNN training across sequence lengths and maximum delay budgets.
- Visualization of learned delay distributions per layer, alongside firing rate maps, to mechanistically explain why recurrent delays outperform feedforward ones.
- At least one experiment with an architecture beyond small FC networks (e.g., a shallow convolutional RSNN on N-MNIST or DVS Gesture).

---

## Novel Insights

The most genuinely novel insight is the empirical demonstration that, under tight parameter budgets, learned recurrent delays outperform learned feedforward delays for temporal processing—a result not previously quantified in the SGL literature. The complementary finding that feedforward delays achieve competitive accuracy at lower firing rates than recurrent delays is also novel and practically actionable: it suggests a design rule that the choice of delay type should depend on the efficiency/performance tradeoff required by a given deployment. The fixed-random-vs-learned recurrent delay comparison (Fig. 3B) further reveals that the topology of recurrent delays matters less than their optimization—the simple introduction of heterogeneous delays already dramatically improves training stability, while learning refines performance marginally but consistently.

---

## Suggestions

- Conduct at least a brief asymptotic analysis of memory overhead as a function of maximum delay $d_{\max}$ and sequence length $T$, since this directly affects scalability.
- Report PS-MNIST over multiple seeds in the camera-ready or response, even if three seeds; the variance on a single-layer 96% network is likely small, and confirming this would validate the SOTA claim.
- In Table 1, consider adding a clearest-possible qualifier (e.g., "among LIF-based RSNNs") to the SOTA claim, to avoid overstating the contribution relative to excluded methods.
- Show the learned delay histograms to connect the quantitative results to mechanistic understanding.

---

## Score and Decision

The paper fills a genuine gap: SGL-based recurrent delay learning in SNNs has not been done before in a principled, scalable way. The method is technically sound, clearly presented, and the empirical results are strong within their scope. The ablation study substantiates the main claims rather than just reporting headline numbers. The primary weaknesses—limited architectural scope, a selective SOTA framing, and absent overhead analysis—are real but do not invalidate the core contribution. This is a solid contribution to the SNN community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>