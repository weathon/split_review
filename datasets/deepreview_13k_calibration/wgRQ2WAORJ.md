# Aligning Visual Contrastive learning models via Preference Optimization

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 8, 6, 3

## Abstract
Contrastive learning models have demonstrated impressive abilities to capture semantic similarities by aligning representations in the embedding space. However, their performance can be limited by the quality of the training data and its inherent biases. While Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) have been applied to generative models to align them with human preferences, their use in contrastive learning has yet to be explored.
This paper introduces a novel method for training contrastive learning models using Preference Optimization (PO) to break down complex concepts. Our method systematically aligns model behavior with desired preferences, enhancing performance on the targeted task. In particular, we focus on enhancing model robustness against typographic attacks, commonly seen in contrastive models like CLIP. We further apply our method to disentangle gender understanding and mitigate gender biases, offering a more nuanced control over these sensitive attributes. Our experiments demonstrate that models trained using PO outperform standard contrastive learning techniques while retaining their ability to handle adversarial challenges and maintain accuracy on other downstream tasks. This makes our method well-suited for tasks requiring fairness, robustness, and alignment with specific preferences. We evaluate our method on several vision-language tasks, tackling challenges such as typographic attacks. Additionally, we explore the model's ability to disentangle gender concepts and mitigate gender bias, showcasing the versatility of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces an alignment method designed for contrastive models, such as CLIP, using aligned and unaligned image-text pairs. In this setup, each image input has a preferred (or aligned) response and an dispreferred (or unaligned) output. The model is trained to differentiate between these two responses using preference optimisation designed as a one-step Markov decision process. Therefore, they use a preference dataset that pairs images with aligned and unaligned responses, and a regularisation dataset containing clean examples to maintain the model's ability to generalise to other downstream tasks. Importantly, they don't fine-tune the full model but train a single linear projection layer on top of the frozen text and image encoders. 

To further control the model's behaviour, the authors modify the singular values of the learned linear transformation. Specifically, they apply a singular value decomposition (SVD) to the weight matrix of this layer and scale all singular values using a scaling parameter $t$. This intervention technique builds on the intuition that the linear transformation transforms the original similarity function between image and text spaces.

They evaluate the effectiveness of their method in two settings. First, they evaluate its effect on typographic robustness by comparing it against baseline models (incl. standard CLIP, PAINT, Defense-Prefix) across nine datasets (incl. ImageNet, Flowers102, and EuroSAT). The preference dataset is created by adding misleading text to the original images of each dataset. They find that their method performs on par or better than prior methods, with a few exceptions. Despite improving the robustness, some performance gaps between the original and typographic dataset remain; for example, a gap of around 20 % on StanfordCars. Using the intervention technique leveraging the SVD of the linear projection layer, they show that they can modify the trade-off between OCR and object detection performance. In the second setting, they explore the possibility to disentangle gender representations. They train the linear transformation using a dataset of images depicting men and women during activities, and show that by scaling the singular values they can reverse gender-specific representations, including a specific scaling factor where the gender information is effectively neutralised, without significant degradation on the downstream task.

### Strengths
- This paper appears to be the first paper to apply preference optimisation to contrastive models, and presents an interesting use of SVD to control model behaviour. 
- Optimising robustness and mitigating (gender) biases are of significant interest, especially in high-risk domains. 
- The evaluation results suggest comparable and often better performance than alternative approaches in improving robustness while enabling a (to some degree) interpretable intervention technique. 
- The paper is well written and easy-to-follow.

### Weaknesses
 - Despite improving robustness over baseline methods in some datasets, none of the methods consistently outperforms other methods (see Table 1).
- The baseline methods, PAINT and Defense-prefix, and their differences to the proposed method are not explained in the paper.

Minor Comments: 
- Line 23: Incomplete sentence „Our experiments We demonstrate“.
- Line 256: Comma instead of dot used. 
- Line 258: Comma should be a dot, and dot should be a comma. 
- Line 289: „this“ -> „This“ 
- The differences in Table 1 appear to computed inconsistently. While most of the time the differences are computed based on the best alternative method incl. the base model (e.g. OxfordPets), the difference for DTD O is computed with respect to PAINT, whereas CLIP seems to performs better. Overall, I think it would be easier to follow if all differences would be reported relative to the base CLIP model.

### Questions
- The role of the transformation scaling parameter $t$ in the results in Table 1 remains unclear to me. Is the parameter varied between all settings or kept constant?
- The scaling range from -2 to 1.2 in Figure 2 has likely been chosen because the performance improves up until that point. But what happens if you scale between e.g. -4 and 4? It would be interesting to see even if performance starts to deteriorate after some threshold.
- Have you tried training separate linear projection layers for the text and image decoders?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a method for aligning contrastive learning models (CLIP), with human preferences using preference optimization techniques such as DPO and IPO. By formulating contrastive learning as a one-step MDP and fine-tuning CLIP with these techniques, the authors enhance the model robustness of CLIP against typographic attacks and mitigate biases, particularly around gender. Experimental results show improvement on multiple datasets.

### Strengths
Originality: This is the first work to improve contrastive learning models through Preference Optimization. The idea of leveraging true labels and typographic labels for preferences, instead of curating a separate preference set from human annotation, is novel and interesting.

Clarity: This paper is well-written and has very clear motivations, backgrounds, methods, and experiments. 

Significance: The topic of aligning human preferences in contrastive learning is impactful, as models like CLIP are now used widely, yet many undesirable behaviors such as gender biases still exist.

### Weaknesses
Significance: this paper relies on a preference dataset, which requires heavy annotations and the preference set will be very small compared to the training set of CLIP. Also, the preference would be very task-specific (e.g., typographic or gender), limiting the generalizability of the approach to new, unseen attacks or biases.

Quality: the inclusion of SVD makes it much slower to fine-tune on a larger scale. Also, the experiments focus on controlled, relatively smaller-scale datasets (the largest being ImageNet100), so the effectiveness of the approach is yet to be seen on diverse, complex large-scale datasets.

### Questions
Broadly speaking, for a general image-text task, e.g., VQA or retrieval, is there any guidance to design the preferences? The easiest way is following standard RLHF and curating a set with actual human preferences, but could the authors kindly suggest any other auxiliary information we can leverage?

### Soundness
3

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
The paper revisits well-known alignment techniques, such as Direct Preference Optimization (DPO) and Identity Preference Optimization (IPO), in the representation space learned by CLIP. The idea is simple yet effective: reformulate the policy $\pi$ in DPO and IPO by using the similarity scores between preference texts, $y_w$ (preferred) and $y_l$ (unpreferred), and the given adversarial image $x'$. The authors evaluate the proposed method on typographic attacks and show that it improves the CLIP model’s robustness to these attacks while preserving performance on the original datasets (without typographic attacks). To mitigate the overfitting issue of training large models on small datasets, the authors propose training a linear layer (parameterized by $W$) appended to the visual encoder, with both the pre-trained visual and text encoders frozen. Additionally, the authors propose applying SVD decomposition over $W$ as $W=U\Sigma^tV$, allowing the alignment magnitude to be controlled by $t\in\mathcal{R}$. The authors demonstrate that a learned alignment for gender bias can be effectively controlled by adjusting $t$.

### Strengths
1. The proposed method is simple yet effective.
2. The authors provide a new perspective on IPO and DPO concerning the representation space learned by CLIP.
3. The alignment controllability through $t$ is effective.
4. The background and motivation are well-organized.

### Weaknesses
1. Clarity needs improvement.
    * $\mathcal{L}_{pref}$ in (10) appears without a definition. In Corollary 3.2, it is assumed to be either the DPO loss or IPO loss, while the experiments further include the case of KTO loss. The lack of a clear, consistent definition for $\mathcal{L}_{pref}$ across the theoretical derivations and experimental evaluations introduces ambiguity. It is unclear how the different loss formulations (DPO, IPO, KTO) are unified under this single notation, particularly given their distinct weighting mechanisms and optimization objectives. This makes it difficult to understand the precise impact of each loss on the final results.
    * In (9), $\mathcal{I}_{ref}$ is frozen and has no trainable parameters, contributing solely to per-example weighting when substituted in (5), (6), and (7). It is recommended to clarify this in advance. The role of $\mathcal{I}_{ref}$ as a fixed weighting factor is not immediately obvious, and its impact on the overall optimization process needs to be explicitly stated. The reader is left to infer its function, which could lead to misinterpretations of the method's mechanics.
    * In Fig.1, $\mathcal{L}_{pref}$ is computed with the given triplet $(y_w, y_l, x’)$, where $x’$ is an adversarial image. The presence of multiple negative text representations, such as $\tau_1$, $\tau_2$, and $\tau_3$, is confusing without specifying either $y_w$ or $y_l$ as text inputs. The diagram suggests that multiple negative text representations are used in the calculation of $\mathcal{L}_{pref}$, but the relationship between these representations and the preferred ($y_w$) and dispreferred ($y_l$) text inputs is not clearly defined. It is unclear how these multiple negative samples contribute to the loss calculation and how they are selected or generated.
    * The overall loss in (13) is iterated over two different datasets, $D_{pref}$ and $D_{reg}$, simultaneously. Further explanation is needed on how the inputs $(y_w, y_l, x’)\in D_{pref}$ and $x\in D_{reg}$ are paired or sampled. The simultaneous use of two datasets, $D_{pref}$ and $D_{reg}$, introduces a potential source of confusion. The paper does not specify whether the samples from these datasets are paired or sampled independently, and how this affects the overall training process. The lack of clarity on the sampling strategy makes it difficult to understand the training dynamics.
    * The bottom row (differences) in Table 1 is confusing, and it cannot correctly demonstrate the trade-off between O (Original dataset) and T (Target dataset) for each variant of the proposed method. The reviewer recommends indicating the improvement or degradation alongside each accuracy as $\color{green}{(+1.0)}$ or $\color{red}{(-1.0)}$ relative to the base model, i.e., CLIP, for clarity. The presentation of results in Table 1 is not intuitive, particularly the bottom row showing differences. The lack of a clear baseline comparison makes it difficult to assess the relative performance of each method. The use of absolute differences does not effectively convey the trade-offs between performance on the original and target datasets.
2. Lack of a concrete conclusion over comparisons with baselines. The results in Table 1 deserve more discussion. Examples are listed below.
    * No method in Table 1 consistently outperforms the others. Is there a large domain gap between different datasets that prevents any method from generalizing well across all of them? The absence of a consistently superior method across all datasets raises questions about the generalizability of the proposed approach. It is unclear whether the observed performance variations are due to domain-specific characteristics or inherent limitations of the methods.
    * PAINT significantly outperforms the proposed method (including all variants: DPO, IPO, and KTO) on both O and T in the ImageNet* column. Is the constraint of a single trainable linear layer in the proposed method too restrictive? The substantial performance gap between PAINT and the proposed methods on the ImageNet* dataset suggests that the single linear layer constraint might be too restrictive, limiting the model's capacity to learn complex mappings. It is important to discuss the potential limitations of this design choice.
    * A comparison between different variants of the proposed method would be valuable. For example, what types of inputs are weighted more in different variants according to (10)? The paper lacks a detailed analysis of the differences between the DPO, IPO, and KTO variants. It is unclear how the different weighting schemes in equation (10) affect the learning process and which types of inputs are prioritized by each variant.

### Questions
The reviewer appreciates the well-organized background of DPO, IPO, and KTO, as well as the new perspective on these methods with CLIP. The paper focuses on providing new insights into preference optimization with CLIP. However, the most significant difference between DPO, IPO, and KTO—i.e., per-example weighting—is not discussed sufficiently in the paper (KTO might require further discussion). Additionally, the lack of a thorough comparison and the absence of clear distinctions in Table 1 together weaken the contribution. Therefore, the reviewer’s main questions are as follows:

1. What are the differences among the proposed method variants? Which types of inputs or datasets are weighted more or preferred for each variant? 
2. Could these variants be unified into a single method that outperforms the other baselines in Table 1?

The reviewer is open to reconsidering the rating if the authors could address these questions (including those in Weakness section).

Some typos:
* In Ln. 023, “Our experiments” appears incorrectly inserted.
* Table 2 lacks a reference. The possible related reference is in Ln. 1073 in the appendix.
* Several papers in the references are duplicated: Ln. 551 and Ln. 554; Ln. 559 and Ln. 562; Ln. 681 and Ln. 687; Ln. 750 and Ln. 754.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Preference Optimization for training the contrastive learning model CLIP, aiming to enhance the model's robustness against typographic attacks and mitigate gender biases. This approach aligns the model with human preferences. Experimental results on datasets such as ImageNet, Caltech101, and OxfordPets demonstrate the effectiveness of this method.

### Strengths
It is significant to explore aligning non-generative model with human preferences using Preference Optimization.

This paper is well-motivated.

### Weaknesses
See questions.

1. Could this method be applied to other tasks apart from enhancing robustness against typographic attacks and mitigating gender biases?
2. Could you provide the ablation study results for components $\mathcal{L}_{pref}$ and $\mathcal{L}_{reg}$ in the loss function?
3. I do not understand the image in the left part of Figure 1. What does the obscured dog in the left part of Figure 1 signify?
4. What is the role of section 3.4 in your method? Why is fine-tuning the model mentioned in Section 3.4?
5. Could you provide evidence for your claim “the overall matrix $W^TW$ remains close to the identity matrix” in Section3.4？
6. Section 3 does not clearly introduce the method. In the last part of Section 3, you should package and summarize your method to give readers an overall understanding.
7. In Table 1, although the accuracy on the typographic dataset has increased compared to other methods, the accuracy on the original dataset has generally decreased. Therefore, the method has harmed the pretrained knowledge.
8. Could you provide an analysis of the different performances of DPO, IPO, and KTO in your method in Section 4?
9. What is the relationship between Section 4.4.1 and Section 4.1? I am not sure about the role of Section 4.4.1.
10.  What is the meaning of transformation scaling t in Section 4?

### Questions
1. Could this method be applied to other tasks apart from enhancing robustness against typographic attacks and mitigating gender biases?
2. Could you provide the ablation study results for components $\mathcal{L}_{pref}$ and $\mathcal{L}_{reg}$ in the loss function?
3. I do not understand the image in the left part of Figure 1. What does the obscured dog in the left part of Figure 1 signify?
4. What is the role of section 3.4 in your method? Why is fine-tuning the model mentioned in Section 3.4?
5. Could you provide evidence for your claim “the overall matrix $W^TW$ remains close to the identity matrix” in Section3.4？ 
6. Section 3 does not clearly introduce the method. In the last part of Section 3, you should package and summarize your method to give readers an overall understanding.
7. In Table 1, although the accuracy on the typographic dataset has increased compared to other methods, the accuracy on the original dataset has generally decreased. Therefore, the method has harmed the pretrained knowledge.
8. Could you provide an analysis of the different performances of DPO, IPO, and KTO in your method in Section 4?
9. What is the relationship between Section 4.4.1 and Section 4.1? I am not sure about the role of Section 4.4.1.
10.  What is the meaning of transformation scaling t in Section 4?

### Soundness
2

### Presentation
1

### Contribution
2
