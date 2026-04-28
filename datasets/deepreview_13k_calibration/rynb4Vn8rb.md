# DEQuify your force field: Towards efficient simulations using deep equilibrium models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Machine learning force fields show great promise in enabling more accurate force fields than manually derived ones for molecular dynamics simulations. 
State-of-the-art approaches for ML force fields stack many equivariant graph neural network layers, resulting in long inference times and high memory costs. This work aims to improve these two aspects while simultaneously reaching higher accuracy.
Our key observation is that successive states in molecular dynamics simulations are extremely similar, but typical architectures treat each step independently, disregarding this information.
We show how deep equilibrium models (DEQs) can exploit this temporal correlation by recycling neural network features from previous time steps. 
Specifically, we turn a state-of-the-art force field architecture into a DEQ, enabling us to improve both accuracy and speed by $10\%-20\%$ on the MD17, MD22, and OC20 200k datasets. 
Compared to conventional approaches, DEQs are also naturally more memory efficient, facilitating the training of more expressive models on larger systems given limited GPU memory resources.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors follow techniques proposed in [1], [2], and [3] to convert EquiformerV2 into a Deep Equilibrium Model (DEQuiformer), leading to improvements in accuracy and inference speed on MD17, MD22, and OC20 200k datasets. The benefits of DEQuiformer are primarily derived from the ability to re-use previously inferenced fixed points as initializations for the next frame's inference.

### Strengths
- Can trade off accuracy for simulation speed post-training very easily by modulating the fixed-point error threshold on the solver
- The model outperforms EquiformerV2 on training time
- The model outperforms EquiformerV2 on MD17, MD22, and OC20 200K in accuracy and inference time
- The authors empirically show that DEQuiformer successfully and stably converges to a fixed point during inference

### Weaknesses
 - Current work only applies to direct force prediction models
- No evidence that the technique could work on different model architectures
- No current comparisons with the inference times and accuracies of other model architectures

- A significant limitation is the exclusive focus on direct force prediction models. While the authors demonstrate speed improvements, the broader applicability is hindered by the fact that real-world molecular dynamics simulations often require forces derived from potential energy gradients to ensure conservation of energy. The lack of energy conservation in direct force prediction methods can lead to non-physical behavior in long simulations, raising concerns about the reliability of the results. This is particularly relevant for simulations requiring long time scales, where even small deviations from energy conservation can accumulate and lead to significant errors. 

- The paper does not explore the potential of DEQ methods with other model architectures. The current implementation is limited to EquiformerV2, and it is unclear whether the observed benefits would generalize to other architectures, such as those based on convolutional or recurrent neural networks. This limits the broader impact of the work, as it is not clear if the DEQ approach is a generalizable technique or one that is specific to the chosen architecture. Furthermore, the absence of comparisons with other models makes it difficult to assess the relative performance of DEQuiformer in the broader landscape of molecular simulation models.


### Questions
Questions
- On line 278: "Using consecutive samples would have the downside of a large variance in the results depending on the starting index, while 1000 uniformly spaced samples yield similar results to expensively testing on all > 100,000 data points." I'm not sure if I understand this. Depending on the starting index, the accuracy will have high variance compared to the accuracy on testing on all 100,000 data points? Given a fixed datapoint, does this mean the accuracy of the model is different depending on that datapoint's position in the overall sampled trajectory? I'm not sure if this should be the case.

- Do shock simulations where consecutive frames lead to vastly different atomic arrangements lead to different performance/timing results? Are there guarantees that fixed-point reuse leads to less solver steps? 


Limitations
- This is spoken in the limitations section, but I believe a very big drawback of the method is that it only applies to direct force prediction models. Real world molecular dynamics simulation necessitates forces to be formulated as gradients of energies to maintain important physical properties regarding the conservative nature of the force field. Although it's possible to run molecular dynamics simulation using a direct force prediction force field, it's still not clear whether this is trustworthy and safe to do so. Relaxations, on the other hand, don't as rigorously require conservative force fields but also don't require "millions to billions" of timesteps. Molecular dynamics is a fantastic beneficiary of the proposed speedup of inference, but the method isn't applicable at the moment.

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
4

### Summary
This paper applies Deep Equilibrium Networks (DEQ) [1] to EquiformerV2 [2], leveraging DEQ’s advantages of significantly reduced memory overhead and faster inference. The authors further enhance DEQ’s fixed-point solution by integrating temporal correlation from MD datasets as an initialization strategy, which would otherwise be computationally prohibitive. To validate their approach, they compare the performance of various EquiformerV2 and DEQ variants on the MD22, MD17, and OC20 benchmarks.

References:

[1]https://arxiv.org/abs/1909.01377

[2]https://arxiv.org/abs/2306.12059

### Strengths
1. Equivariant networks based on Transformer architectures are highly computationally intensive, requiring high-end GPUs and often taking multiple days to train. Any efforts to reduce this computational burden are valuable.

2. I commend the authors for applying the Deep Equilibrium Model (DEQ) approach to EquiformerV2. Integrating a fixed-point solver into the Transformer architecture—especially by adapting from TorchDEQ[1] and leveraging temporal correlation—is an impressive accomplishment.

References:

[1] https://github.com/locuslab/torchdeq

### Weaknesses
1. Temporal correlation in molecular dynamics (MD) datasets has been used effectively to initialize fixed-point solvers. I like this idea, but it relies on an assumption of ordered data, which breaks down during phase transitions. For instance, in the simple case of water melting, the transformation from solid to liquid occurs abruptly, disrupting the expected order and causing this approach to fail at the transition point. The issue is not just the abruptness of the transition, but the fundamental change in the underlying potential energy surface. The fixed-point solver, initialized with a structure from a different phase, may struggle to converge to the correct solution, potentially leading to inaccurate force and energy predictions. This is especially concerning if the simulation crosses multiple phase boundaries.


2. This approach also struggles with datasets that lack a clear temporal order, where entries are jumbled and any sense of sequence is lost (as noted by the authors for datasets like rMD17 and OC20). This limitation restricts the applicability of the method, impacting one of the core contributions of this work. The method's reliance on sequential data limits its use to datasets where the temporal ordering is preserved. This is a significant limitation because many real-world datasets are not sequentially ordered, or the order may be unknown. The authors should address how their method can be adapted to handle such datasets or provide a more detailed analysis of the types of datasets for which their method is best suited. Can you please discuss potential ways to address this limitation or expand on other potential applications where temporal ordering is preserved?

### Questions
Please also see weakness.

1. To clarify what part was contributed in this paper and taken from[1] can the authors write a pseudo code and highlight the lines? For instance: side-by-side comparison of the original DEQ algorithm and the authors' modified version for equivariant networks.

2.  In Fig 2 why at 0th iteration(for test error) the models start at such different errors? Happens to be that the model starting with lower initial error saturates at lower overall error at end of epochs. I am unclear if this performance gain is due to less parameters (less overfit)in DEQ or due to the time correlation introduced in this paper? Could you please compare DEQ models with and without the temporal correlation initialization, while keeping the parameter count constant?

3. I suggest to add a table with number of parameters across all models.

references:

[1]https://arxiv.org/abs/1909.01377

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
4

### Summary
This work develops and demonstrates a strategy for converting a deep network to deep equilibrium models for the task of machine learning inter-atomic potentials. The strategy is interesting and novel compared to other strategies in that area, and leads to improvements in both the accuracy and inference speed. By re-using solutions in the fixed point solver in subsequent time steps in a simulation, the inference speed is further improved. The results are demonstrated on a few diverse datasets including MD17, MD22, and OC20.

### Strengths
* The strategy is unlike other current approaches to improve ML for molecular simulations using typical message passing systems.
* The strategy works for both molecules and catalysts
* The performance (accuracy and inference speed) can be improved over a current leading model (EquiformerV2), though the EqV2 baselines were not thoroughly tuned for every experiment
* The authors considered possible edge cases and questions about the impact of the fixed point convergence settings on the final performance. 

The authors focus on the benefits of DEQ for accelerating MD simulations by re-using fixed point guesses, but I think there are even more important and influential directions that this paper will unlock. 
1. The underlying simulations for the training data are themselves ground state calculations that come from a self-consistent solver for the electronic structure, and there is a strong analogy between the methods in this work and the methods in the underlying solver. 
2. A subset of the community has been focusing on computing additional equilibrium properties in a system such as charge distribution, and those methods typically work by using standard message passing GNNs to compute an electronegativity and then solving for an equilibrium distribution of charge (e.g. Wai Ko, Behler et al. Nat Com 2021, or Deng, Cedar et al. Nat. Mat. Int. 2023 among many others). I think there is huge potential (pun intended) for this work to lead to large increases in performance in predicting these other ground state problems that require equilibrium across extended systems. Further, there’s probably connections between this work and other methods to accelerate the convergence of the underlying simulations themselves, perhaps by predicting the electron density itself.

### Weaknesses
 * As the authors point out, computing gradients of the resulting properties w.r.t. the atomic positions is difficult (but not impossible) and by not addressing this only direct-force models can be improved currently. This limits the applicability of the method, as many interatomic potential applications rely on energy gradients for molecular dynamics simulations and structure optimization. While direct force prediction is a valid approach, the lack of a clear path to energy-based predictions is a significant limitation.
* The baseline comparisons use model architectures tuned for larger systems. It would be preferable to compare results for the model here on published baseline models for the original (larger) datasets like OC20-2M so that it is clear the results are not simply due to better tuning of the DEQ-architecture compared to the baseline EqV2 architectures. The current comparisons, while showing improvements, do not definitively rule out the possibility that the performance gains are due to a more favorable architecture or hyperparameter tuning for the DEQ model on smaller datasets, rather than an inherent advantage of the DEQ approach itself. A more rigorous comparison would involve using the same model sizes and training procedures as the original publications on the larger datasets.
* The authors state that fixed-point re-use cannot be tested for OC20, but it is not clear to me why. Specifically, OC20 has an MD subset that could be used. Further, the authors could simply run a short-timescale MD simulation using the potential (say in ASE) to compare the inference time savings. The absence of these tests leaves a gap in the evaluation of the method's performance in realistic simulation scenarios. The potential for speedups through fixed-point reuse is a key claim, and its absence on a major dataset like OC20 is a significant oversight.
* Large variations in Table 1 are a bit suspicious (see question below) and decrease confidence in the conclusions for MD22. The reported force MAEs for MD22 exhibit substantial variability across different molecules and model configurations. This raises concerns about the robustness and reliability of the training process and the reported results. The large differences between 1-layer and 2-layer DEQ models, as well as the inconsistencies in the EqV2 baselines, suggest that the training might be unstable or that the models are not converging to consistent solutions.

### Questions
1. In Table 1 MD22, the force MAEs seem highly variable and perhaps highlight convergence/training stochasticity rather than intrinsic model differences. For example, in MD22/Stachyose, all EqV2 results are ~11, as well as DEQ (2-layer), but DEQ (1-layer is 0.31, 30X smaller). Similarly Ac-Ala3-NHME has a 10X larger force MAE for EqV2(1-layer). Any AT-AT/DHA have ~10-20X smaller force MAEs for DEQ than EqV2. Can the authors confirm the results in this table and/or improve the training consistency? I understand one of the points of DEQ is better training dynamics, but the Stachyose results suggest even with DEQ there’s significant stochasticity similar to the baseline.

2. How stochastic is the fixed point solver inside of DEQ2? Specifically, what is the likelihood that you find different solutions for the same inputs? This is probably especially important for molecular dynamics, as multiple possible solutions for the local potential energy surface could lead to interesting dynamics, or possibly history-dependent artifacts. 

3. The authors might want to consider training a model to predict the partial charges or magnetic moments in the mptrj dataset (similar to CHGNet) to greatly improve the applicability of this work. Obviously this is a significant additional experiment, but if these results were competitive there too I think this work would be much more compelling.

4. Experiments for inference-time speedup for simulations in OC20 are also possible, can the authors shed insight on whether the same speedups are seen there too?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work utilizes deep equilibrium models to enhance the accuracy, speed, and memory efficiency of EquiformerV2. Furthermore, DEQuiformer could accelerate molecular dynamics simulations by leveraging the similarity between successive states.

### Strengths
* This paper proposes incorporating DEQ into MLFF.
* Compared to EquiformerV2, DEQuiformer shows advantages.
* The paper demonstrates experiments on the rapid convergence of DEQuiformer's fixed points.

### Weaknesses
Lack of Innovation: Although this paper is, to my knowledge, the first to combine DEQ with MLFF, the concept of DEQ is based on the fixed-point property of neural network hidden states. This work seems to merely change the application scenario to MLFF without actual innovation. The core idea of leveraging fixed-point iterations for efficient computation is not novel, and the paper does not provide a theoretical analysis or empirical demonstration of why this approach is particularly well-suited for MLFF beyond the general benefits of DEQ.

In the introduction, the paper misses a lot of related works in the field, such as [1]-[6].

The paper highlights that in molecular dynamics simulations, because consecutive frames have similar configurations, the fixed point from the previous frame can be used as the initial trial for the next frame, thus accelerating the process. My concerns are as follows:
1. The experiments provided to support this point are insufficient. For example, it would be useful to compare the number of iterations with and without reuse. Additionally, molecular dynamic simulations should be performed to claim your points.
2. The paper mentions using a validation set of 50 samples from MD17, but Fig. 4b states it uses the validation set. Were these 50 samples selected in consecutive order? Additionally, the paper mentions selecting an extra 1000 consecutive samples. If these were used, they should not be considered part of the validation set. The authors should clarify to avoid reader confusion.
3. Fig. 4b is confusing. What is the percentage relative to? The figure needs a clearer explanation. The bars of the same color do not seem to sum up to 100%, which is unclear.
4. Is the acceleration effect of DEQuiformer primarily due to reuse or the reduced number of model layers? I suspect the latter is the main factor.

In conventional MLFF experiments, the MD17 test set includes all remaining data, while rmd17 provides a specific test set. However, this paper uses only 1000 data points from the MD17 test set, which is not a fair comparison.

The paper claims that the data split for MD22 is the same as for MD17, which is inconsistent with the original MD22 paper [7] and conventional MLFF splits[5,6,8,9].

The paper lacks results from other benchmark models for MD17 and MD22. Benchmarking with additional methods could provide a better evaluation of the results.

Why aren’t the energy and force tables for MD17 and MD22 combined? This makes it inconvenient for readers to compare the results. Additionally, the energy results for EquiformerV2 are exceedingly poor. Was the training fully converged? This could imply a bias in lowering the benchmark, making the comparison unfair.

I greatly appreciate that the authors included a limitations section, but I have some questions regarding certain points mentioned. The limitations section mentions uncertainty about whether DEQ is applicable to other MLFFs because EquiformerV2 uses a separate force output head. I don’t quite understand the logic here. Is DEQuiformer based on the assumption that forces have a fixed-point property? It seems to me that DEQuiformer assumes the hidden layers of molecular representations have a fixed-point property, so DEQ should theoretically be applicable to any model predicting any property, even if forces are obtained via autograd.

The presentation of the paper could be improved. For readers not very familiar with the field, more introductory content on concepts like equivariance and Equiformer should be added in the preliminary section.

### Questions
* Lack of Innovation: Although this paper is, to my knowledge, the first to combine DEQ with MLFF, the concept of DEQ is based on the fixed-point property of neural network hidden states. This work seems to merely change the application scenario to MLFF without actual innovation.
* In the introduction, the paper misses a lot of related works in the field, such as [1]-[6].
* The paper highlights that in molecular dynamics simulations, because consecutive frames have similar configurations, the fixed point from the previous frame can be used as the initial trial for the next frame, thus accelerating the process. My concerns are as follows:
1. The experiments provided to support this point are insufficient. For example, it would be useful to compare the number of iterations with and without reuse. Additionally, molecular dynamic simulations should be performed to claim your points.
2. The paper mentions using a validation set of 50 samples from MD17, but Fig. 4b states it uses the validation set. Were these 50 samples selected in consecutive order? Additionally, the paper mentions selecting an extra 1000 consecutive samples. If these were used, they should not be considered part of the validation set. The authors should clarify to avoid reader confusion.
3. Fig. 4b is confusing. What is the percentage relative to? The figure needs a clearer explanation.
4. Is the acceleration effect of DEQuiformer primarily due to reuse or the reduced number of model layers? I suspect the latter is the main factor.
* In conventional MLFF experiments, the MD17 test set includes all remaining data, while rmd17 provides a specific test set. However, this paper uses only 1000 data points from the MD17 test set, which is not a fair comparison.
* The paper claims that the data split for MD22 is the same as for MD17, which is inconsistent with the original MD22 paper [7] and conventional MLFF splits[5,6,8,9].

* The paper lacks results from other benchmark models for MD17 and MD22. Benchmarking with additional methods could provide a better evaluation of the results.

* Why aren’t the energy and force tables for MD17 and MD22 combined? This makes it inconvenient for readers to compare the results. Additionally, the energy results for EquiformerV2 are exceedingly poor. Was the training fully converged? This could imply a bias in lowering the benchmark, making the comparison unfair.

* I greatly appreciate that the authors included a limitations section, but I have some questions regarding certain points mentioned. The limitations section mentions uncertainty about whether DEQ is applicable to other MLFFs because EquiformerV2 uses a separate force output head. I don’t quite understand the logic here. Is DEQuiformer based on the assumption that forces have a fixed-point property? It seems to me that DEQuiformer assumes the hidden layers of molecular representations have a fixed-point property, so DEQ should theoretically be applicable to any model predicting any property, even if forces are obtained via autograd.

* The presentation of the paper could be improved. For readers not very familiar with the field, more introductory content on concepts like equivariance and Equiformer should be added in the preliminary section.

[1] Schütt, Kristof T., et al. "Schnet–a deep learning architecture for molecules and materials." The Journal of Chemical Physics 148.24 (2018).

[2] Gasteiger, Johannes, Janek Groß, and Stephan Günnemann. "Directional Message Passing for Molecular Graphs." International Conference on Learning Representations.

[3] Schütt, Kristof, Oliver Unke, and Michael Gastegger. "Equivariant message passing for the prediction of tensorial properties and molecular spectra." International Conference on Machine Learning. PMLR, 2021.

[4] Coors, Benjamin, Alexandru Paul Condurache, and Andreas Geiger. "Spherenet: Learning spherical representations for detection and classification in omnidirectional images." Proceedings of the European conference on computer vision (ECCV). 2018.

[5] Wang, Yusong, et al. "Enhancing geometric representations for molecules with equivariant vector-scalar interactive message passing." Nature Communications 15.1 (2024): 313.

[6] Wang, Zun, et al. "Efficiently incorporating quintuple interactions into geometric deep learning force fields." Advances in Neural Information Processing Systems 36 (2024).

[7] Chmiela, Stefan, et al. "Accurate global machine learning force fields for molecules with hundreds of atoms." Science Advances 9.2 (2023): eadf0873.

[8] Kovács, Dávid Péter, et al. "Evaluation of the MACE force field architecture: From medicinal chemistry to materials science." The Journal of Chemical Physics 159.4 (2023).

[9] Li, Yunyang, et al. "Long-Short-Range Message-Passing: A Physics-Informed Framework to Capture Non-Local Interaction for Scalable Molecular Dynamics Simulation." The Twelfth International Conference on Learning Representations.

### Soundness
2

### Presentation
2

### Contribution
2
