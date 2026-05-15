Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces ToRA (Tool-integrated Reasoning Agents), a series of fine-tuned language models that interleave natural language reasoning with program-based tool use (computation libraries, symbolic solvers) for mathematical problem solving. The authors (1) curate 16k interactive tool-use trajectories from GPT-4, (2) train models via imitation learning on these trajectories, and (3) propose *output space shaping* — augmenting training data with self-sampled valid trajectories and teacher-corrected invalid ones. ToRA achieves state-of-the-art results among open-source models across 10 mathematical reasoning datasets, with 13–19% absolute improvements over prior work. ToRA-Code-34B is the first open-source model to exceed 50% on MATH (50.8%), competitive with GPT-4's code-based solving (51.8%).

## Strengths

- **Core contribution — interleaved format — is convincingly validated.** The format ablation (Fig. 4) isolates the benefit of interleaving rationale and code from confounds like data quantity or output space shaping. With LLaMA-2, Tool-integrated reasoning outperforms Rationale-only by 29.0% absolute and Program-only by 6.7% on MATH; with GPT-4, the improvements are 19.1% and 9.8%, respectively. This clean comparison directly supports the paper's central claim that interleaving natural language with tool use is synergistic.

- **Output space shaping provides consistent, non-trivial gains.** The ablation (Fig. 5) shows 3.4–4.0% average absolute improvements across GSM8k and MATH, with the correction component adding up to 4.5% benefit over sampling alone (without using more training data). Critically, the gains hold at all scales, including the 70B model (47.3% → 49.7% on MATH), showing the technique is not merely compensating for small model capacity.

- **Extensive and rigorous evaluation across 10 datasets.** The paper compares against multiple strong baselines (WizardMath, Platypus-2, RFT, Toolformer, GPT-4, PaLM-2, Claude-2) on tasks spanning basic arithmetic to competition-level MATH, including out-of-distribution generalization (TabMWP, ASDiv). The margins over prior open-source models are large (13–19% absolute), and the OOD results are particularly compelling — e.g., ToRA-70B achieves 74.0% on TabMWP while WizardMath-70B underperforms the base LLaMA-2-70B (49.8% vs. 57.5%).

- **Informative analysis of tool-use behavior and failure modes.** The library usage analysis (Fig. 6) reveals distinct tool-use patterns across mathematical sub-domains (e.g., sympy for algebra, algorithms for number theory). The manual error analysis (Tab. 3) identifies that reasoning errors (38%) dominate over tool-related issues (28%), providing concrete direction for future improvements.

- **Practical contribution with low overhead.** The models achieve fast inference (avg. 1.02 tool interaction rounds per problem), and the training pipeline is clearly described with reproducible details.

## Weaknesses

### Fatal
None.

### Major

- **No statistical uncertainty quantification for any experimental result.** All accuracies are reported as point estimates with no confidence intervals, variance, or repeated runs. While many margins are large (13–19% absolute), several close comparisons exist (ToRA-Code 34B vs. GPT-4 Code on MATH: 50.8% vs. 51.8%; ToRA-7B vs. some baselines on individual datasets). The reader cannot assess whether the reported gains are reliable or could reflect single-seed noise. This is particularly relevant because the core quantitative claims (SOTA results, improvement magnitudes) rest entirely on these point estimates. The field standard is evolving, and while single-run evaluation was once the norm, the lack of any uncertainty characterization is a meaningful methodological gap.

### Minor

- **Teacher model for output space correction is trained on the same data distribution as the student.** The teacher (CodeLLaMA-34B) is trained on the same 16k GPT-4 trajectories (Data) used for imitation learning. This means the "correction" step can only re-express patterns already present in Data (albeit with the capacity advantage of a larger model or different prefix completions). While the ablation shows that correction provides additional gains over sampling alone (Fig. 5), the mechanism is not fully isolated — it is unclear whether these gains come from genuinely new reasoning paths, simple error fixing on arithmetic, or increased exposure to more training examples. The paper would benefit from an analysis of what the corrected trajectories actually contribute in terms of structural diversity (e.g., different equation forms, different solution strategies).

- **16.9% of MATH training questions lack annotated trajectories (83.1% annotation success rate).** The paper does not analyze whether these omitted problems are systematically harder or belong to specific sub-domains, which could bias the training distribution. A per-topic breakdown of annotation failures would clarify whether certain types of problems (e.g., Geometry with diagram descriptions) are systematically underrepresented.

- **Error analysis (Tab. 3) aggregates across model sizes and datasets.** The manual annotation of 100 trajectories is informative but combines all model scales and topics into a single breakdown. Since error patterns likely differ substantially between, say, a 7B model and a 70B model (smaller models may have more syntax/runtime errors, larger models more reasoning errors), the aggregate numbers have limited diagnostic value. A breakdown by model scale would be more actionable.

- **Headline comparison to GPT-4 CoT is presented without qualification.** The abstract and introduction frame ToRA-Code-34B's 50.8% on MATH as "significantly outperform[ing] GPT-4's CoT result (42.5%)." While factually correct, this comparison conflates a system-level advantage (tool execution) with a modeling one — GPT-4 CoT uses no external tools, while ToRA does. The ablation in Fig. 4 controls for this, but the headline framing could mislead. This is a presentation concern rather than a methodological one.

### Trivial
None significant.

## Nice-to-Haves

- **Repeated runs or bootstrap confidence intervals** for the main results (at least on MATH and GSM8k) would substantially strengthen the paper's quantitative claims.
- **Characterization of corrected trajectories** (e.g., n-gram overlap, edit distance to existing valid trajectories) to clarify whether correction adds structural diversity or merely fixes arithmetic errors.
- **Per-topic breakdown of GPT-4 annotation failures** on MATH to assess potential distributional bias.
- **Error analysis broken down by model scale** (7B vs. 34B vs. 70B) for more targeted insights.
- **Concrete examples** showing the teacher's correction of an invalid trajectory, illustrating how the completion differs from existing valid trajectories.

## Removed Points

- **Missing baselines (ART, AutoGen, ReAct with code execution):** These are prompting/multi-agent frameworks, not fine-tuned models. The paper's contribution is a trained model, and the comparison set already includes the most relevant tool-use baselines (Toolformer, PAL, GPT-4 with code). Demanding comparison with prompting-only frameworks for a fine-tuning paper is scope creep.

- **Criticism that teacher correction may not add "novel reasoning structure":** This concern is valid in principle, but the critic overstates it as a methodological gap. The ablation (Fig. 5) shows correction provides consistent gains, which is empirical evidence that something useful is happening — whether it's "novel structure" or simple error correction. The criticism is retained as a Minor weakness (see above) but in weakened form.

- **Criticism about "conflating system-level advantage with modeling one" in the GPT-4 comparison:** The paper does not claim a modeling advantage — it compares system-level results, which is standard practice. The ablation in Fig. 4 provides the format-controlled comparison. The critic's point is a framing concern, retained as a minor weakness above.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface genuinely novel observations that the authors have missed. The most interesting point to emerge is the tension between the paper's strong empirical results and the lack of formal statistical guarantees — a pattern common to many LLM papers of this era that raises broader questions about evaluation rigor in the field. The error analysis finding that reasoning errors (38%) dominate over tool-use errors (28%) is worth emphasizing: it suggests that future improvements may depend more on better reasoning architectures than on better tool integration per se.

## Suggestions

1. **Add confidence intervals or repeated runs** for the main results on MATH and GSM8k. Even 3 runs with different seeds would substantially strengthen the quantitative claims, particularly for close comparisons. Bootstrap sampling from the test set could also provide uncertainty estimates without retraining.

2. **Analyze what the correction component actually contributes.** A simple analysis comparing the edit distance or solution-structure overlap between corrected trajectories and existing valid ones would clarify whether correction adds diversity or merely fixes surface-level errors. This would significantly strengthen the output space shaping argument.

3. **Provide a per-topic breakdown of annotation failures** for MATH to rule out distributional bias in the training data.

4. **Break down the error analysis by model scale.** This is low-effort (just disaggregate the existing 100 samples by model size) and would make the error patterns more actionable.

## Score and Decision

The paper makes a clear, well-validated contribution — the interleaved format for tool-use reasoning — and supports it with extensive experiments, carefully controlled ablations, and thoughtful analysis. The main weaknesses are the absence of statistical uncertainty quantification and the incomplete isolation of the correction component's mechanism, but neither undermines the core claims. The results are strong enough (large margins across 10 datasets, consistent ablations) that the lack of confidence intervals is a presentation gap rather than a validity threat.

**Originality:** Good — the interleaved format is a natural but underexplored idea, and the output space shaping method is novel.
**Quality:** Strong empirical work with clean ablations, though the lack of variance reporting is a methodological gap.
**Clarity:** Well-written with clear figures and straightforward presentation.
**Significance:** High practical impact — new SOTA for open-source models on MATH, with insights that can guide future tool-use agent design.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>