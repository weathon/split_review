# DiverseAgentEntropy: Quantifying Black-Box LLM Uncertainty through Diverse Perspectives and Multi-Agent Interaction

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Quantifying the uncertainty in the factual parametric knowledge of Large Language Models (LLMs), especially in a black-box setting, poses a significant challenge. Existing methods, which gauge a model’s uncertainty through evaluating self-consistency in responses to the original query, do not always capture true uncertainty. Models might respond consistently to the origin query with a wrong answer, yet respond correctly to varied questions from different perspectives about the same query, and vice versa. In this paper, we propose a novel method, DiverseAgentEntropy, for evaluating a model's uncertainty using multi-agent interaction under the assumption that if a model is certain, it should consistently recall the answer to the original query across a diverse collection of questions about the same original query. We further implement an abstention policy to withhold responses when uncertainty is high. Our method offers a more accurate prediction of the model's reliability and further detects hallucinations, outperforming other self-consistency-based methods. Additionally, it demonstrates that existing models often fail to consistently retrieve the correct answer to the same query under diverse varied questions even when knowing the correct answer.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose a novel method for LLM's uncertainty estimation, which quantifies the LLMs' uncertainty based on the consistency of responses across diverse questions after multi-agent interaction.

### Strengths
1. This paper is well-written. The structure is clear and easy to follow.

2. The idea of measuring UE of LLM via different perspective from different agents is clear and make sense.

3. The design of method is also clear and reasonable.

### Weaknesses
1. Achieve UE by considering the multiple results from various aspect (multiple agents in this paper) is not very new and novel compared to some recent papers: Knowing What LLMs DO NOT Know: A Simple Yet Effective Self-Detection Method（NAACL 2024）, SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. (EMNLP 2023)

2. It would be more solid to compare with some more recent baselines. The baselines are mainly in 2023 or eailer. SC is a very basic baseline model. As uncertainty estimation (UE) is becoming hot recently, there should be some advanced baselines, such as "Know-
ing What LLMs DO NOT Know: A Simple Yet Effective Self-Detection Method". In NAACL

3. From the experimental results shown in Tables 1 & 2, the proposed model cannot always excel the performance of baselines (In table 1 & 2).

4. The related work section should be enriched to provide a more comprehensive overview of related research.

### Questions
None

### Soundness
3

### Presentation
4

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
This paper proposes a new method for estimating the uncertainty of language model outputs. 
There are two core steps: 
1. Prompt the model to answer a set of equivalent but diverse questions from different perspectives. 
2. Allow agent interaction by prompting the LLM to reconcile each pair of different answers from the first step. 

The uncertainty of each semantically unique answer is then their weighted frequency, where the weightage is how frequently the agents changes its answer during the second step of agent interaction. 

The experiments are done on two models (Claude-3-Sonnet and Llama-3-70b-Instruct) on several QA datasets, and the metrics focus on selective prediction performance. Results show that the proposed method is better than the Self-Consistency baseline which simply takes majority vote the multiple sampled solutions. 

My biggest concern about this work is its limited novelty. The proposed method feels similar to existing multi-agent debate work, combined with the sef-consistency and semantic entropy ideas (which are not new either). The authors should better highlight what's the novelty contribution of their proposed framework as compared to existing works.

### Strengths
- The paper is generally well-organized and clearly written. 
- The experiments are reasonably thorough, with comparisons to many relevant baselines.

### Weaknesses
1. Limited novelty. 
It seems every step of the proposed framework is not new. 
For generating paraphrased/equivalent questions and checking answer consistency, there is "SAC3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency" (EMNLP'23). For multi-agent debate, there is "Improving Factuality and Reasoning in Language Models through Multiagent Debate" (ICML 2024). For aggregating diverse answers into uncertainty scores, there is "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation" (ICLR 2023). So it seems to me that the proposed framework is a combination of known techniques for the calibration problem. This feels too incremental for the ICLR standard. 

2. Some nitpick about how you reported the results. I think using AUC as the main metric is fine since you mostly target calibration / selective prediction. But I think you should include all the baselines in Table 1 to contextualize the results of your proposed method. Ideally you might also include a column for cost / number of inference calls. The different metrics in Table 2 are starting to get a bit confusing to me. Why not still use AUC or metrics like Cov@Acc? (E.g., see "Selective Question Answering under Domain Shift" ACL 2020).

### Questions
N/A

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
4

### Summary
This paper presents a novel method, named DIVERSEAGENTENTROPY, to quantify the uncertainty of LLMs. The assumption is that: if the model is certain of its answer to a query, it should consistently provide the same answer across variants of the original query. In the proposed method, given a new query, varies questions are generated using LLMs. Each agent will answer a unique varied question independently, then interact with another agent in a controlled cross-play one-on-one manner. The final uncertainty is calculated to obtain the final answer. Extensive experiments are conducted to test the performance of the proposed method.

### Strengths
* Overall, the paper is very clear and easy to follow. 
* The paper focuses on an emerging problem in the era of LLMs. In the proposed method, the LLM is viewed as a black-box. Therefore, the proposed method can be easily applied to other LLMs. 
* The paper is well-motivated. The examples in Fig. 1 describe the problem well. 
* The experiments are very comprehensive to validate the performance of the proposed method.

### Weaknesses
My main concern is the extra LLM calls in the proposed framework, which may limit the practicality of the proposed method. As discussed in Appendix A.1, the number of LLM calls is much higher than the self-consistency-based approaches. In addition, there are dependencies among the tasks in round 1 -- independent QA and round 2 -- 1-1 interaction, and each round of interaction in round 2, which will make the latency cost higher.

### Questions
1. When generating the varied questions, how can we ensure the answer of the generated question is the same as the original query? 
2. In line 223, how is the answer extracted from the response? 
3. In line 231, how is the difference between the answers measured? Since LLM may output a full answer (as shown in Table 8), or add unnecessary information in the response, will an answer extraction be applied after each 1-1 interaction? 
4. To make the round 2 1 - 1 interaction (as described in line 233-234) more clear, will it be good to share the prompt template?
5. This work focuses on the factual parametric knowledge of LLMs, are there any insights on whether the method can be applied to RAG?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DIVERSEAGENTENTROPY, a novel method for quantifying uncertainty in Large Language Models (LLMs) through multi-agent interaction. Unlike traditional self-consistency methods that rely on repeated sampling of the same query, this approach generates diverse questions about the same underlying fact and creates multiple "agents" from the same base model to answer these questions. The method showed a 2.5% improvement in accuracy compared to existing self-consistency approaches and revealed important insights about LLMs' ability to consistently retrieve knowledge across different contexts.

### Strengths
1, This paper introduces a more comprehensive approach to uncertainty estimation that goes beyond simple self-consistency
2, the experiments are across multiple datasets and model types. The results are promising

### Weaknesses
1, Requires significantly more computational resources (5x more API calls) compared to traditional methods
2, it is primarily tested on factual question-answering tasks and may not generalize well to other types of language tasks

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3
