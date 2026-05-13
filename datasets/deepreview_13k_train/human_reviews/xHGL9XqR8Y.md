# The Wisdom of a Crowd of Brains: A Universal Brain Encoder

- Decision: Reject
- Scores: 3, 8, 6, 8

## Abstract
\vspace*{-0.1cm}
Image-to-fMRI encoding is important for both neuroscience research and practical applications. 
However, such “Brain-Encoders” have  been typically trained per-subject and per fMRI-dataset,
thus restricted to very {limited}  training data.
In this paper we propose a \emph{\underline{Universal} Brain-Encoder}, which can be trained jointly on data from many different subjects/datasets/machines.

What makes this possible is our new \emph{voxel-centric} Encoder architecture, which learns a unique “voxel-embedding” per brain-voxel. 
Our Encoder trains to predict the response of each brain-voxel on every image, by directly computing the \emph{cross-attention} between the brain-voxel embedding and multi-level deep image features. This voxel-centric architecture  allows the \emph{functional role} of each brain-voxel to naturally emerge from the voxel-image cross-attention.
 We show the power of this approach to (i)~combine data from multiple different subjects (a “Crowd of Brains”) to improve each individual brain-encoding, (ii)~quick \& effective Transfer-Learning across subjects, datasets, and machines (e.g., 3-Tesla, 7-Tesla), with few training examples,
 and (iii)~use the learned voxel-embeddings as a powerful tool to explore brain functionality (e.g., what is encoded where in the brain).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a Universal fMRI Encoder for the prediction of brain responses to image stimuli. Unlike traditional subject-specific brain encoding models, the proposed work is trained and validated across multiple subjects and datasets. The model learns voxel embedding through cross-attention with multi-level deep image features, allowing the model to capture functional roles of different brain regions while sharing other network weights across subjects. The model is evaluated on 3 datasets on two measurements: a comparison of the estimated fMRI signal vs. ground truth and the image retrieval accuracy using top-k accuracy.

### Strengths
1. The proposed Universal Brain-Encoder can effectively handling sequences from different subjects, datasets, and machines, which enhances its applicability for both neuroscience research and practical applications

2. The paper presents comprehensive experimental results, and the proposed Universal Brain-Encoder achieves satisfied performance across multiple datasets. Notably, it achieves substantial performance improvements when trained on multi-dataset inputs, supporting the authors' argument regarding the "Crowd of Brains" concept

### Weaknesses
1. The idea appears to closely resemble existing works such as [1], MindFormer [2], MindEye2 [3], MindBridge [4], and BDI [5]. These studies also learn a set of independent parameters for each subject while sharing most parameters across subjects. The novelty of the proposed idea needs further clarification.

2. Some brain decoding methods employ symmetric architectures, so they have both Image-to-fMRI and fMRI-to-Image networks, such as [6] and [7]. A discussion about these approaches should be included in the comparative experiments.

3. The quality of the generated fMRI data requires more validation. The authors should use additional metrics or evaluation methods to assess whether the generated data can still be used to analyze brain activity. For instance, the authors can use existing brain decoding models to prove they can reconstruct images from the generated fMRI sequences.

4. An ablation study on different Voxel Embedding dimensions should be included.

5. Is it better to utilize all voxels in fMRI sequences? The proposed voxel-based approach has the potential to capture latent semantic relationships between brain activities and input signals, whereas manually selected ROIs may lead to information loss. If the method can effectively model all voxels and provide visualize results as demonstrated in Fig. 7, it would yield interesting results.

### Questions
What is the spatial resolution of the pre-processed fMRI datasets and the corresponding dimensionality of the 4D volumetric data? It is curious whether the spatial resolution can support the fine-grained analysis of brain response as shown in Fig. S13.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work trains a universal brain encoder that can predict the brain responses from multiple participants and datasets. The input to the encoder is a stimulus image and a learned 256-dimensional voxel-wise embedding. The voxel-wise embeddings are randomly initialized, and contain no information about the participant or the spatial location of the voxel. All other parameters in the encoder are shared between voxels, participants, and datasets.

- The predictions are evaluated with per-voxel pearson correlation and a per-image retrieval metric.
- Their universal encoder significantly outperforms baseline single-subject encoders (figure 4)
- Inclusion of a higher quality 7T data improves performance on older 3T and 4T datasets (figure 5)
- A pre-trained encoder can transfer to new subjects and datasets just by learning new voxel embeddings. Performance is much higher and learning is faster than a single-subject encoder.
- K-means clustering is applied to the voxel embeddings to identify regions for food, words, faces, sports, indoor scenes, outdoor scenes.

### Strengths
- This is a very strong and well written paper. The methods are easy to understand and well motivated. I could see this encoder being used a lot when working with smaller vision datasets. 
- Retrieval accuracy is impressively high. It looks close to 95% top-1 accuracy for subjects 1 and 2 across 1000 test images (chance is 0.1%).
- Statistical tests are performed for all experiments.

### Weaknesses
I think the paper is lacking some exploration and visualization of the voxel embeddings. Here are some ideas:
- Apply the clustering to more than 2 participants. 
- Other clustering methods besides k-means (i.e. some that can deal with outliers)
- A flatmap visualization with outlines of previously identified category selective regions for faces, bodies, places, and words. This would be helpful for comparing to the clusters identified with k-means.
- A UMAP or tsne applied to the combined embeddings for the 8 participants, and then visualized on the cortical surface with a color mapping.

### Questions
In other papers that use NSD, subject 5 is typically the best performing subject. However in this work the retrieval accuracy is quite a bit lower than subjects 1 and 2. Any ideas why this might be the case?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposed a Universal Brain Encoder that can train on multiple subjects from different datasets. The methods applied cross-attention between features of the image and fMRI voxel. Experiments on three datasets have shown that performance can be improved after fine-tuning with new subjects.

### Strengths
1. The problem of the universal brain-image generation is important.

2. Experiments successfully demonstrated the proposed method can train on multiple subjects from different datasets and achieved a better performance.

3. The presentation of motivations, methods, and experiments is clear and easy to follow.

### Weaknesses
1. The announcement of the *first-ever Universal Brain-Encoder* is too aggressive. The idea of the model is to be able to train on multiple subjects and datasets instead of **universally** applying to any unseen subjects or datasets. The performance of the proposed model on a new subject is tested via few-shot transfer learning instead of zero-shot learning. 

2. The method of cross-attention is not novel and exists in the field of brain-image generation [1,2,3]. The specific implementation and novelty of the cross-attention mechanism at the voxel level are not clearly articulated. It is unclear how this voxel-level cross-attention differs fundamentally from existing methods that also use cross-attention between image features and fMRI data.

3. Lack of ablation studies. For example, in Figure 7, functional embedding is not evaluated to show the functional roles of voxels but the k-means results of voxel embeddings were used. Also, other components, which were claimed essential in the main text, are not evaluated. Specifically, the contributions of the positional and functional embeddings within the cross-attention mechanism are not isolated and quantified. It is not clear how much each component contributes to the overall performance gain.

4. The potential power of finding subject-specific brain parcellation is interesting, but the demonstration in Figure 7 shows this can only proceed on visual networks instead of the whole brain. Brain parcellation is for the whole brain.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a multi-subject fMRI encoding model. The authors set learnable voxel-wise embedding for each subject and optimize the subject-specific voxel-wise embedding and the subject-shared encoding model through the fMRI prediction task. Through the evaluation on multiple fMRI datasets, the authors validate the effectiveness of the proposed method and further validate that few-shot cross-subject transfer can be achieved. Finally, this paper utilizes learned voxel-wise embedding to initially explore concept-selective in the brain cortex, showing its value in neuroscience applications.

### Strengths
+ This paper focuses on the intersting but few-studied issue of multi-subject fMRI encoding.
+ The motivation for this paper is clear and the proposed method has yielded promising results.
+ The proposed method achieves cross-device and cross-subject few-shot transfer learning, making it highly applicable.
+ Neuroscience exploration using the voxel-wise embedding proposed in the paper is promising.
+ The paper gives detailed implementation details of the model model which helps in understanding and also ensures reproducibility.

### Weaknesses
#### 1. More related works should be discussed:
The authors should discuss additional related works or acknowledge that these related works have inspired them, including but not limited to:
+ At the level of model design, the proposed method seems to be a revised version of [1], which employs ROI-wise embedding rather than voxel-wise embedding. 
+ At the level of research ideas, some works also train encoding models and then use them for neuroscience explorations, such as [2][3].
+ at the level of fMRI representation learning, [4][5] already show the use of multi-subject data can enhance each subject's representation, and [4][6][7] already show the use of other subject's fMRI can achieve few-shot transfer learning.

#### 2. Limited evaluation metrics:

In this paper, only voxel-wise Pearson coefficients and retrieval results are used as evaluation metrics, and the inclusion of more metrics such as $R^2$, MSE, etc. can further indicate the fMRI encoding accuracy.


#### 3. On fMRI replicable

The method proposed by the authors fails to address the issue of fMRI replicability, which is a common problem with regression-based fMRI encoding models. The authors already discuss this in their limitation and assume that the fMRI captured by subjects viewing the same image multiple times is the same. However, this assumption may greatly limit the training of fMRI encoding models.

### Questions
+ In Figure 2, the dimension of Voxel Embedding is "1xE", why 1 and not the number of voxels? If it's 1, does it mean that we need to train a model for each voxel? If it is the number of voxels, then the number of voxel embeddings should be much larger than the image tokens (i.e. P), and at this point does the attention module make the randomly initialized voxel embeddings overly self-concerned?
+ In Figure 6(a), why is the performance of coding saturated when the few-shot samples exceed 3000?

I'm willing to further raise my rating according to the author's rebuttal.

### Soundness
3

### Presentation
4

### Contribution
3
