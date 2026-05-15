Now I have a thorough understanding of the paper and can evaluate all claims carefully. Let me produce the final consolidated review.

## Summary

This paper proposes a novel threat model for automated AI accelerator generation platforms (e.g., Gemmini), where a malicious platform developer embeds a hardware Trojan (HT) during design generation and triggers it via hidden information in control instructions. The key technical contribution is the Cross-layer Sensitive Filter Exploration (C-SFE) algorithm, which identifies a minimal set of kernel parameters in intermediate convolutional layers that enables N-to-1 misclassification attacks while keeping the malicious information transmittable within Gemmini's instruction field budget. The attack achieves >97% targeted misclassification on YOLOv8m-cls, ResNet-18, and VGG-16 with as few as 9–28 parameter modifications and only 0.34% LUT overhead.

## Strengths

- **Novel threat model for a genuinely new attack surface.** The paper identifies and formalizes a security gap in full-stack AI accelerator generation platforms (Gemmini, NVDLA/Chipyard) that has not been previously explored. The grey-box threat model (Section 3.1) — where the adversary is the platform developer exploiting the exploration unit, software stack, and hardware generation flow — is well-justified and practically relevant.

- **C-SFE algorithm is cleverly tailored to hardware-imposed constraints.** The algorithm deliberately targets only intermediate convolutional layers, attacks a single kernel per layer, and uses a heuristic (GA) with forward propagation only (no gradients). This design directly addresses the two challenges identified in Section 3.3: minimizing the number of kernels/parameters to fit within the 15-field RoCC budget, and avoiding the first/last layers that security engineers monitor.

- **High attack success with very low parameter modification.** The attack achieves 97.3% (YOLOv8m-cls), 99.2% (ResNet-18), and 98.1% (VGG-16) targeted misclassification rates by modifying only 9, 12, and 28 parameters respectively (Table 1). The resource overhead is negligible (0.34% LUT increase), and the paper further shows that area-focused synthesis can make the malicious design use fewer LUTs than the clean design (Table 2), enhancing stealth.

- **Concrete exploitation of unused instruction bits for covert communication.** Section 3.3 concretely identifies unused bits within RoCC command fields (pool size, kernel dim) across the 7 commands for a convolution operation, deriving 15 usable fields (11 for malicious transmission). The HT reads these fields over the 7-cycle command sequence and replaces target weights as they load into scratchpad. This provides a practical, implementable mechanism for concealing the trigger in normal control flow.

## Weaknesses

### Fatal
None.

### Major
- **The paper's claim of hardware validation ("tested on FPGA") is ambiguously supported.** Section 4.1 describes a working system on a Xilinx U50 at 90 MHz, and Table 2 shows synthesis results for the HT. However, the paper does not explicitly distinguish whether the misclassification rates in Table 1 and Fig. 5 were measured from the actual hardware (with the HT modifying weights at runtime) or from offline software simulation of the weight modifications. The resource utilization confirms the HT was synthesized, and the attack algorithm demonstrably finds effective parameter modifications, but an end-to-end validation linking HT activation → weight corruption → misclassification on the FPGA hardware is not presented. This gap weakens the strongest form of the paper's claimed contribution but does not undermine the threat model or algorithm themselves.

### Minor
- **Narrow comparison with prior weight-attack methods.** The quantitative comparison (Section 4.3) is limited to T-BFA on a single category of ResNet-18. While this is sufficient to illustrate why prior methods are poorly suited (11 kernels vs. 3 kernels, 23 fields vs. within 15-field budget), a head-to-head comparison on additional models and categories — showing that T-BFA consistently exceeds the field budget while C-SFE does not — would substantially strengthen the argument that C-SFE is necessary for this threat model.

- **C-SFE algorithm description omits several parameters needed for reproducibility.** Section 3.4 describes the GA-based kernel exploration and PBPS bit-level strategy, but does not specify the population size (PS), number of generations, crossover/mutation rates, the penalty coefficient β in Equation (2), or the confidence threshold for PBPS termination. These details are essential for others to reproduce the results.

- **Attack results are reported for only one target class per model without variance.** Table 1 and Fig. 5 show results for a single target class per model (panpipe for VGG-16, honeycomb for ResNet-18/YOLOv8m-cls). Reporting the mean and variance across multiple random target classes would demonstrate the attack is not cherry-picked and provide a better sense of robustness.

### Trivial
- Section 3.3 would benefit from explicitly citing the specific Gemmini ISA register/funct values from which the 15 fields are derived, rather than describing them qualitatively.
- The large drop in classification rate between 7 and 6 parameters in Fig. 5 (from ~94% to ~52%) is presented without explanation of why 7 is a threshold for this class.

## Nice-to-Haves
- An ablation study removing K-SIM or PBPS individually to isolate each component's contribution.
- A discussion of potential countermeasures (instruction integrity checks, DSE auditing, RTL inspection) to contextualize the threat.
- Application of the threat model to a second accelerator generator (e.g., NVDLA/Chipyard), even via analysis rather than full FPGA implementation.
- A waveform or logic trace showing the malicious RoCC command bits arriving at the HT and the resulting scratchpad modification would cleanly resolve the hardware validation ambiguity.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point 1 (Field-budget mismatch):** The critic claims that attacking 4 kernels (VGG-16) requires 4×11=44 fields, exceeding the 15-field limit. This is incorrect. The 15 fields are per convolution operation (i.e., per layer), not global across all layers. As described in Section 3.3, each convolution operation sends its own set of 7 RoCC commands (6 config + 1 exec), providing 15 fields per layer. Since C-SFE attacks only **one kernel per layer**, each kernel's information (≤11 fields) comfortably fits within its layer's 15-field budget. The critic conflates cross-layer attack execution (sequential, per-layer) with simultaneous field packing. This is a factual misunderstanding of the paper's attack timing.

- **Criticism about missing field-budget verification (Section 4.3):** The paper already shows this indirectly: the comparison with T-BFA demonstrates that T-BFA requires 23 fields for a single layer's kernels (exceeding the 15-field budget), while C-SFE's per-layer kernel count (1) keeps it within budget. The paper also provides the YOLOv8m-cls example explicitly stating "only needs two fields for kernel's position and three fields for bit-flip mask information" — 5 fields, well within 15.

- **Criticism about unfair comparison:** The paper's comparison with T-BFA uses the same restricted layer set for both methods, which is actually conservative in T-BFA's favor (since restricting layers makes T-BFA's task easier, not harder).

- **Generic scope-creep demands** (larger dataset, more models, confidence intervals where not standard for the field).

## Novel Insights

None beyond the paper's own contributions. The key observation — that automated accelerator generation platforms create a new attack surface where exploration algorithms can be repurposed to find attack parameters, and the unused bits in RoCC command fields can carry malicious information — is the paper's own insight and is well-articulated.

## Suggestions

1. **Clarify the hardware validation chain.** State explicitly whether the results in Table 1 were measured from the FPGA hardware (with the HT triggered) or from simulation. If from hardware, describe the measurement procedure (e.g., "the HT was triggered via malicious RoCC commands embedded in the ONNX Runtime, and the accelerator's outputs were read via Ethernet/UART"). Adding even a single screenshot of hardware classification output would resolve this ambiguity entirely.
2. **Provide the missing C-SFE hyperparameters** (population size, generations, β, threshold) in a short table or appendix.
3. **Expand the comparison with T-BFA** to at least the three models reported (VGG-16, ResNet-18, YOLOv8m-cls), showing the field budget usage and kernel counts for each, to make the advantage systematic rather than anecdotal.
4. **Report attack results across multiple target classes** (e.g., 5–10 randomly selected) for each model, with mean and variance of the misclassification rate.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>