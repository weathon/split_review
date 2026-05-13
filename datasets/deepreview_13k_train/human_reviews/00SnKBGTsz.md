# DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
The process of creating training data to teach models is currently driven by humans, who manually analyze model weaknesses and plan how to create data that improves a student model. 
Recent approaches using large language models (LLMs) as annotators reduce human annotation effort, but still require humans to interpret feedback from evaluations and control the LLM to produce data the student needs. 
Automating this labor-intensive process by creating autonomous data generation agents -- or teachers -- is desirable, but requires environments that can simulate the feedback-driven, iterative, closed loop of data creation. 
To enable rapid and scalable testing for such agents and their modules,
we introduce \framework{}, a testbed of \emph{teacher environments} for data generation agents. 
\framework{} frames data generation as a
sequential decision-making task,
involving an agent consisting of a data generation policy (which generates a plan for creating training data) and a data generation engine (which transforms the plan into data), inside an environment that provides feedback from a student.
The agent's end goal is to improve student model performance. 
Students are iteratively trained and evaluated on generated data, 
with their feedback (in the form of errors or weak skills) being reported to the agent after each iteration.
As a general-purpose testbed, \framework{} includes multiple instantiations of teacher environments across three levels of structure in the state representation and action space, with varying levels of scaffolding support. 
More structured environments are based on automatically-inferred skills and offer a higher degree of interpretability and control over the curriculum.
We support developing and testing data generation agents in three diverse tasks covering both text and images (mathematics, programming, and visual question answering) and test multiple student and teacher models. 
We find that example agents in our teaching environments can iteratively improve students across diverse tasks and settings.
Moreover, we show that environments can teach different skill levels and can be used to test variants of key modules, pointing to directions of future work in improving data generation agents, engines, and feedback mechanisms. Project page: \url{https://DataEnvGym.io}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Gym environments for data synthesis, framing the problem as sequential decision-making. In these environments, actions correspond to data-generation plans, and states represent the performance summary of a student model. The paper implements environments for three tasks: visual question answering (VQA), math, and code generation. Each environment offers three state representations: open-ended, skill-list, and skill-tree. Additionally, it proposes an LLM-based policy for data generation. Experimental results demonstrate that the LLM can make strategically effective choices based on environment-state information.

### Strengths
- Tackle a timely and interesting problem. 
- Provide the necessary infrastructure for the community to study the problem, opening up opportunities for future contributions. 
- Consider various data generation strategies,
- Well-desgined experiments which demonstrate the effectiveness of the proposed approaches and conduct insightful analyses.

### Weaknesses
 * The paper is currently dense and difficult to follow. The introduction includes excessive implementation details, which detract from providing a simple, high-level intuition. Using a specific task example to guide readers through the core concepts would make the paper more accessible.

* The paper focuses solely on the data generation plan rather than a full, end-to-end data generation process. It relies on a fixed, off-the-shelf data-generation engine that cannot be modified. The authors should admit this limitation and discuss potential strategies for overcoming it.

* The quality of the data-generation engine can impact both student performance and the data-generation plan itself. Current approaches do not take into account the data-generation engine capabilities in the design of the policy or the evaluation of the student. For instance, poor student performance might result from the engine producing low-quality data on a specific skill, which could prompt the policy to avoid querying the engine for that skill.

* The learning procedure can be resource-intensive. The authors should report the time, cost, and computing resources used for the experiments.

### Questions
- Is it possible to implement a random-policy baseline where you randomly chose a set of (naturally collected) datapoints from a data pool? The no-state baseline has flavor of this baseline but LLM-informed decisions could be biased. 
- Is it possible to compare this approach with active learning, in which instead of doing data generation, you do data *selection* and ask models to generate only synthetic labels, but not synthetic inputs?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a modular system for automated data generation, designed to minimize the need for human annotations. The proposed approach employs a reinforcement learning-inspired methodology, decomposing the process into a sequence of action predictions (data generation policy) based on state information (feedback from model errors) in an iterative manner. The effectiveness of this approach is demonstrated through three diverse tasks, encompassing text, image, and code generation across different modalities.

### Strengths
This paper presents a novel and insightful perspective on the autonomous data generation problem, leveraging principles from reinforcement learning to conceptualize it as a sequential decision-making process. The authors provide a thorough explanation of this approach, the motivations behind and the underlying mechanics.

This paper proposed a modular framework/testbed that can be easily adapted to various tasks, showcasing its versatility and potential for widespread applicability. The authors demonstrate the effectiveness of their approach through experiments on 3 tasks of multiple modalities, including text, image, and code generation, yielding promising early results.

### Weaknesses
The experiment part should be conducted more thoroughly: specifically, creating a test set that incorporates newly generated data points from the data generation agent and reporting evaluation results for each retrained model over successive iterations would provide more comprehensive insights into the system's performance.

Also the result would be more sound if more quantitative and qualitative results for skill discovery is reported in this paper.

### Questions
In the Experiments section, the authors mention that the baseline student model should not have been heavily post-trained so that there are rooms for further improvements. However, it would be beneficial to provide additional evidence and details to support the claim that the student's performance is improved due to the added data points rather than insufficient training. For instance, the training protocol involved a fixed 10-epoch training period; it remains unclear whether the model had reached convergence within this timeframe or if the introduction of new data points accelerated convergence. Further clarification on this aspect would enhance the overall validity of the results.

Also the result would be more sound if more quantitative and qualitative results for skill discovery is reported in this paper.

### Soundness
4

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
The paper presents DataEnvGym, a framework designed to simulate environments for data generation agents. These agents iteratively generate synthetic data to address weaknesses in student models, aiming to improve model performance across tasks like mathematics, programming, and visual question answering. DataEnvGym provides various structured environments (Open-Ended, Skill-List, and Skill-Tree) where data generation agents create targeted training examples based on feedback from the student model, offering a dynamic approach to automated model improvement.

### Strengths
- Good contribution to automated data generation for model improvement.
- Clearly written with structured sections explaining each environment type and experimental results.

### Weaknesses
 - The paper should clarify early on that the focus is on synthetic data generation for training purposes, as this underpins the motivation for the approach.
- Important related works on algorithms using feedback from training to generate the next training environments are missing [1, 2, 3, 4].
- Lines 460 - 465, I believe there is a typo whereby it says that “each experiment is truncated once the performance consistently decreases for multiple iterations”. Should it be “increases”?
- Repeated runs of experiments without confidence intervals will be valuable, especially since the variance of performance seems to be very high.

### Questions
- How does the performance of the data generation agents change over longer iterations? The paper truncates experiments when performance increases, but it would be insightful to explore whether performance plateaus or continuously increase over extended training.
- Is the total training data allocation fixed in each environment, or does it vary dynamically? The methodology mentions rebalancing but lacks clarity on how these allocations adjust adaptively based on feedback.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces DataEnvGym, a novel testbed of teacher environments for developing data generation agents that iteratively improve student models by generating targeted training data. DataEnvGym frames data generation as a sequential decision-making task where an agent, comprising a data generation policy and engine, interacts with an environment that provides feedback from a student model. The agent's goal is to improve student model performance by generating training data based on student feedback (errors or weak skills). DataEnvGym offers multiple instantiations of teacher environments across three levels of structure: open-ended, skill-list, and skill-tree, each with varying levels of scaffolding support. Experiments across text and image-based tasks (mathematics, programming, and visual question answering) demonstrate that example agents within DataEnvGym can iteratively improve student model performance. Furthermore, the authors analyze the impact of state information, environment structure, and skill discovery quality on agent performance and student learning. The paper concludes that DataEnvGym, with its modular design and support for diverse tasks and student models, provides a valuable platform for developing and evaluating data generation agents, engines, and feedback mechanisms for automated model improvement. The code and leaderboard will be publicly released.

### Strengths
Novel Problem: Automating data generation to improve models is a significant challenge with practical applications. This work directly addresses this problem with a novel approach.

Well-Defined Framework: DataEnvGym is presented as a well-defined framework with clear components (trainer, evaluator, data generation policy, data generation engine) and different levels of structure (open-ended, skill-list, skill-tree). This structure makes the problem tractable and facilitates modular development and testing.

Multiple Tasks and Domains: The inclusion of experiments across diverse tasks (mathematics, programming, visual question answering) and with different student models demonstrates the generalizability of the framework.

Promising Results: The initial results showing improved student model performance across tasks and environments are encouraging and suggest the potential of this approach. The analysis of difficulty/rarity and training dynamics adds value.

Open-Source Release: The commitment to publicly releasing the code and leaderboard promotes reproducibility and encourages further research in this area.

### Weaknesses
Limited Evaluation of Agent Architectures: The focus is primarily on the environment itself, with less emphasis on the architecture and training of the data generation agents. While baseline agents are provided, more sophisticated agent designs (e.g., reinforcement learning agents, agents leveraging larger language models) and their systematic evaluation would significantly strengthen the paper. How do different agent architectures compare in terms of effectiveness and efficiency? Are there specific architectural choices that are particularly well-suited for this task?

Over-Reliance on LLMs for Data Generation: While using LLMs for data generation is a reasonable starting point, it raises concerns about the quality and diversity of the generated data. Exploring alternative data generation methods (e.g., data augmentation techniques, programmatic data generation) and comparing their effectiveness with LLM-based generation would be valuable. How robust is the framework to the quality of the generated data?

Limited Analysis of Skill Discovery Quality: While the paper briefly touches upon the impact of skill discovery quality, a more thorough investigation is needed. How does the quality of the discovered skills affect the performance of the data generation agents and the student models? What are the limitations of the current skill discovery method, and how can it be improved? Quantitative analysis of skill quality (e.g., measuring coherence, coverage, and relevance) would strengthen the paper.

Lack of Comparison with Existing Methods: While related work on knowledge distillation and model weakness discovery is discussed, there's no direct comparison with existing methods for model improvement. How does DataEnvGym compare to techniques like curriculum learning or active learning in terms of effectiveness and efficiency? Including such comparisons would better contextualize the contributions and highlight the advantages of the proposed approach.

Limited Discussion of Scalability: The experiments are conducted with relatively small datasets and models. How does DataEnvGym scale to larger datasets and more complex models? What are the computational challenges associated with training data generation agents in more realistic settings? Addressing these scalability concerns is crucial for practical applications.

### Questions
Limited Evaluation of Agent Architectures: The paper primarily focuses on introducing the DataEnvGym environment, but the evaluation of data generation agents is limited to relatively simple baseline policies. Exploring more sophisticated agent architectures, such as reinforcement learning agents (e.g., using policy gradient methods, Q-learning) or agents incorporating larger language models for planning and decision-making (similar to the approaches used in Shimabucoro et al. (2024), would substantially strengthen the paper. A systematic comparison of different agent architectures in terms of their effectiveness in improving student models, their sample efficiency, and their computational cost would provide valuable insights and contribute to a better understanding of the challenges and opportunities in automated data generation.

Limited Analysis of Skill Discovery Quality: The paper briefly discusses the impact of oracle skills on student performance but doesn't delve deeply into the quality of the skills discovered by the proposed LLM-based method. A more thorough analysis is needed to understand the strengths and limitations of the skill discovery module. This could involve quantitative measures of skill quality, such as measuring their coherence, coverage, and relevance to the target task, or qualitative analysis by human experts. Investigating how the quality of the discovered skills affects the performance of the data generation agents and the resulting student models would strengthen the paper's contribution. Exploring alternative skill discovery methods (e.g., clustering-based approaches, topic modeling) and comparing their effectiveness with the proposed method would further enhance the analysis.

Lack of Comparison with Existing Methods: The paper positions DataEnvGym as a novel approach for model improvement, but it lacks a direct comparison with existing methods like curriculum learning (Bengio et al., 2009) or active learning (Settles, 2009). Evaluating how DataEnvGym compares to these established techniques in terms of student model performance, data efficiency, and computational cost would provide valuable context and highlight the advantages of the proposed framework. This would also clarify the specific niche and contribution of DataEnvGym within the broader landscape of model improvement techniques.

Limited Discussion of Scalability: The experiments in the paper are conducted with relatively small datasets and models. It's essential to address the scalability of DataEnvGym to more realistic scenarios involving larger datasets, more complex models, and a broader range of skills. Discussing the computational challenges and potential optimizations for scaling the framework to more demanding settings would strengthen the paper's practical relevance. For instance, how can the computational cost of LLM-based data generation be reduced while maintaining data quality? How can the skill discovery and agent training processes be optimized for larger datasets? Addressing these questions would provide valuable insights for future research and practical applications.

### Soundness
3

### Presentation
2

### Contribution
3
