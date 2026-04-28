# FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning of Foundation Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Low-Rank Adaptation (LoRA) is a popular technique for efficient fine-tuning of foundation models. However, applying LoRA in federated learning environments, where data is distributed across multiple clients, presents unique challenges. Existing methods rely on traditional federated averaging of LoRA adapters, resulting in inexact updates. To address this, we propose \textbf{Fed}erated \textbf{Ex}act \textbf{LoRA}, or \textbf{FedEx-LoRA}, which adds a residual error term to the pretrained frozen weight matrix. Our approach achieves exact updates with minimal computational and communication overhead, preserving LoRA’s efficiency. We evaluate the method on various models across arithmetic reasoning, commonsense reasoning, natural language understanding and natural language generation tasks, showing consistent performance gains over state-of-the-art methods across multiple settings. Through extensive analysis, we quantify that the deviations in updates from the ideal solution are significant, highlighting the need for exact aggregation. Our method's simplicity, efficiency, and broad applicability position it as a promising solution for accurate and effective federated fine-tuning of foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work provide a method, called FedEx-LoRA, to address the inexact aggregation problem when applying the LoRA in federated learning environment for large language model fine-tuning. FedEx-LoRA calculates a residual error matrix to the frozen pertained matrix on the server and then send it to each client to correct the error bring by the LoRA matrix aggregation on the server. This idea is straightforward. The authors also doing some experiments based on the LLM benchmarks to evaluate the model accuracy.

### Strengths
This work provides a method, called FedEx-LoRA, to address the inexact aggregation problem when applying the LoRA in federated learning environment for large language model fine-tuning.

### Weaknesses
There are some concerns for the proposed methods: 

1) for the federated learning, the network bandwidth between the server and clients is often very limited. This work brings lots of extra communication overhead for each training round. The extra communication data between server and clients equals to the entire model size which brings strong communication overhead, especially for the federated learning environments.

2) the proposed methods requires to calculate n matrix multiplication, where n is the number of the layers for the LLM models. For the federated learning, the server also run on a CPU-based computing node. The n matrix multiplication also brings strong computational overhead for the server. If you want to use GPU to calculate such matrix multiplication, you need to carefully schedule the calculation process since the bandwidth between main memory and GPU memory (PCIe) also limited.

Overall, the final system performance, including the communication and computational efficiency for the proposed method is unacceptable for the federated learning environments.

### Questions
Please see the comments from the above weakness section. Two questions need to answer:

1) how to address the strong communication overhead problem between the server and clients?

2) how to address the strong computation overhead problem on the server?

These two issues will largely cause system performance degradation.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the task of parameter-efficient fine-tuning under Federated Learning setting, particularly focused on the low rank adaptation approach. The work is built on the insights from the earlier FedIT model which used traditional federated aggregation methods to average low-rank matrices A and B individually. However, this approach was found to be inexact aggregation as the average of the products does not equate to the product of the averages.
To address this challenge, the authors propose an innovative method that incorporates a residual term into the pretrained frozen weight matrix. This addition aims to bridge the discrepancy between the average of the products and the product of the averages, enhancing the aggregation performance. The effectiveness of this approach is demonstrated through extensive analysis of NLU and NLG benchmark datasets using RoBERTa and GPT-2 models. The results show notable improvements in performance metrics while maintaining comparably low communication costs compared to the most benchmarked models.

### Strengths
The paper introduces a straightforward yet effective method that ensures exact aggregation in LoRA-based fine tuning for Federated Learning. While it has a slightly higher communication cost compared to FedIT and FFA-LoRA, the increase is minimal given the significant improvement in overall performance.  
Moreover, the method's effectiveness is validated through comprehensive experiments and analysis, affirming its claim of exact aggregation and subsequently better overall performance.
Additionally, the paper has good reproducibility of the results because of its detailed presentation of the experimental settings.

### Weaknesses
The main issue is that the contribution may seem too incremental for ICLR conference as the method primarily focuses on a straightforward adjustment in the aggregation phase—specifically, adding back the discrepancy between the average of the products and the product of the averages. This method, while empirically effective, does not introduce a significant innovation or a novel approach that would typically be expected for ICLR. 

Additionally, there are practical scalability concerns regarding the residue error term matrix, which shares dimensions with W’ and W0. The paper notes that the rank of this matrix is limited to k*r where k is the number of clients. However, in typical federated learning environments, which often involve a large number of clients (potentially hundreds), this could lead to a high-rank matrix and, consequently, significant communication costs. The experimental setup in the paper, which involved only three clients, does not adequately demonstrate the method's communication cost in larger, more realistic scenarios common in federated learning. Furthermore, the paper does not explore the impact of this high-rank residual matrix on the convergence behavior of the federated learning process, which is a critical aspect for practical deployment. The analysis should include how the rank of the residual matrix impacts the stability and speed of convergence, especially when dealing with a large number of clients.

### Questions
1.	It would be good to see the performance comparison for different settings regarding clients e.g., the number of clients,  the portion of randomly selected clients etc. – these are standard evaluations in FL literature
2.	How the residue error term matrix affects the update of A and B? It would be good to see an analysis experiment regarding this.

### Soundness
3

### Presentation
4

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
The paper introduces FedEx-LoRA, a novel approach for federated fine-tuning of LLMs using LoRA. Existing federated fine-tuning methods face limitations in achieving exact aggregation due to the inexact averaging of LoRA adapters. The proposed FedEx-LoRA addresses this by introducing a residual error term added to the frozen weight matrix, ensuring precise updates. FedEx-LoRA is designed to be computationally and communication-efficient, preserving LoRA’s benefits without adding additional training burdens. Empirical results demonstrate improved performance on NLP tasks over SOTA federated fine-tuning methods, highlighting its applicability in distributed training settings where data privacy is a concern.

### Strengths
- Originality: The paper introduces a novel solution to the inexact aggregation problem in federated fine-tuning with LoRA by adding a residual error term directly to the pretrained weight matrix. This innovative approach ensures exact updates while preserving the low-rank efficiency of LoRA, addressing a key limitation in existing methods.

- Quality: The authors provide thorough theoretical justification and extensive empirical evaluations across multiple benchmarks. The experiments consistently demonstrate that FedEx-LoRA outperforms SOTA federated fine-tuning methods, validating the effectiveness and robustness of the proposed approach.

- Clarity: The paper is well-written and organized, clearly explaining the challenges of federated fine-tuning and the limitations of existing aggregation methods. The step-by-step presentation of FedEx-LoRA, along with illustrative diagrams and extensive formulas, makes the methodology accessible and easy to understand.

- Significance: By enabling exact aggregation in federated settings without significant computational overhead, the paper has substantial practical implications for privacy-preserving applications in NLP and beyond. The method enhances the feasibility and performance of federated fine-tuning in real-world scenarios where data privacy and efficient communication are crucial.

### Weaknesses
 - Model limitations: The paper evaluates FedEx-LoRA primarily on RoBERTa and GPT-2, which are smaller foundation models. It remains uncertain how this method performs on larger models, such as Llama and Mistral, where scalability challenges might differ. Specifically, the memory footprint and computational demands of maintaining and aggregating residual matrices could become a significant bottleneck with larger models, potentially negating the efficiency gains of LoRA. The paper lacks a detailed analysis of how the size of the residual matrix scales with model size and how this impacts overall training time and resource consumption.

- Task scope: The evaluation focuses on standard NLP tasks. Assessing performance on more complex tasks, such as reasoning and inference, would strengthen the paper’s claims on generalizability and robustness. The current evaluation does not explore tasks that require multi-hop reasoning or complex inference, which are crucial for assessing the true capabilities of the proposed method. The paper should include evaluations on tasks that test the model's ability to perform complex operations beyond simple text processing.

- Quantization challenges: Introducing residual matrices to the original weights could complicate quantization processes for LLMs, as these residuals require re-quantization at each aggregation round. This could increase computational and memory costs, potentially limiting practical efficiency in federated settings. The paper does not address the practical implications of re-quantizing the residual matrices, including the potential for information loss and the added computational overhead. A detailed analysis of the impact of quantization on the performance of FedEx-LoRA is needed.

- Privacy impacts: Although FedEx-LoRA is presented as beneficial for privacy-preserving federated learning, the paper lacks a detailed analysis of how the approach performs under differential privacy constraints or other mechanisms, which could be helpful for deployment in sensitive domains. The paper should include an analysis of how the residual matrices might leak information about the local client data and how this could be mitigated using privacy-preserving techniques. The current analysis does not provide sufficient evidence to support the claim that FedEx-LoRA is inherently privacy-preserving.

### Questions
- What factors contribute to FedEx-LoRA outperforming centralized LoRA on certain benchmarks?

- Can FedEx-LoRA be extended to other LoRA variants, such as MoE-LoRA and QLoRA, and if so, what adaptations might be necessary?

- How does FedEx-LoRA scale and perform with larger foundation models, such as Llama or Gemma?

- How does FedEx-LoRA perform on more complex tasks, such as commonsense QA, mathematic reasoning, or coding?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Given the problem that averages the A and B matrices of LoRA will result in inexact updates in federated learning, this paper proposes Federated Exact LoRA (FedEx-LoRA). FedEx-LoRA computes the aggregation error on the server, sends the error weights to the clients, and updates the local model by the weights while preserving the aggregated LoRA. The paper provides experiments on RoBERTa and GPT-2 to demonstrate the effectiveness of FedEx-LoRA compared to FedIT and FFA-LoRA.

### Strengths
(1) The problem raised about whether to use FedAvg on LoRA is valuable. It brings up the problem that the optimization target of LoRA federated fine-tuning is the full global model $W$ or a global LoRA $B_GA_G$.

(2) Figure 2 provides some interesting insights for FL researchers. The authors find that the deviations decrease as the model depth increases, which may lead to deeper reflections on the relationship between model architecture and fine-tuning.

### Weaknesses
 **Contribution**: The authors mention in the paper that they identify a critical discrepancy in traditional federated averaging of LoRA adapters. However, this question has been raised and studied in detail. [1] and [2] identified this problem and [2] provided a solution for eliminating this error. None of these previous works are discussed in detail and listed as baselines. The reviewer believes that the author has not adequately researched this field, so the contribution is limited.

**Method**: The reviewer believes that the solution proposed in this paper is too simplistic and impractical. Here are some reasons:

(1) Increased communication cost: According to Figure 1 and Eq. (14), the server needs to send the residual error term to clients for updating the local base model. This makes the communication cost from server to clients as large as full fine-tuning (or at least the full fine-tuning on the layers that apply LoRA). It is not acceptable since we use LoRA to reduce the communication cost. Especially in federated fine-tuning LLMs, this residual error term may be as large as $kT$ times the LLM parameter size.

(2) Increased computation cost: According to Figure 1 and Eq. (11) (12), the server will iteratively compute the production of $BA$ from clients and the residual error term. This has led to a several-fold increase in computation on the server, compared to FedIT.

**Writing**: This paper has some typos, as well as unclear parts that do not conform to the federated learning paradigm.

(1) Eq. (5), (7) look confused, why the aggregation of local LoRA modules $B_i$ and $A_i$ is still the local LoRA? If here the authors mean that the new $B_i A_i$ are local modules in the next epoch, why in Eq. (7) the global model is updated by the local LoRA? These expressions may be understandable to researchers familiar with federated learning through guessing, but they are still difficult to understand.

(2) The paper use $B \cdot A$ in Figure 1. It seems incorrect to use the dot product here. However, in the equations, $BA$ and $B\times A$ are used.

(3) $W_0$, $W^{global}$, $A_{init} B_{init}$, $A_{i} B_{i}$ are used together. It is confusing which round these weights are in and whether they are the global or local weights. It could be better to use communication round numbers and uniform global and local marks.

**Experiments**: Related papers such as FedIT are using LLMs for experiments. But FedEx-LoRA is using RoBERTa and GPT-2. It is understandable that experimental resources are limited, but the research related to LoRA nowadays lacks sufficient convincing power when applied to models smaller than 1b parameters. As mentioned before, the extra communication and computation costs are not well analyzed.

**Missed Baselines**: The paper misses detailed comparison to at least two important related works that focus on the same topic:

[1] Sun, Y., Li, Z., Li, Y., & Ding, B. (2024). Improving loRA in privacy-preserving federated learning. arXiv preprint arXiv:2403.12313.

[2] Wang, Z., Shen, Z., He, Y., Sun, G., Wang, H., Lyu, L., & Li, A. (2024). Flora: Federated fine-tuning large language models with heterogeneous low-rank adaptations. arXiv preprint arXiv:2409.05976.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
1

### Contribution
1
