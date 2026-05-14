Now I have a thorough understanding of the paper and the calibration anchors. Let me compile the final review.

---

## Summary

This paper introduces Ambig-SWE, a benchmark and evaluation framework for studying how LLM coding agents handle underspecified software-engineering instructions through interactive clarification. The core contribution is decomposing interactive problem-solving into three measurable dimensions: (1) detecting when information is missing, (2) asking targeted clarification questions, and (3) integrating the answers to solve the task. Using synthetically underspecified variants of SWE-Bench Verified issues with a simulated user proxy, the authors evaluate six models (proprietary and open-weight) and find that interaction recovers up to 74% of the performance lost to underspecification, that most models default to non-interactive behavior and fail at reliable detection, and that question strategy (exploration-first vs. immediate-asking, behavioral vs. implementation details) matters as much as extraction volume.

## Strengths

- **Novel decomposition of interaction into three measurable dimensions**: The paper structures the evaluation into detection (RQ2), question quality (RQ3), and task completion after interaction (RQ1). This granular framework (Sections 3–5) enables targeted diagnosis of where specific models fail — e.g., Qwen 3 Coder's refusal to interact, Llama's vague questioning — rather than collapsing everything into a single aggregate metric.

- **Actionable, non-obvious qualitative insights grounded in trajectory evidence**: The analysis of question strategies (Section 5.3) reveals concrete behavioral patterns: Claude models use an exploration-first strategy (exploring the codebase before asking), Deepseek and Qwen ask immediately, Qwen 3 Coder rigidly follows protocols even when given corrective guidance (Table 1, Section 3.3), and Haiku uses a rigid three-question template. These observations, backed by trajectory examples (Table 7, Appendix A.7), provide genuine guidance for agent design.

- **Broad model coverage with meaningful comparisons**: The selection spans capability levels (Claude Haiku to Sonnet 4, Llama 3.1 70B to Qwen 3 Coder 480B) and training regimes (proprietary vs. open-weight). Including Qwen 3 Coder — which matches Claude Sonnet 4 on standard SWE-Bench — yields the particularly striking finding that comparable task-solving ability masks radically different interaction behavior (100% FNR).

- **Significant and statistically validated performance gains from interaction**: The Hidden vs. Interaction comparison (Figure 3, Table 4) shows statistically significant improvements for all models via Wilcoxon signed-rank tests, with proprietary models recovering up to 80% of the Full-setting performance. The 74% figure in the abstract is appropriately contextualized as an upper bound.

- **Honest and thorough limitations section**: The paper candidly acknowledges that detection is only measured in early turns, that the question-quality metric is a latent-space proxy, and that the simulated user may be more cooperative than real users (Section 7). This transparency strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

- **Synthetic underspecification limits external validity (partially acknowledged)**: The entire study uses GPT-4o–generated summaries of fully specified SWE-Bench issues as the underspecified inputs. The authors' own distributional difference analysis (Section 2.1) shows that natural underspecified issues contain more concrete technical details (code snippets, error messages, file references), reproducibility information, and conversational fragments. The missing information in the synthetic setting is the result of aggressive but mechanical information removal, which may be easier to recover through targeted questioning than real-world underspecification arising from genuine user omissions. The paper acknowledges this limitation (Section 7) and explains that naturally underspecified issues lack the paired ground-truth needed for causal measurement, which is a reasonable methodological tradeoff. However, without even a small-scale validation on real underspecified issues (e.g., measuring whether interaction patterns persist), the headline finding that interaction recovers up to 74% of performance remains confined to the synthetic setting. This does not invalidate the core contribution — the decomposition framework and behavioral insights — but it does bound the strength of the quantitative claims.

### Minor

- **Information-gain metric in RQ3 is a proxy without task-level validation (acknowledged)**: The central quantitative measure of question quality (cosine distance between embeddings of the summarized issue and post-interaction conversation, Section 5.1) is introduced without demonstrating that it captures task-relevant information rather than verbosity or turn-taking patterns. The paper acknowledges that this metric "weigh[s] all information equally, though models may prioritize details differently" (Section 7). The LLM-as-judge score provides a complementary signal but converges around 4/5 for all capable models, leaving cosine distance as the primary differentiator. The key findings in Section 5 (e.g., "Qwen extracts more information but integrates it worse") are therefore supported by suggestive proxy evidence rather than validated measurement. The qualitative analysis of question strategies (Section 5.3) is independently valuable and does not depend on this metric. The paper's transparency about this limitation mitigates the concern, but the metric should be presented as suggestive rather than definitive.

- **Detection experiment conducted as single-run evaluation**: The detection experiment (Table 2) reports accuracy, FPR, and FNR based on a single presentation of each issue per model per prompt, without repeated runs or confidence intervals. For stark findings (e.g., Qwen 3 Coder's 100% FNR across all prompts), the conclusion is robust even to moderate stochasticity. For models with intermediate and variable values (e.g., Deepseek-v2 degrading from 0.69 to 0.51 with stronger prompts), point estimates alone make cross-model comparisons less reliable than they could be. Single-run evaluation is standard practice in this subfield given computational costs, so this is a minor limitation rather than a methodological error.

### Trivial

- The abstract's claim that "prompt engineering offers limited improvement" is slightly overstated given that Claude Sonnet 4 improves from 0.74 to 0.89 accuracy with strong encouragement (Table 2). The paper does qualify this with "its effectiveness varies across models," and for most other models the claim holds, but the absolute phrasing could be softened.

## Nice-to-Haves

- A small-scale evaluation on a handful of naturally underspecified SWE-Bench issues (even without paired full specifications) to assess whether interaction patterns observed in the synthetic setting generalize — e.g., do agents initiate interaction at comparable rates, do question strategies differ? This would substantially strengthen external validity without requiring paired ground-truth.

- Validation of the cosine-distance information-gain metric, e.g., by correlating it with whether the agent's eventual solution incorporates information stated in user answers, or by collecting human judgments on a subset of post-interaction states.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Synthetic underspecification is not validated against natural user behavior" → downgraded and moved to Major.** The paper does acknowledge and analyze this limitation (Section 2.1, Section 7). The criticism is valid but was framed overly harshly; the paper is transparent about tradeoffs.

- **Harsh Critic: "Detection experiment lacks statistical reliability" → moved to Minor.** Single-run evaluation is standard in SWE-Bench–style benchmarks. With 500 instances, point estimates are reasonably stable. The stark findings (e.g., Qwen 3 Coder's 100% FNR) are robust.

- **Harsh Critic: "The claim about efficiency is based solely on step counts in Hidden vs. Interaction, not compared to Full" → removed.** The paper's claim is specifically about whether adding interaction improves efficiency (comparing Hidden to Interaction). Comparing to Full would address a different question. This is scope creep.

- **Harsh Critic: "The normative standard for detection is slightly idealized" → removed.** The harsh critic acknowledges this is "still informative." The idealization is a reasonable experimental design choice for controlled evaluation.

- **Strength Finder: "Validation of synthetic underspecified issues" → weakened.** The distributional difference analysis is a good start, but the paper's own analysis shows substantial differences between synthetic and natural issues. The validation is partial, not complete. Retained as part of the broader strength about the dataset construction but not as a standalone validation strength.

## Novel Insights

Beyond the paper's own claims, the most novel insight to emerge from this work is the decoupling of information extraction from information integration. The data shows that Qwen 3 Coder achieves the highest cosine-distance information gain (0.179) with the most questions (6.02 avg) yet matches Claude Sonnet 4's resolve rate (46% vs 41.8%), which achieves similar gain (0.171) with 50% fewer questions (4.03). This demonstrates that extracting more task-relevant details does not guarantee better task outcomes — how a model incorporates retrieved information into its solution plan is an independent capability. This finding has implications beyond software engineering: it suggests that training agents to ask good questions is necessary but insufficient; they must also be trained to adapt their behavior in light of answers.

## Suggestions

- Reframe the cosine-distance metric in Section 5 as a suggestive descriptor rather than a primary quantitative result, given the lack of task-level validation. The qualitative strategy analysis (Section 5.3) is strong enough to carry the RQ3 insights independently.

- Add a brief discussion in Section 2.1 or Section 7 about what specific aspects of external validity are most threatened by the synthetic-vs-natural gap (e.g., does aggressive information removal make missing details easier to articulate as questions, inflating interaction benefits?).

- For the detection experiment, note in the paper that single-run estimates provide reasonable stability given 500 instances but acknowledge that future work could assess variance across seeds, particularly for models with intermediate detection rates.

- Soften the abstract's "prompt engineering offers limited improvement" to "prompt engineering offers inconsistent improvement across models" to match the evidence in Table 2.

## Score and Decision

### Anchor comparison:

- **InteractComp** (psEcdvhOJx, avg 3.50): Similar topic (ambiguity detection in interactive agents). Weaker: surface-level analysis, confusing search vs. reasoning limitations, narrow interaction design. Ambig-SWE has substantially deeper analysis and a more structured evaluation framework.

- **RExBench** (0xpakqqTbe, avg 3.00): Code agent benchmark with limited scope (12 tasks), minimal analysis depth. Ambig-SWE is clearly stronger on scope, analysis, and insight.

- **RECODE-H** (IKnuyyPHCV, avg 4.50): Interactive code benchmark with simulated feedback. Shares the synthetic-feedback limitation. Ambig-SWE has more surprising empirical findings (Qwen 3 Coder behavior, exploration-first strategies) and a cleaner decomposition framework. Ambig-SWE is somewhat stronger.

- **SWE-Mirror** (e6Vne8vJHe, avg 5.50): SWE-Bench–adjacent dataset contribution with strong scale and results but narrow novelty claims. Ambig-SWE has less scale but more novel behavioral insights and a more original evaluation framework. Roughly comparable quality, different strengths.

- **SecureAgentBench** (8uDFRItIoe, avg 4.00): Security-focused code benchmark. Narrower scope and less surprising findings than Ambig-SWE.

- **Terminal-Bench** (a7Qa4CcHak, avg 7.33): Hard, carefully curated benchmark with broader scope and more polished execution. Ambig-SWE is weaker on engineering quality and dataset scale.

- **Gaia2** (9gw03JpKK4, avg 8.00): Novel platform + benchmark with comprehensive evaluation, action-level verification, and RL-readiness. Ambig-SWE is substantially weaker on infrastructure contributions and evaluation sophistication.

- **MCPMark** (uobROwBsJm, avg 7.33): Well-engineered benchmark with programmatic verification and diverse CRUD operations. Ambig-SWE has less engineering polish but more novel behavioral insights.

- **AstaBench** (M7TNf5J26u, avg 7.00): Scientific agent benchmark with rigorous tool-controlled comparison. Stronger on infrastructure; Ambig-SWE stronger on behavioral analysis of interaction.

Ambig-SWE is clearly above the low-scoring anchors (RExBench 3.00, InteractComp 3.50) and somewhat above the medium anchors (RECODE-H 4.50, SecureAgentBench 4.00) due to its novel decomposition framework and actionable behavioral insights. It is below the high-scoring anchors (Gaia2 8.00, MCPMark 7.33, Terminal-Bench 7.33, AstaBench 7.00) which have more comprehensive infrastructure contributions and broader scope. It sits in the 5.5–6.5 range, comparable to SWE-Mirror (5.50) but with a different strength profile (insight depth over scale). I score it at **6.0**, reflecting a solid contribution with transparent limitations that is appropriate for acceptance at a poster track.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>