# DynamicsDiffusion: Generating and Rare Event Sampling of Molecular Dynamic Trajectories Using Diffusion Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3, 3

## Abstract
Molecular dynamics simulations are fundamental tools for quantitative molecular sciences. However, these simulations are computationally demanding and often struggle to sample rare events crucial for understanding spontaneous organization and reconfiguration in complex systems. To improve general speed and the ability to sample rare events in a directed fashion, we propose a method called $\textit{DynamicsDiffusion}$ based on denoising diffusion probabilistic models (DDPM) to generate molecular dynamics trajectories from noise. The generative model can then serve as a surrogate to sample rare events. We leverage the properties of DDPMs, such as conditional generation, the ability to generate variations of trajectories, and those with certain conditions, such as crossing from one state to another, using the 'inpainting' property of DDPMs, which became only applicable when generating whole trajectories and not just individual conformations. To our knowledge, this is the first deep generative modeling for generating molecular dynamics trajectories. We hope this work will motivate a new generation of generative modeling for the study of molecular dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Based on DDPM, the author proposes a extension of dynamics diffusion to generate molecular dynamics. The model leverages the conditional generation property of DDPM to generate various trajectories. The model is the first deep generative model for molecular dynamics to the authors' knowledge.

### Strengths
Originality: Combination of DDPM and molecular dynamics. The original part of DDPM is to introduce two variants of sampling. Moreover, a physics-inform layer is introduced to the Unet block. 

Quality: A lot of essential parts are missing.

Clarity: The writing is poor. Many typos and the weird reference style make it hard to read smoothly. There are also missing references in the appendix.

Significance: It is the first generative model for molecular dynamics. The approach enables rare events enhanced sampling. It can reconstruct free energy and dynamics accurately.

### Weaknesses
Unfortunately, the key idea of this paper, using generative modeling (DDPM) for MD simulation, has been done in several works before [1, 2, 3]. They have been archived for over six months, and all have been accepted to relevant conferences/journals. The methods have almost no difference.

Specifically, the core methodology, applying a denoising diffusion probabilistic model to molecular dynamics trajectories, lacks novelty. The paper does not articulate any significant modifications or advancements to the existing DDPM framework that would justify its contribution. The application of DDPM to MD is not novel, and the paper does not address how its approach differs from existing methods in terms of model architecture, training procedure, or handling of specific MD simulation constraints. The absence of a clear technical distinction from prior art is a critical weakness.

### Questions
1. What is the math expression of the energy formulation?
2. What is the performance difference between your proposed 2 sampling methods and the baseline method?
3. Which part is related to Figure 2? The reviewer can guess but wants it to be precise.
4. Wrong reference table for Page 8. The author cited Table 9 for the ablation study of self-attention. But Table 9 is about Jacobian. Missing references on page 18. 
5. Which part of the result shows it can promote symmetry?
Miscellaneous typos need to be further proofread.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes DynamicsDiffusion, a method using the denoising diffusion probabilistic model to simulate the trajectories of molecular dynamics.

### Strengths
- This paper studies an important problem of MD simulation.
- The qualitative results are nice.

### Weaknesses
Unfortunately, the key idea of this paper, using generative modeling (DDPM) for MD simulation, has been done in several works before [1, 2, 3]. They have been archived for over six months, and all have been accepted to relevant conferences/journals. The methods have almost no difference.

[1] https://pubs.acs.org/doi/10.1021/acs.jctc.3c00702

[2] https://dl.acm.org/doi/abs/10.1609/aaai.v37i4.25663

[3] https://openreview.net/forum?id=y8RZoPjEUl

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed Dynamics Diffusion which is based on the denoising diffusion probabilistic model to enable the generation of molecular dynamics simulation trajectories of molecules and the sampling of rare events in the MD simulation. The Dyanmics Diffusion is used to train a UNet-based model which takes in the 3D coordinates of atoms and outputs a single value of conformation energy, of which the Jacobian can be calculated as the predicted noise. The model can also be conditioned on extra parameters such as the simulation temperature to enable conditional generation. To achieve rare event sampling of MD simulation trajectories, the authors adopted the methods of impainting and variation generation that condition the model on specific frames of the trajectories. Experiments have been done using a self-created dataset of particle Brownian motion in double-well and the public alanine dipeptide MD trajectory. Ablation studies of this paper focuses on the UNet architecture (encoder only, self-attention, etc.)

### Strengths
1. Despite some prior work in using diffusion model to train neural networks for the purpose of sampling MD trajectories, application of such method in rare-event sampling in low probability density region is still an under-research field. The impainting and variation generation methods used in this work are very interesting ideas which are demonstrated to work in the paper. 

2. The formulation of the Dynamics Diffusion that predicts the total energy of each frame is similar to methods used in many machine learning potential works. The forces on atoms can be then calculated as the gradient of energy by taking the Jacobian. Such a method ensure the physical validity between the force on atoms and the energy of system.

### Weaknesses
1. The transferability of the proposed UNet architecture can be problematic. The UNet takes a vector with the dimension of $3N$ as input and outputs a scaler (sum of energy of all $N$ atoms). The number of atoms is fixed and there is no information about the atom type. Such design means that the model after training is dedicated to a specific molecule without the possibility of being transferred to another system. It also means that for each molecule, a dataset of molecular dynamics simulation trajectories has to be curated for model training. Although the model can still be used for rare-event sampling as the probability of rare-events can be too low to be caught in MD simulation, the value in generating full MD simulation trajectory using such a model is low. 

2. The number of system tested in this paper is limited. The particle in double-well and alanine dipeptide are relatively small systems. Large systems such as protein dynamics (www.science.org/doi/10.1126/science.1208351) can be added to further strength the claim in this work.

3. The presentation of this work has plenty of room for improvement. The resolution of figures are low (especially Fig. 8 and 11). Labels of both axes in Fig. 11 are illegible. Model related information (architecture, optimizer etc) for both double-well and alanine dipeptide systems are highly redundant. No parentheses or brackets are used for reference in the manuscript. Reading the manuscript with reference author names randomly seperating the sentence is a great experience. When referring to a figure or table, the word "Figure" or "Table" is sometimes missing. Latex render error occurs in page 18 "Result" section. 

4. Some related works of learning MD trajectories using diffusion models (arxiv.org/abs/2305.18046) and rare event sampling using differentiable simulation (arxiv.org/abs/2301.03480) are missing from literature review.

### Questions
1. As shown by the authors, taking Jacobian of the predicted energy term can be costly than predicting the noise (Table A.1). However, the authors only benchmarked the error of models (predicting energy or force) in the 2D double-well system. It is not convincing enough to me that energy prediction+Jacobian is better than force prediction in terms of cost/accuracy tradeoff for larger systems.

2. In Figure 4.c, the trajectories generated by inpainting methods seems to capture the molecular transition dynamics between the two conditioned points. However, the left condition (green dot) is not connected to other states. Is that a plotting mistake?

3. How is the self-attention implemented along with the UNet architecture? The detail is missing in the manuscript.

4. The model architecture and problem formulation enables rare-event sampling with a fixed number of timestep ($\tau$) when the initial and end conditions are given. Based on my understand, the method can garuantee the transition states between the two condition to be sampled. However, the probability of those rare-events cannot be obtained using the model.

### Soundness
2 fair

### Presentation
1 poor

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
In this work the authors present an extension of the standard application of diffusion models in the context of molecular systems to additionally study the dynamics of the systems. The authors achieve this by generating trajectories trained on MD simulation data instead of single instances of the system. The proposed method is evaluated using both a 2D toy example as well as small molecular system in the form of Alanine Dipeptide.

### Strengths
**Originality:** The method lacks algorithmic novelty, most of the presented work are adapted from prior work on diffusion models for time series and molecular data, but this is alleviated by the originality the paper has in applying these previously established techniques to a novel application area. Using Diffusion models for generating molecular transitions is in itself an interesting and novel idea. 

**Significance:** The paper addresses and important problem in (computational) chemistry, the sampling of rare events.

### Weaknesses
Unfortunately the paper lacks in quality and clarity. I've elaborated on this below in my detailed comments and requests for clarifications, but in general the papers notation is hard to follow and unfortunately the experiments do not address the claims made.

### Questions
Please find my detailed list of comments, ordered by section, below.

Where needed, I indicated that something might be a breaking issue. These issue will have to be either clarified or rectified before I will consider increasing my vote to accept.

**Introduction:**
1. This also pertains to the remainder of the paper, please make sure the citations are correctly placed between brackets unless when used as part of the narrative. 
2. The first paragraph of the introduction state "However, their potential in the study of the dynamics of molecular system is still unexplored" when discussing the use of Diffusion models for generating ensembles of molecular conformations. This sentiment is reflected a number of more times throughout the introduction and the remainder of the paper, as such, I would expect the experiments to focus on properties related to the dynamics of the system that can not be determined from the ensembles provided by standard Diffusion models. However, given that the experimental section mostly focusses on evaluating Free Energy estimates (which can be derived from the equilibrium distribution), this does not seem to be the case. I would like the authors view on this observation.
3. Similarly, this paragraph also states "an accurate description is essential to understand the biological functions of proteins and other molecules.". I urge the authors to make these "biological functions" concrete. Are they talking about binding affinity, transition states or some other properties? This distinction is important to be able to judge the contribution of the proposed method. 
4. Related to my prior statement, the last sentence of the first paragraph states "otherwise rare but important events". I would appreciate a clear statement as to why these events are important and would consequently expect the experimental evaluation to focus on correctly identifying them. 
5. The authors state that "standard classical atomistic MD must use an integration time step of 2fs". While this is an often used value, there is no specific requirement for MD to use a 2fs timestep. The word "must" should be reconsidered. 
6. Paragraph 3, 4, and 5 discuss different approaches for sampling rare events, but somewhat lacks organisation. This is largely due to not mentioning general themes or creating a clear topology of the different methods. My understanding is that paragraph 3 discusses ML based methods for reducing the computational cost of determining the molecular forces, paragraph 4 discusses enhanced sampling methods for enforcing transitions, and paragraph 5 discusses direct sampling from the equilibrium distribution using ML frameworks. These overarching themes should be made more clear. In general, I think the paper would benefit from a dedicated related work section that goes more in depth for these 3 paragraphs. The introduction would in that case only need to focus on the most important methods. 
7. Paragraph 3 currently has to narrow of a focus when discussing neural force fields and coarse graining. These are large research fields and can't be done justice with only specific citations. For example, neural force fields come in many other flavours then just the one based on GNNs. To resolve this issue, I would suggest proving citations to survey papers. For example, for machine learning force field [1] is well suited, and for coarse graining [2] provides a clear overview. 
8. For paragraph 4, the discussion of large energy barriers should be part of the earlier discussion on timescales. It should be made clear that "rare events" does not refer to events that happen over a long period in time, but instead to events that happen with very low probability. 
9. For paragraph 4, based on the authors statement to focus on system dynamics, TPS is in my opinion an extremely related topic and requires some additional discussion. For example, an additional discussion of ML based alternatives/extensions here would be appropriate [3, 4, 5, 6]
10. For paragraph 6, the authors use the term "enhanced sampling". From my understanding, this term is often used for methods that augment MD simulations (often by introducing a bias potential or other driving force). This does not seem to be the case for the suggested method. 
11. The list of capabilities of the proposed method states "Generate trajectories that are conditioned to a global parameter like temperature". Based on my own understanding and the presented results, I am not confident that other global parameters, for example friction, will be possible. 
12. Similarly the list of capabilities of the proposed method states "Generate an ensemble of (reactive) trajectories by partially noising and denoising them". I did not find any experimental validation of this. Additionally, a statement such as this would need to be validated to show that the sampling converges to the right distribution over trajectories. 

**Diffusion Generative Modelling for Trajectories**
1. On first reading it is very hard to understand the description of the dataset. And after reading it a couple of times, it is still unclear to me if "trajectory snippet" refers to a single molecular configuration or a short sequence of configurations. Based on the first paragraph, I would assume that the dataset contains trajectories. $p(x)$ would thus be the distribution over trajectories of the system. Ie. $x$ here refers to a trajectory of arbitrary length? If so, it would be beneficial if the authors could include a more formal definition of this probability in terms of the marginal distirbution $p(R_0)$ and the transition distribution $p(R_i | R_{i-1})$. However, based on the second paragraph, i get the impression that $x_i$ is a single configuration, and instead $\boldsymbol{x}_i$ is a short trajectory. This confusion is a breaking issue for me and should be clarified by the authors.
2. The third paragraph, discussing the complete data array is hard to understand. Do the authors intend to clarify in this paragraph that various length of trajectories can be used?
3. In equation one, $\nabla_x$ and $p(x)$ should respectively be $\nabla_{x_i}$ and $p(x_i)$. To prevent further confusion with indexing, I would also suggest to use t instead of i for the updates. 
4. Below the equation the authors state "$\epsilon\rightarrow 0$  we sample one $x_k$ from $p(x)$". I'm unsure what this statement refers to. If $\epsilon\rightarrow 0$ we have no update and thus the sample remains constant. This is independent on whether or not $K\rightarrow \infty$. 
5. Pertaining the same sentence, and related to my earlier point, is $p(x)$ here the distribution over samples, or the distribution over trajectories? 
6. Regarding the last sentence of this same paragraph, the authors refer to a section in the appendix by name here. This should replaced by a forward reference. This happens on a number of occasions throughout the paper. 
7. For equation 2, the notation $R^{(i)}_{\nu, t=0}$  is unclear. Instead of adding the $t=0$ in the subscript would $R^{(i)}_{0}$ not suffice? 
8. I'm unable to follow the authors discussion of the conservative forces and the role the modelling of the forces as the gradient of an energy function plays in this. Especially the claim that UNets do not satsify this property should be substantiated. 
9. Regarding the last sentence of this paragraph, the result presented in the ablation study shows that this difference is not significant. 
10. My understanding is that the authors suggest to use a model architecture that predicts an energy independently for each sample, then sums thism and then takes the gradient to obtain the final force, which is used as the predicted noise. I would like to note that this formalism suggests that the individual samples in the trajectories are independent from each other. ie. a change in one sample does not influence the probability of another sample in the same trajectory. Given that we are looking at trajectories, this is not true. In other words, the inductive bias introduced by the authors does not hold for the modelling of trajectories. This is a breaking issue and I would like to get the authors view on this observation. 

**Experiments**
1. For the discussion of the datasets obtained, it is unclear how the long trajectory is divided into shorter trajectories for the training set. 
2. Regarding the referencing to figures, please correct this to use the correct referencing format where it reads as either "fig. x" of "figure x" instead of simply the number. 
3. Regarding the discussion of the Brownian Motion in a Benchmark potential correctly sampling the wells, the conditional sampling changing the spread of the samples, and correctly identifying the Boltzmann distribution, I'm unsure if these results are informative. As it stands, given that the training data also correctly covers the Boltzmann distribution, it is not surprising that the proposed diffusion method can correctly sample this space. The issue with rare event sampling is that the temperature of the simulation is too low to effectively sample transitions and as a result, the ratio in Boltzmann distribution between different states is incorrect. The temperature for generating the dataset however seem to be high enough to already get a correct estimate. This is a breaking issue and I would appreciate the authors comments on this. 
4. Additionally, an important aspect of the papers contribution is that they extend diffusion models for molecular conformations to the study of dynamics. As of now, the presented evaluation however has focussed on properties of molecular systems that can also be studied without taking into account the dynamics. Standard diffusions models should, in theory, be able to sample the Boltzmann distribution and provide accurate estimates of the FES. This is an breaking issue and I would like to see a more in depth study of the dynamical properties that can not be studied using standard diffusion models.
5. In figure 4, the description of (b1) and (b2) mention Free Energy profiles but the figure shows equilibrium distributions instead. 
6. For 3.2 the authors state, "a (relatively) rare conformational transition occurs around the dihedral angle $\psi$". However, the energy barrier between these two states is considered to be relative low and can thus be sampled in relative short periods at low temperatures. As such, I'm unsure if this transition is suitable for evaluating the method. I would suggest to instead consider transition along the $\phi$ axis. 
7. Again, given that the training for Alanine Dipeptie already correctly determines the FES I'm unsure what the added benefit is from modelling the transitions using a diffusion model. The FES can also be reconstructed using a sample based diffusion model. 
8. The last sentence of section 3.2 reads "pointing to the generalisation capabilities of the method" regarding the observation of a rare transition along the $\psi$ angle. I respectfully disagree with the authors here. This transition is highly physically unrealistic as it flows over a region of high energy.
9. Regarding the ablation study, based on the presented error bars these results are all not significant. This is a breaking issue and I would like the authors comments on how this affects their results 

**Conclusion**
1. The authors state "which can serve as a useful surrogate model of the physics-based simulator, due to its enhanced sampling capabilities". Aside from possible speedup, the presented results do not currently show any enhanced sampling capabilities. As such, I think it would be appropriate for the authors to rephrase this claim. 
2. The authors discuss the extension of their work to generalise accross single molecules. I believe this to be a very good suggestion and hope that the authors continue their research in this direction.

**References**

[1] https://pubs.acs.org/doi/10.1021/acs.chemrev.0c01111

[2] https://pubs.acs.org/doi/10.1021/acscentsci.8b00913

[3] Differentiable Simulations for Enhanced Sampling of Rare Events

[4] Learning Free Energy Pathways through Reinforcement Learning of Adaptive Steered Molecular Dynamics

[5] https://arxiv.org/abs/2207.02149

[6] https://iopscience.iop.org/article/10.1088/2632-2153/acf55c (Only recently published but possibly relevant for the authors)

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper considers the rare event sampling problem in the molecular dynamics simulation which aims to sample the transition state (with a high energy barrier) between two metastable states. Specifically, this paper proposes to solve this problem with a diffusion model that learns to simulate such trajectories (transition paths between the two metastable states). The authors leverage the inpainting flexibility of diffusion models to inpaint missing dynamics in the trajectories. Experiments are conducted on both a synthetic and a real-world molecular dynamics simulation problem.

### Strengths
* Sampling rare events and transition paths is a crucial problem in computational chemistry and has wide applications in studying a wide range of chemical reactions such as protein folding, protein-ligand binding, etc. 
* The proposed method that uses the diffusion model to model the distributions of transition paths and sampling new transition path is technically sound.

### Weaknesses
* The major concern of this work is both the generalizability and scalability of the proposed method. From the method description and experiment section, this method requires sampling a path (though seems to be short, 10 timesteps) as the training data. There is no evidence that demonstrates this could generalize to longer-time dynamics or the transition path (which even requires crossing the energy barrier) nor scale to larger systems since the size of the system scales with the number of the frames used (and I believe for more complicated systems, more frames are needed).
* It seems the different timestep of the path need to be properly isolated when running the diffusion models, otherwise they may affect each other. 
* This is not a major concern but the proposed method itself does not contribute to the technical novelty of this paper as it mostly uses diffusion models developed in previous work and deployed in this problem.
* I am also worried about how physical the generated paths would be. Even though the authors demonstrate the distribution plots and how the dihedral angels change, from my personal experience, sometimes the paths could completely fail while the dihedrals still look good. It would be good to see more evidence in terms of how physical the generated paths are or visualizing some paths.
* Some related work in this area is missing. [1] is also a directed generation approach to find the transition path between two metastable states.

[1] Holdijk, L., Du, Y., Hooft, F., Jaini, P., Ensing, B. and Welling, M., 2022. PIPS: Path Integral Stochastic Optimal Control for Path Sampling in Molecular Dynamics.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
