# YOLO-MARL: You Only LLM Once for Multi-agent Reinforcement Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
\vspace{-10pt}
Advancements in deep multi-agent reinforcement learning (MARL) have positioned it as a promising approach for decision-making in cooperative games. However, it still remains challenging for MARL agents to learn cooperative strategies for some game environments. Recently, large language models (LLMs) have demonstrated emergent reasoning capabilities, making them promising candidates for enhancing coordination among the agents. However, due to the model size of LLMs, it can be expensive to frequently infer LLMs for actions that agents can take. In this work, we propose You Only LLM Once for MARL (YOLO-MARL), a novel framework that leverages the high-level task planning capabilities of LLMs to improve the policy learning process of multi-agents in cooperative games. Notably, for each game environment, YOLO-MARL only requires one time interaction with LLMs in the proposed strategy generation, state interpretation and planning function generation modules,  before the MARL policy training process. This avoids the ongoing costs and computational time associated with frequent LLMs API calls during training. Moreover, the trained decentralized normal-sized neural network-based policies operate independently of the LLM. We evaluate our method across three different environments and demonstrate that YOLO-MARL outperforms traditional MARL algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a framework that utilizes Large Language Models (LLMs) to facilitate MARL collaboration. By leveraging LLMs for task planning and assigning different tasks to underlying agents, the framework influences policy learning through additional rewards, aiming to accelerate MARL algorithm learning.

### Strengths
I believe that using LLMs to enhance collaboration in MARL is a highly promising direction.

### Weaknesses
- The methodology throughout the paper doesn’t feel novel to me; I’ve seen several similar studies, and the quality of this paper doesn’t seem satisfactory.
- None of the result figures appear to be processed; it looks as though they were directly downloaded from WANDB. Some figures show results from only one run, lacking statistical significance. I believe at least five runs should be conducted for each result.
- Certain detailed introductions seem unnecessary, such as STATE INTERPRETATION, while others, like PLANNING FUNCTION GENERATION, are not sufficiently elaborated.
- The improvements in experimental results are somewhat expected. However, for slightly more challenging tasks, such as those in SMAC (although the tasks provided are relatively easy), there is no significant performance improvement observed.

### Questions
- Could you clarify if the inquiry occurs only once at the beginning of the game?
- Could you provide experimental results on more challenging tasks?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces "You Only LLM Once for MARL" (YOLO-MARL), a novel framework that integrates large language models (LLMs) with multi-agent reinforcement learning (MARL) to enhance policy learning in cooperative game environments. The core innovation of YOLO-MARL lies in its one-time interaction with LLMs per game environment, which significantly reduces computational costs and avoids the inefficiencies associated with frequent LLM invocations. The framework utilizes LLMs to generate strategy plans, interpret states, and create planning functions that guide the MARL agents. The approach is tested across various game environments, showing improved performance over traditional MARL algorithms.

### Strengths
(1) The use of LLMs in MARL to reduce the frequency of model calls is relatively novel. The one-time interaction strategy for each environment, minimizing computational overhead while leveraging LLM's capability, is an innovative approach.
Addressing the computational inefficiency in MARL through LLMs is of high relevance, especially given the increasing complexity and scale of multi-agent systems. The potential application across different domains enhances the paper's impact.

(2) The experimental setup is robust, employing several environments to validate the effectiveness of YOLO-MARL against established MARL benchmarks.

(3) The paper is well-organized, with clear descriptions of the methodology, experiments, and results. The inclusion of figures, tables, and appendices aids in understanding the proposed framework.

### Weaknesses
 (1) **The necessity of using MARL settings as opposed to single-agent RL isn't convincingly justified. The claim of innovation specifically in the MARL domain seems overstretched without substantial differentiation from potential single-agent applications.**

(2) The paper fails to discuss several relevant studies that also integrate LLMs with multi-agent systems, which could question the novelty and depth of the literature review. Notably, it omits significant recent works, which could provide crucial context and comparison.

For example:

[1] Hu, Sihao, et al. "A survey on large language model-based game agents." arXiv preprint arXiv:2404.02039 (2024).
multi-agent Cooperation and Communication games:

[2] Gong, Ran, et al. "Mindagent: Emergent gaming interaction." arXiv preprint arXiv:2309.09971 (2023).

[3] Wu, Shuang, et al. "Enhance reasoning for large language models in the game werewolf." arXiv preprint arXiv:2402.02330 (2024).

[4] Zhang, Hongxin, et al. "Building cooperative embodied agents modularly with large language models." arXiv preprint arXiv:2307.02485 (2023).

(3) While the experiments demonstrate faster convergence with YOLO-MARL, the longevity and stability of training are not addressed. More extensive training or delayed results could provide deeper insights into the effectiveness and robustness of the proposed method.

(4) The reliance on human expert and LLM-generated planning functions could limit the applicability in strategic or domain-specific scenarios. The adaptability and accuracy of these functions in complex environments like Go or Dota2 are not discussed.

### Questions
(1) Can the authors clarify why MARL is specifically required for the YOLO-MARL framework? Would similar benefits not be realized in single-agent settings?

(2) It is recommended to include and discuss additional related works. How does YOLO-MARL compare with these approaches, especially concerning reward assignment and policy generation in multi-agent contexts?

(3) Could the authors extend their experiments to show long-term training results? It seems that the YOLO-MARL help faster convergence rather than higher performance, especifically in SMAC. Could the authors show longer training results in MPE and LBF environments?

(4) Additionally, testing in environments with higher strategic depth might validate the framework's utility in more complex scenarios.
How does the dependence on pre-trained LLMs affect the generalizability and reliability of the planning functions, especially in domain-specific environments, e.g., chess? The current experimental environments rely on the general pre-training of the LLM to generate a reasonably effective strategy, which while facilitating MARL convergence, might limit the method's upper potential.

(5) **In my view, using human experience-based "State Interpretation" to prompt the LLM, which then generates a base strategy "Planning Function" for RL, seems to be a straightforward application of LLMs in MARL.** This approach does leverage human-like reasoning for initial strategy formulation but might not fully exploit the potential complexities and capabilities of LLMs in dynamic or highly strategic game settings.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel framework (YOLO-MARL) to enhance MARL by integrating LLMs for high-level task planning in cooperative game environments. The motivation is to minimize computational demands by using only a single LLM interaction per game. YOLO-MARL includes four modules - Strategy Generation, State Interpretation, Planning Function Generation, and MARL Training. Experiments were conducted in useful benchmarks like Level-Based Foraging, MPE, and SMAC, with ablation studies to identify the role of some of the components of the proposed approach.

### Strengths
- The proposed idea is new, interesting, and well-motivated. 
- The paper is easy to read and follow. 
- Ample supplementary material containing examples and code helps in better understanding the proposed approach.

### Weaknesses
 - Some more experiments and analysis/explanations may be required. 
- See questions.

- Does table 1 refer to the same results in Figure 2? Can you mention the standard deviations in the table too? I see a high overlap in them for some results, which raises a concern about the quantifiable impact that using LLMs is making in the proposed approach. 
- Can you consider training Qmix on LBF for longer (about 10M)? This would help observe/compare the performances till/after convergences. Both approaches still seem to not have converged yet. 
- How many independent trials were done for experiments in Section 6? 
- About experiments on smac, can you give more details on the planning function generation using LLMs in this environment, as the actions here are complicated when compared to MPE. Also, the results on smac are almost overlapping. So, does this suggest that we may not need YOLO-MARL on smac maps? Did you also run qmix and YOLO-MARL+Qmix on smac maps? Also, did you consider smacv2? Any comment on why or why not? 
- For experiments on reward generation in your approach, does the LLM generate a reward function? When does the LLM generate it? Before training (just like the strategy and planning function generation)? I am also unsure of more details on how this reward was generated. 
- In Figure 2, any comment on the dip in performance of MADDPG (and YOLO-MARL + MADDPG) around 450K episodes? 
- Referring to Figures 3 and 4, do you think the scalability of the proposed approach is a concern? The results almost start overlapping on increasing the number of agents in MPE. 
- Minor: Can you label the axes in figures.

### Questions
- Does table 1 refer to the same results in Figure 2? Can you mention the standard deviations in the table too? I see a high overlap in them for some results, which raises a concern about the quantifiable impact that using LLMs is making in the proposed approach. 
- Can you consider training Qmix on LBF for longer (about 10M)? This would help observe/compare the performances till/after convergences. Both approaches still seem to not have converged yet. 
- How many independent trials were done for experiments in Section 6? 
- About experiments on smac, can you give more details on the planning function generation using LLMs in this environment, as the actions here are complicated when compared to MPE. Also, the results on smac are almost overlapping. So, does this suggest that we may not need YOLO-MARL on smac maps? Did you also run qmix and YOLO-MARL+Qmix on smac maps? Also, did you consider smacv2? Any comment on why or why not? 
- For experiments on reward generation in your approach, does the LLM generate a reward function? When does the LLM generate it? Before training (just like the strategy and planning function generation)? I am also unsure of more details on how this reward was generated. 
- In Figure 2, any comment on the dip in performance of MADDPG (and YOLO-MARL + MADDPG) around 450K episodes? 
- Referring to Figures 3 and 4, do you think the scalability of the proposed approach is a concern? The results almost start overlapping on increasing the number of agents in MPE. 
- Minor: Can you label the axes in figures.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes to use LLMs to assist in the training of multiagent Reinforcement Learning tasks, by letting the LLM generate Strategy and Planning functions, those functions are used to modify the MDP for better training.

### Strengths
- Contemporary paper proposing to use LLMs to better design the MDP description.
- LLM-guided multiagent RL is a novel subject
- Authors were considerate about the explosive computational cots of using the LLM at every step the agents would take and thus engineered functions in a way that the LLM would need to be queried only once for the environment design.

### Weaknesses
 - The main issue I see is that, although the LLM is used to assist in the design of the MDP description, a great deal of domain knowledge is still required of the designer. Put together, the work to format the environment description for the strategy generation and state interpretation steps is on par or even harder than more classical approaches of performing feature engineering such as OO-MDPs or simply  dedicating a good effort into modeling the task well. 

- While the experimental results show significantly better results for the proposed approach, I feel it's an unfair comparison due to the significant effort required to describe well the environment to the LLM. The main argument in favor of the approach is that it required less coding when compared to classical feature engineering, but overall the same mental exercise would be needed not to mention the additional costs associated to using the LLM.

- My suggestion to make the approach more general and impactful is to instead use a multi-modal foundation model to handcraft some fixed prompts (that would be general for any environment) to analyze the environment autonomously through raw observations (such as images). That way, the approach would require significantly less effort from the designer and would make the approach more impactful.

- For the reasons above, in my opinion the paper does not reach the impact level of a main track ICLR paper.

- minor: I would name the approach in another way given there is already a widely famous YOLO model

### Questions
no specific question.

### Soundness
3

### Presentation
2

### Contribution
2
