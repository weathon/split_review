Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper tackles the problem of learning control-relevant representations from visual observations in offline RL when the observations contain task-irrelevant distractions. The authors formalize the setting as an ExoPOMDP (POMDP with exogenous variables) and propose CLEAR, which learns separate latent representations for agent-centric state and exogenous distractions via two encoders, a compositional decoder, and an inverse-dynamics-based regularization objective that encourages the state representation to be action-informative while discouraging the exogenous representation from being so. Experiments on three DMC environments with four levels of distraction show that CLEAR generally outperforms prior methods, particularly on the hardest 2×2 Grid setting.

---

## Strengths

1. **Principled problem formalization.** The ExoPOMDP framework cleanly captures the structure of visual offline RL with distractions: the four properties of distractions (no effect on reward, unaffected by actions, independent of agent state, present in observation) directly motivate the method's design. The paper derives why prior latent dynamics objectives (SLAC) lack a mechanism to exclude superfluous information, providing a clear theoretical motivation.
2. **Novel and well-motivated regularization.** The use of *both* a maximization objective over \(\hat{S}\) (J_InvDyn-S: actions should be predictable from consecutive states) and a min-max adversarial minimization over \(\hat{E}\) (J_InvDyn-E: actions should *not* be predictable from consecutive exogenous variables) is technically interesting. This goes beyond single-encoder inverse dynamics approaches by explicitly disentangling controllable and uncontrollable latents.
3. **Strong empirical results on the hardest setting.** On the 2×2 Grid distraction — where the observation contains four identical-looking agents and the model must identify which one is controllable — CLEAR significantly outperforms baselines on Walker and Cheetah, maintaining performance close to the Clean (no distraction) setting. The qualitative results (Figure 4) confirm that CLEAR correctly isolates the controllable top-left agent.
4. **Complementary quantitative evidence via state regression.** Table 2 shows that CLEAR's learned representations maintain low linear-regression MSE to ground-truth state across all distraction levels, whereas SLAC's MSE degrades sharply. This provides independent corroboration that CLEAR's representations are faithful to the true state.

---

## Weaknesses

### Fatal
None.

### Major

1. **Abstract and conclusion claims are overstretched given Hopper results.** The abstract claims CLEAR can "perform consistently well across these distractions," and the conclusion states it is "the only latent dynamics method that can consistently remove superfluous information and maintain a level of invariance." However, on Hopper, CLEAR's normalized score drops substantially from Clean (~87.6) to 2×2 Grid (~47.6) — a ~46% degradation. While the paper *does* acknowledge this in a single sentence in Section 5.1 ("For Hopper, while CLEAR is unable to achieve the desired distraction-robust performance"), the high-level claims in the abstract and conclusion do not caveat this failure case. The headline pitch is stronger than the evidence supports. This is the most significant weakness because it undermines the paper's central "consistent" claim.

2. **Ablation study is too thin to fully validate key design choices.** The ablation (Table 3) is conducted on a single environment (Cheetah, Multiple Videos) and does not separate the two regularization terms (J_InvDyn-S and J_InvDyn-E) — they are ablated only as a pair. The paper shows that J_ELBO alone can produce flipped/degenerate representations (Figure 5, three seeds), but it does not quantify the frequency of each failure mode across all 5 seeds or across environments. The claim that "the inverse dynamics regularization term helps stabilize the training procedure" would be much stronger with seed-level variance and per-term ablation. Without this, the reader cannot assess whether one of the two regularization terms is doing all the work.

### Minor

3. **Baseline comparison fairness is partially unaddressed.** Several baselines (TiA, Den-MDP, RePo, Iso-Dream) were originally designed for online RL or model-based planning. The paper extracts representations from their variational posteriors to feed into TD3+BC, citing precedent from Wang et al. (2022). However, it does not discuss whether baseline hyperparameters were re-tuned for this specific representation-extraction evaluation setting. This does not invalidate the results — the protocol is standard in this literature — but it does weaken the claim of "outperforming baselines" since some methods may be under-fitting their intended use case.

4. **Statistical significance language is imprecise.** The paper states that CLEAR "significantly outperforms" baselines (Section 5.1) without formal hypothesis testing. Several comparisons have overlapping error bars (e.g., Cheetah SV: CLEAR 95.4±3.5 vs. Iso-Dream 92.1±5.5; Walker Clean: CLEAR 96.7±2.1 vs. InfoGating 99.2±0.8). Given 5 seeds each, the evidence for significant differences in these specific pairwise comparisons is weak. This is common in RL papers, but the language should be commensurate with the statistical evidence.

5. **Theoretical analysis relies on unobservable quantities.** The decomposition in Equation 2 uses ground-truth state \(S_t\) to define superfluous information, but the paper correctly notes that \(S_t\) is unobservable and "cannot be computed nor minimized directly." This means the theoretical narrative — that prior methods fail because their objective contains an unconstrained superfluous term — is intuitive and plausible but not formally proven. The empirical observation that SLAC's performance degrades with distractions is sufficient motivation, but the framing modestly overclaims theoretical novelty.

### Trivial
None.

---

## Nice-to-Haves

- **Ablate J_InvDyn-S and J_InvDyn-E separately** to determine whether the adversarial minimization over \(\hat{E}\) is essential or whether maximizing action-informativeness in \(\hat{S}\) alone suffices.
- **Diagnose Hopper's failure mode** by running CLEAR with ground-truth state on the same datasets to determine whether the degradation is a representation issue or an RL/task difficulty issue.
- **Report the frequency of flipped/degenerate representations** for J_ELBO alone across multiple seeds and environments, to quantify the reliability of the plain objective.
- **Analyze the min-max convergence** by plotting the inverse dynamics loss on \(\hat{E}\) over training to verify that the adversarial procedure is actually reducing mutual information between \(E\) and actions.
- **Show latent trajectories of \(\hat{S}\) and \(\hat{E}\) over rollouts** with dynamic distractions, to provide stronger evidence of temporal disentanglement than single-frame reconstructions.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism about methods being "originally for online RL" without addressing the paper's justification.** The paper *does* address this (line 158: "we can use the variational posterior to extract representations similar to what was done in (Wang et al., 2022)"). The raw criticism omitted this justification. *Removed per rule about factually ignoring paper content.*
- **"Missing related works"** was suggested in the harsh critic's implicit framing. Per instruction, I do not mention missing related works.
- **"Pure formatting/style nitpicks"** — any such points that appeared have been removed.
- **"Reproducibility nitpicks"** about hyperparameters or implementation details standard for the field — removed.
- **Strength Finder's claim that CLEAR "consistently outperforms all baselines"** — this conflicts with the verified Hopper weakness where CLEAR is on par with InfoGating, not outperforming. *Moved here because it disagrees with a verified weakness.*
- **"Significant overlap" complaint about baselines comparing CLEAR to Iso-Dream** — the paper acknowledges Iso-Dream's comparable performance in video distractions and correctly notes the difference on the harder 2×2 Grid. The harsh critic's framing overstated the overlap issue. *Weakened to minor point above.*

---

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface standard concerns (overclaiming, ablation depth, statistical precision) rather than identifying novel patterns or connections that the paper itself missed.

---

## Suggestions

1. **Tone down the abstract and conclusion** to acknowledge the Hopper limitation explicitly. Replace "perform consistently well across these distractions" with something like "perform competitively across most settings, with a notable degradation on Hopper that warrants further investigation."
2. **Expand the ablation** to (a) separate J_InvDyn-S and J_InvDyn-E, (b) include at least one additional environment (e.g., Walker), and (c) report the per-seed outcomes for J_ELBO alone (e.g., what fraction of seeds produce each type of failure).
3. **Acknowledge baseline hyperparameter limitations** — briefly discuss whether any baselines were tuned for the representation-extraction setting and, if not, note this as a limitation.
4. **Replace "significantly outperforms" with softer language** (e.g., "consistently achieves higher average scores") unless formal significance testing is performed.

---

## Score and Decision

This paper makes a genuine empirical and methodological contribution: the two-encoder + adversarial inverse dynamics design is well-motivated, the ExoPOMDP formalization is clean, and the results on the hardest 2×2 Grid setting are compelling. However, the paper's most visible claims (abstract, conclusion) overstate the evidence by ignoring the Hopper failure case, and the ablation is not deep enough to fully support the claimed benefits of the regularizer. These issues are addressable in revision and do not invalidate the core contribution.

**Originality:** 6/10 — The two-encoder + adversarial inverse dynamics approach is novel relative to prior work, though it builds on established ideas (Iso-Dream, Denoised MDP).  
**Problem importance:** 8/10 — Distraction-robust representation learning for visual offline RL is practically significant.  
**Claims support:** 5/10 — Core empirical claims are supported, but headline claims about consistency are overstretched given Hopper, and the ablation is incomplete.  
**Soundness:** 6/10 — Methodology is sound, but baseline fairness and statistical precision have unaddressed gaps.  
**Clarity:** 7/10 — Well-written with clear figures, though theoretical exposition could more precisely scope its own limitations.  
**Value:** 7/10 — The method and formalization will be useful to practitioners working on visual RL with distractions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>