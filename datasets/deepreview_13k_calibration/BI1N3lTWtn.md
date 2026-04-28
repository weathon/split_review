# A Multi-Level Framework for Accelerating Training Transformer Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
The fast growing capabilities of large-scale deep learning models, such as Bert, GPT and ViT, are revolutionizing the landscape of NLP, CV and many other domains. Training such models, however, poses an unprecedented demand for computing power, which incurs exponentially increasing energy cost and carbon dioxide emissions. It is thus critical to develop efficient training solutions to reduce the training costs. Motivated by a set of key observations of inter- and intra-layer similarities among feature maps and attentions that can be identified from typical training processes, we propose a multi-level framework for training acceleration. Specifically, the framework is based on three basic operators, Coalescing, De-coalescing and Interpolation, which can be orchestrated to build a multi-level training framework. The framework consists of a V-cycle training process, which progressively down- and up-scales the model size and projects the parameters between adjacent levels of models via coalescing and de-coalescing. The key idea is that a smaller model that can be trained for fast convergence and the trained parameters provides high-qualities intermediate solutions for the next level larger network. The interpolation operator is designed to break the symmetry of neurons incurred by de-coalescing for better convergence performance. Our experiments on transformer-based language models (e.g. Bert, GPT) as well as a vision model (e.g. DeiT) prove that the proposed framework reduces the computational cost by about 20\% on training BERT/GPT-Base models and up to 51.6\% on training the BERT-Large model while preserving the performance

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an efficient multi-level training framework, inspired by the observation of similarities within layers of these models during training. This framework employs a novel approach using three operators: Coalescing, De-coalescing, and Interpolation, to manage model scaling and parameter projection across different model sizes. It introduces a V-cycle training process that alternates between smaller, quickly trained models and larger networks, using the former to provide intermediate solutions for the latter. The interpolation operator is particularly crucial for enhancing convergence by adjusting neuron symmetries after de-coalescing. Experiments show that this framework can reduce computational costs by approximately 20% for BERT/GPT-Base models and up to 51.6% for BERT-Large, without compromising on model performance

### Strengths
1. The idea inspired by the multigrid algorithm to accelerate the large model training by coalescing, de-coalescing and interpolation is very clear and promising.
2. Demonstrating the effectiveness of the proposed method is very solid and sound. The interpolation plays an important role in improving the learning ability.
3. The reduction in FLOPs and training time is very significant in NLP transformer models.

### Weaknesses
1. Though significant speedup in the NLP transformer, the proposed method has limited improvement in FLOPs and time reduction in the large vision model. 
2. It's unclear how to initialize the matrix F. It seems the F can be arbitrary and the initialization of F is not discussed sufficiently.
3. The evaluation result on GPT and DeiT-S lacks a comparison with other works.

### Questions
1. Can you explain how the intra- and inter-layer similarity is utilized in the coalescing and de-coalescing procedure? 
2. Can you explain why the performance is limited on the vision transformer?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a multi-level framework for accelerating the training of large-scale deep learning models. This approach is inspired by the observation that training smaller models is more cost-effective and thus the authors propose a solution by generating high-quality intermediate solutions for subsequent larger networks.

Specifically, the authors propose a V-cycle learning process composed of three operations: Coalescing, De-coalescing and Interpolation. The Coalescing operator reduces the model size in terms of width, followed by depth. The De-coalescing operator is the inverse operation of Coalescing, with the de-coalescing matrices defined as the normalized transposition of the coalescing matrices. To address the low-rank issue present in the transformations, the authors also propose the Interpolation operation, which merges the de-coalesced model into the previous one. The authors suggest integrating the three operations into a V-cycle training framework, which learns to coalesce and train small models and then de-coalesce them into bigger models with Interpolation progressively.

The authors also provide experimental results on transformer-based models (BERT, GPT) and a vision model (DeiT), demonstrating significant speed-up (up to >50%) in training while maintaining performance.

### Strengths
The idea is clearly presented, and the experimental results appear robust, providing strong support for the conclusions drawn.

### Weaknesses
I feel the overall novelty of this paper is a bit limited, as compared with LiGO. I find the major differences lie in two aspects:

 -LiGO learns linear mapping matrices via SGD, while this work intuitively defines the coalescing matrix as $[I, I]^T$, seeking to directly coalesce two neighboring neurons and adjacent layers;
 -As discussed in Appendix B, LiGO gradually learns to increase the model size, whereas this paper introduces V-cycle, a first-coalescing-then-decoalescing learning process equipped with interpolation.

Despite the above, the improvements in FLOPs & Walltime and GLUE over LiGO are marginal (see Table 1). Additionally, more controlled experiments would be beneficial to substantiate the rationale for choosing heuristically defined mapping matrices over learnable parameters. The interpolation operation, which the authors claim mitigates the low-rank issue encountered in LiGO, is reminiscent of well-known PEFT methods like LoRA. More comparisons with this line of research would enhance the persuasiveness and credibility of the proposed method.

Lastly, the authors introduce the multigrid algorithm with a detailed description. However, it seems the proposed framework has little to do with this algorithm.

### Questions
What is the significance of the coalescing operation within the overarching framework, and what benefits does it offer compared to initiating the training process with smaller models? In the coalescing step, the compression matrices F_in and F_out in equation 1 and 2, and R in equation 4 are heuristically defined. The recover matrices G in equation 7, and T_in and T_out are also manually defined without further explanation or theoretical basis. I feel the key point of this framework lies in modeling the correlation of parameters between large models and small models. I am not very convinced, from a methodological point of view, why the proposed framework can help to converge faster on the training set D.

Aside from conserving computational resources, what benefits do the interpolating model M_{k} and the de-coalesced model M_{k, de-coalesced} offer compared to continuing training the de-coalesced model M_{k, de-coalesced}?

At the end of the algorithm, the M_{1} model necessitates further training to achieve convergence. I'd like to see the computational overhead of this phase, as well as the comparative experimental results after removing this component.

Most efforts of the experiments are on BERT models. Competitive compared methods, say LiGO, are not included in the results of GPT and DeiT in Table2 & 3. 

In Table 4, as the number of Levels increases, the author's method not only saves more computational resources but also further improves the performance of the final model. What is the rationale for this observed enhancement in performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Transformer-based models perform well in many research areas such as NLP, CV, etc. However, they usually incur exponentially increasing energy costs in the training process. This paper proposes a multi-level framework for training acceleration. The whole working flow is composed of Coalescing, De-coalescing, and Interpolation. More specifically, first, the model is coalesced in both the width and depth direction. Then the large model can be coalesced into a smaller model. Next, to map the parameters back to the original model, the model is depth de-coalesced and then width de-coalesced. Next, after training the smaller model generated by coalescing, it conducts de-coalescing and then merges the coalesced model and de−coalesced model under the control of a hyperparameter. Finally, the merged larger model is trained. The proposed framework is evaluated on both accuracy and speed. The evaluation results show that the framework can keep or even slightly improve the accuracy and reduce the FLOPs and wall time.

### Strengths
+ The work proposes a novel method for improving the speed of Transformer-based models.
+ It is carefully written.
+ It offers enough analysis and explanations about the coalescing and de-coalescing details of the Transformer and the reason why this framework is designed in this way.

### Weaknesses
 - The explanations in section 3 are helpful. However, it would be more helpful if it could include a flow chart or a figure of the structure of the whole framework.
- Algorithm 1 in section 3.4 can help the readers understand the whole flow of the framework but is also kind of sketchy.

### Questions
1. How different are the original model and the final model merged by the coalesced model and de−coalesced model? Do they have the same dimension? What are the differences between these two models?
2. What does the number in the brackets represent in Tables 1 and 4?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a multi-level framework for training large-scale deep learning models like BERT, GPT, and ViT. The framework utilizes operators such as Coalescing, De-coalescing, and Interpolation to exploit inter- and intralayer similarities in feature maps and attentions. It follows a V-cycle training process that progressively adjusts the model size and transfers parameters between levels. Experimental results demonstrate that the proposed framework significantly reduces computational costs  while maintaining performance.

### Strengths
1. The paper introduces a novel multi-level framework for training large-scale deep learning models. By leveraging inter- and intralayer similarities, the framework addresses the challenge of high computational costs in training such models. The proposed operators and V-cycle training process provide a unique and effective solution. The V-cycle training process is different to the previous width/depth expansion methods like bert2BERT [1] and network expansion [2].

[1] Chen, Cheng, et al. "bert2BERT: Towards Reusable Pretrained Language Models." Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2022.
[2] Ding, Ning, et al. "Network Expansion for Practical Training Acceleration." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

2. The paper supports its claims with extensive experiments conducted on transformer-based language models (BERT, GPT) and a vision model (DeiT). The experimental results demonstrate the effectiveness of the proposed framework, showcasing significant reductions in computational costs while preserving performance.

3. Broad Applicability: The strengths of the paper lie not only in its application to specific models like BERT and GPT but also in its potential applicability to other large-scale deep learning models such as ViT. This suggests that the proposed framework has broader relevance and can contribute to addressing the training cost challenges across various domains and tasks.

### Weaknesses
1. The paper lacks in-depth technical explanations about the proposed operators (Coalescing, De-coalescing, and Interpolation) and their implementation. The description of these operators is too high-level, making it difficult to understand the precise mechanisms and potential limitations. For instance, how is the 'coalescing' operation implemented at the tensor level? What specific mathematical operations are involved in 'de-coalescing'? The paper should provide a more detailed explanation of the interpolation process, including the interpolation method used (e.g., linear, bilinear, or other) and the rationale behind its selection. Additionally, the paper should clarify why the V-cycle training process is better than the previous width/depth expansion methods like bert2BERT and Network Expansion, with a more detailed analysis of the specific advantages and disadvantages of each approach.

2. The paper does not provide a thorough comparison with existing methods or alternative approaches for training acceleration, e.g., Network Expansion [1]. The comparison should not only focus on the final performance but also analyze the computational cost, memory usage, and training time. A more detailed analysis is needed to understand the specific scenarios where the proposed framework outperforms existing methods and where it may fall short. For example, does the proposed method have any limitations in terms of model size or training data? The paper should also discuss the potential impact of different hyperparameter settings on the performance of the proposed framework compared to other methods.

3. The paper does not extensively discuss the potential trade-offs or limitations introduced by the proposed framework. For example, are there any trade-offs in terms of model accuracy, generalization ability, or robustness? A thorough analysis of these aspects would provide a more comprehensive understanding of the framework's impact on model performance. The paper should also discuss the potential impact of the proposed framework on the model's convergence speed and stability. Furthermore, it is unclear how the proposed framework affects the model's ability to handle different types of data or tasks. A more detailed discussion of these potential trade-offs is needed to provide a comprehensive understanding of the framework's limitations.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
