## Summary
This paper proposes Overflow-Aware Activity Regularization (OAR), a novel training technique designed to mitigate numerical overflow in the ciphertext message space when evaluating large-scale Recurrent Neural Networks (RNNs) using the CGGI variant of Fully Homomorphic Encryption (FHE). By guiding pre-activations into regions where modular overflow preserves correct sign outputs, OAR enables the use of smaller plaintext moduli (e.g., 6-bit) without severe accuracy degradation. The authors demonstrate the method on a 1.9M-parameter multi-layer RNN evaluated on encrypted MNIST, achieving 90.82% top-1 accuracy with an average latency of 2.1 seconds per sample. The work also introduces the ModSign activation function to better mimic CGGI modulus behavior during quantization-aware training.

## Strengths
- **Novel Methodological Insight:** The core idea of OAR—leveraging the periodic nature of modular arithmetic to guide pre-activations into "correct overflow" regions—is a clever and mathematically sound contribution to FHE-based neural network training. It directly addresses a critical bottleneck (plaintext modulus overflow) that has limited the scaling of CGGI-based RNNs.
- **Strong Empirical Demonstration:** The paper provides a comprehensive evaluation of OAR across different bit-widths and regularization rates, including visualizations of pre-activation distributions that clearly validate the mechanism. The successful deployment of a 1.9M-parameter RNN with 2.1s latency on encrypted MNIST is a compelling practical achievement.
- **Clear Technical Writing:** The method section is well-structured, with intuitive explanations of the overflow problem (Observation 1 & 2) before introducing the formal regularizer. The use of the ModSign function during training to mimic CGGI behavior is a thoughtful design choice that improves quantization alignment.

## Weaknesses
- **Unfair Comparative Claims:** The paper claims a "274x latency reduction compared to SHE [Lou & Jiang, 2019]." However, SHE evaluates a single-layer RNN on the Penn Treebank dataset (language modeling), whereas this work evaluates a multi-layer RNN on MNIST (image classification). Comparing latency across different tasks, datasets, and network architectures is scientifically invalid and misleading.
- **Overstated SOTA Claims:** The abstract and conclusion state "a new state of the art in latency, model performance, and scale" without bounding the claim to the specific evaluated setting (CGGI, 128-bit security, MNIST). Without a comprehensive benchmark table comparing against all recent CGGI/TFHE RNN works under identical settings, global SOTA claims are risky and may trigger reviewer skepticism.
- **Limited Generalization Evidence:** The method is evaluated solely on MNIST. While an enlarged model (128x128 pixels) is tested, the accuracy drop increases significantly (-2.85% to -4.71%), and the paper does not discuss whether this trade-off is acceptable for downstream applications. The failure of OAR at very low bit-widths (3-4 bits) is noted but not deeply analyzed, leaving the scalability limits of the method unclear.
- **Missing Reproducibility Details:** The experimental setup omits the random seed(s) used for initialization and data shuffling. Quantization-aware training is highly sensitive to initialization, and without seed reporting, results cannot be strictly reproduced.

## Key Issues
1. **Invalid Cross-Task Latency Comparison (Major):** The 274x latency improvement claim against SHE is fundamentally flawed because SHE operates on Penn Treebank (language modeling) while this work uses MNIST (image classification). Computational complexity and inference patterns differ drastically between these tasks. This comparison misleads readers about the true efficiency gains and should be removed or strictly bounded to same-task comparisons.
2. **Unbounded SOTA Claims (Major):** Asserting "state-of-the-art" without a comprehensive benchmark table under identical security/protocol settings is overconfident. The claim should be restricted to the evaluated configuration (e.g., "lowest reported latency for a multi-layer RNN of this scale under 128-bit CGGI security on MNIST").
3. **Scalability Trade-off Transparency (Minor):** The enlarged model shows a notable accuracy drop (-2.85% to -4.71%) compared to the regular model (-0.13% to -0.17%). Describing this as "excellent results" without acknowledging the accuracy-latency trade-off reduces scientific balance. The paper should explicitly discuss whether this drop is acceptable for target applications and propose mitigations (e.g., intermediary PBS operations).
4. **Reproducibility Gaps (Minor):** Missing random seed specifications and lack of multi-run variance reporting for quantization experiments reduce reproducibility. QAT is sensitive to initialization, and single-run results may not represent stable performance.

## Actionable Suggestions
- **Remove or Bound Cross-Task Comparisons:** Delete the "274x latency reduction compared to SHE" claim. If a comparison is necessary, explicitly state that SHE uses a different dataset/task and frame it as an illustrative architectural efficiency difference rather than a direct benchmark. Focus on absolute latency (2.1s) and scale (1.9M params) as primary achievements.
- **Restrict SOTA Wording:** Replace "a new state of the art in latency, model performance, and scale" with bounded phrasing: "achieves the lowest reported latency for a multi-layer RNN of this scale under 128-bit CGGI security on MNIST."
- **Clarify Baseline Precision:** Explicitly state that the "plaintext" baseline uses the same 6-bit ModSign quantization, not full-precision floating-point. Optionally report the full-precision baseline accuracy for context to avoid overclaiming.
- **Acknowledge Scalability Trade-offs:** In the enlarged model discussion, acknowledge the larger accuracy drop (-2.85% to -4.71%) and frame it as a manageable trade-off for the 4.57x latency increase. Discuss potential mitigations like intermediary PBS operations.
- **Add Reproducibility Details:** Specify the random seed(s) used for initialization and data shuffling. State whether results are averaged over multiple runs or represent a single best run.
- **Improve Introduction Gap Statement:** Add one sentence explicitly stating that bounded integer domains in schemes like CGGI cause multiply-accumulate overflow in large networks, leading to accuracy collapse unless mitigated. This sets up the OAR contribution more effectively.

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Problem & Domain):** Recurrent neural networks (RNNs) are widely used in privacy-sensitive applications like speech recognition, yet evaluating them over encrypted data remains impractical due to computational costs and ciphertext overflow.
- **S2 (Significance/Challenge):** Fully homomorphic encryption (FHE) schemes like CGGI operate over bounded integer domains, where multiply-accumulate operations in large RNNs frequently overflow the plaintext modulus, causing severe accuracy drops.
- **S3 (Prior Gap):** Previous attempts to mitigate overflow, such as ciphertext splitting or fixed-point arithmetic, incur exponential latency increases, rendering them unsuitable for latency-sensitive sequential tasks.
- **S4 (Proposed Method):** We propose Overflow-Aware Activity Regularization (OAR), a training technique that guides pre-activations into regions where modular overflow preserves correct sign outputs, enabling efficient single-ciphertext evaluation.
- **S5 (Key Result & Bounded Implication):** Using OAR with GPU-accelerated CGGI, we evaluate a 1.9M-parameter multi-layer RNN on encrypted MNIST, achieving 90.82% top-1 accuracy with an average latency of 2.1s per sample—demonstrating a practical balance of scale, speed, and privacy-preserving accuracy.

### Introduction Outline
- **P1 (Big Picture & Motivation):** Establish the importance of ML-as-a-Service and the privacy risks of plaintext computation. Introduce FHE as a solution but highlight its computational overhead.
- **P2 (Specific Gap for RNNs):** Explain why RNNs are particularly challenging for FHE: variable depth, noise accumulation, and critically, *plaintext modulus overflow* in bounded integer schemes like CGGI.
- **P3 (Prior Work Limitations):** Briefly review existing FHE-RNN approaches (SHE, CKKS-based methods, recent CGGI quantization) and explicitly state their failure modes (high latency, accuracy drops due to overflow).
- **P4 (Proposed Solution & Intuition):** Introduce OAR and ModSign. Explain the core intuition: instead of preventing overflow, we train the network to overflow "correctly" by penalizing pre-activations in sign-flipping regions.
- **P5 (Evidence & Contribution Summary):** Preview the key empirical outcomes (1.9M params, 2.1s latency, 90.82% accuracy) and list the concrete contributions (OAR method, ModSign activation, large-scale encrypted RNN evaluation).

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Remove "274x latency reduction vs SHE" claim; replace with bounded same-task comparisons or absolute metrics. | Eliminates misleading benchmarking; prevents major reviewer criticism. | Low |
| **P0 (Critical)** | Bound "state-of-the-art" claims to evaluated setting (CGGI, 128-bit, MNIST). | Improves scientific defensibility and objectivity. | Low |
| **P1 (High)** | Clarify that "plaintext" baseline uses 6-bit ModSign quantization, not full-precision. | Prevents overclaiming; sets accurate performance expectations. | Low |
| **P1 (High)** | Add random seed specification and multi-run variance reporting for QAT experiments. | Enhances reproducibility and statistical reliability. | Medium |
| **P2 (Medium)** | Acknowledge accuracy-latency trade-off for enlarged model (-2.85% to -4.71% drop). | Balances scalability claims; shows critical analysis. | Low |
| **P2 (Medium)** | Refine Introduction gap statement to explicitly introduce modulus overflow as a third barrier. | Strengthens motivation for OAR; improves narrative flow. | Low |

## Experiment Inventory & Research Experiment Plan
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | OAR effectiveness across bit-widths | MNIST RNN, 3-8 bit widths, OAR2 rate 10^-3 | Accuracy, OAR Metric | +71% accuracy gain at 5-bit; OAR metric >99% | OAR mitigates overflow | Fails at 3-4 bits |
| E2 | OAR rate sensitivity | 5-bit & 6-bit, rates 10^-6 to 10^-2 | Accuracy | 10^-4 optimal; 5-bit more sensitive | Hyperparameter guidance | Single seed reported |
| E3 | Pre-activation distribution visualization | FF(1024) layer histograms | Distribution shape | Values concentrated in correct regions | Mechanism validation | Qualitative only |
| E4 | Enlarged RNN scaling | 128x128 pixels, 8.4M params, 128 timesteps | Accuracy | 92.69% plaintext accuracy | Scalability potential | Higher encrypted error |
| E5 | Encrypted inference (Regular) | 1.9M params, Param Sets 1 & 2 | Accuracy, Latency, PD, MAE | 90.82% acc, 2.1s latency | Practical efficiency | MNIST only |
| E6 | Encrypted inference (Enlarged) | 8.4M params, Param Sets 1 & 2 | Accuracy, Latency, PD, MAE | 87.56-89.42% acc, 10-21s latency | Linear latency scaling | Accuracy drop -2.85% to -4.71% |

### Research-Theme Gap Diagnosis
- **Generalization:** Evaluated solely on MNIST. No evidence of transferability to speech recognition or financial forecasting (mentioned in abstract).
- **Low-Bitwidth Robustness:** OAR fails at 3-4 bits. The boundary conditions and gradient dynamics causing this failure are not analyzed.
- **Statistical Reliability:** No multi-seed variance reporting for QAT experiments, which are sensitive to initialization.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Generalization | OAR works on sequential data beyond images | Evaluate on CIFAR-10 or Penn Treebank | Same architecture, no OAR | Accuracy, Latency | <5% accuracy drop | Medium | Validates broader applicability |
| Statistical Stability | Results are consistent across seeds | Run E1/E5 with 3 different seeds | Fixed architecture | Mean±Std Accuracy | Std < 1% | Low | Improves reproducibility |
| Low-Bit Analysis | Gradient spikes cause 3-4 bit failure | Analyze gradient norms during training | OAR vs L2 regularization | Gradient magnitude, Loss curve | Identify divergence point | Low | Explains boundary limits |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a novel and mathematically sound regularization technique (OAR) that effectively addresses a critical bottleneck in FHE-based RNN evaluation (plaintext modulus overflow). The empirical demonstration on a 1.9M-parameter model with 2.1s latency is compelling and practically significant. However, the score is reduced due to unfair cross-task latency comparisons (SHE), unbounded SOTA claims, and limited generalization evidence (MNIST-only). These issues are fixable and do not invalidate the core contribution, but they currently weaken the scientific defensibility of the claims.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Removing misleading comparisons, bounding SOTA claims to the evaluated setting, clarifying baseline precision, and adding multi-seed variance reporting will significantly improve the paper's rigor and reviewer confidence. If the authors also provide a brief analysis of the low-bitwidth failure mode or evaluate on one additional dataset, the paper would be strongly competitive.