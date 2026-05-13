# COPlanner: Plan to Roll Out Conservatively but to Explore Optimistically for Model-Based RL

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Dyna-style model-based reinforcement learning contains two phases: model rollouts to generate sample for policy learning and real environment exploration using current policy for dynamics model learning.
However, due to the complex real-world environment, it is inevitable to learn an imperfect dynamics model with model prediction error, which can further mislead policy learning and result in sub-optimal solutions.
In this paper, we propose \ouralgo, a planning-driven framework for model-based methods to address the inaccurately learned dynamics model problem with conservative model rollouts and optimistic %real 
environment exploration.
\ouralgo leverages an uncertainty-aware policy-guided model predictive control (UP-MPC) component to plan for multi-step uncertainty estimation.
This estimated uncertainty then serves as a penalty during model rollouts and as a bonus during real environment exploration  respectively, to choose actions.
Consequently, \ouralgo can avoid model uncertain regions through conservative model rollouts,  thereby alleviating the influence of model error.
Simultaneously, it explores high-reward model uncertain regions to reduce model error actively through optimistic real environment exploration.
\ouralgo is a plug-and-play framework that can be applied to any dyna-style model-based methods.
Experimental results on a series of proprioceptive and visual continuous control tasks demonstrate that both sample efficiency and asymptotic performance of strong model-based methods are significantly improved combined with \ouralgo.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a model based reinforcement learning method that target for solving the challenge of inaccurately learned dynamic model problem through a combination of conservative model rollouts offline and optimistic exploration with the environment online. To estimate the dynamic model uncertainty, the authors utilize the model disagreement method which learns an ensemble of dynamic models.  This estimate uncertainty are utilized in two folds, it can serve as a penalty term during rollouts and as an incentive when interating with the environment online. The authors conduct experiments in environments like MuJoCo and DeepMind Control and demonstrate the proposed method achieves better sample efficiency and performance than other model-based RL baselines.

### Strengths
This paper is easy to follow and the proposed approach is also simple and flexible to use on existing model based RL methods. The authors have done extensive experiments and ablations to show their strengths in sample efficiency and model performance. I think the part of the success of this paper attributes to the good uncertainty estimation.

### Weaknesses
The good uncertainty estimation comes with the cost of extra computation, in Appendix D.6, there is an above 20% increase for MBPO variant and around 40% increase for the DreamerV3 variant. The test time comparison should also be discussed. While the authors provide the computation cost during training, the inference time cost during the test phase should also be considered. The additional overhead of ensemble model inference and uncertainty calculation during planning may impact the real-time applicability of the method, especially in resource-constrained environments. The paper should provide a more detailed analysis of the trade-off between improved performance and increased computational cost during both training and testing.

### Questions
Where do the authors see the main factor for the extra computation cost?  Is it the uncertainty calculation for all action candidates through the ensemble of dynamic models?

What options is available for trading off computation cost for uncertainty estimation performance?

In Figure 7, while the proposed method reached lower loss, this does not imply that the method achieved better exploration, which the authors claim in related work section, how can this be demonstrated?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a model-based reinforcement learning framework COPlanner to mitigate the model errors from the model rollouts and environment exploration. This framework includes three components, and the most crucial component is the Planner to predict future trajectories based on selected actions and their corresponding uncertainties, and the uncertainties work as penalties during model rollouts and bonuses during environment exploration.

### Strengths
1. The paper is easy to understand.
2. The idea of using the variance over predicted states of the ensemble members to approximate the model uncertainty either penalty or reward seems interesting to me.
3. The proposed framework outperforms baselines in almost all experiments.

### Weaknesses
1. Lack of comparisons to some framework.  In section 3.2, the paper mentions some previous methods to estimate uncertainty samples after generations or to decrease model error by re-weighting or discarding samples with high uncertainty. This should require a comparison to demonstrate using variance through model ensemble.
2. Lack of visualization of experiments. The results are all basically tables, line plots.

### Questions
1. It's still not quite clearly to me how Conservative rate and Optimistic rate are selected. What's the intuition here about why they are always different than each other in every experiment settings? Are they selected according to Action candidate number, and Planning horizon as well?
2. Following the weakness, experiments for comparison and more visualizations are necessary.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents COPlanner, a model-based reinforcement learning algorithm that combines optimistic exploration of high-reward model uncertain regions with pessimistic model learning to avoid biased updates in information-sparse regions. The approach leverages an MPC-style action selection and is evaluated on both proprioceptive as well as visual control tasks.

### Strengths
-	Increasing learning efficiency of model-based reinforcement learning agents is an important research direction, particularly in light of hardware deployment under costly data generation
-	Combining optimistic exploration of uncertain high-reward behaviors with conservative model rollouts to improve information quality of samples is a very promising research direction
-	MPC-style action selection provides several benefits over direct policy evaluation
- The approach is evaluated against several baseline agents on OpenAI Gym as well as DeepMind Control Suite environments, with both proprioceptive and visual tasks for the latter

### Weaknesses
 - Generally, the paper would benefit from a stronger selection of established baselines. For instance, in the proprioceptive DeepMind Control Suite (DMC) experiments, it would be valuable to include comparisons with model-free methods like MPO, DMPO, or D4PG, as well as state-of-the-art model-based approaches like DreamerV3. Similarly, for the visual DMC tasks, incorporating a strong model-free baseline such as DrQ-v2 would provide a more comprehensive evaluation.
 - The visual control experiments are currently run for only 1 million steps. However, based on the convergence behavior observed in similar tasks in Dreamer-v1 (Figure 10), it is likely that the agents have not fully converged on the Acrobot, Finger, and Quadruped tasks within this timeframe. Extending these experiments to at least 2 million steps would allow for a more accurate assessment of the agents' performance and a fairer comparison with existing methods.
 - The Dreamer-v2 scores presented in Figure 9 appear to be significantly lower than those reported by the original authors on GitHub. It is crucial to clarify which specific Dreamer implementation was used to obtain these results, as discrepancies in implementation can lead to substantial variations in performance.
 - The task selection for the proprioceptive DMC experiments focuses on relatively simple tasks. Additionally, some of the "MuJoCo"/Gym tasks have not been run to convergence, making it difficult to draw definitive conclusions about the performance of the proposed method on these tasks. Expanding the task suite to include more challenging environments and ensuring convergence would strengthen the experimental evaluation.
 - The hyperparameter study in Appendix D.4 is a good starting point, but it should be extended to a wider range of environments to identify more generalizable trends. A more comprehensive hyperparameter analysis would provide valuable insights into the sensitivity of the proposed method to different parameter settings and help determine optimal configurations for various tasks.
 - The paper overlooks some highly relevant prior work. For example, the concept of optimistic exploration of uncertain future returns for visual control has been previously investigated in [1], which also builds upon the Dreamer-v2 agent. Similarly, optimistic finite-horizon exploration under nominal reward functions was explored in [2]. Furthermore, work such as POLO [3], which combines online planning with offline learning, is also relevant to the proposed approach.

Minor:

- The DMC tasks are MuJoCo-based, so “MuJoCo” task description should be replaced by “Gym”

### Questions
-	Action selection by optimizing over a 5-step rollout without terminal value function is surprising. Do you have intuition for why this short-term reasoning is sufficient? 
-	The original Dreamer-v3 paper also evaluated on proprioceptive DMC environments - why not use Dreamer-v3 as a proprioceptive baseline as well?
-	There are several task-specific parameter choices for proprioceptive control. How impactful are these? Ideally a single set of hyperparameters would be used throughout.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
