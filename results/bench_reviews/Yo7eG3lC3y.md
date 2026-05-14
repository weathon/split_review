Now I have all the information I need to produce my final consolidated review.

## Summary

This paper introduces LEGO-EVAL, a tool-augmented evaluation framework for fine-grained text-guided 3D scene synthesis, along with LEGO-BENCH, a curated benchmark of 130 instructions with 1,250 constraints. LEGO-EVAL decomposes instructions into individual constraints and validates them by selecting from 21 diverse tools spanning environment interaction, textual reasoning, and multimodal reasoning. Experiments show that LEGO-EVAL achieves 0.81 holistic F1 and 0.63 Cohen's κ against human judgments, substantially outperforming VLM-as-a-judge baselines (0.40 F1, 0.05 κ). Benchmarking existing generation methods reveals that none exceed 10% holistic success rate, demonstrating the difficulty of satisfying all constraints in realistic instructions.

## Strengths

- **Large, consistent improvement over VLM baselines**: LEGO-EVAL achieves 0.81 holistic F1 vs. 0.40 for GPT-4.1-as-a-judge (Table 1), and the gap is consistent across multiple VLM backbones (GPT-4.1, GPT-o4-mini, Gemini 2.5 Pro). This is a clean, reproducible result that directly validates the core thesis that tool-augmented multi-hop grounding substantially improves evaluation reliability.

- **Exposes that current generation methods nearly always fail on fine-grained instructions**: Benchmarking four LLM-based methods (LayoutGPT, Holodeck, I-Design, LayoutVLM) on LEGO-BENCH shows that none exceed 10% holistic success rate (Table 3), and performance collapses on instructions with more than 7 constraints (Figure 6). This is a non-obvious finding that meaningfully advances the community's understanding of where existing methods fall short.

- **Automated constraint extraction works nearly as well as human annotation**: End-to-end evaluation using automatically identified constraints yields holistic success rates within ±0.02 of those using human-annotated constraints across four generation methods (Table 4), demonstrating that LEGO-EVAL can operate fully automatically without losing reliability.

- **Evaluation explanations enable practical scene refinement**: Using LEGO-EVAL's feedback for iterative refinement raises Holodeck's holistic success rate from 8.5% to 18.5% after three rounds, outperforming VLM-as-a-judge feedback (14.5%, Figure 7). This shows the framework has practical utility beyond scoring.

- **Well-curated benchmark with realistic complexity**: LEGO-BENCH's 130 instructions average 9.6 constraints each, span objects, architectural components, materials, and spatial relations (Figure 4), and are curated from real-world observations — making the benchmark representative of actual embodied-agent requirements.

## Weaknesses

### Fatal
None.

### Major

1. **Incomplete ablation of tool types does not support the claim that all three are "indispensable"**: The ablation study (Table 2) has three problems. First, removing Multimodal Reasoning tools alone (w/o M) degrades holistic F1 by only −0.04% — effectively zero — contradicting the paper's claim that all three types are necessary. Second, the effect of removing Environment Interaction tools alone (w/o E) is never reported; the largest drop (−24.90%) occurs only when E and M are removed jointly. Third, "tools returning list of scene components" are kept enabled in all conditions, so no ablation truly isolates a single tool type. The claim that "all three tools are indispensable" is an overstatement given the data; the results more accurately show that Environment Interaction and Textual Reasoning tools contribute meaningfully, while Multimodal Reasoning tools contribute negligibly at the holistic level. A proper full-factorial ablation (each type individually, all combinations) is needed to support the paper's strongest claims about the tool design.

2. **Figure 8 case study contains a contradictory verdict**: The LEGO-EVAL example in Figure 8 shows a green checkmark with "Valid ✓" alongside reasoning that says "the constraint cannot be satisfied." Since the constraint *is* unsatisfied (required objects are absent), the correct verdict is "Invalid ✗." The paper's text states "all methods achieve accurate judgments," which would be true only if the icon were ✗ not ✓. This is almost certainly a visualization error (✓ should be ✗), but as presented it undermines reader trust in the results. The authors must correct the figure and explain how the error occurred.

### Minor

1. **No confidence intervals for main results**: The 260 instruction-scene pairs in Table 1 are a modest evaluation set, yet no bootstrap confidence intervals or statistical significance tests are reported for F1, precision, recall, or Cohen's κ. While the gaps between methods are large, confidence intervals would help readers gauge the reliability of the results.

2. **Constraint-level extraction accuracy (precision/recall) is not reported**: Table 4 only shows end-to-end success rate differences between oracle and identified constraints. Reporting precision and recall of constraint identification by type would allow readers to understand whether certain constraint categories are systematically missed or misclassified, and would strengthen claims about extraction robustness.

3. **Error analysis of LEGO-EVAL failures is absent**: For the roughly 19% of cases where LEGO-EVAL disagrees with human judgment, the paper does not categorize failure modes (e.g., tool failure, argument selection error, validation misjudgment). Such analysis would guide future improvements and help calibrate reader expectations about where the method remains brittle.

### Trivial
- The VLM-as-a-judge baseline description lacks the exact prompt template used. This is acceptable for the main text (which is space-constrained) but should be included in the appendix.

## Nice-to-Haves
- Including a "w/o E" (Environment Interaction alone removed) condition in the ablation study would substantially strengthen the analysis.
- Bootstrap confidence intervals for Table 1 metrics.
- A held-out evaluation set (scenes not used for any form of development) to confirm generalization beyond LEGO-BENCH.

## Removed Points

These points were raised in the reviews but are removed for the reasons stated:

- **"VLM-as-a-judge baseline may be under-optimized"** — The paper uses three distinct state-of-the-art VLMs (GPT-4.1, GPT-o4-mini, Gemini 2.5 Pro) with four perspective images and self-consistency. All three show nearly identical low performance (0.38–0.40 F1, 0.05 κ), strongly suggesting the issue is fundamental 3D grounding failure, not prompt engineering. This criticism is speculative and unsupported.

- **"Missing confidence intervals"** — Kept as a minor weakness above, not removed.

- **"Holodeck object selection confounds generation comparison"** — The paper explicitly states the setup and reason for using Holodeck ("To enable fair comparison, we augment the latter three with Holodeck to produce full scenes"). This is transparent and standard practice. The critic's concern is noted in the nice-to-haves but is not a weakness.

- **"SceneEval Measurable Dataset comparison is unfair"** — The paper explicitly acknowledges SceneEval's limitation (cannot evaluate 41% of constraints) and evaluates it under two settings. This is standard methodology for handling incomparable methods. Not a weakness.

- **"Small dataset size (260 pairs)"** — The number is adequate for the purpose, with clear effect sizes. The paper is not claiming statistical subtlety; the gaps between methods are large. Moved to minor weakness (confidence intervals).

- **"Reproducibility: tool set only in appendix"** — The appendix is stripped by the parser; the paper references it. This is standard formatting for conference papers.

- **"Generation instructions unrealistically dense"** — The paper addresses this directly, noting user descriptions average 18.2 constraints. This is a strength, not a weakness.

- **"Missing related works"** — Per instructions, this is not a valid criticism from the reviewer standpoint.

- **All pure formatting/style/generic nitpicks** — Removed per instructions.

## Novel Insights

The most interesting observation that emerges across both reviews is the tension between the paper's impressive headline numbers (0.81 F1, 0.63 κ) and the thinness of the ablation evidence for the multi-tool design. The ablation shows that Multimodal Reasoning tools contribute at most 0.04% to holistic F1, which raises the question of whether the framework's core strength comes from the structured constraint decomposition + environment interaction tools rather than from the full tripartite tool design. This distinction matters because it affects how future researchers build on this work: the key insight may be that decomposing instructions into constraints and validating each with lightweight environment interaction tools (rather than throwing everything into a VLM) is what drives improvement, not the specific tool taxonomy proposed. The refinement experiment (Figure 7) offers a promising direction for using structured evaluation feedback as a training signal, which could have broader impact if integrated into RL-based generation pipelines.

## Suggestions

1. **Fix the Figure 8 contradiction immediately** — either change "Valid ✓" to "Invalid ✗" or, if the verdict is genuinely correct for the paper's logic, explain the reasoning more carefully. As it stands, the figure contradicts both the reasoning text and the paper's own claim of accurate judgments.

2. **Complete the ablation study** — add at least a "w/o E alone" condition, and ideally a full factorial design (each type individually, all pairwise combinations). Tone down the "indispensable" claim if the data doesn't support it; instead, characterize which tool types contribute most to which constraint categories.

3. **Add bootstrap confidence intervals** for the main evaluation metrics (Table 1) given the 260-sample evaluation set.

4. **Report constraint extraction precision/recall** broken down by constraint type, not just end-to-end SR differences.

5. **Include an error analysis** — categorize a sample of LEGO-EVAL's failures to help the community understand remaining bottlenecks.

## Score and Decision

I now calibrate using the retrieved anchors:

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| VIST3A (Oral) | kI27Niy4xY | 8.0 | Far stronger: clean methodology, strong novelty, rigorous experiments. Current paper is not in this league. |
| SpatialGenEval (Poster) | ddFN3lWpIr | 5.0 | Similar type of contribution (benchmark + evaluation method). SpatialGenEval's ablation and analysis are more thorough. Current paper slightly weaker. |
| Scenethesis (Poster) | SzhezVoaNB | 5.0 | Similar domain. Scenethesis has stronger execution on ablation studies. Current paper has clearer quantitative results but incomplete ablation. Roughly comparable but slightly weaker. |
| LEGO-Puzzles | jQh9SUrnev | 5.5 | Both are benchmark+evaluation papers. LEGO-Puzzles has more thorough analysis. Current paper has stronger methodological novelty (tool augmentation). Comparable quality. |
| PhysToolBench | jaYdn7RbRO | 4.5 | Similar profile: benchmark + method contribution with some methodological gaps. Current paper has cleaner quantitative evidence of improvement over baselines. Similar tier. |
| Agentic 3D Scene Gen | uiopHcWPRO | 4.4 | Similar domain, similar weaknesses (incomplete ablation). Current paper's main result is cleaner (F1 vs. VLM is a clearer win). Slightly stronger. |
| ReSpace | kE3ODBSDFQ | 3.5 | Weaker: missing baselines, unclear novelty. Current paper is stronger. |
| IL3D | 0oxkxG9cCo | 2.0 | Much weaker: primarily dataset aggregation with limited novelty. Current paper is substantially stronger. |

The paper makes a real contribution: a tool-augmented evaluation framework that clearly beats VLM baselines at a practically important task. However, the incomplete ablation study undermines a core claim about tool design, and the Figure 8 contradiction is a concrete error that must be fixed before the paper can be trusted. These are addressable issues, but in their current form they prevent acceptance.

**Score: 4.5** — The paper has solid contributions but contains weaknesses (particularly the incomplete ablation and the contradictory case study) that need resolution before it meets the bar for publication. The core contribution is salvageable and with proper revisions could become a strong paper.

**Decision: Reject**

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>