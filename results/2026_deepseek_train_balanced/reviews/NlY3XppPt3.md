## Summary

This paper proposes a framework for testing AI adaptability by using novel computational models with modified programming languages, instantiates this with "Wuxing" — a decimal-based computer with a modified C language — and reports qualitative results from testing 5 frontier AI models on 3 programming problems. The paper claims all models failed spectacularly, revealing fundamental weaknesses in AI's ability to adapt to unfamiliar contexts.

## Strengths

1. **Novel evaluation concept**: Testing AI on a decimal-based computer with rescaled data types (measured in decimal digits rather than bytes) and modified format specifiers genuinely tests out-of-distribution generalization beyond existing code benchmarks (HumanEval, SWE-bench, CodeForces), which all use standard architectures. The Wuxing framework is a creative instantiation of this idea.

2. **Control comparison (Case 3)**: The paper tests the same CodeForces problem on normal computers without the Wuxing context (line 179: "To determine if the frontier AI models could make similar mistakes even on normal computers"). This provides some ability to attribute failures specifically to the unfamiliar framework rather than general task difficulty.

3. **Granular failure descriptions per model**: The paper identifies specific error types — Sonnet's overflow error where `unsigned long prod = result[i] * n + carry` exceeds Wuxing's 12-digit long capacity (lines 69-71), o1-preview's cent-type overflow for loop counter n=100 when cent stores 0-99 (lines 72-73), Gemini's byte-vs-digit confusion (line 175), GPT-4o's byte-unit estimation despite explicit "decimal digits (D)" specification (line 175). This granularity is more useful than aggregate pass/fail metrics.

## Weaknesses

### Fatal

1. **Prompts explicitly omitted, making the study irreproducible** (line 79): The paper states "[Prompt about Wuxing is actually here, we omitted to save space]" for a key experiment. While Section 2 provides a preamble describing Wuxing, the exact prompt composition — including specific instructions, whether models were told about the absence of `long long`, the number of attempts allowed, and any clarifications — cannot be reconstructed. Without the prompts, the study cannot be reproduced or evaluated for fairness. This is a self-inflicted omission by the authors, not a parser artifact.

2. **Evidence insufficient for the strength of the claims made**: The paper draws sweeping conclusions — "all failed spectacularly" (line 27), "far weaker than humans" (line 229) — from exactly 3 programming problems tested qualitatively on 5 models. Results are reported only through unreadable embedded images (lines 54, 95, 168, 173, 188, 190) with no quantitative metrics: no pass rates, no accuracy numbers, no per-model scoring, no confidence intervals, no statistical tests. For a paper claiming to reveal fundamental AI weaknesses that should "improve AI," this evidence base is far too thin.

### Major

3. **No human baseline for the "far weaker than humans" claim** (line 229): The paper asserts AI is "still far weaker than humans" and that "most participants of CodeForces can solve" these problems (line 157), but conducts no human experiments. Many humans unfamiliar with a decimal-based C variant would also make overflow or type-size errors on their first attempt. Without human performance data on the same Wuxing tasks, this central comparative claim is an assertion, not a finding.

4. **Scope-claim mismatch**: Section 1 (lines 14-20) proposes an ambitious 5-point framework encompassing new computational models, modified languages, entirely new languages, virtual machines, and compilers/AI self-improvement. The experiments test only the narrowest instantiation — writing simple programs with rescaled data-type sizes in one modified C variant. The paper's conclusions are framed as testing general AI adaptability, but the evidence covers only type-size adaptation in one specific setting.

5. **Case 3 undermines the headline failure narrative**: In Case 3 (normal computers without Wuxing), 3 of 5 models produced correct programs (line 194), with complaints limited to non-optimal memory usage (e.g., 20 bytes vs. 12). This shifts the failure from "cannot solve" to "did not produce the most memory-efficient solution" — a much weaker claim that the paper does not clearly distinguish from the "spectacular failure" framing used elsewhere.

### Minor

6. **No conclusion section**: The paper ends abruptly after Future Work (Section 4.2), lacking synthesis of findings, limitations, or concrete takeaways.
7. **Discussion section (Section 4.1) is disconnected from the experiments**: The generic exposition of human problem-solving abilities (observe, analyze, adapt, invent, optimize) reads like a textbook passage and does not systematically connect to the specific model failures observed.
8. **No quantitative memory optimization analysis**: Case 3 faults models for non-optimal code but provides no actual memory footprint comparison between model outputs and human-optimized versions beyond a single byte count in the figure caption.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment comparing the Wuxing narrative framing vs. a straightforward technical description ("C variant where data-type sizes are measured in decimal digits") to isolate whether failures stem from distraction or genuine adaptation difficulty.
- Expanded problem suite covering different aspects of the Wuxing framework (format specifiers, pointer arithmetic, absence of certain operations, floating-point).
- Systematic error categorization per model per problem in a readable table.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

1. **"Conflates distinct failure types"** — The paper does describe different errors per model (overflow, byte-vs-digit confusion, cent-type overflow) with some granularity; the harsh critic overstated this. The paper partially addresses this concern to a reasonable degree.
2. **"Paper is very short"** — Formatting/style nitpick; paper length is a choice, not a contribution validity issue.
3. **"Missing related work"** — Cannot independently verify what related work exists vs. is missing, per review guidelines.
4. **"No temperature/trial settings reported"** — Trivial implementation detail routinely omitted in conference submissions.
5. **"Garbled text formatting issues"** — PDF extraction artifacts, not author errors.
6. **Strength Finder's "Table 1 and Table 2 show models failed"** — Tables are unreadable embedded images, weakening this claimed strength's evidential basis, though the text descriptions partially support the failure observations.

## Novel Insights

None beyond the paper's own contributions. The core idea — testing AI on non-standard computational models — is genuinely novel as a direction, but the review reveals standard rigor gaps (insufficient evidence, missing prompts, no human baseline) rather than surfacing any deeper observation.

## Suggestions

1. Provide full prompts for every experiment in an appendix or supplementary material — this is essential for reproducibility.
2. Add quantitative metrics (pass rates, error categories per model per problem, memory footprint comparison) in readable tables — do not rely on embedded images.
3. Include a human baseline evaluation on the same Wuxing tasks to support the "weaker than humans" claim.
4. Either scale down the claims to match the evidence (e.g., "preliminary findings suggest adaptation difficulties in one specific, narrow setting") or substantially expand the evaluation to support the current claims.
5. Add a conclusion section synthesizing findings and limitations.

## Score and Decision

The paper identifies an interesting direction — testing AI adaptability on non-standard computational models — and the Wuxing framework has some novelty as an evaluation concept. However, the execution is fundamentally flawed for a top-tier venue. Two fatal issues (omitted prompts making the study irreproducible; evidence far too thin for the strong claims) combined with major overclaims (no human baseline, scope-claim mismatch, Case 3 undermining the failure narrative) mean the paper does not meet ICLR standards. The paper reads as a preliminary finding that would benefit from substantial development rather than a completed contribution.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>