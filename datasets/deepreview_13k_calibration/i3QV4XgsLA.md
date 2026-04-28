# EquiJump: Protein Dynamics Simulation via SO(3)-Equivariant Stochastic Interpolants

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 3, 6, 5

## Abstract
Mapping the conformational dynamics of proteins is crucial for elucidating their functional mechanisms. While Molecular Dynamics (MD) simulation enables detailed time evolution of protein motion, its computational toll hinders its use in practice. To address this challenge, multiple deep learning models for reproducing and accelerating MD have been proposed drawing on transport-based generative methods. However, existing work focuses on generation through transport of samples from prior distributions, that can often be distant from the data manifold. The recently proposed framework of stochastic interpolants, instead, enables transport between arbitrary distribution endpoints. Building upon this work, we introduce EquiJump, a transferable SO(3)-equivariant model that bridges all-atom protein dynamics simulation time steps directly. Our approach unifies diverse sampling methods and is benchmarked against existing models on trajectory data of fast folding proteins. EquiJump achieves state-of-the-art results on dynamics simulation with a transferable model on all of the fast folding proteins.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors present a novel equivariant network that predicts  states from an MD trajectory. Presented results look convincing, but unfortunately the State of Reproducibility is not written and the model/code are not available for evaluation.

### Strengths
The network generalizes on multiple protein families and outperforms the SOTA results.

### Weaknesses
It will be useful to assess the stereochemical quality of the produced intermediate protein structures using standard metrics, ProCheck and/or Molprobity. 

A minor point -- It will be also useful to formally prove SO(3) equivariance of the architecture blocks (without reading the original papers).

### Questions
Is it possible to check if the simulated trajectory stays on a closed manifold in the phase space and evaluate its (shadow) Hamiltonian? Would it make sense?  Please try to estimate the phase space volumes and/or energy fluctuations over time.

Please provide ProCheck/Molprobity Ramachandran plot statistics, bond lengths/angles, clash scores, and overall statistics. Please compare these to the values computed on the MD trajectories.

Please provide mathematical proofs or empirical demonstrations of equivariance for the key components of their architecture that are not directly taken from prior work, otherwise please explain the key equivariance components of the prior work, such as equivariant linear layers, etc.

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
In the paper, the authors introduce the EquiJump framework to generate protein dynamics simulation trajectories. Based on the stochastic interpolants framework, the authors capture the conditional probability distribution at different time to generate the whole trajectory. Additionally, the paper extend the interpolants on geometric features and design new network architecture. Experiments on 12 fast-folding proteins show the empirical performance of the framework.

### Strengths
1. The presentation of the method is very clear and easy to understand.

2. To the best of my knowledge, the modification of the stochastic interpolants framework for generating protein dynamics is novel.

3. Employing stochastic interpolants to generate trajectories is a well-founded and rational approach.

### Weaknesses
1. I believe it is essential to conduct comparative analyses with other baseline methodologies to establish the efficacy of your approach. For instance, utilizing a Machine-Learned Force Field (MLFF) that incorporates your network architecture could serve as a viable baseline. Such a comparison could demonstrate that your interpolants method outperforms the MLFF, independent of the network design, thereby highlighting the strengths of your technique.

2. I have observed that the sampling process within the current framework is rather inefficient and time-consuming. Therefore, it would be beneficial to include a comprehensive comparison of computational costs between the EquiJump framework and preceding MLFF methods. Such an analysis would be instrumental in assessing the practicality and efficiency of the EquiJump framework in relation to established techniques.

3. It is also crucial to engage in a detailed discussion on contemporary methods of trajectory generation. References [1-4] represent concurrent studies in trajectory generation. Providing a clear delineation of the distinctions and relationships between your work and these existing studies will help elucidate the unique contributions and advancements your research offers to the field.

### Questions
See the weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes new methods for speeding up protein dynamics simulation using neural networks. The core novelty lies in the development of novel architectures termed EquiJump. This network is shown to recover protein dynamics as measured by trajectory error in 3D as well the evolution of free energy metrics over time.

### Strengths
A substantive assessment of the strengths of the paper, touching on each of the following dimensions: originality, quality, clarity, and significance. We encourage reviewers to be broad in their definitions of originality and significance. For example, originality may arise from a new definition or problem formulation, creative combinations of existing ideas, application to a new domain, or removing limitations from prior results. You can incorporate Markdown and Latex into your review. See https://openreview.net/faq.

The proposed architectural novelty is high with clear descriptions of the new elements. Although I suggest in figure 4, where the architecture is drawn to use consistent naming across the various panes, e.g. what is called the ‘deep network’ in panel (c) becomes the ‘conditioner’ in panel (d) …. Also two panel c’s appear in the figure etc.

The experiments are done on a dataset of 12 folding proteins, which appear to a standard point of comparison. 

I appreciated the representation of molecular data using geometric features, although it was unclear what the irreducible representation is here (Lie algebraic coordinates?).

### Weaknesses
Although the architecture is novel, it is less clear how it is motivated, and why this particular combination works. This also ties in to comparisons, as only one primary comparison point is used – CGMLFF. It is unclear why this specific baseline was chosen, and a more comprehensive comparison against other state-of-the-art methods in protein dynamics simulation is needed to contextualize the performance of EquiJump. The lack of ablation studies on the different components of the architecture further obscures the contribution of each part to the overall performance.

Rotation data representation was unclear – ‘irrep’ would benefit by a clearer definition. Does using special approaches like this, does it reduce the parameterization of the rest of the network? The description of the irreducible representation (irrep) as features in bases of spherical harmonics is still somewhat vague. A more precise explanation of how these features are constructed and used within the network is needed, including the specific order of spherical harmonics used and how they are incorporated into the network's computations. Furthermore, it is not clear how this representation impacts the overall parameterization of the network and whether it leads to a more efficient or compact model.

It would be also important to consider model size when comparing to other models, e.g.  total number of parameters of the network for CGMLFF is noted as 294,565. Would also be useful to see training curves for the models. The absence of training curves makes it difficult to assess the convergence of the models and to identify potential overfitting issues. A comparison of the model size is also critical, and the current discussion only mentions the parameter count of CGMLFF, but not the proposed model. This makes it difficult to evaluate the trade-offs between model complexity and performance.

Training-validation-test splits are not clearly specified from what I can tell. (Majewski 2023) states the data was randomly split between training (85%), validation (5%), and testing (10%). The lack of clarity on the data splitting strategy raises concerns about the reproducibility and generalizability of the results. It is essential to specify how the data was partitioned into training, validation, and test sets, and whether this split was consistent across all experiments.

Improvements in performance are mostly left as visual assessment, e.g. figure 6 and figure 5. It is unclear how one would conclude anything just by looking at these figures. Multiple quantitative ways to compare seem feasible, e.g. see supplementary docs in (Majewski 2023). The reliance on visual assessment for performance comparison is a significant weakness. Quantitative metrics, such as those provided in the supplementary material of Majewski 2023, should be used to provide a more objective and rigorous evaluation of the model's performance. The lack of quantitative metrics makes it difficult to draw any firm conclusions about the superiority of the proposed method.

### Questions
Clarify the training-test-validation splits.
Comment on performance comparison approach more quantitatively (not needing new experiments).
Model size comparison.
Comment on what the specific rotation representation is, and how does it actually help. Also, some insight on how the network archietcture for EquiJump can be motivated.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes EquiJump for protein dynamics simulation. It utilizes two-sided stochastic interpolants to solve the issue of mismatch between  prior distribution and data distribution. The model is designed to meet SO(3) equivariance to capture the dynamics physically, and is evaluated on 12 fast-folding proteins, achieving state-of-the-art performance compared with CG-MLFF.

### Strengths
1. The proposal of  two-sided stochastic interpolants is inspiring and interesting. It enables the model to make sequence generation ($X^t\rightarrow X^{t+1}$), addressing the limitation of common (one-sided) stochastic interpolants, which are restricted to generating samples only from a specified prior distribution (e.g., a Normal Distribution).
2. The paper provides theoretical guarantee of EquiJump, which is verified by  the experimental results on fast-folding proteins. It successfully generates the  trajectories with longer timesteps. Moreover, the representation and visualization of the results are wonderful.

### Weaknesses
1. There are some typos:
  + In Eq. (6), the target to minimize should be $\hat{\eta}$，not $\hat{s}$
  + In line 94, "represents" and "builds" are repeated. Maybe you want to choose either of them?
  + In figure(3),  there are two subfigures (c). And in the final subfigure, the initial step is supposed to be $X^t$， not $X^\tau$.
2. The experiments can be more comprehensive:
  + More baselines. EquiJump is only compared with CG-MLFF. It will be more convincing to compare with predictive models, such as EGNN [1], EqMotion [2] and ESTAG[3]. They are recent equivariant graph neural networks (GNNs) and have been used  to predict molecular dynamics. 
  + More representations. The experimental results are presented by plots and curves. Detailed numerical results (presented by table) can help us understand the priority of your model better.  For example, you can present the RMSD between your generated conformations and the ground truth structures.
  + More metrics. Jensen-Shannon divergence (JSD) is also used as a metric for trajectory prediction.
  + More datasets. I am curious about the performance of your model on the MDAnalysis [4] dataset, too.  It is also a prevailing protein dynamics dataset used for evaluating ML model.
  + Ablation on steps. Currently, you set the integration steps to 500. It is interesting to see the performance of fewer steps (e.g., steps=200/300/400).

### Questions
1. Can you provide more explanations about one-side and two-side stochastic interpolants? It is difficult to understand the contribution of your model if one has not much knowledge about it.
2. How many orders do you use for the feature representation $V$ ? And how do you initialize $V^0$ ($l=0$)?
3. Are there some trainable parameters of $I_\tau$?  From algorithm 1,  it seems that $I_\tau$ is just a linear interpolant, without anything to train.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on enhancing molecular dynamics of proteins and proposes EquiJump, a two-sided stochastic interpolant framework tailored for arbitrary data endpoints with $\mathrm{SO}(3)$-equivarient modules. Experiments on 12 fast-folding proteins verify its superiority by accurately replicating the dynamics.

### Strengths
1. A good try to leverage two-sided stochastic interpolants for MD, which can be considered as a Markov process and therefore serves as a suitable scenario for bridging the arbitrary data endpoints.
2. The work proposes the tensor cloud representation and a corresponding $\mathrm{SO}(3)$-equivariant module, obtaining a more detailed representation of 3D coordinates.
3. Inspired by classical MD methods like umbrella sampling, the work utilizes the resampling technique to uniformly sample different states from MD trajectories for training.

### Weaknesses
1. This work is slightly lacking in innovation: the concept and conclusions of the two-sided stochastic interpolant were elucidated in [1], and the $SO(3)$-equivariant architecture of EquiJump is similar to other existing architectures as well, such as Equiformer [2]. Further explanations of the neccesity to use such architectures are warranted. Specifically, the novelty of the specific architecture within the stochastic interpolant framework is not clearly justified. The choice of a particular equivariant network structure, given the existence of established alternatives, needs more rigorous explanation, including ablation studies to demonstrate the necessity of the chosen design. 
2. EquiJump was trained and evaluated both on the same dataset (fast-folding proteins). Although the dynamics are restored accurately, there's no proof for the transferability to other protein systems of the model. This is a critical limitation, as the practical utility of a molecular dynamics model hinges on its ability to generalize to unseen systems. The lack of out-of-distribution testing severely limits the applicability of the model in real-world scenarios. 
3. EquiJump was only compared to CG-MLFF in this work, where CG-MLFF is performed in a corase-grained fashion, leading to a relatively unfair comparison. It would be more convicing to compare with more advanced models that work on all-atom systems, such as Timewarp [3]. Meanwhile, providing statistical results will be better. The comparison to CG-MLFF, a coarse-grained model, does not provide a strong enough benchmark. A more rigorous evaluation would involve comparisons against state-of-the-art all-atom molecular dynamics models, and the results should be presented with statistical significance.

### Questions
1. Please give more explanations of the neccesity to propose a novel $\mathrm{SO}(3)$-equivariant architecture rather than using existing architecutres like Equiformer. Ablation results will be better.
2. To prepare the training dataset, the resampling technique was used to uniformly sample states with different free energies. I wonder that while the dataset was biased from the Boltzmann distribution, the minimizer of the training objective might also be biased from the real dynamics. Please correct me if I am wrong.
3. Please provide more experimental results of stronger baselines by training from scratch if possible. It would be more appreciated if the results could be reported through statistical metrics.

### Soundness
3

### Presentation
4

### Contribution
2
