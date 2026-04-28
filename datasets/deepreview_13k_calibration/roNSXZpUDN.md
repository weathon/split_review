# {$\tau$}-bench: A Benchmark for \underline{T}ool-\underline{A}gent-\underline{U}ser Interaction in Real-World Domains

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Existing benchmarks for language agents do not set them up to interact with human users or follow domain-specific rules, both of which are vital to safe and realistic deployment. We propose $\tau$-bench, a benchmark with two domains (retail and airline) emulating dynamic conversations between a user (simulated by language models) and a customer service agent provided with domain-specific API tools and policy guidelines. We employ a efficient and faithful evaluation process that compares the database state at the end of a conversation with the annotated goal state, and propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials. Our experiments show that even state-of-the-art function calling agents (gpt-4o) succeed on $<50\%$ of the tasks, and are terribly inconsistent (pass^8 < 25\% in retail). Our findings point to the need for methods that can improve the ability of agents to act consistently and reliably follow rules.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article introduces a novel benchmark called τ-bench, designed to evaluate the ability of language agents to interact and plan with human users and programmatic APIs in real-world scenarios. The main contributions of the article can be summarized as follows:
- **Introduction of the τ-bench Benchmark**: τ-bench simulates dynamic dialogues between users and language agents equipped with domain-specific API tools and strategy guidelines. It is built on a modular framework, featuring realistic databases and APIs, domain-specific strategy documents, and detailed instructions for various user scenarios, along with corresponding real annotations.
- **New Evaluation Metric, passˆk**: In addition to measuring the success rate of agents in task completion (passˆ1), the article proposes a new metric, passˆk, to assess the consistency and robustness of agent behavior across multiple independent trials. This metric is particularly important for real-world agent tasks requiring reliability and consistency, such as customer service.
- **Comprehensive Experiments on Existing Language Models**: The authors conduct extensive tests using τ-bench on a variety of state-of-the-art proprietary and open-source language models, including GPT, Claude, Gemini, Mistral, and Llama. The experimental results indicate that even the most advanced functional calling agents (e.g., gpt-4o) succeed in less than 50% of tasks and exhibit poor consistency (with passˆ8 < 25% in the retail domain).

### Strengths
1. The τ-bench benchmark effectively addresses the limitations of existing evaluations by providing a more comprehensive framework for assessing the capabilities of language agents in real-world environments. The introduction of the passˆk metric presents a novel approach to measuring the consistency and robustness of agent behavior, while the pass in k demonstrates the potential for using agents in data synthesis.
2. The dataset construction closely aligns with practical application scenarios. The testing methods and data definitions exhibit scalability, enhancing the utility of the benchmark for future research.
3. The experiments are comprehensive. The article is well-written and easy to follow.
4. The qualitative experiments are highly detailed, pointing out promising directions for future research.

### Weaknesses
1. **Limitations of user simulation**: The user behaviors are simulated by LLMs in this study. Although the authors explore methods to improve user simulation, these efforts cannot entirely mitigate the potential issues arising from simulated users. It may result in simulated behaviors that diverge from those of real users, thereby affecting the assessment of the agents. Specifically, the simulated users might lack the nuanced and unpredictable behavior patterns of real users, potentially leading to an overestimation of agent performance in practical scenarios. For example, real users might exhibit inconsistent or illogical requests, which the simulated users might not replicate, thus failing to fully test the agent's robustness.
2. **Limitations of Evaluation Metrics**: While the passˆk metric assesses the consistency and robustness of agent behavior, it remains a task success rate-based measure. In some cases, an agent may provide valuable information or service even if it does not fully accomplish the intended task. It may make more sense to use more granular evaluation metrics. For instance, an agent might correctly identify a user's need but fail to execute the final API call due to a minor error. In such cases, a binary success/failure metric would not capture the partial success of the agent, potentially underestimating its capabilities. Furthermore, the pass@k metric, while useful for consistency, does not evaluate the quality of the agent's interactions or the user's experience.

### Questions
This evaluation framework is likely to benefit from more fine-grained task definition and evaluation, such as information gathering, policy understanding, decision-making, etc., assessing the agent's performance on each subtask. This will provide more comprehensive understanding of the agent's capabilities, offering specific guidance for future research. Additionally, the paper could incorporate more dimensions of human evaluation, such as the agent's understanding of user intent, adherence to policy, and user satisfaction with the agent.

Other questions can refer to the weaknesses.

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
4

### Summary
the paper build a novel agent evaluation benchmark considering the complexity of domain policy, user-agent interactions with  realistic databases and APIs. Based on that, the paper propose new evalaution metric pass^k to determine the robust and consistency of agent, and present insightful analysis about existing LLMs.

### Strengths
1. the target problem is valuable and important, such as the  complex policies and rules specific to a task or domain that the agent should follow, and consistency and reliability at scale.
2. the formulation is reasonable and proposed collection pipeline is easy to understand and expand
3. the experiment and analysis are comprehensive and insightful.

### Weaknesses
 1. the contribution is a little overclaimed and the paper does not given enough credits to task-oriented dialogue system (ToD). There are several examples: 1) evaluation scheme in line 78, the dialogue state tracking in ToD also compare the current dialogue state with ground truth expected state; 2) there are many lm-simulated users in ToD (see below) and rule-based user simulator also bring insightful studies; 3) some important works are missing, such schema-guided dialogue dataset which also explore various schema in different domain and build corresponding APIs and collect data via human-to-human ways. Generally, the major contribution of this paper lies in combination of lm-simulated user, real APIs and introduction of domain-specific policy while others such as multi-turn interactions are very similar with ToD. 

 2. the related work is not fully discussed. 1) line 108-111, there are many works focus on multi-step user interaction, such as API-Bank [1], and ToolUltra [2]; 2) there are many LM-simulated user studies [3,4,5].

### Questions
1. line 349, why self-reflection is not suitable? despite the agent only have one change to serve the user, it still can reflect its own reasoning and API call before it generate the final responses.

### Soundness
3

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
The paper proposes a new LLM-agent benchmark for two domains (retail and airline), called tau-bench. The gap that the proposed tau-bench aims to fill is LLM-agent benchmarks that focus on User and LLM agent interactions. I.e. measuring how well a LLM agent performs when interacting with a "human" user. To this end they propose to use a LLM based user simulator. Furthermore, the paper describes how the benchmark is constructed and based on databases and APIs. Finally, the authors also propose a new metric for the benchmark, pass HAT k (pass ^ k). This metric measures what the chance is that all passes are successful given k i.i.d. attempts.

The paper has a detailed evaluation of agents performance on the benchmark, detailed analysis of errors of these agents and some cost analysis of both the agent (LLM-based) and user-simulator (LLM-based). The cost of a single evaluation cost $200. There is also some analysis of user simulator performance.

### Strengths
The paper is very clear, well written and well designed. The paper shows that much effort has been put into this work. 

Important contributions:
1. The main contribution is the benchmark itself. Specifically, the databases, function calls and interaction templates.

2. The evaluation of baseline agents and ablation studies are interesting to see. 

3. The proposal of the metric pass ^ k (pass hat k, vs. the existing metrics pass @ k) is quite interesting.

4. Good comparison against previous work, including task oriented dialogue systems (well done).

### Weaknesses
The main weaknesses of the paper is the analysis of the **user simulator**, evaluation of it, and especially using less *prohibitively expensive* models such as open source model of the size 7B-13B.

1. The paper evaluated the user simulator based on mistakes of agents (and identified 4% of errors). However, it would be interesting to establish guarantees on the user simulator. 
2. Additionally, it would be important to use such evaluation benchmarks of the user simulator to show how smaller models perform as user simulators to make such a benchmark more usable and available to the community.
3. Therefore, at this stage it is not clear at all how smaller models would perform as user simulators, whether it is possible or not.
4. Also, having a benchmark that only works with the highest end APIs is very prohibitive for the research community. (Great projects that could help alleviate this problem for you are: AutoGuide (a RAG mechanism), Act-Re (a finetuning mechanism), StateAct (a prompting mechanism), Optimus-1 (a finetuning & exploration mechanism)).

---
An additional weakness is the presentation of the *unbiased estimator* of the pass ^ k (pass hat k) metric is unclear. There is no derivation or explanation where this formula comes from and why it should be an unbiased estimator.

### Questions
1. How do you evaluate the user simulator?
2. How could you evaluate the user simulator?
3. What would be the performance of a smaller LLM (7B / 13B) as user simulator?
4. How do you derive the unbiased estimator?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes Tau-Bench, a benchmark for measuring the performance of models on user/agent interactions where the model has the ability to use tools. The goal of each interaction is to learn information from the user, and achieve some end state the user wants the agent to accomplish, such as re-booking a flight or initiating a return through an online store. They also introduce a pass^k (similar to pass@k) metric, measuring how often an agent succeeds at a given task when the task is re-run with slight variations in syntax/semantics/etc, simulating multiple users attempting to accomplish the same goal, to measure how reliable an agent is.

### Strengths
This paper proposes a novel benchmark targeting a growing area of interest (user/agent interactions to achieve a goal), and provides a strong foundation for future work in this area. The benchmark is well-defined and easy to understand, the proposed pass^k metric seems like a great measure of reliability across a diverse set of users and scenarios, and the tasks in the benchmark are focused on popular, real-world, tasks that are difficult for current models.

### Weaknesses
I think this paper is very strong overall. There are a few additional results I'd be interested to see, but I don't think any are necessarily required:
* how consistent is pass^k? E.g. if you run pass^16 10 times, what is the variance?
* what is the effect of changing the policy document? does model performance change much with more, fewer, or different constraints?
* do in context examples help improve agent consistency?

### Questions
My one suggestion would be to explore (in the final revision, or follow up work) how well open models can do when finetuned specifically for these sorts of tasks. The formulation of agent trajectories in this work would lend itself very well to both supervised finetuning on example gold interactions, and preference tuning on positive and negative examples. Because the answers are verifiable, reinforcement learning would also be a good candidate. I'm curious how well specialized models can perform these tasks, especially compared to strong closed models such as gpt4o.

### Soundness
4

### Presentation
4

### Contribution
4
