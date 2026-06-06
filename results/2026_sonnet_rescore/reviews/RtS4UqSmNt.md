## Summary

This paper introduces a formal model of *controlled sequential social learning* in which an information-mediating planner (e.g., an LLM) dynamically chooses the precision of private signals given to a sequence of Bayesian-rational agents who also observe predecessors' actions. The central theoretical contributions are a novel convexity proof for the altruistic value function (Theorem 2) and the resulting characterization of optimal planner policies for both altruistic (three-phase, Theorem 3) and biased (five-phase, Theorem 5) planners. The framework is complemented by LLM-based simulations in which LLMs serve as planner, agents, and an oracle, revealing both structural alignment with the analytical optima and interpretable deviations attributable to non-Bayesian LLM reasoning.

---

## Strengths

- **Genuinely novel problem formulation.** The integration of a dynamic signal-precision control problem (MDP with state $b_i$, control $q_i$, Equations 3 and 5) with endogenous sequential social learning fills a concrete gap between static information-design-over-sequences and two-way-communication models (Section 2). The distinction from Arieli et al. (2022) and Wu et al. (2025), which fix the information structure at onset, is well-articulated and meaningful.

- **Technically non-trivial convexity result enabling clean policy characterization.** Theorem 2 (convexity of $V_A^*$) is identified as the linchpin for Theorem 3, and the paper correctly explains why it is hard: agents' actions depend endogenously on the public belief, breaking the linearity argument that works in simpler settings (Section 4). The resulting three-phase altruistic optimal policy (invest maximum near $b=0.5$, invest minimally at intermediate beliefs, do not invest at extremes) is clean and interpretable.

- **Counterintuitive biased obfuscation result with policy relevance.** The finding that the biased planner *intentionally decreases* signal precision below baseline $p$ in regime (C) of Theorem 5 (Section 5, "the planner may decrease precision below $p$") is the most policy-relevant result in the paper. It is counterintuitive, clearly explained, and directly relevant to regulatory questions about LLM information mediators.

- **Isolated characterization of LLM non-Bayesian biases (NB1–NB3).** Section 6.1 and Figure 1b cleanly document that LLM agents underreact to congruent signals (NB1), overreact to contradictory signals (NB2), and consequently require stronger public beliefs for cascade entry (NB3). These findings parallel documented human cognitive biases and stand as a useful empirical contribution in their own right.

- **Thoughtfully constructed simulation system.** The Planner/Agent/Oracle three-role architecture (Figure 1a, Section 6) is a methodologically interesting device for operationalizing the theoretical model in LLMs. The Oracle's role—generating a signal of calibrated precision from a fact sheet—is well-suited to the problem.

---

## Weaknesses

### Fatal
None.

### Major

- **Biased planner characterization is structurally incomplete (Theorem 5).** For the altruistic case, Theorem 3 delivers exact equality characterizations with concrete thresholds $d_A, t_A$ and their ordering ($0 < d_A \leq t_A \leq t_M \leq 0.5$). For the biased case, Theorem 5 provides only *lower bounds* in three of five regions: case (B) $\pi_B^*(b) \geq p$, case (C) $\pi_B^*(b) \geq 1-b$, case (D) $\pi_B^*(b) \geq b$. The thresholds $t_1, t_2$ are shown to exist but are not characterized in terms of model primitives $(p, C, k, \delta)$. The abstract promises "characterization of optimal policies for both altruistic and biased planners," but the biased characterization is materially weaker. This is not fatal—the qualitative five-regime description is interpretively rich and the obfuscation result stands—but the paper should be transparent that the biased case is characterized up to lower bounds, not exactly. Readers wishing to compute the optimal biased policy face an underspecified problem in regimes B, C, D.

### Minor

- **"Validation" framing of the LLM simulation overstates what can be established.** The paper claims in its contributions (Section 1) that the simulation demonstrates "the model is robust to non-Bayesian agent behavior," and Section 6.2 describes the structural similarity as showing the model's robustness. However, the Bayesian-optimal policy (Theorems 3 and 5) was derived for an environment with Bayesian agents; the LLM planner operates in an environment with LLM agents exhibiting NB1–NB3. That these two policies look similar (Figure 2a) could reflect multiple explanations. In fact, Section 6.3's hybrid experiment *does* show the analytically optimal policy is "brittle" when applied to non-Bayesian agents, which is actually in mild tension with the robustness framing. The more precise and honest interpretation—that the LLM planner's emergent strategy qualitatively resembles the analytically optimal one and adapts to non-Bayesian agent behavior in ways the analytical policy does not—is present in the paper but not foregrounded. Foregrounding it would sharpen the narrative.

- **Single-scenario welfare quantification without variance reporting.** Section 6.3 reports that "the biased analytical and LLM planners decreased social welfare by 40 to 50% when misaligned," with the true state fixed to $\omega = B$ (disclosed in the Figure 2c caption). While fixing $\omega = B$ (the worst-case for misalignment) is a defensible design choice, the paper provides no information in the main text about variance across simulation runs, sensitivity to parameter settings, or how representative this scenario is. The claim "immense power to guide or derail social learning" may well hold broadly, but rests quantitatively on one parameterization. Results for $\omega = G$ (where the biased and altruistic planners are aligned) are absent, leaving the welfare comparison incomplete.

### Trivial
None.

---

## Nice-to-Haves

- For the biased case: deriving exact threshold expressions even for a restricted parametric family (e.g., $\beta$ linear, uniform prior) would substantially sharpen Theorem 5. Showing $t_1, t_2$ as explicit functions of $k, p, \delta$ for one special case would let readers compute the optimal biased policy without solving the full MDP.
- The hybrid setting (optimal policy, LLM agents) in Section 6.3 is arguably the most interesting empirical comparison for model-misspecification analysis. Expanding it with varied parameter settings and variance reporting would considerably strengthen the empirical case.
- A brief characterization of the heterogeneous-agents extension (Appendix D) in the main text would be valuable, since agent heterogeneity is one of the most significant gaps between the model and real-world social learning.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Remark 2 framing is "misleading in emphasis."** The paper explicitly labels these as conservative simplifications in Remark 2 ("This is limiting when... but not restrictive when..."). The criticism that this is misleading is not substantiated—the paper is transparent about what is assumed.

- **Harsh Critic: Cost-structure asymmetry between altruistic and biased planners should be in the main text.** Section 3.2 explains the asymmetry clearly in the main text paragraphs for each planner type (altruistic incurs cost only above baseline $p$; biased incurs cost $\beta(|q_i - p|)$ for any deviation from $p$, in either direction). The criticism that this is only in the appendix is a misread.

- **Harsh Critic: Threshold parameters in Theorem 5 are inaccessible without the appendix.** This overlaps with the verified incompleteness weakness (Major above) but also involves appendix content that has been stripped. Retained only in its main-text-verifiable form.

- **Strength Finder: "Quantified welfare impacts demonstrate practical significance" as a standalone strength.** This partially conflicts with the minor weakness about single-scenario statistical credibility. Merged into context rather than listed as a strength.

- **Strength Finder: "LLM simulations validate emergent strategies."** The word "validate" is contested (see Minor weakness on framing). The underlying finding—structural similarity between LLM and optimal policies, Figure 2a and 2b—is retained as a verified strength above with more precise language.

---

## Novel Insights

The most genuinely novel insight synthesized across the reviews is the **conjunction of the obfuscation result and the LLM simulation's NB2 adaptation**: the biased analytical planner obfuscates (reduces signal precision) in regime (C) of Theorem 5 because $b < 0.5$ makes precise signals likely to report bad news; meanwhile, the LLM planner *continues to invest* at very low beliefs because it has learned that its agents may overreact to surprisingly positive signals (NB2). These are two different mechanisms—one analytical, one emergent—that converge on last-ditch investment under pessimistic public beliefs. The paper describes each separately, but their connection illustrates a deeper point: the key strategic levers identified by the theory (exploit low-belief regimes) also appear in the LLM planner's behavior, but via a different route (exploiting LLM overreaction rather than Bayesian signal dynamics). This is underemphasized in the paper and represents the most interesting bridge between the theoretical and empirical contributions.

---

## Suggestions

1. In the abstract and Contribution 2, explicitly qualify that the biased case is characterized with lower bounds in three of five regimes, rather than stating a parallel to the altruistic characterization.
2. In Section 6.2, revise the framing from "validates the theory" / "robust to non-Bayesian behavior" to "shows structural alignment while revealing adaptive deviations," consistent with the hybrid experiment showing brittleness of the analytical policy.
3. For Section 6.3, report the number of simulation runs, variance across runs, and at least one result under $\omega = G$ to complete the welfare comparison and support the quantitative claim.
4. For the biased case: even a single explicitly worked example (e.g., $\beta(x) = kx$, $p = 0.6$, specific $C, \delta$) computing $t_1, t_2$ numerically would help readers understand the five regimes concretely.

---

## Evaluation on Key Axes

- **Originality:** High. The formal integration of dynamic signal-precision control with sequential social learning is new, and the convexity proof strategy is non-standard.
- **Importance of research question:** High. LLM-mediated information dynamics at scale is an urgent societal concern; this is a principled analytical entry point.
- **Claims well-supported:** Moderate-high. The altruistic case is fully supported; the biased case has genuine incompleteness. The empirical framing overclaims somewhat.
- **Soundness of experiments:** Moderate. The simulation design is thoughtful, but statistical characterization of welfare claims is thin in the main text.
- **Clarity of writing:** High. The paper is well-organized, the examples are clear, and the proof sketches are informative.
- **Value to the research community:** High. The framework is tractable and generalizable; the empirical findings (NB1–NB3, hybrid brittleness) are useful for the LLM-as-economic-agent community.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>