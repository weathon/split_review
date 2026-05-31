## Summary
The paper proposes **MadDist** and **TDMadDist**, self-supervised objectives to learn a state embedding whose induced (quasi)metric approximates the **Minimum Action Distance (MAD)**—the minimum number of actions needed to go from one state to another—**using only state trajectories (no rewards, no actions)**. It further introduces quasimetric parameterizations to support asymmetry and evaluates on a suite of environments where ground-truth MAD is available.

## Strengths
- **Clear objective and learning signal based purely on state sequences.** The core loss directly ties embedding distance to temporal separation along trajectories: Eq. (5) optimizes \((d_\theta(s_i,s_j)/(j-i)-1)^2\) over pairs sampled from trajectories (Section 6.1, Eq. 5), making the “state-only” setup concrete rather than aspirational.
- **Explicit support for asymmetric distances via quasimetric constructions.** The paper defines quasimetrics (e.g., IQE variants) and uses them to build an asymmetric distance \(d_\phi(s,s')=d_q(\phi(s),\phi(s'))\) (Section 5–6; see the construction around lines ~120–127), aligning with the fact that reachability distances in MDPs are generally directed.

## Weaknesses

### Fatal
None.

### Major
- **The training objective is trajectory-step distance, but the paper repeatedly claims it learns environment MAD (“minimum number of actions required”), which is not identified from state-only trajectories without strong coverage assumptions.**  
  Concretely, Eq. (5) supervises \(d_\theta(s_i,s_j)\approx (j-i)\) for state pairs *as they occur in the dataset trajectories* (Section 6.1, Eq. 5). This is, at face value, a form of “distance along observed rollouts” rather than the *minimum over actions/policies* required by the MAD definition in the Abstract (“minimum number of actions required to transition between states,” line 9). The paper does not (in the extracted main text) spell out assumptions under which these coincide (e.g., full support exploration / observing all 1-step feasible transitions). Without those assumptions, the central claim is over-broad: multiple MDPs/behavior policies can yield the same state-only trajectory distribution while having different action-graph shortest paths, so “MAD from states alone” is not well-posed in general.

- **MAD’s meaning in stochastic environments is not defined precisely, yet the paper claims broad stochastic evaluation.**  
  The Abstract explicitly claims coverage of “stochastic dynamics” (line 9), and the Conclusion concedes MAD is mainly a heuristic there and contrasts it with SPD (“future work will explore whether it is possible to recover the Shortest Path Distance (SPD)…” lines 261–264). However, the extracted main text does not provide a precise stochastic definition (e.g., support-based reachability vs probability-threshold reachability vs expected steps). Since those notions can produce materially different “minimum action distances,” it is hard to interpret what it means to “learn accurate MAD representations” in stochastic settings (Abstract, line 9) or whether the objective (Eq. 5) corresponds to that definition.

### Minor
- **Downstream-utility claims are stated strongly but (in the extracted main text) are not backed by presented downstream experiments.**  
  The Abstract and Introduction assert MAD “naturally enables critical downstream tasks such as goal-conditioned reinforcement learning and reward shaping” (Abstract, line 9) and the Conclusion suggests incorporation into downstream tasks (lines 261–262). In the provided extracted text, I do not see actual downstream RL/planning results (tables/figures are not present here), so these claims should be phrased more cautiously unless the full paper section (not visible in the excerpt) contains those results.

### Trivial
None.

## Nice-to-Haves
- Add an explicit “when does Eq. (5) recover MAD?” proposition/lemma (even informal) stating sufficient conditions (e.g., determinism + coverage of all 1-step edges; or behavior-policy graph distance as the true target) and then align the experimental protocol to those conditions.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“Baselines unfair / comparison likely conflated”**: removed because the extracted paper text provided does not include the experiments/baselines/tables, so I cannot anchor a concrete, verifiable unfairness claim to a specific table/figure or protocol description.
- **“Table 1 shows near-perfect planning success in OGBench PointMaze”** (Strength Finder): removed because Table 1 / PointMaze results are not present in the extracted text available here; I cannot verify this strength from the paper content provided.

## Novel Insights
A key (and fixable) mismatch is that the *implemented supervision signal* (Eq. 5: matching embedding distance to **temporal index gap along observed trajectories**) is naturally a **behavior-policy/dataset notion of distance**, while the *stated target* (MAD: minimum number of actions “required” between states) is an **optimal-control/action-graph notion**. Making this distinction explicit—possibly by renaming the learned quantity as “trajectory distance” unless coverage assumptions hold—would substantially improve the paper’s conceptual correctness without necessarily changing the algorithm.

## Suggestions
- State explicitly whether the learned target is (a) **dataset graph shortest-path length**, (b) **environment MAD under optimal control**, or (c) some stochastic variant, and give conditions under which (a)=(b).
- For stochastic environments, define MAD formally (support-based / probability-threshold / expected-steps) and ensure both “ground-truth MAD” computation and learning objective correspond to that definition.
- If the full paper does contain downstream planning/RL experiments, ensure the Abstract’s “enables critical downstream tasks” wording is backed by a concrete reported result; otherwise soften to “can be used as a heuristic for …”.

## Score and Decision
**Originality/importance:** high-level idea (state-only learning of controllability geometry) is important; asymmetry via quasimetrics is a reasonable technical angle.  
**Support for claims / experimental soundness:** the core conceptual claim (“learn MAD without actions”) is currently **overstated relative to what the objective provably identifies**; stochastic definition ambiguity further weakens the evidential story.  
**Clarity:** method equations are clear, but the *target quantity* needs sharper definition/assumptions.  
**Value:** could be valuable if reframed with correct identifiability statements and clarified stochastic semantics.

MY FINAL SCORE: <score>5.0</score>  
MY FINAL DECISION: <decision>Reject</decision>