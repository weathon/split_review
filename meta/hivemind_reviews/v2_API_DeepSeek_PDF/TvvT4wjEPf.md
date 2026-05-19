## Summary
# Final Review Report

## Summary

This paper addresses the challenge of practical large-scale privacy-preserving recurrent neural network (RNN) inference using fully homomorphic encryption (FHE). The key technical contribution is **Overflow-Aware Activity Regularization (OAR)**, a training-time regularization method that mitigates numeric overflow in the CGGI ciphertext message space. By guiding pre-activations to "correct" overflow regions where the sign activation function produces accurate outputs despite modular wraparound, OAR enables single-ciphertext-per-activation representation while maintaining high accuracy. Combined with GPU-accelerated CGGI programmable bootstrapping, the authors evaluate a 1.9M-parameter multi-layer RNN on encrypted MNIST, achieving 90.82% top-1 accuracy with 2.1s per-sample latency — substantially faster than prior encrypted RNN work.

The paper is technically sound in its core idea and presents convincing evidence that OAR rescues accuracy at 5-6 bit precision. The latency improvement over prior work is impressive. However, several concerns limit the paper's contribution strength: (1) evaluation is limited to MNIST only, with no validation on other sequential domains (text, time-series, audio); (2) cross-method latency comparisons (274x vs SHE) are not apples-to-apples due to different datasets, hardware, and FHE schemes; (3) the OAR formulation has notation ambiguities that affect reproducibility; and (4) the conclusion overclaims "state-of-the-art" without sufficient breadth of evidence. Novelty claims are marked as deferred pending external literature verification due to Retrieval-Disabled Mode.

## Strengths
**S1. Technically well-motivated solution to a real problem.** The paper identifies a concrete bottleneck in encrypted RNN inference — ciphertext message-space overflow during multiply-accumulate operations — and proposes a targeted regularization solution. The overflow-aware design (OAR) directly addresses the root cause rather than applying generic fixes.

**S2. Impressive latency improvements.** The 2.1s per-sample latency for a 1.9M-parameter multi-layer RNN over encrypted data represents a substantial engineering achievement, enabled by the combination of single-ciphertext representation, CGGI programmable bootstrapping, and GPU acceleration.

**S3. Clear experimental evidence of OAR effectiveness at constrained bit-widths.** Table 1 convincingly demonstrates that OAR rescues accuracy at 5-bit (+70.85%) and 6-bit (+42.53%) precision, where models without OAR perform near random. The ablation across regularization rates (Table 2) and comparison with L2/OAR1/OAR2 (Table 7) provides useful hyperparameter guidance.

**S4. Honest limitations section.** Appendix A.5 transparently acknowledges the MNIST-only evaluation and OAR's failure below 5-bit precision. This improves scientific credibility despite weakening the paper's scope claims.

**S5. Reproducibility-conscious reporting.** The paper reports hardware specs (Table 5), security parameters (Table 6), training hyperparameters, and standard deviation for latency and error metrics. The 4-step quantization algorithm is provided with pseudocode (Algorithm 1).

## Weaknesses
**W1. Single-dataset evaluation (MNIST only).** All experiments are conducted exclusively on MNIST — a relatively simple 10-class grayscale image benchmark. The paper claims "practical large-scale" operation and "new state of the art," but has not validated on any other sequential domain where RNNs are commonly deployed (text classification, time-series forecasting, speech recognition). This fundamentally limits the generalizability claims. *(Annotations: Page 1 - Abstract, Page 7 - Table 1, Page 18 - Appendix A.5)*

**W2. Misleading cross-method latency comparison.** The 274x latency improvement over SHE (Lou & Jiang, 2019) is presented as a headline result, but the comparison involves different datasets (Penn Treebank vs MNIST), different hardware (CPU-only vs 2x A100 GPU), and different FHE schemes (BFV-style vs CGGI). These confounding factors make the direct multiplier unreliable and potentially inflated. *(Annotation: Page 2 - Introduction)*

**W3. Missing full-precision baseline.** The paper reports "plaintext accuracy" of 90.99% for the regular model, but this is the quantized (6-bit ModSign) plaintext accuracy, not the full-precision floating-point accuracy. The true accuracy gap due to quantization is therefore unknown. The paper later cites "99% full-precision plaintext MNIST evaluation" from generic MNIST benchmarks, which is for entirely different architectures. *(Annotation: Page 8 - Section 4.2)*

**W4. OAR formulation clarity issues.** Equation (2) uses ambiguous nested absolute-value notation (`||...||`), a mod operation with unspecified convention, and an offset constant `(k-2)/4` whose derivation from the "continuous derivative at all points" requirement is not shown. These issues hinder reproducibility. *(Annotation: Page 5 - Section 3.1)*

**W5. Enlarged model results are overstated as "excellent."** The enlarged model shows a 4.71% accuracy drop (encrypted vs plaintext) with 35% percent difference in FF(1024) activations and an output MAE of 53.38 — an order of magnitude worse than the regular model. Calling these "excellent results" without adding intermediary PBS operations to demonstrate a fix is not defensible. *(Annotation: Page 9 - Section 4.2)*

**W6. Non-linear OAR metric vs accuracy relationship not explained.** At 7-bit without OAR, the OAR metric is only 74.72% yet accuracy is 95.15%. At 6-bit without OAR, OAR metric is 48.43% with accuracy 46.82%. The paper does not explain this phase-transition behavior, which is important for understanding when OAR is actually needed. *(Annotation: Page 7 - Table 1)*

**W7. Conclusion overclaims.** The conclusion states "setting a new state-of-the-art" without the qualifiers that the evidence supports (MNIST-only, specific model scale, etc.). It also omits the limitations acknowledged in Appendix A.5. *(Annotation: Page 10 - Conclusion)*

**W8. Related Work is organized as a paper list rather than a structured comparison.** The section reads as a chronological summary of three papers rather than a comparison across methodological axes (FHE scheme, representation efficiency, quantization approach, scalability). *(Annotation: Page 9 - Related Work)*

## Key Issues
### Issue 1: Single-dataset evaluation undermines "practical large-scale" claims (Severity: Major, Fixability: Fixable)
The paper's central claim — enabling "practical large-scale privacy-preserving RNNs" — rests entirely on MNIST experiments. While MNIST is a standard benchmark for encrypted inference, it does not test the types of sequential tasks (language modeling, time-series forecasting, audio processing) that motivate RNN use. The claim that OAR works "across RNN scales" (Conclusion) is only shown for two model sizes on one dataset. At minimum, one additional dataset from a different domain is needed.

### Issue 2: Cross-method latency comparison inflates reported speedup (Severity: Major, Fixability: Fixable)
The 274x vs SHE comparison dominates the paper's narrative but involves confounded variables (dataset, hardware, FHE scheme). A fair comparison would require either running SHE's method on the same hardware/dataset, or clearly decomposing the speedup into factors (GPU acceleration, scheme efficiency, quantization choice). Without this, the headline number is misleading.

### Issue 3: Missing full-precision accuracy baseline (Severity: Major, Fixability: Easy fix)
The "plaintext" accuracy of 90.99% is already quantized (6-bit ModSign). The total accuracy cost of the approach (full-precision → 90.82% encrypted) is the sum of quantization loss + encryption noise loss. Without the full-precision baseline, readers cannot assess which factor dominates. This is a simple reporting fix.

### Issue 4: Enlarged model degradation not adequately addressed (Severity: Major, Fixability: Requires additional experiments)
The enlarged model shows 4.71% accuracy drop and ~35% layer PDs. The paper attributes this to FHE noise and suggests intermediary PBS as a fix but provides no experimental validation. This gap undermines the scaling claim.

### Issue 5: OAR formulation ambiguity (Severity: Minor, Fixability: Easy fix)
Equation (2) notation and missing derivation for the `(k-2)/4` offset constant reduce reproducibility. This can be fixed with clearer notation and a brief derivation.

### Top-5 Ranked Error Board
| Rank | Issue ID | Severity | Research-Value Impact | Validity Risk | Fixability | Confidence |
|------|----------|----------|----------------------|--------------|------------|------------|
| 1 | Single-dataset evaluation | Major | High — limits generalizability claims | Medium | Fixable (add dataset) | High |
| 2 | Cross-method comparison confounded | Major | High — headline result may be inflated | High | Fixable (decompose factors) | High |
| 3 | Missing full-precision baseline | Major | Medium — affects accuracy interpretation | Medium | Easy fix (report number) | High |
| 4 | Enlarged model degradation | Major | Medium — scaling claim needs support | Medium | Requires experiments | High |
| 5 | OAR formulation ambiguity | Minor | Low — affects reproducibility | Low | Easy fix (clarify notation) | Medium |

## Actionable Suggestions
### Suggestion A (Must, Priority P0): Add at least one additional sequential dataset evaluation
- **Target**: C1 (OAR effectiveness), C2 (practical large-scale RNNs)
- **Action**: Evaluate the same OAR-equipped quantization pipeline on a text classification dataset (e.g., IMDB reviews) or a speech commands task (e.g., Google Speech Commands v2). Report accuracy with/without OAR at 5-bit and 6-bit, encrypted latency, and plaintext accuracy for both full-precision and quantized baselines.
- **Expected impact**: Directly addresses the most significant weakness (single-dataset validation). If OAR works on a non-image domain, the paper's contribution is substantially strengthened.

### Suggestion B (Must, Priority P1): Decompose the 274x latency comparison
- **Target**: Abstract, Introduction, Related Work
- **Action**: Add a table decomposing the speedup into factors: (a) GPU acceleration vs CPU-only, (b) CGGI scheme vs BFV-style, (c) single-ciphertext vs multi-ciphertext representation. Qualify the headline number in the abstract.
- **Expected impact**: Prevents reviewer dismissal of the central latency claim as cherry-picked.

### Suggestion C (Must, Priority P1): Report full-precision baseline accuracy
- **Target**: Section 4.2, Table 3
- **Action**: Add a row to Table 3 showing the full-precision floating-point accuracy of the same architecture. This allows decomposing the accuracy gap into quantization loss vs encryption noise loss.
- **Expected impact**: Clarifies that the paper's main accuracy cost is quantization (acceptable) rather than encryption noise (potentially problematic).

### Suggestion D (Nice-to-have, Priority P2): Intermediary PBS experiment for enlarged model
- **Target**: Section 4.2
- **Action**: Add 1-2 intermediary PBS operations in the enlarged model's evaluation (e.g., after every 14 timesteps) and report whether the accuracy gap closes from 4.71% to ~1%. This validates the claim that FHE noise (not overflow) causes the degradation.
- **Expected impact**: Strengthens the scaling claim and provides a practical solution for future work.

### Suggestion E (Nice-to-have, Priority P2): Clarify OAR notation and derivation
- **Target**: Section 3.1, Equation (2)
- **Action**: Replace `||...||` with `|...|`, specify modulo convention (mathematical modulo, always non-negative), and add a step-by-step derivation showing why `(k-2)/4` offset yields continuous derivatives. Provide a worked example (x=12, k=16).
- **Expected impact**: Improves reproducibility.

### Suggestion F (Nice-to-have, Priority P3): Analyze the OAR metric vs accuracy non-linearity
- **Target**: Section 4.1.1
- **Action**: Add a scatter plot of per-layer OAR metric vs final accuracy across bit-widths. Discuss the threshold behavior (why 7-bit tolerates 25% incorrect-region pre-activations but 6-bit does not tolerate 52%).
- **Expected impact**: Deepens technical understanding of when OAR is needed vs when it is not.

### Suggestion G (Nice-to-have, Priority P3): Restructure Related Work as a comparison matrix
- **Target**: Section 5
- **Action**: Replace the sequential paper-summary format with a table comparing methods across axes: FHE scheme, ciphertexts-per-activation, quantization approach, supported activations, max parameters evaluated, latency, accuracy retention.
- **Expected impact**: Clearer positioning of the paper's contribution.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: MLaaS privacy problem → FHE solution → RNN challenges (noise + cost)
- P2: Non-interactive setting → CGGI choice → quantization from Anonymous [2025]
- P3: OAR introduced as overflow solution
- P4: Result summary with 274x latency claim
- P5: Section roadmap

**Strengths**: Technically accurate, covers all necessary topics.
**Weaknesses**: The gap (overflow problem) is introduced late (end of P2); the 274x comparison appears before the method is fully explained; P1 mixes motivation and technical challenge in one paragraph.

### Recommended Storyline: Candidate A (Best Alignment)

**Arc**: Big Picture → Gap → Core Insight → Solution → Evidence

- **P1 (Problem + Privacy Motivation)**: ML-as-a-service requires computation over user data, creating a privacy vulnerability. FHE enables encrypted computation but is computationally expensive, especially for RNNs due to recurrent depth requiring frequent bootstrapping.
- **P2 (Prior Work + Gap)**: Prior encrypted RNN work either uses expensive multi-ciphertext representations (SHE: 576s/sample) or suffers large accuracy drops (Anonymous [2025]: -25% from plaintext). The core gap is that single-ciphertext quantization causes overflow errors at large scale.
- **P3 (Core Insight)**: Overflow in modular arithmetic does not always flip the sign activation — there are "correct" overflow regions. By guiding pre-activations into these regions during training, we can use single-ciphertext representation without accuracy loss.
- **P4 (Solution: OAR)**: We introduce Overflow-Aware Activity Regularization (OAR) penalizes pre-activations in incorrect overflow regions, shifting them to correct regions. Combined with the ModSign activation function, this enables accurate encrypted inference at practical latency.
- **P5 (Results + Contribution Summary)**: We evaluate a 1.9M-parameter RNN on encrypted MNIST, achieving 90.82% accuracy with 2.1s latency — substantially faster than prior work at similar scale. OAR improves accuracy by up to +71 percentage points at constrained bit-widths.

### Abstract Outline (Complete)

- **S1 (Problem)**: Privacy-preserving RNN inference using FHE is impractical at scale due to ciphertext overflow in the bounded message space.
- **S2 (Prior Gap)**: Prior methods avoid overflow by using multiple ciphertexts per activation, causing exponential computation increase and prohibitive latency.
- **S3 (Proposed Method)**: We introduce Overflow-Aware Activity Regularization (OAR), a training-time technique that guides pre-activations to overflow regions where the sign activation function produces correct outputs, enabling single-ciphertext representation.
- **S4 (Key Result)**: Using CGGI FHE and GPU acceleration, we evaluate a 1.9M-parameter multi-layer RNN on encrypted MNIST, achieving 90.82% top-1 accuracy with 2.1s per-sample latency — within 0.17% of quantized plaintext accuracy.
- **S5 (Implication/Bounded Claim)**: This is the fastest encrypted RNN inference at this scale reported to date, demonstrating the viability of single-ciphertext quantization for privacy-preserving RNNs, though further evaluation across domains is needed.

### Introduction Outline (Complete, Per-Paragraph)

**P1 — The Privacy-Computation Challenge**
- **Role**: Establish stakes and introduce FHE.
- **Claim**: ML-as-a-service creates a privacy vulnerability; FHE solves it but at high computational cost.
- **Evidence**: Cite Gentry 2009, Podschwadt et al. 2022 survey.
- **Transition**: "However, applying FHE to RNNs is particularly challenging due to..."

**P2 — Why RNNs are Hard with FHE**
- **Role**: Explain the specific technical barrier (noise + cost + overflow).
- **Claim**: RNNs' recurrent structure requires frequent bootstrapping; even modest networks are impractical.
- **Evidence**: Prior encrypted RNN works (SHE, Podschwadt & Takabi 2021, Anonymous 2025) show limited scale.
- **Transition**: "A key bottleneck is that the ciphertext message space overflows during multiply-accumulate operations..."

**P3 — The Overflow Problem**
- **Role**: Define the gap precisely.
- **Claim**: Multi-ciphertext approaches avoid overflow but are exponentially costly; single-ciphertext approaches cause accuracy loss.
- **Evidence**: Anonymous [2025] achieves good latency but -25% accuracy drop.
- **Transition**: "In this work, we observe that overflow does not always cause incorrect activation outputs..."

**P4 — OAR: Core Insight and Solution**
- **Role**: Present the method's conceptual innovation.
- **Claim**: By exploiting the periodicity of modular overflow, pre-activations can be trained to stay in "correct" overflow regions, enabling single-ciphertext inference without accuracy loss.
- **Evidence**: Observations 1-2, OAR formulation (Section 3).
- **Transition**: "We validate this approach through experiments on encrypted MNIST..."

**P5 — Results Summary**
- **Role**: Preview key outcomes.
- **Claim**: OAR enables practical encrypted RNN inference at 2.1s/sample with minimal accuracy loss.
- **Evidence**: Headline numbers (90.82%, 2.1s, +71% improvement).
- **Transition**: "The rest of this paper is organized as follows..."

### Alternative Storyline: Candidate B (For a systems-focused venue)
Focus on latency/throughput as primary contribution, with OAR as the enabler. Lead with the 2. "State-of-the-art latency at 2.1s per sample on a 1.9M parameter model" and position OAR as the key that unlocked this efficiency. This storyline is simpler but de-emphasizes the methodological novelty.

### Alignment Check for Candidate A
- **Problem alignment (HIGH)**: Challenge (overflow in ciphertext) → Solution (OAR) → Evidence (Table 1, 3) are well-linked.
- **Variable alignment (HIGH)**: Key concepts (modular overflow, correct/incorrect regions, sign activation) appear consistently from Introduction through Method to Results.
- **Contribution-evidence alignment (MEDIUM)**: The main accuracy claim is well-supported, but the "practical large-scale" claim is only partially supported by MNIST data. Additional dataset validation would raise this to HIGH.

## Priority Revision Plan
### P0 — Publication-Critical (Must address before acceptance)

| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| P0.1 | Add evaluation on at least one additional sequential dataset (text or speech) | Validates generalizability of OAR; addresses most critical weakness | 1-2 weeks training + evaluation |
| P0.2 | Decompose 274x latency comparison: add table showing GPU/CGGI/single-ciphertext speedup factors, qualify in abstract | Prevents dismissal of core latency claim | 1 day (analysis + writing) |
| P0.3 | Report full-precision floating-point accuracy for the architecture in Table 3 | Allows readers to distinguish quantization loss from encryption noise | <1 day (one forward pass) |

### P1 — Major Revision (High impact on paper quality)

| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| P1.1 | Replace "state-of-the-art" with bounded wording in Conclusion and Abstract | Aligns claims with evidence; improves scientific credibility | <1 day (writing) |
| P1.2 | Restructure Related Work as a comparison matrix across design axes | Improves positioning clarity | 2-3 days (writing) |
| P1.3 | Add intermediary PBS experiment for enlarged model to demonstrate fix | Supports scaling claim | 3-5 days (implementation) |
| P1.4 | Clarify OAR loss composition (λ weight, per-layer aggregation) | Improves reproducibility | <1 day (writing) |

### P2 — Quality Improvement (Significant but not blocking)

| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| P2.1 | Analyze non-linear OAR metric vs accuracy relationship (7-bit anomaly) | Deepens technical understanding | 2-3 days (analysis + writing) |
| P2.2 | Clarify Equation (2) notation (replace ||...|| with |...|, add derivation) | Improves reproducibility | <1 day |
| P2.3 | Remove "time constraints" from Limitations; replace with concrete future-work plan | Improves professionalism | <1 day |
| P2.4 | Add per-class accuracy breakdown or confusion matrix for encrypted evaluation | Enables error analysis | 1 day |

### Revision Sequence (Recommended Order)
1. **Week 1**: P0.3 (full-precision baseline) + P0.2 (comparison decomposition) + P2.2 (Eq. clarification) — quick writing fixes
2. **Week 2**: P0.1 (additional dataset) — the most impactful experiment
3. **Week 3**: P1.3 (intermediary PBS) + P1.4 (loss composition)
4. **Week 4**: P1.2 (Related Work restructure) + P2.1 (OAR metric analysis) + P2.3-P2.4 (polish)

### Expected Impact After Full Revision
- **Validity**: High — confounded comparison resolved, full-precision baseline known
- **Generalizability**: Medium-High — additional dataset validates cross-domain applicability
- **Reproducibility**: High — clarified notation and loss composition
- **Overall paper quality**: Significant improvement from current state

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | OAR effectiveness at various bit-widths (Table 1) | MNIST RNN, 3-8 bit, with/without OAR2 (rate=10^{-3}) | Top-1 accuracy, OAR metric | OAR rescues 5-bit (+70.85%) and 6-bit (+42.53%) | C1 (OAR effectiveness) | MNIST only; OAR fails at 3-4 bit |
| E2 | OAR regularization rate sensitivity (Table 2) | MNIST RNN, 5-6 bit, rates 0 to 10^{-2} | Top-1 accuracy | Best rate = 10^{-4}; 5-bit more sensitive than 6-bit | C1 | Narrow rate sweep |
| E3 | OAR1 vs OAR2 vs L2 comparison (Table 7) | MNIST RNN, 6-bit, multiple rates | Top-1 accuracy | OAR2 > OAR1 > L2; L2 prunes ~9% more weights | C1 | No analysis of why OAR1 underperforms OAR2 |
| E4 | Enlarged model OAR evaluation (Section 4.1.4) | 128×128 MNIST, 8.48M params, 128 timesteps, 6-bit OAR2 | Top-1 accuracy | 92.69% plaintext accuracy; OAR metric 70.57% | C1, C2 | Only plaintext; no encrypted evaluation for this single experiment |
| E5 | Encrypted inference — Regular model (Table 3, 4) | 1.9M params, 28 timesteps, 6-bit, 2 param sets | Encrypted accuracy, latency, PD, MAE | 90.82% (set 2) with 2.1s; PD near-zero in early layers | C2 (practical latency + accuracy) | MNIST only; no full-precision baseline |
| E6 | Encrypted inference — Enlarged model (Table 3, 4) | 8.48M params, 128 timesteps, 6-bit, 2 param sets | Encrypted accuracy, latency, PD, MAE | 87.56-89.42% encrypted; 4.71% accuracy drop; high PD/MAE | C2 | Degradation not resolved; missing intermediary PBS experiment |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Status | Gap |
|-------------------------|---------------|-----|
| **New knowledge** | OAR is a novel regularization concept; validated mechanism (pre-activation shifting) is demonstrated | Mechanism understanding is phenomenological (histograms) not causal |
| **Reproducibility/Reusability** | Algorithm 1, hyperparameters, and security parameters reported | Equation (2) notation ambiguity; OAR loss composition (λ) unspecified |
| **Potential to change practice** | Demonstrates encrypted RNN latency reduction from minutes to seconds at 1.9M scale | Single-dataset validation limits adoption confidence |

### Proposed Research Experiments (P0/P1/P2)

**Experiment R1 (P0) — Cross-Domain Validation**
- **Target Claim**: C1 (OAR generalizes beyond MNIST)
- **Hypothesis**: OAR provides similar accuracy gains on text classification or speech tasks at constrained bit-widths
- **Minimal Design**: Apply the same 4-step quantization + OAR pipeline to an RNN on IMDB text classification (or Google Speech Commands). Evaluate accuracy with/without OAR at 5-bit and 6-bit.
- **Controls/Baselines**: (a) Full-precision, (b) 6-bit quantized without OAR, (c) 6-bit with OAR, (d) 5-bit without OAR, (e) 5-bit with OAR
- **Metrics**: Top-1/ top-5 accuracy, OAR metric per layer, encrypted latency
- **Success Criterion**: OAR improves 5-bit accuracy by >20 percentage points (relative) and 6-bit accuracy by >10 points
- **Estimated Cost/Time**: 1-2 weeks (dataset preprocessing, training, encrypted evaluation)
- **Expected Paper-Quality Gain**: Directly addresses the most critical weakness (single-dataset evaluation); transforms contribution from "MNIST result" to "generalizable method"

**Experiment R2 (P1) — Full-Precision Baseline for Regular Model**
- **Target Claim**: C2 (transparent accuracy decomposition)
- **Hypothesis**: The majority of accuracy loss is from quantization, not encryption noise
- **Minimal Design**: Train the same 1.9M-parameter architecture in full-precision floating-point (no quantization); report test accuracy
- **Controls/Baselines**: Compare against Table 3's "plaintext" (6-bit ModSign) and encrypted accuracy
- **Metrics**: Full-precision top-1 accuracy
- **Success Criterion**: N/A (descriptive, not comparative)
- **Estimated Cost/Time**: <1 day (one training run)
- **Expected Paper-Quality Gain**: Enables readers to clearly see quantization loss vs encryption noise loss

**Experiment R3 (P1) — Intermediary PBS for Enlarged Model**
- **Target Claim**: C2 (OAR scales to larger models)
- **Hypothesis**: Adding 1-2 intermediary PBS operations during the 128-timestep evaluation will reduce accuracy gap from 4.71% to <2%
- **Minimal Design**: Insert PBS operations after timesteps 42 and 84 (dividing into three segments). Evaluate encrypted accuracy with parameter set 2.
- **Controls/Baselines**: (a) No additional PBS (current result), (b) 1 additional PBS, (c) 2 additional PBS
- **Metrics**: Encrypted accuracy, latency, per-layer PD/MAE
- **Success Criterion**: Accuracy gap reduces from 4.71% to <2% with <2x latency increase
- **Estimated Cost/Time**: 3-5 days
- **Expected Paper-Quality Gain**: Validates the claim that FHE noise (not overflow) causes enlarged model degradation, and provides a practical mitigation

**Experiment R4 (P2) — OAR Metric vs Accuracy Threshold Analysis**
- **Target Claim**: C1 (understanding when OAR is needed)
- **Hypothesis**: There exists a threshold OAR metric value (~70-80%) above which accuracy is largely independent of OAR, and below which accuracy drops sharply
- **Minimal Design**: Compute per-layer OAR metrics and final accuracy for multiple bit-width/rate combinations; plot OAR metric vs accuracy
- **Controls/Baselines**: Use existing data from Tables 1 and 2
- **Metrics**: Accuracy vs OAR metric scatter plot, threshold identification
- **Success Criterion**: Identifies clear threshold that explains the 7-bit anomaly (74.72% OAR metric with 95.15% accuracy)
- **Estimated Cost/Time**: 1-2 days (analysis + plotting, no new training needed)
- **Expected Paper-Quality Gain**: Deepens technical contribution; provides practical guidance for practitioners

```text
ASCII Diagram — Experiment Upgrade Plan
Stage 1 (Week 1): P0 experiments
  [R1: Cross-domain validation]
  [R2: Full-precision baseline]
      |
      v
Stage 2 (Week 2-3): P1 experiments  
  [R3: Intermediary PBS for enlarged model]
  [R3a: Accuracy verification]
      |
      v
Stage 3 (Week 4): P2 analysis + writing
  [R4: OAR metric threshold analysis]
  [Integrate all results into paper]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Rationale*: The paper presents a technically sound and well-motivated solution (OAR) to a real problem (ciphertext overflow in encrypted RNNs). The latency results at 2.1s for a 1.9M-parameter model represent genuine engineering progress. However, the score is constrained by the following evidence-grounded concerns: (1) single-dataset (MNIST-only) evaluation fundamentally limits the generalizability claims, (2) the headline 274x latency comparison is confounded by different datasets, hardware, and FHE schemes, (3) full-precision accuracy baseline is not reported, making accuracy decomposition impossible, (4) the enlarged model shows significant degradation not adequately addressed, and (5) novelty claims cannot be externally verified in this run (Retrieval-Disabled Mode). The paper has a solid core idea but needs broader validation and more cautious positioning before it can be considered a strong contribution.

**Post-Revision Target: [7.5, 8.5] / 10**

*Rationale*: If the authors address the P0/P1 items — particularly adding a second dataset evaluation, decomposing the latency comparison, reporting full-precision baseline, and adding intermediary PBS for the enlarged model — the paper would move from a promising but narrow result to a well-validated method with clear positioning. The upper bound of 8.5 reflects the ceiling imposed by the incremental nature of the contribution (OAR builds directly on Anonymous [2025]'s 4-step quantization) and the lack of external novelty verification in this review.

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Encrypted RNN inference is impractical]
     |
     v
[Root Cause: Ciphertext message-space overflow during MAC ops]
     |
     v
[Solution: Overflow-Aware Activity Regularization (OAR)]
     |
     +---> [OAR1: Linear hat penalty (Eq. 2)]
     |         Notation: ambiguous ||...||, mod convention unspecified
     |
     +---> [OAR2: Quadratic hat penalty (Eq. 3)]
     |
     +---> [ModSign activation (Eq. 6)]
     
[Evidence Map]
     |
     +---> E1: Table 1 — OAR rescues 5/6-bit accuracy (STRONG)
     |         Gap: 7-bit anomaly unexplained (74.7% OAR metric → 95.2% acc)
     |
     +---> E2: Table 2 — Rate sensitivity (ADEQUATE)
     |         Gap: No λ decomposition (how OAR loss weighted vs classification loss)
     |
     +---> E3: Table 3/4 — Encrypted evaluation (ADEQUATE for regular, WEAK for enlarged)
     |         Gap: Full-precision baseline missing; enlarged model -4.71% gap
     |
     +---> E4: Section 4.1.4 — Enlarged model (WEAK)
     |         Gap: Only plaintext; encrypted shows large degradation
     |
     [CRITICAL GAP: Single dataset (MNIST) only — no cross-domain validation]
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current: Narrow validation, overstated claims]
     |
     v
[Revision Week 1: Quick fixes]
     +---> Add full-precision baseline (P0.3)
     +---> Decompose 274x comparison (P0.2)
     +---> Clarify Eq. (2) notation (P2.2)
     |
     v
[Revision Week 2: Critical experiment]
     +---> Cross-domain validation (P0.1) — text or speech dataset
     |
     v
[Revision Week 3: Scaling evidence]
     +---> Intermediary PBS for enlarged model (P1.3)
     +---> Clarify OAR loss composition (P1.4)
     |
     v
[Revision Week 4: Polish & restructuring]
     +---> Related Work as comparison matrix (P1.2)
     +---> Analyze OAR metric threshold (P2.1)
     +---> Conclusion: bounded claims (P1.1)
     |
     v
[Expected: Well-validated method, clear positioning, score 7.5-8.5/10]
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Privacy-Preserving NN Inference with FHE (Root)
│
├── Branch 1: FHE Scheme Choice
│   ├── Leaf 1.1: CGGI (TFHE) — bit-wise, PBS-based
│   │   ├── [Anonymous 2025] — 4-step quantization, single-ciphertext, -25% acc drop
│   │   └── This paper — OAR + ModSign, recovers accuracy, single-ciphertext
│   ├── Leaf 1.2: BFV/BGV — word-wise, larger plaintext space
│   │   └── [SHE: Lou & Jiang 2019] — multi-ciphertext fixed-point, 576s latency
│   └── Leaf 1.3: CKKS — approximate arithmetic
│       └── [Podschwadt & Takabi 2021] — batched sub-RNNs, 19.5min latency
│
├── Branch 2: Quantization Strategy
│   ├── Leaf 2.1: Fixed-point multi-ciphertext
│   │   ├── [SHE: Lou & Jiang 2019]
│   │   └── [Folkerts et al. 2023] (REDsec)
│   └── Leaf 2.2: Binary/ternary single-ciphertext
│       ├── [Anonymous 2025] — sign activation, 4-step QAT
│       └── This paper — adds OAR to handle overflow
│
├── Branch 3: Activation Function Support
│   ├── Leaf 3.1: Polynomial approximation (SHE)
│   └── Leaf 3.2: PBS-based exact evaluation (CGGI)
│       └── This paper — sign function via PBS
│
└── Branch 4: Scalability Demonstrated
    ├── [SHE: 180K params] — single-layer RNN
    ├── [Anonymous 2025: 12.6M params] — RNN with attention
    └── [This paper: 1.9M-8.48M params] — multi-layer RNN

[Novelty-Aware Positioning]
This paper's core contribution is the OAR regularizer + ModSign, which
solves the overflow problem inherent in single-ciphertext quantization.
It builds directly on [Anonymous 2025]'s 4-step framework and extends
it with overflow-aware training. The key differentiator vs prior work
is achieving single-ciphertext efficiency WITHOUT the -25% accuracy
drop. (Novelty verification deferred — see note below.)
```

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason |
|------|-----------------|----------------|-------------|
| 1 (Abstract + Intro P1) | 2 | Covered | — |
| 2 (Intro P2-P4 + FHE background) | 3 | Covered | — |
| 3 (CGGI scheme, Quantization of RNNs) | 1 | Covered | — |
| 4 (Observations) | 0 | Skipped | Text extraction limited; observations covered in page 5 annotation |
| 5 (OAR formulation, Eqs. 2-4) | 2 | Covered | — |
| 6 (ModSign, Experimental setup) | 1 | Covered | — |
| 7 (Tables 1-2, results) | 1 | Covered | — |
| 8 (Encr. data setup, 4.2) | 1 | Covered | — |
| 9 (Tables 3-4, enlarged model, Related Work) | 2 | Covered | — |
| 10 (Conclusion, References start) | 1 | Covered | — |
| 11-12 (References) | 0 | Skipped | Non-substantive (reference list) |
| 13-17 (Appendix: Algorithm, setup, regularizer comparison) | 0 | Partially covered | Algorithm 1 and training details in markdown; no additional annotation needed beyond page 18 |
| 18 (Output logits, Limitations) | 1 | Covered | — |

**Note on external literature verification**: This review was conducted in Retrieval-Disabled Mode (external paper search unavailable). All novelty/comparison conclusions in this report are therefore grounded solely in manuscript-internal evidence and the author-cited references. A full external novelty audit is required before final acceptance decisions. The related-work taxonomy tree above reflects only the papers cited in the manuscript itself and should be validated against the broader literature.