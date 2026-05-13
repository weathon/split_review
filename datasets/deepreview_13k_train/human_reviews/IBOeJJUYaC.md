# A Neural Material Point Method for Particle-based Simulations

- Decision: Reject
- Scores: 3, 6, 3, 5, 6

## Abstract
Mesh-free Lagrangian methods are widely used for simulating fluids, solids, and their complex interactions due to their ability to handle large deformations and topological changes.
These physics simulators, however, require substantial computational resources for accurate simulations.
To address these issues, deep learning emulators promise faster and scalable simulations, yet they often remain expensive and difficult to train, limiting their practical use.
Inspired by the Material Point Method (MPM), we present NeuralMPM, a neural emulation framework for particle-based simulations.
NeuralMPM interpolates Lagrangian particles onto a fixed-size grid, computes updates on grid nodes using image-to-image neural networks, and interpolates back to the particles. 
Similarly to MPM, NeuralMPM benefits from the regular voxelized representation to simplify the computation of the state dynamics, while avoiding the drawbacks of mesh-based Eulerian methods.
We demonstrate the advantages of NeuralMPM on several datasets, including fluid dynamics and fluid-solid interactions.
Compared to existing methods, NeuralMPM reduces training times from days to hours, while achieving comparable or superior long-term accuracy, making it a promising approach for practical forward and inverse problems. A project page is available at \texttt{\url{https://neuralmpm.isach.be}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors present a Neural Material Point Method (NeuralMPM) for improving the efficiency of the numerical simulation. Comparing to traditional MPM method, NeuralMPM  perform grid operations using image-to-image neural networks. The proposed method is validated on several fluid and fluid-solid interactions datasets. It demonstrates that the proposed method can effectively reduce the training time while achieve comparable or better long-term accuracy, comparing to the benchmarks.

### Strengths
The paper is well-organized and easy to follow.

### Weaknesses
The paper describes computational fluid dynamics (CFD) as the background or motivation for NeuralMPM. MPM is powerful for simulating objects with large deformation (elasticity, plasticity, fractures etc) and handling collision contact naturally. However it may not the best common choice for simulating incompressible fluid (such as water) in the general CFD context, as it is not handling the divergence-free constraint in incompressible fluid. In these scenarios, another hybrid Eulerian-Lagrangian method FLIP, or pure Lagrangian based method (such as SPH) might be better choices.

The original MPM pipelines can be generally divided into three stages as particle-to-grid(p2g), grid-update, grid-to-particle(g2p). The proposed method essentially replace the original grid-update with a U-net and utilize p2g and g2p as is. Therefore, the main claim (From Line 519 tp Line 521 "The use of voxelization allows NeuralMPM to bypass expensive graph constructions ... constant runtime.") of the effectiveness on efficiency of the proposed method comes from MPM itself but not new knowledge introduced by the NeuralMPM.

The authors' claim that their method aims to accelerate existing simulations while also potentially outperforming them by overwriting the inductive bias of MPM with sufficient training data is contradictory. If the goal is acceleration, the limitations of MPM remain. If the goal is enhancement, there is insufficient experimental support, such as demonstrating the method's ability to simulate plasma behavior using MPM as a base. The technical contribution is limited if the method is solely accelerating MPM simulations.


### Questions
- For MPM simulation, the particle-to-grid(p2g) and grid-to-particle(g2p) are generally considered as expensive stages or bottleneck of the runtime performance[1]. As scatter or gather operations are more challenging for parallel computation comparing to in-place operations of grid-updates. Just wondering what is the motivation of making surrogate model for grid-update part instead of p2g or g2p when developing NeuralMPM?

- In Table 1, the proposed NeuralMPM performs much better than GNS on VariableGravity (MPM) case (14.48 vs 134 on MSE) and MultiMaterial (MPM) (9.6 vs 14.79), however worse on WaterRamps(MPM) and SandRamps(MPM). These three cases are all MPM based, what do you think the reasons why there are such as huge performance gaps between similar cases? In addition, the proposed method also show much advantages on the SPH based case (i.e., Dam Break 2D), would you mind sharing some intuition on why this is the case?

- In Inference time and memory part and Figure 6, it demonstrates that the proposed method is applied to cases with 1M (i.e., 1000k) or even 10M (i.e., 10000k) particles, while in Table 1 the model is trained on cases with less than 5k particles. Just wondering if the model are re-trained on the 1M or 10M cases or they can be trained on 5k and transfer to a 200 or even 2000 times larger case?

- For the generalization, the authors mention that the model trained on 64x64 grid size can generalize to 64 x128 without re-training. Just wondering would you mind providing a larger case until the generalization fails? It would be helpful to understand what is the limit of the generalization ability.

[1] Wang et al, A Massively Parallel and Scalable Multi-GPU Material Point Method, ACM Trans. Graph (2020)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Inspired by material point method (MPM), the authors proposed a neural emulator framework for particle-based simulations. The downstream tasks include weather forecasting, computational design, inverse problem, and animation industry. Their method is compared to the traditional MPM, and two other state-of-arts data driven methods, namely DMCF and GNS.

### Strengths
- The article is easy to follow, and sufficient background knowledge is provided to readers. I appreciate that.
- The proposed neural emulator is demonstrated more efficient than traditional MPM and other data-driven methods in computational time, more accurate, and it requires much shorter training time, and smaller memory usage.  
- Since the model operates on regular grid only, it allows use of a simple network architecture such as convolutional UNet. 
- Being able to solve inverse problems to predict boundary condition is an interesting idea.

### Weaknesses
 - The common drawback of autoregressive models is its instability for long-term predictions. The examples shown in the paper all seem to have a short period of time simulated. Although rollout loss can mitigate error accumulation to some degree, it cannot help long-term prediction. If a simulation (for example consider water particles continuously added through an inlet)  lasts much longer, the model might not be able to predict accurately after certain time.
- From my understanding, for a different grid resolution, whether coarser or finer, it would require training a new model. 
- Based on the current memory usage and training time, it might be difficult to scale to 3D problems with the current setups.

### Questions
- How is `taichi-MPM` implemented? Also consider comparing to state-of-arts MPM implementations, such as [this one](https://dl.acm.org/doi/10.1145/3386569.3392442).
- The paper claims to be able to emulate up to 30 millions particles, but I do not see any examples of videos or snapshots.
- About *able to generalize to different domain shapes* on line 188 page 4,  what exactly are "different domain shapes"?  Does it work for non-square shapes like circles?
- Do you have examples on smoke simulation such as smoke passing an object? Have you tried on examples with nonzero initial velocities? 
- Does it require separate models for each example, such as `WaterRamp`, `SandRamps`, `Goop`? Can you train a single model that generalizes to problems with any different setups, ie, fluid property, boundary condition, initial velocity? 
- Can you explain why numerical simulators are non-differentiable?
- It would be nice to have a diagram on network architecture.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to adopt material point method for particle-based simulation. The method first interpolates particles onto the grids, and simulate the interactions among grids to generate velocities, which are further distributed to particles again. The proposed method delivers faithful rollouts as shown in experiments.

### Strengths
* This method tries to integrate with MPM for simulation.
* The approach seems to be more robust in specific domains.

### Weaknesses
1. The method is technically limited.
    1. The adaptation of MPM is naive. The main difference between the proposed method and the original MPM is that the proposed method does not need the template states in material space, or equivalently, the “material space” in this method is dynamically determined. For example, when predicting frames from $t$ to $t+m$, the “material space” is defined by states at time $t$. In this way, this method is very close to existing MPM pipeline, leading to limited novelty. The core idea of using a neural network to update the grid states, while maintaining the particle-to-grid and grid-to-particle transfer, is not a significant departure from standard MPM implementations. The novelty is further diminished by the fact that the grid update is a relatively straightforward application of a neural network, lacking any complex or novel architectural components.
    2. The continuous predictions of m steps seems questionable. For example, when the particles move very fast from $t$ to $t+m$, the grid constructed at time $t$ may not be suitable for particles at time $t+2$, which is in the middle of the duration, because the distribution of the particles changes dramatically. In other words, such formulation seems to be more reasonable for particles moving very slow, where the distribution of particles changes slowly as well or remains similar, leading to limited fields of application. The method's reliance on a fixed grid for multiple time steps is concerning, as it does not account for the evolving particle distribution, potentially leading to inaccuracies, especially in scenarios with high particle velocities and rapid changes in density.
2. There are some questions about the data.
    1. The data is a bit tricky. Since the data is also generated by MPM methods, the data will have similar bias as the proposed model. Both the data and the proposed method naturally behave similar under the framework of MPM. In other words, if the data is generated by other physics simulators without MPM, such as PBS, the proposed method may fail to learn the dynamics. The use of MPM-generated data introduces a significant bias, as the model is essentially learning to emulate the behavior of the simulator it was trained on. This raises concerns about the model's ability to generalize to real-world scenarios or simulations generated by different methods.
    2. How many particles are included in each scenario? And how long is each sequence?
3. The evaluations are insufficient.
    1. The author only provides results on 2D domain. Can the method be applied to 3D domain as shown in the GNS method? The settings of only using 2D domains seems a bit simple. The lack of 3D experiments is a significant limitation, as many real-world physics simulations occur in three dimensions. The method's applicability to 3D scenarios remains unclear, and the provided 2D results do not sufficiently demonstrate its generalizability.
    2. As shown in the generalisation results in Appendix, the author claims that the missing of ground truth results from the unknown simulation parameters. However, since the method can be applied to simulate different materials as mentioned at L230-231, the author can adopt a set of reasonable but simple parameters and generated the corresponding scenarios, enabling quantitative comparisons on those domain. Existing evaluations are insufficient to proof the generalisation abilities of the proposed method. The generalization experiments are not rigorous enough. The lack of quantitative comparisons with ground truth data in the generalization experiments makes it difficult to assess the model's true performance in unseen scenarios. The claim that the missing ground truth is due to unknown simulation parameters is not a strong justification, as the authors could have generated their own data with known parameters.
    3. In the supplementary videos, the visualisation results obtained by baselines are missing, which prevents from comparing with baselines qualitatively. Since the work focuses on dynamic predictions, the video results of animations are also important to evaluate the methods. The absence of visual comparisons with baseline methods in the supplementary videos makes it difficult to assess the qualitative performance of the proposed method. Visual comparisons are crucial for understanding the dynamic behavior of the simulations and for identifying potential artifacts or inaccuracies.
    4. At L025, the author claims that the proposed method can better handle long-term predictions. However, from existing evaluations, one is hard to find the evidence to prove this claim. Can the author explain clearly or even provide more results for long-term predictions?
4. The author may considers TIE [1] as related work or even compare with it, which is also a particle-based simulator.

### Questions
Besides questions mentioned in weaknesses, here is one more question:
1. Why does GNS take so long to train as mentioned at L252? Is it because different training schedules are applied? For example, the training of GNS adopts much smaller learning rate or batch size?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes combining conventional MPM simulation with neural networks to enhance its training speed and generalization ability. This method interpolates the Lagrange particles into the background grid and uses an image-to-image network to process and solve motion equations to obtain the final outcomes.

### Strengths
Strength
1. Replacing parts of the traditional numerical simulation framework with neural networks instead of learning the whole dynamic process can improve the generalization ability, reduce the training difficulties. 

2. The hybrid physical solver can be considered the next generation of physical simulation because the classic part and neural part can mutually benefit from each other. The classic part provides basic priors and genralization ability and the neural part improve the accuracy and efficiency. 

3. Conventional GNN-based particle simulators requires large amount of data for training, while the proposed method only need fewer training data thanks to its MPM solver priors.

### Weaknesses
Weakness:

1. This work relates to hybrid (classic and learning-based) simulation solvers, but it seems to provide insufficient background on related work in the area, especially lacks more recent works. Most of the works mentioned in the paper are from 2023 or earlier. This will make the paper appear less to-date, even though the method is innovative. Hence I list some relevant recent works below and suggest the author can discuss and compare with them to make the background sections to-date.


"DEL: Discrete Element Learner for Learning 3D Particle Dynamics with Neural Rendering." 2024. This paper also builds a hybrid numerical solver by integrating conventional particle mechanics into neural network design, which should be included in the same subfield with NeuralMPM, i.e. the neural-based physics solver.

“A Neural Material Point Method for Particle-based Simulations” 2024  By the way, this paper also proposes a hybrid model based on the MPM method, could you please clarify what is the main difference between NeuralMPM and this one?

"ElastoGen: 4D Generative Elastodynamics". 2024. This paper introduces elastic dynamics into the learning generative pipeline, it directly generates the network parameters that are designed according to projection dynamics, which seems to be an application of hybrid solvers.


2. NeuralMPM still requires full 2D particle trajectories to train the model, which could be hard to access in most cases.  Moreover, This method is currently limited to simulating 2D scenarios. Are there any obstacles to extending it to 3D? I believe this could be achieved by simply replacing the UNet with its 3D convolutional version. 

3. I hope the author can provide a quantitative analysis of this method's execution efficiency compared to traditional methods. Since the process is carried out by a neural network, efficiency is expected to improve, which could be another potential advantage of this approach.

4. Explicit integration in traditional methods is very sensitive to the time step size. After training, I’m curious whether this method can perform computations with a larger time step. Compared to explicit integration in traditional methods, can it operate with a larger time step?

### Questions
See Weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents NeuralMPM, a learning-based PDE solver inspired by the Material Point Method. It falls in the category of Lagrangian (or particle-based) methods, but the MPM, by interpolating Lagrangian particles onto a fixed-size grid via voxelization, makes it a hybrid Eulerian-Lagrangian approach.

The advantage of NeuralMPM is the fact that it still carries information via particles, i.e. it is not mesh-based, like Eulerian methods, but it borrows from such methods the regular grid structure to compute the state dynamics, which is computationally less expensive than particle-based approaches. The voxelization onto a grid makes NeuralMPM amenable to networks that work in a Euclidean setting. 

NeuralMPM is validated on 6 datasets, including fluid dynamics and fluid-solid interactions, with different materials and physical properties. NeuralMPM outperforms 2 other architectures, GNS and DMCF, in 4 out of 6 scenarios, converges quickly (10-fold improvement) and its performances in terms of speed and computation are more robust as the number of particles of the system increases.

### Strengths
The text is clearly written. It reads well, the introduction on CFD methods and the review of the MPM approach is clear and thorough, the problem setting of the NeuralMPM is clearly defined. Ablations are thorough and well presented. I liked how conclusions were drawn. The limitations of NeuralMPM and possible future work showed good confidence in this field of research. 

I feel the main strengths are Fig. 5, relative to convergence, and Fig. 6 relative to the model’s robustness show important contribution of NeuralMPM, as computational complexity is one of the main limitations of learning-based PDEs solvers.

### Weaknesses
Reading Section 2, I am not sure I quite understand how novel is NeuralMPM. How does it compare to other methods that use MPM in a learning setting? How does it differ from the work of Li et al. (2024)? What are its main contributions?

NeuralMPM is compared against only two models, namely GNS and DMCF, making it hard to assess how good it actually is. 

In general, I don’t think authors make a compelling argument for the merits of their model, probably due to their choice of figures. A list below: 

1. why using the WaterRamps dataset in Figure 4 if WaterRamps is the only dataset over which NeuralMPM does not outperform the other two models?

2. Figure 7: you claim that ”A NeuralMPM model trained on a square domain can naturally generalise to larger rectangular domains (twice as wide here) when using a fully convolutional U-Net”, but without ground truth (as you claim in Fig. 19 and line 486) for the right hand side particles how can we assess how good is NeuralMPM at generalising? I am having a hard time believing that the evolution from starting point to $t_1$ is realistic (where did the leftmost blob of water go?).
Also, the labels between the left and right section of the figure are confusing (Predictions and GT for left and Predictions $t_1$, Predictions $t_2$ for right). 

3. In line 469 you claim that “one notable advantage of NeuralMPM is its invariance to the number of particles, as the transition model only processes the voxelized representation.” Doesn’t figure 6 confute the claim? After 10^5 particles the FPS decreases and after 10^4 the GPU usage increases for NeuralMPM. They don’t seem to be an incredibly large number of particles either.  Could you please clarify this point?


4. You claim that NeuralMPM is superior to GNS, but the results reported by their authors show otherwise, as shown in Fig. 3. Without a discussion on what might cause this discrepancy, it is hard to assess the merits of NeuralMPM over GNS.

The abstract and conclusions don’t highlight the merits of the paper enough, in my opinion, especially because there’s plenty of details and quantitative results in Section 4. For example: 
Line 22: We demonstrate the advantages of NeuralMPM on several datasets (how many? Which ones?), including fluid dynamics and fluid-solid interactions
Line 23: Compared to existing methods (which methods?), NeuralMPM reduces training times from days to hours (can you quantify the improvement?)
Line 516: NeuralMPM trains in a fraction of the time (what fraction?) it takes to train alternative approaches (what are alternative approaches?)

### Questions
Is this the first approach in the literature of a differentiable MPM method?

Line 187: you mention that the FNO underperforms. What is your intuition behind a neural operator performing worse on a PDE solution task as opposed to a purely convolutional architecture like U-Net?

Why have you chosen specifically GNS and DMCF? It would be good to expand on that in the text.

Fig. 3: interesting that you could not reproduce the reported GNS results when you retrained it. Do you have an explanation for that? Is it due to different hyperparameters, different hardware, etc? Without further insight it’s difficult to conclude whether NeuralMPM outperforms GNS or not. 

Fig. 3: Why didn’t you include a line also for the DMCF approach? Couldn’t you retrain it like you retrained GNS?

Table 1: why aren’t there results reported obtained via classical Taichi-MPM?

You report full convergence of the GNS method after 240h. What is the convergence time reported by the original authors?

In Fig. 4 you provide an example of trajectories for the WaterRamps dataset for your NeuralMPM approach and the GNS and DMCF. In Table 1, however, WaterRamps is the only dataset over which NeuralMPS shows no improvement compared to other methods. Why have you chosen to plot results over the WaterRamps dataset? Have you considered plotting examples for MultiMaterial, DamBreak or Variable Gravity? Since the improvement over the latter datasets is so significant, it would make sense to corroborate the results with figures. You have 8 additional figures in the appendix, why not having also figure of comparison on those datasets to make your argument more compelling?

Line 434: How do you explain the faster convergence of NeuralMPM? Is it due to the voxelization that makes computations easier? Also, in Figure 6 there’s the Taichi-MPM method, but that is missing in Figure 5. How does the convergence of the Taichi-MPM method compares?

### Soundness
2

### Presentation
2

### Contribution
2
