# COMBO: Compositional World Models for Embodied Multi-Agent Cooperation

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
In this paper, we investigate the problem of embodied multi-agent cooperation, where decentralized agents must cooperate given only partial egocentric views of the world. To effectively plan in this setting, in contrast to learning world dynamics in a single-agent scenario, we must simulate world dynamics conditioned on an arbitrary number of agents' actions given only partial egocentric visual observations of the world. To address this issue of partial observability, we first train generative models to estimate the overall world state given partial egocentric observations. To enable accurate simulation of multiple sets of actions on this world state, we then propose to learn a compositional world model for multi-agent cooperation by factorizing the naturally composable joint actions of multiple agents and compositionally generating the video. 
By leveraging this compositional world model, in combination with Vision Language Models to infer the actions of other agents, we can use a tree search procedure to integrate these modules and facilitate online cooperative planning.
To evaluate the efficacy of our methods, we create two challenging embodied multi-agent long-horizon cooperation tasks using the ThreeDWorld simulator and conduct experiments with 2-4 agents. The results show our compositional world model is effective and the framework enables the embodied agents to cooperate efficiently with different agents across various tasks and an arbitrary number of agents, showing the promising future of our proposed framework. More videos can be found at \url{https://vis-www.cs.umass.edu/combo/}.

  \keywords{ Multi-Agent Planning \and Compositional World Model \and Embodied Intelligence  \and Generative Models}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a compositional world model for multi-agent cooperation, leveraging large generative models and compositional diffusion models to build accurate simulations with an arbitrary number of agents. 

The authors present a novel framework called COMBO, which involves the following procedures:

1. **Estimate the Current World State**: Use a diffusion model to infer the state from partial egocentric observations.
2. **Action Proposal and Evaluation**: Employ a pretrained Vision-Language Model (VLM) to suggest actions, predict other agents’ intentions.
3. **Future Frame Generation**: Produce future frames based on the current world state image and a text prompt, representing joint actions of multiple agents. This is performed by the Compositional World Model, leveraging a compositional diffusion architecture.
4. **Evaluate and Plan**: Assess the predicted outcomes from the compositional world model using the VLM, and plan with a tree search algorithm based on these evaluations.

To assess their model, the authors test their approach on three datasets—TDW-Game, TDW-Cook, and 2D-FetchQ—and compare it to several baselines, including a VAE-based world model, MAPPO, CoELA, and LLaVA. The results demonstrate that the COMBO framework significantly outperforms these baselines, especially in planning capabilities.

### Strengths
**Novelty**. Suggested framework, named COMBO, offers a unique solution to the multi-agent planning problem by utilizing compositional world modeling for accurate simulation.

**Clear Framework Explanation.** The framework is presented clearly and is easy to follow. Each setting and procedure is understandable through Figure 3 and Algorithm 1. The roles of each module are well-explained in the text and formulation.

**Well-designed Experiments And Clarified Implications of Results.** The experimental setup and baseline choices effectively test the COMBO approach's capabilities. The results demonstrate impressive performance and highlight the necessity of the design choices in their architecture.

### Weaknesses
 **Lack of Figure Clarity and Interpretability.** The figures in the paper are unclear and difficult to interpret. Illustrations should enhance understanding, but these require reading the text to decipher them. For instance, Figure 1-(b) displays a random assortment of images without any labels. I believe this can be resolved by adding explicit labels for sequential processes that each frame means. Similarly, Figure 4 presents consecutive frames without explanations. Adding annotations, e.g. state, instruction, prediction t=1~3, would make the figures more informative.

**Limited Scalability and Impact.** Despite its impressive performance, the proposed model may struggle to scale in more realistic scenarios, such as handling low-level controls with continuous action spaces and operating without access to ground truth environmental labels during training. I believe that those compositional world modeling abilities seem reliant on structured inputs through prompts, which aren't typically available in realistic multi-agent cooperation setups.

### Questions
- Does the action prompt to CWM use a cropped image token along with text, as depicted in Figure 4, or is that just an illustration?
- As mentioned in the weaknesses, I have concerns about potential scalability. Can this be generalized to continuous action spaces, such as in robotics tasks? If so, it would be beneficial to include experiments on this. Additionally, I wonder if the CWM training setup will be applicable in realistic scenarios. In my opinion, we might only have access to egocentric observations and action history during training.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper propose to use compositional video diffusion model as "world model" for an environment with several agents cooperatively solving the task. In addition to learning scores for each agent independently, the diffusion model is trained only on regions reachable by an agent. Such model was used in COMBO agent that is effectively planning by fine-tuning VLM to propose reasonable action given current states while also fine-tuning VLM for intend prediction and for the evaluation of the current state.

### Strengths
- The problem of join cooperation of several agents is interesting, and the approach for world modeling by merging observations from different agents seems plausible. 

- Decomposition of the full state to regions that can be affected by each agent (while not correct in general e.g. turning on light would change the whole image, however it is a reasonable assumption that the overall scene in effected by agents mostly independently)

### Weaknesses
 - Scaling loss with the reachability assumes that reachability is provided externally, in real world agents "reachability" should be additionally estimated / discovered from the exploration data.  It would be great if the authors would cover better how to discover the reachability regions if they are not provided. Also, what about regions what are not reachable by any agent? In current formulation, it is not clear if those regions are modeled or not in the world model.  

 - Fine-tuning of VLM on the "collected short rollouts" potentially lead to agent that memories how other agents behave. While this approach can work, it would always require fine-tuning "intend prediction" if the agent is changing policy. It would be great if the authors can show that VLM can use some of the initial observations of the agent behaviors to adapt its predictions  on the fly (e.g. with in context learning). 

- In both of the TDW-Game and TDW-Cook performance is saturated learning to agents that perform near (and in case of the TDW-Cook somehow better 22.8 vs 24.0) than Oracle Cooperator. Thus, it would be great if authors can increase the difficulty of those tasks and show possible failure cases of their approach. For example, currently world model assumes that visual information and actions is enough to predict the next state. However, for in closer to real world scenarios some parameters are hidden (e.g. objects mass) and thus effective world model would need to deal successfully with estimation of such parameters and using them for the determining of the optimal actions.

### Questions
- Please describe in more details on what data intend and outcome evaluation was fine-tune on? How realistic collection of such data for real-world agents?  

- Potentially more details could be provided on modification of 2D FetchQ environment, as I didn't find any in the appendix. 

- Why Co-Gaild baseline is used in this task but not used on the original environments? 

- Is usage or fine-tuning of VLM really necessary for these tasks? If so, does this fine-tuning leads to generalizable action generation /agents intends? For example, how robust agents would follow recipes if some ingredients are not seen in the training? Without studying and showing such generalizations, it is not clear why LLM are needed and if more simple supervised models would do the same job.  

- Some formulas could be better connected. E.g in section 4 X is used for world model state, while in 5 s is used.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors of this paper explored a compositional workload model for embodied multi-agent cooperation. Unlike previous approaches to embodied multi-agent cooperation, they introduced an explicit world model that simulates the next state by incorporating the estimated actions from the Intent Tracker along with the agent's actions. This model stands out from other single-agent, model-based reinforcement learning approaches by explicitly accounting for multi-agent cooperation dynamics. Utilizing this world model, they implemented a tree search planning strategy similar to Monte-Carlo Tree Search [1]. Their approach demonstrated superior performance in embodied multi-agent cooperation tasks and, due to the compositional nature of their model, exhibited strong generalization capabilities.

[1] Silver, David, et al. "Mastering the game of Go with deep neural networks and tree search." nature 529.7587 (2016): 484-489.

### Strengths
- They designed explicit compositional world model. It is one of the most distinguishable designs in their modeling, which supports the look ahead planning (tree search planning), and they showed it is beneficial through the empirical evaluation results. As a part of this, the world state estimation is good to build the world model for multi-agent setting.
- It is a well written paper. I can easily follow their discussions without unnecessary questions.

### Weaknesses
 - The room of the evaluated benchmarks is too small to show the effectiveness of their proposed modeling. In Table 1, COMBO outperformed previous works. Although, when comparing with LLaVA, it shows comparable success rate except TDW-Cook Cooperator 1 setting. Their efficiency on solving the tasks is clearly better than LLaVA, but we felt it is not good enough to evaluate the effectiveness of their modeling.
- The generalization performance evaluation is too weak to show that in lines 521-524 and Table 5. They trained the model with 4 agents and applying it to 3 agent only, then what happens if we test with 2 or much more agents such as 10? Additionally, COMBO is more efficient than LLaVA, but LLaVA also showed good success rates for 3 agents setting. The LLaVA is trained on the 3 agents setting? If yes, it should be mentioned in the caption of the figure or the paragraph. If no, then we think this empirical evidence is weak to show the generalizationality of the COMBO.

### Questions
- In Figure 1, what means the surrounding figures? Maybe we guess it is to visualize the look ahead planning, but I am not sure it is a good visualization for showing that.

### Soundness
3

### Presentation
3

### Contribution
3
