## Summary

This paper applies the existing Goal-Oriented Environment Inference (GOEI) algorithm (Takahashi et al., 2024) to a two-player, five-card variant of the card game Hol's der Geier. GOEI is a Bayesian model-based RL method that learns a compact latent state representation by clustering observations according to their predictive value for final rewards. The authors train GOEI on 300,000 games of a random strategy versus Nash equilibrium (NE), then evaluate the resulting policy against the NE opponent. GOEI achieves a median reward rate of –0.010 (effectively the symmetric NE reward of 0.000) while using only 452 representational states — 2.9% of the 15,542 possible observations. Q-learning, used as a baseline, plateaus at –0.079. The paper frames this as a validation that GOEI successfully extracts core state representations in a more realistic setting than the abstract environment of the original work.

## Strengths

- **Impressive state compression with near-optimal performance**: The best GOEI configuration (β=0.2, α=25) uses only 452 states (S₁=5, S₂*=8, S₃*=31, S₄*=408) out of 15,542 possible observations — a 97.1% reduction — while achieving a median reward rate of –0.010 against the NE opponent, essentially at the symmetric NE reward of 0.000 (Table 1, Figure 2A). This is the paper's central result and is clearly presented.

- **Informative mutual-information analysis**: Figure 3 provides a feature-level breakdown of what information is retained vs. discarded by the reduced state representation. The analysis shows that current-table-card and remaining-table-card information are relatively preserved in early rounds, while score-difference information is preserved in the final round — a plausible and interpretable pattern that lends credibility to the learned abstraction.

- **Clean experimental separation of inference from policy optimization**: By training GOEI on fixed Rand-vs-NE games and testing the derived policy separately (Section 3.3), the evaluation isolates the quality of environment inference from the complications of interactive exploration. This is a sound experimental design choice for studying state reduction per se.

- **Hyperparameter sensitivity analysis**: Figure 4 systematically varies the Dirichlet process concentration α and Dirichlet pseudocount β across nine configurations, showing that performance is robust across a reasonable parameter range and that the expected trade-offs (smaller β accelerates learning, larger α avoids local minima) are empirically confirmed.

## Weaknesses

### Major

- **No model-based baseline to isolate state reduction**: The paper's central argument is that state reduction enables GOEI's success. The sole baseline is Q-learning, a model-free method. Attributing Q-learning's failure to the size of the observation space (line 294) confounds state-reduction benefits with model-free vs. model-based advantages. A model-based approach that learns a transition model over the full 15k+ observations and solves via dynamic programming is not attempted. Since the paper argues this is "practically difficult" (line 126), but provides no evidence (e.g., a memory or runtime estimate), the case that state reduction — rather than model-based planning — is the decisive factor remains unproven. This undermines the paper's core argument about GOEI's mechanism.

- **Narrow experimental scope limits the significance of the contribution**: The paper tests only a single opponent (NE strategy), in a single five-card game variant. The training data come from a single matchup (Rand vs. NE). The learned state representation is never tested against non-NE opponents, nor is the policy evaluated in a setting where the opponent changes. For a paper whose contribution is purely empirical validation, this scope is thin. The paper's own Discussion (Section 5) acknowledges that interactive online learning — where strategy changes affect inference — is not tested at all, which is the scenario the Introduction motivates.

### Minor

- **The sufficiency condition (Eq. 4) is never directly verified**: The paper formally defines the state reduction problem as finding a state set satisfying the predictive sufficiency condition in Eq. (4). The evaluation, however, measures only policy performance against a single opponent. A policy can perform near-optimally against NE while the state representation remains insufficient for arbitrary action sequences. While the paper defines success operationally as NE-level play (line 106-107), directly quantifying the prediction error of the reduced-state model against the true reward distribution for held-out action sequences would substantially strengthen the core claim. This is an evaluation gap, not a fatal error.

- **The introduction overpromises relative to what is demonstrated**: The Introduction motivates GOEI in terms of explainability and online adaptation. However, the experiments do not address interactive online learning (inference and strategy optimization are separated), and the authors acknowledge (line 350-351) that they "could not give a verbal explanation of the reduced state representation more concretely than Figure 3." The framing sets expectations the experiments do not fulfill.

### Trivial

- The computation of NE's "effective state number" (used as a dashed-line comparison in Figure 2B) is described ad-hoc (lines 200-207, 286-287) and would benefit from a clearer justification or connection to standard state-partition concepts.

## Nice-to-Haves

- Testing the learned state representation against opponents whose strategies differ from NE would gauge whether the core captures opponent-invariant task structure or is overfit to the training opponent.
- Including a model-based baseline over the full observation space (even at reduced scale or with approximations) would isolate the contribution of state reduction.
- Reporting a direct prediction-error metric for Eq. (4) on held-out action sequences would replace the current indirect argument from policy performance.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that "the comparison with Q-learning does not use the right baseline" — KEPT as a Major weakness** (reformulated above), since this is a valid concern grounded in the paper's experimental design.
- **Harsh Critic sub-point about "Q-learning learning curves for more epochs"**: This is a reasonable suggestion but too minor to include as a standalone weakness. Moved to Nice-to-Haves implicitly.
- **Harsh Critic point about "the optimal Bellman equation requiring a full model and reproducibility concern"**: The paper describes how GOEI builds the reduced-state model (Section 3.2, Eq. 5-9). The concern about next-observation prediction for planning is addressed by the model structure described — GOEI infers \(p(s_{t+1} | a_t, s_t)\) over reduced states, and planning uses this over the state space rather than the observation space. This is clear from Eqs. 5-9. Removed.
- **Harsh Critic comment about "the paper does not analyse why Q-learning fails"**: The paper's argument is that the observation space is too large (line 294). While one could wish for deeper analysis, this is a subjective preference, not a verifiable error. Removed.
- **Strength Finder's claim about "rigorous experimental separation... provides clean evidence that the state reduction itself — not the exploration policy — yields the near-optimal strategy"**: This slightly overclaims; the separation isolates environment inference from online exploration, but it does not isolate state reduction from model-based planning. The strength is retained but trimmed.
- **Strength Finder's claim about "GOEI successfully isolates a minimal core sufficient for optimal play"**: The word "sufficient" is imprecise without Eq. (4) verification. The retained strength is framed more carefully as "near-optimal performance with extreme compression."

## Novel Insights

None beyond the paper's own contributions. The key finding — that GOEI can compress observations to 2.9% while retaining near-NE performance on a card game — is the paper's contribution, but it does not reveal new algorithmic properties, failure modes, or theoretical insights about state-reduction methods beyond what was already demonstrated in the original GOEI paper on an abstract environment.

## Suggestions

- A model-based full-observation baseline (e.g., tabular transition model learned from the training data, solved via value iteration) would cleanly separate the contribution of state reduction from that of model-based planning. This is the single most important experiment to add.
- Evaluate the learned state representation against non-NE opponents (e.g., π₀, π₁, or the Rand strategy) to test whether the core captures opponent-invariant structure.
- Consider a direct test of Eq. (4): for a held-out set of (observation, action-sequence) pairs, compare the model's predicted reward distribution to the ground-truth distribution computed from the game rules. This would directly validate the core-sufficiency claim.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing)**:
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7ienVkNf83.md` (3.00, Reject): EReLELA — emergent language for state abstraction; weak results; our paper is stronger with cleaner results and more impressive compression.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rRRgj3iIHR.md` (3.00, Reject): AlphaDou — Doudizhu AI; fundamental issues; our paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XWfjugkXzN.md` (1.67, Reject): Sampling Information Sets; fundamental issues; our paper much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EHmjRIA4l2.md` (3.00, Reject): Compositional World Models; modest results; our paper's compression result is more striking.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7J0NsFXnFd.md` (5.25, Reject): RL-CFR — novel algorithm + strong poker results; our paper is clearly weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MTcgsz1SHr.md` (5.75, Accept): EVPA — novel pruning/abstraction + strong speedup; our paper is clearly weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nRgGCnw8eZ.md` (4.00, Reject): KrwEmd — novel algorithm, limited scope; comparable to our paper in contribution level.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/czpx02orl7.md` (4.75, Reject): Abstract World Models — theory + limited experiments; our paper is slightly weaker due to no novel method.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PbvbLyqT6.md` (8.00, Accept): DDCFR — novel framework + theory; our paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/stUKwWBuBm.md` (8.00, Accept): Tractable MARL; our paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9pW2J49flQ.md` (8.00, Accept): DeepLTL; our paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DzGe40glxs.md` (8.00, Accept): Interpreting Emergent Planning; our paper is much weaker.

**Round 2 (narrowing)**:
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oEzY6fRUMH.md` (4.75, Reject): State Chrono Representation — novel method, limited experiments, overlapping CIs. Our paper has no novel method but cleaner results and more striking compression. Comparable or slightly weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/x7Q0uFTH2a.md` (3.75, Reject): Weak Bisimulation — sparse reward issues; our paper is cleaner and more complete. Our paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/p5SurcLh24.md` (4.75, Reject): Unified MB/MF RL — novel algorithm but limited scope. Our paper is weaker (no novel algorithm).
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/chVYVLJIAh.md` (5.50, Reject): λ-AC — decision-aware RL study; stronger contribution with theoretical and empirical investigation. Our paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pCj2sLNoJq.md` (5.50, Accept): Generalist Hanabi Agent — card game, novel architecture, multiple settings, zero-shot coordination. Our paper is clearly weaker.

**Bracket**: This paper lands between 3.75 and 4.75. Round 2 anchors at 3.75 (x7Q0uFTH2a) and 4.75 (oEzY6fRUMH, p5SurcLh24) bound the range. The paper is stronger than the 3.75 anchor (cleaner results, better presentation) but weaker than the 4.75 anchors (both of which have novel methods, whereas this paper is purely a validation study). The closest comparison is KrwEmd at 4.00 — another paper with a modest algorithmic contribution and limited experimental scope, rejected. Our paper is similar in contribution level: no novel algorithm, narrow experiments, but clean results. I place it at **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>