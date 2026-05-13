# Improving Large Language Model based  Multi-Agent Framework through Dynamic Workflow Updating

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Multi-agent frameworks powered by large language models (LLMs) have demonstrated great success in automated planning and task execution. However, the effective adjustment of workflows during execution has not been well studied. A flexible workflow is crucial, as in many real-world scenarios, the initial plan must adjust to unforeseen challenges and changing conditions in real-time to ensure the efficient execution of complex tasks. In this paper, we define workflows as activity-on-vertex (AOV) graphs. We continuously refine the workflow by dynamically adjusting task allocations and agent roles based on historical performance and previous AOV graphs with LLM agents. To further enhance system performance, we emphasize modularity in workflow design based on measuring parallelism and dependence complexity. Our proposed multi-agent framework achieved efficient sub-task concurrent execution, goal achievement, and error tolerance. Empirical results across various practical tasks demonstrate significant improvements in the efficiency of multi-agent systems through dynamic workflow updating and modularization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the author(s) propose a multi-agent framework to enable dynamic workflow update, by integrating activity-on-vertex (AOV) graphs. In particular, an agent is prompted to generate several workflows in the form of AOV, and the one with the highest parallelism level and lowest dependency complexity will be selected. Various agent roles will be assigned to complete the workflow tasks, and the framework allows workflow refinement and dynamic updating if agents encounter errors.

### Strengths
- The paper adds value to agent-based workflow generation and automation.
- Activity-on-vertex graphs are incorporated to better manage task dependency and parallelism.
- Comparative analysis is conducted with multiple related work in terms of both success rate and human rating.

### Weaknesses
 - A framework architecture or sequence diagram is needed to demonstrate the overview of the proposed solution.
- I am wondering why the proposed solution does not check the workflow correctness in the first place, but the parallelism and modularity. It seems counterintuitive to prioritize these aspects over ensuring the workflow's logical validity. A workflow that is highly parallel but fundamentally incorrect is not useful. The paper should clarify the rationale behind this design choice, perhaps by discussing the trade-offs involved.
- Section 4.1.3: Why “Flow gets 100% success rate” while in Table 3 the overall success rate is 80%? This discrepancy needs to be addressed, as it undermines the credibility of the reported results. The authors should provide a clear explanation for this inconsistency or correct the error.
- The evaluation results can be elaborated. For instance, in the three scenarios, how many updates are required respectively? This information is crucial for understanding the dynamic nature of the workflow updates and the robustness of the proposed framework. Without this, it's difficult to assess the practical applicability of the method.
- Table 1: “task 1, 2 completed, task 3 under-work”, task 2 and 3 should be exchanged according to the above AOV. This indicates a potential error in the representation or interpretation of the AOV graph, which needs to be corrected.
- The paper organization can be adjusted. For instance, there is no Section 4.2, then why Section 4.1 is needed? The lack of a Section 4.2 makes the structure illogical and confusing. The authors should either include a Section 4.2 or reorganize the existing sections to ensure a coherent flow.
- A proof-reading is needed as some typos are found.

      - Section 2: “previous approach like …” -> “Previous”.

      - Section 4.1: “… the average performance of Flowis 93% …” -> “Flow is”.

### Questions
- I am wondering why the proposed solution does not check the workflow correctness in the first place, but the parallelism and modularity.
- Section 4.1.3: Why “Flow gets 100% success rate” while in Table 3 the overall success rate is 80%?
- The evaluation results can be elaborated. For instance, in the three scenarios, how many updates are required respectively?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to enhancing the performance of LLM-based multi-agent systems through the use of activity-on-vertex (AOV) graphs. By defining workflows as AOV graphs, the authors enable dynamic updates during task execution, which facilitates better resource allocation and real-time adjustments. This flexibility is crucial for efficiently managing complex tasks. The paper presents a practical multi-agent framework that incorporates quantitative measures to evaluate workflows, allowing for efficient selection and improved planning capabilities. To empirically demonstrate the framework's effectiveness, the authors conduct experiments across three diverse tasks: game generation, LaTeX slide generation, and website design. They provide detailed evaluations and analyses of the results, showcasing the superior performance of their framework compared to existing open-source solutions.

### Strengths
-  The paper effectively points out a significant gap in existing frameworks, specifically regarding the adaptability of workflows in real-time, especially in the face of unforeseen challenges.
-  The paper is well-structured and easy to follow, offering clear definitions and detailed formulas that enhance comprehension.

### Weaknesses
 -  Limited novelty. While dynamic workflow generation and execution have been extensively discussed in prior studies (e.g., [1][2][3][4]), this paper's approach lacks sufficient novelty. Directed acyclic graphs (DAGs) and graph-based frameworks have already been established as effective structures in LLM-based agent frameworks. To strengthen its contribution, the paper should include comparative analysis with these existing approaches, highlighting specific advantages and unique aspects of the proposed method.

- Cost analysis. What's the cost of the Flow?  There is no discussion of Flow’s cost relative to other frameworks, leaving the efficiency of the proposed method unclear.

- Experiment specifications. What's the specified experiment settings? Important experimental settings, such as the number of candidate graphs (𝐾) and the agent count, are not specified. 

- Updating machinism. The description of workflow refinement process lacks critical details. In line 318: the phrase “systematic review to determine if the workflow requires refinement” lacks clarity regarding how this review is conducted and the criteria for determining when refinements are needed. Additionally, further details are needed on “this rigorous verification process” mentioned in line 323, particularly regarding how the system handles verification when no errors are found.

- Flow basic execution. Lacks several key information of Flow deisgn and execution. 1) How Flow determines when all prerequisite tasks has been completed? 2) How Flow handle the cases where some parallel tasks have not yet finished --dose Flow wait, reprioritize tasks, or initiate partial updates in such scenarios? 3) Critical setup information is missing, such as the total number of agents available in Flow’s default configuration. 

- The current experiments cover only three tasks, which may not be sufficient to substantiate Flow's superior performance comprehensively. Expanding the experiments to include more diverse tasks and standardized benchmarks would strengthen the claims regarding its generalizability and robustness.

- LLM dependency. The paper does not address how Flow would perform with less powerful LLMs, such as GPT-3.5 or other open-source models. Exploring this would provide valuable insights into the framework’s robustness and generalizability

### Questions
Please refer to the questions in Weaknesses.

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
The paper presents a multi-agent system approach to automating (essentially coding) tasks such as website creation or game creation. Their multi-agent approach does better than other single agent approaches from the literature. A key to tracking the multi-agent system's progress on such complex tasks was utilizing a graphical representation of sub-tasks, task assignments and progress, namely activity-on-vertex directed acyclic graphs to represent the workflow. Results on multiple tasks (while anecdotal) show the proposed approach does better than other approaches in the literature.

### Strengths
The paper presents an interesting and intuitive approach to representing workflows and enabling multi-agent systems to execute complex tasks. Results support the validity of the approach. The paper also tackles an important open problem in the literature: automating complex tasks. The authors also perform a good analysis of the experiments, taking the time to specify errors that different agents performed in completing their tasks.

### Weaknesses
The authors mostly evaluate their approach anecdotally as opposed to on standard benchmarks or datasets. This is understandable given the lack of complex task datasets in this domain.

The paper contains grammar mistakes and presentation issues that make the paper difficult to read. A few examples: in the abstract, did you mean "define workflows *as* activity on vertex (AOV)"?; line 162 should say "inspired by" as opposed to "inspire by"; Figure 1 should say "the game must end" instead of "must be ended"; Figure 2 should say "initial" as opposed to "intial"; in Tables 1, 2 and 3, instead of saying "ours", say "Flow (ours)" to be consistent with the writeup in the various sections; line 118, "1)" instead of "1)."; line 132, "LLM-based" as opposed to "LLM based".

### Questions
NA

### Soundness
3

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
This paper focuses on enhancing large language model (LLM)-based multi-agent systems by improving dynamic workflow management and modular task execution. The proposed system refines workflows using an Activity-on-Vertex (AOV) graph structure, enabling flexible and dynamic task allocation adjustments. The system encourages modularity, allowing for concurrent task execution and minimizing inter-task dependencies. This results in greater robustness and efficiency, especially in complex, evolving task scenarios. Experimental results across tasks like game development, LaTeX slide creation, and website building show that the system can outperform several existing approaches (AutoGen, CAMEL, MetaGPT), with better success rates and human satisfaction scores.

### Strengths
This paper introduces dynamic workflow updating and modularization, which appear to be novel.

This paper clearly outlines the methodological innovations, with well-structured sections on each component, from workflow initialization to modular design.

This paper has clear contribution to the design of multi-agent collaboration frameworks, particularly for complex adaptive tasks. By improving modularity and enabling efficient concurrent sub-task execution, the proposed framework has potential applications across fields requiring adaptable, scalable automated task execution.

### Weaknesses
While this paper presents some interesting research ideas and promising experiment results, I have several concerns as detailed below.

1. The general idea of supporting dynamic workflow management has been studied previously, in particular in the context of single-agent and multi-agent planning systems. It might be novel to expand this idea in LLM-based multi-agent systems, however the corresponding technical novelty may need to be clearly highlighted and better justified.

2. It seems that a key assumption of this paper is that a highly modular workflow structure can reliably cope with task failures. While this is intuitively meaningful, what happens if we find that a module is unsolvable? In which case, we may need to adjust other modules and potentially the entire workflow structure. Consequently, most part of the workflow execution may be interrupted. Hence, it is essential to theoretically analyze this assumption and understand the specific conditions for it to be valid for practical applications.

3. If building a modular workflow is motivated by the goal of improving robustness of workflow execution, why didn't authors directly analyze the expected amount of changes required by any workflow due to unexpected/random task failures? This expected quantity can be used to determine which workflow should be adopted, in addition to the parallelism metric or the dependency metric. Meanwhile, past studies in the distributed computing community may have developed some existing metrics to measure parallelism and the level of dependency. It is important to clarify why the authors chose to use their own metrics and highlight the corresponding technical novelty.

4. The discussion of how subtasks are assigned to different agents with varied roles is quite brief. The lack of sufficient technical details makes it hard for me to understand this aspect of the system design and its importance to the overall effectiveness of the system. Similarly, while discussing the regeneration of the workflow graph (on page 6), shouldn't this process consider the execution status of the existing/current workflow (e.g., the completion status of different modules) to avoid unnecessary resource wastage? This aspect was not clearly explained in the paper.

5. I don't fully agree with the authors' statement that non-coding tasks may introduce bias on page 7. Besides coding related tasks, many other tasks such as logic reasoning and mathematics analysis tasks may also be important for us to understand the effectiveness and broad usefulness of the newly developed multi-agent system. Meanwhile, given how errors were simulated in Section 5, I was wondering how likely that any task may fail in practice. If tasks seldom fail, is it necessary to find a modular workflow in the first place?

6. Additionally, in terms of the evaluation criteria, I am not sure whether using success rate and human rating is sufficient and fair for comparing different approaches. For each benchmark problem, it is not clear whether the authors followed the common criteria to measure success rates. Meanwhile, for human rating, it largely depends on human participants involved in this research and may not objectively or accurately reveal the varied usefulness of all competing approaches.

### Questions
The paper assumes that a highly modular workflow structure can cope with task failures, but what happens if a module turns out to be unsolvable? Does the system have a mechanism to adjust other modules or restructure the entire workflow dynamically? Could you provide more theoretical analysis on the conditions under which modular workflows remain effective in practical applications?

Given the goal of improving workflow robustness, why did you not directly analyze the expected amount of changes required when tasks fail? How could this expected quantity complement the metrics of parallelism and dependency?

Could you elaborate on how subtasks are assigned to different agents with varied roles? How does the assignment strategy impact the system’s overall effectiveness? Also, when regenerating the workflow graph, does the system consider the execution status of current tasks to avoid resource wastage?

Why do you believe non-coding tasks might introduce bias in evaluation? Would it be possible to include additional tasks such as logic reasoning or mathematical analysis to demonstrate the system’s broader applicability?

Could you clarify how human rating was conducted and address concerns that it may not fully reflect the varied usefulness of all competing approaches?

### Soundness
3

### Presentation
3

### Contribution
3
