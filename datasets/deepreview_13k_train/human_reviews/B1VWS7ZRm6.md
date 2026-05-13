# On Transferring Expert Knowledge from Tabular Data to Images

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Transferring knowledge across modalities has gained considerable attention in machine learning. Expert knowledge in fields like medicine is often represented in tabular form, and transferring this information can enhance the comprehensiveness and accuracy of image-based learning. Unlike general knowledge reuse scenarios, tabular data is divided into numerical and categorical variables, with each column having a unique semantic meaning. In addition, not all columns can be accurately represented in images, making it challenging to determine "how to reuse" and "which subset to reuse". To address this, we propose a novel method called CHannel tAbulaR alignment with optiMal tranSport (CHARMS) that automatically and effectively transfers relevant tabular knowledge. Specifically, by maximizing the mutual information between a group of channels and tabular features, our method modifies the visual embedding and captures the semantics of tabular knowledge. The alignment between channels and attributes helps select the subset of tabular data which contains knowledge to images. Experimental results demonstrate that CHARMS effectively reuses tabular knowledge to improve the performance and interpretability of visual classifiers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the task of transferring expert knowledge from tabular data to images, and achieve good performances on image tasks.

### Strengths
- This paper addresses an important problem of transferring structured expert knowledge to images, which has practical applications.

- This paper proposes a novel method CHARMS that automatically transfers relevant tabular attributes to images via optimal transport and auxiliary tasks.

- This paper achieves good performance improvements over baselines on multiple datasets.

- This paper provides intuitive visualizations and mutual information analyses to explain knowledge transfer.

### Weaknesses
 - Limited exploration of extremely large tabular datasets with hundreds of attributes.

- It is widely witnessed that there are many uninformative features in the tabular data, I am not sure if the model can consistently perform well in such cases. The authors can test on tables that are manually added some Gaussian noisy columns/ features (e.g., 10 columns, 20 columns) and observing the performance changes.

- Can this model work on complex vision tasks like segmentation/detection that may require localization?

- It appears that hyperparameter tuning is performed only on your models, while the compared models are not tuned. This raises concerns about fairness. Besides, did the compared approaches use ImageNet-1k pre-trained weights like your model?

- I recommend testing the approach with new backbones. Older backbones like ResNet-50 differ significantly from current backbones like CLIP's image encoder. Since the CLIP image encoder is trained to align with text supervision, it can extract "semantic-level" features from images. In contrast, ResNet-50 primarily learns "pattern-level" features. This raises questions about the potential benefits of the proposed approach on CLIP backbones.

- Some related work about tabular learning are missing, e.g., T2G-Former, TabPFN, TabNet, TANGOS, TapCaps.

### Questions
See Weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is set in the context of training a model using multi-modal data where one modality is available only as training data and another modality is available both during training and inference. The authors tackle the problem of transferring knowledge from the training-only modality (i.e. tabular data in this paper) to the training and inference modality (i.e. image data in this paper). As motivation for this problem, the authors list scenarios where the cost of acquiring tabular data is exceptionally high so it might not be available during inference (e.g. information provided by medical domain experts). The paper presents a novel method that independently treats tabular and image features, specifically attributes (i.e. columns) of tabular data examples and "image channels" that correspond to high-level image features. The method aims to align the two sets of features and leverage this alignment to select the most important ones. An added benefit of this approach is the ability to interpret the connection that the method establishes between specific tabular and image features. The authors empirically evaluate their approach and compare it against various multi-modal learning baselines. Results over 6 different datasets demonstrate that their method performs very well compared to the baselines.

### Strengths
**S1**: The idea to independently treat image and tabular features of individual data examples is interesting. The proposed method looks interesting and useful. The added benefit of interpretability is also a nice byproduct of the core idea.

**S2**: Experimental results indicate that the proposed method is a pretty good fit for the tabular data modality compared to other cross-modal knowledge transfer baselines.

**S3**: Even though the presentation is sub-par (see weaknesses), I appreciate that the authors made a decent effort to

### Weaknesses
 **W1**: The presentation of the paper is its weakest quality. It contains many awkwardly sounding statements and poorly specified claims. Some specific examples below:
* **W1.1**: (Abstract) "transferring this information can enhance the *comprehensiveness* and accuracy of image-based learning" -- What is comprehensiveness of image-based learning? The term is vague and lacks a clear definition in the context of image-based learning. It's unclear what aspect of image understanding or performance is being referred to by 'comprehensiveness'.
* **W1.2**: (Abstract) "how to reuse" and "which to reuse" -- these phrases are entirely confusing out-of-context... Reuse what? The abstract lacks the necessary context to understand what is being reused, making these phrases ambiguous and uninformative. It's unclear what specific elements or information are being considered for reuse.
* **W1.3**: (Section 1) The first sentence lists different forms of data (which is general knowledge) but then for every form of data it provides citations. Firstly, I don't think we need a citation to say that image or text data exists. Second, why is Karpathy & Fei-Fei, 2015 the source that tells us that text data exists? I would remove the citations here. The citations are unnecessary and do not add value to the introduction. Citing general knowledge is inappropriate and the specific citation for text data is particularly odd.
* **W1.4**: (Section 1) "transformer ... methods to construct a feature space would result in a loss of interpretability" -- it is not clear at this point why interpretability an important goal. The paper does not establish why interpretability is a crucial factor in this context. The motivation for prioritizing interpretability over other potential benefits of transformer-based methods is missing.
* **W1.5**: (Section 1) "Therefore it is crucial to identify the information that *can be transferred* to instruct the learning of images." -- In principle, any information can be transferred. The difference is that not all information transfer is useful or cost-effective. The statement implies a constraint on what *can* be transferred, which is misleading. The real challenge is identifying what information transfer is *beneficial* rather than what is technically possible.
* **W1.6**: (Section 1) "We emphasize the importance of knowledge transfer from tabular data to image data" is listed as a contribution. I'm not sure if motivating a problem can be counted as a contribution (unless the motivation is somehow non-trivially creative). Simply stating the importance of a problem is not a contribution in itself. The contribution should be the proposed solution or a novel perspective, not just the problem statement.
* **W1.7**: (Section 2) "In recent years, the learning of tabular data has become an important research direction in the field of machine learning and data science." -- This statement feels wrong and is immediately contradicted (1986 was not recent). The claim about recent importance is inaccurate, given the long history of tabular data research. The reference to 1986 highlights the contradiction in the statement.
* **W1.8**: (Section 3.2, last paragraph) The shortcomings of existing methods are stated in a very vague way. What is the "specific information" that is not captured by the output-based approach? What does it mean when you say that "the MFH method ... cannot fully compensate for the limitations of the transfer mode"? How does the embedding-based approach "lose some attribute information in the tabular data" and why is that crucial? Also, instead of "from tabular to images" it should be "from tables to images". The criticisms of existing methods lack specific details. The terms 'specific information', 'limitations of the transfer mode', and 'lose some attribute information' are not well-defined, making it difficult to understand the shortcomings of the compared methods. The language should be more precise, and the phrasing should be 'from tables to images'.
* **W1.9**: (Section 4.2) The issue of "duplicated semantics across different channels" is not self-explanatory to me. The concept of duplicated semantics across different channels is unclear and requires further explanation. It's not obvious what kind of duplication is being referred to or why it's a problem.
* **W1.10**: (Section 4.2) "channel-wised" and "attribute-wise" should be "channel-wise" and "attribute-wise". Also the entire sentence "Then the cost matrix is constructed from the channel-wise similarity between attribute-wise similarity and calculates the OT transfer matrix" is completely confusing to me. The sentence is grammatically incorrect and the logic is unclear. The relationship between channel-wise similarity, attribute-wise similarity, and the cost matrix is not well-defined, making the explanation difficult to follow. The terms should be corrected to 'channel-wise' and 'attribute-wise'.
* **W1.11**: (Section 4.3) You say that the image network can have an "understanding" of the attributes. I would avoid such human-sounding jargon when talking about an artificial neural network. Using anthropomorphic language like 'understanding' is inappropriate for describing the behavior of a neural network. It's more accurate to describe the network's behavior in terms of learned representations and mappings.
* **W1.12**: (Section 5.1) "Each attribute of the table feature represents a scene" -- what does this mean? The statement is unclear and lacks context. It's not obvious how a table attribute can represent a scene, and this requires further explanation.
* **W1.13**: (Section 5.1) "each image is well marked with features, including 40 attribute markers" -- what does this mean? The meaning of 'attribute markers' is not clear. It's not obvious how images are marked with these markers or what they represent.
* **W1.14**: (Section 5.1) "Avito is challenging you to predict demand" -- I would avoid referring to the reader as "you". The use of 'you' is informal and should be avoided in academic writing. It's more appropriate to use a passive voice or refer to the reader in a more general way.

**W2**: Even though I appreciate injecting an empirical argument against using mutual information methods (i.e. section 4.1) before going forward with the presentation of the proposed method, the section itself (i.e. section 4.1) was entirely confusing to me. First, I wasn't sure if the authors intended to refer to Figure 8 (placed in the appendix) or Figure 2 (placed right inside section 4.1. Second, the flow of the explanation was quite difficult to follow and I cannot say I understood it. I understand the conclusion that the authors want to draw (i.e. mutual information is not great), but I could understand the reasoning. Finally, I didn't understand the elements of the figure itself which made it impossible for me to see what the intended conclusion is. The section on mutual information is poorly explained. It's unclear which figure is being referenced, and the explanation of the experiment and results is difficult to follow. The reasoning behind the conclusion that mutual information is not a good approach is not clearly presented, and the elements of the figure are not well-defined, making it impossible to understand the intended message.

**W3**: There is some information that I wish was present in the experimental results section. Specifically, I would like to see a description of the experimental protocol explaining how the numbers in Table 1 were derived (I can make an educated guess but I would prefer to see it explicitly). Also, the LGB, RTDL, and Resnet methods are listed alongside knowledge transfer baselines and I'm not sure how to interpret them. I assume they refer to scores of models without cross-modality knowledge transfer, but I also assume LGB and RTDL are supposed to target tabular data while Resnet image data. Since the target scenario is to evaluate the model on image data only, I'm not sure how LGB and RTDL are useful here. Finally, some of these models seem to outperform knowledge transfer methods. Even though this doesn't necessarily kill the main thesis of the paper, I still feel like it should be discussed explicitly as opposed to merely ignoring it. That being said, in the introduction, the third contribution implies that "CHARMS effectively reuses tabular knowledge to improve the performance of visual classifiers" which seems to be a claim that is not really supported by the presented numbers. The experimental setup is not clearly described. The protocol for deriving the numbers in Table 1 is missing, and the inclusion of LGB and RTDL alongside knowledge transfer baselines is confusing. It's not clear why tabular-specific models are included when the target task is image-based. The fact that some baselines outperform the proposed method is not adequately addressed, and the claim that CHARMS effectively reuses tabular knowledge is not fully supported by the results.

### Questions
**Q1**: What is the reasoning behind using the term "channel" to refer to high-level image features? I find it confusing since the word channel in images typically refers to e.g. the color channels. Especially since in the paper, you use the term in both the high-level feature sense and the color channel sense.

**Q2**: In section 5.2, you measure the mutual information during training. What are the quantities between which you are measuring the mutual information? This is not clear to me and makes the entire section (including the figure) quite hard to understand.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors introduce a novel method, CHARMS to transfer relevant tabular knowledge automatically and effectively by maximizing the mutual info between channels an tabular features. They propose three kinds of integration methods: output-based transfer, parameter-based transfer and embedding-based transfer. The authors make the claim that the existing methods yield low mutual information and the proposed method considers the specific characteristics for each modality and transfers knowledge to guide the image model. The authors evaluate the proposed model on 4 classification tasks and 2 regression tasks using 6 datasets. They evaluated the model using accuracy for classification and RMSE for regression.

### Strengths
The idea of the proposed method is interesting, novel and technically sound. These are the main strengths of this paper:

1. The paper is well written. The authors provide sufficient information to support their claims.
2. The method automatically transfers relevant tabular knowledge to images. 
3. The method also filters relevant info by aligning the attributed with channels. This strengths the correlated channels during transfer.  
4. In terms of quality, the proposed method outperforms other methods for classification and regression tasks.

### Weaknesses
There are some areas the authors can improve on:

1. Phi has been first used in page 4, equation 3 but hasn’t been explained until page 6. The mathematical definition below equation 1 to introduce phi is insufficient given the context of introducing the preliminaries. It is unclear what the exact function of \(\phi\) is at this stage, and it is not immediately obvious that it is an image feature extractor. A more detailed explanation of its role and how it relates to the image data is needed earlier in the paper.
2. In evaluation metrics, accuracy has been mentioned for measurement of performance for classification tasks. Accuracy isn’t always the most informative on the model performance. Consider other matrices for checking the model performance, such as precision, recall, F1-score, and AUC, to provide a more comprehensive view of the model's behavior, especially on imbalanced datasets. The paper should also discuss the potential limitations of using accuracy alone.
3. Limitations have not been discussed in the paper. The authors should address the limitations of their approach, such as scenarios where the tabular data might not be strongly correlated with the image data, or when the tabular data is of low quality. A discussion of the computational cost of the method would also be beneficial.
4. It would strengthen the paper to see some human evaluation to show the model is useful for an expert using the system. The paper lacks any discussion of how the model's predictions or outputs would be interpreted or used by a domain expert. This is important to assess the practical utility of the method.
5. A clear explanation on the different types of tasks and their usage for both the types of tasks would help understand the impact of the proposed model better. The paper should provide more detail on how the proposed method is adapted for both classification and regression tasks. The specific loss functions and optimization strategies used for each task should be clearly explained.

### Questions
1. What is “attention image” referred to above equation 6?
2. According to Table 1, the proposed model underperforms the LGB and RTDL on the DVM task by a large margin. Why is this so? A one-line explanation in the paper would help the reader understand the proposed method better.
3. Is the code for this method openly available for checking the reproducibility of this study?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to learn a classification task with the help of tabular data only for training. The idea of the paper is to identify the correspondences between the image features and the attributes in the tabular data and train the model to predict the tabular data based on the correspondences in addition to the task. The experiments show some performance boosts.

### Strengths
(1) It is interesting to see the performance boost with this method.

### Weaknesses
(1) The paper has a lot of mathematical notations that are not defined or ambiguous. For example, according to Section 4.2, $\mathbf{x}^T_{num}$ contains numerical data in the table, which is transformed to $\psi(\mathbf{x}^T) \in \mathbb{R}^{D \times E}$ together with the categorical data. I think it’s not straightforward to transform numerical values into an embedding. A more specific definition is necessary. Also, I think $S_{I_j}$, which I guess is the $j$-th channel of $S_I$ and is not explicitly mentioned in the paper, should be a matrix but implicitly used as a vector in Eq. (5). The second part of Eq. (5) if $<\mathbf{C}, \mathbf{T}>_F$ stands for the Frobenius norm, which is not explained in the paper, the summations over $i$ and $j$ should not be necessary. At least, min in this equation should be argmin. 

(2) According to Eq. (6), what this method actually does is multi-task training, where in addition to the target classification task, it also leans to classify/regress the attributes in the table (I guess $\phi(\mathbf{x}^T)$ in the second term of $\mathcal{L}_{i2t}$ is a typo of $\phi(\mathbf{x}^I)$ as well as $\mathcal{A}_p$ and $\mathcal{A}_q$ are $A$ corresponding to the numerical and categorical values in the table, respectively). If this is the case, this approach is suboptimal as the computation of $A$ is outside of the optimization for the target task and the attribute prediction tasks. In this sense, a comparison with the case where, instead of the tabular alignment in the method, a fully connected layer or an MLP dedicated to each attribute prediction task is necessary.

(3) If my assumption about $\phi(\mathbf{x}^T)$ in Eq. (6) is correct, I think the second term of $\mathcal{L}$ in Eq. (6) does nothing to the performance.

### Questions
I would like to have responses on (2) and (3) in the weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
