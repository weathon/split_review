# Latent Intuitive Physics: Learning to Transfer Hidden Physics from A 3D Video

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
\vspace{-2pt}
    We introduce latent intuitive physics, a transfer learning framework for physics simulation that can infer hidden properties of fluids from a single 3D video and simulate the observed fluid in novel scenes. Our key insight is to use latent features drawn from a learnable prior distribution conditioned on the underlying particle states to capture the invisible and complex physical properties. To achieve this, we train a parametrized prior learner given visual observations to approximate the visual posterior of inverse graphics, and both the particle states and the visual posterior are obtained from a learned neural renderer. The converged prior learner is embedded in our probabilistic physics engine, allowing us to perform novel simulations on unseen geometries, boundaries, and dynamics without knowledge of the true physical parameters. We validate our model in three ways: (i) novel scene simulation with the learned visual-world physics, (ii) future prediction of the observed fluid dynamics, and (iii) supervised particle simulation. Our model demonstrates strong performance in all three tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors model a probabilistic particle-based fluid simulator-- which they claim to be the first of its kind, to address the problem of learning inaccessible physical parameters of fluids using visual observations such as density, viscosity, pressure, and transferring these visual fluid properties to simulate new scenes with new initial and boundary conditions.

### Strengths
- The proposed simulator uses consecutive states/image observations to infer fluid dynamics without complete knowledge of the true physical parameters of the fluid.
- The simulator showcases a direct benefit of inferring latent space components apart from its role in the data-generating process-- namely in terms of intuitive physical inference.
- The authors also show real-world experiments on high-resolution images from dyed-water fluid tanks to estimate fluid positions, a challenging task due to reflection, refraction, and the need for high-fps multi-view images. 
- The proposed method can take into account the stochasticity of the underlying fluid dynamics unlike other competitive baselines, and not make fluid category-specific initialization assumptions.

### Weaknesses
- I am not sure about the claim of latent intuitive physics being proposed by them first, especially when similar ideas have existed in the literature on causal representation learning and other intuitive physics methods, albeit in different formats. I think this claim can be softened to say this is the first method to perform this for fluids using 3D exemplars.
- The authors report that the initial velocities are zero for initial state estimation-- how does this tally up with the initial conditions in the particle datasets considered? Isn't a random rotation, scaling, and initial velocity applied to the initial fluid body?

### Questions
- Is the zero initial state velocity a general assumption for all experiments performed? Does this correspond to $(z_{t=1}, \tilde z_{t=1})$ being zero-initialized?
- Why is there a difference in the type of posterior used in the pre-training and the inference stages, being particle-based and visual, respectively?
- Why is the prior learning less prone to overfitting?

### Soundness
4 excellent

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
In this manuscript, the authors investigated a transfer learning framework for physics simulation from 3D Video. While conventional methods require known physical states to infer fluid simulation, this study has developed a framework that operates without them, relying on latent features extracted from 3D video inputs.

### Strengths
I find this paper interesting and agree that getting inspiration from the concept of intuitive physics plays an essential role in the literature. In addition, modeling a model in terms of video-based processing can contribute to future research on understanding human brain mechanisms.

### Weaknesses
This framework includes many model processing, and it was hard for me to understand the whole structure at the first read. In particular, when I tried to understand the model architecture, I expected Figure 3 to include all the information. However,  Figure 3 lacks information about the neural renderer, and the term "type-aware preprocessing" is not used in the main text, leading to comprehension difficulties. Improving the connection between Figures 2 and 3 would enhance readers' understanding.

### Questions
I expect the authors' future direction of real-world videos. It might be beneficial to describe the current state and the challenges more in the main text in addition to the information provided in the Appendix.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper proposes a new learning framework to extract hidden physical properties from a single 3D video to simulate the observed fluid in new scenes. It works in a probabilistic setting with a particle-based model. A parameterized prior gets the visual observations as input and tries to approximate a 'visual posterior' obtained from a learned neural renderer. Numerical results demonstrate the effectiveness of the proposed approach in novel scene simulations and the prediction of the future behavior of the observed fluid.

### Strengths
I have little background in the main areas of this publication. The overall method appears to be sophisticated, well-designed and sufficiently different from related work as far as I can judge.  The numerical experiments make a solid impression. They test different aspects of the proposed method against competitors, give promising results, ablate at least some design choices (of including stages B and C in the framework), and briefly discuss the extension from simulated to real-world experiments.

### Weaknesses
I found the paper very dense and extremely hard to follow for someone outside of the field (like myself). A more introductory section including a more formal (mathematical) definition of which functions with what kind of inputs and outputs are approximated by certain networks would have helped me.  Similarly, the description of the experiments and their evaluation could have been clearer including the metrics used for the evaluation (Tables 2 and 3 just say "prediction errors", Table 4 does not specify a metric at all, and Table 1 refers to "average position errors on unseen fluid geometries and boundary conditions", which I cannot understand either). Yet, such aspects might be clear to anyone more familiar with the topic. As I am neither familiar with graphics, nor with particle-based simulations, nor with learned probabilistic models, I am certainly not a good reviewer for this paper (and I informed the area chair accordingly).

### Questions
I fear I'd have to invest significant extra time in reading this (but also prior) work in order to ask meaningful questions.

### Soundness
3 good

### Presentation
3 good

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
This paper proposes to transfer the attributes of fluid from videos for further simulations in novel scenes. The properties shown in videos are encoded into a latent space, which is further used by pretrained probabilistic physics engine to rolloout the dynamics of fluid in unseen scenes. Experiments show the effectiveness of probabilistic simulation models over baselines as well as the superior performance of physical inference from visual observations.

### Strengths
* A probabilistic simulation model with better performance than existing models.
* The proposed method is able to transfer the properties from videos to simulate the fluid dynamics in novel scene.
* The proposed method obtains superior performance in most cases.

### Weaknesses
1. Since this is a probabilistic model, the predicted dynamics may be different for different sampled feature $\mathbf{z}_t$. Is there any reference to show the variations of predicted particle states? For example, the model would predict one sequence for multiple times and calculate the standard deviation compared with the ground truth.
2. What's the unit of measurement in Table 3? Is it millimeter or centimeter?
3. What's the standard deviation of the prediction errors in Table 2? For example, one scene should include several sequences. The errors may vary from sequence to seqence. What's the variation of the errors?

### Questions
* In Fig 4, is it an accurate reference of the results for the phrase "row 3-6". It seems like the results start from row 2.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
