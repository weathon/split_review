# Learning local equivariant representations for quantum operators

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Predicting quantum operator matrices such as Hamiltonian, overlap, and density matrices in the density functional theory (DFT) framework is crucial for understanding material properties. Current methods often focus on individual operators and struggle with efficiency and scalability for large systems. Here we introduce a novel deep learning model, SLEM (strictly localized equivariant message-passing) for predicting multiple quantum operators, that achieves state-of-the-art accuracy while dramatically improving computational efficiency. SLEM's key innovation is its strict locality-based design, constructing local, equivariant representations for quantum tensors while preserving physical symmetries. This enables complex many-body dependence without expanding the effective receptive field, leading to superior data efficiency and transferability. Using an innovative SO(2) convolution technique, SLEM reduces the computational complexity of high-order tensor products and is therefore capable of handling systems requiring the $f$ and $g$ orbitals in their basis sets. We demonstrate SLEM's capabilities across diverse 2D and 3D materials, achieving high accuracy even with limited training data. SLEM's design facilitates efficient parallelization, potentially extending DFT simulations to systems with device-level sizes, opening new possibilities for large-scale quantum simulations and high-throughput materials discovery.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a data driven method to solve KS-DFT. Instead of solving the KS system to consistency, this method puts the configuration of atoms through a carefully designed SO(2) neural network and directly predicts the quantum operators at self consistency. While there are many other existing works trying to accomplish the same thing, the key technical contributions of this paper can be summarized as the following two points:

- The SLEM architecture, compared to traditional methods, SLEM has a strictly local design, its effective cutoff does not increase as more layers are added. This architecture is more scalable/parallelizable because the dependency is much smaller.
- The parameterization of the invariant overlap operators, which enables the prediction of overlap operator without requiring lots of parameters.

The above innovations is verified to be effective in the empirical evaluations on various systems. The advantages reported include 

- Better generalization due to the more restricted model assumption.
- Better scaling behavior w.r.t angular momentum.
- Faster iteration speed and smaller memory footprint.

### Strengths
- The two key contributions are novel, they are clearly explained in the paper and based on my understanding they are technically sound.
- The strictly local structure is significant and likely to be widely adopted in the future given the nice properties, not only more parallelizable, but also leads to lower errors.

### Weaknesses
I have a major concern on the way the evaluation is carried out

- The training and testing happens on the same system using trajectories of molecular dynamics. Although this type of evaluation may be also used in the baselines that the author compare to, I feel it is not sufficient. A good generalization is not surprising if the MD trajectories have a good coverage of different atomic geometric configurations. We run into the chicken egg dilemma, if DFT is already calculated on a system, why would we need to fit a blackbox model and do it again faster. In my opinion, the evaluation should be performed across different materials in a combinatoric way, i.e. train on material made of `AB` and `BC` and `AC`, evaluate on material made of `ABC`. Or on materials that contain same elements but in different proportions, i.e. train on `1A2B` and evaluate on `2A1B`.

Another concern is on the theoretical soundness

- Based on my understanding, only atoms pairs the has a distance smaller than rcut is considered, which means that the interaction between atomic orbitals from distant atoms are not considered, however, the operator needs to include all pairs of interactions to form a matrix. How are the noninteracting entries of the matrix set?
- Although the empirical study favors a strictly local structure, it is unintuitive theoretically. For example, the hartree term in DFT is a slow decaying term, using `(ij|kl)` to represent the four center integral, and `(i|j)` as the overlap; When `(i|j)` and `(k|l)` are both large, the `(ij|kl)` term is not negligible even when `ij` is distant from `kl`. It would added to the soundness of this paper if the authors could provide a theoretical support.
- With the above said, it is crucial to discuss the limitation of this method, i.e. in which scenario would this method fail due to the strictly local assumption.

### Questions
My questions are stated in the above concerns, I would be happy to raise my score if the authors address them.

### Soundness
4

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
5

### Summary
The paper introduces Strictly Local Equivariant Message-passing (SLEM), a deep learning model designed to predict multiple quantum operator matrices, such as Hamiltonians, density matrices, and overlap matrices, within the density functional theory (DFT) framework. SLEM tries to address key challenges in efficiency and scalability that traditional methods face when handling large quantum systems. The authors validate SLEM’s performance across 2D and 3D material systems, demonstrating high accuracy for the experiments.

### Strengths
By focusing on a strictly localized equivariant message-passing framework, the authors present a creative way to address the challenges of efficiency and scalability in quantum mechanical computations. The use of SO(2) convolutions to manage high-order tensor complexity is particularly novel, as it reduces the computational burden associated with f and g orbitals.

The methodological rigor of the paper is detailed theoretical justifications for the design choices of SLEM. The authors provide mathematical foundations for the model's ability to preserve physical symmetries while maintaining strict locality utilizing quantum mechanical properties. The paper is well-organized, with a logical flow from the problem motivation to the model formulation and experimental validation. 

The contributions of this work is important, especially for the fields of quantum chemistry and materials science. The ability to efficiently predict quantum operators without expanding the receptive field could accelerate DFT calculations and open new possibilities for simulating large-scale quantum systems.

### Weaknesses
The experimental comparisons presented in the paper are limited to only two other models, and these comparisons are not consistently provided for all experiments. Expanding the range of baseline models, including more well-established methods, would strengthen the validation of SLEM’s computational efficiency, scalability, and accuracy. Incorporating additional well-known benchmark datasets, such as QH9 [1], nablaDFT [2], and potentially QM9 [3, 4] (used in models like HamGNN), could provide a more reliable and widely recognized basis for evaluation. This would help clarify the practical advantages of SLEM more comprehensively. Additionally, while the authors conduct in-house simulations for some datasets, details about these datasets are not provided. More transparency about the data generation process and the choice of neural network potentials for sampling MD simulations would address concerns about the accuracy, quality, and reproducibility of the dataset. Given that datasets are often created using well-established computational methods like DFT, clarifying these choices would be beneficial.

Moreover, the mathematical formulation of SLEM is quite complex and may be difficult for practitioners who are not experts in quantum mechanics or advanced tensor operations. Providing a more accessible explanation or simplified overview could make the approach more approachable. Additionally, combining some of the experimental tables into one could improve readability and streamline the presentation.

In addition, the mathematical formulation of SLEM is highly complicated and could be difficult to implement for practitioners not deeply familiar with quantum mechanics and advanced tensor operations. The paper could be improved by providing a more accessible explanation. Furthermore, some of the experiment tables can be merged into one which would improve the readibility.

### Questions
1) What was the reason for selecting only two models for comparison with SLEM, and how were these models chosen? Would you consider expanding your evaluation to include additional, widely recognized benchmark datasets, as previously suggested?

2) In the computational scalability analysis, SLEM was compared with E3NN. However, I noticed that E3NN’s performance metrics, such as MAE, were not included in the accuracy tables. Did E3NN achieve better accuracy compared to SLEM, even if it was more computationally expensive?

3) The paper states that structures for the Si, GaN, and HfO₂ systems were sampled via molecular dynamics using neural network potentials. Since these potentials may introduce approximations relative to traditional quantum mechanical methods like DFT, could you clarify the potential impact on the quality and reliability of your training data? How do you ensure that these approximations do not compromise the accuracy and generalizability of SLEM’s predictions?

4) Could the authors share more details about the in-house simulations used for data generation, such as specific parameters and configurations? Providing this information would greatly aid in the reproducibility of the study as well as the quality of the data.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces SLEM, a model for predicting quantum operator matrices that achieves state-of-the-art accuracy and improves computational efficiency. It is strictly local and uses a SO(2) convolution technique, enabling it to handle systems with heavy atoms and high angular momentums while maintaining efficiency. The work shows experimental validation across various materials, demonstrating better performance in both accuracy and computational cost compared to existing methods

### Strengths
The main innovation and strength of this paper is combining strict locality, with an architecture heavily inspired in Allegro, with the SO(2) convolution trick, offering a compelling solution to handling heavy atoms and large systems efficiently while maintaining accuracy. The work can be considered well validated through comprehensive benchmarks, and they demonstrate the previous claims of both improved accuracy and reduced computational costs compared to state-of-the-art methods. The authors also create new datasets, and making them available would improve this paper's impact

### Weaknesses
A major limitation of the paper is its insufficient demonstration of transferability. While the authors show good performance on individual systems, they train and evaluate on the same type of material (e.g., training on Si and testing on Si configurations). There's no evaluation of cross material transferability. For instance, training on light elements and testing on heavy elements, or training on one crystal structure and testing on another. Also, the parallelization benefits, while promising (and I believe them, since they should be inherited from Allegro), are mainly theoretical with regards to this paper. The paper lacks concrete scaling studies on large systems or benchmarks on multiple GPU setups that would validate their claims about improved parallelizability.

### Questions
1) Are there specific cases where you expect the strict locality assumption to break down? The method perhaps could not handle systems with strong electronic correlations.
2) It is not clear from the paper (at least I could not find it) which is the cutoff used, or if different cutoffs were used for different systems. This could enable comparing the receptive field of the model proposed in this paper and other approaches using message-passing.
3) Evaluating the model performance in a transferability task would enhance significantly the submission.
4) Evaluating the scaling of the model in a multigpu setting would also enhance significantly the submission.

### Soundness
3

### Presentation
3

### Contribution
3
