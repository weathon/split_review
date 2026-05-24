Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transitions to iteratively refine intermediate states toward higher reward. The method is evaluated across two language backbones (MDLM, LLaDA-8B) and one image backbone (MaskGIT) with four text reward functions and one image reward function, consistently outperforming existing inference-time guidance methods (BoN, FK, SVDD, SoP) — often by substantial margins (up to 8× faster scaling).

## Strengths

- **Consistent and large-margin empirical superiority across modalities.** IterRef outperforms all baselines on every combination of backbone and reward function. Notably, on MDLM with Toxicity, IterRef at 4T NFEs matches FK at 32T NFEs (8× advantage), and on Sentiment/CoLA/Perplexity, IterRef at 2T NFEs exceeds all baselines at 32T NFEs. These results are documented in Figure 2 and Table 1, and hold across both text and image domains.

- **Principled algorithmic design with practical efficiency.** The choice of balancing function (Eq. 2) reduces the importance weights to uniform sampling and the acceptance ratio to a simple reward-difference comparison \(\beta=\min(1,\exp((r(x_t')-r(x_t))/\alpha))\). This eliminates the need for auxiliary proposal regeneration and pool resampling, cutting per-iteration cost by nearly half (§3.3). The method also reuses rejection pools, further reducing overhead.

- **Novel insight into discrete diffusion dynamics.** Table 2 reveals that later denoising stages (0.1T) are more impactful than early stages for refinement, and that evenly-spaced application across steps works best on most metrics. This contrasts with known continuous-diffusion behavior (where early steps dominate) and provides actionable guidance for practitioners.

- **Demonstrated value in a safety-critical application.** The detoxification case study on LLaDA-8B (Figure 5) shows IterRef reducing toxicity below 10% starting from a 4× compute budget, with a consistent ~10% gap over baselines — validating practical relevance for alignment.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed theoretical guarantee.** The abstract states "proving convergence to the reward-aligned distribution" and the introduction claims "a theoretical guarantee that iterative refinement sampling converges to the target distribution" (§1). What is actually proven in Proposition 1 is that the MTM chain *at a single fixed timestep t* converges to \(p^*(x_t)\) *under the assumption* that the forward–backward kernel \((q, p_\theta)\) is reversible. The paper never discusses whether this reversibility condition holds for practical absorbing-state discrete diffusion models, nor does it clarify that the full multi-step sampling procedure does *not* inherit this guarantee. The contributions list (bullet 3) does include "under certain assumptions" as a qualifier, but the abstract and introduction present the result much more categorically. This mismatch between the presented and actual theoretical substance is a significant weakness. The empirical method may still be sound, but the paper claims much stronger theoretical support than it provides.

2. **No uncertainty quantification in language experiments.** All language results (Figure 2, Tables 2–3) report only mean scores over 15 prompts × 20 samples, with no confidence intervals, standard deviations, or significance tests. Given the small prompt set, the observed improvements could be driven by a handful of favorable cases. The paper makes strong comparative claims ("consistently outperforms," "8× faster") that would be far more convincing with error bars. This is a standard expectation for empirical papers making comparative claims, and its absence undermines the evidential weight of the results.

### Minor

3. **Missing hyperparameter reporting for \(\alpha\).** The temperature parameter \(\alpha\) controls the KL regularization strength and appears in all core equations (target distribution, acceptance ratio, intermediate reward). The main text never reports the value(s) of \(\alpha\) used in experiments or studies its sensitivity. (Hyperparameters are listed as \(\alpha, N, k\) in Algorithm 2 input, with no values given.) This omission makes reproduction harder and leaves open the question of how sensitive the results are to this key knob.

4. **No ablation of the Metropolis acceptance step.** The method uses the Metropolis correction \(\beta\) for acceptance. A natural baseline is to always accept the highest-reward proposal (greedy refinement). Without this comparison, it is unclear whether the detailed-balance correction provides empirical benefit or whether the gains come primarily from the noising-denoising proposals themselves. Adding this ablation would strengthen the paper.

5. **No analysis of intermediate reward approximation error.** The method approximates \(r(x_t)\) by \(r(\hat{x}_0)\) where \(\hat{x}_0\) is the model's one-step prediction. This proxy is used throughout (as the paper notes, following prior work). However, no analysis is given for how error in this proxy propagates — especially at high noise levels where predictions are unreliable. The paper should at minimum acknowledge this limitation.

6. **Effective timestep analysis conflates step selection with compute allocation.** Table 2 compares applying IterRef at a single timestep (all 4T NFEs concentrated there) with the "Evenly" condition (same budget spread across all steps). This conflates *which timesteps* are refined with *how many refinement passes* each step receives. A cleaner experiment would hold the number of refinement passes constant while varying the timestep selection. The current design still answers a practically useful question, but the interpretation is confounded.

### Trivial

7. The notation "T" in "2T NFEs" is not defined in figure captions; readers must infer from the implementation details that T = number of base denoising steps (e.g., 1000 for MDLM). Clarifying this in captions would help.

## Nice-to-Haves

- Including DSearch and DTS (discussed in Related Work) as baselines would strengthen the comparison, though the paper explains they follow a fundamentally different paradigm (search over trajectories vs. in-situ refinement).
- A sensitivity study for \(\alpha\) would help users calibrate the method for new tasks.
- Reporting wall-clock time alongside NFEs (the paper mentions this is in Appendix C.4, which is stripped) would give a more practical view of efficiency.

## Removed Points

- **Criticism about DSearch/DTS not being included as baselines**: These search-over-trajectory methods are structurally different from the inference-time guidance approaches compared in the paper. The paper notes this distinction in Related Work. Their absence is a limitation but not a flaw, demoted to Nice-to-Have.
- **Criticism about the "Evenly" timestep experiment being fundamentally "confounded"**: The experiment is designed to answer a practical resource-allocation question (where to spend compute). The conflation is inherent to that practical question, not an experimental flaw. Demoted to Minor (point 6 above).
- **Figure legend garbled in detoxification results**: The figure caption shows unexplained abbreviations ("SLP", "SR", "SVTOD") that likely correspond to baselines (BoN, SVDD, FK, SoP) — this appears to be a parser/formatting artifact, not an author error.
- **Criticism about theoretical guarantee being "unsupported"**: The paper *does* state the reversibility assumption in Proposition 1 and qualifies "under certain assumptions" in the contributions. The core issue is overclaiming in the abstract/intro, which is kept as Major point 1.
- **Strength Finder's claim about "theoretical guarantee" as a core strength**: Demoted — the guarantee is conditional on an unchecked assumption and only covers a fixed timestep, not the full procedure. The remaining strengths (empirical, design insight, safety application) are kept.
- **Strength Finder's generic praise about "important problem"**: Removed — the problem framing is not a strength specific to this paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The key insights (later-stage refinement is more effective in discrete diffusion than in continuous diffusion; increasing iterations \(k\) matters more than increasing particles \(N\)) are already presented and discussed by the authors.

## Suggestions

1. Tone down the theoretical claim in the abstract and introduction. Replace "proving convergence to the reward-aligned distribution" with a precise statement: the MTM chain at a fixed timestep converges under an explicit reversibility assumption, and this assumption may not hold for learned denoisers. Add a discussion of when reversibility is or is not satisfied.
2. Add confidence intervals, standard deviations, or per-prompt boxplots to all language experiments. The systematic nature of the gains partially mitigates this concern, but formal uncertainty quantification is needed for the strong comparative claims.
3. Report the values of \(\alpha\) used and add a brief sensitivity analysis.
4. Add an ablation comparing IterRef with a greedy variant (always accept the highest-reward proposal) to isolate the effect of the Metropolis correction.
5. Acknowledge the intermediate reward approximation as a limitation and, if possible, analyze how error at high noise levels affects results.

## Score and Decision

### Calibration Evidence

**Round 1 — Bracketing (initial search to identify score range):** The paper was compared against anchors in three bands. Weak anchors (avg score ~3.0, rejected, diffusion acceleration papers) were clearly below this paper. Middle anchors (avg 4.67–7.00) included the most topically similar papers. Strong anchors (avg 8.0+, accepted, on diffusion conditioning/guidance) represent a higher tier of theoretical depth or evaluation rigor. The initial bracket was **5.0–6.5**.

**Round 2 — Narrowing:** Retrieved anchors from within (4.5–7.5):

- **Ombm8S40zN** (avg 6.25, Accepted) — "Steering Masked Discrete Diffusion Models via DDPP." Both tackle reward-guided discrete diffusion. DDPP uses fine-tuning, IterRef uses inference-time MCMC. DDPP had weaker empirical breadth but stronger theoretical framing. IterRef has a slight empirical edge but similar-level presentation issues. **Comparable.**
- **peNgxpbdxB** (avg 6.00, Accepted) — "Scalable Discrete Diffusion Samplers." About training discrete diffusion for sampling from unnormalized distributions. Narrower scope. **Slightly weaker anchor.**
- **XsgHl54yO7** (avg 6.50, Accepted) — "Unlocking Guidance for Discrete State-Space Diffusion and Flow Models." About guidance in discrete state-spaces. Comparable topic, accepted with strengths in generality and weaknesses in theoretical depth. **Slightly stronger anchor.**
- **MBDH5zyxHM** (avg 4.60, Rejected) — "Controlled Denoising For Diffusion Models." Inference-time guidance via block-wise BoN. Weaker empirical results, more limited in scope. **Clearly below this paper.**
- **D7PQ54l5Q1** (avg 4.75, Rejected) — MCMC for diffusion inverse problems. Limited novelty, weak experiments. **Clearly below this paper.**

The round-2 anchors confirm the paper sits between the rejected papers at ~4.6–4.75 and the stronger accepted papers at ~6.5–7.0. Within this range, the paper is most comparable to the DDPP paper (6.25) in overall quality, with similar trade-offs between empirical breadth and theoretical/evaluation rigor.

**Final position:** The paper is slightly below the discrete guidance paper (6.50) which has cleaner theoretical framing, but above the rejected methods papers (4.6–4.75). The strong and consistent empirical results across multiple backbones/tasks are the main positive, while the overclaimed theory and missing uncertainty quantification are the main negatives.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**