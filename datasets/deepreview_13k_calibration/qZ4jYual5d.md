# Robust Lurie Networks with Controllable Convergent Dynamics

- Decision: Reject
- Avg Score: 3.50
- Scores: 1, 5, 5, 3

## Abstract
The Lurie Network is proposed as a unifying architecture for modelling time-invariant nonlinear dynamical systems. Many existing continuous-time models including Recurrent Neural Networks and Neural Oscillators are special cases of the Lurie Network when applied to this domain. Motivated by the need for a general inductive bias, shared by many systems, this paper proposes an approach to enable network weights and biases to be trained in such a manner that a generalised concept of stability is guaranteed. This generalised stability measure is that of $k$-contraction which enables global convergence to a point, line or plane in the neural state-space. This result is leveraged to construct a Graph Lurie Network (GLN) satisfying the same convergence properties. Unconstrained parametrisations of these conditions are derived allowing the models to be trained using standard optimisation algorithms, whilst limiting the search space to solutions satisfying the $k$-contraction constraints. Empirical results show significant improvement in terms of prediction accuracy, generalisation and robustness compared to other unconstrained and stability-constrained models. Furthermore, both models consistently learnt representations which respected the convergence behaviour of the dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a new architecture for modeling dynamical systems and continuous-time recurrent neural networks. The architecture is theoretically proven to be stable using the k-contraction theoretical framework. The architecture is applied to toy ODEs and compared to other Neural ODE and continuous time architectures.

### Strengths
Constructing networks to be stable from the ground-up and theoretically proven to be stable is always welcome.

The methodology for carefully constructing test trajectories is sound; this is a detail that is often overlooked.

### Weaknesses
The paper is impacted by presenting only very simple example problems. The experiments are applied to 3 degree of freedom first order ODEs that are arbitrary and not very commonly studied. The models only have 87 parameters. Trivial problems are good if the main contribution of the paper is a key insight about ML. However, the paper purports itself to demonstrate a new architecture that is proven to be superior with empirical demonstration of superior performance. For that type of claim, “serious” benchmarks for systems that are difficult to learn, due to stiffness or complexity, are required. E.g., Lipschitz RNN did sequential MNIST, audio prediction, and adversarial robustness.

Further, the problems are so small and simple that the proofs do not seem relevant. None of the problems demonstrate the necessity or improvement of the architecture. Would a naive model not be able to learn those systems? How are graph neural networks relevant to problems with only 3 dimensions? Connectivity in that case is trivial.

A minor flaw that could be fixed easily: The datasets are designed by integrating the Euler method. The accuracy of the training data construction was not discussed, nor time step size. This probably indicates that the ground truth solutions used as training data are actually quite inaccurate, and the model is not learning the actual dynamical, i.e. they are just overfitting to very simple algebraic recurrences. A much more accurate integrator would have to be used to generate the data (standard is Dormand-Prince, ode45, with a very small tolerance), or, alternatively, problems with analytical solutions, such as the nonlinear pendulum. The nonlinear pendulum in xy coordinates is a good tough benchmark problem because it is very stiff, has an embedded constraint, has different cycles of attraction, is energy conserving, and has 4 dimensions, and has an analytical solution.

Significant details on how the model is trained are missing. What are the hyperparameters of the architecture? What is the loss function? What are the labels that are used? Is the label dx/dt, or is the loss function on next timestep prediction? Which ML libraries are used? What is the HPC system that was used? CPUs/GPUs/TPUs?
- Page 3: What is y?
- What is \Phi? and \phi? Its definition seems to change.
- Is Appendix A novel work? Or just a summary of well known results? A few background definitions and references are nice, but 5 pages is excessive for a conference paper with an 8 page limit.
- Figure 3 : The stddev is not very informative for N=3 samples. Drawing 3 lines would be clearer. At that respect, what does the loss trajectory show that is not reflected in the tables? There is also nothing meaningful to say about the loss trajectory.

### Questions
- Significant details on how the model is trained are missing. What are the hyperparameters of the architecture? What is the loss function? What are the labels that are used? Is the label dx/dt, or is the loss function on next timestep prediction? Which ML libraries are used? What is the HPC system that was used? CPUs/GPUs/TPUs?
- Page 3: What is y?
- What is \Phi? and \phi? Its definition seems to change.
- Is Appendix A novel work? Or just a summary of well known results? A few background definitions and references are nice, but 5 pages is excessive for a conference paper with an 8 page limit.
- Figure 3 : The stddev is not very informative for N=3 samples. Drawing 3 lines would be clearer. At that respect, what does the loss trajectory show that is not reflected in the tables? There is also nothing meaningful to say about the loss trajectory.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of learning dynamical systems with convergence guarantees. Specifically, it enforces the k-contraction property on Lurie Networks by finding sufficient conditions on the parameters to guarantee the property and constructing the network with parameterizations that inherently satisfy the sufficient conditions. Their parameterizations allow unconstrained optimization of the parameters to train the model. The results are extended to construct a Graph Lurie Network to find more efficient parameterization to guarantee the k-contraction property for the multiple dependent Lurie Networks rather than just treating them as a giant aggregated Lurie Network. Experimental results show that enforcing the k-contraction property improves accuracy, generalization, and robustness on various benchmarks.

### Strengths
The paper is well-written and easy to follow. The authors clearly deliver the main benefits and drawbacks of each sufficient condition they established. The experiments demonstrate the effectiveness of the proposed architectures evidently.

### Weaknesses
The proposed parameterizations are sufficient to guarantee the sufficient conditions for the k-contraction property. However, it is unclear how restrictive the parameterizations are in expressing any Lurie Networks that satisfy the k-contraction property. Any explanation or intuition for this point would be helpful in understanding the power of the proposed architecture.

The experiments are done only for the low-dimensional systems. Results for high-dimensional systems could demonstrate how much imposing the k-contraction property increases sample efficiency with limited data.

Experimental results for the proposed parameterization of GLN (in Thm. 7) are missing. Practical examples would help the readers understand the value of the extension to GLN.

This is a minor error, but the notation [i, j] for integers i,j is used differently from its definition in Section 2.1 to indicate a continuous interval in the experiment section.

### Questions
When we are learning unknown systems, how should we decide the value k?

In the experiments, why the biases of the Lurie Networks were set to zero for some tasks?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Simple neural ODE with convergence guarantees via $k$-contraction analysis

### Strengths
1. neural ODEs with convergence guarantees
2. $k$-contraction analysis to neural ODE could be useful for control theory and computational neuroscience

### Weaknesses
1. Most applications of neural ODE in deep learning do not care the properties of converging to a single or a few equilibrium points. Even for those stable LSSM, the Hippo matrix construction ensures that the model converges very slow in order to achieve long-range memory. From my understanding, the model in this work may have fast converging behaviors, and thus it could suffer from the vanishing gradient issue.
2. The Lurie network in (2) only contains a single hidden layer, which means that the model expressivity is quite limited. However, in the literature of Lurie networks [1-3],  the general implicit network model contains very deep MLPs, residual networks and many other feed-forward networks as special cases. 
3. The experiments in this work use very tiny networks. The largest one only has 983 parameters.
4. The theoretic contribution is incremental as it involves application of $k$-contraction theory (Wu et al. 2022) to a simple neural ODE, i.e., the SDP formulations in (4) and (7) follow directly from Theorem 1. The model parameterization method is nice, but a similar pipeline has already established in [3] for contraction analysis ($k=1$). 
5. A few important references are missing in this paper. For example, to the best knowledge of the reviewer, Ref. [1] is the first paper to form an MLP as a Lurie system and then use incremental analysis to obtain a tight Lipschitz bound. Ref. [2] further extended it to general implicit network and Ref [3] showed the connection between implicit networks and contracting neural ODEs.

### Questions
1. Consider the case of $k=1$, does your parameterization (9) contain all contracting models of the form (2)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a unifying architectures for time series that represent $k$-contracting dynamics (Lurie network). The $k$-contracting dynamics are usually found in many dynamical systems. For example, $k=1$ represents stable systems with only 1 stable equilibrium points in the state-space, $k=2$ represents equilibrium points (stable & unstable) that lies on a line in the state-space, and $k=3$ represents system that can oscillate indefinitely. The authors first present a general form of Lurie network and present the analysis of the constraints of its parameters to achieve the desired value of $k$. They also present a way to represent the architecture so constrained optimization can be avoided during the optimization. Experimental results comparing (constrained and unconstrained) Lurie networks with other architectures are present for some small test cases.

### Strengths
1. The paper presents a unifying architecture (Lurie network) to represent $k$-contracting dynamics and also its parametrization to avoid constrained optimization during the training.
2. Sound theoretical justification of the architecture's capability of representing $k$-contracting dynamics.
3. The authors also present a way to incorporate Lurie network in graph case.

### Weaknesses
I have several major concerns and some minor concerns. The following is my major concerns:
1. The presented architecture does not take external inputs. The network that is represented as $\dot{x} = Ax + B \Phi(Cx + b_y) + b_x$ does not allow any external inputs (e.g., $u(t)$ in LSSM and Neural Oscillator) from the another layer to influence the output of the presented layer.
2. The non-existence of external input (as in my previous point above) makes the claims of Lurie network being a generalized form of other architecture (e.g., LSSM, Neural Oscillator) invalid. The other layers like LSSM can be a part of a bigger neural network by taking the output from other layer as the inputs ($u(t)$), while the presented Lurie network can't.
3. It seems like prior knowledge of the dynamics of the modelled system needs to be known (i.e., whether it's $k=1$-contracting, $k=2$, or $k=3$). This makes it hardly applicable as we would not know the dynamics of most systems of interest. Furthermore, even if we know the system is $k$-contracting, the specific value of $k$ is often unknown and would require a hyperparameter search, which is not ideal.
4. The performed experiments seem to be very small scale (with less than 100 parameters). This raises a scalability concern whether the network can perform well with larger parameter counts. I understand that not all research group has large-scale computing capability. However, training with ~10k parameters or above should be done relatively quickly with a GPU.
5. Lack of comparisons with well-established time-series datasets and with well-established architectures. The premise of Lurie network is the generalization of other time-series architectures such as LSSM, Antisymmetric RNN, etc. However, the presented experiments did not compare the performance of Lurie network with those architectures (except Lipschitz RNN) and with the datasets where those architectures were tested on.

My minor concerns are:
1. The notation $1e-5$ is not a scientific notation (although it's used a lot in code), instead please use $1\times 10^{-5}$

I'm happy to increase my score if my major concerns are addressed.

### Questions
1. How was the roll-out during the training done? I'm assuming it's using some ODE solver, but the details of ODE solver used is not present in the paper.
2. The values in Table 1 is unclear. In each cell, there are 2 rows. I assume the first row represents the mean and std of the MSE loss on test set, but the values on the 2nd row of each cell has unclear meaning. What are those?
3. Related to weakness #3 above, is there a way for Lurie networks to remove the need for prior knowledge of the values of $k$?

### Soundness
3

### Presentation
2

### Contribution
2
