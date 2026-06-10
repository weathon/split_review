## Summary
This paper introduces LEGO-EVAL, a tool-augmented VLM evaluation framework for text-guided 3D scene synthesis, and LEGO-BENCH, a benchmark of 130 fine-grained instructions with ~1,250 constraints spanning object and architectural components. LEGO-EVAL achieves 0.81 holistic F1 (vs. 0.40 for VLM-as-a-judge) and 0.63 Cohen's kappa (vs. 0.05) against human judgments on 260 instruction-scene pairs. Benchmarking reveals that existing synthesis methods satisfy at most ~10% of fine-grained instructions holistically.

## Strengths
- **Large, consistent improvement over all baselines (Table 1).** LEGO-EVAL with GPT-4.1 achieves 0.81 holistic F1 and 0.63 Cohen's kappa vs. 0.40/0.05 for the best VLM-as-a-judge, with gains holding across backbone models (GPT-4.1-mini: 0.70, Qwen2.5VL-32B: 0.64) and at both holistic and partial evaluation levels (0.83 vs. 0.68 partial F1).
- **Ablation demonstrates tool-augmented design drives improvement, not just a better VLM (Table 2).** Disabling Environment Interaction + Multimodal Reasoning tools causes a -24.90% drop in holistic F1, and disabling Textual Reasoning causes -5.05%, showing all three tool categories contribute meaningfully.
- **End-to-end automation with minimal degradation (Table 4).** Automatic constraint identification vs. human-annotated constraints yields ≤0.03 SR difference across four synthesis methods, validating the framework as fully automated.
- **Practical downstream utility as refinement feedback (Figure 7).** Using LEGO-EVAL as feedback improves Holodeck's holistic SR from 8.5 to 18.5 over 3 iterations, outperforming VLM-as-a-judge feedback (8.5 to 14.5), demonstrating value beyond static evaluation.
- **Insightful component-level analysis (Table 5).** Tool planning accuracy (Tool F1) correlates more strongly with final evaluation performance than argument selection accuracy, providing interpretable understanding of what drives framework effectiveness.

## Weaknesses

### Fatal
None.

### Major
- **Figure 8 case study contains a contradictory judgment that undermines the paper's showcase example.** The paper states "all methods achieve accurate judgments" (line 350), but LEGO-EVAL outputs "Valid ✓" while simultaneously explaining "the constraint cannot be satisfied" (lines 338–340). The paper's own text confirms "the flashlight and laptop do not exist in the scene" (line 350), so the constraint is unsatisfied and the correct judgment is Invalid. The other two methods (VLM-as-a-Judge and SceneEval) arrive at the correct binary output (Invalid) despite flawed reasoning. This is the paper's primary qualitative showcase and it either reflects a labeling error or exposes a systematic issue in how LEGO-EVAL handles missing prerequisite objects. The paper should fix the label, explain why "Valid" is correct if it is, and analyze how frequently this pattern occurs in the test set.

### Minor
- **Inter-annotator agreement for human ground truth not reported in main text.** The entire evaluation rests on agreement with 260 human judgments, but the main text provides no inter-annotator agreement statistics. Without knowing whether humans agree at 0.75 or 0.95 kappa, it is impossible to contextualize LEGO-EVAL's 0.63 kappa. The reference to Appendix B.2 is noted, but the main text should report at minimum a summary statistic.
- **LEGO-EVAL used as both feedback signal and evaluation metric in refinement experiment (Section 5).** Since LEGO-EVAL provides the feedback and also evaluates the output, improvement may partly reflect optimization toward LEGO-EVAL's own biases rather than genuine scene quality. Independent human evaluation of refined scenes would strengthen this claim.
- **No discussion of computational cost.** LEGO-EVAL uses GPT-4.1 with multi-step tool execution per constraint (~1,250 constraints across 130 instructions). For a framework designed for iterative refinement, API cost and evaluation time are practical concerns that should be discussed.
- **Balanced 50/50 test set design may not reflect real-world class distribution.** The 130 valid + 130 intentionally invalid scenes simplify interpretation but the paper does not discuss whether results are robust to different ratios.

## Nice-to-Haves
- Discuss how much engineering effort is required to make a new scene generator compatible with LEGO-EVAL's Unity-based tool set, particularly for methods that don't output Unity-compatible formats.
- Brief error analysis of the ~19% of cases where LEGO-EVAL disagrees with humans (0.81 F1 implies ~19% disagreement).
- Show end-to-end evaluation (Table 4) holds across multiple scene generators, not just Qwen2.5VL-32B.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Harsh critic's claim that "The scene contains neither object" as the primary issue in Figure 8.** The paper's own text on line 350 states "the flashlight and laptop do not exist in the scene," so the paper's position is consistent. The real issue is the Valid/Invalid label contradiction, which is kept as a Major weakness above.
- **Strength finder's claim about Figure 8 as a strength.** This conflicts with the verified weakness — the figure shows contradictory labeling, not a clean demonstration of superiority.
- **Criticism that "more than doubles" in the conclusion overstates improvement.** The conclusion refers to holistic F1 (0.81 vs. 0.40 = 2.025x), which is technically accurate.

## Novel Insights
The paper reveals a striking finding that even the best existing synthesis method (LayoutVLM) satisfies only ~10% of fine-grained instructions holistically, and success rates drop to ~0.5% for complex instructions with 13+ constraints. This gap between partial success (60% average SR) and holistic success (10%) highlights that current methods fail at composing all constraints simultaneously — a practically important insight for the embodied AI community.

## Suggestions
- Fix or clarify the Figure 8 case study: either correct "Valid ✓" to "Invalid ✗" or explain why the current labeling is correct.
- Add inter-annotator agreement statistics to the main text or a prominent table/footnote.
- Add a brief discussion of evaluation cost (API calls, wall-clock time) to help practitioners.
- Analyze the error pattern in Figure 8 systematically: how many constraints in the test set involve missing prerequisite objects, and how does LEGO-EVAL handle them?

## Calibration Report

**All anchors retrieved:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SYNBUILD-3D | TCSaLeANpN | 3.00 | 1 | Weak 3D dataset paper — LEGO-EVAL clearly stronger |
| MCTBench | BVACdtrPsh | 3.00 | 1 | Weak benchmark — LEGO-EVAL has better methodology |
| Evaluating Unseen CBMs | kTjEPEy96Q | 3.00 | 1 | Weak eval framework — LEGO-EVAL much stronger |
| Path-Tracing Distillation | f7Zq9CqQEM | 3.40 | 1 | Weak 3D generation — LEGO-EVAL clearly better |
| CF-GISS | Yj6IdXSOZk | 5.00 | 1 | 3D scene synthesis — LEGO-EVAL has stronger experiments |
| ISG | rDLgnYLM5b | 7.20 | 1 | Interleaved generation eval — comparable scope, LEGO-EVAL has stronger relative gains but Figure 8 issue |
| Davidsonian Scene Graph | ITq4ZRUT4a | 6.00 | 1 | T2I eval framework — LEGO-EVAL has stronger results |
| Benchmarking Diffusion | nkCWKkSLyb | 5.50 | 1 | Image editing benchmark — LEGO-EVAL more complete |
| PhysBench | Q6a9W6kzv5 | 8.00 | 1 | Large-scale VLM benchmark — larger scope, no labeling issues |
| LOKI | z8sxoCYgmd | 8.00 | 1 | Synthetic data detection — different domain, higher bar |
| MMIE | HnhNRrLPwm | 8.00 | 1 | Multimodal benchmark — much larger scale |
| TetSphere Splatting | 8enWnd6Gp3 | 7.60 | 1 | 3D generation — different focus, higher bar |
| DivScene | G6DLQ40VVR | 6.25 | 2 | Object nav benchmark — LEGO-EVAL more complete system |
| LLMs as Aligners | kZEXgtMNNo | 6.00 | 2 | VLM evaluation — LEGO-EVAL has stronger quantitative results |
| VisualAgentBench | 2snKOc7TVp | 5.75 | 2 | Visual agents — LEGO-EVAL has more methodological novelty |
| VideoNIAH | ZJo6Radbqq | 5.75 | 2 | Video benchmark — different domain, comparable bar |
| Point-based Completion | llSiIJosDj | 7.00 | 2 | 3D completion — different focus |
| 3D-PC | UIFAJZ22ZF | 6.67 | 2 | 3D perception benchmark — LEGO-EVAL comparable quality |
| EditRoom | Y2Dh8rWwlb | 6.67 | 2 | 3D room editing — comparable domain quality |
| VQA benchmarking | EXitynZhYn | 7.00 | 2 | VLM eval — comparable quality |

**Round 1 bracket:** 5.5–7.5. The paper is clearly above weak anchors (3.0–3.4) which have fundamental issues, and below strong anchors (7.6–8.0) which are larger-scale or lack the Figure 8 labeling problem.

**Round 2 narrowing:** The paper sits above the 5.75–6.25 anchors (stronger system, better results, more methodological novelty) but below ISG (7.2) which has larger scale and no contradictory case study. The 6.5–7.0 range is the right zone, with EditRoom (6.67) and 3D-PC (6.67) as the closest comparables.

**Final score: 6.5** — positioned between the mid-tier anchors (5.75–6.25) and the stronger eval-framework anchors (7.0–7.2), reflecting strong quantitative results and thorough experimentation but offset by the contradictory Figure 8 case study and missing inter-annotator agreement statistics.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>