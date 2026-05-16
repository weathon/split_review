Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes DIV-SE and IDIV-SE, two methods that use LLM-generated diverse reasoning "approaches" and "personas" to construct multiple prompts, then ensemble the outputs via majority voting. The core idea is to introduce diversity at the level of reasoning strategies (rather than relying on stochastic decoding) to improve accuracy without modifying the decoding process. The paper evaluates on arithmetic reasoning (AQuA, GSM8K), planning (Blocksworld), and commonsense QA using GPT-3.5, GPT-4, and LLaMA-2 70B, reporting consistent gains and Pareto-optimal cost–accuracy trade-offs.

## Strengths

1. **Large, demonstrable gains on challenging planning benchmarks**: On Blocksworld 4/5 with GPT-4, DIV-SE achieves 69.6% accuracy, substantially exceeding the zero-shot-CoT baseline of 40% and SC-10's 41.2%. On Blocksworld 3, DIV-SE reaches 94%, a 24-point improvement over the zero-shot-CoT baseline (Section 3.1.3). These are impressive results on a benchmark where prior methods have struggled.

2. **Pareto-optimal cost–accuracy trade-offs across multiple settings**: The paper systematically compares DIV-SE/IDIV-SE against CoT and self-consistency at varying ensemble sizes, showing that both proposed methods lie on the Pareto frontier in nearly every setting (Figs. 1, 3). For example, on Blocksworld 3 with GPT-4, zero-shot DIV-SE substantially outperforms few-shot SC-10 at roughly 4× lower cost. This provides concrete evidence that prompt-level diversity can be more efficient than scaling decoding stochasticity.

3. **Practical mechanism that works with T=0**: Unlike self-consistency, which requires stochastic decoding (T>0), DIV-SE and IDIV-SE operate at T=0 (Section 3, paragraph on temperature). This makes them applicable to black-box APIs and deployments where decoding parameters cannot be altered — a genuine practical advantage over methods like SC.

4. **Broad applicability across models and domains**: The methods show gains on GPT-3.5, GPT-4, and LLaMA-2 70B across arithmetic, planning, and commonsense benchmarks (Figs. 4, 5, Tables 1, 2). While gains vary, the consistent positive trend across model families and reasoning types supports the generality of the approach.

## Weaknesses

### Fatal
None.

### Major

1. **IDIV-SE mechanism is underspecified, hampering reproducibility**: The paper states that IDIV-SE "combines n approaches within the same prompt and aggregates the n resulting outputs" (Section 2.2) and visualizes this in Fig. 2, but never explains the crucial details: how does a single prompt with multiple demonstrations produce *n* distinct outputs? Is the LLM instructed to generate solutions for each approach sequentially within one response (and then the output is parsed)? Or is the same prompt called n times (which would defeat the "in-call" purpose)? The error propagation analysis (Section 3.3.1) mentions "generations of earlier approaches" and "subsequent approaches," suggesting the LLM autoregressively produces answers for each approach in a single generation — but this is never explicitly stated, the prompt template is not shown, and the parsing procedure is not specified. Without this information, IDIV-SE's results cannot be reliably reproduced or interpreted. The DIV-SE method (multiple separate calls with different prompts) is clearer, but IDIV-SE is claimed as a contribution.

2. **No ablation isolating diversity from demonstration count**: The paper's central claim is that *diversity of thought* (different reasoning approaches) drives improvement. However, the comparison is against standard CoT (single demonstration set) and SC (same prompt, stochastic decoding). There is no control where the prompt includes the *same number of demonstrations* but all following the *same approach*. The observed gains could therefore stem from having more in-context examples, better phrasing from style transfer, or other artifacts — not necessarily from diversity of approaches. This is a fundamental evidential gap for the paper's main thesis. A simple ablation (e.g., multiple copies of the same demonstration vs. diverse demonstrations) would directly address this.

3. **Blocksworld state-of-the-art claim is not properly substantiated**: The abstract and Section 3.1.3 claim that DIV-SE "exceed[s] the highest previously reported accuracy by at least 29.6 percentage points" and achieves "state-of-the-art accuracy." The paper reports its own baselines (CoT at 40%, SC-10 at 41.2%) and shows a 29.6-point improvement to 69.6%, but it does not cite what the "highest previously reported accuracy" was in the prior literature (e.g., Valmeekam et al., 2022, 2023, or any subsequent work). Without explicit comparison to specific published numbers, the SOTA claim is unverifiable. The paper should either cite prior results with exact numbers or remove the SOTA framing.

### Minor

4. **Diversity is asserted but not measured**: The paper claims that DIV-SE/IDIV-SE produce more diverse reasoning paths than SC, but never quantifies diversity (e.g., via n-gram overlap, embedding similarity, or any other diversity metric). This makes it impossible to verify whether the methods actually differ from SC in the intended way, or whether the improvements come from an entirely different mechanism.

5. **No statistical significance or variance reporting**: All accuracy values are reported as point estimates without standard deviations or confidence intervals. Given the modest ensemble sizes (3 or 5) and the observed variability across settings, some form of variance reporting would improve the reliability of the conclusions.

6. **Key experimental details not reported**: The held-out set size used for selecting (persona, approach) pairs is not reported, nor is the number of candidate combinations evaluated (Section 2.1, Step 2). The paper states this selection is performed once (for GPT-3.5) and reused across all models, but the sensitivity of results to this selection is not explored, raising mild overfitting concerns.

7. **Cost estimation is approximate**: The paper uses an assumed conversion rate (1000 tokens ≈ 750 words) rather than reporting actual token usage (Section 3). While this is unlikely to change the qualitative conclusions, it makes the cost-accuracy comparisons less precise than they could be.

8. **LLaMA-2 experiments use 8-bit quantization**: The paper notes using "8-bit quantization" for LLaMA-2 70B (Table 2 caption) without discussing how quantization might affect the results, especially in the zero-shot setting where gains are negligible.

9. **Error propagation methodology has clarity issues**: The error propagation analysis (Section 3.3.1) is described as "if the LLM generates the same outcomes as in the original session within 3 attempts." Since all methods (except SC) use T=0, "within 3 attempts" is confusing — with a fixed prompt and T=0, all attempts would be identical. The paper should clarify the temperature setting used in this test and why multiple attempts are relevant.

### Trivial
None.

## Nice-to-Haves

- An ablation that controls for demonstration count while varying diversity (as described in Major weakness 2) would directly support the paper's core claim.
- Explicit comparison to published Blocksworld results from Valmeekam et al. or other follow-up work.
- A quantitative diversity analysis (e.g., embedding similarity of generated reasoning chains across methods).
- Reporting standard deviations for the main accuracy results.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Criticism that the error propagation test is logically flawed due to T=0 determinism** (Harsh Critic, Section-by-Section, item on Section 3.3.1): The reviewer wrote "With T=0, runs are deterministic, so the test… should always yield the same result. The fact that it sometimes does not suggests either non-determinism or a misunderstanding." This misunderstands the test: the comparison is between *different prompts* (the chained IDIV-SE prompt vs. separate per-approach prompts), which would produce different deterministic outputs. The "3 attempts" is indeed confusing, but the core logic of the test is sound. The criticism is removed as a misunderstanding.

2. **Criticism that the paper does not test whether baseline prompt alterations affect performance on Blocksworld** (Harsh Critic, Section-by-Section, item on Section 3.1.3): The paper states "For the baseline runs, we introduce minor alterations to the prompt" (Section 3.1.3), indicating the baselines used the same modified prompt. The concern about unfair confounding is inflated since both baselines and proposed methods share the same prompt modifications.

3. **Criticism that temperature choice (T=0 for proposed methods) is not discussed** (Harsh Critic, Section-by-Section, item on Section 3): The paper explicitly states this design choice ("For all other approaches, we set T=0") and the rationale for operating without modifying decoding is stated in the introduction. The reviewer's suggestion to try T>0 is a reasonable extension question but not a weakness of the current paper.

4. **Strength Finder's claim about "consistent gains across multiple models and reasoning domains"**: This is inflated — gains on CommonsenseQA are modest, and Blocksworld on GPT-3.5 shows zero improvement. The strength is demoted to a qualified observation.

5. **Strength Finder's claim about error propagation analysis "validating that chaining diverse prompts does not significantly harm output quality"**: The error propagation methodology has clarity issues (Minor weakness 9), so this claimed strength is overstated and has been removed.

## Novel Insights

The reviews surface two key points beyond the paper's own contributions. First, the inability to isolate whether diversity of *approaches* versus simply having *more demonstrations* drives the gains points to a broader methodological challenge in the prompting literature: many proposed "novel" prompting strategies may derive gains from increased example count or prompt length rather than their claimed mechanism. Second, the IDIV-SE underspecification issue illustrates that even simple-seeming "in-call ensembling" ideas require precise specification — does the model generate one merged output or multiple parallel outputs within one response? This distinction matters for both interpretation and reproducibility, and many prompting papers are similarly vague on such procedural details.

## Suggestions

1. **Clarify the IDIV-SE mechanism**: Provide the exact prompt template and an example output with parsing logic. Show how n answers are extracted from a single generation. This is a prerequisite for reproducibility.

2. **Run a control ablation**: Include an experiment where the prompt includes multiple copies of the *same* demonstration (or demonstrations following the same approach) at the same count as DIV-SE. If the diverse approaches still outperform this control, the diversity claim is supported; if not, the gains are attributable to demonstration count.

3. **Provide explicit SOTA comparisons**: Cite the specific accuracy numbers from prior Blocksworld work (Valmeekam et al., 2022, 2023, or subsequent methods) alongside DIV-SE results to substantiate the SOTA claim, or remove the claim.

4. **Quantify diversity**: Report a simple diversity metric (e.g., embedding similarity of reasoning chains) for DIV-SE, IDIV-SE, and SC to verify that the methods introduce reasoning-level diversity beyond stochastic decoding.

5. **Add variance estimates**: Include standard deviations or confidence intervals for the main accuracy results, particularly for smaller ensemble sizes.

## Score and Decision

This paper tackles a well-motivated problem — introducing diversity at the prompt level rather than relying solely on decoding stochasticity — and demonstrates practically meaningful gains on challenging benchmarks, especially Blocksworld. The Pareto-frontier analysis is thorough and supports the claim that prompt-level diversity can improve the cost-accuracy trade-off. However, the paper has three significant gaps: (i) the IDIV-SE mechanism is underspecified to the point of being hard to reproduce, (ii) the core claim about "diversity of thought" is not isolated from alternative explanations (more demonstrations, better phrasing), and (iii) the SOTA claim on Blocksworld is not properly benchmarked against published prior work. These are all addressable with clarifications and additional controls. The overall contributions — the DIVERSEPROMPTING approach, the empirical results, and the cost-accuracy analysis — are valuable and likely to be of interest to the community.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>