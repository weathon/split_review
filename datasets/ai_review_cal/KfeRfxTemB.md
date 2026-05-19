- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
I've verified the key equations. Now let me write the consolidated review.

## Summary

This paper introduces Fracture Cluster Options (FraCOs), a multi-level hierarchical reinforcement learning framework that discovers reusable options by clustering behavior patterns ("fractures" — state-action sequence pairs) and ranking them by expected future usefulness across tasks. The approach is evaluated in tabular grid-world environments (showing accelerated learning with increasing hierarchical depth) and in deep RL experiments on the Procgen benchmark (showing improved IID and OOD performance over PPO, PPG, and OC-PPO).

## Strengths

1. **Principled option-selection criterion for generalization.** The usefulness metric (Eq. 2) combining appearance probability, relative frequency, and entropy of usage across tasks is a well-motivated, novel approach to selecting options specifically for future-task generalization, going beyond prior methods that optimize for demonstration-matching or within-task performance. (Section 5.2)

2. **Clean tabular evidence for the benefit of hierarchical depth.** In three grid-world environments (Four Rooms, Nine Rooms, Ramesh Maze) and the MetaGrid environment, increasing the number of FraCO hierarchy levels monotonically accelerates learning on unseen tasks. These experiments are run with 10 seeds, use IQM with standard errors, and show a consistent pattern. (Section 6.1, 6.2, Figures 2–3)

3. **Empirical outperformance of strong baselines on Procgen.** FraCOs and FraCOs-SSR achieve higher IID and OOD IQM returns than PPO, PPG, and OC-PPO across eight Procgen environments, with results aggregated over 8 seeds. The inclusion of OC-PPO as a direct hierarchical competitor is relevant and helps contextualize the gains. (Section 6.3, Figures 4–5)

4. **Natural avoidance of option collapse.** The paper correctly identifies that FraCOs' selection mechanism (fixed, externally-discovered options selected by usefulness) avoids the option collapse problem that plagues Option-Critic methods, and the empirical comparison with OC-PPO supports this claim. (Section 3, Section 6.3)

## Weaknesses

### Fatal
None.

### Major

1. **Deep implementation diverges significantly from the theoretical framework.** In the tabular version, fractures are defined as *(state, action_sequence)* tuples and clustering captures state-dependent behavior patterns. The deep implementation replaces this with "grouping fractures with the same action sequences, regardless of state differences" (line 309), discarding the state information that is central to the theoretical definition. The paper asserts "these modifications do not change the theory of FraCOs, just the implementation" (line 309), but this is misleading — clustering action sequences alone finds action primitives rather than state-conditioned behavior patterns, which is a conceptually different object. While practical simplifications for high-dimensional observations are understandable, the paper does not justify why ignoring state preserves the properties of FraCOs or analyze what the resulting options actually represent. This weakens the link between the tabular theoretical foundation and the deep empirical results, making it unclear whether the Procgen gains are attributable to FraCOs as defined or to a different mechanism.

### Minor

2. **No flat (non-hierarchical) baseline in the tabular experiments.** The tabular experiments compare FraCOs agents at different hierarchical depths (1–4 levels) against each other but not against a base Q-learning agent without any FraCOs. The paper's headline claims about "accelerating" learning on unseen tasks would be strengthened by showing whether even a single level of FraCOs outperforms the flat alternative, or whether FraCOs adds overhead that only pays off with sufficient depth. As presented, the evidence primarily supports "more depth helps" rather than "FraCOs helps."

3. **Unclear training protocol for deep baselines.** The paper specifies that FraCOs and OC-PPO receive a 20M-step warm-up phase (for option learning) followed by 5M steps of fine-tuning after policy reset (lines 318–319). It does not specify whether PPO and PPG baselines train for the full 25M steps, for only the 5M post-warm-up period, or under some other schedule. Without this information, the comparison is uninterpretable — if baselines train for fewer total steps, the comparison is unfair in their favor; if they train for the full 25M but with different option-learning benefits, the comparison is ambiguous. This needs clarification.

4. **Deep implementation details are under-specified in the main text.** How the neural network estimates initiation probabilities and policies in the deep setting — particularly given the simplification to action-only clustering — is described in only a single sentence (line 309). It is unclear how the initiation set (Eq. 7) and termination condition are computed when fractures no longer encode state information. While hyperparameters and architecture details may be in the appendices (stripped by the parser), the main text should at minimum describe the mechanism by which the learned neural network maps observations to initiation/termination decisions for the action-only clusters.

### Trivial
None.

## Nice-to-Haves

- A flat Q-learning baseline in tabular experiments (Exp 1–2) would cleanly demonstrate that FraCOs itself — not just depth — improves over standard RL.
- Per-environment result tables with standard errors for the Procgen experiment (beyond the bar chart) would allow assessing whether gains are consistent or driven by a subset of environments.
- An analysis of what the deep FraCOs actually learn (e.g., do different options activate in different states? are they interpretable?) would strengthen the claim that reusable patterns are being discovered.
- Reporting computational cost (total environment steps and wall-clock time) relative to baselines would be useful for practitioners.

## Removed Points

- **Mathematical inconsistency in usefulness formula (Critic's Issue 1):** REMOVED. The critic claims Eq. (3) adds entropy while Eq. (4) subtracts it. This is a misreading. In Eq. (4), the term -∑ p log p *is* the standard Shannon entropy (H = -∑ p log p, as stated in the paper: "approximated using Shannon's entropy formulation"). Both equations add entropy; the signs are consistent. **No change needed.**

- **Appendices not available / reproducibility concern about missing appendix content:** REMOVED per policy (parser-stripped content is assumed to exist in the original submission).

- **"Pure formatting/style nitpicks" from the harsh critic's section-by-section notes:** REMOVED as they are general observations without actionable criticism or evidence of actual problems.

- **Strengths from Strength Finder that are generic or sycophantic:** None identified — the listed strengths are specific, evidenced, and reasonable.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully recontextualizes or extends the paper's findings beyond what the authors themselves present.

## Suggestions

1. **Clarify or justify the deep implementation.** Either (a) develop a state-sensitive clustering method for high-dimensional observations (e.g., using learned embeddings so that fractures remain *(state_embedding, action_sequence)* pairs), or (b) provide a clear theoretical or empirical justification for why clustering by action sequences alone preserves the generalization properties of FraCOs. At minimum, analyze what the action-only clusters represent and whether they capture different behaviors than action primitives.

2. **Specify the training schedule for all baselines in Section 6.3.** State explicitly how many total environment steps each method (PPO, PPG, OC-PPO, FraCOs) receives, when evaluations occur, and ensure fair comparison on the same total budget.

3. **Add a flat Q-learning baseline to the tabular experiments.** This is a simple addition that would cleanly separate the effect of "having FraCOs at all" from "having more FraCO levels."

4. **Expand the description of the deep initiation/termination mechanism in the main text.** One sentence is insufficient; describe how the neural network predicts whether a FraCO can be initiated in a given state and how termination is determined when the clustering was action-only.
