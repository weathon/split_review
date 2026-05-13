# Fourier Transporter: Bi-Equivariant Robotic Manipulation in 3D

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
Many complex robotic manipulation tasks can be decomposed as a sequence of pick and place actions. Training a robotic agent to learn this sequence over many different starting conditions typically requires many iterations or demonstrations, especially in 3D environments. In this work, we propose Fourier Transporter (\ours{}), which leverages the two-fold $\SE(d)\times\SE(d)$  symmetry in the pick-place problem to achieve much higher sample efficiency. \ours{} is an open-loop behavior cloning method trained using expert demonstrations to predict pick-place actions on new configurations. \ours{} is constrained by the symmetries of the pick and place actions independently. Our method utilizes a fiber space Fourier transformation that allows for memory-efficient computation. Tests on the RLbench benchmark achieve state-of-the-art results across various tasks.\blfootnote{Project website: \href{https://haojhuang.io/fourtran_page/}{https://haojhuang.io/fourtran\_page}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method called Fourier Transporter (FOURTRAN) to enhance the efficiency of training robotic agents in performing pick and place actions in 3D environments. By incorporating the bi-equivariant symmetry of the problem into a behavior cloning model, FOURTRAN utilizes a Fourier transformation to encode the symmetries of these actions independently, which enables memory-efficient construction and improves sample efficiency.

### Strengths
- The paper proposes FOURTRAN for leveraging bi-equivariant structure in manipulation pick-place problems in 2D and 3D.
- The paper presents a theoretical framework for exploiting bi-equivariant symmetry. It contains proofs for propositions that address the symmetry constraints and properties of the model.

### Weaknesses
 - The current model is limited in a single-task setting, while the baseline methods are designed for multi-task purposes. I'm concerned that the comparisons may not be fair.
- It relies solely on open-loop control, disregarding path planning and collision awareness.
- The paper is not well-written and some of the terms are difficult to understand. It uses a lot of notations, but many of them are not explained.
- There are no real robot experiments.

### Questions
- What is **fiber space** Fourier transformation?
- In Figure 2, how do you crop the object in the scene? What if there are multiple objects?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for taking advantage of bi-equivariance found in some manipulation problems (equivariance with respect to both the pick and the place pose) for representing distributions over pick-place actions, which exist in $\textrm{SE}(3) \times \textrm{SE}(3)$ and pose sample-efficiency challenges when represented without taking advantage of symmetry. The proposed method demonstrates very strong performance on a variety of imitation learning benchmarks, particularly those requiring fine-grained control.

### Strengths
The argument for a bi-equivariant policy is compelling. The use of Wigner D-matrices to represent an output distribution is very clever and (to my limited knowledge of the literature) seems novel. Their use in the place network to generate fast cross-correlations for bi-equivariance is definitely novel. All theory is well presented and seems well-backed, if a little dense at times to readers less versed in differential geometry and representation theory.

Empirical results are extremely compelling. The proposed method seems to strongly outperform some relatively strong baselines on very low-data BC tasks.

### Weaknesses
Weaknesses mostly center around presentation: the paper contains a lot of dense jargon, which is understandable given the material but could be improved:
 - Given that the Wigner D-matrix representation and corresponding 3D Fourier transform is the key insight that allows this action representation to work, it would be worth spending some more time to describe them in more detail. Specifically, the paper could benefit from a more intuitive explanation of how the Wigner D-matrices capture the rotational aspects of the pick and place poses, and how the 3D Fourier transform operates on these matrices. It is not immediately clear to a reader unfamiliar with representation theory how these mathematical tools are leveraged to achieve bi-equivariance.
 - Some pseudocode/method description would be welcome. The current description of the method lacks the necessary detail for a reader to implement the proposed approach. For example, the exact steps involved in the lifting operation, the computation of the cross-correlations, and the final prediction of the pick and place poses are not clearly laid out. This makes it difficult to fully grasp the practical aspects of the method.

Otherwise, further analysis of the representations introduced would be nice:
 - $\ell$ is introduced as a parameter, but there is no discussion of how this parameter affects the expressiveness of the representation or the computational cost. A more detailed analysis of the role of $\ell$ would be beneficial.
 - the number of rotations in the lifting operation is also not discussed in detail. The paper should provide some guidance on how to choose this number, and how it affects the accuracy and efficiency of the method. It's unclear if there's a trade-off between the number of rotations and the quality of the learned representation.

### Questions
Is it possible that $\textrm{SO}(2)x\mathbb{R}^3$-equivariance (2D rotational+translational) is actually more general if grasp dynamics are dependent on the object's orientation with respect to gravity?

It seems like $I_{60}$ is used in the lifting operation, but as far as I can tell there's no reason the set of rotations has to form a subgroup. Is this correct, e.g. could the granularity be increased by simply sampling more rotations (roughly evenly spaced in $\textrm{SO}(3)$) in this step?

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach for solving 2D and 3D pick and place tasks. The key innovation lies in leveraging Fourier transformation in fiber space to create a memory-efficient and sample-efficient bi-equivariant model. The paper provides theoretical analyses of the method and evaluates it in 2D and 3D simulation benchmarks. When compared to other methods on the RLBench (James et al. (2020)), this approach achieves a substantially higher success rate, and on the Ravens benchmark (Zeng et al., 2021), it demonstrates some improvements.

### Strengths
The paper shows novelty in the use of Fourier transformation in fiber space, leading to memory efficiency and enhanced sample efficiency for 3D pick and place tasks. Additionally, the proposed methods demonstrate superior performance compared to baseline approaches in select RLBench tasks.

### Weaknesses
While the paper demonstrates strong results on RLBench tasks, it's important to note that some tasks like "stack-blocks" and "stack-cups" primarily operate in 2D space, which may not fully reveal the strengths of the methods in 3D. It would be valuable to include additional
tasks that involve more 3D rotation angles, such as “put books on bookshelf”.

In section 5.3 2D Pick-Place results, the last line: ”It indicates that the
SO(2) × SO(2) equivariance of FOURTRAN is more sensitive to rotations.
”. Does “sensitive” means more precise or prone to noise? It would be interesting to conduct separate tests with high-resolution thresholds to distinguish the impact of position error and rotation error. For example, considering parameters like τ = 1cm and ω = 7.5° as well as τ = 0.5cm and ω = 15°. Additionally, a box plot of the rotation error would also provide more insight into the effect of the method.

Minor issues and typos

* The last line in 3 Background: Appendix C
* The last line on page 4: “Here the action on the base space rotates the pick location and the fiber action transforms the pick orientation.” should it be: “Here the action on the base space transforms the pick location and the fiber action rotates the pick orientation”?
* Page 7:  “The different 3D tasks are shown graphically in Figure 4” should be Figure 3
* Table 3: Success rate(%) of three......
* Page 15: icosohedral -> icosahedral

### Questions
In section 5.3 2D Pick-Place results, the last line: ”It indicates that the
SO(2) × SO(2) equivariance of FOURTRAN is more sensitive to rotations.
”. Does “sensitive” means more precise or prone to noise? It would be interesting to conduct separate tests with high-resolution thresholds to distinguish the impact of position error and rotation error. For example, considering parameters like τ = 1cm and ω = 7.5&deg; as well as τ = 0.5cm and ω = 15&deg;. Additionally, a box plot of the rotation error would also provide more insight into the effect of the method.


Minor issues and typos

* The last line in 3 Background: Appendix C
* The last line on page 4: “Here the action on the base space rotates the pick location and the fiber action transforms the pick orientation.” should it be: “Here the action on the base space transforms the pick location and the fiber action rotates the pick orientation”?
* Page 7:  “The different 3D tasks are shown graphically in Figure 4” should be Figure 3
* Table 3: Success rate(%) of three......
* Page 15: icosohedral -> icosahedral

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the fourier transporter, a neural architecture that explicitly captures the bi-equivariant relationships implicit in many pick and place tasks, that is, an object may exhibit rotational symmetry in both picking actions, and placing actions. The architecture first selects an appropriate pick pose using a network that outputs a distribution over picking actions (positions and orientations), with positions used to crop a region about the object to be placed.  This region is then lifted to form a stack of rotated features (a steerable filter) by a network to capture the rotational symmetry present in the picking action. The fourier transform of these features is applied, and used to perform cross-correlation (in the fourier domain, to allow for more efficient computation) with a feature map generated over the workspace observation to determine a distribution over placing positions.   A coarse to fine approach is used to refine the resolution of the pick and place actions, by sampling more rotations as required to refine the pick and place actions. Behaviour cloning experiments are conducted on a range of simulated 3D and 2D manipulation tasks (RLBench, Raven) and show improved success in terms of success rate as a function of training demonstrations. Ablations appear to indicate that most of the heavy work is done by the lifting operation.

### Strengths
The paper is well written and motivated, and does an excellent job of formalising the equivariance in robotic pick/place tasks, nicely mapping theory to practice.

The core contribution (applying the cross-correlation in the fourier domain) is a great way to reduce complexity and allow more lifting angles and finer resolution pick/place, particularly when combined with coarse to fine sampling.

Bi-equivariant networks provide a seemingly impressive boost in performance when compared to prior models that do not consider these symmetries.

### Weaknesses
The core weakness of this work is the strength of the contribution when compared to the equivariant transporter network proposed in Huang 2022. As far as I can tell key differences include generalising to 3D, more empirical experiments in this domain, and the implementation of the cross correlation in the fourier domain. As mentioned in this work, it is true that the Huang 2022 paper only considers SO(2), and is a subset of the general theory presented here, but more needs to be done to justify why the extension to 3D is non-trivial, particularly when it comes to the major claims of this work, greater angular resolution, computational benefits of fourier implementation, and sample efficiency. Specifically, the paper needs to more clearly articulate the limitations of extending the Huang 2022 approach to SO(3), and why the proposed method is necessary. The current presentation does not adequately highlight the computational intractability of a naive extension of the previous approach to 3D rotations, and the specific benefits of the fourier domain implementation in this context.

Along these lines, I would have liked to see an explicit experiment showing clear evidence of higher angular resolution performance (beyond the 15/7.5 degree results in table 2). The current experiments do not sufficiently demonstrate the advantage of the proposed method in scenarios requiring very fine-grained angular control, and it is unclear if the reported improvements are directly attributable to the higher angular resolution capabilities of the Fourier approach.

No error bars are provided in experiments (Tables 1/2), so we have no indication that the results are significant. I am sure they are, but this is important for the table 2 comparison with Huang 22.

The mapping between Figure 2 and the equations in Section 4 is incomplete, and not easily followed. Not all notation is clearly defined (eg. $Ind_{\rho l}, \rho_{irrep}, h$ etc.) and equations don't immediately use the network notations ($\psi, \phi$). I recognise that much of this notation is standard in group theory, but it is not in robot learning, so there would be value in defining this. This forces the reader to make assumptions/ spend significant time interpreting the mappings between text and figures, and hurts readability. I also recognise that this is out of a desire to formalise and explain the general problem before introducing the specifics of the architecture and approach taken to address this, but the current structure of this section/ group theory jargon made this difficult to follow.

### Questions
What level of rotational variation is present in the demonstrations and experiments? Is it possible to share some data on the typical distributions and tolerances in pick/place angles the tasks here require?

Could you explain table 3 in more detail - the  ablation here appears to undermine many of the choices this work makes. If a unet + data augmentation can capture many of the equivariance relations, and the lifting operation is the big contributor, then why do we need bi-equivariance? Is this simply an artifact of the test scenarios not adequately evaluating 3D equivariance symmetries?

In terms of the extension to 3D, it seems that the lifting operator introduces challenges around partial occlusions, that may be hard to learn regardless of the bi-equivariance structure. Could you comment on the general performance/ potential limitations in this regard?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
