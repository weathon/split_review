# Physics-Informed Weakly Supervised Learning for Interatomic Potentials

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 8, 6

## Abstract
Machine learning plays an increasingly important role in computational chemistry and materials science, complementing computationally intensive ab initio and first-principles methods. Despite their utility, machine-learning models often lack generalization capability and robustness during atomistic simulations, yielding unphysical energy and force predictions that hinder their real-world applications. We address this challenge by introducing a physics-informed, weakly supervised approach for training machine-learned interatomic potentials (MLIPs). We introduce two novel loss functions, extrapolating the potential energy via a Taylor expansion and using the concept of conservative forces. Our approach improves the accuracy of MLIPs applied to training tasks with sparse training data sets and reduces the need for pre-training computationally demanding models with large data sets. Particularly, we perform extensive experiments demonstrating reduced energy and force errors---often lower by a factor of two---for various baseline models and benchmark data sets. Finally, we show that our approach facilitates MLIPs' training in a setting where the computation of forces is infeasible at the reference level, such as those employing complete-basis-set extrapolation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose two self-supervised losses to train machine learning interatomic potentials. One is based on a Taylor-expansion approach, and the other is based on a consistency loss. They use these losses to train MLIPs on ANI, a TiO2 dataset, and some molecules in rMD17. They look at training models with mostly n=100 to n=1000 samples, and performance primarily on energy and forces prediction, as well as an example of running the molecular dynamics simulation.

### Strengths
- Self-supervised learning strategies for MLIPs are not very common, so it is nice to see some attempts towards developing these.
- Using these losses could be useful in cases where only energy labels are available, and not forces

### Weaknesses
There are many concerns I have with this method and actual utility in the broader scope of the MLIP literature.

- The results are not very convincing that this is a method that would actually get used. The authors are looking at a low number of data points, when larger datasets now exist. It is true that they are looking at more data points in the ANI dataset, though the level of accuracy and data generation of this dataset is suspect.

- In some cases, models can be trained by taking gradients of the energy to get a conservative force field, including cases the authors looked at. If this is the case, why do we need these losses? How do these losses compare in accuracy to taking gradients of the energy? This would make sense to do in datasets like rMD17 and other molecular datasets that have the forces.

- Stability analysis is only done for 3-6 ps which is very, very short. The models are also barely improving and still not usable, and it is not a good sign that it does not do well for such a simple molecule like aspirin. Why are the authors doing NVE simulations instead of NVT? Why not try NVT?

- The poor molecular dynamics performance means that these potentials are not very good, so they cannot be used for actual simulations.

- The authors say that they run NVE simulations and that this means the total energy is conserved. This is not necessarily true, because the authors may not have a potential that actually conserves energy. The authors can test actual energy conservation with their model.

- There is a line on 361 about “this observation indicates strong evidence of the effectiveness of PIWSL applied to bulk materials.” This is a very specific dataset (TiO2) and such claims are much greater than what is actually being presented. If the authors want to go towards such claims, they should be looking at datasets like the Materials Project, which is much more representative of bulk materials.

- Besides the above example, there are too many strong conclusions are being drawn from not great results to back these up, as these experiments are not being done on more representative datasets and sizes.

### Questions
- Do these loss terms help for more representative benchmarked datasets like Materials Project? Or MD22, which is a more representative dataset than MD17

- How does using these losses compare to taking energy gradients when the forces are known?

- Do the losses actually improve energy conservation?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a new pre-training method for MLIPs by augmenting the typical supervised loss with a physics-inspired loss (PIWSL). The proposed objective has a part that encourages the model to learn a conservative force field, and another part that ensures consistency of the potential energy surface based on a Taylor expansion around structure in the dataset. The authors conduct experiments on small datasets showing that their physics-informed loss improves performance compared to training just with supervision on energies and forces.

### Strengths
Strengths:
- The paper is written clearly and the method is motivated and presented well.
- Pre-training / self-supervised methods are important for the field of ML and could be particularly impactful for the field of MLIPs, where data is computationally expensive to generate.
- The proposed method is novel and physically motivated. It seems to be easy to implement programmatically and could be applied generally to any MLIP.

### Weaknesses
The main weaknesses are in the evaluation of the proposed method. In most other areas of ML, weakly-supervised learning is done with large datasets to learn general representations that can then be transferred / fine tuned downstream. However, in this paper, the experiments are done on extremely small datasets ranging in size from 100 - 1000 samples. This makes it hard to argue that the PIWSL serves as a useful objective, especially as the field migrates to larger datasets (OC20, MPTrj, SPICE, etc.). Concretely (roughly in order of importance):
- The experiments are done on extremely small datasets, making it hard to argue that the PIWSL helps the model learn useful representations (I suspect that any form of regularization would improve performance on datasets this small). On these small datasets, a non-deep learning based model like sGDML [3] outperforms all of the models tested in this paper in Table A9 by a large margin. It would be much more compelling if PIWSL still improved performance on the larger (1M+ samples) more common datasets (OC20, SPICE, MPTrj, full ANI-1x dataset, etc.).  
- Since the models are trained on such small datasets, the errors are currently huge (more than 10 kcal / mol across in almost all cases in table 1 for instance). Therefore, the improvement of ~1 kcal / mol with PIWSL still leaves the models with a huge error (reflected in the poor simulation performance in Figure 3.) As the dataset size increases, the improvement from PIWSL seems to decrease as well (mentioned by the authors in Fig. 2).
- The baseline NoisyNodes isn’t really a valid comparison since it is meant to only work for equilibrium structures. A much more valid comparison would be something like DeNS [1] that does work for the non-equilibrium structures that the authors test on.
- The models tested do not necessarily cover the state-of-the-art models for these types of molecular datasets. Equiformer and eSCN for instance are tuned for OC20 and are often outperformed by models like MACE [2] on molecular datasets. Something like MACE is also often able to get errors well below 1 kcal / mol with just supervision from energies and forces. If PIWSL still helped with these better models, that would be more compelling.

Weakly/self-supervised strategies have shown to be extremely effective in other fields of ML, and I am optimistic that methods like the ones presented by the authors will be important for MLIPs. However, the current evaluations in the paper do not provide convincing evidence that the current instantiation of PIWSL would actually help the best MLIPs when trained on large datasets. I would be happy to raise my score with more rigorous evaluations.

### Questions
- Why were the simulations done with the NVE ensemble (it makes it harder to compare to the work in Fu et. al. (2023) since they do an NVT with NoseHoover)? This is briefly discussed around line 400 but I feel like some results with NVT simulations could be helpful, since at the moment the NVE simulations yield very low stability.
- What happens if the models are trained explicitly to minimize curl as opposed to the PISC loss?

References:
[1] Yi-Lun Liao, Tess Smidt, Muhammed Shuaibi, & Abhishek Das. (2024). Generalizing Denoising to Non-Equilibrium Structures Improves Equivariant Force Fields. 
[2] Ilyes Batatia, Dávid Péter Kovács, Gregor N. C. Simm, Christoph Ortner, & Gábor Csányi. (2023). MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields
[3] Stefan Chmiela, Valentin Vassilev-Galindo, Oliver T. Unke, Adil Kabylda, Huziel E. Sauceda, Alexandre Tkatchenko, & Klaus-Robert Müller (2023). Accurate global machine learning force fields for molecules with hundreds of atoms. Science Advances, 9(2), eadf0873.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes an extended loss for the training of machine learning interatomic potentials. Two additional terms are added in the loss, the physics-informed Taylor-expansion-based consistency (PITC) loss and the physics-informed spatial-consistency (PISC) loss. The idea behind these terms is to generate additional approximate training data points by a first-order Taylor expansion of the energy at a given training data point. The goal is to increase the robustness of the machine learning interatomic potential for applications in this training approach. The approach is validated in several benchmarks.

### Strengths
- The approach appears to provide consistently better results.
- The approach is independent on the machine learning potential model.
- The approach can be easily integrated in other projects.

### Weaknesses
 - The potential energy curve of the C-H bond is badly represented in both cases, with and without PIWSL. For me, the argument is not strong if it still fails but not as badly. Maybe this has just to be trained to better/more (400, 800) training data and then both will give good results. To show the advantage of PIWSL, I think you have to find the sweet spot where PIWSL can already deal with a low amount of data and the conventional approach fails due to the lack of data. You could then also add a graph, where both approaches are trained on more data and both succeed to demonstrate that it is really the more efficient data handling of PIWSL. I think, the reference and predicted curves should at least agree in the range where the relative energy is below about 2 kcal/mol, because this region will be sampled in molecular dynamics simulations. However, especially the error for bond increases in plot d appears very large (>1 kcal/mol), currently.
- The approach increases the computational time required for training significantly.

### Questions
- Are the reported E and F RMSE values for training or test data?
- If I understand it correctly, the training was stopped after a per-defined number of training epochs. However, the PIWSL method requires 2-3 times more training time due to the additional calculation. I think a fair comparison would be to reduce the number of training epochs for PIWSL by a factor of 2-3 or otherwise increase the number of training epochs for the baseline approach. You could also just use the wall-clock time as stopping criterion instead of a given number of epochs. Did you check the convergence of the baseline approach? You could add learning curves to validate the convergence.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work presents a physics-informed, weakly supervised approach for training machine-learned interatomic potentials. The method is innovative, and the ideas are inspiring. However, it may not be practical for real-world applications, highlighting the need for further validation and case studies. Additionally, the improvements in experimental results are minimal, particularly with the rMD17 dataset, a common benchmark.

### Strengths
1. The work introduces a physics-informed, weakly supervised approach for training machine-learned interatomic potentials.
2. The method is innovative, and the ideas are truly inspiring.

### Weaknesses
The proposed method may not be practical for real-world applications, highlighting the need for further validation and case studies. Specifically, the method's reliance on a physics-informed loss function, while theoretically sound, may introduce biases or limitations when applied to complex systems with diverse chemical environments. The lack of extensive testing on a variety of materials beyond the rMD17 dataset raises concerns about the generalizability of the approach. Additionally, the improvement in experimental results is minimal, particularly with the rMD17 dataset, which is a common benchmark. This dataset, while widely used, may not be sufficiently challenging to demonstrate the advantages of the proposed method, given its relatively homogeneous nature and limited structural diversity. The reported error reductions are not substantial enough to justify the added complexity of the physics-informed training, especially when compared to simpler, data-driven approaches.

### Questions
In training MLIPs for small molecules, there is usually a substantial amount of data available (over 1,000 samples). How effective is the proposed method with a larger dataset of small molecules?

How effective is training on datasets for large molecules, such as the MD22 dataset?

### Soundness
4

### Presentation
3

### Contribution
3
