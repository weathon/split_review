- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5
I now have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper studies zero-shot generalization (ZSG) in offline reinforcement learning within a contextual MDP framework. It first proves (Proposition 4) that merging data from multiple environments without context information makes the dataset indistinguishable from an "average MDP," and the optimal policy for that average MDP can be near-optimal for no individual environment — a clean impossibility result. It then proposes two meta-algorithms, PERM (model-based) and PPPO (model-free), which leverage a pessimistic policy evaluation (PPE) oracle to produce policies whose suboptimality decomposes into a supervised learning error that shrinks with the number of training environments and a reinforcement learning error controlled by dataset coverage. Experiments on Procgen using IQL with multiple value networks (IQL-4V) show modest improvements over single-network IQL.

## Strengths

1. **Clean impossibility result establishing the need for context-aware methods.** Proposition 4 proves that without context information, the merged offline dataset is compliant with an "average MDP." The 2-context example (Figure 1) starkly illustrates that the optimal policy of this average MDP can have near-zero expected return while the true ZSG-optimal policy achieves 0.5. This provides a rigorous justification for why new algorithm designs are necessary, going beyond earlier empirical observations.

2. **First provable suboptimality bounds for zero-shot generalization in offline RL.** Theorems 9 (PERM) and 14 (PPPO) provide finite-sample bounds that decompose the ZSG gap into an SL error term (which decreases with the number of training environments \(n\)) and an RL error term (controlled by dataset coverage via the uncertainty quantifier). This is a genuine theoretical contribution — prior theoretical work on multitask offline RL (Bose et al., 2024; Ishfaq et al., 2024) required additional interaction with downstream tasks, placing it outside the zero-shot regime.

3. **Coherent theoretical framework connecting pessimism to generalization.** The paper structures the problem cleanly: PPE as a meta-evaluation oracle, PERM for model-based optimization, and PPPO as a model-free variant whose bound depends only on \(|\mathcal{A}|\) rather than policy-class covering numbers (Remark 15). Remark 11 further shows the bound reduces to the single-environment PEVI bound when \(|C|=1\), demonstrating consistency with prior work.

## Weaknesses

### Fatal
None. The theoretical results, given their assumptions (access to an oracle satisfying Definition 5, i.i.d. context sampling), are sound. The limitations lie in the connection between theory and experiments, and in the strength of the empirical validation.

### Major

1. **Theory-experiment disconnect.** The paper's theoretical guarantees require (a) an oracle \(\mathbb{O}\) returning an uncertainty quantifier \(\Gamma_{i,h}\) with high-probability guarantees (Definition 5), and (b) maintaining per-environment models or critic functions for PERM. The experiments instead use IQL-4V, which the paper itself describes as "not exactly the same optimization objective" and "a first-order approximation of what could be achieved with the PERM framework" (line 217). No theoretical guarantee is provided for this variant, nor is it shown that IQL-4V implements any concrete instance of the PPE oracle. Conversely, the theory relies on covering numbers that would be astronomically large for the deep neural network policies used in the Procgen experiments (Remark 10 gives \(\log \mathcal{N}_\epsilon^\Pi = O(|\mathcal{A}||\mathcal{S}|H\log(1+|\mathcal{A}|/\epsilon))\) for the general case, which is intractable for image-based state spaces). The brief mention of linear MDPs (line 205) is not developed into a practical instantiation. Thus the experiments do not actually validate the theory, and the theory does not cover the experimental setting.

2. **Weak empirical evidence.** The reported improvements are modest: on the Expert dataset, IQL-4V achieves a normalized mean of 0.710 vs. IQL's 0.685; on the Mixed dataset, 0.612 vs. 0.595 (Table 2). Standard deviations overlap in many cases. No statistical significance tests are reported. The comparison includes only BC and IQL from Mediratta et al. (2023); other recently proposed ZSG methods for offline RL (Yang et al., 2023; Mazoure et al., 2022) are discussed in related work but not compared against. The ablation study (Table 3) on a single game (Miner) shows a trend with increasing number of value networks but again lacks statistical rigor. The paper claims "effectiveness of our proposed approach" (line 225), but the evidence is too thin to support this unequally, especially given the methodological mismatch described above. PPPO is never tested experimentally.

### Minor

1. **Ambiguous context definition and grouping.** The context space \(C\) is introduced abstractly, and the paper never specifies what a "context" concretely represents (e.g., different Procgen games? different levels within a game?). In the experiments, 200 Procgen training levels are grouped into 4 environments of 50 levels each (line 224) with the brief justification "for practical reason." The rationale for this specific grouping (why 50? why not 10 or 100?) and its effect on the i.i.d. assumption of the theory are not discussed. This makes it harder to assess whether the experimental setup respects the theoretical assumptions.

### Trivial

1. PPPO (Algorithm 3) is proposed with theoretical guarantees but never implemented or experimentally evaluated, despite being presented as a key contribution alongside PERM.

## Nice-to-Haves

- **Instantiate the framework concretely in a tractable setting.** As the harsh critic suggested, restricting the theory to linear MDPs and running small-scale experiments where the oracle can be implemented exactly (e.g., least-squares with concentration bounds) would allow clean empirical validation of the suboptimality bounds.
- **Compare against additional ZSG methods** discussed in related work (Yang et al., 2023; Mazoure et al., 2022) to help calibrate the contribution.
- **Statistical significance tests** (e.g., paired bootstrap across games) for the Procgen results, given the modest margins and overlapping error bars.
- **A clear limitations section** discussing the oracle assumption, the i.i.d. context assumption, the challenge of uncertainty quantification in high dimensions, and the gap between theory and practice — rather than deferring only the i.i.d. assumption to future work.

## Removed Points

- **Criticism about overclaiming "first":** The paper claims to be "the first to theoretically study the generalization ability of offline RL in the contextual MDP setting" and "the first offline RL methods that provably enjoy the ZSG property." It clearly distinguishes its zero-shot setting from prior multitask/few-shot work (Bose et al., 2024; Ishfaq et al., 2024) by noting that those approaches "require additional interactions with the downstream tasks" (lines 12–13, 45). This distinction is genuine and properly qualified with "to the best of our knowledge." *Removed: not a valid weakness given the clear framing.*

- **Criticism that Proposition 4's contribution is "modest" because the failure of offline RL without context is already known from prior empirical work:** The paper's contribution is the *theoretical* proof, not the empirical observation. Dismissing a rigorous theoretical result as "modest" because an empirical trend was known is unfounded — proving *why* something happens is a different order of contribution from observing *that* it happens. *Removed: dismissive of a genuine theoretical result.*

- **Criticism about PPPO data-splitting wasting data:** The paper explicitly states (Remark 13, line 187) that the data-splitting trick "is only used to avoid the statistical dependency...for the purpose of theoretical analysis." The critic is criticizing an acknowledged theoretical convenience as if it were a practical proposal. *Removed: the paper explicitly flags this as a theoretical device.*

- **Criticism that the oracle has no concrete construction for non-tabular settings:** While true that no concrete construction is given, the paper states (Remark 7) that "bootstrapping technique...is straightforward to implement" and the framework is presented as a *meta-algorithm*. This is a scope choice, not an error. The point is merged into Major Weakness 1 (theory-experiment gap). *Merged, not independently listed.*

- **Strength about PPPO being "model-free with reduced complexity":** PPPO is theoretically proposed but never empirically tested. Claiming this as a strength without any experimental validation is premature. *Removed: untested theoretical algorithms should not be presented as demonstrated strengths.*

## Novel Insights

The harsh critic's central observation — that the paper's experiments (IQL-4V on Procgen) do not actually implement or validate the theoretical framework (PERM/PPPO with certified uncertainty quantifiers) — is the most penetrating insight across the reviews. It cuts deeper than the usual "stronger baselines" or "more experiments" criticisms because it identifies a *category mismatch*: the paper tries to serve two masters (rigorous theory and large-scale empirical validation) without connecting them through an intermediate setting where the theory is actually realizable. The missing piece is not more Procgen games or bigger neural networks, but a *verification experiment* — e.g., a linear MDP or tabular environment where the oracle can be concretely implemented and the suboptimality bounds numerically checked. Neither reviewer identified this specific missing link, but synthesizing their observations surfaces it clearly.

## Suggestions

1. **Add a verifiable instantiation.** Run experiments on a linear MDP or tabular environment where the PPE oracle can be concretely realized (e.g., using least-squares value iteration with Hoeffding-style concentration bounds). This would allow direct numerical verification of the suboptimality bounds in Theorems 9 and 14, bridging the theory-experiment gap.

2. **Reposition the paper or strengthen the heuristics.** If the large-scale Procgen experiments remain, explicitly reposition them as heuristic demonstrations inspired by the theory (not validations of it), and substantially strengthen them: add more baselines, report confidence intervals of the mean or paired significance tests, and discuss why the gap between theory and practice is acceptable for a first theoretical treatment.

3. **Clarify the context grouping rationale.** Explain why 50 Procgen levels per environment was chosen and discuss whether the i.i.d. context assumption is violated by this grouping.

4. **Remove or qualify the "effectiveness" claim.** The current wording ("suggests the effectiveness of our proposed approach," line 225) overstates what the data support, given the small margins, overlapping error bars, and acknowledged algorithmic mismatch.
