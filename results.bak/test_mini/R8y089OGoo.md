## Summary

This paper proposes DIPOLE (Dichotomous diffusion Policy improvement), an RL algorithm for fine-tuning diffusion policies. The core idea is to reformulate the KL-regularized RL objective into a "greedified" form whose optimal policy naturally decomposes into two dichotomous policies — one maximizing return, one minimizing it — each trained with bounded sigmoid-weighted regression losses that avoid the instability of exponential weighting. During inference, the policies' scores are combined linearly, providing controllable greediness via a single hyperparameter ω. The method is evaluated on 39 tasks across ExORL and OGBench in offline and offline-to-online settings, and scaled to a 1-billion-parameter VLA model for autonomous driving on the NAVSIM benchmark.

---

## Strengths

1. **Clean, theoretically grounded dichotomous decomposition.** The derivation from the greedified KL-regularized objective (Eq. 5) to a pair of bounded sigmoid-weighted policies (Eq. 8–9) is mathematically elegant and directly addresses a real problem: the exponential weighting in Eq. (4) causes loss explosion when β is large. The bounded sigmoid weights (σ(βG) and 1−σ(βG)) provably preclude this instability, and the connection to classifier-free guidance (Eq. 10) provides interpretability and a principled mechanism for controlling greediness.

2. **Demonstrated scalability to a 1B-parameter real-world system.** The NAVSIM experiment (Table 4) shows DIPOLE fine-tuning a large vision-language-action model (DP-VLA) with a 1.4-point PDMS improvement on the standard navtrain split (88.3 → 89.7), outperforming strong baselines including Hydra-MDP (86.5), UniAD (83.4), and DPPO (89.0). This goes well beyond standard RL benchmarks and shows practical viability for complex, high-dimensional real-world tasks.

3. **Comprehensive evaluation across diverse RL benchmarks.** The paper tests on 39 tasks across ExORL (9 tasks, 4 domains) and OGBench (30 tasks, 6 domains), plus 4 offline-to-online tasks, with 8 random seeds and standard deviations. DIPOLE achieves best or near-best performance on most tasks against strong baselines including IQL, ReBRAC, FQL, IFQL, CFGRL, and IDQL.

4. **Simple, stable training procedure.** Unlike DDPO/DPPO (requiring multi-step likelihood approximations and Gaussian assumptions) or direct reward backpropagation (noisy gradients through the denoising chain), DIPOLE trains two diffusion models with standard weighted regression losses. This avoids approximation error accumulation and makes the method straightforward to implement and scale.

---

## Weaknesses

### Major

1. **Overclaimed "best performance" on ExORL.** The caption of Table 1 states "*DIPOLE* achieves the best performance." This is factually inaccurate: on the Jaco tasks (reach-top-right, reach-top-left), DIPOLE scores 117 and 110, while FQL scores 224 and 222 and IFQL scores 193 and 181 — DIPOLE is substantially worse. The paper claims "best or near-best" in the OGBench caption (Table 2), which is more defensible (though DIPOLE underperforms IFQL on humanoidmaze-large-navigate (6 vs. 11) and FQL on antsoccer-arena-navigate (57 vs. 60)). The ExORL caption should be corrected to match the more careful OGBench phrasing. This is not a fatal error — the results still show DIPOLE is strong overall — but the caption as written is misleading.

2. **Missing direct comparison to the exp-weighted regression baseline (Eq. 4).** The paper's core motivation is that the closed-form exp-weighted regression (Eq. 4) is unstable and inefficient, and the dichotomous decomposition solves this. Yet the paper never compares DIPOLE to a direct implementation of that exp-weighted baseline using the same diffusion architecture, value function, and data. The baselines used (IQL, FQL, IFQL, CFGRL) all use different architectures or additional mechanisms. A clean ablation replacing the dichotomous decomposition with simple exponential weighting (same architecture, same value estimates) would be the most informative validation of the claimed stability advantage. Without it, the evidence that the decomposition itself — rather than the overall pipeline — causes improvement is weaker than it could be.

### Minor

3. **NAVSIM test-set-trained result presented alongside standard baselines without sufficient separation.** The paper reports a variant trained on the *navtest* split achieving 94.8 PDMS in Table 4, directly compared to baselines that were trained only on training data. The paper does disclose this ("an RL application scenario where RL can be applied in human take-over situations") and the navtrain variant (89.7) is reported separately, which mitigates the concern. However, presenting the navtest variant in the same comparison table alongside standard methods inflates the headline number and could mislead a casual reader. The navtrain result (89.7, +1.4 over DP-VLA) is the more honest apples-to-apples comparison and is still competitive. The paper should more clearly segregate the navtest variant, e.g., in a separate table or with an explicit "exploratory/not a standard benchmark result" disclaimer.

4. **No sensitivity or ablation study for ω in the main text.** The greediness factor ω is a new hyperparameter introduced by the method. The paper refers to Appendix D.4 for ablations (which are present in the original submission but stripped by the parser), but the main text would benefit from at least a brief sensitivity analysis (e.g., a small table or figure showing performance across ω values for one or two tasks) to help readers understand how to set it and how robust performance is to this choice. The NAVSIM experiments do not report the ω value used.

### Trivial

- The paper notes that "we do not observe the adoption of this scheme in many recent diffusion-based RL methods" regarding exp-weighted regression; this is a bit tautological since the reason it's not adopted is the instability the authors describe.

---

## Nice-to-Haves

- A training loss / stability plot comparing DIPOLE to the exp-weighted regression (Eq. 4) would strongly support the claimed stability benefit.
- A brief discussion of computational overhead: training two diffusion models doubles the parameter count and compute vs. single-model baselines like FQL. Reporting training time or parameter counts would be helpful for practitioners.
- A discussion of why DIPOLE underperforms on the Jaco manipulation tasks relative to locomotion tasks, to improve transparency about failure modes.

---

## Removed Points

- The harsh critic claimed the navtest issue "invalidates the headline AD result" — this is too strong. The paper discloses the navtest training scenario, and the navtrain variant (89.7) independently demonstrates improvement. The criticism is retained but demoted to Minor.
- "Ablations and hyperparameter analysis deferred to appendix" — this is a presentation preference; the ablations exist in the original submission. Retained as Minor (sensitivity for ω in main text would improve the paper) but not treated as a major gap.
- Several harsh critic points about "not a new observation," "justification could be stronger," and "not specified whether dichotomous policies are warm-started" are removed as they are either commentary, preferences, or speculative without concrete evidence that the paper's choices are wrong.
- The Strength Finder's generic strengths ("addressed an important problem," "targeted an interesting question") are removed.
- Strength Finder's "Comprehensive evaluation" and "Simple training procedure" are retained as they are specific and grounded in the paper's content.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Correct the ExORL caption to "DIPOLE achieves best or near-best performance" (matching the OGBench caption) to accurately reflect the Jaco results.
2. Add an ablation comparing DIPOLE to a direct exp-weighted regression baseline (Eq. 4) with the same architecture and data, as this directly tests the core stability claim.
3. Clearly separate the navtest variant from the main AD comparison table, or add an explicit caveat that it is not a standard benchmark result.
4. Include a brief ω sensitivity analysis in the main text to demonstrate robustness of the hyperparameter.

---

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| `eM8Db7ukSB.md` (LLMDPD) | 2.50 | R1 | Much weaker; shallow contribution, poor evaluation |
| `IsJaTCzyBA.md` (BiTrajDiff) | 2.50 | R1 | Much weaker; unclear contribution |
| `cr3FWHXgEZ.md` (MMD diffusion) | 3.00 | R1 | Much weaker; limited scope |
| `MKM8EiaowV.md` (Traj Diff + RL) | 3.00 | R1 | Much weaker; different domain |
| `mQfv9Nl2n5.md` (QUAD) | 3.00 | R1 | Much weaker; less novel |
| `sOSdvn2sM2.md` (DP-CPPO) | 5.50 | R1+R2 | Weaker theory, less broad evaluation; DIPOLE is stronger |
| `1fALdE637I.md` (CDPO) | 4.00 | R1 | Weaker; unclear contribution |
| `A2JF06XcPG.md` (NCDPO) | 4.00 | R1 | Comparable methodology quality but less evaluation breadth |
| `tM34PZf8W9.md` (RL-D2) | 4.50 | R1 | Different domain (discrete actions); comparable quality |
| `TidLO0qdp0.md` (RFF) | 4.67 | R1 | Different problem (unlearning); comparable quality |
| `PL0tJOfm7I.md` (ALT) | 5.50 | R2 | Different contribution type; DIPOLE has stronger theoretical novelty |
| `Q1CP0iAmOb.md` (H^3DP) | 6.67 | R2 | Comparable quality; DIPOLE has stronger theory but H^3DP has cleaner evaluation |
| `VSWjHIveqZ.md` (SMP) | 6.50 | R2 | Comparable; DIPOLE has broader RL evaluation |
| `mIeKe74W43.md` (MVP) | 7.00 | R2 | Slightly stronger overall; cleaner evaluation but less original theory |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing:** Comparing to DP-CPPO (5.5), H^3DP (6.67), and MVP (7.0), DIPOLE has a more original theoretical contribution than any of these anchors but is held back by overclaiming (ExORL caption) and the navtest presentation issue. The paper is clearly stronger than the 4–5.5 anchors and sits below the 7.0 anchor (MVP). Final position: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>