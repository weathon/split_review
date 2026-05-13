# Generating Freeform Endoskeletal Robots

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
The automatic design of embodied agents (e.g.~robots) 
has existed for 31 years and
is experiencing 
a renaissance of interest in the literature.
To date however,
the field has remained narrowly focused on
two kinds of anatomically simple~robots: 
(1)~%
fully rigid, jointed bodies;
and 
(2)~%
fully soft, jointless bodies.
Here we 
bridge these two extremes with
the open ended creation of 
terrestrial 
endoskeletal robots:
deformable soft bodies
that leverage
jointed internal skeletons 
to move efficiently
across land.
Simultaneous de novo generation 
of external and internal structures
is achieved by 
(i)~%
modeling 
3D endoskeletal body plans 
as 
integrated 
collections of 
elastic and rigid cells
that directly attach
to form
soft tissues
anchored to
compound rigid bodies;
(ii)~%
encoding these
discrete mechanical subsystems 
into a 
continuous yet
coherent
latent embedding;
(iii)~%
optimizing the sensorimotor coordination of 
each decoded design using 
model-free
reinforcement learning;
and 
(iv)~%
navigating this
smooth yet
highly non-convex
latent manifold using 
evolutionary strategies.
This 
yields an 
endless stream of 
novel species of 
``higher robots'' 
that, 
like all higher animals,
harness 
the 
mechanical advantages 
of both 
elastic tissues
and 
skeletal levers
for terrestrial travel.
It also provides 
a plug-and-play 
experimental 
platform
for benchmarking
evolutionary design 
and
representation learning 
algorithms in complex hierarchical embodied systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes (1) a simulation framework, (2) a generative model, and (3) a co-optimization procedure for endoskeletal robots that consist of both rigid bones and soft tissue, in contrast to rigid-only or soft-only bodies in many previous works. (1) The endoskeletal robots are simulated as a collection of elastic and rigid voxels in a 3D space, with type-specific constraint forces between them. (2) The learning-based generative model is trained by autoencoding a large dataset of synthetic training data (valid voxelized body plans) into a latent space. After training, the decoder generates voxelized body plans from this latent space, which are post-processed into a graph structure defining a simulated robot body. (3) The co-optimization procedure uses two nested training loops, in which the outer "evolutionary" loop searches through the latent space with CMA-ES to design better morphology, and the inner "lifetime" loop learns a reused actor/critic architecture with PPO to control an arbitrary morphology on control tasks. The agent is rewarded for forward locomotion across a variety of terrains.

### Strengths
**S1: Novelty.** Unlike many previous works that focus exclusively on rigid or soft bodies, this work combines them into a single framework. The manuscript provides an extensive related works section for situating this work within the field, which was helpful.

**S2: Clarity.** The manuscript was a pleasure to read. The writing is clear and concise, with appropriate details provided in the extensive appendices. The mathematical notation is simple and consistent. The figures are thoughtfully designed. Overall, great work!

**S3: Quality.** The methods are appropriately applied, and the experimental results are technically sound and informative (especially with the ablations).

Overall, I believe this is a solid work which I will recommend acceptance of, provided that my feedback below is adequately addressed.

### Weaknesses
 **W1: Code.** I did not see a link to code, which is critical for reproducibility. Can the authors please provide this during the rebuttal?

**W2: Videos.** It will be useful to see qualitative results (i.e. videos) in addition to the quantitative reward plots. Currently, the reward values aren't contextualized, so it's had to tell if the behavior is actually good, only that it's improving.

**W3: Ablation of discrete action space.** It would be useful to show the comparison of discrete vs continuous action space (line 310), and provide some discussion. Is this a constraint from your simulation, or a learning issue? Wouldn't PPO also be able to control continuous action spaces, as it does in other related sim works?

**W4: Minor figure/text edits.**
- Figure 2 has nice aesthetics, but could be simplified. It has a lot of extraneous subpanel labels that aren't useful (Figure 5 too). Really the figure has 3 columns (initial, training, final), and the rows are instances of the same population. This message could be highlighted with in-figure annotations, like an arrow indicating the direction of training time.
- Figure 1 looks pretty, but what is its purpose? It looks like a bunch of molecules floating on a dark ocean, which was confusing as it primed me to think about fluid simulations, (but the sim only works on terrestrial envs, line 533). Also, the entire caption is one really loong sentence.
- Typos: line 376 sampled, line 398 the the, Fig 7 subpanel A label, Equation 10 star misplaced

### Questions
**Q1: Actor/critic inputs.** What's the rationale for conditioning the actor and critic on different state?

**Q2: Ablation of evolved designs.** On line 498, is that statement a mistake? It does not seem like Optimized RL is doing well with the initial designs. And I'm not sure how catastrophic forgetting is related, i.e. forgetting how to control a bad initial policy?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors introduced a new brain-body design of freeform endoskeletal robots. The authors introduce a computational framework that integrates the generation of external and internal structures through a combination of 3D modeling, latent space encoding, reinforcement learning, and evolutionary strategies.

### Strengths
1. The authors integrated 3D modeling, latent space encoding, reinforcement learning, and evolutionary strategies into a cohesive framework for robot design.

2. Optimizing in the latent space significantly reduces the computational burden of the co-design process.

3. The use of a universal controller and simultaneous optimization of morphology and control through reinforcement learning demonstrates the robustness and adaptability of the approach.

4. The research topic of this paper is interesting and significant.

### Weaknesses
1. While the paper focus on the co-design problem of endoskeletal robots, which is innovative, the main contribution of this paper seems to be not clear. Besides, the analysis of scalability and the potential real-world applications are needed.

2. It would be better to have a picture to describe the whole co-design pipeline of the method. 

3. The whole co-design pipeline (Learning the latent space description-> Training a universal controller via RL-> Optimizing morphology through EA) is not new. The most important innovation of the article seems to turn out to be the modeling of endoskeletal robots.

4. The authors utilize multiple advanced techniques, which may lead to high computational costs and complexity, might limit practical applications.

5. The latent space encoding, while effective, may lack interpretability, making it difficult to understand the underlying principles that guide the design evolution.

### Questions
1. Could the authors provide more insights into the latent space encoding? Specifically, how do specific regions of the latent space correspond to different types of robot designs?

2. Can the proposed method find endoskeletal robot morphologies which can generalize to several tasks?

3. How does the proposed method compare to other state-of-the-art approaches (Such as transform2act, ea+rl bi-level optimization) in terms of design diversity, performance, and computational efficiency?

4. What are the potential real-world applications of the robots designed by your methods? How feasible is the transition from simulated designs to real-world robotic systems? What are the main challenges in this transition?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors designed and implemented a software library capable of generating three-dimensional freeform endoskeletal robots. Across various tasks, the researchers demonstrate the simulations’ ability to provide a means of benchmarking the evolutionary design and representational learning of complex embodies systems.

### Strengths
Provides an easy-to-use computational design of freeform endoskeletal robots and the library software for benchmarking the representations and evolution of these agents over time.

### Weaknesses
The paper's conclusion that "design evolution finds better designs but they do not imply that evolution (i.e. cumulative selection) is necessary" appears to contradict the study's methodology, which used reward values that created selection pressure across generations. Please clarify how this conclusion aligns with the reward-based selection used in the experiments, and if possible, provide evidence that random mutations alone could achieve similar results. We recommend rephrasing to better reflect the relationship between mutations and selection pressure while maintaining the valuable insights about design diversity.

### Questions
What insight may explain the evolution of the agents in these specific directions? Can we find similarities of this biologically?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper bridges the two opposing types of robots namely fully rigid and fully soft robots in current literature by introducing a novel multi-physics simulator of 3D endoskeletal robots that feature rigid, jointed bodies covered by soft materials. The authors employ a variational autoencoder trained on synthetic body plans to yield smooth and expressive latent representation of morphology. With the aid of a Graph Transformer-based modular control policy trained alongside morphological evolution, the authors showcase the feasibility of their simulation environment and latent representation to support the emergence of complex, lifelike morphologies capable of navigating various terrains. This work lays an important foundation for developing more sophisticated, biomimetic and free-form artificial organisms.

### Strengths
1. The paper introduces an open-source simulation environment of 3D endoskeletal robots with four predefined terrains. The voxel-based representation is conceptually simple and meanwhile offers great convenience for future work to benchmark their brain-body co-design algorithms. It also provides an open-endedness to design more complicated terrain maps for specific needs. 

2. I appreciate that the authors meticulously designed a suite of control experiments to demonstrate the indispensability of morphological evolution. This is generally absent in existing brain-body co-design studies, which take morphology and control as a whole to evaluate task performance.

### Weaknesses
The introduction seems a bit too verbose. The authors are suggested to only keep the most essential information regarding current state of the art and their contributions, and relegate the remaining to Related Work or Appendix.



### Questions
1.Some previous studies have demonstrated that Graph Neural Networks tend to have difficulty with long-distance communication, as messages would be diluted in multiple hops [1]. Could you explain why you have chosen a Graph Transformer, instead of a conventional Transformer with full connection between modules (as in [1,2])? 

[1] Kurin V, Igl M, Rocktäschel T, et al. My body is a cage: the role of morphology in graph-based incompatible control[C]//9th International Conference on Learning Representations. 2021.

[2] Gupta A, Fan L, Ganguli S, et al. Metamorph: learning universal controllers with transformers[C]//International Conference on Learning Representations. ICLR, 2022.

2.Is your simulation environment currently restricted to locomotion on various terrains? Does it or will it support manipulation tasks, such as carrying or pushing an object? 

3.Could you explain why the population is cloned during policy training? 

Thank you!

### Soundness
4

### Presentation
3

### Contribution
4
