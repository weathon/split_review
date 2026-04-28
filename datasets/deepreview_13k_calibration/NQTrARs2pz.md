# HomieBot: an Adaptive System for Embodied Mobile Manipulation in Open Environments

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Embodied Mobile Manipulation in Open Environments (EMMOE) is the challenge that agents understanding user instructions and executing long-horizon everyday tasks in home environments. This challenge encompasses task planning, decision-making, navigation and manipulation, and is crucial to develop a powerful home assistant capable of autonomously completing daily tasks. However, the absence of a holistic benchmark, data incompatibility between large language models (LLMs) and mobile manipulation tasks, the lack of a comprehensive framework, and insufficient dynamic adaptation mechanisms all continue to hinder its development. To address these issues, we propose EMMOE, the first unified benchmark that simultaneously evaluates high-level planners and low-level policies, and new metrics for more diverse evaluation. Additionally, we manually collect EMMOE-100, the first everyday task dataset featuring detailed decision-making processes, Chain-of-Thought (CoT) outputs, feedback from low-level execution and a trainable data format for Large Multimodal Models (LMMs). Furthermore, we design HomieBot, a sophisticated agent system which integrates LMM with Direct Preference Optimization (DPO) as the high-level planner, small navigation and manipulation models as the low-level executor. Finally, we demonstrate HomieBot's performance and methods for evaluating different models and policies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces three main contributions:

1. EMMOE: A unified benchmark for evaluating both high-level planners and low-level policies in embodied mobile manipulation tasks.

2. EMMOE-100: A dataset with 100 complex everyday tasks featuring task-planning processes and COT outputs

3. HOMIEBOT: An intergrated agent system combining high-level planner and low-level executors.

### Strengths
1. The new evaluation metrics are novel, potentially providing a valuable resource for the research community and practical applications.

### Weaknesses
1. **Insufficient Methodology Details**
   - The data processing and augmentation methods are not adequately explained:
     * The "fixed-format conversation data" conversion process in SFT Augmentation is not described
     * No clear explanation of how the uniform script processes the EMMOE-100 data
     * The DPO Augmentation section lacks clear algorithmic description or flowcharts

2. **Limited Experimental Evaluation**
   - Inadequate baseline comparisons and empirical analysis:
     * No evaluation of existing RL algorithms or LM-based agents on the EMMOE benchmark
     * Only one system (HOMIEBOT) is evaluated, lacking comparative analysis
     * The relatively low success rates (31.8% training, 20% testing) are not thoroughly analyzed
     * Missing ablation studies or detailed error analysis to understand performance bottlenecks

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work focuses on studying embodied AI instruction following mobile manipulation in simulated environments. To this end, the paper proposes the EMMOE-100 dataset and benchmark and HOMIEBOT as a system integration solution to it. Some unique contributions involve that it is a dataset of human-controlled embodied agent trajectories:
1. Decomposition into subtasks
1. Annotated reasoning process with every execution
1. Replanning for some failed subtasks
The paper also introduces metrics to measure Task Progress, Success end rate, and success replan rate and presents results for SFT and SFT+DPO on the Video-LlaVA model.

### Strengths
1. The paper introduces the human controlled embodied agent trajectories, unlike the use of PDDL in ALFRED and other RL benchmarks.
1. The focus seems to be on open-ended long horizon questions, multiple ways of solving it, annotating sub-goals and deliberately collecting replanning trajectories.

### Weaknesses
1. Overclaim: it does not seem like the first to unify the high-level and low-level. This has been discussed in Robotics Task and Motion planning (TAMP) literature and has been introduced as baselines in previous simulator benchmarks. Connection with previous work and clarity on the unique contribution of this work is needed.

2. Lack of failure analysis: The paper does not discuss the limitations and failures modes of the combined high-level and low-level modules. The rule-based error detection approach, while providing some initial error handling, appears to be brittle and not easily scalable to more complex scenarios. For example, the provided example of checking if an object is 'closed' before a 'put' action does not account for the variety of valid 'put' locations such as 'in a sink' or 'on a shelf', which do not have 'open' or 'closed' states.

3. Limited discussion: It is unclear why the success rate for HOMIEBOT is so low in training and test tasks. 

4. Clarity: Paper is not well formatted and has lots of typos (line 180 control, 185-186 between)

5. Limited novelty: with discrete action space, the work looks very similar to ALFRED (Shridhar et al.) and FiLM (Min et al.) with a few enhancements.

### Questions
1. Why not use continuous action space? Habitat Replica allows for continuous action space. HM3D 
2. How is the Success end rate, and success re-plan rate measured? How is the count for end and replan computed for each trajectory?
3. Why is “trainable data format” listed as an important contribution compared to the existing datasets? 
4. How does the high-level planner know when and where low-level execution fails?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a benchmark of 100 tasks in home robotics, collected within the Habitat simulator using human demonstrations annotated with detailed reasoning explanations. The benchmark evaluates models using success rate, success end rate, and success replan rate. The authors train Video-LLaVA on this dataset with either SFT (supervised fine-tuning) or DPO (Direct Preference Optimization) and find that SFT+DPO performs best on the train set across all metrics, while SFT-only achieves the highest scores on the test set.

### Strengths
- Introduction of a new benchmark for home robotics with a diverse set of 100 tasks.
- Collection of detailed annotations to capture the reasoning process and a diverse set of tasks in home environments.
- Strong metrics to evaluate embodied execution, focusing on nuanced aspects of embodied execution.
- Propose a dataset for SFT and DPO fine-tuning from egocentric trajectories.

### Weaknesses
 - Limited baseline comparisons, which reduces the clarity of contributions relative to existing methods.
- Lack of diverse model comparisons, including text-only and zero-shot multi-image baselines (e.g., Qwen2VL, GPT-4o), and no modular vs. end-to-end performance analysis.
- Insufficient analysis of task-specific challenges and bottlenecks within the benchmark; error analysis and reasoning failure modes are explored to some degree, but not in detail.
- No discussion of potential real-to-sim discrepancies for the manipulation models, which could impact model generalization.

### Questions
- Could the authors provide stronger baseline comparisons, especially with text-only and zero-shot multi-image models?
- How do modular models compare to end-to-end approaches on this benchmark?
- Can the authors analyze the primary failures observed by the model, and give qualitative analysis of what are the major challenges in the benchmark for existing models?
- Is there any observed real-to-sim gap affecting the manipulation models, and if so, how does it impact performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a unified benchmark named “EMMOE” designed to simultaneously evaluate both high-level planning and low-level control abilities of embodied agents. This benchmark comprises 100 complex everyday tasks based on scenarios from the Replica dataset, including long-horizon tasks, open-ended tasks with multiple possible outcomes, logical tasks, etc. To better assess agent performance, the authors propose three new metrics: Task Progress, Success End Rate, and Success Re-plan Rate. Additionally, the paper provides training data using Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO), featuring Chain-of-Thought (CoT) outputs and replan processes. A baseline agent, HomieBot, is introduced, featuring a Large Multimodal Model (LMM) for high-level planning and several task-specific models for low-level control. HomieBot achieves a 31.8% success rate on training tasks and 20% on test tasks.

### Strengths
1. The objectives of the study are clearly stated.
2. The related work cited in this article is extensive.
3. The provision of the datasets (including CoT, replanning, etc.) is beneficial for future embodied AI research.

### Weaknesses
1. The article lacks clear organization.
     - In Section 3, describing the dataset for model training (Section 3.2, Data Augmentation for SFT and DPO) is misplaced. This section should focus on the benchmark construction, not the training data for the embodied agents. The training data details should be moved to a later section dedicated to the agent's training methodology.
     - The work aims to evaluate high-level planning and low-level execution abilities. However, there is no individual assessment of these abilities. For instance, metrics like the success rate of high-level planning and low-level execution in isolation are missing. Furthermore, the relationship between the proposed evaluation metrics (TP, SER, SRR) and these abilities is not clearly established. It is unclear how each metric specifically reflects the high-level planning or low-level execution performance.
    - The problem is not well defined. A formal problem formulation regarding high-level planning and low-level execution would significantly improve the paper. This formulation should clearly define the inputs, outputs, and constraints for each stage.
   - Some content in the article is unclear. For instance, on page 4, line 207, the statement “if subtask i fails but subtask i + 1 succeeds” lacks clarity regarding the relationship between subtask i and subtask i+1. It seems to imply that these are different attempts at the same task, but this should be explicitly stated and clarified.
2. There are a lot of mistakes in the paper,
   - In Section 3.3, Equation 1 appears to be incorrect. The equation should account for the variability in nodes to be checked for different keypaths. A more accurate representation would be $TP=max_{{k_i}\in K_T} (\frac{len(k_i^{check})}{len(k_i)})$.
   - On page 6, line 278, there is a conceptual confusion between *task* and *trajectory*. M is defined as the set of all tasks, and $t \in M$, so $t$ should be a single task. However, the author also states “t is a task trajectory,” which conflates the concepts. These terms need to be clearly defined and consistently used.
   - The criterion “Success End Rate” is not reasonable. For example, if an agent never outputs “End” but can complete some tasks, the equation will be infinite. The correct equation should be $\frac{\text{number of successful tasks whose last output is End}}{\text{number of successful tasks}}$.
   - On page 4, line 318, $i$ is not defined.
   - Spelling errors: On page 4, “controll” should be “control”.
3. The experimental section needs improvement. There is even no evaluation of the model before fine-tuning, making it difficult to assess the impact of the proposed fine-tuning methods.

### Questions
See Weaknesses

### Soundness
2

### Presentation
1

### Contribution
1
