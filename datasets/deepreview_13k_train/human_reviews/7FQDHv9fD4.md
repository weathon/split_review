# Decomposing heterogeneous dynamical systems with graph neural networks

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Natural physical, chemical, and biological dynamical systems are often complex, with heterogeneous components interacting in diverse ways.
We show that graph neural networks can be designed to jointly learn the interaction rules and the structure of the heterogeneity from data alone.
The learned latent structure and dynamics can be used to virtually decompose the complex system which is necessary to parameterize and infer the underlying governing equations.
We tested the approach with simulation experiments of moving particles and vector fields that interact with each other.
While our current aim is to better understand and validate the approach with simulated data, we anticipate it to become a generally applicable tool to uncover the governing rules underlying complex dynamics observed in nature.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes using graph neural networks (GNNs) to jointly learn interaction rules and heterogeneous structure in complex dynamical systems from data alone. Extensive experiments on simulated systems including particle interactions, wave propagation, reaction-diffusion, and signaling networks, showing its good performance.

### Strengths
1. The paper is in general easy to follow and with clear writing flow. The problem is well-motivated, by using GNN to learn system dynamics over time and in the meanwhile, uncover the underlying latent properties in an interpretable way that facilitates further analysis.

2. The evaluation of dynamical systems in the experiment sections are extensive, though adding some baselines for comparison would be better.

### Weaknesses
1. There is no related work section. Some works are discussed in the introduction part, but there are many existing neural simulators that use GNN to rollout trajectories of multi-agent dynamical systems [1,2,3,4]. Discussion about existing work and comparison in the experiment section are helpful to provide a comprehensive analysis.

2. As mentioned above, for rollout MSE across different datasets, it is suggested to compare against representative baselines. Also the run time comparison can be included across compared methods.

### Questions
The authors mention the method can infer the underlying governing equations, (line 17) but I do not see any analysis in the experiment part. It would be interesting to see how can we extract formula from a learned GNN.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper fits GNNs to dynamic systems and showed that it is feasible.

### Strengths
- The figures are well-presented.
- The experiment details are clear.

### Weaknesses
 - First of all, what does heterogeneity mean in this context? Meaning that the particles are of different types? The closest thing I can find to a definition is "The latent heterogeneity of the particles is encoded by a two-dimensional learnable embedding $a_i$ that is part of the node features." But why two?
- The simulation of dynamic systems has been routinely done by GNNs, most notably Sanchez-Gonzalez et al., 2020, as cited in the paper. The only difference seems to be that they do not consider this "heterogeneity" whose definition is not clear? But does this method introduced here even outperform the baselines without such input?
- This paper uses a very classical method that is not equivariant on 3-dimensional space. How does it deal with rotational equivariance?
- There is no baseline nor quantitative comparison.
- No code is provided.

### Questions
See Weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper demonstrated that a graph neural network can both learn the dynamics and structure of a dynamical system. The parameters showed both underlying structure and differential equations. The proposed model was tested on several simulated datasets, and visually showed a meaningful relationship between the true and predicted values.

### Strengths
This model can be applied to various complex realistic systems to reveal the underlying structure and dynamics.

### Weaknesses
1. The presentation is poor. It is hard to track simulations they did for the model. People need to check figure, table, video and supplementary figure to understand what they have done without any hint or explanation.
2. The interpretations are lack to explain their results. Only showing several latent representations are not enough to convince or help understand the model's strength.

### Questions
1. Have you compared your proposed model with a conventional GNN, i.e., the loss is l2-norm between x and x_hat? What is the significant improvement by the proposed model?
2. How do you choose to use first-order or second-order derivative to train the model?
3. At a single time point, why don't you use both first-order and second-order or even with higher-order derivative to train the model, where the information should be more compact?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper demonstrates that GNNs can be designed to jointly learn both interaction rules and heterogeneous structures directly from data. The learned latent structures and dynamics can then be used to decompose complex dynamic systems and infer the underlying governing equations. To evaluate the proposed approach, simulation experiments on moving particles and vector fields are conducted, highlighting its potential for capturing intricate dynamics.

### Strengths
The paper introduces a novel approach where GNNs jointly learn interaction rules and heterogeneous structures directly from data, enabling the decomposition of complex dynamic systems and inference of underlying governing equations. Simulation experiments on moving particles and vector fields demonstrate the model's effectiveness in representing complex dynamics, with promising potential for broader applications across various types of dynamic systems.

### Weaknesses
Novelty: Ordinary Differential Equations (ODEs) and Partial Differential Equations (PDEs) are well-established frameworks for modeling the evolution of dynamical systems over time. Several ODE/FDE-based GNNs, such as Continuous Graph Neural Networks (CGNN), have leveraged this approach to simulate time-evolving, interacting components in these systems. While the authors mention using simple MLPs instead of differentiable functions, it remains unclear what advantages MLPs offer over ODE-based methods. A discussion on this aspect would clarify the benefits of MLPs in the proposed approach and strengthen the novelty claim. Is it possible to provide a comparative analysis between their MLP-based approach and ODE-based methods like CGNNs, and also discuss the relative advantages and disadvantages in terms of computational efficiency, expressiveness, or ease of implementation?

Lack of experiments over real data: While the approach is tested on simulated data, it lacks validation on real-world data observed in natural systems. This limitation raises concerns about the method’s practical effectiveness and generalizability to real-world dynamics, where noise and complexities may differ significantly from simulations. Including experiments with real data would strengthen the evidence for the approach’s applicability, for example, applying the proposed method to data from physical experiments, biological systems, or social networks is more convincing.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
