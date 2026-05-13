# Narrowing Information Bottleneck Theory for Multimodal Image-Text Representations Interpretability

- Decision: Accept
- Scores: 8, 3, 5, 5

## Abstract
The task of identifying multimodal image-text representations has recently received increasing attention, particularly with models like CLIP (Contrastive Language-Image Pretraining), which excel at learning complex associations between images and text. Despite these advancements, ensuring the interpretability of such models remains crucial for their safe application in real-world scenarios, such as healthcare. Numerous interpretability methods have been developed for unimodal tasks; however, these approaches often fail to transfer effectively to multimodal tasks due to fundamental differences in representation. Bottleneck methods, widely recognized in information theory, have been applied to enhance CLIP’s interpretability, but they often suffer from strong assumptions or inherent randomness. To address these limitations, we introduce the Narrowing Information Bottleneck  Theory, a novel approach that re-engineers the bottleneck method from the ground up. This theory is designed to satisfy modern attribution axioms, offering a robust solution for improving the interpretability of multimodal models. In our experiments, compared to state-of-the-art methods, our approach improves image interpretability by an average of 9\%, text interpretability by an average of 58.83\%, and increases processing speed by 63.95\%. Our code is publicly available at: https://anonymous.4open.science/r/NIB-DBCD/.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors squeeze the information for classification through a bottleneck - in essence they are trying to reduce to the most important features. Importantly, it also shows negative and positive features for classification rather than just positives. To do this, it is trialed on 3 popular datasets, conceptual captions, imagenet, and flickr8k.
 
The method outperforms other interpretability methods on confidence drop, e.g how much model confidence decreases when good features according to the interpretability method are removed, and confidence increase, e.g how much model confidence goes down when negative features are removed.

### Strengths
While numerous interpretability methods exist, they cannot cope well with the multimodality od data.
The proposed methods addresses this issue, with 9% improvement for text interpratability, and 58% improvement fo image interpratability.
The proposed method also eliminates randomness an hyperparameter dependency.
Also, current methods stem from gradient analysis, which introduces additional challenges.

### Weaknesses
I am curious why the representation of both images and text is of the same dimension, d
Proof of Theorem 1 is obvious, so it should not be a theorem.
Theorem 2 is basically a consequence of Theorem 1. It should not be a theorem. Both are nasically Remarks.

Even in the example shown with the image of the dog and cat, it responds strongly with the corner of the image, which is not interpretable.
Similarly, how does the method respond when the image is cluttered with more information, or the relevant information makes up a much smaller total proportion of the image. More examples are needed.
Choice of layer number, can you justify theoretically why layer 9 has been chosed.

### Questions
Can the authors  show interquartile range of performance outcomes in Table 2? in addition, other image examples. whilst the method clearly outperforms the others on average, it is not clear if it is robust.
 Even in the example shown with the image of the dog and cat, it responds strongly with the corner of the image, which is not interpretable.
Similarly, how does the method respond when the image is cluttered with more information, or the relevant information makes up a much smaller total proportion of the image. More examples are needed.
Choice of layer number, can you justify theoretically why layer 9 has been chosed.

### Soundness
3

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
4

### Summary
The paper addresses the challenge of improving interpretability in Vision-Language Pre-trained Models, such as the multi-modal model CLIP (Contrastive Language-Image Pretraining) which maps images and texts into a shared embedding space. Existing interpretability methods, designed for unimodal tasks, are generally insufficient for explaining the complex relationships between visual and textual modalities. To assess the interpretability in the model CLIP, Wang et al (2023) recently introduced the Multi-modal Information Bottleneck (M2IB) approach, aiming to find attribution parameters that maximize the likelihood of observing features of one modality given features associated with the respective other modality.

Following from Wang et al (2023), here, the authors propose the Narrowing Information Bottleneck Theory (NIBT), a new interpretability approach that redefines bottleneck methods in information theory. NIBT targets the randomness and hyperparameter dependency associated with previous approaches, such as M2IB, to deliver more deterministic interpretability outcomes. The method includes a mechanism to pinpoint negative features that adversely impact model predictions, aiming to further enhance the interpretability.

Through simulations on the datasets Conceptual Captions, ImageNet, and Flickr8k, the authors state that NIBT significantly improves interpretability and processing speed compared to state-of-the-art methods.

### Strengths
The paper introduces the Narrowing Information Bottleneck Theory (NIBT), a new interpretability method that redefines traditional bottleneck concepts from information theory. This approach departs from the randomness and hyperparameter sensitivity inherent in previous methods, enabling a deterministic alternative for multimodal representation interpretability.

The concept of attributing negative features—dimensions that negatively impact model performance—is original. This feature provides an innovative perspective on model understanding, distinguishing NIBT from other methods focused solely on positive attributions.

The paper provides theoretical derivations and mathematical proofs for its main claims.

The method is assessed across three datasets, including Conceptual Captions, ImageNet, and Flickr8k.

### Weaknesses
1. The Narrowing Information Bottleneck Theory (NIBT) is introduced to address limitations in previous bottleneck methods by providing a deterministic approach, aiming to reduce randomness and dependency on hyperparameters. The method states to use a single scalar λ to control information flow across all feature dimensions. This simplification is significant:

1.1. The scalar λ as a universal control across all dimensions suggests a uniform bottleneck effect, which can be problematic if different features vary significantly in their contribution or sensitivity. In practice, applying a single λ across all dimensions might oversimplify the dynamics of feature importance, potentially reducing interpretability in models where feature contributions are heterogeneous. The method does not account for the possibility that some features might require a stronger bottleneck than others, or that the optimal bottleneck strength might vary non-linearly across the feature space. This could lead to either over-constraining important features or under-constraining irrelevant ones, thus hindering the overall interpretability.

1.2. The noise distribution, ϵ∼N(0,σ^2), plays a role in regularizing the information flow by adding Gaussian noise to the controlled dimensions. This assumption is justified under the simplification of feature distributions. However, the authors should justify why the Gaussian assumption holds across different multimodal applications, as non-Gaussian feature distributions might invalidate this approach or reduce its robustness. The method does not provide a mechanism to adapt the noise distribution to the specific characteristics of the input data, which could be problematic in scenarios where the feature distributions are highly non-Gaussian or multimodal. The use of a fixed Gaussian noise distribution might not adequately capture the complexities of real-world data, potentially leading to suboptimal results.


2. Equations

2.1. Equation 1 is well-grounded in information theory, with a clear goal of maximizing relevant information while minimizing redundancy with respect to the input. The critical factor here is the interaction between λ and β. While NIBT eliminates β, this raises questions about managing trade-offs between task-relevant and redundant information. The authors should address potential limitations of a fixed λ and how it impacts feature discrimination. The absence of a mechanism to balance the trade-off between task-relevant and redundant information could limit the method's ability to effectively filter out noise and focus on the most salient features. The method should provide a more nuanced approach to managing this trade-off, rather than relying on a fixed parameter.

2.2. Equation 2: The decomposition of features into spatial (i) and channel (c) dimensions adds specificity but introduces complexity. By normalizing the interaction with Gaussian noise across spatial dimensions, the method assumes consistency in spatial features' importance, which may not hold in multimodal contexts where image regions and text embeddings exhibit varied significance. The method does not account for the fact that different spatial locations might have varying degrees of importance for the task at hand, and that this importance might not be uniform across different modalities. This could lead to a loss of fine-grained spatial information, which is crucial for accurate interpretability.


3. Theorems

3.1. Theorem 1: it claims that mutual information, I(z~(λ),x), is a monotonically increasing function of λ, with I(z~(0),x)=0. The proof relies on KL divergence and a Gaussian assumption. While monotonicity is proven under Gaussian noise, real-world feature distributions could violate this condition. The impact of deviations from Gaussianity on this monotonic relationship needs to be tested. Also, the assumption of independence between noise and features for bottleneck properties needs further validation, as dependency might arise naturally in multimodal models where spatial and channel-wise correlations exist. The theorem's reliance on the Gaussian assumption and the independence of noise and features limits its applicability in real-world scenarios where these assumptions might not hold. The method should address the potential impact of non-Gaussian feature distributions and dependencies between noise and features on the monotonicity of the mutual information.

3.2. Theorem 2: the reduction of σ toward zero should be more justified. Practically, in cases of low signal-to-noise ratios, completely removing σ could reduce robustness. A discussion of trade-offs in interpretability and stability as σ approaches zero would help add clarity. Also, the claim that I(ar{z}(λ), x) becomes deterministic as σ decreases suggests a very controlled bottleneck. It is theoretically sound, but validating this deterministic behavior across different datasets (especially with diverse noise levels) is needed to confirm this claim. The method should provide a more detailed analysis of the trade-offs between interpretability and stability as σ approaches zero, and validate this behavior across diverse datasets with varying noise levels. The method should also address the potential impact of low signal-to-noise ratios on the robustness of the results.

3.3. Theorem 3: equation is both novel and complex, stating that negative values represent features that reduce information relevance. The introduction of negative features could indeed improve interpretability by explicitly identifying detrimental features. The authors should show that these attributions correspond to irrelevant or misleading features across model types. Another remark is that the integral's dependency on λ suggests that the influence of each feature diminishes as λ decreases. Yet, this gradual reduction might fail for complex, highly nonlinear multimodal interactions. A closer look at cases where feature relevance changes nonlinearly with λ could show edge cases where the method’s assumptions do not hold. The method should provide empirical evidence that the identified negative features are indeed detrimental to model performance across different model types. The method should also address the potential limitations of the gradual reduction of feature influence as λ decreases, particularly in scenarios with complex, highly nonlinear multimodal interactions.


4. Qualitative Analysis: The paper includes one visual comparison with M2IB only, but a more detailed qualitative assessment would be beneficial. For example, showing more examples where NIBT succeeds and where it fails compared to other methods would provide a better understanding of the strengths and limitations.

For the interpretation of Figure 1, the authors write: "As shown in Figure 1, our proposed method successfully distinguishes and excludes negative properties from the explanation. In Figure 1d, the M2IB method continues to highlight irrelevant negative features, such as the cat’s face, even when the subject is a dog. However, in Figure 1b, our method correctly ignores these negative properties, focusing on more relevant, positive features, showcasing its improved attribution performance." Looking at this unique visualisation, the method proposed seems to lack specificity and highlight areas of the image that are not relevant, compared to M2IB.


5. Computational Efficiency: The authors emphasize the efficiency of NIBT, Yet the experiments lack a detailed breakdown of computational costs relative to model complexity and dataset size. Including this analysis would better illustrate the trade-offs between interpretability and computation.


6. The paper does not address whether the differences in the results between the different methods are statistically significant. Adding statistical tests (e.g., t-tests or bootstrap analysis) would add rigor to the claims of superiority over baseline methods.


7. Regarding the impact of negative feature attribution: The paper does not at the moment empirically validate whether the identified negative features are truly detrimental.


8. The ablation studies on num steps and target layer provide useful insights, but they feel somewhat limited in scope. It would be useful to look at the interplay between num steps, target layer, and other model hyperparameter would give a more holistic view of how these factors influence performance.

### Questions
Q1. You write that "the interpretability methods proposed in this paper aim to improve model transparency and are intended for enhancing the trustworthiness of AI systems, especially in sensitive domains such as healthcare" (lines 540-542). You chose to present results on three datasets. Are these datasets sufficiently diverse to reflect real-world multimodal scenarios, especially in domains where interpretability is crucial, like medical imaging? Why did you not choose at least one medical imaging dataset like the M2IB paper?

Q2. Could you please explain why you present the illustration of your method compared to the M2IB method in the paper (and compared to other methods in your code) on a unique image of a cat and dog. Why did you choose two simple and short text captions to illustrate your method? 

Q3. The paper claims an average improvement of 9% in image interpretability and a 58.83% increase in text interpretability. The important increase in text interpretability is striking and suggests that NIBT offers substantial benefits. Could you please justify why the improvement in text interpretability is so much higher than in image interpretability? Are there inherent differences in how text and image features are handled by CLIP that NIBT is better suited for?

Q4.  How does identifying negative features improve model interpretability in practical applications? For instance, could this lead to better debugging of models or highlight biases in the training data? Providing concrete examples would strengthen the argument for this feature. 

Q5. Are there scenarios where the method might fail?

### Soundness
1

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
This paper presents the Narrowing Information Bottleneck Theory (NIBT) as a solution to the challenges of randomness and hyperparameter sensitivity in the interpretation of multimodal models like CLIP. The authors systematically summarize existing methods of Multimodal Image-Text Representation (MITR) interpretability and modify the traditional Bottleneck approach with NIBT, which enhances the interpretability of both image and text representations. The proposed method shows improved performance in attribution accuracy and computational efficiency across various datasets.

### Strengths
1.	The paper systematically and theoretically analyzes the current MITR interpretability methods. The theory is based on information theory and seems reasonable. 
2.	The proposed NIBT is simple by replacing the univariate Gaussian noise in the bottleneck layer with the multivariate gaussian distribution to control all dimensions of the model hidden states.

### Weaknesses
1.	The proposed method is simple by changing univariate distribution to multivariate distribution, but it's unclear whether it will correlate with the limitations of IBP. The theoretical analysis and the proposed algorithm seem loosely connected to me. I don't see the proposed method as a direct result of the theoretical analysis. Specifically, while the paper introduces the Narrowing Information Bottleneck Theory (NIBT) and discusses the importance of controlling the information flow, the jump to using a multivariate Gaussian distribution feels somewhat arbitrary. The paper does not sufficiently demonstrate how this specific choice of distribution directly addresses the limitations of the Information Bottleneck Principle (IBP) in the context of multimodal interpretability. It's not clear how the multivariate Gaussian, compared to other possible distributions, is theoretically justified as the optimal choice for narrowing the bottleneck and improving interpretability.
2.	The story is a little bit hard to follow. It would be better for authors to make the story clearer. The narrative lacks a clear and concise explanation of how the theoretical concepts translate into the practical implementation of the algorithm. The connection between the information-theoretic arguments and the actual steps of the proposed method needs to be more explicitly laid out. The paper would benefit from a more step-by-step explanation of how the narrowing process is achieved, and how the multivariate Gaussian distribution facilitates this narrowing in a way that directly enhances interpretability.

### Questions
1.	The proposed method NIBT claims no randomness. But the computation of z_{ic} still contains the sampling noise.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles the challenge of enhancing interpretability in multimodal image-text models like CLIP, which are widely used in applications demanding high reliability, such as healthcare. The authors introduce the Narrowing Information Bottleneck Theory, a re-engineered bottleneck approach that aligns with modern attribution standards to improve interpretability. Experimental results demonstrate significant gains: a 9% improvement in image interpretability, a 58.83% boost in text interpretability, and a 63.95% increase in processing speed compared to state-of-the-art methods.

### Strengths
- Clarity and Structure: The paper is well-organized and written in a clear, accessible manner, making it easy to follow even for readers who may be less familiar with the technical aspects of interpretability in multimodal models.
- Code Accessibility: The authors have made their code publicly available, which greatly enhances the reproducibility of the research and provides valuable resources for the community to build on this work.
- Mathematical Rigor: The theoretical formulae are meticulously derived and clearly presented, enhancing the paper’s rigor and allowing readers to grasp the technical foundation of the Narrowing Information Bottleneck Theory.
- Comprehensive Literature Review: The paper thoroughly addresses related work, including important methods like M2IB, COCOA, and FALCON. This contextualization not only strengthens the theoretical foundation but also allows readers to understand how the proposed method improves upon existing approaches.

### Weaknesses
 - Paper Length: The paper exceeds the ICLR25 page limit, taking more than 10 pages for the main text. According to the ICLR25 “Call for Papers,” submissions with main text on the 11th page are subject to desk rejection. The authors may need to condense certain sections to adhere to submission guidelines.
- Application-Specific Relevance: Although the paper emphasizes the importance of interpretability for high-risk applications such as medical diagnosis and content moderation, it lacks application-specific experiments. No quantitative or qualitative evaluations on healthcare or content moderation datasets are included, which would provide critical insight into the real-world applicability of the proposed method. The absence of such experiments significantly limits the assessment of the method's practical utility in these crucial domains.
- Experiment Scope: The experimental evaluation appears limited. In contrast to the M2IB paper, which includes evaluations on diverse datasets (image captioning, radiology, and remote sensing), this paper only tests on standard image datasets. A broader range of datasets, particularly those relevant to the claimed high-risk applications, would strengthen the evidence for the proposed method’s versatility and robustness in high-stakes domains. The current evaluation does not sufficiently demonstrate the method's ability to generalize beyond standard image datasets.
- Table Formatting: The significant figures in Tables 2 and 3 lack consistency, which affects readability and may lead to confusion when comparing results. The inconsistent precision makes it difficult to accurately assess the magnitude of the reported improvements.
- Minor Typos:
  - Line 44-45: “blackbox” should be formatted as ``blackbox’’.
  - Line 322: “Appendix” is referenced without any supporting link, in contrast to Line 296, which does provide a reference.

### Questions
- Can the authors clarify whether the current content will be revised to meet ICLR’s page limitations for the main text?
- Have the authors considered adding experiments on healthcare or content moderation datasets to validate the method’s relevance for high-risk applications?
- Given the limited dataset variety in the current experiments, could the authors discuss how the proposed method might generalize to other domains, even by qualitative analysis?
- Would it be possible to revise Tables 2 and 3 to ensure consistent significant figures for improved readability?

### Soundness
1

### Presentation
2

### Contribution
1
