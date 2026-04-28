# Autonomous agents from automatic reward modeling and planning

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Large language models (LLMs) have demonstrated remarkable capabilities across a range of text-generation tasks. However, LLMs still struggle with problems requiring multi-step decision-making and environmental feedback, such as online shopping, scientific reasoning, and mathematical problem-solving. Unlike pure text data, collecting large-scale decision-making data is challenging. Moreover, many powerful LLMs are only accessible through APIs, which hinders their fine-tuning for agent tasks due to cost and complexity. To address LLM agents' limitations, we propose a framework that can automatically learn a reward model from the environment without human annotations. This model can be used to evaluate the action trajectories of LLM agents and provide heuristics for task planning. Specifically, our approach involves employing one LLM-based agent to navigate an environment randomly, generating diverse action trajectories. Subsequently, a separate LLM is leveraged to assign a task intent and synthesize a negative response alongside the correct response for each trajectory. These triplets (task intent, positive response, and negative response) are then utilized as training data to optimize a reward model capable of scoring action trajectories. This reward model can be integrated with LLM-based agents and various planning algorithms to enhance task-solving performance. The effectiveness and generalizability of our framework are demonstrated through evaluations conducted on different agent benchmarks. In conclusion, our proposed framework represents a significant advancement in enhancing LLM agents' decision-making capabilities. By automating the learning of reward models, we overcome the challenges of data scarcity and API limitations, potentially revolutionizing the application of LLMs in complex and interactive environments. This research paves the way for more sophisticated AI agents capable of tackling a wide range of real-world problems requiring multi-step decision-making.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes ARMAP, a novel framework that enhances the task-solving abilities of large language model (LLM)-based agents in interactive, multi-step environments. The authors tackle key challenges associated with data scarcity and API restrictions, presenting a method that automates reward model learning from LLM agents’ interactions within an environment, thus eliminating the need for human annotations or commercial LLM-based evaluation. The reward model can then guide planning algorithms (e.g., Monte Carlo Tree Search and Reflexion) to improve LLM agents’ performance in tasks requiring iterative decision-making, such as e-commerce navigation and simple scientific experiments.

### Strengths
Innovative Reward Modeling Approach: The ARMAP framework leverages LLMs to generate diverse action trajectories, then synthesizes task goals and feedback to train a reward model. This automation of reward modeling is a strong innovation, addressing critical limitations in agent-based tasks by reducing reliance on costly and often proprietary data.

Framework Flexibility: The framework’s compatibility with multiple planning algorithms (MCTS, Reflexion, Best-of-N) demonstrates flexibility and potential for broader application. The performance boost across different LLMs (Llama, Phi, and Mistral) also underscores the generalizability of the ARMAP model.

Effectiveness in Customization: ARMAP’s ability to modify reward targets for controllable behavior generation (e.g., minimizing action length or cost) is a valuable capability for task-specific tuning, as demonstrated in the Webshop experiments.

### Weaknesses
Limited Scope of Tested Environments: Although the ARMAP framework was evaluated in multiple environments, these remain relatively constrained in task diversity (e.g., online shopping, elementary science tasks). Further exploration into environments with more complex multi-modal interactions or requiring intricate goal alignment would provide stronger evidence of the framework’s versatility. Specifically, the current environments do not fully test the agent's ability to handle complex state spaces, long-horizon planning, or noisy observations that are common in real-world scenarios. The reliance on relatively simple tasks may not reveal potential limitations of the reward model in more challenging settings.

Potential Overhead in Data Synthesis: While the automated reward modeling is valuable, the reliance on in-context LLMs for both task generation and trajectory synthesis could introduce computational overhead. It would be useful to discuss the cost-benefit analysis of this approach, particularly in environments requiring higher levels of interaction fidelity. The computational cost of generating diverse trajectories and training the reward model, especially with larger LLMs, should be analyzed more thoroughly, considering both time and resource consumption.

Dependence on LLM Quality: ARMAP’s effectiveness is inherently tied to the quality of the LLMs generating the synthetic data. While the framework was evaluated on open-source models, a more explicit discussion of performance across varying LLM qualities or limitations when using smaller LLMs would provide more insight into its applicability in resource-constrained scenarios. The sensitivity of the reward model to the quality of the generated trajectories and the potential for bias introduced by the LLM should be investigated further.

### Questions
Some suggestions for improvement:

Why do we need pairwise comparisons - this works in foundation model post-training, but why not use success/failure reward model training and using that as areward or value function?

Can you extend the experimental scope to include more diverse or high-stakes decision-making environments, such as ALFRED, BEHAVIOUR or HABITAT to illustrate ARMAP’s performance on tasks requiring more advanced capability.

Computational Efficiency Analysis: Including an analysis of the framework's data demands and comparisons with reward learning approaches would be beneficial, especially if extending the applicability of ARMAP to realistic low-resource settings.

Detailed Error Analysis: A more granular analysis of failure cases in each environment, particularly for tasks that involve complex dependencies or decision making, would provide deeper insights into the limitations of the current approach and inform possible improvements in reward modeling.

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
The paper proposes a framework named ARMAP, aimed at enhancing the task-solving capabilities of LLM-based agents in challenging environments that necessitate multi-step decision-making. While traditional LLMs perform well in text-based tasks, they face challenges with interactive, goal-oriented tasks due to limited access to large-scale decision-making data. ARMAP tackles these issues by developing an automated reward model that assesses action trajectories without requiring human annotations.

The framework comprises three main components:
1. Data Generation: An LLM agent interacts with the environment, producing diverse action trajectories that include both successful and unsuccessful task completion attempts. These trajectories, encompassing task intents, positive outcomes, and negative outcomes, are utilized to train the reward model.
2. Reward Model: A specialized model evaluates the effectiveness of each trajectory in fulfilling a task, thereby guiding the LLM agents in their planning.
3. Planning Algorithms: By integrating the reward model with planning methods like Monte Carlo Tree Search (MCTS) and Reflexion, the agent can optimize its actions to follow high-reward paths.

Experiments depict ARMAP’s efficacy across various benchmarks, demonstrating improved planning performance for different LLM agents. The approach offers advantages in flexibility and practicality, as it reduces reliance on human labels and expensive, closed LLMs, thereby facilitating the development of more autonomous and efficient AI agents capable of managing real-world tasks.

### Strengths
Automated Reward Modeling: It presents an innovative method for autonomously learning reward models without the need for human-annotated data, addressing issues related to data scarcity and dependence on costly closed-source LLMs. This makes the framework scalable and practical for real-world applications.

Enhanced Decision-Making for LLM Agents: By offering a reward-based evaluation system, ARMAP significantly boosts the ability of LLM agents to perform complex, multi-step tasks that require sequential planning, an area where standard LLMs often struggle.

Efficiency and Cost-Effectiveness: By eliminating the need to fine-tune LLMs and avoiding reliance on proprietary LLM APIs, ARMAP provides a cost-effective solution that could make high-performing AI agents more accessible for widespread use.

### Weaknesses
Limited Applicability in Highly Dynamic Environments: While the framework performs well in simulated environments with fixed rules, such as online shopping simulations and controlled benchmarks, its effectiveness in rapidly changing, unpredictable real-world environments is uncertain. The model may struggle with scenarios that require quick adaptation to new patterns not present in the training data.

Computational Overhead with Complex Planning: The integration of planning algorithms like MCTS, while effective, can introduce significant computational costs, especially when exploring multiple trajectories. This may limit ARMAP’s efficiency in resource-constrained settings or for tasks requiring real-time responses.

### Questions
Synthetic Data Quality: How do you ensure the quality and diversity of the synthetic trajectories generated by LLMs? Have you observed any limitations when these synthetic trajectories don’t align closely with real-world decision-making patterns?

Computational Cost in Real-Time Applications: Given the computational demands of planning algorithms like MCTS, how would ARMAP perform in applications requiring real-time decision-making? Are there strategies for reducing overhead while retaining performance?

Reward Model Generalization: How well does the reward model generalize to tasks and environments different from those it was trained on? Have you tested ARMAP in domains requiring more complex, domain-specific knowledge, such as legal or medical contexts?

Scalability and Practical Deployment: What are the main challenges you foresee in scaling ARMAP for broader deployment in real-world applications? Are there specific areas (e.g., hardware requirements, integration with other models) that need further development?

### Soundness
2

### Presentation
2

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
ARMAP presents a novel framework for autonomous agents by leveraging reward modeling and planning. It trains a reward model on contrastive trajectories, enabling effective decision-making in complex environments through LLM-as-agents. Unlike input-optimized prompting-based approaches, ARMAP scores steps within task trajectories, focusing on task completion. The ablation study supports the framework’s effectiveness and adaptability.

### Strengths
Originality: The automatic reward model and data generation approach presented is novel, allowing the framework to guide task completion within complex decision-making environments effectively.

Quality: ARMAP stands out by using a reward model to evaluate and guide navigation steps in agentic environments, enhancing decision-making processes and setting a solid foundation for handling intricate tasks autonomously.

Clarity: The paper is well-written, with a clear flow that effectively communicates the core concepts and approach. While a few notational details could be clarified, the overall presentation is strong and accessible.

Significance: The framework's value is demonstrated through LLM-agent task performance, highlighting flexibility in controllable task generation and practical application via a reward model, which reduces reliance on large LLMs or human labeling.

### Weaknesses
Specificity in Reward Model Design: The paper lacks detailed information on the size and neural architecture of the reward model. Specifically, the paper does not clarify the number of parameters, the layer configurations, or the activation functions used within the reward model. Additionally, challenges in reward model development are not clearly defined. More depth and specific examples are needed to clarify these choices and support the framework's claims. For instance, what specific difficulties were encountered when training the reward model, such as convergence issues, overfitting, or sensitivity to hyperparameter tuning? 

Limited Dataset Scope: The study could benefit from evaluating on a broader set of complex, long-trajectory decision-making agent datasets. Including established datasets such as AlfWorld or BabyAGI, which could strengthen the empirical evaluation and demonstrate robustness across diverse environments. The current evaluation is limited to a single environment, which raises questions about the generalizability of the proposed approach. 

Insufficient Detail on Multimodal and Visual Input Integration: While the paper mentions multimodal feedback and visual inputs, it lacks clarity of their impact on reward model training. The paper does not specify how visual information is encoded and processed by the reward model. An ablation study that isolates the effect of visual inputs compared to text-based inputs could better illustrate their importance and further validate the framework’s design. It is unclear if the visual inputs are simply concatenated with text embeddings or if a more sophisticated fusion method is employed.

### Questions
Although the automatic reward model training is a good idea, there are few concerns after going through the paper and demand clarity of choice:
1. Writing and Formatting:
    * In Figure 1, the title "Tree Planning" should use lowercase "(c)" instead of capital "(C)."
2. Reward Model Specifics:
    * Could authors clarify the size of the reward model used in this study?
    * In Line 100, authors mention challenges in developing a reward model (RM). Could they provide a few specific examples of these challenges for clarity?
    * What neural architecture was selected for the reward model in this framework? Is this inspired from any previous works?
3. Dataset Selection:
    * Some established decision-making agent datasets, such as AlfWorld, BabyAGI, or PDDL, are not included. These embodied agent datasets offer complex, long trajectories that could be valuable to the study. Could authors comment on their absence or suitability?
4. Multimodal Feedback:
    * Line 150 refers to multimodal feedback. Could you specify which modalities other than text were used in predicting the next action?
5. Reward Model Type:
    * In Line 161, you state a focus on developing the reward model. Is this a classification model with a defined set of output classes, or is it a regression model?
6. Observation Clarification:
    * In Line 225, the phrase “...corresponding environment observations...” could benefit from refinement, as there’s typically one extra observation at the start. Could this section be adjusted to clarify the distinction?
7. Trajectory Generation and Instruction Use:
    * In Figure 2, authors mention using “initial language instructions in the environment” to generate trajectories, but it’s unclear if any LLM was employed to identify keywords. For instance, in “I am looking for jeans with 40w x 34l size, and price lower than 200 dollars,” did the framework use LLM predictions to determine "Jeans" as the keyword for search?
8. Impact of Visual Inputs:
    * What role do visual inputs play in the reward model’s training? Have authors conducted any ablation studies that use only text from trajectories to measure their impact? It would be helpful to know if the visual inputs significantly influence the final model performance. I find this missing.

These points would enhance the clarity and depth of the paper, particularly around architectural choices and empirical coverage. I am looking forward to the rebuttal during the discussion phase.

### Soundness
4

### Presentation
3

### Contribution
3
