### Summary

This paper proposes a method for learning visual concepts using pre-trained text-to-image (T2I) models. The key idea is to train a set of concept encoders to extract concept embeddings from images, which can be used to generate novel images with different concept combinations. The concept encoders are trained using a reconstruction loss and an anchoring loss that encourages the embeddings to be close to text embeddings obtained from a pre-trained visual question answering (VQA) model. The method is evaluated on several datasets and shown to achieve better disentanglement and compositionality compared to text-based prompting baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple yet effective. It leverages existing pre-trained models and requires minimal additional training.
- The use of text anchors from a pre-trained VQA model is a novel idea that helps to improve the disentanglement of concept embeddings.
- The method is evaluated on multiple datasets and shown to achieve better disentanglement and compositionality compared to baselines.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on the quality of the pre-trained VQA model for obtaining text anchors. If the VQA model is not accurate or biased, it could affect the performance of the proposed method.
- The method is only evaluated on a limited number of datasets. It would be interesting to see how it performs on more diverse and challenging datasets.
- The method requires training a set of concept encoders for each dataset. This could be computationally expensive and time-consuming, especially for large datasets.

Minor issues:
- Figure 3: The notation for the concept encoders is not consistent with the rest of the paper. It should be $f_{k, \gamma}$ instead of $f_{k}$.
- Section 3.3: The description of the generalization to unseen concepts via test-time finetuning is not very clear. It would be helpful to provide more details on how this is done and what the results are.

### Suggestions

The reliance on a pre-trained VQA model for text anchors is a significant point that needs further consideration. While the authors acknowledge this dependency, the potential impact of VQA model biases on the learned concept embeddings is not fully explored. For instance, if the VQA model consistently associates a specific color with a particular object, this bias could be transferred to the concept encoder, leading to a less disentangled representation. It would be beneficial to investigate the sensitivity of the proposed method to different VQA models or to explore techniques for mitigating the impact of VQA biases. This could involve using an ensemble of VQA models or incorporating a debiasing strategy during the training process. Furthermore, a more detailed analysis of the types of errors made by the VQA model and their effect on the final concept embeddings would be valuable.

Expanding the evaluation to more diverse and challenging datasets is crucial for demonstrating the robustness of the proposed method. The current evaluation is limited to relatively simple datasets, and it is unclear how the method would perform on datasets with more complex scenes, objects, and attributes. For example, evaluating on datasets with fine-grained object categories or datasets with significant variations in lighting and viewpoint would provide a more comprehensive assessment of the method's capabilities. Additionally, it would be interesting to see how the method performs on datasets where the concepts are not explicitly labeled, requiring the model to learn them from the data. This would provide a more realistic evaluation of the method's ability to discover and represent visual concepts.

The computational cost of training a separate set of concept encoders for each dataset is a practical concern that needs to be addressed. While the authors mention that the training time is reasonable, the memory requirements and the overall scalability of the method are not fully discussed. For large datasets, training multiple encoders could become prohibitively expensive. It would be beneficial to explore techniques for reducing the computational cost, such as using a shared encoder architecture or employing knowledge distillation techniques. Furthermore, a more detailed analysis of the training time and memory requirements for different dataset sizes would be valuable for assessing the practical applicability of the method.

### Questions

- How sensitive is the method to the choice of the pre-trained VQA model? Have you tried using different VQA models and how does it affect the results?
- How does the method perform on datasets with more complex scenes and objects? It would be interesting to see the results on datasets like COCO or ImageNet.
- What is the computational cost of training the concept encoders? How does it scale with the size of the dataset?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
