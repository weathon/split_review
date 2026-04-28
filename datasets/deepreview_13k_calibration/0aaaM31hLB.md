# Learning Symmetries through Loss Landscape

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Incorporating equivariance as an inductive bias into deep learning architectures, to take advantage of the data symmetry, has been successful in multiple applications such as chemistry and dynamical systems. The build of equivariance architecture, particularly w.r.t. roto-translations, is crucial for effectively modeling geometric graphs and molecules, where the understanding of 3D structures enhances generalization. However, despite their potential, equivariant models often pose challenges due to their high computational complexity. In this paper, we study the capabilities of unconstrained models (which do not build equivariance into the architecture) and how they generalize compared to equivariant models. We show that unconstrained models can learn approximate symmetries by minimizing additional simple equivariance loss. By formulating equivariance as a new learning objective, we can control the level of approximate equivariance in the model. Our method achieves competitive performance compared to equivariant baselines while being 10x faster at inference and 2.5x at training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates unconstrained models for handling data symmetry. The authors demonstrate that by designing a loss function specifically tailored for learning equivariance, unconstrained models can approximate data symmetry by minimizing this equivariant loss. This approach allows the models to efficiently control the level of equivariance while maintaining flexibility.

### Strengths
- The paper is well-written and presents the core ideas in a clear and accessible manner.
- Using a "landscape" to describe the benefits of unconstrained models is particularly novel and insightful.

### Weaknesses
 - The study introduces this equivariant loss without providing a strong theoretical foundation for the proposed approach. Also, the proposed method is quite straightforward, and its distinction from data augmentation is unclear. It essentially computes the loss on a larger augmented dataset by sampling transformed data.   I suspect this method is already well-known within the community, which limits the novelty of the contribution.

- The experimental comparisons are performed on a limited set of classic models rather than state-of-the-art models, raising concerns about the practical applicability of the method to more advanced techniques.

### Questions
Please address my concerns in the weakness part, especially the novelty of the proposed method and the theoretical foundations.

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
4

### Summary
The paper introduces an augmented loss function that incorporates a measure of average equivariance, aiming to enhance the prediction of approximately equivariant information. The authors validate this approach on both equivariant and non-equivariant tasks, utilizing transformer and graph neural network architectures. Furthermore, they conduct a visual analysis of the loss landscape, comparing two different architectures: Transformer with the augmented loss and GATr without.

### Strengths
1. The augmented loss function is generalizable across various architectures.

2. The augmented loss function requires relatively few samples to work effectively making it computationally efficient.

### Weaknesses
The proposed methodology can be described as approximate equivariance, but the paper lacks an adequate background and comparative analysis against existing works on approximate equivariance. This raises concerns about both the novelty and the empirical validation of the approach.

1.  Novelty: Augmented loss functions enforcing approximate equivariance have been studied (e.g. [1]) including an average measure (e.g. [2]).

2. Empirical Support:  The paper does not benchmark against other methods that address approximate equivariance (e.g., [1]), nor does it consider theoretically grounded approaches to symmetry breaking (e.g., [3], [4]) or simpler strategies like combining SE3Transformer with MLPs.

### Questions
1. To address fundamental concerns, I recommend a more comprehensive background and analysis, alongside broader empirical comparisons. Specifically, the study should include a wider range of architectures that go beyond strictly equivariant and non-equivariant models, particularly for the motion capture task, which is inherently non-equivariant.

2. In practice, if a single randomly sampled group element is used per sample in each training step (as mentioned at the end of Section 3.1), this should be explicitly stated in Section 3.2 where the sampling procedure is discussed and the number of samples M is introduced.

3.  The paper lacks heuristic, theoretical and/or empirical justification for the choice of one group element per sample per training epoch sufficient. As a result the particular choice of measure is understudied.  Moreover, it remains unclear how the equivariance error is measured in Section 6. How many samples are used for this computation?

4.  It's entirely unclear if the difference in the loss landscape is a result of the augmented loss function or a result of the architectural difference. I would strongly recommend performing comparisons with a fixed architecture.

5. The MD17 dataset includes two regression targets: energy and forces. Please clarify in the text which target is being used (likely force regression) and how the results are generated.

6. Near the end of Section 6.2, the statement "Best performance is observed at an intermediate level of equivariance..." is confusing. Since the paper modifies the loss function, not the architecture, this needs further explanation for supporting the proposed methodology. Otherwise, the conclusion is simply to not utilize strict equivariant architectures for non-equivariant tasks.

### Soundness
2

### Presentation
2

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
The paper attempts to build equivariance into unconstrained models by posing equivariance as a constrained optimization problem, which can, in turn, also control the level of approximate equivariance in the models. The authors demonstrate results in N-body dynamical systems, motion capture, and molecule dynamics, and they analyze the effect of the level of approximate equivariance on task performance.

### Strengths
- The paper is well-motivated and clearly written (particularly the sections on background and methods).
- The limitation section discusses an important limitation of the interplay between optimization paths and loss landscape.
- The experiments are conducted in different domains and examine several essential aspects of the algorithm, giving more insights into the method and how levels of equivariance can affect downstream task performance.

### Weaknesses
 - **Related work**:
   - Although the paper uses equivariance as a constrained optimization problem and discusses it in the context of unconstrained models, it misses several crucial relevant works. Discussion of these works would help to place the submission in the literature and give a view of how this work differs from and compares to existing works.
  - Learning equivariance from data [1, 2], approximate/soft equivariance [3, 4, 5, 6], equivariance as a constrained optimization problem [7, 8], and equivariance with unconstrained models [9, 10, 11, 12].
  - Can the authors highlight the differences from Sec 3.2 of [13]?

- **$\beta$ and $\alpha$ as hyperparameters**:
  - The authors suggest that the level or extent of equivariance can be controlled with $\beta$ and $\alpha$ - is there a formal way to define this "level" of equivariance or is it an intuition tied to the loss itself, i.e., higher $\frac{\beta}{\alpha}$ indicates more equivariant? 
  - Next, how would someone know the optimal level of equivariance while using your proposed algorithm - $\beta$ is not learned, and the results indicate that the optimal $\beta$ can be identified from the test data results, which is not ideal. Rephrasing this, how do you know how much equivariance is required for the task, and thus what values of $\alpha$ and $\beta$ to set?


- **Methodology**:
  - How will your algorithm work if group $G$ is unknown?
  - How can your method reasonably approximate equivariance if $G$ is very large and the duration of training is not enough?
  - The highest level of equivariance is when $\alpha = 0$ and $\beta=1$. However, this is equivalent to data augmentation, which does not guarantee exact equivariance. Can your algorithm guarantee exact equivariance?
  - While the trends are consistent for both metrics, as reported in the paper, it might be helpful to discuss which metric - Eq. 9 or Eq. 10 is better suited for evaluation. How does Equation 9 work (or make sense) when $f(x)$ is non-scalar?
  - For Motion Capture, if the symmetry constraints are already known, instead of complete SE(3) equivariant baselines, why didn't the authors select appropriate equivariant models that are equivariant to the required SE(3) subgroup or consider symmetry breaking [14, 15]? What $G$ did your algorithm use? If it is the subgroup of SE(3), then it is an unfair comparison.

- **Minor spelling errors**:
  - L156 "requiring equivariant into" should be "requiring equivariance in"
  - L396 "it is" should be "its"

### Questions
- How will your algorithm fare when there are data constraints? Equivariant models are inherently data efficient, but your algorithm does not seem to be.
- The loss landscape plots depend on the selected directions - so how can we infer from just two random directions that the loss landscape is better for Transformers or GATr? The optimization paths should affect, and although it is discussed to some extent in limitations, it would be better if there is more discussion on this.

Most of the other questions I had are listed in the Weaknesses section. I will be happy to improve the score if the authors address the questions and weaknesses with supportive evidence during the discussion phase.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors analyze the application of unconstrained models in equivariant tasks by conducting a comprehensive analysis of unconstrained models, comparing their performance and computational efficiency against equivariant models. Besided, the authors introduce a novel, simple loss function that enables these models to approximate symmetries, which can be optimized during training.

### Strengths
Relaxing equivariance is a valuable research direction that can break through the constraints on generalization or expressive power caused by strictly equivariant operations.

### Weaknesses
1. The primary concern is the authors' motivation. The idea of using group transformations for data augmentation is native, but for many equivariant tasks, it is challenging to obtain a general model through data sampling due to the bias introduced by limited sampling. For instance, for point clouds or molecules, sampling across all angles would expand the dataset by hundreds of times and still struggle to enable the model to effectively learn fine-grained rotation equivariance. I suggest the authors validate their approach on common 3D datasets such as QM9 or ModelNet40.

2. The authors base their introduction in the first three sections on general equivariance, yet the impact of different equivariance groups on algorithms varies. For example, permutation equivariance and translation equivariance can be directly covered by simple operations, making the paper's method inapplicable. The authors should specify which equivariant tasks their method focus on.

3. Relaxing equivariance is a widely discussed topic, and the authors lack relevant citations and analysis [1] [2] [3] [4]. Moreover, the main advantage of unconstrained models is their ability to learn more complex features. It is worth noting that strictly equivariant operations can limit the expressive power of GNNs [5] [6], but unconstrained models may surpass these limitations. Additionally, some tasks are not strictly equivariant, allowing unconstrained models to be applicable. The authors' emphasis on the lower computational complexity of unconstrained operations is incorrect. In the 3D domain, models like torchmd are strictly equivariant yet have low complexity.

    [1] Residual pathway priors for soft equivariance constraints, Finzi, et al.

    [2] Approximately equivariant networks for imperfectly symmetric dynamics. Wang, et al.

    [3] Relaxing equivariance constraints with non-stationary continuous filters. van der Ouderaa, et al.

    [4] Learning Partial Equivariances from Data. Romero, et al.

    [5] On the Universality of Rotation Equivariant Point Cloud Networks. Nadav Dym, Haggai Maron. 

    [6] On the Expressive Power of Geometric Graph Neural Networks. Chaitanya K. Joshi, Cristian Bodnar, Simon V. Mathis, Taco Cohen, Pietro Liò.

4. I do not understand how the loss surface in Figure 1 was created and why it demonstrates the advantages of unconstrained models.

5. There are numerous issues with the paper's presentation:

    (a) The equations in lines 218, 224, and 227 lack numbering.

    (b) In line 215, the definition of G is finite, which is problematic for integrals where the group size can be infinite. Most groups mentioned in the paper are infinite, and I do not understand why the authors restrict groups to being finite in their initial definition.

    (c) All the references have formatting issues because none of them specify the source of the papers. For instance, "Equivariant Graph Hierarchy-Based Neural Networks" in your paper is accepted in NeurIPS 2022, not arxiv.

    (d) Appendix B is incomplete; several titles are clustered together without any explanatory text.

### Questions
See weekness.

### Soundness
1

### Presentation
3

### Contribution
1
