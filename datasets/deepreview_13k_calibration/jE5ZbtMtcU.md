# BLEND: Behavior-guided Neural Population Dynamics Modeling via Privileged Knowledge Distillation

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Modeling the nonlinear dynamics of neuronal populations represents a key pursuit in computational neuroscience. Recent research has increasingly focused on jointly modeling neural activity and behavior to unravel their interconnections. Despite significant efforts, these approaches often necessitate either intricate model designs or oversimplified assumptions. 
Given the frequent absence of perfectly paired neural-behavioral datasets in real-world scenarios when deploying these models, a critical yet understudied research question emerges: how to develop a model that performs well using only neural activity as input at inference, while benefiting from the insights gained from behavioral signals during training?
To this end, we propose \textbf{BLEND}, the \textbf{B}ehavior-guided neura\textbf{L} population dynamics mod\textbf{E}lling framework via privileged k\textbf{N}owledge \textbf{D}istillation. 
By considering behavior as privileged information, we train a teacher model that takes both behavior observations (privileged features) and neural activities (regular features) as inputs. A student model is then distilled using only neural activity. 
Unlike existing methods, our framework is model-agnostic and avoids making strong assumptions about the relationship between behavior and neural activity. This allows BLEND to enhance existing neural dynamics modeling architectures without developing specialized models from scratch.
Extensive experiments across neural population activity modeling and transcriptomic neuron identity prediction tasks demonstrate strong capabilities of BLEND, reporting over $50\%$ improvement in behavioral decoding and over $15\%$ improvement in transcriptomic neuron identity prediction after behavior-guided distillation. Furthermore, we empirically explore various behavior-guided distillation strategies within the BLEND framework and present a comprehensive analysis of effectiveness and implications for model performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors propose behavior-guided neural population dynamics modelling framework via privileged knowledge Distillation. They considering behavior as privileged information, and train a teacher model that takes both behavior observations (privileged features) and neural activities (regular features) as inputs, while a student model is distilled using only neural activity. The authors calm that the framework is model-agnostic, avoiding strong assumptions about the relationship between behavior and neural activity. 

The authors present empirical evaluation that includes extensive experiments across neural population activity modeling and transcriptomic neuron identity prediction tasks. They report over 50% improvement in behavioral decoding and over 15% improvement in transcriptomic neuron identity prediction after behavior-guided distillation. Additionally, the authors also explore various behavior-guided distillation strategies within the proposed framework and present analysis of effectiveness and implications for model performance.

### Strengths
Originality
- Interesting approach. The idea to train a teacher model using neural activity and behavioral signals, while subsequently distilling its knowledge to a student model that utilizes solely neural activity as input seems novel. The inference phase is the common, where the authors use the distilled student model for neural population activity analysis and transcriptomic identity prediction tasks, but having embodied the privilege, behavioral information.

Quality
- The paper is well motivated, structured and presented, the problem is well introduces and connected to existing work. The writing is good. There is extensive and diverse evaluation. The proposed approach demonstrates a good capacity for capturing implicit patterns within neural activity. It shows improvements, outperforming state-of-the-art models.

Clarity
- The idea and the main point of the paper are well explained. 

Significance 
- The authors provide new perspectives on how behavioral observations can be leveraged to guide the complex modeling of neuronal population dynamics.

### Weaknesses
I would be interested and I believe it would be nice to see the cross-correlation within the data e.g., between the neural activity and behavior data, so that we can have a better understanding if there is a cross-correlation (such as time-lagged cross-correlations or mutual information analyses between neural features and behavioral variables). 

This would help quantify the relationship between these data types (the extend of correlation and/or how much they complement) and potentially pinpoint and explain the benefits of the approach. It can also serve as additional insight to get to know more about why the proposed approach provides significant improvement in performance.

### Questions
Could you provide insights into which components of the BLEND framework (e.g., teacher-student architecture, distillation process, loss functions) contribute most significantly to the performance improvements? How do these components leverage the relationship between neural activity and behavior to enhance model performance?

Could you discuss the potential for applying BLEND to other multimodal neuroscience datasets, such as combining neural activity with gene expression data or neuroimaging? What modifications, if any, would be necessary to adapt BLEND for these different data types?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors proposed a two-step training process to create a model which is capable of creating a model that performs well using only regular features (neural activity) at inference time while benefiting from insights gained from privileged features (behaviour).

### Strengths
The paper is well written and easy to follow, thanks to the clear structure. The method is introduced after the problem, and both are well formulated and discussed. The ablations studies are well performed, and the qualitative analysis are interesting to see. In general, the whole experimental section address the right points.

### Weaknesses
First two images must be reworked. Right now, those are single images divided into sub images within the draw. This lead to a weird referencing approach in the paper. I suggest dividing them into proper figures, and improve figure's 1 resolution.

NVM acronym is not defined

My main concern is about distillation collapsing. Image to have two points B1 and B2 with the associated Xs. What happens while training (which I suggest decomposing to avoid overflow of equation number) when F_t(X1, B2) is similar to F_t(X2, B2) but X1 and X2 are not? In that case, the teaching model will collapse both X1 and X2 into the same point of the student model, since Distillation Loss push them to be similar. Do you think that this could happen? If so, I believe that such aspect must be addressed somehow.

### Questions
My main concern is about distillation collapsing. Image to have two points B1 and B2 with the associated Xs. What happens while training (which I suggest decomposing to avoid overflow of equation number) when F_t(X1, B2) is similar to F_t(X2, B2) but X1 and X2 are not? In that case, the teaching model will collapse both X1 and X2 into the same point of the student model, since Distillation Loss push them to be similar. Do you think that this could happen? If so, I believe that such aspect must be addressed somehow.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on developing a framework that incorporates behavior information during the training process, while using only the neural activities during inference stage for improved neural-behavior modeling. The proposed method is called BLEND, which uses the trick of privileged knowledge distillation, and distills a teacher model that is aware of behavioral information to a student model for inference. The model demonstrated strong empirical performance on both behavioural decoding tasks and neuron identity prediction tasks.

### Strengths
- Writing is clear with adequate literature review;
- Solid technical/experimental contribution, the experiments are adequately done;
- Overall, an important topic for the community to consider using privileged knowledge distillation in such tasks. The performance improvement seems large, demonstrating opportunities for potential future works.

### Weaknesses
 - Intuitions & clearness of section 3.2.1
1. While I personally appreciate the comparison of different distillation techniques, it is unclear to me their intuitions (e.g., when to use which), and I'd appreciate if the authors can provide more about such intuitions in section 3.2.1. to improve clearness.
2. It'd be even better if the authors can present a case study, ideally with synthetic datasets, showing why/when a distillation strategy is better. For example, in Table 3, it seems LFADS-Hard performs better than LFADS-Soft, yet for NDT NDT-Correlation in general performs better, did the authors check the reason behind it? Can the authors provide more reasoning/hypotheses based on the performance? 

- Fairness and more details of model selection and evaluation protocol. 
1. The models in Table 1 and 2 are named as "Distill-Best", which I assume is employing the best distillation strategy. What are the performance of the worst distillation strategies then? Can the authors be more specific about the model selection pipeline here?
2. Has the models run across different random seeds? What is the standard deviation? Is the training stable? Are there any special techniques applied to ensure the distilled model is good? (disclaimer: I didn't read the appendix, if some of those info are available in appendix, please make more detailed co-references.)

- The paper can benefit from more experimental case studies.
1. While there are a bunch of experiments, some of the authors claims were not well justified. Especially, as stated in footnote 1 "BLEND can be readily extended to accommodate scenarios wherein behavioral information is discrete or non-temporal in nature." - While the framework is easily extendable to discrete labels, can the authors actually attempt to perform an experiment given behavioral signals as discrete labels? e.g. The authors can mimic what is done in [1] and use the final reaching target direction to guide the learning, and show the corresponding performance of the model.

- Lack of theoretical & analytical results that supports the experimental results.

- Minor formatting suggestions:
1. Do the authors mind putting Table 1 and 2 at either the bottom or top of the pages?

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript propose a novel algorithm of BLEND to deal with neural activity reconstruction. Concretely, the behavior signals are used as the privileged knowledge and combined with masked neural activity data to train a teacher model. Then the teach model is distilled to a student model, which only use masked neural activity data as the input for reconstruction. The effectiveness of BLEND is verified on two benchmarks.

### Strengths
- The organization of this paper is well and the presentation of method is clear.

- A novel approach of BLEND, which conbines privilege knowledge (training teacher model) and knowledge distillation (training student model), is proposed for neural activity reconstruction.

- BLEND has achieved a good performance on two benchmarks.

### Weaknesses
I am not an expert in computational neuroscience, and cannot give a rational judgement w.r.t. experiments. However, I still think there are some major weaknesses in terms of writing and the rationale of BLEND, please see details as follows.

- **Q1:** The gap between BLEND and previous approaches is unclear, and the proposal of BLEND is suddenly. Is there other approaches that uses both masked neural activity data and behavior signals for training and only masked neural activity data for test? If it is, a detail comparison should be presented. Otherwise the significance of this scenario should be clear first.

- **Q2:** The rationale of proposed BLEND. The superiorty of BLEND is only verified on two recent benchmarks with limited baselines. It will be more convincing if a theoreitcal or empirical analysis can be provided to show why a better neural activity reconstruction is achieved by incorporating behavior signals. Therefore, the internal struction between neural activity data and behaivor signal data should be investigated.


- **Q3:** BLEND incorporates the technique of knowledge distillation. Is there a large performance drop by comparing teacher models and student models? In the experiments, many different distillation methods are used but only the performance of the best one is reported, which is not very fair for comparison.

Based on the above questions, I think there lacks a investigation on the characteristic of neuron data, so the rationale of proposed method cannot be well verified, i.e., why is BLEND good for the specific type of neuron data.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
