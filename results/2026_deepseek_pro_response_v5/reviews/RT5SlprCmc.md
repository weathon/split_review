Now I have good calibration data. Let me finalize the review.

**Round 1 Bracket:** Based on comparing against the anchors, I initially bracketed this paper between ~4.75 and ~6.25.

**Round 2 Narrowing:** After reading qofh48zW3T (6.00), OjCWG58ZyY (5.50), and comparing against oEzY6fRUMH (4.75) and TOiageVNru (6.00) from Round 1, I position this paper as:

- Better than oEzY6fRUMH (4.75): clearer contributions, stronger results
- Roughly comparable to OjCWG58ZyY (5.50): both have real contributions undermined by specific experimental issues
- Below qofh48zW3T (6.00) and TOiageVNru (6.00): those papers have stronger theoretical grounding and cleaner validation
- Well below I7DeajDEx7 (6.75): stronger overall package

**Final Score: 5.0.** The quasimetric confound is a significant experimental design issue, but the paper has genuine strengths (scale-invariant loss, benchmark suite, strong planning results) and the issue is addressable.

Let me finalize the review now.

## Summary
This paper proposes two algorithms (MadDist and TDMadDist) for learning the Minimum Action Distance (MAD) from state-only trajectories in MDPs. The key innovations are: (1) a scale-invariant loss that normalizes prediction error by trajectory distance, (2) support for asymmetric quasimetric distance functions (including a novel simple ReLU-based quasimetric $d_{\text{simple}}$), and (3) a benchmark suite with known ground-truth MAD across diverse environments. The paper evaluates against QRL and a Hilbert embedding baseline, showing strong correlation, Ratio CV, and downstream planning results — particularly for MadDist, which achieves near-perfect success rates on OGBench PointMaze tasks.

## Strengths
- **Scale-invariant loss design (Equation 5):** MadDist normalizes prediction error by trajectory index difference $(j-i)$, preventing distant state pairs from dominating the loss. This directly addresses a weakness in Steccanella & Jonsson (2022)'s unscaled squared error. The empirical payoff is clear: MadDist achieves substantially lower Ratio CV than Hilbert across all environments in Figure 3 (e.g., ~0.15 vs ~0.35 on OGBench Giant Maze).
- **Asymmetric/quasimetric formulation with strong empirical evidence:** By supporting quasimetrics ($d_{\text{simple}}$, $d_{\text{WN}}$, $d_{\text{IQE}}$), the proposed methods capture directional structure that symmetric baselines cannot. Figure 3 demonstrates the consequence: in the highly asymmetric CliffWalking environment, the Hilbert baseline reaches only ~0.8 Pearson correlation while MadDist reaches ~0.9+, and the Ratio CV gap is even wider.
- **Downstream planning validation (Table 1):** MadDist achieves perfect (1.00 ± 0.00) success rates on 4 of 6 OGBench PointMaze planning environments, including the challenging Stitch settings that require composing information from disconnected trajectories. The gap is decisive: Hilbert scores 0.05–0.67, QRL 0.81–0.97. This closes the loop from representation quality to practical utility.
- **Comprehensive benchmark suite with known ground-truth MAD:** The paper constructs environments spanning discrete/continuous state spaces, deterministic/stochastic dynamics, noisy observations, and strongly asymmetric dynamics — enabling the first rigorous quantitative comparison of MAD approximation quality across diverse MDP structures.

## Weaknesses

### Fatal
None.

### Major
- **Unspecified quasimetric in main experiments creates a confound:** The main experimental section (Section 7, Figure 3, Table 1) never states which quasimetric MadDist and TDMadDist used. QRL is known to use IQE (Section 5, line 204). But whether MadDist used $d_{\text{simple}}$, $d_{\text{WN}}$, or IQE in the reported results is unspecified — the paper says only that these choices are explored in Appendix E (stripped). This confounds attribution: if MadDist used $d_{\text{simple}}$ and QRL used IQE, MadDist's advantage could come from the quasimetric rather than the learning algorithm, or vice versa. The paper needs to disentangle the quasimetric choice from the algorithm comparison to cleanly validate either contribution.

### Minor
- **TDMadDist underperforms without adequate analysis:** Figure 3 shows TDMadDist underperforming MadDist across all three environments, and in two of three it trails QRL as well. Table 1 shows it winning on only 1 of 6 PointMaze environments. The paper acknowledges this with one sentence ("While TDMadDist underperforms the MadDist and QRL algorithm...") but offers no analysis of why TD bootstrapping fails here. Given that TDMadDist is presented as a co-equal algorithmic contribution, the paper should either analyze the failure modes or reframe it as a negative result.
- **No absolute error metric reported:** The evaluation uses Pearson/Spearman correlation and Ratio CV, all of which measure relative ordering or scaling consistency. A method that systematically predicts $d_{\text{MAD}} \times c$ for all pairs would score perfectly on these metrics while being potentially less useful for reward shaping. The downstream planning results (Table 1) partially address this, but reporting an absolute metric like MAE or RMSE would strengthen the claim that learned distances are directly usable for reward shaping and goal-conditioned RL.
- **Contrastive loss (Equation 6) lacks justification:** $\mathcal{L}_r$ penalizes random state pairs whose predicted distance falls below $d_{\max}$. But in any connected environment, some randomly sampled pairs are genuinely close in MAD. The paper does not discuss how $d_{\max}$ is chosen or whether this term could harm performance for genuinely close random pairs. An ablation showing MadDist with and without $\mathcal{L}_r$ would clarify whether this term is necessary.

### Trivial
- **Discrepancy in reported number of seeds:** Line 220 states "means over five independent runs" while the Figure 3 caption (line 232) says "minimum and maximum values across three random seeds." This should be reconciled.
- **Equation 9 (line 171) is garbled by the PDF parser:** The TD loss $\mathcal{L}'_r$ is corrupted in the extracted version. This is a parser artifact, not an author error, but worth noting.

## Nice-to-Haves
- Bringing NoisyGridWorld results into the main body would directly address the stated research question about robustness to observation noise (line 194).
- A full factorial experiment (MadDist × {d_simple, IQE, d_WN} vs. QRL) in the main body would cleanly separate algorithmic and quasimetric contributions.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Half the described environments don't appear in the main body's figures"** — NoisyGridWorld, UMaze, and MediumMaze results are in Appendix F of the original paper; the parser stripped appendices. This is not an author error.
- **"The paper should discuss the relationship between the behavior policy and MAD estimates"** — The paper explicitly uses random policies for data collection (line 220) and MAD is defined independently of policy (Section 4). This criticism is largely orthogonal to the paper's stated contribution.
- **"Specific hyperparameter values never stated"** — These are in Appendix D, which was stripped by the parser.
- **Generic criticism about compute time / larger datasets** — Not relevant to the paper's contributions.
- **Strength about TDMadDist being "a principled contribution"** — Conflicts with the verified weakness that it underperforms without analysis. Removed as a standalone strength.
- **Generic strength about "clear positioning against related work"** — This is too generic to list as a specific strength, though the related work section is competent.

## Novel Insights
The paper's core insight — that asymmetric quasimetric distances can be learned from trajectory data using a scale-invariant loss — is a sensible incremental improvement over Steccanella & Jonsson (2022) and Wang et al. (2023b). The most genuinely novel observation is the empirical finding that a trivially simple ReLU-based quasimetric ($d_{\text{simple}}$) can match or outperform the more elaborate IQE construction in practice, though this claim currently resides only in the stripped appendix and the main results do not disentangle quasimetric choice from algorithm choice.

## Suggestions
- Specify in the main text which quasimetric was used for the MadDist and TDMadDist results in Figure 3 and Table 1. If different quasimetrics were used across environments, state this explicitly.
- Either drop TDMadDist as a primary contribution or add a diagnostic analysis explaining why bootstrapping degrades performance relative to direct regression.
- Add an absolute error metric (e.g., MAE normalized by true distance) alongside correlation and Ratio CV.
- Resolve the "five runs" vs. "three seeds" discrepancy.
- Consider moving one key NoisyGridWorld result into the main body to address the noise-robustness question directly.

**Anchor comparison summary:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| oEzY6fRUMH (State Chrono Representation) | 4.75 | R1 | Our paper has cleaner formulation and stronger results |
| OjCWG58ZyY (Goal-Conditioned RL with Virtual Experiences) | 5.50 | R2 | Similar quality; both have real contributions undermined by specific issues |
| qofh48zW3T (Distributional Distance Classifiers) | 6.00 | R2 | Stronger theoretical grounding; our paper has more significant experimental confound |
| TOiageVNru (Physics-informed TD Metric Learning) | 6.00 | R1/R2 | Similar structure; our paper's quasimetric confound is more problematic |
| I7DeajDEx7 (Episodic Novelty Through Temporal Distance) | 6.75 | R1 | Clearer presentation, better theoretical depth; our paper is clearly weaker |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>