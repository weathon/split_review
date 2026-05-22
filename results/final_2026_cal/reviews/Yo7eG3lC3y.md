Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Verification of key reviewer claims against paper

**Claim 1: Baseline asymmetry (tools vs no tools)** — Verified. LEGO-EVAL uses tools querying Unity simulator internals (`get_object_list`, `get_object_info`, etc.), while baselines get only 2D renderings. However, this IS the paper's contribution; the comparison shows the value of tool augmentation. The paper frames this as a comparison of evaluation methods, which is accurate but could be more transparent about where the gains come from.

**Claim 2: Embodied agent connection untested** — Verified. The paper motivates with embodied agents but never tests agent performance. This is common motivational framing, but the critic is correct that no downstream evidence is provided.

**Claim 3: Object-Architecture inconsistency** — Verified. Section 3.1 lists four constraint types (Floor Layout, Material Selection, Object Selection, Object Placement). Figure 4b additionally shows "Objects - Architectures" as a separate category, which doesn't cleanly map. Minor inconsistency.

**Claim 4: Tool failure mode analysis** — The paper mentions tools like `get_object_match` use VLMs, but failure mode analysis is not provided in the main text. Referred to Appendix C.3 (stripped). This is a reasonable concern.

**Claim 5: Negative scene creation** — Paper says "manually curate 130 additional scenes that intentionally do not fully satisfy the instructions." Details in Appendix B.2 (stripped). Not a valid criticism of the submitted paper since appendix detail is standard.

**Claim 6: Near-zero kappa** — Paper explains why baselines fail (CLIP lacks 3D understanding, VLMs misidentify components, SceneEval can't evaluate 41% of constraints). The critic's concern is addressed.

**Claim 7: 10% holistic success rate relies on LEGO-EVAL** — Paper already shows LEGO-EVAL agrees with humans (κ=0.63). This is addressed.

**Claim 8: Figure 8 case study** — The paper claims LEGO-EVAL accurately recognizes absence of objects. The critic's point about tool advantage vs reasoning parity is the same as claim 1. Merge.

---

## Final Review

Here is my consolidated review:

---

## Summary

This paper introduces LEGO-EVAL, a tool-augmented evaluation framework for fine-grained assessment of text-to-3D scene synthesis, along with LEGO-BENCH, a benchmark of 130 instructions averaging 9.6 constraints each. The framework equips a VLM with 21 diverse tools (environment interaction, textual reasoning, multimodal reasoning) that query the Unity simulator to ground scene components, enabling multi-hop evaluation of constraints about objects, layouts, materials, and spatial relations. Experiments show LEGO-EVAL achieves 0.81 holistic F1 and 0.63 Cohen's κ against human judgments, substantially outperforming VLM-as-a-judge (0.40 F1, 0.05 κ). Benchmarking four scene generation methods on LEGO-BENCH reveals that all methods achieve at most 10% holistic success rate, highlighting significant limitations in current approaches.

## Strengths

- **Large and well-supported improvement over VLM-as-a-judge in human alignment.** Table 1 shows LEGO-EVAL achieves holistic F1 of 0.81 and Cohen's κ of 0.63, versus the best VLM baseline (GPT-4.1) at 0.40 and 0.05 respectively—more than doubling the F1 score. The κ=0.63 indicates substantial agreement, while baselines hover near chance, directly supporting the claim that tool-augmented multi-hop grounding is essential for reliable evaluation.

- **Reveals that existing scene generation methods nearly always fail on fine-grained instructions.** Table 3 reports that all four evaluated methods (I-Design, LayoutGPT, Holodeck, LayoutVLM) achieve at most 10.0% holistic success rate on LEGO-BENCH. Figure 6 further shows success rates drop sharply as instruction complexity increases, providing the community with a clear diagnosis of current limitations.

- **Principled ablation demonstrates all three tool types are necessary.** Table 2 shows removing textual reasoning tools drops holistic F1 by 5.05%, and removing both visual and textual tools drops it by 24.90%. Figure 5 confirms each tool type is actively used across constraint categories, establishing that no single modality suffices for fine-grained grounding.

- **Automated constraint extraction is nearly as reliable as human annotation.** Table 4 compares evaluations using automatically identified constraints vs. human-annotated ones across four scene generation methods; differences in both holistic and partial success rates are ≤ 0.03. This supports the practical claim that LEGO-EVAL functions as a fully end-to-end automated evaluator.

- **Demonstrates utility as a refinement signal.** Figure 7 shows using LEGO-EVAL feedback over three iterations raises Holodeck's holistic success rate from 8.5% to 18.5%, compared to 14.5% with VLM-as-a-judge, with qualitative evidence (Figure 8) showing LEGO-EVAL avoids the hallucinations that plague VLM-based evaluation.

## Weaknesses

### Major

- **The baseline comparison is structurally asymmetric, and the paper does not adequately qualify this.** LEGO-EVAL accesses ground-truth scene metadata through simulator tools (e.g., `get_object_list` returns exact object positions and rotations), while baselines receive only 2D renderings. The resulting 0.41 F1 gap shows that access to structured simulator internals yields more reliable evaluation than vision-only inference—which is a valid result—but the paper presents this as a general superiority claim ("outperforms VLM-as-a-judge by 0.41 F1") without sufficiently disentangling the contribution of privileged simulator access from the contribution of the planning/reasoning pipeline itself. An experiment where baselines are given partial structured information (e.g., object lists) would isolate the value of the planning and reasoning components more cleanly. As it stands, the headline number conflates two factors: tool access and reasoning quality.

### Minor

- **The embodied agent motivation is asserted but never tested.** The paper repeatedly frames the work as critical for embodied agent training ("ultimately enabling more capable and reliable embodied agents"), yet no experiment measures actual agent performance (e.g., success rate on navigation or manipulation tasks) in scenes that pass vs. fail LEGO-EVAL's criteria. This is common motivational framing, but the significance of the framework for embodied agents remains speculative. The contribution stands without this validation (the evaluation framework and benchmark are independently valuable), but the paper overstates its downstream impact.

- **Constraint categorization inconsistency.** Section 3.1 defines four constraint types (Floor Layout, Material Selection, Object Selection, Object Placement), but Figure 4b introduces an additional "Objects - Architectures" category that does not cleanly map to the four-type scheme. The paper should clarify how this fifth category fits into the taxonomy.

- **Tool failure modes are not analyzed.** Several tools (e.g., `get_object_match`) rely on VLMs that can make errors, but the paper does not analyze how such errors propagate through the evaluation pipeline. Since the framework's reliability depends on tool correctness, understanding these failure modes would strengthen trust in the benchmark results.

### Trivial

- The "Valid ✓" label in the LEGO-EVAL box of Figure 8 appears to contradict the reasoning text ("the constraint cannot be satisfied") — if the constraint cannot be satisfied, the judgment should be "Invalid". This should be corrected for consistency.

## Nice-to-Haves

- **Confidence intervals or statistical significance tests** for the main results in Table 1 would help assess reliability given the 260-pair dataset.
- **Ablation giving baselines partial structured inputs** (e.g., object lists) would cleanly decompose the contribution of tool access vs. reasoning.
- **Releasing the user-generated descriptions** (avg 18.2 constraints mentioned in Section 4.2.2) as an additional resource would strengthen the benchmark.

## Removed Points

These points were flagged but removed after verification against the paper:

1. **"Near-zero kappa warrants explanation"** — The paper already explains why baselines fail (CLIP lacks 3D understanding, VLMs misidentify components, SceneEval can't evaluate 41% of constraints). The explanation is present.

2. **"Negative scene creation not described in sufficient detail"** — The paper states "manually curated 130 additional scenes that intentionally do not fully satisfy the instructions" and refers details to Appendix B.2. Standard practice for supplementary material.

3. **"10% holistic success rate relies on LEGO-EVAL's evaluation"** — The paper already validates LEGO-EVAL against human judgments (κ=0.63 substantial agreement), so this concern is addressed.

4. **"No statistical significance testing"** — While a nice-to-have, confidence intervals for Cohen's κ and F1 on a 260-sample dataset are not standard for this type of evaluation and don't undermine the clear trends.

5. **"130 instructions is a small benchmark"** — The benchmark is manually curated with an average of 9.6 constraints each (1,250 total constraints). The complexity per instruction compensates for the modest size, and many established benchmarks in the field operate at similar scales.

## Novel Insights

None beyond the paper's own contributions. The key insight—that tool-augmented VLM evaluation substantially outperforms vision-only methods for fine-grained 3D scene assessment—is well demonstrated but is essentially the paper's own thesis, not a novel synthesis from the reviews.

## Suggestions

- Add an experiment where VLM-as-a-judge baselines receive structured inputs (object lists + coordinates) to isolate the contribution of LEGO-EVAL's planning and reasoning from the contribution of simulator tool access.
- Tone down the embodied-agent claims in the conclusion unless downstream validation is added (even a small-scale experiment measuring agent performance on pass vs. fail scenes).
- Resolve the constraint taxonomy inconsistency between Section 3.1 (4 types) and Figure 4b (5 types including "Objects - Architectures").
- Analyze and report the failure modes of individual tools (e.g., VLM-based tools) and their propagation to overall evaluation accuracy.

## Score and Decision

My round-1 bracket placed the paper between the weak anchors (<3.5, fundamentally flawed papers) and strong anchors (>7.5, seminal contributions). The round-2 anchors narrowed the comparison:

- **SpatialGenEval (5.0, Accept Poster)**: Benchmark-only contribution with VLM-in-the-loop evaluation concerns. LEGO-EVAL is stronger due to its method contribution and human-alignment validation.
- **MV-RoboBench (6.5, Accept Poster)**: Benchmark for multi-view spatial reasoning, 1.7k manually curated items. Comparable quality; LEGO-EVAL additionally contributes a method (not just a benchmark), but has a smaller dataset and a more notable baseline-comparison framing issue.
- **FineSplat (5.33, Reject)**: Fine-grained 3D understanding method. LEGO-EVAL is stronger empirically and more thorough in evaluation.
- **VLM4VLA (7.0, Accept Poster)**: Systematic study of VLM-to-VLA transfer. Stronger empirical breadth but different contribution type.

LEGO-EVAL sits at the upper end of the middle band—it has a genuine method contribution, thorough experiments with human validation, and useful ablations, but the baseline comparison asymmetry and unvalidated embodied-agent framing prevent it from reaching the top band. The paper is comparable to MV-RoboBench in overall quality, with LEGO-EVAL's method contribution balanced against MV-RoboBench's larger benchmark and broader model evaluation.

**MY FINAL SCORE: <score>6.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**