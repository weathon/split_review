# AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Automated machine learning\,(AutoML) accelerates AI development by automating tasks in the development pipeline, such as optimal model search and hyperparameter tuning. Existing AutoML systems often require technical expertise to set up complex tools, which is in general time-consuming and requires a large amount of human effort. Therefore, recent works have started exploiting large language models\,(LLM) to lessen such burden and increase the usability of AutoML frameworks via a natural language interface, allowing non-expert users to build their data-driven solutions. These methods, however, are usually designed only for a particular process in the AI development pipeline and do not efficiently use the inherent capacity of the LLMs. This paper proposes \algname{}, a novel multi-agent framework tailored for full-pipeline AutoML, i.e., from data retrieval to model deployment. \algname{} takes user's task descriptions, facilitates collaboration between specialized LLM agents, and delivers deployment-ready models. Unlike existing work, instead of devising a single plan, we introduce a retrieval-augmented planning strategy to enhance exploration to search for more optimal plans. We also decompose each plan into sub-tasks (e.g., data preprocessing and neural network design) each of which is solved by a specialized agent we build via prompting executing in parallel, making the search process more efficient. Moreover, we propose a multi-stage verification to verify executed results and guide the code generation LLM in implementing successful solutions. Extensive experiments on seven downstream tasks using fourteen datasets show that \algname{} achieves a higher success rate in automating the full AutoML process, yielding systems with good performance throughout the diverse domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an SOP for solving autoML tasks with multiple LLm agents. The user's prompt. i.e., the ML task is first passed to a prompt agent which re-organizes the instruction into ML tasks with specific information, e.g., the problem itself, the data, and model etc. Then the ML task is passed to a manager agent to generate a plan with RAG. The manager agent will generate multiple plans and each plan will be decomposed into executable sub-tasks that are assigned to the corresponding agent to perform. The manager will select the best and executable plan from the generated plan to generate code. The prompt parser agent is finetuned with open-source LLM and the rest of the agents are GPT-based models. The proposed method is evaluated on different ML tasks, such as image classification, NLP, and graph mining problems and compared with various baselines.

### Strengths
1. The paper is well-organized and written.
2. The detailed prompt for each agent is given, which significantly improves the reproducibility of the work.
3. The performance of the proposed model is promising against various baselines.
4. I appreciate the resource cost is given.

### Weaknesses
1. The evaluation is only performed on synthetic datasets; no public benchmarks are tested. Public datasets like IMDB, Cora, and Citeseer are used for autoML tasks. The synthetic dataset I mentioned is the one for testing the performance of autoML algorithms. Since in 4.1, no evidence shows public benchmarks for evaluating autoML algorithms are given. Please specify any benchmarks if you do use some.

2. I am unclear about how the manager agent verifies the plans if no plans are executed and tests with generated code. Can you explain a bit?

3. The generated plans seem homogeneous, similar, and not diverse enough, making it easy for all to fail if one fails (Appendix C2). Therefore, I am not sure about the effectiveness of the plan selection, given that the manager selects the plan based on the "simulated" result from the data and model agent.

4. Using LLM agent to solve autoML is not a new research problem. Specifically, what is the difference between the paper:
https://arxiv.org/abs/2410.17238
Both papers use reflection, while the paper above uses a more sophisticated mechanism, e.g., MCTS, which yields a strong performance. Why don't you consider using MCTS instead? Does this work compatible with MCTS?

5. What is the reason for fine-tuning mixtral for prompt parser?

### Questions
1. I am unclear about how the manager agent verifies the plans if no plans are executed and tests with generated code. Can you explain a bit?
2. The generated plans seem homogeneous, similar, and not diverse enough, making it easy for all to fail if one fails (Appendix C2). Therefore, I am not sure about the effectiveness of the plan selection, given that the manager selects the plan based on the "simulated" result from the data and model agent.
3. Using LLM agent to solve autoML is not a new research problem. Specifically, what is the difference between the paper:
https://arxiv.org/abs/2410.17238
Both papers use reflection, while the paper above uses a more sophisticated mechanism, e.g., MCTS, which yields a strong performance. Why don't you consider using MCTS instead? Does this work compatible with MCTS?
4. What is the reason for fine-tuning mixtral for prompt parser?

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
4

### Summary
This paper presents AutoML-Agent, a novel multi-agent framework designed for full-pipeline Automated Machine Learning (AutoML), addressing the limitations of existing AutoML systems that require technical expertise and are time-consuming. By leveraging large language models (LLMs) and facilitating collaboration between specialized agents, AutoML-Agent automates tasks from data retrieval to model deployment. The paper introduces a retrieval-augmented planning strategy to enhance exploration for optimal plans and decomposes each plan into sub-tasks handled by specialized agents. Extensive experiments demonstrate AutoML-Agent's higher success rate in automating the full AutoML process and yielding good performance across diverse domains, making it a significant contribution to the field.

### Strengths
(1) The paper proposes a novel multi-agent framework tailored for full-pipeline AutoML, leveraging large language models (LLMs) in a task-agnostic manner from data retrieval to model deployment. This represents a groundbreaking attempt in the field of AutoML, offering a comprehensive solution to automate the entire AI development pipeline.

(2) By introducing retrieval-augmented planning with role-specific plan decomposition and prompt-based plan execution, the paper addresses the complexity of planning in full-pipeline AutoML. This approach enhances the flexibility and efficiency of the search process, enabling the framework to handle diverse and complex tasks more effectively.

(3) This paper integrates structure-based prompt parsing and multi-stage verification to ensure the quality of resulting solutions and instructions before actual code implementation. This approach improves the accuracy of the full-pipeline implementation, demonstrating the superiority of the proposed AutoML-Agent framework through extensive experiments across multiple application domains.

### Weaknesses
(1) While the paper presents an innovative framework, it would greatly benefit the research community if the associated code were openly available on platforms like Github. 

(2) The paper could benefit from a more in-depth discussion of the framework's limitations and potential areas for improvement. Specifically, the paper lacks a detailed analysis of the computational resources required by the multi-agent system, which is crucial for practical deployment. Furthermore, the paper does not explore the sensitivity of the framework to different LLMs or prompt engineering strategies, which could significantly impact its performance and robustness.

### Questions
None.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces AutoML-Agent, an innovative multi-agent large language model (LLM) framework designed to achieve full automation in machine learning (AutoML) from data retrieval to model deployment. The framework receives task descriptions from users and coordinates multiple specialized LLM agents to execute tasks in parallel, thereby improving search efficiency. It also proposes a retrieval-enhanced planning strategy to enhance exploration and optimize planning. Furthermore, AutoML-Agent integrates structured prompt parsing and multi-stage validation to ensure the quality of the generated solutions and instructions.

### Strengths
- The AutoML-Agent framework proposed in this paper is an innovative multi-agent system that leverages the capabilities of large language models (LLMs) to achieve full automation in the workflow from data retrieval to model deployment.
- The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The AutoML-Agent framework proposed in this paper relies on the collaborative work of multiple agents, which may lead to significant computational resource consumption. In environments with limited computing power, implementing this framework using open-source large language models (LLMs) might face challenges.

### Questions
- The method proposed in this paper has only been experimentally validated on current SOTA models, Mixtral-8x7B and GPT-4o. Given that the performance improvements observed in downstream tasks may primarily be attributed to the inherent advantages of the large language models (LLMs) themselves rather than the proposed method, I am uncertain about the generalizability of the experimental conclusions to smaller-scale or less powerful models. To further demonstrate the robustness of the proposed method, it is suggested that the authors supplement the paper with experimental results on such models.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduced the AutoML-Agent, a multi-LLM-agent framework that aims to automate the entire pipeline of automated machine learning. The framework employed Retrieval-Augmented Planning (RAP), which uses retrieved knowledge to devise multiple end-to-end plans, aiming to enhance exploration and search for more plans. The framework is claimed to be user-friendly to non-expert users, allowing them to build data-driven solutions solely through natural language instructions. The experiments seem to be extensive, investigating the effectiveness of AutoML-Agent on 7 downstream tasks and proving the superiority over existing models.

### Strengths
[+] Integrate a lot of techniques from LLM-agent into this AutoML-Agent framework, including Retrieval-Augmented Planning, task decomposition, plan proposing, planning verification, etc. 

[+] The experiments seem to be extensive and the results look good.

### Weaknesses
[-] The core contribution of this paper is the multi-agent framework with RAP for processing AutoML tasks in an end-to-end manner. While the ambition of AutoML is significant and the framework is claimed to be powerful, the benchmarks and tasks presented are very simple. I believe these tasks would not require such a complex framework and should be manageable for most ML practitioners.

[-] Additionally, I question the motivation and necessity behind devising this AutoML-agent framework. Do non-expert users really exist and need this level of assistance? Although the limitation section acknowledges the issues of hallucination and unreliability within LLMs, I want to emphasize that systems or frameworks with bugs can be prohibitive for non-expert users, making it extremely difficult for them to debug and resolve problems. This is not necessarily a flaw of this paper, but it seems premature to propose frameworks that may not be practical at this time.

### Questions
1. Why does RAP propose multiple plans for a task? Especially, this is not inference time compute (thoughts instead of execution) but indeed executes all the plans and compares the results in the last, which results in a significant amount of costs. 
2. How do judge the difference between the LLM-agent framework for Auto-ML and the general LLM-agent? It seems to me that the general LLM-agent framework can cater to AutoML tasks since they are just a small subset of real complex tasks.

### Soundness
3

### Presentation
3

### Contribution
2
