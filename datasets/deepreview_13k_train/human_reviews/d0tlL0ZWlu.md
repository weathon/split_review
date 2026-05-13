# EXPLOITING DISTRIBUTION CONSTRAINTS FOR SCALABLE AND EFFICIENT IMAGE RETRIEVAL

- Decision: Accept
- Scores: 6, 5, 5, 6, 3

## Abstract
Image retrieval is crucial in robotics and computer vision, with downstream applications in robot place recognition and vision-based product recommendations. Modern retrieval systems face two key challenges: scalability and efficiency. 
    State-of-the-art image retrieval systems train specific neural networks for each dataset, an approach that lacks scalability. 
    Furthermore, since retrieval speed is directly proportional to embedding size, existing systems that use large embeddings lack efficiency.
    To tackle scalability, recent works propose using off-the-shelf foundation models. However, these models, though applicable across datasets, fall short in achieving performance comparable to that of dataset-specific models. 
    Our key observation is that, while foundation models capture necessary subtleties for effective retrieval, the underlying distribution of their embedding space can negatively impact cosine similarity searches.
    We introduce \spacefullname \ (\spacename), which, when used for projection, significantly improves the performance of foundation models. We provide an in-depth theoretical analysis of \spacename. 
    Addressing efficiency, we introduce Single-shot Similarity Space Distillation (\distname), a novel approach to learn embeddings with adaptive sizes that offers a better trade-off between size and performance. 
    We conducted extensive experiments on four retrieval datasets, including Stanford Online Products (SoP) and Pittsburgh30k, using four different off-the-shelf foundation models, including DinoV2 and CLIP. \spacename\ demonstrates up to a $16\%$ improvement in retrieval performance, while \distname\ shows a further $10\%$ improvement for smaller embedding sizes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for facilitating the image retrieval task. It focuses on solving two challenges, scalability and efficiency, existed in the image retrieval. To tackle scalability, strong variance constraints are introduced to restrict the latent features. The variance of feature in different dimensions could be similar, so that improving the discriminative ability of the latent features. For the efficiency, a Single-shot Similarity Space Distillation method is introduced to generate adaptive size features, and keep the cosine similarity of sample features. The experiments show that the AE-SVC improve the retrieval performance, especially for the foundation models. The (SS)_2D can improve the performance for smaller embedding sizes.

### Strengths
1. The paper presents Autoencoders with Strong Variance Constraints (AE-SVC), an unsupervised method. By enforcing orthogonality, mean centering, and unit variance constraints in the latent space, AE-SVC shifts the cosine similarity distribution to be more discriminative. This advancement addresses the scalability issue in current SOTA methods.
2. The authors introduce Single Shot Similarity Space Distillation ((SS)_2D), that preserves the similarity structure of embeddings without requiring retraining for different dimensions. (SS)_2D produces adaptive embeddings where smaller segments maintain high retrieval performance, addressing the impracticality of separate training for varying embedding sizes found in methods like PCA or traditional autoencoders.
3. The paper's two-step approach, first enhancing embeddings with AE-SVC and then applying (SS)_2D, yields significant improvements in retrieval performance across multiple datasets and foundation models. Experimental results show that this method not only accelerates retrieval speed by reducing embedding dimensions but also surpasses the accuracy of existing unsupervised techniques and even the original full-sized embeddings.

### Weaknesses
1. The detail of the projection function F in L280 may need more explanations. The size of the embedding \hat{z} is adaptive. The change of the embedding size whether influences the projection F. In other words, there are matched functions for different size m.
2. The figures in Fig. (3,4,5) are small. It is hard to distinguish data points of lower embedding dimensions. It could be better that the quantity results are listed in a table.

### Questions
1. During training, does the back propagation happen after traversing the whole dataset or a batch of the images? Would the choice of two ways influence the performance?
2. Does the embedding size reduction influence the cosine similarity variance or other constraints for AE-SVC of the output features? 
3. Does the performance be changed if the order of SVC and (SS)_2D switch? Or would the performance be improved if append SVC on the resized embeddings?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper discusses two major concerns regarding image retrieval: scalability and efficiency. The concerns are more meaningful when existing retrieval methods use foundation models as feature extractors. To improve the foundation model's performance on retrieval tasks, the authors proposed Autoencoders with Strong Variance Constraints, which enforced three constraints on the learned latent space. Meanwhile, Single-shot Similarity Space Distillation outputs more compact embeddings with flexible dimensions for the model efficiency.

### Strengths
The authors focus on major concerns about using the foundation model in image retrieval or even more CV tasks: how to promote foundation model features and balance model performance and efficiency. By aligning teacher and student similarity spaces, the proposed distillation with flexible output dimensions indeed reduces retrieval compute resources.

### Weaknesses
1. The motivation of AE-SVC is worth discussing: it encourages the network to learn the normal embedding distribution (mean to 0, std to 1), but gt labels of dataset-specific tasks may biased.
2. The authors claim that they are the first to explore representation learning ideas in image retrieval, considering retrieval is essentially a feature learning task, the soundness is not as remarkable as claimed.
3. AE-SVC is only compared with the standard PCA in Sec.5.2, more competitors (e.g. PCA variants or AnyLoc ) are needed to demonstrate the effectiveness of AE-SVC, if possible.
4. Experiment settings in Fig.4 and Fig.5 are not consistent. Compared with AE-SVC, the results of (SS)2D seems incomplete.

### Questions
1. My major concern is whether the learned normal distribution is still effective in the biased target domain, which is common in dataset-specific tasks. Without the prior information of the target domain, it is ambiguous for neural networks to distinguish instances by discriminative features or global features ( discriminate shirt shape or visually more similar image in the example in Fig.2, the former would be right in commerce recommendation system and the latter is more likely to be the output of the common search engine)
2. The settings of Fig.4 and 5 are not consistent, and it is hard to discriminate results in different styles (color, line and dot). It would be better to list the results in tables for better comparison.
3. It is contrary to common sense that the performance of ViT > DINO-Base > DINO-Large in InShop results in Fig.4, but the results of Pittsburgh30K and TokyoVal are normal.
4. Without additional data, student models learned from teachers would get inferior results. Based on AE-SVC (orange) in Fig.5, it seems that applying feature distillation (green) further improves the retrieval performance. It would be better to add an analysis of this point in the experiment.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses two key challenges in large-scale image retrieval systems: scalability and efficiency. To enhance scalability, the authors focus on improving the performance of existing foundation models. For efficiency, they propose an effective unsupervised dimension reduction technique.

### Strengths
- Overall, the paper is well-motivated and well-written, aiming to solve an important problem in large-scale image retrieval.
- The theoretical aspects are well-developed, though it is unclear if the approximation in Eq. 11 is sufficiently supported. It may benefit from references to statistics or mathematical literature rather than an Arxiv paper in biology.
- Experiments demonstrate the method's effectiveness, showing significant improvement.

### Weaknesses
- I am somewhat skeptical about the scenario described in L39-L42; in fact, self- or semi-supervised learning might address this issue (see related works [1, 2]).
- I have some doubts about the novelty of AE-SVC, as it combines several common losses. Additionally, there are four losses in Eq. 5, but no explanation is provided on how they are balanced. Experiments or theoretical support in this regard would be beneficial.
- The experimental results are somewhat limited. Is there additional related work beyond PCA for comparison? Also, I noticed a lack of ablation studies, as only two experiments, shown in Fig.4 and Fig.5, are provided.

[1] eProduct: A Million-Scale Visual Search Benchmark to Address Product Recognition Challenges

[2] V2L: Leveraging Vision and Vision-language Models into Large-scale Product Retrieval

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to improve image retrieval under the context of using pretrained image foundation models. Two concrete techniques are designed: (1) Autoencoders with Strong Variance Constraints (AE-SVC) regularizes the embeddings from foundation models to improve the the retrieval performance, (2) Single-shot Similarity Space Distillation ((SS)_2D) compresses the embedding in an adaptive way to accelerate the retrieval. The paper provides theoretical and empirical analyses to justify the effectiveness of AE-SVC. The experimental results show that the proposed approaches can effectively improve the retrieval performance/efficiency of embedding from four different visual foundation models across four datasets.

### Strengths
1. The proposed approaches are quite simple yet effective. AE-SVC is backed up by some reasonable empirical analyses in Sec.4. The adaptive dimension reduction brought by (SS)$_2$D is interesting and can be practically useful to avoid training multimodal models for different embedding dimensions.

2. The authors conduct thorough experiments to demonstrate the effectiveness of the proposed approaches: 4 image retrieval datasets and 4 visual foundation models are considered, and AE-SVC + (SS)$_2$D consistently show positive results for efficient and accurate image retrieval.

3. A codebase is provided in the supplementary material. Roughly looking through the code, all necessary model/data components are included, ensuring the reproducibility of the paper.

### Weaknesses
1. The theoretical analysis in Sec.4 is only conducted based on the Gaussian distribution assumption, which does not necessarily hold for the embeddings from the visual foundation models. Based on the PDF visualization in Figure 3, the true distribution of cosine similarity between image embeddings is far from Gaussian.

2. In large-scale retrieval, approximate nearest neighbour (ANN) is commonly used to accelerate the retrieval process, so the complexity analysis of image retrieval in the paper is not necessarily right in real-world applications. 

3. The figure placement can be optimized. The method details should not be in the first figure, which increases the burden of understanding the introduction, and forces people to switch back and forth when reading the method section.

### Questions
The paper focuses on improving the embedding from image foundation models by unsupervised training without any labels. However, given the recent advancements in multimodal LLMs, it seems possible to leverage these models (like GPT-4o) to automatically produce reasonable labels for fine-tuning image embedding models. If this is feasible, would the proposed approaches still be practically useful, given the fact mentioned in the paper that dataset-specific models are better than foundation models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work uses a foundation model for image retrieval, making two contributions: (1) AE-SVC trains an autoencoder on top of the foundation model such that the latent vectors have statistical (mean and covariance) properties inspired or equivalent to centering, PCA and whitening. (2) SS2D performs dimensionality reduction jointly for multiple target dimensions by distilling a similarity matrix from the AE-SVC encoder to another student encoder. Both are learned on the test (reference) set, while the foundation model is pre-trained and frozen.

### Strengths
The idea is well motivated. The methodology is sound. The writing is of high quality and mostly clear. The experiments support the claims on a number of datasets and models. The two contributions are shown to be effective comparing with simple baselines.

### Weaknesses
The novelty is incremental, while important related work and baselines are missing. The setting of learning on the test set is questionable. Comparisons with baselines are lacking, not fair and not informative enough. Section 4 fails to properly separate existing work by Smith et al. (2023) from this work and is partly unclear. More details follow.

1. The paper addresses image retrieval and performs evaluation on standard deep metric learning and place recognition datasets. It misses revelant foundational work on image retrieval, including methodologies, benchmarks and protocols:

    > [*1] Gordo et al. 2016, Deep Image Retrieval: Learning Global Representations for Image Search
    >
    > [*2] Radenovic et al. 2017, Fine-Tuning CNN Image Retrieval with No Human Annotation
    >
    > [*3] Radenovic et al. 2018, Revisiting Oxford and Paris: Large-Scale Image Retrieval Benchmarking
    >
    > [*4] Weyand et al. 2020, Google Landmarks Dataset v2: A Large-Scale Benchmark for Instance-Level Recognition and Retrieval

    This work should be repositioned against this work in terms of novelty and protocols used. The related work and experiments sections should be extended accordingly, considering additional training and test datasets and evaluation protocols from these works.

2. The motivation for AE-SVC is scalability. That is, it is challenging to have a labeled dataset-specific training set, hence it is suggested to learn in an unsupervised on the test (reference) set. On one hand, this setting is extremely problematic because it transfers the burden from training to testing, by having to learn something on the test set. The latter is in many practical applications constantly changing, hence the model would need to be constantly updated. It is a kind of overfitting to the test set that has never been used in standard work like the references above. To my knowledge, it has only been used in

    > [*5] Liu et al. 2019, Guided Similarity Separation for Image Retrieval

    Hence, this work should be a baseline for comparison if the authors insist in their setting of learning on the test set. On the other hand, if the motivation to learn in an unsupervised way, this can still be done on a separate training set. For example:

    > [*6] Kim et al. 2022, Self-Taught Metric Learning without Labels

    Besides, learning in [2*] may be supervised, but with labels obtained automatically without human annotation. Self-supervised learning should not be a reason to learn on the test set.

3. In AE-SVC, I believe variance loss (3) is redundant. It is merely the diagonal part of covariance loss (2). Other than that, the covariance loss (2) and centering loss (4) are inspired by centering, PCA and whitening. Hence, AE-SVC should be compared to a baseline where centering, PCA and whitening are performed as post-processing on features extracted by the foundation model, without learning. This baseline is missing. Whitening has a long history in image retrieval but ignored here. Also very successful is supervised discriminative whitening [*2], which could be adapted for self-supervision to be used as a baseline.

4. In SS2D, I believe the loss is the same as

    > [*7] Park et al. 2019, Relational Knowledge Distillation

   The authors cite this paper but do not discuss the actual relation with their work. I believe the only new component here is applying it for dimensionality reduction and learning for multiple target dimensions at once, which are pretty incremental contributions. Also very relevant is

    > [*8] Kalantidis et al. 2022, TLDR: Twin Learning for Dimensionality Reduction

    in the sense that it is also learning a kind of autoencoder on top of frozen feature for dimensionality reduction. Instead of a reconstruction loss, it uses the Barlow Twins loss on the output vectors, which is the same as the covariance loss here, but uses cross-correlation instead. Both the architecture and cross-correlation matrix should be compared to as baselines.

5. Section 4 is useful and interesting, but it is presented as new to a large extent while it actually all comes from Smith et al. (2023). The only new part is the experiment of Figure 3. In addition, parts are copied from Smith et al. (2023) without carrying over all relevant information, such that the resulting text is unclear. For example, (8) refers to "discriminative power" but there is nothing to discriminate here, whereas Smith et al. (2023) compare the distribution of target similarities to a "null" or "background" distribution where the term "discriminative" makes sense. As another example, (14) results in a "global minimum" without saying anything about the function being convex, which is shown indeed by Smith et al. (2023).

    In the analysis of Section 4, the data is taken to be centered and nothing is said about the effect of this choice to the distribution of similarities, either here or in Smith et al. (2023). To my understanding, the variance of similarities is a **concave** function of the mean and is **maximized** when the mean is zero. This is the opposite of what happens with whitening and raises questions on the motivation of minimizing the variance. To the very least, the experiment of Figure 3 should be extended to also show the distribution of similarities with centered data but without PCA and whitening. It should also include centering, PCA and whitening as post-processing steps rather than being learned with (2), (3) and (4).

6. In the experiments of Figures 4 and 5, the current work (AE-SVC, SS2D or SSD) uses an additional encoder on top of the foundation model, while the "default" and "PCA" are using the foundation model alone, hence are not comparable. These results tell us nothing about whether the benefit is coming from the properties encouraged by the loss functions, the additional learned parameters or the adaptation to the test set. These are three factors that should be evaluated independently in some way, for example by fine-tuning the last layers of the foundation model rather than adding an extra encoder.

    Whitening by post-processing after PCA should be definitely added as a baseline. TLDR or other state of the art dimensionality reduction methods should also be added, because centering, PCA, whitening and VAE are very basic baselines.

### Questions
1. The mean and covariance quantities in (4) and (2) (also variance in (3), but this is redundant as discussed above), are global in the sense that they are measured on all $n$ samples of the test set. What happens when the test set is large and how are they treated when learning with a stochastic optimizer in mini-batches? Are mini-batches used in this work?

2. Can the authors confirm or refute my understanding that the variance of similarities is a concave function of the mean and is maximized when the mean is zero? In the latter case, how would they update the paper?

### Soundness
2

### Presentation
3

### Contribution
2
