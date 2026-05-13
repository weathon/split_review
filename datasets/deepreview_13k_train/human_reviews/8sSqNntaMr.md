# RouteLLM: Learning to Route LLMs from Preference Data

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost. More powerful models, though effective, come with higher expenses, while less capable models are more cost-effective. To address this dilemma, we propose several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality.  We develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance. Our evaluation on widely-recognized benchmarks shows that our approach significantly reduces costs—by over 2 times in certain cases—without compromising the quality of responses. Interestingly, our router models also demonstrate significant transfer learning capabilities, maintaining their performance even when the strong and weak models are changed at test time. This highlights the potential of these routers to provide a cost-effective yet high-performance solution for deploying LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces RouteLLM, a framework for training router models that direct queries between stronger and weaker LLMs to optimise cost-performance tradeoffs. It employs preference data from Chatbot Arena. Empirical results show that data augmentation is important to letting the routers outperform a random baseline on MMLU and GSM8K. It also demonstrates that the routers generalise across domains, and do not need to be retrained.

### Strengths
1. The paper presents a novel framework of directly using human preference data, as opposed to reward models, to route between a pair of LLMs.
2. The empirical evaluation is comprehensive, touching multiple architectures, LLMs and common benchmarks.
3. Both metrics of "average performance gap recovered" and "call-performance threshold" are clear reflections of real world considerations: the general ability for the router to close the performance gap between the better and worse model, as well as the cost to doing so for a minimum quality bar.
4. The increasing variation in LLM quality and cost makes it more important to be able to efficiently tradeoff between cost and performance. On MT Bench, RouteLLM is able to achieve comparable performance to GPT-4 with a cost saving of ~3.7x.

### Weaknesses
1. The paper focuses on a binary routing of "strong" versus "weak" model, but doesn't consider other binary differences between models. For example, the router could be used to differentiate between models with different specializations, such as coding or writing, or even models trained on different data distributions. This could be a more practical application of the router in real-world scenarios.
2. The paper does not discuss in depth why certain architectures perform better or worse, especially with respect to the improvement in the causal LLM's performance when faced with data augmentation. Specifically, it's unclear why a causal LLM benefits so much from data augmentation, while other architectures do not, and what the underlying mechanisms are that drive this difference. This makes it difficult to understand the limitations of the approach and how to best apply it to new scenarios.

### Questions
1. How well do the routers do at separating models which are much closer in ability e.g. two different 7B models?
2. How well do the routers do if the two models are not strictly "stronger" or "weaker", but rather have been finetuned to do different tasks?

### Soundness
4

### Presentation
4

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
Large language models (LLMs) excel at a wide range of tasks, but choosing the right model often involves balancing performance and cost. This paper proposes a routing approach, RouteLLM, to dynamically select between a stronger and weaker LLM during inference. Experiments on three real-world benchmarks demonstrate the effectiveness of RouteLLM.

### Strengths
S1. The proposed approach, RouteLLM, is able to achieve over 2x cost savings on popular benchmarks with
minimal impact on response quality.

S2. Authors demonstrate that RouteLLM enables routers to generalize to unseen data while maintaining strong performance across multiple LLMs.

### Weaknesses
W1. Unclear novelty and limited technical contribution. Training a router to harness the respective strengths of different LLMs has been widely studied [1,2,3,4]. Specifically, how to generalize LLM routing to OOD data has been studied in [5], how to use LLMs to generate more training data to help improve routing performance has been explored in [6], which authors did not compare to. Moreover, some technology (SW ranking) proposed in this paper shares unignorable similarity to prior work [7]. 

W2. Weak baselines. Provided the rich literature on this topic as aforementioned, considering a random router as the only baseline is insufficient in this work. The effectiveness of RouteLLM could be further demonstrated if authors could compare it to more advanced baselines (e.g., a subset from [1-6]).

W3. In Sec 5.5, authors provided the overhead analysis. Notably, SW ranking is both expensive ($37 / 1M requests) and slow (2.9 requests / second), which makes it hard to use in practice. Furthermore, the overhead analysis lacks a comprehensive accounting of all computational costs. Specifically, the cost of embedding extraction, which is a necessary step for both SW ranking and matrix factorization, is not included. Also, given that the model size ratio between BERT-base (110M) and causal LLM (8B) is 110M / 8B ~= 1%, it is surprising to see the cost overhead of BERT-base is ~60% of the causal LLM, and the achieved throughput is only 60% higher, according to Table 7. More details on how the overheads are estimated could be very helpful.

### Questions
Q1. In Sec 3.1, authors introduced the cost threshold \lambda. It is unclear that how to choose the right cost threshold when user have specific cost budgets.

Q2. Some details in overhead analysis are unclear. Both SW ranking and matrix factorization rely on embeddings generated by text-embedding-3-small. Are the costs incurred by embedding extraction included in the overhead analysis? Also, given that the model size ratio between BERT-base (110M) and causal LLM (8B) is 110M / 8B ~= 1%, it is surprising to see the cost overhead of BERT-base is ~60% of the causal LLM, and the achieved throughput is only 60% higher, according to Table 7. More details on how the overheads are estimated could be very helpful.

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
3

### Summary
The paper presents a framework for training router models using human preference data and data augmentation, achieving over 2x cost savings on popular benchmarks with minimal impact on response quality. The authors employ a binary routing approach to direct simple queries to a cost-effective model (e.g., Mixtral-8x7B) and complex queries to a stronger model (e.g., GPT-4). They demonstrate generalization across unseen data and new LLMs without retraining, providing a single trained router adaptable to multiple use cases.

### Strengths
- Demonstrates significant cost savings (over 2x) without compromising response quality, verified on MMLU, MT Bench, and GSM8K.
- Introduces APGR to quantify performance relative to cost, effectively balancing quality and cost constraints (Eq. 7).
- Implements diverse methods for defining the win prediction model.
- Demonstrates robustness and adaptability, as the router generalizes effectively to unseen LLM pairs and domains without retraining.

### Weaknesses
 - Lacks detailed analysis of routing patterns under different $\alpha$ values, such as which query types tend to be routed to strong vs. weak models, making it unclear how to set optimal $\alpha$ values for specific use cases (Sec. 5.1).
- Insufficient exploration of the router's decision-making robustness, especially regarding handling ambiguous queries where strong and weak models may perform similarly.
- Performance still heavily depends on data augmentation with high-cost LLM-judged labels.

### Questions
- Does the paper provide guidance on selecting the most suitable win prediction method across various scenarios?
- Could insights be provided on optimal $\alpha$ values for different query types, including a breakdown of routing decisions under varying $\alpha$ thresholds?

### Soundness
3

### Presentation
3

### Contribution
2
