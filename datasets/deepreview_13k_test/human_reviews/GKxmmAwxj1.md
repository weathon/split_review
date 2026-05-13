# Scalable Normalizing Flows Enable Boltzmann Generators for Macromolecules

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
The Boltzmann distribution of a protein provides a roadmap to all of its functional states. Normalizing flows are a promising tool for modeling this distribution, but current methods are intractable for typical pharmacological targets; they become computationally intractable due to the size of the system, heterogeneity of intra-molecular potential energy, and long-range interactions. To remedy these issues, we present a novel flow architecture that utilizes split channels and gated attention to efficiently learn the conformational distribution of proteins defined by internal coordinates. We show that by utilizing a 2-Wasserstein loss, one can smooth the transition from maximum likelihood training to energy-based training, enabling the training of Boltzmann Generators for macromolecules. We evaluate our model and training strategy on villin headpiece HP35(nle-nle), a 35-residue subdomain, and protein G, a 56-residue protein. We demonstrate that standard architectures and training strategies, such as maximum likelihood alone, fail while our novel architecture and multi-stage training strategy are able to model the conformational distributions of protein G and HP35.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Based on previous works which use normalizing flows to generate distribution of conformations of proteins, this paper extends the scalability of NFs by (1) using internal coordinates instead of Cartesian coordinates (2) introducing 2-Wasserstein distance as training loss. (3) introducing new architecture. The proposed methods were proved useful in a small "protein" ADP and two larger proteins, in terms of distance distortion, energy and NLL loss.

### Strengths
This paper proposed to use internal coordinates instead of Cartesian coordinates, and split the backbone and side chain. From my point of view, this is the correct way to do protein conformation generation, since the Cartesian coordinates is redundant and highly correlated, whereas the internal coordinate is more compact and less correlated. I like this idea.

### Weaknesses
Please refer to the "questions" section.

### Questions
1. I didn't fully understand the exact difference between the proposed "new architecture" and NSF. Is GAU the difference, or something else? Could you illustrate the difference more explicitly. Thanks.
2. The experiment results are very good, but it is better to understand what is the key factor for the improvement by more ablation studies, such as NSF+NLL+KL+W2, Cartesian coordinate+your architecture+NLL+KL+W2, etc.
3. In Table 1, I notice that in Protein G and HP35, some energy are as large as 10^6 to 10^10. What are the reasons for these extremely high energies? If they are caused by some naive reasons, can we quick-fix them to make the comparison more fair?
4. In Table 1, NLL loss of Protein G is negative, why?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a flow architecture and training scheme that improves scalability of Boltzmann generators, allowing application to macromolecules.
The architecture operates on a subset of the internal coordinates (bond angles of side chains are held constant) - which is lower dimensional that the full set of internal coordinates (or cartesian coordinates) while still capturing the most important information on the protein's structure.
The authors introduce a 2-Wasserstein loss which encourages the flow to match the marginal distribution of the distance matrices of the backbone atoms, which leads to more realistic samples.

### Strengths
- The authors apply their method to larger molecules than much of previous literature - this is an important step away from toy problems like alanine dipeptide. 
- The addition of the Wasserstein loss helps the model generative more realistic molecules that don’t have clashes.

### Weaknesses
- Multi-stage training strategy introduces complexity that means significant more effort will be required to tune the algorithm. The third stage of training actually contains two stages. Although the rationale behind the individual losses is clear, the authors do not provide much rationale for each stage of the multi-stage training.
- The architecture is not novel and I do not think this is a significant contribution - internal coordinates have been commonly used, and fixing bond angles of side chains has also been done in literature.

### Questions
- What is the rationale/intuition behind each stage of the multistage training? For example, how come the Wasserstein loss is dropped for the final training period? Can this be unified into a single training stage (potentially with annealing of some loss coefficients)?
- The protein-G dataset introduced in the paper seems like it would be useful - will this dataset be released?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors create a tractable Boltzmann generator for medium sized protein molecules and show it can recapitulate realistic simulations.

### Strengths
Table 1 is very clean and interpretable. Generally, this is an ablation study baked into the main results of the paper, which is helpful. 

I think it is great that this method scales to something larger than alanine dipeptide! It makes me sad how frequently this is the only system a method is developed on.

I think Figure 3 is also good to show the examples of proteins that the authors are modeling. I think the figure would be improved by showing the secondary structure on the x-axis of the plot.

### Weaknesses
While I think the background section is helpful, sections 2.2 and 2.3 may be helpful to put into context when discussed in the method. While I realize they are described in detail in previous literature, it seems somewhat disjointed when all presented together.

Generally, I need some justification as to why ML models need to be fit to simulation data. Can’t I just run the simulation? What does this give us that a simulation doesn’t?

“For protein G, we use a von Mises base distribution for dihedral coordinates; we noticed that using a von Mises base distribution improved training for the protein G system as compared to a uniform or truncated normal distribution.” Why isn’t this consistent? While I like the Von Mises Distribution, it is odd to me that it isn’t consistent across proteins. As a reader, I want a method I can apply to any protein of interest, or heuristics on which probability distribution to use.

How was the training and test set defined for Protein G? I’d prefer for any notion of novel conformations to be independently confirmed by the simulation. For Figure 4b and 4c, would they never be observed during the simulation?

“An overlay of high-resolution, lowest-energy all-atom structures of protein G generated by the BG model. This demonstrates that our model is capable of sampling low-energy conformations at atomic resolution.” - I don’t think this conclusion is validated by the Figure in 4d. The most you can say is that it kind of looks like the same protein?

### Questions
How do “metastable” conformations differ from stable conformations?

For equation 3, for the upper triangle of a distance matrix, over the sum, one can potentially use the (i < j) notation.

“In addition, for larger systems, maximum likelihood training often results in high-energy generated samples.” What does this mean in practice?

Any reason in particular for 58 rotational quadratic spline coupling layers? Or any of the other subsequent number of coupling layers in section 4.1?

Table 1: “Results for ∆D and u(·) that are within tolerable range are bold-faced,” What is “tolerable range”?

Can you define RMSF? I only have a rough understanding of it based of RMSD.

What exactly is unstable during training of these methods? There is a number of works by John Ingraham et al showing instability during training of chaotic systems, particularly of proteins.

Figure 4a - What is the star? I don’t see this defined in the paper.

### Soundness
3 good

### Presentation
2 fair

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
The authors introduce a new flow architecture and training loss to train Boltzmann generators for large proteins. The flow architecture operates on internal coordinates of the backbone and the side chains, while bonds and bond angles of the side chain remain fixed. In addition to the commonly used forward and reverse KL divergence to train Boltzmann generators, they also employ a novel loss based on the distribution of the backbone all atom distance matrix. 
They show in their experiments on protein G and HP35 that their Boltzmann generator is capable of generating samples with low energies. Moreover, they show for protein G that their Boltzmann generator samples meta-stable states unseen during training.

### Strengths
- The paper is well written and easy to follow. 
- The authors introduce a new normalizing flow architecture, which uses preexisting building blocks. 
- The main novelty is the training with the 2-Wasserstein distance loss that measures the derivation of the all distance matrix for the backbone between Boltzmann generator samples and samples from the target distribution. 
- The new loss (in combination with the architecture) provides a way to scale Boltzmann generators to larger proteins
- Their experiments demonstrate that these trained Boltzmann generators produce samples with low energies, and in the case of protein G, they even generate structures that were previously unseen during the training phase.
- That the Boltzmann generators samples unseen states might allow to have non equilibrium training data that even misses some meta-stable states, which is important to gain advantages over traditional MD. 
- The work hast the potential to be an important contribution for the community.

### Weaknesses
- One of the main goals of Boltzmann generators is to generate samples from the equilibrium Boltzmann distribution. As the output distribution will usually differ from the target distribution, Boltzmann generators employ reweighting to the target distribution (Noe et al. 2019). This allows to generate unbiased samples from the target distribution with the Boltzmann generator. However, efficiently doing reweighting requires that the output distribution is close to the target distribution. This can be measured using Kish's effective sample size (ESS), using the reweighting weights. Hence, the ESS should be reported in the paper. Merely presenting the mean energy values of samples does not provide a comprehensive assessment of the Boltzmann generator's ability to efficiently generate samples from the equilibrium distribution. In addition, also reweighted energies distribution could be shown. 
- Boltzmann generators generally struggle to achieve a speed-up over traditional MD simulations, as they require data from these MD simulations to be trained.  The comparison presented in Figure 4 may not be entirely fair, given that generating Boltzmann generator samples necessitates the entire training dataset, which probably took considerably more time to generate than the test data.
- In general, it does not seem that the method could be made transferable, which makes it difficult to provide a real alternative to traditional MD simulations. 
- The authors should consider discussing this limitation in their work, along with citing relevant work on transferable models for MD acceleration, such as references [1, 2, 3], and the recent advancements in Boltzmann generators for molecules in Cartesian coordinates, e.g. [4, 5]. These could be directly trained in a transferable manner, unlike Boltzmann generators operating in internal coordinates.
- The code is currently not available

In summary, I believe that if the authors address these concerns, including reporting the ESS and discussing limitations, their paper has the potential to make a substantial and impactful contribution to the community.

[1] Bowen Jing et al. Torsional diffusion for molecular conformer generation. NeurIPS, 2022

[2] Leon Klein et al. Timewarp: Transferable acceleration of molecular dynamics by learning time-coarsened dynamics. arXiv preprint arXiv:2302.01170, 2023

[3] Xiang Fu et al. Simulate timeintegrated coarse-grained molecular dynamics with multi-scale graph networks. Transactions on Machine Learning Research, 2023.

[4] Leon Klein et al. Equivariant flow matching. arXiv preprint arXiv:2306.15030, 2023.

[5] Laurence I Midgley et al. Se (3) equivariant augmented coupling flows. arXiv preprint arXiv:2308.10364, 2023

### Questions
- The 2-Wasserstin loss is supposed to measure the distance between the backbone atom all distance distributions. However, from the notation in Equation (6) it seems as they measure the distance of the backbone bond and torsion angles.
- Only the mean energy is reported. Although this is computed with only samples with below median energy, I suspect that this mean might still be distorted significantly. Could the authors comment on how the energy distribution looks like when all high energy samples are discarded? In general, high energy samples will have nearly zero weight and are therefore not relevant if the rest of the samples have reasonable energies. Alternatively, one might consider reporting the minimal sampled energy in addition to the mean. That way, it is easier to see which methods do not generate any useful samples. 
- Can the authors elaborate on the time requirements for equilibrium Molecular Dynamics (MD) simulations in comparison to the time required for sampling with a Boltzmann generator?
- Have the authors attempted to train the baseline model using their proposed training method? This experiment could help discern the relative impact of the new loss function and the proposed architecture on the improved results.
- What does the energy distribution for HP35 look like? Is it close to the target distribution? What does the reweighted distribution look like?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
