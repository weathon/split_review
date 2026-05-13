# Learning Time-Dependent Density Functional Theory via Geometry and Physics Aware Latent Evolution

- Decision: Reject
- Scores: 8, 8, 6, 5

## Abstract
We consider using machine learning to simulate time-dependent density functional theory (TDDFT) to predict physical properties of molecules and materials beyond their ground states. In particular, by simulating the electronic response of the system under an external electromagnetic field, the optical absorption spectrum can be calculated using real-time TDDFT (RT-TDDFT), which provides physical information about the excited states and dipole strength function. However, RT-TDDFT simulation requires the direct propagation of electronic wavefunctions of all valence electrons for extended periods, making the process very time-consuming. In this work, we model electron density as volumetric data and train neural networks to map between coarse time steps. To make the model aware of the atomistic environment, we incorporate 3D message passing into the model architecture. Additionally, we use latent evolution to regularize the model towards learning the underlying physics. Our method is termed TDDFTNet. To evaluate our approach, we generate datasets using molecules from the MD17 dataset. Results show that TDDFTNet can learn the time propagation of electron densities accurately and efficiently.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new approach to accelerating RT-TDDFT simulations using machine learning. The authors design a novel neural network architecture called TDDFTNet that incorporates the 3D geometry of the molecule and uses a latent evolution approach to model the changes in electron density over time. The novelty of this method stems from the message passing architecture and time evolution in a physics-aware latent space. The method is evaluated on datasets of molecules from the MD17 dataset and shows promising results in accurately predicting the evolution of electron density and the optical absorption spectrum.

### Strengths
- The proposed TDDFTNet architecture is well-motivated and incorporates key physical constraints to ensure the model learns physically meaningful representations.
- The use of a latent evolution approach is novel in this context and allows the model to capture long-term dependencies in the data.
- The experimental results demonstrate the effectiveness of the proposed method in accurately predicting the evolution of electron density and the optical absorption spectrum.
- The ablation studies provided show a systematic improvement in results as different components of TDDFTNet are added.

### Weaknesses
 - The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future directions. For example, the current architecture is designed for isolated molecules; how can the method be extended to handle periodic systems or systems with explicit solvent molecules? Furthermore, the method is evaluated only for single photon excitations. How can the method be extended to handle more complex excitation scenarios, such as multiphoton excitation or strong field phenomena?
- The evaluation is limited to a small set of molecules from the MD17 dataset. It would be beneficial to see how the method performs on a larger and more diverse dataset, including more complex molecules and materials. The MD17 dataset is composed of relatively small organic molecules; it is unclear how well the method would generalize to larger molecules with more complex electronic structures, such as transition metal complexes or biomolecules. Furthermore, the dataset only includes ground state geometries. How would the method perform on excited state geometries?
- The paper would benefit from a more detailed comparison with the numerical simulation computation time. How well does this method perform against Octopus? How is the speed up if you run Octopus with a similar coarser grid? The paper should include a detailed breakdown of the computational cost of both the training and inference phases of the proposed method, as well as a comparison to the computational cost of traditional TDDFT calculations using Octopus. It is also important to compare the accuracy of the proposed method to that of Octopus for the same grid spacing.

### Questions
- The paper primarily evaluates TDDFTNet on small organic molecules. How well do you expect this method to generalize to larger and more complex systems, such as macromolecules or periodic systems? What modifications or extensions might be necessary to handle such cases?
-  The current work focuses on simulating the response to an impulse electric field. Can TDDFTNet be extended to study other excited state dynamics, such as those induced by different types of perturbations or those involving non-adiabatic transitions? Can we incorporate perturbation parameters or a continuously time dependent external potential in the model? How well would it generalize
- As mentioned in weakness, a more detailed comparison with Octopus would improve the paper. How are the computational costs if you incorporate training costs? This paper highlights the common pitfalls in ML-PDE works and might be a good framework for comparing TDDFTNet and Octopus: https://www.nature.com/articles/s42256-024-00897-5

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presented a novel machine learning (ML) approach for real-time time-dependent density functional theory (RT-TDDFT) simulations. Specifically, the authors modeled electronic density as volumetric data and incorporated a message-passing neural network (MPNN) for modeling atomistic interactions with ML. By training a deep neural network termed TDDFTNet with a part of the MD17 dataset, this paper showed that the proposed TDDFTNet can accurately and efficiently predict the time propagation of electron densities subject to an external pulse electromagnetic field.

### Strengths
### Originality
*I am not quite familiar with the recent literature on RT-TDDFT simulations. My reference comes from the `Related Work` section of this paper.*
1. The authors proposed an ML-based approach for RT-TDDFT simulations by discretizing the electronic density as volumetric data to simplify the representation of electron density as opposed to using basis sets in popular quantum chemistry theories.
1. The authors integrated message-passing for training TDDFTNet to model atomistic interactions.
1. The current literature on RT-TDDFT simulations is limited and this work provides a novel approach to address the challenges in RT-TDDFT simulations.

### Quality
1. The authors provided a detailed description of the problem setting and method in sections 3 and 4. Figure 2 is particularly helpful in representing the architecture of TDDFTNet.
1. The experiments and shown results are detailed and well-organized. The authors compared the performance of TDDFTNet on three molecules and compared the results with the ground truth from first-principle calculations by Octopus, an RT-TDDFT simulation software.

### Clarity
1. The paper is detailed in introducing the problem setting, method, the chosen experiment, and presenting the results.

### Significance
1. RT-TDDFT simulations are computationally expensive with first-principle calculations. Yet they are crucial for simulating molecules and modeling various physical properties. An efficient ML-based approach like TDDFTNet is significant for screening molecules and accelerating discoveries.
1. The TDDFTNet model is a good starting point for further research in RT-TDDFT simulations with ML.

### Weaknesses
 **The training and evaluation were done with the same molecules.**
- The authors chose three molecules, water, malondialdehyde, and ethanol, from the MD17 dataset. For each molecule, 1600 geometries were sampled for training.
- However, the results of the optical absorption spectra and predicted dipoles were reported on the same three molecules. Even though the reported results could be from a different set of geometries, this still brings concerns about information leakage and generalization of the model to unseen molecules.
- To address this, the authors could introduce two other sets of experiments:
    1. Use different sizes for the training set geometry samples and evaluate the model on the same three molecules. For example, report the performance when training with 200, 400, 800, and 1600 geometries per molecule. If similar accuracy can be achieved with fewer samples, then TDDFTNet could still be useful even if it suffers generalization issues.
    1. Train the model on one set of molecules and evaluate it on another set of molecules.

**The discretization of the electronic density as volumetric data limits the scalability of the model.**
- The results shown are for three small molecules and the authors did not discuss the scalability of the model to larger molecules.
- For larger molecules, the discretization of the electronic density as volumetric data could be computationally expensive and may not be feasible since large molecules come with larger volumes.
- In addition, the volumetric representation brings concern with the grid size/fidelity of the representation. The authors should discuss the impact of the grid size on the performance of TDDFTNet.

### Questions
The questions are highly related to the weaknesses mentioned above. The authors should consider addressing the following questions in addition to the concerns shared in the weaknesses section:
1. In the experiment, the authors trained and evaluated TDDFTNet on the same molecule(s). The current implementation seems to suggest a combination of fewer first-principle calculations and TDDFTNet for RT-TDDFT simulations on the same molecule(s). How does TDDFTNet generalize to unseen molecules? Could the authors provide results on the generalization of TDDFTNet to unseen molecules?
1. Is the TDDFTNet model scalable to larger molecules such as toluene, caffeine, or even larger molecules? How does the volumetric representation of the electronic density impact the scalability of TDDFTNet to larger molecules?
1. Does the grid size/fidelity of the volumetric representation impact the performance of TDDFTNet? Did the authors experiment with different grid sizes and evaluate the performance of TDDFTNet?

### Soundness
3

### Presentation
3

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
This paper proposes a method for learning the time-dependent electron density, which is particularly significant for applications in biological chromophores, quantum transport, and plasmonic catalysis. The neural TDDFT model predicts the time evolution of electron density using an encoder and a propagator module in an autoregressive manner.

### Strengths
- The paper introduces a physics-aware approach that enhances model performance in a convincing manner.
- By leveraging a valuable benchmark dataset from computationally intensive simulations and evalutation metrics, this work sets up new tasks and has the potential for significant impact on the community.

### Weaknesses
 - The paper does not include comparisons with 3D neural PDE models, such as GNO [1] and FNO [2], which could serve as valuable baselines. Specifically, the lack of comparison with FNO, which excels in learning global dynamics, is a missed opportunity to benchmark the proposed model's ability to capture long-range interactions in electron density evolution. The absence of GNO comparison is also notable, given its capacity to handle irregular geometries, which could be relevant for future extensions of this work.

- Unlike recent models for (static) electron density that aim to predict continuous densities [3,4,5,6], neural TDDFT relies on a grid-based training algorithm, which restricts the output to a fixed resolution. This grid-based approach limits the model's applicability to systems with varying spatial scales and could introduce discretization errors, especially when dealing with highly localized electron densities. The fixed resolution also prevents the model from being directly applied to adaptive mesh refinement techniques, which are common in computational chemistry and physics.


### Questions
- Does the output of electron density ensure normalization?
- How is optical absorption calculated? Additionally, the reason why optical absorption is important should be highlighted to enhance the understanding of this work.
- Why does the model rely on a grid-based approach, unlike coefficient-based or GNN-based methods?
- What is the impact of model error? How much error is acceptable to replace the conventional method, and is the model’s output sufficient in quality?
- Why is dipole loss included in the model’s loss function? Wouldn’t predicting the ground-state density difference accurately be enough?

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
3

### Summary
This paper proposes an algorithm to simulate the time-dependent density functional theory (TDDFT) and predict the properties of molecules. Compared to traditional simulators, NN-based methods can speed up the process. By using encoder, the method encoders atom types and atom coordinates into latent space, then with propagators to predict the density function as time evolution goes.

### Strengths
This paper does an interdisciplinary research for simulating the TDDFT with a neural network based method and provides some analysis about how to fit the network design with respect to specific physical science constraints.

### Weaknesses
1. This paper just simply combines neural networks into the physical sciences problems for predicting TDDFT for molecules. Due to the lack of comparison with other learning based methods and insufficient experiment results, I don’t see the novelty and effectiveness of this method from the learning perspective. Maybe this work is more appropriate for some physical science journals. 
2. This paper only does experiments on a very limited number of molecules and only provides in-distribution testing for these samples. I think the value of this method would be limited if it needs to train for each molecule individually. 
3. There is no comparison for this method with other state-of-art work but I think using neural networks to predict for molecules is a very popular topic.

### Questions
1. Why do the experiments only test on three molecules? Does each molecule need an independent model? And what is the result if the model is trained on one type of molecule but tested on another unseen molecule?
2. What about the comparison of TDDFTNet with other state-of-art learning based methods to predict properties of the molecules?
3. Please clarify what the three subplots in figure 4 is about.

### Soundness
2

### Presentation
2

### Contribution
2
