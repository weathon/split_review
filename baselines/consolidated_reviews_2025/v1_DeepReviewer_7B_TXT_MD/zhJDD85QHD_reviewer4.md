### Summary

This paper proposes a novel approach called Concept-based Explainable Image Representation (CEIR) for learning high-quality image representations without label dependency. The method first uses a Contrastive Language-Image Pretraining (CLIP) model to project input images into a concept vector space. A Variational Autoencoder (VAE) is then trained to learn a latent representation from these projected concepts. The authors demonstrate that CEIR achieves state-of-the-art results in unsupervised clustering tasks on various datasets, including CIFAR10, CIFAR100-20, CIFAR100, STL10, and ImageNet. The paper also highlights the interpretability of the learned representations, showing that CEIR can generate human-understandable concepts from both training and open-world images.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The motivation for the proposed method is clearly explained, and the methodology is presented in a structured manner.
2. The proposed method is innovative in its use of a concept-based approach to learn image representations without relying on labels. This approach is particularly valuable in scenarios where labeled data is scarce or unavailable.
3. The authors provide extensive experimental results on multiple datasets, demonstrating the effectiveness of CEIR in unsupervised clustering tasks. The results are competitive with state-of-the-art methods, highlighting the potential of the proposed approach.
4. The paper emphasizes the interpretability of the learned representations, which is a significant advantage of concept-based methods. The authors demonstrate that CEIR can generate human-understandable concepts from both training and open-world images, making it a valuable tool for understanding and interpreting image data.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. For example, the authors do not address how the method would perform on datasets with complex or abstract concepts, or how the choice of concept labels might affect the quality of the learned representations. Specifically, the paper does not explore the sensitivity of the method to the quality of the initial concept embeddings from CLIP, nor does it analyze how the performance might degrade with less informative or noisy concept embeddings. Furthermore, the paper does not discuss the potential for the learned concept space to collapse or become trivial, especially if the concept embeddings are not sufficiently diverse or discriminative.
2. The evaluation metrics used in the paper are not comprehensive. While the authors report NMI, ACC, and ARI for clustering tasks, they do not provide a detailed analysis of the learned representations using other metrics, such as the ability to preserve semantic relationships between concepts or the robustness to adversarial attacks. The paper lacks a quantitative assessment of the interpretability of the learned representations, such as the degree to which the concepts align with human-understandable categories or the stability of the concept assignments under perturbations. The absence of these metrics makes it difficult to fully assess the quality and utility of the learned representations.
3. The paper does not compare the proposed method with other state-of-the-art representation learning methods, which makes it difficult to assess the true performance of the proposed approach. The paper should include comparisons with other unsupervised representation learning methods, such as autoencoders or contrastive learning approaches, to provide a more comprehensive evaluation of the proposed method's strengths and weaknesses. Without these comparisons, it is difficult to determine whether the proposed method offers any significant advantages over existing techniques.

### Suggestions

The authors should conduct a more thorough analysis of the limitations of their proposed method. This should include an investigation into the sensitivity of the method to the quality of the initial concept embeddings from CLIP. Specifically, the authors should explore how the performance of CEIR degrades when using less informative or noisy concept embeddings. This could involve experiments with different CLIP models or by introducing noise into the concept embeddings. Furthermore, the authors should analyze the potential for the learned concept space to collapse or become trivial. This could be done by examining the diversity and discriminative power of the learned concepts, and by visualizing the concept space to identify potential issues. The authors should also discuss the computational cost of the method, particularly the training of the VAE, and how this cost scales with the size of the dataset and the number of concepts.

To address the lack of comprehensive evaluation metrics, the authors should include a quantitative assessment of the interpretability of the learned representations. This could involve measuring the degree to which the concepts align with human-understandable categories, perhaps by using human evaluation or by comparing the learned concepts with existing taxonomies. The authors should also evaluate the robustness of the learned representations to adversarial attacks. This could be done by adding small perturbations to the input images and measuring how the concept assignments change. Additionally, the authors should explore the ability of the learned representations to preserve semantic relationships between concepts. This could be done by measuring the correlation between the distances in the concept space and the semantic similarities between the corresponding concepts. The authors should also consider using metrics that specifically measure the quality of the learned representations for downstream tasks, such as image classification or retrieval.

Finally, the authors should include a more comprehensive comparison with other state-of-the-art representation learning methods. This should include comparisons with other unsupervised representation learning methods, such as autoencoders or contrastive learning approaches. The authors should also compare their method with other concept-based representation learning methods, if available. This comparison should be done on a variety of datasets and using a range of evaluation metrics. The authors should also discuss the computational cost of their method compared to other methods. This would help to determine whether the proposed method offers any significant advantages over existing techniques in terms of both performance and efficiency. The authors should also provide a more detailed analysis of the strengths and weaknesses of their method compared to other approaches.

### Questions

1. How does the proposed method handle datasets with complex or abstract concepts? Are there any specific strategies or modifications that could be made to improve performance on such datasets?
2. How sensitive is the method to the choice of concept labels? Could the authors provide more insights into how the quality of the concept labels affects the quality of the learned representations?
3. What are the computational costs associated with training the proposed method? How does it scale with the size of the dataset and the number of concepts?
4. How does the proposed method compare with other state-of-the-art representation learning methods in terms of both performance and computational efficiency?

### Rating

6

### Confidence

3

**********
