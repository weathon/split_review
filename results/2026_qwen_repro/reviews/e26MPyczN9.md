Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

---

## Summary

This paper re-evaluates three influential claims of programmatic policy superiority in reinforcement learning (TORCS, KAREL, PARKING), showing that controlled experimental factors—cautious reward shaping in TORCS and sparse observations in KAREL—substantially close the reported generalization gap between neural and programmatic representations. Building on this, it introduces a formal expressivity/discoverability framework (Definitions 2–3) and identifies memory-scaling problems (pathfinding, nested subproblems) as a class where programmatic policies have inherent structural advantages, validated with a FUNSEARCH-synthesized BFS program.

## Strengths

- **Sound re-evaluation design with clear evidence.** In TORCS, reducing the speed-weighting parameter β from 1.0 to 0.5 in the intrinsic reward allows DDPG to match NDPS on unseen tracks (Table 1: 76% of seeds generalize from G-TRACK-1, 100% from AALBORG). In KAREL, augmenting observations with the previous action enables feedforward PPO to match LEAPS on 100×100 mazes across STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER (Table 2: all 1.00 return). These are concrete, replicable demonstrations that the original neural failures were driven by reward misspecification and observation design, not representational incapacity.
- **Clean analytical framework distinguishing expressivity from discoverability.** Definitions 2 and 3 formalize the distinction between whether a solution *exists* within a representation and whether a search algorithm can *find* it. This provides a useful lens for diagnosing why prior comparisons may have reported programmatic advantages even when both representations were expressive.
- **Honest reporting of failure modes.** The PARKING results (Table 3) show neither representation generalizes well (PSM: 0.16 success rate, DQN: 0.18). Rather than forcing a narrative of programmatic superiority, the authors correctly frame PARKING as an open challenge and a target for future representational design.
- **Substantive theoretical insight on memory-scaling problems.** The argument that fixed-capacity neural architectures (feedforward and RNNs with bounded hidden state width) cannot represent solutions requiring working memory that grows with input size is technically sound and relevant—pathfinding, nested subproblem handling, and similar algorithmically structured tasks genuinely demand this property.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing bridge between re-evaluation benchmarks and the expressivity framework.** The paper runs three benchmarks (Section 4) and then introduces a theoretical framework in Section 5 about memory-scaling problems, but never analyzes whether TORCS or KAREL fall into the class where neural expressivity holds but discoverability failed, or whether they are constant-memory problems where both representations are expressive. The paper notes briefly in Section 4.4 that KAREL's maze admits wall-following (constant memory), and that PARKING *might* point in the direction of distinguishing representations, but this connection is never systematically developed or tested. This leaves the reader unable to assess whether the paper's own experimental results are consistent with its own theoretical framework. — This weakens the coherence of the two-part structure.

- **FUNSEARCH proof-of-concept is under-documented.** Section 5 reports that three runs of FUNSEARCH each returned a correct BFS implementation and that it generalizes to any pathfinding problem, but provides no detail on: the modified KAREL task formulation (SparseMaze is referenced as Figure 7 but not described in the main text), how the synthesized program interacts with the environment at test time, what evaluation protocol was used beyond "provably generalizes." Three runs with 3 successes and no variance, no comparison to simpler search, is insufficient to support what is presented as evidence for the expressivity claim. — The claim survives but is not strongly substantiated.

- **The claim that programmatic and neural policy spaces are "similar" is informal.** In Section 5, the paper asserts that the TORCS DSL induces "a space resembling ReLU networks" citing Orfanos & Lelis (2023), and states that "if the programmatic space had solutions that generalized, then the neural space also encoded such solutions." This is a strong claim about representational overlap that is asserted rather than measured. No quantitative comparison of the two spaces is provided. — This undermines the rigor of the equivalence argument, though the paper's empirical results still support the qualitative claim.

- **The LSTM failure in KAREL is under-analyzed.** Table 2 shows that PPO with LSTM fails to learn even on small problems in several cases (e.g., STAIRCLIMBER: 0.13 return, TOPOFF: 0.63), yet the paper notes only that "LSTMs can, in practice, approximate finite-state machines" and says "we could not adjust learning to yield generalizable solutions." Why the LSTM search fails is not analyzed. Given the paper's emphasis on discoverability, this is a missed opportunity to illustrate the discoverability concept concretely. — A brief analysis would strengthen the paper's own framework.

### Trivial

- The paper states "BFS provably generalizes OOD" but the "proof" is a standard correctness property of BFS, not a novel contribution. The paper should clarify this is an established algorithm, not a new proof.

## Nice-to-Haves

- Include more FUNSEARCH details in the appendix: the SparseMaze task definition, evaluation protocol, sample efficiency, and a comparison to what a gradient-based method would find on the same task.
- Add a brief analysis of the PARKING failure mode: is it expressivity or discoverability? Even a speculative discussion would strengthen the paper's argument.
- Consider explicitly checking whether the three re-evaluated benchmarks are constant-memory or memory-scaling problems, and adding this characterization as a table or figure.

## Removed Points

These points are flagged to be removed—treat with caution:

- **Harsh Critic Point 1 (conflate representational effect with unfair comparison):** The critic argues that programmatic policies' inability to optimize aggressively is a representational property (implicit regularization), not a "confind." While this reframing has merit, the paper explicitly separates intrinsic reward from the evaluation metric (Equation 2): the reward is a training signal, not a change to the underlying task. The criticism, while insightful, is a matter of framing rather than factual error. Removed as a difference of interpretation, not a concrete flaw.

- **Harsh Critic Point 3 (PARKING undermines conclusions):** The critic claims DQN marginally outperforms PSM on PARKING (18% vs 16%), undermining the narrative. However, the paper explicitly acknowledges this in Section 4.3 and frames PARKING as a domain where "neither representation works well." The data do not contradict the paper's stated conclusions—it just doesn't support a clear winner. Removed as overstated.

- **Strength Finder: Systematic ablation in KAREL:** The claim that the paper "carefully decouples" partial observability from recurrence is partially overstated—the experiment augments observations rather than systematically ablating them, and PPO with ConvNet data is from prior work. I keep the strength but soften it: the KAREL results are informative but not as rigorously designed as claimed.

- **Hard Rules removed:** Criticisms about TORCS reward design being unfair comparisons (removed under scope/filtering); criticisms about missing proofs or appendix material (removed—parser strips these sections); general statements about "evaluation lacks rigor" or "bridging is missing" that were not anchored to specific tables/sentences were verified or removed.

## Novel Insights

The most genuinely novel observation in the reviews is the tension identified by the harsh critic: the paper's "confind" framing for TORCS may obscure a real representational finding. The observation that programmatic policies' restricted expressivity *happens* to prevent overfitting to speed is not just semantics—it's a practical phenomenon with implications for representation design that the paper could have developed rather than dismissing as a confound. This reframing (programmatic representations as regularizers by construction) is an insight the paper itself does not explicitly articulate, and it could strengthen the paper's contribution to representation design in RL.

## Suggestions

- Add a table or section explicitly characterizing each re-evaluated benchmark along the expressivity/discoverability axes (e.g., "TORCS: expressive for both, discoverability controlled by reward; KAREL: expressive for both, discoverability controlled by observations; PARKING: unknown expressivity, neither discoverable"). This would directly connect Parts 1 and 2.
- Clarify in Section 5 whether the TORCS/ReLU similarity claim is a qualitative analogy or a formal result, and cite Orfanos & Lelis with more specificity about what is proven.
- Include the SparseMaze/SparseKarel task description (Figure 7) in the main text or appendix so the FUNSEARCH results are interpretable.

## Score and Decision

**Round 1 — Bracketing:** I retrieved anchors across three score bands on related topics (RL generalization, benchmark re-evaluation, programmatic vs neural representations). The strong anchors (8.0) are mechanistically interpretive or well-motivated benchmark papers with extensive experiments. The middle anchors range from 5.5 to 6.5. The weak anchors (2.0–3.0) have fundamental methodological flaws or overclaims. Based on these comparisons, the plausible bracket for this paper is **5.5–7.0**.

**Round 2 — Narrowing:** Within this bracket, I examined:
- *The Generalization Gap in Offline RL* (score 6.5): A benchmark-focused re-evaluation paper with thorough experiments and clear conclusions. This paper is similar in spirit: empirical re-evaluation, well-designed experiments, but limited in scope (no new method proposed). This paper has a slightly stronger theoretical framing (expressivity/discoverability) but less thorough experimental coverage (3 domains vs. 8+). Comparable or slightly below.
- *On Generalization Within MORL* (score 5.75): Also a generalization study with formalization + benchmark. This paper's empirical contribution (concrete re-evaluations closing the gap) is stronger. This paper should score above this anchor.
- *How the Level Sampling Process impacts ZSG* (score 5.67): Has some soundness concerns (MI never measured despite central claims). This paper's claims are better supported by actual experiment data. This paper should score above this anchor.
- *Improving Generalization of Meta RL via Explanation* (score 4.2): Has significant methodological concerns and presentation issues. This paper is clearly stronger.

**Round 1 bracket:** 5.5–7.0.  
**Round 2 narrowing:** The paper sits between the 5.75 MORL anchor and the 6.5 offline RL anchor. The paper's empirical re-evaluations are well-executed and clearly demonstrate their claims (unlike the MORL paper's metric issues), but the lack of integration between Parts 1 and 2 and the thin FUNSEARCH documentation hold it below the offline RL paper. The expressivity/discoverability framework adds genuine value but is not as rigorously developed as a theoretical contribution would require.

**Anchor list:**
- DzGe40glxs.md (8.0, Round 1 strong): Mechanistic interpretability in RL — stronger theoretical/motivational grounding, not directly comparable.
- 9pW2J49flQ.md (8.0, Round 1 strong): LTL instruction learning — different topic.
- OI3RoHoWAN.md (8.0, Round 1 strong): LLM task generation — different topic.
- pISLZG7ktL.md (8.0, Round 1 strong): Data scaling in imitation learning — different topic.
- It4KL6XnPq.md (3.0, Round 1 weak): Foundation policies with memory — weaker paper.
- fvTaoyH96Z.md (2.33, Round 1 weak): Randomization for generalization — flawed paper.
- MpA6HMD7Wq.md (3.0, Round 1 weak): Symbolic vs black-box in learned optimization — different topic, weaker.
- hCfhfwSfCg.md (2.0, Round 1 weak): LLM-guided exploration — weak paper.
- NGVljI6HkR.md (3.67, Round 1 middle): Programmatic vs latent spaces — directly related but much weaker.
- lUWf41nR4v.md (4.5, Round 1 middle): Program synthesis + state machines — different approach, weaker.
- tuEP424UQ5.md (5.75, Round 1 & 2 middle): MORL generalization benchmark — comparable paper, this paper is slightly stronger on empirical grounding.
- 3w6xuXDOdY.md (6.5, Round 1 & 2 middle): Offline RL generalization gap — closest anchor, this paper has similar empirical rigor but less breadth; slightly below.
- qg5JENs0N4.md (5.5, Round 2 middle): TD vs SL stitching — related to generalization, this paper is clearer and better supported.
- PR6RMsxuW7.md (6.25, Round 2 middle): Planning + DRL integration — different topic, comparable quality.
- vTLLyVCsrD.md (4.2, Round 2 middle): Meta-RL explanation — methodologically more flawed.
- X1p0eNzTGH.md (5.67, Round 2 middle): Level sampling for ZSG — has soundness issues, this paper is stronger.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>