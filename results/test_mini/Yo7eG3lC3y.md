Now I have sufficient calibration. Let me compose the final consolidated review.

---

## Summary

This paper introduces LEGO-EVAL, a tool-augmented evaluation framework for fine-grained text-guided 3D scene synthesis, along with LEGO-BENCH, a benchmark of 130 instructions with 1,250 human-annotated constraints. The core idea is to decompose evaluation into constraint identification, tool execution planning, argument selection, and validation, using 21 tools (environment interaction, textual reasoning, multimodal reasoning) to ground scene components. LEGO-EVAL achieves a holistic F1 of 0.81 and Cohen's κ of 0.63 against human judgments, substantially outperforming VLM-as-a-judge baselines (best F1 0.40, κ 0.05). Benchmarking four generation methods reveals that none exceed 10% holistic success rate, highlighting a major gap in current capabilities.

## Strengths

- **Large and consistent gains over strong baselines:** LEGO-EVAL's holistic F1 (0.81) more than doubles the best VLM baseline (GPT-4.1 at 0.40), and its Cohen's κ of 0.63 versus 0.05 provides compelling evidence that tool-augmented multi-hop grounding aligns far better with human judgment than standard VLM-based evaluation (Table 1).

- **Principled framework design with clear ablation support:** The decomposition into four stages (constraint identification → tool planning → argument selection → validation) is well-motivated. The ablation (Table 2) shows that each tool type contributes meaningfully: disabling environment interaction tools drops holistic F1 by 24.90%, and disabling textual reasoning drops it by 5.05%, validating the multi-modal tool design.

- **LEGO-BENCH fills a real gap:** The benchmark provides 130 fine-grained instructions with an average of 9.6 constraints each, spanning objects, architecture, layout, and materials. The disparity between partial and holistic success rates (Table 3, Figure 6) is an insightful finding — methods exceed 50% on average partial SR yet all fall below 10% holistic SR, cleanly demonstrating that current generation methods fail on complete instructions.

- **End-to-end automation validated:** Table 4 shows that automatically extracted constraints yield success rates differing by at most 0.02 from human-annotated constraints across four generation methods, supporting practical deployment without manual constraint annotation.

- **Refinement experiment demonstrates practical utility:** Figure 7 shows LEGO-EVAL used as a feedback signal improves Holodeck's holistic SR from ~8.5% to ~18.5% over 3 iterations, versus ~14.5% for VLM-as-a-judge, demonstrating downstream value beyond just evaluation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The evaluation framework requires structured scene APIs (e.g., Unity backend) and is not a general-purpose evaluator.** The 21 tools (get_object_list, get_spatial_relation, etc.) depend on a simulator that exposes structured object metadata. The paper acknowledges this in Section 3.2 ("These tools interact with the Unity environment") but the abstract and conclusion describe LEGO-EVAL as a "comprehensive evaluation framework" without qualification. The paper does not discuss what abstractions would be needed to port the framework to other scene representations (e.g., NeRF, raw meshes, ProcTHOR). Adding a sentence to the conclusion scoping this to simulators with structured APIs would resolve the issue cleanly.

2. **Figure 8 contains an apparent contradiction between the output and text.** LEGO-EVAL displays "Valid ✓" for a constraint ("The flashlight and the laptop are facing the same direction") while the caption text states "the constraint cannot be satisfied." For a binary satisfaction judgment, "Valid ✓" for a constraint that cannot be satisfied is confusing — one would expect "Invalid ✗". The accompanying text claims "all methods achieve accurate judgments," which is inconsistent unless "Valid ✓" refers to something other than constraint satisfaction (e.g., evaluation completeness). This needs clarification, though it does not affect the paper's quantitative claims.

3. **No confidence intervals or significance tests reported.** Table 1 and Table 3 report point estimates without error bars. Given the modest dataset size (260 instruction-scene pairs) and the use of LLM-based evaluation components with inherent stochasticity, bootstrapped confidence intervals would help assess reliability. This is standard practice for evaluation benchmarks and would strengthen the paper.

4. **The benchmark results in Table 3 effectively use LEGO-EVAL as the evaluator, but LEGO-EVAL's own error rate (κ=0.63) is not propagated into the benchmark conclusions.** A sensitivity analysis (e.g., what fraction of the reported sub-10% holistic SR could be explained by evaluator noise rather than generator failure) would make the conclusions more robust. However, this is a common limitation shared by virtually all papers that use automatic metrics for evaluation.

5. **Error analysis of LEGO-EVAL's own failures is absent.** With κ=0.63, LEGO-EVAL disagrees with humans on a substantial minority of cases. No confusion matrix, error taxonomy, or analysis of systematic failure patterns (e.g., small objects, ambiguous spatial language, occlusion) is provided. This would help users understand when to trust the framework and when to be cautious.

6. **The comparison of generation methods (Table 3) augments I-Design, LayoutGPT, and LayoutVLM with Holodeck for object selection, which conflates contributions.** The paper notes this in Section 4.2.1, but it limits the interpretability of individual method comparisons.

### Trivial

- The paper would benefit from a case where LEGO-EVAL itself fails (not just successes), to help readers calibrate trust.

## Nice-to-Haves

- A visualization of the tool execution plan graph for a complex instruction would help illustrate the multi-hop grounding process.
- A discussion of computational cost (number of LLM calls and total runtime per evaluation) would aid practical adoption.

## Removed Points

- Criticism about "not releasing the tool API specification" — the paper is under anonymous review; release status per se is not a valid criticism of the technical contribution. Removed per hard rule on release/availability.
- Criticism that "comprehensive evaluation framework" is "misleading" — the paper explicitly states the tools interact with Unity in Section 3.2. The term "comprehensive" refers to the breadth of tools and evaluation dimensions, not cross-platform generality. The point is kept in weakened form as Minor #1 (scope clarification needed), but the stronger charge of "misleading" is removed.
- Strength Finder's bullet about "Automated constraint extraction is validated to match human annotations" — this is well-supported (Table 4), kept as a strength.
- Strength Finder's "Reveals critical limitations of existing generation methods" — specific enough (≤10% holistic SR, breakdown by constraint type), kept.

## Novel Insights

The reviewers' most insightful observation is that the very mechanism that gives LEGO-EVAL its accuracy — tool-based grounding via structured scene APIs — also defines its scope boundary. The framework succeeds precisely where VLMs fail (multi-hop reasoning over quantifiable scene properties) precisely because it leverages structured scene data that is only available in certain simulators. This tension between accuracy and generality is inherent to the tool-augmented approach and worth acknowledging explicitly. Additionally, the disparity between partial SR (>50%) and holistic SR (<10%) across all generation methods, highlighted by the paper and reinforced by reviewers, is a striking result that should push the field toward holistic instruction satisfaction rather than per-constraint optimization.

## Suggestions

1. Clarify the scope in the abstract and conclusion: replace "comprehensive evaluation framework" with a more precise phrase such as "evaluation framework for simulators with structured scene APIs."
2. Resolve the Figure 8 inconsistency (Valid ✓ vs. "constraint cannot be satisfied") — either correct the label or clarify what "Valid" refers to.
3. Add bootstrapped confidence intervals to Tables 1 and 3.
4. Include an error analysis of LEGO-EVAL's disagreements with humans (confusion matrix per constraint type).
5. Add a brief discussion of the computational cost of LEGO-EVAL relative to VLM-as-a-judge.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| ImagenWorld (bld9g6jFh9) | 6.67 | Larger-scale benchmark (3.6K conditions vs 130), but LEGO-EVAL's tool-augmented methodology is more novel. LEGO-EVAL slightly weaker overall. |
| SpatialGenEval (ddFN3lWpIr) | 5.00 | Similar evaluation-benchmark paper in T2I domain. LEGO-EVAL has stronger human agreement validation (κ=0.63 vs VLM-only evaluation). Comparable quality. |
| Scenethesis (SzhezVoaNB) | 5.00 | 3D scene generation paper. LEGO-EVAL is comparable in contribution and rigor, with clearer quantitative evidence. |
| SANEval (Er9rKIjTkD) | 4.00 | T2I compositional evaluation benchmark with limited human validation and proprietary API dependence. LEGO-EVAL is stronger on methodology and validation. |
| SceneMaker (Xo1h3mIN9O) | 3.00 | 3D generation paper with significant pipeline-complexity flaws. LEGO-EVAL is substantially stronger. |
| IL3D (0oxkxG9cCo) | 2.00 | Weak dataset paper with limited novelty. LEGO-EVAL is far stronger. |

Positioning: LEGO-EVAL is stronger than SANEval (4.00) and comparable to Scenethesis (5.00) and SpatialGenEval (5.00), but weaker than ImagenWorld (6.67) on scale. Score of 5.5 is justified.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>