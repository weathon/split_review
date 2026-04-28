# GenVP: Generating Visual Puzzles with Contrastive Hierarchical VAEs

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Raven’s Progressive Matrices (RPMs) is an established benchmark to examine
the ability to perform high-level abstract visual reasoning (AVR). Despite the current success of algorithms that solve this task, humans can generalize beyond a given puzzle and create new puzzles given a set of rules, whereas machines remain locked in solving a fixed puzzle from a curated choice list. We propose Generative Visual Puzzles (GenVP), a framework to model the entire RPM generation process, a substantially more challenging task. Our model’s capability spans from generating multiple solutions for one specific problem prompt to creating complete new puzzles out of the desired set of rules. Experiments on five different datasets indicate that GenVP achieves state-of-the-art (SOTA) performance both in puzzle-solving accuracy and out-of-distribution (OOD) generalization in 22 out
of 24 OOD scenarios. Further, compared to SOTA generative approaches, which struggle to solve RPMs when the feasible solution space increases, GenVP efficiently generalizes to these challenging scenarios. Moreover, our model demonstrates the ability to produce a wide range of complete RPMs given a set of abstract rules by effectively capturing the relationships between abstract rules and visual object properties.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Briefly, this paper presents a framework to solve and create complete new puzzles out of the desired set of rules for Raven’s Progressive Matrices (RPM) by introducing the contrastive learning scheme (i.e., cross-puzzle and cross-candidate contrastive loss) and MoE mechanism for puzzle rule prediction. The experimental results are strong.

### Strengths
+ The paper is well-written and easy to follow. The idea of the proposed method is quite interesting.
+ Extensive and comprehensive experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
1) The technical novelty of the proposed method seems to be marginal since the authors directly employ the existing techniques (e.g., contrastive learning scheme and MoE). More detailed discussions and analyses are required to demonstrate the contribution of the proposed method. Specifically, the paper lacks a clear explanation of how the specific combination of contrastive learning and MoE contributes to solving RPM puzzles beyond what these techniques achieve individually. The use of contrastive learning, while effective for representation learning, is not novel in itself, and the paper does not sufficiently explain why this particular implementation is crucial for the task. Similarly, the MoE mechanism, while powerful, needs more justification in the context of RPMs. The paper should elaborate on the specific advantages of using MoE over simpler ensembling techniques or even a single, well-trained model.

2) More ablation studies are required to demonstrate the contribution of the main component of the proposed method in the main paper. For instance, the mentioned rule estimators for the RPM-Level inference, the performance gain of the introduced MoE mechanism, and the contrastive learning scheme. The paper does not provide sufficient analysis on how each rule estimator contributes to the overall performance. It is unclear which rule estimators are most important and why. Furthermore, the performance gain from the MoE mechanism is not clearly quantified against simpler alternatives. The impact of the contrastive learning scheme should be isolated and analyzed, showing how it improves the model's ability to solve RPM puzzles compared to a model trained without it. The ablation study should include a breakdown of the performance of each rule estimator, both individually and in combination with others, to understand their respective roles.

### Questions
Please refer to the Weaknesses section.

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
The authors proposed a novel deep latent variable model GenVP for RPM problems. GenVP extracts image features and then uses these features to form relevant and irrelevant representations for later inference. The proposed MoE estimator can infer categories of attribute-level rules used to generate RPM panels. The proposed model was evaluated through experiments on RAVEN/I-RAVEN, VAD and PGM, showing better performance than other generative-based methods.

### Strengths
1.	This paper is generally well-written and the main idea is easy to follow. The authors proposed a new generative model GenVP to encode rule-related information. It will be more useful to construct interpretable machine learning algorithms for abstract visual reasoning.
2.	Compared to the previous generative approach RAISE, GenVP is unconditional and therefore can generate novel RPMs without given context.
3.	The decomposition of relevant and irrelevant representations improves the robustness of GenVP when there is too much noise or resolution in puzzles.
4.	The authors showed that their GenVP can perform better than previous generative methods.

### Weaknesses
1.	Many important factors in GenVP should be carefully tuned. For example, and in the sampling process should be carefully handcrafted. The specific impact of the various beta parameters in the ELBO loss function is not clear, and the sensitivity of the model to these parameters needs further investigation. The sampling process, while based on a VAE framework, could be more thoroughly described, particularly how the mean and variance are predicted and how this affects the quality of generated samples. The lack of detail makes it difficult to assess the robustness of the sampling process.
2.	The proposed model seems to rely heavily on ground truth rule annotations. GenVP leverages rule annotations of each RPM sample in the training process. This limits the applicability of this method to unlabelled visual reasoning datasets. The authors should investigate why the models cannot learn the rules well without annotations. The reliance on explicit rule annotations during training raises concerns about the model's ability to generalize to scenarios where such annotations are not available. It is unclear how the model would perform on datasets with novel rules or attribute combinations not seen during training. The authors should explore methods to reduce this dependency, such as self-supervised or weakly supervised learning techniques.
3.	Using VAE-based generative solvers or contrastive loss is not novel in RPMs. Is there any novel technical or insightful design in GenVP compared to previous approaches. The use of VAEs and contrastive loss, while effective, is not a novel approach in the context of RPM solvers. The paper needs to clearly articulate the unique contributions of GenVP beyond the combination of these existing techniques. It is unclear what specific architectural or algorithmic innovations are present that differentiate GenVP from prior work using similar methods.

### Questions
1.	Could the authors explain the process of answer selection in detail?
2.	Will the selection of hyperparameters heavily influence the performance of GenVP? The RPM datasets contain just small sets of object attributes and rules, and the selection of hyperparameters can probably matter a lot in this case. The authors should discuss this as well.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a latent variable model named GenVP for RPM-style visual puzzles. GenVP is trained from RPM images and the corresponding categorical rule matrices by inferring hierarchical Gaussian latent representations, which can be decoded back to images, through an ELBO loss and a global-local masked contrastive loss. GenVP learns a set of underlying rules controlling how an RPM is composed. The experiment results show that GenVP outperforms SOTA generative approaches in both out-of-distribution generalization and large solution space scenarios.

### Strengths
1.	This paper defines delicate generation and inference models for RPMs, and the details are easy to follow. The choice and hierarchy of latent variables are reasonable, e.g., decomposing relevant and irrelevant attributes from an image.
2.	Experiments are comprehensive, with a focus on OOD configurations and some challenging datasets. According to the testing and visualization results, the proposed GenVP outperforms SOTA generative approaches.

### Weaknesses
1.	Limitation of the application scenarios. The design of the generative model seems rather tailored to RPM problems. This focuses on a very specific problem hence its significance might be limited. It is unclear how to apply GenVP in other abstract visual reasoning tasks.
2.	Requirement of annotation of rules. Can a GenVP be trained without supervision of rules? For human beings, one does not require to learn rules through supervision, the rules can be discovered by the test subject.
3.	The interpretability of answer selection. GenVP infers MoE rule matrix predictions for candidates and chooses the one with the largest set of active rules as the final answer. Why not select answers by comparing the generated answers to candidates? Maybe it is a more human-like way of answer selection.

### Questions
1.	In the graphical model of GenVP in Figure 1, $R$ is a shaded circle which means observation; however, from the context of model description it seems that $R$ is inferred. 
2.	Could the authors provide results on any other visual puzzles or abstract visual reasoning tasks? My main concern is whether GenVP can be applied to more realistic reasoning problems with a unspecific rule set.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article introduces a new framework called Generative Visual Puzzles (GenVP), which aims to simulate the entire generation process of Raven's Progressive Matrices (RPMs). It not only performs excellently in solving existing puzzles but also demonstrates strong capabilities in creating new puzzles and generalizing to new, unseen puzzle scenarios.

### Strengths
1.The authors propose GenVP, a novel approach for solving and creating visual puzzles.
2.The authors design a new cross-puzzle and cross-candidate contrastive loss for AVR. The proposed GenVP is robust to noise.
3.The authors conducted extensive experiments to demonstrate the superior performance of the GenVP method.
4.GenVP can generate a large number of new puzzles beyond the original source dataset.

### Weaknesses
1.Although the author's experiments are very detailed, the rules of the puzzle generation task in this article are relatively simple, and the task's search space is relatively small.
2.According to Figure 2, it can be seen that the image quality of the puzzles generated by this method is still not good enough; the edges of the puzzle elements are relatively blurry, and there are artifacts.

### Questions
1.Although the author has done a lot of mathematical derivations, I am still somewhat confused about the process of generating puzzles. Could the author please describe in more detail how to generate puzzles from the rules?
2.It seems that the author did not compare the visualization of image generation with previous methods. Is it because previous methods couldn't generate such images?
I will consider to raise my score according to the rebuttal and discussion with  other reviewers

### Soundness
3

### Presentation
3

### Contribution
3
