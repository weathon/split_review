# DON’T STOP ME NOW: EMBEDDING BASED SCHEDULING FOR LLMS

- Decision: Accept
- Scores: 8, 5, 6, 5

## Abstract
Efficient scheduling is crucial for interactive Large Language Model (LLM) applications, where low request completion time directly impacts user engagement.
Size-based scheduling algorithms like Shortest Remaining Process Time (SRPT) aim to reduce average request completion time by leveraging known or estimated request sizes and allowing preemption by incoming jobs with shorter service times.
However, two main challenges arise when applying size-based scheduling to LLM systems. First, accurately predicting output lengths from prompts is challenging and often resource-intensive, making it impractical for many systems. As a result, the state-of-the-art LLM systems default to first-come, first-served scheduling, which can lead to head-of-line blocking and reduced system efficiency. Second, preemption introduces extra memory overhead to LLM systems as they must maintain intermediate states for unfinished (preempted) requests.

In this paper, we propose \algnospace{}, a method to obtain output predictions from the target LLM itself. After generating each output token, we recycle the embedding of its internal structure as input for a lightweight classifier that predicts the remaining length for each running request.
Using these predictions, we propose a prediction-based SRPT variant with limited preemption designed to account for memory overhead in LLM systems.
This variant allows preemption early in request execution when memory consumption is low but restricts preemption as requests approach completion to optimize resource utilization. On the theoretical side, we derive a closed-form formula for this SRPT variant in an M/G/1 queue model, which demonstrates its potential value. In our system, we implement this preemption policy alongside our embedding-based prediction method. Our refined predictions from layer embeddings achieve 2.66x lower mean absolute error compared to BERT predictions from sequence prompts. \alg{} achieves 1.66x to 2.01x lower mean latency on the Alpaca dataset and 1.76x to 24.07x lower mean time to the first token compared to the state-of-the-art serving system.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the challenges of efficient scheduling in interactive Large Language Model (LLM) applications. It uses a combination of length prediction and batching for speedup.  It introduces TRAIL, a method that uses the LLM’s own embeddings to predict the remaining length of requests, enabling a prediction-based Shortest Remaining Process Time (SRPT) variant with limited preemption. This approach aims to reduce memory overhead and optimize resource utilization by allowing preemption early in request execution and restricting it as requests near completion. Experiments show lower mean latency and time to the first token compared to current approaches.

### Strengths
1. The use of LLM embeddings for predicting residual request lengths, is novel, interesting, and intuitive. It has a clear potential to improve request scheduling as seen in the evaluation in this paper and can also be useful in any scenario where output length prediction is required and thus can have a broad positive impact.

2. The use of pre-emption based on length prediction has also not been fully explored in other works to the best of my knowledge. The authors propose a clear SRPT-like approach based on predicted request length and also make interesting observations about the extent of pre-emption that is useful (Fig 5) which will be useful for future research in this space.

### Weaknesses
1. The main algorithm is not very clearly explained although the issues are relatively minor and can be fixed by addressing questions 1-4 below.

2. By solely relying on length-based scheduling there is a risk of violating latency SLAs. In general, a real-world scheduler should be able to tune between FCFS and length-based scheduling to handle requests with different SLAs.

3. The evaluation is largely limited to the mean latency and does not adequately capture the tail behavior of the proposed approach or baselines. I would recommend including the corresponding P95 latency plots, along with comments, for Fig 5,6, and 7 to address this.

### Questions
1. It seems strange to take the average of prefill embeddings for inference. Is this the only approach you have tried, or did you try other (for e.g. non-linear) ways to aggregate the prefill embeddings?

2. What is 44? (shape of the embedding tensor after the prefill phase is [1,44,4096] as mentioned in Section 3.1 on page 4)

3. What is $\hat{q}_\text{prior}$? How is it initialized?

4. What is the LLM forward pass latency per token for the setting(s) in Table 1? Please include that number so we can get a clearer idea of the latency overhead of length prediction.

5. There appears to be an inconsistency in notation between 'C' in Section 3.3 and 'c' in Section 4.2. Please clarify if they are the same or different and fix the notation accordingly. Also do you have any ideas on how one could choose a good value of 'C'/'c' in real world? Can it be learned/adjusted in real-time based on the batch/request characteristics?

6. It is mentioned in Section 4.2 that vLLM-SJF_BERT prioritizes incoming requests over existing running requests. What does that mean? Shouldn't it be scheduling requests just based on the predicted length and not based on arrival time?  

7. I would recommend adding an oracle baseline where requests are scheduled based on their exact decode length. While the true decode length will not be known in practice, this will serve as a useful benchmark and approaches can be ranked based on how close they are to this one.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces TRAIL, a method for predicting the remaining output length of an LLM based on its internal structural embeddings. Using these predictions, the authors propose a scheduling algorithm, a variant of the shortest remaining processing time, to reduce latency. They derive the theoretical expected response time for a job and implement the scheduling policy within the vLLM serving system for evaluation.

### Strengths
The problem the authors address: the inefficiency of FCFS scheduling in LLM serving, is practical. Overall, I think the proposed solution is useful. Online token length prediction is inherently challenging, and their approach of using bins and classifiers is reasonable based on my experience. The feature design for the predictor is a novel contribution. The paper appropriately tackles key considerations in LLM serving, such as the uncertainty in output token length, the difficulty of making accurate predictions, the drawbacks of adding memory overhead during runtime decoding, and the distinction between the initial token generation (prefill) and the decoding of subsequent tokens.

### Weaknesses
Some terms could be more precise and consistent. For example, in the context of LLM serving, what the paper refers to as a “job” is actually a “request.” The term “job” typically implies a collection of multiple requests or tasks. While the authors note that “job” and “request” are used interchangeably, this distinction isn’t necessary and could lead to confusion. Additionally, the term “TRAIL” is described as a prediction method in the abstract but appears to refer to a scheduling policy in the evaluation section. This inconsistency should be clarified.

In Figure 6, the main experimental results show that the trends for Trail and Trail-BERT exhibit a faster growth rate compared to vLLM-FCFS and vLLM-SJF_BERT. Could you increase the request rate further to demonstrate whether the latency of Trail and Trail-BERT will remain below that of vLLM-FCFS and vLLM-SJF_BERT as the request rate continues to increase?

In multi-GPU settings with larger models, the results may differ due to the additional time required for initializing the Ray engine, GPU-to-GPU communication, and other overheads. While I believe the scheduling algorithm remains effective, it would be beneficial to evaluate its performance on larger models in a multi-GPU environment.

I'll raise the score if the authors successfully address the experiment issue.

### Questions
Could you explain why the performances of vLLM-FCFS and vLLM-BERT are so close in all metrics? Is it because that BERT prediction does not work at all, as shown in figure 3?

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
In this work, the authors propose a strategy for predicting output length that builds upon state-of-the-art approaches such as S3. The approach modifies output length prediction by leveraging embeddings from different layers of the LLM and providing them to a trainable, lightweight predictor module. These predictions are then used in conjunction with size-based scheduling approaches such as SRPT, resulting in reduced overall latency and TTFT. The key idea here is that length-aware scheduling reduces memory overhead and, consequently, preemptions.

### Strengths
A major strength of this paper is its output length prediction module, which iteratively refines predictions using embeddings from the LLMs. This approach enables the use of SRPT-based scheduling methods. The work also proposes two approaches for predicting output length and discusses the overhead associated with LLM inference. Additionally, the paper presents closed-form expressions based on queuing theory for mean response time.

### Weaknesses
The paper has a few weaknesses that should be considered. 
1. The output length prediction assumes uniform bucket sizes, which may lead to overfitting if the number of requests in each bucket varies significantly. A comprehensive evaluation of the distribution per bucket is required for a fair evaluation of this approach. 
2. The assumption that the output length predictor needs access to the layers of the LLMs may not hold for many OpenAI models, whose internal architecture is unknown. The generalizability of the approach in such cases needs to be discussed. 
3. Finally, some tasks from the Alpaca dataset are more unpredictable than others. For instance, tasks such as writing a story are far more arbitrary than classifying a sentence. Therefore, remarks on the performance of the approach with respect to different tasks should be added for better generalizability.
4. It is unclear whether a certain layer carries most of the information about the output length for every LLM, or if this is a generic assumption that may not hold for all models

### Questions
1. Can the generalizability of this approach across different LLMs be evaluated? Is it a generic assumption that for every LLM, a certain layer carries most of the information about the output length, or could this vary depending on the model?
2. How can this approach be applied in the cases of OpenAI models where the internal architecture is unknown?
3. What is the output length distribution used in the paper, and how would the performance vary if the buckets are selected based on their size?
4. Can the paper provide more information on the Alpaca dataset, and what was the distribution of the data used with respect to the root verb of instructions from the Alpaca dataset?
5. How does the paper ensure that the performance of the approach is consistent across different tasks within the Alpaca dataset, given that some tasks may be more unpredictable than others? Can the authors provide the breakdown of the MAE and heatmap with respect to different root verbs of instructions?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors address the scheduling of LLM inference jobs. In particular, to provide a high-quality experience, LLM inference should be fast enough to allow real-time conversational user interaction. Scheduling jobs according to their length has since long been shown to minimize average waiting time, but it requires knowing the length of jobs in advance. Due to its autoregressive nature, LLM-based text generation can lead to highly varying execution times. To overcome this limit, related work proposes various models to predict the length of LLM inference. The authors here improve on this by, rather than using smaller LLM models such as BERT-like ones, predicting the inference length based on the state of the internal layers of the LLM. Moreover, the authors also address the drawback of job preemption, which requires saving intermediate state, which can be considerable for modern LLMs with consequent issues of either exhausting GPU memory or costly memory transfers, by only allowing preemption at the initial steps of a job. In contrast, jobs close to termination can not be preempted. The authors evaluate both the accuracy of their intermediate layer-based job length prediction and preemption-tuned scheduling against three baselines covering vanilla and state-of-the-art solutions.

### Strengths
+ Significantly lower mean latency compared to the considered baselines.
+ The model used to predict the LLM output length is way simpler than the ones used by SOTA-related work, which reduces the overall computational burden of LLMs (especially in the context of energy efficiency over the whole sector). 
+ Theoretical proof of the proposed scheduling scheme with limited preemption and dynamic threshold to adapt to the variability of inference lengths.

### Weaknesses
 - Layer-based prediction only tested on one LLM, which makes it unclear how well the method generalizes to other LLMs.
- The choice of the layer used for prediction is model-dependent and requires a preliminary study.
- A deeper sensitivity analysis of the parameter c would have been nice to analyze the optimal value for c better.
- Lack of some design rationales (see questions below)

To give more meaning to the average prediction error presented in Figure 2, it woudl have been nice to provide soem statistics on the inference length.

### Questions
The rationale for the number and size of bins for predicting the LLM inference length is missing. What is the mean length of responses? New models have significantly larger contexts. Does this influence the choice? How? Also, would it not make more sense to choose a divider of 512 instead of ten (e.g., 8 or 16) since length is intrinsically an integer?

Learning rate decreased to 0 does not seem to make much sense. I guess it is close to 0. Please check.

Length prediction overhead is small in relative terms but could be significant in absolute terms, especially from an energy point of view. It would be nice to comment on this. Also, how are batches accumulated in this scenario since you want to predict after each next token has been generated? What is the prediction time with a batch size of one?

### Soundness
3

### Presentation
3

### Contribution
2
