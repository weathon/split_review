Now I have all the calibration information I need. Let me write the final review.

## Summary

This paper proposes MadDist and TDMadDist, two algorithms for learning the Minimum Action Distance (MAD) from state trajectories alone, without requiring reward signals or action identities. The key technical contributions are: (1) a scale-invariant loss that normalizes squared prediction error by the trajectory step distance, preventing distant pairs from dominating the gradient; (2) integration of asymmetric quasimetric distance functions (including a simple novel one, $d_{\text{simple}}$) instead of the symmetric metrics used in prior work; and (3) a benchmark suite of environments with known or approximately known MAD values. The paper evaluates on discrete and continuous domains, reporting correlation metrics and downstream planning success rates.

## Strengths

1. **Scale-invariant loss (Eq. 5) that prevents distant pairs from dominating**: The MadDist loss normalizes the squared error by $(j-i)$, i.e., $((d_\theta(s_i,s_j)/(j-i) - 1)^2$, unlike the unnormalized formulation of Steccanella & Jonsson (2022). This is a well-motivated technical improvement whose empirical benefit is visible in Figure 3: MadDist consistently achieves the lowest Ratio CV across environments (e.g., ~0.15 in OGBench PM Giant Navigate vs. ~0.2 for QRL and ~0.5 for Hilbert), indicating more consistent scaling across distance ranges.

2. **Trajectory-level path-distance supervision enables global coherence**: Unlike QRL (Wang et al., 2023b), which only enforces locality constraints, MadDist directly supervises distances between all pairs of states on each trajectory using their known index difference. Table 1 shows this pays off in Stitch environments (which require composing information from disconnected trajectories): MadDist scores 0.99–1.00 vs. QRL's 0.74–0.95, exactly the setting where global coherence matters most.

3. **Principled separation of quasimetric from learning algorithm**: The paper cleanly decouples the choice of quasimetric ($d_{\text{simple}}$, $d_{\text{WN}}$, $d_{\text{IQE}}$) from the learning objective, making the framework modular. The proposed $d_{\text{simple}}$ satisfies the triangle inequality (proved in Appendix B) and is computationally efficient.

4. **Well-chosen evaluation environments with explicit asymmetry tests**: The benchmark includes environments where asymmetry in MAD is inherent (KeyDoorGridWorld, CliffWalking), and the results confirm that symmetric methods (Hilbert) cannot capture this, while asymmetric methods (MadDist, QRL) can. This provides clear evidence for the value of the quasimetric approach.

## Weaknesses

### Major

1. **Mismatch between "known ground truth" claims and the approximation used for continuous environments.** The abstract states the paper evaluates on "environments with known MAD values," and Section 7 (line 208) claims "perfect knowledge of the ground truth distances." However, for all PointMaze environments — which constitute 6/6 entries in Table 1 and 1/3 environments in Figure 3 — the "ground truth" is the all-pairs shortest path on a **discretized maze graph** computed via Floyd-Warshall (line 217). The paper acknowledges this is "to approximate the ground truth MAD" (line 217) but nowhere quantifies the gap between this discretized approximation and the true MAD of the force-actuated continuous system. The headline quantitative metrics (Pearson/Spearman correlations, Ratio CV) and the downstream planning evaluation (Table 1) all measure fit to this approximation, not to the true MAD. Whether the discretization error is negligible or significant, the paper provides no analysis. This overstatement is structural because the paper's central quantitative claims about the precision of MAD recovery are anchored on these continuous-domain results. The paper should either explicitly qualify all such claims or provide evidence that the discretization gap is negligible.

### Minor

2. **Inconsistent statistical reporting (3 vs. 5 seeds).** The "Empirical Setup" paragraph (line 220) states: "All reported results are means over five independent runs (random seeds)." Yet every caption and description of Figure 3 (lines 230, 232, 238, 240) says "Shaded regions indicate minimum and maximum values across three random seeds." These cannot both be correct as written. This concrete inconsistency must be resolved.

3. **No analysis of why TDMadDist underperforms.** The Discussion (line 226) notes that "TDMadDist underperforms the MadDist and QRL algorithm" but offers no explanation. The TD bootstrap should in principle allow information to propagate more efficiently along trajectories. Understanding why it fails — whether due to target network staleness, unreliable bootstrapped targets early in training, or something more fundamental — would strengthen the paper by informing which approach to build on.

4. **Ceiling effects in the downstream planning evaluation.** In Table 1, MadDist achieves a success rate of $1.00 \pm 0.00$ (zero variance across seeds) on 4 of 6 environments. This makes it difficult to interpret whether MadDist's advantage over QRL (e.g., $1.00$ vs. $0.97$ on PM Large Navigate) reflects genuine improvement or merely the evaluation's inability to discriminate above a threshold. The two environments without ceiling effects (PM Giant Navigate: $0.93 \pm 0.17$; PM Giant Stitch: $0.99 \pm 0.07$) are more informative, but the paper does not analyze why perfect performance occurs on some environments and not others.

5. **Claim that $d_{\text{simple}}$ "outperforms more elaborate quasimetrics" is listed as a main contribution but not supported in the main text.** The paper states (line 19) that $d_{\text{simple}}$ "outperforms more elaborate quasimetrics in the existing literature" with evidence deferred to Appendix E. For what is listed as one of three main contributions, even a brief summary table or key finding in the main body would help readers evaluate this claim.

6. **Garbled equation (Eq. 9) and notation inconsistency.** The TDMadDist $\mathcal{L}'_r$ loss term (line 171) contains a garbled expression (`- 12(9))`) with missing/extra parentheses, making the equation uninterpretable as presented (this may be a parser artifact, but it must be correct in the original submission). Separately, the state embedding is denoted $\phi_\theta$ in Section 4 (line 82) but $\phi_\phi$ in Section 6 (lines 127, 131) for the same quantity — a minor but unnecessary inconsistency.

### Trivial

None.

## Nice-to-Haves

- An analysis of how data coverage (100 or 1000 random-policy trajectories) affects accuracy for different distance ranges would help readers understand the method's sample efficiency.
- The quasimetric ablation results from Appendix E, if summarized briefly in the main text, would strengthen the $d_{\text{simple}}$ claim.

## Removed Points

The following points were removed from the inputs after verification against the paper:

- **"No actions" claim being misleading** (Harsh Critic): The paper says "requiring neither reward signals nor the actions executed by the agent." This is literally true — only state sequences are needed, not action identities. The concern about potential misreading is speculative and does not reflect an error in the paper. **REMOVED.**

- **Data coverage analysis** (Harsh Critic): Asking for detailed analysis of how random walks cover long-range distances is a reasonable suggestion but is a speculative concern, not a verified weakness of the paper's claims. **REMOVED** (moved to Nice-to-Haves).

- **Only 3 environments in Figure 3** (Harsh Critic): The paper states full results across all environments are in Appendix F, which is standard practice. The appendix is stripped by the parser; the paper cannot be penalized for its absence. **REMOVED.**

- **Ratio CV limitation** (Harsh Critic): The claim that Ratio CV "can be low even when predictions are systematically wrong" is a general property of the metric that the paper acknowledges by using it alongside Pearson and Spearman. Not a specific weakness of this paper. **REMOVED.**

- **Hilbert baseline as "staged comparison"** (Harsh Critic): The paper clearly explains why Hilbert is included (to demonstrate the value of asymmetry), and the critic acknowledges the relevant contest is between MadDist and QRL. Including a weaker method from a different paradigm as a lower bound is standard practice. **REMOVED.**

- **NoisyGridWorld results missing from main text** (Harsh Critic): Results are stated to be in Appendix F, which is parser-stripped. Cannot verify as missing. **REMOVED.**

- **Strength Finder's generic/superficial strengths**: Various generic statements about the paper addressing an important problem were removed as they conflict with verified weaknesses or lack specific grounding. Only concrete, evidenced strengths were retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Resolve the 3-seed vs. 5-seed inconsistency and clearly state which applies to which results.
- Add brief analysis quantifying the discretization gap between Floyd-Warshall shortest paths on the maze graph and the true MAD in continuous PointMaze, or at minimum qualify all claims about "known ground truth" when referring to these environments.
- Include a summary of the quasimetric ablation ($d_{\text{simple}}$ vs. $d_{\text{WN}}$ vs. $d_{\text{IQE}}$) in the main text.
- Provide even a short qualitative discussion of why TDMadDist underperforms — this would improve the paper's contribution by informing future work.

## Score and Decision

**Calibration anchors considered (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| FjifPJV2Ol.md (Solving Schrodinger Bridge) | 3.40 | R1 (low) | The current paper is substantially stronger — cleaner formulation, better evaluation |
| NRRHkJE03w.md (Conservation Principles) | 3.00 | R1 (low) | Same as above |
| 5AbtYdHlr3.md (Stochastic Safe Action) | 3.00 | R1 (low) | Same as above |
| x7Q0uFTH2a.md (Weak Bisimulation) | 3.75 | R2 (mid-low) | Current paper is clearly stronger — more coherent method, better evaluation |
| oEzY6fRUMH.md (State Chrono Repr.) | 4.75 | R1+R2 (mid) | Current paper is stronger — cleaner formulation, less ad-hoc losses |
| WQ6rnDriHj.md (Unifying Diverse Decision) | 4.75 | R2 (mid) | Current paper is stronger — better-motivated, more technically precise |
| 9SwObx9Jdn.md (Geodesics with Actor-Critic) | 4.75 | R2 (mid) | Current paper is stronger — broader evaluation, clearer contribution |
| qofh48zW3T.md (Distributional Distance Classifiers) | 6.00 | R1 (mid) | Comparable but current paper is slightly weaker — less theoretical insight, evaluation has overstatement issues |
| I7DeajDEx7.md (Episodic Novelty Through Temp. Dist.) | 6.75 | R1 (mid-high) | Current paper is weaker — less experimental depth, more evaluation concerns |

**Round 1 bracket**: [4.5, 6.0] — The paper is clearly above the 3.0–4.0 range but below the strong acceptance papers (6.75+).

**Round 2 narrowing**: Comparison with anchors at 4.75 and 6.00 confirms the paper sits between these clusters. It is stronger than the 4.75 papers (cleaner formulation, better-motivated, more principled evaluation) but weaker than the 6.00 anchor (more incremental contribution, ground truth overstatement issue, seed inconsistency).

**Final score**: 5.5 — A technically sound paper with a well-motivated contribution and clean formulation, but held back by evaluation overclaims (ground truth approximation treated as exact), a concrete reporting inconsistency, and ceiling effects that prevent strong quantitative differentiation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>