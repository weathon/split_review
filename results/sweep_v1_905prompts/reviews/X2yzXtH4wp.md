## Summary

This paper introduces Ambig-SWE, a benchmark for evaluating how LLM-based coding agents handle underspecified instructions in software engineering tasks. It extends SWE-Bench Verified by generating underspecified variants of GitHub issues and evaluates 6 models across three settings (Full, Hidden, Interaction) that form clean counterfactuals. The authors decompose underspecification resolution into three capacities — detection, questioning, and leveraging interaction — and evaluate each. Key findings include: interaction recovers significant performance (up to ~76% of the gap between hidden and full settings for the best model), models struggle to detect underspecificity reliably, and question-asking strategies vary substantially across models.

## Strengths

- **Decomposition of underspecificity resolution into three distinct capacities (detect, ask, leverage).** This structured evaluation framework (Sections 3–5) enables targeted diagnosis of where different models fail, which is more actionable than a single aggregate score. The paper demonstrates that strong overall performance can mask weaknesses in specific sub-capabilities (e.g., Qwen 3 Coder's high resolve rate but complete non-interaction in RQ2).

- **Construction of Ambig-SWE with clean counterfactual design.** Using GPT-4o to generate underspecified variants from fully-specified SWE-Bench Verified issues, with distributional analysis comparing generated to natural underspecified issues (Section 2.1, Figure 2). The three-setting design (Full / Hidden / Interaction) provides paired ground truth for causal measurement of interaction's impact — a significant methodological advantage over studying underspecification in the wild.

- **Systematic empirical findings about model interaction behavior.** The paper produces several nontrivial and actionable results: (a) the detection experiment (RQ2, Table 2) showing most models fail to distinguish well-specified from underspecified inputs, with Qwen 3 Coder at 100% FNR across all prompt conditions; (b) the navigational information analysis (Table 1) revealing Qwen 3 Coder's counterproductive rigid protocol-following; (c) the question-quality analysis (Section 5.3) identifying exploration-first vs. ask-first strategies with different efficiency tradeoffs.

- **Controlled experimental design with principled user proxy.** The GPT-4o user proxy receives the full issue and responds only with information explicitly present, saying "I don't have that information" for missing details (Section 2.2). This avoids the hallucination confound common in simpler interaction setups and cleanly isolates the agent's ability to detect and recover from missing information.

## Weaknesses

### Major

- **Unequal turn budgets confound cross-model comparisons in the Interaction setting.** Claude Sonnet 4 and Qwen 3 Coder are allocated up to 100 turns while all other models are capped at 30 (Section 3.1). The paper's justification ("greater reasoning and planning capacity") conflates model capability with additional computational runway. Since interaction consumes turns (asking questions, reading responses, adjusting plans), the 70-turn advantage could mechanically inflate interaction-based performance for these two models regardless of their inherent competence. This primarily affects the cross-model claim that "Claude Sonnet 4 attains the highest relative performance (89%)" — a result that may partially reflect the extra budget rather than better interaction capability. The within-model comparisons (Hidden vs. Interaction for the same model) remain valid, as each model operates under the same budget in both settings. The authors should either equalize budgets or provide control experiments showing the extra turns are not the driver of reported advantages.

- **Partial Hidden evaluation of Claude Sonnet 4 on 100/500 instances creates an asymmetric comparison.** The paper reports Sonnet 4's Hidden resolve rate as 40% based on a 100-instance subset, while all other models and settings use the full 500 instances (footnote 4). The paper does not specify whether Sonnet 4's Interaction and Full rates (61.4% and 68.0%) are computed on the same 100-instance subset or on all 500. If they differ, the Interaction vs. Hidden comparison for Sonnet 4 is invalid — performance differences could reflect instance difficulty. If they use the same 100 instances, the 40% figure carries wider error bars than other models' 500-instance results but is presented alongside them without caveats or confidence intervals. The claim that findings are "still statistically significant" does not address the composition mismatch. Given that Sonnet 4's Interaction-vs-Hidden comparison is central to the paper's headline result, this needs clarification and ideally a full 500-instance evaluation.

### Minor

- **The detection experiment (RQ2) operationalizes "interaction" as a proxy for "detection of underspecificity," conflating multiple behaviors.** False positives (interaction on full issues) and false negatives (no interaction on hidden issues) are treated as detection failures. However, a model might skip interaction on an underspecified issue because it chooses to explore the codebase independently (as the paper itself notes Sonnet 4 does extensively in Section 3.2), or might ask a question on a well-specified issue due to misreading or general caution. The paper partially addresses this through qualitative analysis in the Hidden setting but does not disentangle "chose not to ask" from "failed to detect" in the quantitative metrics (Table 2). As a result, the accuracy/FPR/FNR numbers may understate actual detection ability for models that pursue non-interactive information-seeking strategies.

- **The "recovery of performance" metric is framed as Interaction/Full without acknowledging an alternative that would produce different relative rankings.** The paper states models "recover up to 80% of the performance in the Full setting" (Interaction/Full). An alternative framing — (Interaction − Hidden) / (Full − Hidden) — measures recovery of the gap actually attributable to underspecificity. Under this alternative, Sonnet 4 achieves ~76% gap recovery and Sonnet 3.5 ~61%, so the ranking does not change (Sonnet 4 still leads), but the gap between models narrows substantially. The paper should acknowledge this framing choice to avoid potential overinterpretation. (Note: the harsh critic's claim that Sonnet 3.5's gap recovery is "approximately 78%" is factually incorrect based on the paper's numbers: (39.6−24.2)/(49.4−24.2) = 61.1%.)

### Trivial

- The claim that Deepseek "performs worse than its Hidden setting when file locations are absent" (Section 3.3) references a 4.62% resolve rate without navigational info vs. a 5.60% Hidden rate — a difference of ~1 percentage point that is likely within noise. The paper should note this is not a robust difference.

## Nice-to-Haves

- **Confidence intervals or standard errors** on resolve rates would help assess whether reported differences (e.g., Qwen's 52.38% vs. 55.43% with/without navigational info) are meaningful.
- **A voluntary-interaction condition** (interaction offered but not required) would isolate the effect of agent proactivity from the effect of being forced to ask, since the Interaction setting uses a compulsory-interaction prompt.
- **Quantitative classification of question strategies** (Section 5.3) across a larger sample would substantiate the qualitative taxonomy (behavioral vs. implementation vs. navigational questions).

## Removed Points

These points from the inputs were removed with justification:

- **Harsh critic's claim that "recovery of the gap" metric shows Sonnet 3.5 (~78%) outperforming Sonnet 4 (~76%):** The critic's numbers are factually wrong. Using the paper's published figures, Sonnet 3.5's gap recovery is 61.1% and Sonnet 4's is 76.4%. Removed as factually incorrect.
- **Criticism about the Hidden setting not specifying the prompt:** The paper explicitly states "We do not give any interaction-related instructions" (Section 2.3) and footnote 3 clarifies the contrast. Removed as already addressed.
- **Criticism about Deepseek "worse than its Hidden setting" not being directly supported:** The paper clearly provides numbers showing 4.62% < 5.60%, making the claim factually supported (though the difference is small). Removed as the critic mischaracterized the evidence as missing.
- **Request for inter-rater reliability on interaction coding:** The paper defines interaction as asking a user-facing question, which is a clear operationalization. Removed as a nitpick.
- **Formatting/style critiques and missing appendix content:** These are parser artifacts, not author errors.
- **Several generic strengths from the Strength Finder** (e.g., "this paper addressed an important problem") were dropped as superficial.

## Novel Insights

Beyond the paper's own contributions, the synthesis of reviews surfaces a tension not explicitly discussed: the paper's strongest quantitative claims (about which model benefits most from interaction) rely on comparisons that are partially confounded by design choices (turn budgets, subset evaluation), while its most robust contributions are qualitative and structural (the benchmark, the three-capability decomposition, the behavioral analyses in Sections 3.3 and 5.3). The paper would be strengthened by acknowledging this asymmetry — the headline performance numbers carry caveats, but the diagnostic framework and behavioral insights are more durable contributions that do not depend on perfect confound control.

## Suggestions

1. **Run a control experiment** equalizing turn budgets for all models at 30 (or re-evaluating Sonnet 4 and Qwen 3 Coder with a 30-turn cap in the Interaction setting) to determine whether the extra turns drive their reported advantages.
2. **Complete the Hidden evaluation of Sonnet 4** on all 500 instances, or clearly state which subset is used for each setting and provide confidence intervals.
3. **Add confidence intervals or error bars** to all main result tables (especially Figure 3 and Table 1) to enable assessment of which differences are meaningful.
4. **Clarify the detection metric** by analyzing trajectories of models that did not interact on hidden issues — distinguishing "codebase exploration" from "genuine failure to detect" would substantially strengthen RQ2.
5. **Report both Interaction/Full and (Interaction-Hidden)/(Full-Hidden)** for transparency on the recovery metric.

## Score and Decision

My round-1 bracket was (5.5, 7.0) based on comparing to anchors in the weak (≤3.5), middle (3.5–7.5), and strong (≥7.5) bands. Round 2 narrowed this by comparing to anchors inside that bracket: MINT (6.75), RefactorBench (6.50), and SWE-bench (6.25). The paper under review is comparable to MINT in overall quality (both study interaction in LLM-based problem solving, both have clean experimental design, both have some methodological concerns), slightly above RefactorBench (which has fewer instances and models), and slightly above SWE-bench (which is foundational but has narrower evaluation). It sits below Active Task Disambiguation (7.33) which proposes a novel method with theoretical grounding. I therefore place it at 6.5 — a solid empirical contribution with a useful benchmark and interesting findings, but with methodological concerns that should be addressed.

### Anchors consulted
- BltaWJZMeR (DataSciBench, 3.20): Round 1 weak anchor. Less relevant topic, lower quality benchmark paper.
- oWm80iR1m9 (SOP-Agent, 3.00): Round 1 weak anchor. Different topic.
- ly10tMV6cD (Structure-Rich Text Benchmark, 3.25): Round 1 weak anchor.
- qit4pa6PpY (Instruction-following Benchmark, 3.00): Round 1 weak anchor.
- JAMxRSXLFz (Active Task Disambiguation, 7.33): Round 1 middle anchor. Method paper on similar topic. Ambig-SWE is below this — less novelty though more realistic evaluation.
- hREMYJ5ZmD (Agents Help Agents, 4.25): Round 1 middle anchor. Less relevant.
- c2C2NQKjZw (Codev-Bench, 4.25): Round 1 middle anchor.
- Zk9guOl9NS (What Makes LLMs Reason in Code Gen, 7.00): Round 1 middle anchor. Empirical study similar in style. Ambig-SWE is slightly below.
- 6s5uXNWGIh (MLE-Bench, 8.00): Round 1 strong anchor. Higher quality benchmark paper.
- YrycTjllL0 (BigCodeBench, 9.00): Round 1 strong anchor.
- OI3RoHoWAN (GenSim, 8.00): Round 1 strong anchor.
- or8mMhmyRV (MaestroMotif, 7.75): Round 1 strong anchor.
- sf1u3vTRjm (ML-Bench, 5.75): Round 2 anchor. Comparable area, slightly below Ambig-SWE.
- VTF8yNQM66 (SWE-bench, 6.25): Round 2 anchor. Foundational SWE benchmark. Ambig-SWE is comparable but narrower.
- 6z4YKr0GK6 (ScienceAgentBench, 6.00): Round 2 anchor. Similar type of contribution. Ambig-SWE is slightly above.
- riTiq3i21b (SWE-bench Multimodal, 5.00): Round 2 anchor. Extension of SWE-bench similar in spirit. Ambig-SWE is above.
- NiNIthntx7 (RefactorBench, 6.50): Round 2 anchor. Similar benchmark paper. Ambig-SWE is comparable.
- zAdUB0aCTQ (AgentBench, 6.20): Round 2 anchor. Broader agent benchmark. Ambig-SWE is comparable.
- MMwaQEVsAg (Commit0, 6.67): Round 2 anchor. Code generation benchmark. Ambig-SWE is comparable.
- jp3gWrMuIZ (MINT, 6.75): Round 2 anchor. Multi-turn interaction benchmark. Ambig-SWE is comparable but slightly below due to methodological concerns.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>