Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces Ambig-SWE, an underspecified variant of SWE-Bench Verified, and a three-capacity evaluation framework (detection, clarification, leveraging) for studying how LLM-based coding agents handle underspecified instructions. The paper evaluates six models across three settings (Full, Hidden, Interaction) and finds that interaction can recover up to 89% of fully-specified performance, but models default to non-interaction without explicit prompting and struggle to distinguish well-specified from underspecified instructions. The analysis of navigational vs. informational detail requests and question-asking strategies provides actionable insights for agent designers.

## Strengths

- **Decomposition of underspecificity handling into three distinct capacities (detection, clarification, leveraging).** This structured framework (RQ1–RQ3) enables targeted diagnosis of where models fail. For example, §4.2 reveals that Qwen 3 Coder exhibits 100% FNR across all prompts — a failure mode invisible in aggregate resolve rates alone. This decomposition is a genuine methodological contribution that goes beyond prior work (Chen et al., 2025; Kim et al., 2024), which focuses on single missing details.

- **Construction of Ambig-SWE, a controlled paired underspecified dataset.** The paper generates synthetic underspecified variants of SWE-Bench Verified issues (§2.1) and includes a distributional difference analysis comparing against naturally underspecified issues. The paired ground-truth design enables causal measurement of interaction impact that is impossible with naturally underspecified issues (which lack verified correct specifications). The dataset itself is a reusable resource for the community.

- **Empirical finding that interaction recovers substantial performance but models default to non-interaction.** Figure 3 shows Claude Sonnet 4 achieves 89% relative performance of the Full setting when interaction is enabled, while §4.2 shows all models default to non-interaction without explicit prompting. The finding that Qwen 3 Coder never interacts even under strong encouragement (100% FNR, Table 2) despite strong SWE-Bench capabilities is striking and practically important.

- **Analysis of navigational vs. informational detail requests (Table 1).** The finding that requesting navigational information (file paths) improves performance for most models but degrades it for Qwen 3 Coder (52.38% resolve with info vs 55.43% without) is a specific, well-supported insight about rigid protocol-following behavior that would be invisible in aggregate metrics. This is the kind of actionable finding that makes the paper useful for agent designers.

- **Question-asking strategy analysis (Section 5).** The qualitative analysis identifying exploration-first strategies (Claude models), answerability concerns (Deepseek), and rigid templates (Haiku) is insightful and goes well beyond simple win-rate comparisons. The discovery that Claude Sonnet 4 achieves comparable information gain to Qwen with 50% fewer questions through exploration-first strategies is well-supported by both cosine distance and LLM-as-judge metrics.

## Weaknesses

### Fatal
None.

### Major

- **Detection evaluation (RQ2) conflates identification with interaction behavior.** The paper claims to evaluate whether LLMs can *identify* whether a task description is missing information (Section 4, RQ2), but the metrics (accuracy, FPR, FNR) are computed from the binary interaction/non-interaction decision. This conflates two distinct abilities: detecting that information is missing, and deciding to act on that detection. The paper's own analysis in §3.2 states that Qwen 3 Coder "relies on its internal knowledge for key insights about missing information" in the Hidden setting — strongly suggesting it *detects* gaps but chooses not to ask. Conversely, Llama 3.1's 95% FPR under Moderate prompting (§4.1, Table 2) could reflect over-cautiousness rather than an inability to discriminate. Because the metric is behavioral rather than representational, the abstract's claim that "models struggle to distinguish between well-specified and underspecified instructions" is not fully supported by the evidence presented. The paper acknowledges this partially in limitations (Section 7: detection measured only within first three turns) but does not address the deeper conflation. This is the paper's most significant weakness and tempers the claims about the "detection" capacity.

### Minor

- **Reliance on synthetic underspecification without validation of transfer to natural underspecified issues.** The paper's distributional analysis (§2.1) honestly identifies that the synthetic issues are more aggressively stripped of code snippets, error messages, and file references than natural underspecified issues. While the paper argues these differences may not affect agent performance, it provides no validation that model behaviors (interaction patterns, detection, question strategies) transfer to real-world underspecified scenarios. This leaves a gap between the real-world claims in the abstract/introduction and the evidence base.

- **User proxy (GPT-4o) as a potential confound.** The simulated user is conservative but remains an LLM that might systematically influence results. Performance gains from interaction (RQ1) could partly reflect the proxy's tendency to provide well-formed, cooperative answers that real users would not. Detection behavior (RQ2) may be influenced by models' expectation of receiving appropriate answers. The paper acknowledges this in Section 7, but does not quantify the impact (e.g., via a less cooperative proxy or human responses on a subset).

- **Claude Sonnet 4 evaluated on 100/500 instances in Hidden setting.** As noted in the footnote (§3.1), this subset's selection method is not described. If non-representative, comparisons with other models' Hidden rates (computed on all 500) could be biased. The paper claims statistical significance (Table 4) but does not describe how the subset was chosen.

### Trivial
None.

## Nice-to-Haves

- A direct detection experiment (asking models explicitly whether an instruction is missing information) would cleanly separate detection ability from interaction policy.
- Validation on a small set of naturally underspecified issues from original SWE-Bench (the ones filtered out by SWE-Bench Verified) would strengthen external validity.
- An ablation replacing the GPT-4o proxy with a less cooperative variant would quantify the proxy confound.

## Removed Points

- **"Artificial underspecification limits external validity"** (Harsh Critic Critical Issue 2, in full) — Demoted from structural to minor above. The paper explicitly provides a distributional analysis of the differences (§2.1) and justifies why the paired ground-truth design requires synthetic data ("We did not evaluate on naturally underspecified SWE-Bench examples because they lack the paired ground truth... necessary for causal measurement"). The paper is transparent about the limitations, so this is a scope constraint, not a fatal flaw.

- **"Detection evaluation is the only evidence for the paper's core contribution"** — Overstated. RQ1 and RQ3 are independently strong and the three-capacity framework is still valuable even if the detection measurement is noisy. The paper's primary contributions (dataset, decomposition, empirical interaction findings) do not collapse.

- **"Missing experiments" suggestions** (direct detection, validation on natural issues, proxy ablation) — Moved to Nice-to-Haves. These are reasonable extensions for future work, not fatal omissions. The paper has clear scope boundaries and the core experiments are sufficient for the claims made (after appropriately tempering the detection claims).

- **"Evaluation is uneven" (section-by-section notes about variance)** — The harsh critic notes "variance is not reported" for one finding — this is a minor presentation preference, not a structural weakness. SWE-Bench evaluation typically reports single-run resolve rates.

- **Strength Finder's generic strengths** ("decomposition into three capacities" kept; "construction of Ambig-SWE" kept; "empirical finding about 89%" kept). All three are specific and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's conflation-of-detection insight is a valid methodological critique but is stated clearly in the paper's own limitations section (though less forcefully). The strength finder's observations are all drawn directly from the paper's reported results. The most interesting cross-cutting observation — that the detection measurement issue primarily affects RQ2 while RQ1 and RQ3 are methodologically sound — emerges from synthesizing the reviews against the paper text, but is not truly novel beyond what a careful reader would observe.

## Suggestions

1. **Reframe RQ2 claims.** Replace "detection" language with "interaction initiation behavior" throughout Section 4 and the abstract. The three-capacity framework can still name "detection" as a conceptual goal while honestly describing the metric as a behavioral proxy. Add an explicit caveat that interaction decisions may reflect policy rather than detection ability.

2. **Add a direct detection probe.** Present models with full vs. underspecified issues and ask explicitly whether the instruction is missing information. Even on a subset of 50 instances, this would provide clean accuracy/FPR/FNR numbers independent of interaction policy and would substantially strengthen the detection claims.

3. **Describe the Claude Sonnet 4 Hidden subset selection method.** If it was random, state this explicitly. If stratified, describe the strata.

4. **Consider a brief user proxy robustness check.** A simple variant with a less helpful proxy ("I'd rather not say," or shorter responses) on 50-100 instances would strengthen the RQ1 conclusions substantially without requiring a full human study.

## Score and Decision

### Calibration Anchors

**High-scoring (avg >=6.5):**
- *JAMxRSXLFz* (Active Task Disambiguation, avg 7.33) — Proposes BED-based clarification question selection. Simpler benchmarks (20 Questions, HumanEval) but cleaner evaluation. Current paper has broader evaluation and more practical insights but weaker on rigor due to detection measurement issue. **Current paper is slightly weaker.**
- *MMwaQEVsAg* (Commit0, avg 6.67) — Benchmark for library generation from scratch. Similar benchmark-contribution structure. Current paper has deeper analysis (three capacities, navigational/informational). **Comparable.**

**Medium-scoring (avg 3.5-6.5):**
- *TFR0GrzERG* (Task Description ICL, avg 5.25) — Analysis paper with mixed reviews and clarity issues. Current paper is stronger empirically and better written. **Current paper is stronger.**
- *YKK1jXEWja* (Prospector, avg 5.25) — Self-asking + trajectory ranking method with limited novelty. Current paper has clearer contribution. **Current paper is stronger.**
- *PfrpYGKGPL* (Entity-Deduction Arena, avg 5.50) — 20 Questions variant evaluating clarification questions. Small evaluation set (30 entities). Current paper is more thorough and has larger-scale evaluation. **Current paper is stronger.**
- *G7sIFXugTX* (SWE-Search, avg 4.00) — MCTS for SWE agents. Writing quality issues, limited baselines. Current paper is better written and more thorough. **Current paper is substantially stronger.**
- *riTiq3i21b* (SWE-bench Multimodal, avg 5.00) — Extends SWE-bench to multimodal domains. Similar benchmark contribution. Current paper has deeper behavioral analysis. **Current paper is slightly stronger.**

**Low-scoring (avg <=3.5):**
- *BW8O4wHgbo* (Multi-agent Path Finding, avg 3.00) — Thin negative results paper about LLM limitations for MAPF. Very limited contribution. **Current paper is substantially stronger.**
- *P0eEalHM5h* (LLMs Synergy, avg 3.40) — Instruction-following agent paper with weak results. **Current paper is substantially stronger.**

**Score:** Relative to these anchors, the paper is clearly above the midpoint. It is substantially stronger than papers scoring 3-5 and comparable to benchmark+analysis papers scoring 6-7. The main weakness (detection conflated with interaction) is real but does not invalidate the core contributions (dataset, framework, RQ1 and RQ3 findings). The paper provides a reusable benchmark and structured evaluation that will be useful to the community.

**Score: 6.0**

**Decision: Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>