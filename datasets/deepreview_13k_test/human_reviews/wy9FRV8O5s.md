# ZeroDiff: Solidified Visual-semantic Correlation in Zero-Shot Learning

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Zero-shot Learning (ZSL) aims to enable classifiers to identify unseen classes. This is typically achieved by generating visual features for unseen classes based on learned visual-semantic correlations from seen classes. However, most current generative approaches heavily rely on having a sufficient number of samples from seen classes. Our study reveals that a scarcity of seen class samples results in a marked decrease in performance across many generative ZSL techniques.  We argue, quantify, and empirically demonstrate that this decline is largely attributable to spurious visual-semantic correlations. To address this issue, we introduce ZeroDiff, an innovative generative framework for ZSL that incorporates diffusion mechanisms and contrastive representations to enhance visual-semantic correlations. ZeroDiff comprises three key components: (1) Diffusion augmentation, which naturally transforms limited data into an expanded set of noised data to mitigate generative model overfitting; (2) Supervised-contrastive (SC)-based representations that dynamically characterize each limited sample to support visual feature generation; and (3) Multiple feature discriminators employing a Wasserstein-distance-based mutual learning approach, evaluating generated features from various perspectives, including pre-defined semantics, SC-based representations, and the diffusion process. Extensive experiments on three popular ZSL benchmarks demonstrate that ZeroDiff not only achieves significant improvements over existing ZSL methods but also maintains robust performance even with scarce training data. The code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes to exploit diffusion mechanism to enhance the generative models in zero-shot learning. Specifically, existing generative zero-shot learning methods heavily relies on a large quantity of seen class samples, and the performance of such methods degrades with insufficient samples. To address this problem, the proposed method augments the training set by generating more seen-class and unseen-class samples with diffusion mechanism. With more available samples (either real or generated), the proposed method surpasses existing zero-shot learning methods in both general and sample-limited situations.

Besides, the proposed mutual learning mechanism helps learning better discriminators in the generative process, which in turn improves the generators and classifiers, also contributing to the better performance of the proposed framework.

### Strengths
(1)	The proposed method is reasonable and technically solid. To be specific, although addressing the limited data issue by generating more data is quite straightforward, the details of the structure are still novel and effective. For example, the mutual learning mechanism of the discriminators and the incorporation of the diffusion module are well designed.
(2)	The proposed method is effective. As shown in the experiments, the proposed method can achieve better performances than existing methods in most general zero-shot learning situations, and the proposed method consistently surpasses existing generative ZSL methods in data-limited situations. Such results validate the effectiveness of the proposed method.
(3)	The authors provided some visualization results of the learned features, which could provide us with some insights into the possible future direction for further improving ZSL methods.

### Weaknesses
(1)	The main manuscript is quite confusing without the appendix. For example, how to finetune the feature extractors, and the details of training and testing are not clearly presented in the main manuscript, making it somehow hard to understand the proposed method when reading the main paper. It would be better if the authors could briefly explain and highlight such key details in the main paper as well as explain them in detail in the appendix.
(2)	It would be better to conduct more experiments in the ablation study part (Table 3). Since the proposed method adopts two kinds of visual features instead of one kind of feature as in most existing ZSL methods, it would be necessary to show how the additional feature contribute to the final performance. That is to say, it would be better to show the performances of G+R+D_{adv}, G+D_{adv}+D_{diff}+L_{mu}, etc..

### Questions
(1)	More experiments in the ablation study should be conducted to clearly show the contribution of the additional contrastive feature. Specifically, it would be better to see the results of G+R+D_{adv}, G+D_{adv}+D_{diff}+L_{mu}, and etc..

(2)	In recent years, GPT-series models exhibit amazing performances on zero-shot learning tasks, sometimes even surpasses the models specifically designed for ZSL tasks. It would be interesting to discuss the pros and cons of specifically designed ZSL models compared to such large multi-modal models (LMMs). For example, what are the advantages of specifically designed ZSL models? Are they still necessary in the existence of such large multi-modal models? If so, in which scenarios could the ZSL models perform better than the LMMs? Is it possible to combine both ZSL models and LMMs to achieve even better performances?

It would be sufficient to compare the proposed method with LMMs on a small portion of test samples (e.g. 100 images per dataset), and the results and discussions could be included in a separate new section. I believe these experiments and discussions would surely make the paper more insightful.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes ZeroDiff, a generative framework for zero-shot learning (ZSL). It includes three key components: 1) diffusion augmentation, which transforms limited data into an expanded set of noised data to mitigate generative model overfitting; 2) supervised-contrastive-based representation, which dynamically characterizes semantics of individual samples; and 3) multiple feature discriminators, which evaluate generated features from various perspectives.

### Strengths
- The analysis of the performance degradation of ZSL due to a spurious visual-semantic correlation learned from a limited number of seen samples is inspiring.
- The proposed diffusion augmentation and dynamic semantics methods are interesting.

### Weaknesses
- Identify and highlight the 1-2 most critical components that provide the key insights. The proposed pipeline is quite complex. It might be hard to tune the whole model. Moreover, it is also hard to know what is the key insight of the proposed method, since there are too many components.
- Provide more motivations and justifications on the design choices of the key components. For example, 1) a clear explanation of the complementary benefits of using both CE and SC loss-based features should be provided. It claims that the SC loss-based representation contains more instance-level semantics. Then why both CE loss-based features and SC loss-based features are used jointly, rather than simply use SC loss-based representation? 2) The theoretical reasoning behind how the denoising discriminator alleviates instance overfitting is required. 3) A detailed justification for each element in the concatenated input to the DFG, explaining how each contributes to the model's performance. In other word, what is the motivation of taking the concatenation of the semantic label a, latent variable z, diffusion time t, noised feature vt, and SC-based representation r0 as condition of DFG? It would be better to give more insightful and in-depth analysis to these design choices, rather than simply verifying by experiments.
- More detailed ablation study would be beneficial to show the effectiveness of the proposed method. Since the proposed method contains many components, the ablation study may not sufficient. For example, though table 3 gives the ablation study of each component, it is still unclear the effectiveness of the detailed design choice within each component, such as the condition of DFG module.
- Provide a more detailed caption for Fig. 4 that explains the key differences between (a), (b), and (c). It is hard to see the key difference among Fig. 4 (a), (b), and (c). It would be better to give more explanations.

### Questions
- How to ensure stable training of such a complex pipeline?
- What are the motivations of the design choices of the key modules?
- How to effectively evaluate the design choices of each module?

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
5

### Summary
The paper proposes a novel diffusion-based generative framework ZeroDiff for ZSL. Starting with a very motivating indicator, the paper claims that current generative methods learn spurious visual-semantic relationships when training data is insufficient, resulting in the failure of generated features. The comparison results well validate the effectiveness of the proposed method.

### Strengths
1. The paper proposes a novel diffusion-based generative method for ZSL.
2. The experiments are comprehensive.

### Weaknesses
1. The paper claims that generative-based methods learn spurious visual-semantic relationships when training data is insufficient. Is the conclusion applicable to non-generative ZSL methods?
2. As shown in Fig.2, \delta_{adv} increases over the three datasets as the training progresses. However, the paper aims to learn a model with low \delta_{adv} values. Does that mean we are getting a worse model as the training continues? It isn't very clear. The authors need to clarify the relationship between increasing \delta_{adv} values and model performance, and explain how this relates to the goal of learning substantial visual-semantic correlations. It would be helpful to explore what an ideal \delta_{adv} curve should look like.
3. In L262, the authors fine-tune the backbone model by the SC loss. However, the baseline methods do not fine-tune the feature extractor. Therefore, the comparison seems to be unfair. The authors should either apply the same fine-tuning to the baseline methods, or provide results for their method without fine-tuning, to ensure a fair comparison. Additionally, it would be helpful to discuss the impact of this fine-tuning on the overall performance.
4. The whole training process is divided into three stages, which makes it very complicated and hard to read. In addition, the author uses too much information as input for G in L301. Is this reasonable and necessary? The authors need to discuss potential ways to simplify the approach or explain why each component is necessary for the method's performance. It would be helpful to conduct an ablation study that shows the impact of each input on the final performance.

### Questions
Please see the weakness above.

### Soundness
3

### Presentation
2

### Contribution
3
