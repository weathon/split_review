# Probabilistic Language-Image Pre-Training

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 6, 6, 6, 6

## Abstract
Vision-language models (VLMs) embed aligned image-text pairs into a joint space but often rely on deterministic embeddings, assuming a one-to-one correspondence between images and texts. This oversimplifies real-world relationships, which are inherently many-to-many, with multiple captions describing a single image and vice versa. We introduce Probabilistic Language-Image Pre-training (ProLIP), the first probabilistic VLM pre-trained on a billion-scale image-text dataset using only probabilistic objectives, achieving a strong zero-shot capability (\eg, 74.6\% ImageNet zero-shot accuracy with ViT-B/16). ProLIP efficiently estimates uncertainty by an ``uncertainty token'' without extra parameters. We also introduce a novel inclusion loss that enforces distributional inclusion relationships between image-text pairs and between original and masked inputs. Experiments demonstrate that, by leveraging uncertainty estimates, ProLIP benefits downstream tasks and aligns with intuitive notions of uncertainty, \eg, shorter texts being more uncertain and more general inputs including specific ones. Utilizing text uncertainties, we further improve ImageNet accuracy from 74.6\% to 75.8\% (under a few-shot setting), supporting the practical advantages of our probabilistic approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel approach for vision-language models (VLMs) that leverages probabilistic embeddings to capture better the inherent many-to-many relationships between images and text descriptions. 

In general, the contribution includes
* Novel Probabilistic Embeddings: The paper introduces a fully probabilistic VLM that assigns each image-text pair a probability distribution rather than a deterministic embedding, addressing the inherent ambiguity in real-world image-text matching. This approach shows promise in capturing a richer semantic alignment by allowing multiple captions to represent an image and vice versa.
* Efficient Uncertainty Estimation: Unlike prior probabilistic VLMs, ProLIP efficiently estimates uncertainty by introducing an “uncertainty token” ([UNC]). This no-parameter simplification is computationally efficient and effectively captures the variance within embeddings, enhancing interpretability.
* Inclusion Loss: This paper introduces a novel inclusion loss, which enforces distributional inclusion relationships, and strengthens ProLIP’s interpretability by aligning learned uncertainties with human expectations (e.g., general captions should cover more specific ones).
* Performance on Zero-Shot Classification: ProLIP demonstrates strong results in zero-shot classification tasks, such as outperforming a CLIP baseline with similar architecture. The improvement in ImageNet classification accuracy (from 74.6% to 75.8%) with the use of uncertainty highlights the approach’s practical advantages.

### Strengths
1. Originality
* The paper introduces a novel Probabilistic Vision-Language Model (PrVLM), named ProLIP, which represents a shift from deterministic vision-language models to probabilistic embeddings. This approach innovatively captures the natural ambiguity in image-text relationships, where multiple captions may describe a single image, and a single caption may match multiple images.
* The concept of an uncertainty token ([UNC]) is a creative contribution, allowing the model to quantify uncertainty in a computationally efficient way, without additional parameters. This method differentiates ProLIP from previous probabilistic VLMs, which typically rely on additional modules to estimate uncertainty.
* The inclusion loss is another novel component of the paper. By enforcing a distributional inclusion relationship, the loss function allows the model to create more interpretable representations that respect hierarchical relationships within image-text pairs. This focus on hierarchical embedding structures is an innovative step for VLMs.

2. Quality
* The authors have conducted a thorough and robust set of experiments to validate ProLIP's effectiveness. These include zero-shot classification tasks across multiple datasets, evaluations of ProLIP’s uncertainty estimation, and comparisons with both deterministic (e.g., CLIP) and probabilistic baselines.
* The paper is methodologically sound and clearly specifies the assumptions, architectures, and loss functions. The experiments are carefully controlled, with baseline comparisons and ablation studies that effectively illustrate ProLIP’s strengths in various contexts.

3. Clarity
* The paper is written in a clear and accessible manner. Technical terms and novel concepts (e.g., inclusion loss, uncertainty token) are well-defined, with explanations that make the content readable.
* Figures, such as the visualizations, are well-crafted and effectively illustrate key points. 

4. Significance
* The introduction of probabilistic embeddings and inclusion loss contributes to the broader AI field’s understanding of how uncertainty modeling can enhance interpretability and generalization in multi-modal tasks. This may inspire further work in this direction.

### Weaknesses
1. Interpretability and Visualization: 
*  Although the inclusion loss aligns with human intuitions, the visualization methods could be improved. For example, it would be interesting to see more direct comparisons with non-probabilistic models in terms of how well ProLIP aligns visual and textual hierarchies in practice. Specifically, the paper lacks a clear demonstration of how the learned probabilistic embeddings capture the hierarchical relationships between images and text compared to deterministic embeddings. The visualizations provided are somewhat abstract and do not offer a concrete understanding of the practical advantages of the proposed approach in terms of hierarchical alignment. A more detailed analysis, perhaps using a dataset with explicitly defined hierarchical relationships, would be beneficial.

2. Limited Exploration of Task-Specific Uncertainties: 
*  The paper briefly touches on using uncertainty for image-to-text retrieval but could expand by exploring how uncertainty contributes to other downstream tasks. For instance, analyzing ProLIP’s impact on retrieval diversity or specificity could further highlight its advantages. The current evaluation primarily focuses on zero-shot classification, which might not fully capture the potential of the probabilistic embeddings. It would be valuable to see how the uncertainty estimates can be leveraged in tasks such as image captioning, where the model could generate multiple captions with varying degrees of specificity, or in visual question answering, where the model could express its confidence in its answers.

3. Human evaluation
*  While the experiments indicate that ProLIP’s learned uncertainties align with human intuitions, a concrete user study or human evaluation would reinforce these claims. The current evidence relies on indirect observations and comparisons, but a direct evaluation of how humans perceive the model's uncertainty estimates would provide stronger support for the approach. This could involve asking human subjects to rate the uncertainty of image-text pairs and comparing these ratings with the model's uncertainty scores.

### Questions
1. Could you clarify the design choice of the probabilistic pairwise contrastive loss (PPCL) over simpler alternatives, like KL divergence-based objectives? Have you tested how PPCL compares with other probabilistic loss functions in terms of training stability and final performance?

2. The inclusion loss is an interesting addition. Could you explain in more detail the intuition behind using this specific formulation, and how it compares with other metrics like Wasserstein distance?

3. The paper shows that ProLIP’s uncertainty estimates align well with general human expectations, such as more uncertainty for shorter text descriptions. Did you conduct any quantitative or qualitative user studies to validate this alignment? If not, how would you suggest evaluating the alignment between model uncertainty and human perception in future work?

4. You demonstrated ProLIP’s zero-shot classification ability, but could it also support a few-shot learning approach? What further modifications would be needed to explore few-shot learning capabilities and potentially improve its applicability in low-resource settings?

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
5

### Summary
This paper introduces ProLIP, a fully probabilistic approach to language-image pre-training. The authors begin by noting that CLIP's loss function oversimplifies the complex relationships between real-world images and texts. In response, ProLIP proposes a novel loss function that better captures the distributional relationships between these modalities. Extensive experiments were conducted to demonstrate the effectiveness of the proposed method.

### Strengths
- This paper is well-motivated, starting from the many-to-many matching relationships within a batch of images and texts. It is also well-structured and easy to follow.
- The authors provided strong mathematical support for the proposed learning objective.
- Extensive experiments were conducted to demonstrate the effectiveness of the proposed method.
- The proposed method has been proven effective on datasets containing billions of image-text pairs.

### Weaknesses
 - The proposed method was trained only on ViT-B and ViT-L vision encoders. Scaling up to ViT-H  and comparing with other methods are important to further demonstrate the scalability of ProLIP.
- As shown in Table 1, ProLIP introduces a more complex loss design and training process compared to CLIP, yet it achieves only a 0.9% improvement in ImageNet zero-shot classification and an average gain of 0.7%. Also in Table C.1, ProLIP with ViT-L also just exhibits slight improvement over CLIP. This modest improvement may indicate scalability challenges for the proposed method.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper works on a probabilistic CLIP that can model the uncertainty of the data. The model measures the uncertainty with a multi-dimensional Gaussian distribution, and it is trained with proposed novel inclusion loss. The paper also simplified the sampled distance loss from previous paper. Given that, the paper first shows some analysis that the estimated uncertainty aligns with several intuitions. Lastly, it shows two applications of image traversals (find a more concrete caption for the original caption iteratively) and prompt enhancement for the zero-shot image classification task.

### Strengths
1. The paper constructs a probabilistic VLM that can capture of uncertainty from the multimodal dataset. 

2. The paper proposes the inclusion loss and also provide intuitive understanding of it. 

3. The paper contains interesting analysis of the uncertainty. 

4. The paper proposes to utilize the uncertainty to conduct prompt rewriting.

### Weaknesses
1. The intuition behinds the paper is that multimodal paired data can be actually many-to-many mapping. I think that this intuition would lead to a multi-modes representation intuitively, as different text can be assigned to a single image, e.g., "A dog is walking" and "A man is looking at the building". However, the modeling in this paper is a Gaussian distribution with a single mean that can not conduct good mode coverage. 

2. (Minor) The basic behinds contrastive learning is that the positive pair is sampled from the joint distribution $P(x, y)$ while the negative pairs are sampled independently $P(x)P(y)$. Given that, contrastive learning does not force a 1-1 mapping from its maths intuition. Practically, the behavior might be different from the above as model learning might force 1-1. The motivation in Abs/Intro and Sec 2.1 might need a revision. The current claim is a little bit stronger to me and this might be fixed by writing or explanations. Also, in Sec 2.2, it claims that "VL tasks suffer from uncertainty as shown in Sec 2.1". This is a little bit beyond the context of Sec 2.1, as Sec 2.1 does not have strong VL task experimental evidence. I treated it as over-claim now but I think that it can be solved by writing revision. 

3. The two applications (image caption traversals and prompt enhancement) of the estimated uncertainty are not representative, and it would be better if more applications (more concretely, proof of concepts) are presented. For example, the data filtering, error estimation, etc.

### Questions
1. Please specify the context why $\mu_1$ and $\mu_2$ are norm-1 vectors (i.e., because CLIP normalizes them during training?)? I think that the original CLIP only normalizes when calculating the contrastive loss, maybe there is a re-parameterization here. Also please include them in text which would be friendly to reader. 

2. I wonder how the estimated variance from the model is used in the classification task? 

2. I appreciate the comparisons to KL divergence in Sec 3.3. The paper only measures KL(p1||p2) which has a different form to the proposed inclusion metric. How about adding a comparison to metric KL(p1 || p2) - KL(p2 || p1)? 

3. The inclusion loss is defined as $L(Z1, Z2)$ = $Z1 \in Z2$. Thus, in Line 259 and Line 264, should that be $L(t, v)$ and $L(partial, all)$ instead the current $L(v, t)$ and $L(all, partial)$? 

4. In Fig 5, it shows that the estimated variance of image is smaller than text. The loss defined in Eqn (6) is unsymmetrical for image and text (because of the hyperparemeters and the text VIB loss). Would that be possible that the smaller image variance is from this loss design? 

4. Please specify the exact formulation (i.e., implementation) of VIB in main text or in appendix.

4. Please specify how the uncertainty information is utilized when conducting the image traversals task. 

5. (An open question; no concrete answer required) What would be the golden uncertainty of a particular data in the PrVLM? I.e., the best distribution that a model should converge to?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a probabilistic VLM model that accounts for the many-to-many relationships between images and text. This model introduces an uncertainty token to estimate uncertainty without significantly increasing the parameter count. Additionally, the inclusion loss enhances interpretability by enforcing consistency between image-text pairs and between original and masked inputs.

### Strengths
The paper creatively applies probabilistic modeling to VLMs to better capture the many-to-many relationships between image and text pairs. It introduces a straightforward setup by adding an uncertainty token, effectively minimizing additional parameters. The paper provides a detailed analysis of the sources and levels of uncertainty in both image and text modalities, and explores various applications of this approach.

### Weaknesses
The paper primarily evaluates the model's performance on single-object scenarios, as seen with ImageNet in the main results (Table 1). While Table C.1 provides metrics for datasets with longer, more complex queries, such as Flickr, ProLIP shows a significant drop compared to CLIP. Including performance metrics and a detailed analysis of datasets with complex queries involving multiple objects and interactions in the main results would offer a more comprehensive evaluation of the model's capabilities. Furthermore, the analysis of uncertainty, while interesting, seems to lack a strong connection to the practical performance of the model. The paper claims that single object images have higher uncertainty, but this is not well-motivated and could be an artifact of the dataset. The paper does not explore the impact of this uncertainty on downstream tasks in a detailed manner.

### Questions
1. In Table C.1, ProLIP underperforms compared to CLIP on several datasets, such as Flickr. Could the authors provide a detailed analysis to explore the reasons behind this discrepancy?
2. The paper suggests that images with a single object are more uncertain than those with complex scenes. Intuitively, one might expect complex scenes to have higher uncertainty due to the variety of possible descriptions. Could the observed uncertainty levels be influenced by the choice of dataset used in the analysis?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces **Probabilistic Language-Image Pre-training** (ProLIP), an approach to vision-language models that integrates probabilistic modelling to capture the inherent uncertainty in image-text relationships. ProLIP departs from conventional deterministic embeddings by mapping inputs as random variables, estimating uncertainty using an "uncertainty token," and enforcing an inclusion loss to maintain distributional relationships between image-text pairs and between original and masked inputs.

### Strengths
-  This paper is well-written.
-  The research problem and motivation are well-defined, highlighting that CLIP-like models tend to oversimplify image-text alignment by assuming a one-to-one relationship.
-  ProLIP is claimed to be the first approach to pre-training probabilistic VLMs on a billion-scale image-text dataset, a feat that requires extensive computational resources.

### Weaknesses
 -   The improvement over deterministic VLMs like CLIP is limited, with only a marginal gain of around 0.9% in ImageNet accuracy (Table 1) when models are exposed to the same number of samples.
-   While the paper introduces the uncertainty token for efficient uncertainty estimation, it lacks empirical evidence demonstrating the claimed efficiency. The uncertainty token, while not adding parameters directly, increases the sequence length, which could impact computational cost due to the quadratic complexity of attention mechanisms in transformers. This needs to be quantified.
-   Compared to PCME++, ProLIP incorporates an uncertainty token and an inclusion loss, scaling the training dataset to CLIP’s level, yet the observed improvement remains modest, limiting the paper’s overall contribution. The novelty of the loss function and its impact on performance compared to PCME++ needs further clarification.
-  ProLIP requires the use of CSD to perform zero-shot prediction, which increases its complexity and makes it less straightforward than CLIP. The computational overhead of CSD compared to standard cosine similarity is not clearly addressed.

### Questions
- Although the authors claim ProLIP efficiently estimates uncertainty by incorporating an "uncertainty token" without adding parameters, this approach effectively increases the input length. Given that transformer complexity is quadratic relative to the input length, this addition likely increases the computation required for multi-head attention. How does the "uncertainty token" quantitatively compare to previous probabilistic VLMs in terms of training efficiency and inference speed? For example, the authors can report training time per epoch, inference latency on standard hardware, or FLOPs compared to baseline models.

- Is there any limitation discussed in the paper? (e.g. computational requirements)

### Soundness
3

### Presentation
3

### Contribution
2
