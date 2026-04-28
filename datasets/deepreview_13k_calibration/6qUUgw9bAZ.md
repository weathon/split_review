# Learning How Hard to Think: Input-Adaptive Allocation of LM Computation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Computationally intensive decoding procedures---including search, reranking, and self-critique---can improve the quality of language model (LM) outputs in problems spanning code generation, numerical reasoning, and dialog.
Existing work typically applies the same decoding procedure for every input to an LM. But not all inputs require the same amount of computation to process.
Can we allocate decoding computation \emph{adaptively}, using more resources to answer questions whose answers will be harder to compute?
We present an approach that 
predicts the distribution of rewards given an input and computation budget, then allocates additional computation to inputs for which it is predicted to be most useful.
We apply this approach in two decoding procedures: first, an \emph{adaptive best-of-$k$} procedure that dynamically selects the number of samples to generate as input to a reranker; second, a \emph{routing} procedure that dynamically responds to a query using a decoding procedure that is expensive but accurate, or one that is cheaper but less capable.
Across a suite of programming, mathematics, and dialog tasks, we show that accurate computation-allocation procedures can be learned, and 
reduce computation by up to 50\% at no cost to response quality, or improve quality by up to 10\% at a fixed computational budget.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an approach to adaptively allocate computational resources for language model (LM) decoding based on input difficulty. The authors propose a framework that predicts the marginal benefit of additional computation for each query, enabling dynamic adjustment of decoding procedures to maximize efficiency without sacrificing output quality. They demonstrate their method across tasks in math, code generation, and dialogue, achieving up to 50% reduction in compute usage in some cases. The paper also introduces two adaptive procedures—best-of-k sampling and routing between models of varying complexity—and provides a thorough evaluation using both online and offline allocation strategies.

### Strengths
- The paper adeptly formulates the "adaptive computation scaling allocation" in the context of LM decoding, addressing a topic that is both timely and relevant.
- The proposed computation-allocation framework is comprehensive, covering various cases and scenarios, including binary reward, pairwise optimization in routing, and both online and offline design considerations.
- The experiments conducted on three diverse and representative domains demonstrate the efficiency and efficacy of the proposed computation-allocation strategies.

### Weaknesses
 - The main concern is that the current computation-allocation solution is only evaluated in scenarios with identical distributions (i.e., the training data used to train the difficulty model comes from the same distribution as the test set). It is unclear whether the trained difficulty model generalizes to other distributions. The generalizability of the difficulty model is crucial for determining the practicality of the proposed computation-allocation framework.
- Following from the above, since the choice of LLMs does not seem to affect the evaluation of the proposed method’s efficacy, why not select a single fixed LLM, such as Llama3-7b-Instruct? By doing so, it might be easier to assess the generalizability of the method. (Please correct me if there is an issue with my understanding.)
- The implementation of the baselines is weak, with only one effective but not particularly practical baseline (best-of-k and random) in each scenario. Between the proposed method and these baselines, there are likely other reasonable approaches that could better demonstrate the effectiveness of the proposed framework.
- The related work section is too concise and lacks comprehensiveness, especially in the discussion of relevant adaptive computing research. Only one recently published paper is mentioned, which undermines the paper's completeness and contextual grounding.

### Questions
- Typos:
    - Line 352: "which in an" should be "which is an".
    - "LoRa" should be changed to "LoRA".
    - In Figure 1, "Large LM" should be changed to "large LM" for consistency.
- What's the definition of "N" in equation (10)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Presents an input-adaptive method for test-time compute-allocation. Decoding methods apply either sequential (eg weak vs strong model) or parallel compute (eg more samples in best-of-n). For a given method, this paper proposes to predict the marginal utility of every unit of computation, then use these predictions to optimize compute allocation. The paper proposes to predict these utilities given only the input.

The resource allocation problem can be solved in an offline manner given a fully observed dataset, referred to as online allocation in the paper, or solved via online access to only a partially observed dataset, referred to as offline allocation in the paper.

Experimental results across coding, math, and chat indicate that utility prediction is difficult at the extremes, and allocation decisions are sensitive to utility errors. Overall, adaptive allocation outperforms uniform or random allocations. The partially-observed strategy empirically often does better than the fully-observed case, possibly due to coarsening effects that hide errors in utility prediction.

### Strengths
The paper tackles a novel and timely problem, and offers a reasonable approach. The paper is clearly written.

### Weaknesses
A small criticism is the naming convention of online versus offline. Online optimization refers to "optimization problems having no or incomplete knowledge of the future (online)," which is not how online is used in this paper.

Other than that, this paper is a good step in improving adaptive test-time compute, identifying the importance of accurate utility estimation in problems with very low success rates. The paper's reliance on accurate utility prediction is a significant weakness, particularly at the extremes of the input space where the model's predictions are less reliable. This sensitivity to prediction errors can lead to suboptimal resource allocation, especially in scenarios where the marginal utility of computation varies drastically. The paper also does not fully explore the potential for error propagation when utility predictions are used sequentially, which could compound the impact of initial mispredictions.

### Questions
Drawing inspiration from the online secretary problem, it would be interesting to see how online estimation of pass rates for coding can aid utility estimation. For example, one could increase the total computation budget and, for each problem, reserving some of that budget to utility estimation. This would alleviate some of the burden from the prediction model.

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
This work proposes an input-adaptive computation allocation mechanism for improving the efficiency of test-time computation. The core idea is to train a model that predicts the distribution of rewards given a query and a budget. It incorporates training an MLP LM head and LoRA as the reward predictor that estimates the difficulty of a batch of queries. The proposed adaptive best-of-k outperforms the efficiency of standard best-of-k baselines in math, code, and chat domains. In addition, the author demonstrates the improvement in routing in terms of different model sizes and decoding schemes. The additional case study in inspecting the allocation of computation at different budgets is intriguing.

### Strengths
1. Scaling the test-time compute is effective but costly, this work contributes to a timely direction with a smart input-adaptive allocation scheme improving test-time efficiency.

2. The empirical improvement in efficiency is noticeable, and this work has covered adaptive allocation in representative popular subdomains: sampling, model size, and decoding method.

3. The presented analysis in Figure 6 is intuitive.

### Weaknesses
1. The selection of datasets and backbone language models may be questionable. I suspect this method should be ideally generalizable across tasks, however, only a single data in each domain is selected. I expect to see more tasks like HumanEval, MBPP for coding, Hendrycks MATH, and GSM for math. Meanwhile, for each domain, the author selects a specific backbone LM rather than the same choice across all tasks. This may raise concerns about the generalization of the proposed method. The lack of consistent evaluation across diverse datasets and models makes it difficult to ascertain the robustness of the proposed approach.

2. The underlying difficulty of this method is to actually train a very good difficulty estimator. However, the training difficulty, and the heavy training data resource requirement for learning a good reward predictor have not been explicitly discussed in the context. Moreover, it is highly dependent on the task, and I suspect the difficulty of some tasks will not be easy to predict. The paper lacks a detailed analysis of the computational overhead and data requirements for training the difficulty estimator, which is crucial for practical applications. The sensitivity of the estimator to different tasks and the potential for performance degradation on complex tasks are not sufficiently addressed.

3. The proposed method only considers the query for training the reward predictor. However, though there is a latency for querying the model, I suspect introducing $y$ will be more informative to reflect the difficulty of a task. The absence of response information in the reward predictor could limit its accuracy, especially for tasks where the initial query does not fully capture the complexity. The potential benefits of incorporating the model's initial response into the difficulty estimation process should be explored.

4. In Figure 3 (middle), besides the left bottom and right top clusters, the rest correlation appears to be relatively poor. Therefore, I suspect the efficiency gain could be mostly coming from predicting “unanswerable” for the queries in the left bottom regions and putting 0 costs there, also assigning a minimum budget to always correct questions. However, the middle region is actually the region that should benefit from a smart computation allocation scheme, and the correlation is not convincing here. The paper does not provide a detailed analysis of the correlation in the moderate difficulty range, which is critical for evaluating the effectiveness of the adaptive allocation scheme. The lack of strong correlation in this region raises concerns about the method's ability to effectively allocate resources for moderately difficult tasks.

### Questions
1. Though I understand using a query only to predict the reward should incur less latency, will $y$ be more informative and easier to train the predictor?

2. Could you please report the Spearman Correlation in Figure 3 (b, middle column)?  

3. Could you provide more clarification on the computing budget? Is it based on the inference calls?

I will be happy to raise my score if the author could address the aforementioned limitations and concerns.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for the adaptive allocation of decoding computation. By employing an LLM-based probe to predict the difficulty of a given query, the approach dynamically adjusts the allocation of decoding resources. The authors validate the method’s effectiveness across coding, math, and chat tasks. Results demonstrate that, under computational constraints, this approach outperforms the baseline BoK method.

### Strengths
1. This paper achieves efficient decoding from a different perspective, showing clear improvements over the original BoK method.
2. The authors apply their method across three distinct domains—code, math, and chat—demonstrating generalizability of their method.

### Weaknesses
1. In the experiments for code and math, the authors employ less-used benchmarks rather than widely adopted ones like HumanEval and MATH, raising concerns about the method’s applicability to broader tasks. The chosen benchmarks may not accurately reflect the complexities and nuances present in widely used benchmarks, potentially leading to an overestimation of the method's effectiveness. For instance, the coding tasks might lack the intricate dependencies and real-world constraints found in HumanEval, and the math problems might not cover the diverse range of mathematical reasoning required by MATH.

2. The paper's baseline comparison is limited to the BoK method, lacking comparative experiments with other stronger efficient decoding methods, such as Speculative Decoding. This narrow comparison makes it difficult to assess the true potential of the proposed method against state-of-the-art techniques. Speculative decoding, for example, leverages a smaller model to propose candidate tokens, which are then verified by a larger model, often resulting in significant speedups. Without comparing against such methods, it is unclear whether the gains achieved by the adaptive allocation are truly substantial or merely incremental improvements over a relatively weak baseline.

### Questions
1. Please explain the choice of benchmarks and how they compare to HumanEval and MATH in terms of difficulty distribution. Or please add more benchmarks like HumanEval and MATH. 

2. If a more complex decoding method, such as MCTS, is employed, would it necessitate retraining the probe? This could suggest a mismatch between the model's capabilities when using more advanced decoding methods and the probe's predictions. Additionally, it raises the question of whether the probe's prediction accuracy may be affected by factors such as varying prompts or decoding methods, and whether the probe demonstrates robustness under these conditions. Please explain the discuss the generalizability of the probe.

### Soundness
3

### Presentation
3

### Contribution
2
