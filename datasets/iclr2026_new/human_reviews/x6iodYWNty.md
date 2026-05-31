## Human Reviewer 1

### Summary
A number of problems in different domains can be framed as homotopy
interpolations between an easily solved source problem and a complex target
problem. Such problems are typically solved with a predictor-corrector
framework. Here, a solution is found to the initial easy problem. Then, the
predictor advances the problem following the homotopy interpolation, and the
corrector modifies the solution to fit the new problem.

Prior work has treated these homotopy problems separately in different domains.
This paper proposes to unite a number of these problems under a single
framework. It then proposes a neural predictor-corrector framework, which uses
reinforcement learning to train a policy that outputs the next level for the
predictor and the next tolerance for the corrector --- previously, these values
were determined via heuristics. Experiments show that the final RL agent
effectively learns to set these values.

### Strengths
1. This application of reinforcement learning seems quite novel to me. I
   appreciate that PPO is able to be used "out of the box" to solve the problem.
2. The problems chosen for the paper are quite diverse, which shows the
   applicability of the framework. For example, I could see the application to
   sampling / Langevin dynamics could eventually tie into generative modeling.
3. The computational requirements for this method are quite low (lines 314-315),
   making the research more accessible.
4. The limitation of sensitivity to reward scale is acknowledged in the
   appendix.
5. The ablation of the state components helps in showing that all parts of the
   state are necessary for NPC.

Overall, I found the paper quite easy to read despite not having much
familiarity with homotopy interpolations myself.

### Weaknesses
My main concern is that it seems the experiments were only conducted over one
trial, as I could not find any mention of repetitions, and no error bars are
reported in the tables. It is advisable to conduct multiple trials of each
algorithm and use statistical testing to check that differences between
algorithms are significant.

I have also listed several questions in the section below; these are minor points that I think would be useful to address in the updated paper.

### Questions
1. I am unclear if the Homotopy Paradigm discussed in Sec. 3.1 is a novel
   contribution of this work. Is the term "Homotopy Paradigm" already widely
   used in the literature? If so, could a citation for it be added in Sec. 3.1?
   I think I am confused because the first sentence of the introduction
   (line 32) seems to indicate that the Homotopy paradigm is already well-known,
   while lines 121-122 indicate that it is a perspective introduced in this
   work. Assuming this perspective is novel, it may be good to list it as a
   contribution in the introduction. Right now, the first contribution of the
   introduction (line 82) makes it clear that unifying the approaches under the
   homotopy paradigm is novel, but it is unclear if the homotopy paradigm itself
   is novel.
2. Based on Appendix D, it seems the NPC framework shifts the manual effort from
   tuning the parameters for the predictor and corrector to tuning the reward
   scales for the RL training. What do you see as the benefits and tradeoffs of
   this shift? Might there be cases where it is easier to just use the
   heuristics? When is it better to try to tune the rewards?
3. Table 6 shows that removing certain components from the state can increase
   the number of iterations required more than removing other components, e.g.,
   removing the corrector's tolerance increases by 64, while removing the
   homotopy level only increases by 21. Does this say anything about which parts
   of the state are most essential to NPC?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The homotopy paradigm is a principle to solve optimization problems by transporting solutions to problems from a simple family to a target problem domain. The paper discusses application areas in which this principle is applied: annealing in optimization and sampling. The predictor corrector (PC) method is a family of methods that solve homotopy problems by predicting a new location of a solution and then correcting that prediction. Existing PC approaches typically rely on a an interpolation schedule that must be chosen in advance. While some domains offer natural choices, others do not as the authors claim. Therefore, the authors propose to learn an interpolation using RL, which is implemented by learning the predictor and corrector steps using a neural network. The evaluation of the paper contains tasks from 4 domains and ablation studies that showcase the generalizability of the approach and competitive performance. The ablations provide some insights into the importance of the individual components.

### Strengths
- The paper provides a nice unifying perspective that was at least new to me.
- The method seems to improve over baselines on the reported problems. For some of the domains they evaluate on (GNC, root finding) I am not sure how well chosen the baselines are but that is rather on me.
- The method is pretty simple, and thus seems to be easy to reimplement. I am surprised that almost no hyperparameters must be changed from the stablebaselines defaults.
- Overall the paper is pretty clear and well written.

### Weaknesses
### Method
- The paper presents a very interesting and simple idea: use (reinforcement) learning to improve optimization and sampling methods. While I am not aware of any paper that discusses this under a single umbrella of homotopy problems, I have seen works that use learning to propose sampling steps, eg [1, 2, 3, 4, 5]. Some of these methods are mentioned in the related work section, yet I think it should become more clear that the objective of the paper is a unifying perspective.

### Wording:
- "Because the predictor-corrector procedure is non-differentiable and early decisions influence the entire trajectory, supervised or self-supervised training is inadequate" I think its totally fair that you use RL, but if you had data for supervised training, I think you could actually train in supervised fashion as your NN will be differentiable, no?
- I am not sure if you can call the predictor and corrector schedules in Song et al. (2020) "handcrafted heuristics " as you state in your text, but their design choices are theoretically well motivated. Generally, using a linear schedule makes sense for many problems I would say.

### Evaluation
- The global optimzation problems are only in 2d, which seems pretty low to me, given that other communities like the derivative-free optimization community optimize on those functions in >10d. I would be interested in seeing the results on higher dimensions. But I think this point alone is not enough for rejection in my eyes.
- I think the results are not the strongest on every task, for instance on the sampling problems, PGS seems to be on par at least. But I think this is a nitpick, since the approach seems to be more motivated to convince in its generality.

### Clarity
- While the high level idea of the paper is clear to me, some details of the algorithm are not: Why do you predict the corrector actions in line 3 of the algorithm? Is it always that single action you apply in line 7? If you predict both steps at once why have them separate at all? It would make much more sense to me if you first predicted the predictor step and then iteratively multiple different corrector steps based on H.

### Minor
- You should mention in the main paper that the functions you test on are 2d in Section 5.3.

---
### Sources
[1] Richter, Lorenz, and Julius Berner. "Improved sampling via learned diffusions." _arXiv preprint arXiv:2307.01198_ (2023).

[2] Wang, Congye, et al. "Reinforcement learning for adaptive MCMC." _arXiv preprint arXiv:2405.13574_ (2024).

[3] Xi Lin, Zhiyuan Yang, Xiaoyuan Zhang, and Qingfu Zhang. Continuation path learning for homotopy optimization. In International Conference on Machine Learning, pp. 21288–21311. PMLR, 2023.

[4] Ichikawa, Yuma. "Controlling continuous relaxation for combinatorial optimization." _Advances in Neural Information Processing Systems_ 37 (2024): 47189-47216.

[5] Hruby, Petr, et al. "Learning to solve hard minimal problems." _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_. 2022.

### Questions
- How do you weigh the two terms in your reward formulation? A specific equation would be very helpful.
- For how long did you train your model? I am not familiar with the defaults of stable baselines and the info is not listed in the appendix.
- How did you choose your kernel for computing the KSD in the evaluation?
- As you state yourself, there are prior methods that use learning in the context of PC, but which seem to not generalize as well as yours as you point out in line 111. It would be interesting to see a comparison here, to understand better at which cost the generalization of your method comes, if an at all, especially as it is one of the key claimed contributions. Have you done such comparisons?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes a Neural Predictor-Corrector (NPC) framework that leverages reinforcement learning (RL) to address homotopy problems across diverse domains, including robust optimization, global optimization, polynomial root-finding, and sampling. The core idea is to unify these traditionally independent homotopy tasks under a shared predictor-corrector (PC) structure, replacing hand-crafted heuristics for step-size selection and iteration termination with RL-learned adaptive policies. The authors employ an amortized training regime to enable one-time offline training and deployment on unseen instances, and validate NPC through experiments showing improved efficiency and stability compared to classical baselines.

### Strengths
1. Unified Framework for Diverse Homotopy Tasks: The paper identifies and formalizes the common PC structure underlying homotopy problems in optimization, root-finding, and sampling—an insight that helps consolidate fragmented research in these domains and highlights potential generalizability across tasks.
2. Empirical Validation Across Domains: The authors conduct comprehensive experiments on four representative homotopy tasks (Graduated Non-Convexity, Gaussian Homotopy, Homotopy Continuation, Annealed Langevin Dynamics) and provide detailed ablation studies (e.g., RL state component analysis) to support the effectiveness of NPC in improving efficiency while preserving solution accuracy.
3. Amortized Training for Practical Deployment: The amortized training design addresses a key limitation of task-specific learning methods by enabling deployment on unseen instances without per-task fine-tuning, which enhances the practical utility of the framework for real-world applications.

### Weaknesses
1. Limited Novelty in RL for Optimization/Sampling: The core premise of applying RL to improve optimization or sampling workflows is not new. As noted in the paper’s related work, prior studies (e.g., Li, 2019; Belder et al., 2023; Ye et al., 2025) have already explored RL for adaptive parameter tuning, optimizer design, and schedule prediction in similar problem spaces. The paper does not sufficiently distinguish NPC from these existing RL-driven optimization/sampling frameworks beyond its focus on homotopy-specific PC structures.
2. Incremental Improvement Over Traditional Methods: NPC largely builds on the well-established PC algorithm for homotopy problems and only replaces heuristic step-size/termination rules with RL policies—this constitutes a relatively minor modification rather than a paradigm shift. The framework does not introduce new theoretical insights into homotopy methods or RL for sequential decision-making; instead, it refines existing components with incremental adjustments, limiting its contribution to methodological advancement.
3. Dependence on Manual Reward Scaling: A critical practical limitation is the need for manual tuning of reward scales for each problem instance (detailed in Appendix A), which undermines the framework’s claim of being a “general solver.” This manual step not only increases the barrier to deployment but also contrasts with the goal of automating heuristic-driven decisions—an issue that the paper acknowledges but does not meaningfully address beyond proposing future work.

### Questions
1. Generalization to Non-Homotopy PC Tasks: The paper emphasizes unification across homotopy problems, but many non-homotopy tasks (e.g., iterative convex optimization, SGD with adaptive learning rates) also use PC-like structures. Does NPC’s RL policy generalize to these non-homotopy PC tasks, or is it inherently tied to the homotopy interpolation paradigm? If not, what limits its generalizability?
2. Comparison to Learning-Based PC Baselines: The paper compares NPC to classical PC methods but only briefly mentions learning-based baselines (e.g., Simulator HC for polynomial root-finding). Could the authors include a more detailed comparison to these learning-based alternatives?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4