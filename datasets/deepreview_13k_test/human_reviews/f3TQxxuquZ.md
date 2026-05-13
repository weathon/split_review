# One-stage Prompt-based Continual Learning

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Prompt-based Continual Learning (PCL) has gained considerable attention as a promising continual learning solution as it achieves state-of-the-art performance while preventing privacy violation and memory overhead issues. Nonetheless, existing PCL approaches face significant computational burdens because of two Vision Transformer (ViT) feed-forward stages; one is for the query ViT that generates a prompt query to select prompts inside a prompt pool; the other one is a backbone ViT that mixes information between selected prompts and image tokens. To address this, we introduce a one-stage PCL framework by directly using the intermediate layer's token embedding as a prompt query. This design removes the need for an additional feed-forward stage for query
ViT, resulting in $\sim 50\%$ computational cost reduction for both training and inference with marginal accuracy drop ($\le 1\%$).
We further introduce a Query-Pool Regularization (QR) loss that regulates the relationship between the prompt query and the prompt pool to improve representation power. The QR loss is only applied during training time, so there is no computational overhead at inference from the QR loss.
With the QR loss, our approach maintains $\sim 50\%$ computational cost reduction during inference as well as outperforms the prior two-stage PCL methods by $\sim 1.4\%$ on public class-incremental continual learning benchmarks including CIFAR-100, ImageNet-R, and DomainNet.
  \keywords{Efficient learning \and Continual learning \and Transfer learning}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission proposes a method for one-stage prompt-based continual learning (PCL) where a separate forward pass of a ViT is not  required to extract the query tokens from the given image. Instead, they utilize intermediate [CLS] tokens from the previous layer as query tokens such that a single forward pass of the ViT is sufficient for PCL. To improve performance, they use a reference ViT during training to generate reference query tokens and use a query pool regularization loss to match the intermediate [CLS] tokens to the reference query tokens. Evaluation is done on CIFAR10 and ImageNet-R datasets, which show superiority of the proposed method.

### Strengths
- The problem of having to do 2 forward passes of a ViT in PCL is an important task to tackle.
- The proposed method is not specific to a model architecture, which makes it widely applicable.
- The idea itself is well presented and easy to follow.
- The empirical evaluation shows strong performance of the proposed method.

### Weaknesses
- The query pool regularization introduces extra computation in the training phase, especially as more advanced reference ViTs are used. I do not think this is particularly fair in comparison to prior work as they used less resources during training. Specifically, as the idea of continual learning depends much more heavily on the computation cost of training and inference due to the training phase being run continuously, I do not think matching the computation cost during the inference phase only is fully fair. Recent works such as [A] tackle this specific part of the resource constraints in continual learning and I believe the proposed method needs to discuss on the computation cost of the training phase more thoroughly.

[A] Real-Time Evaluation in Online Continual Learning: A New Hope, Y. Ghunaim et al., CVPR2023

### Questions
- Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a single stage PCL framework that directly using the intermediate layer’s token embedding as a prompt query, so that the first query pre-training ViT could be avoid and half of the computational cost is avoid. The paper describe why using intermedia layer output to construct query embedding, and further propose QR loss to regulate the relationship between the prompt query and the prompt pool, and enhance the representation ability. Experimental result show that this approach could maintain performance under 50% less cost.

### Strengths
1. Reducing the computational cost by reducing query ViT seems well and could be regarded as new direction compared with prompt construction or weighting. I think the exploring on intermediate layer output as prompt is reasonable, organization of the paper is also good to follow.

2. The designed QR loss for supplementing the absent of [CLS] tokens in the query is interesting, it could maintain the representation power.

3. The result and discussion in the experimental part is convinced, the figure 4 shows the obvious improvement on consuming. Relative discussion and ablation study, parameter analysis also seems well.

### Weaknesses
I think some specific description should be more clear:
1. Although the training avoid the query ViT process, the author mentioned that QR loss need a reference ViT architecture. This process also need to forward the input, so for reducing the two-step forward, what's the difference between Query function forward and reference forward? Why the (training) computational cost still reduce 50% when QR loss with reference forward existing?
2. The author mention that this approach focuses on improving efficiency through a new query selection. But from the description, seems that how to select query that different from previous PCL is not clear, both of them apply the [CLS] token embedding (no requirement of query ViT in this process is the major difference).

### Questions
Is QR without query ViT could perform better generalization on unseen task/domain?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the OS-Prompt framework, a new one-stage Prompt-Based Continual Learning (PCL) approach for image recognition tasks. By restructuring the traditional two-step feedforward stages, the OS-Prompt aims to optimize computational costs in PCL. Experiments are conducted on datasets such as Split CIFAR-100 and Split ImageNet-R, comparing the efficacy of OS-Prompt with other continual learning methodologies.

### Strengths
1.	Addressing Computational Inefficiencies: The paper astutely identifies a significant limitation in current PCL methods, notably the high computational cost stemming from the two separate ViT feed-forward stages. The introduction of the OS-Prompt as a remedy is commendable, achieving an impressive reduction in computational cost by nearly 50% without compromising on performance.
2.	Innovative QR Loss Introduction: In response to the minor performance decline observed with the one-stage PCL framework, the paper introduces a QR loss. This strategic addition ensures that the prompt pool remains consistent with token embedding from both intermediate and final layers. Importantly, the implementation of the QR loss is efficient, adding no extra computational burden during the inference phase.

### Weaknesses
1.	Potential Scalability Concerns: While the OS-Prompt framework demonstrates efficiency improvements on benchmarks like CIFAR-100 and ImageNet-R, the paper does not provide insights into how this method scales with larger, more complex datasets. This leaves questions about its applicability in broader, real-world scenarios where data variability and volume might be significantly higher.
2.	Lack of Exploration on QR Loss Limitations: The introduction of the QR loss is innovative, but the paper could benefit from a more in-depth discussion on its potential limitations or scenarios where it might not be as effective. A deeper dive into the trade-offs associated with the QR loss would provide a more balanced view of its utility.
3.	Comparative Analysis Depth: While the paper highlights the superiority of the OS-Prompt over the CodaPrompt method, it might be beneficial to see how the proposed framework fares against a wider array of contemporary methods. A more extensive comparative analysis would offer readers a comprehensive understanding of where OS-Prompt stands in the broader landscape of PCL techniques.

### Questions
Please the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a one-stage prompt-based continual learning strategy that simplifies the query design and improves computational efficiency. In particular, it directly uses the intermediate layer's token embedding as a prompt query and introduces a query-pool regularization strategy to enhance the representation power. The experimental evaluation shows that the proposed method achieves about 50\% computation cost reduction and better performance on two benchmarks.

### Strengths
- The paper is well-written and easy to follow.

- The proposed idea is well-motivated and the method is simple and effective.

### Weaknesses
- Assumption on the pretrained network. One limitation of existing PCL methods is that they rely on supervised pretraining on ImageNet1k, which has a large impact on the model performance but can be infeasible for a general CL task. Does this method still work without using supervised pretraining? For instance, what if replacing the supervised pretraining model with an unsupervised pretraining model (e.g. DINO [1])?

[1] Caron et al. Emerging Properties in Self-Supervised Vision Transformers. ICCV2021.

- Lack of clarity in experimental results. In particular, Figure 2 is not very clear. Is the token embedding distance depicted in this Figure related to the current task? What are the distances between token embeddings for tasks 1 to t-1 when task t is learned? Such an illustration could provide more insights into how the method alleviates catastrophic forgetting.

### Questions
See the comments in the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
