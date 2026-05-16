Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces Allie, a chess AI trained exclusively on human game data (no self-play, no engine distillation) that jointly models moves, pondering time, and resignation behavior. The key technical innovation is a time-adaptive Monte-Carlo tree search (MCTS) procedure whose search budget is proportional to predicted human think time, enabling near-perfect skill calibration across opponents from 1100 to 2500 Elo. A large-scale online study (7,483 games against 2,412 humans) shows the adaptive search variant achieves a mean skill calibration error of only 49 Elo and performs at grandmaster level against 2500-rated opponents, substantially outperforming both search-free baselines and standard (non-adaptive) MCTS.

## Strengths

- **Time-adaptive MCTS achieves near-perfect skill calibration across the full human skill spectrum.** AllieAdaptiveSearch attains a mean SCE of only 49 Elo and a maximum of 95 Elo (Table 4). Against 2500 Elo opponents it performs at an estimated 2528 Elo, while every search-free baseline (AlliePolicy, AllieStrong, MaiaStar) falls below 2260 Elo. The near-linear relationship in Figure 5 is a compelling visual demonstration that directly supports the central claim.

- **State-of-the-art human move prediction.** AlliePolicy achieves 55.7% top-1 move-matching accuracy on the Lichess test set, outperforming MaiaStar (51.6%) and GPT-3.5 (53.7%) with 95% confidence intervals reported (Table 2). This advantage holds across nearly the entire skill spectrum (Figure 2), a core requirement for human-aligned play.

- **Holistic modeling of human behavior beyond moves.** Allie models pondering time (Pearson r = 0.697 with human think time, Figure 3) and resignation behavior (86.4% TPR, 0.1% FPR). No existing baseline models these behaviors, making this a genuinely novel capability that directly supports the paper's expanded definition of human-alignment.

- **Value function learned solely from human game outcomes correlates reliably with Stockfish evaluations** (Figure 4). This enables value-guided search (MCTS) without any self-play or oracle distillation — a cleanly supervised approach.

- **Large-scale online human study with robust empirical support**: 7,483 games against 2,412 human players spanning Elo 1000–2600 (Section 4.3). The breadth and size of this evaluation go well beyond typical offline metrics and provide direct evidence for the skill calibration claims.

## Weaknesses

### Fatal
None.

### Major
- **The Elo estimation method for the central SCE metric is not specified.** The paper defines SCE(B) = |SystemElo(B) − HumanElo(B)| (line 385) but never explains how SystemElo(B) is inferred from game outcomes. Elo is not directly observable from a win/draw/loss record — it requires a rating model (e.g., maximum likelihood under Bradley–Terry). The paper does not state the estimation algorithm, how draws are handled, or any prior/regularization used. The footnote on line 382 is empty. Since the headline result (mean SCE of 49 Elo) depends on this estimation procedure, the central quantitative claim cannot be verified or replicated from the paper as presented. **This does not invalidate the paper** — the qualitative pattern in Figure 5 is independently strong evidence — but it is a significant methodological transparency gap for the paper's strongest numerical result.

### Minor
- **MaiaStar online evaluation protocol is underspecified.** The paper deploys MaiaStar on Lichess (Section 4.3) but does not specify the move selection strategy (greedy decoding? sampling? temperature?), resignation handling, or any other playing protocol. For AlliePolicy the paper states "moves were sampled from the model distribution," and for AllieStrong "top moves are played," but MaiaStar's protocol is omitted entirely. While the paper's core controlled comparison is AllieSearch vs. AllieAdaptiveSearch (both using MCTS), the underspecification weakens the MaiaStar baseline comparison.

- **No confidence intervals or significance tests for SCE.** The paper reports 95% CIs for move-matching accuracy (Table 2) but not for the SCE numbers in Table 4. Given the large number of games (7,483), bootstrapped intervals or significance tests for the difference between AllieAdaptiveSearch (SCE 49) and AllieSearch (SCE 80) would substantially strengthen the headline quantitative claims.

- **Training hyperparameters are partially reported.** The paper states the model was trained for 2M steps with batch size 131,072 tokens (line 163) and mentions MCTS hyperparameters follow AlphaZero (line 133), but does not report learning rate, optimizer, scheduler, warmup steps, or weight decay. These matter for reproducibility, especially given the GPT-2 weight initialization.

### Trivial
None.

## Nice-to-Haves
- **Human-human agreement rate for move-matching.** The paper claims "human-aligned" behavior but does not calibrate the move-matching accuracy (55.7%) against how often two humans of similar skill agree on the same position. This would provide a natural upper bound and help contextualize the indistinguishability claim.
- **Ablation on adaptive search vs. random allocation.** The paper compares adaptive vs. non-adaptive MCTS at equal average rollouts, but does not test whether the benefit comes from allocating search to the *right* positions (as predicted by human time) or simply from allocating heterogeneous rollouts. An ablation with randomly distributed (non-time-aligned) rollout budgets would directly test the "humanlike reasoning" hypothesis.
- **Proper scoring rule for value prediction.** The paper uses MSE on {-1, 0, 1} outcomes, which is standard but could benefit from discussion of alternative proper scoring rules for ternary outcomes.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Claim that previous systems cannot model human-like behaviors beyond piece movement is overstated"** — Removed: The paper's claim is factually accurate. Maia models move prediction but not pondering time or resignation; GPT-3.5 was not designed for chess. The paper's framing is precise.
- **"Linear interpolation for soft tokens is not justified"** — Removed: The paper explicitly justifies the design choice (data sparsity, ordinal nature of Elo, lines 97–101). A regressor-style approach would amount to a different method, not a fix to a flaw.
- **"Unfair comparison to MaiaStar" (framed as a structural issue)** — Downgraded to Minor underspecification (above). The core controlled comparison is AllieSearch vs. AllieAdaptiveSearch (both use MCTS); MaiaStar is one of several baselines, and the paper is not claiming to beat it decisively. The real issue is transparency, not fairness.
- **MSE on {-1, 0, 1} could be improved with a proper scoring rule** — Moved to Nice-to-Haves. This is a standard practice, not a weakness.

## Novel Insights

The reviews surface a genuine tension at the heart of the paper: the headline quantitative result (49 Elo SCE) is underspecified, yet the visual evidence (Figure 5) and the controlled comparison against non-adaptive MCTS are strong enough to support the core claims even if the exact estimation method were clarified. This pattern — a paper whose strongest numerical claim is opaque but whose experimental design and qualitative evidence are solid — is common and the reviews handle it appropriately. The most insightful observation is that a human-human agreement baseline would meaningfully discipline the "indistinguishability" framing, shifting it from an aspirational definition to an empirically grounded claim.

## Suggestions

1. **Make the Elo estimation procedure fully explicit** — provide the formula, whether draws are handled, any prior/regularization, and the number of games per bin. Add bootstrapped 95% confidence intervals for SCE in Table 4.
2. **Specify MaiaStar's online playing protocol** — state whether it used greedy decoding, sampling, temperature, and any resignation logic.
3. Include a short table of training hyperparameters (learning rate, optimizer, scheduler, warmup) in the main paper.

## Score and Decision

This is a strong paper with a clear contribution: a novel approach to human-aligned chess AI that jointly models moves, pondering time, and resignation, and uses a clever time-adaptive MCTS to achieve state-of-the-art skill calibration. The large-scale human study is a significant empirical contribution. The weaknesses are real but addressable — the Elo estimation gap is the most important to fix, but it affects interpretability, not validity, of the core result. The paper's claims are well-supported by the controlled comparison between AllieSearch and AllieAdaptiveSearch and by the visual evidence in Figure 5.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>