- Decision: Accept
- Avg Score: 5.40
- Scores: 6, 6, 8, 1, 6
Now I have the paper content and can verify every claim against the source. Let me construct the consolidated review.

## Summary

BrainPy is a differentiable brain simulator built on JAX that introduces custom sparse/event-driven operators, JIT connectivity operators with near-zero memory footprint, and an AlignPre/AlignPost abstraction that decouples synaptic dynamics from communication — enabling biophysically realistic brain simulation while preserving full differentiability for gradient-based training. The paper demonstrates efficiency (2–5 orders of magnitude speedup vs. dense operators), scalability (4M+ neurons on a single GPU), and a biologically plausible GIF network trained on a working memory task.

## Strengths

1. **Event-driven and sparse operators achieve massive measured speedups.** Section 4.1 (lines 141–142) reports that `brainpy.math.event.csrmv` is 2–5 orders of magnitude faster than dense JAX/PyTorch operators, with speed increasing as firing frequency decreases — directly validating the core efficiency claim. The comparison is performed on both CPU and GPU with controlled baselines (JAX dense/sparse and PyTorch dense).

2. **JIT connectivity operators enable a concrete scaling demonstration to 4M+ neurons on a single GPU.** Section 4.2 (lines 148–159) shows near-constant memory for the JIT operator as matrix size grows, and scales a COBA-LIF network linearly to over 4 million neurons with 80 incoming synapses per neuron — a concrete scalability result on a single GPU.

3. **The AlignPre/AlignPost abstraction is a clean design innovation.** Section 3.3 (lines 84–104) decomposes synaptic projections into dynamics vs. communication, enabling automatic merging of duplicate synaptic traces and allowing standard DL components (linear, conv, normalization) to serve as communication mechanisms. This is a novel framing that directly addresses the bridge between brain simulation and BIC.

4. **Differentiable training of a biophysically fitted GIF network on a cognitive task.** Section 4.3 (lines 162–173) demonstrates that a network fitted to PFC neuron data can be trained via gradients to nearly 100% accuracy on a delayed match-to-sample task, with post-training dynamics resembling monkey PFC recordings — concrete evidence of the differentiable simulation capability for realistic models.

5. **Modular multi-scale model-building interface.** Section 3.4 (lines 106–117) describes a recursive `DynamicalSystem` class that composes from ion channels to systems, with user-controlled depth, providing flexibility that descriptive-language simulators lack.

## Weaknesses

### Fatal
None.

### Major

1. **Unspecified hardware and backend settings for the full-simulator speed benchmarks (Fig. 1C–D) undermine the efficiency comparison.**  
   Lines 143–144 report "BrainPy shows the best performance" against NEURON, NEST, Brian2, ANNArchy, and BindsNet on COBA-LIF and COBA-HH networks, but the paper nowhere specifies what hardware (CPU model, GPU model, or both) was used for each simulator, nor which backend each baseline employed (e.g., Brian2 with C++ code generation, NEST with OpenMP). Since BrainPy runs on GPU via JAX/XLA whereas several baselines are typically CPU-based, the speed advantage could partially reflect hardware disparity rather than architectural superiority. This does not invalidate the paper's core contribution, but it makes the headline efficiency claim over baselines uninterpretable as presented.

2. **Claimed memory savings from automatic synapse merging are asserted but not quantified.**  
   Section 3.2 (lines 99–101) describes how AlignPre/AlignPost projections can merge duplicate synaptic traces across projections with identical time constants, and mentions a 30-brain-area network as a showcase. However, no quantitative memory-usage data are reported — no comparison with/without merging, no scaling curve, no footprint numbers. Since this is presented as a design benefit, its absence weakens the methodological validation.

### Minor

3. **Overclaim on MNIST reservoir accuracy.**  
   Line 161 states that 98.9% on MNIST is "on par with the state-of-art machine learning algorithms." For MNIST, standard CNN baselines exceed 99.5%, making this phrasing imprecise. The reservoir result is still strong; the claim should be scoped to "competitive with standard machine learning algorithms" or a specific baseline should be cited.

4. **No statistical reporting (error bars, multiple runs) for speed/memory measurements.**  
   Speed and memory plots (Figs. 1, 4) are shown as single curves without variance. While this is common in simulator benchmark papers, given the known volatility of GPU kernel timing, reporting means and error bands over multiple runs would strengthen confidence in the reported order-of-magnitude claims.

5. **No discussion of JIT compilation overhead.**  
   The paper (Section 3.5, lines 120–122) describes object-oriented JIT compilation as a key advantage, but does not benchmark compilation time vs. simulation speedup. For large models, JIT compilation can take minutes; acknowledging this trade-off would make the presentation more complete.

6. **Missing code repository URL and version identifier.**  
   For a software contribution paper, providing the repository URL and the specific version evaluated is standard practice for reproducibility. The paper names the package (BrainPy) but does not include this information.

### Trivial

None.

## Nice-to-Haves

- A controlled ablation where BrainPy and all baselines run on the same CPU hardware would cleanly separate the efficiency claim from hardware effects.
- A bar chart showing memory footprint with and without AlignPre/AlignPost merging for the 30-area network would validate the memory-savings claim.
- The novelty of the event-driven operators could be sharpened in Section 3.1: the speedup over dense is a known consequence of event-driven computation; the paper's advance is implementing these operations *within JAX while preserving full differentiability*. Making this explicit would prevent readers from misinterpreting the contribution.

## Removed Points

- **Missing related works (NeuroSim, Lava, HAO et al.):** Removed per the rule that missing related-work citations cannot be reliably verified by the reviewer and should not be raised as weaknesses.
- **"Event-driven speedup is a fundamental consequence, not a novel insight":** Removed because this mischaracterizes the contribution — the novelty is implementing event-driven ops within a differentiable JAX framework, which the paper already states. The speedups are the evaluation, not the claimed novelty itself.
- **JIT operator notation imprecision:** Removed because the paper describes the operator in words and the semantics are clear; this is a presentational preference, not a weakness.
- **AlignPre/AlignPost exactness lacking formal justification:** Removed because the paper explicitly scopes these to homogeneous parameters (line 90) and states they are exact within that scope. The reviewer's concern about edge cases (non-homogeneous delays) asks the paper to cover cases it already excludes by design.
- **Sparse operator not shown in plot:** Removed because the paper states sparse was compared; without access to the figure it is impossible to verify whether it is plotted or omitted.
- **Training GIF narrative implying biological plausibility:** Removed because the reviewer acknowledges this is not a flaw; the paper's framing is appropriate for a demonstration of differentiable simulation capability.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's ambitious cross-disciplinary claims and the practical difficulty of running fair multi-simulator benchmarks, but neither reviewer identifies a structural weakness or unaddressed prior art that the paper itself does not already discuss. The key insight — that decoupling synaptic dynamics from communication (AlignPre/AlignPost) is a natural point for inserting DL components into biophysical simulations — remains the paper's most interesting intellectual contribution and is well supported by the design description.

## Suggestions

1. **Specify hardware and backend configurations** for every simulator in Fig. 1C–D (CPU model, GPU model, backend flags such as Brian2 C++ codegen, NEST OpenMP threading). If BrainPy ran on GPU while baselines ran on CPU, either add a CPU-only control or explicitly acknowledge and discuss the asymmetry.
2. **Add a quantitative memory-usage comparison** for the 30-brain-area network with and without AlignPre/AlignPost merging, ideally as a bar chart in the main text or supplement.
3. **Tone down the MNIST claim** from "on par with state-of-the-art" to a more specific characterization (e.g., "competitive with commonly used baselines").
4. **Add the code repository URL** in the camera-ready version, along with the evaluated version tag.
5. **Include error bands or standard deviations** for the speed benchmark plots, or at minimum note the number of runs and variance.
