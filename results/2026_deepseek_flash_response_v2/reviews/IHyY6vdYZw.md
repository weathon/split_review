## Summary

This paper introduces VisualPRM400K, a ~400K-sample multimodal process supervision dataset (the first such multimodal dataset, to the authors' knowledge), along with VisualPRM (an 8B Process Reward Model trained on this data) and VisualProcessBench (a 2,866-sample, 26,950-step human-annotated benchmark that requires detecting *all* erroneous steps, not just the first). Under Best-of-N evaluation, VisualPRM improves the performance of 3 MLLM families across 6 model scales (7B–78B) on 7 multimodal reasoning benchmarks by +3.7 to +8.9 points.

## Strengths

1. **First large-scale multimodal process supervision dataset.** VisualPRM400K (~400K samples, ~2M step labels) fills a concrete gap: prior PRM datasets (PRM800K, Math-Shepherd, OmegaPRM) were text-only. The automatic Monte Carlo pipeline follows the validated Math-Shepherd methodology, scaling it to the multimodal setting, and the dataset will be released to the community.

2. **Consistent BoN improvements across diverse architectures and scales.** Table 2 demonstrates improvements across 3 model families (MiniCPM-V, Qwen2.5-VL, InternVL2.5), 6 parameter scales (7B–78B), and 7 benchmarks. This breadth of evaluation exceeds what is typical in prior PRM work, which often tests on a single model family or domain.

3. **Well-constructed benchmark with "all-errors" annotation.** VisualProcessBench (2,866 samples; 26,950 human-annotated steps; 39 person-days of expert annotation with review/re-annotation quality control) improves over prior benchmarks (Zheng et al., 2024; Lightman et al., 2023) by requiring identification of all erroneous steps rather than only the first, which better matches modern models' reflection capabilities. The annotation quality-control procedure is sound and well-documented.

4. **PRM advantage over ORM/SC widens with more candidates.** Figure 4 shows that the gap between VisualPRM and both Self-Consistency and ORM grows as N increases from 8 to 128 (up to 4.3 points advantage at N=128 for InternVL2.5-8B). This non-trivial empirical finding supports the core argument that process-level supervision scales better with additional test-time compute.

5. **Efficient single-forward-pass inference.** VisualPRM scores all steps in one forward pass using the generation probability of the "+" token, whereas MLLM-as-a-judge requires autoregressive generation per step — a genuine practical advantage.

## Weaknesses

### Major

1. **No error bars, confidence intervals, or variance reporting on BoN results.** Tables 2, 4, and 5 report all BoN results as single points despite the inherently stochastic procedure (sampling N=8 responses at temperature 0.7 from a policy model). Without uncertainty quantification, it is impossible to assess whether observed gaps (e.g., the 1.5-point PRM-vs-ORM gap at N=8 in Figure 4) are robust or within sampling noise. This is the most significant evidential gap in the paper.

2. **No oracle/upper-bound analysis for BoN.** A standard practice in BoN evaluation is to report oracle performance — the accuracy achievable if a perfect critic selected the best among N candidates. Without this ceiling, the reader cannot contextualize whether a 5.9-point improvement on InternVL2.5-78B (Table 2) represents a critic approaching the bound or leaving substantial headroom. The paper already has the sampled responses and ground-truth correctness, making this a straightforward omission.

### Minor

3. **Threshold for PRM evaluation on VisualProcessBench is unspecified.** Line 236 states that "a step is considered correct if the probability of outputting '+' exceeds that of outputting '-' by a certain threshold," but the threshold value is not stated in the main body. If this was appendix-only, it should be in the main text for reproducibility. If the threshold was tuned per benchmark or model, the comparison against MLLMs (evaluated with a fixed prompt) would be potentially unfair.

4. **"Correct completions" in the Monte Carlo pipeline (Equation 2) are not defined.** The paper computes mc_i = num(correct completions)/num(sampled completions) but never specifies how correctness of a completion is determined (e.g., answer extraction procedure, matching rules, tolerance for equivalent expressions). This is a non-trivial detail that directly affects dataset quality.

5. **The PRM-vs-ORM comparison tests a narrower claim than advertised.** The ORM is trained from the same process-level data collapsed into a single outcome label (lines 242–267). This is a controlled ablation of supervision granularity, but the paper's claim that "PRMs consistently outperform ORMs in BoN evaluation" (line 106) is broader than what this experiment supports — a competitive ORM would typically be trained on much larger quantities of independent outcome-level data. The comparison is still informative but should be reframed.

6. **Training data derives from a single source (MMPR v1.1) and cross-contamination is not addressed.** The paper does not discuss whether problems from evaluation benchmarks (MMMU, MathVision, MathVerse, etc.) overlap with the MMPR training source, nor does it analyze whether VisualPRM might overfit to MMPR-style visual domains.

7. **No analysis of why supervising all steps outperforms early-stopping.** Table 4 shows this finding but offers no hypothesis or analysis of the mechanism. Given that prior work (Math-Shepherd, PRM800K) used early-stopping, this discrepancy warrants discussion.

### Trivial

8. **Advantage-based PRM's poorer performance is attributed to "inherent noise" as a post-hoc conjecture** (line 269) without supporting evidence.

## Nice-to-Haves

- Report oracle BoN accuracy to bound the critic's headroom.
- Add error bars (bootstrap CIs or results across random seeds) to BoN results.
- Provide and justify the threshold used in VisualProcessBench PRM evaluation.
- Include a properly trained ORM baseline on independent outcome-level data, or clearly reframe the comparison as "step-level vs. collapsed outcome-level supervision from matched data."
- Discuss potential data leakage/contamination between MMPR training data and evaluation benchmarks.

## Removed Points

These points were raised by the reviewer commentary but are removed from the main evaluation for the following reasons:

- *"First multimodal" claim as a weakness*: The reviewer flagged this as a framing risk, not a scientific flaw. The paper is the first multimodal process supervision dataset to the authors' knowledge, and this is a verifiable contribution claim. REMOVED as speculative framing concern.
- *Concerns about the "overall" column being unweighted*: The paper explicitly states (line 211) that "The overall score is the average score of the above benchmarks." This is transparent, not misleading. REMOVED.
- *Missing related works*: No external sources to verify. REMOVED by policy.
- *Formatting/style nitpicks*: REMOVED by policy (parser artifacts, not author errors).
- *Missing appendix details*: The appendix is stripped by the parser. REMOVED by policy.
- *Criticism that the ORM comparison is fundamentally unfair*: The comparison is a controlled ablation (same data, different supervision granularity), which is a valid experimental design. The issue is properly about claim scope, not fairness. Downgraded from "major methodological gap" to minor framing issue above.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no synthesis that fundamentally reframes the paper's findings.

## Suggestions

1. Add oracle BoN performance to Tables 2 and 4.
2. Report error bars (bootstrapped confidence intervals or results across random seeds) for all BoN experiments.
3. Disclose the threshold used in VisualProcessBench PRM evaluation and the procedure for setting it.
4. Clarify how "correct completions" are determined in Equation 2 (answer extraction, matching rules).
5. Reframe the PRM vs. ORM comparison to accurately describe what is tested (process-level vs. collapsed outcome-level supervision from matched data).
6. Address cross-contamination risk between MMPR training data and evaluation benchmarks.

## Calibration Summary

**Round 1 (bracketing):** Queried for papers on multimodal PRMs/datasets/benchmarks across score bands:
- Low band (<3.5): MCTBench (3.0), BenchMol (4.8 but modality representation, not relevant). These are clearly weaker papers.
- Middle band (3.5–7.5): OpenPRM (6.0), Let's Verify Step by Step (5.5), ToolComp (5.4). These are the most directly comparable.
- High band (>7.5): RM-Bench (8.0), MMIE (8.0). These are benchmark papers with near-flawless execution.

**Bracket:** 4.0–7.0 (narrowing to the upper-middle region).

**Round 2 (narrowing):** Queried within (5.0–6.5) for PRM and multimodal-reasoning papers:
- OpenPRM (6.0, accept): Similar PRM construction + evaluation focus. Comparable rigor; our paper has broader evaluation but similar missing-detail issues.
- MJ-Bench (6.0, reject): Multimodal reward model benchmark. Less directly comparable. Rejected despite 6.0 score due to limited novelty.
- MMMU-Pro (5.8, reject): Incremental benchmark. Less novel than our paper.
- ToolComp (5.4, reject): Smaller-scale benchmark. Our paper is clearly stronger.

**Final score positioning:** This paper is most comparable to OpenPRM (6.0, accept) — both have valuable contributions with real but fixable evidential gaps. The paper is stronger than ToolComp (5.4) and MMMU-Pro (5.8) in scale and novelty, and is comparable to Let's Verify Step by Step (5.5) in contribution while having better reproducibility commitments. I place the paper at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>