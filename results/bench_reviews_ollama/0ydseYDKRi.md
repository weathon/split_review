## Summary
The paper introduces "Beyond the Rainbow" (BTR), an extension of Rainbow DQN integrating six modern components (Impala+maxpool, Spectral Normalization, IQN, Munchausen, Vectorization) to achieve an IQM of 7.4 on Atari-60 while training in under 12 hours on a desktop PC. The paper also reports Procgen results, demos training on three Wii games, and conducts ablations with mechanistic measurements (action gaps, policy churn, dormant neurons, SRank).

## Strengths
- **Strong compute/walltime operating point**: 200M Atari frames in <12h on a desktop with a 2.9M-parameter network is a meaningful and well-documented contribution (Fig. BTR_walltime, Table 2 comparing 0.9 vs 7.7 A100-GPU-days vs Dreamer-v3).
- **Substantial gain over Rainbow baseline**: IQM 7.4 vs Rainbow 2.7 vs DQN 0.9 (Fig. 1), with humans matched/exceeded on 52/60 games.
- **Procgen generalization**: BTR exceeds Rainbow+Impala (width x4) on all 16 Procgen environments using a smaller model and ~20% of the walltime (8h vs 41h).
- **Mechanistic component analysis**: Action gap, action swap, policy churn, dormant neuron, SRank, and noise-robustness measurements (Table 1, Fig. analy) go beyond standard ablations; the action gap evidence (0.276 vs 0.060 without Munchausen) is concrete and informative.
- **Reproducibility**: Source code in supplementary, full hyperparameters, and architectural details provided.

## Weaknesses

### Fatal
None.

### Major
- **Headline "SOTA on a desktop" excludes the most relevant compute-efficient peers.** BTR is benchmarked primarily against Dopamine's compact Rainbow and DQN. Other non-distributed, compute-efficient agents that occupy a similar operating point are not compared on Atari-60 under a matched protocol. The Related Work explicitly redefines SOTA as "excluding recurrent approaches" (and notes Dreamer-v3/MEME reach 9.6 vs BTR's 7.4). The framing therefore overstates the position of the work relative to its natural peer group.
- **Per-environment best-of-training evaluation inflates the headline IQM.** Footnote 2 states the IQM uses "the best single evaluation for each environment throughout training" rather than end-of-training. While the authors note this is common, it is not uniform across the literature, and the magnitude of the gap to Rainbow/Dreamer-v3 reported in Fig. 1 vs Table 2 (7.4 vs 9.6) depends on protocol consistency that is not demonstrated. The paper should report both final-window and best-of-training numbers for all compared agents.
- **Wii-games contribution is qualitative.** Section 4.2 advertises "three modern games solved" as a top-line contribution, but the evidence is screenshots and videos — no learning curves, no seed variance, no comparison to random/scripted baselines, no quantitative score distributions. As reported, this is a demo, not a result, and is too thin to substantiate "have never been solved using RL."

### Minor
- **Ablations rely on three seeds on Atari-5; mechanistic measurements (Table 1) are computed on a single game (Phoenix).** Causal claims like "Munchausen reduces policy churn by 5.6%" and "SN/maxpool aid noise robustness" rest on one game without confidence intervals or significance testing. Given that several non-Impala components show small final-performance effects (Fig. BTR_ablations) with shaded 1-σ bands, the seed variance likely overlaps the effect sizes. Replicating Table 1 on 3–5 games would substantially strengthen the analysis.
- **Munchausen-vs-Double dismissal is asserted, not tested.** "As Munchausen does not use argmax over the next state, Double DQN is obsolete" is plausible but not supported by an ablation comparing Munchausen alone vs Munchausen+Double.
- **Pareto framing for components that hurt final performance**: Vectorization and maxpooling are defended on walltime/robustness grounds. A clean Pareto plot (final score vs walltime/params/noise robustness) would make the "trade-off" argument rigorously rather than rhetorically.
- **Procgen baseline is narrow**: Only Rainbow+Impala is compared. Standard Procgen baselines beyond Rainbow would strengthen the result, though the comparison shown is informative on its own.
- **Hard exploration**: Montezuma's Revenge failure is acknowledged in the Conclusion but not quantified.

### Trivial
- "BTR appears to continue increasing performance beyond 200M frames" is asserted in §4.1 without a supporting extended-training curve.
- Mario Kart "consistently finishing in first place" lacks any reported run count, CPU difficulty, or seed.

## Nice-to-Haves
- A head-to-head matched-protocol comparison against the closest desktop-trainable, sample-efficient peers on Atari-60.
- Quantitative Wii-game results (multi-seed learning curves, lap-time/score distributions vs scripted/random baselines).
- Bootstrap CIs (e.g., rliable) on ablation IQMs.
- A per-component Pareto plot over (final score, walltime, params).
- Replicating the Phoenix-only Table 1 measurements on multiple games.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"Six-component choice is engineering, not science"** — meta-critique about design-space justification; the paper plainly describes why each was chosen and is consistent with the integration-style contribution Rainbow itself made.
- **"Walltime comparison without comparable hardware specs"** — the paper explicitly grounds walltime claims on a single specified desktop PC, which is the central operating-point claim. The asymmetry (BTR's hardware is weaker than the cited baselines') favors the baselines, so this is acceptable per asymmetric-comparison rules.
- **Strength: "Strong reproducibility stance"** — already covered by the kept reproducibility point; merged.
- Generic "important problem" framing from the Strength Finder — dropped as not specific.

## Novel Insights
None beyond the paper's own contributions. The most genuinely interesting analytical observation already in the paper is that Munchausen+IQN together drastically widen action gaps and reduce harmful action swaps, while Impala explains most of the performance gain via plasticity-related effects (lower dormancy, higher weight norm) — these are useful diagnostics but are the paper's own claims rather than reviewer-derived insights.

## Suggestions
- Report both end-of-training and best-of-training IQMs side by side; recompute baselines under matched protocols where feasible.
- Replace the Wii-games "contribution" claim with a "case study/demonstration" claim, or add multi-seed learning curves and a random/scripted baseline.
- Replicate the under-the-hood measurements (Table 1) on at least 3–5 games and add bootstrap CIs to ablation IQMs.
- Add a Pareto plot of (final score, walltime, parameter count) over the ablations to support the trade-off narrative.
- Add an ablation isolating Munchausen vs Munchausen+Double to substantiate the "Double is obsolete" claim.
- Quantify hard-exploration performance (e.g., Montezuma's Revenge score) rather than only acknowledging the failure.

---

**Axis assessment.** *Originality*: moderate — Rainbow-style integration rather than a new algorithmic idea, but the specific six-way combination, the walltime operating point, and the mechanistic measurement suite are novel together. *Importance*: high — accessibility of strong RL on a single desktop is a real and valuable problem. *Claim support*: mixed — the operating-point and Rainbow-improvement claims are well supported; the "SOTA on a desktop" framing and the Wii-games contribution claim are not. *Soundness*: adequate for the Atari/Procgen results, thin for the ablation mechanism claims (single-game, three seeds) and the Wii demos. *Clarity*: good; component-by-component exposition and clear tables. *Value*: a useful contribution to the practitioner/hobbyist segment of RL with a publicly released artifact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>