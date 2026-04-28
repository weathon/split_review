# Mode-Aware Continual Learning for Conditional Generative Adversarial Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
The main challenge in continual learning for generative models is to effectively learn new target modes with limited samples while preserving previously learned ones. To this end, we introduce a new continual learning approach for conditional generative adversarial networks by leveraging a mode-affinity score specifically designed for generative modeling. First, the generator produces samples of existing modes for subsequent replay. The discriminator is then used to compute the mode similarity measure, which identifies a set of closest existing modes to the target. Subsequently, a label for the target mode is generated and given as a weighted average of the labels within this set. We extend the continual learning model by training it on the target data with the newly-generated label, while performing memory replay to mitigate the risk of catastrophic forgetting. Experimental results on benchmark datasets demonstrate the gains of our continual learning approach over the state-of-the-art methods, even when using fewer training samples.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper suggests a generative learning method using a conditional generative adversarial network (cGAN) for the continual learning framework. They introduce a new score metric named Discriminator-based Mode Affinity Score, to measure the similarity of the target image class with source classes. This score is obtained by comparing the approximated Hessian matrix of the discriminator in cGAN frameworks on the loss of generated source images given the source image and the target image.

### Strengths
Suggest a new method for generative continual learning method and achieve improved performance against the baselines.
The suggested score metric seems to pick similar source classes with the target class.

### Weaknesses
 - Overall, the motivation and presentation are weak. The need for continual learning for generative models and their own challenges beyond conventional continual learning scenarios and challenges are not well discussed, and this makes the reader feel that this work is a simple incremental work by transferring conditional generative adversarial networks on continual learning setting with simple repeats the well-known challenges - catastrophic forgetting - again.

- Limited investigation of 'modes'. The paper only assumes a mode is a class. However, this seems not realistic and outdated since recent generative models already have a surprising generalization and zero-shot ability on various styles/classes in a single model. Simple incremental learning in each 'class' means nothing these days.

- Similarly, tasks are too simple. Evaluation with MNIST/CIFAR and Flower dataset is a bit far from the recent generative model and/or continual learning trends. I recommend ImageNet/Coco + a, which can be better candidates. Additionally, baselines are also too old (most of them were published around three to four years ago). When we consider this venue for 2024, it is hard to confirm that the proposed idea and baselines are sufficiently strong compared to its counterparts/alternatives.

- No empirical comparison of the proposed metric. I fail to find the merits of the suggested score metric compared to other possible approaches to select similar source classes/modes with the target one, including FiD or other various types of metrics such as mutual information / KL or JS divergence metrics on their embeddings, etc. There are tons of techniques to meet the same purpose, but no comparison or demonstration to show the impact/strengths of the suggested score is provided.

### Questions
.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors tackle continual image generation, aiming to identify similar mode for target mode for accelerated learning while preventing catastrophic forgetting. They introduce the Discriminator-based Mode Affinity Score, utilizing the Hessian matrix of the discriminator loss w.r.t. images from each mode. This affinity score aids in comparing the target mode with existing ones, assigning a pseudo label to the target mode. The method leverages target data, labels, and replay data from the source to fine-tune GANs. Theoretically, the authors prove that the performance of existing modes remains unaffected upon integrating a new mode. Empirically, their method surpasses current techniques on CIFAR-10, CIFAR-100, and Oxford-flowers datasets, showcasing its efficacy.

### Strengths
1. The exploration of GANs within continual learning for image generation is a compelling research topic.

2. The authors introduce affinity scores derived from the Hessian matrix, which is new.

3. The authors demonstrate that their method outperforms baseline models by conducting experiments on 3 datasets.

### Weaknesses
1. The validity of the proposed affinity scores enhancing continual learning’s effectiveness remains unclear. Despite Section 3.2’s assertion that "our measure aligns more closely with human intuition and consistently demonstrates its reliability", the paper lacks empirical or theoretical analysis to substantiate this claim. The authors propose using the Hessian of the discriminator loss to compute a mode affinity score, but do not provide sufficient justification for why this specific measure is appropriate for quantifying mode similarity in the context of continual learning. It is not clear how the eigenvalues or eigenvectors of the Hessian matrix relate to the semantic similarity of the generated images. The paper would benefit from a more thorough explanation of the connection between the Hessian and the desired affinity measure, perhaps by showing that the proposed measure correlates with other established measures of mode similarity or by providing a theoretical analysis of the properties of the proposed measure.

2. The employment of a memory replay technique to prevent catastrophic forgetting is not novel, as it is contribution from existing work and thus does not contribute to the originality of this research. While the use of replay buffers is a common technique, the paper does not clearly articulate how the replay buffer is integrated with the proposed affinity score. Specifically, it is unclear how the replay data is selected, how the replay data is used during training, and whether the replay data is specific to the source mode or includes data from previous modes. The paper should provide more details on the replay mechanism and its interaction with the proposed affinity score to better understand its contribution.

3. Theorem 1 merely establishes that the integration of a new mode will not enhance the performance of existing modes, without providing insight into why the proposed method excels. Thus, Theorem 1 provides no positive roles for enhancing the soundness of this work. The theorem, as it stands, is a negative result and does not explain why the proposed approach is effective in mitigating catastrophic forgetting. The paper would benefit from a theoretical analysis that provides insight into the mechanism by which the proposed affinity score and replay buffer contribute to the preservation of performance on existing modes while learning new modes. A theoretical result that demonstrates a bound on the performance degradation of existing modes would be more useful.

4. The paper lacks a quantitative assessment of performance on the Oxford-flowers dataset, making it difficult to gauge the method's effectiveness in that context. The absence of quantitative results on the Oxford-flowers dataset makes it difficult to compare the performance of the proposed method with existing techniques. The paper should include quantitative metrics, such as FID or IS scores, to demonstrate the effectiveness of the proposed method on this dataset. Without these metrics, the claim of surpassing current techniques is not fully supported.

5. The textual quality and logical coherence of Section 4 are weak. It would be better to reorganize section 4, make it more clear and concise. The current structure of Section 4 makes it difficult to follow the experimental setup and results. The paper would benefit from a more structured presentation of the experiments, including a clear description of the experimental protocol, the hyperparameter settings, and the evaluation metrics. The results should be presented in a clear and concise manner, with appropriate tables and figures.

### Questions
1. two "between"s in "our proposed dMAS quantifies the Fisher Information distance between between the model weights" in Sec 3.2.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work tackles the task of continual learning in class-conditional GANs (cGANs). The method consists of two main contributions. In the first part, the authors propose a method to measure the affinity between the classes in a pretrained cGAN and a target class based on the Fisher Information distance. In the second part, the authors use the obtained affinity scores to form the target class embedding as the weighted sum of the most similar source classes. The authors evaluate their proposed method on different datasets in two setups: transfer learning and continual learning.

### Strengths
-- The paper is well-written.

-- The proposed method for measuring the affinity between classes is interesting and novel.

-- The experiments show the effectiveness and consistency  of the proposed affinity score in identifying the most similar classes

-- Based on the provided results, the incorporation of the proposed score in transfer and continual learning appears to be effective compared to the baselines.

### Weaknesses
 -- The idea of class-specific knowledge transfer in conditional GANs has been previously explored in cGANTransfer[1] by learning the class affinities. A discussion of the work and how it compares with the proposed method would improve the completeness of the paper. [2] is another relevant work that could be discussed in the paper.

-- To complete the experiments and to better show the advantage of their proposed affinity score, authors could include some comparison with other affinity metrics such as FID. It is not clear how the baseline "Sequential Fine-tuning (Zhai et al., 2019)" is using FID to determine class affinities. In my understanding, the referred baseline approaches lifelong learning with knowledge distillation, without incorporating class similarities. A more detailed explanation of how FID is used in this baseline is needed. On a related note, the term "Sequential Fine-tuning" has been cited inconsistently throughout the paper, sometimes by (Wang et al., 2018) and sometimes by (Zhai et al., 2019). In my opinion, the term Sequential Fine-tuning describes the method in (Wang et al., 2018) better than the one in (Zhai et al., 2019).

-- Although the proposed method has been evaluated on several datasets, it would be better if more complex datasets such as Imagenet were included in the experiments. The continual learning setup uses only two classes as targets in each trial. For a more realistic setup, more target classes might be needed in the evaluations.



### Questions
-- Is the target embedding obtained using the class affinity fixed in the proposed method, or is it also fine-tuned with the rest of the generator? what is the reason for such a choice?

-- In section 4.1, the authors mention they initialize the source cGAN randomly. By initialization, do they mean weight initialization or the classes used as the source modes?

-- How does the method compare to the baselines, if there are no semantically similar classes in the source model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies an interesting topic in continual learning, aiming to train a conditional GAN without forgetting. The main idea of this work is to develop a new discriminator-based mode-affinity measure that can evaluate the similarity between modes. The experiment results on several datasets have demonstrated that the proposed approach achieves promising results.

### Strengths
1. The introduction section of this paper is written well.
2. The proposed approach is reasonable.

### Weaknesses
1. The main contribution in this paper is very small. This work just proposes a discriminator-based mode-affinity measure, which is a natural choice. The novelty of this measure is not clearly justified, and it's unclear why existing methods are insufficient.
2. In the introduction section, the primary motivation of introducing Discriminator-based Mode Affinity Score is lacking. Why do we need such an approach? What are the limitations of current mode affinity measures that this new measure addresses? The paper needs to clearly articulate the gap it fills.
3. The notations X_a in this paper are not clear to me. These notations should be bold because they are matrixes. It is unclear if X_a represents a single data point or a batch of data points. The paper should clarify the dimensionality and structure of X_a.
4. This paper employs the conditional GAN. However, I do not find the actual loss functions as well as the model in the text. The specific architecture of the generator and discriminator, as well as the exact form of the conditional loss function, are missing. This makes it difficult to reproduce the results.
5. In algorithm 2, the definition of various models, such as G_θ is not defined in the paper. The whole methodology section is hard to follow since it misses some important information. The paper needs to explicitly define all symbols and models used in the algorithms.
6. The proposed approach relies on class and task information, which can not be used in a more realistic continual learning setting such as unsupervised learning. The paper should discuss the limitations of the proposed approach in scenarios where task or class labels are not available.
7. Why use the conditional GAN instead of other models such as WGAN? The paper should justify the choice of conditional GAN over other generative models, especially in the context of continual learning.
8. In theorem 1, some notations are not defined or explained. For example, what is "trace" in Eq.1. What is $|| ||_F$ in Eq.1? The paper should define all mathematical notations used in the theorems and equations.
9. To avoid forgetting, this work employs the generative replay mechanism, which has been done in a wide range of works. The paper should clearly state that the replay mechanism is not a novel contribution and should focus on the novelty of the mode-affinity measure.
10. The whole algorithm 1 is unclear to me because a lot of definitions are not explained. For example, $S$ in algorithm 1 is not described in the text. The paper should provide a clear and detailed explanation of all the steps and variables in the algorithm.
11. The main objective function and the models are not defined and described in the text, which makes it difficult for the readers to understand the main contribution. The paper needs to explicitly state the objective function and the model architectures used.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
