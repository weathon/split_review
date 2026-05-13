# Reconstructing Training Data From Real-World Models Trained with Transfer Learning

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
\vspace{-4pt}
Current methods for reconstructing training data from trained classifiers are restricted to very small models, limited training set sizes, and low-resolution images. Such restrictions hinder their applicability to real-world scenarios. In this paper, we present a novel approach enabling data reconstruction in realistic settings for models trained on high-resolution images. Our method adapts the reconstruction scheme of~\cite{haim2022reconstructing} to real-world scenarios -- specifically, targeting models trained via transfer learning over image embeddings of large pre-trained models like DINO-ViT and CLIP. Our work employs data reconstruction in the embedding space rather than in the image space, showcasing its applicability beyond visual data. Moreover, we introduce a novel clustering-based method to identify good reconstructions from thousands of candidates. This significantly improves on previous works that relied on knowledge of the training set to identify good reconstructed images. Our findings shed light on a potential privacy risk for data leakage from models trained using transfer learning. % methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores optimization-based **data inversion** techniques from pre-trained models with transfer learning, in which we could reconstruct the training data simply given the pre-trained encoder and classifier itself. It extends the model-inversion techniques with improved designs like loss, generative decoder. The clustering-based approach further demonstrates the possibility of high-quality reconstructions to the original data. Experiments on two common datasets reveals the potential privacy risks associated with models trained on sensitive data.

### Strengths
[**Novelty**] 
- Working in embedding space instead of directly reconstructing images is an innovative approach, and makes it more scalable to different models on both visual and non-visual data
- the adoption of clustering and averaging technique is novel, which identifies high-quality reconstructions when training data is not available

[**Significance**] 
- it highlights the significant privacy risks associated with models trained with sensitive data in a transfer learning setup, in which high-resolution data reconstruction in real-world conditions emphasizes the critical need for privacy-preserving mechanisms with today's pre-trained models. 

[**Completeness & Clarity**]
- High-quality visualizations, including comparisons of reconstructed images to original data and plots that illustrate reconstruction metrics, add depth to the evaluation, making it easier to interpret the results.
- The writing is clear, which effectively lays out the motivation and approach, and well explains the limitations

### Weaknesses
- On significance, while I like the simple paradigm of solving x when f is known within f(x)=y, I kind feel that reconstructed data samples are not exactly matching with the actual training data, especially when the training data is not available. It is more close to averaged per-category data when training data is not available, the author might want to turn down their scope.
- Another thinking is that the current method may only work with classifiers-based model, for more more fine-grained training data reconstruction from segmentation model like SAM might be more desired. Also the reconstruction quality varies significantly with the choice of backbone model (DINO, CLIP, etc.), which affects the novelty of the clustering approach by making it model-dependent.
- As the author also mentioned, the inversion process used to map embeddings back to images is computationally expensive, which could hinder scalability

### Questions
- I am also wondering whether we have any baselines in this line of data inversion techniques
- a quick question, for diffusion-based generative models, wondering whether it is also a more realistic concern to reveal training data directly.

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
This paper studies the training data reconstruction problem. Different from previous methods, this paper studies the data reconstruction from models trained in a transfer learning approach, and claims the first approach to reconstruct images from the latent features. The experimental section showcases comprehensive results to verify the efficacy of proposed method in different datasets and backbone networks.

### Strengths
1. This paper is easy to follow.
2. I appreciate the comprehensive experiments performed to analyze the effectiveness of the proposed approach.

### Weaknesses
1. The technique contribution is limited. This paper aims to reconstruct images from latent features (embeddings), however, the key components used for this purpose are borrowed from previous works. Specifically, it use ‘’Reconstructing training data from trained neural networks’’ to reconstruct embeddings, followed by ‘’Splicing vit features for semantic appearance transfer’’ to convert embeddings into RGB images.
2. The resolution of reconstructed images are still low (224x224).
3. The experiment part contains results of this method, but without any comparison with other approaches.

### Questions
See weakness

### Soundness
2

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
2

### Summary
This paper demonstrates the reconstruction of high-resolution training images from models trained using a transfer learning approach, as well as the reconstruction of non-visual data. Moreover, it introduces a novel clustering-based approach for effectively identifying training samples without prior knowledge of the training images.

### Strengths
1. The writing is well done and clear.

2. They present the weaknesses and limitations of their method in detail.

3. The experiments consider various commonly used pre-trained feature extractors such as CLIP, demonstrating the effectiveness of their method.

### Weaknesses
1. The method is limited to specific cases where a fixed feature extractor and some MLP layers serve as the classifier. It cannot generalize to other more common transfer learning scenarios, such as fine-tuning an entire classifier or certain layers of a classifier.

2. The introduced method lacks innovation. Specifically, the core contributions of reconstructing embedding vectors in Section 3.1 and mapping embedding vectors in Section 3.2 to the image domain either originate from other works or involve only simple modifications, such as changing the MSE loss to the cosine similarity loss. Please clearly explain the novel aspects of the method introduced.

3. The format of Figure 9 is incorrect as it exceeds the page boundary.

### Questions
My confusion is the aforementioned weaknesses. If there are any misunderstandings, please point them out.

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
5

### Summary
This paper proposes a new method for training data reconstruction. Different from other works, this paper proposes to recover the image embedding first, and then employs a inversion network to reconstruct the images. Especially, this paper proposes to use the clustering-based approach for effectively identifying training samples. Experiments show the performance of the proposed method.

### Strengths
The proposed method has show better performance compared with baselines, on the datasets of Food-101 and iNaturalist.

### Weaknesses
1. The experiments are only conducted on the CLIP and DINO which has served as the common components for the image diffusion models. However, I think the proposed network should be suitable for various networks. I wonder the training data reconstruction with other basic networks, like ResNet. And the authors should explain why they focused on transformer-based models in the experimental section.

2. This paper claims to be suitable for the reconstruction of high-resolution images, while the experiments are only conducted on the datasets with low resolution like 224 (why 224x224 fits that definition of "high resolution" in this paper?). I wonder the performance with higher resolution like 512.

3. There is no quantitative metric to compare the reconstruction effects between the proposed method and baselines. For example, using the reconstructed images can lead to a model with the similar accuracy of the original model?

4. The presentation of this paper is not good. For example, the texts in Fig.9 has be out of the width constraint, which could be resized.

### Questions
1. What is the performance of the proposed method with more types of networks besides the transformer?

2. What is the reconstruction performance on images with higher resolution?

3. Can the authors provide more reliable quantitative metrics?

### Soundness
2

### Presentation
2

### Contribution
2
