Now I have a thorough understanding of the paper and all the calibration anchors. Let me write the final consolidated review.

## Summary of calibration

**Round 1 bracket**: I identified the narrowest plausible range as [3.5, 5.5] — clearly above the 2.5–3.0 papers (which had fatal methodological or novelty flaws) but below the 5.0–6.0+ papers (which had stronger methodological contributions and proper framing).

**Round 2 narrowing**: I examined anchors at 4.0 (sSWiZr8QU7 — gray-box simulation, comparable application-focus with similar novelty concerns), 4.5 (hz3NtNpDNv — Hottel Zone furnaces, similar applied-ML contribution level), 5.0 (5rfj85bHCy — HyResPINNs), and 5.2 (fH9eqpCcR3 — MPP physics pretraining). The paper under review is comparable to the 4.0–4.5 anchors in terms of application contribution but is pulled down by the architectural misrepresentation issue, which is a more significant framing flaw than anything in those anchors.

**Final score**: 3.5 — the paper has a clear motivation and reasonable experimental setup, but the core contribution is undermined by overclaimed architecture naming and framing.

---

## Summary

This paper compares three neural network architectures—a plain MLP, a "U-Net-like residual network," and a "DeepONet-style model"—for predicting the time evolution of temperature and 11 chemical species during hydrogen-oxygen-air thermal explosion. The authors report that their U-Net-style model achieves substantially lower MSE (0.00137) with non-overlapping 95% confidence intervals compared to the MLP (0.0202) and DeepONet (0.0181). The dataset covers wide parameter ranges (T ∈ [250,5000] K, p ∈ [10⁴,2×10⁷] Pa, Δt ∈ [10⁻¹⁰,10⁻⁵] s) and a multi-step recursive training loss is used.

## Strengths

- **Statistically significant performance gap**: Table 1 shows non-overlapping 95% confidence intervals for the U-Net ([7.692e-4, 1.980e-3]) versus both MLP ([1.840e-2, 2.218e-2]) and DeepONet ([1.647e-2, 1.969e-2]), providing rigorous evidence that the improvement is not due to random variation.

- **Broad and realistic training dataset**: The parameter ranges (covering 4+ orders of magnitude in pressure and 8+ orders in Δt) go well beyond prior work, which often used fixed chemistry timesteps or narrow conditions. This makes the experimental comparison more meaningful for realistic combustion applications.

- **Multi-step recursive loss**: Training with a 30-step accumulated-error loss (Equation 4) is a sound and demanding evaluation protocol that better reflects the practical use case of autoregressive rollout than single-step prediction would.

- **Qualitative phase alignment evidence**: Figure 4 demonstrates that even on difficult trajectories, the U-Net model maintains synchrony with reference temperature and species peaks, while the other models exhibit phase lag and drift. This goes beyond raw MSE to show that architectural differences affect temporal dynamics.

## Weaknesses

### Major

- **Misleading architectural naming overstates the contribution**. The so-called "U-Net-like residual network" (Section 4.2) is a fully-connected network with exactly two residual connections (one local skip from the expansion layer to the block output, one global skip from input to output) — no downsampling, no upsampling, no convolutions, no encoder-decoder hierarchy. Calling it "U-Net-style" and claiming it provides "encoder-decoder design with skip connections" that captures "multi-scale representation" (Section 5, line 268) is inaccurate. The architecture is an MLP with residual connections, which could fairly be called "ResMLP." Similarly, the "DeepONet-style model" (Section 4.3) processes dt as a scalar input in the trunk branch rather than encoding the query coordinate t for continuous evaluation, and outputs the full state vector rather than a scalar per coordinate — diverging substantially from the standard DeepONet framework (Lu et al., 2021). The paper frames the comparison as one between fundamentally different architectural families (U-Net, DeepONet, MLP), when in reality it compares MLP variants. This undermines the paper's core claim about "the importance of selecting appropriate network architectures."

- **The core empirical finding is unsurprising given what is actually being compared**. The U-Net and MLP differ only by two residual connections — a well-known technique dating to ResNet (2016). The 10×–15× MSE improvement from adding skip connections confirms established knowledge rather than providing novel architectural insight. The paper would need a controlled ablation (varying skip connection configurations, depth, width) to support claims about "hierarchical feature extraction" and multi-scale representation learning, but no such ablation is performed.

- **The paper overclaims architectural conclusions that the experimental design cannot support**. The conclusion states that "the choice of architecture can be as critical as the size or the diversity of the dataset" and that "U-Net-based architectures" show "promise" for chemical kinetics. However, since the U-Net is actually an MLP with residual connections, these claims conflate a minor modification (skip connections) with wholesale architectural innovation. The paper does not demonstrate that U-Nets (in the standard Ronneberger et al. sense with encoder-decoder and spatial down/up sampling) are beneficial for this problem, nor does it compare actual operator-learning methods.

### Minor

- **Missing implementation detail: training procedure for the 30-step rollout.** Equation (4) describes a multi-step recursive loss, but the paper does not specify whether each recursive step uses the model's own previous output (autoregressive mode) or ground-truth values (teacher forcing). This is critical for reproducibility and for interpreting the results, as teacher forcing would mask error accumulation.

- **Confidence interval computation not specified.** Table 1 reports 95% CIs, but the paper does not describe how they were computed (bootstrap? parametric assumption?). Given the highly non-Gaussian error distribution (standard deviation exceeds the mean by 16× for the U-Net), the CI computation method matters for interpretation.

- **High variance in errors is acknowledged but not analyzed.** The U-Net's standard deviation (0.0218) is 16× its mean (0.00137), indicating that a small number of trajectories dominate the error. The paper does not analyze these failure cases, report quantile statistics, or check whether predictions satisfy basic physical constraints (non-negativity, species conservation).

- **Training details**: batch size of 5,000 (10% of the 50k training set) is unusually large and may affect convergence comparisons across models. The paper does not discuss learning rate schedules, weight initialization, or whether the same random seed was used across all models.

### Trivial

- None.

## Nice-to-Haves

- An honest rename of the architectures ("MLP with residual connections" instead of "U-Net-like"; "multi-branch network" instead of "DeepONet-style") would align the paper's framing with what was actually done and strengthen the contribution.
- A systematic ablation study adding/removing the skip connections individually, and varying depth/width, would substantiate the claims about architectural effects.
- Reporting median error, per-trajectory error histograms, and the fraction of physically implausible predictions would better characterize model behavior than aggregate MSE alone.

## Removed Points

- Concerns about dataset size (50k samples insufficient) — the wide parameter coverage and multi-dimensional input make this a reasonable dataset size for the problem, and the criticism is speculative without evidence of data-limited behavior.
- Criticisms about "no discussion of data distribution, class imbalance" — the paper explicitly describes the wide parameter sampling and notes the dataset includes trajectories with long induction times and abrupt ignition events.
- The demand for comparison with ISAT/PRISM tabulation methods — this is outside the paper's stated scope (architecture comparison), though it would be a useful addition.
- Criticism that the DeepONet "cannot predict at arbitrary times" — the paper's own setup predicts fixed Δt steps for all models, so this applies to all architectures equally.
- Various formatting and phrasing nitpicks from the harsh critic.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the problem or methods that the paper itself misses.

## Suggestions

1. **Rename the architectures honestly.** Call the "U-Net" an "MLP with residual connections" (or "ResMLP") and the "DeepONet" a "multi-branch network" or "split-input MLP." This would prevent the paper from claiming conclusions it cannot support about U-Net or DeepONet architectures for combustion kinetics.

2. **Add a controlled ablation study.** Compare the plain MLP, MLP+global skip only, MLP+local skip only, and MLP+both skips. This would isolate the contribution of each architectural element and provide the evidence currently missing for claims about "hierarchical" or "multi-scale" representations.

3. **Specify the rollout training procedure.** Clarify whether the 30-step recursive loss uses teacher forcing or autoregressive prediction. This is essential for reproducibility.

4. **Report per-trajectory error distributions** (histograms, quantiles, maximum per-species errors) and analyze the worst-case trajectories to understand when and why the models fail.

5. **Check and report physical constraints** — whether predictions ever produce negative concentrations, violate conservation, or exceed temperature bounds.

## Score and Decision

**Calibration anchors consulted across all rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| otXB6odSG8 (Atmospheric Radiation Neural ODE) | 3.0 | R1 | Weaker — limited novelty, poor baselines; our paper has better data and clearer statistical evidence |
| yGdoTL9g18 (Res-F-FNO turbulence) | 3.0 | R1 | Comparable weakness in novelty; our paper has better experimental framing |
| HDmmwwTIlf (Characteristic-based NN for PDEs) | 2.5 | R1 | Clearly weaker — narrow scope, no comparison |
| SYiOxXWlKU (EPINN stiff ODEs) | 2.5 | R1 | Comparable domain but weaker execution |
| sSWiZr8QU7 (Hybrid Gray Box Simulation) | 4.0 | R2 | Comparable applied-ML contribution level, but our paper's architectural misrepresentation is a more significant flaw |
| hz3NtNpDNv (Hottel Zone Furnace Networks) | 4.5 | R1/R2 | Comparable application focus and contribution level; our paper is slightly weaker due to the overclaiming issue |
| 5rfj85bHCy (HyResPINNs) | 5.0 | R1/R2 | Stronger methodological novelty than our paper |
| fH9eqpCcR3 (Multiple Physics Pretraining) | 5.2 | R2 | Stronger methodology and evaluation |
| A23C57icJt (Open-CK Combustion Benchmark) | 6.25 | R1/R2 | Clearly stronger — comprehensive benchmark dataset, thorough evaluation |
| nhrXqy5d5q (KinFormer) | 6.0 | R2 | Clearly stronger — novel method (MCTS + conditional transformer), rigorous evaluation |

**Round 1 bracket**: [3.5, 5.5]  
**Round 2 narrowing**: The paper is comparable to the 4.0–4.5 anchors in application-level contribution but the architectural misrepresentation is a more serious framing flaw than any weakness in those anchors. The paper is clearly above the 2.5–3.0 papers but does not reach the 5.0+ level of methodological contribution.  
**Final score**: 3.5

<score>3.5</score>
<decision>Reject</decision>