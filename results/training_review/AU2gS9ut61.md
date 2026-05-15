Here is my consolidated final review.

---

## Summary

BrainPy is a differentiable brain simulator built on JAX/XLA that unifies brain simulation and brain-inspired computing (BIC) within a single framework. The paper contributes (1) custom sparse/event-driven operators with automatic differentiation support, (2) JIT connectivity operators enabling near-constant memory scaling to millions of neurons on a single GPU, (3) a synapse abstraction (AlignPre/AlignPost) that decouples dynamics from communication, and (4) an object-oriented JIT compilation strategy for optimizing element-wise brain dynamics. Demonstrations include speed benchmarks against NEURON, NEST, Brian2, and ANNarchy, scaling to 4M-neuron networks, reservoir computing on KTH/MNIST, and differentiable training of a biologically grounded GIF network on a working-memory task with post-training dynamics compared to primate PFC recordings.

## Strengths

- **Custom sparse/event-driven operators with full automatic differentiation (Sec. 4.1).** The `brainpy.math.event.csrmv` operator achieves substantial speedups (2–5 orders of magnitude) over dense and sparse alternatives in JAX and PyTorch on both CPU and GPU (Fig. 3A,B). Because these operators support forward- and reverse-mode gradients, they directly address the core gap: traditional brain simulators lack differentiability, while DL frameworks lack dedicated sparse/event-driven primitives for brain dynamics.

- **JIT connectivity operators for large-scale simulation with constant memory (Sec. 4.2).** The `brainpy.math.jitconn` operators store only four scalars per connection (p, μ, σ, seed) instead of a full matrix. This yields near-constant memory as network size grows (Fig. 4A), 1–2 orders of magnitude speedup over dense/sparse operators (Fig. 4B), and scaling to 4 million neurons on a single GPU (Fig. 4C). This is a concrete improvement over prior simulators that typically require distributed clusters for comparable scales.

- **Differentiable training of a biologically plausible spiking network on a cognitive task (Sec. 5.3).** A GIF network with AMPA/GABA synapses is trained via gradients (impossible in traditional simulators) on the delayed match-to-sample task, reaching near-100% accuracy within a few epochs (Fig. 5F). The post-training spiking patterns are compared to primate PFC recordings (citing Constantinidis 2016). This directly demonstrates the paper's central claim: enabling gradient-based learning for biophysical brain models that were previously non-differentiable.

- **Synapse abstraction (AlignPre/AlignPost) decoupling dynamics from communication (Sec. 4.3).** This decomposition cleanly separates element-wise memory-intensive dynamics from the communication matrix, allowing sparse matrices, DL layers, or convolutions as interchangeable communication mechanisms (Fig. 2). The automatic merging of duplicate synaptic traces across multiple projections is a principled innovation for reducing memory in large networks.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that BrainPy provides a differentiable brain simulation framework with dedicated optimizations for sparse, event-driven, scalable computation — are substantiated by the evidence presented. The weaknesses below are addressable in revision.

### Minor

1. **The "bridge" framing is somewhat broader than the demonstrated scope.** The paper repeatedly claims BrainPy "bridges" brain simulation and BIC, but the biological simulation demonstrations are limited to point-neuron models (LIF, HH single-compartment, GIF). Multi-compartment neurons with complex morphology and distributed ion channels — a key capability that distinguishes simulators like NEURON — are neither demonstrated nor benchmarked. While the modular interface (Sec. 4.4) is presented as supporting such models, the paper would significantly strengthen its central claim by including even one example of a multi-compartment or morphologically detailed model. Without this, the claimed "bridge" reads as aspirational rather than fully realized.

2. **Missing experimental details for speed benchmarks.** The simulator comparison (Fig. 3C,D) does not disclose hardware specifications (CPU model, GPU model, memory) for any tool tested. The operator benchmarks (Fig. 3A,B) do not report matrix sizes, sparsity ratios, or numerical precision used. These omissions make it difficult for readers to assess the fairness of comparisons or reproduce the results. At a minimum, hardware details and matrix dimensions should be reported.

3. **Overclaimed MNIST result.** The paper states 98.9% accuracy on MNIST with a 50,000-node reservoir is "on par with the state-of-art machine learning algorithms" (Sec. 5.2). This is misleading: modern deep learning methods exceed 99.5% on MNIST, and the comparison to a single prior study (Antonik 2019) does not constitute a rigorous evaluation. The result is a useful scalability demonstration, but the "state-of-art" language should be moderated.

4. **Thin quantitative evidence for biological plausibility claim.** The claim that post-training dynamics "exhibit comparable patterns to the neural activity of PFC neurons recorded from monkeys" (Sec. 5.3) is supported only by a single visual example (Fig. 5G) with no quantitative similarity metric (e.g., firing rate distribution comparison, tuning curve correlation, or decoding analysis). This weakens what is otherwise the paper's most compelling demonstration of differentiable biophysical simulation.

5. **The 30-area network is mentioned but not quantitatively evaluated.** Section 4.3 describes automatic synaptic merging and mentions constructing a 30-area network, but no memory savings, speed, or accuracy results are reported for this network. It serves as a motivating example rather than a validated demonstration.

### Trivial
- The description of object-oriented JIT compilation (Sec. 4.5) as enabling "whole-graph optimization of class-based models" could benefit from a concrete code example showing what distinguishes it from standard JAX `jit` on functions.
- The reservoir scaling results on KTH (94.4% with 30,000 nodes vs. 91.3% with 16,384 nodes from Antonik 2019) are presented as "superior accuracy," but the comparison confounds model size with methodology — it is unclear how much improvement comes from scaling versus the JIT connectivity operators themselves.

## Nice-to-Haves

- Ablation: how much of the speedup comes from event-driven computation vs. sparse representation vs. JIT kernel fusion? Disentangling these would strengthen the claims about operator design.
- Error bars or confidence intervals on speed benchmarks would improve rigor, especially given GPU execution variability.
- A comparison of differentiable training against existing SNN libraries (snnTorch, Norse, SpikingJelly) on a common task would further validate the claim that BrainPy's biophysical neuron models offer advantages over simpler LIF models.
- Explicit discussion of how online plasticity (e.g., STDP) is handled within the JIT framework would clarify a practical limitation of the JIT connectivity approach (which assumes static weights).

## Removed Points

- **"No mention of existing JAX-based brain simulation projects"** — Removed per the rule that missing related works cannot be confirmed without external sources.
- **"Unfair hardware comparison (GPU vs. CPU) invalidates results"** — The paper shows operator benchmarks on both CPU and GPU (Fig. 3A,B), and BindsNet (included as a baseline) is GPU-based. The absence of hardware disclosure is a reporting gap (captured above), but the reviewer's assumption that all baselines are CPU-only and the comparison is therefore "unfair" is not fully supported by the paper's content and overstates the severity of the omission.
- **"The speedup of 100,000× appears implausible"** — The 2–5 orders-of-magnitude range is described for event-driven operators at low firing rates (10 Hz). Event-driven computation inherently avoids O(N) work when few spikes occur, making large speedups at low firing rates physically plausible. The criticism about missing experimental detail (matrix sizes, sparsity) is retained; the implausibility claim is not.
- **"JIT compilation description as object-oriented is vague"** — Moved to Trivial. The paper does provide explanation (Sec. 4.5) that brain dynamics are memory-intensive, element-wise operations benefit from XLA kernel fusion, and the approach transforms class-based `DynamicalSystem` models into XLA binaries. The description is adequate for a systems paper, though a concrete code diff would strengthen it.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle the authors themselves have not identified. The core novelty — a differentiable brain simulator on JAX with dedicated sparse/event-driven operators and JIT connectivity — is well articulated in the paper.

## Suggestions

1. **Add a multi-compartment neuron example**, even a simple one (e.g., a CA1 pyramidal cell with 2–3 compartments and active conductances), and compare simulation accuracy and speed against NEURON. This single addition would substantially bolster the "bridge" claim.
2. **Disclose all hardware details** (CPU model, GPU model, memory, CUDA version) for every benchmark, and report matrix sizes, sparsity ratios, and precision used in operator comparisons.
3. **Replace or qualify the "state-of-art" language** for the MNIST reservoir result, and consider comparing against additional baselines.
4. **Add a quantitative metric** for the biological plausibility comparison in Sec. 5.3, such as firing rate distributions, selectivity indices, or population decoding accuracy.
5. **Provide quantitative memory/speed results** for the 30-area network with automatic synapse merging to validate the claimed advantage.

## Score and Decision

This paper presents a genuine engineering contribution — a differentiable brain simulator on JAX that fills a real gap between brain simulation and BIC. The technical design (event-driven operators, JIT connectivity, synapse abstraction) is principled and the demonstrations (speed benchmarks, 4M-neuron scaling, differentiable training on a cognitive task) are largely convincing. The weaknesses are in experimental reporting and claim moderation, not in the core methodology. The paper would be strengthened by the suggested additions but is solid in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>