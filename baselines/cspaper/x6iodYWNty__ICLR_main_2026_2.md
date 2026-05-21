---
job_id: 0316fae1-d365-4f21-9181-cf4ac2d45c80
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: x6iodYWNty.pdf
paper: Neural Predictor-Corrector: Solving Homotopy Problems with Reinforcement Learning
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, sitting at the intersection of reinforcement learning, optimization, sampling, and learned algorithm design.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, presents a coherent method and broad experiments, and while there are notable technical and empirical weaknesses, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious embedded prompts, or other manipulative content targeting automated review systems in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes Neural Predictor-Corrector (NPC), a reinforcement learning framework that learns adaptive predictor step sizes and corrector stopping rules for homotopy-based solvers. The paper argues that several problem families, including graduated non-convexity for robust optimization, Gaussian homotopy for global optimization, homotopy continuation for polynomial root-finding, and annealed Langevin dynamics for sampling, can be viewed through a common predictor-corrector lens, and evaluates a single high-level framework across these settings. The main empirical claim is that amortized offline training yields policies that improve efficiency on unseen instances while preserving solution quality.

## Strengths
The paper has a clear cross-domain ambition, and that is its most compelling aspect. Framing robust optimization, Gaussian homotopy, homotopy continuation, and annealed Langevin dynamics under one predictor-corrector control perspective is interesting and useful, especially for an ICLR audience that values learned algorithm design rather than yet another task-specific heuristic.

The high-level formulation is easy to grasp. **Figure 1** and **Figure 2** do a good job of conveying the central intuition: the interpolation is explicit, but the solution path is implicit and must be tracked, with predictor and corrector playing complementary roles. **Figure 3** is also helpful in making the RL control loop concrete by showing which quantities are treated as state, which knobs become actions, and how reward feeds back into the agent.

The empirical coverage is broader than many papers in this area. It is not common to see one framework tested across optimization, root-finding, and sampling in a single submission. Even if the tasks are relatively small-scale, the breadth does support the paper’s “unified solver” narrative better than a single-domain study would.

Several result tables do suggest consistent efficiency gains. In particular, **Table 1** and **Table 4** show large reductions in corrector iterations and runtime while maintaining essentially unchanged accuracy/success metrics. For example, in **Table 4**, HC on katsura10 and cyclic7 drops from 39/41 iterations to 7/8 while preserving 100% success, which is a strong empirical signal that the learned policy can speed up the classical pipeline rather than merely trading away correctness. Likewise, **Table 1** shows sizable runtime reduction on the GNC registration benchmarks with very similar rotation/translation errors.

The paper is also commendably explicit about one limitation. The discussion in Appendix D that reward scaling must be tuned per problem class is important, and the authors deserve credit for not pretending the RL setup is fully plug-and-play already.

## Weaknesses
1. **The mathematical specification of the algorithm is not consistently correct, and in a paper whose contribution is mainly a learning-based controller for numerical procedures, this matters.**  
   The most visible issue is **Algorithm 1 on Page 5**, line 6:  
   \[
   \texttt{while } H(\mathbf{x}_{t_n}, t_n) \le \epsilon_n \texttt{ and } i_n \le i_n^{\max} \texttt{ do}
   \]
   This stopping condition appears reversed. If \(H(\mathbf{x}_{t_n}, t_n)\) is already below tolerance, the corrector should stop, not continue iterating. Presumably the intended condition is something like \(H(\mathbf{x}_{t_n}, t_n) > \epsilon_n\), or some task-specific residual criterion. This is not a cosmetic typo, because the paper’s central claim is precisely about learning corrector termination rules. If the core algorithm statement is wrong, it undermines confidence in the exact MDP being optimized and in the reproducibility of the method.

   There are additional notation-level ambiguities around what the corrector is actually monitoring. On Pages 5 to 6, the paper alternates between “tolerance,” “attained tolerance,” and “optimality metric,” but does not formally define a single generic stopping residual shared across tasks. For a framework paper, this level of underspecification is frustratingly hand-wavy.

2. **The formulation across problem classes is more “common control wrapper around heterogeneous solvers” than a genuinely unified algorithmic object, and the paper occasionally oversells the depth of the unification.**  
   The predictor and corrector mechanisms are fundamentally different across Sections 3.3 and Appendix A. In GNC, the predictor updates weights; in GH and ALD, the predictor is effectively just a schedule over smoothing/noise levels; in HC, the predictor is Padé extrapolation. Likewise, the correctors range from Gauss-Newton/LM to momentum descent to Newton to Langevin updates. What is actually shared is mostly the RL policy interface over \(\Delta t\) and stopping criteria. That is still a valid contribution, but it is weaker than the paper’s broader rhetoric about a unified solver architecture.

   **Figure 3** reinforces this point unintentionally. The diagram shows a generic RL agent controlling “predictor’s next level” and “corrector’s tolerance,” but the surrounding text reveals that these actions instantiate quite different semantics depending on the task. I would encourage the authors to tone down the stronger universality claims and present the contribution more precisely as a learned controller for a family of homotopy-style PC solvers.

3. **The RL objective is underspecified, making it hard to assess whether the reported gains come from principled sequential optimization or from reward engineering tailored per domain.**  
   On **Page 6**, the reward is described as
   \[
   R=\sum_{t=1}^T \lambda_1 r_t^{\text{acc}} + \lambda_2 r^{\text{eff}},
   \]
   but \(r_t^{\text{acc}}\) is only loosely defined as “convergence velocity or relative error change.” This is not enough for reproduction or for evaluating whether the same training signal is used consistently across the four problem classes. The concern becomes sharper because the appendix later states that the reward scales \(\lambda_1,\lambda_2\) are manually tuned per task and even per noise regime. That is a substantial amount of hidden problem-specific engineering for a paper advocating a general framework.

   This is not just a documentation issue. If the method’s behavior is sensitive to reward scaling, then amortized generalization claims should be stated much more carefully. A policy that generalizes within a narrowly curated training distribution after manually calibrated reward shaping is useful, but it is not the same as a robust, generally transferable learned homotopy controller.

4. **The empirical evidence for generalization is weaker than the prose suggests.**  
   The paper repeatedly emphasizes “generalization to unseen instances,” but the experiments mostly demonstrate within-problem-class transfer under relatively modest shifts. Examples: training on one point-cloud sequence and testing on other sequences, training on randomized Ackley coefficients and testing on fixed small-dimensional functions, training on a 10-mode GMM and testing on a 40-mode GMM/funnel/DW-4. This is evidence of some transfer, yes, but not of broad amortized generalization in the stronger sense implied by the introduction and conclusion.

   There is no experiment testing whether a single policy transfers across multiple homotopy families, nor any experiment showing graceful degradation under stronger distribution shift. The paper would be much stronger if it explicitly separated three claims: generalization across instances, across parameter ranges, and across solver families. Right now these are blurred together.

5. **Several baseline comparisons are either incomplete or not fully fair, especially when the contribution is positioned as outperforming “classical and specialized baselines.”**  
   In **Table 3**, CPL is penalized by including training time in the runtime column, whereas the classical methods and NPC inference are compared at test time. One can argue for reporting total cost, but then the paper should also report NPC training cost, which is currently absent from the main tables. Without that, the comparison is asymmetric.

   In **Table 5**, iDEM achieves materially better \(\mathcal{W}_2\) on some tasks, but is dismissed as “not directly comparable in runtime.” Fair enough, but then the conclusion “consistently outperforms existing approaches in computational efficiency” becomes too strong. If some strong baselines are omitted from runtime comparison and others are disadvantaged by including training time, the narrative should be toned down.

   More broadly, the paper often compares against default or canonical schedules rather than carefully tuned task-specific heuristics. Since the whole motivation is replacing heuristics, a fair bar is not a strawman fixed schedule but a reasonably optimized schedule baseline. **Figure 4** is illustrative here: the classical methods are shown as trade-off curves produced by manual tuning, while NPC is a single learned operating point that lies below the curve. This is visually appealing, but the figure does not tell me whether the classical curve includes the strongest adaptive non-learned policies available in the corresponding literature, or only the authors’ chosen schedules. As presented, **Figure 4(a,b)** is suggestive, not decisive.

6. **The experiments are broad but somewhat shallow, and the scale is limited for the paper’s ambition.**  
   The GH benchmarks in **Table 3** are 2D toy functions in the main paper, which is not very convincing for a method supposed to speak to difficult non-convex optimization. The appendix includes 10D Ackley, and there the result is less flattering: NPC has much lower runtime but notably worse objective value (\(0.47\) versus \(0.01\) for Classic GH in **Table 9**). That is exactly the kind of trade-off the main paper should discuss openly, because it hints that the method may become more fragile as dimensionality grows.

   Similarly, the sampling experiments are on low- to moderate-dimensional synthetic targets, and the root-finding evaluation is on a small benchmark set. I am not demanding large-scale industrial workloads, but for a paper claiming a broadly useful neural solver, the evidence currently feels more like a promising proof of concept than a fully convincing demonstration.

7. **Some equations and task-specific mathematical definitions are ambiguous or potentially inconsistent.**  
   A few examples:
   - In **Equation (2)** on Page 4 and **Equation (9)** in the appendix, the Gaussian homotopy notation is sloppy. Writing \(g(\mathbf{x}) \star \mathcal{N}(0,t\sigma^2)\) is fine informally, but then the expectation form uses \(g(\mathbf{x}+t*\sigma)\), where \(t*\sigma\) is undefined and dimensionally odd. Usually one expects \(\mathbf{x}+\sqrt{t}\sigma\) or \(\mathbf{x}+t\sigma\) with a clear variance parameterization.
   - In the HC derivation around **Equation (19)**, the chain-rule expressions for \(\mathbf{x}''(t)\) and especially \(\mathbf{x}'''(t)\) are presented too tersely to verify. Given that the predictor uses these derivatives to form the Padé approximation in **Equation (20)**, skipping derivation details weakens confidence.
   - The ALD formulation is particularly confusing. **Equation (4)** on Page 5 defines \(H(\mathbf{x},t)\propto \exp(-(1-t)f(\mathbf{x})-tg(\mathbf{x}))\), which reads like an unnormalized density. But the corrector description later refers to minimizing or differentiating \(H\) much like an objective. If the update uses the score of the intermediate density, that should be written as \(\nabla_{\mathbf{x}}\log H(\mathbf{x},t)\) or equivalently the gradient of the negative potential, not simply “the change in a statistical distance” or “\(\nabla H\)” in a generic way. This notation mix-up is more than pedantry, because sampling and optimization are not interchangeable here.

8. **The paper does not sufficiently disentangle where the gains come from.**  
   The ablation in **Table 6** only removes state components. That is useful, but not enough. The central design space includes at least: learned step size, learned stopping rule, reward shaping, amortized training distribution, and the underlying classical predictor/corrector implementation. There is no ablation comparing: (i) learned \(\Delta t\) only, (ii) learned stopping only, (iii) both, (iv) a lightweight non-RL adaptive controller. Without this, the paper leaves open the nagging question of whether full RL is necessary, or whether much of the gain comes from one easier-to-design adaptive heuristic.

9. **Presentation is decent overall, but there are enough local inconsistencies to matter.**  
   There are several grammatical slips and notation inconsistencies across Pages 5 to 9. More importantly, some captions and footnotes are careless. For example, **Table 2** repeats the footnote “The agent is trained on the Aquarius sequence for the point cloud registration task,” even though Table 2 is about multi-view triangulation, which reads as a copy-editing error and causes confusion about what was actually trained where. These are not fatal, but they add friction in a paper that already spans multiple technical domains.

## Questions
1. Please clarify the exact corrector stopping condition in **Algorithm 1, line 6**. Is the inequality sign reversed? More generally, what is the precise task-specific residual/criterion being compared to \(\epsilon_n\) in each of the four domains?

2. Can the authors provide a complete formal definition of \(r_t^{\mathrm{acc}}\) for each problem class in the main paper, not only informal prose? Right now the reward is too underdefined to reproduce. It would also help to know how sensitive performance is to \(\lambda_1,\lambda_2\).

3. How much of the improvement comes from learning the predictor schedule versus learning the corrector termination rule? An ablation with “learned \(\Delta t\) only” and “learned stopping only” would meaningfully increase my confidence.

4. What is the actual offline training cost of NPC for each problem family? Since **Table 3** includes CPL training time in runtime, it would be fair to report NPC training cost somewhere in the main paper, even if only as a separate number.

5. Can the authors sharpen the generalization claim? Specifically, what distribution shift is intended: new instances from the same family, new parameter ranges, or genuinely different tasks within a family? Right now the paper sometimes implies more than the experiments establish.

6. For sampling, could the authors clarify whether the corrector uses \(\nabla_{\mathbf{x}}\log H(\mathbf{x},t)\), \(\nabla_{\mathbf{x}} H(\mathbf{x},t)\), or the score of the target/intermediate density? The notation around **Equation (4)** is confusing, and a precise statement is needed.

7. Regarding **Figure 4**, what exact procedure generated the classical trade-off curves? Were adaptive non-learned baselines from the literature included, or only manually tuned fixed schedules? This matters for interpreting the “below the curve” argument.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The experiments use public benchmarks and synthetic tasks, and the paper does not raise immediate concerns related to privacy, bias, safety, or legal compliance based on the presented content.

## Soundness Rating
3: good. The core empirical story is plausible and supported by multiple experiments, but there are important issues in algorithm specification, mathematical precision, and ablation depth that prevent a higher soundness score.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are helpful, but there are too many notation inconsistencies, underspecified objectives, and local errors for a framework paper spanning several technical domains.

## Contribution Rating
3: good. The cross-domain framing and learned control perspective are interesting and valuable, even if the unification is somewhat overstated and the empirical validation does not fully support the broadest claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real idea and the breadth of empirical coverage is a meaningful plus, but it also has several nontrivial issues in specification, fairness of comparison, and scope of claims. I lean positive because the learned controller view over homotopy solvers is worth putting in front of the community, though the paper needs tightening.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the technical presentation with care, though some domain-specific numerical details would still benefit from author clarification.