# On the Effectiveness of Discrete Representations in Sparse Mixture of Experts

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 5, 5, 5

## Abstract
Sparse mixture of experts (SMoE) is an effective solution for scaling up model capacity without increasing the computational costs.
  A crucial component of SMoE is the router, responsible for directing the input to relevant experts; however, it also presents a major weakness, leading to routing inconsistencies and representation collapse issues.
  Instead of fixing the router like previous works, we propose an alternative that assigns experts to input via \emph{indirection}, which employs the discrete representation of input that points to the expert.
  The discrete representations are learnt via vector quantization, resulting in a new architecture dubbed Vector-Quantized Mixture of Experts (VQMoE).
  We provide theoretical support and empirical evidence demonstrating the VQMoE's ability to overcome the challenges present in traditional routers.
  Through extensive evaluations on both large language models and vision tasks for pre-training and fine-tuning, we show that VQMoE achieves a 28\% improvement in robustness compared to other SMoE routing methods, while maintaining strong performance in fine-tuning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission proposes VQMoE, a new variant for sparse mixture of expert models (SMoE).
VQMoE utilizes the vector-quantization technique to construct a router, which is conventionally
made of softmax-based subnetwork and tends to collapse. 
VQMoE adopts two-stage training: in the first stage, the VQ and conventional router are parallelly trained,
and in the second stage, the conventional router is removed and routing is solely performed by VQ.
Theoretical analyses claim that VQMoE performs consistent expert selection in terms of distance metric in the latent space,
and VQMoE's expert selection strategy (simply assigning a expert to each cluster) is optimal.
Experiments are conducted in language modelling, down stream tasks, and computer-vision tasks. and they demonstrate
better parameter-performance trade-off by VQMoE than existing MoE variants.

### Strengths
- The idea of performing routing by clustering is intuitive and promising.
- The proposed method is simple and seemingly easy to implement, which shows the potential of the proposed method for replacing existing MoE-based methods.
- The experiments are extensively conducted in language and vision domain.

### Weaknesses
 - Proposition 4.2:
I have concerns in this statement’s mathematical rigorousness.
Optimality in what metrics is discussed in the proposition? Training error or loss?
What assumption is used in the proof?
It looks that $E_j(x_j) = \min_{c \in [1,k]}(E_j(x_c))$ (l. 795) requires that expert E_j is optimally trained with sample x_j.
Then, the proposition is claiming "if VQMoE is optimally trained with expert assignment strategy to asign E_j to x_j, samely assigning E_j to x_j is optimal in inference" is nearly a tautology. This statement lacks a clear definition of optimality, and the connection between training and inference optimality is not well-established. The argument seems to assume that optimal training automatically leads to optimal inference, which is not necessarily true in complex models. The proposition needs to specify the loss function being minimized and the assumptions under which this optimality holds. Furthermore, the claim that assigning expert $E_j$ to cluster $x_j$ is optimal needs more rigorous justification beyond the observation that the expert has learned knowledge specific to that cluster during training. It is unclear if this assignment is optimal in terms of generalization performance, or if it is only optimal in terms of training loss on the seen data.

- On the two-stage training:
The necessity of the two-stage training is not experimentally confirmed.
1) How good is the first-stage-only training (i.e., VQ loss is used as a regularizer but the conventional Top-k routers are kept and used in inference) results?
2) Is it impossible to start the second-stage training (i.e,. train VQ routers without  Top-k routers from scratch) from scratch?

### Questions
Please see Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents VQ-MoE approach that uses both sparse MoE and a MoE that is routed based on some vector quantization of the tokens. It claims to theoretically demonstrate that this discrete representation is optimal and addresses the issue of collapse. It presents results in text and image.

### Strengths
I did not understand this work to be able to identify strengths.

### Weaknesses
Very confusingly written and not a clear explanation of the method. Despite reading this work on 3 different occasions I still do not understand the method. I am not able to explain what it does despite being familiar with both MoE and VQ-VAE. In some handwaving way it seems it pre-trains both a sparse moe and a “table lookup” based on a quantization of the intermediate representations and then it discards the sparse moe and only uses the “vq” table lookup during finetune.

I am not sure the scale of the data and experiments are enough to draw any conclusions. For example most MoE papers pretrain on a very different scale of thing. For image results SoftMoe pretrained on JFT-4B and shows zero-shot numbers in CIFAR-100 (ViT-B/16 - 71.0, Soft MoE-S/16 -  67.2) significantly above the **finetune** numbers shown here (67.3 VQMoE) . I think overall the scale of examples here are just not suitable for exploring and comparing MoE methods.

XMoE shows wikitext-103 results where a dense transformer reaches a pplx (22.61) smaller than any reported by this work (23.85 for large VQMoE).

### Questions
Please provide clear explanations of what is done at pre-training, finetune and inference so one can clearly see what it attempts to be done.

What is the setup for image tasks? What was the model pretrained on?

What does your dense baseline obtains in wikitext-103 and why is it so different from XMoE reported numbers?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Vector-Quantized Mixture of Experts (VQMoE), a novel architecture that addresses the challenges of representation collapse and inconsistency in training Sparse Mixture of Experts (SMoE) by using discrete representations learned through vector quantization. Theoretical support and empirical evidence demonstrate VQMoE's ability to overcome traditional router issues, showing a improvement in robustness over other SMoE routing methods while maintaining strong fine-tuning performance.

### Strengths
1. The introduction of Vector Quantization is interesting.

2. The writing is clear.

### Weaknesses
1. The definition of symbols is confusing, especially on Page 3.

For example, what does the v_k mean in Line 129?

What does the Eq. (3) mean in Line 132?

f^v in Line 142 is not present in Eq. (4).

What does the g(x)_c + g(x)_d mean in Line 148?

2. The lacked comparison.

In my understanding, this work maps samples into several discrete embeddings, i.e., the codebook. Thus, each sample corresponds to one embedding and use this embedding for routing. This is similar to [1]. [1] clusters samples into different cluster centers and generates one embedding for each cluster center. Then, [1] uses embedding for routing. Thus, can the authors provide a comparison with this method?

[1] Gou Y, Liu Z, Chen K, et al. Mixture of cluster-conditional lora experts for vision-language instruction tuning.

3. The additional training need for the pre-training stage.

In general, the MoE can be directly used to replace the FFN of the LLM in the fine-tuning stage. However, this work must train the codebook in the pre-training stage. Thus, I kind of disagree with the claim made in Line 367. Although not training the routing in fine-tuning, the additional training time is needed for pre-training.

Besides, I would like to know that whether this technique works for unbalanced datasets. When most samples correspond to one vector in the codebook, this technique may be hard to prevent the collapse. It will be helpful to provide some explanations about it.

In conclusion, although the writing is clear, the rigorousness should be enhanced. In addition, I am concerned about the lacked comparison and the additional training need for the pre-training. Thus, I vote for 5 now.

### Questions
Please refer to the Weaknesses.

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
The article proposes a novel architecture, the Vector-Quantized Mixture of Experts (VQMoE), which aims to address routing inconsistency and representation collapse issues in Sparse Mixture of Experts (SMoE) models, marking the first solution of its kind. Unlike traditional SMoE methods that rely on a router to assign tasks to experts, VQMoE uses discrete representations obtained through vector quantization to select experts. The authors present a theorem demonstrating the existence of routing inconsistency in SMoE and propose a proposition for optimal expert selection. Proofs of the theorem and proposition are provided using counterexamples, and a two-stage training approach is employed. The core idea of VQMoE is to simultaneously learn both continuous and discrete representations, thereby combining the advantages of each. The continuous representation aids the model in capturing complex data details, while the discrete representation quantizes the input, selecting appropriate experts to handle specific tasks. The authors conducted experiments on large language models (LLMs) and vision classification tasks, showing that VQMoE achieves a 28% increase in robustness compared to existing SMoE routing methods.

### Strengths
1. This paper is the first to study discrete representations in Sparse Mixture of Experts (SMoE). Unlike traditional SMoE methods that rely on routers to assign tasks to experts, VQMoE uses discrete representations obtained through vector quantization to select experts, addressing routing inconsistency and representation collapse issues in the model.  
2. A novel VQMoE architecture is proposed that simultaneously learns both continuous and discrete representations.  
3. A theorem and a proposition are presented, with theoretical proofs and experimental validation provided to support them.

### Weaknesses
1. In VQVAE, only one codebook is used. Why are multiple codebooks used in VQMoE, and what difference does this make?
2. The traditional SMoE methods have a drawback of routing inconsistency, which the proposed VQMoE aims to address. However, if two tokens are very similar, how does VQMoE ensure they are not quantized to the same codebook?
3. The proofs of the theorem and definitions in the appendix B, particularly Figures 4 and 5, are unclear. It would be helpful if the authors provided a more detailed explanation of these figures.
4. Performance testing on ImageNet is missing from the classification task evaluations.
5. Although the paper states that experiments were conducted in the Vision domain, they are limited to classification tasks, with no experiments in areas like object detection or segmentation.
6. The writing and formula expressions in the paper are sometimes unclear, with some statements potentially leading to misunderstandings. Examples include the description of Equation (3); the subscripts in Equation (1) being in the lower right corner while they appear in the upper right in Equations (4) and (5); the meaning of `where g(x)c + g(x)d` in Equation (4); the reason for two Cifar10 results under Vision Transformer (Large) in Table 3; “Figures 3c and 3c” in Section 5.5; and “where j ≠ j” in Appendix B.1 for the proofs. Additionally, should `min(dist(y, ey))` be represented as `min(dist(y, ex), dist(y, ey), dist(y, ez))`? I hope the authors will carefully revise these issues in the paper and provide more theoretical and experimental support for the key proofs.

### Questions
My questions align with the issues raised in the weaknesses section, and I hope the authors will provide thorough explanations.
1. For Weakness 1, please provide an ablation study or theoretical analysis comparing single versus multiple codebooks in VQMoE and explain the rationale behind this design choice.
2. For Weakness 2, please provide experiment results or theoretical analysis of how VQMoE handles very similar tokens.
3. For Weakness 3, please provide step-by-step explanations for Figures 4 and 5, including what each axis represents, how the data points were generated, and how these figures support the theorem and definitions in Appendix B.
4. For Weakness 4, please explain why ImageNet was not included, and please include experiments on ImageNet.
5. For Weakness 5, please include additional experiments on vision tasks such as object detection and image segmentation.
6. For Weakness 6, I hope the authors will carefully review the content to address equation inconsistencies, typographical errors, and unclear explanations.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Vector-Quantized Mixture of Experts (VQMoE) as an alternative to SMoE to enhance the efficiency of the Mixture of Expert models. The main objective is to address the "representation collapse" issue, where a small number of experts receive the majority of tokens or all experts converge to learn similar representations, primarily due to the inefficiency of router operations. VQMoE employs a method that assigns experts without a router by using vector quantization. The validity of this approach is theoretically demonstrated, and VQMoE outperforms existing MoE methodologies across various datasets, including both text and visual data.

### Strengths
1. The paper propose a novel MoE approach that mitigates dependency on routers, thereby preventing representation collapse and reducing train/inference computation.
2. Theoretical validation of VQMoE's efficiency was attempted (Theorem 4.1, Proposition 4.2).
3. Experiments were conducted on both text and visual datasets, demonstrating that the model performs well even as the model scales up.

### Weaknesses
1. There are several weaknesses in the theoretical analysis section:

Theorem 4.1 – The assumption that MHA and expert embeddings converge, converging with t_m>>t_e  does not appear to account for the possibility of representation collapse. A specific mathematical approach addressing the occurrence of representation collapse is missing.

Proposition 4.2 – Here, an even less agreeable assumption is made. It assumes that input data can be divided into k clusters; however, it is well-known in the deep learning field that high-dimensional data, such as text or images, does not cluster cleanly. Furthermore, this claim expects the number of clusters to match the number of experts, which is unlikely to hold for real-world data.

2. In the case of visual experiments, only low-resolution datasets were used, making it difficult to conclude that the performance has been sufficiently validated. Additional experiments on high-res datasets, such as ImageNet, would be necessary to strengthen the findings.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
