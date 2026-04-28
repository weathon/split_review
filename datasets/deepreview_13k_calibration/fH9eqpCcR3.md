# Multiple Physics Pretraining for Physical Surrogate Models

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 5, 3, 6

## Abstract
We introduce multiple physics pretraining (MPP), an autoregressive task-agnostic pretraining approach for physical surrogate modeling. MPP involves training large surrogate models to predict the dynamics of multiple heterogeneous physical systems simultaneously by learning features that are broadly useful across diverse physical tasks. In order to learn effectively in this setting, we introduce a shared embedding and normalization strategy that projects the fields of multiple systems into a single shared embedding space. We validate the efficacy of our approach on both pretraining and downstream tasks over a broad fluid mechanics-oriented benchmark. We show that a single MPP-pretrained transformer is able to match or outperform task-specific baselines on all pretraining sub-tasks without the need for finetuning. For downstream tasks, we demonstrate that finetuning MPP-trained models results in more accurate predictions across multiple time-steps on new physics compared to training from scratch or finetuning pretrained video foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a multiple physics pretraining approach for surrogate modeling, which learns general useful features across diverse physical tasks with a shared embedding and normalization strategy. The experiment results show the proposed MPP-pretrained model outperforms task-specific baselines on all pretraining sub-tasks and also show superior finetuning results on new physics tasks.

### Strengths
1. Constructing a physics-based foundational model and exploring multiple task pretraining for computational physics tasks is both interesting and beneficial.
2. The experiments demonstrate impressive results in both pretraining sub-tasks as well as substantial transfer potential for new tasks with low-data system.
3. The authors have conducted several training strategies to perform the pretraining effectively.

### Weaknesses
1. More attempts can be made to address the transferability problems between different types of physics equations. For instance, when discussing the Navier-Stokes (NS) equations, whether at high or low Reynolds numbers, the equation forms are quite similar, which allows for the investigation into whether a single model still possesses robust merged learning capabilities for more different classes of equations, such as diffusion equations and wave equations. It would be beneficial to see experiments that explicitly test the model's ability to transfer knowledge across these more distinct equation types, rather than just variations within fluid dynamics.

2. What are the advantages and disadvantages of this new approach compared to the Finite Element Method (FEM) for systems with explicit control equations or empirical formulas? One of my biggest problem is whether the physics task should be treated as a purely data-driven problem, or if it ought to incorporate certain explicit priors or equation-based guidelines. The paper does not adequately discuss the trade-offs between these approaches, particularly in terms of computational cost, accuracy, and generalizability to unseen scenarios. A more thorough comparison with traditional numerical methods is needed to understand the practical implications of this work.

3. For models without PDEs, how can we determine the similarity of multiple physics fields and whether they can be learned simultaneously? I’m concerned about the improved performances are due to the limited diversity of different physics tasks. The current benchmark primarily focuses on fluid dynamics, and it's unclear if the observed performance gains would generalize to more diverse physical phenomena. The lack of a clear metric for quantifying the similarity between physics tasks makes it difficult to assess the true potential of the proposed pretraining approach.

4. In the appendix, experimental data from 1-step to 9-step show little change in the field, whether looking at ground truth or predicted solutions. If the selected time steps were longer, would the model still be able to accurately predict future changes? The paper should include experiments with longer time horizons to evaluate the model's long-term predictive capabilities and its ability to capture the temporal dynamics of the systems.

### Questions
Overall, the purposes behind this work are valuable. However, there remain many questions that need to be addressed. Please consider to answer the above questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an autoregressive task-agnostic pretraining approach for physical surrogate modeling. As like foundation models, the proposed method proposes training large surrogate models to predict the dynamics of multiple heterogeneous physical systems simultaneously by learning features that are broadly useful across diverse physical tasks.

### Strengths
This paper builds on recent advances in deep learning for physical simulation to enable surrogate models to work for diverse physical systems with a few fine-tuning iterations. The exposition for the motivation is written crisply and convincing, and is generally easy to follow. The experiments are performed for diverse physical systems. The results show that large surrogate models outperform strong baselines, and even models with a relatively few parameters can learn such diverse physics evolutions and perform competitively.

### Weaknesses
Although the generalizing capability is significant, the computational cost of the proposed models is still concerning. The followings are associated questions: 
* How do the authors expect the computational cost of the proposed models and how does it compare against other baselines in Table 1?
* It is still a bit unclear if the comparison reported in Table 1 is fair, since the parameters of the first 4 models do not look comparable.
* Is the model applicable to 3D simulations?

Many details of the inverse problems seem missing, and it makes assessing the performance of the proposed model a bit difficult in this regard. The followings are some of the questions:
* How do you define the inverse problem and what model was used for the tasks?
* How does the performance compare to other baselines?
* What is the running time of the proposed model and how is it comparable to the other baselines?
* Could the authors provide insights or results on the inverse problem for boundary condition?
* Providing qualitative results would be helpful.
 
**Minor comments** 

Typo in section 5.1: must handle all all systems and regimes without finetuning

### Questions
Please have a look at the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present Multiple Physics Pretraining (MPP), a methodology for task-agnostic pretraining of surrogate models in physics. This technique facilitates pretraining on a large scale, allowing for knowledge transfer across a variety of physical domains. To handle the problem that features of physical tasks are diverse, a shared embedding and normalization strategy are introduced to project the fields of multiple systems into a single shared embedding space. The experiments show that a single MPP-pretrained transformer can output competitive or outperform task-specific baselines ( fluid mechanics-oriented benchmark) on all pretraining sub-tasks without finetuning.

### Strengths
- The idea to construct a large pre-trained base model for physical simulations is promising. The current learning based surrogate models usually have limited generalization ability, which require re-training from scratch given different governing equations. The pre-trained model has the potential to improve the generalization ability or make it possible only to fine-tune on specific tasks without training from scratch.
- In the experiments part, the proposed model can achieve one order of magnitude smaller errors comparing to the existing methods.

### Weaknesses
 - The experiments for validating the proposed model are currently limited to 2-D cases (incompressible and compressiable Navier-stokes equations,  shallow-water equations, and a 2D DiffusionReaction equation). It is unclear whether the proposed model can achieve same level of performance and accuracy when applied to more realistic 3D physical simulations. Specifically, the current experiments do not address the challenges of increased degrees of freedom and the potential for different physical phenomena to dominate in 3D simulations, such as the emergence of complex turbulent structures or boundary layer effects that are not fully captured in 2D.
- It seems that the current model mainly focus on predicting the solution one time step further. The video results (diffre, incompNS, mpp_swe) shown in the supplemental materials exhibits strong checkboard artifacts as the timesteps grow. This suggests potential numerical instability issues, where small errors in each time step can accumulate and lead to divergence or unphysical oscillations in long-term simulations. The presence of checkerboard patterns specifically indicates a potential issue with the spatial discretization or the model's ability to capture high-frequency spatial modes accurately.
- The proposed model can only handle simulations on structured mesh. However unstructured mesh (e.g., triangular, tetrahedra) is a more common choice in real world simulations. In addition, the multi-resolution i.e., mesh with adaptive resolution, which is also a common technique in large scale simulations, has not been taken into consideration. This limits the applicability of the method to real-world scenarios where complex geometries and varying levels of detail are often required. The lack of support for adaptive mesh refinement also means that the method may not be computationally efficient for problems with localized regions of high activity.

### Questions
- It is mentioned in the appendix that the model is trained for 500 epochs for one task. How long does the training process take?
- Are there any intuitive explanation for the checkboard artifacts as the timesteps grow shown in the video? Does it mean the proposed method is numerical unstable to some extent?
- Does the proposed method have the potential to be applied to 3D simulations while keeping the efficiency and accuracy? (as the max memory usage of current model is ~60GB)

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
The core of this paper is the proposal of a new transformer structure for pre-training on different neural operator datasets. Specifically, the paper employs several different PDE datasets from PDEBench for training, and the results can generalize to specific datasets in a zero-shot manner. Overall, the idea is novel, paving a new path for the application of neural operators in data-constrained scenarios. However, the learning of neural operators significantly differs from other data types like text and images, and whether a simple auto-regressive approach can be used for unified pre-training remains ambiguously addressed in the paper. Detailed concerns are noted in the drawbacks. All in all, I appreciate the idea presented in this paper, yet there is considerable room for improvement in problem definition, paper composition, experimental design, and comparisons. Thus I recommend the authors revise the paper and submit it to the next venue.

### Strengths
1. The idea presented in this paper is relatively novel.  To the best of my knowledge, no published work has utilized an auto-regressive approach for pre-training on different types of PDEs to enhance performance on downstream tasks.
2. The network structure proposed in the paper is efficient, and capable of handling datasets or PDE problems of varying sizes, resolutions, and channel counts within an acceptable level of complexity.
3. The experimental results validate that even with differences in equation parameters or properties, pre-training can significantly save data, which is a valuable point. Additionally, the authors found that transformers pre-trained on video datasets are also beneficial for tasks of operator learning. This is an interesting fact.

### Weaknesses
1. Firstly, the paper forcibly combines different types of datasets for training without considering the potential conflicts in PDE solutions. For instance, one can construct two PDEs that have identical or minimally differing data within a certain frame count, yet due to the non-linearity of PDEs or inherent differences in the equations, they exhibit substantial differences in subsequent evolution. Unlike Ref [1] which unifies the form of PDEs, this paper's approach to mixed dataset training could lead to the model learning meaningless representations, especially in the presence of conflicting data. Specifically, the paper does not address how the model distinguishes between different PDEs when the initial conditions or short-term dynamics are similar, but the long-term behaviors diverge significantly. This is a critical issue because the model could learn to average out these conflicting dynamics, resulting in poor generalization. From the experiments and provided open-source code, it seems the paper selected equations with vastly different properties for pre-training, which doesn't address this challenge faced in PDE pre-training.

2. Although the experimental section is logically well-structured, the descriptions of the experimental results and settings remain unclear. For example, PDEBench provides multiple datasets for CNS M1.0 and CNS M0.1, but the paper doesn't clearly state which dataset was used for training or testing. The paper should specify the exact subsets used, including the specific parameters and initial conditions. Besides, the source of the results for other baselines is not clarified, and the comparisons have too few baselines. The lack of clarity makes it difficult to reproduce the results and assess the true performance of the proposed method. It is also unclear how the baselines were trained and whether they were optimized for each specific dataset or used a more general approach.

3. I believe the paper's contribution of pre-training PDE representations is overstated. Upon careful examination of the appendices, I found that the paper nearly only utilized a few fluid dynamics datasets from PDEBench and a small diffusion-reaction equation dataset. Compared to the NLP or CV community, which employs almost all publicly available data on the internet for pre-training, the scale of pre-training in this paper is not large; it's more aptly termed as transfer learning. The limited diversity and scale of the pre-training data raise concerns about the generalizability of the learned representations to a broader range of PDE problems. The paper should acknowledge the limitations of the pre-training dataset and temper its claims about the universality of the learned representations.

### Questions
None

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a pretraining strategy for autoregressive modeling of physical systems. It proposes a model architecture and training regime to handle the heterogeneity of training data. Experiments on the PDEBench dataset demonstrate the ability of the method to model different systems with state of the art accuracy. The authors further investigate the added value of the pretrained model in low-data settings and parameter-estimation tasks.

### Strengths
Strength 1: The authors experimentally validate the hypothesis that a single model can learn on diverse fluid mechanics systems, which is a key step for the development of general “foundation” models for physics tasks. This line of experiments is well explained and rigorously reported. The use of the PDE-Bench dataset tasks and baseline models will ease all future work of the community to build and improve on the proposed approach. 

Strength 2: The architecture is novel and constitutes a first usage of transformer-based architectures for autoregressive modeling of physics systems. Given the exceptional scaling abilities of these models and their results in other scientific domains (chemical physics, biology), it is a promising direction for autoregressive tasks. Reporting the performance of the proposed architecture on PDEBench tasks, without multi-physics training, would already be valuable to the community. 

Strength 3 : The paper is easy to read and the questions it aims at answering are clearly formulated. Design choices and training regime are well motivated by the specificities of multi-systems learning, and clearly documented. This will ease the ramp-up of the community on pre-training tasks, and improve on the proposed architectures by proposing alternate design choices.

Strength 4 : Figures and tables are clear, metrics and units are clearly reported and consistent with previous publications when taken from there

### Weaknesses
Weakness 1: The authors frame their question on the low-data regime (Section 5.2) as “Does MPP provide a fine-tuning advantage over existing spatiotemporal foundation models for new autoregressive prediction tasks?”. Their experimental results indeed support the claim that MMP is superior. However I believe that in order to develop useful foundation models, such models should be compared to the “best one can do” task-specific model in the low-data settings. Monitoring the progress on tasks that are too hard for task-specific baselines (like those implemented in the PDEBench paper) will provide rich insights to the community. The first line of experiments (Section 5.1) does not enable this, as all tasks are used at training time, including the test task. 
A possible experiment to add to section 5.2 would consist in training one of the PDEBench baseline models on the two low-data tasks.

Weakness 2: The model architecture is completely novel and more experimental validation should be done to maximize the value for the community. Specifically, to separate the added-value of the transformer architecture from the added value of the multi-systems training, it could have been interesting to train the MMP architecture on each of the PDEBench tasks individually, and include it in Table 1 as a new single-task baseline. It is also quite common to include ablation studies to validate intuitions or design choices, and the claim that positional encodings help to learn boundary conditions (Section 4.2, last paragraph) should be validated either by such experiment, or by a proof in the supplementary material. The current claim is not sufficiently supported by experimental evidence or theoretical justification.

Weakness 3: The conclusion reminds the motivation behind multi-systems pretraining, but does not clearly recapitulate which questions have been answered and what is left to future studies. The two paragraphs are not well articulated and I feel would benefit from a rework. Ideally the reader should finish the paper with a clear view of the unanswered questions or limitations to be addressed.

### Questions
The paper takes first relevant steps towards training general models to model physical systems. I believe the authors have shown that their method of pretraining is functional, but more thorough experiments on the model architecture and the application to low-data tasks would be beneficial to the community and greatly increase the interest of the paper :

1) Put the low-data results (Section 5.2) in perspective with task-specific baseline performances : are these tasks way too hard for the PDEBench baselines ? Ideally, report the performance of one task-specific baseline in Figure 5. 

2) Rework the conclusion to simply recapitulate the questions answered and which questions should be explored in future studies.

3) In section 4.2 last paragraph, clarify whether the claim on boundary conditions is justified theoretically, validated by an ablation study, or both. Ideally, add relevant information in the supplementary material.

Minor comments to improve readability :

a) Code clarity : Papers that propose pretrained models should be as easy as possible to finetune, so that the community can make quick progress towards more efficient pretraining approaches on challenging downstream tasks. I would recommend rewriting the train.py file to remove a lot of boilerplate code and make it easier to reuse and tweak. 

b) Clarity of Figure 2 and its legend can be improved: ReVIN abbreviation for the normalization layer is not defined. “physics metadata” is not defined neither in text nor in figure legend. 

c) Table 1 : abbreviations for task names are not defined in the manuscript and make it hard to find the correspondence in the initial PDEBench paper. Please define these abbreviations in the table legend.  

d) There is a typo in section 5.1 (word “all” written twice) : our models (denoted by MPP-AViT-*) must handle all all systems and regimes without finetuning

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
