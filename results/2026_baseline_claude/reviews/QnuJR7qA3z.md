## Summary

HARA (Hybrid Arithmetic-ReLU Networks Approximation) is a hardware-software co-design framework for edge deployment of Transformer models. It replaces heterogeneous non-linear operators (GELU, SiLU, Softmax, LayerNorm, RMSNorm) with a single canonical shallow ReLU network (the Unified ReLU Network, URN), whose parameters are initialized via dynamic programming on an optimal piecewise-linear approximation before a brief fine-tuning. The unified hardware block avoids the need for separate specialized units (exp, sqrt, div LUTs), with synthesis estimates projecting >62% area and >51% power reduction, while end-to-end model accuracy on BERT, Swin, LLaMA, and Stable Diffusion drops by less than 0.1%.

---

## Strengths

- **Demonstrably superior initialization strategy.** The ablation study (Table 4) clearly shows the DP→Analytical Conversion→Fine-Tuning pipeline reduces MSE by 3–5 orders of magnitude versus naive direct training across all eight operators. This is concrete, reproducible, and provides the core justification for the method.
- **Unified architectural principle with a clean hardware story.** Replacing a fragmented collection of function-specific LUT units with one reconfigurable URN block is a coherent and practically important design goal. Table 5 provides concrete synthesis numbers (6 nm cell library, Softmax + LayerNorm + GELU baseline = 20,056 µm², HARA = 7,560 µm²), lending credibility to the claimed savings.
- **Coverage breadth.** The framework is validated on four architecturally diverse models (encoder NLP, vision transformer, causal LLM, diffusion model) covering six distinct non-linear operators, demonstrating genuine generality rather than cherry-picked results.
- **Elegant handling of infinite-domain functions.** The symmetry decomposition in Table 1 — reducing GELU/SiLU to ReLU(x) plus a compact negative-domain approximation — is a nice insight that ensures the approximation is valid outside the training interval, a failure mode clearly illustrated in Figure 3.

---

## Weaknesses

### Fatal
None.

### Major

1. **No latency or throughput analysis.** For a paper whose stated goal is edge deployment, the absence of any latency estimate is a critical gap. Area and power are necessary but not sufficient; a large reduction in silicon area for the non-linear unit is not useful if the URN becomes a throughput bottleneck (e.g., because it serializes what were previously parallel specialized units, or because the CLUT configuration overhead dominates). This information is achievable with the same synthesis tools already used and its omission leaves the central claim under-supported.

2. **Hardware efficiency claims rest entirely on synthesis estimates, not physical implementation.** The paper acknowledges this in Section 5, but the acknowledgment does not reduce the evidentiary weight required for a hardware-centric contribution. Synthesis-level estimates can differ from post-layout results by 20–40%, and they say nothing about timing closure, memory bandwidth to feed the CLUTs, or reconfiguration latency between operators within a single forward pass.

3. **Comparison baseline selection is narrow.** Table 3 benchmarks HARA against NN-LUT and RI-LUT only. Polynomial approximations (degree-2 or degree-3, widely used in commercial NPUs), Taylor-series methods, and software-only piecewise-linear schemes with heuristic breakpoints are natural baselines that are omitted. As presented, it is unclear whether HARA's improvement is primarily due to the DP breakpoint search or simply due to allowing more segments (HD scaling) than the baselines.

### Minor

1. The paper fixes a single configuration "HARA (8,8,8)" for Table 6 but does not show a Pareto curve or table illustrating the accuracy–area trade-off as HD varies. Practitioners need this to choose the appropriate operating point.
2. The fine-tuning stage (Stage 3) is described as "brief" without specifying the number of iterations or data used, making the pipeline difficult to replicate exactly.
3. The derivation in Algorithm 1 (line 13) constrains second-layer weights to ±1, which restricts representational flexibility. No ablation or justification is provided for whether this constraint meaningfully harms approximation quality versus easing hardware implementation.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A Pareto plot of approximation MSE vs. hardware area (varying HD) would directly illuminate the efficiency–accuracy trade-off central to the paper's contribution.
- A discussion of the CLUT reconfiguration cost (how many cycles to switch the URN from Softmax mode to LayerNorm mode) is important for understanding pipeline efficiency in multi-operator models.
- Reporting inference wall-clock time on an FPGA prototype (even a preliminary one) would substantially strengthen the hardware claims without requiring a full ASIC tapeout.

---

## Novel Insights

The most technically novel element of the paper is the combination of three observations: (a) activation functions like GELU and SiLU decompose into a linear component (ReLU(x)) and a compact, even, decaying non-linear residual, enabling an infinite-domain approximation from a finite-domain network; (b) DP-based breakpoint optimization of piecewise linear approximations yields provably near-optimal starting points, and these can be converted analytically to a single-hidden-layer ReLU network with the constraint k[0]=0; and (c) the same PWL-to-ReLU structure handles Softmax and LayerNorm once they are re-expressed in base-2 arithmetic, enabling a genuinely shared hardware block. While each ingredient individually is known, their combination as a systematic co-design pipeline for Transformer non-linearities is new and cleanly executed.

---

## Suggestions

1. Run inference timing experiments on a commodity embedded platform (Cortex-M, Jetson, or an FPGA with the URN implemented) to report at least a proxy latency figure.
2. Add a two-column ablation in Table 3 showing a third baseline: uniform-breakpoint PWL (same HD, no DP) to isolate the contribution of the DP search from the sheer number of segments.
3. Report HD sensitivity for each architecture in Table 6 — e.g., HARA (4,4,4) and HARA (16,16,16) — to give practitioners a design trade-off chart.
4. Provide the synthesis script and cell-library configuration as supplementary material so reviewers and practitioners can independently verify the area/power numbers.

---

## Score and Decision

The paper addresses a real problem with a principled method and validates it across diverse architectures. The DP initialization pipeline is clearly and convincingly demonstrated to outperform direct training. However, the primary hardware contribution—area and power savings—is based solely on synthesis estimates without latency or throughput figures, which are the critical metrics for edge deployment. The algorithmic components (DP-based PWL approximation, PWL-to-ReLU conversion) are individually well-known, and the novelty lies in their systematic unification for Transformer non-linearities. This is a valuable engineering contribution but is below ICLR's typical bar for algorithmic depth, and the hardware validation gaps leave the strongest claims unconfirmed.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>