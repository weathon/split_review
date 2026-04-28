# Model Developmental Safety: A Safety-Centric Method and Applications in Vision-Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
\vspace*{-0.1in}

In the real world, a learning-enabled system usually undergoes multiple cycles of model development to enhance the system's ability to handle difficult or emerging tasks, which involve collecting new data, training a new model and validating the model.  This continual model development process raises a significant issue that the model development for acquiring new or improving existing capabilities may inadvertently lose capabilities of the old model, also known as catastrophic forgetting. Existing continual learning studies focus on mitigating catastrophic forgetting by trading off performance on previous tasks and new tasks to ensure good average performance.  However, they are inadequate for many applications especially in safety-critical domains, as failure to strictly preserve the good performance of the old model not only introduces safety risks and uncertainties but also imposes substantial expenses in the re-improving and re-validation of existing properties. To address this issue, we introduce {\bf model developmental safety as a guarantee} of a learning system such that in the model development process the new model should strictly preserve the existing protected capabilities of the old model while improving its performance on target tasks. 
To ensure the model developmental safety, we present a retention-centric framework by formulating the model developmental safety as data-dependent constraints. Under this framework, we study how to develop a pretrained vision-language model, specifically
the CLIP model, for acquiring new capabilities or improving existing capabilities of image classification. We propose an efficient constrained optimization algorithm with theoretical guarantee and use its insights to finetune a CLIP model with task-dependent heads for promoting the model developmental safety. Our experiments on improving vision perception capabilities on autonomous driving and scene recognition datasets demonstrate the efficacy of the proposed approach

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on the model deployment cycle for a learning-enabled system. The author proposes a concept called "model developmental safety" (MDS) to measure whether the learning-enabled system can strictly maintain the performance, i.e., zero forgetting, of the old tasks for safety-critical domains. The author proposes an efficient constrained optimization algorithm tailored to finetune the pretrained CLIP model that takes the MDS as the data-dependent constraint, providing a statistical guarantee for achieving MDS. Experiments have been conducted on BDD100k from autonomous driving scenarios and Places365 for scene recognition.

### Strengths
(1) The proposed "model developmental safety" (MDS) concept seems interesting and relevant to safety-critical applications, though many concerns remain, which will be elaborated on in the Weakness section.

(2) The proposed constrained optimization algorithm is sound for fine-tuning CLIP by retaining old data to achieve MDS; its effectiveness has also been validated by comparison with other methods.

### Weaknesses
(1) The motivation and necessity of the MDS is not sound enough. First, the MDS can be viewed as a more strict version of preventing catastrophic forgetting, i.e., maintaining "zero forgetting" during continual learning. The author claimed in lines 065-069 that zero forgetting is crucial for many safety-critical applications when considering the whole deployment cycle of the learning-enabled cycle, which is reasonable. However, only strictly preserving the model's original performance is not enough. For instance, strictly maintaining the performance of tasks that are not good enough may not bring more benefits to improving the safety of the existing learning-enabled applications. The review may suggest that the author calibrate their statement.

Moreover, other than the traditional paradigm of continual learning, there also exist other paradigms like data engines that consider the whole machine learning cycles [a, b, c] to achieve the safe development of the learning-based system, where [c] provides an automatic self-improved data engine for safety-critical application, i.e., autonomous driving. Different from the present work, [c] does not need to retain old data to maintain the performance; instead, it mines the vast amount of unlabeled data to increase the performance of long-tailed or new tasks while maintaining the performance of the old tasks. Moreover, [c] validates the self-improved data engine on object detection tasks, which is more challenging and safety-critical in autonomous driving and classification. The reviewer may suggest the author include some discussion of other learning paradigms, like automatic data engines, given that they have similar motivations and targeted applications.

(2) The proposed algorithm seems too restricted to the pretrained CLIP model, making it hard to evaluate the applicability of the proposed method for safety-critical real-world applications. Although the proposed method is sound for fine-tuning the pretrained CLIP to achieve MDP, the proposed constrained optimization seems too restricted, making the reviewer wonder whether it has sufficient applicability for other foundation models. The development of the algorithm mainly depends on the CLIP model and the contrastive loss, while the contrastive loss is not the only choice for training the foundation model. The author may want to elaborate on how the proposed algorithm can be extended to different kinds of foundation models.

Moreover, there is a practical concern that the foundation model like CLIP may not satisfy the requirement for the real-time latency of safety-critical applications like autonomous driving, as the real-world intelligent system is also integrated with many different components. The author may want to show that the proposed algorithm can also apply to lightweight models other than foundation models to validate the applicability of the proposed method.

(3) In the experiment, the author only considered the classification task in autonomous driving and scene recognition. However, many safety-critical applications that are more challenging and underperformed [d] will benefit more from MDS, e.g., 2D and 3D object detections for perception and tasks for motion prediction. The author may want to have more case studies other than classification to show the generality of the proposed algorithm.

(4) For the comparison methods, the author only compared with the GEM proposed in 2017, while many other replay-based methods [e, f] have been proposed in recent years that can achieve state-of-the-art performance in the continual learning literature. The author may want to compare with those methods.

Minor:

(1) The reviewer wonders why DevSafety is measured by 'acc', while in Equation (2), it is defined by measuring the difference of empirical loss between the new and old models.

(2) The author may want to elaborate on 'mild conditions' in lines 273-274.

(3) What is the insight of leveraging the moving average estimators in lines 290-291?

(4) Typo in line 312: 'proected' -> 'protected'

(5) In lines 461-464, how should we interpret Figure 2 that the development safety has been achieved?

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
3

### Summary
This paper aims to study the problem of improving model accuracy on new categories while ensuring that accuracy on fixed existing categories does not degrade. It formulates the problem as an inequality-constrained optimization problem and proposes an algorithm to solve it. Overall, I believe the paper's core innovation lies in introducing a new optimization algorithm for solving non-convex constraint problems.

### Strengths
1.The paper provides extensive theoretical analysis of the optimization algorithm to ensure its correctness.

2.Experiments are conducted on large-scale datasets to verify the general performance of the method.

3.The appendix effectively supplements details of the methodology and experiments.

### Weaknesses
1.The article is based on the premise of safety, proposing the assumption of strictly maintaining the original model performance unchanged. However, in real-world applications, classification tasks do not always require extremely high accuracy, and some fluctuation in accuracy is acceptable in certain scenarios. Given that the classification task discussed in the article is not an extreme case, I believe that the strict maintenance assumption proposed may be overly rigid for the actual tasks accomplished by the CLIP model.

2.The abstract and introduction are somewhat misleading, as catastrophic forgetting encompasses a broad range of phenomena beyond the classification issues discussed in the paper, including the ability to recognize image content. The “protected capabilities of the old model” described in the introduction may cause ambiguity.

3.Evaluating model performance solely using the safety ratio metric is insufficient. The issue with the safety ratio metric is that, if a model update method results in an imperceptible decrease in accuracy on existing categories while significantly increasing accuracy on new categories, such a scenario might be acceptable to a certain extent. However, this situation would be rated poorly with this metric. To differentiate these cases from methods that cause significant performance declines on existing categories, it is necessary to include data on the change in recognition accuracy for existing categories after training.

4.When evaluating the ability to protect classification accuracy across multiple categories, the safety ratio is not provided, and I cannot find any points in Figure 2 that obviously exceed the DevSafety (acc) boundary of 0. This raises doubts as to whether the improvement in dressing room classification accuracy was accompanied by declines in certain other categories, making me skeptical of the authors’ conclusion that old performance remains consistent in multi-task scenarios.

### Questions
Please refer to Weaknesses.

### Soundness
4

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
The paper proposes **model developmental safety** to argue the importance of handling catastrophic
forgetting with a constrained optimization framework. The proposed method is evaluated to ensure the development of CLIP models. The experiments cover datasets from self-driving to scene classification.

### Strengths
1. The theoretical analysis of the framework in Section 5 is sound and comprehensive.
2. The evaluation of ensuring CLIP models' continual development is fair.
3. The visualization of the learning trajectories is well-presented.

### Weaknesses
1. Although the authors tried to address the term ambiguity in Section 2 (with AI Safety), the use of the terms "safety" / "safety-centric" in this paper is often overstated because it doesn’t engage with the broader ethical and operational safety considerations commonly associated with the term. Even further, in Line 132, the paper writes "safety of safety", which is not rigorously explained. In fact, the paper focuses on designing constraints to preserve task performance, which, while essential, diverges from widely understood safety principles in deep learning models. An alternative term such as **"developmental stability"**, **"continual stability"**, or **"capability preservation"** can more clearly represent the framework's intentions without abusing the term of safety.

2. The empirical evaluation is lacking. Note that the Vision Language Model (VLM) is a general category of foundation models, and CLIP is only one example of this category. Other representative variants such as LLaVA and BLIP that can generate languages are not evaluated in the paper. In the abstract, the paper writes that *"...we study how to develop a pretrained vision-language model (aka the CLIP model)..."*, which may mislead future readers since "aka" is wrongly used here.

3. Considering the paper's motivation to ensure stable continual development **without harming protected capabilities**, it largely overlaps with the task of **knowledge/representation editing** [1,2,3,4,5,6] on VLM/LLM. However, few pieces of related literature are discussed in the paper. Authors may consider discussing the main advantages of their proposed framework regarding this existing line of research.

### Questions
Please address my concerns stated in the weakness section. Also, please revise or re-consider all uses of "aka" in the paper (e.g., Line 29, Line 124) as they may lead to unnecessary confusion.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper formulates the safety multi-stage development problem using a comprehensive mathematical framework, offering a detailed analysis of its application on CLIP with a theoretically derived, task-dependent head. The authors propose an efficient constrained optimisation algorithm, which is empirically validated through extensive experiments.

### Strengths
- Introducing the concept of model developmental safety is highly valuable, particularly in the context of large language models (LLMs), where the continual development often strains prior safety and alignment constraints. This concept is timely and impactful.
- The paper provides a robust guarantee for model developmental safety (MDS) of CLIP, underpinned by a detailed convergence analysis.
- Leveraging theoretical insights, the authors apply LoRA-based, task-dependent heads to effectively reduce the value of $\delta$, with empirical validation provided in Appendix A.5.3.
- The proposed method demonstrates impressive performance improvements over baselines, notably in terms of the safety ratio, showcasing its effectiveness and robustness.

### Weaknesses
Applying the model developmental safety (MDS) framework to vision-language models like CLIP for image classification is an interesting approach; however, it may not fully showcase the safety-critical nature of MDS. Since image classification in CLIP carries relatively low safety risk, especially compared with application in the safety of Large Language Models (LLM).

Due to this, It’s challenging to distinguish this work from conventional Continual Learning (CL) approaches, despite the explanations in the related work section. To clarify the unique contribution, it could be beneficial to either emphasise scenarios where safety risks in CLIP are more evident or explore a more safety-critical application domain. For instance, focusing on multiple cycles of model development within LLMs—which frequently involved fine-tuning and are urgently required to ensuring safety and alignment—may better align with MDS objectives and make the safety focus more explicit and practical.

 The continual learning (CL) baselines included seem somewhat dated, with the most recent stemming from 2018 (Castro et al., 2018). It would strengthen the paper’s claims to compare the proposed method with more recent baselines mentioned in the related work.

### Questions
- In Eq. (2), the concept of DevSafety seems to be defined as the worst-case performance drop of protected tasks. Could you please elaborate on how this definition differs from similar metrics, such as the forgetting measure commonly used in continual learning? Or is the primary aim of DevSafety indeed to achieve zero forgetting?
- he continual learning (CL) baselines included seem somewhat dated, with the most recent stemming from 2018 (Castro et al., 2018). It would strengthen the paper’s claims to compare the proposed method with more recent baselines mentioned in the related work.
- For clarity, it might be helpful to define $ s(\mathrm{\mathbf{x}}; \mathrm{\mathbf{w}})$ at its first mention (L158), rather than waiting until L179, as this could enhance readability and comprehension for readers.
- Providing a brief discussion of the limitations and potential directions for future work would be valuable, helping readers understand the broader impact and next steps for this research.
- The literature review on Safe Reinforcement Learning (SafeRL) at Line 134, while informative, may fall slightly outside the main scope of this article. You might consider clarifying its relevance to the paper’s focus, or potentially removing this section to maintain a more concise scope.

> Francisco M Castro, Manuel J Marín-Jiménez, Nicolás Guil, Cordelia Schmid, and Karteek Alahari. End-to-end incremental learning. In Proceedings of the European conference on computer vision (ECCV), pp. 233–248, 2018.

### Soundness
3

### Presentation
3

### Contribution
2
