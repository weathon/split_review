# Conformal Language Model Reasoning with Coherent Factuality

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Language models are increasingly being used in important decision pipelines, so ensuring the correctness of their outputs is crucial. Recent work has proposed evaluating the “factuality” of claims decomposed from a language model generation and applying conformal prediction techniques to filter out those claims that are not factual. This can be effective for tasks such as information retrieval, where constituent claims may be evaluated in isolation for factuality, but is not appropriate for reasoning tasks, as steps of a logical argument can be evaluated for correctness only within the context of the claims that have preceded them. To capture this, we define “coherent factuality” and develop a conformal-prediction-based method to guarantee coherent factuality of language model outputs. Our approach applies split conformal prediction to subgraphs within a ``deducibility" graph that we construct to represent the steps of a reasoning problem. We evaluate our method on mathematical reasoning problems from the MATH and FELM datasets, and find that our algorithm achieves coherent factuality across target coverage levels, consistently producing orderings of correct claims that are substantiated by previous ones. Moreover, we achieve 90\% factuality on our stricter definition while retaining 80\% or more of the original claims, highlighting the utility of our deducibility-graph-guided approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper defines “coherent factuality” of language model for reasoning tasks and applies a conformal prediction to guarantee coherent factuality. In addition to the split conformal prediction proposed by (Mohri & Hashimoto, 2024), this work proposes a deducibility graph by employing the “deducibility” property instead of “partial entailment” to take in claims by the ground truth. This criticizes that the previous work focuses solely on independent factuality, which makes the strong assumption that sub-claims are independent. Coherence factuality is applied to mathematical reasoning problems such as MATH or FELM, filtering the sub-graphs with the desired coherence factuality.

### Strengths
This paper clearly points out that existing conformal factuality is not appropriate for reasoning tasks, and suggests deducibility graph and conformal prediction with coherence factuality. In addition, this experimentally achieved the desired correction and substantiation by applying conformal prediction to the newly defined coherence factuality.
This also proposes a claim-scoring function that considers the graph and reflects the confidence along descendants well.

### Weaknesses
It seems to be sufficiently appealed that coherence factuality is more necessary for reasoning tasks than independent factuality. However, if bad claims, as mentioned in the sentence below, are accepted because they are consistent, wouldn't that be of no help in resolving hallucination? I think additional explanations about coherence factuality or deducibility more than as defined in the paper.
"Our definition of deducibility graphs permits the arbitrary treatment of claims that do not follow from the
ground truth".
Similarly, all qualitative results were drawn from the MATH dataset, which has only true claims as far as I know. It appears that additional qualitative results that include bad claims with coherence factuality are needed.

Additionally, an approximate deducibility graph is obtained by creating graph proxies using GPT-4o, but this does not provide theoretical guarantee, which is also mentioned in the paper. This paper said that these graph proxies provide a benefit in imposing the property called dependency, but as mentioned above, it does not come as a big advantage if bad claims are considered, so it appears that the theoretical guarantee of conformal prediction is not fully utilized.

### Questions
As mentioned above, are there any results from experiments using a human annotated ideal graph other than GPT-4o?

Although it seems sufficiently argued that coherence factuality is more necessary than independent factuality for reasoning tasks, if bad claims are accepted because they are consistent how would this help in addressing hallucination issues?

Are there extra qualitative results for other datasets (e.g., FELM)?

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
2

### Summary
The paper defines “coherent factuality” and develops a conformal-predictionbased method to guarantee coherent factuality of language model outputs for reasoning tasks, where claims need to be substantiated and outputted in a comprehensible order to ensure correctness as well as coherence. In addition, they evaluate the method on MATH and FELM datasets, and verify the effectiveness of the method.

### Strengths
Several recent works used conformal prediction to verify the correctness of the generation of LLMs with a strong assumption that the factuality of a claim can be independently evaluated. In order to generalize the method to reasoning domains, where claims need to be substantiated and outputted in a comprehensible order, the paper defines a new notion of factuality ”coherent factuality” and develops a conformal-predictionbased method to guarantee coherent factuality of language model outputs. The paper verified the proposed method on MATH and FELM datasets by comparing the results of the baseline proposed in (Mohri & Hashimoto, 2024).

### Weaknesses
It is not clear how to create and use $C_{true}$ in the experiments on MATH and FELM datasets. The paper said in Line 150 “In practice, we might choose some reference like Wikipedia or a math textbook as our ground truth”, however, there is no statements about $C_{true}$ in the experiments.

The paper uses GPT4o to generate the graphs, but the quality of the graphs is unknown.

In addition, the proposed method can obtain both coherent factuality and independent factuality of the LLM output, however, there is no experiment to demonstrate whether there is an impact on the performance of downstream tasks. Or can the proposed method improve the performance of the downstream tasks?

### Questions
see the weaknesses.

### Soundness
2

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
This work presents a conformal prediction framework for LLMs on reasoning tasks. The key difference between this work and previous work is the consideration of dependencies between claims. Unlike previous framework that scores and removes each claim independently, the proposed framework generates graph with each node representing a claim in the response, and then score and remove the claims while considering the graph structure. On MATH and FELM, the proposed method shows better calibration and stronger guarantee compared to previous methods and a few simpler baselines.

### Strengths
1. Extending the conformal prediction framework to reasoning problems is an important direction. The idea of considering the dependency structure among the claims is straightforward and effective.
2. The proposed framework is simple to implement and shows stronger performance than baselines in the experiments.

### Weaknesses
1. This writing of this paper can be substantially improved and in general should be more rigorous. There are a number of writing issue in this paper making this paper a bit hard to understand. To list a few:
    * One key property of the ideal graph is it uses the "minimal set of the claims". However, this is only mentioned in the appendix.
	* What is the "graph G" at LINE 350? Is it the corresponding subgraph to each node?
	* LINE 402 points to appendix F, but appendix F does not contain the prompts.
	* Figure 4(b) and 4(c) use the same title. This is confusing and seems to be typos.
	* What is "Descendants weight boosting" in LINE 501?
	* What is "independently filtered outputs" in LINE 509?
	* What is "self-consistency scoring" in LINE 970?
	* I don't understand the sentence from LINE 316-318.
	* The graph generation step is a critical part of the proposed method, but all the details are in the appendix. I can understand the specific prompt to be in the appendix, but there need to be some high-level descriptions in the main paper.
2. Reasoning problems are different from general fact-related questions as they often-times require a single correct conclusion. While it's still useful to provide partially correct responses, it is important in this case to also report (e.g., through human studies) how many of the responses actually contain the correct answer, or how useful these responses are after filtering.
3. The proposed method is only tested on one model (which I believe is GPT-4o, but the paper does not explicitly mention where the model responses on MATH come from). It would be great to test at least one more model to see how generalizable the proposed framework is. If the authors can use open-source models, it will also greatly improve the reproducibility of this paper.

### Questions
1. Why do you use "median" in LINE 361? And how do you select the hyper-parameter $\beta$?
2. Do you make any special design to deal with the cases in LINE 153 (i.e., "it is not reasonable to do so in a proof of that fact")?

### Soundness
2

### Presentation
2

### Contribution
2
