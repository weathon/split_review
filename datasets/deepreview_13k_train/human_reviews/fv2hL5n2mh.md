# SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning

- Decision: Reject
- Scores: 3, 5, 1, 5

## Abstract
Automated Machine Learning (AutoML) approaches encompass traditional methods that optimize fixed pipelines for model selection and ensembling, as well as newer LLM-based frameworks that autonomously build pipelines. While LLM-based agents have shown promise in automating machine learning tasks, they often generate low-diversity and suboptimal code, even after multiple iterations. To overcome these limitations, we introduce Tree-\textbf{S}earch \textbf{E}nhanced \textbf{L}LM \textbf{A}gents (\textbf{\methodname{}}), an innovative agent-based system that leverages Monte Carlo Tree Search (MCTS) to optimize the AutoML process. By representing pipeline configurations as trees, our framework enables agents to conduct experiments intelligently and iteratively refine their strategies, facilitating a more effective exploration of the machine learning solution space.
This novel approach allows \methodname{} to discover optimal pathways based on experimental feedback, improving the overall quality of the solutions. In an extensive evaluation across 20 machine learning datasets, we compare the performance of traditional and agent-based AutoML methods, demonstrating that \methodname{} achieves a win rate of 65\% to 80\% against each baseline across all datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method (SELA) that combines LLMs with MCTS to solve AutoML tasks. More concretely, SELA uses LLMs to generate a search space of solutions (essentially generating different possibilities across different stages in the ML pipeline), which is then explored using MCTS. Through experiments on tasks from the AutoML benchmark and Kaggle competitions, the paper demonstrates SELA's efficacy against baseline methods.

### Strengths
- The paper conveys the main ideas and results clearly.
- Handling the NP-hardness of the problem by incorporating LLM agents with a search procedure is intuitive and makes a lot of sense.

### Weaknesses
My main concern with this paper is regarding the novelty of the proposed method. The authors note that prior work has already explored combining LLMs with tree search methods. This makes it unclear if the technical contribution of this paper is novel enough for ICLR. The primary contribution of applying LLMs with tree search to AutoML could be an interesting contribution had the paper shown that tree search cannot be trivially combined with LLMs to solve AutoML problems, and highlighted the key challenges faced.

### Questions
Could the authors elaborate on some key challenges faced when integrating LLM agents with tree search for AutoML tasks, and how SELA addresses them? All in all, I am trying to understand if the application is straightforward.

### Soundness
3

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
3

### Summary
This paper introduces SELA (Tree-Search Enhanced LLM Agents), a novel approach that combines Large Language Model (LLM) agents with Monte Carlo Tree Search (MCTS) for automated machine learning (AutoML). The primary contribution is defining an AutoML pipeline using a tree structure and experimentally demonstrating its effectiveness.

### Strengths
The paper presents an interesting pipeline for AutoML based on LLM agents, where the functional attributes of each node layer are intuitively and innovatively defined.

### Weaknesses
1. The paper lacks sufficient detail and resources for reproducibility.
2. The study involves multiple modules and details; however, the results in Table 2 appear to show only marginal improvements.
3. Regarding the `simulate` phase of MCTS, I understand that your tree has a depth of 6 levels (including the root node). Consequently, $x_{\text{sample}}$ does not necessarily correspond to the final Model Evaluation node, so $c(x_\text{sample})$ does not represent a complete configuration file. How, then, can this be provided to the experimenter $E$ to obtain a score-evaluable code?
4. Regarding lines 205 and 323, when I expand a node at time $\tau_i$, I provide the problem description $p$, dataset information $d$, and $\lambda(x_i)$ (where $\lambda(x_i)$ might concatenate with $\lambda(x_{i-1})$) as the LLM’s prompt, generating $m$ values of $\lambda(x_{i+1})$, from which one is randomly sampled for simulation—is this correct?
5. Given that even the most SOTA models struggle to generate immediately executable code, especially for complex ML tasks, how do you handle cases where the code provided by the LLM fails to execute? Do you assign it a minimum score or apply a different approach?
6. In lines 242–258, could you clarify the distinction between Value and Simulation Score, as well as between Solution Code and Stage Code? My understanding is that Stage Code corresponds to the current node’s code, but is Solution Code a set of codes of child branches? Since the node may have multiple branches.
7. In line 363, "Each framework utilizes the training and validation sets to train models," but I do not see any component in SELA that can be trained.
8. Regarding line 443, as a comparison, how exactly does SELA refine its Solution? I only understand that it finds the optimal solution through MCTS Search, but if a node's result is not good, it seems they won't refine it either, they just won't select it.
9. Line 393 mentions each AutoML rollout is conducted 10 times. Isn’t this count too low for a tree search, potentially resulting in a sparse tree structure?
10. Line 1160 states that each node corresponds to a single feature; however, combining multiple feature engineering techniques is standard practice. Does SELA not support such feature combinations?

### Questions
1. Regarding the `simulate` phase of MCTS, I understand that your tree has a depth of 6 levels (including the root node). Consequently, $x_{\text{sample}}$ does not necessarily correspond to the final Model Evaluation node, so $c(x_\text{sample})$ does not represent a complete configuration file. How, then, can this be provided to the experimenter $E$ to obtain a score-evaluable code?

2. Regarding lines 205 and 323, when I expand a node at time $\tau_i$, I provide the problem description $p$, dataset information $d$, and $\lambda(x_i)$ (where $\lambda(x_i)$ might concatenate with $\lambda(x_{i-1})$) as the LLM’s prompt, generating $m$ values of $\lambda(x_{i+1})$, from which one is randomly sampled for simulation—is this correct?

3. Given that even the most SOTA models struggle to generate immediately executable code, especially for complex ML tasks, how do you handle cases where the code provided by the LLM fails to execute? Do you assign it a minimum score or apply a different approach?

4. In lines 242–258, could you clarify the distinction between Value and Simulation Score, as well as between Solution Code and Stage Code? My understanding is that Stage Code corresponds to the current node’s code, but is Solution Code a set of codes of child branches? Since the node may have multiple branches. 

5. In line 363, "Each framework utilizes the training and validation sets to train models," but I do not see any component in SELA that can be trained.

6. Regarding line 443, as a comparison, how exactly does SELA refine its Solution? I only understand that it finds the optimal solution through MCTS Search, but if a node's result is not good, it seems they won't refine it either, they just won't select it.

7. Line 393 mentions each AutoML rollout is conducted 10 times. Isn’t this count too low for a tree search, potentially resulting in a sparse tree structure?

8. Line 1160 states that each node corresponds to a single feature; however, combining multiple feature engineering techniques is standard practice. Does SELA not support such feature combinations?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The work introduces an LLM based AutoML tool that uses MCTS to search for better performing configurations.

### Strengths
The ablation study showing the strenghts of different base LLMs is interesting.

### Weaknesses
The work introduces an LLM based AutoML tool that uses MCTS to search for better performing configurations.

The work largely seems to be unfamiliar with AutoML tools and the broader literature. This is particularly evident with the work repeatedly claiming falsehoods about AutoML. For example, early on it is said that AutoML tools typically only focus on the model training aspect, while ignoring feature engineering stages and so on. This claim is easily refuted as many of the cited tools do include data preprocessing and feature preprocessing into account and generally tend to the whole machine learning pipeline. It is often left to the user however what to include in the search space, thus a user might only want to focus on the model training element. Further, the work claims as a contribution that the search is inspired by how humans would conduct hyperparameter search/configuration. I.e., repeated experimentation while refining the search. This is exactly what nearly all AutoML tools do. Many are based on bayesian optimization which typically executes an initial design to probe the search space, then queries the most promising configuration(s) based on an internal model, based on the observation of the actual performance the model is refined and the search continues until a configuration budget is exhausted. Again, this is the standard approach in AutoML, making the claim in "contribution 1" not a contribution of this work. Further, contribution 2 hinges on the use of MCTS for AutoML (with an LLM base). However, MCTS has been already used and studied in the realm of AutoML (see the work by Rakotoarison https://inria.hal.science/hal-01966957/file/MOSAIC-wkpICML2018.pdf) strongly diminishing this claimed contribution. Further, the experiments do not consider an AutoML approach that uses MCTS for comparison.

I was already skeptical towards the experiments due to the untruths written about AutoML. I am further convinced that the evaluation of the aproaches is completely unfair. For AutoGluon and AutoSKLearn it is stated that they are simply used in their default configurations. However, it is not clear how much compute budget each method was allocated and that SELA very likely had a much larger configuration budget available than all other methods. Despite these weird setup issues, AutoGluon shows very strong performance, which is waved aside by the work. An important baseline that needs to be compared against in the AutoML realm is also missing. TabPFN uses a foundation model trained on synthetic data to learn to solve ML tasks and has shown highly competitive or even outperforming classical AutoML systems. This method thus has to be considered in a work as it is presented here. Overall the work can absolutely not be published. The work has to be largely rewritten to remove the false claims and the experiments likely need to be completely redone. I do not see immediate action items that would increase my trust in the work and would make me reconsider my scoring.

### Questions
What is the configuration budget allocated to all methods? Since you mentioned AutoSKlearns 600seconds wall-clock time of budget, did you limit SELA to the same small budget?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces SELA, a novel framework that integrates Monte Carlo Tree Search (MCTS) with Large Language Model (LLM) agents to enhance the process of Automated Machine Learning (AutoML). The authors claim that SELA improves the exploration and optimization of machine learning pipelines by leveraging MCTS to systematically explore potential configurations. The framework is evaluated on 20 datasets, demonstrating a win rate of 65% to 80% against traditional and agent-based AutoML methods.

### Strengths
- The integration of MCTS with LLM agents is a creative approach to address the limitations of existing AutoML frameworks. By using MCTS, SELA aims to mimic the iterative and feedback-driven problem-solving approach of human experts, which is a commendable attempt to enhance the adaptability and effectiveness of AutoML systems.
- The experimental results indicate that SELA outperforms several baseline methods across a range of datasets. This suggests that the proposed method has potential advantages in terms of flexibility and performance, offering a fresh perspective on tackling complex machine learning challenges.
- The paper provides a detailed description of the SELA framework, including its components such as the insight proposer, experiment executor, and the MCTS-based search module. This thorough explanation helps in understanding the workflow and the role of each component in the overall system.

### Weaknesses
 - While the integration of MCTS with LLM agents is an interesting approach, the innovation appears limited. The application of MCTS in this context is relatively straightforward and does not introduce significant novel techniques beyond existing LLM-agent frameworks like Data Interpreter. The paper could benefit from a deeper exploration of how MCTS specifically enhances the LLM agent's capabilities in a unique way.
- The experimental evaluation, although showing promising results, is somewhat inadequate. The authors do not provide a clear rationale for the selection of the 20 datasets from the AutoML Benchmark (AMLB). Given the diversity of tasks available in AMLB, it would be beneficial to understand the principles behind the choice of these specific tasks to ensure a comprehensive assessment of SELA's capabilities.
- The paper lacks a detailed analysis of the results and the specific contributions of MCTS to the observed performance improvements. A more in-depth discussion on how MCTS influences the exploration and optimization process, compared to other search strategies (beyond random ones), would strengthen the paper's contributions. In particular, UCB typically requires a significant number of exploitation steps to accurately evaluate the value of each node. However, this would incur a huge workload in an AutoML scenario. It would be beneficial to discuss how the authors achieve a good trade-off between efficiency and effectiveness, and why limited exploitation of UCB suffices to gain a performance improvement.

### Questions
- The experimental evaluation could be more comprehensive. Further exploration and justification of the chosen datasets, along with a deeper analysis of the results, would enhance the paper's impact and contribution to the field.
- Can you provide details on the size of the search pool for the MCTS procedure? Additionally, how many iterations does MCTS typically require to achieve good performance?

My score may be revised upon reviewing the authors' response to these limitations.

### Soundness
3

### Presentation
3

### Contribution
2
