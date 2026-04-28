# Escaping the Big Data Paradigm in Self-Supervised Representation Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
The reliance on large-scale datasets and extensive computational resources has become a significant barrier to advancing representation learning from images, particularly in domains where data is scarce or expensive to obtain. In this paper, we address the critical question: Can we escape the big data paradigm in self-supervised representation learning from images? We introduce SCOTT (Sparse Convolutional Tokenizer for Transformers), a simple tokenization architecture that injects convolutional inductive biases into Vision Transformers (ViTs), enhancing their efficacy in small-scale data regimens while remaining compatible with Masked Image Modeling (MIM) tasks. Alongside, we propose MIM-JEPA, a Joint-Embedding Predictive Architecture within a MIM framework, operating in latent representation space to capture more semantic features. Our approach enables ViTs to be trained from scratch on datasets orders of magnitude smaller than traditionally required --without relying on massive external datasets for pretraining. We validate our method on three small-size, high-resoultion, fine-grained datasets: Oxford Flowers-102, Oxford IIIT Pets-37, and ImageNet-100. Despite the challenges of limited data and high intra-class similarity, our frozen SCOTT models pretrained with MIM-JEPA significantly outperform fully supervised methods and achieve competitive results with state-of-the-art approaches that rely on large-scale pretraining, complex image augmentations and bigger model sizes. By demonstrating that robust off-the-shelf representations can be learned with limited data, compute, and model sizes, our work paves the way for computer applications in resource constrained environments such as medical imaging or robotics. Our findings challenge the prevailing notion that vast amounts of data are indispensable for effective representation learning, offering a new pathway toward more accessible and inclusive advancements in the field.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces SCOTT, a Sparse Convolutional Tokenizer designed to enhance Vision Transformers (ViTs) by incorporating convolutional inductive biases, enabling effective self-supervised learning on small datasets. SCOTT integrates with MIM-JEPA, a Joint-Embedding Predictive Architecture within a Masked Image Modeling (MIM) framework, to capture higher-level semantic features. The approach is validated on fine-grained datasets, such as Oxford Flowers-102 and Oxford IIIT Pets-37, achieving competitive results with significantly fewer data and computational resources.

### Strengths
1. This paper addresses an important problem: enabling model training on small-scale, unlabeled datasets, which is critical for advancing self-supervised learning in data-limited settings.

2. The authors conduct extensive experiments using multiple datasets.

### Weaknesses
1. The contributions of the proposed methods appear incremental compared to previous work.

2. The evaluation and comparisons with baseline and prior methods seem unfair due to differences in training setups.

3. The writing quality could be improved for clarity and readability.

### Questions
This paper proposes SCOTT and MIM-JEPA, two components that collaboratively enable effective model training on small-scale, unlabeled datasets. Together, they achieve promising results and open avenues for future research in resource-constrained settings. However, I have the following questions and concerns.

1. The novelty of SCOTT appears limited. Many prior works have explored injecting convolutional layers into vision transformers, as mentioned in the paper. The key challenge in combining convolutional layers with masked image modeling (MIM) is that the masked areas can diminish due to the convolutional nature. However, sparse convolution techniques, including submanifold sparse convolution, have been well-established for managing masked areas, and it seems that SCOTT directly adopts these existing techniques. Could the authors elaborate on the unique contributions of SCOTT over these previous approaches?

2. I am unclear about the novelty of MIM-JEPA compared to I-JEPA. The training pipelines for the two methods seem very similar. Could the authors provide further details to clarify the specific contributions of MIM-JEPA beyond what is already achieved by I-JEPA?

3. The evaluation methodology raises concerns about fairness:

   3.1 For the baseline of training a model from scratch with fully supervised learning, is only the final (or several) layers trained, or is the entire model fine-tuned? From the text, it appears to be the former, which would weaken this baseline and result in significantly lower accuracy compared to pre-trained methods. To properly evaluate the effectiveness of supervised learning, which is generally a strong baseline, the entire model should be trained for the same number of epochs as in pre-training (300 or 1200 epochs).

   3.2 When comparing with SSL pre-training baselines and other SSL works, the datasets used for pre-training differ, raising concerns about fairness. While prior methods are pre-trained on larger datasets like ImageNet or LVD-142M, SCOTT+MIM-JEPA is pre-trained on the target dataset itself, which is then also used for evaluation (e.g., attention or linear probing). This overlap can lead to an advantage, as the model learns features directly from the target dataset. For a fair comparison, SCOTT+MIM-JEPA should pre-train on a small, unrelated dataset. For instance, if Flowers-102 is used for evaluation, then Pets-37 or ImageNet-100 could serve as a pre-training dataset.

4. The accuracy of SCOTT+MIM-JEPA is still notably lower than models trained on large-scale data. While this is expected, the significant accuracy gap makes it difficult to consider the approach "promising," especially given the aforementioned evaluation concerns.


minor point(s):

1. The method is tailored specifically for MIM-related self-supervised learning, which limits its application scope, as it is not compatible with contrastive learning. However, given the popularity of MIM, this specialization is understandable and not a major issue.

2. The paper's writing could be improved. The paper references many prior works that inspired it, but the current organization makes it challenging to distinguish the unique contributions of this work.

3. Introducing I-JEPA in the background section would be helpful, as the current work builds directly upon it.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Sparse Convolutional Tokenizer for Transformers (SCOTT) which is a tokenization architecture that injects convolutional inductive biases into Vision Transformers. The purpose it enable small-scale data training while compatible with MIM tasks. The author of the paper also proposes Joint-Embedding Predictive Architecture within a MIM framework. The experiments on small-scale dataset shows promising results.

### Strengths
1. This paper is easy to follow and has clean organization. 

2. This topic is promising since training Transformer-based vision model is very data thirsty.

### Weaknesses
1. The comparison experiments in the paper is weak since there are tons of conv+ViT baselines. This paper, however, only compare to a few, also the related works missed many related references. Therefore, the paper’s experiments is not quite convincing.

2. The motivation is clear but this paper lacks the analysis of related works. What kind of problems are there for similar design? Why the proposed method is better? Why choosing such design (e.g., MIM-JEPA)? The overall elaboration is not quite self-sufficient.

3. The experiments are not sufficient to demonstrate the effectiveness of the method. The settings and comparison is too simple, and very limited ablations are conducted.

### Questions
Please refer to weaknesses.

### Soundness
1

### Presentation
2

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
The paper introduces two advancements in self-supervised learning from images with limited data SCOTT (Sparse Convolutional Tokenizer for Transformers) and MIM-JEPA (Masked Image Modeling with Joint-Embedding Predictive Architecture). SCOTT infuses convolutional biases into ViTs, enhancing their effectiveness in data-constrained environments, while MIM-JEPA optimizes the representation learning in a latent space. This dual approach reduces the dependency on large-scale datasets, enabling effective training on datasets like Oxford Flowers-102, Oxford IIIT Pets-37, and ImageNet-100.

### Strengths
1. The integration of convolutional biases through SCOTT and the focus on semantic feature extraction via MIM-JEPA can shift away from the reliance on extensive pre-training datasets.

2. The proposed methods outperform fully supervised methods and achieve results competitive with state-of-the-art models pre-trained on much larger datasets.

### Weaknesses
1. The authors claim that the datasets used are high-resolution; however, I believe these datasets should not be considered high resolution.  (Of course, compared to low-resolution CIFAR and MNIST, there are). I suggest that the authors also include results from higher, domain-specific resolution datasets, as well as from low-resolution datasets, to provide a more comprehensive analysis of performance variations across different resolutions. Specifically, the current evaluation lacks a rigorous exploration of how the proposed method scales with increasing image resolution, which is crucial for real-world applications where high-resolution imagery is common. The absence of such analysis limits the generalizability of the findings.

2. The methodology appears to be primarily limited to classification tasks. Although the authors mention that future work will extend to segmentation, it would be beneficial if they could discuss the potential applicability of their methods to segmentation tasks more explicitly. The current discussion lacks specific details on how the convolutional tokenizer (SCOTT) and the joint-embedding predictive architecture (MIM-JEPA) would be adapted for dense prediction tasks. For example, the paper does not address how the patch-based processing of ViTs, which is not naturally suited for segmentation, would be handled with their approach. A more detailed discussion of the architectural modifications and training strategies required for segmentation is needed.

3. Fine-tuning on pre-trained general models might still be the best way to train domain-specific images, offering less training time and potentially better performance. The authors should consider comparing their approach directly to traditional fine-tuning methods to substantiate their claims and highlight any genuine advantages or limitations. The current comparison is insufficient as it does not provide a direct comparison of training time and computational resources required by the proposed method versus traditional fine-tuning. A more detailed analysis of the trade-offs between the two approaches is necessary to fully evaluate the practical utility of the proposed method.

### Questions
1. What specific advantages do convolutional biases offer over other techniques designed to improve data efficiency in vision models, such as attention augmentation or advanced data augmentation techniques?


2. Can the authors provide preliminary insights on how their approach might be adapted for segmentation?

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
This work demonstrates that robust off-the-shelf representations can be learned with limited data, compute, and model sizes by integrating a Sparse Convolutional Tokenizer into Transformer architectures. The authors introduce CNN-like inductive biases while maintaining compatibility with masked image modeling objectives, enabling the self-supervised pretraining for Masked Image Modeling. To show the advantages of the paper, the authors provide extensive comparisons with other baseline methods on several downstream tasks. The authors also conducted an ablation study to show the effectiveness empirically.

### Strengths
+ The paper is well-organized and easy to read.
+ The paper proposes a Joint-Embedding Predictive Architecture for the Masked Image Modeling task, enabling self-supervised pre-training on a much smaller dataset.
+ This paper provides strong performance across all the tasks and architecture in a self-supervised learning setting.

### Weaknesses
 - The difference between the proposed Sparse Convolutional Tokenizer for Transformers (SCOTT) and SparK is not obvious, it looks more like a simple leverage of previous work. The authors need to claim more of the difference with previous work.
- Experimental results with different settings are not very comparable. As for the model size, pre-training datasets, pre-training method setting are all different from the method proposed in the paper. Although the author claims that achieving absolute performance is not the main goal, the results are supposed to be comparable. For example, experiments can be added to utilize Dino/I-JEPA or other pre-training paradigms to train on the small dataset and compare it with the proposed method.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
