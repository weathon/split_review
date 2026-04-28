# SENSEI: Semantic Exploration Guided by Foundation Models to Learn Versatile World Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
Exploring useful behavior is a keystone of reinforcement learning (RL). Intrinsic motivation attempts to decouple exploration from external, task-based rewards. However, existing approaches to intrinsic motivation that follow general principles such as information gain, mostly uncover low-level interactions. In contrast, children’s play suggests that they engage in meaningful high-level behavior by imitating or interacting with their caregivers. Recent work has focused on using foundation models to inject these semantic biases into exploration. However, these methods often rely on unrealistic assumptions, such as environments already embedded in language or access to high-level actions. To bridge this gap, we propose SEmaNtically Sensible ExploratIon (SENSEI), a framework to equip model- based RL agents with intrinsic motivation for semantically meaningful behavior. To do so, we distill an intrinsic reward signal of interestingness from Vision Language Model (VLM) annotations. The agent learns to predict and maximize these intrinsic rewards using a world model learned directly from intrinsic rewards, image observations, and low-level actions. We show that in both robotic and video game-like simulations SENSEI manages to discover a variety of meaningful behaviors. We believe SENSEI provides a general tool for integrating feedback from foundation models into autonomous agents, a crucial research direction, as openly available VLMs become more powerful.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents SENSEI, a model-based RL framework that guides agents' exploration by eliciting a human notion of "interestingness" from a vision-language model (VLM). The VLM annotates preferences between pairs of observations, gathered through self-supervised exploration. This annotated preference dataset is then used to train a reward model, SENSEI, which is subsequently distilled into the agent’s world model. The proposed approach demonstrates superior performance over baselines in experimental settings, including robotic and video game-like simulations.

While the paper introduces promising ideas, I believe it needs further development before it is ready for publication.

### Strengths
- Exploring how human priors can be integrated into RL agents using VLMs is a valuable research direction.
- The combination of intrinsic rewards derived from both VLMs and epistemic uncertainty effectively enhances performance.
- The graphical illustrations are clear and helpful, aiding readers in understanding the methodology and results.

### Weaknesses
 - The primary concern is the incorporation of a human notion of "interestingness" in the decision-making process. I believe environments where humans can clearly express preferences between observations based on interestingness are limited. For instance, in settings like the game of Go or simple mazes with few interactive objects, it can be challenging to determine what constitutes an "interesting" observation. The authors attempt to address this in the prompt design described in Appendix C.3, where they define "interestingness" for specific environments. However, defining “interestingness” specifically for each environment may limit the method’s ability to incorporate true human priors. In my opinion, the actual prompt the authors use is simply a more specified version of that used in [1], which prompts for the option “most likely to make progress towards the goal” or “most likely to show improvement with respect to the goal.” As a result, the distinction between this work and previous methods may be less substantial. To enhance originality and better substantiate the claims, I recommend refining the prompt design to more clearly elicit human priors from VLMs and including a thorough ablation study on different prompt choices.
- Additionally, I found the formulation unnecessarily complex. The VLM preferences are distilled twice, first into the reward model (SENSEI) and then into the world model. A more straightforward approach might be to incorporate the reward model directly into the world model to simplify the structure and better convey the core idea.

### Questions
- There is only one baseline in the main experiment. This paper could benefit from including more baselines to enable a more comprehensive comparative analysis.

### Soundness
2

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
4

### Summary
This paper proposes a way to combine VLM feedback and exploration bonuses. The main idea of this paper is to combine Plan2Explore, a latent ensemble disagreement-based exploration method, with a MOTIF-based intrinsic reward that tells the agent how interesting a state is. Specifically, SENSEI first trains a semantic reward model based on a dataset using MOTIF (w/ preference-based reward learning), and then runs Plan2Explore augmented with the learned semantic reward function. The authors also propose an additional mechanism to adaptively control the coefficients for the semantic and ensemble-based intrinsic rewards. They show that their method (SENSEI) outperforms Plan2Explore and VLM-MOTIF on MiniHack and Robodesk tasks.

### Strengths
* The proposed method is straightforward and reasonable.
* The authors empirically show that SENSEI improves exploration on both MiniHack and Robodesk, and the paper has some analysis results as well.
* The paper is generally well-written. In particular, I enjoyed reading Sections 1 and 2.

### Weaknesses
 * The method is largely a straightforward combination of two existing techniques: Plan2Explore and MOTIF. While I think this *alone* doesn't necessarily constitute a ground for rejection, I do think the results are not terribly surprising nor extremely insightful in the current form. It may have been more informative to practitioners if the authors had focused much more on ablation studies or analyses (beyond those in Appendix D). For example: Is MOTIF the only way to define a semantic reward model, and if so, how/why is it better than other alternatives? Is having two phases necessary (can we not have a separate pre-training stage)? Is the adaptive coefficient adjusting strategy (Eq. (7)) necessary? How sensitive is the performance to this strategy?
* The experimental results are somewhat limited. The authors only compare SENSEI to its ablations (P2X, VLM-MOTIF), and it is unclear how SENSEI performs compared to other types of exploration methods like LEXA/PEG, or VLM-based exploration methods like ELLM/OMNI/LAMP. I don't expect comparisons with all of these baselines, but I think it is important to have at least some comparisons with different types of previous methods in each category.
* The hyperparameter table in Appendix B implies that SENSEI is potentially sensitive to various hyperparameters. For example, it seems SENSEI requires careful, individual tuning of the quantile hyperparameter for each individual task in Robodesk (it uses 0.75, 0.75, 0.80, and 0.85 for each task). How were these values chosen, and did the authors perform the same level of hyperparameter tuning for the baselines as well? Did the authors decouple the runs for hyperparameter tuning and for the results (the results will otherwise be biased)? How sensitive is SENSEI to these individually tuned hyperparameters (quantile, batch size, learning rate, weight decay, etc.)?
* The authors use only 3 seeds for the experiments, which further makes it difficult to evaluate the empirical contributions of the method.

### Questions
Please answer the questions in the weaknesses section above. The paper is mostly clear, and I don't have any other specific clarification questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose SENSEI, a framework to equip model-based RL agents with intrinsic motivation for semantically meaningful behavior.
They distill an intrinsic reward signal of interestingness from VLM annotations, following MOTIF. The agent learns to predict and maximize these intrinsic rewards using a world model, using RL algorithms similar to Dreamerv3. They conduct experiments on both robotic and
video game-like simulations and achieve good results.

### Strengths
1. Good motivation and experiments. The authors explain their methods very clearly, and their experiments are diverse and convincing. Incorporating VLM into reinforcement learning is a hot topic, but this kind of integration sounds novel.

2. Various related work. The coverage of the huge amount of related work is about as thorough as possible.

3. Sufficient ablation study. The authors conduct several ablations to demonstrate the effectiveness of each component.

### Weaknesses
1. It seems that most components come from existing work. 

2. MOTIF uses much weaker VLMs, so it's possible that the performance gain mostly come from the improvement of VLMs. The authors could perform experiments to demonstrate the extent to which performance declines when using a less powerful model.

### Questions
1. The authors may briefly explain how long it will take to train SENSEI (dataset annotation, reward training and RL training) and the baselines using the same computation resources.

2. The authors emphasize a realistic setting. It would be much harder to create a 200K dataset of preferences if we want to deal with real world embodied agents. Have the authors tried to use a smaller dataset?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce SEmaNtically Sensible Exploration (SENSEI), a technique inspired by the previous work MOTIF, which uses Large-Language Models (LLMs) to express preferences between different observations in order to generate a reward model for a (model-free) reinforcement learning agent. The authors propose adapting this technique for Vision-Language Models (VLMs) and integrating it with world model learning. After an initial data collection phase, an "interestingness" reward model is distilled from the VLM’s preferences over image observations. This reward model is combined with the Recurrent State-Space Model (RSSM) of DreamerV3 and the ensemble technique used in Plan2Explore to develop an exploration policy that is influenced by the learned semantic reward. The results demonstrate that this combination of VLM-MOTIF and Plan2Explore leads to more effective exploration than relying on either technique alone. Additionally, downstream task experiments show that SENSEI outperforms baseline methods in terms of task performance.

### Strengths
- The extension of MOTIF to VLMs feels natural and improves the applicability of such techniques beyond environments with text representations.
- The paper does not solely rely on the semantic reward model but recognizes that epistemic uncertainty is important to consider. The authors analyse this and propose a well-motivated adaptive solution that combines the two sources of information to achieve more effective exploration. 
- The paper provides a solid empirical validation; the experiments are overall well-explained and detailed and show that SENSEI outperforms baseline approaches in terms of exploration quality and downstream task performance

### Weaknesses
 - The proposed method seems to rely on domain-specific prompt engineering. For instance, as shown in Appendix C3, in the Robodesk environment, the VLM is provided with detailed, manually crafted prompts specifying what constitutes "interesting" behavior. This significantly limits the generality and practicality of the proposed method. The prompts explicitly define the objects and interactions that are considered interesting, such as "the robot arm is near the blue box" or "the robot arm is grasping the red ball." This level of specificity means that the VLM is not truly inferring interestingness from the visual input alone, but rather relying on pre-programmed definitions, which would need to be re-engineered for each new environment.
-  The method heavily relies on the dataset collected through a self-supervised exploration technique, which is then used for annotation and reward model training. A key concern here is that the distilled reward model is inherently biased towards the specific data collected through this relatively simple exploration technique. This may not pose issues in small, simple environments but is likely to be fragile in more complex, large-scale environments. The reward model is static, meaning it cannot adapt to observations outside the distribution of the pre-collected dataset, limiting its ability to generalize to novel situations. For example, if the initial exploration phase does not encounter a specific object or interaction, the reward model will not be able to recognize it as interesting in subsequent phases, even if it is crucial for task completion. This lack of adaptability could lead to the agent getting stuck in local optima or failing to explore critical parts of the state space.
- In the Appendix, it is mentioned that the authors used 139409 pairs of observations for Robodesk. If I understand correctly, this means the VLM was prompted 139409 times to obtain the annotations for a single environment. If so, the practicality and scalability of the approach becomes slightly concerning. The cost of the experiments is not mentioned in the paper, but it is likely that querying VLMs this often could become computationally expensive, particularly in larger-scale environments. The computational cost of prompting a VLM for each pair of observations, especially for large datasets, is a significant practical limitation that needs to be addressed, as it might make the method infeasible for real-world applications.

### Questions
**Suggestions**
- Regarding the reliance on detailed prompt engineering, one potential resolution could be to lean more heavily on the prior knowledge and inference capabilities of the VLM. Instead of providing explicit descriptions of the environment, the VLM could be tasked with inferring the context from the visual observations. This would allow the model to deduce what constitutes interesting behavior without needing environment-specific prompts. While this might sacrifice some performance, it could provide a more general solution applicable across a variety of visual environments without manual prompt engineering for each domain.
- A suggestion regarding the concern about over-reliance on the initial pre-collected dataset in larger, more complex environments would be to consider introducing additional phases of data collection and retraining. After the initial exploration and training with the distilled reward model, the agent (using DreamerV3 + SENSEI) could collect new data during subsequent exploration, which could then be annotated and used to retrain a new reward model. Although this approach would still be biased by the initial dataset, I believe that this direction of research could progressively reduce the bias and help the model better adapt to novel observations.

**Minor comments / Questions**
- Line 146, small error 'In reward training phase'
- I would suggest omitting the parts from your section titles in Section 2, such as "UNLEASH YOUR SENSEI", as it does not fit the professional tone of the rest of the paper.
- At a high level, in your proposed exploration scheme, the agent is incentivized to first find interesting states and then switch to an uncertainty-maximizing approach. However, what is not completely clear to me is how or when it then switches back to $\beta_{Go}$ to continue finding new interesting states?
- In Figure 5, why is there no comparison with VLM-MOTIF, whereas in Figure 4, there is?
- In Figure 4, the SENSEI agent performs poorly in the "at chest with key" scenario compared to VLM-MOTIF. You mention that this is because "being at the chest with a key is an 'interesting' state, so there is no real incentive for the agent to explore what would happen if the chest was opened." However, intuitively, one might expect that an open chest would be considered even more interesting. Is there any further intuition as to why the VLM preferences do not guide the agent in exploring this further? Have you seen in annotations that if presented as a pair, the key+chest was rated more interesting than an open chest?

### Soundness
4

### Presentation
4

### Contribution
2
