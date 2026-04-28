# Inverse decision-making using neural amortized Bayesian actors

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Bayesian observer and actor models have provided normative explanations for many behavioral phenomena in perception, sensorimotor control, and other areas of cognitive science and neuroscience. They attribute behavioral variability and biases to different interpretable entities such as perceptual and motor uncertainty, prior beliefs, and behavioral costs. However, when extending these models to more complex tasks with continuous actions, solving the Bayesian decision-making problem is often analytically intractable. Moreover, inverting such models to perform inference over their parameters given behavioral data is computationally even more difficult. Therefore, researchers typically constrain their models to easily tractable components, such as Gaussian distributions or quadratic cost functions, or resort to numerical methods. To overcome these limitations, we amortize the Bayesian actor using a neural network trained on a wide range of different parameter settings in an unsupervised fashion. Using the pre-trained neural network enables performing gradient-based Bayesian inference of the Bayesian actor model's parameters. We show on synthetic data that the inferred posterior distributions are in close alignment with those obtained using analytical solutions where they exist. Where no analytical solution is available, we recover posterior distributions close to the ground truth. We then show that identifiability problems between priors and costs can arise in more complex cost functions. Finally, we apply our method to empirical data and show that it explains systematic individual differences of behavioral patterns.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method for performing Bayesian inference on the parameters of Bayesian observer-actor models, particularly suited for scenarios where Bayesian decision-making can be computationally intractable. The approach leverages a neural network to amortize the decision-making process of the subject by training the network to minimize the expected task-relevant cost with respect to the posterior over latent states and the action distribution. This setup allows for efficient, gradient-based inference of parameters from behavioral data. The authors validate their approach on synthetic data, highlighting its effectiveness and also discuss identifiability issues with recommendations to mitigate them. They further illustrate the method's applicability to human behavioral data.

### Strengths
This paper address an important bottleneck in inverse decision-making by amortizing the agent's behavior using a neural network. This enables efficient Bayesian inference over the subject's behavioral model parameters. The experiments on synthetic data validate the approach through comparison with analytical solutions. The discussion on identifiability and the experiment design recommendations add valuable practical insights.

### Weaknesses
In this work, the proposed approach aims to infer what a subject’s decisions were optimal for. However, there is still an assumption of optimal behavior, which may not always hold in real-world scenarios. Factors such as suboptimal learning or changing task demands can lead to deviations from optimality. Even if these deviations could potentially be reframed as an alternative optimality criterion, doing so would introduce additional identifiability challenges. It would be beneficial  to discuss the limitations of this assumption.

Another potential limitation is that the use of the reparameterization trick requires a specific form of action distribution, which may restrict the model’s adaptability to diverse datasets and tasks where this distributional form does not apply. Specifically, the method is limited to continuous action spaces where the action distribution can be expressed as a reparameterizable distribution, such as a Gaussian. This excludes discrete action spaces or more complex, non-reparameterizable distributions, which are common in many behavioral tasks.

Finally, the presentation could be improved. Several figures lack clear labels and legends, making them difficult to interpret, and acronyms are introduced without prior definition. A revised presentation with attention to these details would enhance the paper.

### Questions
- In figure 2A, could you clarify what is $r^{\ast}$? Should it be $a^{\ast}$ instead?

- The top left panel in figure 2B is missing a label. Should it be $\sigma_0$?

- In figure 2C, it would be useful to include separate x-axis labels for the analytical and nn cases.

- The caption for figure 3B uses $\beta$ as cost asymmetry parameter, but all figure labels use $\alpha$. Are they the same?

- In figures 3B and 3C, it would be helpful to make the ranges of the axes the same in all panels. 

- Figure 4b is difficult to follow, including a legend would be very helpful.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addresses the challenge of using Bayesian models to infer decision-making parameters (inverse decision making) from behavioral data, especially for tasks involving continuous actions where traditional Bayesian methods struggle with computational intractability. 

The authors propose a new method where a pre-trained neural network, trained unsupervisely, was used to approximate an actor model’s parameter. The gradient-based Bayesian inference makes the method relatively efficient. This approach shows promising alignment with analytical solutions where they exist and effectively models human behavioral data in various sensorimotor tasks.

### Strengths
The paper provides an innovative approach by using a neural network to approximate the Bayesian model for inverse inference, which traditionally faces computational intractability issues. Their neural network method, trained in an unsupervised manner, enables efficient inference of decision-making parameters without relying on closed-form solutions or restrictive assumptions (like Gaussian distributions or quadratic costs).

Clear problem formulation and motivation.

### Weaknesses
The authors mentioned that their method could be applicable to a large number of tasks involving continuous responses, including economic decision-making, psychophysical production and crossmodality matching. However, the authors only tested their method on sensorimotor tasks. Testing methods on a diverse set of tasks involving continuous responses would significantly strengthen the paper.

The authors acknowledge that this method is currently constrained to relatively straightforward perceptual models. Extending it to more complex tasks (such as those involving circular variables or advanced cognitive reasoning) remains a limitation in its current form.

### Questions
How scalable is the current approach? What are the computational requirements for training the neural networks for more complex cognitive reasoning tasks?

Could the authors provide more details about the choice of network architecture and hyperparameters?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers an important and fundamental problem of inferring priors and costs from behavior. Typically, the inverse decision-making problem is intractable. Therefore, the author approximate the solution with a neural network, and show that the ground truth can be recovered well on simulated dataset. The author also explore the human behavioral data.

### Strengths
1. The writing is clear, and the core ideas are well articulated. 
2. This paper introduces a novel approach for Bayesian inference about the parameters of Bayesian actor models.

### Weaknesses
The most significant concern is the lack of experimental advancements. This work only presents experimental results from numerical simulations and some simple human behavioral dataset, where simple MLP is able to recover posterior distributions. Presumably, the algorithm proposed by the author will face several challenge when we have to due with high-dimensional input.
1. It might be hard to train $f_{\psi} (\theta, m)$ when $\theta$ contains more than 100M parameters. Specifically, the computational cost of training a neural network to approximate the posterior distribution over a very high-dimensional parameter space is likely to be prohibitive. The number of samples required to adequately train such a network would increase exponentially with the number of parameters, making it impractical for models with 100M+ parameters. Furthermore, the optimization landscape for such a high-dimensional network is likely to be complex, with many local minima, which could lead to unstable or poor performance.
2. The HMC might not have the property of rapid mixing. While the authors mention using HMC, they do not address the potential for slow mixing, especially in complex, high-dimensional posterior distributions. The efficiency of HMC depends on the choice of step size and the geometry of the target distribution. In cases where the posterior is highly non-convex or has strong correlations between parameters, HMC can require a very large number of iterations to explore the space adequately, leading to long computation times and potentially inaccurate results. The authors should provide more details on how they ensure convergence and assess the mixing properties of their chains.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
