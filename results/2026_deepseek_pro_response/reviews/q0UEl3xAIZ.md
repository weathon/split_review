Now I have a good sense of the calibration. Let me finalize the review.

**Bracket from Round 1:** The paper sits between weak anchors (~3.0) and strong anchors (~8.0). Comparing to the middle-band anchors (4.75–6.80), it's on the lower end.

**Round 2 narrowing:** Our paper is:
- Better than YKW98Icu1X (3.75, chess puzzles) — cleaner methodology, clearer results
- Comparable to nRgGCnw8eZ (4.00, poker abstraction) — similar contribution type but cleaner presentation
- Slightly below czpx02orl7 (4.75, abstract world models) — less theoretical ambition but cleaner execution
- Clearly below 5e0yWSNGIc (5.33) and 7J0NsFXnFd (5.25) — less novelty and significance

**Final score: 4.5.** A solid validation study with genuine results but limited novelty for ICLR, and the overclaiming about NE equivalence weakens the contribution.

---

## Summary

This paper applies GOEI (Goal-Oriented Environment Inference), a model-based RL algorithm for state abstraction proposed in prior work (Takahashi et al., 2024), to a 5-card variant of the competitive card game "Hol's der Geier." The authors demonstrate that GOEI learns a compact state representation (452 states, 2.9% of 15,542 possible observations) while achieving near-zero reward rate against a Nash equilibrium opponent, substantially outperforming tabular Q-learning. The paper includes a mutual information analysis of the reduced representation and a parameter sensitivity study.

## Strengths

- **Clear quantitative evidence of substantial state compression with preserved performance**: The best GOEI configuration (β=0.2, α=25) achieves a median reward rate of −0.010 against the NE opponent while using only 452 states across 4 rounds (Table 1). The learning curves (Figure 2A) show rapid convergence within ~500 epochs.

- **Convincing superiority over Q-learning on identical training data**: Q-learning at its best learning rate plateaus at approximately −0.079 against NE (Table 1), while GOEI converges to −0.010. This cleanly isolates state reduction as the enabling factor over raw value estimation.

- **GOEI's states are smaller than NE's own representation at intermediate rounds**: At rounds 2 and 3, GOEI produces 8 and 31 states respectively, compared to NE's 247 and 945 states (Table 1). This is a genuinely interesting result — GOEI discovers a more parsimonious representation than the game's own Nash equilibrium structure.

- **Information-theoretic analysis of what the reduced representation preserves**: The mutual information decomposition (Section 4.2, Figure 3) shows that GOEI discards most per-feature information while preserving task-relevant signals (current table card, score difference at critical rounds). This moves beyond a black-box state count.

- **Rigorous separation of inference from optimization**: Training on fixed-policy games and testing via the optimal Bellman equation on the learned model (Section 3.3) cleanly isolates GOEI's inference quality from exploration–exploitation confounds.

## Weaknesses

### Fatal

None.

### Major

- **The claim of "Nash equilibrium equivalence" overstates what was demonstrated**: The abstract states GOEI "achieves a nearly optimal strategy equivalent to the Nash equilibrium." However, the evaluation tests GOEI's strategy against only one opponent — the NE strategy itself. A reward rate of approximately 0 against NE is necessary but not sufficient for being an NE strategy; a strategy can tie with NE while being exploitable by other strategies. The paper itself acknowledges (line 48) that "better strategies exist against a certain fixed strategy other than NE," yet no tests against π₀, π₁, Rand, or any other opponent are reported. Furthermore, training on (Rand, NE) trajectories and testing against NE creates a closed distributional loop — GOEI learns on exactly the states NE visits. This means the result demonstrates imitation on NE's distribution, not necessarily recovery of the game's core structure. The claim should be weakened to what was actually shown: near-zero loss against the NE opponent with dramatic state compression.

### Minor

- **The explainability motivation is prominently asserted but explicitly abandoned**: The introduction (lines 13–17) builds the case for GOEI around explainability (DNNs "lack explainability," XAI methods are "local and limited in scope"). Yet the Discussion (lines 238–239) states: "we could not give a verbal explanation of the reduced state representation more concretely than Figure 3." The abstract does not mention this limitation. The paper's actual achievement — extreme state compression with preserved performance — is a valid contribution on its own, but the framing mismatch between introduction and results creates unmet expectations.

- **Single-environment evaluation limits what we learn about GOEI**: The paper tests GOEI on one new environment beyond the original abstract toy domain. While the 5-card Hol's der Geier variant is more complex than the original, we learn nothing about boundary conditions, scaling behavior, or which environment properties make GOEI's compression effective. One new environment that mirrors the original paper's findings is a thin contribution for a standalone paper.

- **The sufficiency condition (Equation 4) is never empirically verified**: The paper defines the formal condition for valid state reduction — that the reduced representation must predict the final reward given any action sequence — but relies entirely on downstream performance as a proxy. A direct comparison of reward predictions under the full vs. reduced model would strengthen the claim that the reduction is valid rather than merely performant in this narrow evaluation.

### Trivial

- The abstract's headline "2.9% (452 states) of all possible observations (15,542)" obscures that at round 4 GOEI uses more states (408) than NE does (69); the compression is driven by rounds 2 and 3.

## Nice-to-Haves

- Testing GOEI's learned policy against a panel of opponents (π₀, π₁, Rand) would distinguish "ties with NE on NE's distribution" from "is actually a Nash equilibrium strategy."
- Reporting the Nash equilibrium strategy explicitly (action probabilities in key states) would help readers understand what GOEI is and isn't recovering.
- A discussion of how GOEI's state clustering relates to other state abstraction methods (e.g., bisimulation) would contextualize the results.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Q-learning at η=0.2 is not the strongest baseline; function approximation or eligibility traces could improve it"** — REMOVED. The paper's comparison is against tabular Q-learning, the appropriate baseline for demonstrating that state reduction matters when using tabular methods. Function approximation addresses a different problem.

- **Harsh Critic: "The claim about Bayesian inference being independent of the true causal direction lacks citation"** — REMOVED. This is a standard property of Bayesian inference over joint distributions; the factorization direction does not affect the posterior.

- **Harsh Critic: "No measure of variance for state counts |S*| in Table 1"** — REMOVED. Figure 2B shows quartile ranges for state counts; Table 1 reports medians, which is standard practice.

- **Harsh Critic: "The transition from 28,477 total observations to 15,542 reachable under NE is stated without derivation"** — REMOVED. The paper explains this on line 134: the restriction is "because of action sequences never caused by the NE strategy."

- **Harsh Critic: "Missing comparison to other state abstraction methods"** — REMOVED. This is scope creep for a validation study of a specific existing method.

- **Harsh Critic: The π_k strategy definition lacks justification** — REMOVED. Section 2.2 introduces these as commonly used human strategies with clear mathematical definitions.

- **Strength Finder: "Rigorous separation of environment inference from strategy optimization in evaluation"** — Kept as a genuine strength.

## Novel Insights

The most interesting finding is that GOEI produces fewer states than the Nash equilibrium itself at intermediate rounds (8 vs. 247 at round 2, 31 vs. 945 at round 3), yet matches NE's performance. This suggests GOEI discovers a representation more compact than the game's strategic structure, which is a non-obvious and potentially significant observation about what "core" means in competitive settings.

## Suggestions

- Reframe the paper around compression rather than explainability. The abstract and introduction should lead with what the paper actually demonstrates (extreme state compression with preserved performance), not the explainability goal it acknowledges it cannot deliver.
- Add even a single test of GOEI's learned policy against a non-NE opponent (e.g., π₀ or Rand) to demonstrate the strategy is generally sound, not just calibrated to NE's distribution.
- Verify Equation (4) empirically by comparing reward predictions under the full vs. reduced model for a representative subset of states.

## Score and Decision

**Calibration anchors:**
- YKW98Icu1X (avg 3.75, Round 2): chess puzzle recommendation — weaker than our paper; weaker evaluation, less clear results
- nRgGCnw8eZ (avg 4.00, Round 2): poker hand abstraction — comparable contribution type, our paper has cleaner presentation and clearer results
- czpx02orl7 (avg 4.75, Rounds 1&2): abstract world models with options — more theoretical ambition but more technical issues; our paper is cleaner but narrower
- 5e0yWSNGIc (avg 5.33, Round 2): certified training analysis — better than our paper; clearer novelty and broader significance
- 7J0NsFXnFd (avg 5.25, Rounds 1&2): action abstraction for IIEFGs — better than our paper; novel method with stronger engineering contribution
- hgwGi81ndj (avg 6.80, Round 1): object-centric abstraction — much stronger; novel method with strong results
- xIUUnzrUtD (avg 6.50, Round 1): abstract representations from sequences — much stronger
- stUKwWBuBm (avg 8.00, Round 1): tractable multi-agent RL — top-tier paper; not comparable

This paper is a solid validation study with genuine results but limited novelty for ICLR. The overclaiming about NE equivalence weakens the central claim. The contribution — demonstrating GOEI works on one more environment — is thin for a standalone paper at this venue. Score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>