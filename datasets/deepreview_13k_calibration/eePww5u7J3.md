# Swiss Army Knife: Synergizing Biases in Knowledge from Vision Foundation Models for Multi-Task Learning

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
Vision Foundation Models (VFMs) have demonstrated outstanding performance on numerous downstream tasks. However, due to their inherent representation biases originating from different training paradigms, VFMs exhibit advantages and disadvantages across distinct vision tasks.
Although amalgamating the strengths of multiple VFMs for downstream tasks is an intuitive strategy, effectively exploiting these biases remains a significant challenge. In this paper, we propose a novel and versatile ``Swiss Army Knife'' (SAK) solution, which adaptively distills knowledge from a committee of VFMs to enhance multi-task learning. Unlike existing methods that use a single backbone for knowledge transfer, our approach preserves the unique representation bias of each teacher by collaborating the lightweight Teacher-Specific Adapter Path modules with the Teacher-Agnostic Stem.
Through dynamic selection and combination of representations with Mixture-of-Representations Routers, our SAK is capable of synergizing the complementary strengths of multiple VFMs. Extensive experiments show that our SAK remarkably outperforms prior state of the arts in multi-task learning by 10\% on the NYUD-v2 benchmark, while also providing a flexible and robust framework that can readily accommodate more advanced model designs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a "Swiss Army Knife" (SAK) model that preserves each model's specific strengths through a framework consisting of a shared Teacher-Agnostic Stem and Teacher-Specific Adapter Paths. The SAK dynamically combines representations via Mixture-of-Representations Routers, allowing for tailored outputs for each task. Extensive experiments on multi-task benchmarks show that SAK outperforms several current methods.

### Strengths
1. This paper contributes a multi-task learning framework that leverages the strengths and specific biases of multiple Vision Foundation Models (VFMs), presenting an alternative to traditional knowledge distillation approaches. By preserving individual model biases, the method offers a good solution to challenges in multi-task learning, where distinct vision tasks often benefit from different aspects of visual representation.

2. Extensive experimental results are provided, showing substantial performance gains across established benchmarks. 

3. This paper is well organized and well written.

### Weaknesses
1. The proposed framework, while innovative, introduces a high level of algorithmic complexity by requiring multiple Vision Foundation Models (VFMs) and integrating Teacher-Specific Adapter Paths and Mixture-of-Representations Routers. Given the inherent complexity of multi-task learning, this layered structure may lead to excessive computational overhead without clear evidence of structural necessity. The paper could improve by providing a more rigorous theoretical justification for this architecture, perhaps through ablation studies that explore simpler configurations to assess if comparable results could be achieved with fewer components. Specifically, the paper lacks a detailed analysis of how the number of adapter paths and the complexity of the router affect both performance and computational cost. It is unclear if the observed gains are due to the specific design choices or simply the increased model capacity from adding multiple adapters and routers. A more thorough investigation into the trade-offs between model complexity and performance is needed.

2. The impressive experimental results may be partly due to extensive parameter tuning, but the paper lacks detailed discussions or tests that could isolate the contributions of the model’s design from effects arising purely from tuning. This raises questions about whether the performance gains reflect true architectural benefits or if they could be replicated by tuning existing simpler models. Including experiments with fixed hyperparameters across different tasks or using cross-validation techniques to verify robustness would strengthen confidence in the model’s structural contributions. Furthermore, the paper should clarify the specific hyperparameter search space and the optimization strategy used. Without this information, it is difficult to assess the generalizability of the results and the true impact of the proposed architecture.

### Questions
please see the weaknesses section.

### Soundness
2

### Presentation
3

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
This paper proposes a new method to achieve multi-task learning by coordinating the advantages of multiple Vision Foundation Models (VFMs). In order to solve the problem that the previous distillation method only uses a single student model that cannot preserve the representation bias between different VFMs, a teacher-agnostic stem and a teacher-specific adapter path modules are proposed to parameter-efficiently preserve the representation bias of different VFMs, and then the fusion coefficients of different branches are learned for different tasks through a mixture-of-representations router. Experiments on the PASCAL-Context and NYUD-v2 datasets have demonstrated the effectiveness of the method.

### Strengths
1. By distilling multiple Vision Foundation Models (VFMs) into a stem and multiple parameter-efficient branches, the computational cost is greatly reduced

2. By retaining the unique representation bias of each teacher model through the teacher-specific adapter path module, SAK can extract knowledge from multiple VFMs in a task-adaptive manner, thereby effectively improving multi-task performance

3. Comparative experiments and sufficient ablation experiments on PASCAL-Context and NYUD-v2 datasets demonstrate the effectiveness of the proposed method

### Weaknesses
1. Lack of experimental results on Image level reasoning and Large Vision-Language Model that are consistent with the comparison method RADIO

2. Lack of upper bounds on results before distillation, i.e., results using encoders of three Vision Foundation Models without distillation and routers

3. Compared with the base model selected in this paper, RADIO also selected SigLIP and Theia selected ViT-H. It is necessary to provide the principles of base model selection and experiments on the sensitivity of the model to teacher selection.

4. Can SAK be easily adjusted to add new Vision Foundation Models teachers or changes that meet the needs of specific downstream tasks?

### Questions
1. Compared with the base model selected in this paper, RADIO also selected SigLIP and Theia selected ViT-H. It is necessary to provide the principles of base model selection and experiments on the sensitivity of the model to teacher selection.

2. Can SAK be easily adjusted to add new Vision Foundation Models teachers or changes that meet the needs of specific downstream tasks?

### Soundness
3

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
3

### Summary
This paper introduces a novel method to consolidate different visual foundation models into one model via a mixture-of-expert fashion method. Through their approach, their method Swiss Army Knife (SAK) achieve state-of-the-art performance across various vision tasks.

### Strengths
(1) This paper systematically study the representation bias in different visual foundation models (VFMs), and identify characteristics of VFMs.
(2) The proposed approach achieve state-of-the-art performance on multi-task learning on various vision tasks.
(3) Thorough comparisons with baseline methods are provided to validate the effectiveness of the method. In addition, visualizations on choices of experts are given to provide insights into the method.

### Weaknesses
 (1) The proposed mixture-of-representation router involves conducting weighted sum over both student's and teacher's features, which would increase the inference cost during the process. This is because all teacher models will have to conduct forward propagation to obtain the output representations.
(2) More vision tasks such has instance-level segmentation/detection, depth estimation, could be evaluated.

### Questions
One thing the reviewer tries to seek clarification is how is mixture-of-representation being done when student and teacher has different architecture. In this case, the feature dimension of student and teacher is different.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies the problem of Multi-TaskLearning(MTL) under the context of VisionFoundationModels(VFMs). Specifically, the authors propose the solution termed as “SwissArmyKnife”(SAK), which adaptively distills knowledge from a committee of VFMs to enhance multi-task learning. Experiments on two public benchmarks demonstrates the ability of SAK to synergies the complementary strengths of multiple VFMs.

### Strengths
1. Experiments are extensive. The authors have validated their approach on two public datasets across multiple tasks and provide extensive ablation and analysis to demonstrate the effectiveness of the designs.
2. Inference costs is small. It is plausible that the authors try to embed the multiple vision foundation models into a single model which reduces the inference costs of running multiple models significantly.
3. Writing is clear. Overall, the paper is well-organized and the methodology is easy to follow.

### Weaknesses
1. Missing comparison with Foundation Models at other tasks. While the authors have compared their method with prior arts and vision foundation models (teachers) on two specific datasets, the reviewer is more interested in how is the performance of the delivered model at the tasks that the vision foundation models are good at? For example, after stage 1 training, how is performance of SAK compared to SAM at semantic segmentation, how is performance of SAK compared to DINOv2 at depth estimation, fine-grained classification, etc. With these study, we could have a more clear picture how well is SAK trained with the help of other vision foundation models.
2. Not always outperforming the best foundation models in Fig. 1. The reviewer noticed from Fig. 1 (left) that SAK cannot outperform the best foundation models at each task (which is sort of expected as they are the teachers), could the authors explain why SAK could outperform the teacher? and why it cannot outperform the teacher at every task?
3. Training costs. Although SAK has reduced the inference costs dramatically, it is expected that it may lead to more training costs as it will iteratively get the prediction from every teacher. The reviewer wonders how is the training and memory costs of SAK compared to baseline methods.

### Questions
See weakness above. The reviewer is interested in understanding how well can SAK embed knowledge from multiple vision foundation models and comparisons at the tasks that the vision foundation models are good at will be more convincing.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes SAK to effectively merge different VFMs for downstream vision tasks, mitigating the issue of the divergence of different biases among the different vision representations generated by each model. SAK innovatively proposes a new paradigm for transferring knowledge with the proposed lightweight Teacher-Specific Adapter Path modules instead of using a standalone backbone in a many-to-one distillation manner. Extensive experiments on two commonly-used benchmarks show the effectiveness of SAK.

### Strengths
1. The paper makes a novel attempt to analyze the failures of previous distillation methods. The authors examine the representation biases of VFMs quantitatively and qualitatively to demonstrate that the biases or diversified visual representations have a unique contribution to each downstream task.

2. The proposed adapter path and MoR routers are lightweight and easy to implement, which makes it easy to follow.

3. The experiment results are significant and solid, where the abundant analytical results further prove the effectiveness of the SAK method.

### Weaknesses
1. The training difficulty of the router should be discussed since the gating functions of MoE are always hard to optimize for a balanced routing.

2. The authors are encouraged to provide some results on multimodal LLMs (like LLaVA, Sphinx) to further verify the effectiveness of the proposed methods.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
