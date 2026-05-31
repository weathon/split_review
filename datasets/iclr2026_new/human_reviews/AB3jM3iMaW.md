## Human Reviewer 1

### Summary
The paper proposes an approach for future link prediction in temporal graphs (called link forecasting). It finetunes an LLM (Qwen3-4B) for this task via reinforcement learning. All textual data is removed from the graphs and replaced by IDs.

### Strengths
- Original idea of using LLMs for link forecasting
- Strong results compared both to other LLMs and compared to TGNNs
- Explanation traces are provided and evaluated in a user study
- Paper is well-structured

### Weaknesses
- The motivation for using an LLM remains unclear (apart from some success in preliminary work)

### Questions
- What is the motivation of using an LLM if all textual data is removed?
- Do you have a hypothesis why your approach works so well despite removing all textual data?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper constructs temporal graphs in natural language and finetunes LLMs with reinforcement learning on the dataset. The finetuned model outperforms larger LLMs under the proposed pMRR and LLM-as-a-Judge metrics.

### Strengths
The paper presents that the reasoning ability of LLMs on temporal graphs can be enhanced by RL training, which is not explored by previous works of LLM on temporal graphs, which mainly focus on evaluation and ICL. The full pipeline, from data construction to training and evaluation, is reasonable and easy to follow.

### Weaknesses
The main weakness is a lack of innovation and further insights. The idea that the graph reasoning ability of LLMs can be incentivized through reinforcement learning has been illustrated in previous work. Although the authors claim that previous works focus on static graphs while they target temporal graphs, they don't show what difference it will bring to the reasoning or further insights (e.g., what is special for temporal graphs but not static graphs). In the whole pipeline, the innovation is quite limited. For example, the algorithm is the well-established GRPO, and the LLM-as-Judge evaluation is also commonly used.

### Questions
1. The base models only include Qwen3-4B and Qwen3-0.6B. What's the performance of the model finetuned from a larger Qwen3-8B?

2. What's the performance of the ReaL-TG models on OOD benchmarks, e.g., unseen temporal graph benchmarks?

3. Does the training harm or enhance the general reasoning ability of base models, e.g., the math benchmarks?

4. How does the RL training increase the reasoning of LLMs on temporal graphs? Can you show some intuitive examples?

5. The reason for proposing pMRR is to evaluate the over-generation of LLMs. Can the recall in F1 play a similar role?

6. Why don't you use the proposed metrics as rewards during RL training?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces Real-TG, which employs reinforcement learning with verified rewards (LRVR) like GRPO to fine-tune an LLM for more effective explainable link forecasting on anonymized temporal graphs. It formulates the link forecasting as the QA tasks and designs a specific prompt to instruct LLMs to identify the destination node. The authors also propose a metric (i.e., pMRR) to evaluate the prediction capability of LLMs (as LLMs can provide discouraging over-generation). Extensive experiments show that Real-TG-4B achieves good results across different vanilla LLMs and traditional link forecasting methods.

### Strengths
* The idea of introducing LRVR to LLM-based temporal graph models is interesting.
* The proposed fine-tuning paradigm, Real-TG, is simple and effective.
* The paper is well-written and easy to follow.

### Weaknesses
* The novelty of the proposed Real-TG is limited and lacks technical innovation. In Real-TG, the QA formulation [1], the GRPO pipeline [2], the $\alpha$-temporal random walk [3], and the LLM-as-a-Judge evaluation [4] are introduced from existing works. All these mechanisms resemble existing works and do not introduce principled advances in LLM-based temporal graph learning or RLVR.
* The motivation of the model component design is unclear. 
	* Why is RL chosen instead of SFT? In the literature on large reasoning models, RL is typically used to optimize preferences or human-aligned objectives; however, for tasks with a single correct answer, SFT may be more appropriate. The authors should clarify why RL is necessary and what concrete benefits it confers in this setting.
	* Why adopt $\alpha$-temporal random walks rather than simpler k-hop neighborhoods?
	* Why use F1 as the reward metric rather than other ranking/IR metrics (e.g., MRR)? In equation 1, do the authors compute this F1 over a single pair of samples, since F1 fundamentally requires aggregation over multiple samples? An illustrative example may help with a better understanding of the paper.
* The GRPO procedure is known to be sensitive to hyperparameters. Does Real-TG also suffer from such instability?
* Plots showing reward vs. training step would greatly strengthen confidence in the RL training procedure.
* Why not conduct experiments in the recently proposed benchmark [5] and compare the models that also utilize LLMs for temporal graph learning [6]?

[1] Are Large Language Models Good Temporal Graph Learners?

[2] DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

[3] Zebra: When temporal graph neural networks meet temporal personalized pagerank

[4] Judging Llm-as-a-judge with Mt-bench and Chatbot Arena

[5] DTGB: A Comprehensive Benchmark for Dynamic Text-Attributed Graphs

[6] Unifying Text Semantics and Graph Structures for Temporal Text-attributed Graphs with Large Language Models

### Questions
No

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 4

### Summary
The paper tackles link forecasting on temporal graphs, emphasizing explainable predictions using large language models that generalize to unseen graphs without retraining. It introduces ReaL-TG, a reinforcement learning framework that fine-tunes LLMs with Grouped Regularized Policy Optimization and an outcome-based F1 reward to encourage self-exploration of reasoning strategies from graph structures. Core contributions include the Temporal Context Graph Selection algorithm for relevant subgraph extraction, a QA formulation for the task, and a new evaluation protocol featuring penalized mean reciprocal rank alongside an LLM-as-a-Judge system assessing faithfulness, logical consistency, and answer-explanation alignment. Main results demonstrate that the fine-tuned ReaL-TG-4B model outperforms larger frontier LLMs and traditional temporal graph neural networks on prediction metrics and reasoning quality across seen and unseen datasets from the Temporal Graph Benchmark.

### Strengths
- The paper introduces ReaL-TG, a complete RL-based framework designed to fine-tune LLMs for explainable link forecasting on temporal graphs. This is a novel approach to a task where prior methods lacked explainability.
- The experimental results are impressive. The fine-tuned 4B model (ReaL-TG-4B) significantly outperforms its base model (Qwen3-4B) and, notably, much larger frontier LLMs like Llama3.3-70B and GPT-5 mini on overall prediction accuracy.
- The framework demonstrates excellent generalization. ReaL-TG-4B achieves the highest MRR and PMRR on the two "unseen" TGB datasets, outperforming all baselines.
- The paper successfully demonstrates that ReaL-TG not only improves prediction accuracy but also reasoning quality.

### Weaknesses
- The paper provides an insightful observation of "reward hacking" in the smaller ReaL-TG-0.6B model, which "justifies its predictions by claiming '(uq, vq, tq) has already been seen'". This is a critical finding for outcome-based RL methods. Despite its importance, this phenomenon is not systematically measured. The paper provides no evidence or quantification to demonstrate it.
- The approach injects graph context purely as text; while explainable, it may drop important structural cues vs. learned embeddings.
- Relies solely on six TGB datasets, which may share similar characteristics like social or transaction networks, limiting generalization claims.
- Training data sampled from only four datasets with 1,000 queries, potentially insufficient for diverse temporal patterns.
- Unseen datasets (uci, enron) are smaller, with fewer involved nodes, possibly underrepresenting complex scenarios.

### Questions
- Your definition in Section 4 states PMRR penalizes over-generation, resulting in a lower score than MRR. However, in Table 2, several large baseline models (e.g., Llama3.3-70B, GPT-5 mini) show a PMRR score that is higher than their MRR score. Could you please confirm if the description of PMRR in Section 4 is correct, or explain the mechanism by which over-generation leads to a higher PMRR score.
- Could you please briefly elaborate on the path that makes $(e_2, t_2)$ a 3-hop neighbor in the context of Figure 2? 
- Can you clarify how the termination probability $\alpha$ and the decay factor $\beta$ interact in the random walk?
- Why was the F1 score chosen as the reward function? Did F1 prove uniquely robust to this hacking behavior?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4