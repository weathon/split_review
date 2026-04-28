# Diff-PIC: Revolutionizing Particle-In-Cell Nuclear Fusion Simulation with Diffusion Models

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 6, 5, 8

## Abstract
The rapid development of AI highlights the pressing need for sustainable energy, a critical global challenge for decades. Nuclear fusion, generally seen as an ultimate solution, has been the focus of intensive research for nearly a century, with investments reaching hundreds of billions of dollars. Recent advancements in Inertial Confinement Fusion have drawn significant attention to fusion research, in which Laser-Plasma Interaction (LPI) is critical for ensuring fusion stability and efficiency. However, the complexity of LPI upon fusion ignition makes analytical approaches impractical, leaving researchers depending on extremely computation-demanding Particle-in-Cell (PIC) simulations to generate data, presenting a significant bottleneck to advancing fusion research. In response, this work introduces Diff-PIC, a novel framework that leverages conditional diffusion models as a computationally efficient alternative to PIC simulations for generating high-fidelity scientific LPI data. In this work, physical patterns captured by PIC simulations are distilled into diffusion models associated with two tailored enhancements: (1) To effectively capture the complex relationships between physical parameters and corresponding outcomes, the parameters are encoded in a physically-informed manner. (2) To further enhance efficiency while maintaining high fidelity and physical validity, the rectified flow technique is employed to transform our model into a one-step conditional diffusion model. Experimental results show that Diff-PIC achieves 16,200$\times$ speedup compared to traditional PIC on a 100 picosecond simulation, with an average reduction in MAE / RMSE / FID of 59.21\% / 57.15\% / 39.46\% with respect to two other SOTA data generation approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper describes a computationally efficient alternative to Particle-in-Cell (PIC) simulations for nuclear fusion research, specifically for generating Laser-Plasma Interaction (LPI) data. This is achieved through the application of a diffusion model, designed to replace the resource-intensive and time-consuming nature of PIC simulations by introducing a Physically-Informed Parameter Encoder and the Rectified Flow Technique. The work primarily aims to advance nuclear fusion research by making high-fidelity data generation feasible at a fraction of the traditional computational cost.

### Strengths
The submission is clear in its objectives and introduces novel elements like the Physically-Informed Parameter Encoder (PIPE) and Rectified Flow Acceleration (RFA) Technique, which together can generate high-fidelity data by applying a diffusion model. The experimental setup is robust, providing a detailed comparison of Diff-PIC against state-of-the-art generative models (GANs and Normalizing Flow) on multiple performance metrics (MAE, RMSE, FID). The authors demonstrate significant speedups and error reductions, substantiating the model’s effectiveness with quantitative evidence. Diff-PIC makes a strong alternative to traditional Particle-in-Cell (PIC) simulations, since it achieves orders-of-magnitude speedup, while retaining high fidelity and reducing the computational cost of PIC.

The PIPE provides a novel way to embed physical constraints, ensuring the generated data remains physically consistent without modifying the core diffusion process. This approach keeps the model flexible, allowing it to adapt to various scenarios, such as handling different particle types (e.g., electrons or ions), while avoiding the complexity of embedding physics-informed parameters directly within the diffusion model itself. While RFA is becoming more known in specific domains like high-resolution image generation, it remains novel in scientific applications, particularly for complex simulations like PIC. The inclusion of RFA in Diff-PIC enhances efficiency, offering significant speedup without sacrificing fidelity for generating realistic. Despite some missing details on specific model components or implementation—the paper’s contributions are substantial and have the potential to drive advancements in scientific data generation for PIC simulations and could become a tool for the broader community.

### Weaknesses
The authors discuss how diffusion models align with the problem and highlight PIPE as a benefit for Diff-PIC, but GAN-PIC and NF-PIC include PIPE in their comparisons as well. Also, Diff-PIC’s performance heavily depends on PIPE’s ability to generalize from limited training data, which may require retraining or fine-tuning the encoder if the physical parameter ranges shift. While the paper evaluates Diff-PIC using error metrics and continuity checks, it would benefit from additional validation against physics-specific benchmarks and more interpretability studies. Also, architectural comparisons to GAN-PIC and NF-PIC in the LPI data generation context would provide insights into the superior performance of Diff-PIC.

### Questions
The paper introduces innovative components like the PIPE with polynomial encodings, a U-Net for score-based modeling in the RFA. However, it lacks specific details on critical elements: it does not fully describe the polynomial encoder (such as the choice of polynomial degree or basis functions), the architecture and configurations of the U-Net, or the exact loss function guiding the training process. These missing details limit a clear understanding of how each component is optimized for effective high-fidelity data generation.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Paper uses a diffusion model to generate data simulating a Particle-in-cell simulation for nuclear fusion research. The diffusion model takes parameters (electron temperature, ion temperature, and laser intensity) and timestep and generates an electric field snapshot. The paper designs a parameter encoder which uses positional encoding for timestep, and positional encoding concatenated with a polynomial transformation for electron temperature, ion temperature, and laser intensity. The model is trained with rectified flow-based acceleration using a u-net for learned trajectory. Paper includes experiments of quantitative interpolation, extrapolation, energy evaluation vs snapshot, qualitative comparison with ground truth data, and speedup vs particle-in-cell simulation.

### Strengths
The paper is original in using diffusion model for simulating particle-in-cell data. Paper tackles an important problem of design in nuclear fusion research. Paper is clearly written.

### Weaknesses
A weakness is that it is unclear how close the generated data should be to the true data to be useful for nuclear fusion design/research. hard to evaluate the scale of quantitative error. also do the fine details matter in the E field? because they do not look close in Fig 4 visualization. could authors provide context on what level of accuracy is required for the generated data to be useful in nuclear fusion research, and discuss the importance of fine details in the electric field and how this impacts the utility of their approach.

the main conclusion from paper's experiments seems to be that diffusion with u-net performs better than Gan or normalizing flow, for this task.

### Questions
Perhaps authors could add an ablation study on various pieces of the physically informed parameter encoder? such as the positional encoding or polynomial transformation

Perhaps authors could add uncertainty estimates to numbers in Tables? such as standard deviation over multiple runs or confidence intervals

Can authors add energy evaluation on Gan-Pic and NF-Pic onto Fig 5? Would be good to have same energy evaluation metrics (MAE and RMSE) included for GAN-PIC and NF-PIC in Fig 5, allowing for a direct comparison across all methods

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposed an new approach to tackling the computational challenges in nuclear fusion simulations by applying diffusion model. The contribution including: (1) Proposing PIPE (Physically-Informed Parameter Encoder) that improves the model's ability to understand the relationship between physical parameters and simulation outcomes. (2) Applied rectified flow acceleration. The simulated results shows this diffusion based approach significantly speed-up compared with traditional method.


========== post rebuttal

I still feel the paper's contribution on ML side is not significant enough. However, I'm less familiar with the application side. I'm lean towards to accept, if other reviewer can champion it on ML for science side.

### Strengths
The paper try to apply diffusion model for PARTICLE-IN-CELL NUCLEAR FUSION SIMULATION. Although I'm not sure how important of this problem, i think using diffusion model for simulation in science is an important and exciting topic. Also the the speed-up looks impressive.

### Weaknesses
It's unclear to me what is the ML contribution for this paper.
To me it seems most interesting part is the newly designed encoder. Can the author explain:
"Algorithmic generalization. PIPE improves the generalizability of the conditional diffusion model"
I don't quite get why such design improved generalizability compared with normal mlp/transformer layers. I hope the author would clarify it.

The application value of this paper beyond my expertise, I hope the author could also explain it and also explain how this approach generate new insights for other ML for science problem.

Compared with previous work, "diffusion models in molecular dynamics simulations "

I hope the author can clarify:
1. The above cited paper is first paper apply diffusion to a similar domain.
2. Among the two unsolved problem, can the author explain more how this paper address "Physical soundness must be ensured"? Does it more empirical or theoriotical?
3. "Substantial efficiency improvement" I got this achieved by apply normalizing flow.

### Questions
Please see the weakness part.

Compared with previous work, "diffusion models in molecular dynamics simulations "

I hope the author can clarify:
1. The above cited paper is first paper apply diffusion to a similar domain.
2. Among the two unsolved problem, can the author explain more how this paper address "Physical soundness must be ensured"? Does it more empirical or theoriotical?
3. "Substantial efficiency improvement" I got this achieved by apply normalizing flow.

### Soundness
2

### Presentation
2

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
This paper investigates laser plasma interactions in Particle In Cell simulations (PIC) through diffusion models. They study the evolution of charged particle trajectories, influenced by the electric and magnetic fields (equation 2). The neural network designed uses the diffusion model methodology, with some novel fittings - a physically designed parameter encoder, positional encodings and legendre polynomials, and a distillation framework. The network - from what I see - takes as input electron and ion temperatures $T_e$, $T_i$ and laser intensity $I$ (i.e. $\theta = (T_e, T_i, I)$ to generate the electric field $E$, evolving it over time $t_{as}$ to obtain $E(\theta, t_{as})$. The network optimization takes place through the rectified flow acceleration technique proposed in [1, 2, 3] in equation (5). 

Results are presented to show time evolution snapshots of the electric field, comparing them with two other generative models (GAN and normalizing flow). Metrics checked are MAE, FID and RMSE. They also examine the 'energy' evolution over time. They call this the interpolation and extrapolation capabilities of the generative model. Data distribution is also compared with the 'ground truth' which is obtained from a PIC simulator. The claims are that the model beats the competitors (GAN [4] and normalizing flow [5] ), and is much faster owing to the more efficient rectified flow acceleration technique used. 

Post rebuttal
=========
The authors have taken great pains to explain the method and provide additional ablations and experiments, all of which supports their case that the method works rather well for PIC. The paper paper adds to the body of research work in PIC simulations:
- it works as well or better than competitive methods 
- it is significantly faster than mainstream computational approaches used in plasma physics (owing to the rectified flow acceleration technique)
However, as stated before, the work does not add to novelty in terms of the method used in generative modelling and diffusion models. To this end, I am raising the score but am not (entirely) convinced about it being accepted. That being said, I think it is a marginal call.

[1] Xingchao Liu, Chengyue Gong, and Qiang Liu. Flow straight and fast: Learning to generate and
transfer data with rectified flow, 2022.

[2] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Muller, Harry Saini, Yam ¨
Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling rectified flow transformers for
high-resolution image synthesis. arXiv preprint arXiv:2403.03206, 2024.

[3] Xingchao Liu, Xiwen Zhang, Jianzhu Ma, Jian Peng, and Qiang Liu. Instaflow: One step is enough
for high-quality diffusion-based text-to-image generation, 2024.

[4] GAN: Alankrita Aggarwal, Mamta Mittal, and Gopi Battineni. Generative adversarial network: An overview
of theory and applications. International Journal of Information Management Data Insights, 1(1):
100004, 2021.

[5] NF: Qinsheng Zhang and Yongxin Chen. Diffusion normalizing flow. Advances in neural information
processing systems, 34:16280–16291, 2021.

### Strengths
- This appears to be a first of its kind (at least according to the authors) PIC simulation using generative model. I cannot verify this claim, but no other references of this type of work are compared with in the paper. 

- The methodology appears to be sound, and the evaluation follows the techniques used in generative modelling generally. 

- The evaluation fares quite well, compared to competitors (GAN and normalizing flow), achieving better performance and speed.

### Weaknesses
 - Novelty: The main novelty appears to be the application of an existing method in a new domain (plasma physics). While this is not a complaint in itself, it seems (at least to me) that it is only a replacement of the modalities from more well studied setups involving images. 

- Method and physical validity: It is hard for me to understand how the equation (2) (velocity field evolution) is being solved by the diffusion model. From what I see, we are learning the electric field from snapshots in time. 

- Ablations: The components used in the model should, I think be ablated to show effectiveness of each piece. For instance, how does the positional embedding help? What is the performance without the Chebychev polynomial addition? 

- Network Architecture: Perhaps I am missing this, but I would like to see a block containing the network design - transformer blocks, CNNs, etc.

### Questions
- See 'weaknesses' above: I would like clarification on whether the generative model is learning 2D snapshots of the electric field. What is the ground truth representation? Is the equation (2) at all relevant? 

- The authors mention 'limited' samples. But shouldn't the PIC simulator be able to generate a large number of samples to train the model? How many samples do we think are necessary to qualify as a large enough dataset?

- Did the authors implement the alternative (GAN and NF) methods themselves? I do not see a corresponding reference for these methods for PIC (what is provided is the main method describing GAN and NF).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an approach for accelerating particle in cell simulations for laser in plasma simulations by applying a diffusion model to the computation of electric fields. These fields are produced based on key parameters in the simulation and show good accuracy when compared to literature and non-accelerated simulations.

### Strengths
I find the paper to be very well-written and clear. Further, the topic being approached is very important and introduced in such a way. The experiments performed to validate their method and present prior work to highlight the difference in their approach.

### Weaknesses
The paper is undoubtedly more geared towards nuclear physicists than for people in the ML community. What was missing for me was the advance in the ML direction. What can be taken from this work and applied to improve knowledge in the ML community? By making this connection, I feel it will be better received at ICLR. The use of a time encoding is also unclear. At one point in the paper, it was written that the method works from snapshots. Thus, long-time series are not necessary. However, later in the paper, the authors mention that they use encoding to capture information about time. It is not clear what role time plays in the model. Is there some dynamic information necessary for the model function? If so, why not use a more recurrent kind of architecture? I can imagine, if dynamics are required for a complete description, that a single snapshot can occur many times in different trajectories. Therefore, a time-only encoding would not capture this information, and a state-based memory would be required. I am not an expert in these kinds of simulations, so I am likely misunderstanding something but more clarity there would be great.

### Questions
* Can you elaborate on the time encoding? At one point in the paper, it was written that the method works from snapshots. Thus, long-time series are not necessary. However, later in the paper, the authors mention that they use encoding to capture information about time. Is there some dynamic information necessary for the model function? If so, why not use a more recurrent kind of architecture? I can imagine, if dynamics are required for a complete description, that a single snapshot can occur many times in different trajectories. Therefore, a time-only encoding would not capture this information, and a state-based memory would be required. I am not an expert in these kinds of simulations, so I am likely misunderstanding something but more clarity there would be great.

### Soundness
3

### Presentation
4

### Contribution
3
