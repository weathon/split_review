- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes a threat model for automated AI accelerator generation platforms (e.g., Gemmini) where a malicious platform developer co-opts the design-space exploration unit, the software stack, and the hardware generation flow. The attacker uses a novel Cross-layer Sensitive Filter Exploration (C-SFE) algorithm—a genetic-algorithm-based method using only forward propagation—to locate sensitive model parameters in intermediate convolutional layers, then inserts hardware Trojans triggered via unused bits in control instructions. The attack is demonstrated on three ImageNet models (VGG-16, ResNet-18, YOLOv8m-cls) on a Xilinx U50 FPGA, achieving >97% targeted misclassification with ≤0.34% area overhead.

## Strengths

- **Concrete end-to-end attack chain spanning three platform components.** The paper shows how an attacker can integrate malicious code across the exploration unit (repurposing DSE for parameter search), the software stack (hiding trigger information in .so/.whl files), and the hardware generation flow (inserting HTs in generated RTL). This goes beyond prior work that typically attacks isolated components (model parameters, memory, individual LUTs). (Section 3.2, Fig. 1 red parts)

- **C-SFE achieves targeted attacks with substantially fewer kernels than prior bit-level adversarial weight attacks.** On ResNet-18 for the same target category, C-SFE requires 3 kernels (one per layer) while T-BFA (Rakin et al., 2021) requires 11 kernels unevenly distributed (Section 4.3, Fig. 7). This compactness is what makes the attack practically realizable within Gemmini's 15-field malicious-instruction limit (Section 3.3).

- **Real FPGA validation with hardware overhead measurements.** The attack is not just simulated—it is demonstrated on a U50 Alveo board with Gemmini at 90 MHz. Table 2 reports area overhead (0.34% LUT increase) and the interesting finding that area-focused synthesis can make the malicious design use *fewer* resources than the clean design.

- **C-SFE requires only forward propagation, making it suitable for quantized models.** The fitness function (Equation 1) uses only softmax confidence scores from forward passes, and the PBPS penalty term (Equation 2) incorporates Hamming distance. This design avoids gradient-based methods that are ill-suited for quantized weights and hardware-in-the-loop attack constraints—a genuine technical distinction from prior work like T-BFA.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed generality; the threat model is demonstrated on only one platform (Gemmini).** The paper states its approach is "broadly applicable to any similar automation platform" (end of Section 3.2) and positions itself as "a general threat model" (Section 1 Contribution 1). In reality, the attack exploits specific properties of Gemmini's RoCC commands: wide fields in CISC instructions with unused bits. The paper provides no analysis of how the attack would be adapted to platforms with different communication protocols (e.g., NVDLA with MMIO), different instruction encoding that enforces precise bit-widths, or any defense (parity checks, encoding audits). The threat model is therefore a Gemmini-specific case study, not a demonstrated general framework. This mismatch between the scope of the claims and the scope of the evidence weakens the paper's central positioning.

- **Insufficient statistical rigor in C-SFE evaluation.** The algorithm is stochastic (GA-based), searches on only 50 images from ILSVRC 2012 (line 96), and reports results for a single run per model with a single target class (panpipe for VGG-16, honeycomb for ResNet-18). There is no reporting of variance across multiple GA seeds, different random 50-image calibration draws, or different target classes. The headline rates (97.3%, 99.2%, 98.1%) may therefore reflect lucky configurations that do not generalize. Fig. 5 helpfully shows a threshold behavior for one model-class pair, but without statistical spread the reader cannot assess robustness. This is a significant evidential gap given the small calibration set and stochastic search.

### Minor

- **Detectability analysis is too narrow to support "concealment" claims.** The paper's stealth evaluation is limited to area overhead (Table 2) and a note about area-focused synthesis. No analysis is given of side-channel detectability (power, timing), logic testing (test pattern coverage), structural checks (unused-bit audit of instruction encoding), or software-level binary analysis (the malicious bits in .so/.whl files). The paper asserts (Section 3.2, bullet 2) that it is "difficult for [end users] to detect any hidden interfaces or subtle code modifications" without providing evidence. While a full detectability analysis is beyond a threat-model paper's scope, the abstract explicitly claims the results "clearly illustrate the concealment of the proposed security threat"—a claim that requires more thorough backing than area numbers alone.

- **K-SIM lacks an ablation study.** The Kernel Selection Inference Method is presented as a key enabler for cross-layer kernel selection, but there is no comparison against a baseline that independently explores each layer. Without this, it is unclear how much the inference method contributes vs. the underlying GA search. This does not invalidate the results but limits the ability to attribute the attack's compactness to the right component.

- **Key parameter choices for C-SFE are unreported.** The GA population size (PS), number of generations, mutation/crossover rates, and the penalty coefficient β in Equation 2 are not given. These are necessary for reproducibility and for understanding the algorithm's computational cost. The paper reports that exploration takes "approximately 8 minutes" for ResNet-18 but does not specify under which GA configuration.

- **Threat model framing is somewhat inflated.** The paper presents the attacker (platform developer) scenario as a novel security gap ("largely unexplored," Section 1), but a malicious developer with full control over DSE, RTL generation, and the software stack is a familiar insider-threat scenario. The real novelty is the *specific attack instantiation* (C-SFE + unused-bit HT triggering + compact kernel selection), which the paper would benefit from foregrounding rather than claiming the abstract threat model as the primary contribution.

### Trivial
None.

## Nice-to-Haves

- Testing on a second platform (e.g., NVDLA-via-Chipyard) or at minimum a discussion of how the attack would adapt to different communication interfaces (MMIO, AXI) would substantially strengthen the generality claim.
- Reporting mean and standard deviation of misclassification rates across multiple GA runs (e.g., 5 random 50-image draws, 3 target classes per model) would address the overfitting concern.
- An ablation study isolating K-SIM from naive layer-by-layer exploration would clarify the contribution of the inference method.
- A discussion of how the attack handles non-sequential topologies (e.g., branching architectures in YOLOv8's neck) beyond the brief residual-layer mention in Fig. 4 would improve completeness.

## Removed Points

- **"The threat model's core assumption is treated as a novel vulnerability without adequate justification"** — This criticism is partially valid (the threat-model framing is somewhat overblown), but I have already downgraded it to a minor weakness above. The harsh critic's stronger claim—that the paper's contribution "reduces to 'a malicious developer can do damage'"—is a strawman; the paper's real contribution is the specific attack chain and C-SFE algorithm, which are clearly described and go well beyond generic insider-threat awareness.

- **"No discussion of how the attack would be detected by standard HT detection methods"** — I have already included a condensed version of this as a minor weakness above. The harsh critic's more expansive version (listing power, timing, logic testing, binary analysis in detail) is removed to avoid duplication and because full detectability analysis is scope-appropriate to defer.

- **"The justification for using PTQ is weak"** — This is a speculative judgment about the paper's motivations. The paper provides a concrete justification (PTQ requires calibration data, lines 32–33). The critic's claim that it "feels like a post-hoc justification" is not a grounded weakness.

- **"Figure references are not fully explained"** — A minor formatting/style complaint that does not affect the paper's substance.

- **"The comparison to T-BFA is incomplete"** — The paper clearly states both methods achieved >98% misclassification, and the comparison focuses on kernel count—which is the relevant metric for the hardware-implementation constraint. The comparison is adequate for its purpose.

- **"No analysis of partial compromise (e.g., only modifying DSE)"** — The paper's threat model assumes full platform control. Requiring analysis of sub-attacker scenarios is scope creep.

- **"The threat model is demonstrated to be general, not limited to Gemmini"** (from Strength Finder) — This strength directly contradicts the verified weakness about overclaimed generality. Removed per instruction.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent pattern: the paper has a genuine technical contribution (C-SFE's ability to find compact, hardware-compatible adversarial weight configurations) but wraps it in an overbroad threat-model framing that the experiments cannot support. The most interesting finding from the reviews is that the paper's *strength* (the C-SFE algorithm) is somewhat at odds with its *framing* (the general threat model), and a more candid scope statement would likely strengthen the paper.

## Suggestions

1. **Re-scope the claims.** Replace "general threat model for any similar automation platform" with a precise characterization of the attack surface (platforms with CISC-style control instructions having unused bit fields, DSE-integrated generation flows, and opaque middleware). Acknowledge that other platforms (e.g., NVDLA) would require different attack mechanisms and leave the generality claim as future work.

2. **Add statistical grounding to the C-SFE evaluation.** Run the GA at least 5 times with different random seeds and calibration subsets, report mean ± std of misclassification rates per model, and test on 3–5 different target classes per model to demonstrate the attack is not cherry-picked.

3. **Report GA hyperparameters** (population size, number of generations, β in Equation 2) in a brief table or footnote.

4. **Include a baseline comparison** (e.g., independent single-kernel-per-layer search without K-SIM) for at least one model to quantify K-SIM's contribution.
