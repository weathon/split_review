---

## Summary

DIPOLE proposes a new RL algorithm for training diffusion-based policies. Starting from a "greedified" KL-regularized RL objective, it derives that the optimal policy decomposes into two bounded-weight dichotomous policies — a positive one that maximizes returns and a negative one that minimizes them — each trained stably via sigmoid-weighted diffusion losses. At inference, the combined score mirrors classifier-free guidance and allows controllable greediness via a single scalar ω. Experiments span 39 offline/offline-to-online RL tasks (ExORL + OGBench) and fine-tuning of a 1B-parameter VLA model on the NAVSIM autonomous driving benchmark.

---

## Strengths

1. **Theoretically grounded dichotomous decomposition.** Theorem 1 and Eqs. (7–8) rigorously show that the greedified KL objective's optimal policy factors into `π⁺ ∝ μ·σ(βG)` and `π⁻ ∝ μ·(1−σ(βG))`. Both weights are bounded in (0,1), directly resolving the instability of the unbounded exponential weighting in Eq. (4).

2. **Elegant CFG connection enabling controllable inference.** Eq. (10) shows that `∇ₐ log π*(a|s) = (1+ω)∇ₐ log π⁺ − ω∇ₐ log π⁻`, which is structurally identical to classifier-free guidance. This is not just a curiosity — it converts RL policy improvement into a well-understood inference-time mechanism and gives ω a principled interpretation.

3. **Strong empirical coverage.** Results are reported over 8 seeds across 39 tasks. DIPOLE leads on most ExORL locomotion tasks (e.g., Walker-stand: 953±4 vs. best competitor IFQL at 873±6) and achieves best or near-best aggregate success on 5 of 6 OGBench categories (Table 2). The "DIPOLE w/o rs" ablation in Table 1 confirms that the dichotomous learning mechanism itself — not just rejection sampling — contributes to better-than-CFGRL performance.

4. **Demonstrated scalability to a large real-world VLA.** Fine-tuning a 1B-parameter diffusion VLA (DP-VLA) on NAVSIM with DIPOLE yields 89.7 PDMS on the navtrain split (+1.4 over base) and 94.8 on navtest (+6.5 over base, +5.8 over DPPO at 89.0). Applying RL to billion-parameter diffusion policies in end-to-end autonomous driving is a meaningful proof of concept.

5. **Practical training simplicity.** The training losses in Eq. (9) reduce to adding a bounded scalar sigmoid weight to the standard diffusion regression loss — no backpropagation through the denoising chain, no Gaussian likelihood approximation.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Unexplained underperformance on Jaco manipulation tasks.** Table 1 shows DIPOLE scoring 117±18 on `reach-top-right` and 110±12 on `reach-top-left`, vs. IFQL at 193±9 / 181±11 and FQL at 224±17 / 222±42. These are ~40–50% gaps — larger in absolute terms than DIPOLE's margins of victory on the locomotion tasks. The paper acknowledges Jaco in the table but the text only says DIPOLE "outperforms other baselines in most domains," treating the Jaco deficit as noise. No analysis is offered for why the method underperforms on manipulation, what property of Jaco might disadvantage sigmoid-weighted regression, or whether the advantage function estimates are reliable in that domain. Given that the paper's narrative is that DIPOLE "fully utilizes valuable data in dataset," the Jaco results need to be confronted, not glossed over.

### Minor

- **Navtest headline number somewhat inflates RL contribution.** The paper leads with "+6.5 PDMS" improvement but the navtrain split comparison (88.3 → 89.7, +1.4 points) is the apples-to-apples RL fine-tuning result since it uses separate train/test splits. The paper does acknowledge both variants explicitly in the text and in Table 4, and correctly motivates the navtest setting as targeting "RL application scenarios where ground-truth supervision is lacking." But the abstract and introduction emphasize 6.5 points, which represents a mixture of the base DP-VLA advantage and fine-tuning gain. Authors should be clearer that the navtrain result is the conservative RL-only measure.

- **CFGRL absent from OGBench comparison.** The paper directly positions its contribution against CFGRL (Section 3.2: "our final formulation has some similarity with CFGRL"), but CFGRL appears only in ExORL (Table 1), not in OGBench (Table 2). OGBench is the more demanding benchmark with long-horizon tasks. Including CFGRL in Table 2 would strengthen the comparative case, especially since the paper claims DIPOLE's design achieves more greedy optimization than CFGRL.

- **Greedified objective's theoretical advantage over standard KL is asserted, not established.** Eq. (5) is introduced primarily because it yields an elegant decomposition. The paper motivates it as "greedier" and gestures at analogies to offline RL methods that regularize toward greedier reference policies (Section 3.2), but provides no formal comparison — no policy improvement bounds, fixed-point analysis, or convergence guarantee — distinguishing what Eq. (5) achieves over Eq. (2). This is not a fatal issue (many effective methods are motivated by the computations they enable), but the "greedier" claim deserves more formal support.

### Trivial

- Ablation results are entirely deferred to Appendix D.4 with a single sentence ("We refer to Appendix D.4 for ablation studies"). For a method with two separate learned models and a key hyperparameter ω, a short summary of the ablation findings in the main text would aid readers in understanding what each component contributes.

---

## Nice-to-Haves

- A targeted diagnostic comparing the actual weight distributions `σ(βA)` and `1−σ(βA)` in Jaco vs. Walker tasks would directly test whether the sigmoid weighting is less discriminative on manipulation advantage functions. This would transform the current silence on Jaco into a constructive scope claim.
- Showing performance as a function of ω (evaluated at test time vs. ω used during training) for a couple of environments would quantify the benefit and limits of the controllability claim, turning a theoretical assertion into a demonstrated capability.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "We do not observe the adoption of this scheme in many recent diffusion-based RL methods" slightly overstates the case.** The paper uses this as a rhetorical setup for the subsequent "Why is that?" analysis. The sentence is a colloquial framing of the observation that pure exp-weighted regression is avoided in practice due to the instability issues the paper goes on to describe. The methods cited (Lee et al., 2023; Kang et al., 2023; Zheng et al., 2024) indeed use modified or clipped versions rather than pure exp-weighted regression. This is a style issue, not a factual error — removed.

- **Harsh Critic: Inference-time ω variation is heuristic not theoretically grounded.** The paper derives Eq. (10) showing the score-function decomposition follows directly from Eq. (7); varying ω at inference is a natural consequence of this decomposition. The concern that "the optimality guarantee only holds for the specific ω used during training" applies to essentially all CFG-based methods and is not a paper-specific flaw. Demoted to a theoretical nuance rather than a weakness.

- **Strength Finder: "Addresses an important problem."** Generic. Removed per filter rules.

- **Strength Finder: "Strong applicability for complex real-world decision-making."** Generic closing language from the abstract, not a concrete strength. Removed.

- **Harsh Critic, offline-to-online Table 3 note.** The observation that cube-double shows DIPOLE (89) slightly below FQL (92) is accurate but trivial given standard errors (89±10 vs 92±3) and the general competitive parity across the four tasks. This is not a meaningful weakness — removed.

---

## Novel Insights

The most insightful observation in this paper — which the reviewers hint at but don't fully articulate — is that the dichotomous decomposition can be read as a *generalization* of classifier-free guidance: in standard CFG, the "negative" distribution is the unconditioned model; in DIPOLE, the negative distribution is explicitly trained to capture low-return behavior. This means DIPOLE is doing something richer than CFG — it is training a dedicated critic distribution from data rather than using a structural baseline. This connection suggests a broader design space where different choices of π⁻ could yield other well-known offline RL algorithms as special cases, which the paper sketches (CFGRL as one special case) but does not systematically develop.

---

## Suggestions

1. **Address the Jaco results directly.** Compare the sigmoid weight distributions on Jaco vs. locomotion tasks. If advantage function estimates are noisier or less well-calibrated on Jaco, say so explicitly and discuss whether value learning improvements (e.g., IQL quantile regression tuning) would close the gap.

2. **Add CFGRL to OGBench.** Even a subset of OGBench categories would suffice. This is the most direct competitor and its absence from the harder benchmark is noticeable.

3. **Clarify the NAVSIM headline.** In the abstract or introduction, state both the navtrain (+1.4) and navtest (+6.5) results together, explaining that they serve different purposes, so readers are not misled about the typical RL fine-tuning gain.

4. **Include a 1-paragraph ablation summary in the main paper.** Report at minimum: (a) single model vs. two-head architecture, (b) performance vs. ω, (c) with vs. without rejection sampling (already partially in Table 1). This would make the method's component contributions self-contained in the main text.

---

## Score and Decision

**Originality:** The greedified KL derivation and its natural CFG connection are genuinely novel; the general direction (weighted regression for diffusion RL) is known. Above average.

**Importance of research question:** Training large diffusion policies with RL is a central open problem in embodied AI and autonomous driving. High importance.

**Claims supported:** Strong support on locomotion and most OGBench tasks; the Jaco gap undermines the "fully utilizes valuable data" claim without explanation; navtest framing slightly inflates the driving result. Mostly supported but with notable exceptions.

**Soundness:** The theoretical derivation (Theorem 1, dichotomous decomposition, CFG connection) is technically correct and clearly presented. The training objective is sound.

**Clarity:** Well-organized and clearly written. The method is explained with good intuition. Ablations are deferred too aggressively to the appendix.

**Community value:** High — the CFG connection is immediately useful to practitioners working with diffusion policies, and the VLA scaling result is timely for embodied AI.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>