Now I have sufficient calibration data. Let me write the comprehensive review.

**Calibration Summary:**

Round 1 bracketing placed the paper in (3.5, 7.5). The weak anchor papers (RoomGen 2.0, SynthTools 3.0, RoboView-Bias 3.2) are clearly below this paper, and the strong anchors (VIST3A 8.0, Gaia2 8.0, NavFoM 8.0) are clearly above. Round 2 narrowed the bracket substantially. Papers read in full for comparison: ToolEQA (5.0, Reject) — similar tool-augmented approach but criticized for indistinct novelty and evaluation gaps; Scenethesis (5.0, Accept Poster) — 3D scene generation pipeline with some novelty concerns; Agentic 3D Scene Generation (4.4, Reject) — scene generation with unclear novelty; ManipEvalAgent (4.67, Accept Poster) — evaluation framework for robotics; PhyWorldBench (5.5, Accept Oral) — comprehensive benchmark for physical realism; T2I-CoReBench (6.0, Accept Poster) — composition+reasoning benchmark; ENACT (4.8, Accept Poster) — embodied cognition benchmark. LEGO-EVAL has stronger methodological novelty than PhyWorldBench and is comparable to T2I-CoReBench in contribution density, but has a notable framing issue (structured data vs vision-only comparison without caveat) that papers like T2I-CoReBench do not share. The paper sits between 5.5 and 6.0. Given the framing concern, a score of **5.5** is appropriate.

---

## Summary

This paper proposes LEGO-EVAL, a tool-augmented evaluation framework for assessing alignment between fine-grained textual instructions and generated 3D scenes, alongside LEGO-BENCH, a benchmark of 130 complex instructions with up to 18 constraints each. LEGO-EVAL decomposes evaluation into four steps: constraint identification, tool execution planning, argument selection & execution, and constraint validation, using 21 tools spanning environment interaction (visual), textual reasoning (structured scene data), and multimodal reasoning. The paper reports that LEGO-EVAL achieves 0.81 holistic F1 and 0.63 Cohen's κ vs best VLM-as-a-judge baselines at 0.40 and 0.05, and reveals that existing scene generation methods achieve at most 10% holistic success rate on LEGO-BENCH.

## Strengths

- **Novel tool-augmented evaluation pipeline with clear mechanistic justification**: The four-stage pipeline (constraint identification → tool planning → argument selection → validation) is well-designed and the ablation in Table 2 shows that removing environment-interaction tools causes a 24.9% drop in holistic F1, while textual reasoning and multimodal reasoning tools each contribute non-trivially. This demonstrates that all three tool types are necessary and that the performance gain is not from a single component.

- **LEGO-BENCH reveals a stark, actionable gap in current 3D scene generation**: Table 3 shows all four evaluated methods achieve ≤10% holistic success rate, with performance collapsing to near 0% on complex instructions (13+ constraints) in Figure 6. This negative result is credible and important — it quantifies the limitations of current LLM-based scene generators and motivates future work on fine-grained generation.

- **Automated constraint extraction matches human annotation quality**: Table 4 shows that using LEGO-EVAL's automatically identified constraints yields evaluation results within ±0.03 of those using human-annotated constraints across four generation methods. This demonstrates the framework can operate end-to-end without sacrificing reliability.

- **Evaluation output doubles as a useful refinement signal**: Figure 7 shows that using LEGO-EVAL as feedback improves Holodeck's holistic success rate from ~8.5% to ~18.5% after three iterations, outperforming VLM-as-a-judge feedback (~14.5%). This demonstrates practical utility beyond assessment.

## Weaknesses

### Fatal

None.

### Major

- **Head-to-head comparison with VLM-as-a-judge is presented without adequate caveat about structured data access**: LEGO-EVAL's tools include `get_object_list`, `get_object_info`, `get_spatial_relation`, and `get_room_list` (Figure 3), which directly query structured scene representations (object IDs, exact coordinates, material properties). The VLM-as-a-judge baselines receive only four perspective rendered images. The resulting 0.41 F1 gap is presented as "outperforming" without clearly acknowledging that LEGO-EVAL has access to ground-truth structured data that is fundamentally unavailable to image-only methods. The paper needs to explicitly state that LEGO-EVAL is designed for simulation environments where structured scene APIs are available, and that the comparison demonstrates the value of tool-based structured verification — not superior "visual understanding." Section 3.2 describes the tools but never discusses this as a scoping limitation, which makes the headline claim misleading.

- **Missing controlled experiment isolating the effect of tool orchestration from structured data access**: The ablation in Table 2 disables tool types but never runs the condition where ALL structured-data tools (textual reasoning) are disabled and only visual tools (environment interaction + multimodal reasoning) remain. The paper states that "tools returning list of scene components are necessary for argument selection" and therefore remain enabled — but this means we cannot disentangle whether the performance gains come from having structured data vs. from the planning/rationale mechanism. A controlled experiment with a textual-scene baseline (feeding the LLM a full textual description of the scene) would help separate these factors.

### Minor

- **Benchmark size is limited (130 instructions, 260 instruction-scene pairs)**: While understandable as a first release given the manual curation effort, the relatively small size means the findings in Table 3 (≤10% success rate) are based on a limited sample. Including confidence intervals (e.g., bootstrapped CIs) would help assess the stability of these findings.

- **Results in Table 1 lack statistical significance measures**: No confidence intervals or significance tests are reported for the F1 and κ values. Given 260 instruction-scene pairs and relatively small per-category splits, some differences between methods may not be statistically significant.

- **The paper would benefit from a structured-data baseline**: An LLM prompted with a full textual description of the scene (all objects, their positions, colors, materials) could serve as a baseline that disentangles the value of tool orchestration from the value of having structured access. If LEGO-EVAL still outperforms this baseline, it would highlight the value of the planning mechanism.

### Trivial

- Figure 4(b) has duplicated/misaligned numbers in the pie chart (Object Selection appears twice with different percentages).
- The paper could improve the clarity of the case study in Figure 8: LEGO-EVAL correctly notes the constraint cannot be evaluated because objects are absent, returning "Valid ✓" — this is a sensible design choice but the ✓ symbol may confuse readers who expect a constraint to be satisfied rather than vacuously true.

## Nice-to-Haves

- A discussion of generalizability to non-Unity environments (e.g., Isaac Sim, MuJoCo, or real-world scans) would strengthen the paper, since the current tool set is tied to Unity.
- A finer-grained breakdown of which types of constraints (spatial vs. attribute vs. existence) each method handles well would be informative.
- A comparison with SceneEval's "Measurable Dataset" subset (Table 1) shows LEGO-EVAL also outperforms, but the paper could discuss why SceneEval's fixed criteria fail on 41% of constraints and how LEGO-EVAL's more flexible tool planning overcomes this.

## Removed Points

*The following points from the input reviews were removed with justification:*

1. **"Unfair comparison — this is comparing a database query engine to a human looking at a photo"** (Harsh Critic): Demoted from "structural" to the Major weakness above. The comparison IS informative for the intended use case (instrumented simulation environments), but the framing needs caveats. The critic's framing as purely a database query understates the complexity of tool planning, argument selection, and multi-hop reasoning in LEGO-EVAL.

2. **"The case study claim that LEGO-EVAL 'accurately recognizes the absence' is overstated"** (Harsh Critic): Removed. The statement is factually accurate — LEGO-EVAL does correctly determine the objects are absent. The mechanism (tool-based query vs. visual recognition) is the relevant difference, which falls under the major framing weakness above rather than being a separate issue.

3. **"Misleading framing of the contribution"** (Harsh Critic): Merged into the Major weakness about inadequate caveat. The paper's contribution as a verification protocol for simulation environments is valid; the issue is scope communication, not the contribution itself.

4. **"No comparison with a textual-scene baseline"** (Harsh Critic): Moved to Minor weakness and Nice-to-Have. This is a reasonable suggestion but not required for acceptance.

5. **"Reliance on Unity ground-truth representation should be stated as limitation"** (Harsh Critic): Covered under the Major weakness framing issue.

6. **"Strength: large improvement over baselines"** (Strength Finder): Kept but reframed with caveat. The improvement is real for the intended use case but should not be presented as an apples-to-apples comparison.

7. **Generic strengths from Strength Finder about "important problem" and "well-motivated"**: Removed as generic/superficial. The specific, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The calibration reading surfaced a recurring criticism pattern for tool-augmented evaluation papers: a controlled condition that isolates the contribution of the planning mechanism from the contribution of privileged data access is nearly always requested. The LEGO-EVAL paper is no exception, but its ablation (Table 2) is stronger than most — it at least measures the contribution of each tool type, which many papers in this space skip entirely.

## Suggestions

1. **Reframe the contribution explicitly**: State clearly that LEGO-EVAL is a verification protocol for simulation environments with structured scene APIs. Change "outperforms VLM-as-a-judge" to "using structured tool access, LEGO-EVAL achieves substantially higher agreement with human judgments than vision-only methods."

2. **Add a textual-scene baseline**: Prompt an LLM with a full textual description of the scene (all objects, positions, colors). If LEGO-EVAL still outperforms this baseline, it directly demonstrates the value of tool orchestration beyond structured data access.

3. **Add a visual-only variant of LEGO-EVAL**: As a controlled experiment, run LEGO-EVAL with only environment-interaction and multimodal reasoning tools (disable `get_object_list`, `get_object_info`, `get_spatial_relation`, etc.). Even if performance drops or the pipeline becomes infeasible, reporting this honestly would strengthen the paper.

4. **Add confidence intervals to Table 1**: Bootstrap the F1 and κ values to show their stability.

5. **Discuss generalizability**: Add a paragraph on how the tool framework could be adapted to other simulation environments (e.g., by reimplementing the tool set for a different scene representation).

## Score and Decision

**Round 1 bracket**: (3.5, 7.5) — above weak anchors like RoomGen (2.0) and below strong anchors like VIST3A (8.0).

**Round 2 narrowing**: Read papers at 4.4–6.0 for comparison. The paper is above the rejection-level Agentic 3D Scene Generation (4.4) and ToolEQA (5.0) in terms of contribution clarity and experimental support. It is comparable to PhyWorldBench (5.5, Accept Oral) in contribution density but has slightly weaker evaluation breadth. It is below T2I-CoReBench (6.0, Accept Poster) which has a larger benchmark and broader model coverage, though T2I-CoReBench's evaluation methodology is less novel.

**Final score**: **5.5**

The paper has genuine contributions — a novel tool-augmented evaluation pipeline, a useful benchmark, and a striking negative result. The main weakness is the comparison framing: the headline "outperforms VLM-as-a-judge by 0.41 F1" is presented without adequately acknowledging that LEGO-EVAL accesses structured scene data unavailable to the baselines. This is a real scope-communication issue, not a fatal methodological flaw, and is addressable in revision.

**Decision**: **Reject**

A borderline paper that could become an Accept with revision. The core methodology and benchmark are solid, but the framing of the central comparison is misleading in its current form, and the missing controlled experiments weaken the evidence for the claimed mechanism. A revision that reframes the contribution, adds a textual-scene baseline, and discusses the structured-data requirement as a scoping condition could make this a strong submission.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>