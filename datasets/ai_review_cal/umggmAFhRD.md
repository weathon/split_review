- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes and evaluates DREST (Discounted REward for Same-length Trajectories) reward functions as a method for training agents to satisfy the Incomplete Preferences Proposal (IPP) — being simultaneously USEFUL (pursuing goals effectively conditional on each trajectory-length) and NEUTRAL (choosing stochastically between different-length trajectories). The authors train tabular REINFORCE agents in gridworlds containing coins and a shutdown-delay button, and find that DREST agents learn to press the button with probability ~0.5 (high NEUTRALITY) while collecting optimal coins (high USEFULNESS), with a small "shutdownability tax" relative to conventionally-trained agents. The lopsided rewards experiment shows this robustness extends across a 100× range of coin values even without exact equalization.

## Strengths

- **Quantitative metrics formally operationalize POST conditions.** USEFULNESS (expected fraction of γ-discounted coins collected conditional on trajectory-length) and NEUTRALITY (Shannon entropy of the trajectory-length distribution) are clearly defined in Section 4. These provide measurable evaluation criteria that move beyond purely theoretical specification of the IPP.

- **DREST agents achieve near-maximal NEUTRALITY while maintaining USEFULNESS in the example gridworld.** In the main experiment (Section 6, Figures 1–2), DREST agents press the shutdown-delay button with probability ~0.5 (NEUTRALITY near 1, the maximum for two lengths) and collect the optimal coin for each chosen trajectory-length (USEFULNESS near 1). Default agents press with probability near 1 (NEUTRALITY near 0). This is direct empirical evidence that DREST can simultaneously satisfy both POST conditions.

- **NEUTRALITY is robust across a 100× range of lopsided coin values.** Section 6.1 and Figure 3 show that DREST agents (trained without the c/m normalization) maintain NEUTRALITY above 0.5 across coin values from 0.1 to 10, even without exact equalization of maximum preliminary return. This directly addresses a key practical concern about the approach.

- **The "shutdownability tax" is shown to be small in this setting.** Section 7 reports that DREST agents learn USEFULNESS about as quickly as default agents (Figure 1). This provides initial evidence that the extra training cost for shutdownability may be modest.

- **Clean baseline comparison.** Default agents trained with the same algorithm (tabular REINFORCE) and hyperparameters using a conventional reward function serve as a throughout, well-controlled baseline (Sections 5–6).

## Weaknesses

### Fatal
None.

### Major

- **The claim of generality across multiple gridworlds is unsupported.** The paper states (line 79): "We also train agents in eight other gridworlds, to show that our results do not depend on the specifics of any particular gridworld." No descriptions, quantitative results, or summary statistics are provided for these eight environments — not even qualitatively. The reader cannot verify whether DREST agents maintain USEFULNESS and NEUTRALITY in different layouts, wall structures, coin placements, or numbers of trajectory-lengths. Section 6.1's lopsided-rewards experiment tests a different question (varying coin values) and uses a distinct environment. This is an evidential gap that substantially weakens the central generality claim. A summary table showing mean USEFULNESS, NEUTRALITY, and variance across all tested gridworlds would suffice.

### Minor

- **The optimality theorem is stated without proof or intuition.** Section 5 states (lines 134–136): "For all policies π and meta-episodes E consisting of multiple mini-episodes, if π maximizes expected return in E according to our DREST reward function, then π is maximally USEFUL and maximally NEUTRAL." This theorem is central to the paper's theoretical grounding, but no proof, proof sketch, or even high-level intuition is provided in the main text. The reader cannot assess whether the guarantee holds generally or is environment-dependent. A short proof outline (which could reference a full proof in an appendix) would substantially strengthen the paper.

- **The lopsided-rewards experiment tests a modified reward function but is framed as testing "DREST agents."** The main experiment uses the full DREST reward: λ^(N - (i-1)/k) * (c/m). The lopsided experiment (line 176) removes the c/m normalization: λ^(N - (i-1)/k) * c. The modification is explicitly noted, but the paper then interprets the results (Section 7 heading: "DREST agents are still NEUTRAL when rewards are lopsided") as if the same reward function is being tested. The experiment is better understood as testing an unnormalized variant. The paper discusses adjusting λ to compensate for imbalance but does not actually test this. The results are still informative, but the framing could mislead readers about what exactly is being evaluated.

- **Hyperparameter sensitivity is unexplored.** The paper uses fixed λ=0.9, γ=0.95, 64 mini-episodes per meta-episode, and 2,048 meta-episodes, selected via "trial-and-error" (line 137). No sensitivity analysis is provided. It is unclear whether the results hold across a range of λ values, meta-episode sizes, or decay schedules. This is acceptable for an exploratory proof-of-concept but limits confidence in robustness.

- **NEUTRALITY as Shannon entropy conflates pairwise indifference with uniform distributions over >2 lengths.** The paper notes (Section 4) that NEUTRALITY measures entropy of the trajectory-length distribution. For environments with more than two lengths, an agent could always avoid one length and still have moderate entropy — this does not directly correspond to pairwise lack of preference between all different-length trajectory pairs. The paper could acknowledge this limitation or note that all tested environments have only two lengths.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of whether stochastic choice from indifference with tie-breaking differs from the behavioral notion of preference used.
- A discussion of why the tabular setting might be easier (perfect state identification) or harder (no generalization) for DREST relative to neural-network-based agents (the paper already mentions this as future work in Section 7's Limitations).
- Varying λ in the lopsided experiments to directly test the paper's suggestion that lowering λ widens the range of usable coin values.

## Removed Points

These points were flagged in the reviewer inputs but are removed for the following reasons:

1. **"Theoretical proof grounds empirical results" (from Strength Finder)** — Removed because it conflicts with the verified weakness that the theorem is stated without justification. A stated claim is not the same as a validated proof.

2. **"Multiple gridworlds test generalizability" (from Strength Finder)** — Removed because it conflicts with the verified weakness that no results for the additional gridworlds are presented. The paper claims generality but provides no evidence.

3. **Criticism about the behavioral notion of preference (stochastic choice from indifference with tie-breaking)** — This is a conceptual subtlety that does not harm the paper's central claims. The paper defines preference behaviorally, and the metrics directly correspond to that definition. Not a substantive weakness.

4. **Criticism about NEUTRALITY not corresponding to pairwise lack of preference with >2 lengths at the "Major" level** — Demoted to Minor because the paper's tested environments have only two lengths, and the paper could easily add a caveat. The critic's framing of this as a serious flaw overstates the issue.

5. **"The reader cannot replicate or verify these results" (about eight gridworlds)** — This overlaps with the Major weakness (unsupported generality claim). The replication concern is derivative of the missing evidence.

## Novel Insights

The most striking observation from synthesizing these reviews is that the paper has a clear and well-executed core experiment (the example gridworld + lopsided rewards) but makes an unsubstantiated leap when claiming generality. The DREST design itself — using a discount factor that depends on how often a trajectory-length has been chosen in the meta-episode — is clever and the intuition for why it incentivizes stochastic choice is sound. However, the paper would be much stronger if it either provided evidence for the "eight other gridworlds" or explicitly scoped down its claims to the environments actually tested. The theorem centrality is also notable: it is cited in the Strengths as a formal grounding and in the Weaknesses as unsubstantiated — this tension reflects a real gap in the paper's presentation.

## Suggestions

1. **Add a summary table** of USEFULNESS, NEUTRALITY, and key environment parameters for all nine gridworlds (or clearly scope the claims to the environments that are actually documented).
2. **Include a proof sketch or high-level intuition** for the optimality theorem in the main text.
3. **Clarify the framing of the lopsided experiment** — explicitly state that this tests an unnormalized variant to probe robustness, distinguishing it from the full DREST design.
4. **Run a brief hyperparameter sensitivity test** (e.g., varying λ from 0.8 to 0.99) to show whether the main results hold across a reasonable range.
5. **Acknowledge the Shannon-entropy limitation** for environments with >2 trajectory-lengths.
