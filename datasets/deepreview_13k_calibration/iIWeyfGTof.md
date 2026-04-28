# Does equivariance matter at scale?

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Given large data sets and sufficient compute, is it beneficial to design neural architectures for the structure and symmetries of each problem? Or is it more efficient to learn them from data? We study empirically how equivariant and non-equivariant networks scale with compute and training samples. Focusing on a benchmark problem of rigid-body interactions and on general-purpose transformer architectures, we perform a series of experiments, varying the model size, training steps, and dataset size. We find evidence for three conclusions. First, equivariance improves data efficiency, but training non-equivariant models with data augmentation can close this gap given sufficient epochs. Second, scaling with compute follows a power law, with equivariant models outperforming non-equivariant ones at each tested compute budget. Finally, the optimal allocation of a compute budget onto model size and training duration differs between equivariant and non-equivariant models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
It is well known in the literature that equivariance improves sample efficiency and generalization by adding geometric inductive bias to models and encouraging parameter sharing. This makes equivariant models appealing for settings with low data and where there is a constraint on the number of parameters. However, equivariant networks are more expensive to scale, and it is not clear whether there is any advantage to having this inductive bias when a lot of data is available. Recent papers show that non-equivariant models might be a better choice at scale. This paper provides a systematic approach to understanding the scaling behavior of equivariant models and compares them with non-equivariant ones. The authors conclude that non-equivariant models with data augmentation can close the performance gap given enough data and training. However, they also found that, for a fixed compute budget (in nominal FLOPs), equivariant models are better than non-equivariant ones.

### Strengths
1. The paper is generally well written and tries to address a timely problem. Whether equivariance matters at scale has been under a lot of attention in the community, with arguments for and against equivariant models.
2. This paper is technically sound, with the authors explicitly making their assumptions clear wherever necessary.
3. The experiments with the 3D rigid n-body dynamics dataset are well designed and thoughtful.
4. I appreciate the authors pointing out the limitations of this work in Section 5, in particular, providing the throughput of nominal FLOPs per training wall clock time of different equivariant and non-equivariant models in Figure 6.

### Weaknesses
1. One major concern with this paper is that the authors use nominal FLOPs as the training compute budget to draw a conclusion in line 85/86: “Equivariant transformers are also more compute-efficient, and this advantage persists across all compute budgets studied.” However, the authors themselves point out later that nominal FLOPs do not reflect the real-world run-time and training cost, as equivariant models have poor GPU utilization. I think it’ll be fair to provide an equivalent of Fig. 1 that uses the real training cost in GPU-hours. This can be better for practitioners to draw conclusions on which model to go for with limited compute budget. I understand the authors' point of using nominal FLOPs when analyzing each model separately. However, while recommending which model leads to better loss given a fixed compute budget, the authors should consider GPU hours/wall clock time, which is more practical than nominal FLOPs.
2. When drawing conclusions on whether to use equivariant vs. non-equivariant models on a fixed compute budget, the paper doesn’t discuss the inference speed benefits of non-equivariant models over equivariant ones. Any inference wall clock comparisons of equivariant models with non-equivariant ones would shed more insights on which model to go for given a fixed latency budget. For example, if a bigger non-equivariant model with lower loss takes the same wall clock time for inference (with better GPU utilization), then it might make more sense to go for that model.
3. I think “Overall, our findings hint that strong inductive biases …… large datasets and large compute budgets.” is a very strong claim given that the authors only tested their hypothesis in one synthetic 3D rigid body interaction dataset. I understand that the reason for choosing the dataset was to be able to generate as much data as you want cheaply. I wonder why the authors didn’t consider other domains like images, where a lot of data, models (both equivariant and non-equivariant), and self-supervised learning techniques are available. It would have made the paper stronger to validate their point for both E2 and E3 equivariant models. I think the current experimental setup is too simplistic to make general conclusions on whether equivariance matters at scale or not. The authors should be more transparent about the limitations of this study early on in the paper. The hypothesis the authors tested in this paper is more like “Does E3 equivariance matter at scale for 3D n-body dynamics?”
4. I am not sure if the authors are familiar with the body of work that tries to solve the inefficiencies of equivariant networks by frame averaging or learning canonicalizations of the data. As the purpose of that line of work is mainly to scale equivariance to large models, I think a discussion of that in the related work would be nice.

### Questions
1. Can the authors explain the hierarchical attention part better? Do you assume that you know which tokens belong to which object to design the mask? If so, then isn’t that adding another dimension of problem-specific inductive bias to the architecture? I think this makes things more complicated to generalize the conclusions to any equivariant vs. non-equivariant model.
2. Can the authors explain line 262: “The lower end of this scan corresponds to training for …. the upper end of this scan.”? How many tokens were there for each experiment, and how many times each token was shown—that is, epoch? Maybe making a table of all these experiments in the Appendix would make things easier to understand for readers.

### Soundness
3

### Presentation
3

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
The paper discusses scaling laws for equivariant architecture, particularly $E(3)$-equivariant transformer on rigid-body modelling problem. The experiments resulted in three empirical findings - data efficiency of equivariant models, compute scaling follows power-law with equivariant model favoured over non-equivariant one at each compute budget and different trade-offs between model size and training tokens (duration) for each model.

### Strengths
- The paper is well-motivated and clearly written. Conducting such a study is crucial, so the paper is very timely, and running the experiments on a large scale to draw insights is appreciated.
- The ablations over different aspects of scaling are exhaustive, as the authors consider scaling model size, training tokens, and compute.
- Several (design) choices are described in detail to help the readers understand the decisions behind the experiments.

### Weaknesses
- The primary concern is the limited scope of tasks (benchmarks) and equivariant models:
  - Are these insights going to generalize across all tasks? For instance, the authors point out that one of the motivations for the study is the recent high-profile models' (for protein folding and conformer generation) choice of non-equivariant models -  why didn't the authors consider equivariant counterparts of these models and these tasks?
  - Will these insights generalize to other kinds of equivariant models instead of the $E(3)$ equivariant transformer designed as in GATr, such as a stack of $E(3)$ equivariant layers? Multiple experiments have shown that the choice of equivariant architecture can change the training time.
  - Will there be any differences in the observations for discrete groups, such as $C_n$ or $D_n$, instead of continuous groups, especially for test performance with training data?

- Availability of data/compute budgets:
  - The paper isn't conclusive for seemingly infinite data and large compute (most present-day experiments); instead, it states that for finite compute budgets up to a specific limit ($10^{19}$ FLOPs), the equivariant model outperforms the non-equivariant model (Fig 1). Can the authors share if the two lines are coming close in Fig 1? And given the simplicity of non-equivariant models (and, generally, ease of training), what choice is favourable in the above-described setting?

- Unknown symmetries:
  - Consider that the exact symmetry (or underlying group of transformations) is unknown for a particular task, or some invariant transformations and their effects on the task are known. Is it better to use an equivariant model with a larger group (encompassing these transformations) or a non-equivariant model with these transformation augmentation?

### Questions
- Are there comments on the quality of data? For instance, if the data is noisy (as a random example, say, images with random noise), is constraining models to the space of equivariant models a good idea?
- Can the authors reference papers (or perform experiments) that support the statement, "... a small model trained on a few samples should perform poorly, while a large model trained on many samples should score orders of magnitude better."?
- What differences would you see in the conclusions if you consider "not-permutation equivariant" models?
- The authors decide on some modifications to the architectures, namely, hierarchical attention and object rigidity. Are these modifications equivalently beneficial for both models (please provide some empirical evidence)?
- Can the optimization techniques affect the outcomes? For instance, how susceptible are the results to different learning rate scheduling and optimizers? Can you also detail the early stopping criterion?

### Soundness
2

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
The paper studies the scaling properties of an $E(3)$-equivariant transformer architecture with respect to dataset size, parameter size, and computation budget for a rigid body problem. Laying the experimental foundation on the scaling laws developed for LLMs, authors find that the equivariant architecture is both data- and compute-efficient, and the parameter-size requirements for equivariant and non-equivariant architectures are different.

### Strengths
- With the tendency towards the use of large and pre-trained models for various tasks, the importance of problem-specific information, such as symmetry and equivariance, has been losing attention. A structured and well-setup experimental setting that sheds light on how incorporating symmetries into the architecture or training process can improve the generalization, performance, etc in various scenarios is much needed. The authors implement a carefully designed setup that partially reveals the characteristics of such architectures. 

- The experimental setting covers a reasonable range of different extremes in terms of data availability, compute budget and parameter size.

### Weaknesses
1. While the experimental setup is carefully designed, the experiments are limited to only one architecture and one problem. Equivariances and symmetries are present in a wide range of problems and go beyond the studied $E(3)$ group. For instance, Lie symmetries have recently been utilized for training Neural Operators; See [1].

2. Also, in many domains, transformers are still not the staple architecture. Focusing on only one architecture class while trying to answer the broader question of the "effectiveness of equivariant networks" is limiting. For instance, with PDEs again, Fourier Neural Operators and Convolutional networks are still preferred over transformers (and there exist many equivariant convolutional architectures that can be studied, e.g. [2]). 

3. Some parts of the paper regarding the scaling laws (section 3.3) are not very clear and hard to follow (See question 1). Also, some of the results in Section 4.1 are hard to interpret (see question 2)

4. In the end, while I appreciate the authors' efforts in designing a well-structured experimental setup, I believe the paper is severely limited in terms of experiments and generalizing to other problems.

[1] Brandstetter, Johannes, Max Welling, and Daniel E. Worrall. "Lie point symmetry data augmentation for neural PDE solvers." International Conference on Machine Learning. PMLR, 2022.

[2] Finzi, Marc, et al. "Generalizing convolutional neural networks for equivariance to lie groups on arbitrary continuous data." International Conference on Machine Learning. PMLR, 2020.

### Questions
1. In lines 256 and 295, $D$ is said to be the training length or duration. However, in line 268, $D$ is the number of training tokens. I'd appreciate a clarification on this matter.

2. I am not sure what the takeaway from some of the presented results in section 4.1 is. More specifically, how should I interpret the coefficients listed in Table 2?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to study experimentally the potential benefits of equivariance in different dataset size and compute availability regimes. The study compares an equivariant transformer-type architecture to non-equivariant models with and without data augmentation on a synthetic task of rigid body dynamics. The highlighted findings are an improvement in data efficiency for equivariant models with data augmentation allowing non-equivariant models to come close in performance. It is also argued that given a fix compute budget, equivariant models outperform non-equivariant ones. Finally, power law models for optimal allocation of FLOPs (with model size and training time as variables) are fit, and it is found that the optimal allocation is different for the equivariant model compared to non-equivariant one. The equivariant model tends to achieve better performance by putting more compute in training time, whereas the non-equivariant one performs better when it is made larger.

### Strengths
- The paper tackles as important problem for the geometric deep learning. There are not a lot of works performing systematic comparisons of the performance of equivariant models vs non-equivariant ones. The investigation of scaling laws for equivariant models is also of interest
- The findings on optimal allocation of compute for equivariant models and non-equivariant models has value for practitioners, as they are helpful to guide design decisions and hyperparameter searches.
- The experiments have been done in a systematic way, as far as I can tell

### Weaknesses
I think the study is limited in significant ways that prevent me from saying that the question in the title was satisfyingly answered. I also think that the result analysis and the design of some elements of the study lead to conclusions that are potentially misleading.

**Choice of task**

- First, I don't think rigid body dynamics is an appropriate choice of benchmark task, since there is almost no overlap between the rigid body dynamics and equivariance communities. To the best of my knowledge, none of the state-of-the-art models on this problem (which the models implemented in this paper do not match) are rotation equivariant. It seems like it has been found by the rigid body dynamics community that equivariance is not worth it in this setting. If the authors want to suggest that equivariance might be of importance for this problem, they should compare an equivariant version of one of the state-of-the-art models like FIGNet. 
- Second, the necessity of E(3)-equivariance for this task is questionable. This is because a natural reference frame is given by the direction of gravity and the position of the center of mass. Allen et al. 2022 use this reference frame in addition with O(2) augmentations around the Z axis with great success. A realistic comparison should use this canonical reference frame with O(2) augmentations for the non-equivariant model. I expect that this will make the task easier for the non-equivariant model and data augmentation more computationally efficient.
- Third, there are problems for which equivariance is thought to be more important, and the study does not give evidence that the findings would extend on these problems, despite making general claims. Examples include potential energy/force field prediction, protein folding, molecular generative modelling and medical image segmentation. I think the conclusions of the study would be much more valuable if the authors had chosen to evaluate on one or ideally some of these tasks.
- Fourth, the only type of equivariance investigated is continuous E(3) equivariance. I therefore think it is an overstatement to extend the conclusions to any type of equivariance. Notably, no discrete groups are considered. Both equivariant models and non-equivariant models have been argued to be successful for many discrete groups such as image rotations (ViT not being equivariant for example).

*Summary*: The scope of the paper is ambitious, as from the title and abstract, it proposes to provide insights on the necessity of equivariance in general. However, the only experimental setup investigated is *rigid body dynamics with E(3) equivariance*. Even for this problem I find the experimental setup too artificial to give practical insights. Given this, I think the scope is overstated and that the experiments are lackluster.

**Choice of architectures and training setup**
- Another important limitation is that only one non-equivariant and equivariant architectures are compared. I think the diversity of architectures used in geometric deep learning does not compares with NLP where Transformers are dominant. Notably, I think a comparison using GNN type architectures would be valuable. These architectures are as far as I know more prevalent in geometric deep learning (at least definitely for rigid body dynamics) than Transformers on problems with E(3) equivariance, due to locality being a relevant inductive bias and offering computational advantages. I also think at least one spherical harmonics based architectures like Equiformer should be investigated since these are more widely used than geometric algebras.
- It is not clear how the family of hyperparameters for the two models is obtained. An important aspect of an experimental study like this one is to specify a consistent procedure to come up with hyperparameters since these are important for model performance. I encourage the authors to give more details on this and if possible to use a budget method for hyperparameter tuning.
- I don't see a reason why the learning rate should be the same for the two models. It is mentioned in the paper that different learning rates were experimented with, so I think the authors should tune such parameters separately for each model. The learning rate is known to be important and the optimal one is not expected to the same for every model.
- I do not think that the same batch size should be used for both models. I understand that there is an issue of fair comparison here, since we expect that bigger batch size should lead to better performance. However, it would be more useful to know if the memory utilization of the equivariant model is significantly larger in a way that would make larger batches usable for the non-equivariant one. This is necessary to answer the question asked by the paper since in practice, people look to maximally use the available resources. Being able to do this efficiently should therefore be taken into account when choosing which model to use. I would be more interested in seeing experiments for which resources are used maximally for both models.

*Summary*: I find the study to be too narrow in terms of architectures investigated. The method used for hyperparameter tuning should be reported and made consistent. Finally, the experiment should be designed such that the different models maximally use the available ressources.

**Result analysis**
- The number of FLOPs is not really a metric of computational cost that matters in practice. While I understand that analyzing models in terms of FLOPs has the advantage of being hardware agnostic and to facilitate analysis, I think FLOPs should not be used to draw general conclusions. Therefore, I think the conclusion in the abstract "equivariant models outperform non-equivariant ones at each tested compute budget" is misleading. I think comparing models in terms of inference/training time on given hardware would be significantly more insightful. This is the result that should be put at the forefront of the paper. In particular, for rigid body dynamics forward time is much more important in practice than any measure based on training FLOPs, since the main goal of machine learning simulators is speed.
- From the FLOP throughput given in appendix, it seems like the conclusions obtained from figure 1 would be different if we looked at training time. The gap between equivariant and non-equivariant models would maybe become smaller. I think a version of figure 1 with forward time should be provided in the main paper and the conclusions nuanced appropriately if needed.
- I find the results provided in Figure 1 (and Figure 2 to some extent) to be quite confusing. The authors mention that the results are obtained in the infinite-data setting. If I understand correctly, this is training on a single epoch of data. As mentioned in the paper, this has the effect of making data augmentation irrelevant, since data augmentation will not be able to increase the effective amount of data seen by the non-equivariant model. I think this scenario is however unrealistic. I cannot think of real applications of equivariant models for which data is so abundant that one could only afford to train for a single epoch. If these applications exist, I encourage the authors to highlight them. Otherwise, I think it is misleading to consider that limit over the relevant setting where available compute can handle the available amount of data. I think this limit should be discussed separately from the case N_epochs >> 1 that is more relevant in practice.

*Summary*: I think conclusions on computational efficiency/budget should not be based on number of FLOPs, but on a practically relevant metric like inference time. It also seems like the paper overemphasize the one epoch limit (where data augmentation is useless), which is not relevant in practice.

### Questions
- How were the hyperparameters for the respective models obtained?
- I could not find what distribution of augmentations was used. In particular for augmentations over translations, it is not obvious what augmentations were used.
- Was the test data augmented or kept in a canonical reference frame?
- It would be interesting to see isoflop lines on figure 3 for the reader to see visually what is the optimal allocation of FLOPs

### Soundness
2

### Presentation
3

### Contribution
2
