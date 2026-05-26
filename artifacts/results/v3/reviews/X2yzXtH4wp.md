## Summary

This paper introduces Ambig-SWE, a benchmark for studying how LLM agents handle underspecified instructions in software engineering tasks. It pairs 500 SWE-Bench Verified issues with GPT-4o-generated underspecified variants, and decomposes the problem into three capacities: detecting underspecificity, asking clarifying questions, and leveraging interaction to resolve tasks. The evaluation covers proprietary and open-weight models across these dimensions. The core finding—that interaction significantly improves performance on underspecified inputs—is supported by within-model comparisons. The paper also provides a qualitative analysis of interaction strategies (exploration-first, question quality vs. quantity, navigational vs. informational cues) that yields actionable insights for agent design.

---

## Strengths

1. **Systematic decomposition of underspecification handling into independently evaluated sub-capabilities.** The three-part breakdown (detection in RQ2, clarification quality in RQ3, integration through interaction in RQ1) goes beyond end-to-end accuracy and enables targeted diagnosis of where models fail. This is explicitly stated as Contribution 2 and is well-motivated by the paper's design (Sections 3–5).

2. **Controlled benchmark dataset with paired ground truth.** Ambig-SWE creates underspecified variants of fully-specified SWE-Bench issues, preserving a verified correct specification for each instance. This enables causal measurement of interaction impact—an improvement over studying naturally underspecified issues that lack paired complete specifications (Section 2.1). The dataset provides a reusable testbed for future work.

3. **Qualitative insights into interaction strategies that are robust and practically useful.** The analysis in Section 5.3 identifies three distinct question-asking strategies and their tradeoffs. The finding that Claude Sonnet 4 achieves comparable information gain to Qwen 3 Coder (0.171 vs. 0.179 cosine distance) with ~50% fewer questions through exploration-first questioning, and that question integration matters more than extraction volume, is a genuine insight not undermined by the turn-limit confound. The distinction between navigational and informational interaction benefits (Table 1) is also informative.

4. **Within-model demonstration that interaction significantly improves performance on underspecified inputs.** The Wilcoxon signed-rank tests (Section 3.1, Table 4) confirm that every model performs significantly better in the Interaction setting than the Hidden setting. This within-model finding is valid despite the unequal turn budgets and supports the paper's central claim that interaction is valuable for handling underspecification.

---

## Weaknesses

### Major

- **Unequal interaction turn limits confound cross-model comparisons.** In RQ1, Claude Sonnet 4 and Qwen 3 Coder are allocated up to 100 interaction turns, while all other models (Claude Sonnet 3.5, Claude Haiku 3.5, Deepseek-v2, Llama 3.1 70B) are restricted to 30 turns (Section 3.1, line 106). The stated justification—"to account for their greater reasoning and planning capacity"—does not control for the confound this introduces. More turns directly enable more codebase exploration, more trial-and-error, and more opportunities to ask clarifying questions. The central quantitative claims from RQ1—which models benefit most from interaction, the recovery percentages (89% for Claude Sonnet 4 vs. 54% for Llama 3.1), and the cross-model comparisons—are not reliable given different resource budgets. The Wilcoxon tests (Table 4) test within-model differences (Hidden vs. Interaction), not across-model comparisons, and do not control for this imbalance. The paper also does not acknowledge this disparity in its limitations section (Section 7), which is a significant omission. **Footnote 4** additionally notes that Claude Sonnet 4 is evaluated on only 100/500 instances in the Hidden setting, further complicating the reliability of its Hidden baseline.

### Minor

- **Detection evaluation conflates detection ability with interaction propensity.** RQ2 measures whether models "detect missing information" by observing whether they choose to interact with the user. This operationalization conflates genuine detection of underspecificity with the model's propensity to ask questions under a given prompt framing. Without explicit encouragement, models rarely interact even on severely underspecified inputs, and with strong encouragement they may interact even on fully-specified inputs simply because the prompt tells them to (Table 2). The paper titles the metric "accuracy" and labels columns as FPR/FNR, strongly implying a detection capability reading, while what is actually measured is "interaction appropriateness under a given policy." The results remain informative about interaction behavior, but the framing overstates what is measured. A cleaner approach would include a direct detection task (e.g., asking the model to rate completeness before giving it agentic access).

- **Certain quantitative claims are imprecisely framed.** The abstract states "up to 74% over the non-interactive settings" (also in Section 1). This 74% refers to Claude Sonnet 4's *gap recovery rate* (how much of the Full-Hidden performance gap is closed by Interaction: (61.4-40)/(68-40) ≈ 76.4%), not a 74% relative improvement over its Hidden performance (which would be 53.5%). The phrasing "over the non-interactive settings" is ambiguous and could mislead readers about what is being reported.

- **GPT-4o is used both to generate the underspecified variants and as the user proxy.** This creates a potential systematic affinity: the user proxy's responses may be better aligned with the type of information removed during generation than a different model's responses would be (Section 2.1–2.2). The paper does not discuss this confound or test its sensitivity.

- **The turn limit disparity is not acknowledged as a limitation.** Section 7 (Limitations) mentions the three-turn detection window and the simulated user proxy, but does not mention the unequal turn budgets. This is a significant omission given that it affects the core comparative findings.

---

### Trivial

- None beyond the framing issues already noted as Minor.

---

## Nice-to-Haves

- **Controlled ablation on turn budgets.** At minimum, evaluating a subset of models under both 30 and 100 turns to estimate the effect of turn budget on performance would substantially strengthen the paper.
- **Direct detection task.** Adding a prompt that asks the model to judge completeness before starting the agentic trajectory would provide a cleaner measure of detection capability.
- **Human validation of the dataset.** A small-scale human study confirming that the GPT-4o-generated underspecified summaries produce the same kinds of failure modes as natural underspecification would strengthen ecological validity claims.

---

## Removed Points

These points were raised in the input reviews but are removed or demoted for the following reasons:

- **"The paper does not state whether the dataset will be released"** — REMOVED (Hard Rule: the paper states "Code and data can be accessed at" in the abstract, and questioning existence/release of cited artifacts is prohibited).
- **"Missing related work"** — REMOVED (Hard Rule: cannot confirm missing related works without external sources).
- **Typos/formatting issues** — REMOVED (Hard Rule: parser artifacts not author errors).
- **"Qwen 3 Coder's behavior analysis would benefit from deeper investigation"** — This is a suggestion for strengthening, not a weakness of the current paper. Moved to Nice-to-Haves implicitly.
- **"The comparison between Qwen and Claude on question counts is not controlled for turn limits"** — This is fair but is already subsumed under the broader turn-limit Major weakness above.
- **"Reproducibility concerns about undisclosed hyperparameters"** — REMOVED (Hard Rule: nitpicks about trivial implementation details).

---

## Novel Insights

The most insightful observation to emerge from the reviews, beyond the paper's own contributions, is the interaction between turn budgets and observed model behavior. The harsh critic correctly identifies that Qwen 3 Coder's 45.6% Hidden resolve rate (close to Claude Sonnet 4's 40%) exists despite having 100 turns available in Hidden, while Claude Sonnet 3.5 with only 30 turns achieves 24.2%. This juxtaposition raises the question: does the turn budget affect *exploration behavior* in the Hidden setting, or only interaction? The paper's own analysis of Claude Sonnet 4's "extensive exploration" in Hidden suggests turn budgets may affect non-interactive behavior too, which the paper does not discuss. A secondary insight is that the paper's strongest empirical result—the value of interaction—is actually robust to the turn-limit confound because it rests on within-model comparisons, but the paper consistently frames its results in across-model terms, creating a mismatch between what the evidence supports and what the narrative claims.

---

## Suggestions

1. **Equalize turn limits across all models** for the cross-model comparisons, or at minimum run a controlled ablation with a subset of models at both 30 and 100 turns. Report the effect of turn budget separately and reframe cross-model claims accordingly.
2. **Reframe the detection evaluation** (RQ2) as measuring "interaction behavior" and "interaction appropriateness" rather than "detection accuracy." Add a direct detection prompt as a cleaner complementary measure.
3. **Acknowledge the turn limit disparity explicitly in the limitations section** and discuss how it affects the interpretations of cross-model comparisons.
4. **Clarify the "74%" framing** to distinguish between relative improvement and gap recovery.
5. **Test the GPT-4o user proxy with an alternative model** (e.g., using a different LLM as the proxy for a subset of instances) to assess whether the same-model affinity confound is material.

---

## Calibration Report

**Round-1 bracket:** 4.0–6.0 (after reviewing low-band topic anchors scoring 1.67–3.40, mid-band scoring 4.00–7.33, and weakness-anchored queries).

**All anchors retrieved:**

| Anchor | Avg Score | Round/Query | Comparison to this paper |
|--------|-----------|-------------|--------------------------|
| D2Coder (dsALpkd1OU) | 1.67 | R1-topic-low | Much worse: poor presentation, no clear contribution |
| Seeker (kNvwWXp6xD) | 3.00 | R1-topic-low | Worse: poor writing, limited experiments |
| LLMs Synergy (P0eEalHM5h) | 3.40 | R1-topic-low | Worse: narrow scope, limited evaluation |
| SOP-Agent (oWm80iR1m9) | 3.00 | R1-topic-low | Worse: unclear contributions |
| Active Task Disambiguation (JAMxRSXLFz) | 7.33 | R1-topic-mid | Much stronger: formal framework, cleaner evaluation |
| SWE-Search (G7sIFXugTX) | 4.00 | R1-topic-mid | Somewhat worse: unclear methodology, presentation issues |
| Commit0 (MMwaQEVsAg) | 6.67 | R1-topic-mid | Stronger: well-designed benchmark |
| RefactorBench (NiNIthntx7) | 6.50 | R1-topic-mid | Stronger: clean benchmark design |
| SWE-bench Multimodal (riTiq3i21b) | 5.00 | R2-swe-bench-extension | Comparable: similar SWE-bench extension, some methodological concerns; Ambig-SWE has more creative contribution but worse confound |
| τ-bench (roNSXZpUDN) | 6.50 | R1-weakness-benchmark | Stronger: cleaner benchmark, well-defined evaluation |
| AgentBench (zAdUB0aCTQ) | 6.20 | R1-weakness-benchmark | Stronger: comprehensive multi-environment evaluation |
| Tournament Evaluation (5ZpN6W5uRm) | 3.50 | R1-weakness-turn-limits | Shares methodological concerns but different domain |
| SWE-bench (VTF8yNQM66) | 6.25 | R2 | Stronger: original, more comprehensive |
| AgentQuest (fp6t3F669F) | 6.25 | R2 | Stronger: well-designed interactive benchmark |

**Final score determination:** The closest comparator is SWE-bench Multimodal (5.00), which shares the "SWE-bench extension" framing and has some methodological concerns of its own (superficial baseline adaptations, unclear contribution incrementality). Ambig-SWE has a more interesting conceptual contribution (underspecification decomposition) but a more significant methodological flaw (unequal turn limits that directly affect the central comparative claims). The low-band anchors (1.67–3.40) are clearly worse papers across all dimensions. Ambig-SWE does not share their failures in presentation or contribution clarity. However, it does share a meaningful methodological weakness with the evaluation-focused low-band anchors. **The round-1 weakness-anchored queries around evaluation confounds (query 4) returned papers averaging 3.50–5.75** — Ambig-SWE sits near the upper end of this range because its within-model results are still valid.

**Score: 4.5**

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>