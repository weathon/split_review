Now I have a thorough understanding of the paper and can properly cross-reference all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces LEGO-EVAL, a framework for evaluating the alignment between fine-grained text instructions and synthesized 3D scenes. LEGO-EVAL decomposes instructions into individual constraints, plans tool executions (using 21 tools across environment interaction, textual reasoning, and multimodal reasoning categories), selects arguments, and validates each constraint — returning binary judgments with detailed rationales. The paper also releases LEGO-BENCH, a benchmark of 130 instructions with 1,250 constraints averaging 9.6 per instruction. Experiments show LEGO-EVAL achieves 0.81 holistic F1 (vs. 0.40 for VLM-as-a-judge) and reveals that existing 3D generation methods satisfy at most 10% of instructions holistically.

## Strengths

1. **Large, well-supported quantitative improvement over strong baselines.** Table 1 shows LEGO-EVAL (GPT-4.1) achieves 0.81 holistic F1 and 0.63 Cohen's κ, versus 0.40 F1 and 0.05 κ for the best VLM-as-a-judge. The improvement holds across multiple backbone models (GPT-4.1-mini: 0.70, Qwen2.5VL-32B: 0.64) and at both the holistic and partial levels.

2. **Explicit demonstration of multi-hop grounding failure in existing methods.** Figure 8 provides a concrete case: when a scene lacks both a flashlight and laptop, VLM-as-a-judge hallucinates their locations and orientations, SceneEval misidentifies a painting as a laptop, while LEGO-EVAL correctly recognizes the objects' absence and evaluates accordingly.

3. **Tool ablation proves multi-modal tool design is necessary.** Table 2 shows disabling any tool type degrades performance; removing Environment Interaction + Multimodal Reasoning drops holistic F1 by 24.90%, while removing Textual Reasoning drops it by 5.05%. Figure 5 confirms all three tool types are actively used across all constraint categories, making the case for the full tool suite.

4. **LEGO-BENCH captures real-world complexity that prior benchmarks underrepresent.** With 1,250 constraints spanning objects (55%), architectural components (39%), and both material/object selection (40%) and layout/placement (60%), the benchmark targets aspects (floor layout, material selection, architecture attributes) that prior work like SceneEval explicitly cannot handle (41% of LEGO-BENCH constraints unevaluable by SceneEval).

5. **Reveals a critical gap in existing generation methods.** Table 3 shows the best method (LayoutVLM) achieves only 10.0% holistic success rate. Figure 6 shows success drops to near zero for instructions with 13+ constraints — while real user descriptions average 18.2 constraints (Appendix D.2), exposing a severe limitation in current 3D scene synthesis.

6. **End-to-end automated evaluation validated against human-annotated constraints.** Table 4 shows LEGO-EVAL using automatically identified constraints differs by at most ±0.03 in success rates compared to human-annotated constraints across four generation methods, demonstrating practical usability as a fully automated evaluator.

7. **Demonstrated utility as a refinement signal.** Figure 7 shows iterative refinement with LEGO-EVAL feedback raises Holodeck's holistic success rate from 8.5% to 18.5%, outperforming both VLM-as-a-judge feedback (14.5%) and the unrefined baseline (10.5%).

## Weaknesses

### Fatal
None.

### Major

1. **The headline comparison conflates constraint decomposition with tool augmentation.** The VLM-as-a-judge baseline is given the full instruction and four scene images, then asked for a single binary judgment without any decomposition. LEGO-EVAL both decomposes constraints *and* uses tools. The 0.41 F1 gap (0.81 vs. 0.40) therefore cannot be cleanly attributed to tool augmentation—it could partly come from the simplification of evaluating individual constraints rather than the whole instruction at once. The ablation study (Table 2) keeps decomposition fixed while removing tools, showing tools do matter, but it tests only *combinations* of tool-type removals and never removes *all* tools entirely while keeping decomposition. An experiment that decomposes constraints identically to LEGO-EVAL but asks a VLM to evaluate each constraint individually without tool access would directly isolate the contribution of tools from the contribution of decomposition. This is the most significant gap in the experimental validation.

2. **The refinement experiment (Figure 7) has the same baseline limitation.** VLM-as-a-judge is used as a feedback signal on full instructions without decomposition, while LEGO-EVAL provides decomposed, tool-grounded feedback. The comparison conflates the same two factors. A VLM-as-a-judge baseline that decomposes constraints but evaluates without tools would be needed to separate the benefits.

### Minor

1. **The tool set is tied to the Unity simulator.** The paper states "these tools interact with the Unity environment" (Section 3.2), which means the framework is not immediately generalizable to other simulators or to evaluation of scenes from other rendering pipelines without re-implementing the tool backends.

2. **The ablation "w/o T + M" condition is partially confounded.** The paper acknowledges that "tools returning list of scene components are necessary for argument selection" and keeps them enabled even when "Textual Reasoning" is disabled. This makes the "w/o T" condition somewhat artificial — it removes textual reasoning tools but still provides structured component lists that are textual in nature. Clarifying which tools remain in each condition and why would improve interpretability.

3. **The ablation removing E+M drops two tool types at once.** The largest drop (24.90% F1) comes from jointly removing Environment Interaction and Multimodal Reasoning, making it unclear how much each individual type contributes. A single-tool-type removal for Environment Interaction specifically would disambiguate this.

4. **No failure-mode analysis for the 19% of errors LEGO-EVAL still makes.** The paper reports 0.81 holistic F1, meaning roughly 19% of evaluations are incorrect (false positives or false negatives). Categorizing these errors (planning mistakes, argument selection errors, tool execution issues, validation LLM errors) would help users understand remaining limitations and guide future improvements.

5. **No comparison of benchmark complexity against existing benchmarks.** LEGO-BENCH is described as more comprehensive than SceneEval (which cannot evaluate 41% of constraints), but there is no quantitative comparison of constraint density, diversity, or difficulty against other benchmarks (e.g., Holodeck scenes, ProcTHOR).

### Trivial
None.

## Nice-to-Haves

- A VLM-as-a-judge baseline augmented with constraint decomposition (extract constraints with an LLM, evaluate each independently using the same four images) to isolate the contribution of tools from decomposition.
- A simulated tool-noise experiment (e.g., injecting plausible errors into tool outputs) to test sensitivity, particularly for the Multimodal Reasoning tools that rely on VLMs.
- Reporting inter-annotator agreement for the human judgments used as ground truth (likely in the stripped appendix, but worth noting).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Tool reliability unknown / tools assumed ground truth"** — REMOVED because it misunderstands the setup. Textual Reasoning tools "retrieve textual descriptions from structured scene representations such as exact coordinates" (Section 3.2) — these are simulator ground truth, not learned detectors with error rates. Environment Interaction tools query the Unity simulator's internal state for visual info. The Multimodal Reasoning tools do use VLMs, but the paper explicitly discloses this ("Since VLMs struggle with multi-image inputs... we use LLMs and VLMs to convert images into text descriptions"). The criticism that "any tool will have false positives/negatives" does not apply to tools that query simulator ground truth.

2. **"Insufficient evidence that human judgments are reliable"** — REMOVED per instructions: the paper states "Further details on our dataset collection procedure can be found in Appendix B.2." The appendix (stripped by the parser) likely contains annotation protocols. Criticisms about missing appendix content should not factor into evaluation.

3. **"Correlation analysis does not establish causality"** — REMOVED because the paper presents Table 5 as a *correlation* analysis and does not claim causality. The text says "tool execution planning *correlates* more strongly" and "this *suggests* effective tool planning is critical" — standard tentative language for correlational evidence.

4. **"Hallucination case study is anecdotal"** — REMOVED because the paper presents Figure 8 as a case study ("Case Study." is the heading). It is explicitly illustrative, not a substitute for quantitative hallucination analysis. The value of concrete examples is widely accepted in ML papers.

5. **"Constraint types taken from Holodeck without justification"** — REMOVED. The paper explicitly grounds these in prior work: "similar to the modules in Holodeck (Yang et al., 2024b)" (Section 3.1). Adopting established taxonomies from prior work is standard practice, not a weakness.

6. **"Invalid scene curation not explained"** — REMOVED. The paper states "manually curate 130 additional scenes that intentionally do not fully satisfy the instructions" (Section 4.1.1). This level of description is standard and sufficient for the paper's scope.

7. Several minor/trivial points from the Harsh Critic's section-by-section notes (e.g., "no discussion of tool implementation cost," "130 instructions is modest") are also removed as they are generic, scope-creep, or one-size-fits-all concerns that don't threaten the core contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews raise methodological concerns but do not surface a genuinely novel observation about the problem or method that the paper itself does not contain.

## Suggestions

1. **(Required for rebuttal)** Add a controlled baseline: decompose instructions using the same LLM as LEGO-EVAL, then present each individual constraint + four scene images to a VLM for binary judgment *without* tool access. This directly isolates whether the 0.41 F1 improvement comes from tools or from decomposition alone.

2. **(Required for rebuttal)** Report the absolute F1 scores (not just deltas) for each ablation condition in Table 2, so readers can see whether even the most aggressively ablated version (w/o E+M) still outperforms the baselines.

3. Provide a breakdown of LEGO-EVAL's 19% error cases by failure type (planning, argument selection, tool execution, validation) to characterize remaining limitations.

4. Add a brief quantitative comparison of LEGO-BENCH against prior benchmarks in terms of constraint density, diversity, and coverage.

5. Clarify in Section 4.1.2 that the VLM-as-a-judge baseline evaluates the full instruction as a single query, while LEGO-EVAL decomposes — acknowledge this design difference explicitly when interpreting the 0.41 gap.

## Score and Decision

**Originality:** The decomposition + tool-augmented validation paradigm for 3D scene evaluation is novel and well-motivated. While tool-augmented VLMs exist in other domains, their application to fine-grained 3D instruction-scene alignment is new.

**Importance of research question:** Critical. Evaluating whether generated 3D scenes match fine-grained specifications is essential for training embodied agents that learn correct physics and semantics. The paper convincingly shows existing methods cannot do this.

**Claims well supported:** Mostly yes. The quantitative results are clear and large. The ablation supports the tool design. However, the main comparison conflates decomposition and tool augmentation (Major weakness 1), partially undermining attribution of the improvement.

**Soundness of experiments:** The main experiment is sound in what it measures (LEGO-EVAL vs. existing practice) but lacks a controlled decomposition-only ablation to isolate tool effects. The ablation study, end-to-end validation, and refinement experiment are well-designed.

**Clarity of writing:** Good. The four-step framework is clearly described, the tool set is well-organized, and the experimental setup is easy to follow. The case study in Figure 8 is helpful.

**Value to the research community:** High. LEGO-BENCH fills a gap in fine-grained 3D evaluation, and LEGO-EVAL provides a practical evaluation tool. The finding that existing methods fail on instructions with 13+ constraints (while real descriptions average 18.2) is an important revelation.

Score: 7.0. The paper makes a strong, well-motivated contribution with clear empirical support. The main reservation is the uncontrolled comparison (decomposition confound), which is real but does not invalidate the core results — the ablation study shows tools contribute, and the magnitude of the improvement (0.81 vs. 0.40) is large enough that decomposition alone is unlikely to explain the full gap. This is a strong paper with an addressable methodological gap.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>