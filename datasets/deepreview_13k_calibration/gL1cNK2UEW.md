# DSMentor: Enhancing Data Science Agents with Curriculum Learning and Online Knowledge Accumulation

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Large language model (LLM) agents have shown promising performance in generating code for solving complex data science problems. Recent studies primarily focus on enhancing in-context learning through improved search, sampling, and planning techniques, while overlooking the importance of the order in which problems are tackled during inference. In this work, we develop a novel inference-time optimization framework, referred to as DSMentor, which leverages curriculum learning---a strategy that introduces simpler task first and progressively moves to more complex ones as the learner improves---to enhance LLM agent performance in challenging data science tasks. Our mentor-guided framework organizes data science tasks in order of increasing difficulty and incorporates a growing long-term memory to retain prior experiences, guiding the agent's learning progression and enabling more effective utilization of accumulated knowledge. We evaluate DSMentor through extensive experiments on DSEval and QRData benchmarks. Experiments show that DSMentor using Claude-3.5-Sonnet improves the pass rate by up to 5.2% on DSEval and QRData compared to baseline agents. Furthermore, DSMentor demonstrates stronger causal reasoning ability, improving the pass rate by 8.8% on the causality problems compared to GPT-4 using Program-of-Thoughts prompts. Our work underscores the importance of developing effective strategies for accumulating and utilizing knowledge during inference, mirroring the human learning process and opening new avenues for improving LLM performance through curriculum-based inference optimization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents an inference-time optimization framework called DSMentor for large language model (LLM) agents, focusing on enhancing performance by addressing the overlooked aspect of problem-solving order during inference. By leveraging curriculum learning, DSMentor introduces tasks in ascending order of complexity. Evaluation of DSEval and QRData benchmarks reveals the performance improvements in causal reasoning tasks compared to GPT-4. This work emphasizes the importance of effective knowledge accumulation and utilization during inference, mirroring human learning and paving new ways to optimize LLM performance through curriculum-based approaches.

### Strengths
(1) The paper demonstrates the outstanding performance of DSMentor, which utilizes an easy-to-hard curriculum, across established benchmarks in data analysis and causal reasoning tasks. 

(2) The paper shows that by retrieving easier and more relevant examples from memory and structuring the knowledge in an increasing-similarity order, DSMentor significantly improves data science agents' understanding. 

(3) The paper demonstrates how DSMentor incrementally introduces tasks with increasing complexity, facilitating the agent's progressive learning of causal relationships.

### Weaknesses
(1) While the paper presents promising results, it would be more compelling if the experiments were repeated multiple times to establish a mean performance. This would provide a clearer picture of the consistency and reliability of the proposed method, DSMentor, across different runs and potentially highlight any variability in its performance.

(2) A more comprehensive exploration of the shortcomings, including the reasons behind them and possible mitigation strategies, would strengthen the paper's contributions and provide valuable insights for future research.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces DSMentor, a framework designed to improve the performance of large language model (LLM) agents in solving data science tasks through a combination of curriculum learning and long-term memory. The central innovation is organizing tasks in increasing order of difficulty (curriculum learning) and dynamically accumulating and retrieving knowledge from previous tasks (online memory). DSMentor is evaluated on two benchmarks: DSEval and QRData, where it outperforms baseline agents, particularly in causal reasoning tasks. The framework uses Claude-3.5-Sonnet and Llama-3.1-70b as base models and demonstrates performance gains  over existing methods.

### Strengths
1. DSMentor introduces an inference-time curriculum learning strategy that effectively mirrors human learning, gradually increasing task difficulty to improve the model’s problem-solving abilities.

2. The paper provides thorough experimentation across multiple benchmarks (DSEval, QRData), demonstrating consistent improvements in both general data science tasks and causal reasoning problems.

### Weaknesses
1. DSMentor’s performance may degrade when no similar questions exist in memory, and it lacks a clear strategy to handle novel tasks without prior examples. Additionally, as memory grows, retrieval efficiency may become an issue, but the paper doesn’t address how to manage this scalability challenge effectively.

2. The mentor agent’s ability to assign consistent difficulty ratings across diverse tasks is questionable. The generality of the Difficulty Scale Guidelines may lead to inaccurate assessments, especially for tasks that are too difficult for the mentor agent itself, risking hallucinated scores or poor curriculum design.

3. While the framework stores both correct and incorrect answers in memory, it’s unclear how incorrect answers contribute to future learning. This could lead to confusion if the model inadvertently learns from flawed data.

### Questions
1. How does DSMentor handle cases where no related or similar questions exist in the long-term memory? Would the model's performance degrade in such scenarios?

2. Why are traditional methods unable to effectively retrieve relevant datapoints from memory? What specific limitations do these methods have compared to DSMentor’s approach?

3. How large is the dataset used in DSMentor, and does each data point need manual labeling? If so, what is the process for labeling these data points, especially in large-scale datasets?

4. How does the mentor agent perform in generating difficulty scores across different tasks? Does it produce consistent and normalized difficulty ratings? Given the generality of the Difficulty Scale Guidelines in Figure 3, how does DSMentor ensure reliable and accurate difficulty assessments, especially for diverse task types?

5. The mentor agent’s effectiveness seems to rely on its ability to solve the task itself. What happens if the task is too difficult for the mentor agent, leading to incorrect or hallucinated answers and difficulty scores? How does DSMentor mitigate this risk?

6. As the long-term memory grows, how does DSMentor manage memory retrieval efficiency? What strategies are in place to prevent performance degradation when the memory size becomes too large?

7. What is the specific embedding model $ \varepsilon $ used for memory retrieval, and why is cosine similarity the metric of choice? How does this approach compare to other methods like Retrieval-Augmented Generation (RAG) for identifying relevant examples?

8. If the retrieved answer from long-term memory is incorrect, how does this contribute to improving future answers? Does DSMentor account for incorrect examples in a way that positively impacts performance?

### Soundness
2

### Presentation
3

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
The paper introduces DSMentor, which uses the same LLM in Mentor and Student roles to curate and solve an inference curriculum for Data Science tasks. (problem, attempt, evaluation) triplets are accumulated online into a long-term memory, which can be retrieved from to bring the top-k most similar problems into context. These problems can then be ordered within the context in terms of increasing/decreasing similarity, or increasing/decreasing difficulty (according to the difficulty labels used to form the easy-to-hard problem curriculum).

### Strengths
The paper demonstrates that the method generally outperforms several appropriate baselines and shows that the design is well-motivated through comprehensive ablations. Overall, the experiments are thorough and their presentation is clear.

Using learning curricula in the context of data science problems is well-motivated, given the way that complex tasks can be decomposed into simpler ones.

The method is simple and appears to be effective.

### Weaknesses
AIDE [1] is a leading baseline for data science LLM agents that has not been considered.

In-context curricula for LLMs have been used in several other settings [2, 3], which brings into question the novelty of this work. Especially, given that nothing about the method seems data science specific, besides the difficulty scale guidelines.

### Questions
The fact that the hard-to-easy curriculum does well on some tasks seems unintuitive; why do you think this is?

Why is the scope of the paper restricted to data science problems? Am I correct in my understanding that the method is largely domain-agnostic?

### Soundness
3

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
This paper investigates how the order of the problems affects the performance of data science LLM agents. Specifically, this paper proposes DSMentor, which first prompts LLMs to identify the difficulty of the problems in the dataset, and then solves them in the sequence of increasing difficulty on top of RAG. Experiments on DSEval and QRData demonstrate the effectiveness of the proposed framework.

### Strengths
- The presentation quality is good.
- The experiments are diverse.
- Open-sourced LLMs are considered for empirical evaluation.

### Weaknesses
1. The investigated setting seems unrealistic for me. There is rarely a practical scenario where a set of data science problems with diverse difficulties are given at the same time. For example, in industrial scenarios, the problems with different degrees of difficulties typically come one by one. Moreover, the executability (where LLM agents can obtain the realistic execution feedback) is the most informative feature in data science tasks. However, the setting investigated in this paper fully ignores this, further making the setting more unrealistic.

2. The contribution of this paper is limited. From the perspectives of techniques, I think this paper does not present sufficient novel insights.

- The proposed method of estimating the difficulty is trivial and resource-consuming: 1) How does the difficulty estimation of LLMs align with the ground-truth results? (Results of Pass-rate in Table 3 could have demonstrated this; however, it utilizes llama-8b instead of llama-70b, which fails to fully present this. ) 2) If the estimation is not precise enough, how does it affect the performance for DSMentor? 3) How many tokens (or time/computation resources) are consumed to estimate the difficulties for the whole dataset? Is this worthy enough for performance improvement?

- The order of retrieved examples in RAG has been already investigated in prior works (e.g., [1]); thus, it is not new for the community.

[1] Wang X, Wang Z, Gao X, et al. Searching for best practices in retrieval-augmented generation[J]. arXiv preprint arXiv:2407.01219, 2024.

- The most exciting part of data science task is machine learning, which involves lots of details such as feature engineering, model selection, hyper-parameter tuning. However, this paper seems not to report any results on this.

3. In Line 302-304, why is DSMentor run with three times? If temperature is set to 0 (which means greedy encoding), I cannot identify any randomness involved in this process.

4. In Table 5 and Table 6, it seems that Random (Inc. Similarity) achieves competitive results compared with DSMentor, while avoiding extra inference computation for estimating difficulties.

### Questions
How does DSMentor with relatively weak LLMs perform (such as llama-3.1-8B-instruct)?

### Soundness
1

### Presentation
3

### Contribution
1
