Now I have all the information needed. Let me compose the final review.

## Summary

This paper introduces DIPOLE (Dichotomous Diffusion Policy Improvement), an RL algorithm for diffusion policy optimization. The key idea is a greedified KL-regularized objective whose optimal solution decomposes into two "dichotomous" policies — a positive policy (reward maximization) and a negative policy (reward minimization) — each trained with bounded sigmoid weights to avoid the exponential-weight explosion that plagues standard weighted regression approaches. During inference, the optimal policy's score is recovered as a linear combination of the dichotomous policy scores, controlled by a greediness factor ω, drawing a direct connection to classifier-free guidance. Experiments span 39 offline RL tasks (ExORL, OGBench), offline-to-online fine-tuning, and a large-scale autonomous driving evaluation on NAVSIM using a billion-parameter VLA model.

## Strengths

- **Stable and principled policy optimization via dichotomous decomposition.** The paper identifies a genuine problem with exponential-weighted regression for diffusion policies (weight explosion, training instability) and provides a clean theoretical fix: the greedified KL-regularized objective (Eq. 5) decomposes the optimal policy into two policies with bounded sigmoid weights (Eqs. 7–9). This is mathematically sound and directly addresses the optimality-stability trade-off illustrated in Figure 1.

- **Strong empirical performance across 39 RL tasks.** On ExORL (Table 1), DIPOLE outperforms all baselines across most domains, including strong methods like IQL, ReBRAC, CFGRL, IFQL, and FQL. On OGBench (Table 2), DIPOLE achieves best or near-best performance in 5 of 6 task categories, with particularly strong gains on cube-double-play (44±7 vs. FQL's 29±2) and humanoidmaze-medium-navigate (68±3 vs. 60±14 for IFQL). The offline-to-online results (Table 3) are compelling: e.g., humanoidmaze success rate jumps from 61%→97%, far exceeding IFQL (56%→82%) and FQL (12%→22%).

- **Scalability to large VLA models for autonomous driving.** DIPOLE successfully fine-tunes a billion-parameter vision-language-action model (DP-VLA) on NAVSIM, achieving a 1.4-point PDMS improvement on the standard navtrain split (88.3→89.7) and demonstrating that the method scales to real-world-sized models. This goes beyond the typical D4RL-scale evaluations common in the diffusion-based RL literature.

- **Novel theoretical connection to classifier-free guidance.** The derivation showing that the optimal policy's score function is a linear combination of dichotomous policy scores (Eq. 10), structurally identical to CFG, is insightful and provides a principled explanation for why the CFG-like inference-time combination works for policy improvement.

## Weaknesses

### Major

- **NAVSIM navtest evaluation is not a valid generalization test.** The paper trains DIPOLE on the navtest split and evaluates on the same split (Table 4, row "DP-VLA w/ DIPOLE navtest": 88.3→94.8 PDMS). While the paper labels this variant and frames it as a "human take-over" scenario, the headline 6.5-point gain is then used to claim "demonstrating its potential for real-world autonomous driving applications" without adequately acknowledging that the evaluation is circular — the model has been fine-tuned on the exact scenarios it is tested on. The valid navtrain evaluation (1.4-point gain, 88.3→89.7) is a more modest but cleaner result. The paper should clearly separate these two evaluations and avoid overclaiming from the navtest result. The navtrain result alone would still be a worthwhile contribution.

### Minor

- **No empirical demonstration of ω-based controllability in the main text.** The paper introduces ω as a key hyperparameter enabling "flexible control of the optimality level of generated actions" and draws an analogy to CFG, but does not provide any experiment showing how varying ω affects performance, safety, or action quality. The paper mentions ablations in Appendix D.4 (stripped by parser), but the main text's claim of controllable generation would benefit from even a simple plot of return vs. ω on one ExORL or OGBench task.

- **Contribution of dichotomous structure vs. rejection sampling is partially conflated for OGBench.** For ExORL, DIPOLE w/o rejection sampling is reported (Table 1), showing gains over CFGRL. However, for OGBench (Table 2), only the full DIPOLE is reported with no w/o-rs variant, making it harder to attribute the improvements specifically to the dichotomous training scheme vs. the inference-time rejection sampling. The ExORL w/o-rs results do support the core claim, but the OGBench omission is a gap.

- **Two tasks where DIPOLE underperforms compared to strong baselines are not discussed.** On humanoidmaze-large-navigate (Table 2), DIPOLE scores 6±2 vs. IFQL at 11±2. On antsoccer-arena-navigate, DIPOLE (57±7) is slightly below FQL (60±2). The paper's claim of "best or near-best" is accurate overall, but brief discussion of these cases would improve transparency.

- **Computational overhead of training two diffusion models is not mentioned.** The method trains separate positive and negative diffusion policies, effectively doubling parameters and training cost compared to single-policy methods like FQL. A brief note on this overhead would be appropriate.

### Trivial

- In Table 1, the Quadruped-walk result for DIPOLE has a large standard deviation (928±55), suggesting potentially high variance on that task, but this is not commented on.

## Nice-to-Haves

- An ω ablation study (e.g., return vs. ω for one ExORL or OGBench task) would directly substantiate the controllability claim.
- Statistical significance testing (e.g., paired t-tests or confidence intervals) for the main comparisons, since many results show overlapping standard deviations.
- Comparison with CFGRL on OGBench or NAVSIM, given the similarity in approach.
- Ablation varying β and ω jointly to understand their interplay.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Derivation feels ad hoc / reverse-engineered"** (Harsh Critic Section 3.2 note): This is a subjective opinion about presentation style, not a factual weakness. The mathematics is correct and the derivation is clean.

2. **"NAVSIM baseline already strong so RL gain is less impressive"** (Harsh Critic Section 4.2 note): This is a contextual observation, not a weakness. Improving an already strong baseline is a valid demonstration of the method's effectiveness, not a reason to discount it.

3. **"Missing comparison with CFGRL on OGBench/NAVSIM"** (Harsh Critic Section 5 note): Scope creep. The paper compares with CFGRL on ExORL (where it outperforms it), and the set of baselines on OGBench was already extensive.

4. **"Method improvement is marginal"** (implied by some of the critic's framing): The improvements on ExORL and OGBench are substantial and consistent across 39 tasks, contradicting this characterization.

## Novel Insights

The harsh critic's focus on the NAVSIM navtest issue is useful — it highlights a genuine methodological weakness that the paper glosses over. However, the critic overstates this into a "structural" fatal flaw, when in fact the paper is transparent about the setup and the navtrain result provides a valid, if more modest, demonstration. The deeper insight is that the paper's strongest contribution is the theoretical framework (dichotomous decomposition with bounded sigmoid weights) and the RL benchmark results, which are robust and well-executed. The NAVSIM experiment is best viewed as a promising proof-of-scale rather than a rigorous evaluation.

## Suggestions

1. **Reframe the NAVSIM results.** Clearly separate the navtrain result (valid evaluation, 1.4pt gain) from the navtest result (exploratory in-distribution fine-tuning, 6.5pt gain). Add a sentence acknowledging that the navtest evaluation is not a held-out generalization test. The navtrain result is sufficient to support the scalability claim.

2. **Add an ω ablation.** Even a single figure showing return vs. ω on one ExORL or OGBench task would substantially strengthen the controllability claim. This is the most impactful low-effort addition.

3. **Add DIPOLE w/o rs results for OGBench** (or at least note the ExORL w/o-rs results already address this concern). This would cleanly separate the contribution of the training scheme from the rejection sampling trick.

4. **Briefly discuss computational cost** (two models) and the cases where DIPOLE underperforms (humanoidmaze-large, antsoccer-arena) in the main text.

## Score and Decision

Now let me produce the final calibration analysis.

**Round 1 bracket (wide):** Based on the calibration search, the weak anchors (avg 3.0–3.33) are papers with fundamental flaws (incorrect proofs, no clear contribution). The middle anchors (avg 4.5–6.75) include several accepted papers with solid but imperfect contributions. The strong anchors (avg 7.6–8.0) are exceptional papers. DIPOLE clearly sits in the middle band — it has a sound theoretical contribution and strong empirical results, but has several issues (NAVSIM protocol, no ω ablation, some conflated evaluations).

**Round 2 narrowing:** Comparing DIPOLE to the most relevant anchors from the 6.0–7.0 range:
- **SRPO (6.25, accept)**: DIPOLE has a more novel theoretical contribution and broader empirical validation. DIPOLE is stronger.
- **LDCQ (6.33, accept)**: DIPOLE has cleaner theory and more thorough evaluation. DIPOLE is stronger.
- **LatentDiffuser (6.75, accept)**: DIPOLE has a more novel theoretical contribution and a real-world application. Comparable overall.
- **CTRL (6.50, accept)**: DIPOLE has much more extensive experiments. DIPOLE is stronger.
- **DiffCPS (5.33, reject)**: DIPOLE's theory is sound (unlike DiffCPS's flawed proofs) and its results are stronger. DIPOLE is clearly stronger.

DIPOLE is stronger than the 6.25–6.50 anchors and comparable to the 6.75 anchor. The NAVSIM issue and missing ω ablation prevent it from reaching 7+, but the core contribution is solid and well-supported across 39 RL tasks. A score of 6.5 is appropriate — it places DIPOLE above the typical borderline-accept papers and reflects that the paper has a genuine contribution that would benefit from addressing the identified weaknesses.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>