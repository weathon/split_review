Now I have a thorough understanding of the paper and relevant calibration anchors. Let me compose the final review.

## Summary

This position paper argues that existing LLM theory of mind (ToM) benchmarks are "broken" because they measure only *literal theory of mind* (predicting others' behavior) while failing to measure *functional theory of mind* (adapting one's own actions based on those predictions). The authors formalize both concepts (Definitions 2.1 and 2.2), demonstrate empirically across simple matrix games that LLMs can achieve high literal ToM while exhibiting near-zero functional ToM, and show this gap persists across prompting strategies and even when oracle partner-action information is provided. The paper calls for developing interactive benchmarks that directly measure functional ToM.

## Strengths

- **Clear, non-trivial position with precise formalization.** The central claim is stated unambiguously in bold (Section 1) and operationalized through two formal definitions that make the literal-vs-functional distinction rigorous and evaluable. This allows the community to engage with the claim on concrete grounds rather than vague intuition.

- **Exceedingly effective motivating example.** The RPS scenario (Section 1)—where an LLM predicts an always-Rock opponent yet plays the Nash equilibrium of uniform random—is immediately graspable and powerfully illustrates that prediction and adaptive action can be entirely decoupled.

- **Striking empirical demonstration that the gap is robust and not an artifact of prompting.** Tables 1–4 systematically show the literal/functional ToM gap across multiple games (RPS, IBS, IPD), model families, and seven prompting strategies. The "Gap Remains with Oracle Inputs" finding (Table 3) is particularly compelling: even given the partner's actual next action and payoffs, LLMs fail to act rationally, isolating the failure to rational response rather than prediction.

- **The reverse dissociation (DeepSeek-R1 results, Table 4) strengthens the core argument.** Finding that a reasoning model can achieve strong functional ToM with poor literal ToM demonstrates the two capabilities are genuinely orthogonal, not merely that functional ToM is harder. This is a genuinely novel and thought-provoking result.

- **Thoughtful engagement with the strongest counterargument.** Section 5 directly addresses the "embrace game theory, not ToM" view, acknowledging its validity in closed AI-only settings while arguing it fails for AI interacting with sub-optimal humans—the practically dominant deployment scenario. The connection to the predict-then-optimize literature (Elmachtoub & Grigas, 2022) provides independent theoretical justification for why literal and functional performance can diverge even for self-consistent reasoners.

- **Constructive recommendation.** The task interestingness metric (Section 2.1) and concrete candidate games (Codenames, Hanabi, Taboo, Wavelength) give the community a clear path forward, not merely a critique.

## Weaknesses

### Fatal
None.

### Major

- **The "functional theory of mind" label stretches the concept beyond its natural scope, and this is not merely a terminological quibble—it creates conceptual confusion that weakens the paper's central argument.** The tabular RMax baseline, held up as the gold standard for functional ToM, uses no mental state modeling whatsoever—it is model-free optimistic Q-learning. The paper acknowledges in Section 1 that "functional theory of mind can alternatively be considered to be theory of mind reasoning" and that model-based vs. model-free RL "have the same expressiveness," but this response actually undermines the ToM framing: if a method requiring zero modeling of other minds qualifies as "functional theory of mind," the term has lost its connection to what "theory of mind" means in either psychology or AI. This matters because the paper's central critique—that existing ToM benchmarks miss something important—depends on the claimed gap being about *theory of mind specifically*, not just about adaptive decision-making. A more precise framing would be that existing ToM benchmarks are incomplete for assessing interactive adaptation, which is a weaker but better-supported claim.

- **The empirical scope—simple matrix games against fixed-action or tit-for-tat partners—limits how broadly the "broken" claim generalizes to the domains where existing ToM benchmarks operate.** The paper demonstrates the literal/functional gap in toy games where the "right answer" is trivially exploitable. It does not test whether the gap appears in the false-belief reasoning, emotional attribution, or complex social narrative understanding tasks that constitute the bulk of existing ToM benchmarks. The gap may be large in matrix games but negligible or different in kind in richer social reasoning settings. The paper acknowledges this as a "case study" (Section 6), but the title's sweeping claim ("Theory of Mind Benchmarks are Broken") extends well beyond what the evidence supports. The paper would be significantly stronger with at least one experiment bridging matrix games and standard ToM tasks (e.g., an interactive false-belief scenario requiring action).

### Minor

- **The "broken" vs. "incomplete" framing, while allowable in a provocative position paper, is the paper's weakest rebuttal in Section 5.** The paper says "broken" is appropriate because "functional theory of mind is what we really care about." But existing benchmarks measure prediction of mental states/behavior and do so validly. Calling them "broken" because they don't measure something else is like calling a thermometer "broken" because it doesn't measure humidity. The paper would be on firmer ground saying the benchmarks are *insufficient* or *dangerously incomplete* for deployment decisions—language the conclusion itself approaches ("suitably complex benchmarks that directly measure functional theory of mind").

- **The community-misleading claim is asserted but not demonstrated.** The paper argues that deploying LLMs based on literal ToM scores is "misleading to a potentially dangerous extent" (Section 5), but does not show that researchers drawing on high ToM benchmark scores are implicitly claiming functional adaptation capability. Concrete examples of such misinterpretation would substantially strengthen the "broken" framing.

- **The DeepSeek-R1 dissociation (functional ToM without literal ToM) is acknowledged but not fully integrated into the argument.** This result complicates the narrative that functional ToM is what matters most—if functional ToM can be achieved without literal ToM, it suggests the two capabilities serve different purposes and benchmarks for both are needed. The paper's conclusion calls only for functional ToM benchmarks, but the evidence suggests both are needed.

## Nice-to-Haves

- Demonstration of the literal/functional gap in richer social reasoning tasks beyond matrix games (e.g., interactive false-belief scenarios, conversational trust/adaptation tasks)
- Evidence of actual community misinterpretation of literal ToM scores as implying adaptive capability
- A characterization of when the gap is large vs. negligible (competitive vs. cooperative? exploitable vs. general partners? Short vs. long horizons?)

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"The benchmarks measure what they claim to measure, so they're not broken."* — This is the "thermometer doesn't measure humidity" argument. The paper's claim is that using literal ToM scores to assess whether LLMs have practical ToM capabilities is misleading, not that literal ToM benchmarks fail to measure literal ToM. However, the "broken" framing does invite this misreading, which is why it's noted as a minor weakness above.

- *"Overclaiming: the title says 'broken' but the evidence only supports 'incomplete'."* — Position papers are allowed strong framing. The paper explicitly defends this choice in Section 5 and the conclusion is measured. Demanding hedged titles from position papers would undermine the genre. Kept only the specific weakness that the Section 5 rebuttal is the paper's weakest point.

- *"RMax uses no mental state modeling so functional ToM isn't really ToM"* — This is the same as the major weakness above (terminological stretching), so it's not removed but rather consolidated.

- *"Not enough empirical evidence / experiments are too narrow"* — Evaluated as a major weakness since the paper's central claim is about existing ToM benchmarks, but the experiments only cover matrix games. However, demanding extensive empirical validation beyond what a position paper needs is inappropriate; the concern is specifically about the *scope* mismatch between the claim (all ToM benchmarks) and the evidence (three matrix games).

- *"Missing related work / literature review"* — Removed per instructions against citing missing works.

- *"Section 3 reads like a literature review rather than advancing the argument"* — Removed as a formatting/style nitpick.

- *"Process consistency (Bubeck et al.) is used incorrectly"* — The paper's use is reasonable: Bubeck et al. note that LLM explanations can be inconsistent with their processing, which the paper applies to argue that prediction-performance doesn't entail action-consistency.

## Novel Insights

The DeepSeek-R1 reverse dissociation—strong functional ToM with poor literal ToM—is a genuinely novel finding that challenges the intuitive assumption that understanding others' minds is prerequisite for adapting to them. This raises important questions about what reasoning models learn during chain-of-thought training and suggests the possibility of orthogonal capabilities that scale differently. The predict-then-optimize connection (that not all prediction errors are equally consequential for decision quality) provides an elegant formal bridge between operations research and ToM evaluation that, while not original to this paper, has not been applied in this context before.

## Suggestions

- Revise the "broken" framing to "insufficient" or "dangerously incomplete" in the body text, while keeping the provocative title for discussion (the conclusion already uses more measured language; the body should follow suit to avoid the misreading that existing benchmarks are invalid rather than incomplete).
- Either more carefully justify the "theory of mind" label for functional regret (e.g., by arguing that adaptive behavior in social contexts inevitably requires mental-state-like representations, even if implicit) or explicitly frame the contribution as identifying a gap between two distinct capabilities—prediction and adaptation—where only the former is currently evaluated.
- Add at least one experiment testing the gap in a richer interactive setting (e.g., an interactive version of a standard false-belief task) to demonstrate that the issue generalizes beyond simple game theory.

## Score and Decision

**Calibration anchors used:**

| Paper | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| LLM-as-judge critique | yqKfMr0yvY | 7.67 | Stronger formal framework (measurement theory) but less empirical evidence; our paper is comparable in argumentative clarity but has less mature theory |
| "Benchmarking is Broken" | vFae5rRman | 6.00 | Very similar provocative "broken" framing; our paper has stronger empirical evidence (Tables 1-4) and clearer definitions but makes a narrower claim |
| ASR comparison critique | d7hqAhLvWG | 6.25 | Similar structure (formal framework + demonstration of evaluation flaw); comparable quality of argumentation |
| MAS LLMs miss the mark | FfsxgSZW0c | 6.67 | Similar gap-identification position; our paper has stronger empirical support and clearer formal definitions |
| Model multifacetedness | FJF1sa6elQ | 3.33 | Vague definitions and overclaimed novelty; our paper is clearly above this with concrete definitions and compelling experiments |

This paper has a clearer position, stronger empirical evidence, and better formalization than the 6.0–6.67 anchors, but its terminological scope issue (functional ToM as rebranding) and limited experimental breadth keep it below the 7.67 anchor. The core insight—the prediction-action decoupling—is genuinely important and well-demonstrated. The main weaknesses are addressable without undermining the fundamental contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>