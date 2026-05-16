Let me proceed with the consolidated review based on my thorough reading of the paper and verification of all claims.

---

## Summary

This paper proposes a threat model for automated AI accelerator generation platforms — an underexplored security area — and demonstrates a complete attack chain. The attacker (a malicious platform developer) exploits the design-space exploration (DSE) unit to run a custom bit-level adversarial weight attack (C-SFE) that identifies sensitive intermediate-layer parameters, then embeds a hardware Trojan (HT) with only 0.34% LUT overhead into the generated accelerator. The attack is validated on Gemmini (FPGA, Xilinx U50) with VGG-16, ResNet-18, and YOLOv8m-cls, achieving 97–99% N-to-1 misclassification by modifying only 9–28 total parameters clustered in 3–4 kernels.

## Strengths

- **First systematic evaluation of security in automated AI accelerator generation platforms.** The paper identifies a genuine and timely vulnerability in the "full-stack integration" paradigm (Gemmini, NVDLA, Vitis AI) that has, as the paper notes, been "largely unexplored." This is a novel contribution to the security literature.

- **Effective attack with extremely low perturbation budgets.** C-SFE achieves 97.3% (YOLOv8), 99.2% (ResNet-18), and 98+% (VGG-16) misclassification rates while modifying only 9, 12, and 28 parameters respectively — all clustered into one kernel per intermediate layer. This is significantly more hardware-Trojan-friendly than prior adversarial weight attacks whose modifications scatter across layers.

- **Hardware Trojan with negligible overhead.** The HT occupies only 0.34% of total LUTs on the Gemmini-based design (71,246 → 71,490 LUTs), with minimal FF/BRAM/DSP changes. The paper also shows that with area-focused synthesis the malicious design can even appear to use *fewer* resources than the clean design, aiding stealth.

- **Concrete, realizable attack mechanism.** The method of piggybacking malicious information on unused bits in RoCC command fields (11 bits across 15 fields, hidden within `pool_size` and `kernel_dim` fields) is well-specified and directly implemented. The HT insertion in LoopConv and the Scratchpad Controller is physically realized on FPGA hardware (Xilinx U50 at 90 MHz), not just simulated.

- **C-SFE algorithm is designed for hardware constraints.** Unlike prior gradient-based attacks (T-BFA, etc.), C-SFE uses a heuristic (GA) requiring only forward propagation, targets only intermediate convolutional layers (avoiding the suspicious first/FC layers), and clusters bit flips within individual kernels. This design is explicitly motivated by the constraints of HT insertion and is a clear engineering contribution.

- **Comparison with T-BFA on kernel sparsity.** Section 4.3 shows C-SFE requires attacking only 3 kernels (one per layer) vs. T-BFA's 11 kernels for the same category, directly supporting the claim that prior methods are ill-suited for HT-based threat models.

## Weaknesses

### Fatal

None.

### Major

None. The issues identified are addressable in a revision and do not invalidate the paper's core claims.

### Minor

- **K-SIM description is underspecified.** The Kernel Selection Inference Method (Section 3.4, Figure 4) is the mechanism for inferring kernel positions across layers without repeated exploration, yet it is described only by example (sequential vs. residual cases) without pseudocode, equations, or an explicit algorithmic rule. The text explains that a kernel in layer *i* affects the corresponding filter index in layer *i*−1 via channel-wise dependency, and the residual case adds constraints, but a reader cannot precisely reproduce the inference logic. Since K-SIM is a key component of C-SFE's efficiency claim, this formal gap weakens reproducibility.

- **"Near-original performance" claim is unsupported.** The abstract and contribution list claim "maintaining near-original performance as in uncompromised designs" and "no performance degradation," but the paper presents no throughput, latency, or FPS measurements comparing the compromised vs. clean accelerator. The only hardware data is area/resource utilization (Table 2). While it is plausible that the HT does not affect normal datapath timing (it only triggers on specific instructions), this claim needs experimental support.

- **Generality claim goes beyond the evidence.** The paper states "our approach is broadly applicable to any similar automation platform" (Section 3.2) and describes the threat model as "generic," but the entire attack chain — the 15-field RoCC instruction abuse, the LoopConv/Scratchpad Controller HT insertion points, the specific use of `gemmini_loop_conv_ws` — is tightly coupled to Gemmini's microarchitecture. The paper acknowledges platform differences (e.g., NVDLA uses MMIO not RoCC) but does not discuss what properties another platform must have for the threat model to transfer. This overclaim is common in systems papers but worth noting.

- **T-BFA comparison is limited.** The comparison with T-BFA (Section 4.3, Figure 7) is conducted on one category (category 904) and one model (ResNet-18). While the purpose is to illustrate the qualitative difference in kernel count (3 vs. 11), the thinness of this comparison makes it difficult to assess whether C-SFE consistently requires fewer kernels across diverse targets. The paper would benefit from at least 3–5 categories.

- **Missing hyperparameter: β in the fitness function.** Equation 2 includes a penalty term `β × HD(qNew, qOrg)` where β is never specified. This affects reproducibility of the GA-based bit-level exploration.

- **Synthesis strategy for the baseline comparison is ambiguous.** Table 2 compares a clean design (first 4 columns) with a malicious design. The paper later notes that with an "area-focused" optimization the malicious design uses *fewer* resources, but it never explicitly states whether the first 4 columns use the same synthesis strategy for both clean and malicious designs. The default reading is that they do, but stating this explicitly would improve clarity.

### Trivial

- **Minor numerical inconsistency.** The abstract reports "98.1% for VGG-16" while the conclusion says "over 98%." If Table 1 shows 98.3% (as the reviewer claims), this should be harmonized. (Cannot independently verify the table image, but the abstract and conclusion are consistent as "over 98%" subsumes 98.1%.)

- **Total test image count is implicit.** The paper says 50 calibration images are selected from the ILSVRC 2012 validation set "with the rest used for verifying." The resulting count of 49,950 images is never stated explicitly.

## Nice-to-Haves

- Extend the T-BFA comparison to additional categories and models to strengthen the claim of C-SFE's superior kernel efficiency.
- Report the runtime of C-SFE for VGG-16 and YOLOv8m-cls (only ResNet-18's ~8 minutes is given).
- Discuss how the calibration set size (currently 50 images) affects C-SFE's effectiveness — would 10 or 500 images change the outcome?
- Add throughput/latency measurements on the compromised accelerator to substantiate the "near-original performance" claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Threat model framing ambiguity (Section 3.1)."** The harsh critic suggested ambiguity about whether the attacker is the developer or a third party. The paper states clearly at line 32: "It is assumed that the adversary is the developer of the AI accelerator platform." This is unambiguous. The claim in Section 3.2 about reusing DSE algorithms is consistent with developer-level access. *Removed as a misreading.*

- **"Algorithm 1 not shown."** The harsh critic noted Algorithm 1 is referenced but absent. The paper explicitly refers to the appendix, which has been stripped by the parser. *Removed per hard rule (parser strips appendix content from all papers).*

- **"Missing confidence intervals / multiple synthesis runs for overhead."** Requesting multiple synthesis runs is a wishlist item for a hardware paper that reports single-run synthesis results, which is the standard practice for FPGA implementation papers. *Removed as not standard for this setting.*

- **"Attack effectiveness on arbitrarily chosen target categories."** The paper demonstrates two different target categories (panpipe, honeycomb) across three models. Demanding demonstration that *every* category is equally attackable is scope creep. *Removed.*

- **"K-SIM is underspecified to the point of unreproducibility."** (Original harsh critic framing.) The description is informal but the core logic is communicated: the output of filter *f* in layer *l*−1 becomes an input channel to layer *l*, so disturbing filter *fIdx* in layer *l*−1 affects the corresponding channel in layer *l*. The residual case adds the constraint that filter indices must align. While formalization would help, calling it "unreproducible" overstates the issue — the mechanism is a standard channel-wise dependency. *Downgraded from fatal to minor.*

## Novel Insights

None beyond the paper's own contributions. The most interesting observation emerging from the review is the tension the paper identifies: prior adversarial weight attacks optimize for *bit sparsity* (fewest flips) but produce scattered kernel patterns that are *hardware-inefficient* for Trojan insertion, whereas C-SFE trades some bit-level efficiency for kernel-level clustering. This inversion of the optimization objective (cluster over sparsity) is the paper's genuine insight and is worth emphasizing. No reviewer insight goes beyond this.

## Suggestions

1. **Formalize K-SIM.** Provide at minimum a short pseudocode block or a precise rule (e.g., "for sequential networks, set *fIdx*⁽ˡ⁾ = *fIdx*⁽ˡ⁺¹⁾ where *kIdx* is free; for residual connections with an add operation, additionally constrain *fIdx*⁽ˡ⁾ = *fIdx*⁽ˡ⁺²⁾"). This is the single highest-impact revision.
2. **Add throughput/latency measurements.** Even a simple benchmark showing inference time per image on the compromised vs. clean accelerator would substantiate the "no performance degradation" claim.
3. **Disclose β and other hyperparameters** in a short table or footnote.
4. **Broaden the T-BFA comparison** to a few more categories (3–5 per model) or explain why the single comparison is representative.
5. **Tone down the generality claim** or add a paragraph discussing portability requirements (e.g., "any platform with CISC-style instruction fields containing unused bits and a modular convolution controller is potentially vulnerable").
6. **Clarify the synthesis strategy** for the first 4 columns of Table 2.

## Score and Decision

The paper identifies an important, understudied vulnerability, demonstrates a complete attack chain on real hardware with strong results (high misclassification, negligible overhead), and the C-SFE algorithm is well-motivated by hardware Trojan constraints. The weaknesses are fixable in revision: K-SIM needs a more precise specification, the "near-original performance" claim needs supporting measurements, and the generality claim should be tempered. None of these threaten the paper's core contribution. The paper is a solid contribution to the security and computer architecture communities.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>