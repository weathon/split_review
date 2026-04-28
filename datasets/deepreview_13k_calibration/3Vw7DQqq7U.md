# LEMON: Lossless model expansion

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Scaling of deep neural networks, especially \Transformers{}, is pivotal for their surging performance and has further led to the emergence of sophisticated reasoning capabilities in foundation models.
Such scaling generally requires training large models from scratch with random initialization, failing to leverage the knowledge acquired by their smaller counterparts, which are already resource-intensive to obtain.
To tackle this inefficiency, we present \textbf{L}ossl\textbf{E}ss \textbf{MO}del Expansio\textbf{N} (LEMON), a recipe 
to initialize scaled models using the weights of their smaller but pre-trained counterparts. This is followed by model training with an optimized learning rate scheduler tailored explicitly for the scaled models, substantially reducing the training time compared to training from scratch.
Notably, LEMON is versatile, ensuring compatibility with various network structures, including models like Vision Transformers and BERT.
Our empirical results demonstrate that LEMON reduces computational costs by 56.7\% for \vit{} and 33.2\% for BERT when compared to training from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed a lossless model expansion method which initialize scaled models using the weights of smaller pre-trained model. Specifically, the proposed method break the symmetry of replicated neurons by setting their fan-out weights to be unequal, and introduce average expansion to deal with LayerNorm for indivisible width increment. Besides, the authors explored the training recipes for the expanded models and proposed an optimized learning rate scheduler that decays more rapidly than training from scratch. Experimental results show that the proposed method can effectively expand both Vision Transformer and BERT, while significantly reducing the training overhead.

### Strengths
1. The motivation is clear. The author focus on scaling deep neural networks in effective way by leveraging the knowledge acquired by their smaller counterparts.
2. The paper is well organized in terms of written description. The authors provided easy-to-understand diagrams.
3. The idea is technically feasible and the authors provide detailed proofs in appendix.

### Weaknesses
1. The challenge arising with the ‘symmetry breaking’ is described in the third paragraph of section Introduction: “the expanded model will never gain more capacity than the source model.”This statement raises confusion as training a model with smaller capacity but larger size appears to be of limited value, which incurs greater overhead but achieves limited performance. 
2. Have the considered baselines for expansion in Section 6 been confirmed to be lossless? If not, it is necessary to present the gap with the original model. If they are indeed lossless, an analysis should be provided to explain why the proposed method achieves higher validation accuracy compared to AKI, which also breaks symmetry, as shown in Figure 8.
3. The results in Table 2 are a bit confusing. It is unclear whether model expansion or longer training duration indeed contributes to the improved performance.
4. The novelty of this paper seems quite limited. The key idea of model expansion seems a simple extension of net2net. Are there any essential technical differences? In my opinion, a simple extension of an existing approach is insufficient for a top-tier conference.

### Questions
Please refer to the weakness part.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Idea**: 
* This paper introduces a method for initializing scaled models using the weights of their smaller pre-trained counterparts. The method allows for expanding neural network models in a lossless manner, increasing depth and width without sacrificing performance.
* The paper introduces lossless layer expansion techniques, including row-average expansion, row-zero expansion, column-random expansion, and column-circular expansion.
* The expansion procedure for LayerNorm and Multi-head Attention (MHA) modules in Pre-LN Transformer blocks is explained, showing that the expansion is lossless and preserves the properties of the original layers.

**Experiments and Analysis**: 
* The method is versatile and compatible with various network structures, although the _experiments are only shown on Vision Transformers and BERT_. LEMON outperforms baselines on these architectures in terms of performance and computational cost.
* Detailed explanations and insights into various techniques and approaches for training deep neural networks are provided, with a focus on language models.
* The authors investigate the effects of maximum learning rate and learning rate scheduler when training expanded models.
* LEMON is compared to a similar method called LiGO and shows better results in terms of computational saving.

### Strengths
### S1 - Interesting technical contributions
* The authors provide a comprehensive and detailed exploration of lossless model expansion techniques (e.g. row-average expansion, row-zero expansion, column-random expansion, and column-circular expansion), including addressing the challenges of symmetry breaking and indivisible width increments.
* Provide valuable insights into training recipes for expanded models, including an optimized learning rate scheduler that can further enhance performance.

### S2 - Good results and experimental analysis
* Extensive experiments with ViT and BERT are shown with a thorough investigation of the effects of maximum learning rate and learning rate scheduler when training expanded models.
* The proposed method achieves similar performance to the original models with fewer training epochs, highlighting its efficiency and effectiveness.
* LiGO is a similar very recent method, and LEMON shows better results in terms of computational saving.

### Weaknesses
### W1 - Experiments limited only to ViT and BERT

*   The paper could benefit from experiments on the generalizability of LEMON to other architectures beyond Vision Transformers and BERT models. For example, CNN models are completely unexplored in terms of experiments.
*   I suggest adding model expansion experiments for ResNet18 --> ResNet50 and EfficientNetB0 --> EfficientNetB4 (or other variants). Specifically, the authors should investigate whether the lossless expansion property holds when transitioning between different architectural blocks, such as from the Basic block used in ResNet18 to the BottleNeck block used in ResNet50. Moreover, exploring the application of LEMON to EfficientNets would provide insights into its effectiveness on models designed through neural architecture search, which often have more complex and varied layer structures.

### W2 - Lacks theoretical analysis/explanation of "effect of learning rate and schedule"

*   Sections 5.1 and 5.2 experimentally study the effect of learning rates and schedules. However, the paper lacks a theoretical analysis of why this happens. For example, why does a small learning rate lead to lower final performance? I think only experimental verification is not enough and this requires some theoretical analysis. A deeper dive into the optimization landscape of the expanded models could reveal insights into the observed behavior. For instance, analyzing the Hessian spectrum of the loss function at various stages of training might shed light on the sensitivity of the model to different learning rates. Additionally, investigating the relationship between the learning rate, batch size, and the magnitude of gradient updates could provide a more nuanced understanding of how these factors interact during the training of expanded models.

### Questions
Can "incremental" model expansion help achieve even better performance? For example, instead of expanding from "Model (small) pretrained --> Model (huge)", would it be better to expand in steps as "Model (small) pretrained --> Model (middle) --> Model (big) --> Model (huge)"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a model expansion algorithm that uses the pre-trained parameters of a smaller model to initialize a larger model. The proposed algorithm allows expanding model’s width and depth to arbitrary width and depth for most Transformer variants. The algorithm ensures that the larger model has the same output as the smaller model (thus does not require calibration dataset) to preserve the small model performance while having symmetry breaking for continuous training to further optimize the larger model. The expansion algorithm alone does not ensure that the larger model can achieve the same performance as the same sized model trained from scratch using smaller training cost. The authors found right training configuration is critical for obtaining this goal.

### Strengths
1. The proposed method is simple, yet it allows expanding smaller model to arbitrary width and depth (not necessarily indivisible by the width and depth of the original models) while ensuring the output of the expanded model stays the same as smaller model and parameter symmetry breaking. 

2. The expansion can be performed on individual modules of a Transformer. This localized expansion ensure compatibility with different Transformer variants. 

3. The expansion algorithm alone does not give desired performance. The authors explored different training configuration, including learning rate and scheduler, for more desired performance and found the training configurations greatly affect the results. 

4. The authors performed ablation study to isolate the effect of optimized training configuration from expansion algorithms to make sure the proposed expansion algorithm indeed performs better compared to baselines.

### Weaknesses
1. In Figure 7 (c) and (d), the loss curves for BERT language modeling are still decreasing when training is stopped. It might be better to train the model till convergence to evaluate whether or not the proposed method can have the same performance as the model trained from scratch.

2. Vision Transformer is a pre-norm Transformer, and in BERT language modeling, the authors also used the pre-norm variant. Since the authors claimed compatibility of the algorithm with different variants, it would be better to see the experiments on different variants (at least a post-norm variant) to verify the claim. While in Appendix, the authors show lossless expansion for other variants, it is also important to evaluate the performance metrics.

3. Since this work also studies the initialization of model parameters, it might be interesting to compare the proposed idea with other initialization approach, such as Mimetic initialization (https://arxiv.org/abs/2305.09828, also mentioned in the related work)

### Questions
The suggestions are listed in weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a model expansion method that utilizes knowledge from existing smaller models. The authors analyze and design for different model structures, breaking the symmetry of repeating units by setting unequal output weights. This leads to a lossless model expansion approach. The training process is thoroughly analyzed, and the method achieves promising experimental results for both Vision and NLP Transformer models.

### Strengths
- The paper provides a comprehensive review of related work, presenting the current research status of expanding small models into larger ones.
- The method is highly versatile, as it is designed and analyzed for different structures within the Transformer, making it applicable to commonly used Transformer architectures. Moreover, they provide practical tuning suggestions for training.
- The analysis and observations made in the experiments are interesting.
- The authors demonstrate significant acceleration during the training process.

### Weaknesses
 - After reading this paper, I would like to know more about the practical application of the model expansion method in real-world scenarios. Please provide more examples to illustrate the effectiveness and applicability of the proposed approach.
- How does the performance change in Figure 6b when using a learning rate larger than the default value?

- Regarding the significant drop in accuracy during the early stages of training, it may be attributed to the transfer of pre-trained parameters from one local optimum to another. Considering the requirements of certain real-time systems, such performance drop in model accuracy is unacceptable.  I think maybe we can smooth out this process by, for example, setting a mask to control the number of trainable parameters in each epoch, gradually transitioning them to avoid a drastic drop in accuracy. Overall, solving this problem could be of significant importance for many real-world applications.

### Questions
- Regarding the significant drop in accuracy during the early stages of training, it may be attributed to the transfer of pre-trained parameters from one local optimum to another. Considering the requirements of certain real-time systems, such performance drop in model accuracy is unacceptable.  I think maybe we can smooth out this process by, for example, setting a mask to control the number of trainable parameters in each epoch, gradually transitioning them to avoid a drastic drop in accuracy. Overall, solving this problem could be of significant importance for many real-world applications.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
