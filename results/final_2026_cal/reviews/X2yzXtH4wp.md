Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces **Ambig-SWE**, an underspecified variant of SWE-Bench Verified, and evaluates how six LLM-based agents handle incomplete instructions across three capacities: detecting underspecification (RQ2), asking targeted clarification questions (RQ3), and leveraging interaction to improve task performance (RQ1). The key contributions are a structured three-capacity decomposition that enables targeted diagnosis, a controlled benchmark for studying interaction in code-generation, and empirical findings showing that interaction can recover substantial performance (up to 74% improvement) but that most models struggle with detection and vary significantly in question quality and integration. The work provides a useful diagnostic framework for future agent design.

## Strengths

- **Three-capacity decomposition provides a principled diagnostic structure.** Breaking underspecification resolution into detection (RQ2), question quality (RQ3), and information integration (RQ1) is a genuine conceptual contribution. The paper shows it pays off — e.g., Qwen 3 Coder achieves the highest information extraction (0.179 cosine distance) yet fails catastrophically at detection (100% FNR under all prompts), a finding that a single accuracy metric would mask.

- **Quantitative evidence that interaction recovers performance lost to underspecification is clear and compelling.** Figure 3 shows Claude Sonnet 4 rises from 40% to 61.4% (53.5% improvement), Sonnet 3.5 from 24.2% to 39.6% (63.6%), and Haiku 3.5 from 13.4% to 26.8% (100%). These gains are statistically significant across models (Table 4), directly supporting the core claim that interaction helps.

- **The navigational vs. informational detail analysis (Table 1) reveals model-specific integration failures.** Claude Sonnet 3.5 achieves 59.52% resolve rate with navigational info but only 37.94% without, while Qwen 3 Coder paradoxically worsens (52.38% vs. 55.43%) when given file locations — a nuanced finding that goes beyond "more info helps."

- **Qualitative characterization of question-asking strategies (Section 5.3) is the strongest part of RQ3.** The three identified strategies (volume-oriented, exploration-first, template-based) with concrete examples from Figure 4 provide actionable insights — Claude Sonnet models achieve similar information gain with 50% fewer questions by exploring the codebase first.

- **Distributional difference analysis of generated vs. natural underspecification (Section 2.1) is transparent and honest.** The paper acknowledges that synthetic issues differ from natural ones (more concrete technical details, reproducibility information in natural ones), then argues which differences likely matter for agent performance.

## Weaknesses

### Major

- **RQ2's detection experiment conflates instruction-following with underspecification detection.** The paper operationalizes "detection of missing information" as whether the agent chooses to interact when given different prompt encouragement levels. But the decision to interact is heavily mediated by instruction-following ability. Qwen 3 Coder's 100% failure to interact under *all* prompts (Table 2) is more plausibly a failure to follow the interaction instruction than a detection failure. The paper itself notes "Sonnet models outperform Haiku, likely due to superior instruction following capability" (Section 4.3), which acknowledges the confound without fixing it. The experiment should have separated the detection judgment from the interaction decision — e.g., asking "Do you have enough information?" before any action, then separately evaluating whether interaction is initiated. This weakens a central claim the paper advertises in the abstract and introduction.

### Minor

- **The Hidden vs. Interaction comparison conflates the benefit of information access with the effect of different prompts/system instructions.** The Hidden setting provides no interaction instructions; the Interaction setting explicitly prompts the agent to interact. The paper acknowledges this (Section 2.3: "models do not interact without an explicit prompt") and the 74% improvement claim is about the overall "interactivity" package. Still, readers should be aware that the performance gap cannot be cleanly attributed to *information gain alone* — it includes the behavioral effect of being told to interact. A cleaner control would use the same interaction-aware prompt in both conditions but disable the interaction channel in Hidden.

- **No replication runs or variance reporting for resolve rates.** All resolve rates (Figure 3) are point estimates from single runs. LLM-based agents are stochastic; without confidence intervals or at least bootstrap estimates, the reader cannot tell whether reported differences (e.g., Claude Sonnet 3.5 at 39.6% vs. Haiku 3.5 at 26.8% in Interaction) are robust. This is a standard concern for cost-intensive SWE-Bench evaluations, but worth noting.

- **Claude Sonnet 4 and Qwen 3 Coder are allocated 100 interaction turns vs. 30 for other models (Section 3.1).** The paper justifies this by their "greater reasoning and planning capacity," but this asymmetry introduces a confound: higher resolve rates for these models in the Interaction setting could partly reflect more environment steps, not better interaction quality.

- **The cosine distance metric (RQ3) is not validated against human judgment of information gain or against task success.** It collapses all semantic changes into a single number, but a model could ask questions that change the embedding even if the answer is not useful. The paper acknowledges this as a limitation (Section 7), but it weakens the metric's weight as evidence.

- **LLM-as-judge scores cluster around 4/5 for all capable models (Figure 6), suggesting ceiling effects.** This limits the metric's ability to distinguish meaningful differences in question quality among stronger models.

- **No hyperparameter details (temperature, top-p, sampling parameters) reported for any model.** These affect stochasticity and could influence interaction propensity. Similarly, OpenHands configuration details (timeout, max actions without user interaction) are absent.

### Trivial

- None that survive filtering. (Style/formatting nitpicks are parser artifacts.)

## Nice-to-Haves

- **Validate a sample of Ambig-SWE issues against human developers:** Have experienced SWE practitioners rate the naturalness and severity of synthetic vs. naturally-occurring underspecified issues. This would directly address the construct validity concern the paper honestly raises.
- **Separate detection judgment from interaction decision in RQ2**, as described in the Major weakness above.
- **Report the number of clarification rounds per resolved issue** as a user-burden metric, complementing the total-step analysis in Section 3.2.
- **Validate the cosine distance metric** by showing that higher cosine distance correlates with higher resolve rate conditional on other factors.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

1. *"Claude Sonnet 4 evaluated on only 100/500 instances in Hidden setting undermines comparison"* — The paper transparently notes this (footnote 4) and states findings remain statistically significant. The paper's core comparisons involve Interaction setting which uses all 500 instances.
2. *"Missing related work"* — Per instructions, I cannot verify the existence of missing citations.
3. *"Performance difference not supported with p-values in main text"* — The paper references Table 4 in the appendix. The appendix (stripped by parser) contains the values. Per rules, I cannot penalize for missing appendix content.
4. *"Navigational vs. informational analysis not pre-registered"* — Pre-registration is not standard for this type of empirical work.
5. *"User proxy prompt should be in main text"* — Per missing-appendix rules, the prompt exists in the original submission appendix.
6. *"Qwen 3 Coder's rigidity is under-analyzed"* — The paper discusses this in detail at multiple points (Sections 3.3, 4.2, 5.3).
7. *"The claim that 74% may be misrepresentative"* — The paper is transparent that Hidden has no interaction instructions, and the 74% figure accurately describes the comparison it claims to make (Interaction vs. Hidden/Non-interactive).

## Novel Insights

The observation about **exploration efficiency** (Section 5.3) synthesizes across all three experiments in a way none of the individual RQs fully captures: models that explore the codebase first before asking questions achieve comparable information gain with ~50% fewer questions, and these same models (Claude Sonnet) also show better integration of navigational information. This suggests that question quality and codebase understanding are interdependent — effective questioning may depend on knowing what you can learn independently. The Qwen 3 Coder paradox — highest information extraction yet performance degradation with navigational info — further reinforces that information *acquisition* and information *integration* are separable bottlenecks. Together these paint a richer picture than the paper's own three-capacity framing: the capacities interact, and deficits in one (e.g., rigid task protocols) can negate strengths in another (e.g., good question generation).

## Suggestions

1. **For RQ2, run a control experiment** where the model is first asked "Do you have enough information to proceed?" (yes/no) in a neutral way, before any interaction channel is opened. This separates detection ability from the propensity to follow interaction instructions, directly addressing the major confound.
2. **Add bootstrap confidence intervals** to the resolve rates in Figure 3 by resampling the 500 instances. This is computationally cheap and would significantly strengthen the paper's empirical rigor.
3. **Report temperature and sampling parameters** for all evaluated models to enable replication.
4. **For the cosine distance analysis**, add a per-instance correlation analysis showing whether higher distance correlates with higher resolve rate, to ground the metric in task outcomes.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| Gxw1EDSm9S (Auto-SWE-Bench) | 1.50 | R1 (weak) | Much weaker — flawed benchmark construction, rejected |
| Jv7iRfMxkE (Lita) | 3.33 | R1 (weak) | Weaker — narrow contribution, rejected |
| 0xpakqqTbe (RExBench) | 3.00 | R1 (weak) | Weaker — limited contribution, withdrawn |
| bkjKnO9s7T (SCUBA) | 4.80 | R1 (mid) | Weaker — narrower domain, less conceptual novelty |
| rtcX9qOBaz (VitaBench) | 5.50 | R2 (mid) | Comparable — similar interactive-agent-benchmark framing, similar LLM-on-LLM concerns |
| KjgyAm383Z (EXP-Bench) | 6.00 | R1 (mid), R2 (mid) | Comparable — benchmark + agent eval paper with similar quality and review scores |
| XrP8dp1rCg (AppForge) | 6.00 | R2 (mid) | Comparable — end-to-end software development benchmark, similar level of contribution |
| VKGTGGcwl6 (LLMs Get Lost) | 8.00 | R1 (strong) | Stronger — cleaner experimental design, broader model coverage, tighter causal identification |

**Round 1 bracket:** 5.0–6.5

**Narrowing rationale:** The paper sits above SCUBA (4.80) — its three-capacity decomposition has more conceptual novelty and the analysis is deeper. It is comparable to EXP-Bench (6.00) and AppForge (6.00) — all introduce benchmarks with solid contributions but have methodological concerns (LLM-as-judge, construct validity, evaluation confounds). The RQ2 detection confound and lack of replication runs prevent it from reaching the 7+ tier occupied by papers like "LLMs Get Lost." The paper's real contributions (decomposition, benchmark, qualitative analysis) justify a solid acceptance-level score, placing it at the upper end of the mid-range.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>