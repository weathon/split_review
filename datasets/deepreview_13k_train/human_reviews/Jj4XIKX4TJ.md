# Efficient molecular conformer generation with SO(3) averaged flow-matching and reflow

- Decision: Reject
- Scores: 5, 5, 6, 8, 6

## Abstract
Molecular conformer generation is a critical task in computational chemistry and drug discovery. Diverse generative deep learning methods have been proposed and shown to outperform traditional cheminformatics tools. State-of-the-art models leverage neural transport, employing denoising diffusion or flow-matching to generate or refine atomic point clouds from a prior distribution. Still, sampling with existing models requires significant computational expense. In this work, we build upon flow-matching and propose two mechanisms for accelerating training and inference of 3D molecular conformer generation. For fast training, we introduce the SO(3)-Averaged Flow, which we show to converge faster and generate better conformer ensembles compared to flow-matching and Kabsch alignment-based optimal transport flow. For fast inference, we further show that reflow methods and distillation of these models enable few-steps or even one-step molecular conformer generation with high quality. Using these two techniques, we demonstrate a model that can match the performance of strong transformer baselines with only a fraction of the number of parameters and generation steps. The training techniques proposed in this work lay the foundation for highly efficient molecular conformer generation with generative deep learning model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present AvgFlow, a framework for molecular conformer generation based on Flow Matching technology. The proposed approach aims to achieve rotation-awareness and faster sampling through two key improvements: SO(3)-averaging and a reflow strategy. Integrating and averaging over symmetrical groups of target conformers, the model aims to generalize on the SO(3) group. The authors show that the model converges faster compared to conditional OT and Kabsch alignment-based flow matching. Additional application of the Reflow strategy and further distillation allows the model to perform sampling with as few as two and one steps, respectively.

### Strengths
The paper introduces promising approach by leveraging Conditional Flow Matching and SE(3)-equivariant networks, along with averaging on SO(3) group and Reflow-distillation strategies that accelerate sampling. The integration of these technologies is cutting-edge, especially in the domain of molecular conformer generation — a critical task in drug discovery. The writing is mostly clear, and the overall framework reflects state-of-the-art approaches applied to an important problem.

### Weaknesses
Although the framework integrates several advanced components, each of these techniques is already actively explored in closely related domains, such as proteins and point clouds. There appears to be limited novelty in the adaptation of these methods for the conformer generation task. Moreover, the theoretical rationale and empirical evidence supporting the inclusion of each component could strengthen the novelty of the manuscript. The necessity of using SO(3)-averaging is not fully justified, and the reflow strategy, while reducing sampling steps, results in a noticeable decline in generation performance, without further discussion on the sampling step-generation quality trade-off. These concerns are described further in the questions below.

Below are some key points requiring further clarification or revision:

1. The paper mentions that the SO(3)-averaged flow is applicable when the integral over all rotations is tractable, though real data often do not meet this condition. However, the implementation details are sparse. How are the rotations sampled, and how many are used? Have the authors performed the hyperparameter search for such numbers? Since SO(3)-averaging is a core component, it is essential to clearly explain the sampling and averaging procedures. Authors should explain their implementation details in reference to FrameAveraging [1], one of the examples of similar application of rotation averaging in point cloud domain.  Additionally, the absence of source code limits transparency and reproducibility. Sharing the code—via supplementary materials or an anonymous repository—would enhance the AI community’s understanding of the framework and align with best practices for open research.

2. The model is built on the NequIP backbone, which is SE(3)-equivariant. Given this, it seems the network should already handle rotations without requiring explicit SO(3)-averaging. This additional step may function primarily as a data augmentation strategy, raising concerns about its necessity. A more thorough explanation is needed to justify why SO(3)-averaging is essential, beyond what the SE(3)-equivariant model offers by design.

3. The paper refers to the model as "model agnostic," but there is no clear discussion on how the framework transforms distributions from arbitrary priors. For example, DiSCO [2] recently proposed a Schrödinger bridge-based approach for conformer generation that achieves this transformation. It would be valuable for the authors to compare their approach with DiSCO, at least conceptually, to clarify how their framework embodies the claimed "model agnostic" property, which should be supported by how sampling can be performed from an arbitrary distribution instead of Gaussian prior.

4. While the reflow strategy and distillation techniques reduce the sampling steps, they also result in a significant drop in performance, especially in the GEOM-DRUGS dataset (Table 2). It is crucial to provide a deeper discussion on this trade-off, particularly since balancing performance with sampling efficiency remains a key challenge. Currently, the paper does not provide sufficient supporting evidences that the framework adequately addresses this balance.

5. In the section titled “AVERAGED FLOW LEADS TO FASTER CONVERGENCE TO BETTER PERFORMANCE,” the authors present epoch-based comparisons to demonstrate the efficiency of SO(3)-averaging. However, if each conformer undergoes multiple rotations before averaging, this effectively multiplies the training data per epoch. This process is similar to training with augmented data, which complicates comparisons with models that use only a single orientation per epoch. A more meaningful comparison would be based on training time or the number of batch iterations, rather than epochs.

### Questions
Below are some key points requiring further clarification or revision:

1. The paper mentions that the SO(3)-averaged flow is applicable when the integral over all rotations is tractable, though real data often do not meet this condition. However, the implementation details are sparse. How are the rotations sampled, and how many are used? Have the authors performed the hyperparameter search for such numbers? Since SO(3)-averaging is a core component, it is essential to clearly explain the sampling and averaging procedures. Authors should explain their implementation details in reference to FrameAveraging [1], one of the examples of similar application of rotation averaging in point cloud domain.  Additionally, the absence of source code limits transparency and reproducibility. Sharing the code—via supplementary materials or an anonymous repository—would enhance the AI community’s understanding of the framework and align with best practices for open research.

2. The model is built on the NequIP backbone, which is SE(3)-equivariant. Given this, it seems the network should already handle rotations without requiring explicit SO(3)-averaging. This additional step may function primarily as a data augmentation strategy, raising concerns about its necessity. A more thorough explanation is needed to justify why SO(3)-averaging is essential, beyond what the SE(3)-equivariant model offers by design.

3. The paper refers to the model as "model agnostic," but there is no clear discussion on how the framework transforms distributions from arbitrary priors. For example, DiSCO [2] recently proposed a Schrödinger bridge-based approach for conformer generation that achieves this transformation. It would be valuable for the authors to compare their approach with DiSCO, at least conceptually, to clarify how their framework embodies the claimed "model agnostic" property, which should be supported by how sampling can be performed from an arbitrary distribution instead of Gaussian prior.

4. While the reflow strategy and distillation techniques reduce the sampling steps, they also result in a significant drop in performance, especially in the GEOM-DRUGS dataset (Table 2). It is crucial to provide a deeper discussion on this trade-off, particularly since balancing performance with sampling efficiency remains a key challenge. Currently, the paper does not provide sufficient supporting evidences that the framework adequately addresses this balance.

5. In the section titled “AVERAGED FLOW LEADS TO FASTER CONVERGENCE TO BETTER PERFORMANCE,” the authors present epoch-based comparisons to demonstrate the efficiency of SO(3)-averaging. However, if each conformer undergoes multiple rotations before averaging, this effectively multiplies the training data per epoch. This process is similar to training with augmented data, which complicates comparisons with models that use only a single orientation per epoch. A more meaningful comparison would be based on training time or the number of batch iterations, rather than epochs.

References

[1] Puny, Omri, et al. "Frame Averaging for Invariant and Equivariant Network Design." *International Conference on Learning Representations* (2022).

[2] Lee, Danyeong, et al. "Disco: Diffusion Schrödinger bridge for molecular conformer optimization." *Proceedings of the AAAI Conference on Artificial Intelligence*. Vol. 38. No. 12. 2024.

### Soundness
2

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
This paper propose accelerate 3D molecular conformer generation by introducing SO(3)-Averaged
Flow for faster training and using reflow and distillation for rapid, high-quality inference.

### Strengths
1. The proposed method balances compute cost and performance.  
2. The proposed method removes the need for rotational alignment by averaging over data rotations.  
3. Faster inference is achieved.

### Weaknesses
1. In contribution (iii), it is proposed that Averaged Flow and reflow + distillation are model-independent, and whether there is any relevant
experimental support?
2. To compare the time consumption and computational cost of different steps in ET-Flow, please refer to Table 4 in ET-Flow[1]. If ET-Flow
uses fewer steps, how does the performance change? Is there a significant gap?
[1] ET-Flow: Equivariant Flow-Matching for Molecular Conformer Generation. NeurIPS 2024.
3. In section 3.1, please provide further details on the derivation of the relevant formulas.
4. Could you provide a comparison of different methods and different steps for generating conformers?

### Questions
1. In contribution (iii), it is proposed that Averaged Flow and reflow + distillation are model-independent, and whether there is any relevant
experimental support?  
2. To compare the time consumption and computational cost of different steps in ET-Flow, please refer to Table 4 in ET-Flow[1]. If ET-Flow
uses fewer steps, how does the performance change? Is there a significant gap?  
[1] ET-Flow: Equivariant Flow-Matching for Molecular Conformer Generation. NeurIPS 2024.  
3. In section 3.1, please provide further details on the derivation of the relevant formulas.  
4. Could you provide a comparison of different methods and different steps for generating conformers?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a SO(3) averaging flow matching for molecular conformer generation and adopts a reflow strategy to accelerate the sampling. The SO(3) averaging flow eliminates the need to align the source and target sample and improves the training efficiency by learning the expectation of the conditional vector field that points to the rotated version of the training example. The empirical results on the GEOM-QM9 and GEOM-DRUGS show that the method could reach the same level of performance but be more parameter efficient. The paper also investigates the necessity of the reflow strategy and how the number of sampling steps affects the model performance.

### Strengths
1) The SO(3)-Averaged Flow is a novel concept in which the learned probability path is SO(3) invariant, which could improve the generalization of the flow matching method and is model-agnostic.
2) The ReFlow strategy is investigated for the molecular conformer generation that 21 to 50 times speedup is achieved with a relatively small cost of the performance.
3) The author shows the learning curve the SO(3)-Averaged Flow converges better and much faster than the conditional / Equivariant OT flow matching.
4) The overall presentation is clear and easy to follow.
5) The author highlights a practical trick: the timestep t sampled from the exponential distribution rather than the uniform distribution.

### Weaknesses
1) The main concern I have is that with the SO(3) averaged flow, the method could potentially benefit more from scaling the model size since more model capacity is needed to learn the density to be SO(3) invariant. However, the author only shows the method could reach a comparable performance with less number of parameters. This causes a concern about whether the proposed method could be effective in a larger setting either with more model parameters or larger molecules. The current experimental results do not show how the method performs with more parameters. It's unclear if the parameter efficiency observed is a fundamental advantage or an artifact of the specific model size used. A more thorough investigation of performance scaling with model size is needed to validate the method's potential.

2) Part of the contribution is applying the reflow strategy, a commonly used method for accelerated sampling, to molecular conformer generation. The results are quite promising on the GEOM-QM9 dataset (Table 1), but on a larger dataset GEOM-Drugs (Table 2) the performance degrades significantly for both 'AvgFlow-reflow' and 'AvgFlow-Distill'. This first poses the concern about the necessity of applying the reflow to the problem with huge performance degradation, and second goes back to the question if the SO(3) averaging flow could benefit more from using a large model on a larger dataset. The performance drop with reflow on the larger dataset raises concerns about the robustness of the method and whether the reflow strategy is truly beneficial in this context. The significant degradation suggests that the reflow process may be introducing biases or instabilities, particularly when applied to more complex molecules.

3) I am also a bit concerned about the quality-speed tradeoff the author mentions in the paper. Ideally, both the accuracy and inference speed should be pushed at the same time. The current approach seems to prioritize speed at the expense of accuracy, which may not be desirable in all applications. It would be beneficial to explore methods that can improve both aspects simultaneously, rather than focusing on a tradeoff.

4) Section 3.1 is a bit unclear to me. From algorithms 1, it seems like the training is operated by augmenting the training set with different rotations. Hence, I am not quite sure about the meaning of presenting the idea with the symmetry group in section 3.1. If the author wants to justify the theoretical motivation and advantages, the writing could be improved by explicitly highlighting the theoretical results. The connection between the symmetry group presentation and the actual implementation is not clear, leading to confusion about the theoretical underpinnings of the method. The theoretical motivation needs to be more clearly articulated and linked to the practical implementation.

### Questions
1) Since the method is model-agnostic, how does the method perform using a larger model (transformer architecture from the MCF) from which it could potentially benefit?
2) What is the necessity for applying reflow to the method if there is substantial performance degradation?
3) What's the meaning behind those derivations from section 3.1? Does the author want to justify the method theoretically?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel flow matching training objective termed AvgFlow that incorporates the rotation symmetry in the loss objective to find a suitable path embodied as expected flow across all possible rotations from a prior distribution to the target distribution. Their experiments suggest that the AvgFlow objective results into faster training convergence and improved molecular geometries compared to recent flow matching objective which are the conditional OT and conditional OT + Kabsch alignment. 
Furthermore, the authors show that the inference process can be accelerated by using the Reflow procedure, to straighten the velocity paths during the ODE trajectory, and in extreme cases perform distillation to achieve a 1-step conformer generator.

### Strengths
The paper is well motivated to increase efficiency of flow matching models for 3d molecule conformer generation and fairly compared to the current SOTAs.

The experimental section to compare their AvgFlow objective against other flow matching objective *within* the same Nequip architecture is sound and isolates the effect of the training objective. The further analysis on Reflow and Distillation is also interesting and provides valuable insights for generative modeling in the field of molecular/conformer design.

### Weaknesses
The paper lacks sufficient detail regarding the loss function for the (conditional) flow matching objective in Eq. (7). 
While the authors mention that the target $u_t(x_t) = \frac{\partial}{\partial \alpha} \log Z_t(x, \alpha) |_{\alpha=0}$ I was not able to find the required information how to solve the integral from Equation (6) also when looking into https://arxiv.org/pdf/2006.09740. 
It would be helpful to either provide the code as supplementary information or state in the appendix how the regression target can be computed.



### Questions
Since I have raised my concerns about the lack of details in the Weaknesses section, it would be helpful if the authors could answer the following questions:

1) How can I understand $\hat{x}$ in Eq. (1) ? It is mentioned that $\hat{x}$ is a representative point of the orbit (Line 186) - Is it simply a ground truth conformer from the dataset? I.e. a molecule in a given orientation.
2) What are the $\{(A_t, b_t)\}$ exactly and what is their dimensionality ? If $x_1 \in \mathbb{R}^{N/times3}$, $A_t$ can either be a scalar or an $N \times N$ matrix? Is $b_t$ a constant $N\times3$ matrix? 
3) Equation (4) is not clear with respect to the dimensionality in the potential energy from the exponential function. Which norm are you using ? Is it a matrix norm?
4) How fast/expensive is it to compute the regression target ? In the Kabsch and cond-OT flow work presented by Hassan et al. (2024), usually an SVD has to performed - It seems from the Appendix in https://arxiv.org/pdf/2006.09740 in (34) multiple computational steps are also required to solve the integral.
5) Why wouldn't you simply increase the model size from AvgFlow to ~8M parameter and see how the model performs? This would be also a fairer comparison (on your side) against ET-Flow-SS. While the results in Figure 2 show that AvgFlow show improved performance against Cond. OT and (Cond OT. + Kabsch), the harmonic prior used in ET-Flow-SS might be also beneficial in your use case.
6) How is the sampling speed against ET-Flow-SS ? (Table 3)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed SO(3)-Averaged Flow (AvgFlow), which developed the average flow matching objective for faster convergence in training, and applied the technique of reflow and distillation for reduced ODE steps in sampling. AvgFlow achieves comparable performance to the flow matching counterpart with geometrically sophisticated designs in training on QM9, and slightly inferior on GEOM-Drugs.

### Strengths
- The authors further explored the application of flow matching for molecular conformer generation, which holds the potential of reducing generation time.
- This paper seems to be the first to develop the SO(3)-average flow matching objective.

### Weaknesses
Major:
- The method section is not clear enough. For example in Section 3.1, the authors claimed that the Monte-Carlo estimate of $\hat{x}$ risks introducing a bias, but without further explanation. This is related to Eq (7) where it is not clear on which the expectation is taken. The authors should explicitly compare their derived AvgFlow loss with the original flow matching objective, detailing the differences and highlighting where and why the differences arise. The derivation of the SO(3)-Averaged Flow objective lacks sufficient detail, making it difficult to assess the novelty and contribution. Specifically, the introduction of the Lie group and Haar measure in Eq. (1) needs more context and explanation for readers unfamiliar with these concepts. The paper should clarify the necessity of using these mathematical tools and provide references to their applications in similar contexts.
- This paper lacks enough novelty and empirical contribution. The theoretical part for AvgFlow objective is not elaborated thus the contribution is not immediately clear, the remaining reflow and distillation seems a direct application of known techniques in flow matching literature here. This would be okay, though, if the performance is strong enough. However, AvgFlow (together with the reflow and distill variants) appears not surpassing the performance of ET-Flow given comparable NFE (50~100), and the performance of fewer steps is not directly comparable, unless the author also uses the same reflow and distillation over ET-Flow. Therefore, the contribution of this paper is at least not adequately presented.

Minor:
- Line 169 should be \citep
- Line 312 "The Kabsch alignment objective is to rotationally aligning ..." -> "to rotationally align ..." Please check if there are more grammar errors.

### Questions
- What is the physical plausibility of generated conformers, i.e. not violating the physical constraint for molecules? For example, the PoseBusters [1] passing rate?
- Can the authors provide a more detailed description of baselines?

[1] https://pubs.rsc.org/en/content/articlehtml/2024/sc/d3sc04185a

### Soundness
2

### Presentation
2

### Contribution
2
