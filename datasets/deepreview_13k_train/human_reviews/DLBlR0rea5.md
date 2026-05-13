# How do diffusion models learn and generalize on abstract rules for reasoning?

- Decision: Reject
- Scores: 5, 6, 5, 3, 3, 5

## Abstract
Diffusion models excel in generating and completing patterns in images. 
But how good is their ability to learn hidden rules from samples and to generate and reason according to such rules or even generalize to similar rules? 
We trained a wide family of unconditional diffusion models on Raven's progression matrix task to precisely study this. We quantified their capability to generate structurally consistent samples and complete missing parts according to hidden rules. 
We found diffusion models can synthesize novel samples consistent with rules without memorizing the training set, much better than GPT2 trained on the same data. They memorized and recombined local parts of the training samples to create new rule-conforming samples. 
When tasked to complete the missing panel with inpainting techniques, advanced sampling techniques were needed to perform well. Further, their pattern completion capability can generalize to rules unseen during training. 
Further, through generative training on rule data, a robust rule representation rapidly emerged in the diffusion model, which could linearly classify rules at 99.8\% test accuracy. 
Our results suggest diffusion training is a useful paradigm for reasoning and learning representations for downstream tasks even for abstract rules data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a study of text-free diffusion models performance on a task derived from the Ravens Matrices "GeNRaven", using 5 held out rules as well as per-rule training and test sets to assess whether the diffusion model can 

1. unconditionally generate valid rows following a single rule (C3) 
2. conditionally infill a valid square when presented a ravens matrix.

Authors find that C3 performance generally exceeds infill performance (except for held out rules) and that linear probes can extract classifiers of _all_ rules (including held out rules) from latent representations. The performance is highly sensitive to training parameters and sampling methods used.

### Strengths
- the papers approach is very original and well designed (good comparisons, good ablations, mainly well done experiments, most relevant literature cited)
- quality-clarity: exposition is well done, quality of the paper is good except for the weaknesses below
- significance: I think the questions raised with the preset experiments and potential followups make this a meaningful benchmark to understand compositional generalization in diffusion models

### Weaknesses
 - I don't think reasoning is the appropriate term to use, instead, the authors have found a wonderful way to study _compositional generalization_ https://arxiv.org/abs/2307.05596 this has been found to allow diffusion models to even _interpolate_  latent variables https://arxiv.org/abs/2405.19201 and in the specific holdout setting the authors studied (leave-one-out holdout rules), everything is explained by compositional generalization (the semantic debate whether or not this is "true reasoning" is uninteresting to me here). Reasoning  might include comp. generalization, but also includes things like multi planning (see e.g. https://www.arxiv.org/abs/2409.13373) so the paper should change its framing of what is being studied
- the paper should repeat the strongest results with increasing subsets of held out rule to see whether the breakdown follows the expectations set in the current interpretation as a sanity check -science is about "kill your babies". this is in particular interesting for the linear probe (how many times must a factor appear to be visible?)
- I am unsure about the sample sizes chosen being meaningful, please use something like https://cran.r-project.org/web/packages/effectsize/index.html to justify experimental design. where appropriate, statistical tests should be used to justify claims against a concrete null hypothesis
- was only a single seed run for everything (in particular, training the model)? if yes, please rerun/retrain, do a statistical significance test and report uncertainties (I only see this on evaluation right now)
- The description of the automated evaluation pipeline is insufficient. It is unclear how the consistency of rows with the 40 rules is determined, and how the C2 and C3 metrics are derived from this. More detail is needed to assess the validity of the evaluation.
- The paper does not explore the effect of dimensionality constraints on the latent representation. Specifically, it is unclear whether the model can retain performance if the readout is factorized into lower-dimensional representations corresponding to relations and attributes, and whether a bottleneck on the latent space would affect the generalization performance.

### Questions
1. What happens if you condition on completely unseen shapes, bust consistent rules or vice versa?
2. can you factorize the readout with a dimensionality constraint and retain the performance?
3. How do you perform scoring ? manually or an automated evaluation pipeline?

### Soundness
2

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
4

### Summary
The paper investigates how diffusion models learn abstract rules using synthetic data from the Raven's Progressive Matrices (RPM) task, offering a detailed comparison with autoregressive models. The core contributions are as follows:

1. Demonstrating that diffusion models exhibit significantly less memorization than autoregressive models when trained on RPM data.
2. Showing that diffusion models generate outputs hierarchically, learning to recombine elements at a local scale before forming broader structures.
3. Revealing that the intermediate representations within diffusion models align closely with the underlying rules of the provided samples.
4. Observing that diffusion models only start to effectively learn abstract rules when a certain data scale is reached.

### Strengths
1. Comprehensive and well-designed experiments, particularly the use of synthetic RPM data, which introduces a new perspective on studying diffusion models. This controlled approach contrasts with natural object generation, which often lacks experimental control, allowing a more precise investigation of rule learning.

2. The experiments are rigorous, with careful comparisons between diffusion and autoregressive models, examining factors like memorization and hierarchical generation. This provides strong support for the paper’s findings.

3. The paper is well-organized, presenting methods and results in clearly.

This work broadens our understanding of diffusion models, suggesting their applicability beyond visual generation to reasoning tasks, and providing a framework for controlled abstract rule learning studies.

### Weaknesses
I think the main weakness of the paper is lack of an interesting and useful conclusion that we previously do not know about diffusion models. The main body of the paper is about experimental results, but I personlly did not find the results particularly surprising. I will follow the abstract to discuss one by one:

1. "diffusion models can synthesize novel samples": this seems not so surprising, because we already know that diffusion models can synthesize novel images (like flying monkeys) not existed before. 
2. "memorized and recombined local parts of the training samples": this is an interesting point, because previously we did not know how diffusion models can learn the structure. However, in this paper, they have this claim mainly because of Figure 7, which is a plot showing the model first learns local part, then global parts. It would be better if the authors can provide deeper discussions on this point.  
3. "advanced sampling techniques were needed for inpainting": this is also an interesting point, but it seems that here the authors simply mean that Sequential Monte Carlo will give better performance, but did not provide any deep analysis. 
4. "pattern completion capability can generalize to rules unseen": this is an interesting point, but it seems that the authors mainly provide some unseen examples in test set, and show that diffusion models can work well on these examples. The fact that models can generalize to unseen cases has been observed by many previous studies, and it would be great if the authors can use Raven's task to provide better intuitions and explanations. 
5. "rule representation": this is not in particular surprising, because people previously already observe that deep networks can learn semantic features, or self-supervised learning framework can learn very strong features.

### Questions
I was surprised to see that autoregressive models performed worse than diffusion models. In human visual reasoning, saccadic movements often create a dynamic, sequential prediction process resembling autoregressive models. Could the authors provide some intuition as to why autoregressive models underperform in this context? It would be interesting to understand potential limitations or factors influencing these results within the framework of this paper.

### Soundness
2

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
This paper evaluates the abilities of diffusion models in contrast to autoregressive models on the problem of Raven’s progression matrix. It proposes a dataset based on 40 relational rules and performs various types of experiments to evaluate the learning procedures and abilities of the trained models. It concludes that diffusion models has certain advantages over autoregressive models while in “rule consistent panel completion”, diffusion models happen to be weaker.

### Strengths
Paper is well written.

Experiments on the RPM are detailed and insightful.

It proposes a new dataset that may be useful for the community.

### Weaknesses
Literature review misses relevant prior work.

[1] Lachapelle, S., Mahajan, D., Mitliagkas, I. and Lacoste-Julien, S., 2023. Additive decoders for latent variables identification and cartesian-product extrapolation. Advances in Neural Information Processing Systems, 36.

[2] Bansal, A., Schwarzschild, A., Borgnia, E., Emam, Z., Huang, F., Goldblum, M. and Goldstein, T., 2022. End-to-end algorithm synthesis with recurrent networks: Extrapolation without overthinking. Advances in Neural Information Processing Systems, 35, pp.20232-20242.


Both of these papers consider a setting that has certain similarities to the problem that this paper studies. [1] also considers attributes such as location and color.



-----


The experiments of the paper are rather limited as it only evaluates the diffusion models on one specific dataset that is proposed for the first time in the paper. The dataset itself is not large (40 relational rules and 3x3 matrix of panels), and the achieved accuracy is rather high (99.8%) indicating that it is not very challenging. In my view, to draw conclusions about the learning abilities and learning procedures of diffusion models one would need to see more convincing experimental results on a broader set of related tasks. 


------

While the paper contrasts the abilities of diffusion models against that of autoregressive models, and provides some useful empirical evidence about the cases where one performs better than the other, it is hard to be sure that these would generalize beyond the specific task of Raven’s progression matrix. In its current form, I think it would be more appropriate for the paper to change its title and conclusions to reflect that it is only about the Raven’s progression matrix and not the broader topic of abstract reasoning. But, this makes the scope of the paper rather limited. So, I would suggest that the paper expands its experiments to other reasoning tasks, and try to make broader conclusions beyond the RPM task, perhaps for a certain class of reasoning tasks.

### Questions
Please see weaknesses. Would love to hear any clarifications or additional experiments that authors might want to share.

If authors manage to extend their experiments to some existing reasoning tasks in the literature, for example, one of the papers mentioned above (or any other existing reasoning task that they find appropriate), it would make their results more convincing and more connected to the existing literature.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work studies the ability of diffusion models to learn abstract rules and apply them during the generation of missing parts. Several families of diffusion models with different backbones (UNet and Diffusion Transformer) are trained and tested on the Raven's Progressive Matrices, a well-known reasoning task.
The authors show that in the unconditional generation task, diffusion models are able to generate consistent samples, which demonstrates their success in learning hidden rules. In the conditional generation task where the objective is to generate a missing panel, it is noted that the accuracy of the completion critically depends on the sampling algorithm. In addition, the authors illustrate that the diffusion models have some internal representations that distinguish the learned rules, evidenced by the high classification accuracy of a linear model trained on the hidden states of the diffusion models. This work provides a detailed discussion on the observed behaviour of diffusion models during training and testing, concluding that diffusion models are capable of performing rule-learning given a large data scale.

### Strengths
- This work is one of the first to evaluate a wide range of diffusion models' capability in rule-learning, targeting the task of Raven's Progressive Matrices. 
- Problem description and formulation is well illustrated in the overview diagram.
- Most of the claims are supported by solid results.
- This work provides detailed insights on diffusion models' behaviour in the task of rule-learning and reasoning, discussing potential explanations of those behaviours.

### Weaknesses
- Formal writing: the authors should carefully check all typos and grammar issues in this paper. Examples include but are not limited to: incorrect openings of quotation marks, incomplete sentences (Section 3.3, around line 180), informal use of abbreviations ("esp."), inconsistent naming (Raven's progressive matrix and Raven's progression matrix).
- Organization and presentation of results: this work includes several crowded figures, when they are referenced in the main text, it is often hard to follow since the text and the reference figure are far away from each other. For example, Section 4.3 involves discussions on Figure 4, Figure 10 and Figure 11, where Figure 10 and 11 are only found in the appendix. These results can potentially be summarized into one or two high-level figures that present the major outcomes, with detailed diagrams or tables included in the appendix. This would help readers locate relevant information easily.
- The claim on comparisons to auto-regressive models: the auto-regressive models used for comparison are GPT2 models, which might be out-dated given that there exist much stronger models. Out-performing GPT2 models does not support the claims on out-performing auto-regressive models.

### Questions
- How is GenRAVEN different from other RPM datasets in the literature? Is the encoding introduced in this work a novel transformation of RPM images to numerical data?
- In Section 4.1, it is mentioned that Logic-Attribute rules are hard to learn and will be discussed in Section 6, where there is only a brief observation on the correlation between panel overlapping rate and the performance per rule type. Can you elaborate more on why does that make the Logic-Attribute type different from other types?
- As mentioned in weaknesses, is it possible to include evaluations of more recent auto-regressive models for comparisons? For example, Llama 3.

### Soundness
3

### Presentation
1

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
In this study, the authors assess the capabilities of existing diffusion and language models in the context of abstract reasoning. They represent Raven's Progressive Matrices (RPM) puzzles in a numeric format, mapping each visual attribute to an integer value. The authors conduct several ablation studies on the trained models to evaluate their abstract reasoning abilities.

### Strengths
In this work, the following strengths can be found:
1. They conduct experiments on various state-of-the-art diffusion models as well as GPT-2. These models are trained on a proposed simplified version of Raven's Progressive Matrices, which is suitable for models that lack visual modalities, such as GPT-2.
2. In addition to training existing models on the proposed dataset, the authors provide extensive evaluations and ablation studies to explore the advantages of diffusion-based models compared to language models or better sequence generators, like GPT-2, in this context.

### Weaknesses
Some of the weaknesses of this work are:

### The submitted document needs to be completed.
1. The paper is incomplete. The supplementary material includes sections that are missing content (B.1, B.3, B.4). Some sections are only partially completed, such as B.2.3, which is missing figures and explanations that cannot be linked to experimental results, along with 'XXXXX' entries. Additionally, in section A.2.2, line 748, the authors failed to provide the hyperparameter values. Although these issues are present in the supplementary material, the reviewer believes that the authors should have been more diligent and submitted a complete version of their work.


### Clarity and Presentation
The reviewer suggests that the authors revisit their work, as improvements can be made in the presentation of the paper. The figures should be organized more effectively; currently, Figures 2, 3, and others appear to be placeholders with individual images stacked. Additionally, there are other issues with the presentation of the results: 
1. In Figure 5.D, not all versions are visible. The label "scale" is unclear in the legend, and it seems different models are referenced. What does "model_class" refer to?
2. In Fig. 2.D, what does the individual held-out rule color correspond to? There are five different cases, but the authors do not mention what each of them represents.

### Missing References to Prior Work 
Previous research has explored ways to represent Raven's Progressive Matrices (RPMs) in a format suitable for language models. The reviewer suggests that the authors should reference these studies and compare their RPM representation with existing works. It is possible that the proposed representation may not be appropriate for language models. Here are some relevant references: [1], [2], [3]. Additionally, this work introduces a simplified RPM dataset [4], which appears to be quite similar to the proposed representation.

### Dataset Concerns 
1. The reviewer expresses skepticism regarding the validity and difficulty level of the tested out-of-distribution (OOD) and held-out scenarios. In the proposed simplified dataset, all data is numeric. Therefore, if a model is trained to learn the constancy relation between the numbers on the second channel of the RPM, it may not be very challenging to identify this type of relationship on the first channel. This scenario differs from visual puzzles, where constancy in color is present during training, but testing introduces puzzles with constancy in shape for the first time.


### Contribution Concerns
1. The contribution of this work seems to be limited. The reasons are that the authors do not seem to propose a novel component but rather re-train existing models for a different reasoning dataset. 

[1] Zhang, Chengru, and Liuyun Wang. "Evaluating Abstract Reasoning and Problem-Solving Abilities of Large Language Models Using Raven's Progressive Matrices." (2024).

[2] Webb, Taylor, Keith J. Holyoak, and Hongjing Lu. "Emergent analogical reasoning in large language models." Nature Human Behaviour 7.9 (2023): 1526-1541.

[3] Ahrabian, K., Sourati, Z., Sun, K., Zhang, J., Jiang, Y., Morstatter, F., & Pujara, J. (2024). The curious case of nonverbal abstract reasoning with multi-modal large language models. arXiv preprint arXiv:2401.12117.

[4] Schug, S., Kobayashi, S., Akram, Y., Sacramento, J., & Pascanu, R. (2024). Attention as a Hypernetwork. arXiv preprint arXiv:2406.05816.

### Questions
1. For the ablations, the authors seem to use it as their reference model. However, SiT seems to perform better than DiT. Why did the authors not include SiT in the performed ablations?
2. How do the authors ensure that the training and testing set puzzles do not overlap? The dataset seems huge: 1,200,000 row samples per rule, with 40 rules in total.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This is experimental paper on evaluating diffusion models on a specific puzzle, named Raven’s progression matrix task. This task contains 3*9*9 features, and has 40 relational rules. The task is figure out the underlying relational rule based on the observation of two rows, and complete the third row based on the observation. This paper generates many data points for this task, and tried different variants of diffusion models, then gets some interesting observations, including the diffusion models can synthesize novel samples, learn from local parts of training samples, and can do pattern completion task for unseen rules. Moreover, the feature layer of the models contains semantic meanings of the rules.

### Strengths
I think the strength of the paper mainly comes from the small and concrete experimental setting. Indeed, in the Raven's task, there are limited number of parameters and rules, and one can easily control the data distribution and observe the performance of the diffusion models. 

Originality: I think the main originality arise from the concrete experimental setting, which also contains logic inference as well. I think this can be treated as one of the simplest settings for reasoning. 

Quality: the paper did careful investigation on various aspects of the task, with detailed discussions.

Clarity: the paper is easy to follow. 

Significance: the paper is significant in the sense that it is the first paper that tries to investigate the reasoning ability of diffusion models using a small and concrete task.

### Weaknesses
I think the main weakness of the paper is lack of an interesting and useful conclusion that we previously do not know about diffusion models. The main body of the paper is about experimental results, but I personlly did not find the results particularly surprising. I will follow the abstract to discuss one by one:

1. "diffusion models can synthesize novel samples": this seems not so surprising, because we already know that diffusion models can synthesize novel images (like flying monkeys) not existed before. 
2. "memorized and recombined local parts of the training samples": this is an interesting point, because previously we did not know how diffusion models can learn the structure. However, in this paper, they have this claim mainly because of Figure 7, which is a plot showing the model first learns local part, then global parts. It would be better if the authors can provide deeper discussions on this point.  
3. "advanced sampling techniques were needed for inpainting": this is also an interesting point, but it seems that here the authors simply mean that Sequential Monte Carlo will give better performance, but did not provide any deep analysis. 
4. "pattern completion capability can generalize to rules unseen": this is an interesting point, but it seems that the authors mainly provide some unseen examples in test set, and show that diffusion models can work well on these examples. The fact that models can generalize to unseen cases has been observed by many previous studies, and it would be great if the authors can use Raven's task to provide better intuitions and explanations. 
5. "rule representation": this is not in particular surprising, because people previously already observe that deep networks can learn semantic features, or self-supervised learning framework can learn very strong features.

### Questions
I do not have additional questions, as I listed my questions in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2
