# Enhanced Face Recognition using Intra-class Incoherence Constraint

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
The current face recognition (FR) algorithms has achieved a high level of accuracy, making further improvements increasingly challenging. While existing FR algorithms primarily focus on optimizing margins and loss functions, limited attention has been given to exploring the feature representation space. Therefore, this paper endeavors to improve FR performance in the view of feature representation space. Firstly, we consider two FR models that exhibit distinct performance discrepancies, where one model exhibits superior recognition accuracy compared to the other. We implement orthogonal decomposition on the features from the superior model along those from the inferior model and obtain two sub-features. Surprisingly, we find the sub-feature perpendicular to the inferior still possesses a certain level of face distinguishability. We adjust the modulus of the sub-features and recombine them through vector addition. Experiments demonstrate this recombination is likely to contribute to an improved facial feature representation, even better than features from the original superior model. Motivated by this discovery, we further consider how to improve FR accuracy when there is only one FR model available. Inspired by knowledge distillation, we incorporate the intra-class incoherence constraint (IIC) to solve the problem. Experiments on various FR benchmarks show the existing state-of-the-art method with IIC can be further improved, highlighting its potential to further enhance FR performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, authors present a novel method that can improve existing face recognition (FR) methods by imposing a constraint of dissimilarity with learned embeddings.  

The paper starts with a framework that decomposes the feature space of a superior model into two sub features, with one along that of a inferior model (pro-feature) and the other being orthogonal (innovation feature). Experiments show that the innovation part (orthogonal features)  has a high level of face distinguishability, which can be useful to learn from. Thus authors propose to use the dissimilarity with learning embedding as an auxiliary task in addition to the main face recognition tasks, under the knowledge distillation framework. 

Experiments showed that this method can consistently improve existing methods (ArcFace, CosFace, MagFace, AdaFace) across 6 FR benchmarks. It's observed that the proposed method has a larger benefit on smaller datasets. Author hypothesized that the proposed method works as an feature augmentation mechanism.

### Strengths
The paper is well written and easy to follow.  The paper uses multiple sections to explain the main idea step by step. It starts with the introduction of feature decomposition and uses experiments to demonstrate the usefulness of the orthogonal subfeature; Then experiments show that moving the feature along the direction of the orthogonal subfeature can improve model performance; finally, authors  propose the idea to encourage the model to move towards the direction that dissimilar to learned embeddings.  The idea is implemented within the knowledge distillation framework.   

The proposed method is novel and effective. Existing knowledge distillation methods generally impose a similarity objective to help the student model better mimic the teacher model. The proposed method is on the opposite direction - it leans dissimilarity.  Authors has provided a detailed analysis to justify this novel learning objective.

The experiments are extensive and the results are solid. Multiple classic face recognization models are used as baselines and studied on several common benchmarks. The improvements look consistent. Ablation studies provides good insights for understanding the proposed method.

### Weaknesses
The ablation of the proposed method can be further enhanced.  Authors has hypothesized the proposed method works as a feature augmentation mechanism. It will be insightful if other feature augmentation or regularization methods can be compared, for example, injecting noise to the activations. 

The method is only studied on face recognition. In theory, this method can be applied to other classification tasks (especially fine-grained classification). Existing face recognition benchmarks already have high accuracy, so the improvement doesn't look too significant.

### Questions
It would be interesting if authors can conduct experiments on some more challenging classification tasks.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper starts with the hypothesis that when considering two face recognition (FR) models, the better-performing model can be further improved by combining features orthogonal to the worse-performing model. Authors propose the use of intra-class incoherence constraint (IIC) as a way of accomplishing this when a single FR model is available. Accuracy results on multiple face image datasets indicate that the proposed approach shows slightly better performance over other relevant approaches.

### Strengths
One strength of the paper is the observation that incorporating the features orthogonal to the inferior model can improve the performance of a superior model. I am still not convinced of this as there is no theoretical proof of this, but numerical results are reasonably convincing.

Another strength of the paper is the collection of experimental results. Authors show accuracy results on multiple face image datasets and show comparisons with the state of the art FR methods. Also, ablation studies included seem to support authors' hypothesis.

### Weaknesses
One major weakness of the paper is the most of the concepts and associated discussion seem to be based on the 2-D spaces in Figs. 1 and 2 whereas the feature vectors are in a much higher dimensional space. One problem with over-relying on the figures is that authors speak as if there is one perpendicular component to the inferior model in Fig. 1. For a given model in n-dimensional space, there is a (n-1)-dimensional space orthogonal to it. How do we choose the innovation feature from this space? The paper lacks a clear explanation of how the proposed method effectively navigates this high-dimensional orthogonal space to identify truly beneficial innovation features, rather than simply adding noise or irrelevant components. The assumption that a single orthogonal direction captures all useful innovation is a significant oversimplification.

Another major weakness is that there are no theoretical proofs or justifications for the suggested improvements.  If a superior model can be further improved by combining it with something orthogonal to an inferior model, doesn't that imply that the "superior" model may not have been trained sufficiently? Also, why should we stop with combining the innovation from just one inferior model? Why not consider multiple inferior models and extract and use features orthogonal to these multiple models? The paper does not explore the potential for diminishing returns or negative interference when combining innovations from multiple inferior models. Furthermore, the lack of theoretical backing makes it difficult to assess the generalizability of the proposed approach beyond the specific datasets used in the experiments.

### Questions
1. Please clarify in the paper how the feature vector diagrams in Figs. 1 and 2 generalize to higher dimensions?

2. On Page 2, it is stated that "...innovation is always independent of features from CosFace". Independence and orthogonality are different concepts. Do you mean orthogonality or independence here? If later, please provide a justification for why orthogonality implies independence.

3. Manuscript suffers from language deficiencies. For example, "orthogonal" is a better choice for "perpendicular". Please revise the manuscript carefully to improve the language quality.

4. In Section 3.1, it is stated that "In the first case, as shown in Fig. 2(a), a and b are on different sides of d." In 2-D, it is clear what we mean by different sides. How are different sides defined in higher dimensional spaces?

5. In Eq. (3), should there be a summation over i on the RHS? If not, how come there is no dependence on i on the LHS?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a face representation learning method considering the intra-class dissimilarity. Experimental results on multiple datasets and baselines show the effectiveness of the proposed method.

### Strengths
This paper is well-written and easy to follow, the findings about pro-features and innovation features are interesting.

### Weaknesses
Here are some questions about this paper:
1) The loss L_{dissim} should be described more detailedly, especially the relationship between the motivation describe in introduction and minimizing the cosine similary of teacher and student feature.
2) The student network and teacher network are in the same sturcture. Will it be better if using the trained student network to be the teacher network since the goal of the method is a student network with higher performance? More analysis should be given.
3) Sicne this method mainly focuses on feature distillation and representation learning, more comparision with the SOTA distillation methods should be given.

### Questions
See weaknesses above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method to learn a new, better representation space for facial features, from two existing, already optimal representation spaces. The analysis is based on some geometrical consideration regarding the possibility to improve a representation feature space, by interpolating other representation spaces.
The feature augmentation approach demonstrates very limited improvements on some identification tests. However, the proposed idea has some merits and it is worth further considerations and discussion towards the direction of adaptive techniques for feature space augmentation.

### Strengths
Attempting to design a general feature space augmentation techniques interpolating already sub-optimal baseline spaces.

### Weaknesses
The reported results demonstrate a very limited improvement, maybe not justifying the efforts.
The designed feature augmentation model may be dependent on the training and produce different results on  different pre-trained models.
Language mistakes

### Questions
How would you expect to enlarge the scope of the proposed techniques?
How could you disentangle the proposed augmentation method from the training data, and consequently the learned features?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
