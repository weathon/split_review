I now have a clear picture of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

This paper proposes LRF-Dyn, a spiking self-attention (SSA) variant that augments SSA with local receptive fields (LRF) and replaces explicit attention-matrix computation with a recurrent approximation inspired by neuronal charge–fire–reset dynamics. The authors also present LRF-SSA (SSA + LRF without the dynamic approximation) as an intermediate variant. Experiments on ImageNet classification and ADE20K segmentation using three SSN Transformer backbones (Spikformer, QKFormer, SDT-V3) show modest accuracy improvements (0.4–1.2%) alongside claimed memory reductions up to 49.4%.

## Strengths

1. **Diagnosis of SSA's limited local modeling is well-supported.** Figure 2 quantifies the mismatch: only 20.31% of SSA attention scores fall within Manhattan distance 0–5, versus 76.68% for VSA, and SSA's attention entropy (0.5637) is higher than VSA's (0.1777). This analysis is the paper's strongest contribution and clearly motivates the LRF module.

2. **Consistent improvements across architectures and tasks.** On ImageNet, both LRF-SSA and LRF-Dyn improve accuracy on Spikformer (+1.24% and +1.13%), QKFormer, and SDT-V3 (Table 1). On ADE20K segmentation, SDT-V3 + LRF-SSA gains +2.6 mIoU (Table 2). The breadth of these gains suggests the LRF module has genuine practical value.

3. **Memory reduction is demonstrated numerically.** LRF-Dyn reduces storage complexity from O(d²) to O(kd) (k=8 dendrites), and under Spikformer-8-512 the paper reports a 49.4% inference memory reduction with a +1.13% accuracy gain (Section 6.2, Fig. 5b). These numbers support the claim that the method reduces memory overhead.

4. **Ablation confirms the LRF kernel contribution.** Table 3 shows that increasing the number of LRF kernels (Ω) monotonically improves accuracy for both LRF-SSA and LRF-Dyn on CIFAR-100, providing evidence that the LRF module itself drives the performance gain.

5. **Minimal parameter overhead.** The LRF module adds fewer than 0.2M parameters (Table 1) and requires no architectural modifications to existing Spiking Transformers, making the approach easy to adopt.

## Weaknesses

### Major

1. **Causal/autoregressive nature of LRF-Dyn is not acknowledged or discussed, fundamentally changing the attention mechanism.** Eq. 11 contains a sum over *j = 1 … n−1*, which is a strictly causal (unidirectional) formulation. This means LRF-Dyn does *not* compute bidirectional self-attention as used in standard Vision Transformers or in any of the SSA baselines (Spikformer, QKFormer, SDT-V3). The paper mentions "causal inference" in a single sentence (Section 5.2) but never explicitly states that LRF-Dyn is autoregressive, discusses the implications for representational power, or justifies why a causal formulation is appropriate for image-level tasks. The memory reduction—one of the paper's two main claims—hinges on this causal trick, which is well-known in the linear-attention literature (Katharopoulos et al., 2020, cited by the paper) and is not specific to SNNs or "neuronal dynamics." The ablation in Table 3 compares LRF-Dyn to "Causd SSA" (a causal SSA) rather than to a *bidirectional* LRF-SSA, making it impossible to separate the effect of the dynamic approximation from the effect of simply restricting attention to previous tokens. This is a structural flaw that undermines the paper's main narrative.

2. **Experimental evaluation lacks basic rigor and transparency.** No training hyperparameters are reported—epochs, learning rate schedule, batch size, optimizer, data augmentation, and hardware are entirely absent. All reported accuracy gains are modest (0.4–1.2%) and reported without any measure of variance or statistical significance (single runs). The "49.4% memory reduction" claim (Section 6.2) is stated for a single configuration without specifying how memory is measured (activation peak? total parameters? at which timestep?). Without these details, the experiments cannot be reproduced or fairly compared, and it is unclear whether the reported improvements are meaningful given typical run-to-run variation in this domain (often 0.5–1.0%).

3. **Theoretical framing is decorative and does not cover the main contribution (LRF-Dyn).** Theorems 1 and 2 bound the expected receptive field and compare the entropy of VSA, SSA, and LRF-SSA attention distributions. However, LRF-Dyn—the paper's primary contribution—is not covered by either theorem. The entropy argument in Theorem 2 is asserted rather than connected to practical performance. The proofs are relegated to the appendix. The paper would be unaffected if these theorems were removed; they serve only to give an appearance of rigor without supporting the core claims about LRF-Dyn.

4. **Insufficient ablation to isolate the two contributions.** The paper proposes two distinct changes: (i) adding LRF to SSA, and (ii) replacing attention with a recurrent dynamic. The ablation (Table 3) compares LRF-Dyn to "Causd SSA," which is a weak baseline because causal SSA is expected to perform poorly on non-sequential tasks. The proper comparison would be: SSA (bidirectional) → SSA+LRF (bidirectional) → causal SSA+LRF → LRF-Dyn. This would reveal what each component actually contributes. Without it, the paper cannot claim that the dynamic approximation preserves performance independently of the causal constraint.

### Minor

1. **Undefined notation and unclear derivation.** The variable *v*_{\rho_k}[t] appears in Eq. 11 and *X*_{\rho_k}[t] in Eq. 12 without definition. The subscripts \rho_k are never explained. The transition from Eq. 11–13 to Eq. 15 (Fourier transforms and convolution kernel *K*(*t*)) describes what appears to be a different computational path than the one in Eqs. 11–13, and the text does not reconcile the two. The biological analogy (multi-dendrite neurons) motivates the method but does not explain why the specific numerical formulation should work.

2. **Memory measurement methodology is unspecified.** The paper claims a 49.4% memory reduction but never states what is being measured (inference-time peak activation memory? total parameter storage? at which sequence length or batch size?). A bubble chart (Fig. 5b) is presented without axis definitions or a clear description of how the memory metric is computed. This makes the central quantitative claim difficult to evaluate.

3. **"Energy-efficient" claims are unsupported.** The title and abstract promise energy efficiency, but no energy, latency, or throughput measurements are provided. Memory reduction does not guarantee lower energy—the sequential/causal processing in LRF-Dyn may increase wall-clock latency and energy on batch-oriented hardware. Without these measurements, the energy-efficiency claims are speculative.

4. **Comparison to other memory-efficient attention mechanisms in the SNN literature is absent.** Since the memory reduction technique is essentially causal linear attention (Katharopoulos et al., 2020), the paper should compare or at least discuss other linear-attention or chunked-attention approaches within the SNN context. The related work section covers SNN-Transformer hybrids but does not engage with the efficient-attention literature that the method directly builds on.

5. **The segmentation results may have an unfair baseline.** The authors note (Table 2 footnote) that the SDT-V3 baseline results were reproduced by themselves rather than taken from the original paper, introducing a risk of unintentional baseline degradation. The large +2.6 mIoU gain warrants verification against the originally reported SDT-V3 numbers.

### Trivial

1. Typo: "Causd SSA" in Table 3 (should be "Causal SSA").
2. The notation `v_{\rho_k}` and `X_{\rho_k}` in Eqs. 11–12 is never defined.

## Nice-to-Haves

- Provide training hyperparameters (epochs, batch size, learning rate schedule, optimizer, data augmentation, hardware) for all experiments.
- Report results over at least 3 random seeds with standard deviations for main results.
- Compare LRF-Dyn against a bidirectional version of LRF-SSA (not just "Causd SSA") to isolate the effect of the dynamic approximation.
- Provide energy or latency measurements to support the "energy-efficient" framing.
- Clarify how memory is measured (peak activation memory, total parameters, etc.) and at which configurations.

## Removed Points

These points were raised in the inputs but are removed or demoted for the stated reasons:

- **"The paper omits FlashAttention, Linformer, Performer from related work."** — Removed. The paper's focus is SNN-specific attention, and it does cite Katharopoulos et al. (2020), which is the most directly relevant linear-attention prior art. The absence of ANN-only efficient-attention methods is not a weakness for an SNN paper.
- **"The inclusion of ANN baselines (ResNet, PVT) in Table 2 is irrelevant."** — Demoted to minor. ANN baselines are commonly included in SNN segmentation papers to contextualize the performance gap; this is a standard practice, not a flaw.
- **"The paper would not lose anything if these theorems were removed."** — Removed as opinion. The underlying point (theorems don't cover LRF-Dyn) is kept in Major weakness #3, but the phrasing "remove the theorems" is an editorial judgment, not a weakness.
- **"The paper claims memory reduction without measuring latency, throughput, or energy."** — Kept but demoted to Minor weakness #3 (it is a real gap but secondary to the paper's main claims).
- **"The paper should be more cautious about attributing the performance gap to removing softmax."** — Removed as speculative. The paper's analysis of the softmax-removal effect is reasonable and supported by Figure 2.

## Novel Insights

The most notable observation from the reviews is the disconnect between the paper's biological-motivation narrative (neuronal charge–fire–reset dynamics) and the actual algorithmic mechanism (causal linear attention). The causal sum in Eq. 11 is the source of the memory reduction, not the neuronal dynamics framing. Independent of this paper, this highlights a recurring pattern in SNN-Transformer research: biological analogies are used to rebrand known algorithmic techniques (linear attention, recurrent state aggregation) as "biologically inspired," which can obscure rather than clarify the technical contribution. A more transparent derivation—starting from causal linear attention (`O_n = Q_n Σ_{j<n} K_j^T V_j`), mapping this to a state-space model with decay, and then noting the analogy to neuronal dynamics—would serve both the paper and the field better.

## Suggestions

1. **Clarify the causality question transparently.** State explicitly whether LRF-Dyn is causal. If it is, discuss why this is acceptable for image tasks (e.g., via positional encodings or sufficient context from the LRF module) and provide an ablation comparing causal vs. bidirectional versions of LRF-SSA and LRF-Dyn. If it is not actually causal, correct the summation indices in Eq. 11.

2. **Provide a clean, self-contained derivation of the dynamic approximation.** Start from the known causal linear-attention formulation, then show how it maps to the proposed recurrent form. Remove or tightly integrate the Fourier-transform path (Eq. 15) if it is not central. Define all variables, especially *v*_{\rho_k} and *X*_{\rho_k}.

3. **Report training hyperparameters and uncertainty measures.** Without these, the experiments are not reproducible. Even a brief table in the appendix with epochs, batch size, learning rate schedule, optimizer, data augmentation, and the number of runs would address the most critical reproducibility concern.

4. **Restructure the ablation to isolate the two contributions.** A four-way comparison (SSA baseline, SSA+LRF, causal SSA+LRF, LRF-Dyn) would reveal what each component contributes. Compare LRF-Dyn to a bidirectional version of LRF-SSA to show whether the dynamic approximation preserves performance.

5. **Either provide energy/latency measurements or remove the "energy-efficient" framing** from the title and abstract. Memory reduction is a meaningful contribution in its own right and does not need to be oversold.

## Score and Decision

**Round-1 bracket:** 3.5–7.5 (the paper is clearly above the low-band SNN papers scoring 3.0, but below the accepted SNN-Transformer papers scoring 5.67–7.0).

**Round-2 narrowing:** Within the 3.5–5.0 bracket, four rejected SNN papers sit at 3.67–4.50. The paper under review is comparable to DISTA (4.50, rejected) but has the additional causal-disclosure issue and zero training details, while having broader experimental coverage (ImageNet + ADE20K). These roughly balance to place it at 4.0.

**What the low-band anchors and weakness-anchored papers failed at:** Papers scoring ≤ 4.50 in this domain typically lack training details, present modest improvements without variance, have unclear or decorative theoretical framing, and/or insufficient ablation. The paper under review shares all of these failures.

### Calibration Anchors

| Anchor | Score | Round/Bucket | Comparison |
|--------|-------|-------------|------------|
| BBldjKEBlJ (QuantFormer) | 3.00 | R1-topic-low | Weaker: neural activity forecasting, not comparable SNN-Transformer |
| nwDRD4AMoN (Kuramoto Oscillatory Neurons) | 9.00 | R1-topic-low | Much stronger: accepted, but retrieval artifact (low-sim query, high score) |
| XrunSYwoLr (Spatio-Temporal Approx SNN) | 7.00 | R1-topic-mid | Much stronger: training-free SNN conversion, rigorous theoretical treatment |
| qzZsz6MuEq (Saccadic Attention) | 6.60 | R1-topic-mid | Stronger: clearer methodology, better ablation, accepted |
| 1SIBN5Xyw7 (Spike-driven V2) | 5.67 | R1-topic-mid | Stronger: more complete experiments, accepted despite incremental contributions |
| mjDROBU93g (DISTA) | 4.50 | R1-topic-mid | Similar: rejected, missing ImageNet, 1000-epoch training. Our paper has broader eval but worse reporting |
| CwAY8b8i97 (Spike Accumulation Forwarding) | 4.00 | R2 | Similar: rejected, comparable rigor level |
| 4ILqqOJFkS (SPikE-SSM) | 3.67 | R2 | Slightly weaker: rejected |
| 77plFC53J5 (Feature Overlapping) | 3.75 | R2 | Similar: rejected |
| VxJjw52dZu (LION) | 4.75 | R1-weakness-causal | Slightly stronger: bidirectional vs causal framing, more rigorous, but still rejected |
| NzEIjnIIzv (Bitune) | 7.25 | R1-weakness-causal | Much stronger: bidirectional attention for LLMs, accepted, but different domain |

**Final score: 4.0 — the paper has genuine empirical value (consistent improvements across tasks and architectures with demonstrated memory reduction) but is held back by a structural lack of transparency about the causal nature of LRF-Dyn, absent training details, single-run results on modest gains, and decorative theoretical framing. The core direction is worth pursuing, but the current manuscript is not ready for publication.**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>