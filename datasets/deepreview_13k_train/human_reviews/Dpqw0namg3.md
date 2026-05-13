# LAM Simulator: Advancing Large Action Model Training for Agent via Online Exploration and Feedback Simulation

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Large Action Models (LAMs) for AI agents have significant potential, but their development is often constrained by the reliance on supervised learning and manual data curation, which are both time-consuming and costly. To address these limitations, we present the LAM Simulator, a comprehensive framework designed for online exploration of agentic tasks with high-quality feedback. This framework includes a curated set of high-quality agentic tasks, a diverse collection of tools, and an interactive environment where agent models can call tools, receive execution responses, and obtain action feedback. Our findings indicate that the LAM Simulator significantly enhances model performance and effectively identifies and addresses potential issues. Specifically, our model, LAM-Sim-8x7B, demonstrates an 18.54\% improvement over its base LAM and significantly outperforms other state-of-the-art alternatives on ToolEval benchmark. Furthermore, we have demonstrated that LLMs lacking in agentic capability can greatly benefit from the implementation of LAM Simulator. Our experiments with a model trained on Mixtral-8x7B-Instruct-v0.1 have yielded a doubling to tripling of performance. Remarkably, the data construction process for training these models requires minimal human intervention, making the LAM Simulator a robust framework for accelerating the development of AI agents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The submission introduces a system that incorporates a simulator with a language model for more effective large action models. In response to a user query the LAM Simulator system iteratively refines its response multiple times in a loop. The refinement leverages feedback from the simulator which has syntax verification and request execution tools to improve the final response.

### Strengths
- Preference data generation for finetuning via DPO is neat to address the challenges of multi-turn conversations, it encourages more diverse data pairs
- Compared to past work this submission introduces many more domains the system can handle queries for

### Weaknesses
 - Many parts of the submission seem to lack explanation or additional clarification (perhaps to be put in the appendix) on many details. I ask some direct clarification questions in the questions section. It is also possible that my inexperience with research on these types of agents has led to me being unaware of some terms.
- Figure 1 seems to suggest you can only pass or fail via the syntax verification engine. What happens after the request verification engine?
- There's a lack of example/qualitative user interactions and agent responses (including the generated conversation data in the multi-turn setup). There also appear to be no examples of user command templates, task evaluators etc., (many elements of figure 1). It is quite hard to visualize what exactly is going on and how it might be better than related work.

### Questions
- How come the human-crafted abstracted tasks has such a relatively high proportion of "astronomy" tasks. It feels like strangely very specific, how come there aren't other e.g. science topics? It is claimed in section 3.4 the human-crafted abstracted tasks are meticulously designed for the typical requests the LAM might receive from users. However this seems heavily audience dependent, perhaps I missed a sentence somewhere but is the audience mostly astronomers in this case?
- For task categories what does "data" and "database" mean exactly? Why is the "data" category such a high proportion?
- Why DPO for preference optimization instead of other options?
- What is U. Tool, U. Cat etc in the header of table 1?
- Table 2 shows average errors, but these numbers are meaningless without knowing the number of times the model was evaluated. Moreover, there are no standard deviation metrics in any tables and specifically table 2, it is difficult to know if the results are really statistically significant or if there is some lucky prompting changes/randomness in the inference models or evaluation LLMs.

If all weaknesses and questions are addressed I am happy to raise the score into the accept range. My biggest concern is mostly around the lack of examples and explanations for a lot of terms and phrases.

### Soundness
2

### Presentation
2

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
The paper introduces the LAM Simulator, a framework for enhancing Large Action Model (LAM) training through online exploration and simulated feedback. By providing AI agents with curated tools, feedback, and interactive environments, the framework enables cost-effective, autonomous data generation with minimal human input. Experiments show significant performance improvements, particularly with the LAM-Sim-8x7B model, and error reduction through automated feedback.

### Strengths
1.	**Innovative Framework:** The LAM Simulator introduces a novel method for automating LAM training through simulated feedback and task exploration.
2.	**Performance Improvements:** The framework achieves measurable improvements over baseline models, e.g. GPT-4o, showing its effectiveness in enhancing agent task performance.
3.	Scalability: The reduction in human intervention for data generation makes this framework adaptable for large-scale agent training.
4.	**Comprehensive Evaluation:** The use of multiple evaluators provides continuous feedback, leading to improved agent performance and fewer errors.

### Weaknesses
1. **Limited Comparative Analysis:** While the paper briefly mentions related methods like ToolTalk, WebArena, and APIGen, it lacks a thorough comparison with these and other frameworks for automated data synthesis and agent training. Such a comparison would provide valuable context and clarity on the specific advantages or disadvantages of the LAM Simulator relative to existing approaches. The authors could strengthen the paper by providing empirical comparisons or, at minimum, a more detailed discussion of how the LAM Simulator diverges or improves upon these methods. The current discussion does not sufficiently address how the LAM Simulator's approach to tool usage, multi-turn interactions, and evaluation differs from these existing frameworks, making it difficult to assess its novelty and contribution.

2. **Comparative Performance Analysis on Agent Self-Exploration:** Although the paper demonstrates improvements over xLAM, it would benefit from a direct, quantitative comparison to other self-exploration-based methods. This could include metrics for data quality, agent adaptability, or overall effectiveness in reducing human intervention. Without such benchmarks, it’s challenging to assess how the LAM Simulator stacks up against state-of-the-art methods in self-guided agent learning. The paper needs to clarify how the self-exploration mechanism of the LAM Simulator compares to other methods in terms of exploration efficiency, data diversity, and the ability to escape local optima during training.

3. **Insufficient Examples of Human-Crafted Tools:** The paper describes a curated set of tools used for agent training but doesn’t provide concrete examples or details on these tools in the main text or the appendix. Including examples, especially in an appendix, would improve transparency around the toolset design and selection criteria. This addition would allow readers to better understand the diversity and complexity of tasks the agents are trained on, as well as any limitations or biases in the tool curation process. The lack of specific examples makes it difficult to assess the practical applicability and generalizability of the proposed framework.

### Questions
1. **Lack of Detail on Reward Calculation:** The paper briefly describes using “action rewards” to generate preference data for DPO but doesn’t clarify how these rewards are calculated. Are rewards based on a specific scoring metric, or are they derived from evaluator feedback? A clearer explanation of the reward components and their calculation method would clarify how preference scores are assigned to different actions or paths.

2. **Potential Overfitting to ToolEval Benchmark:** With performance gains reported on ToolEval, there’s a possibility that the LAM Simulator is optimized specifically for this benchmark. Given ToolEval’s structured and predefined nature, the model might be learning patterns specific to ToolEval, which could limit generalizability. Testing the framework on multiple diverse benchmarks, or introducing a new, unstructured benchmark, would give a more robust picture of its true capabilities.

3. **Limited Discussion on the Impact of Feedback Granularity:** The framework provides both action-wise and task-wise feedback, but the paper does not analyze the relative impact of these feedback types on agent learning. Understanding whether detailed, step-by-step feedback leads to more effective training compared to feedback provided only at task completion could help optimize the feedback strategy and reduce computation costs.

4. **What is the success rate of data generation?:** Can the authors provide quantitative information on the success rate of data generation within the LAM Simulator? For instance, out of all attempted tasks or interactions, what percentage completes successfully without errors? This metric would give insight into the reliability and efficiency of the simulator.

5. **What specific measures ensure the quality of generated data?:** The paper mentions filtering methods to ensure data quality, but could the authors elaborate on the full set of criteria or techniques used to evaluate data quality? Are there specific metrics, benchmarks, or thresholds that generated data must meet?

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
3

### Summary
This paper introduces the LAM Simulator, a framework designed to enhance the training and development of Large Action Models (LAMs) for AI agents. The LAM Simulator aims to mitigate the reliance on supervised learning and manual data curation by enabling online exploration of agentic tasks with real-time, high-quality feedback. The framework provides a diverse set of tasks, tools, and feedback mechanisms to help agents learn more effectively. The paper demonstrates significant performance improvements using the LAM Simulator, with models such as LAM-Sim-8x7B showing an 18.54% improvement over the base model on the ToolEval benchmark.

### Strengths
1) One of the key strengths is the ability of the LAM Simulator to automate feedback and reduce the need for human intervention. This is crucial for scaling agentic models and training on more extensive datasets without the burden of manual curation.
2) The empirical results show significant performance improvements on the ToolEval benchmark. The LAM-Sim-8x7B model consistently outperforms other state-of-the-art alternatives, showcasing the potential of the proposed framework.
3) The LAM Simulator integrates action verification mechanisms (e.g., syntax verification, tool name validation), which significantly reduce errors related to tool usage, helping agents perform more reliably in tasks involving multiple tools.

### Weaknesses
1) The tasks used in the evaluation are relatively constrained and do not reflect the complexity of real-world agent tasks. The evaluation primarily focuses on tool-use within a predefined set of APIs, lacking the open-ended nature of real-world scenarios. The paper could have included experiments in more diverse environments, such as dynamic multi-agent systems or open-ended tasks, to demonstrate broader applicability. The current evaluation does not adequately test the agent's ability to handle unexpected inputs, adapt to changing goals, or recover from errors that are common in real-world settings.
2) While the framework’s feedback loop is central to its design, the paper does not sufficiently explore its effectiveness. It would have been useful to include ablation studies or case studies showing how feedback at different stages (e.g., intermediate actions versus final steps) influences learning outcomes. The paper lacks a detailed analysis of how the frequency, type, and timing of feedback impact the agent's learning curve. Furthermore, the paper does not explore the potential for feedback to become less effective as the agent improves, which is a crucial aspect of understanding the long-term training dynamics.
3) The paper does not adequately address how well the LAM Simulator scales to more complex environments or to tasks that require real-time interactions with a broader set of tools. The reliance on predefined tasks and tools may limit its generalization to open-world or unstructured environments. The evaluation does not consider the computational overhead of the action verification mechanism as the number of tools and parameters increases, which is a critical factor for real-time applications. The paper also fails to explore the simulator's performance in scenarios with high tool dependencies, where the success of one action is contingent on the outcome of previous actions.

### Questions
1) How does the LAM Simulator handle situations where the task requirements change dynamically, or where tools malfunction during execution? Would it be able to generalize to such cases?
2) Have you considered applying the LAM Simulator to environments that involve real-time multi-agent interactions or more complex tool dependencies?
3) Can you provide more detailed insights into how the feedback mechanisms evolve as the agent performs tasks over time? Are there diminishing returns to feedback as the agent improves?
4) How does the action verification mechanism scale with an increasing number of tools or tool parameters? Does it introduce any computational overhead that might limit real-time applicability?

### Soundness
3

### Presentation
3

### Contribution
2
