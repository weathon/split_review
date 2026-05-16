Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper proposes Ranking-Constrained Actor-Critic (RCAC), the first offline reinforcement learning approach for learning branching policies in MILP solvers. RCAC trains a scoring function \(G_\omega\) to weight actions by dual-bound improvement, then constrains the actor-critic policy to only consider the top-\(k\) actions ranked by \(G_\omega\), thereby handling sub-optimal or small training datasets. Experiments on six benchmarks show RCAC consistently outperforms imitation learning (GGCN) and online RL (tMDP) baselines, particularly on easy problems where variance-controlled results are reported.

## Strengths

- **First offline RL formulation for branching in MILP solvers** — The paper explicitly and verifiably states this claim (Section 1: "first attempt to apply the offline RL algorithms to MILP solving"; Section 5.1: "de facto the first work in applying offline RL in learning to branch"). This addresses a real limitation of prior neural branching methods that assume near-optimal demonstrations.

- **Consistent empirical gains on easy benchmarks with proper statistics** — On SC, MIS, CA, and CFL, RCAC trained on sub-optimal (VHB) or small near-optimal (FSB) datasets achieves lower solving time and smaller search trees than GGCN across all four datasets, with means and standard deviations reported over 5 seeds (Tables 2 and 3). For example, on CA, RCAC (VHB) solves in 50.1s vs. 88.0s for GGCN; on MIS, RCAC (VHB) uses 2.4k nodes vs. 4.0k for GGCN.

- **Data collection efficiency convincingly demonstrated** — Table 1 shows that collecting the VHB or small-FSB dataset takes 0.2–1.0 hour for easy problems and 6–8 hours for hard problems, versus 4–10 hours (easy) or 72–144 hours (hard) for the standard FSB dataset. This directly supports the paper's practical motivation.

- **Ablation shows RCAC improves beyond its own ranking model** — Table 5 compares the ranking model \(G_\omega\) alone against full RCAC. RCAC further reduces solving time and tree size in most cases (e.g., CA: 66.8s / 3.7k nodes for \(G_\omega\) vs. 50.1s / 2.5k nodes for RCAC). Figure 3's \(k\)-ablation on CA shows monotonic improvement with larger \(k\), confirming RCAC is learning Q-values for the candidate set rather than simply distilling \(G_\omega\).

- **Well-motivated reward design** — Section 3.1 provides a clear rationale for choosing dual-bound improvement over solving time, LP iterations, or tree size: it is system-invariant, directly reflects branching quality, and remains informative under time limits.

- **Clean positioning relative to prior work** — Section 5.1 draws a clear conceptual line between RCAC and the most similar methods (Huang et al., 2023b; Qu et al., 2022), noting those methods "still assume cheap access to a near-optimal expert heuristic without considering a sub-optimal dataset."

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation: vanilla offline actor-critic without the ranking constraint** — The paper ablated \(G_\omega\) vs. RCAC and varied \(k\) on CA (Section 4.4), but never compares RCAC against the same actor-critic algorithm trained on the same data *without* the ranking constraint (i.e., using all actions for Bellman backups and policy improvement). This control is essential to attribute improvement to the proposed ranking-constraint mechanism rather than to using offline RL in general. If unconstrained offline actor-critic performs similarly, the claimed mechanism is not the source of improvement; if it collapses due to OOD errors, that would be strong evidence for the constraint. As it stands, we only know RCAC > GGCN (IL) and RCAC > \(G_\omega\), not that the constraint specifically is what makes the difference.

- **No statistical variance reported on hard benchmarks (WA, AP)** — The paper explicitly states on line 178: "We evaluate each model on 20 testing instances from the official split and report the best results for each model." Unlike the easy benchmarks where mean and std over 5 seeds are reported, the hard-problem results provide no measure of variance. Given that hard problems are a core motivation for the paper ("especially for large problems where accurate solvers have a hard time scaling"), the lack of variance information makes it impossible to assess whether RCAC's apparent lead (best score on WA, second-best on AP) is reliable. The inconsistency in reporting standards between easy and hard benchmarks is unexplained and undermines the central claim.

### Minor

- **\(k\) selection not justified for main experiments** — The method introduces a critical hyperparameter \(k\) (top-\(k\) candidates from \(G_\omega\)), but the paper never states what value of \(k\) is used in the main experiments (Tables 2, 3, 4). Only an ablation on CA is provided (Figure 3), showing larger \(k\) is better on that dataset. Without knowing \(k\) for the other benchmarks, the results cannot be reproduced, and the reader cannot tell whether \(k\) was tuned per problem.

- **Hyperparameters \(\lambda\) and \(\delta\) not specified** — \(\lambda\) (reward-weighting factor in the scoring function, Eq. 3) and \(\delta\) (the negative penalty for OOD actions) are introduced but never assigned values or justified. \(\gamma\) (discount factor) and \(\zeta\) (reward threshold) are at least partially addressed (\(\zeta=0\) by default), but \(\lambda\) and \(\delta\) are left unspecified.

- **tMDP excluded from hard benchmarks without showing its easy-benchmark performance** — The paper excludes tMDP from WA and AP "due to its long training time and bad performance on easy problems" (line 178), but does not provide any quantitative result to substantiate this "bad performance" claim. Since tMDP is the only other RL-based neural method, its absence from the harder comparison set is a lost reference point.

- **Related work distinction could be more technically concrete** — The claim that Huang et al. (2023b) and Qu et al. (2022) "still assume cheap access to a near-optimal expert heuristic" (line 219) is stated without a concrete technical comparison of what those methods actually do. A few sentences contrasting their algorithmic assumptions with RCAC's would strengthen the novelty claim.

### Trivial
None.

## Nice-to-Haves

- **Brief discussion of why standard offline RL methods (CQL, BRAC, I-DQN) are not directly applicable** — The paper would benefit from a short note acknowledging these well-known methods and explaining why the dynamic action space or reward structure in B&B makes direct application non-trivial. Even a negative result or a reasoned argument would be informative.
- **Inference cost breakdown** — A short comment on per-node inference overhead (especially given three GNNs for \(G_\omega\), \(\pi_\phi\), and \(Q_\theta\)) would help practitioners understand the computational trade-off.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism that VHB is "not a standard baseline, created by the authors"** — The harsh critic raises this but then says it is "acceptable"; moreover, VHB is a clearly defined heuristic (FSB with prob 0.05, otherwise pseudocost branching) and serves a specific purpose as a sub-optimal behavior policy. This is reasonable design practice for a method paper, not a weakness.

2. **Strength claim about "robust experimental design"** — The Strength Finder lists this as a supporting strength, but it conflicts with the verified major weakness (no variance on hard benchmarks). Since the weakness is verified and the strength overgeneralizes, the strength is dropped.

3. **Criticism about "the paper would benefit from a brief discussion of why [CQL/BRAC] are not directly applicable"** — This is a wishlist suggestion, not a weakness. Moved to Nice-to-Haves.

4. **Criticism about "a short comment on the per-node inference overhead"** — Also a wishlist item. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on a standard critical pattern: the core idea is novel and the easy-benchmark evidence is solid, but the experimental evaluation needs a key ablation and better statistical reporting on hard problems to fully support the paper's claims.

## Suggestions

1. **Add the missing control ablation** — Compare RCAC against the same actor-critic architecture trained on the same data *without* the ranking constraint (all actions allowed). Report on at least one easy dataset (CA) and one hard dataset (WA). If the unconstrained version performs worse, the ranking constraint is validated; if similar, the paper must rethink the claimed mechanism.

2. **Report mean and standard deviation for hard benchmarks** — Aggregate existing runs (if multiple seeds were used) or re-run with 3–5 seeds. The reader needs variance to assess reliability on WA and AP.

3. **Specify all hyperparameter values** — State the chosen \(k\) for each benchmark, and report values for \(\lambda\) and \(\delta\) in a table, ideally with a brief sensitivity check.

4. **Provide a quantitative statement about tMDP's performance on easy problems** — If tMDP was run on the easy benchmarks, report its results or a summary so the exclusion from hard problems is grounded.

## Score and Decision

**Originality**: High — first offline RL formulation for MILP branching.  
**Importance of research question**: High — reducing dependence on expensive near-optimal demonstrations is practically significant.  
**Claims well supported**: Moderate — strong on easy problems with proper statistics; weak on hard problems (no variance) and the ranking-constraint mechanism is not isolated from vanilla offline RL.  
**Soundness of experiments**: Moderate — good experimental design overall, but the missing ablation and lack of variance on hard benchmarks are notable gaps.  
**Clarity of writing**: Good — clear motivation, method description, and empirical presentation.  
**Value to the research community**: Good — useful benchmarks, novel method, and a new problem framing for the learning-to-branch community.

The paper makes a genuine contribution and the easy-benchmark evidence is convincing. The two major weaknesses — missing ablation control for the ranking constraint and no variance reporting on hard problems — are fixable and do not invalidate the core contribution, but they do prevent full acceptance of the paper's strongest claims in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>