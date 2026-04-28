# Compositional Generative Inverse Design

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Inverse design, where we seek to design input variables in order to optimize an underlying objective function, is an important problem that arises across fields such as mechanical engineering to aerospace engineering. Inverse design is typically formulated as an optimization problem, with recent works leveraging optimization across learned dynamics models. However, as models are optimized they tend to fall into adversarial modes, preventing effective sampling. We illustrate that by instead optimizing over the learned energy function captured by the diffusion model, we can avoid such adversarial examples and significantly improve design performance. We further illustrate how such a design system is compositional, enabling us to combine multiple different diffusion models representing subcomponents of our desired system to design systems with every specified component. 
In an N-body interaction task and a challenging 2D multi-airfoil design task, we demonstrate that by composing the learned diffusion model at test time, our method allows us to design initial states and boundary shapes that are more complex than those in the training data. Our method generalizes to more objects for N-body dataset and discovers formation flying to minimize drag in the multi-airfoil design task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address the complex task of inverse design with what I believe is a rather novel approach. 
A first line of work optimizes over the forward process using an optimization procedure (CEM, gradient based optimization), this suffers from falling into adversarial local optima and potentially poor likelihood of the generated solution.
To fight such a behavior, the others propose to optimize over a linear combination of an EBM, accounting for the generation of likely condition, and the design objective.
In addition, the authors propose to estimate the EBM in a compositional fashion to simplify learning. 
The proposed framework is tested through two main sets of experiments: N-body problem and airfold optimization

### Strengths
The authors approach is very interesting.
The paper is straightforward and aims at directly addressing the problem it uses. 
It is clear and fairly well-written. The experiments provided by the authors seem to confirm the validity of the proposed method.

### Weaknesses
I personally found the experiments slightly harder to read compared to the rest of the paper. For other remarks see questions.

### Questions
1. Can the authors describe the role of $\alpha$ line 12, Alg.1 ?
2. Can the authors comment on the choice of the energy function for the airfold design ? How do we compare to training data ?
3. Can the authors comment on how to balance $\lambda$ during the optimization ? Could the optimization end up in a poor likelihood region ?
3Bis. Can other forward / optimization steps be considered for such a task ?
4. What is the influence of the number of optimization steps  ?
5. For the airfold design: what is the relationship between the initial objective function and the reported ratio  ? Which quantity is actually at stake here ? 
6. Can the authors think of any limitation when applying a compositional energy approach ? For instance is it computationally efficient to learn “smaller models” vs one big EBM ?

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
This works investigates inverse desigs in dynamic systems. The authors look into inverse design while avoiding adversarial samples in order to improve efficiency. The authors proposed a new formulation for inverse design by energy optimization, and introduced the Compositional Inverse Design with Diffusion Models (CinDM), which is able to branch out and generate further designs than observed.

### Strengths
1. The generative optimization structure containing both the energy-based model and the design objective is quite unique and novel. It enables the optimization problem for design to be more readily approached via the joint learning procedure.
2. The experiments conducted in Section 4 are complete which explains well the questions raised at the beginning of the section.
Overall, the ability shown in the work to generalize is quite impressive and seems promising with potential to be applied to more applications.

### Weaknesses
 1. This is more of a question. On the joint optimization, it is trying to minimize the energy component which is calculated from the trajectories and the boundary, and minimizing the design objective as well. It is proposed to achieve this by optimizing the design and the trajectory at the same time. In the joint optimization formulation as in Eqn.(3), the design objective function is weighted by $\lambda$. I am curious how this hyperparameter is estimated/configured, and how sensitive the optimization results are to the change in $\lambda$.

### Questions
Additionally, I wonder whether changing its value will lead to different results in the experiments.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new approach to inverse design by optimizing over the energy function learned by a diffusion model combined with the target function instead of backpropagating through (surrogate) dynamics. The "compositional" comes from the fact that the energy functions/diffusion models are learned over overlapping slices across time and state space. Experiments are performed on fluid dynamics and n-body dynamics tasks.

### Strengths
Originality:

- the paper adopts or re-invents various tricks I've seen across the literature (unrolling across time steps and jointly diffusing, using a diffusion model as a smoothed ODE effectively) but does so in a clever combination
- novelty: I'm not aware of any similar work, although conditional policydiffusion or codefusion might come close, and adding noise to FNO etc. is standard practice
- clarity: overall clear presentation, especially on hyperparameters (kudos!), some questions (see below)
- significance: difficult to judge in a still rather niche topic, but I think the general idea (learning sliced energy models to perform inverse design on) has promise to have high impact

### Weaknesses
 - maybe I missed it, but page 7, I don't think $M$ is ever defined. How exactly do you train $M$ beyond the range of timesteps in training?
- I would question the compositionality of the method and call it a "piecewise" or "mixture" approach? Given that you simply partition the spaces required into overlapping pieces (unless I misunderstood something)
- Were the numbers of parameters matched for the different baselines? Given that you a partitioned energy functions, there might be potential for unfairness here?

### Questions
- Did you try training a single shared network across the overlapping chunks? I was kind of expecting something like this (maybe with different degrees of subsampling to give long and short range dynamics)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel approach to tackle inverse design problems commonly found in engineering fields by optimizing energy functions within a diffusion model, instead of using traditional optimization techniques over learned dynamic models. This method addresses the challenge of adversarial modes encountered in the optimization process, improving design performance. By employing a compositional design system, the paper illustrates the potential to merge multiple diffusion models representing different subsystems, enhancing the complexity and specificity of the design.  The introduced Compositional Inverse Design with Diffusion Models (CinDM) method is highlighted for its capability to address out-of-distribution and more intricate design inputs beyond the training data, demonstrating promising advancements in the field of inverse design.

### Strengths
- A novel approach in addressing an interesting problem in the field of neural inverse design.
- The results seem to be well enough, showcasing the benefits of this novel approach. However, further evaluation with the state-of-the-art counterpart neural inversion methods is required.

### Weaknesses
The manuscript lacks discussion on some pivotal related works, notably the contributions by Ren et al. [1] and Ansari et al [2]. Ren et al. elucidated various neural inversion methodologies and assessed their efficacy and accuracy encompassing Neural Adjoint, Tandem, Invertible Neural Networks, among other techniques. Additionally, they proposed a regularization scheme to mitigate the occurrence of out-of-distribution solutions.

On the other hand, Ansari et al. put forth a method wherein uncertainty information is integrated during the neural network inversion process. They asserted a multitude of benefits for this tactic, such as avoiding out-of-distribution solutions and erroneous local minima, alongside diminishing the model's susceptibility to initialization conditions.

These inversion methods should be mentioned and where possible compared with the proposed approach. In the cases where a comparison is not possible, sufficient explanation is required.

[1]  Ren, Simiao, Willie Padilla, and Jordan Malof. "Benchmarking deep inverse models over time, and the neural-adjoint method." Advances in Neural Information Processing Systems 33 (2020): 38-48.

[2] Ansari, Navid, et al. "Autoinverse: Uncertainty aware inversion of neural networks." Advances in Neural Information Processing Systems 35 (2022): 8675-8686.

- A proper discussion over the limitations is missing.
- The code and dataset is missing.

### Questions
- How other neural inversion methods perform in the context of the proposed experiments?
- How sensitive is this inversion method to hyperparameters and initialization?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
