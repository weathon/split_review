Now I have a thorough understanding of both the paper and the calibration landscape. Let me produce the final consolidated review.

---

## Summary

This paper introduces LEGO-EVAL, a tool-augmented evaluation framework for text-guided 3D scene synthesis that explicitly grounds scene components via a suite of 21 tools (environment interaction, textual reasoning, multimodal reasoning) to verify per-constraint instruction–scene alignment. The authors also contribute LEGO-BENCH, a benchmark of 130 fine-grained instructions (avg. 9.6 constraints each) spanning object/architecture attributes and spatial relations. LEGO-EVAL achieves a holistic F1 of 0.81 and Cohen's κ of 0.63 against human judgments, more than doubling the best VLM-as-a-judge baseline (F1=0.40, κ=0.05). Benchmarking existing generation methods reveals ≤10% holistic success rates, exposing severe limitations in current approaches.

## Strengths

- **Dramatic improvement in evaluation accuracy with robust evidence.** LEGO-EVAL achieves holistic F1 of 0.81 and Cohen's κ of 0.63, compared to 0.40/0.05 for the best VLM-as-a-judge baseline and 0.33/0.00 for SceneEval (Table 1). The use of three different VLMs (Gemini-2.5-Pro, GPT-4o-mini, GPT-4.1) all converging to κ≈0.05 strengthens the claim that the gap is not due to poor prompt engineering for a single model.

- **Clean, well-motivated framework with validated design.** The four-stage pipeline (constraint identification → tool planning → argument selection → validation) is clearly articulated. The ablation study (Table 2) demonstrates that disabling environment interaction tools causes a 24.9% drop in holistic F1, while textual and multimodal reasoning tools also matter, confirming that all three tool types are necessary and that the gains are not merely from task decomposition.

- **A useful, realistic benchmark that exposes real limitations.** LEGO-BENCH provides 130 instructions with 1,250 total constraints across diverse categories (Figure 4). Benchmarking four methods (LayoutGPT, Holodeck, I-Design, LayoutVLM) reveals that holistic success rates top out at 10%, convincingly demonstrating that current generation methods cannot satisfy fine-grained real-world instructions.

- **Practical end-to-end utility demonstrated.** The framework operates effectively with automatically extracted constraints (Table 4, negligible difference from human-annotated constraints), and serves as a superior feedback signal for iterative refinement (Figure 7, LEGO-EVAL feedback improves Holodeck's success rate from ~8.5% to ~18.5% over 3 refinement rounds vs. ~14.5% for VLM feedback).

- **Convincing qualitative evidence.** The case study (Figure 8) concretely shows how LEGO-EVAL avoids the hallucinated object localizations that plague both VLM-as-a-judge (which hallucinates a flashlight and laptop) and SceneEval (which misidentifies a painting as a laptop), correctly recognizing that neither object exists and therefore the constraint cannot be evaluated.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Per-constraint ground-truth annotation process is under-described in the main text.** The paper reports partial (per-constraint) F1, recall, precision, and κ in Table 1, which requires knowing which individual constraints are satisfied vs. violated in each of the 130 negative scenes. Section 3.3 states that constraints are annotated, and Section 4.1.1 says negative scenes were "manually curated" to "intentionally not fully satisfy" instructions. The inference that curators tracked which constraints they violated is reasonable, and details likely appear in Appendix B.2 (stripped by the parser), but a brief description of the annotation protocol for negative scenes in the main text would strengthen confidence in the partial-level metrics.

- **No analysis of individual tool output accuracy.** The paper ablates entire tool *types* (Table 2) and measures tool *planning* accuracy (Table 5), but never directly measures how often individual tools (e.g., "get property description," "get spatial relation") return incorrect information. Since multimodal reasoning tools rely on VLMs that can err, understanding whether tool failures limit evaluation accuracy would strengthen the robustness claims. The high overall human agreement (κ=0.63) provides indirect validation, but a brief error analysis would be informative.

- **CLIPScore threshold selection is post-hoc rather than principled.** Three fixed thresholds (15, 20, 25) are evaluated, but no validation split or threshold-sweep rationale is provided. Plotting F1 as a function of threshold would give a fairer picture of CLIPScore's best-case performance and make the comparison more rigorous.

### Trivial

- The exact prompt and output format for the VLM-as-a-judge baseline are not specified in the main text (details presumably in appendix). While the use of three VLMs with self-consistency already makes the comparison credible, providing the prompt in an accessible location aids reproducibility.

## Nice-to-Haves

- **A constraint-by-constraint VLM baseline** (VLM prompted to evaluate each constraint individually without custom tools, using the same decomposition as LEGO-EVAL) would isolate whether gains come from decomposition alone or specifically from the tool suite. The current evidence (Table 2 ablation, Figure 1) already strongly suggests tools are critical, but this additional baseline would make the argument airtight.

- **Tool-level error analysis with qualitative examples** showing where a specific tool returns incorrect information and how that propagates (or is corrected) in the final judgment, giving richer insight into framework robustness.

- **Evaluation on scenes generated outside the Holodeck/Unity stack** to demonstrate generality. The current tool set is tied to Unity; extending to other simulators would broaden the framework's community utility.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"Unsubstantiated per-constraint ground truth" (Harsh Critic, Point 1):** The critic claimed per-constraint labels cannot be verified. However, the paper explicitly states constraints are annotated (Section 3.3) and negative scenes were manually curated to intentionally violate constraints (Section 4.1.1). The partial metrics reported in Table 1 presuppose that curators tracked which constraints were violated — this is a natural consequence of deliberately constructing scenes that "do not fully satisfy" instructions. The appendix (stripped by parser) contains further collection details. Kept as a minor documentation concern rather than an evidential gap.

- **"VLM baseline is a strawman" (Harsh Critic, Point 2):** The critic argued the VLM baseline may be performing near chance due to poor prompting. But three different VLMs (Gemini-2.5-Pro, GPT-4o-mini, GPT-4.1) all converge to κ≈0.05 with self-consistency — this pattern across diverse models makes a prompt-engineering explanation implausible. The paper's Figure 1 directly demonstrates *why* VLMs fail (cannot ground small/scene components from images), providing a mechanistic explanation independent of prompt design.

- **"No measurement of individual tool accuracy makes claims unsubstantiated" (Harsh Critic, part of Point 3):** The critic claimed the high human agreement "could simply reflect that the tools are sufficiently accurate for the specific constrained scenes." But the tools span diverse constraint types and 260 scene pairs; the benchmark's constraint diversity (Figure 4) and the strong ablation results (Table 2) make this concern overblown. Kept as a minor point (tool accuracy analysis would be informative but is not essential to validate the core claim).

- **"Introduction overstates weakness of existing methods without acknowledging scene graphs could be provided to VLMs" (Harsh Critic, Section-by-Section):** The paper explicitly discusses SceneEval as an existing method that attempts structured evaluation, and the VLM baseline already provides 4 viewpoint images. Providing a full scene graph to a VLM would essentially be giving it the answer — the point of evaluation is to test whether models can *autonomously* assess alignment.

- **"No discussion of tool-augmented approaches outside 3D scenes" (Harsh Critic, Section-by-Section):** The paper explicitly discusses VisProg and ViperGPT in Section 2 (Related Work, paragraph on tool-augmented language models), directly contradicting this claim.

- **"No confidence intervals or significance tests" (Harsh Critic, Section-by-Section):** Confidence intervals are not standard practice in 3D scene evaluation benchmarks; none of the calibration anchor papers in this domain report them. The 260-pair dataset and consistent pattern across multiple metrics/models make the results interpretable without them.

- **Various formatting/style nits and missing-appendix criticisms (Harsh Critic, multiple points):** These are parser artifacts or reflect the stripped appendix — the original submission includes the relevant details.

## Novel Insights

The paper's most novel empirical insight is that multi-hop grounding via explicit tool use — rather than end-to-end VLM judgment — is what drives evaluation accuracy for 3D scenes. This is supported by the stark contrast between VLM-as-a-judge (κ=0.05, near chance) and LEGO-EVAL (κ=0.63, substantial agreement), combined with the ablation showing that environment interaction tools alone account for a ~25% drop in F1. The finding is significant because it challenges the increasingly common practice of using off-the-shelf VLMs as evaluators for complex spatial tasks, and provides a concrete alternative architecture (tool-augmented constraint-by-constraint verification) that generalizes beyond the specific 3D scene domain.

## Suggestions

- Briefly describe the per-constraint annotation protocol for negative scenes in the main text (even one sentence clarifying that curators logged which constraints were violated when constructing the 130 negative scenes would address the documentation concern).
- Include the VLM-as-a-judge prompt in an accessible location (main text or a clearly referenced appendix section).
- Add a short paragraph or table in the analysis section characterizing the frequency and types of multimodal reasoning tool failures observed, perhaps on a small sample, to complement the strong end-to-end results.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | How LEGO-EVAL compares |
|---|---|---|---|
| T2I-CoReBench (`iqAFhWistW`) | 6.0 | Accept (Poster) | Similar: both introduce well-structured benchmarks with comprehensive evaluation. LEGO-EVAL adds a novel *evaluation framework* (not just a benchmark) with stronger human validation (κ=0.63 vs. checklist-based MLLM evaluation). Slightly stronger. |
| Scenethesis (`SzhezVoaNB`) | 5.0 | Accept (Poster) | LEGO-EVAL is substantially stronger: better human validation, more thorough experiments, clearer novelty in evaluation methodology rather than system integration. |
| SANEval (`Er9rKIjTkD`) | 4.0 | Reject | LEGO-EVAL is clearly stronger: genuine novelty in tool-augmented grounding vs. incremental extension, much stronger human validation, cleaner experimental design. |
| Agentic 3D Scene Gen (`uiopHcWPRO`) | 4.4 | Reject | LEGO-EVAL is stronger: cleaner contribution, better ablations, stronger human evaluation. |
| CHOrD (`xszAt23a17`) | 4.0 | Reject | LEGO-EVAL is stronger: more thorough experiments, clearer evaluation methodology, stronger human validation. |
| RoomGen (`g7Kxs5NE7R`) | 2.0 | Reject | LEGO-EVAL is clearly far superior: genuine novelty, strong validation, comprehensive experiments. |

LEGO-EVAL sits above the 4.0–5.0 band and is comparable to or slightly stronger than the 6.0 anchor. The paper makes a genuine contribution with a novel framework, strong empirical results, a useful benchmark, and practical demonstrations. Weaknesses are minor and addressable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>