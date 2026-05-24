Now I have all the information I need to write the consolidated review.

## Summary

This paper introduces Ambig-SWE, an underspecified variant of SWE-Bench Verified (500 issues), and evaluates six LLM agents across three settings—Full (fully specified), Hidden (underspecified, no interaction), and Interaction (underspecified with simulated user)—to study how agents detect missing information, ask clarification questions, and leverage interaction. The core finding is that interaction recovers up to 74% of performance lost to underspecification, with proprietary models recovering ~80% of their Full-setting resolve rates, yet most models default to non-interactive behavior absent strong prompting and prompt engineering alone is insufficient for reliable detection.

## Strengths

1. **Ambig-SWE provides a controlled testbed for underspecification in realistic agentic code tasks.** The dataset creates paired fully-specified and underspecified variants of SWE-Bench Verified issues (Section 2.1), enabling causal measurement of how missing information and interaction affect agent performance—something not possible with natural underspecified issues that lack ground-truth specifications.

2. **The three-setting design (Full, Hidden, Interaction) enables structured attribution of performance gaps.** This decomposition (§2.3, Figure 3) cleanly separates the cost of underspecification from the benefit of interaction and from residual deficiencies in fully-specified performance, going beyond end-to-end accuracy on SWE-Bench.

3. **Interaction recovers substantial performance: all models improve significantly** (Wilcoxon, p<0.05) from Hidden to Interaction settings, with proprietary models recovering ~80% of the Full-setting resolve rate (Section 3.1-3.2, Figure 3). Claude Sonnet 4 achieves the highest absolute Interaction performance (61.4%). This directly supports the paper's central claim about the value of interaction.

4. **The decomposition into three capacities (detection, clarification, integration) is a useful analytical framework** (§4, §5, §3 respectively). This enables finer-grained insights than SWE-Bench accuracy alone, such as: Qwen 3 Coder exhibits 100% false-negative rate across all prompt conditions (Table 2), and Claude Sonnet models achieve comparable information gain with ~50% fewer questions than Qwen through exploration-first strategies (Section 5.2).

5. **Systematic multi-model evaluation across six proprietary and open-weight models** reveals capability scaling effects and specific behavioral patterns (e.g., Deepseek's dependence on navigational details, Llama's low question specificity, Qwen's rigid protocol-following), providing concrete diagnostic information for future agent design.

## Weaknesses

### Fatal

None.

### Major

1. **Claude Sonnet 4's Hidden setting is evaluated on a different subset (100/500 instances) than its Interaction and Full settings (500/500).** Footnote 4 (page 4) acknowledges this, and the paper claims findings remain significant. However, the headline "89% relative performance recovery" is computed as (Interaction − Hidden)/(Full − Hidden) using a Hidden value from 100 instances and Interaction/Full values from (likely) all 500 instances on an overlapping instance pool. Cross-setting comparisons for this model are thus based on potentially non-identical instance distributions. While the paper provides statistical support for the significance of the Hidden→Interaction gain, the magnitude of the recovery rate itself is not directly comparable across settings for this model.

2. **The detection evaluation (RQ2) operationalizes "detection" as whether the model chooses to interact, conflating detection with the decision to act on detection.** In Section 4.1, models are presented with either fully-specified or underspecified inputs and the system tracks whether they interact. A model could correctly identify missing information but still not interact—because it defaults to non-interactive behavior, because it can infer the missing detail from the codebase, or because the prompt insufficiently encourages interaction. The paper's own finding that "models default to non-interactive behavior without explicit encouragement" (Section 1) confirms this confound. The strong encouragement condition partially mitigates the concern, but the conclusions in Section 4.3 ("LLMs struggle to detect missing information even in obvious cases") extend beyond what the experimental design cleanly measures—it measures *interaction behavior* under different prompt conditions, not detection *ability* per se. The accuracy/FPR/FNR metrics reflect this conflation.

### Minor

3. **The synthetic underspecification may differ qualitatively from natural underspecification.** The distributional analysis (Section 2.1) reveals that generated underspecified issues remove code snippets and error messages more aggressively than natural underspecified issues, and no features are more common in generated than in natural issues. The paper argues these differences likely don't affect agent performance (since agents cannot access external links, etc.), but this is an untested assumption. No calibration experiment is provided to show that performance on synthetic underspecification correlates with performance on natural underspecified issues. This limits external validity claims for the benchmark.

4. **Turn budget differs across models in the Interaction setting** (Claude Sonnet 4 and Qwen 3 Coder get 100 turns vs. 30 for others, Section 3.1). The paper justifies this as accounting for "greater reasoning and planning capacity," but it risks confounding turn allowance with model capability. The observed performance gaps between these models and others could partly reflect unequal interaction budgets. The analysis does not control for or ablate turn count.

5. **The user proxy (GPT-4o constrained to the issue text) is an unusually cooperative and bounded respondent** (Section 2.2). It only provides information explicitly present in the full issue and says "I don't know" otherwise. Real users may volunteer irrelevant information, hedge, give partial answers, or fail to respond. The paper acknowledges this as a limitation (Section 7) but does not probe robustness to less cooperative proxies. The results thus reflect interaction with an idealized user.

6. **The analysis of navigational vs. informational information (Section 3.3, Table 1) is purely correlational.** Models that request navigational details may differ on other confounding dimensions (e.g., they may be deployed on systematically harder issues, or be more thorough overall). The finding about Qwen 3 Coder's performance worsening with navigational information could reflect selection effects rather than a causal effect of navigational information.

7. **Question quality metrics (cosine distance and LLM-as-judge scores from Section 5) are not validated against task outcomes.** The paper shows a disconnect between information gain and resolve rates, but does not establish what these metrics actually capture about task-relevant information. LLM-as-judge scores cluster around 4/5 for capable models (Figure 6), suggesting ceiling effects, and cosine distance differences are small (0.13–0.18). Whether either metric reliably measures "question quality" is unclear.

### Trivial

None.

## Nice-to-Haves

- A calibration experiment running a small set of models on naturally underspecified SWE-Bench issues (e.g., the ones pruned from Verified) would strengthen external validity claims for the benchmark.
- Running the Interaction setting for Claude Sonnet 4 on the same 100-instance subset as Hidden would directly address the cross-setting comparability concern.
- A controlled experiment asking models to rate whether a description is missing information (separate from the interaction decision) would provide a cleaner detection measure.
- Analyzing whether models actually *use* the information obtained through interaction (e.g., measuring whether final patches incorporate specific details from user responses) would deepen the integration analysis.
- Propensity score matching or instrumental variable approaches could strengthen the causal claim about navigational information's effect.

## Removed Points

- **"Previous work claim not cited with specific examples"**: The paper cites Chen et al., 2025 and Kim et al., 2024 in support of this claim (Section 1, line 35). The critic appears to have missed these citations. REMOVED (factually wrong).
- **"Multiple interdependent gaps not formally categorized"**: The critic asserts this bullet point "is never formally categorized or measured." This is a framing point in the introduction to motivate the work, not a claimed contribution. The paper's dataset does introduce one level of underspecification consistently across all items. REMOVED (strawman).
- **"Section 7 doesn't discuss Claude subset issue"**: The limitations section is not expected to repeat every footnote-level acknowledgment. The paper addresses this in the experimental setup. REMOVED (too minor).
- **"Pure formatting/style nitpicks"**: None in the original reviews, but the parser-introduced formatting artifacts (image descriptions replacing figures, garbled text) should be ignored per instructions.
- **Various generic "could improve" suggestions** from the Strength Finder's "Missing Parts" section that go beyond the paper's stated scope (training a dedicated model, probing less cooperative users, adding complete trajectories). Moved to Nice-to-Haves.
- **Several strength finder items were generic/superficial** (e.g., "the paper addresses an important problem") and were dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the methodological tension in the detection experiment (conflation of detection with interaction decision) and the subset comparability issue—both are genuine concerns but were already partially acknowledged in the paper.

## Suggestions

1. **Address the Claude Sonnet 4 subset issue.** Either run Hidden on the same 500 instances (if feasible) or carefully document the subset selection, report confidence intervals for the recovery rate, and verify robustness by showing results hold when Claude Sonnet 4's Hidden is evaluated only on the 100-instance subset for all settings.

2. **Cleanly separate detection from interaction in RQ2.** Add a controlled experiment where models are asked to explicitly rate whether a task description is missing information (without an interaction channel), or use a two-stage design where the detection judgment is elicited before the interaction decision.

3. **Add external validity evidence for synthetic underspecification.** Even a modest calibration experiment (e.g., 20-30 naturally underspecified issues with human-provided ground truth) showing that performance rankings transfer from synthetic to natural underspecified inputs would substantially strengthen the benchmark's credibility.

4. **Run an ablation controlling for turn count.** Show that the main results for Claude Sonnet 4 and Qwen 3 Coder hold (at least directionally) when restricted to the same 30-turn budget as other models.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Active Task Disambiguation (JAMxRSXLFz) | 7.33 | Stronger methodology (cleaner detection framing, formal definitions) but simpler tasks (20 questions, HumanEval). This paper tackles more realistic agentic complexity but has weaker detection evaluation. |
| Tau-bench (roNSXZpUDN) | 6.50 | Similar benchmark contribution for agent-user interaction. Tau-bench has cleaner evaluation metrics (pass^k) but narrower domain. Comparable quality. |
| RefactorBench (NiNIthntx7) | 6.50 | Similar benchmark paper with 100 handcrafted tasks. Both papers provide useful decomposition of agent capabilities. This paper evaluates more models. Comparable quality. |
| Commit0 (MMwaQEVsAg) | 6.67 | More ambitious benchmark (library-from-scratch) but fewer baseline agents. Both papers address interaction/feedback. Comparable quality. |
| SWE-bench Multimodal (riTiq3i21b) | 5.00 | Similar benchmark extension of SWE-Bench, but with less insightful analysis of agent behavior. This paper's decomposition framework and analysis are stronger. |
| Curse of Instructions (R6q67CDBCH) | 3.50 | Much weaker evaluation methodology and trivial extensions of existing work. This paper is substantially stronger. |

The paper sits in the 6.0–6.5 band. It makes a genuine contribution with a useful benchmark and insightful decompositional analysis of agent interaction behavior. The main weaknesses—the Claude Sonnet 4 subset comparability and the detection/interaction conflation in RQ2—are real but do not invalidate the core findings about interaction recovery, model comparisons, or question quality analysis. These are addressable in a revision. The paper is clearly above the rejection threshold but not at the "strong accept" level due to these methodological concerns.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>