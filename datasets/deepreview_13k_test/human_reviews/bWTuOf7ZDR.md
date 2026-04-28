# Personalized Federated Fine-tuning for Heterogeneous Data: a Two-Level Low Rank Adaptation Approach

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
We study the personalized federated fine-tuning task with heterogeneous client data in the context of foundation models, where clients collaboratively fine-tune a foundation model (e.g., BERT, GPT) without sharing their local data, achieving personalized models simultaneously. While recent efforts have applied parameter-efficient fine-tuning techniques like low-rank adaptation (LoRA) or training prompts in federated settings, they often overlook data heterogeneity and model personalization.  The primary challenge is that a single common adapter or prompt learner may not suffice for the diverse data of all clients. To address this issue, we propose PF2LoRA, a new personalized federated fine-tuning algorithm based on a novel \emph{ two-level low rank adaptation framework} on top of LoRA. Given the pretrained foundation model whose weight is frozen, our algorithm aims to learn two levels of adaptation simultaneously: the first level aims to learn a common adapter for all clients, while the second level fosters individual client personalization. This framework explicitly accommodates variations in adapter matrix ranks across clients and introduces minimal additional memory overhead, as the second-level adaptation comprises a small number of parameters compared to the first level. Our experiments on natural language understanding and generation tasks demonstrate that PF2LoRA significantly outperforms existing federated fine-tuning methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed a two-level LoRA framework for foundation models to address data heterogeneity and personalization in FL, which contains a homogeneous LoRA for aggregation and a heterogeneous LoRA for personalization in each client.

### Strengths
1. This paper focuses on personalized federated fine-tuning of foundation models, which is an emerging and promising research direction.

2. The paper conducts extensive experiments across various NLP tasks and detailed algorithms and codes are provided to support its reproducibility.

### Weaknesses
1. The motivations and applications of this paper are unclear. If the setting of this paper is similar to HETLoRA focusing on employing different ranks to accommodate varying system capabilities, then the upper-level LoRA of PF2LoRA would be useless as long as there is a client whose computational capacity can only support a very low rank (e.g. r=1). Alternatively, if this paper aligns with the setting of HOMLoRA, then the need for different ranks for personalization is questionable. It might be more effective to simply further fine-tune the aggregated upper-level LoRA or maintain a uniform rank across the lower-level LoRA.

2. The paper asserts that their framework can overcome the HETLoRA’s limitation of fixed rank initialization that does not consider data by automatically adjusting ranks based on training data. However, the explanation of this automatic mechanism is insufficient, and it seems that the LoRA ranks in PF2LoRA are predefined and not truly data-dependent, contradicting the claims made, as observed in the experiments.

3. Some related work is missing [1][2]. For example, it would be better if the paper could add a comparison analysis with [1] which emphasizes personalization using two LoRAs. Additionally, the experimental results on the GLUE benchmark reported in this paper are significantly lower than those in work [2], which used the same baseline and datasets, why does this happen?

[1] Yang, Y., et al. (2024). Dual-Personalizing Adapter for Federated Foundation Models. arXiv preprint arXiv:2403.19211.

[2] Zhang, Z., et al. (2023). Fedpetuning: When federated learning meets the parameter-efficient tuning methods of pre-trained language models. In Annual Meeting of the Association of Computational Linguistics 2023 (pp. 9963-9977). Association for Computational Linguistics (ACL).

### Questions
See weakness.

### Soundness
2

### Presentation
2

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
This paper proposes a two-level low-rank adaptation method, named PF2LoRA, to address data heterogeneity and model personalization challenges in federated fine-tuning of foundation models. In PF2LoRA, all clients first collaboratively train a general adapter, followed by each client training a personalized adapter with a unique rank to suit their local tasks. Extensive experiments on natural language datasets demonstrate the superiority of the proposed method.

### Strengths
1. This paper is easy to read and understand.
2. The experiments are extensive and validate the effectiveness of the method.

### Weaknesses
1. In line 176, the authors argue that fixed-rank initialization may lead to underfitting or overfitting issues. However, this claim lacks supporting evidence.
2. In PF2LoRA, stage 1 requires all clients to jointly train an adapter with a rank  r . Isn’t this essentially a “fixed-rank initialization”? Why would this phase not also cause underfitting or overfitting issues?
3. The authors argue that one of HETLoRA’s weaknesses is the need to tune several hyperparameters. However, PF2LoRA also has multiple hyperparameters, such as  r ,  \tilde{r} , and  \alpha . I believe the number of hyperparameters isn’t the key issue; rather, it’s whether the hyperparameters are easy to adjust and how sensitive the method is to them. This paper lacks a discussion on these aspects.
4. Based on my current understanding, PF2LoRA appears to be an incremental improvement over HETLoRA, transforming the training process into a two-stage approach. In line 196 (Eq. (2)), if we set  B_{k}A_{k} = BA + D_{k}C_{k} , isn’t this effectively training a different-rank adapter for each client as in HETLoRA? The main difference is that PF2LoRA separates the common component  BA  for a two-stage training scheme, while HETLoRA trains  BA  and  D_{k}C_{k}  simultaneously.

### Questions
Please see the weaknesses above.

### Soundness
3

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
5

### Summary
Towards solving the data heterogeneity problem, the paper proposes PF2LoRA, which adopts two LoRA adapters in a personalized federated fine-tuning algorithm. On each client, one LoRA is kept private on-device for personalized learning and another is shared by all clients for federated fine-tuning. By applying this two-level low-rank adaptation and other optimizations, PF2LoRA achieves better performance than baselines.

### Strengths
(1) The data heterogeneity problem is valuable for research in federated fine-tuning. The paper designs a valid solution for LoRA fine-tuning in this topic. The idea of using two sets of LoRA is straightforward, and easy to be implemented.

(2) The paper provides a theoretical justification of the proposed method. Also, the 'Detailed Implementation for Language Models' section is useful for reproducing the results.

(3) The paper is well-written and easy to follow. The reviewer gets a clear idea from the paper after reading it.

### Weaknesses
(1) For the data heterogeneity problem itself, the reviewer believes that the key point or bottleneck in federated fine-tuning is the heterogeneous computational resource problem, but not the data heterogeneity. If the clients have enough resources, they can just apply homogeneous local LoRA ranks that are large enough, and can achieve better performance. It is the limited local computational resource problem that makes the clients use LoRA, and maybe adopt different LoRA ranks.

Therefore, the question here is whether it is realistic to adopt two LoRAs on the clients, which actually increases the cost. If we mainly consider the computational cost, there are some works that already optimize this problem [1] [2].

(2) The two-level optimization looks a little confusing. The goal of the local LoRA is to minimize the local loss function and the goal of the global ones is to learn a common adapter for all clients. Will this cause the global LoRA not to learn enough local knowledge since local LoRAs already overfit on local objects? In other words, since the local LoRAs are not used to update the global model, what is the purpose of using these local LoRAs?

(3) The experiments seem not sufficient since models as large as GPT-2 are used. Related works use models larger than 1b. Is there any reason to use smaller models?

(4) Some related works are missed:

[1] Bai, J., Chen, D., Qian, B., Yao, L., & Li, Y. (2024). Federated fine-tuning of large language models under heterogeneous language tasks and client resources. arXiv preprint arXiv:2402.11505.

[2] Wang, Z., Shen, Z., He, Y., Sun, G., Wang, H., Lyu, L., & Li, A. (2024). Flora: Federated fine-tuning large language models with heterogeneous low-rank adaptations. arXiv preprint arXiv:2409.05976.

[3] Chen, H., Zhang, Y., Krompass, D., Gu, J., & Tresp, V. (2024, March). Feddat: An approach for foundation model finetuning in multi-modal heterogeneous federated learning. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 38, No. 10, pp. 11285-11293).

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a two-level low rank adaptation approach to achieve personalized federated learning to address the data heterogenous in federated learning. The experiments on multiple datasets has shown the effectiveness of the proposed methods.

### Strengths
1. The attemp to introduc LoRa into federated learning to utilize pretrained model seems to be interested for me. 
2. The paper is well organized, makes the readers easy to understand the background and the proposed method.

### Weaknesses
1. The authors claim that existing studies that utilizing LoRa in federated leanring mainly focus on HOMLoRA, rather than personalized federated learning. However, I have found multiple studies that using the LoRa technique to achive personalized federated learning [1-5]. Some of them also introduce a two-level adaption idea [2], [5]. Can authors include a detailed comparison with these studies and  discuss the novelty over the proposed method?

2. In the paper, the author said that the proposed method are more suitable to resource-constrained devices. However, in experiments, the authors only conduct a comparison over the trainable parameters. Can the authors provide a comparison over the communication costs, such as the FLOPS on the proposed methods? Moreover, can the authors provide some evidence that the proposed method can be executed on resource-constrained devices such as mobile phone?

3. As the authors have discussed, HETLoRA utilize a fixed rank initialization, which is independent of data and may cause underfitting or overfitting issues. However, the proposed method seems also uses the pre-defined rank when adopting LoRa. So why does not the proposed method suffer the same challenges as HETLoRA?

4. Can the authors provide some ablation studies about the two-stage training strategy. I am intersted to see that whether the client-specific adapters can better search the optimal on local clients given the trained common adapter?

[1] pFedLoRA: Model-Heterogeneous Personalized Federated Learning with LoRA Tuning
[2] FDLoRA: Personalized Federated Learning of Large Language Model via Dual LoRA Tuning
[3] Personalized Wireless Federated Learning for Large Language Models
[4] SA-FedLora: Adaptive Parameter Allocation for Efficient Federated Learning with LoRA Tuning
[5] FedFMSL: Federated Learning of Foundations Models With Sparsely Activated LoRA

### Questions
I would be appreciate and raise my score if the author can address the questions listed in the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
