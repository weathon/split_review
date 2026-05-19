- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 8, 6, 6, 6
Now I have enough information to write the final consolidated review. Let me compose it.

## Summary
This paper presents Allie, a chess AI trained exclusively on human game data using a decoder-only Transformer with three output heads (policy, value, pondering time). The key contribution is a time-adaptive Monte-Carlo tree search (MCTS) that allocates search budget proportionally to the model's predicted human pondering time at each position. The system is evaluated through both offline metrics (human move prediction, rule learning, time/resignation modeling) and a large-scale online study (7,483 games across 2,412 players), with the headline result that AllieAdaptiveSearch achieves a mean skill calibration error of only 49 Elo across the 1100–2600 Elo spectrum.

## Strengths
- **State-of-the-art human move prediction accuracy**: Allie achieves 55.7% move-matching accuracy, outperforming MaiaStar (51.6%) and GPT-3.5 (53.7%) on the full Lichess test set (Table 2, confidence intervals ±0.1%). The advantage holds across almost the entire skill spectrum (Figure 3).
- **Holistic human behavior modeling beyond move prediction**: The model predicts pondering time with Pearson's r = 0.697 correlation to human times (Figure 4), achieves 86.4% true positive rate for resignations with only 0.1% false positive rate. No prior chess system models this combination of behaviors.
- **Near-perfect skill calibration via adaptive search**: In a large-scale online study, AllieAdaptiveSearch achieves mean SCE of 49 Elo and max SCE of 95 Elo (Table 3), a substantial improvement over AllieSearch (80/166), AlliePolicy (127/351), and MaiaStar (146/336). Against 2500-rated opponents it performs at 2528 Elo.
- **Learning chess rules from human data alone**: The model's top move is valid 100% of the time on human games and 99.9% on random games, with only 0.2% probability mass on invalid moves even in check (Table 1). This demonstrates genuine rule induction.
- **Soft control tokens for Elo conditioning**: The linear interpolation between weak and strong tokens (Section 3.1) addresses data sparsity while preserving scalar distances between ratings, a technically sound solution to strength-conditional generation.
- **Reliable value estimation from game outcomes**: Allie's learned value function correlates with game outcomes as well as Stockfish (an oracle) does, despite being trained solely on game outcomes without search supervision (Figure 5). This provides a foundation for value-guided MCTS.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **SCE estimation procedure is not fully specified**: The paper defines SCE(B) = |SystemElo(B) − HumanElo(B)| but does not describe how SystemElo(B) is computed from game outcomes (Section 5.3). While the performance rating formula used on Lichess is standard in the chess community and the relative comparisons across systems are meaningful regardless, the paper's most prominent quantitative claim would benefit from explicit disclosure (e.g., performance rating formula, whether a Bradley-Terry model, or MLE approach was used). This is a clarity gap in an otherwise well-specified empirical section.
- **No uncertainty quantification for SCE values**: Table 3 reports mean and max SCE without confidence intervals or error bars. Given that 7,483 games were collected across multiple Elo bins, bootstrapped intervals would allow readers to assess whether the gap between AllieAdaptiveSearch (49) and AllieSearch (80) is statistically significant.
- **The confound between positional complexity and clock pressure in pondering-time prediction**: The pondering-time head is trained on all blitz moves (the paper only excludes time-pressured moves from *evaluation*, not training; line 152: "omit from evaluation any moves made under time pressure"). In blitz games, short think times are often driven by clock pressure rather than position simplicity. While the aggregate result (adaptive search outperforms non-adaptive search) empirically validates the approach regardless of mechanism, the paper's interpretive claim that adaptive search enables "humanlike reasoning at critical positions" would be strengthened by analysis showing that positions with high predicted think time are indeed those where more search improves move quality.
- **Non-blind human study**: Players knew they were playing a bot (acknowledged in the Discussion, line 472). This is unlikely to affect game *outcomes* (and thus the main calibration claim), but it limits interpretation of the qualitative feedback and the ecological validity of the human-likeness claim. The paper already suggests a Turing test for future work.

### Trivial
- The joint loss function (Equation 1) sums cross-entropy, MSE for time, and MSE for value without mention of loss weighting. If these losses operate on different scales, training dynamics could be dominated by one head. The model clearly works, but the paper should confirm that all heads were trained effectively.
- The paper does not specify the number of games per Elo bin in the online study, which would help assess whether SCE estimates are reliable for extreme bins (e.g., 2500-rated opponents).

## Nice-to-Haves
- Show that positions with high predicted think time are those where additional search most improves move quality (e.g., by comparing win probability improvement from search against think time). This would directly validate the mechanism behind adaptive search.
- Include bootstrapped confidence intervals for the SCE values in Table 3.
- Run a small-scale blind Turing test (e.g., 100 games where opponents cannot distinguish bot from human) to strengthen ecological validity.
- Ablate the effect of GPT-2 initialization by training from scratch, to quantify the benefit of language model pretraining for chess modeling.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Criticism that the constant c was tuned to advantage**: The critic worried c might have been tuned to maximize calibration, giving AllieAdaptiveSearch an unfair advantage over AllieSearch. The paper specifies (Table 1) that c is "set such that MCTS performs 50 rollouts on average across all positions" — a calibration constant, not a performance-tuned hyperparameter. Both search variants use the same average compute, so no unfair advantage exists. **Removed as factually unsupported.**
- **Criticism about missing model architecture details**: The critic notes missing depth/width/heads. The paper states it uses GPT-2 medium (355M params), which is a well-known architecture with published specifications. Standard detail for a paper citing a known architecture. **Removed as nitpick.**
- **Criticism about missing related works**: Cannot be verified externally per instructions. **Removed per policy.**
- **Criticism about missing appendix content**: The parser stripped appendices. Per instructions, these exist in the original submission. **Removed per policy.**
- **Strength Finder point about "important problem"**: Generic; lacks concrete evidence specific to this paper's execution. **Removed.**
- **Harsh critic's generic "Section-by-Section Notes"**: These are mostly commentary, not structured weaknesses. The points about loss weighting and model architecture (addressed above) were the only concretely actionable items.

## Novel Insights
The reviews reveal two observations that are not fully articulated in the paper itself. First, the time-adaptive MCTS framework is notable for its *efficiency-first* design: by tying search budget to predicted human think time, the system automatically allocates compute proportionally to the complexity that humans perceive, achieving strong results without the massive overhead of constant high-rollout search. This is a principled answer to the practical question of how much search a human-aligned system needs. Second, the contrast between AllieSearch (standard MCTS, SCE 80) and AllieAdaptiveSearch (adaptive MCTS, SCE 49) — using the same *average* compute — suggests that the *distribution* of search matters more than the total budget. This has implications beyond chess: in any domain where a learned proxy for "difficulty" (here, pondering time) can guide inference-time compute, adaptive allocation may dominate uniform compute budgets.

## Suggestions
- **Specify the SystemElo estimation procedure in a short paragraph.** For example: "SystemElo is computed as the performance rating R_perf = R_avg + 400 · log10(S/(1−S)), where R_avg is the average opponent Elo in the bin and S is the system's score fraction (wins + 0.5·draws) / games." This small addition resolves the main reproducibility concern.
- **Add bootstrapped confidence intervals to Table 3.** Resample games within each Elo bin and recompute SCE to produce 95% CIs for the mean and max values.
- **Clarify whether time-pressured positions (<30s remaining) were excluded from training or only from evaluation.** If they were included in training, add an analysis controlling for clock time (e.g., early opening moves only) to show the pondering-time head captures positional complexity rather than time pressure.
- **Report the number of games per Elo bin** in the online study, alongside a brief acknowledgment of how sparse bins may affect SCE reliability.
