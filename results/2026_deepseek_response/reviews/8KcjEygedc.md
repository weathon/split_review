## Summary

This paper develops a theoretical framework for understanding when "less is more" in data curation. It studies high-dimensional binary classification under label-agnostic and label-aware pruning oracles, deriving exact scaling laws for test error via random matrix theory. The central result (Theorem 2) proves a sharp phase transition: when the data generator is strong, keeping only hard examples is optimal; when the generator is weak, keeping easy examples is optimal. The theory is validated on synthetic data, connected to recent LLM reasoning results (LIMO, s1, Sun et al.), and tested on ImageNet classification and model collapse prevention.

## Strengths

- **Theorem 2 (Section 3.1) — optimal pruning phase transition**: The paper proves that when the generator is excellent (ρ→1) and the pruner is excellent (ρ₀→1), keep-hard uniquely minimizes error; when the generator is poor (ρ<1) with an excellent pruner, keep-easy is optimal. This is a crisp, non-trivial theoretical result that resolves the "less is more" vs. "more is more" paradox and gives practitioners a principled condition for deciding which strategy to use.

- **Theorem 1 — exact scaling laws via deformed Marchenko-Pastur law**: The paper derives closed-form asymptotic expressions for test error under general symmetric pruning functions, going beyond the empirical scaling curves of prior work (Sorscher et al. 2022) to provide a precise analytical characterization of how pruning affects generalization.

- **Theorem 3 — label-aware curation generalization**: The framework extends to label-aware pruning (Eqn 6), subsuming special cases studied in Feng et al. (2025) and Firdoussi et al. (2024), and is necessary for explaining methods like LIMO and s1 which combine correctness filtering with difficulty-based selection.

- **Clean synthetic validation (Figure 1)**: The four-regime simulation shows clear match between theory (solid lines) and simulation (dashed lines with error bars) across small/large n and strong/poor generator regimes, including the critical "less is more" optimum at p≪1 in the bottom-left quadrant.

- **ImageNet crossover demonstration (Figure 2)**: The paper shows that with a weak generator (160K examples) keep-easy outperforms keep-hard, while with a strong generator (1.2M examples) keep-hard becomes superior — directly confirming the theory's predicted phase transition on a realistic vision benchmark.

## Weaknesses

### Fatal
None.

### Major
1. **ImageNet experiments lack sufficient detail for reproducibility.** The main text (Section 4.3) states that "a pre-trained model" serves as both generator and pruner, but does not specify the model architecture, how margins (xᵢᵀwₒ) are computed from a deep network, the training procedure (optimizer, epochs, learning rate schedule), or how the pseudo-labeled dataset is generated and split. Without these details, the reader cannot assess whether the experiment's setup respects the theoretical assumptions or reproduce the results. This weakens the paper's claim to "empirically confirm our theoretical predictions on ImageNet" (line 27). The paper mentions Appendix B for "a comprehensive set of validations," but the main text should at minimum summarize the key experimental parameters.

2. **LLM reasoning connection is interpretive, not evidential (Section 4.2).** The paper presents data from LIMO, s1, and Sun et al. (2025) as empirical support for the theory, but no quantities are measured, no new experiments are run, and no falsifiable predictions are tested. The base LLM is treated as a generator with quality ρ that differs across question difficulty slices; this is a plausible post-hoc narrative rather than a validated model of these systems. While a theory paper can usefully offer explanations, the paper presents this (line 27: "provide a rigorous justification") as stronger evidence than it actually is. This overstates the evidential support.

### Minor
1. **The central test-error formula (Theorem 1) is presented schematically, with key functional forms deferred to the appendix.** The quantities m, m̃, and r are said to be "explicitly determined by the constants in Eqn (8)" but their actual relationship to the pruning parameters γ, β, β̃ is not shown in the main text. The reader cannot check even qualitative properties such as monotonicity or phase boundaries without the appendix. This is a presentation choice that reduces the paper's self-containedness, though it is standard for RMT-heavy work.

2. **Synthetic validation only compares keep-hard against random pruning, not against keep-easy, in the large-n strong-generator regime (bottom-left quadrant of Figure 1).** Including keep-easy would strengthen the demonstration that keep-hard is genuinely optimal, not merely better than random.

3. **Model collapse experiment (Figure 3) does not specify how "hard valid examples" are selected each round.** The description says "applying the 'keep hard' strategy at each step," but does not state the threshold α used, whether it is fixed or adapted, or whether the margins are computed from the current model or the original oracle.

### Trivial
None.

## Nice-to-Haves

- **Quantitative predictions on real-world experiments**: Even a simplified prediction (e.g., that the crossover point in Figure 2 should shift in a predicted way as a function of a measurable proxy for ρ) would significantly strengthen the practical claims.
- **Phase diagram in (ρ, p) space**: The paper claims phase transitions but only shows error vs. p for two n values. A phase diagram with theoretical boundary and simulated points would demonstrate precision.
- **Variance/error bars for ImageNet results** (Figure 2): The synthetic experiments have error bars; the ImageNet experiments do not.
- **A simpler closed-form special case in the main text** (e.g., no pruning, p=1) would give the reader concrete intuition for how the theory works.

## Removed Points

These points were flagged for removal; treat them with caution if referenced elsewhere:
- "The paper should note that pruning rules are defined relative to the oracle direction wₒ, not the true decision boundary" — The paper clearly states this in Section 2.2 (Eqn 5 and surrounding text: "based on its projection onto the oracle vector wₒ").
- "Formulas are entirely deferred to appendix, making the paper impossible to assess" — The paper states the theorem structure and key dependencies in the main text; appendix deferral is standard for RMT-based theoretical work. Downgraded to Minor.
- "Missing appendix content / references" — The parser strips appendix content from all submissions; this is not an author error.
- Criticisms about missing reproducibility details that are standard for the field (hyperparameters, large artifacts) — downgraded to Nice-to-Have where relevant.

## Novel Insights

None beyond the paper's own contributions. The phase transition result (Theorem 2) is the most novel element; the calibration and synthetic validation are cleanly executed but follow standard methodology for this line of work.

## Suggestions

1. **Add an experimental details subsection** (or significantly expand Section 4.3) specifying: the architecture used for ImageNet, how margins are extracted from the deep network, the training hyperparameters, and the pseudo-labeling protocol for the model collapse experiment.
2. **Reframe the LLM connection** as post-hoc explanatory insight rather than empirical validation of the theory, and add a sentence acknowledging that the theory has not been directly tested on these systems.
3. **Include keep-easy curves in the bottom-left quadrant** of Figure 1 to show that keep-hard is truly optimal, not just better than random.
4. **State the explicit test-error formula for the no-pruning (p=1) special case** in the main text to help readers build intuition.
5. **Add a phase diagram figure** (ρ vs. p with theoretical phase boundary and simulated markers) to sharpen the presentation of the phase transition claim.

## Score and Decision

**Calibration Report:**

*Round 1 (broad bracket):* 
- Weak band (0–3.5): EOPLy80bBm (avg 3.00), e2F0mJJeN0 (avg 3.00), 6PGT9OJX5N (avg 3.00), gInIbukM0R (avg 2.50) — all are heuristic/empirical pruning papers without theoretical contributions; the current paper is clearly stronger.
- Middle band (3.5–7.5): I9Dsq0cVo9 (avg 5.50, RMT analysis of synthetic data + pruning — closest topical match), Bk13Qfu8Ru (avg 7.00), 93XT0lKOct (avg 6.00), 9ccZzuix2D (avg 5.33).
- Strong band (7.5+): Tzh6xAJSll (avg 7.60, scaling laws for associative memories), pISLZG7ktL (avg 8.00), wg1PCg3CUP (avg 8.00), et5l9qPUhm (avg 8.00, strong model collapse).

*Round 2 (narrowing, 5.5–7.5):*
- GH2LYb9XV0 (avg 5.50, grokking in linear estimators — toy model with theory + synthetic validation, mixed connection to practice): The current paper has stronger conceptual novelty (phase transition) and broader scope. **Better.**
- O6znYvxC1U (avg 6.33, BNN spectrum analysis): Pure theory, less practical connection. **Comparable or better.**
- tNn6Hskmti (avg 6.25, two-layer NN analysis): Similar methodological depth. **Comparable.**
- nxnbPPVvOG (avg 5.67, linear estimation): Narrower scope. **Better.**
- VoI4d6uhdr (avg 7.00, bias amplification theory): Tighter empirical validation. **Slightly weaker.**
- wFD16gwpze (avg 7.33, neural scaling laws): Better empirical grounding. **Weaker.**

The paper sits between the 5.5–6.0 range: it has stronger conceptual novelty than GH2LYb9XV0 (5.50) and the closest topical anchor I9Dsq0cVo9 (5.50), but the ImageNet experimental details are too sparse and the LLM connection too interpretive to reach the 6.5+ range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>