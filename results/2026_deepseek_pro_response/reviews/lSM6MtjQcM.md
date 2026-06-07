Now I have a clear picture. Let me finalize.

**Round 1 bracket: 4.5–6.0.** The paper is clearly above MHPP (4.25, Reject) and comparable to ENAMEL (5.75, Accept), but below LiveCodeBench (6.25, Accept) and well below Spider 2.0 / CS-Bench (8.0 / 6.75).

**Round 2 narrowing:** AetherCode shares LiveCodeBench's weakness of not fully proving test case quality, but lacks LiveCodeBench's stronger evaluation design (contamination analysis, multi-task). AetherCode's distinctive problem sourcing (IOI/ICPC 2024–2025) is a real differentiator, but the paper doesn't empirically demonstrate its differential value. I'd place AetherCode at **5.5** — a borderline accept, with genuine construction strengths but insufficient evidence of benchmark value.

---

## Summary
AetherCode is a benchmark of 456 competitive programming problems sourced from premier global competitions (IOI, ICPC, NOI, USACO, CCPC) from 2024–2025, paired with expert-validated test suites constructed through a hybrid G-V Agent + human expert pipeline. The paper evaluates 17 LLMs (11 reasoning, 6 non-reasoning) and reports that the best model (o4-mini-high) achieves only 35.5% Pass@1, demonstrating substantial headroom over saturated benchmarks like HumanEval. The benchmark includes multi-dimensional categorization (10 categories, 144 sub-tags) and difficulty labels calibrated from contestant solve rates.

## Strengths
- **Problem curation from premier competitions with recent vintage.** AetherCode systematically collects problems from IOI and ICPC competitions (2024–2025 focus, 400 problems from 2024, 56 from 2025), distinguishing it from benchmarks that source from LeetCode/CodeForces. The 2024–2025 window minimizes contamination risk compared to predecessors drawing from 2011–2023. The manual PDF-to-Markdown conversion with proofreading (Section 2.1) is labor-intensive but valuable for LLM usability.
- **TPR/TNR framework for test case quality.** Reframing test suite evaluation as binary classification (Section 2.3.1) — measuring correctness via TPR and comprehensiveness via TNR — is a conceptually clean contribution that provides falsifiable quality guarantees, a departure from prior work that equated quantity with quality. The G-V Agent alone achieves 89.9% TNR; human verification brings TPR to 100% (Section 2.3.2).
- **Low model performance demonstrates genuine headroom.** Table 3 shows the strongest model (o4-mini-high) at 35.5% Pass@1 overall and only 3.8% on "Extreme" problems, with reasoning models substantially outperforming non-reasoning models. These results directly substantiate that the benchmark is far from saturated, unlike HumanEval (>90%) or LiveCodeBench (>80%).
- **Multi-dimensional categorization enabling fine-grained analysis.** The hierarchical taxonomy (10 top-level categories, 144 sub-tags) with human-calibrated difficulty segmentation enables insights such as non-reasoning models bottlenecking on Dynamic Programming and Mathematics, while o4-mini-high uniquely handles Computational Geometry (Table 4). The paper honestly caveats that category difficulty distributions (e.g., Trees) may confound comparisons.
- **Expert-in-the-loop test case pipeline with substantial human investment.** 67 competitive programming experts (Codeforces >2000, some International Grandmasters) constructed targeted test cases, and a specialized audit team (≥3 ICPC gold medals, ≥2 years problem-setting experience) performed final verification (Section 2.3.3). This layered pipeline is more rigorous than the mutation-based or crawler-reliant approaches in prior benchmarks.

## Weaknesses

### Fatal
None.

### Major
- **No cross-benchmark comparison to establish differential value.** The paper evaluates 17 models on AetherCode but never evaluates any of those models on existing benchmarks (LiveCodeBench, CodeELO, CodeContests, etc.) under comparable conditions. As a result, the reader cannot determine whether AetherCode provides rankings or insights that differ from what existing benchmarks already offer. The paper argues for AetherCode's value via Table 1's feature comparison and the low absolute scores in Table 3, but the central question for a new benchmark — does this tell us something existing benchmarks don't? — goes unanswered. This substantially weakens the paper's contribution as a benchmark paper.
- **TNR evidence is partly circular and the audit is unquantified.** Section 2.3.3 states that experts "were tasked with constructing targeted test cases specifically designed to fail the various incorrect solutions we had collected." Achieving 100% TNR on those same collected solutions is therefore close to tautological. The paper is aware of this and introduces an expert audit team that "additionally writes various incorrect and inefficient solutions to verify the comprehensiveness of the test cases" (Section 2.3.3). However, the paper provides no quantification: how many additional held-out incorrect solutions were written, across how many problems, and what TNR was achieved on those held-out solutions? Without these numbers, the headline 100% TNR claim cannot be meaningfully interpreted by the reader.

### Minor
- **Difficulty self-rating (★★★) in Table 1 contradicts the paper's motivation.** The paper's introduction argues that existing benchmarks suffer from "insufficient difficulty" (lines 17-21), yet Table 1 rates AetherCode at ★★★ — the same tier as LiveCodeBench and APPS, and strictly below CodeContests, USACO, CodeELO, and LiveCodeBench Pro (all ★★★★). The ★ scale is never defined anywhere in the paper. The actual evaluation results (Table 3) provide the real difficulty evidence, but this unresolved tension in the paper's own framing is a coherence problem.
- **Human-LLM gap is asserted but not measured.** The paper's framing — from the title through the abstract to the conclusion — centers on the claim that LLMs fall short of human performance. But no human baseline on AetherCode is ever reported. The "Extreme" difficulty category (problems no contestant solved) is used as a loose proxy, but competition conditions (time pressure, single-attempt) differ fundamentally from LLM evaluation conditions (multiple attempts, no time limit). This affects the paper's narrative framing rather than the benchmark's utility, but it is a prominent and repeated unsupported claim.
- **Pass@k estimation methodology is underspecified.** Each model is evaluated 4 times per problem, and Pass@1, Pass@2, and Pass@4 are reported (line 166-167). With only 4 total samples, Pass@4 is based on a single draw of 4 — it has high variance per problem. The paper does not specify whether it uses the unbiased Pass@k estimator from Chen et al. (2021), nor does it report any measure of variance or confidence intervals. This matters for interpreting the "exploration potential" analysis (Section 3.1), which draws conclusions from Pass@1→Pass@4 deltas.

### Trivial
- Sampling parameters (temperature, thinking budget for reasoning models) beyond max output length are not discussed.
- The paper does not address the compliance/licensing status of redistributing IOI/ICPC problem statements and test cases for an open-source benchmark.

## Nice-to-Haves
- A cross-benchmark comparison evaluating 5–6 models on both AetherCode and LiveCodeBench/CodeELO under identical conditions would be the single highest-leverage addition, directly addressing whether AetherCode surfaces differential weaknesses.
- Quantifying the expert audit (number of held-out incorrect solutions written, TNR achieved on them) would transform the TNR claim from circular to evidential.
- Either calibrating the ★ ratings with a defined methodology or removing them from Table 1 would resolve the tension with the paper's motivation.
- Adding a human baseline (even a small sample) or reframing the human-gap rhetoric to what the data actually supports.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Failure diagnosis is superficial" as a standalone major criticism.** REMOVED. The WA/TLE/RTE/CE classification is basic, but the paper does extract model-specific insights (Claude's efficiency prioritization, GLM-4.5's language non-compliance, o4-mini-high acknowledging inability) that add diagnostic value beyond aggregate scores. Not listed as a separate weakness.
- **Strength Finder: "Revealing the LLM–human performance gap" as a core strength.** MODERATED. The low performance numbers are real and valuable evidence of headroom. But characterizing this as revealing a "human gap" is unsupported without human baseline data. The strength is reframed to emphasize the headroom evidence rather than the human comparison.
- **Strength Finder: "Self-contained, open-source design" as a supporting strength.** REMOVED. While practically useful, this is a design choice rather than a novel contribution.
- **Strength Finder: "Granular failure-mode diagnosis" as a supporting strength.** REMOVED. The four-way classification (WA/TLE/RTE/CE) is standard; the model-specific findings are folded into the evaluation summary.
- **Strength Finder: "Temporal and organizational metadata" as a supporting strength.** REMOVED. This is a design feature, not a significant contribution.
- **Harsh Critic: "The fraction of problems with <50 incorrect solutions is not reported."** REMOVED. This is a specific detail already captured in the TNR circularity Major weakness.
- **Harsh Critic: "The qualitative analysis is relegated to appendix."** REMOVED. The parser strips appendices; this analysis exists in the original submission and is not a paper flaw.

## Novel Insights
The TPR/TNR framework for test suite evaluation is a genuinely useful conceptual reframing that could be adopted by future benchmark efforts — treating test suites as binary classifiers with measurable sensitivity and specificity, rather than judging them by test case count. The paper's finding that the G-V Agent alone achieves 89.9% TNR but cannot reach 100% without targeted expert annotation provides a concrete measurement of the gap between automated and expert test case generation, which could inform future work on automated test generation for code benchmarks.

## Suggestions
- Run a subset of models (e.g., o4-mini-high, Gemini-2.5-Pro, GPT-4.1, DeepSeek-V3, Qwen3-32B) on LiveCodeBench or CodeELO and report both rankings side-by-side with AetherCode rankings. This would be the most impactful addition for establishing the benchmark's differential value.
- Report the number of held-out incorrect solutions written by the audit team and the TNR on those solutions, per problem or in aggregate.
- Define the ★ difficulty scale in Table 1 or remove it to avoid the contradiction with the paper's own motivation.
- Specify whether the unbiased Pass@k estimator is used and report confidence intervals for the main results.

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| DataSciBench (BltaWJZMeR) | 3.20 | R1 | AetherCode is substantially stronger — better curation, more rigorous test cases, clearer presentation |
| MHPP (TVFVx8TUbN) | 4.25 | R2 | AetherCode is clearly stronger — larger scale, premier competition sourcing, expert-validated test cases vs 14 avg tests |
| ENAMEL (suz4utPr9Y) | 5.75 | R2 | Comparable quality. ENAMEL has more rigorous metric design; AetherCode has broader scope and better sourcing. AetherCode slightly weaker on evidence. |
| LiveCodeBench (chfJJYC3iL) | 6.25 | R1/R2 | Most directly comparable. LiveCodeBench has stronger evaluation design (contamination analysis, multi-task); AetherCode has better problem sourcing and test case methodology. AetherCode falls short on demonstrating differential value. |
| CS-Bench (fjEZ2LPceZ) | 6.75 | R2 | CS-Bench is stronger — more comprehensive scale, multilingual, but different type of benchmark (knowledge vs code generation) |
| Spider 2.0 (XmProj9cPs) | 8.00 | R1 | Clearly stronger — dramatic cross-benchmark gap (91%→17%), real enterprise data |

AetherCode is a solid benchmark construction effort with genuine strengths in problem curation (IOI/ICPC 2024–2025) and test case methodology (TPR/TNR framework, expert pipeline). However, the evaluation of the benchmark itself falls short: there is no cross-benchmark comparison to establish differential value, the TNR evidence is partly circular, and several narrative claims (human-LLM gap, ★ difficulty ratings) are unsupported. These are addressable issues, but in their current form they leave the paper's contribution insufficiently demonstrated. The paper sits between ENAMEL (5.75) and MHPP (4.25), closer to ENAMEL given the stronger problem curation and expert investment.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>