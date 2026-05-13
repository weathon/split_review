# Stealix: Model Stealing via Prompt Evolution

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Model stealing poses a significant security risk in machine learning by enabling attackers to replicate a black-box model without access to its training data, thus jeopardizing intellectual property and exposing sensitive information.
Recent methods that use pre-trained diffusion models for data synthesis improve efficiency and performance but rely heavily on manually crafted prompts, limiting automation and scalability, especially for attackers with little expertise.
To assess the risks posed by open-source pre-trained models, we propose a more realistic threat model that eliminates the need for prompt design skills or knowledge of class names.
In this context, we introduce Stealix, the first approach to perform model stealing without predefined prompts. Stealix uses two open-source pre-trained models to infer the victim model’s data distribution, and iteratively refines prompts through a genetic algorithm based on a proxy metric, progressively improving the precision and diversity of synthetic images.
Our experimental results demonstrate that Stealix significantly outperforms other methods, even those with access to class names or fine-grained prompts, while operating under the same query budget. These findings highlight the scalability of our approach and suggest that the risks posed by pre-trained generative models in model stealing may be greater than previously recognized.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Stealix, a new method to steal black-box classification models with the help of open-source models. Stealix iteratively (1) optimizes prompts so that they can produce images that are close to the images from the target class using the open-source text-to-image models, (2) evaluates the prompts with prompt consistency score defined as the fraction of the generated images that are labeled as the target class by the victim model, and (3) use the optimized prompts and their generated images to construct the image set for the next iteration. Finally, Stealix trains a classifier using the collected samples from the above process. Experiments on EuroSAT, PASCAL, CIFAR10, and DomainNet show that the proposed algorithm can train a surrogate that achieves better classification accuracy than prior approaches.

### Strengths
* The paper evaluates the proposed algorithm on 4 datasets, and the results look promising.

### Weaknesses
 * My main concern is that the description of the method sections is quite confusing. It makes it hard for me to fully understand every detail of the algorithms and judge their validity.

* The paper studies the setting where the class names of the victim are unknown to the attacker, while one image per class is available to the attacker. The paper claims that this setting is realistic, but that is questionable to me.

Please see the "Questions" section for more elaboration of these points.

### questions:
 ## The description of the method is confusing

*  Fitness value in Section 4.3 is defined for prompts, not images. I am confused about the description in Section 4.4 "The triplet with the highest fitness value (PC) in S t is selected as the elite, carried forward to the next generation S t+1to guide the production of improved triplets." The triplet by definition contains 3 images, with no prompts inside. How do you define the fitness value for the triplet?

* In Section 4.4 it says "Once the parent set is formed, two parents from S p are chosen sequentially, each split at a random point. The segments are recombined to form a new triplet, ensuring both parents contribute to the new triplet." The two parents are just two triplets, each with 3 images. What do you mean by "split at a random point" and "segments" for image triplets?

* Will the negative samples in line 25 of Algorithm 1 be used to train the surrogate model? If so, do you use their raw label from the victim model as the training label, or simply minimize their prediction prob of class c? This is not described in the paper.

* Are the prompts randomly initialized at every iteration t?

*  Line 4 of the algorithm says that the last two elements of the image triplets are randomly sampled from the sets X_c^+ and X_c^-. But these two sets are initialized as empty sets in Line 3. How do you draw samples from empty sets?

* Line 16 of Algorithm 1 claims that Line 17 and Line 18 consume the query budget. But the budget should have already been consumed in Line 15.

* What does "CIFAR10 is a standard classification dataset, where class names can be treated as ground truth for synthesizing relevant images." mean in Section 5.1? Do you mean that you use the class names in CIFAR10 experiments? If so, it contradicts the earlier claims in the paper.

* Line 460 says "retain the positively labeled images to form the transfer dataset for training the attacker model.". Could the authors elaborate on it more? I do not understand this sentence.

## The studied setting is questionable

The paper studies the setting where the class names of the victim are unknown to the attacker, while one image per class is available to the attacker, and claims that this setting is more realistic than prior work. However, I have some questions:

* **Regarding class names.** The paper claims that the assumption that the attacker does not know class names made in this paper is a significant advance compared to prior work. However, if the service provider of the classification model does not release the class names publicly, then this classification model has no use to the end users, as the users do not know what the returned classification results mean. All the classification services out there I am aware of have released the class information publicly. Could the authors provide an example of a real-world classification service where class name information is not known to end users?

* **Regarding one image per class.** The paper assumes that one image per class is available to the attacker. I would regard this as a huge constraint. I can think of real-world cases where getting those images is hard, such as medical image diagnosis systems. Moreover, assuming "one image per class is available, while class names are unavailable" is unnatural to me. If the attacker has access to one image per class, they can directly look at those images and might be able to have a good guess of the class name. Again, it would be more convincing if the authors could provide real-world examples where such assumptions hold.

* **Regarding the experiments.** The paper should list clearly which baseline methods require real images (and how many) and which do not. Without noting that, it is hard to say if the claimed benefit of Stealix over baseline methods comes from the availability of real images (one image per class) or the designed methodology.

Moreover, given the availability of one image per class, one simple approach is to augment the images with approaches such as DA-Fusion, and then train the surrogate model directly. If I understand it correctly, such a simple baseline is not considered in the paper.


## Other questions

* Line 16 of Algorithm 1: consumed -> consume

* Line 446 claims that "Since the attacker lacks access to victim data", but the paper assumes that one image per class is available to the attacker.

* The paper claims in multiple places that their generated data distribution aligns with that of the victim data, such as "By designing prompts to synthesize images that align with the victim data distribution, ..." in Section 4.1,  "we underscore the crucial role of aligning the distribution of generated data with that of the target model" in Section 7, and many more (just search "align" and you will find all the places). Note that "align the distribution" has a mathematical implication and it can mislead the readers to think that you are minimizing d(p_victim, p_synthetic), where p_real and p_synthetic are the distributions of victim data and synthetic data, for some distance metric d. Obviously, the proposed approach is not doing that (or at least, this claim is not quantitatively evaluated and justified). I would suggest the authors to rephrase these claims. 

### Questions
## The description of the method is confusing

*  Fitness value in Section 4.3 is defined for prompts, not images. I am confused about the description in Section 4.4 "The triplet with the highest fitness value (PC) in S t is selected as the elite, carried forward to the next generation S t+1to guide the production of improved triplets." The triplet by definition contains 3 images, with no prompts inside. How do you define the fitness value for the triplet?

* In Section 4.4 it says "Once the parent set is formed, two parents from S p are chosen sequentially, each split at a random point. The segments are recombined to form a new triplet, ensuring both parents contribute to the new triplet." The two parents are just two triplets, each with 3 images. What do you mean by "split at a random point" and "segments" for image triplets?

* Will the negative samples in line 25 of Algorithm 1 be used to train the surrogate model? If so, do you use their raw label from the victim model as the training label, or simply minimize their prediction prob of class c? This is not described in the paper.

* Are the prompts randomly initialized at every iteration t?

*  Line 4 of the algorithm says that the last two elements of the image triplets are randomly sampled from the sets X_c^+ and X_c^-. But these two sets are initialized as empty sets in Line 3. How do you draw samples from empty sets?

* Line 16 of Algorithm 1 claims that Line 17 and Line 18 consume the query budget. But the budget should have already been consumed in Line 15.

* What does "CIFAR10 is a standard classification dataset, where class names can be treated as ground truth for synthesizing relevant images." mean in Section 5.1? Do you mean that you use the class names in CIFAR10 experiments? If so, it contradicts the earlier claims in the paper.

* Line 460 says "retain the positively labeled images to form the transfer dataset for training the attacker model.". Could the authors elaborate on it more? I do not understand this sentence.

## The studied setting is questionable

The paper studies the setting where the class names of the victim are unknown to the attacker, while one image per class is available to the attacker, and claims that this setting is more realistic than prior work. However, I have some questions:

* **Regarding class names.** The paper claims that the assumption that the attacker does not know class names made in this paper is a significant advance compared to prior work. However, if the service provider of the classification model does not release the class names publicly, then this classification model has no use to the end users, as the users do not know what the returned classification results mean. All the classification services out there I am aware of have released the class information publicly. Could the authors provide an example of a real-world classification service where class name information is not known to end users?

* **Regarding one image per class.** The paper assumes that one image per class is available to the attacker. I would regard this as a huge constraint. I can think of real-world cases where getting those images is hard, such as medical image diagnosis systems. Moreover, assuming "one image per class is available, while class names are unavailable" is unnatural to me. If the attacker has access to one image per class, they can directly look at those images and might be able to have a good guess of the class name. Again, it would be more convincing if the authors could provide real-world examples where such assumptions hold.

* **Regarding the experiments.** The paper should list clearly which baseline methods require real images (and how many) and which do not. Without noting that, it is hard to say if the claimed benefit of Stealix over baseline methods comes from the availability of real images (one image per class) or the designed methodology.

Moreover, given the availability of one image per class, one simple approach is to augment the images with approaches such as DA-Fusion, and then train the surrogate model directly. If I understand it correctly, such a simple baseline is not considered in the paper.


## Other questions

* Line 16 of Algorithm 1: consumed -> consume

* Line 446 claims that "Since the attacker lacks access to victim data", but the paper assumes that one image per class is available to the attacker.

* The paper claims in multiple places that their generated data distribution aligns with that of the victim data, such as "By designing prompts to synthesize images that align with the victim data distribution, ..." in Section 4.1,  "we underscore the crucial role of aligning the distribution of generated data with that of the target model" in Section 7, and many more (just search "align" and you will find all the places). Note that "align the distribution" has a mathematical implication and it can mislead the readers to think that you are minimizing d(p_victim, p_synthetic), where p_real and p_synthetic are the distributions of victim data and synthetic data, for some distance metric d. Obviously, the proposed approach is not doing that (or at least, this claim is not quantitatively evaluated and justified). I would suggest the authors to rephrase these claims. 

------
Given all these concerns, I have to give a rejection. If I missed anything, please correct me in the rebuttal and I will be happy to revisit the score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Stealix, a novel approach for model stealing that operates without requiring predefined prompts. The focus of the research is to expose the risk posed by pre-trained generative models in stealing proprietary machine learning models. Stealix employs two open-source pre-trained models and a genetic algorithm to iteratively refine prompts and generate synthetic images that align with the victim model’s data distribution. This enables attackers to replicate the victim model’s functionality using significantly fewer queries, even without expertise in prompt design. The approach highlights vulnerabilities in using pre-trained generative models for tasks like image synthesis, especially when coupled with black-box models available via public APIs.

### Strengths
1. Introduction of a novel threat model: The paper proposes a novel realistic threat model that deepens our understanding of the risks associated with pre-trained generative models.
   
2. Well-written and clear exposition: The writing is clear, making the technical details accessible. The paper explains its methodology and results effectively, allowing the reader to follow the progression of the experiments and findings.

3. Strong performance: The experimental results show that Stealix significantly outperforms previous methods in terms of attack model accuracy, even with a low query budget.

### Weaknesses
1. Prompt Refinement as the major factor in performance improvement:  In comparing the results from Table 5 with those from other methods in Table 1, it appears that the main contributor to Stealix’s performance improvement is the Prompt Refinement process. However, this refinement approach seems quite similar to that proposed by Wen et al. (2024). The paper does not clearly highlight the unique advantages of Stealix's refinement method compared to the existing technique. Furthermore, Stealix utilizes the same models (OpenCLIP-ViT/H and Stable Diffusion v2) as Wen et al. (2024) for their experiments, raising the question of what specifically distinguishes Stealix.

2. Lack of details on t in generating S: The paper could benefit from a more detailed explanation of how t is set or updated during the generation of S. For instance, in Algorithm 1, t is updated throughout the process, but it is not clear how this is done in the experiments. Providing more detail on this parameter would help clarify the methodology.

3. Missing experiments on Prompt length (L): The paper does not provide experimental results on the impact of different prompt lengths (L). A more detailed analysis of how the prompt length affects performance could improve the evaluation of the method.

4. Lack of time comparisons: The Stealix method appears to be time-consuming. Providing a report on the computational time required for Stealix compared to other methods would aid in understanding its practical applicability. In Appendix A, line 662, the authors mention "to save optimization time," but a more detailed explanation of the actual time saved or required would be beneficial. This is an essential metric for evaluating whether the proposed threat model is feasible in real-world scenarios and whether it should be prioritized in risk management.

### Questions
1. What distinguishes Stealix's Prompt Refinement from Wen et al. (2024)'s approach?: The performance improvement seems to come primarily from Prompt Refinement, but the method appears very similar to Wen et al.'s. Could you clarify what specific aspect of Stealix leads to its superior performance?

2. Could you explain in more detail what is meant by "one-shot setup" in the Method section, lines 214-215? Does the attacker need to know at least one class from the victim model, or can it work without any class information? Additionally, what are the implications of this one-shot setup on the method's practicality, and how does it compare to other approaches in terms of required prior knowledge?

3. Source code not available: The absence of source code makes it difficult to reproduce the results and assess the practicality of the method. Sharing the code would be beneficial for further verification and application.

Additionally, I would appreciate responses to the above weaknesses points.

[Reference] Yuxin Wen, Neel Jain, John Kirchenbauer, Micah Goldblum, Jonas Geiping, and Tom Goldstein. Hard prompts made easy: Gradient-based discrete optimization for prompt tuning and discovery. In Advances in Neural Information Processing Systems (NeurIPS), 2024.

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
3

### Summary
The authors propose a realistic threat model where the attacker has no access to prompts or class information from the victim model. Specifically, they introduce a novel model-stealing approach, Stealix, which leverages the CLIP model to automatically generate prompts optimized through contrastive learning. This method removes the need for human-crafted prompts.

### Strengths
The paper is well-written and easy to follow.
It is interesting that the design of the next triplet considers both effectiveness and diversity.
The extensive experiments and accompanying discussion provide valuable insights.

### Weaknesses
1. The paper employs two large foundation models to steal knowledge from a relatively small victim model, specifically ResNet-34. This approach, however, may not seem practical. If the attacker’s objective is to steal general knowledge from a smaller model, the large foundation models already possess advanced capabilities that might surpass what a smaller model like ResNet-34 could offer. Conversely, if the goal is to steal domain-specific knowledge, such as that learned in medical imaging, these large foundation models may also lack such specialized knowledge, potentially leading to lower quality generated images and reduced accuracy due to the limitations of CLIP and the diffusion model (DM). Could the authors provide a more practical scenario where their method would be beneficial? Additionally, it would be helpful to know if it’s feasible to extract knowledge from a larger model, as these models are more expensive to train and may use private datasets, making the task more realistic.

2. Although the method claims not to rely on class names or training data distribution, it does require at least one image per class. This requirement may actually provide more information than a class name alone. For instance, selecting an image per class implies prior knowledge of each category, and images include more detailed information than a simple class label. Given this, it seems that the primary novelty over previous work lies in using CLIP to automatically generate prompts rather than manually crafting them.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel method for model stealing by leveraging off-the-shelf diffusion models to synthesize query images. More specifically, the proposed method uses prompt optimization to automatically craft reasonable prompts and genetic optimization to increase the diversity of the prompts and their corresponding image generations. Prompt optimization is done using a hard prompt optimization by maximizing the CLIP similarity between the generated image and the predicted class by the target model (if the prediction is correct) or minimizing the similarity if the target model's prediction is wrong. The genetic optimization relies on image triplets consisting of a base sample of the target class, a positive, correctly classified synthetic image, and an incorrectly classified image. By iteratively optimizing these image triplets using prompt consistency as a metric, the method creates a diverse set of images that are then used to train the surrogate model that imitates the victim model.

### Strengths
- The paper is clearly written and easy to follow. Notably, all hyperparameters and settings are explicitly described and stated, supporting reproducibility. I enjoyed reading this paper.
- Using genetic optimization in combination with prompt optimization to craft a diverse set of attack samples is a clever attack method compared to hand-crafted prompts. Removing the human factor from the pipeline speeds up the process and increases the parallelization of the attack.
- The results are convincing, clearly beating existing baselines by a significant margin. Furthermore, multiple ablation and sensitivity studies are conducted, including multiple datasets, architectures, correlation analyses, and an image diversity analysis. Each of these analyses offers interesting insights.

### Weaknesses
 - The method primarily relies on existing work on genetic optimization and hard prompt optimization. While combining these methods is novel in the domain of model stealing, the individual parts already exist in literature. I do not find this compellingly flawed but I want to mention that the paper proposes no novel, technical contributions besides combining existing methods.
- The method overview in 4.1 does not seem exact. Why should the attack be interested in minimizing the cross-entropy loss between the victim model and the surrogate model under label-only access? From my understanding of the paper, the attack goal is to replicate the target model's label prediction performance and not to imitate the distribution of the confidence scores (which the cross-entropy loss measures). I think a correct target would be to align the label predictions, i.e., the predicted labels by the victim and surrogate models should match, not their prediction score distribution, which also aligns with the metrics used in Table 1.
- The experiments seem to be conducted only once per setup. For stable results, each experiment should be repeated at least three times with different seeds to eliminate influences due to randomness in the training/attack process.

### Questions
- Is there an explanation why the knowledge distillation accuracy in Table 1 is, in some cases, substantially lower than the victim model's test accuracy? I understand that vanilla knowledge distillation has some drawbacks, but I expect the student model's accuracy to be better, for example, in the CIFAR10 case.
- How are the qualitative samples from Fig. 5 picked? Are they cherry-picked or randomly selected?

### Soundness
3

### Presentation
3

### Contribution
3
