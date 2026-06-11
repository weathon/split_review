## Summary

This paper re-evaluates claims from prior work that programmatic policies generalize better than neural policies in RL. Through controlled experiments on TORCS (modifying the reward function to be more cautious), KAREL (using a simpler feedforward architecture with last-action augmentation), and PARKING, it shows that much of the reported generalization gap stemmed from experimental confounds (reward shaping, unnecessarily complex architectures) rather than representational differences. The paper introduces an *expressivity/discoverability* framework to reason about when representation choices matter, and identifies a class of problems—those requiring working memory that grows with input size—where programmatic representations offer a principled advantage. A FUNSEARCH-based proof-of-concept demonstrates BFS program synthesis for a wall-sparse maze.

## Strengths

- **Controlled reward-function ablation in TORCS isolates the cause of the generalization gap.** The paper replaces the original reward (β=1.0) with a cautious one (β=0.5) and shows that neural DRL policies go from crashing on every OOD track to successfully generalizing on 76% of G-TRACK-2 and 69% of E-ROAD test problems (Table 1). This directly demonstrates that the prior reported advantage of programmatic policies in TORCS was confounded with reward design, not representation.

- **Simple feedforward + last-action augmentation matches LEAPS in KAREL.** "PPO with a_{t-1}" achieves perfect 1.00 (0.00) return on 100×100 grids for STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER (Table 2), matching LEAPS programmatic policies and surpassing LSTM baselines. This refutes the claim that programmatic representations are necessary for OOD generalization in KAREL.

- **Expressivity/discoverability framework provides a useful conceptual tool.** Definitions 2 and 3 partition OOD generalization into whether the policy space contains a generalizing solution (expressivity) and whether the search algorithm can find it (discoverability). This provides a clean vocabulary for understanding why prior work's observed gaps were about discoverability rather than expressivity.

- **Principled identification of a problem class where fixed-capacity architectures provably fail.** The paper argues convincingly that general pathfinding requires Ω(log|V|) bits for vertex indexing and that BFS/IDDFS require working memory growing with input size, whereas fixed-capacity neural architectures have O(1) memory independent of input size. This provides a formal, not just empirical, answer to when programmatic representations have an inherent advantage.

- **Honest reporting of PARKING results.** The paper transparently reports that neither representation reliably generalizes on PARKING (Table 3) and acknowledges the mixed evidence, which strengthens the credibility of the overall analysis.

## Weaknesses

### Major

- **TORCS seed selection bias undermines the headline claim.** Only 13/30 seeds (43%) learned to complete G-TRACK-1 and 4/15 (27%) learned AALBORG under β=0.5; OOD evaluation is performed only on these successful seeds. The programmatic policies (NDPS) succeeded consistently across seeds. The abstract and main claims state that "neural policies… can match or exceed the OOD generalization of programmatic policies" without caveating this selection issue. The practical significance of a method that works 43% of the time vs. one that works consistently is very different. The paper does report these fractions honestly in the table caption, which is good practice, but the framing overstates what the evidence supports.

- **FUNSEARCH proof-of-concept does not connect to the paper's RL narrative.** The proof-of-concept uses FUNSEARCH (a program synthesis system) with an LLM to generate a Python BFS implementation, using a policy-rollout return as the fitness function. There is no gradient update, no policy gradient, no RL training loop—it is program synthesis with a task-specific evaluation function. The paper's entire framing (Sections 1–4) is about RL policy learning. To support the central thesis about when programmatic representations help in RL, one would need to see that (a) neural policies fail on the wall-sparse maze, (b) programmatic policies learned through an RL-compatible process succeed, and (c) this success is attributable to the representation rather than the search algorithm. None of these are demonstrated. The paper would be stronger either by expanding this into a proper RL experiment or by removing it and positioning the paper as purely a re-evaluation + theoretical argument.

### Minor

- **The KAREL experiment changes the architecture, not just the training procedure.** The comparison shows that a feedforward network with last-action augmentation (a meaningfully different architecture than the original ConvNet/LSTM baselines) closes the gap. While this is a useful finding, the paper's framing sometimes implies it is "fairer tuning" of the original baselines, when it is actually a different architectural choice. Clarifying this distinction would improve precision.

- **No statistical testing on key results.** The TORCS results (Table 1) report means and fractions but no confidence intervals or formal comparisons. Given the small number of successful seeds (13 for G-TRACK-1, 4 for AALBORG), this matters for assessing reliability.

- **Expressivity framework's treatment of neural architectures is incomplete.** The paper claims that "commonly used neural architectures cannot encode a solution" requiring instance-scaling memory, but mentions memory-augmented networks (lines 312–313) only in passing, dismissing them as "imperfect" and lacking "formal correctness and input-scale generalization guarantees." This conflates the *existence of a representation* with *provable generalization*. The paper would benefit from explicitly distinguishing these two questions.

- **HARVESTER failure is underexplained.** "PPO with a_{t-1}" achieves 0.04 on 100×100 HARVESTER, which is essentially failure. The paper does not discuss why this task differs from the other four, nor whether the constant-memory argument explains it.

- **Asymmetric experimental budgets.** NDPS results are reported for 3 seeds (from the original paper), while DRL (β=0.5) uses 30/15 seeds. The paper should discuss whether this asymmetry affects the comparison.

### Trivial

None.

## Nice-to-Haves

- A direct RL experiment on the wall-sparse maze comparing programmatic methods against neural baselines would significantly strengthen the positive thesis.
- Code for the re-evaluation experiments available as supplementary material at submission time would strengthen reproducibility, especially for a re-evaluation paper.

## Removed Points

These points were flagged for removal. Treat them with caution.

- **"The TORCS reward change solves a different optimization problem" (from Harsh Critic).** The paper explicitly addresses this: it states the reward is intrinsic (Equation 2 is used only for learning, not for evaluation) and the evaluation metric (lap time, crash) remains unchanged. The critic's concern is acknowledged by the paper's own defense; kept as a minor concern about framing but the bulk of the criticism is adequately addressed by the paper.

- **"NDPS uses a neural oracle, creating circularity" (from Harsh Critic).** Noted in passing but does not affect the paper's main claims about confounds in prior work. The paper's re-evaluation does not depend on this point.

- **"Reproducibility statement is weak; code should be available at submission" (from Harsh Critic).** Per hard rules, code availability after review is standard practice and not a weakness that should carry weight in evaluation.

- **"Missing appendix/proofs" (from Strength Finder).** Per hard rules, the parser strips these sections from all papers; they exist in the original submission.

- **"Pure formatting/style nitpicks."** Removed per hard rules.

- **Various speculation-based concerns and area-of-concern sweeps without concrete anchors in the paper.** Removed per filtering discipline.

- **Strength Finder's generic strengths about "important problem" or "interesting question."** These are superficial and lack specific content; dropped.

## Novel Insights

The key meta-insight from synthesizing the reviews is that this paper's two contributions operate at different levels of completeness. The re-evaluation of TORCS and KAREL is thorough, well-controlled, and convincingly demonstrates that prior reported advantages were inflated by confounds. The positive thesis—that programmatic representations matter when instance-scaling working memory is required—is theoretically well-motivated (the capacity argument is sound) but the empirical support is thin: the FUNSEARCH proof-of-concept is program synthesis, not RL, and there is no direct comparison with neural baselines on the critical problem class. This asymmetry between a well-supported critique and a promissory positive thesis is the paper's central structural tension. A cleaner paper would either commit fully to the re-evaluation (dropping the proof-of-concept) or substantially expand the positive evidence.

## Suggestions

1. **Address the seed selection issue directly:** Either report OOD results for *all* seeds (including failures), or reframe the contribution around robustness vs. brittleness rather than claiming equivalence.
2. **Either expand or remove the proof-of-concept:** A proper RL experiment on the wall-sparse maze comparing a programmatic method against neural baselines would substantially strengthen the paper. If this is not feasible, remove the proof-of-concept and position the paper as a re-evaluation + theoretical framework.
3. **Add confidence intervals or statistical tests** for TORCS and KAREL results.
4. **Clarify the KAREL framing:** Acknowledge explicitly that the paper shows a *different* architecture closes the gap, not that the original baselines work with better tuning.
5. **Discuss why HARVESTER fails** where the other four KAREL tasks succeed.
6. **Distinguish more carefully** between "existence of a representation" and "provable generalization guarantees" when discussing memory-augmented neural architectures.

---

## Calibration Anchors

All anchors retrieved across rounds (path, avg human score, round, comparison):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/It4KL6XnPq.md | 3.00 | R1 (low) | Much weaker paper; no direct topical relevance |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/N18Z2MkMEa.md | 3.00 | R1 (low) | Much weaker; unrelated topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NGVljI6HkR.md | 3.67 | R1 (mid) | Similar topic (programmatic vs latent spaces) but weaker execution; significant clarity and detail issues reported. Current paper is clearly stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lUWf41nR4v.md | 4.50 | R1 (mid) | Program synthesis + state machines; has missing detail and baseline concerns. Current paper is somewhat stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tuEP424UQ5.md | 5.75 | R1 (mid) | MORL generalization benchmark. Comparable quality; both have solid contributions but limited novelty. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/X1p0eNzTGH.md | 5.67 | R2 | Level sampling for ZSG; has significant clarity/overclaim issues. Current paper is clearly stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/UfczlMudN6.md | 6.00 | R2 | GRAM — new method for RL generalization with good scores but limited generality; rejected despite 6s. Current paper comparable. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/3w6xuXDOdY.md | 6.50 | R2 | Offline RL generalization benchmark; cleaner evaluation, accepted. Current paper slightly weaker due to seed selection issue and thin proof-of-concept. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Y1XkzMJpPd.md | 6.75 | R1 (mid) | OMNI-EPIC open-endedness; different topic. Current paper not directly comparable. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/m3xVPaZp6Z.md | 7.50 | R2 | Policy Rehearsing; method paper with strong results. Current paper weaker than this anchor. |

**Round 1 bracket:** 5.0–6.5  
**Round 2 narrowing:** Placing the paper between the 5.67 anchor (weaker paper with significant issues) and the 6.50 anchor (stronger, cleaner benchmark study), and comparable to the 6.00 GRAM anchor (similar-level concerns). The seed selection bias in TORCS and the thin proof-of-concept prevent the paper from reaching the 6.0–6.5 range, while the solid re-evaluation experiments and useful framework place it clearly above the 4.5–5.0 range.

**Final score: 5.5**

<score>5.5</score>
<decision>Accept</decision>