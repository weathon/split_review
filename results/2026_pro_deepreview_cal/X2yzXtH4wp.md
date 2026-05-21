Now I have all the information I need. Let me compose the final review, carefully filtering the harsh critic's and strength finder's outputs against the paper.

---

## Summary

This paper introduces Ambig-SWE, a framework for evaluating how LLM coding agents handle underspecified instructions. The authors extend SWE-Bench Verified with GPT-4o-generated underspecified issue variants and design a three-setting evaluation (Full, Hidden, Interaction) using a simulated user proxy. They decompose interactive problem-solving into three capacities — detecting underspecification, asking targeted clarification questions, and integrating acquired information — and evaluate six models (Claude and open-weight) across these dimensions. The key finding is that interaction substantially recovers performance lost to underspecification (Claude Sonnet 4 recovers 89% of its fully-specified performance), but most models default to non-interactive behavior and struggle with reliable detection.

## Strengths

- **Clean, controlled interactive evaluation framework**: The three-setting design (Full, Hidden, Interaction) with a GPT-4o user proxy restricted to ground-truth information isolates causal effects of interaction on task completion. This enables direct measurement of how much performance interaction recovers — a design choice that is both simple and powerful (§2.2–2.3).

- **Multi-capacity decomposition yields targeted diagnostics**: By separately evaluating detection accuracy and false-positive/negative rates (Table 2), information gain from questions (Figures 5–6), and reliance on navigational detail (Table 1), the paper pinpoints *where* different models fail — e.g., Qwen 3 Coder's 100% false-negative rate in detection despite strong coding ability, versus Claude Sonnet 4's 0.03 false-positive and 0.18 false-negative under strong prompting. This decomposition is the paper's most distinctive contribution.

- **Quantitative evidence of large interaction-driven recovery**: Figure 3 and the Wilcoxon Signed-Rank tests (Table 4, Appendix) demonstrate that interaction significantly raises resolve rates for all six models. Claude Sonnet 4 recovers 89% of its fully-specified performance; Claude Sonnet 3.5 and Haiku recover ~80%. These gains are substantial and consistent.

- **Dataset construction validated against natural underspecification**: The distributional difference analysis in §2.1 comparing synthetic underspecified issues with naturally underspecified SWE-Bench issues shows the synthetic versions are more aggressively stripped of code snippets and error messages, but introduces no artificial patterns. This transparency about differences strengthens rather than weakens the evaluation.

- **Detailed qualitative analysis of question-asking strategies**: Section 5.3 identifies three distinct patterns — question quantity/user burden tradeoffs, exploration-first vs. ask-immediately strategies, and answerability/specificity targeting — with concrete examples (Figure 4). The observation that Claude Sonnet 4 achieves comparable information gain to Qwen 3 Coder (cosine distance 0.171 vs. 0.179) with 50% fewer questions is a crisp, actionable finding.

- **Breakdown of navigational vs. informational detail reveals integration failures**: Table 1 shows that Qwen 3 Coder's resolve rate *decreases* when it receives file locations, while Deepseek-v2 collapses below its Hidden-setting performance without navigational information. These findings expose rigid protocol-following and poor feedback integration, directly supporting the paper's argument about training deficiencies.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "up to 74%" figure is undefined**: The abstract and introduction claim interactivity "can boost performance by up to 74% over the non-interactive settings," but no formula, derivation, or precise referent is provided. The underlying data exists (Figure 3), but what the 74% represents — relative improvement from Hidden to Interaction, recovery rate toward Full, or something else — is ambiguous. This should be explicitly defined and contextualized.

- **Claude Sonnet 4 Hidden evaluation on only 100/500 instances without documented subset selection**: Due to cost (noted in footnote 4), Claude Sonnet 4 was evaluated on a reduced Hidden-condition sample. While the paper states the differences remain statistically significant (Table 4), it does not describe how the 100-instance subset was selected (random? stratified?), which affects confidence in the Hidden-vs-Interaction comparison for this model, the model most prominently featured in the headline findings.

- **Synthetic underspecification differences warrant more explicit discussion of generalization bounds**: The distributional difference analysis (§2.1) shows synthetic issues lack code snippets, error messages, and other partial cues that real users often provide. While the paper acknowledges these differences, a more direct discussion of what kinds of real-world underspecification the findings are expected to generalize to — and what kinds they may not — would strengthen the contribution. This does not undermine the core findings, since the framework is designed as a controlled diagnostic tool rather than a realism simulator.

- **Turn-limit differences noted but implications for cross-model comparison under-discussed**: Claude Sonnet 4 and Qwen 3 Coder receive up to 100 turns while other models get 30 (§3.1). The paper acknowledges this but does not discuss how it affects cross-model absolute comparisons. Within-model comparisons (Hidden vs. Interaction vs. Full) are unaffected; the paper should state this explicitly.

- **User proxy responses not validated with human audit**: The GPT-4o proxy is constrained to answer only from the full issue, responding "I don't have that information" when queried beyond its knowledge. This is a sound design, but a small manual audit confirming the proxy never hallucinates information would raise confidence in the interaction setting's integrity.

### Trivial

- The detection measurement window ("first three turns") is specified only in Section 7 (Limitations), not in Section 4.1 where the RQ2 experiment is described. This should be stated upfront in the experimental setup for clarity.

## Nice-to-Haves

- Human validation of a subset of synthetic underspecified issues (e.g., having developers rate plausibility) would fortify external validity claims.
- Tying question quality more directly to downstream success — e.g., binning trajectories by the type of information obtained and showing how the agent used it — would make the case that better questioning causes better integration rather than merely correlates with it.
- Discussing whether detection failure is due to models genuinely failing to *recognize* missing information versus a strong prior against initiating dialogue (e.g., from training data that rarely includes interactive code-assistance scenarios) would enrich interpretation of RQ2.
- Reporting confidence intervals for Claude Sonnet 4's Hidden-condition results that account for the smaller sample size (100 vs. 500).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's "Detection measurement inconsistency" claim**: The critic asserted an inconsistency between Section 7 ("first three turns") and Section 4.1 (claimed to describe tracking interaction "at any point in the trajectory"). Verifying against the paper: Section 4.1 states only that models are tracked "during [their] solution trajectory" and does not specify a window — it does not contradict the three-turn window specified in Section 7. This is not an inconsistency; it is simply an underspecified experimental detail in §4.1 that is clarified in §7. The critic's framing as a "critical issue" is unfounded.

- **Harsh Critic's speculation about Qwen 3 Coder's rigidity being an artifact of input format**: The critic speculates that Qwen 3 Coder's non-interactive behavior "could partly be an artifact of an input format that the models were not trained to handle." This is pure speculation about training data that cannot be verified from the paper. The paper reports the behavior as an empirical finding; speculating about its cause without evidence is not a valid weakness.

- **Strength Finder's generic strengths**: The Strength Finder included generic framings like "addressed an important problem" — these are surface-level and carry no evaluative weight. I retained only strengths with concrete, verifiable anchors in the paper.

- **Harsh Critic's suggestion that Qwen 3 Coder's detection accuracy is "chance" and "contributes no new information"**: The paper already reports Qwen 3 Coder's 100% FNR explicitly in Table 2 and discusses it as "rigid non-interactivity" and a "concerning finding" (§4.3). The harsh critic's framing of this as something the paper should "acknowledge more explicitly" is redundant — the paper already treats this as a key finding.

## Novel Insights

The most striking insight emerging from the synthesis of this paper's results is the dissociation between information extraction and task success — a finding that goes beyond the paper's stated contributions. Qwen 3 Coder extracts the *most* information (cosine distance 0.179) yet underperforms Claude Sonnet 4 (0.171) in resolve rate, and its performance *worsens* when given navigational information (Table 1). Meanwhile, Claude Sonnet 3.5 and Haiku extract nearly identical information (0.136 vs. 0.135) yet differ by 12.8 percentage points in resolve rate. This pattern — that how models *integrate* acquired information matters far more than how much they extract — is the paper's deepest empirical finding and has implications beyond software engineering for any interactive agent design.

## Suggestions

- Define the "74%" metric explicitly (e.g., `(Interaction − Hidden) / Hidden` for the best-performing model) and add a small table or sentence showing the absolute percentage-point gains alongside relative improvements.
- Move the "first three turns" specification from Section 7 to Section 4.1 so readers have the detection window before seeing the results.
- Describe the Claude Sonnet 4 Hidden subset selection method (random sampling, stratification) and consider reporting confidence intervals that reflect the reduced N.
- Add a sentence clarifying that cross-model absolute resolve-rate comparisons are confounded by different turn limits, while within-model comparisons remain valid.

## Score and Decision

**Calibration anchors:**

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| CscKx97jBi (Code Gen with Feedback) | 3.00 | R1 | Much weaker — narrow scope, thin evaluation |
| BltaWJZMeR (DataSciBench) | 3.20 | R1 | Weaker — less focused, less rigorous |
| NiNIthntx7 (RefactorBench) | 6.50 | R2 | Weaker — narrower model coverage, 100 tasks only |
| MMwaQEVsAg (Commit0) | 6.67 | R2 | Weaker — different focus, less analysis depth |
| jp3gWrMuIZ (MINT) | 6.75 | R2 | Weaker — broader but shallower; Ambig-SWE's decomposition is more novel |
| JAMxRSXLFz (Active Task Disambiguation) | 7.33 | R1/R2 | Most comparable — similar topic (clarification for ambiguity) but on simpler benchmarks; Ambig-SWE has larger empirical scope and more systematic decomposition |
| mw1PWNSWZP (OctoPack) | 7.33 | R2 | Different focus (instruction tuning), less relevant |
| EhrzQwsV4K (L2MAC) | 7.20 | R2 | Different focus (long code generation), less relevant |
| 6s5uXNWGIh (MLE-Bench) | 8.00 | R1/R2 | Stronger — broader scope, human baselines, more rigorous execution |
| YrycTjllL0 (BigCodeBench) | 9.00 | R1 | Much stronger — landmark benchmark |

**Round 1 bracket**: 6.5–8.0. The paper is clearly above the weak-anchor cluster (~3.0) and below the top-tier benchmark papers (8.0+).

**Round 2 narrowing**: Within the 6.5–8.0 bracket, Ambig-SWE is most comparable to JAMxRSXLFz (7.33) in topic and to MINT (6.75) in structure. It exceeds both: it tackles a harder domain (SWE-Bench vs. 20 Questions/HumanEval vs. repurposed datasets), evaluates more models (6 vs. 3 vs. 20 but shallower), and offers a more actionable decomposition. It does not reach MLE-Bench (8.00) in scale or rigor. The paper's weaknesses are all minor (presentation clarity, sample-size documentation, proxy validation) — none threaten the core contribution.

**Final score: 7.5**. This reflects a solid accept-quality paper with a well-motivated framework, clean experimental design, and actionable empirical findings, held back from the 8+ tier by some presentation imprecision and a few under-documented experimental choices that are easily fixable.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>