# SpecDec++: Boosting Speculative Decoding via Adaptive Candidate Lengths

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Speculative decoding reduces the inference latency of a target large language model via utilizing a smaller and faster draft model. Its performance depends on a hyperparameter $K$ --- the candidate length, i.e., the number of candidate tokens for the target model to verify in each round.
However, previous methods often use simple heuristics to choose $K$, which may result in sub-optimal performance. 
We study the choice of the candidate length $K$ and formulate it as a Markov Decision Process. We theoretically show that the optimal policy of this Markov decision process takes the form of a threshold policy, i.e., the current speculation should stop and be verified when the probability of getting a rejection exceeds a threshold value.
Motivated by this theory, we propose \ours, an enhanced version of speculative decoding that adaptively determines the candidate length on the fly. We augment the draft model with a trained acceptance prediction head to predict the conditional acceptance probability of the candidate tokens. \ours will stop the current speculation when the predicted probability that \textit{at least one token gets rejected} exceeds a threshold.
We implement \ours and apply it to the llama-2-chat 7B \& 70B model pair. 
Our adaptive method achieves a 2.04x speedup on the Alpaca dataset (an additional 7.2\% improvement over the baseline speculative decoding). On the GSM8K and HumanEval datasets, our method achieves a 2.26x speedup (9.4\% improvement) and 2.23x speedup (11.1\% improvement), respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduced an enhancement of speculative decoding by predicting the candidate length on the fly. The algorithm is inspired by a framework that optimizing a corresponding Markov decision process, where an small neural network is trained to predict an optimal threshold. In the experiments, it shows around 10% improvement over vanilla speculative decoding on llama-2 chat 7B& 70B pair.

### Strengths
**Theoretical Soundness:** The paper is theoretically grounded, providing a solid foundation for the proposed approach.

**Ease of Implementation:** The method is straightforward to implement, which adds to its practical appeal and accessibility.

### Weaknesses
**Limited Practical Improvement:** The reported improvement over vanilla speculative decoding appears minimal, with only a 10% speedup for a large model. Moreover, vanilla speculative decoding is significantly slower than state-of-the-art methods like Medusa [1] and Eagle [2], raising questions about the method's practicality, especially given the additional complexity of training a candidate length prediction model. In terms of theoretical analysis, while the optimal strategy is presented as a threshold function, the threshold’s dependency on both target and source models makes it unclear how a fundamentally residual model can capture this relationship, as the input only includes the context.

**Insufficient Experimentation:** The experiments are limited to a single pair of models and model sizes, which leaves the method’s generalizability unaddressed. It remains unclear if the speedup improvement would increase, decrease, or remain stable with varying model sizes, making it difficult to assess its applicability across different model configurations.

**Lack of Comparisons with State-of-the-Art:** The paper only compares the method against baseline speculative decoding without benchmarking it against more advanced methods. It would be valuable to know if this method could be combined with other speculative decoding techniques and how it performs relative to them.

[1] Cai, Tianle, et al. "Medusa: Simple llm inference acceleration framework with multiple decoding heads." arXiv preprint arXiv:2401.10774 (2024). 

[2] Li, Yuhui, et al. "Eagle: Speculative sampling requires rethinking feature uncertainty." arXiv preprint arXiv:2401.15077 (2024).

### Questions
- **Training and Parameter Overhead:** How long does it take to train the additional candidate length prediction model? Understanding the time and resource requirements for training this predictor would clarify the overall cost-benefit of the method.

- **Transferability and Generalizability:** Is the predictor transferable or generalizable to other model pairs, or does it require retraining for each new model configuration? Insights on its adaptability would help assess its practicality across different use cases.

- **Performance with Varied Model Pairs:** What is the performance of the method on other model pairs with varying sizes? Testing across different model sizes and configurations would provide a clearer picture of its scalability and effectiveness.

- **Comparison with Other Speculative Decoding Strategies:** How does this method perform relative to other state-of-the-art speculative decoding strategies? It would be valuable to see comparisons with existing methods to better understand its competitive edge.

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
4

### Summary
the paper proposed learning based method for generating adaptive candidate lengths for Speculative Decoding (SpD) algorithm.  SpD algorithm is used for lossless inference acceleration by using a small draft model (run autoregressively) and large target model (run in parallel). The candidate length is usually fixed during SpD run, however, this candidate length affects the speed-up observed with SpD. A fixed candidate length can harm the speed-up depending on the downstream task and the size of the draft model leading to wasteful candidate token generation. The authors train an additional head for predicting when to stop the draft model from generation.

### Strengths
The paper solves an existing problem of draft token generation through a learning based method which is interesting as opposed to non-learning based heuristics or hyper-parameter search of fixed draft length.

The motivation for an adaptive draft length is explained well shown with an ideal case example, with proper definitions to discard rate and verification rate.

The training of the additional draft head for predicting draft token generation stop or continue is well explained.

### Weaknesses
Though the paper solves an important problem by a learning-based approach the overall gains seem small (7% - 11%) over vanilla speculative decoding. 

The paper has not compared with existing heuristic based adaptive draft length methods which use either draft entropy or other confidence scores for stopping or continuing the draft generation 

The hyper-parameter search required for finding the w_{reject} and probability threshold is an additional set of hassle also present in vanilla SpD, in this regard it seems like it could be better to simply try vanilla SpD with multiple draft lengths on a small subset of downstream task and then choose one with best performance for entirety of the task. 

Lack of comparison with different draft models (TinyLLama-1B) and other models available like OPT-family

Only a single draft model of size 7B was tried, it would be interesting to see what happens to this method with TinyLLama (1B Llama model) and other small llama models.

### Questions
Can authors compare their method with non-learning based adaptive draft length approaches? 

Can authors compare with other draft models and/or draft-target model families? 

Can same adaptive candidate-length draft head be used if the hidden dimension is same for different models or do we need to retrain the adaptive candidate-length draft head? (is the newly trained draft head transferable to different model?)

Extra: why are diffusion models mentioned in the Appendix section B without any relation to adaptive draft length? 

Also do the authors have any comments on the future work or what other research problem their work opens?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new speculative decoding method called SpecDec++, whose main contributions are formalizing the candidate length selection problem as a Markov Decision Process (MDP) and dynamically adjusting the number of candidate tokens. This is achieved through a well-trained acceptance prediction head that predicts the conditional probability of candidate tokens being accepted by the target model. The method demonstrates substantial speedup over baseline speculative decoding approaches with fixed candidate lengths.

### Strengths
1、Speculative decoding is of significant importance for improving the inference efficiency of large language models.

2、The paper provides sufficient justification in theoretical analysis by modeling the problem as an MDP and proposing a threshold policy, which offers a solid theoretical foundation for dynamically adjusting the candidate length.

3、By reducing the number of forward passes of the target model and decreasing the number of discarded tokens, SpecDec++ achieves faster inference speed compared to the baseline.

### Weaknesses
1、The paper aims to accelerate inference by reducing the number of forward passes of the target model and decreasing the number of discarded tokens, but the experiments show only a modest improvement over the baseline. Moreover, the training cost for the head is substantial. I wonder if these two aspects are not the key bottlenecks of speculative sampling, or if this method is not very effective in addressing these issues. This makes me somewhat skeptical about the effectiveness of this approach.

2、The paper introduces two evaluation metrics to demonstrate the effect of dynamically adjusting the candidate token length, but the length of accepted tokens is also a crucial metric. I am not sure if this method has any impact on the length of accepted tokens.

3、The paper only presents results on the llama-2-chat 7B and llama-2-chat 70B models. I suspect this is due to the high training costs, but a single set of results is less convincing.

### Questions
1、Are there other methods to reduce the training cost, or are there alternative approaches to determine whether to stop the draft model's generation?

2、The paper claims that the method can be seamlessly integrated with other improvements. Could at least one example be provided for experimentation?

3、It would be desirable to conduct experiments on a broader range of models.

### Soundness
3

### Presentation
3

### Contribution
2
