Now I have all the information I need. Here is my consolidated final review.

---

## Summary

This paper introduces *Ambig-SWE*, an underspecified variant of SWE-Bench Verified designed to evaluate how LLM-based code agents handle incomplete task descriptions. It decomposes underspecificity resolution into three capacities—detection of missing information, quality of clarification questions, and task completion through interaction—and evaluates six proprietary and open-weight models across three experimental settings (Full, Hidden, Interaction). The key finding is that interaction can substantially recover performance lost to underspecificity (e.g., Claude Sonnet 4 achieves 89% relative performance vs. its fully-specified setting), but most models rarely initiate clarification unprompted and struggle to distinguish well-specified from underspecified inputs.

## Strengths

- **Decomposition of underspecificity into three measurable sub-capacities (detection, clarification, task integration).** Rather than treating underspecificity as a monolithic problem, the paper designs targeted experiments for each dimension (RQ1 in §3, RQ2 in §4, RQ3 in §5), enabling fine-grained diagnosis of where different models fail. This structured evaluation goes beyond prior work that typically considers only a single missing detail (Chen et al., 2025; Kim et al., 2024).

- **Clear quantitative evidence that interaction recovers substantial performance lost to underspecificity.** Figure 3 shows significant gains across all models from Hidden to Interaction settings, with Wilcoxon signed-rank tests confirming significance. The finding that Claude Sonnet 4 achieves 89% relative performance (61.4% vs. 68.0%) and that proprietary models recover up to 80% of the Full-setting gap (§3.2) is well-supported.

- **Granular analysis of navigational vs. informational information acquisition (Table 1) with differential impact across models.** Disaggregating whether models ask for file locations vs. behavioral details reveals striking patterns: Qwen 3 Coder's performance actually *decreases* when given navigational information (55.43% → 52.38%) due to rigid protocol-following, while Claude Sonnet 3.5 improves substantially (37.94% → 59.52%). This is a novel and actionable insight for agent design.

- **Qualitative analysis of question-asking strategies (§5.3, Figure 4) revealing distinct failure modes.** The identification of exploration-first (Claude), immediate-asking (Deepseek/Qwen), and rigid-template (Haiku) strategies, along with the finding that Qwen extracts the most information (0.179 cosine distance) yet requires 50% more questions than Claude Sonnet 4 without proportional gains, offers concrete guidance for training better interactive agents.

- **Identification of Qwen 3 Coder's complete non-responsiveness to interaction prompts (100% FNR across all conditions, Table 2) and its rigid protocol-following behavior.** This documents a concrete failure mode not previously characterized in the literature.

## Weaknesses

### Fatal

None.

### Major

- **RQ2 (Detection) conflates detection capability with interaction behavior, invalidating the paper's strongest claim about detection.** The experiment measures whether models *choose to interact* when given full vs. underspecified issues, then interprets this as detection ability (Section 4: "we evaluate whether LLMs can detect missing information"; Table 2: "underspecificity detection"; §4.3: "models struggle to detect missing information even in obvious cases"). However, a model could correctly identify that information is missing yet not act on it (e.g., Qwen 3 Coder at 100% FNR—we cannot know whether it detects underspecificity, only that it refuses to ask questions). Similarly, Llama 3.1's high interaction rate on full issues (FPR up to 0.95) may reflect over-triggered detection, not "arbitrary" behavior. The metric (interaction yes/no) is not a valid measure of the construct (detection ability). Fixing this requires either (a) a separate binary classification experiment where models are directly asked to judge underspecificity, or (b) reframing RQ2 as a study of *interaction initiation behavior* and tempering all detection-related claims. Because the abstract's headline claim that "models struggle to distinguish between well-specified and underspecified instructions" rests partly on this experiment, this weakness is substantive.

### Minor

- **Unequal turn budgets (up to 100 turns for Claude Sonnet 4 and Qwen 3 Coder vs. 30 for others) compromise clean cross-model comparisons.** The paper acknowledges this (§3.1) but does not discuss how the asymmetric budget could affect conclusions. For example, Claude Sonnet 4 increases steps from 65 to 75 when interaction is enabled (§3.2)—this is still within a 30-turn budget, suggesting the extra allocation may not matter much for this model. But Qwen 3 Coder also uses ~65 steps, and the claim about its "rigid" behavior using "extra turns" might be partially confounded. Reporting results with a common limit or a sensitivity analysis would strengthen the paper.

- **The "up to 74% improvement" claim in the abstract and introduction does not match the reported data.** The abstract states interaction boosts performance "up to 74% over the non-interactive settings." Computing relative improvements from Figure 3 yields: Claude Haiku 3.5 (100%), Claude Sonnet 4 (53.5%), Qwen (18.0%), Claude Sonnet 3.5 (63.6%), Deepseek (32.1%), Llama (50.0%). None is 74%. Gap-recovery calculations also do not cleanly yield 74%. This numerical imprecision does not undermine the core finding (interaction helps substantially) but signals a need for more careful reporting of central numbers.

- **Dataset validity: the generated underspecified issues lack human validation for realism.** The paper compares generated issues to natural ones via distributional analysis (§2.1) but does not have human annotators rate whether the synthetic underspecification is ecologically valid (e.g., whether real users would write such descriptions). This is not a fatal gap—the authors reasonably justify not using natural underspecified issues due to missing ground truth—but a small human annotation study (e.g., 50–100 issues rated for plausibility and degree of underspecificity) would strengthen confidence in the dataset's representativeness.

### Trivial

- The Wilcoxon signed-rank test results are referenced but exact p-values or effect sizes are not reported in the main text (Table 4 is in the stripped appendix).
- The cosine distance metric (§5.1) may conflate information gained from interaction with information gained from codebase exploration that happens between questions; this is acknowledged only implicitly.

## Nice-to-Haves

- A cost/efficiency analysis (tokens, time, API calls) comparing the Interaction and Hidden settings would help practitioners assess the practical trade-offs of interaction.
- A systematic categorization of question types (e.g., "what file?", "expected behavior?", "stack trace?") with frequencies across models would strengthen RQ3 beyond the three qualitative examples in Figure 4.
- Including a state-of-the-art open-weight model like Mistral Large or a recent Qwen variant would broaden the open-weight coverage.

## Removed Points

- **"Reproducibility: undisclosed hyperparameters / missing appendix content."** The parser strips appendix sections; these exist in the original submission. REMOVED per hard rules.
- **"Formatting/style nitpicks."** These are parser artifacts or irrelevant to scientific content. REMOVED per hard rules.
- **"Missing related work."** The review cannot verify the existence of unmentioned related work without external knowledge. REMOVED per hard rules.
- **"Typos/spelling/grammar issues."** These are parser artifacts in the extracted text, not author errors. REMOVED per hard rules.
- Several minor weaknesses from the harsh critic about "strawman" concerns or areas outside the paper's stated scope (e.g., demanding the paper address real-user interaction beyond the proxy). REMOVED or moved to Nice-to-Haves.
- **Strength Finder strengths that are generic** (e.g., "paper addresses an important problem"). These lack specific evidence. REMOVED.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix RQ2's construct validity.** The simplest fix: reframe RQ2 as a study of *interaction initiation behavior in response to ambiguity* rather than *detection ability*, and remove all claims about models "detecting" or "failing to detect" underspecificity. Alternatively, run a separate binary classification experiment asking models directly whether an issue is underspecified. Without this change, the paper's strongest negative claim is unsupported.
2. **Clarify the "74%" number.** Either correct it to match the reported data, or explicitly state the calculation method that produces it.
3. **Add a brief discussion** of how the unequal turn allocation might affect comparisons, and ideally report a sensitivity analysis or results under a common budget.
4. **Include a small human evaluation** of the generated underspecified issues (e.g., 50 issues rated for plausibility and degree of missing information) to strengthen dataset validity claims.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Three broad queries returned anchors in weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands. The middle-band anchors were most relevant: Active Task Disambiguation (7.33), ScienceAgentBench (6.00), Codev-Bench (4.25), AgentBench (6.20). The paper's profile—benchmark + evaluation + analysis, with a notable weakness—placed it between 4.5 and 7.0. Initial bracket: **5.5–7.0**.

**Round 2 (Narrowing):** Two queries targeting 5.0–7.5 retrieved SWE-bench (6.25), ScienceAgentBench (6.00), Commit0 (6.67), LiveCodeBench (6.25), OpenRCA (6.75), and previously seen anchors. I read SWE-bench (6.25) in full. Ambig-SWE is less foundational than SWE-bench but adds a novel underspecificity dimension and deeper analysis of interaction behavior. It is comparable to ScienceAgentBench (6.00) in evaluation quality and stronger on actionable insights, but held back by the RQ2 construct validity issue.

**Final score: 6.0.** The paper makes a genuine contribution (a useful benchmark, a structured decomposition framework, and several concrete empirical findings), but the RQ2 framing problem and the numerical imprecision in the headline 74% claim keep it from the upper part of the bracket. The core weakness is fixable; the strengths are real.

**Anchor list:**
- DataSciBench (3.20, R1): weaker paper; Ambig-SWE is substantially stronger.
- SOP-Agent (3.00, R1): weaker paper.
- D2Coder (1.67, R1): much weaker.
- Codev-Bench (4.25, R1): comparable submission quality but Ambig-SWE has more analysis depth.
- Active Task Disambiguation (7.33, R1/R2): stronger method contribution and cleaner evaluation; Ambig-SWE has more realistic benchmarks but a significant design flaw.
- ScienceAgentBench (6.00, R1/R2): comparable; both are benchmark+evaluation papers with careful design, but Ambig-SWE provides more actionable insights.
- AgentBench (6.20, R1): slightly higher; broader scope but less deep analysis per task.
- SWE-bench (6.25, R2): more foundational; Ambig-SWE builds on it with a new dimension.
- Commit0 (6.67, R2): slightly stronger on benchmark design; different task (library generation).
- LiveCodeBench (6.25, R2): comparable; contamination-free focus is a strength, but Ambig-SWE studies a more interesting behavioral question.
- OpenRCA (6.75, R2): stronger on benchmark realism (enterprise systems); Ambig-SWE has more analytical depth.
- MLE-Bench (8.00, R1): stronger overall.
- BigCodeBench (9.00, R1): stronger overall.
- Spider 2.0 (8.00, R1): stronger overall.
- Cybench (8.67, R1): stronger overall.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>