# PWM: Policy Learning with Multi-Task World Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Reinforcement Learning (RL) has achieved impressive results on complex tasks but struggles in multi-task settings with different embodiments. World models offer scalability by learning a simulation of the environment, yet they often rely on inefficient gradient-free optimization methods. We introduce Policy learning with large World Models (PWM), a novel model-based RL algorithm that learns continuous control policies from large multi-task world models. By pre-training the world model on offline data and using it for first-order gradient policy learning, PWM effectively solves tasks with up to 152 action dimensions and outperforms methods using ground-truth dynamics. Additionally, PWM scales to an 80-task setting, achieving up to 27\% higher rewards than existing baselines without the need for expensive online planning. Visualizations and code available at \href{https://www.imgeorgiev

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel model-based reinforcement learning approach to pretrain a large multi-task world model on offline data with multiple tasks, followed by learning policies using first-order optimization for each task individually. Extensive experiments on DMC and Metaworld are conducted to showcase the strengths of the proposed method. While claiming to tackle multi-task challenges, this work tends to train a singular strategy for each isolated task.

### Strengths
1. This paper is clearly written and easy to follow. 
2. This paper presents sufficient experimental results to demonstrate the validity of its proposed method.

### Weaknesses
1. My primary concern revolves around the novelty of the proposed approach. This study appears to amalgamate TD-MPC2 and SHAC methodologies. To elaborate, a multi-task world model incorporating a task embedding and SimNorm activation mirrors aspects of TD-MPC2 for representation learning. Subsequently, during the policy learning phase, policies are acquired via first-order optimization akin to SHAC. Consequently, the original contribution of this work may seem somewhat limited.
2. In Figure 13, PWM exhibits inferior performance compared to SHAC in high-dimensional tasks like Anymal, Humanoid, and SHU Humanoid. Does this observation suggest that in intricate environments, precise world models hold greater significance?
3. DreamerV3 is a powerful baseline model capable of handling various domains with a single configuration. It would be best to compare the proposed method with it in Figure 5.
4. In Figure 6, the left figure indicates that TM-MPC2 outperforms PWM in Metaworld, contradicting the statement "In both settings PWM achieves higher reward than TD-MPC2 without the need for online planning."
5. In Lines 348-349, the mean of 'm' and 'n' are not explicitly defined or mentioned.

### Questions
Please see the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper learns a differentiable multi-task world model from offline data, and then learns a policy using first-order optimization through the world model. They find that a well-regularized world model (they use SimNorm activation to normalize the latent vector) that prioritizes smoothness over correctness of the transition predictions is more effective for learning policies. They explain this phenomenon with two pedagogical examples, related to discontinuous contact dynamics and chaotic dynamics. They demonstrate improvement over TD-MPC2, a leading MBRL agent published at the previous ICLR, and in some cases over SHAC, an approach that relies on ground truth world model differentiation.

### Strengths
- Good baseline comparisons with impressive results for PWM. The comparison to a method that uses ground truth dynamics gradients (from the differentiable simulator) is valuable and compelling. 

- Good ablation experiments investigating sensitivity to the environment dynamics and the degree of world model regularization.

### Weaknesses
 - A diagram of the model and policy training would be helpful (i.e. more detailed than Figure 1). Perhaps specifically illustrating what is different about this vs. TD-MPC2. 

- I find Figure 2 confusing: What is the y-axis of the middle plot? What does a negative value mean? Is theta the angle (perhaps confusing because it is overloading the use of the theta symbol)? Additionally, I’m a little confused about how this example relates to a broader phenomenon of contact-induced discontinuities: the main problem here appears to be the long stretch of flat J, which causes the optimization to get stuck, as opposed to the fact that there is a non-differentiable discontinuity. Is it just a fluke of this toy scenario that the regularization helps? Why does SimNorm decrease the optimality gap? I’m a little ambivalent as to whether this example helps with understanding or just adds confusion, and on my initial read-throughs I didn’t find this “intuitive” example to be super intuitive, at least as-presented.

- Figure 6, MT80: is something wrong with this plot on the left? It look like PWM performs WAY worse, or am I misreading it? I am assuming this was a drafting error, but if it is not then it deserves more discussion.

- The use of V in Eqn 4 is confusing, because I don’t think it has any relation to Eqn 2 (or does it?)

- What are scenarios (if any) where this reduction in world model accuracy for the sake of smoothness could be problematic? I would appreciate a little more discussion. Perhaps for transfer between tasks that share dynamics but do not share any reward structure? Does the discrepancy between TDMPC2 and PWM on mw-stick-pull potentially point to this? 

- What might explain the reduced performance of PWM on the higher dimensional tasks, relative to SHAC (Figure 13)? Inaccuracies of the world model? If so, perhaps due to not having enough training data, or due to the regularization of the world model?

- Where does the dataset come from? Is a source algorithm such as PPO used to gather the data? How much do these results depend on that? Do the datasets have examples of successful performance on each task? Does data from the task for which a policy is extracted need to have been included in the initial world model training?

- Why can’t there be a comparison with DreamerV3 in a multi-task setting? In general, I am somewhat confused about how Dreamer, which I believe also uses first-order gradient optimization through a differentiable world model, relates to this work and would appreciate a little more discussion. 

- Is performance sensitive to the simnorm hyper parameters?


Minor: 
- Some initial confusions (that were eventually cleared up, but hung around in my head for a while): what does '10 minutes' refer to? Of gameplay? Computation? On one GPU? Is new data acquired per task or it is reusing the pre-trained offline data for each specific task?
- I had to look at the specific references to understand that the first sentence of the intro was talking about foundation models. It is an interesting comparison, and I like the point, but could perhaps be made a little bit more obvious.
- In discussing large-data approaches to multi-task performance, I wonder how this relates to SIMA from the paper ‘Scaling Instructable Agents Across Many Simulated Worlds’?
- Typo in caption of Fig 1 (‘prpose’)
- Typo line 188 (‘optimality hap’)
- Typo line 377 (‘generalizble’)

### Questions
1) Figure 6, MT80: is something wrong with this plot on the left? It look like PWM performs WAY worse, or am I misreading it? I am assuming this was a drafting error, but if it is not then it deserves more discussion.

2) The use of V in Eqn 4 is confusing, because I don’t think it has any relation to Eqn 2 (or does it?)

3) What are scenarios (if any) where this reduction in world model accuracy for the sake of smoothness could be problematic? I would appreciate a little more discussion. Perhaps for transfer between tasks that share dynamics but do not share any reward structure? Does the discrepancy between TDMPC2 and PWM on mw-stick-pull potentially point to this? 

4) What might explain the reduced performance of PWM on the higher dimensional tasks, relative to SHAC (Figure 13)? Inaccuracies of the world model? If so, perhaps due to not having enough training data, or due to the regularization of the world model?

5) Where does the dataset come from? Is a source algorithm such as PPO used to gather the data? How much do these results depend on that? Do the datasets have examples of successful performance on each task? Does data from the task for which a policy is extracted need to have been included in the initial world model training?

7) Why can’t there be a comparison with DreamerV3 in a multi-task setting? In general, I am somewhat confused about how Dreamer, which I believe also uses first-order gradient optimization through a differentiable world model, relates to this work and would appreciate a little more discussion. 

8) Is performance sensitive to the simnorm hyper parameters?


Minor: 
- Some initial confusions (that were eventually cleared up, but hung around in my head for a while): what does '10 minutes' refer to? Of gameplay? Computation? On one GPU? Is new data acquired per task or it is reusing the pre-trained offline data for each specific task?
- I had to look at the specific references to understand that the first sentence of the intro was talking about foundation models. It is an interesting comparison, and I like the point, but could perhaps be made a little bit more obvious.
- In discussing large-data approaches to multi-task performance, I wonder how this relates to SIMA from the paper ‘Scaling Instructable Agents Across Many Simulated Worlds’?
- Typo in caption of Fig 1 (‘prpose’)
- Typo line 188 (‘optimality hap’)
- Typo line 377 (‘generalizble’)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Policy learning with multi-task World Models (PWM) as a new model-based reinforcement learning algorithm. The main idea is to employ a pre-trained regularized and differentiable world model to simulate the environmental dynamics and then adopt first-order gradient methods to obtain the optimal policy efficiently. The author conducted experiments on both contact-rich single-task and large multi-task settings, showing that PWM had a better performance in learning high-reward policies and drastically improved the training time compared to previous methods. The author also provides additional examples and ablation studies to show the correlation between the accuracy of world models and the final performance, revealing that smoothness instead of accuracy is the key factor for higher rewards in gradient optimization.

### Strengths
1. The key idea of the paper is well delivered using pedagogical examples and is easy to follow

2. The results are highly reproducible with detailed experimental settings and code included, which also benefits the community for further study.

3. The experiments conducted in this paper are quite comprehensive and solid.

### Weaknesses
1. Typos and incorrect format
- Incorrect citing format in chapter 4.2: when the authors or the publication are included in the sentence, the citation should not be in parenthesis, please use \citet{} instead.
- Typos in Equation (2): it should be $\gamma^{h-t+1}$ instead of $\gamma^h$
- Typos in Algorithm 1: "$\nabla$" is omitted in all equations regarding learnable parameters update.
- Typos in Figure 10: missing ")" in the caption.

2. Lack of novelty
- The key idea of policy optimization via the pathwise derivative of a learned world model has already been proposed in MAAC[1], which is not included in the related works. The author should show the main differences between MAAC and the proposed PWM via analysis or experiments.

3. A total training time cost comparison between PWM and other algorithms is not revealed in the paper.

### Questions
1. Since there are no interactions between the target policy and the environment, could this method be considered as an offline policy learning method? If so, how would this method solve the distributional shift problem? For example, will the world overestimate the value of some state-action pairs not included in the dataset and result in poor performance?
2. As mentioned in weakness 2, what will you consider to be the major differences between your method and MAAC? 
3. I would like to know the comparison of the total training time (including world model training) of the PWM with other model-free methods like PPO and SAC.
4. How is "high-dimensional" defined in your work? For example, in Figure 4, "Hopper" is also considered a high-dimensional task. But according to the document (https://gymnasium.farama.org/environments/mujoco/hopper/), it only has an 11-dim observation space and a 3-dim action space.
5. According to Table 3 and Table 4, the PWM method shows much larger variances than model-free methods. What's the main reason for this and is it able to avoid the problem?
6. Some curves in Figure 13 are incomplete. What's the reason for that?

I am happy to increase my score if the authors justify these questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces PWM, proposing to use first-order gradient optimization for policy learning on top of offline pretrained world models. This method differs from zero-order optimization (MPPI) used in its base method TD-MPC2. Two didactic examples are presented to demonstrate that a well-regularized world model may be more useful for policy learning compared to real dynamics, confirming the well-known objective mismatch problem in the community. Main experimetns are conducted for single-task and multi-task learning, outperforming model-free baselines, zero-order method TD-MPC2, and method using real dynamics.

### Strengths
1. Didactic examples are informative.
2. Experiment results: sample efficiency to learn a task within 10 minutes seems promising.
3. The paper is well-written and easy to understand.

### Weaknesses
The major concerns are novelty and clarity of contributions. This paper does not well highlight its own contribution to the existing literature.

- The paper's contribution is conveyed (at least partially) on top of the fact that "world models methods often rely on inefficient gradient-free optimization methods for policy extraction." This holds for the TD-MPC series of work but is not valid for another series of popular methods, Dreamer. Actually, since DreamerV1, the policy learning process is done by first-order gradient optimization using the world model as a differentiable dynamics. The formulation of actor-critic learning in Equ (6-9) is almost the same as in the Dreamer series.
- Based on the above discussion, I believe the contribution of this work is additions to the following two problems: 1. objective mismatch in MBRL; 2. a multi-task RL with world models. However, contributions to this two aspect are also not groundbreaking. For the former, this problem has been well-known since Lambert et al. (2020), and for the latter, MBRL is also well-known for being beneficial for multi-tasking.

### Questions
Besides, there are several minor questions.

1. For the single-task setting, what's the difference between PWM and Dreamer (beyond implementation details)? Can PWM compare to DreamerV3 in the setting of Section 4.1?
2. In Line 298, do you mean world models are also finetuned with online interaction data? How about the multi-task setting? It seems the multi-task setting is fully offline.
3. In Figure 6 (left), why PWM significantly underperforms TD-MPC2?
4. In Line 357, does the baseline TD-MPC2 use the same hyperparameter as $H=16$?
5. Can the author explain why PWM benefits from smaller batch sizes?
6. Typo: Line 036 prpose => propose

Overall, I find this paper interesting and informative. If the authors address my concerns well, I am willing to raise my rating.

### Soundness
3

### Presentation
2

### Contribution
2
