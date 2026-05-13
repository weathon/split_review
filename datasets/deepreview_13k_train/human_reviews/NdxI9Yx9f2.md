# Seeing the Whole in the Parts in Self-Supervised Representation Learning

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Recent successes in self-supervised learning (SSL) model spatial co-occurrences of visual features either by masking portions of an image or by aggressively cropping it. Here, we propose a new way to model spatial co-occurrences by aligning local representations (before pooling) with a global image representation. We present CO-SSL, a family of instance discrimination methods and show that it outperforms previous methods on several datasets, including ImageNet-1K where it achieves 71.5% of Top-1 accuracy with 100 pre-training epochs. CO-SSL is also more robust to noise corruption, internal corruption, small adversarial attacks, and large training crop sizes. Our analysis further indicates that CO-SSL learns highly redundant local representations, which offers an explanation for its robustness. Overall, our work suggests that aligning local and global representations may be a powerful principle of unsupervised category learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents CO-SSL, an SSL method that learns similar representations for frequently co-occurring visual features, enhancing robustness and outperforming previous models (71.5% Top-1 accuracy on ImageNet-1K). It introduces RF-ResNet to control the receptive field size and analyze local representation impact. Results indicate CO-SSL’s high redundancy in local features contributes to robustness, suggesting co-occurrence learning as a powerful unsupervised category learning principle.

### Strengths
1. the idea of co-occurrence is important in SSL
2. the title is clear and intuitive

### Weaknesses
1. The spatial co-occurrence has been identified as useful before. E.g. in SimCLR cropping has shown it importance. [1] further proposes SSL training on patches. The proposed method should compare with such methods and include a better analysis of why the proposed multiple head is better, in addition to short empirical study in Fig3.
2. The experimental improvement in Table 1 is also limited, which is a) related to point 1; b) potentially indicates that the original design (e.g. BYOL, simclr) implicitly considers spatial occurrence with patch/cropping. The design may not be very necessary, or it is even a duplicate.
3. Please include ablation study on number of heads (e.g. Fig.1 only have 2), conv layers to have different projection and number of projection embeddings. See [2] for an example showing different performance at conv3 conv4

minors:
1. Please include caption below figure and not use see text for details and omit captions.

### Questions
see Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper leverages the spatial co-occurrences of SSL by focusing on local representations. It proposes a new method to learn the correspondence between local features to global features within an image, based on a modified ResNet that bounds local receptive field. The paper demonstrates the performance of the proposed CO-SSL, and its robustness against corruptions.

### Strengths
1. The analytical experiments (robustness, similarities, saliencies) are insightful. From visualizations in Figure 4, CO-SSL works well.

2. The work has promising extensions, and probably can shed light on modifying ViTs to enhance local focus and processing.

3. This paper is trying to make solid contributions as it not only proposes new objectives but also a new architecture, thanks for the hard work.

### Weaknesses
1. Referring to Table 2, why applying CO-SSL to DINO does not improve the baseline method as effectively as that for BYOL? This also makes me curious about the effectiveness of CO-SSL on other similar work with two models, e.g., Barlow Twins. I expect CO-SSL to generalize to other SSL methods as well, or the contribution is narrowed. Specifically, the discrepancy in performance gains between DINO and BYOL raises concerns about the method's robustness across different self-supervised learning frameworks. The lack of consistent improvement suggests potential limitations in the approach's adaptability or that the method is highly sensitive to the specific architecture and training regime of the base SSL method.

2. Following (1), while the authors claim that "in principle, the approach is adaptable to most SSL methods,", we don't know the effectiveness and performance. In later experiments, the authors mainly focuses on improving BYOL. Can the authors provides results with DINO+CO-DINO, and more? While I in general appreciate the proposed objectives and modified architectures, given the insufficient experiment settings, I am skeptical whether the proposed methods is limited to BYOL and cannot generalize to other SSL methods. The absence of a thorough evaluation across diverse SSL methods, beyond BYOL, makes it difficult to assess the true scope and impact of the proposed approach. The claim of general adaptability needs more empirical backing to be fully convincing. It is crucial to demonstrate that the method is not merely a specialized tweak for BYOL.

3. It would be great if the authors can analyze and explain the co-occurrences more, specifically, is it brought by convolutions? Will the observations and solutions here hold for transformers? The paper would benefit from a deeper analysis of the underlying mechanisms that drive the observed co-occurrences. It's not clear if the method's effectiveness is intrinsically linked to convolutional architectures or if it can be extended to other architectures like transformers. A more detailed investigation into the nature of these co-occurrences and their relation to architectural choices is needed.

### Questions
While I acknowledge the hard work and the promising future extensions of this works, there are several concerns that need to be addressed, majorly regarding its generalizability to many SSL methods. This paper has a narrowed demonstration of applying CO-SSL to only one or two methods, which cannot convince the audience about its capability effectively. Please see the weakness section for more details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel contrastive learning approach for encouraging spatial cooccurrences by promoting the similarity between local features and global features. To study the impact of local representations, this work introduces RF-ResNet to limit the receptive field of local representations. The proposed framework, CO-SSL, demonstrates superior performance in classification, transfer learning, and robustness. The analysis indicates that RF size is inverse  to the minimum crop ratio.

### Strengths
1. This work proposes a novel contrastive learning approach, termed CO-SSL, to encourage spatial cooccurrences. The proposed method demonstrates efficiency in pretraining on ImageNet.
2. It is proved that CO-SSL learns stronger local similarities,  regardless of the neural architecture.

### Weaknesses
The original contribution comparing to BYOL with multi-crops is limited:
The loss function between local and global embeddings can be treated as BYOL introducing local crops. 

Conclusion on RF and Crop Size Relationship:
The conclusion drawn about the relationship between receptive field size and crop size is currently not well-supported. Figure 3(a) shows a general trend but does not clearly demonstrate an inverse correlation. The authors need to strengthen their argument by providing a more rigorous analysis or additional data points that highlight this relationship. Moreover, basing the conclusion solely on ImageNet-100 is limiting, as different datasets may have varying object characteristics that affect the optimal crop size. The authors should consider using additional datasets to validate their findings and discuss how the crop size might be influenced by the specific objects and their arrangements within the dataset images.

The experiments are not clearly explained :
1. what the numbers in Figure 2 present is not clear.
2. the calculation of the RF size is missing.

### Questions
**Clarity of RF-ResNet Explanation and Figure 2:**
The paper introduces the RF-ResNet architecture, which is designed to limit the receptive field (RF) of local representations. However, the explanation regarding how the RF fields are calculated and what the numbers in Figure 2 represent is indeed unclear. The authors should provide a more detailed explanation of the RF calculation, possibly with a formula or a clear description of the process. Additionally, Figure 2 should be annotated to explain the significance of the numbers, such as the receptive field sizes and how they correspond to the architectural modifications. This will help readers understand the relationship between the architecture and the receptive field size.

**Difference Between RF99-ResNet50 for img224 and ResNet50 for img99:**
The paper compares the performance of RF99-ResNet50 with that of a standard ResNet50. It would be beneficial for the authors to clearly articulate the differences between these two models, especially in the context of input image sizes. Specifically, the RF99-ResNet50 is designed to have a receptive field of 99x99 pixels, while the ResNet50 is not constrained in this way. The authors should explain how these differences impact the models' ability to capture local and global features. The proposed model processes multiple local representations in parallel, similar to dealing with multiple local crops. The authors should provide a direct comparison of the performance of their model with BYOL that uses multi-crops. This comparison should include not only accuracy metrics but also an analysis of sample efficiency and computational costs. If the proposed method offers improvements over BYOL with multi-crops, this should be clearly highlighted and justified with data.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the task of self-supervised learning and proposes a family of instance discrimination methods that make global and local representations similar, called COSSL. It shows improved performance over existing SSL methods across various settings of ImageNet.

### Strengths
- the paper is easy to follow
- the proposed method is simple yet effective, and it shows superior results across settings
- the authors show the proposed method can be integrated into other strong SSL methods (e.g. BYOL and DINO) and leads to further performance improvement. If this holds true across different architectures and SSL methods, it could potentially be an important technique in the SSL toolkit.
- the performance improvement on the robust benchmark is interesting and important.

### Weaknesses
 - The presentation of the paper should be improved: 
1. consider explicitly listing the contributions of the paper at the beginning.
2. improve the quality of the figures and the corresponding captions. The captions for Figures 1 and 2 do not help in understanding the method at all.
3. which part of Section 3.1 is specific to BYOL, and which parts are general and can be used in other methods? 
4. avoid using the same notation to denote different things, for example, $z^{'i}_{\xi}$ is a different thing from the one without I.
5. avoid abusing terminologies. For example, the authors evaluate the robustness of the methods in Table 3. But Line 312 says Table 2 is also an evaluation of robustness. This would be understandable if there were no Table 3 and evaluation against adversarial examples. But in the current context, it leads to confusion.

- The method, at first glance, seems to be more general than what is in the paper. However, the current method has many specific designs. For example, the method is only evaluated on ResNet. I think it is quite natural to wonder how the proposed method behaves on more recent architectures such as transformers, MLP-mixers, etc. Should the loss look different on different architectures or it is optimal to minimize the negative cosine similarity? How should one define "global feature" and "local feature"  in other settings? For example, if one wants to deploy the method in transformers, should one use the CLS token as the global feature or the pooling of all patch features?

- What is the motivation behind the RF-ResNet? The paper says it is used for analysis purposes (line 211). But it is also mentioned as one of the contributions on line 64. What is the advantage of RF-ResNet compared to standard ResNet? From what I understood, RF-ResNets are less robust than the standard ResNet and do not bring significant performance improvement. Table 1 is the only place the authors show that RF-ResNet50 is slightly better than ResNet50. However, RF-ResNet 50 also has slightly more parameters than ResNet50 (23.7M vs 23.5M on line 238). So I'm not sure if it is a valid contribution besides the analysis purposes. 

- How is the generalization of the learned representations from the proposed method to other downstream tasks beyond ImageNet classification? While linear probing on ImageNet is quite common for assessing the quality of representation learning methods, a good linear probing performance does not always translate to other tasks such as scene understanding. When an image describes a complicated scene, I'm not sure if it is really beneficial to force all local features to be close to the global feature because there could be more than one object/topic. Perhaps it makes more sense to have more than one global feature or set the number of global features as a hyper-parameter. For example, when using 4 global features, the final feature map can be divided into 4 regions and each region computes its own loss as in equation 2.

### Questions
- Does it make sense to also use the loss from Equation 2 at intermediate layers? I saw in A.3 that the authors did some initial experiments by selecting local features from intermediate layers. I wonder what if the global features are also from the same layer (otherwise, it does not make sense to use it as the "anchor point" for features from different layers).

- CO-DINO is also evaluated in many places in the paper. However, the author did not provide any implementation details in terms of how to combine CO-SSL with DINO.

- Is it necessary to use different projectors and predictors for computing the loss in equation 2? What does the performance look like if the local features are also from the same projectors and predictors as the global features?

- Why 99 and 29 are chosen as the RF for ResNet 50 and ResNet 18 in the experiments? Does the same conclusion hold for other RF sizes? 

- What is the depth of the additional MLP added after the pooling layer? What is the effect of the depth of this MLP to the final performance?

### Soundness
3

### Presentation
1

### Contribution
2
