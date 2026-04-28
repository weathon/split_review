# DiffSim: Aligning Diffusion Model and Molecular Dynamics Simulation for Accurate Blind Docking

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Predicting the ligand’s binding conformation within a target protein is a pivotal step in drug discovey. Based on prior knowledge of the binding site (protein pocket) on the target protein, biochemical researchers use molecular docking software to generate the ligand conformation within that pocket. Despite its speed, molecular docking is ill-suited for blind docking where the pocket is unknown, and the generated ligand conformation often lacks required precision. Recently, deep generative models, especially diffusion models, have been proposed for accurate blind docking. However, it is found that while deep generative models excel in locating the pocket, they still lag behind traditional methods in terms of conformation generation. Thus, bridging such gap with a hybrid approach is naturally expected to further improve the model performance. Therefore, in this study, we introduce a blind docking approach named DiffSim to seamlessly integrate the diffusion model with molecular dynamics (MD) simulation. We propose a novel loss function to align reverse diffusion sampling with MD simulation trajectories, aiming to efficiently generate ligand conformations informed by MD-modelled protein-ligand interactions at atomic resolution. Through theoretical analysis, we unveil the consistency in dynamics between diffusion models and MD simulation, demonstrating that the diffusion model is essentially a coarse-grained simulator for MD simulation. Empirical results demonstrate the effectiveness of our approach and highlight the potential of combining physics-informed MD simulation with deep learning models in drug discovery.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new method called DiffSim for accurate blind protein-ligand docking. The key ideas are:

- DiffSim integrates a diffusion-based generative model with molecular dynamics (MD) simulation to combine their strengths.
- It aligns the reverse diffusion sampling process with MD trajectories using a novel loss function.
- An active learning approach selectively chooses training samples for MD simulation.
- Theoretical analysis shows consistency in dynamics between diffusion models and MD, making DiffSim a reasonable hybrid.
- DiffSim outperforms previous blind docking methods on standard RMSD and centroid distance metrics.

### Strengths
- Novel idea to seamlessly combine generative diffusion model with MD simulation.
- Theoretical analysis gives useful insights into connections between the two approaches.
- Active learning makes selective use of expensive MD simulation.
- Strong empirical results validate accuracy improvements over state-of-the-art methods.

### Weaknesses
 - More analysis of alignment loss function forms could be useful, and also ablation study isolating active learning benefits would be informative.
- Testing on more diverse protein-ligand complexes beyond PDBBind. Currently, the benchmark comparison is limited. Some other papers are necessary to be compared. Such as, E3Bind, https://openreview.net/forum?id=sO1QiAftQFv, FABind, https://arxiv.org/abs/2310.06763.
- Computational efficiency comparison to alternatives would be helpful. It is necessary to give computational comparison since MD is usually cost, while diffusion with many steps are also cost.
- The experimental results are not good as expected, which leads to a negative view of the effectiveness of the method.

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes DiffSim as a hybrid framework of protein docking. DiffSim first uses a diffusion model alone to do a quick "pocket search". Then DiffSim aligns the reverse diffusion sampling trajectories with the simulation trajectories from MD. It uses active learning to select a subset of training samples for MD simulation.

### Strengths
The general topic of utilizing MD to improve neural docking method is interesting.

The entire framework is significant in contribution, and the improved performance is satisfying for stats on RMSD and Top 1 acc.

The introduction of "bias and variance" between MD and reverse diffusion is interesting.

### Weaknesses
1. The discussion between the connection of diffusion an MD is weak, and the proposed aligning method seems not to be solid. Lemma 3.1 simply states that the reverse diffusion process has the same differential form of a Langevin dynamics. This is known since 2020. But, the per-step marginal distributions of reverse dynamics should be very much different, therefore a step-wise bounding between reverse diffusion and MD traj is not solid in theory. More specifically, Langevin dynamics sample from an Boltzmann distribution under the energy function, while intermediate reverse diffusion steps sample from a Gaussian, changing as $t$ evolves. This introduce a variable "energy" (log probability) in reverse diffusion models. Authors would refer to [1] [2] or [3] for deeper discussions between diffusion and MD.

2. Lack of visualization, which is vital for MD analysis. Authors should provide consistent dynamics of reverse diffusion to justify that the trajectories are correctly learnt.

3. The hypothesis of "bias and variance" tradeoff is not supported by any results. Authors should report the recorded metrics as they can be easily calculated.

### Questions
1. I'd like to see more visualization results and studies of empirical evidence of "bias and variance" tradeoff.

2. Analysis must be done on the MD trajectories to show that the proposed protocol is reasonable.

3. Authors claim that Top1 acc is improved more significantly than Top5 and credit this to "bias and variance" tradeoff. This needs more justification.

### Soundness
2 fair

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
The paper proposes an interesting hybrid approach for blind docking by integrating diffusion models and molecular dynamics (MD) simulations. The motivation of combining these two methods to achieve accurate and efficient blind docking is reasonable.

### Strengths
1. The idea of aligning reverse diffusion and MD trajectories is novel and has potential.
2. The paper demonstrates that the diffusion process, the reverse process, and Langevin equation are mathematically equivalent in form.
3. The paper proposes a loss function to align reverse diffusion sampling with MD simulation trajectories.

### Weaknesses
1. The results look a little better than diffdock. The result only improves significantly on the Centroid Distance metric for TOP-1.
2. Due to the choice of DiffDock as the backbone model, its limitations in the degrees of freedom seem conflict with the philosophy of MD.
3. One benchmark is not enough to show the effectiveness of the method.

### Questions
1. What if MD combined with an all-atom diffusion model such as Geodiff [1], it feels that an all-atom diffusion method is more compatible with MD.
2. Do the authors try different RMSD thresholds for active learning?
3. Has the author tried comparing the efficiency of DiffSim with traditional docking tools and other deep learning methods?
4. I believe DiffSim is designed to enable flexible binding docking. Perhaps it would be beneficial to incorporate visualization features that display protein changes, such as side chain alterations, during the process.
5. Also, what is the pocket RMSD? or if you just use holo protein/pocket as initial docking?
5. It might be valuable to include a discussion on the time efficiency of molecular dynamics (MD) simulations in this stage, particularly in the context of protein MD.

[1] Xu, Minkai, et al. "GeoDiff: A Geometric Diffusion Model for Molecular Conformation Generation." International Conference on Learning Representations. 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes DiffSim, a denoising diffusion model of MD simulation for protein-ligand docking. The authors create an MD dataset themselves, which is another critical contribution to the community.

### Strengths
- This paper studies an important question of MD simulation.
- The authors generate the MD dataset, which is quite valuable.

### Weaknesses
I think one main concern of this paper is the lack of related works and baselines. Other comments may come next after this is solved.

I can understand the technical novelty of DiffSim if we follow the DiffDock research line. However, from the AI for MD literature, there have been several published works on using denoising diffusion for MD simulation [1,2,3]. They are not cited and compared in this work, and I would like to know the authors’ feedback on this.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
