Now I have sufficient calibration. Let me synthesize the final review.

## Summary

The paper proposes **DIPOLE** (Dichotomous Diffusion Policy Improvement), an RL algorithm for diffusion policy optimization. The key idea is to formulate a greedified KL-regularized objective whose closed-form optimal policy decomposes naturally into a pair of dichotomous policies (positive/reward-maximizing and negative/reward-minimizing) trained with bounded sigmoid-weighted losses. During inference, the two policies' scores are linearly combined (analogous to classifier-free guidance) with a greediness factor ω. The method is evaluated across 39 offline RL tasks (ExORL, OGBench), offline-to-online settings, and a large-scale autonomous driving benchmark (NAVSIM) using a 1B-parameter vision-language-action model.

## Strengths

- **Novel theoretical formulation with genuine insight.** The dichotomous decomposition (Eq. 7–8) transforms an unstable exponential-weighted objective into two bounded sigmoid-weighted objectives, elegantly addressing the optimality-stability trade-off. The connection to classifier-free guidance (Eq. 10) is both insightful and practically useful, providing principled controllability via the ω parameter. This is a non-trivial theoretical contribution that goes beyond incremental combination of existing ideas.

- **Strong empirical results across diverse settings.** Tables 1–3 show DIPOLE consistently outperforming prior SOTA methods (IQL, ReBRAC, IFQL, FQL, CFGRL) across 39 locomotion and manipulation tasks with 8 seeds each. On ExORL, DIPOLE achieves notably large gains (e.g., Walker stand: 953 vs next-best 873; Walker walk: 910 vs 844). The offline-to-online results (Table 3) also show strong fine-tuning gains (e.g., humanoidmaze-medium: 61→97).

- **Successful scaling to a real-world billion-parameter system.** The NAVSIM autonomous driving experiment (Table 4) demonstrates that DIPOLE fine-tunes a 1B-parameter VLA model, achieving PDMS improvements from 88.3 to 89.7 (navtrain) and 94.8 (navtest). This goes significantly beyond the typical D4RL-scale evaluation seen in comparable diffusion-RL papers (e.g., DAC, SRPO, EFM) and demonstrates practical applicability.

- **Controllable inference without retraining.** The ω greediness factor enables adjusting policy conservativeness at test time via simple score interpolation (Eq. 10), which is both elegant and practical.

## Weaknesses

### Major

- **Missing direct comparison against exponential-weighted diffusion regression.** The paper's central motivation is that the exponential weighting scheme (Eq. 3–4) suffers from optimality-stability trade-offs and inefficient learning. Yet no baseline in Tables 1–3 is a diffusion policy trained with that exponential-weighted loss (e.g., directly implementing Eq. 4 with clipping or small β). Without this comparison, the reader cannot determine whether the dichotomous formulation empirically improves over the approach it is designed to replace. The comparisons against IFQL (expectile regression), FQL (flow distillation), and CFGRL (CFG-based conditioning) test different mechanisms, not this specific one. This is a gap in the experimental validation of the paper's core motivation.

- **The AD navtest result uses a non-standard evaluation protocol presented alongside standard baselines.** Table 4 presents "DP-VLA w/ DIPOLE navtest" (94.8 PDMS) as the headline result in bold. This variant trains on the test split — the paper mentions this but presents it in the same table as baselines (UniAD, PARA-Drive, etc.) that use the standard train/test split. The fair comparison is the navtrain variant (89.7, +1.4 points over the already-strong 88.3 imitation baseline). While the test-set training is rationalized as an RL application scenario, presenting the 94.8 result as the marquee number without visually distinguishing the protocol change is misleading. The paper would be stronger if the navtrain result were the primary AD result and the navtest variant were cleanly separated.

### Minor

- **DIPOLE without rejection sampling underperforms relative to IFQL on several tasks.** Table 1 shows DIPOLE w/o rs scoring substantially below IFQL on multiple ExORL tasks (e.g., Jaco tasks: 84/63 vs IFQL's 193/181; Walker walk: 679 vs 844). The full DIPOLE with rejection sampling recovers strong performance, but this means the method's advantage partially depends on an inference-time technique common to several baselines. The paper does not analyze why the trained score combination alone is sometimes insufficient.

- **No ablation of the ω greediness factor in the main text.** The ω parameter is central to the method's controllability claim, but its sensitivity is not analyzed in the main paper (only referenced to Appendix D.4). Similarly, interaction between ω, β, and task difficulty is unexplored.

- **The derivation from Eq. (5) to Theorem 1 is motivated somewhat tersely.** The greedified objective (Eq. 5) is introduced as "we instead consider" with limited justification for the specific functional form of the regularizer (sigmoid-based reference weighting). While the math works out cleanly, the conceptual motivation for the particular form would benefit from more exposition.

### Trivial

- The CFG analogy in the introduction is slightly overstated (CFG combines conditional/unconditional models while DIPOLE combines positive/negative policies), though the paper correctly clarifies the difference in Section 3.2.

## Nice-to-Haves

- Adding a direct exp-weighted diffusion baseline (Eq. 4 with clipping or small β) on a subset of ExORL tasks would directly validate the paper's stated motivation.
- Computational overhead comparison (training two diffusion models vs one) would help practitioners assess the practical cost.
- The AD experiment would benefit from having the DPPO baseline on navtrain as well for completeness.

## Removed Points

- **Formatting/style nitpicks** (various from the harsh critic) — removed per hard rules. These are parser artifacts, not author errors.
- **Criticism about missing appendix content** — removed per hard rules. The parser strips appendices from all papers.
- **"The paper does not mention that clipping the exponential weight or using a small β are common workarounds"** (from Section 3.1 notes) — the paper *does* mention this: line 95 explicitly says "many methods mitigate this issue by either using a small β or clipping the weighting term."
- **Criticism that the CFG analogy "is overstated" in the introduction** — the paper says "closely aligns with," not "is identical to," and later clarifies the exact relationship. This is accurate, not overstated.
- **Claim that the greedified objective is introduced "without a principled derivation"** — the derivation is provided via Theorem 1 (proof in Appendix B, which exists in the original submission). The main text states the theorem and explains the rationale for the sigmoid weighting (boundedness, smoothness). This is standard practice for conference papers.
- **Strength Finder's generic strengths** ("addressed an important problem", "targeted an interesting question") — removed per filtering rules; only concrete, evidence-backed strengths retained.
- **Weakness about "reproducibility details missing from main text"** — the paper references Appendix C and D for implementation details, which is standard for conference papers.
- **The human-finder related weaknesses** — these came from different papers and were unrelated to the current paper.

## Novel Insights

The key insight that emerges from this paper is that the *ratio* of two stably-trained sigmoid-weighted policies (positive and negative) can replace an unstable exponential-weighted policy, while simultaneously providing controllable greediness through a single interpolation parameter ω. This connects KL-regularized RL to classifier-free guidance in a deeper way than prior heuristic uses — the paper shows this connection emerges naturally from a specific greedified KL objective rather than being engineered ad-hoc. The empirical finding that this formulation scales cleanly to a 1B-parameter driving model without training instability is practically significant.

## Suggestions

1. **Add an exponential-weighted diffusion baseline.** Implement Eq. (4) with a diffusion policy (using either clipping or small β for stability) and compare on a subset of ExORL or OGBench tasks. This directly tests whether the dichotomous decomposition provides the claimed benefits.
2. **Restructure the AD experiment.** Make the navtrain result the primary AD result, and present the navtest variant in a clearly separated section or as an ablation, with an explicit caveat about the evaluation protocol difference.
3. **Add an ω ablation in the main text** showing performance vs ω for 2–3 representative tasks, and discuss the interaction with β.
4. **Analyze DIPOLE w/o rs failure modes.** For tasks where w/o rs underperforms IFQL, investigate whether adjusting β or ω would close the gap.

## Score and Decision

**Round 1 bracket:** [6.5, 8.0]

**Anchors consulted:**
- DAC (ldVkAO09Km, avg 6.50, Accepted) — KL-constrained policy iteration via diffusion noise regression. DIPOLE has stronger novelty (dichotomous decomposition vs reformulation), more extensive experiments, and real-world scaling. **DIPOLE is stronger.**
- EFM/QIPO (HA0oLUvuGI, avg 6.25, Accepted) — Energy-weighted flow matching for offline RL. Criticized for limited novelty. DIPOLE has a clearer theoretical contribution and broader evaluation. **DIPOLE is stronger.**
- SRPO (xCRr9DrolJ, avg 6.25, Accepted) — Diffusion behavior distillation with score regularization. More incremental. DIPOLE has stronger novelty and comprehensive evaluation. **DIPOLE is stronger.**
- DVF (TeeyHEi25C, avg 6.25, Rejected) — Value function estimation with diffusion. DIPOLE is far stronger in execution, clarity, and empirical validation. **DIPOLE is much stronger.**
- Diffusion Planner (7BQkXXM8Fy, avg 7.50, Accepted) — Empirical study of diffusion planning design choices. Different contribution type (empirical vs algorithmic). DIPOLE has stronger algorithmic novelty but narrower empirical investigation of design choices. **Roughly comparable quality, different strengths.**
- DMBP (ZULjcYLWKe, avg 7.00, Accepted) — Robust offline RL with diffusion. Different problem focus. **Not directly comparable.**
- Safe Offline RL (j5JvZCaDM0, avg 7.50, Accepted) — Safe RL with diffusion. Different problem focus. **Not directly comparable.**

**Narrowing:** DIPOLE sits above DAC/EFM/SRPO (6.25–6.50) due to stronger novelty and broader evaluation, but below the empirical rigor of the Diffusion Planner study (7.50). The missing direct baseline and AD presentation issue prevent the highest tier.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>