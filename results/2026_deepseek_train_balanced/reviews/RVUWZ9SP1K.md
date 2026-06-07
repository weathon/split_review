## Summary

This paper proposes ActionFiller, a framework for OS agents that uses "fill-in-the-blank" prompting to decompose long instructions into shorter, reusable subtask and action prompts. It introduces a Foresight Optimization Agent (FOA/FOM) that generates subtask prompts by blending past human experiences with flexible planning, an Action Template Agent (ATA) that categorizes action prompts into three types (executable sequences, parameterized sequences, pure text descriptions), and a CohesiveFlow agent that resolves non-executable prompts via LLM-based parameter prediction and text decomposition. The paper also introduces EnduroSeq, a 30-sample benchmark for long-horizon OS tasks, and evaluates on WindowsBench.

---

## Strengths

- **Three-tier action prompt categorization.** The paper distinguishes three types of action prompts (executable sequences, parameterized sequences, pure textual descriptions) via the Action Template Agent (Section 3.2, lines 65–67). This is a structural departure from methods that treat all predicted actions as uniformly executable, and CohesiveFlow (Section 3.3) concretely addresses types 2 and 3 through LLM-based resolution.

- **Two-pass subtask prompt generation in FOA.** The FOA first generates a subtask prompt grounded in past human experiences, then generates a separate detailed prompt without human references, and integrates both (Section 3.2, line 60). This explicitly addresses the tension between reusing reliable templates and adapting to novel contexts.

- **CohesiveFlow's closed-loop update after execution.** After each action, CohesiveFlow re-evaluates the remaining action sequence conditioned on the actual execution outcome (Section 3.3, line 76: $\hat{A}_{t+1:}=\mathcal{LLM}(S_{t},A_{1:t})$), which is a practical improvement over open-loop execution pipelines.

- **EnduroSeq's open-vs-static task taxonomy.** The benchmark's distinction between open (multi-path) and static (single-path) tasks (Section 3.3, lines 89–96) targets a meaningful dimension for OS agent evaluation that existing short-instruction benchmarks do not capture.

---

## Weaknesses

### Fatal

None.

### Major

1. **Core efficiency claim is unmeasured.** The paper's central motivation is minimizing reliance on observers/detectors to improve execution efficiency (abstract "minimizing redundant operations and enhancing efficiency"; Section 3.1 "our objective is to minimize the number of observations"; contributions list "enhances execution efficiency"). Yet the evaluation reports only Success Rate and Completion Rate. No metric for observation counts, execution time, token cost, or step counts is reported anywhere. The efficiency half of the paper's dual claim (completion + efficiency) is entirely unsupported by evidence. This is not a peripheral weakness — efficiency is the paper's stated raison d'être.

2. **No ablations of the framework's components.** ActionFiller has at least three identifiable components (FOA/FOM for subtask generation, ATA for action prompt typing, CohesiveFlow for resolution). Not a single ablation is performed. It is impossible to determine which component drives the reported improvements, whether the gain comes from any specific design choice, or whether the framework adds value over simply providing more detailed prompts to the LLM.

3. **Very small evaluation with no variance reporting.** Both WindowsBench and EnduroSeq contain only 30 samples each (Section 3.3, line 89; Section 4.2, line 115). The paper reports single-point estimates with no confidence intervals, standard deviations, or statistical tests. Given that LLM-based systems exhibit high run-to-run variance, the reported numbers cannot be assessed for reliability.

4. **No related work section.** The paper jumps from Section 1 (Introduction) directly to Section 3 (ActionFiller) — there is no Section 2 surveying prior OS agent methods (UFO, CogAgent, SeeClick, AppAgent, etc.) beyond a handful of citations dropped into the introduction (lines 16, 18, 23). Without a structured discussion, the reader cannot assess what is genuinely novel or how the approach relates to the existing landscape.

5. **Method description is underspecified for reproducibility.** The "past human experiences" and "structural memory $S\mathcal{M}$" (line 51) are the foundational knowledge source, yet the paper does not specify: how the memory is constructed, how many functions it contains, how retrieval works, or whether it is manually curated. The actual prompt templates for FOA, ATA, and CohesiveFlow are not shown. There is also a naming inconsistency: "Foresight Optimization Agent (FOA)" in the abstract (line 7) vs. "Foresight Optimization Module (FOM)" in Section 3.2 (line 25), which suggests incomplete editing.

### Minor

1. **Baseline comparison fairness is unclear.** Baselines (GPT-4o, GPT-o1, line 117) are compared against ActionFiller (which also uses an LLM, line 76: "a large language model (LLM) such as GPT4"). The paper does not specify whether the baselines are given access to the same structural memory, action space definitions, or past experiences that ActionFiller uses. The improvement could simply reflect giving ActionFiller more curated context rather than a novel framework design.

2. **EnduroSeq curation is not described.** The 30 samples are said to be "carefully curated" (line 89), but no curation methodology, validation protocol, inter-annotator agreement, or release plan is provided. This falls short of the documentation standard expected for a benchmark contribution.

3. **Single case study is anecdotal.** The case study (Section 4.4) presents one example where GPT-4 misinterprets an instruction while ActionFiller succeeds. This does not constitute systematic evidence of superiority.

4. **No discussion of limitations or cost.** The paper uses multiple LLM calls per task (FOA, ATA, CohesiveFlow). The trade-off between potentially higher LLM token costs and potentially fewer observer calls is never discussed or measured.

### Trivial

- Naming inconsistency: FOA (Foresight Optimization Agent) vs. FOM (Foresight Optimization Module). The paper should use one consistent name.

---

## Nice-to-Haves

- Reporting observation counts or execution time to substantiate the efficiency claim would significantly strengthen the paper.
- Ablations that isolate the contribution of FOA, ATA, and CohesiveFlow would clarify which design decisions matter.
- Adding confidence intervals or multiple-run statistics for the 30-sample benchmarks would help assess reliability.
- Prompt templates should be included in an appendix for reproducibility.

---

## Removed Points

The following points from the input reviews were removed per filtering criteria:

- *"The equations on line 76 appear garbled (likely a parser issue)"* — This is a PDF-to-text parser artifact, not an author error (Hard Rule: remove formatting artifacts).
- *"The line between type 2 and 3 prompts is blurry"* — Subjective; the paper does distinguish the types conceptually and provides definitions for each.
- *"Missing related works"* as in "you should have cited specific papers" — Retained as "no related work *section*" (a structural criticism about the paper's organization), not as a complaint about specific missing citations (which would violate the rule against fabricating knowledge of external references).
- *Strength Finder's claim that the paper "addressed an important problem"* — Generic/superficial praise lacking specific anchor to the paper's content.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add a Related Work section** surveying existing OS agent frameworks (UFO, CogAgent, SeeClick, AppAgent, etc.) and explicitly situating ActionFiller's contribution relative to them.
2. **Measure the efficiency claim directly.** Report the number of observer calls, execution steps, or wall-clock time for both ActionFiller and baselines. Without this, the paper's core motivation is unsupported.
3. **Perform ablations** that disable CohesiveFlow and/or the FOA to isolate which component drives the reported gains.
4. **Specify the structural memory** $S\mathcal{M}$ construction methodology (manual curation, automatic extraction, size, coverage) and include prompt templates in an appendix.
5. **Expand the evaluation** with statistical testing or multiple runs given the small (n=30) sample sizes, and describe EnduroSeq's curation protocol and release plan.

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>