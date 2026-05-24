Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Ambig-SWE, an underspecified variant of SWE-Bench Verified designed to evaluate how LLM agents handle incomplete instructions in software engineering tasks. The authors decompose the resolution of underspecification into three capacities — detecting missing information, asking targeted clarification questions, and integrating interaction to complete the task — and evaluate six proprietary and open-weight models. The key finding is that interaction can substantially recover performance (e.g., Claude Sonnet 4 goes from 40.0% Hidden to 61.4% with interaction, recovering 89% of its Full setting performance), but most models default to non-interactive behavior unless explicitly prompted, and prompt engineering alone is insufficient for reliable detection.

## Strengths

1. **Structured decomposition of underspecification handling into three distinct capacities.** The paper separately evaluates detection (RQ2), question quality (RQ3), and interactive integration (RQ1). This fine-grained breakdown is a clear improvement over prior work that treats underspecification as a single missing detail, and it enables targeted diagnosis of where models fail. Evidence: Section 1 contributions (2) and the three corresponding research question sections.

2. **Controlled dataset with paired well-specified and underspecified instances enabling causal measurement.** Ambig-SWE synthesizes underspecified versions of SWE-Bench Verified issues using GPT-4o while preserving original ground-truth specifications. The distributional comparison to naturally occurring underspecified issues (§2.1) is a valuable quality check showing that the synthetic issues are more aggressively stripped but that natural issues with similar vagueness exist. The paper explicitly justifies why natural underspecified examples cannot serve as a control (lack of paired ground truth).

3. **Quantitative demonstration that interaction significantly recovers performance lost to underspecificity.** Figure 3 shows resolve rates across Hidden, Interaction, and Full settings for six models with statistical significance testing. Claude Sonnet 4 achieves 61.4% in Interaction vs. 40.0% in Hidden, recovering ~89% of its Full performance (68.0%). The relative improvement exceeds 50% for several models, and the Wilcoxon test results confirm the significance of these differences.

4. **Empirical insight that question quality matters more than question quantity.** Section 5.2 shows Claude Sonnet 4 achieves comparable information gain to Qwen 3 Coder (cosine distance 0.171 vs. 0.179) with 50% fewer questions (4.03 vs. 6.02), and Section 5.3 qualitatively identifies an exploration-first strategy that avoids asking implementational details recoverable from the codebase. This provides actionable design guidance.

5. **Careful analysis of navigational vs. informational question types.** Table 1 breaks down how often models acquire file-location information and reports resolve rates with and without it, revealing that Deepseek-v2 collapses from 13.19% to 4.62% without navigational details while Claude Sonnet 3.5 maintains relatively high performance (37.94% vs. 59.52%). This provides nuanced understanding beyond overall accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **RQ2 conflates detection with decision to interact.** The experiment measures whether a model *chooses to interact* when presented with a full or hidden issue and treats this as evidence of "detecting missing information." However, a model could detect underspecification yet still not interact (due to instruction-following, task habits, or cost), or interact for reasons unrelated to underspecification (as a routine). This is particularly problematic for Qwen 3 Coder, which has 100% FNR across all prompts — this argues more about non-interactivity than detection failure. The paper's central claim about detection ability (stated in the abstract and RQ2 framing) is partially unsupported by the current experimental design, which tests *interactive behavior under prompt variation* rather than the cognitive capacity of detection. **Why it matters:** This is not a fatal flaw — the data on interaction behavior is still informative — but the paper should either (a) add a cleaner detection experiment (e.g., a forced-choice classification: "Is this issue underspecified?" with no agent context) or (b) reframe RQ2 explicitly in terms of interactive behavior rather than detection.

### Minor

1. **"Up to 74%" headline claim is not clearly computed.** The abstract and introduction state that interactivity improves performance "up to 74% over the non-interactive settings." From Figure 3, the largest relative improvement (Hidden → Interaction) is for Claude Haiku 3.5 at 100% (13.4% → 26.8%). For Claude Sonnet 4, the improvement is 53.5%. The gap-recovered metric for Claude Sonnet 4 is ~76.4%, which is close but not exactly 74%. The paper should explicitly state how this number is computed. **Why it matters:** This is a small inconsistency that undermines a headline quantitative claim; easily fixable with a footnote or clarification.

2. **No confidence intervals or standard errors for main resolve rates (Figure 3).** Given 500 instances, the resolve rate estimates have non-negligible variance. Reporting confidence intervals would help gauge reliability of the observed differences between models and settings. **Why it matters:** Adds rigor without additional experiments.

3. **LLM-as-judge metric in RQ3 shows ceiling compression.** Scores converge around 4/5 for all capable models (Figure 6), reducing discriminating power. The paper does not calibrate the metric by showing examples of scores 1–5 or comparing against human judgments on a subsample. **Why it matters:** This reduces confidence in one of the two question-quality metrics, though the cosine distance metric remains informative.

4. **Several quantitative claims lack significance tests or variance measures.** The claim about "Qwen 3 Coder requiring 50% more questions than Claude Sonnet 4" (6.02 vs. 4.03) is stated without standard deviations or significance tests. Similarly, the efficiency analysis in §3.2 reports average steps but provides no formal comparison. **Why it matters:** More careful reporting would strengthen these secondary claims.

### Trivial
- The paper could benefit from tabulating the "relative performance" percentages (e.g., "80% of full performance") mentioned in §3.2 rather than listing them in prose.

## Nice-to-Haves

- **Validate the synthetic underspecification with human judges.** Having human annotators rate the hidden issues on "would an expert need clarification to solve this?" would further validate that the dataset captures genuine underspecification beyond the LLM-based distributional analysis already conducted.
- **A more detailed comparison of action step distributions** (median, IQR, not just mean) for Hidden vs. Interaction settings would strengthen the efficiency claims in §3.2.
- **Include an analysis of Deepseek's divergent behavior** (degrading with stronger prompting in RQ2), which is noted but not explored further.

## Removed Points

- **Criticism that synthetic dataset limits external validity (Harsh Critic Point 2).** The paper already acknowledges this limitation in §7 ("Our simulated user proxy may be more cooperative than real users") and justifies the design choice (lack of paired ground truth for natural examples). This is an acknowledged scope constraint, not a hidden weakness.
- **Criticism that the user proxy (GPT-4o) might over-align with the summarization model (GPT-4o).** The paper acknowledges this implicitly by noting the proxy is deliberately conservative (responding "I don't know" when information is absent). Without evidence that this specific alignment causes a meaningful distortion in results, this is speculative.
- **Criticism that the Interaction setting uses a compulsory interaction prompt (a confound in RQ1).** The paper explicitly notes that "without compulsory interaction, the model defaults to non-interactive behavior for most issues, as seen in the Hidden setting" (§3.1). The purpose of the prompt is to enable studying what happens when models *do* interact, not to isolate the effect of the prompt itself. This is a deliberate experimental design choice, not a confound.
- **Criticism about the quality gap between synthetic and natural underspecification (distributional differences).** The paper conducts a thorough distributional difference analysis and transparently reports the differences. This is a methodological characteristic, not an unacknowledged weakness.
- **Strength Finder claims about "addressing important problem" / generic praise.** These are removed as generic/superficial.

## Novel Insights

Two observations emerge from synthesizing the reviews that go beyond the paper's own stated findings. First, the disconnect between *detection capability* and *interactive propensity* (RQ2) is itself a finding worth highlighting: even if models can detect underspecification internally, they may be trained to suppress interactive behavior. This suggests future work should not only benchmark detection but also study the decision boundary for when to interact. Second, the exploration-first strategy (Claude models exploring the codebase before asking questions) versus ask-first strategy (Qwen, Deepseek) represents a fundamental design tradeoff in agent architecture that the paper surfaces but does not fully characterize. The finding that exploration-first yields comparable information gain with fewer questions hints at a more general principle: *ask only what you cannot discover*.

## Suggestions

1. **Clarify the "74%" computation** in the abstract and introduction with an explicit formula or footnote. If it refers to gap-recovered rather than relative improvement, state this clearly.
2. **Either add a non-interactive detection experiment or reframe RQ2.** The simplest fix is a forced-choice classification task ("Is this issue underspecified?") without any agent context, which would directly test detection ability. Alternatively, reframe RQ2 as measuring "interactive behavior under prompt variation" rather than "detection."
3. **Add confidence intervals to Figure 3** and consider including standard deviations for the question-count comparison in RQ3.

## Score and Decision

**Calibration Anchors (retrieved from corpus):**

| Anchor | Avg Score | Comparison to This Paper |
|--------|-----------|------------------------|
| BigCodeBench (YrycTjllL0) | 9.00 | More comprehensive benchmark with human annotations; stronger empirical breadth |
| MLE-Bench (6s5uXNWGIh) | 8.00 | Broader scope; more thorough evaluation but much higher cost barrier |
| Active Task Disambiguation (JAMxRSXLFz) | 7.33 | Both tackle ambiguity/underspecification; proposed method + evaluation vs. this paper's diagnostic framework |
| Commit0 (MMwaQEVsAg) | 6.67 | Both extend SWE evaluation; Commit0 tackles library generation whereas this paper tackles interactive underspecification |
| SWE-bench Multimodal (riTiq3i21b) | 5.00 | Both extend SWE-bench; comparable contribution level but this paper's interactive evaluation is more novel than adding a modality |
| Enhancing Software Agents with MCTS (G7sIFXugTX) | 4.00 | Applied technique to SWE agents; less conceptual contribution |
| SWE-Bench+ (pwIGnH2LHJ) | 3.75 | Identified data quality issues in SWE-bench but limited constructive contribution |
| ALMANACS (wwO8qS9tQl) | 3.00 | Limited novelty and weak evidence for claims |
| Exploring Planning Capabilities (koza5fePTs) | 2.00 | Largely reproduces known results with minimal novelty |

**Comparative assessment:** This paper is substantially stronger than the low-scoring anchors (2.00–3.75), which either reproduce known results or offer limited contribution. It is comparable to or slightly stronger than mid-range SWE-extensions like SWE-bench Multimodal (5.00) and Commit0 (6.67), thanks to the more fundamental contribution of decomposing underspecification into evaluable capacities and the careful dataset design with paired controls. It is less comprehensive than top anchors like BigCodeBench (9.00) or MLE-Bench (8.00), which have larger scale and additional validation layers. The primary weakness — the RQ2 confound between detection and interaction behavior — is significant but addressable and does not invalidate the paper's broader contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>