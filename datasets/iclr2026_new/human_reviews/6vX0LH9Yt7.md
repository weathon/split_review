## Human Reviewer 1

### Summary
The paper proposes a fluid simulation pipeline integrating numerical simulation, neural physics and generative control. This one provides better latency than existing physics-based methodologies by only employing numerical simulation when encountering complex fluid dynamics through an automatic fallback. In particular, a GNN-based neural simulator handles low-latency updates, while a fallback to the Material Point Method (MPM) retains accuracy when the dynamics is more complex. In addition, a diffusion-based generative controller enables interactive control by mapping user sketches to external force fields. Experiments show reduced latency (11-29%) and competitive physical fidelity across 2D and 3D settings.

### Strengths
- The method is simple and intuitive, with the fallback mechanism ensuring that costly numerical simulation is only performed when the complexity of the fluid dynamics warrants it. While hybrid pipelines are sometimes under-appreciated in the literature, these often yield the best trade-offs.
- The latency reduction is significant. Reducing ~10-30% latency while maintaining fidelity is impressive and of practical utility for interactive graphics applications.
- Interactive control via sketches is visually compelling and, to the best of my knowledge, conceptually new.

### Weaknesses
- My main concern lies on the novelty of the proposed methodology with respect to PAC-Nerf [1]: although used for different objectives, both this work and Pac-NERF combine a learned neural surrogate with a physics-based simulator to get both efficiency and physical plausibility. This work should be mentioned and thoroughly discussed.
- While visually compelling, the sketch interface seems more an application layer than a core technical contribution. It’s unclear to me if the diffusion-based control module is novel or simply applied to this domain.
- The presentation needs some minor adjustment and refinement, with e.g. table 2 floating over section titles.
- While I am not up to date with all the applicable methods, the set of considered baselines seems somewhat limited. This makes it hard to assess the actual benefits with respect to the state of the art.

Considering the weaknesses and the strengths, I am inclined to reject at this time. However, as this field is not my primary area of expertise, I am happy to revise my score if these concerns are adequately addressed in the rebuttal or not shared by the other reviewers.

[1] Li, Xuan, et al. "Pac-nerf: Physics augmented continuum neural radiance fields for geometry-agnostic system identification." ICLR 2023

### Questions
- Can the fallback be learned or adaptive instead of rule-based? E.g. by having a confidence-based trigger instead of a fixed threshold.
- I did not fully understand what influences the latency reduction (e.g. when to expect 10% rather than 30%). Is this dependent on the complexity of the dynamics?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper proposes a neural physics system for real-time, interactive fluid simulation. The work is highly innovative and engaging. It implements a system that employs an AI solver for low-complexity fluid dynamics and a traditional solver for high-complexity dynamics, augmented by a diffusion-based controller for interactive user control.

### Strengths
1. The research addresses a highly interesting and valuable problem, aiming to balance speed, accuracy, and interactivity, presenting a prototype of a potentially practical system.
2. The core idea is novel.
3. The method for generating training data for the controller is simple yet effective.
4. The paper is clearly written.

### Weaknesses
1. In Figure 7, why does the grid MSE finally decrease when transitioning from the neural physics phase to the MPM phase? Intuitively, one might expect it to increase monotonically. Could the authors provide insight into this phenomenon?
2. **Sensitivity of the Fluid Complexity Threshold (`r_c`)**: How sensitive is the hyperparameter `r_c`, used to trigger the MPM solver? If the simulation scenario changes, would the value of `r_c`require adjustment? This dependency may limit the practical utility and generalizability of the simulator.
3. **Integration of Controller and Neural Solver**: The force field learned by the Diffusion-based Fluid ControlNet must be used in conjunction with MPM. Why wasn't the interaction between the controller and the neural physics solver explored? How could such an integration be implemented?
4. **Efficiency of the Diffusion Model**: Sampling from diffusion models is often computationally intensive. What sampling strategy was employed, and what is the associated latency? Are there potential avenues for optimization?
5. **Limited Performance**: While the overall system idea is intriguing, the visual results presented in Figure 11 suggest that the network may not have effectively learned meaningful physical dynamics. Although the latency might be low, the current level of accuracy appears insufficient for practical application. How does the authors plan to bridge this significant gap between performance and usability?

### Questions
See Weaknesses

### Soundness
1

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper presents a hybrid neural Material Point Method (MPM) framework that combines physically based simulation with learned material models to improve efficiency and offer artistic. A graph neural network (GNN) predicts particle accelerations within an MPM solver, operating on lower resolutions to cut latency while remaining compatible with the standard p2g/g2p update loop. The system includes a safeguard: it monitors rollout drift via a complexity proxy and, when a threshold is crossed, automatically falls back to a classical MPM step to correct errors. Lastly, the authors introduce a diffusion-based “Fluid ControlNet” that learns to generate external force/acceleration fields from user sketches; training targets are obtained by a reverse-simulation paradigm that solves the accelerations needed to invert forward dynamics. Results demonstrate a few 2D/3D water/sand scenes.

### Strengths
- The proposed fallback mechanism is am elegant safeguard against simulation drift, enabling stability against potential issues encountered in long-horizon rollouts.

- Integrating a diffusion model to learn reverse accelerations for artistic control is a creative idea, offering a novel way to steer physically based simulations through generative methods.

### Weaknesses
- The presentation in its current format is sub-par. Several plots rely on scattered points that difficult clear understanding, while Figure 7 is particularly confusing. Why does the red rollout abruptly stop? It's also suspicious that the hybrid error high before the cutoff, so it seems like the approximation has a high baseline error. Moreover the abrupt truncation of the red plot could be an attempt of potentially masking issues of the method on further roll-outs. 

- The related-work discussion is brief relative to the breadth of prior neural simulators, hybrid solvers, and control methods; important positioning (what’s new vs. NeuralMPM/MPMNet/Neural SPH) could be sharper.

- No supplemental video is provided, which is crucial for judging visual fidelity, stability, and interactive behavior of fluids (especially the control sequences).

- Results are limited and could be better presented. Is hard to understand what Figure 11 is demonstrating beyond qualitative snapshots, 

- The paper motivates diffusion models by claiming “strong conditional generation with temporal coherence and spatial flexibility,” but the architecture description does not employ explicit temporal attention or other mechanisms typically used to enforce coherence over long horizons in diffusion video models; this mismatch deserves either justification or an ablation.

- The scope feels split across its two contributions: real-time acceleration via a neural–MPM hybrid with fallback and sketch-driven “artistic” control via a diffusion controller. However it feels like both contributions are under-explored, seems like each direction could merit a focused paper with deeper ablations.

### Questions
- What are the parameters used to model the sand and water materials? 
- Did the authors collect feedback from users about how intuitive/efficient the proposed force-based control strategy is?

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a hybrid neural-numerical framework for real-time, interactive fluid simulation. A graph-neural-network  runs at reduced spatio-temporal resolution to cut latency, while a safeguard falls back to an MPM solver to preserve fidelity when particle acceleration is high. On top of simulation, the authors introduce a diffusion-based controller (Fluid ControlNet) trained via a reverse-simulation data pipeline to generate external force fields from user freehand sketches for intuitive interactive fluid control.

### Strengths
The blend of classical and neural approaches effectively balances their respective strengths and limitations, making this a pragmatic and promising path forward.

### Weaknesses
While the hybrid direction is practical, I find the core mechanism of monitoring the error then hard-switching to a classical solver is a generic wrapper with limited novelty. As presented, it could be applied to most neural simulators; the paper should demonstrate if any part of their design makes fallback uniquely efficient, and compare against to other neural simulation baselines by applying the same fallback onto other neural simulators. 

The generative controller is also weakly motivated: classic optimization-based methods for interactive fluid control (e.g., “Fluid Control Using the Adjoint Method” ; McNamara et al., 2004) tackle the same task without needing diffusion models for control. Table 3 also showed little improvement by using the generative model.

### Questions
Novelty of fallback. What, concretely, makes your fallback uniquely efficient versus a generic wrapper, if there is any? Can you support it with an experiment? 

Comparison with baselines: please compare your method with other neural simulation methods by applying the same fallback mechanism so performance on the neural simulation can be evaluated.  

Controller motivation & baselines. Why diffusion over classic optimization/adjoint control (e.g., McNamara et al., 2004) for the same interactive tasks? Table 3 shows little evidence that the generative force field is helping much.

Discussion with related works:   McNamara et al., 2004 is closely related and is not discussed in related works. Please check missing references.

### Soundness
1

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4