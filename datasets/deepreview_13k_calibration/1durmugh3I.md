# Towards Fast, Specialized Machine Learning Force Fields: Distilling Foundation Models via Energy Hessians

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
The foundation model paradigm is transforming Machine Learning Force Fields (MLFFs), leveraging general-purpose representations to perform a variety of computational chemistry tasks. Although MLFF foundation models have begun to close the accuracy gap relative to first-principles methods, there is still a strong need for faster inference speed. Additionally, while model development is increasingly focused on general-purpose models which transfer across chemical space, practitioners typically only study a small subset of systems at a given time. This underscores the need for fast, specialized MLFFs relevant to specific downstream applications. In this work, we introduce a method to transfer general-purpose representations from MLFF foundation models to smaller, faster MLFFs specialized to specific regions of chemical space. We formulate our approach as a knowledge distillation procedure, where the smaller "student" MLFF is trained to match the Hessians of the energy predictions of the "teacher" foundation model. We demonstrate our approach across multiple recent foundation models, large-scale datasets, chemical subsets, and downstream tasks. We find that our specialized MLFFs can be up to 20 times faster than the original foundation model, while retaining, and in some cases exceeding, its performance. Specialized models trained via our approach also outperform those trained from scratch without Hessian distillation. We also show that distilling from teacher models with weaker inductive biases into student models with stronger constraints, like conservative forces, is effective. More broadly, our work suggests a new paradigm for MLFF development, in which foundation models are released along with smaller, specialized simulation "engines" for common chemical subsets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a new method for improving the efficiency of Machine Learning Force Fields (MLFFs) by utilizing a knowledge distillation technique. The method distills knowledge from large, general-purpose foundation MLFF models (FMs) into smaller, faster MLFFs specialized for specific regions of chemical space. This is accomplished by aligning the energy Hessians, which are the second derivatives of the energy with respect to atomic positions, between the teacher FM and the student MLFF. By strategically subsampling rows of the Hessian, the authors significantly reduce the computational cost of the distillation process. The authors demonstrate that their approach can achieve speedups of up to 20 times compared to the original FMs while retaining, and in some cases exceeding, the accuracy of the foundation models.

### Strengths
- The distilled MLFFs are up to 20x faster than their foundation model counterparts, enabling more efficient simulations.
- The distilled MLFFs achieve comparable or even better force prediction accuracy than the original FMs and demonstrate improved MD stability results.
- The Hessian distillation method is model architecture agnostic.
- Subsampling hessian rows significantly reduces computational costs without sacrificing performance. Its also interesting that subsampling quality doesn't impact the performance much.

### Weaknesses
 - Training with hessian distillation increases the computational cost compared to undistilled training.
- An anonymous link to the code is not available.

### Questions
- Some models use conservative forces and some don't. Do you have a sense of how much that impacts when you distill Hessians from a non-conservative model instead or if the student model is conservative? Or do you expect that not to impact performance as it seems like hessian quality doesn't?
- Why are the rows sampled so different for GemNet across training set and the same for PaiNN? What would be the general suggestion to set this hyperparameter? Or should everyone be iterating on this for every dataset, model architecture, etc?
- Why don't you compare the results with Kelvinius et al. 2023 on OC20-2M and COLL on which the original work was performed?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method for transferring general-purpose representations from large ML force field (MLFF) foundation models to smaller, faster MLFFs specialized for specific regions of chemical space, with the aim of improving inference speed. The approach is formulated as a knowledge distillation (KD) process, where the smaller “student” MLFF learns to match the Hessians of energy predictions made by the “teacher” foundation model. By selectively subsampling rows of the Hessian corresponding to individual atomic coordinates, the “student” MLFF achieves a training process that is computationally efficient relative to foundation models and demonstrates improved force prediction on downstream datasets.

### Strengths
* The approach is well-motivated, leveraging knowledge from large MLFF foundation models and adapting it to specific chemical space regions using knowledge distillation. The method also achieves promising results across organic and material molecular systems.
* The paper is well-organized and easy to follow.

### Weaknesses
 * Although the method shows promising results, the rationale for using Hessian information as a distillation signal is unclear, which may impact the perceived technical contribution. Additional theoretical or intuitive insights on this choice would clarify the method’s grounding. Specifically, while the Hessian does capture curvature information of the potential energy surface, it is not immediately obvious why matching Hessians would be a superior distillation target compared to, say, matching forces or energies directly, especially given the computational cost of calculating Hessians. A more detailed explanation of the specific advantages of Hessian matching, beyond simply capturing curvature, is needed.
* Foundation models are often trained with energy and force supervision, possibly derived from various electronic structure methods, making the physical reliability of Hessians from pre-trained foundation models questionable.
	* Notably, the authors mention that some student models outperform foundation models in specialized chemical spaces even before distillation, suggesting that foundation models may not fully converge in certain cases. This raises questions about the significance and reliability of using Hessians from foundation models as distillation targets. If the foundation model's Hessian is not a reliable representation of the true potential energy surface, then distilling to match it may not be the optimal strategy. Furthermore, the fact that student models can outperform the foundation model without distillation suggests that the foundation model might be overfitting to its training data or that the student model's architecture is better suited for the specific chemical space.
	* Accurate Hessians are crucial for tasks like geometry optimization (as referenced in Figure 1). It remains unclear how potentially inaccurate Hessians from foundation models could affect the student model's performance in such applications. For example, if the foundation model predicts spurious or inaccurate vibrational frequencies, this could negatively impact the student model's ability to perform reliable geometry optimizations or molecular dynamics simulations.
* It is uncertain whether the proposed method can be extended to MLFF architectures designed with energy-conserving forces or high-order equivariance, which are often crucial factors for stable and transferable ML force fields. Discussing the impact of these inductive biases on the Hessian-driven KD approach would strengthen the work. Specifically, many MLFFs are designed to conserve energy by construction, and it is not clear how the Hessian-based distillation approach would interact with these constraints. Similarly, the use of higher-order equivariance is often crucial for accurate force predictions, and it is unclear whether the Hessian distillation approach would preserve this property.

### Questions
See “Weaknesses” for detailed questions and suggestions.

Potential typos:
* Line 420: “disilling” should be “distilling.”

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
5

### Summary
This paper introduces a method to distillate MLFF foundation models to smaller, faster MLFFs with energy Hessians, achieving significant speed improvements while maintaining performance.

### Strengths
* This paper proposes a new method to distill MLFF foundation models into smaller, faster MLFFs with Hessians, which is highly beneficial for simulating realistic systems.
* The paper is written in a clear and concise manner, facilitating effortless understanding.

### Weaknesses
Related concerns are discussed in the questions section.

* The tables in the paper show only force results, without energy, so I'm curious about the energy results after distillation.
* A major concern is that the primary use of the distilled MLFF model is for molecular dynamics simulations, where conservation properties are crucial for scientists in physics, chemistry, biology, and materials science. I understand the authors avoided second-order derivatives to calculate the Hessian by directly predicting forces, using JVP calculations. However, a pretrained model might predict forces directly to save computation due to its large size, but the student model should compute forces using autograd, similar in the SFT in JMP[1], which makes more sense. Although Fig. 2 shows stable molecular dynamics in the NVT ensemble, following [2], energy will not be conserved in the NVE ensemble.
* The paper claims that the student model outperforms the teacher model, which is confusing. I suspect this is because the energy and force labels used in training come from the dataset itself. While the inclusion of Hessian loss is shown to be better than using only energy and force loss, this highlights the importance of derivatives. Since the Hessian matrix introduces force derivatives, could training a traditional MLFF from scratch, with forces computed via autograd, achieve similar or better results? Additionally, the statement in Fig. 3b about "speculating that s may play a similar role as the batch size" is akin to conclusions from traditional MLFF training, suggesting that direct autograd training without Hessian distillation might yield similar outcomes. The authors could compare such models to illustrate the Hessian's impact.
* Regarding the appendix experiment using force for distillation, what is the specific loss function? If I'm correct in understanding that the Hessian term in Eq. 3 is replaced by the force term, could the poor results from force distillation be due to the inherent force label loss in the data, where the teacher model's force predictions contradict the data labels? This implies that the force distillation setup might be flawed.

### Questions
* The tables in the paper show only force results, without energy, so I'm curious about the energy results after distillation.
* A major concern is that the primary use of the distilled MLFF model is for molecular dynamics simulations, where conservation properties are crucial for scientists in physics, chemistry, biology, and materials science. I understand the authors avoided second-order derivatives to calculate the Hessian by directly predicting forces, using JVP calculations. However, a pretrained model might predict forces directly to save computation due to its large size, but the student model should compute forces using autograd, similar in the SFT in JMP[1], which makes more sense. Although Fig. 2 shows stable molecular dynamics in the NVT ensemble, following [2], energy will not be conserved in the NVE ensemble.
* The paper claims that the student model outperforms the teacher model, which is confusing. I suspect this is because the energy and force labels used in training come from the dataset itself. While the inclusion of Hessian loss is shown to be better than using only energy and force loss, this highlights the importance of derivatives. Since the Hessian matrix introduces force derivatives, could training a traditional MLFF from scratch, with forces computed via autograd, achieve similar or better results? Additionally, the statement in Fig. 3b about "speculating that s may play a similar role as the batch size" is akin to conclusions from traditional MLFF training, suggesting that direct autograd training without Hessian distillation might yield similar outcomes. The authors could compare such models to illustrate the Hessian's impact.
* Regarding the appendix experiment using force for distillation, what is the specific loss function? If I'm correct in understanding that the Hessian term in Eq. 3 is replaced by the force term, could the poor results from force distillation be due to the inherent force label loss in the data, where the teacher model's force predictions contradict the data labels? This implies that the force distillation setup might be flawed.

[1] Shoghi N, Kolluru A, Kitchin J R, et al. From Molecules to Materials: Pre-training Large Generalizable Models for Atomic Property Prediction[C]//The Twelfth International Conference on Learning Representations.

[2] Fu X, Wu Z, Wang W, et al. Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations[J]. Transactions on Machine Learning Research.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel technique for knowledge distillation from foundation model force fields to smaller, faster, and more specialized force fields. The core idea is to align the Hessians of the energies with respect to atomic positions between the teacher (foundation model) and student models, facilitating efficient knowledge transfer. Experiments demonstrate that this approach improves stability and accuracy in the derived force fields compared to simpler distillation methods.

### Strengths
1. Clarity and Readability: The paper is very well-written and accessible, making the proposed method easy to follow.
2. Practicality: The approach is straightforward to implement and is cost-effective relative to similar knowledge distillation methods.
3. Experimental Validation: MD simulations performed validate the method, underscoring the practical benefits of the proposed technique.
4. Implementation Insights: The paper also offers practical implementation guidance for practitioners, which is particularly useful for real-world applications.

### Weaknesses
The baseline methods used for comparison seem to perform notably poorly, raising questions about fairness. This might be genuine, but the absence of hyperparameter tuning for the baselines undermines this. The authors specifically tuned their method by adjusting the Hessian distillation loss term, "we reduce the weight of the Hessian distillation loss term, λKD, by a factor of 4 during training once the student’s validation loss on the original objective, LEF (φ), becomes lower than that of the frozen FM, LEF (ψ)" (l.207-209). Further clarification on the role of this schedule, as well as the sensitivity to λKD, would be helpful. Would similar tuning or scheduling benefit the alternative approaches as well?

### Questions
* Why is there a tank in Figure 1?
* While the Hessian has a nice physical interpretation, as the authors point out, do higher derivates improve transfer further? One way to improve runtime in such cases would be to use Forward on Backward differentiation.

### Soundness
3

### Presentation
3

### Contribution
2
