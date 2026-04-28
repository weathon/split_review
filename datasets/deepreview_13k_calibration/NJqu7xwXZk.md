# FedOne: Query-Efficient Federated Learning for Black-box Discrete Prompt Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Black-Box Discrete Prompt Learning (BDPL) is a prompt-tuning method that optimizes discrete prompts without accessing model parameters or gradients, making the prompt tuning on a cloud-based Large Language Model (LLM) feasible.
Adapting Federated Learning (FL) to BDPL could further enhance prompt tuning performance by leveraging data from diverse sources. 
However, all previous research on federated black-box prompt tuning had neglected the substantial query cost associated with the cloud-based LLM service. 
To address this gap, we conducted a theoretical analysis of query efficiency within the context of federated black-box prompt tuning. Our findings revealed that degrading FedAvg to activate only one client per round, a strategy we called *FedOne*, enabled optimal query efficiency in federated black-box prompt learning. 
Building on this insight, we proposed the FedOne framework, a federated black-box discrete prompt learning method designed to maximize query efficiency when interacting with cloud-based LLMs.
We conducted numerical experiments on various aspects of our framework, demonstrating a significant improvement in query efficiency, which aligns with our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses Black-box Discrete Prompt Learning (BDPL) in Federated Learning and proposes FedOne. The proposed FedOne selects one client at each round, and the selected client updates the sample probability for each token at different positions. This work provides a theoretical analysis and shows the convergence rate of the proposed algorithm. Extensive experiments show the remarkable performance of the proposed work.

### Strengths
1. This work proposes an interesting solution to addressing BDPT in federated learning. 
2. The work discloses an interesting discovery that sampling one client at every round can provide remarkable performance. 
3. The experience is conducted on the GLUE dataset and two pretrained models, i.e., Roberta and GPT-3.5. And the experimental results are promising.

### Weaknesses
1. The proposed method requires each client to store a size of $n \times N$ $\alpha$s. Nowadays, the pretrained embedding layer of an LLM gets larger, e.g., from 32k in LLaMA-2 to 128k in LLaMA-3. Therefore, it costs a large amount of computation and communication overhead. 
2. This paper does not explicitly discuss the effect of $n$. This should be part of the ablation study. 
3. The review of FL is insufficient. I see there are a number of works addressing LLM fine-tuning under federated learning. The authors should concretely discuss why the existing works are infeasible. 
4. $\eta^*$ goes to an order of $O(\sqrt{T})$. This sounds really weird. I think the author should justify the reason.

### Questions
See **Weaknesses**.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on federated Black-Box Discrete Prompt Learning (BDPL) and offers the first theoretical analysis of this approach, uncovering valuable insights from the findings. Specifically, the authors demonstrate that utilizing FedAvg with a single client in each training round yields the highest query efficiency. The numerical results corroborate this theoretical conclusion, reinforcing the validity of the proposed method.

### Strengths
1. The paper presents a convergence error analysis of federated BDPL.
2. Building on these theoretical results, the authors optimized federated BDPL by strategically determining the number of participating clients for each training round.

### Weaknesses
1. The paper builds upon an existing federated BDPL framework.
2. The rationale behind the FedONE algorithm is not adequately explained.

### Questions
1. The rationale behind the FedONE algorithm lacks a proper explanation. Specifically, if I understand correctly, FedONE aggregates only one client in each round. Does this imply that, in each round, the clients will set their local model parameters $\alpha$ to match those of the selected client? Intuitively, this could lead to significant fluctuations in model training, particularly when the local data across clients are highly heterogeneous. Further clarification on how to interpret and address this phenomenon is needed.

2. Additional experiments should be included to assess the impact of data heterogeneity across clients.

### Soundness
2

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
This paper proposes a more cost-efficient federated learning framework called **FedOne** to optimize query efficiency when interacting with the cloud large language model (LLM). A convergence analysis for Federated BDPL is also been explored in this paper. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. Improving the query cost efficiency is important in federated learning scenarios. The proposed method is simple and reasonable with a theoretical guarantee. 

2. The paper is well-written and easy to understand.

### Weaknesses
1. More details on optimizing $K_{*}$ from "$>1$" to "$=1$" for improving query efficiency in Section 3.2 should be provided, as it is the most important part in the whole paper. According to the current version, the proposed method is too simple and too straightforward. The effect of the value of $K_{\*}$ on model convergence should be also analyzed in this section. Specifically, the trade-off between the number of activated clients ($K_{\*}$) and the convergence rate needs to be rigorously discussed. While activating more clients might seem beneficial, it could lead to diminishing returns or even hinder convergence due to increased variance or communication overhead. A clear mathematical relationship or empirical evidence demonstrating the optimality of $K_{\*}=1$ under different scenarios would significantly strengthen the paper's core argument.

2. The experiment does not contain related baselines to compare with, such as [1],[2]. As a result, it is very hard to evaluate whether the **FedOne** reflects the SOTA performance. The lack of comparison makes it difficult to assess the practical significance of the proposed method. Including these baselines would provide a clearer context for evaluating FedOne's performance and demonstrating its advantages over existing approaches.

3. It is unclear whether the number of clients has an effect on the performance of FedOne. A more in-depth analysis exploring the relationship between the total number of clients and the performance of FedOne is needed. Intuitively, a larger number of clients might offer a richer pool of data, potentially leading to improved model performance. However, it could also introduce challenges related to heterogeneity and straggler effects. An experimental evaluation varying the number of clients would provide valuable insights into the scalability and robustness of FedOne.

### Questions
Please refer to the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a prompt tunning method in federated learning system, incorporated with black-box LLMs on the cloud. The method, FedOne, is proposed to reduce the cost on APIs usage. Theoretical analyses and experiments are conducted to support the main claims.

### Strengths
- This work focuses on a new perspective of federated learning with LLMs, APIs usage cost reduction.
- The experiments' results seem positive, and the proposed FedOne's overall generalization ability is validated on various datasets.
- The discussion about the weaknesses of white-box prompt learning is interesting in the literature of federated learning.

### Weaknesses
 - Considering that the computational cost on the entire LLM of white-box prompt learning is transfer to the cost on APIs usage of black-box prompt learning, the overall motivation is questionable. More detailed cost-benefit analyses and related facts would explain this well.
- The claim and the proof of Corollary 2, which support the main idea that 1 client is needed, is naive and questionable either. $K_{*}$ is related to aggregation and overall variance (e.g., $\lambda$ in Assumption 3) due to the fact that larger $K$ reduce the aggregation noise in federated learning setting. Even if small stepsize can be use to minimize it, as claimed in Line 269, the training process in slower, leading more global epochs. Thus, the bound, from Line 1519 to 1595, seems vaccum and the claim do not make sense. A more comprehensive analysis could help, which takes into account the trade-offs between reduced aggregation noise from larger $K$ and the increased number of global epochs.
- In the reported results, Fune-tuning works better than FedOne. A more detailed analysis of this result and the compatibility of the two methods would help to explain the underlying reasons.

### Questions
- Can $\lambda$ the gradient diversity and $K$ be decoupled in the analyses?
- Are there any facts supporting that cost on a local LLM is larger than cost on APIs usage? Could you please provide a more detailed cost-benefit analysis comparing the computational costs of white-box prompt learning v.s. the API usage costs of black-box prompt learning?
- Are there scenarios where FedOne might be preferable despite lower performance? Could you please discuss potential improvements to FedOne that could help close the performance gap with fine-tuning.

### Soundness
2

### Presentation
2

### Contribution
3
