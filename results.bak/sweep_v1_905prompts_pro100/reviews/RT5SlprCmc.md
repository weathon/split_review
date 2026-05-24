Now I have a solid picture of where this paper sits. Let me compose the final review.

---

## Summary

This paper presents MadDist and TDMadDist, two self-supervised algorithms for learning the Minimum Action Distance (MAD) from state-only trajectories. The key novelty is the use of asymmetric quasimetric distance functions — including a newly proposed simple quasimetric (d_simple) — to capture directional structure that symmetric embeddings miss. The paper evaluates on a diverse suite of environments with known ground-truth MAD, spanning discrete/continuous state spaces, deterministic/stochastic dynamics, and strongly asymmetric settings. MadDist consistently outperforms both a quasimetric RL baseline (QRL) and a symmetric Hilbert embedding baseline, and the learned distances translate to strong performance on downstream goal-oriented planning.

## Strengths

- **Asymmetric quasimetric support demonstrably improves MAD recovery in directional environments.** In CliffWalking and KeyDoorGridWorld, MadDist achieves Ratio CV of ~0.1–0.2 while the symmetric Hilbert baseline remains above 0.35 and 0.6 respectively (Figure 3). This directly validates the paper's central claim that asymmetry matters.

- **Global trajectory supervision yields more accurate representations than local constraints alone.** MadDist's loss combines scaled trajectory-index regression (Eq. 5), upper-bound constraints across arbitrary trajectory spans (Eq. 7), and a contrastive repulsion term (Eq. 6). Across all environments, this produces higher Pearson correlation and substantially lower Ratio CV than QRL, which only enforces local locality constraints (Figure 3).

- **A diverse, reproducible benchmark suite with known ground-truth MAD.** The paper introduces environments spanning discrete (CliffWalking, KeyDoorGridWorld) and continuous (PointMaze, OGBench) state spaces, deterministic and stochastic dynamics, noisy observations, and strong asymmetry — all with computable ground-truth MAD. This enables precise quantitative evaluation and serves as a testbed for future work.

- **Strong downstream planning results.** The learned MadDist embeddings translate to near-perfect success rates on OGBench PointMaze planning tasks (Table 1), including the challenging Stitch environments that require composing information from disconnected trajectories.

## Weaknesses

### Fatal

None.

### Major

- **The experimental data description contains a contradiction that undermines clarity, though not validity.** Section 7 states: "Each method was trained for 50,000 gradient steps on an offline dataset gathered by a random policy." However, the OGBench PointMaze datasets are explicitly described (line 330) as *navigate* ("collected by a noisy expert policy") and *stitch* ("short goal-reaching trajectories") — neither of which is a random policy. The OGBench results almost certainly use the provided navigate/stitch datasets (standard in the literature), but the paper's blanket "random policy" statement is inconsistent with this. This needs correction but does not invalidate the comparative results.

### Minor

- **Evaluation protocol for learned distance functions is underspecified.** The paper reports Spearman/Pearson correlations and Ratio CV for state pairs but never specifies how evaluation pairs are sampled. If pairs are drawn only from training trajectories, the high correlations could reflect interpolation rather than generalization. The methodology for sampling evaluation pairs should be stated explicitly.

- **The planning experiment setup is deferred to a stripped appendix.** Table 1 reports near-perfect success rates (1.00 ± 0.00 in four environments) but the planning methodology is only summarized with "a detailed description … provided in Appendix H." Without knowing whether planning involves greedy following, search, or something else — and how goals relate to training data — the practical significance is harder to assess.

- **TDMadDist's underperformance relative to MadDist receives minimal analysis.** The paper acknowledges that TDMadDist underperforms MadDist (and sometimes QRL) in most settings but does not investigate why the TD formulation degrades performance. Since TDMadDist is presented as a co-equal algorithmic contribution, a brief diagnostic (target update rate, error accumulation, etc.) would strengthen the paper.

- **The contrastive loss L_r (Eq. 6) is not ablated or justified.** This term pushes randomly sampled state pairs apart, encouraging d_θ(s, s') to exceed d_max. In many environments, two randomly sampled states can be genuinely close; the inductive bias this term introduces could potentially conflict with upper-bound constraints. Its contribution is never isolated empirically or justified theoretically in the main text.

### Trivial

- The data collection paragraph should distinguish between custom environments (random policy) and OGBench (provided navigate/stitch datasets) to avoid apparent contradiction.
- Missing discussion of hyperparameter sensitivity (w_r, w_c, d_max, H_c) — Appendix D is stripped but even a brief note in the main text would help.

## Nice-to-Haves

- A direct comparison with the symmetric method from Steccanella & Jonsson (2022) — which forms the backbone of the MadDist loss — would isolate the effect of asymmetry and the scale-invariant loss more sharply than the Hilbert baseline alone.
- An ablation removing or varying L_r to assess its contribution to MadDist's performance.
- A discussion of when the method might *fail* to recover the true MAD, to bound its applicability.

## Removed Points

These points from the harsh critic were considered but removed or downgraded:

- **"Equation 9 is garbled" (formatting/parser issue):** The equation rendering artifacts are a parser problem, not an author error. The intended equation is clear from context. → REMOVED per formatting nitpick rule.

- **"TDMadDist consistently underperforms" as a fatal claim:** The harsh critic framed this as undermining confidence in the whole framework. The paper presents MadDist as the primary method and TDMadDist as secondary; underperformance of a secondary variant does not invalidate the primary contribution. → Retained only as Minor.

- **"Missing comparison with Steccanella & Jonsson (2022)" as fatal:** The paper includes the Hilbert baseline (a symmetric embedding that also approximates MAD), which already demonstrates the value of asymmetry. Adding Steccanella & Jonsson would strengthen the ablation but its absence does not invalidate the core claim. → Moved to Nice-to-Haves.

- **"Random policy on 100×100 maze would be ineffective, results implausible":** The harsh critic argues that if a random policy were used on OGBench Giant Maze, the results would be impossible. This is correct — but the actual results almost certainly use the provided navigate/stitch datasets (as the environment names indicate), not a random policy. The issue is a description error, not a validity error. → Retained as Major (presentation).

- **"Perfect success rates suspicious":** The harsh critic suggests the 1.00 ± 0.00 results could indicate information leakage. This is speculative — without the appendix, we cannot assess the planning setup. The point is absorbed into the Minor weakness about appendix-deferred description. → Demoted.

- **"Inefficiency of Floyd-Warshall vs. SSP discussion is irrelevant":** The harsh critic notes the computational advantage of MAD over SSP only applies when the graph is known, not in the learning-from-trajectories setting. This is a fair observation but does not constitute a weakness — the paper correctly states MAD is efficient to compute when the graph is known and robust to probability changes. → REMOVED as a nitpick that misunderstands the paper's context-setting.

- **Strengths removed from Strength Finder:** "A simple, scalable quasimetric proves effective" — the ablation is in Appendix E (stripped), so this claim cannot be verified from the visible text. → Demoted, noted in review as conditional on appendix.

- **Speculative "contrastive loss could distort embedding" critique:** The harsh critic speculates that L_r could conflict with upper-bound constraints. The paper does not ablate this, so the concern is reasonable but speculative. → Retained as Minor, not elevated to Major.

## Novel Insights

Beyond the paper's own contributions, the review process highlights a methodological tension: the value of asymmetric quasimetrics for MAD learning is convincingly demonstrated, but the precise contribution of individual loss components (scaled regression vs. upper-bound constraints vs. contrastive repulsion) remains entangled. Future work that systematically ablates these components — ideally with a symmetric MadDist variant as a controlled comparison — could produce sharper insights about which design choices matter most.

## Suggestions

- Revise the data collection paragraph to distinguish between environments where a random policy was used (CliffWalking, NoisyGridWorld, KeyDoorGridWorld, UMaze, MediumMaze) and OGBench environments where the standard navigate/stitch datasets were used. This resolves the contradiction without any change to results.
- Specify how evaluation state pairs are sampled, ideally in the main text. If pairs are drawn uniformly from the state space, state that explicitly; if from held-out trajectories, describe the split.
- Either add a brief analysis of TDMadDist's failure modes (target update rate, error accumulation) or clearly position it as a preliminary exploration rather than a co-equal contribution.
- Ablate L_r to quantify its contribution — a single figure showing MadDist with and without L_r would substantially strengthen the paper.

## Score and Decision

**Round 1 bracketing:** Low band anchors (2.5–3.0) were in unrelated domains. Middle band (3.75–6.20) contained the most relevant comparators: Action Distances for PbRL (3.75), State Chrono Representation (4.75), Distributional Distance Classifiers (6.00). High band (8.0) contained theory-heavy or different-domain papers. Initial bracket: 4.5–7.0.

**Round 2 narrowing:** Retrieved BS-MPC (5.50), Distributional SM (5.75), ETD (6.75), Unbalanced Atlas (6.67). This paper is clearly stronger than BS-MPC (which was criticized for marginal novelty and inconsistent results) and Distributional SM (toy experiments), and comparable to ETD (6.75) in quality, though ETD has more thorough evaluation while this paper offers a cleaner methodological contribution. The presentation issues (data description contradiction, missing evaluation protocol) pull it slightly below ETD.

**Anchor comparison summary:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| oEzY6fRUMH (State Chrono Rep) | 4.75 | R1 | Our paper is stronger: cleaner method, better results, more diverse environments |
| F07ic7huE3 (BS-MPC) | 5.50 | R2 | Our paper is stronger: clearer conceptual gap, more consistent empirical gains |
| OMwD6pGYB4 (Distributional SM) | 5.75 | R2 | Our paper is stronger: much stronger empirical validation |
| qofh48zW3T (Dist. Distance Classifiers) | 6.00 | R1 | Comparable: both address distance learning for RL; ours has broader environment coverage |
| I7DeajDEx7 (ETD) | 6.75 | R2 | ETD slightly stronger: more thorough ablations and evaluation; ours has cleaner novelty |

**Final score:** 6.0

The paper makes a genuine, well-motivated contribution — asymmetric quasimetric learning for MAD — and provides solid empirical evidence across diverse environments. The residual issues (contradictory data description, underspecified evaluation protocol, unanalyzed secondary algorithm) are addressable and do not undermine the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>