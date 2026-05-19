Now let me produce the final consolidated review.

---

## Summary

This paper addresses the previously underexplored problem of learning sparse continuous policies under offline RL, where dataset actions falling outside the sparse policy's support cause undefined log-likelihoods and training failure. The authors propose Fat-to-Thin Policy Optimization (FtTPO), a two-stage framework that first learns a heavy-tailed "fat" proposal policy from the dataset and then distills its knowledge into a sparse "thin" actor via reverse KL divergence. The method is instantiated using the q-Gaussian family (sparse q=0 for the actor, heavy-tailed q=2 for the proposal) and includes a q-exponential advantage weighting that truncates low-advantage actions. Results are shown on a safety-critical treatment simulation where FtTPO outperforms Gaussian-policy baselines, and on the D4RL MuJoCo suite where it claims competitive performance.

## Strengths

1. **First systematic approach to out-of-support actions in sparse-policy offline RL.** The paper clearly identifies the problem (Section 3.1): sparse policies assign zero density to dataset actions, yielding undefined log-likelihoods. Prior ad-hoc fixes (random action replacement, reverse KL) are shown to fail empirically. FtTPO is the first method designed specifically to circumvent this issue by using a heavy-tailed proposal as a bridge. This fills a genuine gap in the literature.

2. **Strong empirical demonstration on a safety-critical task.** On the treatment simulation (Section 5.1, Figure 2), FtTPO achieves the highest cumulative reward with tight confidence intervals, and its learned policy concentrates tightly around a small action band — unlike Gaussian baselines which show excessive variance or collapse. This provides direct evidence that a sparse policy learned via FtTPO can be both safe (by avoiding dangerous actions) and high-performing.

3. **Novel q-exponential advantage weighting.** Section 4.3 proposes weighting actions by \(\exp_q((Q-V)/\tau)\) with \(q<1\), which explicitly truncates low-advantage actions below a threshold. This improves on standard exponential weighting (which always assigns non-zero weight) and connects naturally with the sparse policy formalism.

4. **Ablation study comparing key components.** Section 5.3 compares FtTPO against: a SPOT-based actor loss (FtTPO-SPOT), the proposal-only policy (TAWAC-HT), and a Gaussian-proposal variant (FtTPO-SG). The results show that the simple KL actor loss is not worse than SPOT, the sparse actor is not worse than the heavy-tailed proposal, and the heavy-tailed proposal is beneficial over a Gaussian — collectively supporting the design choices.

## Weaknesses

### Fatal
None.

### Major

1. **MuJoCo comparison visualization limits evidence for competitive claims (Evidential).** Figure 4 shows only FtTPO and the single best-performing baseline per environment with full opacity; all other baselines are rendered with low transparency. While the paper is transparent about this design choice, it prevents the reader from independently verifying whether FtTPO consistently matches or exceeds all baselines. The paper's claim that FtTPO "performs favorably to or sometimes better than" state-of-the-art algorithms is modestly worded, but the evidence is incomplete without a clear, full-visibility comparison (e.g., a table of normalized final scores with error bars across all methods and tasks).

2. **Missing comparison to the fat (heavy-tailed) proposal on the safety task (Evidential).** The paper motivates sparse policies by their safety advantage — yet on the task where safety matters most (the treatment simulation, Section 5.1), the baselines are all Gaussian-policy methods. The most relevant control for isolating the benefit of *sparsity* is the paper's own fat proposal policy (TAWAC-HT). The ablation study (Figure 6) compares FtTPO to TAWAC-HT on MuJoCo, where safety is not the primary concern, but this comparison is absent from the safety task. Without it, the paper cannot rule out that the performance gain comes from the two-stage design rather than from sparsity per se.

3. **Mean-copying heuristic is a core design element left unjustified (Methodological).** The paper states (line 104): "before every update of the actor, copy the proposal mean to the actor." This is a strong intervention — it directly initializes the sparse actor's mean to the proposal's mean before every update — yet it receives no ablation, no theoretical justification, and no discussion of when it might fail. Given that the thin actor's learning is central to the contribution, the lack of analysis makes the framework appear fragile rather than principled. An ablation comparing FtTPO with and without this step is necessary.

### Minor

1. **Ablation results presented only as proportions (Evidential).** Figure 6 presents performance as a percentage of FtTPO's final score, which hides absolute variance across seeds. For example, if FtTPO scores 100 and TAWAC-HT scores 99, the proportion is 99% but the difference may be within noise. Providing absolute normalized scores with confidence intervals would allow readers to assess statistical significance.

2. **q-exp advantage weighting not ablated (Evidential).** The paper sets \(q_w=0\) for the weighting coefficient (Section 4.3) and cites prior work for interchangeability of \(q\) and \(\tau\), but does not experimentally separate the effect of the weighting sparsity from the actor sparsity. An ablation comparing FtTPO with \(q_w=1\) (standard exponential weighting) against \(q_w=0\) would clarify the contribution of each component.

3. **Importance-sampling estimator for the thin loss is vaguely described (Clarity).** The paper states using "an unbiased estimator of KL divergence that has less variance (Schulmann, 2020)" (line 104) but does not write the estimator or explain why it is preferred over a simple Monte Carlo estimate of the reverse KL. The current description is insufficient for reproducibility.

4. **Safety-task dataset is small (50 trajectories × 24 steps) (Evidential).** While 10 seeds provide some statistical confidence, the small dataset raises questions about the generalizability of results. This is noted as a limitation to be transparent about rather than a flaw that invalidates the findings.

### Trivial
None.

## Nice-to-Haves
- **Include ad-hoc baseline comparisons (RAR, reverse KL) on the treatment task.** The paper shows these fail on a simple environment (Figure 1); replicating on the safety task would further validate the need for FtTPO.
- **Include SPOT comparison on the treatment task** in addition to the MuJoCo ablation.
- **A discussion of limitations** — e.g., the assumption that the fat policy's mean is a reasonable starting point for the thin policy, or scenarios where the thin policy cannot shift to new modes outside the fat policy's support.
- **A brief positioning relative to safe RL frameworks (e.g., CMDPs)** to clarify the scope of the safety contribution.

## Removed Points

These points were flagged during review but removed after cross-checking against the paper:

1. **"Bounded/Unbounded action space contradiction"** — The critic claimed a contradiction between "unbounded action space" (line 165) and plots showing actions in [-2,2]. The paper describes baseline policies' outputs as "spanning the action range [-2,2]" (line 169), which refers to the range of actions produced by the baselines, not a constraint on the action space. The action space is unbounded; the [-2,2] describes the baselines' behavior. No contradiction exists.

2. **"Reproducibility details missing"** — Removed per hard rule: nitpicks about reproducibility such as undisclosed hyperparameters or code should not be included.

3. **"Schulmann (2020) is non-standard"** — The paper cites this reference, which must be treated as existing. The substantive point about the estimator being vaguely described is retained as a minor weakness.

4. **"Related work on safety should discuss CMDPs"** — This is scope creep; the paper scopes its contribution to the specific safety-as-reward setting and the out-of-support problem.

5. Various formatting, typo, and presentation nitpicks — removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses largely recapitulate the paper's claims and limitations rather than adding new observations about the broader field.

## Suggestions

1. **Replace or supplement MuJoCo learning curves** with a table of normalized final scores (with standard deviations) for all baselines on all 9 tasks, so readers can verify the paper's competitive claims at a glance.
2. **Add TAWAC-HT as a baseline on the safety treatment task** to isolate whether the benefit comes from sparsity or from the two-stage design.
3. **Ablate the mean-copying heuristic** — run FtTPO without copying the proposal mean before actor updates. If performance drops, analyze why and characterize the failure mode.
4. **Provide absolute normalized scores with CIs** in the ablation study (Figure 6) rather than proportions.
5. **Write the exact importance-sampling estimator** for the thin actor loss to improve reproducibility.

## Score and Decision

**Originality:** The paper identifies a genuine and previously unaddressed problem. The two-stage framework is novel in this context and well-motivated.

**Importance:** Sparse policies have clear safety applications (medicine, robotics), making this a relevant problem. However, the paper does not yet fully demonstrate the advantage of sparsity over heavy-tailed alternatives on the safety task.

**Claims supported:** The safety-task results are well-supported. The MuJoCo competitive claims are only partially supported due to the visualization issue. The claim that sparsity provides a safety advantage is weakened by the missing TAWAC-HT comparison on the treatment task.

**Soundness:** The method is conceptually sound. The experimental evaluation has gaps (noted above) but is not fundamentally flawed.

**Clarity:** The paper is clearly written and well-structured, though the estimator description and ablation presentation could be improved.

**Value:** With strengthened evaluation, this would be a useful contribution to the offline RL and safe RL communities. In its current form, the evidence is promising but incomplete.

The paper's core idea has genuine merit and the safety-task results are compelling, but the evaluation has three significant gaps (MuJoCo comparison, missing TAWAC-HT on safety task, mean-copying not ablated) that must be addressed to fully support the claims. The weaknesses are substantive but not fatal — the paper does not make obviously false claims, and the core approach is reasonable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>