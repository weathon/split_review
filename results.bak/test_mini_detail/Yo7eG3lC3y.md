Now I have a good picture of the calibration landscape. Let me finalize my review.

**Round 1 bracket**: I initially bracketed this paper between weak anchors (avg ~3-4) and strong anchors (avg ~8). The paper is clearly stronger than rejected benchmarking studies on VLMs' 3D reasoning (avg 4.0) and dataset papers with weak technical contributions like 3D-GRAND (avg 5.0). It's closer to accepted poster papers like SPARTUN3D (5.75) and HAZARD (6.75), but not at the level of spotlight papers (avg 8.0).

**Round 2 narrowing**: Comparing to SPARTUN3D (5.75) — LEGO-EVAL has a stronger technical contribution (tool-augmented evaluation is genuinely novel, not just another dataset). Comparing to HAZARD (6.75) — LEGO-EVAL's methodological contribution is more novel but the benchmark is smaller. Overall, this paper sits between 6.0 and 7.0. I'm placing it at **6.5**.

Now let me write the final review.

Key weaknesses I identified from reading the paper:
1. The ablation claims "all three tool types are indispensable" but Multimodal Reasoning tools contribute only 0.04% to holistic F1 — this contradicts the claim.
2. No error analysis — what kinds of constraints does LEGO-EVAL fail on?
3. The benchmark size is modest (130 instructions, 260 pairs)
4. Tools are Unity-specific, unclear generalizability
5. The case study in Figure 8 has a confusing labeling

Let me now write the full review.## Summary

This paper introduces LEGO-EVAL, a tool-augmented evaluation framework for fine-grained text-guided 3D scene synthesis. The key idea is to equip VLMs with 21 diverse tools (environment interaction, textual reasoning, multimodal reasoning) that explicitly ground scene components before verifying instruction constraints. The paper also contributes LEGO-BENCH, a benchmark of 130 instructions with 1,250 constraints spanning object placement, object selection, floor layout, and material selection. LEGO-EVAL achieves an F1 score of 0.81 and Cohen's κ of 0.63 for holistic instruction-scene alignment, compared to 0.40 and 0.05 for the best VLM-as-a-judge baseline (GPT-4.1), and reveals that existing 3D scene generation methods satisfy at most 10% of instructions on LEGO-BENCH.

## Strengths

- **Large and reliable improvement over VLM-as-a-judge baselines**: LEGO-EVAL achieves 0.81 F1 and κ=0.63 vs. the best VLM baseline's 0.40 F1 and κ=0.05 (Table 1). The Cohen's κ of 0.63 indicates substantial agreement with human judgments beyond chance, whereas the VLM baseline shows near-chance agreement (κ=0.05). This gap is large and consistently observed across both holistic and partial evaluation levels.

- **Demonstrated multi-hop grounding that VLMs cannot perform**: In the case study (Figure 8), LEGO-EVAL correctly identifies that neither the flashlight nor the laptop exists in the scene and therefore the orientation constraint cannot be satisfied. In contrast, VLM-as-a-judge hallucinates both objects and their relative orientations, while SceneEval misidentifies a painting as a laptop. This qualitative evidence directly supports the paper's central claim that tool-augmented grounding is necessary.

- **Comprehensive benchmark with real-world constraint diversity**: LEGO-BENCH contains 130 instructions with 1,250 constraints (avg. 9.6 per instruction) spanning object placement (39.5%), object selection (23.3%), floor layout (21.8%), and material selection (15.4%). SceneEval cannot evaluate 41% of these constraints, demonstrating that prior evaluation tools are insufficient for the complexity of real-world indoor environments.

- **End-to-end evaluation capability validated**: Table 4 shows that LEGO-EVAL's automatically identified constraints produce nearly identical evaluation results to human-annotated constraints (max difference of 0.03 in success rates), showing the framework can operate fully automatically without requiring manual constraint annotation.

## Weaknesses

### Fatal
None.

### Major

- **The claim that "all three tool types are indispensable" is contradicted by the ablation data.** The ablation (Table 2) shows that disabling Multimodal Reasoning tools alone (w/o M) reduces holistic F1 by only **0.04%** — essentially zero. Disabling Textual Reasoning (w/o T) drops F1 by 5.05%, and disabling both Environment Interaction and Multimodal Reasoning (w/o E+M) drops it by 24.90%. The individual contribution of Multimodal Reasoning tools is negligible, yet the paper states "all three tools are indispensable for comprehensive and reliable evaluation" (Section 4.1.3). This overclaiming weakens one of the central supporting arguments and should be corrected to accurately reflect which tool types drive performance.

- **No error analysis or failure case characterization.** The paper reports strong aggregate metrics (F1, κ) but never analyzes *where* LEGO-EVAL still fails. Given that the method achieves 0.81 F1, it makes errors on ~19% of cases. Understanding failure modes — e.g., does it struggle with certain constraint types, complex spatial relations, or specific tool planning failures? — is important for assessing the method's limits and would substantially strengthen the paper.

### Minor

- **The benchmark is modest in size.** LEGO-BENCH contains 130 instructions, yielding 260 instruction-scene pairs for evaluation (130 valid + 130 invalid). While the constraint count (1,250) is substantial, the number of distinct instructions is relatively small for a benchmark intended to support robust evaluation. This does not invalidate the results but limits the statistical power of fine-grained analyses.

- **Tool ecosystem is specific to the Unity environment.** The 21 tools are tightly coupled to a particular simulation platform. Generalizing the approach to other 3D simulators (e.g., AI2THOR, Habitat) would require reimplementing the entire tool suite. The paper does not discuss this limitation or how the tool design could be abstracted.

- **The case study in Figure 8 contains a confusing labeling inconsistency.** LEGO-EVAL marks the constraint as "Valid ✓" but the explanation states "the constraint cannot be satisfied." If the constraint cannot be satisfied (because objects are missing from the scene), the judgment should be "Invalid ✗." While this appears to be a formatting/presentation error rather than a methodological flaw, it creates confusion about the method's outputs.

### Trivial
None.

## Nice-to-Haves

- Perform an ablation that isolates Environment Interaction alone (w/o E) rather than only w/o E+M, to cleanly decompose the contribution of each tool type.
- Analyze the cost/compute overhead of LEGO-EVAL's multi-step tool execution pipeline compared to single-pass VLM baselines.
- Discuss the extent to which the method's reliance on GPT-4.1 as the backbone LLM for planning and argument selection creates a dependency; testing with open-source models (already partially done with Qwen2.5VL-32B) is appreciated but could be expanded.

## Removed Points

The Harsh Critic returned an empty/non-responsive message ("你好，我无法给到相关内容"—"Hello, I cannot provide relevant content"), so there are no reviewer points to filter.

From the Strength Finder: The strength claiming the ablation study "validates necessity of all three tool types" is partially removed because the data does not actually support the "indispensable" claim for Multimodal Reasoning tools (0.04% drop). This point has been reframed as a weakness above. Generic strengths (e.g., "this paper addressed an important problem") have been dropped as they lack specific evidentiary content.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a critique or observation that the paper itself does not already contain or implicitly address.

## Suggestions

- **Correct the "indispensable" claim.** Remove or weaken the assertion that all three tool types are equally indispensable. The data clearly shows that Multimodal Reasoning tools contribute negligibly. A more accurate framing would emphasize that Environment Interaction and Textual Reasoning tools drive performance, while Multimodal Reasoning tools provide marginal additional benefit in specific settings.

- **Add an error analysis section.** Analyze the ~19% of cases where LEGO-EVAL disagrees with human judgments. Categorize failures by constraint type, tool type used, or planning error type. This would significantly increase the paper's contribution by revealing where future work should focus.

- **Fix the Figure 8 inconsistency.** Ensure the "Valid/Invalid" labels in the case study match the reasoning provided. If the constraint truly cannot be satisfied, the label should be "Invalid ✗."

- **Discuss generalizability.** Add a paragraph in the limitations about how the tool design could be adapted to other 3D simulators or whether certain tools (e.g., textual reasoning tools querying structured scene data) are inherently platform-specific.

- **Expand the ablation design.** Report w/o E individually (even if some tools must stay enabled for argument selection, a clean decomposition would strengthen the analysis).

## Score and Decision

**Round 1 (Bracketing):** Queried for papers on 3D scene synthesis, evaluation, and tool-augmented LLMs in three score bands. Weak anchors (avg 2.0–3.4) included papers on unrelated topics or with fatal flaws. Middle anchors (avg 4.0–5.75) included "On Inherent 3D Reasoning of VLMs" (4.0, rejected), "3D-GRAND" (5.0, withdrawn), and "SPARTUN3D" (5.75, accepted poster). Strong anchors (avg 7.75–8.0) included spotlight/oral papers. The paper is clearly stronger than the weak and middle-low anchors, but not at the level of the top anchors. Initial bracket: **4.5–7.5**.

**Round 2 (Narrowing):** Queried the bands (4.5–6.0) and (6.0–8.0). Read full reviews of SPARTUN3D (5.75, accepted poster) and HAZARD (6.75, accepted poster). Compared to SPARTUN3D: LEGO-EVAL has a stronger methodological innovation (tool-augmented pipeline vs. dataset + alignment module) and a much larger improvement over baselines (doubling F1 vs. 1-2% improvements). Compared to HAZARD (avg 6.75): LEGO-EVAL's benchmark is smaller but its methodological contribution is more novel and the results are more decisive; the papers are of comparable quality. The paper is weaker than the spotlight papers (avg 8.0) which have either much larger benchmarks or foundational methodological advances.

**Final score: 6.5.** This is a solid paper with a genuinely novel approach, convincing results, and a useful benchmark. The main weaknesses (overclaiming about multimodal tools, absence of error analysis) are addressable and do not undermine the core contribution.

**Anchors used across all rounds:**
- /home/wg25r/review_agent/human_reviews/b1vVm6Ldrd.md (avg 3.00, round 1): Unrelated topic (ToM benchmark), weak paper.
- /home/wg25r/review_agent/human_reviews/uBhqll8pw1.md (avg 4.00, round 1): VLM 3D reasoning study, rejected; LEGO-EVAL has much stronger results and methodological contribution.
- /home/wg25r/review_agent/human_reviews/i7hXOqzUcK.md (avg 5.00, round 1/2): 3D-GRAND dataset paper, withdrawn; LEGO-EVAL's technical contribution is substantially stronger.
- /home/wg25r/review_agent/human_reviews/s3sJenvY5H.md (avg 4.75, round 1): Robotic simulation evaluation framework; LEGO-EVAL's results are more decisive.
- /home/wg25r/review_agent/human_reviews/FGMkSL8NR0.md (avg 5.75, round 2): SPARTUN3D, accepted poster; LEGO-EVAL has stronger novelty and larger improvements.
- /home/wg25r/review_agent/human_reviews/n6mLhaBahJ.md (avg 6.75, round 2): HAZARD, accepted poster; comparable quality — LEGO-EVAL's method is more novel but benchmark is smaller.
- /home/wg25r/review_agent/human_reviews/IKOAJG6mru.md (avg 5.00, round 2): RoboTool, rejected; LEGO-EVAL's experiments are more rigorous.
- /home/wg25r/review_agent/human_reviews/7gUrYE50Rb.md (avg 8.00, round 1): EQA-MX, spotlight; LEGO-EVAL does not reach this level of benchmark scale and community impact.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>