# Towards Efficient and Scalable Multi-agent Reasoning via Bayesian Nash Equilibrium

- Decision: Reject
- Scores: 6, 3, 5, 8

## Abstract
Large Language Models (LLMs) have achieved significant success in tasks such as natural language understanding, generation, and reasoning, driving advancements in machine translation, summarization, and question-answering systems. Particularly in multi-step reasoning tasks, LLMs demonstrate robust logical reasoning capabilities. To further enhance the reasoning abilities of LLMs, researchers have developed methods that generate intermediate reasoning steps, thereby improving performance in solving complex problems. However, these approaches primarily focus on single LLMs, limiting the diversity and creativity of the reasoning process. Inspired by psychological studies, there is a growing interest in exploring multi-LLM frameworks to boost model performance through collaborative reasoning. Existing multi-agent debate frameworks can enhance answer accuracy through dialogue and argumentation but suffer from high computational costs and lack theoretical guarantees for convergence. To address these challenges, we propose a novel method—BNE-Q. This method integrates belief networks and a central network within the Decentralized Partially Observable Markov Decision Process (DEC-POMDP) framework to achieve a Bayesian Nash Equilibrium (BNE). During the inference phase, the central LLM provides step-by-step strategies and format guidelines, while execution LLMs independently generate answers based on these guidelines. The central LLM then consolidates the answers to form a commitment. In the optimization phase, by calculating the cosine similarity between the answers and the commitment, we optimize the execution LLMs' belief networks to achieve stable convergence of the multi-agent system. Our method not only reduces the computational overhead compared to traditional multi-agent debate methods but also ensures convergence through theoretical analysis. Experimental results demonstrate that BNE-Q performs exceptionally well across six benchmark tests, including complex reasoning and planning tasks, validating its theoretical robustness and practical effectiveness. Our work provides a new approach for developing multi-LLM collaborative reasoning frameworks, significantly enhancing reasoning capabilities in large-scale multi-agent environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes EcoNash, a hierarchical reinforcement learning framework for scalable, multi-agent reasoning by using Bayesian Nash Equilibrium (BNE) to enhance coordination among large language models (LLMs). This paper first proposes a tight bound for MA-LLM's performance improvement. Then introduce EcoNash, which reduces the communication and computational costs typical in multi-agent systems by enabling LLMs to independently generate optimal responses based on their own beliefs. Experimental results show EcoNash surpasses single and multi-agent models in complex reasoning tasks and proves to be effective at scaling with increased model ensemble sizes.

### Strengths
1. The introduction is organized and well-written.
2. The experiments are comprehensive, including multiple baselines and different sizes of LMs.
3. The empirical results demonstrate the superiority of the proposed method against the baselines.
4. The method can be scaled by increasing the number of Agents and improving performance.

### Weaknesses
1. I don't see a strong connection between Sec 3.2 and the following method
2. Fig 1 should be clearer.
3. Lack of information about the model structure of the belief encoders and hyperparameters of optimizing them.
4. Since the proposed method needs to tune a Q function, the author should include a baseline with a learned action-value function, e.g. [1][2]
5. In Table 4, the author may also show the performance w.r.t. the token consumption.

### Questions
1. Line 196, why differences of Q-values can be bound by separating estimation errors and policy suboptimality? There should be some references.
2. Appendix A.3 should be named 'Assumptions' instead of 'PROOF OF PROPOSITION', and several references are recommended here. It's the most direct way to show that these are standard assumptions. 
3. What does assumption 3 mean in Appendix A.3?
4. Equation 1, how to update target Q network weight? Is the Q target value missing an input of belief?
5. Will the Coordinator LM and the Executor LM be tuned?
6. What's the computation cost of tuning the Belief Encoders and Coordinator LM? 
7. For each task/dataset and each LLM, a new group Belief Encoder and Q values will be trained. Is that correct or wrong?


## Reference
[1] Feng, Xidong, et al. "Alphazero-like tree-search can guide large language model decoding and training." arXiv preprint arXiv:2309.17179 (2023).

[2] Liu, Jiacheng, et al. "Don't throw away your value model! Generating more preferable text with Value-Guided Monte-Carlo Tree Search decoding." First Conference on Language Modeling. 2024.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a way to optimize multi-agent LLM systems for Bayesian Nash Equilibrium (BNE). It showed strong results against other popular benchmark methods. Even though the paper is very well-written, I have to reserve my recommendation for acceptance until some confusion is cleared up.

### Strengths
1. The paper is written very well. The structure and organization are both very clear.
2. The paper uses actual game theory objectives to ground multi-agent debate optimization. This effort is very applaudable.

### Weaknesses
1. Currently, the paper lacks quite a few key details to properly understand the work.
2. Training details are almost completely missing.
3. The provided code (through a URL) is very minimal/barebone. It includes data files and code for Game of 24 -- which is not even reported in the actual paper. 
4. The comparison is between EcoNash (a method that involves fine-tuning the model) and other methods (RAP, ToT, rStar, etc.) -- essentially comparing a fine-tuned model with prompting methods. The higher performance is not entirely surprising.
5. It might be cool to see if fine-tuning, according to Nash equilibria, leads agents to develop distinct "personas" or emergent differentiations.

### Questions
1. What is the hardware spec for fine-tuning the LLaMA3.1-405B model? If it is hard to estimate or proprietary, please express that clearly in the paper. Similarly, please report the time spent running the training loop. Early stopping is mentioned but no hyperparameter is reported (how many epochs did you train, what's the exact criteria)? If you used an API for fine-tuning, that is totally fine too -- please report which company's API you used (it seems like Together's API?), and can you report the cost (a rough number is ok)? 
2. Glicksberg's Fixed Point Theorem [1] seems to be used to prove the min-max value for zero-sum games. I believe in your framework, it's a cooperative game? Does this theorem still apply? Please point me to some textbook/tutorial/paper that uses this theorem to prove convergence for Bayesian Nash Equilibrium.
3. Is the proof for the payoff function to be continuous w.r.t. $\theta$ valid? This might be my misunderstanding -- but in Sec 3.3.2. Reward Setting: you use a lot of different rewards, including correctness, which we know is 0/1 for many of the questions.


[1] https://en.wikipedia.org/wiki/Glicksberg%27s_theorem


-------------------------------------- 

Additional questions and concerns:

I am concerned the authors are not acting in good faith. For example, if you look at the draft, Table 8 just says "Hyperparameters of EcoNash", but the author's follow up response to me explained this is only a `a representative example for the GSM8K task with LLaMA 3.1 70B`. So why is this not clearly stated in the paper draft when they added the table? 

> Through this process, the learned embeddings guide the executor LLMs to generate responses that are more consistent and coordinated, enabling improved overall performance.

> For inference, we used the Together API. Regarding performance validation on a math dataset using LLaMA 3.1 405B, the approximate cost was $75.

These two parts combined are very confusing. How are embeddings sent to executor LLMs to guide their response generation? TogetherAPI does not seem to support taking in embedding (it only supports returning embeddings). Can the authors at least explain this? Is it possible for the authors to show which part of TogetherAPI did they use to send in embeddings that guide the Executor LLM to generate responses?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes EcoNash, a multi-agent framework geared towards achieving Bayesian Nash equilibrium, which has a sublinear regret instead of linear regret in the regular multi-agent debate setup. The method consists of a coordinator LLM that tells a question-specific strategy to each executor LLM and the executor LLM that acts as the solver and executes the strategy based on its internal state using the agent-specific belief network. The beliefs from all the agents are relayed into the coordinator LLM via embeddings from the belief encoder which then aggregates and commits. The networks are trained using gradient descent with TD and SD loss. Empirically, the authors show that 4 different LLMs (of different sizes and families), EcoNash outperforms various prompting based baselines: CoT, SC, multi-agent debate and also uses fewer tokens (more efficient or low latency).

### Strengths
* Multi-agent techniques are a popular and effective method for improving the reasoning performance of LLMs, however, they are computationally expensive. So the paper addresses a problem on an important topic and their better regret bounds and token efficiency results are compelling.
* The BNE take on multi-agent conversations are relatively novel to this domain, and is conceptually intriguing -- could be useful for the ICLR community
* The empirical results over prompting baselines give good improvement on multiple datasets and models

### Weaknesses
 * The authors can present the paper's content more clearly and make it easier to follow. I found a lot of crucial details not adequately explained in theoretical results, experimental setup and training, and general examples/intuition that would make the paper more appealing to the multi-agent reasoning community. See questions below (1-6, 8)
* I have major questions or doubts about the assumptions made in the theoretical results, which are mostly delegated to the appendix. Overall this section was tough to follow and missed necessary background and intuition needed for it to be beneficial for LLM reasoning community. See questions below (7, 11)
* The paper does not clearly explain their experimental setup, which involves training, and in its current form, it would be hard for any reader to be able to have a working implementation of their method (also brings up reproducibility concern). It also raises doubts about if the baseline comparisons are fair or adequate (no training baselines), and the ablations and analysis for why the method works appear to be insufficient (see questions: 8-10, 12-15).

PS: I would be open to revisiting the scores if the authors add some of these missing details and simplify the explanations and content presentation of the paper. In the current form, I don't think the content is clear and coherent for the community at large to benefit from it.

### Questions
1.  3.1.1: What is a type function?
2.  Problem with the notation: shouldn’t tuple of $\theta$ s and actions be ordered, so $\theta_i$ and $\theta_{-i}$ does not account for the orderings, the authors should clarify that.

3. Appendix A.3: H is entropy and I is mutual information – if so it should be stated or defined?
4.  Also roles coordinator and executor LLMs should be defined in the method before referring to this proof, i.e., somewhere in 3.1 possibly the “implementation” part of 3.1.1 as the title suggests?
5. Broader point on Sec 3: for it to be useful for researchers in LLM agents, it is important to build the intuition for what coordinator LLMs inputs and especially outputs are (question and strategy) and should be stated at the start of Sec 3. While some of these examples and prompts are referred to in Sec 4 (mainly in the appendix), it would be useful to introduce these earlier on, or add an example in the figure, or possibly moved to the main paper.

6. Figure 1: need to label the belief network – blue box?
7. Lemma 1: How do you get the bound for estimation and policy suboptimality errors as $(\sqrt{t})^{-1}$? This is the assumption that proof in Appendix B.2 hinges on and is not explained in the appendix either. Similarly, why did the authors set the value of $\delta_t$ to a constant max in B.3.

8. Figure 1 and Sec 3.3.1: Can the authors share more details on “informative strategy and a format based
on the input question q” that the Coordinator LLM generates? 
9.  Missing Training details/experimental setup of the belief encoding and network, number of parameters, what learning rate and hyperparameters were used, how were they tuned? What is the training dataset?

10. All the baselines are solely prompting-based, but their method trains the belief network and encoding. Can you compare it to directly finetuning the LLM with LoRA with minimal parameters or prefix tuning or soft-prompt optimization which may be more similar to what the authors do?

11. Issue with the prompts in appendix C and computing rewards using prompts: use llm-as-a-judge capabilities to assess model responses for reasoning which is already something models are bad at [Huang et al. 2024](https://arxiv.org/abs/2310.01798) Requires models to stick to token counts which models are bad at [Yuan et al. 2024](https://arxiv.org/abs/2406.17744), so do the authors use a cutoff or in-context examples?
      * To measure the soundness and relevance of these reward scores,what it you sampled the scores with high temperature, added noise or replaced it with random rewards – how does the performance change in these scenarios?
      * Most strategy suggestions from the coordinator can be seen as a plan and then asking the executors to solve it. This is similar to works such as [Plan and Solve](https://arxiv.org/abs/2305.04091), [Adapt](https://arxiv.org/abs/2311.05772), etc., but how faithful are the executors to the plan as pointed out in [Lyu et al. 2023](https://arxiv.org/abs/2301.13379). How do we know that most improvements are not coming from additional diversity (missing factor in homogeneous LLM agent settings) from sampling multiple plans that the coordinator sends to different LLMs. To simulate this, authors could run self-consistency with "plan and solve" instead of just solutions.
      * Does assumption 2 (posterior alignment) in Appendix A.3 imply executor LLM is faithful to the plan/strategy generated by coordinator LLM? If so that may not always occur since CoT and math responses in zero-shot generative settings are not known to be faithful. Eg. the model can say it solving for 2x - 6 + 2 = 0 but say that it solves x=3 (instead of x=2).
     * In general, it is unclear how simply prompting the LLM guarantees the assumptions in A.3 are met.

12. Dataset metrics for travelplanner in Sec 4.2 need to be explained. 

13. Minor: Figures 2 and 3 are never referred to in text, which makes it harder to read the relevant sections

14. Instead of using LLM as a judge to output the reward, something models are shown not to be good at why not use an external RM from the reward bench? Also if you already have scores for different executors that give answers, why not do weighted SC, or best-of-N based on reward or an ensemble?
15. In sec 4.3, when comparing the token counts, the SC numbers look quite high. Is there an explanation for this? Usually SC is done using temperature sampling (so input is provided ones, and k outputs are sampled). Are counting the input tokens 64 times too and is that the reason for the high token counts?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes the EcoNash framework, a new solution designed for efficient and scalable coordination in multi-agent systems utilizing Large Language Models (LLMs). The framework leverages Bayesian Nash Equilibrium (BNE) to optimize multi-agent interactions while minimizing communication overhead. By combining global and local coordinators and clustering LLM agents, EcoNash achieves effective coordination with reduced computational costs.

The paper introduces a detailed theoretical analysis, including a convergence guarantee and a Bayesian regret bound, demonstrating the efficiency and stability of the proposed approach. EcoNash’s hierarchical structure enables it to achieve sublinear regret, significantly improving learning and convergence rates compared to existing multi-agent debate methods.

Experimental results across multiple benchmarks show that EcoNash outperforms both single-agent and traditional multi-agent methods, achieving improved scalability and efficiency. The framework contributes to advancing multi-agent reasoning, particularly in large-scale deployments where resource constraints and scalability are critical considerations.

EcoNash’s hierarchical coordination and emphasis on distributed reasoning allow agents to achieve Bayesian Nash Equilibrium independently, which is theoretically well-founded and empirically validated. Overall, the paper is well-written, methodologically sound, and experimentally thorough. I recommend it for acceptance.

### Strengths
This paper introduces EcoNash, a novel multi-agent reasoning framework that combines hierarchical coordination with Bayesian Nash Equilibrium (BNE) principles to enhance the scalability and efficiency of large language models (LLMs) in multi-agent systems. The EcoNash framework reduces computational costs and minimizes the need for extensive inter-agent communication, which addresses common challenges in multi-agent LLM frameworks. By leveraging distributed reasoning and theoretically proving convergence with BNE, the authors provide a framework that is both theoretically sound and empirically validated.

The paper is well-written, methodologically sound, and experimentally thorough. The experiments on benchmark datasets convincingly demonstrate the framework’s scalability and efficiency, while the theoretical analysis provides a solid foundation for the proposed coordination mechanism. I recommend the paper for acceptance.

### Weaknesses
While the paper presents a valuable contribution, a few areas could be enhanced to fully realize its goals:

1. **Scalability of Coordination Mechanism**: EcoNash leverages a central Coordinator LLM to achieve distributed reasoning among Execution LLMs, yet the scalability of this coordination mechanism as agent numbers grow is unclear. Since scalability is a primary aim, it would be useful to explore alternative coordination structures (e.g., decentralized or multi-coordinator configurations) that could mitigate potential bottlenecks from a single coordinator, especially in large agent systems. Specifically, the paper does not address the computational complexity of the coordinator as the number of agents increases, nor does it discuss the potential for communication bottlenecks as the coordinator must process and distribute information to an increasing number of execution LLMs. The paper should explore the practical limitations of this centralized approach and propose solutions for very large-scale deployments.

2. **Assumptions in Convergence Proofs**: The paper’s theoretical contributions are strong, particularly in proving convergence to BNE. However, several key assumptions, such as those related to the reward structures and learning rates, are briefly mentioned without full elaboration. Detailed analysis on how these assumptions align with real-world LLM behavior could clarify the conditions under which EcoNash’s convergence is robust. A more thorough exploration of these theoretical aspects would strengthen the rigor of the convergence claims. For instance, the paper should provide a detailed analysis of how the Lipschitz continuity of policy functions is ensured in the context of LLMs, and how the bounded and continuous Q-functions are derived from the reward structure. The sensitivity of the convergence results to variations in learning rate schedules should also be addressed.

3. **Heterogeneous Agent Configurations**: The experiments focus on homogeneous agent setups, which may not fully represent practical, mixed-capability multi-agent settings where different models operate together. Including experiments with heterogeneous agents (e.g., LLMs of varying sizes or architectures) would better validate EcoNash's adaptability and efficiency under more diverse configurations, highlighting its flexibility in real-world applications. The paper should investigate the impact of varying agent capabilities on the overall system performance, including how the belief encoder and centralized mixing network handle diverse outputs and reasoning styles from different LLMs. This is crucial for demonstrating the practical applicability of EcoNash in realistic scenarios.

4. **Reward Design Specificity**: The paper’s use of multi-faceted reward designs (e.g., action likelihood, task-specific, and self-evaluation rewards) is innovative, but the implementation lacks full transparency, particularly regarding how these rewards are balanced to avoid bias or feedback loops. Providing more specific details on the reward design and ensuring balanced feedback mechanisms would strengthen the framework’s robustness and generalizability. Additionally, discussing potential trade-offs among different reward types (e.g., consistency versus creativity) could offer further insights. The paper should clarify how the weights for each reward component are determined and adjusted during training, and how the self-evaluation reward is implemented to avoid potential biases or feedback loops that could lead to suboptimal performance. A detailed analysis of the impact of different reward balancing strategies on the final performance is needed.

5. **Comparison with Related Multi-Agent Systems**: The paper compares EcoNash against traditional multi-agent debate and coordination methods, but it could benefit from a comparison with additional recent multi-agent LLM approaches. For example, frameworks that optimize coordination in decentralized ways or those that involve explicit negotiation protocols could serve as useful baselines. Such comparisons would contextualize EcoNash’s performance and clarify its unique strengths. The paper should include comparisons with state-of-the-art multi-agent LLM frameworks that employ different coordination mechanisms, such as decentralized approaches or explicit negotiation protocols, to provide a comprehensive evaluation of EcoNash's performance and highlight its unique contributions.

### Questions
1. **Scalability of the Coordination Mechanism**: Could the authors clarify how EcoNash's coordination structure scales as the number of agents grows, particularly with a single Coordinator LLM? Are there any plans or existing methods for adapting the framework to include multiple coordinators or a more decentralized approach to avoid potential bottlenecks?

2. **Clarification on Assumptions in Convergence Proofs**: The theoretical results on convergence to BNE are valuable. However, could the authors clarify the assumptions made regarding the reward structures, learning rates, and agent behavior during convergence? Additionally, how sensitive are the convergence results to these assumptions?

3. **Heterogeneous Agent Configurations**: Could the authors discuss the feasibility and potential implications of using EcoNash with heterogeneous agents? Are there specific challenges the authors anticipate if agents of different sizes or architectures were integrated? Experimenting with a mixed-LLM setup could provide insights into EcoNash’s adaptability.

4. **Details on Reward Balancing and Bias Prevention**: The use of diverse rewards (action likelihood, task-specific, and self-evaluation) is innovative. Could the authors provide more details on how these reward types are balanced during training to prevent any unintended biases or feedback loops? How sensitive is the model's performance to changes in the reward balance?

5. **Additional Baselines for Comparison**: EcoNash is compared against traditional multi-agent debate and coordination methods, but it could benefit from a comparison with recent multi-agent LLM frameworks, particularly those using decentralized coordination or negotiation protocols. Would the authors consider including these as additional baselines, if possible, in the final paper?

6. **Implementation of Self-Evaluation Rewards**: The self-evaluation reward mechanism is intriguing for improving reasoning consistency. Could the authors elaborate on how this reward is designed and applied across different tasks? Are there any specific criteria used for self-evaluation that may vary by task type?

These questions aim to clarify potential improvements to EcoNash and enhance understanding of the approach. Addressing these points could strengthen the paper’s claims, particularly around scalability, reward balancing, and adaptability in diverse agent settings.

### Soundness
4

### Presentation
4

### Contribution
4
