## Summary

This paper casts distributed Traffic Engineering as a Swarm Markov Decision Process (SwarMDP) with variable-sized per-node action spaces and introduces eleganTE, a training/evaluation framework built on the ns-3 discrete-event simulator. The authors provide benchmark scenarios, two learned policies (MLP and GNN) as baseline demonstrations, and compare them against OSPF and EIGRP. The core contributions are the formulation, the framework, and the initial baselines.

---

## Strengths

1. **The SwarMDP extension to variable-sized action spaces is technically sound and fills a genuine gap.** Section 3 (Eq. 1, line 58–66) formalizes distributed routing where each node specifies a distribution over its (variable-sized) neighbor set per destination. This addresses the fixed-input-dimension limitation of prior RL-RO work catalogued in Section 2 (line 43) and is a necessary condition for topology-general policies.

2. **eleganTE's use of ns-3 for faithful simulation is a meaningful engineering improvement over REPETITA's abstract-graph evaluation.** Section 4 (lines 86–93) describes how the framework captures protocol interplay (TCP congestion control, real queue dynamics) that abstract-graph analysis misses. The monitoring-graph, demand-driven-application, and odd-routing modules are well-designed components, and the odd-routing module as a drop-in replacement for OSPF/EIGRP is a clean architectural choice.

3. **The learned policies demonstrate lower delay than OSPF and EIGRP on the predef4s scenario** (Figure 4, line 162), providing proof-of-concept that RL-based routing can outperform shortest-path heuristics on a scenario specifically designed to expose their weaknesses.

4. **The GNN policy processes arbitrary-sized topologies at inference time** (Figure 5, line 127)—a genuine architectural generalization capability that fixed-dimension methods lack. Combined with the variable-sized action space, this demonstrates the machinery for topology-independent routing decisions, even if the resulting performance on larger graphs is currently weak.

5. **Section 2's systematic mapping of prior RL-RO work against six requirements** (lines 41–47) is careful and provides a clear, structured justification for why a new formalism is needed.

---

## Weaknesses

### Fatal
None.

### Major

1. **The "benchmark" label is not earned by the presented evidence.** The title and Section 5.2 (line 141) call the contributions a "benchmark," but a benchmark requires standardized scenarios *with multiple methods evaluated under them*. Only OSPF, EIGRP, random, and the authors' own MLP/GNN policies are compared. **No existing RL-based RO method from the surveyed literature** (Stampa et al., Bernárdez et al., Valadarsky et al., etc.) is implemented or evaluated in eleganTE. A future researcher cannot use this paper to compare method X vs. method Y on scenario Z. This mismatch between the paper's branding and its content undermines the contribution. The paper is better described as a *framework with initial baselines*.

2. **The claim of being "the first formalism that fulfills all requirements for general-purpose RO" (lines 30, 191) is contradicted by the paper's own Limitations section.** Section 7.1 explicitly states: "we leave the evaluation of scenarios with changing topologies and corresponding policies for future work" (requirement #4: Robustness/Resilience) and "for truly distributed TE a decentralized training and execution paradigm is necessary" (requirement #5: Scalability). If two of the six requirements are explicitly deferred, the claim that the formalism *fulfills* all of them is inaccurate. The paper would be more credible framing the SwarMDP as a step toward fulfilling these requirements with specific gaps identified.

3. **The evaluation evidence is insufficient to establish the framework's value for RL-based RO.** Several specific problems compound:
   - **Only two classical baselines** (OSPF, EIGRP) are compared, neither of which optimizes the paper's composite reward function. No RL-based routing methods from prior work are included.
   - **High variance undermines the learned policies' reliability.** The paper itself acknowledges this repeatedly (lines 162, 169, 184), but provides no controlled analysis (ablation studies, sensitivity analysis) to determine whether the issue is the framework, the policy architecture, PPO's instability, the reward design, or the problem's inherent difficulty.
   - **No numerical tables are provided.** Results are reported only in figures (Figures 3–7), making it impossible for future researchers to precisely verify or compare against these numbers. For a paper that positions itself as a benchmark, this is a significant omission.
   - **The generalization experiment is framed misleadingly.** Figure 5 evaluates a GNN trained on 10-node topologies on 25- and 50-node topologies. The text says it "highlights the generalization capabilities" (line 169), but the results demonstrate *failure* to perform well at larger scales. The paper later honestly notes this difficulty (line 30), but the positive framing of essentially negative results undermines trust.

### Minor

1. **No comparison with REPETITA.** The paper criticizes REPETITA for evaluating routing on abstract graph computations (lines 48–49) but does not include any experiment showing that the choice of evaluation framework *changes* routing outcomes. A simple study (same policy in REPETITA vs. eleganTE) would directly validate the paper's core thesis.

2. **No inference latency results.** Requirement #1 (Timeliness) demands sub-second routing decisions. The paper criticizes Bernárdez et al. for "multiple model inference steps" preventing sub-second responsiveness (line 43) but reports no inference wall-clock time for its own policies, even for the largest 50-node scenario.

3. **Single-path unicast routing assumption is not justified.** The paper commits to single-path routing (line 56) without discussing how this relates to multi-path TE approaches (ECMP, flow-based splitting) that are standard in practice and common in related work (Xu et al. 2018, Huang et al. 2022).

### Trivial
None.

---

## Nice-to-Haves

- A code/data availability statement is expected for a framework/benchmark paper.
- The TCP traffic experiment (Section 6.3, Figure 7) is very minimal (predef5 only, no delay data) and could be expanded.
- An ablation of reward function components (ρ_wd, ρ_dr, λ) in the main text (currently deferred to appendix D.2) would strengthen the formulation's justification.

---

## Removed Points

- *Criticism about "no comparison against other RL-based RO methods" appearing multiple times* — merged into Major weakness #1 above. Duplication removed.
- *Criticism that OSPF/EIGRP don't optimize the paper's composite reward function* — This is noted within Major weakness #3 but de-emphasized, as it is standard practice to compare learned policies against heuristics on the learned objective even when the heuristics were not designed for it. The asymmetry here hurts the baselines, which is the authors' intended demonstration.
- *Criticism about the requirement list being "self-defined" and circular* — This is speculative. Defining one's own requirements and then claiming to meet them is only circular if the requirements are trivial, which they are not (Timeliness, Compatibility, Generality, Robustness, Scalability, Realism are well-motivated from Section 1).
- *Strength claiming "GNN policy generalizes to larger unseen network sizes" as a clear positive* — Downgraded to a qualified strength (#4). The GNN architecture enables variable-size processing, which is a genuine technical capability, but the actual performance on larger networks is poor.
- *Strength about Section 2's systematic comparison* — Kept as strength #5.
- *"No code release" criticism* — Moved to Nice-to-Haves since the rule forbids questioning existence/release status of cited entities, but noting the absence of a statement is still a reasonable suggestion.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewers agreed on the core strengths (SwarMDP formulation, ns-3 integration) and the core weaknesses (overclaimed "benchmark" and "first formalism" labels relative to thin evaluation). The most actionable insight is that the paper is structurally caught between a framework contribution (which it delivers) and a benchmark contribution (which it does not, due to the absence of any prior RL-RL method comparison).

---

## Suggestions

1. **Reframe the paper's contribution.** Change "Benchmark" in the title to "Framework and Initial Baselines" or "Evaluation Platform." Replace "first formalism that fulfills all requirements" with "a formalism designed to address all requirements, with specific gaps identified for future work." The paper's Limitations section already does the honest work — the main claims should match it.

2. **Add at least one prior RL-based RO method** from the surveyed literature (e.g., Bernárdez et al. 2023's link-weight approach) to the comparison. This single experiment would transform the paper from a framework proposal into an actual benchmark with cross-method comparison.

3. **Add a REPETITA comparison** showing the same policy evaluated in both frameworks produces different results, directly validating the paper's critique of abstract-graph evaluation.

4. **Provide numerical result tables** (mean, median, IQR for each metric × scenario × method) to enable future researchers to verify and build upon the results.

5. **Report inference latency** for the learned policies across network sizes (10, 25, 50 nodes) to support the Timeliness requirement.

---

## Score and Decision

The paper makes a solid engineering contribution (eleganTE, SwarMDP formulation) but suffers from a significant mismatch between its framing and its evidence. The "benchmark" and "first formalism to fulfill all requirements" claims are not supported by the presented experiments. The evaluation includes only classical baselines, no prior RL methods, high-variance results, and no numerical tables. The core ideas have merit, but in its current form the paper overclaims relative to what it demonstrates.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>