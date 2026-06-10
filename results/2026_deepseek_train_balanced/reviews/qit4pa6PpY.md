## Summary

This paper introduces an instruction-following benchmark that augments five existing knowledge QA datasets (MMLUPro, MathQA, BoolQ, PIQA, Winogrande) with 13 answer-conditioned instructions. The key idea is that by grounding instructions in verifiable knowledge-task answers, both task accuracy and instruction-following can be measured simultaneously using deterministic (LLM-free) evaluation. The paper evaluates 16 models from 1B to 405B parameters and reports that even frontier models show substantial performance drops on simple output-format instructions. A distractor (no-effect) instruction analysis is also included.

## Strengths

- **LLM-free evaluation for both task performance and instruction-following**: Table 1 demonstrates that this benchmark is among the few (alongside RuleBench) to use deterministic "Direct" evaluation rather than LLM-as-judge, avoiding the circularity of using an LLM to evaluate LLM outputs. This is a genuine methodological advantage that improves reproducibility and objectivity.

- **Simultaneous measurement of knowledge accuracy and instruction adherence**: The core design — conditioning instructions on correct answers — is clever. A single model response reveals both whether the model knows the correct answer and whether it applied the instructed transformation, enabling the study of interactions between knowledge and instruction-following that prior benchmarks (IFEval, InFoBench) do not readily support.

- **Novel distractor/no-effect instruction analysis**: The inclusion of instruction instances that should produce no change to the answer (e.g., numeric formatting applied to non-numeric answers) and the finding that models at all scales show 5–20% drops on these instances is genuinely interesting and, as the paper notes, has not been studied in the instruction-following setting before.

- **Systematic scaling study across 1B–405B parameters**: The evaluation covers 16 models across four size categories with consistent inference settings (greedy decoding, same prompt templates), enabling clean comparisons of how scale affects instruction-following precision.

## Weaknesses

### Major

1. **Zero-shot Chain-of-Thought creates a systematic confound between instruction-following and answer-extraction failures** (line 212: "In all our experiments, we perform zero-shot Chain-of-Thought (CoT) reasoning"). CoT causes models to produce extended reasoning text before the final answer. The post-processing pipeline searches for a keyword and extracts the answer after it (line 215). When the model wraps the answer in natural language (e.g., "The answer is 'eslaf'") or fails to produce the expected keyword entirely — which the paper acknowledges happens (line 217: "models may not always follow this, and can instead generate a wide range of other keywords... or no keyword at all") — the extraction fails, and the response is counted as an instruction-following failure. Critically, the paper does not distinguish between "model did not understand the instruction," "model understood but wrapped the answer in natural language," and "the regex failed to find the substring." Because CoT is used for *every* evaluation, this confound infects all reported scores. A no-CoT subset (direct answer generation) would be needed to isolate whether the observed failures are instruction-following problems or CoT+parsing artifacts. This is the most serious weakness because it directly questions what the benchmark's scores actually measure.

2. **No empirical comparison to existing instruction-following benchmarks** (IFEval, InFoBench, FoFo, RuleBench). Table 1 compares these benchmarks on conceptual dimensions, but for a benchmark paper the critical missing validation is whether model rankings on this benchmark correlate with, or differ from, existing benchmarks. Do GPT-4o and Llama-3.1-405B also rank first on IFEval? If rankings are identical, the contribution reduces to a different lens on the same capability — useful but less novel. If rankings diverge, that divergence is precisely the evidence needed to demonstrate that this benchmark captures something distinct. Without this analysis, the paper's claim of novelty remains unsubstantiated by comparative evidence.

3. **The strict metric — used as the primary measure for headline results and the benchmark ranking (Table 2) — conflates genuine instruction violations with formatting artifacts**. The paper acknowledges that strict failures include "minor copying errors, such as missing a period or comma" (line 139), and provides a loose metric (Levenshtein ≤ 2) as a complement. However, the headline claim that "models fail to follow simple instructions" and the central rankings are built on strict scores. The paper's justification — "we do not expect models to make such mistakes given clear instructions" (line 139) — is an unsubstantiated assumption, not evidence. The gap between strict and loose scores is reported and discussed (e.g., lines 249–250), which partially mitigates this concern, but the paper never quantifies what fraction of strict failures are genuine instruction violations vs. formatting imprecision. A human-annotated error taxonomy on model outputs would directly address this.

### Minor

4. **The no-effect/distractor analysis lacks a bare knowledge-task baseline**. The paper compares no-effect instruction performance against the PCA (print correct answer) baseline. However, PCA itself shows a ~20% drop from the label-answering task (line 232). Without comparing against the bare knowledge task (i.e., the model answering the question with no instruction wrapper at all), the 5–20% additional drop on no-effect instructions (line 263) could reflect the increased prompt length or structural complexity of any instruction — even a no-op one — rather than the specific content of the instruction acting as a distractor. This weakens the interpretation of a core claimed finding.

5. **The automated error classification (IFError and KnowledgeError sets, Section 3.4) is defined as a contribution but is never empirically applied in the results**. The paper describes how these sets are constructed but never quantifies how many model errors fall into each category. The only mention (line 237) references an \input'ed figure whose actual content cannot be verified in the text. For a claimed contribution (item (v) in the contributions list), the lack of executed analysis is a notable gap.

6. **No variance or uncertainty reporting**. Results are based on a single random subset of 1500 samples per dataset with greedy decoding. No bootstrap confidence intervals, no multiple random seeds, no sensitivity analysis for the random subset selection. The benchmark ranking in Table 2 reports scores to four decimal places (e.g., 0.4790, 0.5161), which implies a precision that is unwarranted without any estimate of variance. This is a standard reproducibility and rigor concern for an empirical benchmark paper.

7. **Prompt templates are not shown**. The paper states models see prompts "based on prompt guides for the original knowledge tasks in lm-evaluation-harness" (line 212) and references a keyword used for extraction (line 215), but the actual prompt template is never presented. For a benchmark whose results depend critically on prompt structure and post-processing logic, this is a reproducibility gap that should be addressed.

### Trivial

- Numerical scores reported to four decimal places in Table 2 where the underlying sampling procedure supports at most two significant digits of precision.

## Nice-to-Haves

- Running a subset of experiments without CoT (direct answer generation) would disentangle instruction-following from CoT+parsing confounds.
- Reporting per-instruction-type results (beyond aggregated categories) would be more informative since the 13 instructions vary enormously in difficulty.
- Providing human performance on a sample of the benchmark would help calibrate whether the low absolute scores (GPT-4o at 51.6%) reflect genuine difficulty or evaluation artifacts.
- Including per-dataset breakdowns more granular than what the \input'ed figures currently provide.

## Removed Points

*These are points from the inputs that were filtered out per the filtering rules; they are retained here for transparency but should not be considered part of the review.*

- **Criticism about figures being \input'ed and not visible**: Parser artifact — the original PDF contains these figures. Removed.
- **Criticism about missing appendix/content**: Parser strips appendices; they exist in the original submission. Removed.
- **Questioning RuleBench citation or existence**: Hard rule — all cited references are assumed to exist. Removed.
- **"Human study only 75 instances" as a standalone weakness**: This is a reasonable sanity check for a benchmark of this type; the scale is appropriate for its purpose (validating instruction clarity). Removed as overblown.
- **Strength Finder's claim about "automated high-precision error classification" as a core strength**: The paper defines this taxonomy but never empirically applies it — the claimed strength is aspirational rather than executed. Removed from strengths.
- **Formatting/style nitpicks (typos, whitespace, etc.)**: Parser artifacts, not author errors. Removed.
- **Generic "evaluation lacks rigor" / "baselines may not be fair" without concrete anchor**: Removed per filtering discipline.

## Novel Insights

The most interesting observation that emerges from cross-referencing the reviews is a structural tension in the paper's design: the benchmark's core innovation — grounding instructions in verifiable knowledge tasks — is elegant and genuinely useful, but the evaluation methodology (strict exact match on CoT outputs) systematically undermines the ability to attribute failures to instruction-following rather than to confounding factors. This tension is not internal to the reviews but is a real pattern visible across them: the strength of the benchmark construction is repeatedly undercut by a measurement strategy that lacks the necessary controls. The paper would be substantially stronger if it resolved this mismatch by adding targeted experiments (no-CoT condition, human error annotation on model outputs) that directly validate what its headline scores represent.

## Suggestions

1. **Run a no-CoT subset** on a representative sample of models and instructions. Report the proportion of errors that disappear when CoT is removed — this directly quantifies the CoT confound and allows clean attribution of the remaining errors to instruction-following.

2. **Conduct a human annotation study on model outputs** (not just on the instructions themselves) to classify strict-match failures as genuine instruction violations vs. formatting imprecision. Report the proportions to validate what the strict metric captures.

3. **Add empirical comparison to at least IFEval** — compute Spearman rank correlation between model rankings on this benchmark and IFEval (or InFoBench). If rankings differ, analyze the divergence to demonstrate novel coverage.

4. **Add a bare-task baseline for the no-effect analysis** — compare performance on the knowledge task with no instruction wrapper, to isolate the distractor effect from general prompt complexity.

5. **Report confidence intervals** (e.g., bootstrap over random subsets) and round scores to a precision justified by the sample size.

6. **Apply the IFError/KnowledgeError taxonomy** to model outputs and report the distribution of errors across categories — this would turn an underutilized contribution into a genuinely useful analysis.

## Score and Decision

**Score**: 5.0 — The benchmark design is clever and well-motivated, but the evaluation has two structural confounds (CoT, strict metric conflation) that weaken the central claims, and the lack of empirical comparison to existing benchmarks limits the demonstrated contribution. The paper could be strong after addressing these issues.

**Decision**: Reject (borderline, could be accepted with major revisions addressing the CoT confound and empirical benchmarking comparison)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>