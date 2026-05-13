# A Multi-Grained Group Symmetric Framework for Learning Protein-Ligand Binding Dynamics

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
In drug discovery, molecular dynamics (MD) simulation for protein-ligand binding provides a powerful tool for predicting binding affinities, estimating transport properties, and exploring pocket sites. There has been a long history of improving the efficiency of MD simulations through better numerical methods and, more recently, by augmenting them with machine learning (ML) methods. Yet, challenges remain, such as accurate modeling of extended-timescale simulations. To address this issue, we propose NeuralMD, the first ML surrogate that can facilitate numerical MD and provide accurate simulations of protein-ligand binding dynamics. We propose a principled approach that incorporates a novel physics-informed multi-grained group symmetric framework. Specifically, we propose (1) a BindingNet model that satisfies group symmetry using vector frames and captures the multi-level protein-ligand interactions, and (2) an augmented neural ordinary differential equation solver that learns the trajectory under Newtonian mechanics. For the experiment, we design ten single-trajectory and three multi-trajectory binding simulation tasks. We show the efficiency and effectiveness of NeuralMD, with a 2000$\times$ speedup over standard numerical MD simulation and outperforming all other ML approaches by up to ~80\% under the stability metric. We further qualitatively show that NeuralMD reaches more stable binding predictions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Authors  propose a principled approach that incorporates a novel physics-informed multi-grained group symmetric framework. Specifically, we propose (1) a BindingNet model that satisfies group symmetry using vector frames and captures the multi-level protein-ligand interactions, and (2) an augmented neural ordinary differential equation solver that learns the trajectory under Newtonian mechanics.

Authors devised NeuralMD, an ML framework that incorporates a novel multi-grained group symmetric network architecture and second-order ODE Newtonian dynamics, enabling accurate predictions of protein-ligand binding dynamics in a larger time interval.

### Strengths
1. Authors have quantitatively and qualitatively verifed that NeuralMD achieves superior performance on 13 binding prediction tasks.
2. Authors showed the efficiency and effectiveness of NeuralMD, with a 2000× speedup over standard numerical MD simulation and outperforming all other ML approaches by up to ~80% under the stability metric.

### Weaknesses
One potential limitation of this work is the dataset. Currently, authors are using the MISATO dataset, a binding simulation dataset with a large timescale. However, NeuralMD is agnostic to the time interval, and it can also be applied to binding dynamics datasets with time interval as a femtosecond. The lack of empirical validation on datasets with smaller time intervals, such as femtosecond-scale molecular dynamics simulations, makes it difficult to fully assess the generalizability of the proposed method. Furthermore, while the authors claim a 2000x speedup over standard numerical MD, the practical implications of this speedup are not fully explored. For instance, the computational cost of training the NeuralMD model is not discussed, which is crucial for evaluating the overall efficiency of the method. It is also unclear how the accuracy of NeuralMD scales with the size and complexity of the protein-ligand systems, which is an important consideration for real-world applications.

### Questions
1. Authors qualitatively show that NeuralMD reaches more stable binding predictions. Is there a way to shoe quantitatively as well.
2.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a geometric deep learning framework for MD simulation of protein-ligand complexes. It is composed of a BindingNet model to represent a protein-ligand complex at multiple levels and a neural ordinary differential equation (ODE) solver to predict the trajectory under Newtonian mechanics. The method is evaluated on a recent large-scale MD simulation benchmark MISATO and shows state-of-the-art performance on multiple benchmarks. Importantly, it achieves a 2000x speedup over standard numerical MD simulation methods.

### Strengths
* This paper proposes a physics-informed architecture that involves Newtonian mechanics in trajectory inference. 
* This paper presents a comprehensive evaluation on protein-ligand binding MD simulation benchmarks.
* The proposed model shows state-of-the-art performance on multiple benchmarks.
* The proposed method is scalable, with 2000x speed up compared to standard MD simulation tools.

### Weaknesses
 * This paper lacks ablation studies illustrating the benefit of different components.
* The description of evaluation metric is not crystal clear (see questions below)

### Questions
1. Can you present ablation studies by replacing your BindingNet architecture with other existing geometric architectures such as EquiFormer and EGNN? 
2. Can you conduct ablation studies to understand the benefit of multi-level protein-ligand representation? I am not sure if having multi-level representation is helpful
3. For the MAE and MSE metric, is the MAE/MSE calculated over the whole trajectory (every time step) or only the final step?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work proposes a fast numerical MD method for simulating the protein-ligand binding dynamics in a large time interval. This method consists of two main modules: (1) a physics-informed multi-grained group symmetric network to model the protein-ligand complex, and (2) a second-order ODE solver to learn Newtonian mechanics. The proposed method can achieve 2000× speedup compared to the numerical MD methods and outperforms other ML methods on 12 tasks.

### Strengths
1.	The author proposed NeuralMD, an ML framework that incorporates a novel multi-grained group symmetric network architecture and second-order ODE Newtonian dynamics, enabling accurate predictions of protein-ligand binding dynamics in a larger time interval. 
2.	The authors are the first to explore a large-scale dataset with binding dynamics released in May 2023.
3.	NeuralMD offers a 2000× speedup over standard numerical MD simulation and outperforms other ML approaches by up to ~80% under the stability metric.
4.	NeuralMD not only achieves good performance in single-trajectory binding dynamics predictions, but also has good generalization ability among multiple trajectories.

### Weaknesses
1.	This work is based on the first large-scale dataset with binding dynamics, which may have its own limitations. Specifically, the dataset may exhibit biases or artifacts due to the simulation methods used to generate it, and these could impact the generalizability of the proposed method. The lack of variety in simulation conditions, such as temperature, pressure, and the specific force fields employed, could limit the applicability of the model to different scenarios.
2.	The paper does not provide a direct comparison with other state-of-the-art methods in terms of computational efficiency. While a 2000x speedup over standard numerical MD is mentioned, a more detailed analysis of computational cost, including FLOPS, memory usage, and wall-clock time, compared to other ML-based MD methods is missing. This makes it difficult to assess the true practical advantage of the proposed method.
3.	The article briefly mentions protein-ligand binding dynamics but does not further explain their importance and how such dynamics can be modeled. In addition, the article does not adequately discuss the interactions between proteins and ligands and how these interactions can be incorporated into the simulations. For instance, the specific types of interactions (e.g., hydrogen bonds, hydrophobic interactions, electrostatic forces) and their representation within the model are not clearly defined.
4.	The paper does not discuss the potential limitations or drawbacks of the NeuralMD framework. This includes potential issues with numerical stability for long simulation times, sensitivity to hyperparameter choices, or the model's ability to handle large conformational changes. A more thorough discussion of these limitations would be beneficial.
5.	The paper does not delve deeply into the practical implications or real-world applications of the proposed method. It would be valuable to discuss how this method could be used in drug discovery, protein engineering, or other relevant fields. The lack of discussion on how the method could be applied to more complex systems or to predict binding affinities is a significant oversight.
6.	The language of the article is somewhat poorly formulated, with some grammatical errors and spelling mistakes.

### Questions
1.	The paper states that the speed of this method is superior to standard numerical MD simulation methods, but this method is only compared with one method and is not compared with ML-based MD simulation methods. Please explain the reasons for this and compare it with more methods to prove the efficiency of the proposed method.
2.	The title of the article mentions a "multi-grained group symmetric framework", but not enough experimental results were provided to prove its effectiveness.
3.	The methods section of the article mentions "BindingNet model that satisfies group symmetry using vector frames and captures the multi-level protein-ligand interactions" but does not explain in detail how this model captures the multi-level interactions. interactions", but does not explain in detail how this model captures the multi-level interactions. Could you provide more details or examples to illustrate this point?
4.	The proposed method only is evaluated on one dataset, which might be specific to the used dataset. The authors need to evaluate their method on other datasets and compare it with more methods.
5.	How does the ML approach discussed in the article compare with other ML methods used for simulating protein-ligand binding dynamics? What is the advantage of the ML method used in this work compared to others? 
6.	The article does not describe in detail the specific methods used for the experiments; for example, in the case of protein-ligand binding dynamics simulations, no specific information on the simulation software used, simulation conditions, model parameters, etc. is mentioned. This makes it difficult for the reader to understand and assess the feasibility of the experimental methods.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to learn a 2nd order neural ODE which emulates molecular dynamics trajectories of ligand-protein interactions from the Misato dataset. The force prediction is done via a new architecture called BindingNet, which is based on 3 levels of frames (ligand, protein atom, protein residue) and which is claimed to be SE(3)-equivariant. The method is shown to be more accurate than diffusion-based next-step predictors and more stable than simulating the dynamics with a learned force field.

### Strengths
* It is encouraging to see the first works make use of the MISATO dataset, which contains a wealth of information about the very difficult problem of protein-ligand binding.
* Directly learning the long-timescale dynamics with a neural ODE rather than a fixed-timestep next-step predictor is an interesting idea which merits broader exploration.

### Weaknesses
 * Problem formulation. Although learning a neural ODE for long-timescale dynamics is an interesting idea, the deterministic problem formulation seems inappropriate as MD simulation itself is not necessarily deterministic. Thermostats and barostats typically introduce stochasticity, and even in their absence the removal of water molecules (which are explicit in the MISATO simulations) injects intrinsic uncertainty into the modeling problem. Hence, the dynamics are fundamentally stochastic and I am skeptical that any neural ODE can faithfully capture the long-timescale dynamics of these protein-ligand systems.

* Performance and baselines. Even in the single-trajectory setting, the MAE for the ligand coordinates seems rather large, in the range of 2-6 angstroms. This is perhaps due to the suboptimal problem formulation already discussed. However, the numbers provided are not meaningful because we do not know what the RMSF is in these simulations. The RMSF is the best result that can be achieved by a single static structure and is an essential missing baseline. The MAE in the multi-trajectory setting is even larger (7 anstroms) and suggests a complete dissociation of the ligand from the binding pocket. Finally, the stability metrics are only marginally better than DenoisingMD and do not represent a qualitative resolution of the problem.

* Misleading title. “Group symmetric” suggests a much more general framework than SE(3)-equivariance, and the key contribution of the paper is not the equivariant architecture in my opinion.

* Mathematical errors. Although the paper places much emphasis on SE(3)-equivariance, the construction of the atom-level and residue-level frames appears to be non-equivariant. Specifically, the cross product is not translation equivariant since
$$(x_i + t) \times (x_j + t) = (x_i \times x_j) +  (x_i - x_j) \times t$$
is not a function of $(x_t\times x_j)$ and $t$. Noticeably, the appendix claims the cross-product to be SE(3)-equivariant but only establishes rotation equivariance. Further, while I agree that the local frame construction described in the appendix is equivariant, this is different from what is done in the main text, since there is no nearest-neighbor atom $x_k$ and absolute positions $x_i, x_j$ are used.

Justification for score. Although the paper is a commendable attempt to learn from MD data, I am not convinced that the problem formulation makes sense, and the experimental results are rather weak. The frame based architecture is not a significant technical advancement over existing frame architectures and appears to have flaws.

### Questions
* The architectural details in Eq 5 and Fig 4 are very unclear, with several ambiguous uses of the dot product. Please label the embeddings with the dimensionality (so it is clear if they are scalars or vectors) and define symbols before they are used (for example $h_i$). It is also not clear what kind of MPNN is used and what is the meaning of the number of "layers."
* Please clarify if by MAE you mean RMSD or some alternative definition of positional error (with or without a factor of $\sqrt{3}$)
* "We keep the same backbone model (BindingNet) for energy or force prediction for all the baselines." If so, please provide significantly more details about how these baselines were retrained.
* If this work considers the semi-flexible, how did you deal with the protein movement that is present in the MISATO MD trajectories?
* What is your integration timestep? If it is adaptive, please provide more details about how many timesteps are required for a typical 8ns simulation.
* In the single-trajectory setting, how is the temporal division carried out?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
