Now let me do calibration searches.Round 1 bracket: 5-7. Let me narrow.## Summary
The paper proposes Agentic Reinforced Policy Optimization (ARPO), an agentic RL algorithm for multi-turn LLM tool-use agents. ARPO has two pillars: (i) an entropy-based adaptive rollout that branches additional partial samples after a tool call when post-feedback token entropy rises above a threshold, and (ii) an "advantage attribution estimation" with hard/soft variants for credit-assigning the shared prefix vs. branched suffix tokens. Across 13 benchmarks (math, knowledge QA, deep search) on Llama3.1-8B / Qwen2.5-7B / Qwen3-8B/14B, ARPO outperforms GRPO, DAPO, and REINFORCE++, and reportedly does so with roughly half the tool-call budget.

## Strengths
- **Broad empirical evaluation with consistent gains across two backbone families and three domains.** Tables 1–2 show ARPO outperforms GRPO/DAPO/REINFORCE++ on Llama3.1-8B (55.3 vs. 51.1 avg) and Qwen2.5-7B (58.3 vs. 56.5 avg), and the deep-search numbers on Qwen3-14B are striking: 43.7% on GAIA (vs. 36.9 for GRPO) and 36.0% on WebWalkerQA (vs. 30.0), with only 1k RL samples.
- **Tool-call efficiency curve in Figure 7a is a concrete, practical result.** ARPO sits in the 250–300 tool-calls/step band while GRPO sits at 400–450 during training, supporting the efficiency framing even if the per-problem accounting could be clearer.
- **The Pilot study in §2 is a genuine empirical observation that motivates the design.** The finding that the 10–50 tokens immediately following a tool-call response carry sharply elevated entropy — and that search feedback induces more uncertainty than Python feedback — is a useful and reproducible measurement on tool-use trajectories.
- **The hard-vs-soft advantage ablation (Figure 5) is informative**, showing the soft variant yields more stable training reward curves and motivating the default choice.

## Weaknesses

### Fatal
None.

### Major
- **The central claim — "entropy is the right branching signal" — is not isolated experimentally.** The entire motivation in §2 / Figure 2 is correlational (entropy spikes after tool calls), and §3.1 builds branching on that signal, but the paper never runs the obvious control: branching at random positions, at low-entropy positions, or unconditionally after every tool call, at matched branch budget. Without that, the gains in Tables 1–2 could be explained by "branched rollouts help" rather than "entropy-guided branching helps." This is the most important missing ablation given that the abstract, introduction, and §3.1 all rest on the entropy signal being load-bearing.
- **The "Soft Advantage Estimation" reduces to vanilla GRPO loss on branched trajectories.** §3.2 explicitly writes "we retain the original GRPO loss formulation" (line 154) and the argument in Eq. 4 is that GRPO's importance ratio already assigns identical weights to shared-prefix tokens — i.e., the deployed default is GRPO loss on a tree of prefix-sharing rollouts. The hard variant underperforms (Figure 5), so the "advantage attribution estimation" pillar is effectively a relabeling of an emergent property of GRPO when fed prefix-sharing trajectories, not a new estimator. The contribution would be more accurately framed as "we use GRPO loss on a tree of rollouts with shared prefixes."
- **The "half the tool-call budget" headline lacks accounting.** This claim appears in the abstract, intro, §5.2, and conclusion. Figure 7a reports "total calls per step" but never clarifies whether ARPO's global rollout size $M$ is held equal to GRPO's group size $G$, whether the count is summed over global + partial samples, or how branching is amortized per problem. ARPO's rollout structure — $N$ global samples plus up to $M-N$ branched continuations — should mechanically produce *more* per-problem tool calls than vanilla GRPO unless $M$ is reduced. Without spelling out the budget at the per-problem, per-step level, the most prominent quantitative claim in the paper is hard to interpret on its own.

### Minor
- **The "Generalized Policy Gradient Theorem" (§3.3, Eq. 6) does not actually justify ARPO's design choices.** It just applies the policy-gradient theorem at the macro-action level, which is true for any segmentation — random, fixed-length, tool-boundary, or entropy-based. It therefore does not provide theoretical support for the entropy-based branching schedule, the $P_t = \alpha + \beta\Delta H_t$ rule, or the hard-vs-soft choice. Calling it the "theoretical foundation" of ARPO overstates what is delivered; the theorem is true but not load-bearing.
- **Normalization of $\Delta H_t$ is under-specified.** §3.1 says $\Delta H_t = \text{Normalize}(H_t - H_{\text{initial}})$ is computed by "summing all the values of $\Delta H$ and dividing by the vocab size $V$" (line 118). Dividing by $V$ rather than by $k$ (the number of monitored tokens) makes $\Delta H_t$ vanishingly small for realistic $V$, which directly affects when the threshold $P_t > \tau$ fires. This should be clarified or, if a typo, corrected — the entire branching mechanism degenerates if $\tau$ is misaligned with the actual scale of $\Delta H_t$.
- **Some "consistently outperforms" framing is overstated.** On Qwen2.5-7B, ARPO trails GRPO on GSM8K (92.2 vs. 92.8) and HotpotQA (58.8 vs. 59.0), and ties on MATH. The overall average advantage is real, but "consistently outperforms across 10 datasets" (§5.1) does not match the table; "outperforms on average, with parity or small losses on a handful of saturated benchmarks" would be more accurate.
- **Sensitivity to $\tau$ and $Z$ is not surfaced in the main text.** The mechanism degenerates to vanilla GRPO if $\tau$ is too high and to fixed-depth tree search if too low; the reader cannot tell from the main paper how robust the reported gains are to this single knob.
- **The multi-tool bonus $r_M = 0.1$ in Eq. 5 is inherited from Tool-Star but not analyzed in the ARPO context.** A simple report of how often branches that preserve a joint-tool-use prefix earn the bonus would clarify whether ARPO's gains are partly mediated by inheriting the multi-tool prefix in branched samples rather than by entropy-targeted exploration per se.

### Trivial
- The §5.2 "rollout diversity" claim ("54 clusters vs. 48 for GRPO") rests on a single DBSCAN run with unspecified $\epsilon$/min_samples; reporting silhouette or Davies–Bouldin would make the qualitative claim of "tighter intra-cluster compactness" quantitative.
- The "pioneeringly" framing in §1 for the entropy analysis overclaims novelty given the cited entropy-based RL studies (Wang et al. 2025b;c; Cheng et al. 2025; Zheng et al. 2025b). "We apply entropy analysis to the tool-feedback boundary specifically" would be more accurate.

## Nice-to-Haves
- A controlled branch-signal ablation (random / periodic / always-after-tool-call / low-entropy / entropy-guided) at matched branch budget on at least one benchmark from each domain — this would directly test the central thesis of the paper.
- Variance across seeds for the main tables. The 4 pp average gain on reasoning is consistent but small, and the rebuttal would be much stronger with seed variance.
- Tool-call accounting per problem and per training step, with $M$ and $G$ matched and reported side-by-side.
- Sensitivity sweeps for $\tau$, $Z$, and $M$–$N$.
- A regime where hard advantage estimation wins (e.g., deeper trees, longer horizons), if one exists — that would recover the "estimation" contribution rather than leaving it as a relabeling of GRPO loss.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Multi-tool bonus could be reward-hacked on math benchmarks by inserting useless search calls / on knowledge benchmarks by inserting Python calls."* (Critic §5.2 note.) The bonus is inherited from Tool-Star and applies equally to all RL baselines in Table 1, so it cannot account for ARPO's relative gains. Kept only the milder interaction-with-branching version in Minor.
- *"Pioneeringly quantify" overclaiming novelty is partially addressed by the paper's own citations of prior entropy-based RL studies.* Demoted to Trivial above rather than treated as a Major framing issue.
- *Generic critique that the paper introduces "six hyperparameters without sensitivity analysis in the main text"* — partially mitigated by §A.2 ablations and the soft/hard ablation. Kept only the most consequential knob ($\tau$) in Minor.

## Novel Insights
None beyond the paper's own contributions. The empirical observation that the first 10–50 tokens after tool feedback carry sharply elevated entropy — and that this gap is wider for search than for Python — is a genuinely useful tool-use-specific finding worth highlighting, but it is part of the paper's stated contribution rather than a meta-insight from the reviews.

## Suggestions
- Run a branch-signal ablation at matched branch budget: random vs. always-after-tool vs. low-entropy vs. entropy-guided. This is the single highest-value experiment for the paper.
- Spell out tool-call accounting: define the budget per problem and per training step; match ARPO and GRPO at equal total tool calls and report performance, then match at equal performance and report tool calls. Currently the reader is invited to assume both directions hold simultaneously.
- Re-frame §3.2 honestly. State that the deployed algorithm uses GRPO loss on prefix-sharing branched trajectories, and that "advantage attribution estimation" is a rollout-structure contribution rather than an advantage-estimator contribution. Alternatively, find a regime where the hard estimator wins.
- Tie the theory in §3.3 to the design. A variance-reduction bound for entropy-targeted branching, or a regret argument for the $P_t = \alpha + \beta\Delta H_t$ schedule, would make Eq. 6 load-bearing instead of decorative.
- Fix the $\Delta H_t$ normalization description in §3.1, and report sensitivity to $\tau$ in the main text.
- Tone down "consistently outperforms" to match the table where ARPO ties or slightly trails on a few saturated benchmarks; the deep-search gains are the genuine headline.

## Axis Evaluation
- **Originality:** Moderate. The high-level pattern — branch sampling at uncertain points — is not new in RL more broadly, but applying it specifically to the post-tool-call boundary in agentic LLM training and tying it to a measured entropy spike is a useful and concrete framing.
- **Importance of the research question:** High. Credit assignment and exploration for multi-turn tool-using LLM agents is a timely and underexplored direction in RLVR.
- **Whether claims are well supported:** Mixed. The "ARPO outperforms trajectory-level RL" claim is supported broadly. The "entropy is the right branching signal" claim is asserted but not isolated. The "half the tool-call budget" claim is presented without tight accounting. The "advantage attribution estimation" framing is more aspirational than the deployed algorithm warrants.
- **Soundness of experiments:** Reasonable breadth (13 benchmarks, multiple backbones), but missing the key entropy-signal ablation and seed variance. The deep-search numbers (Qwen3-14B + ARPO at 43.7% GAIA, 10.0% HLE, 36.0% WebWalker, with 1k RL samples) are striking.
- **Clarity:** Mostly clear at the high level; weakest in §3.1 (normalization, hyperparameter definitions) and §5.2 (tool-call accounting).
- **Value to the community:** Real. The empirical results on deep search and the tool-call efficiency curve will be of interest to practitioners training tool-using agents, and the released code lowers the barrier to follow-up work.

## Score Calibration

Anchors retrieved:

- Round 1, weak band:
  - `E2CR6hmV1I.md` (avg 3.00, Reject) — Multi-agent process-reward paper; far weaker empirical breadth than ARPO and less coherent methodology.
  - `zEhTnQZB3D.md` (avg 2.33, Reject) — Continual RL with language tips; small scope and weak results.
  - `P0eEalHM5h.md` (avg 3.40, Reject) — LLM synergy / instruction-following; weaker empirics than ARPO.
  - `cb4etlGvOY.md` (avg 2.50, Reject) — Autonomous agents in-context paper; very small evaluation.
- Round 1, middle band:
  - `YCu7H0kFS3.md` (avg 4.75, Reject) — EAST, activation-steering for exploration; narrower empirical scope than ARPO.
  - `0G6rRLYcxm.md` (avg 5.00, Reject) — Maximum next-state entropy in classical RL; not LLM-agent specific.
  - `PfrpYGKGPL.md` (avg 5.50, Reject) — Entity-deduction arena; benchmark paper.
  - `YvKJGYL4j7.md` (avg 6.25, Accept) — Trajectory entropy maximization in MARL; theoretically cleaner than ARPO but classical RL only.
- Round 1, strong band:
  - `or8mMhmyRV.md` (avg 7.75, Accept) — MaestroMotif skill design; broader contribution than ARPO.
  - `xoXn62FzD0.md` (avg 8.00, Accept) — SMC for controlled LLM generation; more principled methodologically.
  - `9pW2J49flQ.md` (avg 8.00, Accept) — DeepLTL; clean theoretical contribution.
  - `OOxotBmGol.md` (avg 8.00, Accept) — LLAMBO; clear scope.
- Round 2 anchors (narrowing inside 5–7):
  - `fp6t3F669F.md` (avg 6.25, Accept) — AgentQuest benchmark; benchmark contribution rather than algorithmic.
  - `GBIUbwW9D8.md` (avg 5.75, Accept) — R-MCTS reflective tree search for VLM agents; very comparable in spirit — adds branching/search to an LLM agent and reviewers raised similar "simple twist on existing method" and "experimental controls unclear" critiques. ARPO has broader empirical scope (13 benchmarks vs. one).
  - `kpL66Mvd2a.md` (avg 5.50, Reject) — Tree search for LM agents; very topically similar, similar reviewer concerns about controls.
  - `zAdUB0aCTQ.md` (avg 6.20, Accept) — AgentBench; benchmark.
  - `aVfDrl7xDV.md` (avg 6.25, Accept) — Bayesian-OPRO; uncertainty-guided search at test time. ARPO has stronger headline numbers and broader empirical sweep, but more methodological wrinkles (soft = GRPO, theory not load-bearing).
  - `DpFeMH4l8Q.md` (avg 5.67, Accept) — Group preference optimization.
  - `rlgplAuN2p.md` (avg 6.80, Accept) — OCEAN offline CoT evaluation; cleaner methodology than ARPO.
  - `fWRBheSJth.md` (avg 6.67, Accept) — GReaTer prompt optimization; cleaner story than ARPO.

Round-1 bracket: 5.0–7.0. Round 2 narrowed it: the paper sits between R-MCTS (5.75, also a "simple twist + strong empirics" agent paper) and the cluster around 6.25–6.8 (BOPRO, AgentQuest, GReaTer, OCEAN), which have cleaner methodological framing but narrower empirical sweep. ARPO has stronger and more diverse empirical evidence than R-MCTS (13 benchmarks, two backbone families, plus the striking deep-search numbers), but is held back by (i) the missing branch-signal control, (ii) the soft = GRPO collapse, and (iii) the tool-call accounting gap. I place it just above the R-MCTS/BOPRO band and at or slightly below the 6.25–6.8 cluster.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>