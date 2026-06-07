## Summary

This paper proposes DIPOLE (Dichotomous Diffusion Policy Improvement), an RL algorithm for diffusion/flow-matching policy optimization. The core idea is to replace the unstable exponential weighting in KL-regularized RL with a greedified objective that decomposes the optimal policy into a positive (reward-maximizing) and a negative (reward-minimizing) policy, each trained with bounded sigmoid weights. At inference, the optimal policy's score is a linear combination of the two dichotomous scores (controlled by a greediness factor ω), connecting the method to classifier-free guidance. Experiments span 39 tasks across ExORL and OGBench (offline and offline-to-online), plus fine-tuning a 1-billion-parameter vision-language-action model on the NAVSIM driving benchmark.

## Strengths

- **Principled derivation from KL-regularized RL to classifier-free-guidance-style inference.** Section 3.2 shows a clean chain: greedified objective (Eq. 5) → closed-form solution (Eq. 6) → dichotomous decomposition via sigmoid identity (Eq. 7–9) → score combination (Eq. 10). The connection to CFG (Ho & Salimans, 2022) is genuinely insightful and distinguishes DIPOLE from ad-hoc inference-time guidance methods like CFGRL. This theoretical contribution is the paper's strongest element.

- **Bounded sigmoid weights solve a real instability problem in exp-weighted regression.** The paper correctly identifies that exp(βG) in Eq. (4) can cause loss explosion when β is large. Replacing it with σ(βG) and 1−σ(βG) (both in [0,1]) precludes unbounded loss growth. This is grounded in a specific, verifiable problem with the standard KL-regularized approach, and the mathematical resolution is clean.

- **Broad empirical evaluation across diverse settings.** The paper evaluates on 39 tasks across two benchmarks (ExORL, OGBench) in both offline and offline-to-online settings with 8 seeds. The inclusion of a "DIPOLE w/o rs" variant that controls for rejection sampling and the offline-to-online experiments provide a more complete picture than most diffusion-RL papers. The demonstration on a 1B-parameter VLA driving model (NAVSIM) shows scalability beyond simulated locomotion.

- **Controllable greediness at inference via ω.** The greediness factor ω is derived formally (Eq. 6–10) and provides practitioners with explicit control over how aggressively the policy pursues high-value actions, which existing weighted-regression approaches (Zheng et al., 2024; Kang et al., 2023) do not offer.

## Weaknesses

### Major

- **Missing the most informative ablation: direct exp-weighted regression with clipping.** Section 3.1 motivates DIPOLE by identifying instability in the exp-weighted loss of Eq. (4). The paper dismisses clipping or temperature reduction with "these treatments compromise the optimality of the extracted policy" but never tests this claim empirically. The paper's central contribution is a solution to the exp-weighting problem; without comparing DIPOLE against the alternative of simply training a single diffusion model with Eq. (4) plus clipping/temperature reduction on the same tasks, it is impossible to attribute observed gains to the dichotomous decomposition specifically. This is the single largest gap in the experimental design.

- **Table 1 caption overclaims relative to the paper's own data.** The caption states "DIPOLE achieves the best performance." On the two Jaco tasks (reach-top-right: 117 vs. 193 IFQL, 224 FQL; reach-top-left: 110 vs. 181 IFQL, 222 FQL), DIPOLE underperforms both baselines by roughly a factor of two with non-overlapping error bars. The text later says "outperforms other baselines in most domains," which is more accurate, but the absolute caption is misleading. The paper does not explain this failure mode, and a reader must manually discover it.

### Minor

- **NAVSIM headline result comes from non-standard evaluation.** The abstract and introduction present the NAVSIM result without distinguishing between training on navtrain (+1.4 PDMS, from 88.3 to 89.7) and navtest (+6.5 PDMS, from 88.3 to 94.8). The larger number (94.8) comes from training and evaluating on the test split, which is not the standard benchmark protocol. The paper does disclose this in the body (Section 4.2, Table 4), but the prominent presentation in the abstract conflates two evaluation protocols with different evidential weight. The legitimate benchmark gain (+1.4 PDMS) is much more modest.

- **DIPOLE w/o rs underperforms IFQL and FQL on several ExORL tasks.** Table 1 shows DIPOLE without rejection sampling trails IFQL/FQL on Cheetah-run (194 vs. 269/222), Cheetah-run-backward (227 vs. 310/231), and both Jaco tasks. Since rejection sampling is a standard post-hoc technique rather than a contribution of this paper, it is unclear how much of the reported advantage is attributable to the learning algorithm. The paper notes this variant exists but does not discuss the implications.

- **Missing DPPO navtrain comparison.** Table 4 reports DPPO only on navtest (89.0). Without DPPO on navtrain, the reader cannot tell whether DIPOLE's +1.4 PDMS navtrain gain exceeds what DPPO would achieve under the same training split.

- **Internal contradiction on adoption of exp-weighted scheme.** Section 3.1 states "we do not observe the adoption of this scheme in many recent diffusion-based RL methods," but the same paragraph cites Kang et al. (2023) and Zheng et al. (2024) as adoptions. If those papers qualify as adoptions, the statement is self-contradictory. The contribution would be better framed as fixing known limitations rather than observing absence.

### Trivial

- None.

## Nice-to-Haves

- Ablate sigmoid weighting in isolation: train a *single* diffusion policy with σ(βG) weights (without dichotomous decomposition) and compare. This would isolate whether the gains come from the bounded weight function or from the positive/negative ratio structure.
- Add hyperparameter sensitivity analysis for β and ω. These control greediness and are central to the method; some discussion even in the main paper would help.
- Acknowledge the computational cost of training two diffusion models (or two LoRA modules in the VLA setting) explicitly, including wall-clock time.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- **Missing hyperparameter sensitivity (β, ω) and ablation studies:** The paper references Appendix D.4 for these. The appendix is stripped by the parser; in the original submission these details exist. Removed per rules.
- **NAVSIM test-split is "methodologically questionable":** The paper explicitly labels navtrain vs. navtest in Table 4 and provides a justification ("human take-over situations… lacking ground-truth supervision"). The concern is downgraded to Minor (presentation) rather than a methodological flaw, since the disclosure is adequate in the body.
- **DIPOLE w/o rs "wins on 5 of 6" (from Strength Finder):** The Strength Finder claimed DIPOLE w/o rs outperforms CFGRL on "all six ExORL tasks" then clarified "5 of 6." In fact, DIPOLE w/o rs wins on 5 of 8 ExORL tasks against CFGRL. This factually incorrect strength claim is removed, though the broader point about rejection-sampling dependence is valid and retained as a Minor weakness.
- **Generic reproducibility concerns about undisclosed details:** These are standard for conference papers with appendix deferrals. Removed per rules.
- **Specific claim about CFGRL "lacks theoretical backing":** This is the paper's own characterization of prior work, not a reviewer observation. Keeping or removing it would change the paper's claims, so it stays as written.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an observation that the paper itself does not fully exploit: the dichotomous decomposition (Eq. 7–9) is structurally analogous to importance-splitting or mixture-ratio estimation in statistics. The positive policy is a reward-skewed version of the reference, the negative policy is a reward-anti-skewed version, and their ratio at inference time performs a form of likelihood-ratio weighting. This perspective suggests that the method could be extended beyond the two-policy case (e.g., multiple quantile levels of G(s,a)) and that the boundedness of the sigmoid weighting is related to the boundedness of importance weights in clipped importance sampling. The paper's empirical evaluation, while broad, does not characterize the conditions under which the two-policy ratio estimator degrades (e.g., low-data regimes where the denominator policy π⁻ has high variance due to sparse low-value samples).

## Suggestions

1. **Add the exp-weighted regression baseline (Eq. 4) with clipping to the ExORL and OGBench tables.** This is the single most informative comparison for the paper's central claim. If DIPOLE outperforms it, the case is made; if not, the contribution needs reframing.

2. **Revise the Table 1 caption and abstract** to qualify the performance claims. Replace "achieves the best performance" with language that acknowledges the Jaco underperformance.

3. **Separate the NAVSIM navtrain and navtest results more prominently** in the abstract and introduction, or flag the navtest result as an in-distribution fine-tuning scenario not comparable to standard benchmark evaluations.

4. **Add a discussion of when the positive/negative decomposition could fail** — specifically, when data is scarce for low-return samples, the negative policy may be poorly estimated, and the ratio in Eq. (10) could become unstable.

## Score and Decision

**Bracketing (Round 1):** Lower band (score ≤ 3.5) retrieved papers averaging 3.0–3.4 on related diffusion RL topics — papers with confused methodology or weak experiments. Middle band (3.5–7.5) retrieved papers averaging 3.67–6.25, including SRPO (6.25, Accept), BDQL (3.67, Reject), and value-function diffusion (6.25, Reject). Upper band (≥ 7.5) retrieved papers averaging 7.6–8.0 on topics only tangentially related (fluid simulation, game theory). DIPOLE is clearly above the lower band; initial bracket placed it at **5.0–7.0**.

**Narrowing (Round 2):** Two queries targeting the 4.5–7.5 range retrieved DAC (6.50, Accept), EFM (6.25, Accept), and RTDiff (5.75, Accept), plus SRPO (6.25) already seen. Full reviews inspected for DAC, EFM, and the earlier SRPO.

- **DAC (6.50):** Stronger D4RL results but narrower scope (only D4RL). DIPOLE has broader evaluation and VLA scaling but has the empirical gaps (missing exp-weighted baseline, overclaiming). Comparable overall.
- **EFM (6.25):** Also addresses weighted regression stability via energy-weighted flow matching. DIPOLE has a more novel decomposition idea but EFM has no corresponding empirical gap. DIPOLE is slightly stronger on balance.
- **SRPO (6.25):** Narrower evaluation, less novel contribution. DIPOLE is stronger.

Comparing against all retrieved anchors, DIPOLE sits approximately in the **5.5–6.5** range. The theoretical contribution is genuinely strong and above the median of the anchor set, but the missing exp-weighted ablation and the overclaiming issues prevent it from reaching the upper end.

**Calibration anchors consulted across both rounds:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| BDQL (gEdg9JvO8X) | 3.67 | R1 | Inferior — confused methodology, unconvincing results |
| Latent Diffusion Planning (k1qVBh5fnb) | 3.40 | R1 | Inferior — narrower scope, less novel |
| SRPO (xCRr9DrolJ) | 6.25 | R1/R2 | Similar — DIPOLE has broader evaluation but empirical gaps |
| DAC (ldVkAO09Km) | 6.50 | R2 | Comparable — DIPOLE has broader scope but missing ablation |
| EFM (HA0oLUvuGI) | 6.25 | R2 | Slightly weaker — DIPOLE's dichotomous idea is more novel |
| RTDiff (0FK6tzqV76) | 5.75 | R2 | Comparable — DIPOLE has stronger theory but similar empirical concerns |
| Value func. estimation (TeeyHEi25C) | 6.25 | R1/R2 | Inferior — presentation issues, weak baselines |

**Final score: 6.0.** The theoretical contribution is well above the acceptance threshold — the dichotomous decomposition and CFG connection are genuinely novel and cleanly derived. The empirical evaluation is broad and demonstrates scalability to a real-world driving model. However, the missing exp-weighted ablation and the overclaiming on ExORL/NAVSIM prevent a higher score. These are fixable in revision without changing the core method.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>