### Summary

The paper presents a model for integrating and processing multimodal information inspired by neuroscience, called the Information-Theoretic Hierarchical Perception (ITHP) model. The model uses the information bottleneck concept to distill information from various modalities, designating a prime modality and treating others as detectors to create compact and relevant latent representations. ITHP outperforms state-of-the-art benchmarks in multimodal sentiment analysis tasks on CMU-MOSI and CMU-MOSEI datasets, even surpassing human-level performance on some metrics.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The model's use of the information bottleneck principle to create compact and relevant latent representations is a novel contribution to the field of multimodal learning.

The model has been tested on multiple datasets and has consistently outperformed state-of-the-art benchmarks, demonstrating its effectiveness in multimodal sentiment analysis tasks.

The model's ability to surpass human-level performance on some metrics is a significant achievement that highlights the potential of multimodal learning models.

### Weaknesses

#### Some Related Works


#### comment

The paper claims that the proposed model is inspired by neuroscience, but the connection between the model and neuroscience is not very clear. The authors should provide more details on how the model is inspired by neuroscience and how it relates to the brain's information processing mechanisms.

The model's performance is evaluated on a limited number of datasets. To demonstrate the generalizability of the model, it should be tested on a wider range of datasets and tasks.

The paper does not provide any insights into the interpretability of the model. It is difficult to understand how the model is making its predictions, which is a common problem with deep learning models. The authors should consider adding techniques to improve the interpretability of the model.

### Suggestions

The authors should more clearly articulate the specific neuroscientific principles that inspired the Information-Theoretic Hierarchical Perception (ITHP) model. While the idea of a prime modality and supporting modalities is mentioned, the paper lacks a detailed explanation of how this relates to known neural mechanisms. For example, the paper could benefit from a discussion of how the model's hierarchical structure and information bottleneck approach align with the brain's hierarchical processing of sensory information and the concept of efficient coding. The authors should provide a more detailed explanation of how the model's architecture and information processing mechanisms map to specific brain regions and neural pathways. This would involve discussing how the model's latent representations relate to neural representations and how the model's information distillation process aligns with the brain's selective attention mechanisms. Without these details, the claim of neuro-inspiration remains vague and unsubstantiated.

To strengthen the paper's claims of generalizability, the authors should evaluate the ITHP model on a more diverse set of datasets and tasks. The current evaluation is limited to multimodal sentiment analysis tasks on CMU-MOSI and CMU-MOSEI datasets. While these datasets are commonly used, they do not fully capture the complexity and diversity of real-world multimodal scenarios. The authors should consider evaluating the model on datasets that involve different modalities, such as visual, auditory, and textual data, and tasks that require different types of reasoning, such as action recognition, event detection, and visual question answering. This would provide a more comprehensive assessment of the model's ability to generalize to different types of multimodal data and tasks. Furthermore, the authors should provide a detailed analysis of the model's performance on each dataset and task, highlighting the strengths and weaknesses of the model in different scenarios. This would help to identify the limitations of the model and guide future research.

The authors should address the lack of interpretability of the ITHP model by incorporating techniques that allow for a better understanding of the model's decision-making process. The paper currently does not provide any insights into how the model is making its predictions, which makes it difficult to trust the model's results and to identify potential biases. The authors could consider using techniques such as attention visualization, saliency maps, or feature importance analysis to identify the most relevant input features that contribute to the model's predictions. Furthermore, the authors could explore methods for visualizing the model's latent representations to gain a better understanding of how the model is encoding multimodal information. This would involve developing techniques for projecting the high-dimensional latent representations into a lower-dimensional space that can be visualized and interpreted. By improving the interpretability of the model, the authors can increase the trustworthiness of the model and provide valuable insights into the underlying mechanisms of multimodal integration.

### Questions

Can the authors provide more details on how the model is inspired by neuroscience and how it relates to the brain's information processing mechanisms?

How does the model's performance compare to other state-of-the-art multimodal learning models on a wider range of datasets and tasks?

Are there any plans to improve the interpretability of the model?

### Rating

5

### Confidence

2

**********
