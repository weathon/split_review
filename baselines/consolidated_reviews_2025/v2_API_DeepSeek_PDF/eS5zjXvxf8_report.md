## Summary
# Final Review Report

## Summary

This paper presents MULTIIOT, a large-scale benchmark for multisensory learning on the Internet of Things (IoT), aggregating over 1.15 million samples across 12 sensor modalities and 8 tasks from existing public datasets (KITTI, Ego4D, TouchPose, DIP-IMU, LLVIP, etc.). The authors provide standardized implementations of six modeling paradigms—domain-specific, unimodal, adapter, unimodal multi-task, multisensory, and multisensory multi-task—and conduct experiments to benchmark performance across all tasks. The main empirical finding is that multisensory multi-task models consistently outperform unimodal baselines, but performance degrades under longer sequences and sensor noise.

**Strengths:** The paper addresses a real need for unified IoT benchmarks. The breadth of modalities (12) and tasks (8) is genuinely wider than existing multimodal IoT resources. The systematic comparison of six modeling paradigms provides a useful starting point for the community. The zero-shot/few-shot transfer experiment is a valuable direction. Broader impacts discussion shows awareness of privacy and bias concerns.

**Core Weaknesses (see Key Issues for details):** (1) The paper aggregates existing datasets without collecting new data, but this is not clearly stated—"collected" language overstates the contribution. (2) No variance/statistical significance is reported for any result, making it impossible to assess reliability of the observed improvements. (3) The zero-shot experiment is critically underspecified: "fix-8" is never defined. (4) Missing reproducibility-critical details: train/val/test splits, dataset-specific preprocessing, seed reporting. (5) Causal attribution claims ("can be attributed to...") are made without controlled ablations. (6) The noise/heterogeneity analysis is purely qualitative. (7) Novelty claims cannot be verified due to external retrieval being unavailable in this review run; manual literature comparison is deferred.

**Recommendation:** The benchmark has potential value as a community resource, but the manuscript requires substantial revisions in experimental rigor, claim bounding, and reproducibility before it meets ICLR standards. Major weaknesses in reproducibility and missing statistics are fixable but require significant additions.

## Strengths
1. **Broad modality and task coverage.** MULTIIOT aggregates 12 distinct sensor modalities (IMU, thermal, GPS, camera, capacitance, depth, gaze, pose, LiDAR, video, audio, image) and 8 tasks (gaze estimation, depth estimation, gesture classification, pose estimation, touch contact classification, event detection, activity recognition, 3D reconstruction). This is the most diverse IoT-focused benchmark assembled to date, and the unified evaluation framework addresses a genuine fragmentation in current IoT ML research where individual papers use different datasets and protocols.

2. **Systematic multi-paradigm baseline suite.** The paper provides six modeling paradigms ranging from domain-specific heuristics to multisensory multi-task models. This standardized baseline suite is a practical contribution: it gives the community a clear starting point and a common reference for future work on MULTIIOT. The finding that multisensory multi-task models consistently outperform simpler alternatives across all 8 tasks is informative and empirically grounded within the benchmark's scope.

3. **Zero-shot and few-shot transfer experiment.** The inclusion of transfer learning experiments (Table 4) is a forward-looking contribution that goes beyond standard benchmark reporting. Even though the description is currently underspecified (see Weaknesses), the core idea—studying whether representations learned on MULTIIOT transfer to unseen modality-task combinations—is a valuable research direction that could have high impact.

4. **Privacy and bias awareness.** The broader impacts section (Section 6) discusses data privacy, federated learning, differential privacy, and bias amplification. This shows the authors' awareness of the ethical dimensions of human-centric IoT data, which is particularly important given that many of the constituent datasets (Ego4D, TouchPose, DIP-IMU) contain personally identifiable information.

5. **Comprehensive related work coverage.** The related work section surveys relevant IoT representation learning methods (DIP-IMU, EyeMU, TouchPose, LLVIP, RGBDGaze), multimodal transformers, self-supervised pretraining, and general-purpose multimodal architectures (Perceiver, HighMMT, Gato, PolyViT). While the organization could be improved (see Weaknesses), the breadth of coverage demonstrates that the authors are aware of the landscape.

## Weaknesses
The weaknesses are organized from most to least critical. Each weakness is grounded in specific evidence from the manuscript, and a concrete remediation path is provided in the Actionable Suggestions and Priority Revision Plan sections.

### W1. Missing variance statistics and significance testing (Critical)
Every result in Tables 1-4 is reported as a single point estimate without standard deviations, confidence intervals, or significance tests. Since improvements between modeling paradigms are often small (e.g., 98.7% vs 99.3% for gesture classification), readers cannot determine whether these differences are statistically meaningful. **Evidence:** Table 1, Page 6. **Impact:** Undermines the paper's main empirical claim that multisensory multi-task models "consistently outperform" alternatives. Without variance, the claim is not falsifiable.

### W2. Undefined "fix-8" dataset in zero-shot experiment (Critical)
The zero-shot and few-shot transfer experiment (Page 7, Section 4.2) uses a target dataset called "fix-8" that is never defined or introduced anywhere in the paper. The term appears only once with no description of its composition, size, source datasets, or how it relates to the 8 main tasks. **Evidence:** Page 7, lines 33-34: "We chose the fix-8 dataset as the target." **Impact:** This experiment is not reproducible and its conclusions are unverifiable.

### W3. Missing reproducibility details (Major)
The experimental setup (Section 4.1, Page 6) does not specify: (a) train/validation/test splits for any of the 8 tasks, (b) dataset-specific preprocessing (input sizes, normalization, signal windowing), (c) number of random seeds, (d) how asynchronous modalities are temporally aligned, (e) the exact neural architecture per modality (only "CNNs for images" and "RNNs for sequential data" are mentioned). **Evidence:** Page 6, lines 21-30; Appendix B (Pages 18-19) repeats the same generic statements. **Impact:** A benchmark's primary value is enabling reproducible comparison—missing these details defeats the purpose.

### W4. Unsupported causal claims (Major)
The text repeatedly uses causal language that is not supported by controlled experiments. For example, Page 6: "This can be attributed to their ability to integrate information across modalities and tasks" — no ablation isolates the fusion mechanism from confounds (total parameter count, training dynamics, input dimension). **Evidence:** Page 6, lines 40-42; Page 7, lines 22-24. **Impact:** The paper's central interpretation is presented as proven causality when the evidence only supports correlational observation.

### W5. Superlative claims without comparison (Major)
The paper repeatedly calls MULTIIOT "the most expansive IoT benchmark to date" and "the largest and most diverse of its kind" (Abstract, Page 2, Conclusion). No comparison table against existing IoT or multimodal benchmarks is provided to substantiate these claims. Since external literature retrieval is unavailable in this review run, these claims require manual verification. **Evidence:** Page 1, lines 17-18; Page 2, line 30; Page 9, lines 33-34.

### W6. Qualitative noise and heterogeneity analysis (Major)
The experiments on long-range interactions and noise heterogeneity (Section 4.3, Page 7-8) report only qualitative observations ("marked decline in performance," "rapid decline") without quantifying the degradation. Noise parameters (variance level, which modalities) are unspecified. Figure 3 is referenced but the rendered text does not include a proper labeled figure. **Evidence:** Page 7-8, lines 15-27; Figure 3 caption. **Impact:** These experiments are central to the claimed identification of "fundamental challenges," but are presented too imprecisely to be useful.

### W7. Data aggregation misrepresented as collection (Minor)
Section 2.2 states "We collected diverse data from IoT devices" (Page 3, line 8), but all data comes from existing public datasets (KITTI, Ego4D, TouchPose, DIP-IMU, etc.). No new data was collected. **Evidence:** Page 3-4, Sections 2.2-2.3. **Impact:** While dataset aggregation is a valid contribution, the framing overstates the novelty and may mislead readers about the benchmark's scope.

### W8. Formula notations are imprecise (Minor)
Equation (2) for adapter models (Page 5) uses ambiguous notation: $y = M_{W+A}(x) = M_W(A_{W_A}(x))$ conflates weight addition with function composition. Equation (1) is trivial (just the definition of empirical risk). **Evidence:** Page 5, lines 51-60.

### W9. Related work is a flat list, not comparative (Minor)
The three related work paragraphs (Page 9) list methods chronologically without organizing around analytical axes. There is no comparison table contrasting MULTIIOT with existing multimodal/IoT benchmarks (MultiBench, MME, etc.). **Evidence:** Page 9, lines 6-31.

### W10. Weak conclusion synthesis (Minor)
The conclusion (Page 9) largely repeats the abstract's claims without consolidating specific findings, reporting what remains open, or offering actionable future directions beyond generic statements. **Evidence:** Page 9, lines 32-39.

## Key Issues
The following are the highest-priority issues that must be addressed for the manuscript to meet publication standards, presented as a ranked board.

### Ranked Issue Board

| Rank | Issue | Severity | Validity Risk | Research-Value Impact | Fixability | Annotation ID(s) |
|------|-------|----------|--------------|----------------------|------------|------------------|
| 1 | Missing variance/statistics on all results | Critical | High (main claim not falsifiable) | High (benchmark comparisons meaningless without error bars) | Easy | dc02af5b |
| 2 | "fix-8" dataset undefined in zero-shot experiment | Critical | High (experiment unverifiable) | Medium (interesting direction but unreproducible) | Easy | 5e33efb6 |
| 3 | Missing train/val/test splits, preprocessing, seeds, architectures | Major | High (benchmark not reproducible) | High (core purpose of benchmark undermined) | Medium | dc551971 |
| 4 | Causal attribution without controlled ablations | Major | Medium (claims overstate evidence) | Medium (weakens scientific credibility) | Medium | dc02af5b |
| 5 | Unsupported superlative claims ("most expansive") | Major | Medium (no comparison table) | Medium (novelty positioning unclear) | Easy | ff59cc8c |
| 6 | Qualitative noise/heterogeneity analysis without numbers | Major | Medium (key results non-quantitative) | Medium (undermines challenge identification) | Medium | baa616ae |
| 7 | Data aggregation framed as new collection | Minor | Low (scope clarification) | Low (easy fix) | Easy | e0456b48 |
| 8 | Imprecise formula notation (Eq. 2) | Minor | Low (notational) | Low | Easy | 4f40dc10 |
| 9 | Related work is flat list, not comparative | Minor | Low (organizational) | Low (improves positioning) | Medium | 1c6fa1bd |
| 10 | Conclusion lacks synthesis | Minor | Low (presentational) | Low | Easy | e03b8eb3 |

### Key Issue 1 (Critical): No variance reporting
**Evidence:** Tables 1-4 report single-point estimates only. The main claim is that "multisensory multi-task method consistently outperforms" alternatives. Without standard deviations from multiple runs, a 0.6% improvement (99.3% vs 98.7% on gesture classification) could be within noise range.
**Required Action:** Re-run all experiments with ≥3 random seeds and report mean±std. Add paired significance tests (e.g., Wilcoxon signed-rank) comparing multisensory multi-task against the strongest baseline for each task. Add an Appendix table with full per-seed results.

### Key Issue 2 (Critical): Undefined "fix-8" dataset
**Evidence:** Page 7, Section 4.2: "We chose the fix-8 dataset as the target." This term appears nowhere else in the paper.
**Required Action:** Define fix-8 explicitly: which datasets compose it, sample counts per task/modality, and why it was selected for transfer evaluation. State whether the zero-shot model saw those modalities/tasks during training or only the task combinations are novel.

### Key Issue 3 (Major): Missing reproducibility details
**Evidence:** Section 4.1 and Appendix B describe architectures only as "CNNs for images" and "RNNs for sequential data." Modality-specific preprocessing, data splits, and alignment procedures are absent.
**Required Action:** Add a comprehensive Appendix table mapping each of the 12 modalities to: exact architecture name, input dimensionality, architecture hyperparameters, preprocessing steps, and train/val/test split used. Specify temporal alignment method for asynchronous modalities.

### Key Issue 4 (Major): Causal over-attribution
**Evidence:** Page 6: "This can be attributed to their ability to integrate information across modalities and tasks." No ablation disentangles fusion benefit from increased parameter count or other confounds.
**Required Action:** Add a controlled ablation that matches total parameter count between multisensory and unimodal baselines. Alternatively, add a "randomized modality" control where one modality's input is shuffled. Replace causal language with correlational wording ("is consistent with," "suggests that").

### Key Issue 5 (Major): Unsubstantiated "most expansive" claim
**Evidence:** The phrase appears in Abstract, Section 2, and Conclusion. No comparison table against existing IoT/multimodal benchmarks is provided.
**Required Action:** Either add a benchmark comparison table (dimensions: # modalities, # tasks, # samples, sensor types, etc.), or downgrade the claim to "to our knowledge, the largest assembled IoT benchmark" and cite the next-largest benchmarks explicitly.

## Actionable Suggestions
The following suggestions are ordered by impact. Each includes the target section, the concrete problem, and the required revision action.

### S1. Add variance and significance testing to all results (Must, Critical)
**Target:** Tables 1-4 and Section 4.2.
**Action:** Re-run every experiment with 3 random seeds. Report mean ± standard deviation in all tables. Add a paired significance test (e.g., Wilcoxon signed-rank or paired t-test) comparing multisensory multi-task against the strongest baseline for each task. Add a sentence in Section 4.2: "All results are reported as mean ± std over 3 random seeds. Bold indicates p < 0.05 against the best non-multisensory-multitask baseline (paired Wilcoxon)."
**Expected benefit:** Makes the main claim statistically grounded and falsifiable.

### S2. Define fix-8 dataset for zero-shot experiment (Must, Critical)
**Target:** Section 4.2, Table 4, Page 7.
**Action:** Add a paragraph or appendix subsection defining fix-8. Include: (a) which constituent datasets and data splits compose it, (b) sample count per task/modality, (c) which modalities/tasks the pre-trained model has vs has not seen during training, (d) the exact zero-shot evaluation protocol. Alternatively, rename the experiment to avoid the opaque "fix-8" term and use explicit dataset/task names.
**Expected benefit:** Makes the zero-shot experiment reproducible and interpretable.

### S3. Document full reproducibility details (Must, Major)
**Target:** Section 4.1 and Appendix B (Pages 18-19).
**Action:** Create a comprehensive Appendix table with columns: Task | Dataset Source | Original Split Used | Input Modalities | Preprocessing (resize, normalization, windowing) | Architecture per Modality | Encoder Parameters | Number of Seeds. Also specify temporal alignment for asynchronous sensor data (e.g., "IMU at 60Hz was downsampled to match camera frame rate at 30fps via averaging over 2-frame windows").
**Expected benefit:** Enables exact reproduction and fair comparison by the community.

### S4. Add controlled ablation for fusion benefit (Must, Major)
**Target:** Section 4.2, new subsection after Table 1.
**Action:** Add a "matched-parameter control" experiment where the multimodal model's total parameter count is matched to the unimodal model (by reducing encoder width/depth). Also add a "modality randomization" control where one modality's input is shuffled while keeping all other factors fixed. Report which tasks benefit most from which modalities.
**Expected benefit:** Separates the effect of additional input data from the effect of larger model capacity, enabling causal claims about fusion.

### S5. Add benchmark comparison table (Must, Major)
**Target:** Section 2 or Related Work (Page 9).
**Action:** Create a table comparing MULTIIOT to existing multimodal and IoT benchmarks (MultiBench, MME, MultiInstruct, VTAB, etc.) along dimensions: # modalities, # tasks, # samples, sensor types, IoT-specific challenges covered, public leaderboard. If the paper claims to be "the most expansive," it must provide transparent evidence.
**Expected benefit:** Grounds the novelty claim in verifiable evidence.

### S6. Quantify noise/heterogeneity experiments (Must, Major)
**Target:** Section 4.3 (Pages 7-8), Figure 3.
**Action:** For the long-range experiment, report the exact performance at each truncated length (e.g., 25, 50, 100, 200, 300 steps) in a supplementary table. For the noise experiment, specify noise distribution parameters (σ values), which modalities were noised, and the exact performance drop for each method. Replace "marked decline" with "performance dropped from 87.5% to 62.3% at σ=1.0."
**Expected benefit:** Converts qualitative observations into actionable empirical findings.

### S7. Rewrite "collected" to "aggregated/compiled" (Nice-to-have, Minor)
**Target:** Section 2.2, Page 3.
**Action:** Replace "We collected diverse data from IoT devices" with "MULTIIOT aggregates data from 12 publicly available IoT sensor datasets." Add an explicit statement: "No new data was collected; our contribution is the unified format, standardized preprocessing, and evaluation protocol."
**Expected benefit:** Honest framing increases credibility.

### S8. Fix adapter model notation (Nice-to-have, Minor)
**Target:** Page 5, Equation (2).
**Action:** Replace Eq. (2) with a textual description of the adapter architecture: "For each transformer layer l, we insert a bottleneck adapter $A_l$ after the feedforward sublayer: $h'_l = h_l + \text{ReLU}(h_l W_{\text{down}}) W_{\text{up}}$. Only $W_{\text{down}} \in \mathbb{R}^{d \times r}$ and $W_{\text{up}} \in \mathbb{R}^{r \times d}$ are trainable."
**Expected benefit:** Accurate representation of standard adapter design.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current manuscript follows this arc:
1. **Introduction P1:** IoT is important (generic)
2. **Introduction P2:** IoT data poses challenges (generic)
3. **Introduction bullet list:** Two contributions (benchmark + baselines)
4. **Section 2-3:** Benchmark details (modalities, tasks, modeling approaches)
5. **Section 4:** Experiments and results
6. **Section 5:** Related work
7. **Section 6:** Conclusion

**Issue:** The introduction does not establish a clear research gap before presenting the solution. It opens with broad IoT enthusiasm ("unprecedented surge") and examples, but does not identify what specific limitation in prior work MULTIIOT addresses. The contribution bullets appear before the reader understands why a new benchmark is needed. The title is method-focused ("MULTIIOT") rather than problem-focused, making it harder for readers to quickly assess relevance.

### Proposed Storyline (Recommended)

Arc: **Big Picture → Specific Gap → Solution → Evidence → Impact**

**Title:** "MULTIIOT: A Unified Benchmark for Multisensory Representation Learning on the Internet of Things"

**Abstract Outline (5-sentence plan):**
- **S1 (Problem):** IoT generates diverse sensor data (IMU, thermal, depth, audio, video) for real-world tasks in health, automation, and smart cities.
- **S2 (Gap):** Existing IoT ML research is fragmented across individual datasets and task-specific methods, lacking a unified benchmark for reproducible cross-modal comparison.
- **S3 (Solution):** We introduce MULTIIOT, a benchmark aggregating 1.15M samples across 12 modalities and 8 tasks from public IoT datasets, with standardized evaluation splits and baseline implementations.
- **S4 (Key Result):** Systematic evaluation of six modeling paradigms shows multisensory multi-task models consistently outperform unimodal baselines (e.g., 93.8% vs 88.0% on touch classification), but performance degrades substantially under longer sequences and sensor noise.
- **S5 (Impact):** MULTIIOT reveals three open challenges—high-modality fusion, long-range temporal modeling, and sensor heterogeneity—providing the community with a foundation for future research.

### Introduction Paragraph-by-Paragraph Plan

**P1 (Big Picture):** Start with a concrete, domain-grounded statement about a real IoT problem, not "unprecedented surge."
*Target claim:* IoT sensor data is abundant and diverse, but this diversity creates an opportunity and a challenge.
*Evidence anchor:* Cite specific real applications where multiple IoT sensors are needed (health monitoring with wearables, autonomous driving with cameras+LIDAR+GPS).
*Transition:* "However, research on ML for IoT remains fragmented..."

**P2 (Gap):** Identify the specific fragmentation problem.
*Target claim:* Current IoT ML papers each use different datasets, modalities, and evaluation protocols, making progress hard to track and methods hard to compare.
*Evidence anchor:* Cite a few representative works (DIP-IMU, EyeMU, TouchPose) and note that they cannot be compared due to different datasets and metrics.
*Transition:* "To address this gap, we propose MULTIIOT..."

**P3 (Solution):** Present the benchmark and its design principles.
*Target claim:* MULTIIOT unifies 12 modalities and 8 tasks under a common evaluation framework.
*Evidence anchor:* Summarize statistics (1.15M samples, 12 modalities). State that it aggregates existing data (transparently).
*Transition:* "We validate MULTIIOT through a systematic empirical study..."

**P4 (Evidence Preview):** Summarize key findings concisely.
*Target claim:* Multisensory multi-task models work best, but current architectures still struggle with long sequences and sensor noise.
*Evidence anchor:* Preview one or two numbers from Table 1.
*Transition:* "Based on these findings, we identify three open challenges..."

**P5 (Contribution List):** State contributions explicitly.
*Target:* Three clear contributions: (1) MULTIIOT benchmark, (2) empirical findings about multisensory IoT learning, (3) identified open challenges.

### Alternative Storyline Option: Problem-Paradigm-Evidence

**Title:** "Benchmarking Multisensory Learning for IoT: The MULTIIOT Suite"

This arc leads with the benchmark as a scientific instrument:
- **P1:** State that evaluating multisensory IoT methods requires a standardized benchmark (framed as a missing scientific instrument).
- **P2:** Describe the benchmark design (what modalities/tasks, why these choices).
- **P3:** Report baseline results and what they reveal about multisensory learning.
- **P4:** Discuss open challenges as hypotheses for future work.

This option works better if the paper's primary contribution is positioned as a resource/benchmark rather than new scientific findings.

### Alignment Checks for Recommended Storyline

- **Problem alignment:** The gap (fragmented evaluation) matches the solution (unified benchmark).
- **Variable alignment:** Modalities and tasks introduced in Section 2 match those evaluated in Section 4.
- **Contribution-evidence alignment:** The claim that multisensory multi-task models are better is directly evidenced by Table 1, though variance is missing (see Key Issues).

The recommended storyline improves reader comprehension by establishing "why a new benchmark" before presenting "what the benchmark contains." It also sets realistic expectations by transparently stating the data is aggregated from existing sources.

## Priority Revision Plan
The plan below is ordered by impact on paper quality and publication readiness. Each item is labeled P0 (pre-submission critical), P1 (highly recommended), or P2 (quality improvement).

### P0 Items (Must fix before resubmission)

| # | Task | Effort | Impact | Related Weakness |
|---|------|--------|--------|-----------------|
| P0.1 | Re-run all experiments with 3 seeds, add mean±std and significance tests to Tables 1-4 | 3-5 GPU-days | High: makes core claim testable | W1 |
| P0.2 | Define fix-8: add dataset composition, sample counts, and zero-shot protocol description | 1 day (writing) | High: makes transfer experiment reproducible | W2 |
| P0.3 | Add train/val/test split documentation, preprocessing details per modality, and exact architectures to Appendix | 2-3 days | High: enables reproduction and fair comparison | W3 |
| P0.4 | Add matched-parameter control ablation to separate fusion benefit from capacity increase | 2-3 GPU-days | High: supports causal interpretation | W4 |
| P0.5 | Add benchmark comparison table (MULTIIOT vs MultiBench, MME, etc.) | 1 day (literature + writing) | Medium: grounds superlative claims | W5 |

### P1 Items (Highly recommended)

| # | Task | Effort | Impact | Related Weakness |
|---|------|--------|--------|-----------------|
| P1.1 | Quantify noise and long-range experiments with exact numbers and noise parameters | 1-2 days (re-analysis + writing) | Medium: converts qualitative→quantitative | W6 |
| P1.2 | Rewrite "collected"→"aggregated" throughout, add transparency statement | 0.5 day | Medium: honest framing | W7 |
| P1.3 | Restructure Introduction to Big Picture → Gap → Solution → Evidence → Contributions | 1 day (rewriting) | Medium: improves narrative | Storyline |
| P1.4 | Restructure Related Work around comparison axes; add benchmark comparison table | 1 day | Medium: improves positioning | W9 |

### P2 Items (Quality improvement)

| # | Task | Effort | Impact | Related Weakness |
|---|------|--------|--------|-----------------|
| P2.1 | Fix adapter model Eq. (2) notation | 0.5 day | Low: accuracy | W8 |
| P2.2 | Rewrite Conclusion to synthesize findings (specific numbers, open challenges) | 0.5 day | Low: presentation | W10 |
| P2.3 | Expand broader impacts with MULTIIOT-specific bias/privacy analysis | 1 day | Low: completeness | — |

### Revision Timeline (Recommended)

- **Week 1 (P0):** Add seed variance (P0.1) + matched-parameter control (P0.4). While experiments run, write fix-8 definition (P0.2) and split documentation (P0.3).
- **Week 2 (P0+P1):** Analyze noise/heterogeneity quantitatively (P1.1). Add benchmark comparison table (P0.5). Restructure Introduction (P1.3) and Related Work (P1.4).
- **Week 3 (P2+Polish):** Fix notation, rewrite Conclusion, expand broader impacts. Final proofread and consistency check.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 | Benchmark 6 modeling paradigms on 8 tasks (Table 1) | All 8 tasks, 6 model types, single run each | Task-specific (see Section 4.1) | Multisensory multi-task best on all tasks | Multisensory fusion + multitask beneficial | No variance; confounded by capacity |
| E2 | Modality ratio ablation (Table 2) | Vary % of modalities used (25%/50%/all) | Same as E1 | Adding modalities monotonically improves performance | Multimodality helps | Which modalities matter most? Diminishing returns? |
| E3 | Task ratio ablation (Table 3) | Vary % of tasks trained jointly | Same as E1 | Multi-task improves or maintains performance | Multi-task learning beneficial | No per-task interaction analysis |
| E4 | Zero-shot/few-shot transfer (Table 4) | Pre-train on source tasks, evaluate on "fix-8" with 0/5/10/20 shots | Gaze est. (cm), Touch cls. (%) | Multimodal multitask best; few-shot helps | Transfer learning enabled by multisensory training | "fix-8" undefined; source-target overlap unclear |
| E5 | Long-range interaction test (Fig 3 left) | Truncate sequences to varying lengths | Same as E1 (subset) | Performance declines with longer sequences | Models fail at long-range dependencies | No quantitative results reported |
| E6 | Noise heterogeneity test (Fig 3 right) | Add Gaussian noise to data | Same as E1 (subset) | Performance declines with noise | Models sensitive to sensor noise | Noise parameters unspecified; only qualitative |

### Research-Theme Gap Diagnosis

1. **New Knowledge (weakly supported):** The paper's primary empirical finding (multisensory multi-task > unimodal) is known from prior multimodal work and is not surprising. The genuinely new knowledge would be: under what precise conditions does multisensory fusion break down? At what sequence length? At what noise level? For which modality combinations? These questions remain unanswered due to the qualitative analysis in E5/E6.

2. **Reproducibility/Reusability (partially supported):** The benchmark is released with code and leaderboards, which is positive. However, the lack of documentation (splits, preprocessing, architectures) severely limits reusability. Until P0.3 is completed, the benchmark cannot be used by others for fair comparison.

3. **Potential to Change Practice (moderate):** If the benchmark gains adoption, it could standardize IoT ML evaluation. However, the lack of a strong baseline suite with proper tuning and controls reduces the benchmark's credibility as a reference point.

### Proposed Research Experiments

#### P0 Experiments (Must add before resubmission)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------|-------------|-----------|---------------|--------------------|---------|------------------|-----------|--------------|
| R1 | Multisensory multi-task "consistently outperforms" | Gains are statistically significant | Re-run all E1 with 3 seeds, compute mean±std, Wilcoxon signed-rank test | Same 6 model types | Same as E1 | ≥80% of comparisons with p<0.05 | 3-5 GPU-days | High: statistical grounding of core claim |
| R2 | Fusion benefit is causal, not capacity-driven | Fusion benefit persists under matched parameter count | Reduce multisensory encoder to match unimodal total params | Unimodal (original), Multisensory (reduced), Multisensory (original) | Same as E1 | Reduced multisensory still outperforms unimodal on ≥6/8 tasks | 2 GPU-days | High: supports causal interpretation |
| R3 | Quantitative long-range degradation | Performance decays at specific thresholds | Report exact accuracy at each sequence length (25,50,100,150,200,250,300) | Single-task vs multi-task models | Same as E1 | Tabulate and identify threshold where performance drops >5% relative | 0.5 GPU-day | Medium: converts qualitative→quantitative |

#### P1 Experiments (Highly recommended)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------|-------------|-----------|---------------|--------------------|---------|------------------|-----------|--------------|
| R4 | Which modalities matter most | Modality importance varies by task | Leave-one-modality-out ablation for each task | Full multisensory vs leave-one-out | Same as E1 | Identify modality importance ranking | 3 GPU-days | Medium: actionable insight for sensor selection |
| R5 | Zero-shot transfer is reproducible | Source-target modality gap determines transfer difficulty | Define fix-8 explicitly; measure overlap | Same as E4 | Same as E4 | Documented gap between in-distribution and transfer performance | 1 day (analysis) | Medium: makes transfer experiment credible |
| R6 | Noise robustness with quantitative thresholds | Models tolerate noise up to σ threshold | Add Gaussian noise at σ ∈ {0.01, 0.05, 0.1, 0.5, 1.0} to each modality independently | Report per-modality noise sensitivity | Same as E1 | Tabulate σ threshold causing >10% degradation per modality | 1 GPU-day | Medium: practical robustness characterization |

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (This week): Retrospective fixes (P0)
├── R1: Re-run with 3 seeds + significance tests
├── R2: Matched-parameter ablation
└── R3: Quantify long-range degradation
    ↓
Stage 2 (Next week): New experiments (P1)
├── R4: Modality importance ablation (leave-one-out)
├── R5: Fix-8 definition + transfer documentation
└── R6: Quantitative noise sensitivity thresholds
    ↓
Stage 3 (Before submission): Polish and consolidate
├── Re-check all tables and figures
├── Update Introduction and Related Work
└── Final consistency and reproducibility audit
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 4.5 / 10

**Rationale (prioritizing research value + novelty):**

- **Research Value (5/10):** The benchmark addresses a genuine need for unified IoT evaluation, and the breadth of modalities/tasks is a tangible contribution. However, the lack of reproducibility-critical details, variance statistics, and the undefined zero-shot experiment significantly reduce the benchmark's immediate utility. The core finding (multisensory multi-task > unimodal) is directionally correct but not surprising given prior multimodal learning literature.

- **Novelty (3/10):** MULTIIOT aggregates existing datasets rather than collecting new data or introducing novel modeling approaches. The benchmark's novelty lies in the unification and standardization effort, which is a service contribution rather than a conceptual advance. The empirical findings about challenges (long-range, noise) are presented too qualitatively to constitute novel scientific insights. External novelty verification is deferred due to retrieval being unavailable in this run.

- **Soundness (4/10):** The experimental design has fundamental issues: no variance reporting, unsupported causal claims, missing controls (matched-parameter ablation), and qualitative analysis of key experiments. These issues directly affect the reliability of the main conclusions.

- **Reproducibility (3/10):** Missing train/val/test splits, dataset-specific preprocessing, architecture details, seeds, and the undefined "fix-8" dataset make most experiments unreproducible in their current form.

### Post-Revision Target: [6.5, 7.5] / 10

**Evidence-grounded prediction if all P0 and P1 items are completed:**

If the authors: (1) add variance and significance testing, (2) fix the "fix-8" definition, (3) document all reproducibility details, (4) add matched-parameter ablation, (5) quantify the noise/heterogeneity experiments, (6) add benchmark comparison table, and (7) restructure the narrative—the paper would achieve a score in the 6.5-7.5 range. This reflects the solid resource contribution (unified benchmark) with adequately rigorous empirical validation.

The upper bound of 7.5 is limited by the inherent nature of the contribution: it is a benchmark/resource paper rather than a novel methodological or theoretical contribution. For a paper at ICLR, benchmarks with rigorous characterization and surprising empirical findings can be strong contributions at this level.

### Score Breakdown

| Dimension | Current | Post-Revision Target |
|-----------|---------|---------------------|
| Research Value | 5/10 | 7/10 |
| Novelty | 3/10 | 5/10 |
| Soundness/Validity | 4/10 | 7/10 |
| Reproducibility | 3/10 | 8/10 |
| Presentation/Clarity | 5/10 | 7/10 |
| **Overall** | **4.5/10** | **[6.5, 7.5]/10** |