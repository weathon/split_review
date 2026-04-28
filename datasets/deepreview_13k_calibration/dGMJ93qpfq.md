# A PATCH LEVEL PERSPECTIVE OF PROMPT TUNING

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 5, 6, 3

## Abstract
Prompt tuning is an efficient way to adapt large foundation models, such as CLIP, by introducing learnable prompts with the input data tokens, offering a practical alternative to full model finetuning. However, when prompts are trained on base/target tasks, they often overfit, leading to reduced performance on novel, unseen tasks. To address this limitation, various techniques leverage global image semantics to improve accuracy on unseen tasks while maintaining performance on base tasks. However, they often overlook the rich fine-grained local information that could be crucial for capturing finer semantics and improving generalisation. In this work, we propose a modular approach to prompt tuning that leverages local semantics by incorporating patch-level information, representing the first integration of such semantics in this context. Specifically, we integrate patch-level information across vision, text, and predictions through three consistency mechanisms: 1) Patch-based consistency loss that aligns patches from the prompted input image with those from the same image processed by a frozen model, while also enforcing inter-view consistency by applying the loss across different views, capturing fine-grained regional dependencies and improving vision representation quality, 2) Text prompt consistency loss, where view-specific text prompts are tailored and regularised to maintain coherence across views, and 3) Vision features for each view, enriched with patch-level information, are used to generate predictions based on view-tailored text features. These predictions are then regularised across views, complementing the earlier consistency mechanisms and contributing to a cohesive overall framework. Our approach outperforms existing methods across multiple benchmarks, including base-to-novel generalisation, domain generalisation, and cross-dataset evaluation. These results underscore the potential of integrating fine-grained details for more robust and adaptable prompts, marking a step forward in foundation model tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new approach to prompt tuning for large vision-language models, leveraging patch-level information rather than global image semantics alone. In terms of technical design, it incoperates three key techniques:
Patch-based Consistency Loss: Ensures fine-grained regional alignment in image patches across different views.
Text Prompt Consistency: Creates view-specific text prompts to maintain cross-view coherence.
Vision Feature Regularization: Integrates patch-level details to enhance prediction quality.
The new method shows gains on three setups: base to novel, cross datasets, and domain generalization.

### Strengths
1. The combination of techniques showed gains on all nearly all eval metrics in all the three setups.
2. The authors conducted many ablation studies regarding different components and design choices of the model. They are very informative.

### Weaknesses
Overall, the final solution seems to be too complicated. There are quite a few components, losses, and tricks. There was not always a good explanation of why a certain component/trick would help. Some ablation experiments are still missing. The number of trained parameters is much higher than PromptSRC and DePT. The training cost is also much higher especially given that an augmented view is needed on top of the original view. The eval cost is also much higher since the text embedding needs to be conditioned on every image. More specifically:

1. How much can the inter-view patch loss help on top of the intra-view patch loss? This design greatly increases the training cost, so it would be great if the effect of this design is shown. The current ablation only shows the performance with either inter-view or intra-view loss, but not the performance with only intra-view loss. It is not clear if the inter-view loss is adding a significant benefit given the increased training cost.
2. Why is the convolution projection layer of patch features needed? Table 9 showed that it further improved some eval numbers. But what is the rationale of those gains? Are the gains worthy the additional complexity of the system? Especially given that it is not just a MLP, but a 3x3 convolutional block added on top of a visual transformer. Why not one additional transformer block? The justification for using convolution over a transformer block is not clear, especially given that the visual backbone is a transformer.
3. The authors chosed to condition the text embedding on image patch features. This greatly increased the eval/inference cost. Let's say there are N images and M classes. Without that conditioning, we only need to compute N image embeddings and M text embeddings. But since the text embedding needs to be conditioned on the image that is in question, so now we need to compute N image embeddings and MxN text embeddings. Moreover, this conditioning design made the addition of the clustering algorim necessary as well. The added complexity and computational cost of conditioning the text embedding on image patches is a significant concern, and the justification for this design choice is not fully convincing.
4. The authors chose to add the average of the patch features to the image-level features to get the final image embedding. Are any of the embeddings normalized? Could the authors elaborate on their design regarding which features are normalized and which are not, and explain why this deisgn choice?

### Questions
The original motivation of the paper is just to add patch-level information into prompt tuning. But the final design is much more complex than what is needed to involve patch-level information in prompt tuning. Is it that a very simple design would not show gain? Then does it suggest that the original motivation is not very convincing? The final solution showed gains, but was it just because it added patch-level information, or was it because all the increased system complexity and added trainable parameters?

### Soundness
4

### Presentation
4

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
This paper propose a prompt tuning method for CLIP. Unlike previous methods that use global feature consistency, the proposed method use the local feature consistency together. By incorporating the local features effectively, the proposed method achieve strong fine-tuning performance on various benchmarks

### Strengths
+ The proposed method is reasonable and sounds interesting. 

+ The authors conducted heavy ablation studies which is helpful to understand the proposed method.

+ The proposed method achieve strong performance on various benchmark and various settings.

### Weaknesses
 - The performance improvement over baseline seems marginal. The proposed method brings less than 0.5%p compared to baseline for most of evaluating settings. I suggest the authors to conduct repeated experiments and present the standard deviation, and show that the proposed method is statistically significant

- The proposed method has many choice of hyper-parameters and designs, which may not be appropriate for data limited learning.

### Questions
1, In section 3.2, the authors find the closest zero-shot patch from the anchor view using cosine similarity. However, because we know the augmentation parameters to generate the novel view, we already know the exact matching between anchor and augmented images. Why the authors find the closest patch using cosine similarity? How if we find the matching patch using the augmentation parameters?

2. In Eq (10), is g^i the class token from visual encoder? Then, what is the motivation of the sum of the global and local features in Eq 10? Can we try other operation like dot-product?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the overfitting problem in prompt tuning for CLIP on downstream vision tasks. The authors propose several regularization methods based on patch-level consistency losses, including a patch-con loss that considers both visual inter- and intra-view consistency, a text-consistency loss across views, and an inter-logit loss between decision.

### Strengths
* The paper introduces regularization losses based on patch information, which serves as a valuable complement to global information.

### Weaknesses
 * The proposed method is complex, incorporating three additional loss functions, which could make implementation and analysis challenging.
* The figure illustrating the method lacks clarity and does not sufficiently explain the approach on its own.
* The improvements demonstrated are marginal compared to recent works, such as Cascade Prompt Learning ([1]), which tackle the same issue of overfitting in prompt tuning.
* Equation 5 appears to contain a typo.
* Equation 9 is unclear: it references a "Voronoi Clustering" result as a set, which typically lacks an inherent order. How is the clustering result ordered here?

### Questions
* Equation 5 appears to contain a typo.
* Equation 9 is unclear: it references a "Voronoi Clustering" result as a set, which typically lacks an inherent order. How is the clustering result ordered here?

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
5

### Summary
This paper introduces a new approach of prompt tuning in vision-language models, called Patch-Aware Prompting (PAP) framework, created on top of baseline model PromptSRC [1] and DePT [2]. It integrates patch level visual information, with the textual embeddings for better vision-text alignment. This patch level information are extracted through Voronoi clustering of patch features, while connected with several consistency losses. While being attached with PromptSRC and DePT, the proposed method has achieved better performances and SOTA methods, in three different generalization tasks.


[1] Ji Zhang, Shihan Wu, Lianli Gao, Hengtao Shen, and Jingkuan Song. Dept: Decoupled prompt tuning. ArXiv, abs/2309.07439, 2023.

[2] Muhammad Uzair Khattak, Syed Talal Wasim, Muzammal Naseer, Salman Siddique Khan, Ming Yang, and Fahad Shahbaz Khan. Self-regulating prompts: Foundational model adaptation without forgetting. 2023 IEEE/CVF International Conference on Computer Vision (ICCV).

### Strengths
1. The proposed method has used a very old clustering method called Voronoi clustering, which is interesting.
2. The paper writing and presentation are overall good.

### Weaknesses
1. The proposed method looks like an extension of the baseline model PromptSRC, compromising a superior level of novelty. But it is also unclear how the authors take DePT model as an independent model, where DePT is itself an augmentation approach of the existing VLM baselines.

2. Why and how is the Voronoi clustering enhancing the alignment of text and vision? Why not direct addition of class features into the text embeddings just like CoCoOp? Why the patch level features are working better than class features here? I don't want any experimental data, but concrete qualitative reasons are needed.

3. Why only PromptSRC+PAP and DePT+PAP? PAP can also be attached with CoPrompt, MaPLe, CoOp, KgCoOp etc. 

4. It is recommended to consider the baselines consistent in every task, as some baselines are missing in table 1 and 2. The results of baselines used in table 3 are needed in table 1 & 2.

5. There is a mistake in Figure 1. B_{an} is denoted there as B_{av}.

### Questions
See the weakness section. I would like to increase my rating, if the proper justification of my questions will be given.

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
4

### Summary
This work aims at improving the generalization ability of existing prompt tuning methods for vision-language models.
The authors recognize that previous works often overlook the rich fine-grained local information while regularizing the learning
target. To address this issue, they introduce three consistency loss based on patch-level information into the overall objective function. By experiments under the base-to-new generalisation, cross-dataset and domain generalisation settings, 
they successfully validate the effectiveness of their method.

### Strengths
1. Most parts of the paper are clearly presented.
2. Promising results with extensive experiments.

### Weaknesses
My concern focuses on the novelty of this work. This work combines consistency regularization and fine-grained information, both of which are ideas similar to those found in existing works:
* Shuvendu Roy and Ali Etemad. Consistency-guided prompt learning for vision-language models.
ArXiv, abs/2306.01195, 2023.
* Muhammad Uzair Khattak, Syed Talal Wasim, Muzammal Naseer, Salman Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan:
Self-regulating Prompts: Foundational Model Adaptation without Forgetting. ICCV 2023: 15144-15154
* Long, S., Zhao, Z., Yuan, J. et al. Mutual Prompt Leaning for Vision Language Models. Int J Comput Vis (2024).

The designed losses in Eq(5),(11),(13) are simple extension to equations in PromptSRC. Eq(12) can be found in some Adapter-based methods, and Eq(6)(7) can be found similar form in contrastive pre-training methods, such as "Lewei Yao, Runhui Huang, Lu Hou, Guansong Lu, Minzhe Niu, Hang Xu, Xiaodan Liang, Zhenguo Li, Xin Jiang, Chunjing Xu: FILIP: Fine-grained Interactive Language-Image Pre-Training. ICLR 2022". The quantitative prompts in Eq(9)(10) are similar to those in "Rishabh Bhardwaj, Amrita Saha, Steven C. H. Hoi, Soujanya Poria: Vector-Quantized Input-Contextualized Soft Prompts for Natural Language Understanding. EMNLP 2022: 6776-6791". Due to the reasons mentioned above, this work is more like an incremental improvement.

Besides, the proposed method introduces too many extra hyper-parameters, and the authors mentioned that the performance on each dataset is sensitive to the setting of these hyper-parameters. As such, I am wondering how to set these hyperparameters? Also, the training time has also increased significantly.

Clarity:
The use of symbols in the paper is somewhat confusing and many of them are not enough explained, although their meaning can be derived from the context in most cases. Fig 1 and the descriptions in main text are mis-matched. The description of the motivation in Eq(9)(10) is too simplified. Some of the equations are wrong, such as Eq(1)(2).

### Questions
Clarity:
The use of symbols in the paper is somewhat confusing and many of them are not enough explained, although their meaning can be derived from the context in most cases. Fig 1 and the descriptions in main text are mis-matched. The description of the motivation in Eq(9)(10) is too simplified. Some of the equations are wrong, such as Eq(1)(2).

Reproducibility: This paper would have good reproducibility as most parts are simple to implement. It would be nice to supply where the Voronoi-based clustering code can be found, further improving the reproducibility.

### Soundness
3

### Presentation
3

### Contribution
2
