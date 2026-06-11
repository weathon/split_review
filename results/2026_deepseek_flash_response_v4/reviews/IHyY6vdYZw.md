## Summary

This paper presents VisualPRM400K, the first multimodal process supervision dataset (~400K samples with ~2M step-level annotations generated via Monte Carlo sampling), VisualPRM (an 8B multimodal Process Reward Model trained on this data), and VisualProcessBench (a 2,866-sample benchmark with 26,950 human-annotated step-level correctness labels). The key empirical finding is that VisualPRM consistently improves BoN reasoning performance across all 49 combinations of 7 policy models (MiniCPM-V2.6, Qwen2.5-VL-7B, InternVL2.5 at 4 scales) and 7 multimodal reasoning benchmarks, with overall gains ranging from +3.7 to +8.9 points.

## Strengths

1. **Consistent BoN gains across all 49 (model × benchmark) entries with no negative results** (Table 2): Every single combination shows a positive delta, with several double-digit improvements (e.g., +16.9 on MathVerse-VO for MiniCPM-V2.6). This breadth rules out cherry-picking and demonstrates generalization across model families, scales, and difficulty levels.

2. **First multimodal process-supervision dataset and benchmark, filling a documented gap** (Sections 2 and 3.3): Existing PRM work (PRM800K, MathShepherd, OmegaPRM) is limited to text-only tasks. VisualPRM400K is the first multimodal dataset of its kind. Additionally, VisualProcessBench requires detecting *all* erroneous steps rather than just the first, aligning with models that have reflection/self-correction abilities. Both contributions address gaps explicitly identified in prior work.

3. **PRM outperforms ORM and SC across the full N range, with the gap widening at larger N** (Figure 4): For InternVL2.5-8B, PRM outperforms SC by 2.4 points at N=8 and 3.1 points at N=128; for MiniCPM-V2.6 the gap grows from 1.2 at N=8 to 2.7 at N=128. This escalating advantage supports the core claim that fine-grained step-level rewards are more valuable than outcome-level rewards as compute budgets increase.

4. **Computational efficiency advantage explicitly demonstrated** (Section 4.3): VisualPRM computes scores for all steps in a single forward pass by using a "+" token's generation probability as the step score, whereas MLLM-as-judger approaches require autoregressive generation per step — a concrete methodological advantage.

5. **Human annotation quality control documented in detail** (Section 3.3): 13 human experts worked 39 person-days at ~$37/person-day, annotators could skip unclear questions, and each of 10 splits had ~10% manually reviewed by the paper authors with erroneous splits sent back for re-annotation.

6. **Ablation of value-based vs. advantage-based PRM with a testable explanation** (Table 4, Section 4.3): Value-based PRMs consistently outperform advantage-based PRMs, and the paper provides a specific attribution tied to automatic data pipeline noise rather than a generic hand-wave.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Label noise from the mc_i > 0 binarization threshold with only 16 MC samples**: The process supervision labels use mc_i > 0 as the correctness threshold with 16 Monte Carlo continuations per step. A step where only 1/16 continuations (6.25%) yield a correct answer is labeled "correct." Only ~10% of steps are labeled incorrect (Section 3.1), suggesting the threshold is quite permissive. The paper reports (Section 3.2, referencing the now-stripped appendix) that trying a stricter threshold hurt PRM performance. This is consistent with two possible explanations: the specific threshold tried was inappropriate, or the labels are noisy enough that a stricter threshold removes too much signal. Either way, the dataset quality would benefit from a direct human validation study of a sample of labels.

2. **Base model for VisualPRM is not specified**: The paper states VisualPRM is an 8B multimodal PRM trained in a multi-turn chat formulation, but never states which model it is initialized from (InternVL2.5-8B? Qwen2.5-VL-7B?). This is a basic reproducibility gap. Given the authors state they will release the model, this is not fatal, but the paper text should state the base model explicitly.

3. **No error bars or variance estimates for BoN results**: BoN results depend on sampling randomness (temperature 0.7). Without confidence intervals, small differences between methods (e.g., PRM vs. ORM at 1.5 points in Figure 4) are hard to interpret as meaningful or within noise. Reporting variance would strengthen the empirical claims.

4. **Unclear how text-only benchmarks are handled**: For the text-only results (Table 5: GSM8K, MATH-500, GPQA-Diamond), it is not explained what image input (if any) is provided to VisualPRM, which is a multimodal model. A brief clarification is needed.

### Trivial
None.

## Nice-to-Haves
- A human validation study sampling a few hundred VisualPRM400K labels to evaluate the agreement of mc_i > 0 annotations with human judgments.
- An ablation comparing PRM performance when trained on VisualPRM400K vs. a version with fewer MC samples per step, to measure the marginal value of the 16-sample pipeline.
- Analysis of systematic failure cases where the PRM degrades performance.
- A brief discussion of the computational cost trade-off of BoN evaluation.

## Removed Points
- **"Headline BoN improvements conflate sampling more candidates with PRM"** — Removed because the paper properly ablates this in Figure 4 (comparing PRM vs. SC vs. ORM at the same N). Presenting Pass@1 vs. +VisualPRM as the headline result is standard practice; the controlled comparison is in the ablation section.
- **Concern about the "first multimodal" claim being invalidated by concurrent work** — Removed because the paper cannot address unpublished concurrent work, and this is a standard claim type.
- **Criticism about asymmetric comparison with MLLMs on VisualProcessBench** — Removed because it is expected behavior that a dedicated small model competes with larger prompted models; the paper does not overclaim.
- **Concern about "monocultural" training data from InternVL2.5** — Removed because the paper evaluates on MiniCPM-V2.6 and Qwen2.5-VL-7B as policy models, demonstrating transfer across model families.
- **Missing computational cost discussion for BoN** — Removed as it is outside the paper's stated scope; moved to Nice-to-Haves.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Specify the base model used to initialize VisualPRM in Section 3.2.
2. Add a brief clarification of how text-only inputs are handled by VisualPRM (e.g., blank/dummy image placeholder or architecture-specific handling).
3. Add confidence intervals or variance estimates for the main BoN results, especially in Figure 4 where methods differ by 1–2 points.
4. Consider adding a human validation study on a sample of VisualPRM400K labels to directly address the label-noise concern.
5. Briefly discuss the computational cost of BoN evaluation (N=8 responses per question) in relation to the observed gains.

## Score and Decision

**Calibration process:**

**Round 1 (Bracketing):** Searched for topically similar papers in three bands: weak (avg < 3.5), middle (3.5–7.5), and strong (> 7.5). The weak band produced papers averaging 2.33–3.25 (definitely below the current paper). The strong band produced papers at 8.0 (above the current paper). The middle band produced the most relevant anchors: OpenPRM (6.00, Accept), Let's Verify Step by Step (5.50, Accept), and ToolComp (5.40, Reject). Initial bracket: [4.5, 6.5].

**Round 2 (Narrowing):** Searched within (4.5, 6.5) for additional anchors. Identified Inference-Aware Fine-Tuning (5.67, Accept), MuirBench (5.20, Accept), MMMU-Pro (5.80, Reject), and Critique-out-Loud (5.25, Reject). Reading these confirmed the paper is stronger than MuirBench (pure benchmark, mixed reviews about superficial insights) and ToolComp (smaller benchmark, rejected), comparable to Let's Verify Step by Step (seminal dataset paper with similar reproducibility gaps, accepted at 5.50), and slightly below OpenPRM (method contribution with higher technical novelty, accepted at 6.00).

**Final score rationale:** The paper has a clear contribution (first multimodal PRM dataset and benchmark), strong empirical evidence (all 49 entries positive), and thorough ablations. Its main weakness — potential label noise from the mc_i > 0 threshold — is a real concern but does not invalidate the empirical findings, which show consistent improvements. The base-model specification gap and missing variance estimates are addressable. Comparable to the "Let's Verify Step by Step" paper (5.50, accepted), which also had reproducibility concerns but provided a valuable dataset. The paper is solid mid-range work.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>