# Knowing What Not to Do: Leverage Language Model Insights for Action Space Pruning in Multi-agent Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
label{abstract}
  Multi-agent reinforcement learning (MARL) is employed to develop autonomous agents that can learn to adopt cooperative or competitive strategies within complex environments. However, the linear increase in the number of agents leads to a combinatorial explosion of the action space, which may result in algorithmic instability, difficulty in convergence, or entrapment in local optima. While researchers have designed a variety of effective algorithms to compress the action space, these methods also introduce new challenges, such as the need for manually designed prior knowledge or reliance on the structure of the problem, which diminishes the applicability of these techniques.
  In this paper, we introduce \textbf{E}volutionary action \textbf{SPA}ce \textbf{R}eduction with \textbf{K}nowledge (\texttt{eSpark}), an exploration function generation framework driven by large language models (LLMs) to boost exploration and prune unnecessary actions in MARL. Using just a basic prompt that outlines the overall task and setting, \texttt{eSpark} is capable of generating exploration functions in a zero-shot manner, identifying and pruning redundant or irrelevant state-action pairs, and then achieving autonomous improvement from policy feedback. In reinforcement learning tasks involving inventory management and traffic light control encompassing a total of 15 scenarios, \texttt{eSpark} consistently outperforms the combined MARL algorithm in all scenarios, achieving an average performance gain of 34.4\% and 9.9\% in the two types of tasks respectively. Additionally, \texttt{eSpark} has proven to be capable of managing situations with a large number of agents, securing a 29.7\% improvement in scalability challenges that featured over 500 agents.git}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the eSpark framework, which integrates large language models (LLMs) to address the challenges of exploration in environments with an increasing number of agents by pruning unnecessary actions. This approach is tested across various settings, including inventory management and traffic signal control, and demonstrates significant performance improvements.

### Strengths
**Innovative Use of LLMs**: The paper effectively harnesses the capabilities of LLMs to generate exploration functions, providing a novel approach to action space pruning in MARL.
Clear Presentation: The paper is well-structured and clearly presents the methodology, experiments, and results. The use of figures and tables is effective in illustrating the improvements made by eSpark.

### Weaknesses
 **High Training Costs**: The eSpark framework necessitates multiple iterations, each generating k exploration functions and evaluating all state-action pairs within the action space. This approach substantially increases both the financial and computational complexity of training, requiring greater GPU memory and prolonging the overall training duration. The paper does not provide a clear analysis of how the number of iterations impacts the final performance, nor does it quantify the increase in computational resources compared to standard MARL baselines. This lack of detail makes it difficult to assess the practical feasibility of the method, especially in resource-constrained environments.

**Lack of Theoretical Guarantees**: The manuscript lacks a comprehensive assessment of the quality of exploration functions produced by the large language model (LLM). Consequently, it is challenging to ascertain whether the utilization of LLMs for pruning adversely affects the pursuit of optimal solutions. The paper does not address the potential for the LLM to generate suboptimal or even detrimental exploration functions, which could lead to the algorithm converging to a poor local optimum. Furthermore, the stochastic nature of LLM outputs introduces an element of unpredictability, making it difficult to analyze the convergence properties of the algorithm.

**Limited Experimental Environments**: The experiments are confined to two specific tasks—logistics and traffic management—raising questions about the algorithm's generalizability and effectiveness in more widely encountered task environments. It remains uncertain whether the proposed algorithm can be effectively generalized across a broader spectrum of task scenarios. The chosen environments, while complex, may not fully represent the diversity of challenges found in other MARL problems, such as those with sparse rewards or highly non-stationary dynamics. The lack of experiments in more diverse environments makes it difficult to assess the robustness of the proposed method.

### Questions
1. The example provided in Section 3.2 bears limited relevance to the proposed method in this paper. Could a more compelling example be introduced to illustrate the advantages of using LLMs for generating exploration functions? The current example merely demonstrates the reasoning abilities of GPT, which is a widely accepted understanding, and does little to support the argument that LLMs can effectively generate exploration functions.

2. The paper only presents the final results in a tabular format without accompanying training curves. Specific details regarding the number of iterations required by eSpark and how the iteration count affects its performance remain unaddressed. Would it be feasible to include these additional visualizations?

3. Relying solely on rewards as feedback may not adequately capture the current state of the policy. Could the authors consider providing more informative feedback, such as the individual components of the rewards?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces eSpark, a novel framework designed to enhance Multi-Agent Reinforcement Learning (MARL) by leveraging Large Language Models (LLMs). Specifically, it addresses the combinatorial explosion of action spaces in MARL by utilizing LLMs to prune irrelevant and redundant actions, thereby improving the efficiency of exploration. eSpark generates exploration functions in a zero-shot manner, using only a basic task description, and refines the exploration process iteratively based on policy feedback. The framework is evaluated across tasks in inventory management and traffic light control, showing significant improvements in performance relative to existing MARL methods.

### Strengths
- Innovative Use of LLMs in MARL: The paper presents a novel application of LLMs for action space pruning in MARL. Leveraging LLMs to generate exploration functions in a zero-shot manner is a unique and promising approach that could pave the way for more efficient MARL systems.
- Scalability and Generalization: The proposed eSpark framework demonstrates strong scalability, as shown in scenarios involving over 500 agents. The method also generalizes well across different domains, including traffic control and inventory management, indicating its wide applicability.
- Performance Gains: eSpark achieves notable improvements over baseline MARL methods, including an average performance gain of 34.4% in inventory management tasks and 9.9% in traffic control tasks, showcasing its effectiveness in complex environments.

### Weaknesses
I believe the biggest limitation of this paper is the lack of in-depth analysis and discussion of the proposed method. The baselines selected in the paper are mainly MARL methods and heuristic approaches, lacking comparisons and discussions with existing LLM-based methods[1-4]. Additionally, the environments chosen in the paper do not include classical MARL benchmarks, such as SMAC. Lastly, the paper does not provide detailed analysis or case studies of the action masks generated by the LLM; it mainly focuses on overall performance.

### Questions
1. How can eSpark be extended to continuous action spaces? Does this limit its usage?
2. In the current eSpark framework, each agent independently generates its action mask without considering collaboration between agents. Could this limit eSpark's utility in tasks requiring strong cooperation?
3. Generating an action mask at each time step is somewhat equivalent to generating a reward function at each time step, a topic that has already been explored in single-agent RL. The authors should analyze and discuss this.
4. The benchmarks selected by the authors primarily come from the operations research field. What was the rationale behind this choice?

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
In this paper the authors propose an action pruning method called eSpark for action pruning in multi-agent reinforcement learning using LLMs. This approach utilizes LLMs to improve MARL training via optimized exploration functions, which are used to prune the action space. eSpark begins by using LLMs to generate exploration functions from task descriptions and environmental rules in a zero-shot fashion. It then applies evolutionary search within MARL to pinpoint the best performing policy. The authors overcome the limitations of the existing action pruning methods which are either computationally expensive, hard to scale or require the underlying domain structure knowledge. The authors show that their proposed method is able to prune action space for large number of agents with a 29.7% improvement in scalability.

### Strengths
Strengths:

1.	The paper is clear and well-written.

2.	eSpark requires no complex prompt engineering and can be easily combined with MARL algorithms.

3.	The paper effectively shows that eSpark can handle scenarios with a large number of agents, which is a significant step in overcoming limitations of existing MARL methods. 

4.	Good ablation studies provided for the proposed method.

### Weaknesses
See the questions below.

Questions:

1.	Did authors test what will be the performance with other base MARL algorithms other than IPPO?

2.	While the paper states that no complex prompt engineering is needed, did the authors experiment with different prompts, and how did that influence the exploration function quality?

3.	It seems like the authors only compare their method against the random pruning and heuristic pruning methods. There are other works that the authors have mentioned in the related work section for pruning. Have authors considered comparing with those baselines?

4.	Does the inclusion of the LLM checker at any time cause the flawed exploration functions (e.g., variable misuse, misaligned task logic)? How can this be handled?

### Questions
Questions:

1.	Did authors test what will be the performance with other base MARL algorithms other than IPPO?

2.	While the paper states that no complex prompt engineering is needed, did the authors experiment with different prompts, and how did that influence the exploration function quality? 

3.	It seems like the authors only compare their method against the random pruning and heuristic pruning methods. There are other works that the authors have mentioned in the related work section for pruning. Have authors considered comparing with those baselines?

4.	Does the inclusion of the LLM checker at any time cause the flawed exploration functions (e.g., variable misuse, misaligned task logic)? How can this be handled?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents eSpark, a framework that leverages large language models (LLMs) to enhance multi-agent reinforcement learning (MARL) by pruning unnecessary actions. eSpark addresses the challenge of combinatorial action space growth in MARL, generating exploration functions in a zero-shot manner without manual intervention. Through iterative cycles of policy feedback and evolutionary search, it optimizes agent behavior. Evaluated on inventory management and traffic control tasks across 15 scenarios, eSpark outperforms baseline methods, showing a 34.4% performance gain and improved scalability with up to 500 agents. The framework demonstrates the effectiveness of LLM-driven action pruning in some environments.

### Strengths
1. The paper's primary strength lies in its innovative integration of large language models (LLMs) into multi-agent reinforcement learning (MARL) for action space pruning.
2. The extensive experiments and ablation studies provide robust evidence of eSpark’s effectiveness and generalizability.

### Weaknesses
 - While the paper aims to address the dimensional explosion in complex environments with many agents, the experimental settings, though varied, may not fully represent truly complex real-world environments. This raises doubts about whether the experiments sufficiently support the paper’s stated motivation.  
- The framework lacks a theoretical guarantee on how pruning actions with LLMs affects the optimality of learned policies, leaving open the possibility that some optimal actions may be discarded during exploration.  
- The computational efficiency comparisons may not be entirely fair, as different algorithms could have varying levels of computational complexity, especially with the use of LLMs, which are resource-intensive.  
- The paper does not include comparisons with straightforward, rule-based action space pruning techniques, which could serve as useful baselines and provide clearer insights into the added value of the LLM-driven approach.  
- While the framework performs well with homogeneous agents, it is unclear how well it would generalize to heterogeneous agents or to tasks with sparse rewards. The lack of experiments in such scenarios limits the generalizability of the proposed method.  
- The effectiveness of the eSpark framework depends heavily on the quality of the LLM outputs. Errors in exploration function generation or feedback handling could negatively impact performance, yet the paper provides limited discussion on handling these risks.

### Questions
- How would eSpark perform in settings with heterogeneous agents, where each agent may require distinct exploration functions? Is there a plan to extend the framework to such scenarios?
- How does the framework manage incorrect or suboptimal outputs from the LLMs, especially during iterative exploration function generation? Are there fallback mechanisms to prevent performance degradation from such errors?

### Soundness
3

### Presentation
3

### Contribution
2
