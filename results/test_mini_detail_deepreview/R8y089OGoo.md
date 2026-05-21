Now let me write the final review after careful analysis.

## Summary

This paper proposes DIPOLE (Dichotomous Diffusion Policy Improvement), a novel RL algorithm for diffusion policy optimization. The key idea is to reformulate the KL-regularized RL objective using a "greedified" reference policy weighted by a bounded sigmoid function rather than an unbounded exponential. This yields a closed-form optimal policy that decomposes into two dichotomous policies — a positive policy (reward-maximizing) and a negative policy (reward-minimizing) — each trained with stable sigmoid-weighted losses. During inference, the policies are combined via a linear score combination that mirrors classifier-free guidance (CFG), offering controllable greediness through a hyperparameter ω. The method is evaluated on 39 tasks across ExORL and OGBench benchmarks (offline and offline-to-online settings) and on a 1-billion parameter vision-language-action model for autonomous driving on NAVSIM, demonstrating consistent improvement over strong baselines.

## Strengths

- **Bounded sigmoid weighting replaces unstable exponential weights, enabling stable diffusion policy training.** Section 3.1 identifies that the exponential weight exp(βG) in the standard KL-regularized objective (Eq. 3) causes loss explosion, and the proposed greedified objective (Eq. 5) replaces it with the bounded sigmoid σ(βG). Figure 1 illustrates this contrast. This directly addresses the stability–greediness trade-off that prior weighted-regression methods mitigate only via clipping or small β, which compromises optimality.

- **Dichotomous policy decomposition yields a theoretically grounded inference mechanism with a clear connection to classifier-free guidance.** Equations 7–10 show that the optimal policy can be expressed as a ratio of a positive policy π⁺ (reward-maximizing) and a negative policy π⁻ (reward-minimizing), each trained with bounded sigmoid weights. The score combination ε̃ = (1+ω)ε⁺ − ωε⁻ (Eq. 10) mirrors CFG, enabling flexible control of greediness via ω. This is a clear theoretical advance over CFGRL (Frans et al., 2025), which uses heuristic indicator-based weighting.

- **Comprehensive evaluation across 39 tasks on ExORL and OGBench, with strong performance in both offline and offline-to-online settings.** Tables 1–3 show that DIPOLE achieves best or near-best performance on most tasks. For example, on humanoidmaze-medium-navigate (Table 2), DIPOLE achieves 68 ± 3 versus 60 ± 14 for IFQL and 58 ± 5 for FQL. In offline-to-online (Table 3), DIPOLE improves from 61→97 on humanoidmaze-medium-navigate while IFQL reaches only 82 ± 20.

- **Scalability demonstrated on a billion-parameter VLA model for real-world autonomous driving.** Section 4.2 and Table 4 report that DIPOLE fine-tuning of a 1B-parameter DP-VLA model on NAVSIM achieves a PDMS improvement of 1.4 points on the navtrain split (88.3→89.7), substantially outperforming both the imitation baseline and the DPPO variant. This demonstrates the method works at a scale where prior diffusion-RL methods face computational or stability issues.

## Weaknesses

### Fatal
None.

### Major

- **The NAVSIM navtest result (94.8 PDMS, trained on the test split) is presented in the same main table alongside standard evaluations, which is potentially misleading.** The paper explicitly states that this variant is "trained on the test split without using any ground-truth" (line 232) and frames it as a realistic human-takeover scenario. However, the headline-grabbing 6.5-point improvement over the 88.3 baseline comes from training on the evaluation set. All other methods in Table 4 (UniAD, Transfuser, Hydra-MDP, etc.) are evaluated without test-set training. The paper would benefit from clearly separating this result (e.g., in its own section or with a bold visual divider) to prevent readers from conflating it with a standard evaluation. The relevant standard result is the navtrain improvement of 1.4 PDMS (88.3→89.7), which is solid but modest. The navtest result does not invalidate the method — DIPOLE also outperforms DPPO on the same navtest split (94.8 vs 89.0) — but the presentation inflates the apparent headline contribution.

### Minor

- **No ablation on the greediness factor ω.** The paper claims ω enables "flexible control over the level of greediness" and draws an analogy to CFG guidance scales, but never shows a controlled sweep (e.g., ω ∈ {0.5, 1.0, 2.0, 5.0}) on a representative task. Such an ablation would empirically validate the claim and help practitioners set this hyperparameter. (The paper does refer to Appendix D.4 for ablation studies, but these are not accessible in the provided text.)

- **No analysis of what the negative policy π⁻ actually learns.** The negative policy is trained to minimize return via (1−σ(βG)) weighting, but the paper offers no visualization or analysis of its learned behavior. Does it collapse to low-return modes? Does it serve primarily as a baseline in the CFG-style combination? A simple qualitative example would clarify the mechanism.

- **Missing direct comparison to gradient-based/policy-gradient diffusion RL methods (DDPO, DPPO, DRaFT, ReFL) on the ExORL or OGBench benchmarks.** The paper's introduction and related work motivate DIPOLE by critiquing these methods for instability and inefficiency (Section 1). DPPO is compared on NAVSIM (Table 4), but no comparison to any gradient-based diffusion RL method appears on the main RL benchmarks. While the included baselines (CFGRL, IFQL, FQL, IDQL) are the relevant offline diffusion-policy methods, comparing against the methods the paper claims to improve upon would strengthen the evidence. This gap weakens the cross-domain generalizability claim.

### Trivial

- The normalizing constant Z(s) in Eq. 5 and the constant C in Eq. 10 are mentioned but their role in the score combination is not fully explained — the claim that normalizing factors cancel in the gradient expression could be justified more explicitly.

## Nice-to-Haves

- Report wall-clock training time or parameter counts, since training two separate diffusion models (positive and negative) double the compute relative to a single policy. A brief comparison with DPPO or FQL would clarify practical trade-offs.
- Add a paragraph providing a first-principles justification for the greedified objective (Eq. 5), e.g., from a control-as-inference or variational perspective, to complement the current motivation by analogy to prior work.

## Removed Points

- **"The greedified objective is reverse-engineered and lacks principled design."** — REMOVED. The paper explicitly motivates the sigmoid as a bounded alternative to the exponential (Section 3.1), cites similar designs from Singh et al. (2022), Hong et al. (2023), and Xu et al. (2025), and shows it leads to a clean dichotomous decomposition. The derivation is well-motivated; calling it "reverse-engineered" is an opinion, not a verifiable flaw.
- **"Missing diffusion-RL comparisons are a fatal flaw."** — DEMOTED to Minor. The paper compares against 5–6 strong diffusion/flow baselines (CFGRL, IFQL, FQL, IDQL) on 39 tasks. DPPO is compared on NAVSIM. The absence of DDPO/DRaFT/ReFL on the RL benchmarks is a gap, not a fatal omission, especially since these methods operate in different settings (online RL, generative fine-tuning) from the paper's primarily offline evaluation.
- **"The navtest result invalidates the evaluation."** — DEMOTED from fatal to Major (see above). The paper is transparent about the navtest training, the navtrain result (89.7) independently validates the method, and DIPOLE outperforms DPPO on the same navtest split.

## Novel Insights

Beyond what the paper itself contributes, the reviewer inputs collectively surface one insight not foregrounded in the paper: the dichotomous decomposition can be viewed as a specific instantiation of **contrastive policy learning** — the positive policy learns "what to do" while the negative learns "what not to do" — and their CFG-style combination interpolates between these two extremes. This framing suggests that the method could be extended to incorporate additional contrastive signals (e.g., safety constraints, task specifications) by adding more policy terms to the linear score combination. The paper's current framing focuses on greediness control, but the contrastive interpretation opens a richer design space.

## Suggestions

1. **Restructure Table 4** to clearly separate the navtest result from standard evaluations — either through an explicit visual divider, a separate sub-table, or relegation to the appendix with a brief mention in the main text.
2. **Add an ω ablation** on at least one ExORL or OGBench task to demonstrate the effect of greediness control empirically.
3. **Include a brief analysis** (qualitative or quantitative) of the negative policy's learned behavior.
4. **Add wall-clock compute comparisons** to at least one baseline (e.g., DPPO or FQL) since the method trains two diffusion models.

## Score and Decision

**Calibration process:**

**Round 1 (bracketing):** Search for papers on "diffusion policy reinforcement learning offline RL" returned anchors:
- Low band (avg < 3.5): BDQL (3.67), Offline MARL with SSD (3.00), CFDG (3.00) — papers with serious methodological flaws or limited contributions.
- Mid band (3.5–7.5): Score Regularized (6.25), DAC (6.50), EFM (6.25), Value Function Diffusion (6.25) — papers with genuine contributions but clear limitations.
- High band (>7.5): Diffusion Planner (7.50) — strong empirical paper.

Initial bracket: **between 6.0 and 7.5**. The paper is clearly stronger than BDQL (3.67) and similar papers in the low band, with a novel algorithm and comprehensive evaluation. It may be stronger than the mid-band papers (DAC 6.5, EFM 6.25) due to greater novelty and evaluation breadth, but has presentation issues that prevent reaching the high band's top end.

**Round 2 (narrowing):** Targeted search for papers on "diffusion policy offline RL stable training" in (6.0, 8.0) and "dichotomous policy diffusion RL sigmoid weighting" in (4.5, 6.5) returned:
- DAC (6.50): Formulates KL-constrained policy iteration as diffusion noise regression. Strong method but Q-ensemble confounding and limited tasks. **DIPOLE compares favorably** — more novel decomposition, more comprehensive evaluation (39 tasks vs D4RL), and demonstrates scaling to 1B parameters.
- EFM (6.25): Energy-weighted flow matching. Some reviewers questioned novelty over existing weighted-regression methods. **DIPOLE is clearly stronger** — better motivated problem, more novel solution, more thorough evaluation.
- Diffusion Planner (7.50): Empirical study of design choices. **DIPOLE is comparable** — more theoretical novelty but the Planner has broader empirical scope (6,000+ models tested). Both are strong papers with different contribution types.

The round-2 comparisons show DIPOLE sits above the 6.25–6.5 papers and is comparable to the 7.5 anchor. The main limitation is the navtest presentation issue, which is real but does not undermine the core contribution.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>