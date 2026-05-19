## Summary
# Final Review Report

## Summary

This paper presents BAP (Branch-Aware Parallel execution), a runtime optimization system for DNN inference on mobile CPUs, targeting ASR models (Whisper, Conformer CTC) and vision transformers (MobileViT). BAP addresses a practical problem: existing mobile inference frameworks like TFLite use sequential node-by-node scheduling and aggressive memory reuse that cannot exploit branch-level parallelism in models with dynamic control flows and tensor operations.

BAP's technical approach has three components: (1) a graph analysis pipeline that classifies nodes (sequential/branching/merging) and partitions the computation graph into parallelizable subgraphs using topological sorting, (2) a branch-aware memory allocation strategy that isolates per-branch memory arenas indexed by a 32-bit NodeID encoding (layer/branch/local index) to prevent Read-After-Write conflicts during concurrent execution, and (3) multithreaded execution with a fixed thread pool and task stealing for load balancing.

The paper reports evaluations on four mobile platforms (Dimensity 8100, Kirin 980, Google Tensor, BCM2711) showing 14-38% latency reduction, 4.1-15.6x memory allocation savings vs. TFLite naive plan, and 8-25% energy savings. The core strengths are the practical relevance of the problem, clean system design with clear algorithmic components, and thorough multi-device evaluation.

**Major weaknesses identified:** (1) Missing variance/statistical reporting across all latency/memory/energy results, (2) Insufficient baseline comparisons — NN-Stretch (the closest conceptual match) and TFLite's inter-op parallelism are excluded, (3) Unspecified TFLite thread count configuration may bias comparisons, (4) Contribution claims lack explicit differentiation from prior work, (5) Energy measurement methodology uses estimated (not directly measured) power values without calibration disclosure, (6) Algorithm 1 has ambiguity in merge-node assignment and duplicate-subgraph removal, (7) Conclusion overstates average improvements not directly evidenced.

Due to external literature search being unavailable in this run, novelty and comparative positioning conclusions are deferred to manual verification.

## Strengths
1. **Practical relevance.** The problem of accelerating ASR and transformer models on mobile CPUs is timely and well-motivated. As speech interfaces and on-device AI become widespread, reducing inference latency on off-the-shelf edge devices has clear practical value.

2. **Clean system design.** BAP's three-component architecture (graph analysis → branch-aware memory allocation → multithreaded execution) follows a logical decomposition. The use of topological sorting on subgraphs to identify parallel layers (Algorithm 2) is a well-grounded approach to dependency resolution.

3. **Comprehensive device coverage.** The paper evaluates across four diverse hardware platforms (Dimensity 8100, Kirin 980, Google Tensor, BCM2711) spanning high-end smartphones to a single-board computer. This provides meaningful insight into how the method scales across different core counts and memory bandwidths.

4. **No accuracy degradation.** BAP does not modify model weights or architecture, so it preserves the original model's output accuracy. This is a clean property that avoids the accuracy-efficiency trade-off common in quantization/pruning approaches.

5. **Transparent implementation effort.** The paper discloses 2,116 lines of C++ code for the core algorithms and integration into TFLite 2.17.0, which aids reproducibility assessment.

6. **Layer-wise analysis.** Table 3 provides a fine-grained look at which layers benefit from parallelization and which see small overheads, giving readers insight into the method's operating characteristics.

## Weaknesses
The following weaknesses are ordered by severity and research-value impact.

**W1 (Major) — Missing statistical variance across all experimental results.** No standard deviations, confidence intervals, or min-max ranges are reported for any latency, memory, or energy measurement. Only 5 runs were averaged as point estimates. On mobile devices, OS scheduling, thermal throttling, and DVFS introduce 5-15% measurement variance. Without variance, readers cannot assess whether the reported latency reductions (14-38%) are statistically significant or within noise. [Page 7 - Performance Metrics, Page 8 - Latency Analysis]

**W2 (Major) — Insufficient baseline comparison and circular exclusion of closest methods.** The strongest conceptual baselines — NN-Stretch (graph branching for parallel execution) and TFLite inter-op parallelism (multi-threaded task graph) — are excluded with the justification that they "mainly focus on DNNs without dynamic control flows and rely on heterogeneous processors." This is a circular exclusion: NN-Stretch's core innovation is branch transformation, which is CPU-executable, and its heterogeneous aspect is separable. Without comparison, readers cannot attribute BAP's gains to its claimed novelty (branch-aware memory allocation) versus simply exploiting branch-level parallelism that existing frameworks could use with scheduler adaptations. [Page 7 - Baselines]

**W3 (Major) — Unspecified TFLite thread count configuration.** The paper does not specify how many threads TFLite was configured to use. If TFLite ran with its default (often 1 thread on mobile) while BAP used N threads, then the comparison partially measures "using more threads" rather than "branch-aware parallelism." The paper acknowledges TFLite's multithreading is "constrained to certain operations" but never quantifies this. A fair comparison requires running both BAP and TFLite with the same thread count. [Page 8 - Latency Analysis]

**W4 (Major) — Contribution claims lack explicit differentiation from prior work.** The three bullet contributions in the Introduction are stated without comparison to existing methods (NN-Stretch, CoDL, TFLite Arena). The paper does not answer: What does BAP's graph analysis do that NN-Stretch's branching does not? How is BAP's memory allocation different from CoDL's memory isolation? Without explicit differentiation, the contributions appear incremental. [Page 2 - Contributions]

**W5 (Major) — Energy measurement methodology concerns.** Energy is measured via Android BatteryManager API, which provides OS-estimated (not directly measured) power values with coarse temporal resolution (~5-60s averaging windows). At 10ms polling, readings may be aliased. The paper does not disclose display brightness, background process control, thermal state management, or whether the power model was calibrated per device. The reported 8-25% energy savings could fall within measurement uncertainty. [Page 9 - Energy Analysis]

**W6 (Major) — Algorithm 1 has ambiguous merge-node handling and underspecified duplicate removal.** Merge nodes encountered during subgraph partitioning are not clearly assigned to a branch or layer. The pseudocode states "finalize the group" for merge nodes but does not specify where the merge node itself belongs. Duplicate subgraph removal ("eliminate duplicates by comparing their structures") is underspecified — graph isomorphism is NP-complete, and no hashing or signature method is provided. [Page 5 - Algorithm 1]

**W7 (Major) — Branch/Layer definitions have mutual recursion.** A branch is defined as "a set of sequentially connected nodes within a layer" while a layer is "a set of branches that can be executed concurrently." This circular dependency makes it ambiguous which construct is derived first during graph analysis. An independent implementation could produce different results. The "no inter-branch dependencies" condition is stated but never formally defined. [Page 4 - Definitions]

**W8 (Moderate) — Conclusion overstates average improvements.** The conclusion claims "averaging 27% to 30%" latency reduction, but the paper only reports per-model per-device ranges (14-38%). The averaging method (weighted vs arithmetic, which models included) is not specified. Given that model sizes range from 67M to 912M parameters, an unweighted average may not represent typical deployment scenarios. [Page 10 - Conclusion]

**W9 (Moderate) — Very small evaluation datasets.** Only 10 images (MobileViT) and 5 audio samples (ASR) are used. For latency benchmarking, sample count directly affects mean estimate reliability. With 5 samples × 5 runs = 25 measurements per condition, confidence intervals are wide. [Page 7 - Performance Metrics]

**W10 (Minor) — NodeID encoding missing overflow guards and decode specification.** The 32-bit packed encoding (16-bit layer, 8-bit branch, 8-bit index) does not document overflow protection or signed-integer portability. No decode method is provided. [Page 6 - NodeID formula]

## Key Issues
### Issue 1: Baseline Fairness — TFLite Thread Count and NN-Stretch Exclusion
**Severity: Major | Affects: Validity of latency comparison**
The paper compares BAP against TFLite runtime without specifying TFLite's thread count. If TFLite used 1 thread (common mobile default) while BAP used N threads, the 14-38% latency reduction partially reflects "using more parallelism" rather than "branch-aware memory allocation." The paper also excludes NN-Stretch (the closest conceptual baseline) with a justification that conflates heterogeneous scheduling with graph branching.

**Required action:**
- (Must) Report TFLite's exact thread configuration and add a controlled multi-threaded TFLite baseline.
- (Must) Include a re-implemented CPU-only NN-Stretch baseline or provide a principled argument why it cannot be compared.
- (Must) Add an ablation: "BAP minus branch-aware memory" vs. "BAP full" to isolate memory allocation's contribution.

### Issue 2: Missing Statistical Variance in All Results
**Severity: Major | Affects: Reproducibility and statistical reliability**
Every latency, memory, and energy result is reported as a point estimate without standard deviation, confidence intervals, or min-max. Mobile benchmarks are notoriously noisy (5-15% variance from thermal throttling, OS scheduling, cache warm-up). Without variance, the significance of individual comparisons (e.g., 14.6% vs. 24.7% across devices) cannot be assessed.

**Required action:**
- (Must) Report mean ± std over ≥10 runs (after warm-up) for all latency/memory/energy figures.
- (Must) Disclose DVFS control, CPU governor settings, and thermal monitoring.
- (Nice-to-have) Add paired significance tests against the strongest baseline.

### Issue 3: Contribution Differentiation from Prior Work
**Severity: Major | Affects: Novelty perception**
The three contribution bullets (Page 2, lines 88-95) describe what BAP does but not what is *new* compared to NN-Stretch, CoDL, or TFLite Arena. For example, NN-Stretch also creates parallel branches; CoDL also isolates memory across execution units. The paper must state the concrete differentiation axis.

**Required action:**
- (Must) Add a comparison table or paragraph that maps each contribution to the closest prior work and states the specific difference.
- (Must) Move performance-only claims from contribution list to a results summary.

### Issue 4: Algorithm 1 Correctness Ambiguity
**Severity: Major | Affects: Reproducibility**
The merge-node handling in Algorithm 1 is ambiguous: when a merge node is encountered, does it become part of the current subgraph, start a new subgraph, or belong to the next layer? Duplicate removal via "comparing their structures" is underspecified — graph isomorphism checking is NP-complete without a concrete hashing strategy.

**Required action:**
- (Must) Specify the merge-node assignment rule with concrete examples.
- (Must) Document the duplicate-removal algorithm (hash signature method, expected O(n) or O(n log n) complexity).
- (Nice-to-have) Provide a worked example on a small graph.

### Issue 5: Energy Measurement Methodology
**Severity: Major | Affects: Validity of energy claims**
BatteryManager API provides OS-estimated (not directly measured) power values. The paper does not disclose calibration, display state, thermal management, or background process control. The 8-25% savings may be within measurement uncertainty.

**Required action:**
- (Must) Specify the exact BatteryManager API calls and acknowledge estimation limitations.
- (Must) Report display brightness, airplane mode, and thermal state during measurement.
- (Must) Add a qualification sentence that energy values are OS-estimated, not directly measured.

## Actionable Suggestions
### S1 — Rewrite the Abstract with Compact 5-Sentence Structure (Must)
**Target: Page 1 - Abstract**
Replace the current abstract with a structured version:
- S1: Problem statement (dynamic DNNs on mobile)
- S2: Specific gap (sequential scheduling misses branch-level parallelism)
- S3: Method (BAP's three components in one sentence)
- S4: Key results with ranges (18-38% latency, 4.1-15.6x allocation, 8-25% energy)
- S5: Bounded conclusion (without accuracy loss or model refactoring)

### S2 — Differentiate Contributions from Prior Work (Must)
**Target: Page 2 - Introduction, Contributions paragraph**
For each of the three contribution bullets, add a comparison clause. 
*Example:* "C1: We introduce BAP, a CPU-specific optimization system. Unlike NN-Stretch which relies on heterogeneous processor co-execution and requires model structure transformations, BAP operates entirely on CPU via runtime graph analysis without model modification."

### S3 — Add Variance Reporting to All Results (Must)
**Target: Pages 7-10 - All experimental figures and tables**
Add standard deviation or 95% confidence intervals to: Figure 2 (latency), Figure 3 (peak memory), Table 2 (allocation memory), Figure 4 (energy), Table 3 (layer-wise latency), Figure 5 (thread scaling). Run each configuration ≥10 times after a warm-up pass.

### S4 — Add Controlled Baseline Comparison (Must)
**Target: Page 7 - Baselines paragraph**
Add two baselines: (1) TFLite with explicit `SetNumThreads(N)` matching BAP's thread count, and (2) a CPU-adapted version of NN-Stretch's graph branching without heterogeneous offloading. Report both TFLite-single and TFLite-multi in all latency figures.

### S5 — Add Ablation Study: Memory Allocation Component (Must)
**Target: Page 8-10 or new subsection in 4.3**
Add "BAP w/o branch-aware allocation" (using TFLite's Arena allocator but with BAP's parallel scheduling) vs. "BAP full" to isolate the memory allocation contribution. This is essential for attributing which component drives the gains.

### S6 — Formalize Algorithm 1's Merge-Node Handling and Duplicate Removal (Must)
**Target: Page 5 - Algorithm 1 and surrounding text**
- Specify: "Merge nodes are not assigned to any branch. They terminate all incoming branches and become the first node of the next layer's sequential segment."
- Replace duplicate-removal with: "For each subgraph S, compute a hash H = SHA-256(concat(sorted(node_ids))). Use a hash set for O(n) deduplication."

### S7 — Disclose Energy Measurement Details (Must)
**Target: Page 9 - Energy Analysis**
Add: "BatteryManager.BATTERY_PROPERTY_CURRENT_NOW provides OS-estimated current draw, not direct measurement. Measurements were taken with display at 50% brightness, airplane mode enabled, and 30-second cooling periods between runs."

### S8 — Convert Related Work from Listing to Axes (Nice-to-have)
**Target: Pages 2-3 - Related Work**
Reorganize into three comparison axes: (1) Computational reduction methods (quantization/pruning/fusion) — orthogonal to BAP, (2) Architecture redesign methods (MobileNet/MobileBERT) — single-thread focus, (3) Parallel execution methods (CoDL/NN-Stretch/BAND) — closest but require heterogeneous hardware or static graphs. End with BAP's position in axis 3.

### S9 — Strengthen Conclusion with Explicit Limitations (Nice-to-have)
**Target: Page 10 - Conclusion**
Add concrete limitations: (a) BAP operates within TFLite's graph representation — models with heavily fused ops may expose fewer branches, (b) energy savings depend on workload balance — imbalanced branches reduce gains, (c) thread count tuning is currently manual and device-dependent.

### S10 — Add NodeID Decoding and Overflow Documentation (Nice-to-have)
**Target: Page 6 - NodeID formula**
Add a decode method: layer = (NodeID >> 16) & 0xFFFF, branch = (NodeID >> 8) & 0xFF, index = NodeID & 0xFF. Document that LayerID < 65536, BranchID < 256, LocalIndex < 256. Use uint32_t types.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction follows: (P1) Broad mobile inference challenges → (P2) CPU viability + four challenges → (P3) BAP proposal + contributions. The main weakness is that P1 is too broad (covering quantization, fusion, accelerators) and does not quickly narrow to BAP's specific focus. The reader must wait until P3 to understand the core idea.

### Candidate Storyline A (Recommended): Problem → Specific Gap → Solution → Evidence
This is a standard "narrowing funnel" structure.

- **P1 (Problem):** Real-time ASR and transformer inference on mobile devices is critical but faces a specific bottleneck: existing inference frameworks (TFLite, MNN) schedule operations sequentially and manage memory for linear tensor lifecycles, leaving branch-level parallelism unexploited.
- **P2 (Gap):** Existing approaches either (a) reduce computation via quantization/pruning, (b) redesign architectures for efficiency, or (c) co-execute across heterogeneous processors. None address CPU-only branch-level parallelism for models with dynamic control flows.
- **P3 (Solution):** We propose BAP, which combines three components — automatic branch detection, per-branch memory arena allocation, and multithreaded scheduling — that collectively reduce latency by 14-38% across four platforms without model refactoring.
- **P4 (Contributions):** Explicitly differentiate each contribution from prior work.

### Candidate Storyline B: Challenge-Response-Synthesis
- **P1:** Identify four specific challenges of parallel DNN inference on mobile CPUs (graph analysis, RAW conflicts, scheduling overhead, model refactoring).
- **P2:** Map each challenge to one prior approach that partially addresses it but falls short.
- **P3:** Show how BAP's three components jointly address all four challenges.
- **P4:** State contributions with explicit comparison to each prior approach from P2.

### Abstract Outline (Complete)
**S1 (Problem):** "Real-time inference of ASR and transformer models on mobile devices is limited by the sequential scheduling and linear memory management of existing CPU inference frameworks."
**S2 (Gap):** "These frameworks cannot exploit branch-level parallelism in dynamic computation graphs, leaving significant latency on the table."
**S3 (Method):** "We propose BAP, which automatically detects parallelizable branches via graph analysis, isolates per-branch memory arenas to prevent RAW conflicts, and executes branches concurrently with optimized multithreading."
**S4 (Results):** "On four mobile platforms, BAP reduces inference latency by 18-38% (avg. 27-30%), cuts memory allocation by 4.1-15.6x vs. TFLite naive, and saves 8-25% energy without accuracy loss or model refactoring."
**S5 (Bounded conclusion):** "BAP is most effective for models with three or more parallel branches per layer; for predominantly sequential models, gains are smaller."

### Introduction Outline (Complete, following Storyline A)
**P1 — Problem framing (2-3 sentences):** 
"Real-time ASR (Whisper, Conformer) and vision transformer (MobileViT) inference on mobile devices is increasingly demanded by voice assistants, live translation, and augmented reality. However, existing mobile inference frameworks (TFLite, MNN) are designed for static, linear computation graphs. When faced with dynamic control flows — branching subgraphs, variable-length inputs, and conditionally executed operations — these frameworks default to sequential node-by-node scheduling and memory management optimized for single-thread execution. This leaves a critical source of latency unaddressed: branch-level parallelism within the computation graph itself."

**P2 — Gap analysis (3-4 sentences):**
"Existing optimization strategies fall into three categories that are orthogonal to branch-level parallelism. First, computational reduction methods (quantization, pruning, operator fusion) shrink model size but preserve sequential scheduling. Second, architecture redesign (MobileNet, MobileBERT) improves single-thread efficiency but does not exploit graph-level parallelism. Third, heterogeneous co-execution methods (CoDL, NN-Stretch) parallelize across CPU+GPU but require static graphs or processor-specific memory management, making them incompatible with dynamic tensor operations. No existing approach targets CPU-only branch-level parallelism for dynamic models without model modification."

**P3 — Solution preview (2-3 sentences):**
"We propose BAP, a runtime system with three components: (1) a graph analysis pipeline that classifies nodes and partitions the graph into parallelizable subgraphs via topological sorting, (2) a branch-aware memory allocator that isolates per-branch memory arenas to prevent RAW conflicts during concurrent execution, and (3) multithreaded execution with a fixed thread pool and work stealing. BAP operates entirely within TFLite's existing graph representation and requires no model training, architecture changes, or accuracy trade-offs."

**P4 — Contributions (bullets with differentiation):**
"C1: A CPU-specific parallel execution system for dynamic models. Unlike NN-Stretch (which requires heterogeneous processors) and TFLite's intra-op parallelism (which only parallelizes individual kernels), BAP extracts branch-level parallelism from the computation graph itself. C2: A branch-aware memory allocation strategy that isolates per-branch arenas. Unlike TFLite's Arena (which assumes sequential lifecycles) and CoDL's memory partitioning (which targets heterogeneous processors), BAP's allocation is tailored to concurrent branch execution and dynamic tensor reallocation. C3: Measured 18-38% latency reduction and 8-25% energy savings across four platforms without model refactoring."

## Priority Revision Plan
### P0 — Critical (Must fix before submission)

| Priority | Item | Effort | Impact | Expected Outcome |
|----------|------|--------|--------|------------------|
| P0.1 | Add variance reporting (std/CI) to all results | Medium | High | Statistical credibility; refutes/reveals noise-floor concerns |
| P0.2 | Add NN-Stretch + TFLite-multi baselines | High | High | Fair comparison establishes true gain attribution |
| P0.3 | Specify TFLite thread count and add multi-threaded baseline | Low | High | Eliminates confounding factor in latency comparison |
| P0.4 | Differentiate contributions from prior work in Introduction | Low | High | Clarifies novelty boundary for reviewers |
| P0.5 | Disclose energy measurement methodology details | Low | High | Prevents validity challenge on energy claims |
| P0.6 | Fix Algorithm 1 merge-node and duplicate-removal ambiguity | Low | Medium | Ensures reproducibility |

### P1 — Important (Strengthen the paper)

| Priority | Item | Effort | Impact | Expected Outcome |
|----------|------|--------|--------|------------------|
| P1.1 | Add memory-allocation ablation study | Medium | High | Isolates branch-aware allocation contribution |
| P1.2 | Rewrite abstract with compact 5-sentence structure | Low | Medium | Improved first impression and clarity |
| P1.3 | Formalize Branch/Layer definitions (remove recursion) | Low | Medium | Eliminates definitional ambiguity |
| P1.4 | Report latency as range (min-max) not just "up to" numbers | Low | Medium | More honest presentation of results |
| P1.5 | Reorganize Related Work by comparison axes | Medium | Medium | Better positioning of BAP in the field |

### P2 — Nice-to-have (Quality polish)

| Priority | Item | Effort | Impact | Expected Outcome |
|----------|------|--------|--------|------------------|
| P2.1 | Strengthen conclusion with concrete limitations | Low | Medium | More honest scientific communication |
| P2.2 | Add NodeID decode method and overflow guards | Low | Low | Completeness for reproducibility |
| P2.3 | Increase evaluation samples (≥30 for each condition) | Medium | Low | Reduced measurement noise |
| P2.4 | Add thread-scaling curves for TFLite alongside BAP | High | Low | Complete comparison picture |

### Revision Order Recommendation
1. **First:** P0.3 (specify TFLite thread config — clarifies the entire baseline comparison)
2. **Second:** P0.2 + P0.4 (add missing baselines + differentiate contributions — addresses core validity/novelty issues together)
3. **Third:** P0.1 + P0.5 (add variance and energy methodology — strengthens empirical foundation)
4. **Fourth:** P0.6 + P1.3 (fix Algorithm 1 and definitions — improves reproducibility)
5. **Fifth:** P1.1 (ablation study — isolates memory allocation contribution)
6. **Sixth:** P1.2 + P1.5 + P2.1 (writing improvements)
7. **Seventh:** P2.2-P2.4 (polish items)

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | Latency reduction (overall) | 4 models × 4 devices, 5 runs each | Mean inference time (ms) | 14-38% reduction vs TFLite runtime | C1, C3 | No variance; TFLite thread count unspecified |
| E2 | Memory allocation savings | 4 models, arena size measurement | Allocation memory (MB) | 4.1-15.6x vs TFLite naive | C2, C3 | Compared against naive plan (easy target), not optimized planning |
| E3 | Peak runtime memory | 4 models × 4 devices | Peak memory (MB) | <5% increase vs TFLite runtime | C3 | No variance; small increase magnitude not tested statistically |
| E4 | Energy consumption | 2 devices (Pixel 6, K50), 4 models | Power (mW), Energy (mJ) via BatteryManager | 8-25% energy savings | C3 | BatteryManager is estimated, not measured; methodology underdocumented |
| E5 | Layer-wise parallelism | MobileViT-XS, Whisper on Pixel 6 | Per-layer inference time (ms) | Up to 67.7% (Whisper) / 58.1% (MobileViT-XS) reduction | C1 | Only 2 models; only 1 device; no variance |
| E6 | Thread count impact | 4 models on Pixel 6 | Latency vs thread count (1-8 threads) | Diminishing returns after 3-4 threads | C1 | TFLite scaling curve not shown for comparison |
| E7 | Accuracy preservation | All models | Output equivalence verified | Outputs identical to pretrained model | C3 | Mentioned but not quantitatively demonstrated |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Evidence Strength | Gap |
|--------------------------|-------------------------|-----|
| **New knowledge** (branch-aware memory allocation for dynamic DNNs) | Moderate | Missing ablation isolating memory allocation contribution from parallel scheduling |
| **Reproducibility** | Low-Medium | Missing: variance, TFLite thread config, Algorithm 1 merge-node rule, energy methodology details |
| **Impact on practice** (can practitioners adopt BAP?) | Medium | Requires TFLite runtime fork; not tested on non-TFLite frameworks (MNN, ONNX Runtime); deployment documentation absent |

### Proposed Research Experiments

#### P0 Experiments (Critical before submission)

**EXP-R1: Ablation for Memory Allocation Contribution**
- **Target Claim:** C2 (branch-aware memory allocation is necessary for safe parallel execution)
- **Hypothesis:** BAP's latency gain comes primarily from parallel scheduling; branch-aware allocation is needed primarily for correctness, not speed.
- **Minimal Design:** Compare (a) BAP full vs (b) BAP with TFLite Arena allocator (same parallel scheduling, same branch graph, but shared arena). Report latency, correctness (output mismatch count), and memory peak for all 4 models on 1 device (Pixel 6).
- **Controls:** Same thread count, same warm-up, same inference batches.
- **Metrics:** Latency (ms, mean±std over 10 runs), memory peak (MB), output mismatch count.
- **Success Criterion:** If (b) shows correct execution (0 mismatches) with similar latency to (a), then branch-aware allocation is not necessary for correctness. If (b) has mismatches or crashes, the allocation strategy is validated.
- **Estimated Cost:** ~2 days implementation + 1 day measurement.
- **Expected Gain:** Directly validates C2; strengthens novelty attribution.

**EXP-R2: Controlled Multi-threaded Baseline**
- **Target Claim:** C1 (BAP's branch-level parallelism outperforms TFLite's intra-op parallelism)
- **Hypothesis:** BAP's advantage over TFLite shrinks when both use the same thread count.
- **Minimal Design:** Run TFLite with `SetNumThreads(N)` for N = 1,2,3,4,6,8 on Pixel 6 for all 4 models. Report latency curves vs BAP on the same plot (extending Figure 5).
- **Controls:** Same CPU governor, same thermal conditions, same batch size.
- **Metrics:** Latency (ms) vs thread count.
- **Success Criterion:** If BAP remains faster at equivalent thread counts, the branch-level approach is validated. If TFLite matches BAP at high thread counts, the gain is from parallelism quantity, not branch awareness.
- **Estimated Cost:** 1-2 days measurement + figure generation.
- **Expected Gain:** Resolves W2/W3; establishes fair comparison.

**EXP-R3: Variance and Statistical Significance Package**
- **Target Claim:** All latency/memory/energy claims
- **Hypothesis:** Reported gains are statistically significant and not within noise.
- **Minimal Design:** Re-run all experiments (E1-E6) with 10 runs per configuration after warm-up. Report mean ± std. Flag CPU governor settings (performance mode), thermal throttling status, and cache warm-up procedure.
- **Controls:** Identical hardware setup and timing.
- **Metrics:** Mean ± std, coefficient of variation, 95% CI.
- **Success Criterion:** If all latency reductions have p < 0.05 (paired t-test vs TFLite), the significance is established. If not, report which comparisons are non-significant.
- **Estimated Cost:** 2-3 days of re-benchmarking.
- **Expected Gain:** Resolves W1; dramatically improves statistical credibility.

#### P1 Experiments (Strengthen the paper)

**EXP-R4: Extended Model Coverage**
- **Target Claim:** Generalizability across model types
- **Hypothesis:** BAP generalizes to other dynamic models (e.g., BERT, T5, Whisper-large).
- **Minimal Design:** Add 2 more models: BERT-base (transformer encoder) and a TTS model (e.g., FastSpeech2). Evaluate on Pixel 6 and Raspberry Pi 4B.
- **Metrics:** Latency reduction, memory allocation savings.
- **Success Criterion:** Consistent gains (>10% latency reduction) across added models.
- **Estimated Cost:** 3-5 days.
- **Expected Gain:** Broadens applicability claims beyond the current 4-model set.

**EXP-R5: Energy Measurement Calibration**
- **Target Claim:** C3 (energy savings)
- **Hypothesis:** BatteryManager-estimated energy correlates with external measurement but has systematic bias.
- **Minimal Design:** Calibrate BatteryManager readings against a known power draw (e.g., screen-on fixed brightness + CPU stress test). Report correlation coefficient.
- **Controls:** Same device, same measurement session.
- **Metrics:** Estimated vs expected power draw.
- **Success Criterion:** Correlation r > 0.9 across load levels; otherwise, report the uncertainty range.
- **Estimated Cost:** 1 day.
- **Expected Gain:** Validates or bounds the energy claims.

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Experiments (Gate for submission)
├── EXP-R1: Ablation (BAP vs BAP+TFLiteArena)
│   └── Validates C2: memory allocation contribution
├── EXP-R2: TFLite multi-threaded baseline
│   └── Resolves W2/W3: fair baseline comparison
└── EXP-R3: Variance package (10 runs + std + CI)
    └── Resolves W1: statistical credibility

P1 Experiments (Strengthen paper impact)
├── EXP-R4: Extended models (BERT, TTS)
│   └── Broadens generalizability claims
└── EXP-R5: Energy calibration
    └── Validates energy measurement methodology

Timeline: P0 first (1-2 weeks), P1 next (1-2 weeks)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

**Rationale:** The paper addresses a practically relevant problem with a clean system design and demonstrates promising latency reductions across diverse hardware. However, the score is primarily limited by:

- **Research value (6/10):** The core idea (parallelizing branch execution on CPUs) is incrementally novel over NN-Stretch and TFLite's existing parallelism, but the contributions lack explicit differentiation from prior work. Without the proposed ablation study (EXP-R1) and controlled baseline comparison (EXP-R2), the true novelty contribution cannot be assessed.
- **Validity/soundness (5/10):** The absence of statistical variance across all results, unspecified TFLite thread configuration, and estimated (not measured) energy values significantly weaken the empirical foundation. The Algorithm 1 ambiguity reduces reproducibility.
- **Novelty (6/10):** Deferred to manual verification due to external literature search being unavailable. Based on the manuscript alone, the branch-aware memory allocation concept appears to be a well-executed engineering contribution, but the conceptual increment over graph-level parallelism methods requires external comparison.
- **Reproducibility (5/10):** Algorithm ambiguities, missing implementation details (merge-node handling, duplicate removal, NodeID decode), and unstated TFLite configuration choices reduce reproducibility.

**Post-Revision Target: [7.5, 8.5]/10**

This target assumes that all P0 items are addressed: (1) variance reporting added, (2) NN-Stretch and TFLite-multi baselines included, (3) TFLite thread count specified, (4) contributions explicitly differentiated, (5) energy methodology disclosed, and (6) Algorithm 1 formalized. If these are fixed, the paper would provide a solid, reproducible contribution to mobile DNN inference optimization.

The upper bound of 8.5 is constrained by the inherently incremental nature of the contribution (CPU-only branch parallelism within an existing framework). A score above 8.5 would require demonstrating the approach on a fundamentally new problem domain or achieving order-of-magnitude improvements over the strongest baselines.