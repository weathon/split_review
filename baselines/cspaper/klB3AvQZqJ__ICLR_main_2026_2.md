---
job_id: ddb62ecd-0102-4107-8cad-cc46af25b837
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: klB3AvQZqJ.pdf
paper: Constraint-Aware Reward Relabeling for Offline Safe Reinforcement Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically offline reinforcement learning, safe RL, and safety-constrained learning.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, method, experiments, quantitative results, and a concluding summary; although I have significant concerns about novelty, theory, and empirical support, these are review-level issues rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious content targeting automated reviewers in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies offline safe reinforcement learning and proposes CARL, a wrapper method that alternates between estimating a cost critic and relabeling rewards with a large negative penalty for state-action pairs whose predicted cost-to-go exceeds a safety budget. The method is intended to work with standard offline RL backbones such as TD3-BC and IQL, and the paper presents a theorem motivating an unconstrained reformulation based on pointwise state-action safety constraints. Experiments on DSRL benchmark tasks suggest that CARL often attains low normalized cost under strict budgets while retaining competitive reward.

## Strengths
The paper focuses on a practically relevant setting, namely offline safe RL under tight cost budgets. That regime is important and under-explored relative to the much more common average-cost or moderately constrained settings.

The method is simple to describe and easy to implement. Algorithm 1 on Page 6 is minimalistic and the “wrapper around an existing offline RL method” design is appealing from a usability perspective. I can see practitioners trying this quickly without re-engineering an entire constrained RL stack.

The empirical section is reasonably broad in task coverage. In particular, Table 1 on Page 8 spans a fairly large set of Bullet and Safety-Gym tasks, and Table 2 shows that the basic relabeling mechanism is not tied only to TD3-BC. Even though I have several reservations about how strongly these results support the paper’s claims, the breadth of evaluation is a real plus.

The paper does a decent job illustrating one practical motivation for the incremental update scheme. Figure 1 on Page 6 is useful, because it visualizes the oscillatory behavior that can arise when cost estimates and policy updates drift apart. This figure supports the authors’ intuition that interleaving cost evaluation and policy optimization more tightly may stabilize training. I wish this were developed more rigorously, but as a motivating diagnostic, the figure is effective.

The “unsafe-only data” experiment is interesting. Figure 3 on Page 9 gives a concrete qualitative picture that CARL can move behavior from unsafe dataset regions toward safer regions, at least in the shown tasks. That is one of the more memorable parts of the paper.

## Weaknesses
1. **The central conceptual move is weaker than the paper suggests, and the novelty claim is overstated.**  
   The core mechanism is to estimate a cost critic and replace the reward by a large negative constant when the predicted cost-to-go exceeds a threshold, see Equation (5) on Page 5. At a high level, this is still a penalty-based method, just with a binary, critic-dependent penalty instead of a scalar Lagrange multiplier. The paper repeatedly contrasts this against Lagrangian approaches, but the distinction is less sharp than claimed. In fact, the appendix itself explicitly frames CARL as another instantiation of penalty-based safe RL. That does not make the paper invalid, but it does reduce the originality of the contribution. For an ICLR main-track paper, “use a learned safety critic to gate reward relabeling for an offline RL backbone” feels more like an incremental algorithmic variant than a genuinely new framework. The paper would be stronger if it positioned itself as a simple practical heuristic with careful analysis, rather than as a new formulation that sidesteps prior constrained optimization ideas.

2. **The theoretical reformulation is not fully convincing, because it quietly changes the problem and then proves equivalence only under strong assumptions.**  
   On Page 4, Equation (2) replaces the original CMDP constraint in Equation (1) with the stronger requirement  
   \[
   Q_c^\pi(s,\pi(s)) \le \kappa,\ \forall s.
   \]
   This is not a benign reformulation, it is a stricter problem. The paper acknowledges that a solution to Equation (2) implies a solution to Equation (1), but not vice versa. That means the proposed method is not actually solving the stated OSRL problem in general, it is solving a stricter surrogate. This matters scientifically because the method may reject reward-optimal policies that satisfy the original expected-cost constraint but violate pointwise safety only in rare or unreachable states. The manuscript treats this stronger formulation as an advantage, but from an optimization perspective it is a different objective class, not merely a cleaner derivation.

3. **Theorem 1 is too narrow to justify the practical algorithm, and parts of the proof are sloppy.**  
   The theorem on Page 4 states equivalence between Problem (2) and the unconstrained problem in Equation (3), but only **assuming there exists a solution to Problem (2)**. That is a strong existence assumption, especially in offline settings with limited support, and it is exactly the regime where safety can be hard. More importantly, the theorem is about an optimization with reward function \(r_\pi\) that depends on the policy \(\pi\), while the practical algorithm on Pages 5 to 6 uses an approximate critic \(Q_c\) and performs one-step interleaved updates with changing relabels. There is a large gap between “if we optimize the exact policy-dependent relabeled objective globally, then the optimizer is safe” and “our stochastic mini-batch procedure with approximate FQE and function approximation learns a safe policy.”  
   There are also technical slippages in notation. Equation (3) defines \(r_{\pi}(s,a)\), but the optimization is written as \(\max_\pi V_{r_s}^{\pi}\), which appears inconsistent. In the proof, the notation also alternates between \(r_\pi\) and \(r_{\pi^*}\) in a way that makes the policy dependence of the reward easy to confuse. This may sound cosmetic, but here it matters, because the whole theorem hinges on policy-dependent reward shaping.

4. **Several mathematical definitions in the problem setup are imprecise or incorrect enough to undermine confidence.**  
   On Page 2, the value functions are defined as  
   \[
   V_r^\pi(s)=\mathbb{E}\left[\sum_{t=1}^T \gamma^t r_t \mid s_1=s \right],
   \]
   and  
   \[
   Q_r^\pi(s,a)=\mathbb{E}_{\tau\sim\pi}[V_r^\pi(s')\mid s_1=s,a_1=a].
   \]
   This is not the standard definition of \(Q_r^\pi\). Normally,
   \[
   Q_r^\pi(s,a)=\mathbb{E}\left[\sum_{t=1}^T \gamma^{t-1} r_t \mid s_1=s,a_1=a\right]
   \]
   or equivalently \(r(s,a) + \gamma \mathbb{E}[V_r^\pi(s')]\). The current definition drops the immediate reward term and uses a shifted discounting convention. Immediately after that, the paper says “Similarly \(V_c^\pi(s)\) and \(Q_r^\pi(s,a)\) denote the cost state- and action-value functions respectively,” which is almost certainly a typo for \(Q_c^\pi\). These are not minor editorial blemishes in a theory-heavy section, they affect the exact meaning of the proposed constraints and theorem. If the notation for \(Q\)-functions is off, then the statement \(Q_c^\pi(s,\pi(s)) \le \kappa\) itself becomes ambiguous.

5. **The safety guarantee is only as good as the cost critic, yet the main paper does not sufficiently quantify critic quality or calibration.**  
   CARL depends critically on whether \(Q_c^\pi(s,a)\) is accurate near the threshold \(\kappa\), because Equation (5) applies a discontinuous binary decision. False negatives directly create unsafe actions with no guardrail. False positives unnecessarily destroy reward signal. The paper acknowledges this dependency only lightly. The appendix noise study is useful, but in the main paper there is no analysis of calibration, no threshold margin study, no estimate of false safe vs false unsafe classifications, and no comparison to softer relabeling rules. This is a major omission because the proposed method turns estimation error into a hard combinatorial decision.  
   The issue is visible in the results tables too. In Table 1 on Page 8, CARL still violates the cost threshold on some Safety-Gym tasks, for example CarGoal2 has cost \(1.77 \pm 0.51\), which is unsafe, and CarCircle1 / CarCircle2 are also well above 1. So even by the paper’s own criterion, the practical method is not reliably imposing the pointwise safety logic advertised in Section 4.

6. **The empirical claims are somewhat selective, and the headline statement of “reliably enforces safety” is stronger than what Table 1 actually shows.**  
   The abstract says CARL “reliably enforces safety constraints under small cost budgets,” but Table 1 on Page 8 gives a more mixed picture. It is indeed safe on all Bullet tasks, but on Safety-Gym tasks it is safe on 8/11 tasks by the authors’ own summary, which is respectable but not “reliably” in the stronger sense implied by the framing. Also, some baselines achieve substantially higher reward while remaining safe on individual tasks, for example BC-Safe and FISOR in some velocity tasks, and CAPS in a few circle tasks.  
   More importantly, the paper’s interpretation of “best or second-best safe method” is not systematically quantified. A compact aggregate, such as average reward among safe methods, number of safe wins, or Pareto dominance counts, would make the claim much more convincing. Right now the reader has to manually scan Table 1 and infer the narrative.

7. **The comparison against baselines is incomplete for the paper’s strongest claims.**  
   The central selling point is that CARL handles strict budgets well without heavy machinery. Yet the main paper does not include direct comparisons to simple penalty baselines that are closer to CARL than the chosen competitors, for example an offline RL backbone trained with a fixed reward \(r-\lambda c\), a thresholded penalty variant using immediate cost rather than \(Q_c\), or a soft version of Equation (5) such as  
   \[
   r'(s,a)=r(s,a)-\beta \max(Q_c^\pi(s,a)-\kappa,0).
   \]
   Without such ablations, it is hard to isolate whether the gains come from the binary relabeling idea specifically, or from using a decent offline RL backbone plus any reasonably strong safety penalty. The hard-filtering comparison in Appendix Table 8 is useful, but that is a straw baseline; it does not probe the real design alternatives.

8. **The “no additional hyperparameters” claim is too convenient.**  
   The paper repeatedly states that CARL introduces no task-specific hyperparameters, but this is only partly true. The penalty magnitude is critical, and the main paper already departs from the theorem by using \(R_{\max}\) from the dataset instead of \(V_{\max}\), see Page 7 and Appendix Table 5. That is a design choice with material performance impact. Table 5 shows very large behavioral differences between \(R_{\max}\) and \(V_{\max}\), for example in DroneCircle reward drops from \(0.53\) to \(0.02\), and in AntVelo from \(0.99\) to \(0.38\). So the method is in fact quite sensitive to how the penalty is instantiated. Calling this “no additional hyperparameters” feels like sleight of hand. The authors avoided tuning \(\lambda\), but replaced it with a thresholded penalty whose magnitude choice still matters a lot.

9. **The main empirical evidence for the stability story is underdeveloped.**  
   Figure 1 on Page 6 is presented as evidence that large \(M\) and \(K\) lead to oscillation, motivating \(M=K=1\). But the figure shows only one task, one backbone, and one setting. There is no systematic ablation over \(M\) and \(K\) in the main paper, no quantitative stability metric, and no results table showing whether \(M=K=1\) is consistently better across tasks. Since this design choice is central to the algorithm, anecdotal evidence from one AntRun curve is not enough. The paper itself says theoretical convergence is unclear; that is fine, but then the empirical support for the chosen schedule should be stronger.

10. **Some presentation and exposition issues make the paper harder to trust than necessary.**  
   There are multiple typographical and notation issues across Pages 2 to 4, including the \(Q_r^\pi\)/\(Q_c^\pi\) mix-up, the \(r_s\) vs \(r_\pi\) inconsistency, and awkward statements like “state- and ation-value functions.” These are not catastrophic individually, but they accumulate in the exact sections where precision matters most. Also, Figure 2 on Page 9 is not very informative as presented. It shows reward and cost versus budget for only three tasks, which supports the claim that CARL can exploit larger budgets, but the figure excludes the more challenging tasks where adaptation may fail or be more nuanced. Since the text emphasizes generality across changing budgets, the figure reads a bit curated.

11. **The paper occasionally over-interprets qualitative evidence.**  
   Figure 3 on Page 9 is visually appealing, but the accompanying discussion is stronger than the evidence warrants. Showing red rollout points shifted into a safer region compared with blue dataset points does not establish that the method “transforms unsafe dataset trajectories into safe ones” in any deep sense; it only shows final policy outcomes in three tasks. A more convincing analysis would quantify coverage, distance to unsafe regions, or episode-level safety rate in the main paper. Otherwise, the figure remains a nice anecdote rather than hard evidence.

12. **The practical scope is narrower than the framing suggests.**  
   The method assumes access to per-transition costs in the offline dataset and hinges on reasonably learnable cost-to-go structure. That is fine for DSRL, but the introduction occasionally implies broad applicability to safety-critical domains like healthcare and autonomy. Those domains often have sparse, delayed, or partially observed safety signals, where the binary relabeling rule in Equation (5) may be brittle. This is more of a framing issue than a flaw, but the manuscript overstates transferability from benchmark CMDPs to real deployment settings.

## Questions
1. The main theoretical story depends on Equation (2), which is strictly stronger than Equation (1). Can the authors clarify whether they view CARL as a solver for the original expected-cost CMDP, or explicitly as a solver for a stricter surrogate problem? A rebuttal that carefully distinguishes these two objectives would increase my confidence.

2. Please correct and clarify the value-function definitions on Page 2. In particular, is the intended definition
   \[
   Q_r^\pi(s,a)=r(s,a)+\gamma \mathbb{E}_{s'\sim P(\cdot\mid s,a)}[V_r^\pi(s')]
   \]
   and similarly for \(Q_c^\pi\)? If so, the current notation should be fixed, because it affects both Equation (2) and Theorem 1.

3. Can the authors provide a more formal bridge between Theorem 1 and Algorithm 1? Right now the theorem assumes exact optimization with the policy-dependent reward \(r_\pi\), whereas the algorithm uses approximate FQE and one-step stochastic updates. Even a proposition or clear discussion of what parts of the theorem survive under approximation would help.

4. What happens with softer relabeling rules, for example penalizing by \(-\beta \max(Q_c^\pi(s,a)-\kappa,0)\) instead of a hard threshold in Equation (5)? This seems like the most natural comparator to isolate whether the discrete safe/unsafe decision is essential.

5. Since Table 5 shows that \(R_{\max}\) versus \(V_{\max}\) has a large effect, can the authors explain why this should not be viewed as an additional sensitive hyperparameter? If the answer is “we always use dataset-derived \(R_{\max}\),” then that should be presented more carefully and perhaps benchmarked against a few scaled variants such as \(0.5R_{\max}, R_{\max}, 2R_{\max}\).

6. Could the authors provide a compact aggregate summary over Table 1, such as number of safe tasks, average reward on safe tasks, or a Pareto score? The current narrative claims are plausible, but the table is large enough that an aggregate view would make the case much stronger.

7. Figure 1 motivates \(M=K=1\). Do the authors have a broader ablation over \(M,K \in \{1,5,10\}\) across several tasks? A rebuttal table here could materially improve my assessment, because this choice is central to the method.

8. For the unsafe-only training setting shown in Figure 3, can the authors report the corresponding quantitative numbers in the main paper, not only in the appendix? The figure is suggestive, but explicit reward, normalized cost, and safe-rate summaries would make that claim more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond the usual deployment caveats for safe RL benchmarks. The paper uses standard simulated benchmark environments and does not raise a specific ethics issue requiring separate review.

## Soundness Rating
2: fair. The empirical study is fairly broad, but the theory is narrower than the claims, the mathematical presentation has nontrivial imprecision, and the connection between theorem and algorithm is not adequately supported.

## Presentation Rating
2: fair. The paper is readable overall, but several notation inconsistencies, overstatements, and underdeveloped explanations in the theory section materially hurt clarity.

## Contribution Rating
2: fair. The method is simple and potentially useful, but the conceptual advance over existing penalty-based or constrained offline safe RL formulations appears limited, and the evidence does not fully justify the strength of the claimed contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a useful practical idea and a reasonably broad benchmark evaluation, but in its current form I do not think the novelty, theoretical precision, and empirical isolation are strong enough for ICLR main track. The method feels like a sensible heuristic wrapper that may be valuable in practice, yet the paper oversells it as a new formulation with stronger guarantees than are actually established.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with offline RL and safe RL, and I checked the main equations, theorem statement, figures, and results tables carefully.