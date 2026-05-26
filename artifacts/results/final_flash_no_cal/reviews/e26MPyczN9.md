Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper re-evaluates influential claims that programmatic policies generalize better than neural policies in RL. Through controlled experiments on TORCS, KAREL, and PARKING, the authors show that much of the reported gap stemmed from experimental confounds (reward shaping, observation design) rather than representational superiority. The paper introduces an Expressivity–Discoverability framework and argues that the genuine advantage of programmatic representations lies in handling problems requiring working memory that scales with input size — supported by a proof-of-concept using FUNSEARCH to synthesize BFS for a modified KAREL maze.

## Strengths

- **Controlled TORCS re-evaluation (Table 1, Section 4.1):** The β=0.5 intervention is a crisp causal experiment. Simply reducing the speed incentive in the intrinsic reward makes neural DRL policies match NDPS's OOD generalization, directly isolating reward shaping — not representation — as the cause of the prior gap. This is the strongest piece of evidence in the paper.

- **KAREL re-evaluation (Table 2, Section 4.2):** The paper shows that a simple feedforward network with action-augmented observations (PPO with a_{t-1}) matches or exceeds LEAPS on OOD 100×100 grids on 4/5 tasks. This is a clean demonstration that partial observability plus a simpler architecture — not programmatic representation — was responsible for the generalization, and it provides a practical insight about observation sparsity.

- **Expressivity–Discoverability framework (Definitions 2–3, Section 5):** This provides a principled vocabulary for analyzing why representation comparisons can be confounded (both spaces may satisfy expressivity while only one has controlled discoverability). The framework is used consistently throughout the paper and is likely to be useful beyond this work.

- **Honest PARKING reporting (Section 4.3):** The paper reports noisy results on PARKING where neither representation dominates, and discusses the mixed evidence even-handedly. This transparency strengthens the paper's credibility.

- **Theoretical identification of memory-scaling as a distinguishing factor (Section 5):** The argument that fixed-capacity neural architectures cannot represent algorithms whose working memory grows with input size (e.g., BFS requires a queue/visited set of size Θ(|V|)) is logically sound and well-motivated. The connection to the expressivity property is clearly drawn.

## Weaknesses

### Major

- **Mismatch between the strength of the positive claim and the empirical support.** The paper states in the abstract that it "provide[s] an answer" to when programmatic representations have an inherent OOD advantage, identifying memory-scaling as the decisive factor. However, the evidence for this claim consists of (i) a theoretical capacity argument and (ii) a single proof-of-concept on one constructed KAREL variant using 3 runs of FUNSEARCH. The critical negative experiment — actually running the neural baselines (e.g., PPO with a_{t-1}, LSTM) on the wall-sparse maze to empirically verify that they *fail* on a task requiring instance-scaling memory — is not performed. For a paper whose re-evaluation sections set a high empirical bar, this creates an asymmetry: the negative results (prior work was confounded) are rigorously supported, while the positive result (here is when programmatic helps) is presented at a lower standard of evidence. The conclusion that the paper has "resolved" the question overstates what the evidence can support. The theoretical argument is valuable and the proof-of-concept is promising, but the framing should be calibrated to match — e.g., "we identify memory-scaling as a promising candidate for a principled distinction, and provide a proof-of-concept demonstrating its plausibility" rather than "we provide an answer."

### Minor

- **Missing empirical comparison on the proposed distinguishing task.** Following from the above, the paper would be substantially strengthened by running the same neural architectures that were successfully tuned in Sections 4.1–4.2 on the wall-sparse KAREL maze (or a similar task requiring instance-scaling memory). If they fail as predicted, this would directly validate the core positive hypothesis with the same rigorous standard applied to the re-evaluations. If they succeed (e.g., through some unexpected strategy), the paper would need to refine its argument — but either outcome would be informative. This is the single most important experiment that is absent.

- **Inconsistency in PARKING seed counts.** Section 4.3 states "For each policy type, we trained 30 independently seeded models," but the results (Table 3 and the following paragraph) report 30 PSM models and only 15 DQN models. The reason for this discrepancy (e.g., DQN training being more expensive or some seeds failing to converge) is not explained, which weakens the symmetry of the comparison.

### Trivial

- None.

## Nice-to-Haves

- **Test the neural baselines on the wall-sparse maze** (as described under Minor weaknesses). This would complete the empirical loop that the paper's logical structure calls for.
- **Provide more detail on the FUNSEARCH experiment:** e.g., how the observation and action spaces were mapped to Python, what the synthesized BFS program looked like, how the 3 runs compared, and any failure modes encountered.

## Removed Points

- The harsh critic's framing that the paper "does not resolve the question it poses" is noted but downgraded from a fatal indictment to a Major weakness because the theoretical expressivity argument is independently valid and the proof-of-concept is explicitly labeled as such. The issue is one of framing calibration, not scientific invalidity.
- The claim that "the paper does not establish a causal link between the memory-scaling factor and representation success in a controlled study" is partially valid but overstates the paper's intended contribution for the positive part — it is a proof-of-concept, not a controlled causal study. I have kept the essence (missing neural baselines) in the Minor weaknesses.
- Generic concerns from the harsh critic about "the evidence does not match the strength of the assertion" have been condensed into the single Major weakness above rather than maintained as separate items.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that the paper has two very different-strength contributions bundled together. The re-evaluation work (TORCS, KAREL) is thorough, creative, and genuinely novel in its identification of reward shaping / observation design as confounds — this is a significant corrective to the literature. The positive contribution about memory-scaling, while theoretically well-grounded, would benefit from being positioned as a research program rather than a delivered result. Neither reviewer identified a flaw in the re-evaluation methodology; both agreed it is the paper's strongest aspect. The Expressivity–Discoverability framework provides a useful lens that connects the two halves.

## Suggestions

1. **Reframe the positive contribution.** Replace conclusive language ("We provide an answer") with more measured phrasing that matches the proof-of-concept level of evidence (e.g., "We identify a candidate distinguishing factor and provide initial evidence for its plausibility"). This would not weaken the paper; it would inoculate it against overclaiming criticism and keep focus on what is convincingly demonstrated.

2. **Run neural baselines on the wall-sparse maze** and report the results — either as a central experiment or in an appendix. This single addition would transform the positive contribution from a suggestive proof-of-concept into a validated finding.

3. **Explain the PARKING seed count discrepancy** in the text or a footnote.

4. **Provide more details on the FUNSEARCH synthesis** (e.g., the prompt design, the synthesized program structure, success/failure analysis across the 3 runs) to make the proof-of-concept more informative and reproducible.

## Score and Decision

This paper makes a significant and well-supported contribution by rigorously re-evaluating prior claims about programmatic policies. The TORCS and KAREL experiments are carefully designed, the Expressivity–Discoverability framework is valuable, and the overall writing is clear. The positive claim about memory-scaling is interesting and theoretically motivated but is presented with more certainty than the current evidence supports, and the key experiment testing neural baselines on the proposed task is missing. These issues are addressable in revision and do not undermine the core re-evaluation contributions, which alone are strong enough to merit acceptance. I recommend acceptance with revisions to calibrate the framing of the positive contribution and to consider adding the missing experiment.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>