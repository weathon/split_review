Now I have enough calibration data. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

I will now produce the final review.

---

## Summary

The paper introduces *Ambig-SWE*, an extension of SWE-Bench Verified with synthetically underspecified GitHub issues, and evaluates LLM-based agents on three decomposed capacities: (i) detecting when instructions are incomplete, (ii) asking targeted clarification questions, and (iii) leveraging interaction to improve task completion. The authors evaluate six models (Claude Sonnet 3.5/4, Claude Haiku 3.5, Qwen 3 Coder, Deepseek-v2, Llama 3.1 70B) across three settings (Full specification, Hidden/underspecified without interaction, and Interaction). Key findings include that interaction recovers up to 74-89% of fully-specified performance for the best models, but models default to non-interactive behavior and struggle to distinguish underspecified from well-specified inputs. The paper contributes a useful benchmark, a clean three-capacity evaluation framework, and actionable empirical insights about question-asking strategies.

## Strengths

1. **Systematic decomposition of underspecificity resolution into three capacities.** The paper breaks the problem into detection (RQ2), questioning (RQ3), and integration (RQ1), enabling targeted evaluation rather than a single aggregate score. This decomposition is the paper's sharpest analytical contribution and goes beyond prior work that treats underspecification as a monolithic problem (Section 1, contribution 2).

2. **New benchmark for underspecificity in multi-step agentic code generation.** Ambig-SWE extends SWE-Bench Verified with synthetic underspecified variants, enabling controlled study of how agents handle multiple interdependent missing details (Section 2.1). The distributional analysis comparing generated to natural underspecified issues provides reasonable evidence that the dataset captures realistic forms of underspecification.

3. **Concrete evidence that interaction recovers substantial performance.** Figure 3 shows that all models improve significantly from Hidden to Interaction setting, with Claude Sonnet 4 recovering ~89% of its Full setting performance. The finding that Qwen 3 Coder's performance *worsens* when given navigational information (Table 1) is a striking and non-obvious result about rigid protocol-following behavior.

4. **Nuanced qualitative analysis of question-asking strategies.** Section 5.3's analysis along three dimensions (quantity, exploration efficiency, answerability) is the paper's most insightful part. The observation that Claude Sonnet models explore the codebase first before asking—achieving comparable information gain with ~50% fewer questions than Qwen—is a concrete, actionable finding for agent design. Figure 4 provides grounded examples supporting the analysis.

5. **Conservative user proxy design.** The GPT-4o proxy responds only with information explicitly present in the full issue and says "I don't have that information" otherwise (Section 2.2). This avoids hallucinated information that would confound results, a methodological strength over more permissive proxy designs.

## Weaknesses

### Major

1. **RQ2 conflates detection of underspecificity with willingness to interact.** The experiment operationalizes "detection" as whether the model chooses to interact, which conflates two distinct capabilities: recognizing that information is missing, and being willing to ask about it. Under the Neutral prompt, nearly all models show near-zero interaction (Table 2) — not because they fail to detect underspecification, but because default behavior is to proceed without asking. The paper acknowledges this indirectly ("models default to non-interactive behavior without explicit encouragement") but continues to frame the experiment as measuring "underspecificity detection" throughout Section 4. This is a meaningful gap between the claim and the evidence.

   *Why it matters*: The detection capacity is one of the paper's three core claims. The current experiment cannot cleanly support conclusions about detection ability independent of interaction propensity.

   *Mitigation*: The Strong Encouragement prompt partially addresses this by reducing the interaction barrier, and Claude Sonnet 4's 89% accuracy under this condition is suggestive. However, this is not the default framing.

2. **The cosine distance metric for information gain conflates volume with informativeness.** Section 5.1 measures "information gain" as cosine distance between embeddings of the initial task and the cumulative knowledge after interaction. This metric mechanically rewards longer interactions regardless of whether added information is useful. Qwen 3 Coder asks the most questions (6.02 avg.) and scores highest on this metric (0.179), yet the paper itself notes that its performance does not correspondingly improve — indeed, its resolve rate *worsens* with navigational information (Table 1). The paper acknowledges this disconnect ("these disconnects reveal that how models integrate information matters as much as how much they extract") but does not address the fundamental metric validity issue.

   *Why it matters*: The authors correctly observe the limitation, but the metric as presented in Figures 5-6 is the primary quantitative evidence for RQ3. Its weak construct validity means the numerical scores are largely uninterpretable as measures of "information gain."

   *Mitigation*: The LLM-as-judge metric provides complementary evidence, but converges around 4/5 for all capable models, providing no discrimination.

### Minor

3. **Qualitative findings about question "answerability" are conditioned on the specific user proxy.** The finding that "Deepseek's highly specific implementation questions often exceed user knowledge" (Section 5.3) depends on the proxy's design: the proxy knows file locations and implementation details because they are in the full issue, but a real user might know them or not. The paper notes this in Section 7's limitations but the RQ3 conclusions are presented as general capabilities rather than behavior in this controlled setting.

4. **No direct comparison between synthetic and natural underspecified issues on agent performance.** Section 2.1 provides a distributional analysis comparing generated to natural underspecified issues, but does not include an experiment testing whether agent behavior differs on synthetic vs. real underspecified inputs. Given the paper's core contribution is the synthetic dataset, this comparison would strengthen claims about its validity.

5. **Significance test details are relegated to the appendix.** Key comparisons (Hidden vs. Interaction, Interaction vs. Full) reference Wilcoxon-Signed Rank tests, but p-values and test statistics are not reported in the main text (Section 3.1). For a results-driven paper, this makes the statistical evidence less accessible.

### Trivial

- None that warrant noting.

## Nice-to-Haves

- Including trajectory examples for the Qwen 3 Coder rigid behavior finding (the paper mentions this behavior but does not show a trajectory in the main text).
- A deeper investigation into *why* Qwen 3 Coder fails to interact across all prompt conditions — even a speculative analysis based on training data composition would be valuable.
- Redesigning the RQ2 experiment to include an explicit detection probe (e.g., ask the model "Is any crucial information missing?" before it begins working) would cleanly separate detection from interaction initiation.
- Replacing or supplementing the cosine distance metric with one that measures predictive information gain (e.g., how much acquired information reduces uncertainty about the correct patch).

## Removed Points

These points from the reviewer inputs were removed as they do not reflect genuine weaknesses:

- **"Missing related work"** — Removed per instruction: do not mention missing related works without external verification.
- **"Formatting/style nitpicks"** — Removed per instruction.
- **"Reproducibility concerns about missing appendix content"** — The appendix sections are stripped by the parser; they exist in the original submission.
- **"Statistical details should appear in main text"** — This is demoted to Minor (kept as weakness #5) because the paper does reference the appendix for details, which is common practice; the concern is noted but softened.
- **"Strength Finder strengths about problem importance / topic significance"** — Generic strengths removed. Only concrete, evidence-grounded strengths retained.
- **"Missing parts: analysis of why Qwen 3 Coder fails to interact"** — Moved from weakness to Nice-to-Have, as this is a suggestion for improvement, not a flaw in what the paper does present.

## Novel Insights

The reviews surface a perspective that was not fully articulated in the paper itself: the RQ2 experimental design, while described as measuring "detection," is better characterized as measuring a **combined detection + action propensity** under varying prompt pressures. The observation that across the Neutral → Moderate → Strong encouragement spectrum, models not only increase interaction but also change *which* type of input (underspecified vs. full) they interact with differently reveals that **prompt framing does not uniformly increase detection — it reshapes the decision boundary**, and does so heterogeneously across models. Deepseek's counterintuitive degradation with stronger prompting (best accuracy under Neutral, worst under Strong) suggests that detection and prompt-following may interact in non-trivial ways that the paper's framing does not fully explore. This interaction between instruction-following capability and underspecificity detection is a potentially richer research question than detection alone.

## Suggestions

1. **Reframe RQ2.** Rename the experiment to "Interaction Initiation Under Underspecification" or restructure it to include an explicit detection probe (asking the model "Is any crucial information missing?" before it acts). The current data on how interaction rates vary with prompt type and input completeness is valuable — it just needs to be described accurately.

2. **Replace or heavily caveat the cosine distance metric.** Either replace it with a metric that measures predictive information gain (e.g., how much uncertainty about the correct patch is reduced by the acquired information) or add a paragraph explaining clearly what cosine distance does and does not measure, and why the numbers should not be over-interpreted.

3. **Add a small-scale experiment comparing agent behavior on synthetic vs. natural underspecified issues.** Even 20-30 manually annotated natural underspecified issues from SWE-Bench would provide evidence about whether the synthetic dataset induces similar agent behavior to real underspecification.

4. **Move a p-value or effect-size statistic into the main text** for at least the Hidden vs. Interaction comparison across all models, so readers can assess significance without navigating to the appendix.

## Score and Decision

### Calibration

I retrieved calibration anchors across three rounds:

**Round 1 (Bracketing):**
- Weak band (<3.5): D2Coder (1.67), Improve Code Generation with Feedback (3.00), DataSciBench (3.20) — all clearly weaker than Ambig-SWE.
- Middle band (3.5-7.5): SWE-Bench+ (3.75), SWE-bench Multimodal (5.00), SWE-bench (6.25), Commit0 (6.67). Initial bracket: 5.5-7.0.
- Strong band (>7.5): MLE-Bench (8.00), BigCodeBench (9.00), Spider 2.0 (8.00), Cybench (8.67) — all clearly stronger than Ambig-SWE in scope and rigor.

**Round 2 (Narrowing):**
- τ-bench (6.50): User-agent interaction benchmark with domain-specific policies. Ambig-SWE has sharper analytical decomposition (three capacities vs. pass^k metric) but narrower domain scope. Comparable quality.
- MINT (6.75): Multi-turn interaction with tools and feedback. Broader scope; Ambig-SWE has deeper domain-specific analysis. Comparable quality.
- Active Task Disambiguation (7.33): Method paper for ambiguity resolution; stronger methodology on simpler benchmarks. Not directly comparable but indicates the upper boundary for this topic area.
- ScienceAgentBench (6.00), AgentBench (6.20), LiveCodeBench (6.25): Similar-quality benchmark papers. Ambig-SWE's decomposition framework is a distinguishing strength, but its scope (single domain, synthetic underspecification) is narrower.

**Final position:** The paper is clearly stronger than SWE-Bench+ (3.75) and SWE-bench Multimodal (5.00). It is comparable to τ-bench (6.50) and MINT (6.75) — all are accepted benchmark papers with similar levels of contribution and methodological care. It is weaker than the 8+ papers (MLE-Bench, BigCodeBench, Cybench) which have broader scope, more extensive validation, and more rigorous methodology. Within the 5.5-7.0 bracket established in round 1, the paper sits in the middle, comparable to SWE-bench (6.25) in overall quality. The RQ2 framing issue and cosine distance limitation prevent it from reaching the upper end of the bracket.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>