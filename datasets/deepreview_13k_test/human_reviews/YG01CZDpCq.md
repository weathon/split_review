# Don't Paint Everyone with the Same Brush: Adaptive Prompt Prototype Learning for Vision-Language Models

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Vision Language Models (VLMs) have demonstrated great potential on zero-shot classification tasks by computing the similarity between visual and textual embeddings. To adapt VLMs to a downstream task, recent advances introduced context optimization. It optimizes a single embedding for either visual or textual modalities, aiming to improve performance on both base and new classes. However, we identify a critical issue by using single embedding for each class. That is, for image samples of a single class, the visual appearance may vary significantly. Thus, existing methods relying on a singular textual embedding fail to capture the visual variance, leading to suboptimal performance on downstream tasks. In this paper, we propose an Adaptive Prompt Prototype Learning (APPLe) for VLMs. Specifically, we build various prompts as class prototypes to cover the visual variance. Moreover, there are inevitably some ambiguous words in prompts, bringing noise to the textual features. To resolve this problem, an adaptive attention mechanism is designed to weigh the importance of different prototypes. It learns to assign higher scores to the representative prototypes, and lower scores to the flawed or less representative prototypes. To evaluate the effectiveness of APPLe, we conduct experiments on three representative tasks, i.e., generalization to unseen classes, new target datasets, and unseen domain shifts. APPLe exhibits a consistent performance improvement of 3.66% on new classes and 2.79% on the harmonic mean.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study how to better prompt VLM, specifically CLIP model to tackle image classification tasks. The authors notice that using a single text prompt for each class is insufficient to capture the diversity of visual representations within that class. To address this, the authors introduce Adaptive Prompt Prototype Learning (APPLe), a technique that provides multiple text prompts for each class. Additionally, to mitigate the impact of noise in the textual prompts, the authors develop an adaptive attention mechanism capable of disregarding ineffective prompts. The implementation of these strategies results in performance that surpasses that of the current state-of-the-art methods.

### Strengths
- The authors demonstrate robust performance across both training-free and training-based methods, consistently outperforming strong baselines on nearly all datasets for both 'Base' and 'New' sets.
- Notably, the training-free methods implemented by the authors are capable of surpassing some training-based method.
- The authors present comprehensive analyses and comparisons with baseline methods, contributing valuable insights to the field.

### Weaknesses
- The authors keep claiming that CLIP only uses one prompt, but in CLIP paper section 3.1.4, they discuss how they use 80 prompts to improve the performance without sacrificing test time speed (unlike APPLe which is slower with more prompts). The authors should definitely compare their method to CLIP with 80 prompts as a baseline.
- The presentation can be improved:
    - It needs to be clarified how training-free works. I think the authors should more explicitly describe it. My understanding is that training-free = 50 prototypes only (the second row in Table 4). Correct me if I am wrong.
    - The description of the training process is also vague. Section 4 omits details on how prototype features are fine-tuned. It seems to me that the text encoder and the prompts are only used to initialize the prototypes. Correct me if I am wrong.

### Questions
- The authors primarily experimented with one CLIP model. It is unclear if this method can work with different CLIP variants, open-sourced CLIP replication or other VLM models. I'm curious if changing the model architecture, training data, or VLM format would yield different results.
    - While the method appears to be general, I'm concerned about it potentially "overfitting" to a specific model and dataset.
- How does the training process for cross-dataset transfer work? When training on the source data (e.g., ImageNet), the model learns prototype features for ImageNet classes and adaptive attention weights for them. How does this transfer to target datasets where prototypes and attention weights remain untouched during fine-tuning?
- Could you clarify the importance of the quality of prompts used in the experiments? What would happen if we used GPT-4 to generate the prompts? How does the quality of the input prompt to the GPT model impact the final performance?
- Although the authors claim that fine-tuning the prompt textual features does not lead to overfitting issues, there are no ablations on the performance of training with frozen prototype features to demonstrate whether fine-tuning the prototype is necessary.
- In Equation 7, the authors selected a method that can balance between all prototypes and the closest prototypes. Are there other balancing methods, such as using the Boltzmann operator or logsumexp, that could be considered?
- While the authors aim for diverse prompts, it might be interesting to fix the prototype and only train the attention weights and forcing the attention weights to be a multinomial distribution with low entropy. This would be essentially learning to select the best prototype. It would be interesting to see if GPT-3 can produce a better single prompt than the hand-designed prompts used in CLIP.
- Have the authors attempted to use the embedding ensembling method used in CLIP?


Minors:
-  In Equation 7, stating the "average cosine similarity" is not entirely accurate because the cosine similarities are weighted by the attention weights.
-  While the trend in Figure 5 is clear, it could be valuable to include settings with 0/1 and 1/0 to further illustrate the findings.

Justification:
In terms of performance, this paper demonstrates strength, and I commend the authors for their straightforward yet valuable concepts. Nonetheless, there are various intriguing aspects that remain unaddressed, leaving certain concerns. Additionally, the authors have made claims about the CLIP paper that may not be accurate.

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed an Adaptive Prompt Prototype Learning (APPLe) method for VLMs. The author has designed an adaptive attention mechanism to alleviate the noise and flaws within the prompts. The experimental results show that the method proposed by the author has consistent performance improvement on all 11 datasets and all tasks.

### Strengths
1. In the experimental results table, absolute performance improvements have been added to make the experimental results more intuitive.

2. The article has a complete system and clear organization, from problem introduction, formula reasoning, and image explanation to experimental results, making it easier for readers to read.

3. The method proposed by the author has better advantages compared to some counterpart methods.

### Weaknesses
1. As an important contribution, the Attention weighting and L_dec only gain limited performance improvements, which degrades the contribution to the community. The overall compared methods are also very limited. 

2. There is some confusion in the layout of tables and images.

3. Although using multiple prompts as category prototypes can help capture visual differences, in practice, not every visual sample closely matches each prototype. 

4. The article mentions the introduction of prototype decorrelation loss to suppress the co-occurrence of multiple confident prototypes. However, specific details on how the loss was designed and worked were not mentioned. This may affect the performance of the model in tasks with complex category distributions or a large number of categories.

5. It is not clear how to initialize these prototypes and how to obtain the base and novel class prompts.

### Questions
See Above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the prompt learning of visual-language models.  Different from previous prompt learning methods such as CoOp, this paper goes further to explore how to assign different prompts for different classes for better performance.  To achieve this goal, this paper proposes to construct the various prompts with LLMs as class prototypes and learns an attention module to reweight these class prototypes. This paper follows the setting of CoCoOp and MaPLe to evaluate the methods, and compare the methods with baseline methods including CoOp, CoCoOp, and MaPLe. The proposed method achieves more than 2% improvement on average.

### Strengths
1) This paper proposes to leverage multiple prompts to enhance the recognition ability. For different classes, the prompts are allowed to be different. Its idea makes sense since the "classes" are the abstract of the observation, in which different classes may have different focuses. 
2) The proposed method takes each prompt as a point and tries to find a prototype (with an attention model) for given classes. This method is easy but effective. 
3) The proposed method achieves good performance on the base-2-new setting.

### Weaknesses
The main concern is about the presentation, which does not effectively verify the methods and demonstrate the superiority. I summarize some detailed suggestions below. 
1) The experiments follow the base-to-new setting in CoCoOp. However, the base-to-new setting is more about generalization ability. Besides, the performance of the base-to-new setting is very sensitive to the hyperparamers, especially for epochs. It is because the performance of this setting requires a balance between alignment and generalization, which can be achieved by reducing the epochs.  When tuning the training epochs of CoOp, it will also achieve good performance. It is suggested to use the few-shot learning setting in CLIP and CoOp, which is more fair and supportive to demonstrate the effectiveness of the proposed methods. 
2) The main idea of this paper is to explore how to assign multiple prompts to one class. PLOT also shares similar targets to leverage multiple prompts (ProDA is similar too). Thus, it is much better to employ these methods as the main baselines for comparison, instead of CoCoOp which targets generalization. It is suggested to compare with PLOT and ProDA in the few-shot setting.  It is better to add a discussion about the difference between the proposed method and them. 
3) What are your prompts for GPT-3 to generate prototypes?  Is the model robust for different generations?
4) There are a series of methods for the class-wise LLM-generated prompts, such as [1-2]. It is suggested to add some discussions and comparisons with these methods. 
 [1] Menon, Sachit, and Carl Vondrick. "Visual Classification via Description from Large Language Models." ICLR 2023.
 [2] Pratt S, Covert I, Liu R, et al. What does a platypus look like? generating customized prompts for zero-shot image classification. ICCV 2023.

### Questions
Please refer to the weaknesses part.  The main concern is about the unsuitable experimental comparison and fewer discussions. 
I will modify the final score after the discussion with the authors and other reviewers.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
this paper addresses the significant visual variance  problem when apapting VLMs to downstream tasks. The authors incorporate multiple prompts as class prototypes, use attentin matrix to weigh the prototypes, and design a prototype decrrelation loss to surpass co-occurence of multiple confident prototypes. Experiments show that the proposed method outperforms existing methods significantly.

### Strengths
1. the whole method is carefully designed for multiple class prototypes, like adaptive attention, closest prototype, prototype decorrelation. 
2. the improvement is siginficant. 
3. experiments are well designed with the design of the methods. the adaptive attention visualization, understanding prototpyes by image retrieval and convincing. the analysis of failure cases gives helps me better understand the paper.
4. the Discussion and Comparison to Context Optimization Methods are inspiring.

### Weaknesses
1. As stated in the paper, Prototype learning traces its roots to classical models such as K-Nearest Neighbors (Peterson, 2009) and Learning Vector Quantization. Though some new aspects (adaptive attention, decorrelation, etc) are introduced in this paper, the technical novely seems stil limited. 
2. The paper addresses the adaptive attention of prototypes. This does work but is also somewhat a straightforward point. The paper does not tackle the adaptive attention of words inside a prototype. The importance is verified in the failure case analysis in the experiments.

### Questions
what's the learnable part of prompt prototypes in Figure 2?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
