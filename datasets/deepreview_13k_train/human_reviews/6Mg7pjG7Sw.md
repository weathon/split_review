# CSA: Data-efficient Mapping of Unimodal Features to Multimodal Features

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Multimodal encoders like CLIP excel in tasks such as zero-shot image classification and cross-modal retrieval. However, they require excessive training data.
We propose canonical similarity analysis (CSA), which uses two unimodal encoders to replicate multimodal encoders using limited data.
\name maps unimodal features into a multimodal space, using a new similarity score to retain only the multimodal information.
\name only involves the inference of unimodal encoders and a cubic-complexity matrix decomposition, eliminating the need for extensive GPU-based model training.
Experiments show that \name outperforms CLIP while requiring $300,000\times$ fewer multimodal data pairs and $6\times$ fewer unimodal data for ImageNet classification and misinformative news captions detection.
\name surpasses the state-of-the-art method to map unimodal features to multimodal features.
We also demonstrate the ability of \name with modalities beyond image and text, paving the way for future modality pairs with limited paired multimodal data but abundant unpaired unimodal data, such as lidar and text.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new approach called Canonical Similarity Analysis (CSA) that addresses the challenge of training multimodal encoders, like CLIP, which typically require large amounts of paired multimodal data. CSA achieves efficient multimodal mapping by using two unimodal encoders, thereby reducing data requirements significantly. CSA utilizes canonical correlation analysis to map unimodal features into a multimodal space and introduces a weighted cosine similarity function to replicate multimodal similarity scores. Experiments across tasks such as image classification, misinformation detection, and cross-modal retrieval demonstrate CSA’s data efficiency and robustness, especially in scenarios with limited or noisy data.

### Strengths
S1: (**Data Efficiency and Good Performance**) CSA requires significantly fewer multimodal data pairs by relying on unimodal encoders, which could benefit researchers constrained by data or computational resources. It needs as little as 35,000 image-text pairs to match the performance of CLIP on ImageNet, which is especially notable.

S2: (**Computational Simplicity**) One of the most accessible aspects of CSA is its ability to function effectively without requiring GPU-intensive training, which is a significant advantage for researchers with limited computational resources. 

S3: (**Theoretical Analysis**)The authors include a theoretical analysis for CSA using canonical correlation analysis.

### Weaknesses
W1: (**Hyperparameter Sensitivity and Limited Justification for $s$ Selection**)
The choice of the hyperparameter $s$ in the canonical similarity metric (Section 4.2) lacks comprehensive justification. While the authors discuss a trade-off in feature distinguishability based on $s$, a more detailed sensitivity analysis showing how varying $s$ affects downstream performance across tasks would add clarity, as the framework is quite sensitive to $s$ indicated by content in Table 3. Table 3 provides some insights, but a broader, task-specific evaluation could make the effects of this parameter choice clearer and improve reproducibility for other researchers. Specifically, the paper should explore how the optimal value of $s$ changes when the dimensionality of the input features varies significantly across modalities, as this could impact the effectiveness of the canonical correlation analysis. Furthermore, the paper should investigate the robustness of the method to suboptimal choices of $s$, which is crucial for practical applications where fine-tuning this parameter might be difficult.

W2: (**Weakness on Number of Modalities Supported**) While CSA shows promising results with image-text pairs and briefly explores audio-text applications in the appendix, the experimental evaluation of additional modalities remains limited and lacks depth. The audio experiments, while mentioned, do not provide a strong enough demonstration of CSA’s effectiveness beyond the main image-text modality. This limited exploration weakens CSA’s claim of generalizability across modalities and would benefit from more robust testing on diverse modality pairs to strengthen its applicability in multimodal contexts. The paper should include experiments with modalities that have significantly different characteristics from images and text, such as sensor data or medical imaging, to demonstrate the versatility of the proposed approach. The current experiments do not fully support the claim that CSA can effectively handle a wide range of modalities.

W3: (**Scalability Concerns**) While CSA requires fewer training samples to match performance on certain benchmarks (e.g., ImageNet classification with 35,000 image-text pairs), some datasets or applications may still demand larger sample sizes to achieve comparable performance, especially those with more complex or diverse data structures. For instance, datasets like OpenImages (available at https://storage.googleapis.com/openimages/web/index.html), which contain extensive variety in both images and captions and a wide array of object categories, may require larger data samples for CSA to perform effectively. In such cases, the scalability limitations of CSA's matrix decomposition approach become more evident, as the cubic complexity of these operations could lead to significant computational strain on larger datasets. More experimental validation on these varied datasets would clarify the scalability and generalizability of CSA across a broader range of applications. The paper needs to address the computational cost associated with the SVD, especially as the dimensionality of the input features increases, and provide a more thorough analysis of the method's scalability limits.

### Questions
The reviewer will consider increasing the score if the authors can address the weaknesses mentioned above, most likely empirically.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes CSA: Canonical Similarity Analysis method to train a multimodal encoder from two independent unimodal encoders with limited data. Unlike traditional methods that train both encoders on multimodal data, CSA only requires the unimodal encoders to generate embeddings, avoiding the need to train them on multimodal pairs.

The authors show that their CSA method matches or beats CLIP and the baseline ASIF on image classification on ImageNet and LeafySpurge datasets. However, the authors’ method falls short of CLIP’s performance on the cross-modal retrieval task. Their experiments also show that CSA outperforms the baselines when detecting mislabeled ImageNet images, and detecting misinformative captions.

The paper concludes that CSA is a robust method to replicate CLIP similarity scores using two pre-trained unimodal encoders and limited data.

### Strengths
- The paper is well motivated: Finding data-efficient ways to train multimodal models using existing pretrained unimodal encoders is an important research direction.
- The method used in the paper appears novel, with only one other related work (ASIF) that uses independent unimodal encoders to project embeddings onto a multimodal representational space.
- The proposed approach (CSA) beats or matches CLIP’s performance in image classification tasks using significantly lesser data.
- The paper’s experiments also show that CSA is more robust to mislabeled images in the image classification task. CSA is also slightly more capable in detecting misinformative captions compared to CLIP and other baselines. Finally, the authors show that CSA is more robust to noisy data compared to the previous baseline ASIF.
- Overall, this study could pave the way for more advancements in this space of adapting independent unimodal encoders to multimodal models.

### Weaknesses
 - In Figure 3, CSA was only trained on in-distribution image-caption pairs. This may lead to an unfair comparison to CLIP, as the CSA training has seen the ImageNet/Leafy Spurge distribution that its being tested on during the training process. CLIP’s rise to fame is due to its general zero-shot capabilities. The zero-shot capabilities of CSA are not fully evaluated in this paper.
    - A fairer comparison might be to fine-tune CLIP on ImageNet/Leafy Spurge. This could be done by training the last projection layer of CLIP, analogous to keeping the unimodal encoders frozen in CSA training.
    - Additionally, including out-of-distribution datasets would give a clearer view of CSAs true zero-shot capabilities: An example could be to train CSA on MS COCO and then evaluate the performance on ImageNet / Leafy Spurge.

- Similarly, in Figure 4, comparing CLIP to CSA may not be entirely fair. Although CLIP likely encountered ImageNet images in training, they represent a very small fraction of its large dataset. A fairer comparison could be to fine-tune CLIP (again, perhaps just the  projection layer) on ImageNet images, including those with mislabeled data, before proceeding with this analysis (See Question 2).

- The paper's conclusion suggests that CSA outperforms CLIP in cross-modal retrieval ("CSA shows competitive performance compared to CLIP models in image classification, mislabeled data detection, **cross-modality retrieval**, and misinformation detection tasks with
limited data."). However, this is misleading, as Table 2 shows that CSA underperforms CLIP in this task.

### Questions
1. In Figure 4, does the smaller subset of ImageNet (5k images) include all of the mislabeled images from ImageNet? A statistic showing the percentage of mislabeled images in the training set for Figures 4(a) and 4(b) would offer more insight into these results.
2. Why did the authors choose not to fine-tune CLIP on ImageNet? Was there some intuition behind this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a canonical similarity analysis (CSA) framework, a novel approach that projects two distinct unimodal feature spaces from pre-trained encoders into a unified multimodal feature space. The CSA has great data efficiency and discovers the inherent trade-offs of informative embeddings and distinguishing data. The extensive experiments show that the CSA achieves competitive performances against CLIP models across a range of tasks, including image classification, mislabeled data detection, cross-modality retrieval, and misinformation detection, even with a limited dataset.

### Strengths
1. This paper proposes the canonical similarity analysis (CSA) framework, which can replicate the CLIP multi-modal model. It just uses two unimodal encoders but demands much less computation cost and related data.
2. This paper provides the theoretical analysis on the trade-off of obtaining informative embeddings and distinguishing multimodal data, considering various hyperparameters of CSA.
3. The extensive experiments on various downstream tasks (such as image classification, cross-modal retrieval, and misinformative caption detection) show that CSA outperforms the traditional CLIP model, while requiring much fewer paired multimodal data and fewer unimodal data.

### Weaknesses
1. This paper proposes a post-tuning mapping framework on the unimodal features, which would compute the matrix optimization without training any encoders. Hence the performances heavily rely on the choices of visual and textual encoders. The experiments part only shows the one encoder situation (gtr + dino). More model encoders analysis for CSA are needed. Specifically, the paper should explore how the performance of CSA varies with different pre-trained encoders, including those with different architectures and training objectives. For instance, using a ResNet-based visual encoder or a BERT-based text encoder could reveal the robustness of CSA to different feature representations. Furthermore, it is crucial to analyze the impact of encoder quality on the final performance of CSA. Do better encoders always lead to better CSA performance, or is there a point of diminishing returns?
2. In the performance comparisons, the ASIF is the only fair baseline method, which lacks of persuasion. It is important to add more comparative experiments for more related methods, e.g., some prompt tuning and adapter tuning work (PEFT methods). What’s more, when compare CSA with CLIP (e.g., Flickr in Tab. 2, ImageNet in Fig. 3), the CSA is the fine-tuned model on the specific dataset, but the CLIP is the zero-shot model without fine-tuning. Such experimental comparison is unreasonable. The CSA should fine-tuning on the ImageNet and then test on the Flickr. It's also important to consider that fine-tuning CLIP on the same datasets as CSA might lead to performance gains for CLIP, making the comparison even more challenging. The paper should also include a comparison with other methods that perform similar post-hoc alignment of pre-trained features, to establish the novelty of the proposed approach.
3. The feature dimensions of $q$ and $r$ are the important hyper-parameters for CSA, and the Tab.1 also shows the different dimension choices on different datasets, hence the related ablation study is missing in this paper. Specifically, the paper should provide a detailed analysis of how the choice of $r$ affects the performance of CSA. Since $r$ represents the dimensionality of the intermediate feature space after CCA, it is important to understand how different values of $r$ impact the trade-off between information preservation and computational cost. Furthermore, the paper should investigate the sensitivity of CSA to the choice of $q$, the output dimension of unimodal encoders. While $q$ is stated to be fixed, it is still important to understand how the choice of this dimension, which is determined by the pre-trained encoders, impacts the final performance.

### Questions
1. The visualization experiments can show the interpretability of multi-modal learning, I wonder to know the visualization results of embedding spaces.
2. Although the CSA does not require GPUs to optimize the fitting matrix, I wonder to know the run-time cost of the optimization process on different datasets and feature dimensions. Is it faster than the training a traditional network?

### Soundness
3

### Presentation
2

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
A new similarity calculation strategy, CSA, based on Canonical Correlation Analysis, is proposed to replace the correlation matrix in CLIP for aligning images and text modalities. CSA allows better alignment of features encoded by unimodal encoders for the same samples without requiring as many training samples as CLIP. A theoretical explanation of CSA is provided. Experiments are conducted on a large number of datasets, all of which outperform the baseline model ASIF.

### Strengths
1. It only requires using a pre-trained unimodal encoder along with CSA, training on a small number of sample pairs (such as a single image and its corresponding caption) to achieve alignment between two modalities, greatly saving computational resources.
2. In image classification tasks, it achieves results comparable to CLIP using fewer resources.
3. Experimental results significantly outperform the baseline model ASIF.

### Weaknesses
1. The theoretical discussion of CSA lacks detailed explanation for Equation (9), and the connection to contrastive learning is not clearly established, indicating a lack of novelity in CSA. Specifically, the derivation of Equation (9) is not provided, making it difficult to assess the validity of the approach. The link between maximizing canonical correlations and the objectives of contrastive learning, such as pulling semantically similar embeddings closer and pushing dissimilar embeddings apart, is not explicitly shown. This absence of a clear connection makes it hard to understand why CSA would be an effective alignment strategy, and whether it is simply a re-implementation of existing contrastive learning principles.
2. In comparisons with CLIP for image classification tasks, only a limited amount of training data was used, with no comparisons made on larger-scale training datasets. This limits the generalizability of the results. The experiments do not explore the performance of CSA when trained with larger datasets, which is crucial to understand its scalability and potential. The paper does not provide a clear understanding of how CSA would perform when exposed to the same scale of data as CLIP, which is a critical aspect for practical applications.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel method called Canonical Similarity Analysis (CSA) to improve data efficiency when mapping unimodal features (e.g., from image or text) into multimodal feature spaces, effectively replicating models like CLIP but requiring significantly fewer data using pretrained unimodal models. The method leverages two pretrained unimodal encoders and applies Canonical Correlation Analysis (CCA) to align the features using a small portion of the training set. CSA does not involve training neural networks, only solving a matrix decomposition for feature mapping. The authors demonstrate its effectiveness outperforming a pretrained CLIP in some cases with far fewer multimodal data.

### Strengths
- The paper is well-organized, making it easy to follow the proposed approach and experimental setup. 
- A key strength of CSA is its remarkable data efficiency, achieving effective mapping and strong results with significantly less training data compared to the baselines. 
- Additionally, the method demonstrates robustness in handling noisy and limited multimodal data, which is essential in real-world applications where large correctly labeled datasets are often scarce. 
- Finally, the theoretical analysis offers valuable insights into the trade-offs between reducing noise and preserving meaningful similarity scores, further enhancing the paper's contribution.

### Weaknesses
 - One major issue is that CSA uses different backbones, such as DINOv2-Giant and a GTR-t5-large as unimodal encoders (lines 715-716), compared to the multimodal baseline using a CLIP ViT-bigG/14 pretrained on LAION-2B (line 712). This creates an unfair comparison and makes hard to objectively state the efficacy of the approach. Specifically, the use of different architectures and pretraining datasets for the unimodal encoders versus the CLIP baseline introduces confounding variables, making it difficult to isolate the impact of the CSA method itself. The performance gains observed could be attributed to the superior representation power of the DINOv2 and GTR models rather than the effectiveness of CSA.
- Additionally, the paper's performance on cross-modal retrieval tasks, particularly in text-to-image retrieval, is noticeably weaker than CLIP, which limits its impact in this commonly used task. The lower performance in text-to-image retrieval, a core task for multimodal models, suggests that CSA's learned representation space might not be as effective for aligning text and image features as directly trained models like CLIP. This is a significant limitation, as cross-modal retrieval is a key application for such models.
- Moreover, the greatest weakness is that CSA requires a small portion of training data (i.e. 35k pairs on ImageNet) to solve the matrix decomposition for the features mapping, but all the evaluations are compared to zero-shot CLIP (not fine-tuned on the same portion of training data), which leads to an unfair advantage. Evaluation (e.g Figure 3(a)/3(b) and Table 2(a)/2(b)) should include few-shots adaptation baselines (e.g CoOp [1], CLIP-Adapter [2], etc..) or at least the standard CLIP linear evaluation protocol [3] for a fair comparison with the multimodal baseline. Note that using CSA on 800 pairs of Leafy Spurge could be the main reason for its improved performance against zero-shot CLIP. This is because this data is so different from the training distribution that merely adapting to it leads to the observed improvements. The lack of a fair comparison with few-shot adapted CLIP models makes it difficult to assess the true data efficiency of CSA. The observed performance gains on the Leafy Spurge dataset could be primarily due to the adaptation to a new distribution rather than the inherent strength of the CSA method.

### Questions
- Q1. Have you considered evaluating CSA using the same backbone as CLIP (e.g. using the same image and text encoders but pre-trained on two different datasets from OpenCLIP)? This would empirically strengthen your hypothesis and demonstrate the effectiveness of your method.
- Q2. Just out of curiosity, how scalable is CSA when handling larger training datasets? How much could it benefit from optimizing the matrix decomposition on a large-scale multimodal dataset?
- Q3. Is it possible to possible to solve CSA on a different dataset from the downstream one? It would be interesting to see whether this improves performance in tasks like cross-modal retrieval, where CSA currently underperforms compared to CLIP.
- Q4. Could the authors better explain why the Leafy Spurge dataset was chosen as an evaluation benchmark, and how its characteristics make it particularly suitable for demonstrating CSA's capabilities?

I would be happy to improve my rating if the authors address my concerns, particularly regarding the fairness of the current comparison.

**Minor observations**:
- Error in Table I. In the supplementary material, it is stated that the CLIP model used is the ViT-bigG-14 trained on LAION-2B. However, in Table I, CLIP is attributed to 12B pairs of training data.
- Error in Table I. Moreover CLIP ViT-bigG-14 is 2.5B of params in total.

### Soundness
3

### Presentation
2

### Contribution
3
