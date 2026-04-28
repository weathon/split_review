# Parameter-Efficient Multi-Task Model Fusion with Partial Linearization

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Large pre-trained models have enabled significant advances in machine learning and served as foundation components.
Model fusion methods, such as task arithmetic, have been proven to be powerful and scalable to incorporate fine-tuned weights from different tasks into a multi-task model. 
However, efficiently fine-tuning large pre-trained models on multiple downstream tasks remains challenging, leading to inefficient multi-task model fusion. %
In this work, we propose a novel method to improve multi-task fusion for parameter-efficient fine-tuning techniques like LoRA fine-tuning.
Specifically, our approach partially linearizes only the adapter modules and applies task arithmetic over the linearized adapters.
This allows us to leverage the the advantages of model fusion over linearized fine-tuning, while still performing fine-tuning and inference efficiently.
We demonstrate that our partial linearization technique enables a more effective fusion of multiple tasks into a single model, outperforming standard adapter tuning and task arithmetic alone.
Experimental results demonstrate the capabilities of our proposed partial linearization technique to effectively construct unified multi-task models via the fusion of fine-tuned task vectors. 
We evaluate performance over an increasing number of tasks and find that our approach outperforms standard parameter-efficient fine-tuning techniques. The results highlight the benefits of partial linearization for scalable and efficient multi-task model fusion.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Efficient finetuning on the pretrained large model has been an important topic. In this work, a partial linearization method (L-Lora) is proposed under the context of PERF(parameter-efficient finetuning).  The key idea is applying linearization to adapter modules and applies task arithmetic over the linearized adapters. In practice, first-order Tayler expansion is used to linearize the model dynamics at time $t$. Based on the derivation from a neural tangent kernel theory, the hypothesis is that partial linearization of a subset of model parameters during fine-tuning can also improve weight disentanglement compared to full non-linear fine-tuning. CLIP and Flan-T5 are used to verify the hypothesis in vision-language and language domains.

### Strengths
- Evaluations are conducted on both vision-language and language tasks. 
- The proposed method achieved significant performance improvement, compared with the standard LoRA strategy.

### Weaknesses
 - In vision domain, only the high-level vision task like image classification tasks evaluated, the mid-level and low level task are missing, for example, semantic segmentation.


### Questions
- From table 1, seems the L-LoRA method are outperforming full-finetuning under some model fusion settings, do we have some possible illustrations?
- Is it possible to evaluate L-LoRA on image segmentation foundational models like SAM?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method for Parameter-Efficient Fine Tuning (PEFT) of large pre-trained foundational models for multi-task models. The authors build on prior work in weight disentanglement (Ortiz-Jimenez et al. 2023) and extend it to LoRA for better fusion of models. The authors hypothesise that partial linearisation of a model through the LoRA modules during fine-tuning can improve weight disentanglement, which is conducive to better task arithmetic. Results are shown on a variety of experiments whereupon the proposed models outperforms others on vision classification tasks.

### Strengths
1. This is a very well written paper, motivations are clear, results are (mostly) well presented and it is clear to understand the results.

2. The idea to perform partial linearisation on LoRA modules is interesting and nicely presented. The results, especially on CLIP-ViT-B-16 (Figure 5a) are compelling argument to the original hypothesis of the work being correct.

### Weaknesses
1. A key result of the paper is the result from Appendix A which allows the authors to hypothesize that partial linearization of a subset of module parameters (here LoRA) can improve weight disentanglement.

    1a. This result needs to be in the main body of the text and properly explained. Without, it is difficult to 
    understand exactly why the authors claim this.

    1b. Having checked the derivation in Appendix A, the authors show that the model output of a linearised 
    model is only determined by the gradient of the loss in the non-linearised model on task $t_i$. How 
    exactly then does this allow the authors to make the central hypothesis, which guides the presented 
    method? Specifically, the derivation shows that the change in the linearized model's output is proportional to the gradient of the loss with respect to the model's parameters at initialization. This relationship, while mathematically sound, does not immediately explain why linearizing a subset of parameters (LoRA) would inherently lead to better weight disentanglement compared to linearizing all parameters or not linearizing at all. The connection between this specific form of linearization and the core hypothesis needs to be more explicitly justified.

2. The results on the NLP task (Flan T-5-Base) need to be better explain. The method (L-LoRA) not only performs worse than full fine-tuning (so does LoRA fine-tuning) but also worse on average than LoRA. Why is this? Is the presented model only applicable to vision tasks? The performance drop of L-LoRA compared to LoRA on the NLP task is particularly concerning. The authors should investigate whether this is due to the specific nature of the NLP tasks chosen, or if there is a fundamental limitation of the L-LoRA method when applied to sequence-based models. The lack of consistent performance across different modalities raises questions about the general applicability of the proposed approach.

### Questions
1. Section 4.2 introduces parameter scaling laws for weight disentanglement. However, what does this have to do with the method or key results? The scaling laws suggest over-parameterisation is necessary for weight disentanglement. I struggle to see the connection between this and the need to partially linearize a model for fine-tuning.

2. A remark in the manuscript is made bottom of page 8 that "...higher cosine similarity...implies greater redundancy and overlap...This results in more destructive task interference with naïve merging". I don't follow this as it seems to be opposite to most work in multi-task training. In that setting, naïve training would favour similar tasks as it would not require methods to mitigate task interference (see GradNorm method). Why is this then opposite in the context of this paper?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel method to improve multi-task fusion for parameter-efficient fine-tuning techniques like LoRA fine-tuning. Specifically, their approach partially linearizes only the adapter modules and applies task arithmetic over the linearized adapters. This allows us to leverage the advantages of model fusion over linearized fine-tuning, while still performing fine-tuning and inference efficiently. Extensive experiments are conducted.

### Strengths
1. The code is provided.
2. This paper proposes a new linearized LoRA method.
3. Extensive experiments are conducted.

### Weaknesses
1. The novelty of this paper is limited. This paper simply adapts the proposed method in [1] by replacing full fine-tuning with LoRA. Thus, the method in this paper is obviously more efficient than [1] since LoRA is more efficient than full fine-tuning.
2. The definition of the task vector of LoRA in this paper seems to be unreasonable.
3. The L-LoRA has a large performance drop on single-task fine-tuning (Figure 7) and a slight increase on the merged case (Table 1, especially in the NLP domain) compared to LoRA. Thus, it is unclear what are the advantages of L-LoRA compared to LoRA.

### Questions
### Major Concerns:
1. The novelty of this paper is limited. [1] studies the linearized full fine-tuning while this paper simply replaces full fine-tuning with LoRA. Although the authors emphasize the proposed method is more efficient than [1], it is obvious since LoRA is more efficient than fully fine-tuning.
2. What's the meaning of $\phi_0$? For the full fine-tuning, $\theta_0$ is the pre-trained model weight and is shared for every task $\tau_i$. However, for LoRA, $\phi_i$ is newly added parameters for each task $\tau_i$. Thus, what is $\psi_0$? Is $\psi_0$ a shared initialization for LoRA matrixes of every task $\tau_i$?
3. In [2], the task vector of full fine-tuning is defined as $\nu_i=\theta_i-\theta_0$, which means the parameter change of $\theta_0$. Thus, why the task vector of LoRA in this paper is defined as the change of LoRA parameters $\phi_i-\phi_0$ rather than the change of $\theta_0$ as in [3], i.e., $A_iB_i$, where $\phi_i=[A_i, B_i]$ is the LoRA parameters.
4. Table 1 only shows the average normalized scores over multiple datasets, so how about the performance of each dataset? Could you provide it in the Appendix?
5. It seems the proposed L-LoRA method does not perform well on the NLP domain, according to the results in Table 1 and the similarity heatmap in Figure 8.
6. Why use the proposed L-LoRA rather than the existing LoRA? The single-task fine-tuning results in Figure 7 show that L-LoRA has a large performance drop compared to LoRA in many datasets.  

### Minor Concerns:
1. The caption of Figure 3(c): not linearized?


**References**

[1] Task Arithmetic in the Tangent Space: Improved Editing of Pre-Trained Models. arXiv:2305.12827.

[2] Editing Models with Task Arithmetic. ICLR, 2023.

[3] Effective and Parameter-Efficient Reusing Fine-Tuned Models. arXiv:2310.01886.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach to enhance multi-task fusion in large pre-trained models. The authors introduce partial linearization of adapter modules combined with task arithmetic, improving the fusion of multiple tasks while maintaining efficient fine-tuning and inference. Experimental results demonstrate that this method outperforms standard techniques, especially as the number of tasks increases. The contribution lies in its ability to construct unified multi-task models effectively and efficiently fuse fine-tuned task vectors, highlighting the benefits of partial linearization for scalable multi-task model fusion.

### Strengths
- The paper exhibits a clear and logical structure, making it easy to comprehend.

- The proposal's effectiveness is demonstrated through comprehensive experiments conducted on both NLP and image classification tasks. The visualization provided in Figure 6 offers intriguing insights into disentanglement error, further substantiating the proposal's efficacy.

### Weaknesses
 - The absence of experiments conducted on larger-scale models diminishes the significance of the proposal.


### Questions
- Can the proposed methods demonstrate effectiveness on SOTA models?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
