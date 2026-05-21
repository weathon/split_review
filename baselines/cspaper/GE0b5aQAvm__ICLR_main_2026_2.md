---
job_id: be33d51a-058d-4c8b-97ce-d5b8086d64e3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GE0b5aQAvm.pdf
paper: Neural Policy Ensembles Are Sub-Optimal
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through reinforcement learning, control-oriented learning theory, and policy ensembling.

## Minimum Quality
Pass ✅. The submission includes the expected core sections, namely abstract, introduction, related work, methodology/theory, experiments, results, and conclusion; although there are serious concerns about correctness, novelty, and clarity, these are better handled in full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions to automated reviewers, or other suspicious embedded text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies weighted ensembles of policies and argues that nonlinear neural policy ensembles are sub-optimal relative to linear policy ensembles, with additional claims about instability under time-varying ensemble weights and about the sub-optimality of nonlinear policy mixing. The paper presents three main theoretical results, one comparing neural and linear ensembles in LQR-like settings, one on instability of neural ensembles under changing weights, and one showing that non-convex mixing is worse than convex mixing for weighted quadratic costs. It also includes empirical studies on synthetic linear and nonlinear control environments intended to support the theoretical claims.

## Strengths
The paper tackles a timely and potentially important question, namely when policy ensembling helps or hurts in control settings. This is relevant both to reinforcement learning and to broader mixture-of-experts style decision systems.

The paper makes an effort to combine theory and experiments rather than relying on one alone. In particular, Sections 3, 4, 5, and 6 are aligned around three concrete claims: sub-optimality, stability, and policy mixing.

The policy-mixing result in **Section 3.3**, especially **Theorem 3** and **Corollary 1**, is the cleanest part of the paper. Within the narrow LQR weighted-cost setup written in the paper, the conclusion that the weighted objective is minimized at the convex weights \(\lambda\) is intuitive and reasonably motivated. Even though I have concerns about how broadly this is later interpreted, this section is more coherent than the earlier theoretical parts.

The experiments are at least broad in coverage. The paper includes multi-regime linear systems, switching-pattern analyses, diversity experiments, stability experiments, and nonlinear mixing experiments. The breadth is visible in **Figures 1 to 5**, and that breadth helps readers see what empirical behaviors the authors want to emphasize.

A figure-specific strength is that **Figure 2** is useful for understanding what the paper means by "switching patterns" and where the claimed gap is supposed to come from. The top-left bar chart and top-right box plot directly show that the authors are not relying on only one regime schedule. Even though I am not convinced the evidence supports the paper's sweeping conclusions, this figure does help communicate the intended failure mode more concretely than the text alone.

A table-specific strength is that the paper does expose a nontrivial amount of hyperparameter information for the neural baselines in **Page 17, the large configuration table** and **Tables 1 and 2**. This is better than many theoretical-control papers that simply assert the neural baseline was "well tuned" without showing any configurations.

## Weaknesses
1. **The central claim is much broader than what the paper actually proves.**  
   The title, abstract, and introduction repeatedly make sweeping statements about "neural policy ensembles" in general, and even extend the implications to RL and MoE/agentic AI. However, the actual theoretical setting is much narrower, mostly LQR or linear dynamical systems with quadratic costs, plus weighted averaging of already-trained policies. For example, **Theorem 1 on Page 3** assumes a stabilizable linear system \(\dot x = Ax + Bu\) and compares neural policies to corresponding optimal linear LQR policies. In such a setting, linear optimal controllers are already structurally privileged, so a broad conclusion like "nonlinear function approximators are inherently unsuitable for ensemble control methods" from **Page 1** is not supported. This matters because the paper advertises a general impossibility result, while the mathematics only addresses a narrow slice of policy ensembling.

2. **The main sub-optimality theorem appears conceptually built into the assumptions.**  
   In **Theorem 1**, the comparison is between neural policies and "corresponding optimal linear policies" \(\pi_i^L = K_i^* x\) solving individual LQR problems. If the benchmark class is already the optimal policy class for those problems, then it is not surprising that arbitrary nonlinear policies can do worse. The "nonlinearity" assumption in **Definition 10 / Equation (8)** explicitly enforces deviation from affinity via \(\kappa(\pi^\theta, D) > 0\). So the theorem is not showing a deep limitation of neural ensembling so much as contrasting non-affine policies against the known optimal linear structure in LQR. That sharply weakens the claimed novelty and significance.

3. **There are serious mathematical problems in the proof of Theorem 1.**  
   The most glaring issue is in **Supplementary Page 11, Equation (17)**, which states that for \(x \in S\),
   \[
   \Pi^N(x) = \sum_{i=1}^M w_i \pi^{\theta_i}(x) \notin \operatorname{conv}\{\pi^{\theta_1}(x), \ldots, \pi^{\theta_M}(x)\}.
   \]
   But by **Definition 8 / Equation (6)**, the ensemble is exactly a convex combination of \(\{\pi^{\theta_i}(x)\}\) because \(w_i \ge 0\) and \(\sum_i w_i = 1\). Therefore \(\Pi^N(x)\) must lie inside that convex hull, not outside it. This is not a minor typo; it breaks the geometric logic of Steps 2 to 5 in the proof, including the deviation \(d(x)\) in **Equation (18)** and the lower bounds in **Equations (19), (23), and (25)**. Once that convex-hull claim fails, the proof as written does not establish the theorem.

4. **Several derivations rely on undefined or unjustified quantities and transitions.**  
   In **Theorem 1's proof**, \(Q_{\text{ens}}\), \(R_{\text{ens}}\), \(\lambda_{\min}(R)\), the geometric constant \(C\), and the measure estimate in **Equation (20)** are introduced without sufficient derivation. The jump from nonlinearity measure \(\kappa_0\) in **Equation (8)** to a positive-measure problematic set \(S\) in **Equation (20)** is asserted, not proven. Likewise, **Equation (22)** lower-bounds the value difference by a quadratic action gap term, but this does not follow directly without a careful comparison argument for trajectories generated by different closed-loop systems. Since the states \(x(t)\) themselves differ under \(\Pi^N\) and \(\Pi^L\), the inequality is not immediate. These are core proof steps, not peripheral details.

5. **The stability theorem is also underspecified and mathematically shaky.**  
   In **Theorem 2 on Page 3** and its proof on **Pages 12 to 13**, the paper claims that if \(\|\dot w(t)\| \ge \beta > 0\), then the ensemble can be unstable, and gives a threshold \(\beta > \frac{\min_i \alpha_i}{2 \max_i \|V_i\|_\infty}\). There are several issues. First, \(\|V_i\|_\infty\) over what domain? Globally, a positive definite Lyapunov function is typically unbounded, so this quantity is usually infinite. Second, the proof uses
   \[
   \left| \sum_i \dot w_i(t) V_i(x) \right| \le \beta \max_i \|V_i\|_\infty \|x\|^2
   \]
   in **Equation (30)**, which mixes a supremum norm of \(V_i\) with an extra \(\|x\|^2\) factor in a way that is not defined. Third, the key coupling term in **Equation (33)** is lower-bounded as
   \[
   |\Delta_{\text{coupling}}| \ge C L_f \kappa_0 \|x\|^2,
   \]
   but Lipschitz continuity usually provides upper bounds, not lower bounds. This is a major sign error / directionality problem. As written, the theorem does not look technically sound.

6. **The notation and modeling are inconsistent across continuous-time and discrete-time setups.**  
   The paper begins with a continuous-time system in **Section 2.1**, defines a discounted infinite-horizon value in continuous time in **Equation (1)**, and states the HJB equation in **Equation (3)**. But a large part of the empirical section and later theory uses discrete-time systems, for example **Equation (10)** on Page 4 and the experiments in **Sections 4 and 5**. The paper never clearly explains how the continuous-time theory maps to the discrete-time experiments, nor whether the same results are supposed to hold in both settings. This matters because HJB-based arguments and Riccati/LQR optimality statements differ materially between continuous and discrete time.

7. **The exposition repeatedly conflates "neural", "nonlinear", and "non-convex".**  
   The paper treats these almost as interchangeable concepts, but they are not. A neural network policy may represent a linear map exactly, for example using identity activation or appropriate parameterization. Yet the paper’s rhetoric often assumes "neural" implies harmful nonlinearity. This is visible in **Definition 7** and then throughout the introduction and conclusion, especially statements such as "nonlinear function approximators are inherently unsuitable for ensemble control methods" on **Page 1**. The empirical section even includes identity activations in the tuning table on **Page 17**, which undercuts the simple neural = nonlinear framing. The distinction matters for both theory and practical interpretation.

8. **The empirical setup does not convincingly validate the general claims.**  
   Most experiments are synthetic and heavily aligned with the theoretical assumptions favoring linear structure. The main comparison in **Section 4** is between analytically optimal LQR controllers and small neural networks trained for 100 or 200 episodes on LQR-style tasks. Showing that a lightly trained neural controller underperforms LQR on LQR is not enough to justify the paper’s strong conclusions about neural policy ensembles broadly. This is especially problematic because the introduction explicitly targets RL and MoE systems, but there is no modern RL benchmark or genuine state-dependent expert routing experiment.

9. **The neural baselines do not appear especially strong or fair.**  
   The supplementary material on **Pages 15 to 16** states that for the \(n_x=4, n_u=2\) case, the hidden size is chosen by parameter-count matching and yields \(h = 1\). That is an extremely small network, and although **Page 17** later shows wider networks in tuning tables, the paper is inconsistent about what configuration is the main baseline. More importantly, the training is fixed to short schedules with no serious model selection protocol. The paper says on **Page 16**, "The experimental design relies on a fixed set of hyperparameters, with no explicit search or estimation process to find optimal values." That directly contradicts the claim in the abstract and main text that the neural ensembles are "well-tuned." This matters because underpowered neural baselines can easily manufacture the claimed gap.

10. **The results tables are internally confusing and, in places, suspiciously repetitive.**  
   On **Page 17**, several rows in the large hyperparameter table have identical or near-identical values across different architectures, activations, and training settings, for example the recurring pairs of LQR mean costs and neural mean costs. The final "P-value" column also appears malformed, with entries like "2.418553 4.281000e-08", seemingly concatenating an effect size and a p-value into one cell. This creates uncertainty about whether the table was assembled correctly, and it makes the empirical claims harder to trust. Similarly, **Table 1** and **Table 2** are introduced in a confusing way, and "Table 2" is named but not actually shown in the provided text.

11. **The figures do not support several of the strong interpretive claims as written.**  
   In **Figure 1**, the top-left bar chart does show higher mean episode cost for the neural ensemble than for the LQR ensemble, and the bottom trajectory plot suggests larger deviation from the setpoint. But these figures only show that the chosen neural baseline performed worse on this particular multi-regime linear task; they do not establish the general theorem-level claim that neural ensembles are fundamentally sub-optimal. The text on **Pages 5 to 6** overstates what the figure shows by saying "Hence the performance of the neural ensemble is always inferior to that of the linear ensemble." One experiment cannot support "always."  
   Likewise, **Figure 2** is visually useful, but the text attributes the gap to "convexity violations" and "slower adaptation" without isolating those causes experimentally. The weight-evolution and adaptation-speed panels suggest a behavioral difference, but they do not identify mechanism. These interpretive leaps weaken the empirical argument.

12. **The paper overclaims significance for nonlinear domains where its own theory does not apply.**  
   In **Section 6**, the authors test nonlinear mixing on an oscillator and soft pendulum and then say on **Page 9** that "there is no underlying theory for mixing in nonlinear systems, empirical validation is required on a case by case basis." That caveat is actually appropriate, but it conflicts with the title and broader framing that suggest a general negative result for neural policy ensembles. If the nonlinear-domain claims require case-by-case empirical validation, the paper should not present its conclusions as a universal principle.

13. **Related work and positioning are too shallow for such a strong thesis paper.**  
   The paper cites some general RL ensemble and MoE references, but the discussion in **Section 7** is thin and does not carefully separate the different uses of ensembles: epistemic uncertainty estimation, bootstrap critics, action averaging, gating/routing, and state-dependent mixtures. Since the title takes a very strong position, the paper needs a much sharper accounting of which ensemble formulations are actually covered by the theory and which are not. As written, prior work is invoked mostly as motivation rather than as direct points of comparison.

14. **There are multiple presentation issues that hurt credibility.**  
   Examples include inconsistent naming such as "Lemma 1" in the main paper versus "Lemma 2" in the supplement for the same result, the typo-like term "vadDerPol" on **Page 8**, repeated "Under review as a conference paper at ICLR 2026" insertions in the middle of the text, and awkward claims like "extremely strong statistical significance" on **Page 6**. None of these alone would be decisive, but together they reinforce the impression that the paper has not been polished to ICLR standards.

## Questions
1. The most important issue is **Equation (17)** in the proof of **Theorem 1**. Since \(\Pi^N(x)=\sum_i w_i \pi_i(x)\) with \(w_i \ge 0\) and \(\sum_i w_i=1\), \(\Pi^N(x)\) must lie in the convex hull of \(\{\pi_i(x)\}\). Can the authors clarify whether this is a typo, or whether the intended claim involved something else, such as trajectories or parameter-space mixing rather than action-space convex combinations? A convincing correction here is necessary because the current proof collapses at that step.

2. Please state precisely what class of policy ensembles your theory is intended to cover. Is it only static action averaging with fixed or externally updated scalar weights, as in **Definition 8**, or does it also include state-dependent gating as in common MoE formulations? This clarification would substantially affect how I interpret the scope of the claims.

3. For **Theorem 2**, over what domain is \(\|V_i\|_\infty\) defined, and how do you justify finiteness? Also, can you provide a corrected derivation for **Equations (30) to (35)**, especially the lower bound in **Equation (33)**, which currently seems inconsistent with standard Lipschitz arguments?

4. In the experiments, what exact neural architecture and training configuration should be considered the main baseline? **Pages 15 to 16** suggest a parameter-matched network with hidden size \(h=1\), but **Page 17** reports results for 32 and 64 hidden units and multiple depths. Please reconcile this inconsistency, and explain how model selection was done without using test performance.

5. Can the authors provide a stronger empirical case outside of LQR-favorable settings, ideally with a modern RL benchmark and a state-dependent mixture baseline? Right now the experiments mostly show that neural controllers underperform optimal LQR controllers on LQR-like problems, which is much weaker than the paper’s broader framing.

6. For the large hyperparameter table on **Page 17**, please clarify the malformed "P-value" column and why multiple rows have nearly identical cost statistics across distinct architectures. If these are aggregate values reused across settings, that should be explained explicitly.

7. In **Figure 2**, the paper attributes the observed difference to slower weight adaptation for neural ensembles. How exactly are the Bayesian updates linked to neural vs. linear ensembling here, given that the weight learner appears shared? Is the effect coming from base-policy quality, from the weight update, or from a specific mismatch between the learned policies and the regimes?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns stood out from the paper itself. The work is about control-policy ensembles and synthetic experiments, and I did not identify human-subjects, privacy, or legal-compliance issues that would require ethics review. The paper does make broad claims relevant to safety-critical control, but that is better handled as a technical-evidence issue rather than an ethics flag.

## Soundness Rating
1: poor. The paper raises an interesting question, but the main theoretical claims are not adequately supported as written, and there are major issues in the proofs, assumptions, and empirical validation relative to the breadth of the conclusions.

## Presentation Rating
2: fair. The overall structure is complete and the paper is readable at a high level, but notation, scope, theorem statements, proof details, and some tables are inconsistent enough to significantly hinder confidence.

## Contribution Rating
1: poor. The cleanest contribution is the narrow weighted-cost mixing observation in the LQR setting, but the main headline claims are overstated relative to what is actually established, and the broader scientific contribution to ICLR is limited in the current form.

## Overall Rating
2: Reject, not good enough. The paper asks a relevant question, but the current submission overclaims, contains serious mathematical flaws, and does not provide evidence strong enough to support its broad conclusions about neural policy ensembles.

## Reviewer Confidence
4: confident. I am confident in this assessment; the main concerns are specific and substantial, especially the convex-hull contradiction in **Equation (17)** and the instability proof issues, though there may still be additional context the authors can provide in rebuttal.