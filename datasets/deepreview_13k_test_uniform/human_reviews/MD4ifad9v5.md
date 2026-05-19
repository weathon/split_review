# Adaptive higher order reversible integrators for memory efficient deep learning

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
The depth of networks plays a crucial role in the effectiveness of deep learning. However, the memory requirement for backpropagation scales linearly with the number of layers, which leads to memory bottlenecks during training. Moreover, deep networks are often unable to handle time-series data appearing at irregular intervals. These issues can be resolved by considering continuous-depth networks based on the neural ODE framework in combination with reversible integration methods that allow for variable time-steps. Reversibility of the method ensures that the memory requirement for training is independent of network depth, while variable time-steps are required for assimilating time-series data on irregular intervals. However, at present, there are no known higher-order reversible methods with this property. High-order methods are especially important when a high level of accuracy in learning is required or when small time-steps are necessary due to large errors in time integration of neural ODEs, for instance in context of complex dynamical systems such as Kepler systems and molecular dynamics. The requirement of small time-steps when using a low-order method can significantly increase the computational cost of training as well as inference. In this work, we present an approach for constructing high-order reversible methods that allow adaptive time-stepping. Our numerical tests show the advantages in computational speed when applied to the task of learning dynamical systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper uses time-reversible ODE integration to solve neural ODEs. It focuses on a specific class of higher-order reversible integrators, and uses the time reversibility property to avoid inconsistency between the system states $z$ on the forward vs. backward passes. This allows a backward propagation of gradient information with memory costs independent of the sequence length.

The authors demonstrate this strategy for tuning parameters of dynamical systems or learning ODE terms parametrized by neural networks.

### Strengths
The idea of using higher-order reversible integrators to solve ODEs is inherently appealing, as the potential to reduce memory costs and improve accuracy is good. The ideas are mostly clearly explained, and the examples, if somewhat simplistic, are at least relevant to the stated goals.

### Weaknesses
Overall the paper doesn't provide significant theoretical results, and the experimental results are fairly weak (details below):

Literature review and citations are inadequate. There is a considerable and active literature on learning dynamical systems with ML, but this hasn't really been acknowledged. As a start, foundational papers such as Chen (2018) and Rackauckas (2020) should be cited, and many of the references in Ghadami (2022) will be relevant. There is also a considerable literature on physics-constrained (e.g. McGreivy 2023) and Hamiltonian neural networks (Greydanus 2019 and later articles) that has not been adequately cited. The first paragraph of the introduction makes fairly broad claims ("learning models of dynamical systems") with loose terminology ("numerical methods") but the cited references are all highly specific, a broad overview of the field should be given with major relevant works cited.

The assessments of improvements to speed/accuracy tradeoffs arising from the proposed approached are quite weak:
* In both tables 2 and 3 we never compare to alternative methods or even weak baselines such as a non-reversible integrator with adaptive step size (e.g. Forward Euler or RK4), but rather only between low- and high-order version of reversible integrators. We are missing a clear picture of how the proposed technique improves on alternative methods. It can' simply be that higher-order integrators are more efficient on these particular problems, that's simply not of sufficient general interest
* For parameter estimation tasks, we should consider accuracy with regard to the reference (ground truth) parameters, or prediction errors on held-out initial conditions. The training loss doesn't necessarily indicate which method is actually better in these senses.
* A fixed step size was used in table 2, providing an unrealistic picture of how this would be used and losing sight of the fundamental reasoning behind the technique
* Fig. 2 seems to exaggerate the benefits of Y4 over ALF, since in a realistic scenario the step size would be automatically set by each method. The loss landscape should (also) be shown for adaptive step sizes scenario, and for the same 10^-8 accuracy tolerance as used for computing table 1.
* The problems are fairly easy. The system state was fairly low dimensional in all examples. The only example where a neural network was trained involved learning a low-dimensional potential with strong inductive biases from physics. There are many examples of challenging dynamical system learning tasks in the literature, including some benchmark studies. Ideally we should see an improvement of cost-accuracy tradeoffs on some established task.

One of the advantages of backward mode differentiation over forward mode is that we don't need to compute input-output gradients $d\phi_{j+1}/d\phi_j$ which are of size $n^2$. But here we do, at least in the current formulation, calculate and store the matrix explicitly. Is this strictly necessary, or is there some way around it? What happens when $d\phi_{j+1}/d\phi_j$ is sparse, for example when representing local interactions in a discretized PDE? The authors claim that their time integrators could work for "potentially very high-dimensional $z$" (line 173) but this doesn't seem to scale.

Checkpointing for gradient calculation should be mentioned as an alternative to the present approach for reducing memory costs, and the relative merits of each should be discussed.

For the proposed tasks and dataset sizes, many other approaches are possible. Examples include simulation-based inference (Cranmer 2020) that treats the forward process as a black box, or simply training an attention-based or recurrent network to impute missing in continuous time. These should at least be discussed, with references.

The notation in 2.1 is fairly confused. $\sigma$ is supposed to be an activation function but then turns out to have learnable parameters. The role of $h$ in eq. 3 isn't clearly stated. $F$ seems to be used once for $f$, and $T$ is used without definition. At the same time, there is probably too much detail here, as we don't really need an explanation of backprop.

The manuscript could benefit from some careful proofreading, e.g. for grammatical errors (line 369: "have a special structure").

References:

Chen RT, Rubanova Y, Bettencourt J, Duvenaud DK. Neural ordinary differential equations. Advances in neural information processing systems. 2018;31.

Rackauckas C, Ma Y, Martensen J, Warner C, Zubov K, Supekar R, Skinner D, Ramadhan A, Edelman A. Universal differential equations for scientific machine learning. arXiv preprint arXiv:2001.04385. 2020 Jan 13.

Ghadami A, Epureanu BI. Data-driven prediction in dynamical systems: recent developments. Philosophical Transactions of the Royal Society A. 2022 Aug 8;380(2229):20210213.

Greydanus S, Dzamba M, Yosinski J. Hamiltonian neural networks. Advances in neural information processing systems. 2019;32.

McGreivy N, Hakim A. Invariant preservation in machine learned PDE solvers via error correction. arXiv preprint arXiv:2303.16110. 2023 Mar 28.

Cranmer K, Brehmer J, Louppe G. The frontier of simulation-based inference. Proceedings of the National Academy of Sciences. 2020 Dec 1;117(48):30055-62.

### Questions
Are step sizes treated as fixed on the backward pass, or do we somehow take gradients w.r.t step size calculations? If the former, how large are the resulting errors compared to the errors in backward propagated states as computed with a non-time-reversible integrator of the same order?

Line 505: "The potential is obtained by integrating the neural network numerically" -- please explain.

The description of Heun's method (line 213) is both very terse (what is it?) and very detailed (initilaization values etc.)

### Soundness
2

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
"Improving neural network architectures inspired by ODEs" and "using neural networks to learn ODEs" have been investigated alternately. This paper proposes a novel architecture based on a composition method, which improves model design and achieves memory efficiency during training thanks to its reversibility.

### Strengths
The focus of the study is reasonable, with a thorough survey of related works and sound theoretical foundations. If this paper were a contribution to applied mathematics, it would deserve high praise.

### Weaknesses
However, the validation falls short. The experiments are limited to simple datasets, which are insufficient to demonstrate the general applicability of the proposed architecture. In what settings is this architecture genuinely effective? For instance, while reversible dynamical systems, like the Kepler problem used in the study, are a clear application, this alone is somewhat narrow, as one could achieve similar outcomes by applying reversible integrators within Neural ODE frameworks. On the other hand, could applying this architecture to general tasks, like image processing, compromise performance due to the reversibility constraint? The study would benefit from a clarified scope of applicability and a more comprehensive set of experiments.

While the theoretical memory efficiency is convincing, there is no experimental validation. Although ALF is presumably the baseline, only computation time is compared. An experimental comparison of memory consumption is also necessary, along with theoretical orders for computational and memory costs.

Considering ICLR's focus on machine learning, this paper falls short of expected standards due to the ambiguity of its contributions and insufficient empirical support.

### Questions
See weakness.

Minor comments:
- References are cited without parentheses, which hinders readability. Proper citation using \citep tags with parentheses is recommended.
- The composition method could construct more complex architectures, and such an exploration could add value to the study.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In summary, the paper presents a novel approach to construct higher-order reversible integrators for memory-efficient deep learning, with the main contribution being the development of higher-order reversible integrators based on the asynchronous leapfrog (ALF) method. The proposed methods demonstrate improvements in training speed and accuracy, particularly in learning dynamical systems. It opens up new avenues for training neural ODEs with restricted memory budgets.

### Strengths
- I find the idea novel and original. The paper extends the capabilities of existing reversible integrators like ALF and reversible Heun, which were previously limited to low orders of accuracy. By demonstrating the feasibility of higher-order reversible integrators, the authors open new possibilities for improving the efficiency and accuracy of neural ODE-based deep learning.

- The paper is presented with exceptional clarity, guiding readers seamlessly through key concepts. It begins with a thorough setup of neural ODEs, followed by a well-balanced discussion of the advantages and limitations of two gradient computation methods, effectively motivating the notion of reversibility. The structured flow continues with an in-depth explanation of numerical methods, culminating in the core contribution: the construction of higher-order methods using ALF or Heun’s method. The integration of these methods within the neural ODE training framework (i.e. leveraging state-adjoint equations), is explained with precision, enhancing comprehension and practical relevance.

- The significance of this work is moderate. While it can be seen as a direct follow-up to the contributions of Zhuang et al. (2021) and Kidger et al. (2021), it still brings meaningful value, particularly in the context of neural network training for dynamical systems with multiple time scales.

### Weaknesses
- My primary concern lies with the soundness of the conclusion. Indeed, we see smaller errors and computation time of adaptive Y4 when comparing with adaptive ALF in both Kepler and nonlinear harmonic oscillator under some settings. It's not clear to me:
   -  Where the savings of the computation time come from? Is it because adaptive Y^4 in general uses larger step sizes? Is there a limit on $k$ for adaptive $Y^{2k}$ to outperform adaptive ALF on computation time? Why or why not there is a limit? I would suggest the authors to add more comparisons by varying parameter $k$ and report the results.
   -  Why the final loss of Y4 is lower? (When solving differential equations, it's easier to understand that higher order methods often outperform lower order methods w/ the same step size. However, when training neural networks, it's less obvious - the training is more or less "agnostic" to the computation schemes you are incorporating ... eg. why Runge Kutta is better than Euler?) What if we increase the number of epochs? Will it help adaptive ALF to achieve lower loss? Could the authors provide some justifications and experimental data to support them?

- The author may consider adding more contexts for the "adaptive stepping" presented in Hairer et al. (2006) in the Background section.

- The authors may consider adding a broader set of literatures for the readers. For examples,
  - known reversible methods other than asynchronous leapfrog and Heun:
     - Loup Verlet. Computer” experiments” on classical fluids. i. Thermodynamical properties of Lennard-Jones molecules. Physical review, 159(1):98, 1967.
  - for composition of mixed-order methods, although it is less developed than the theory for composing same-order integrators, there are some frameworks addressing this topic, especially in contexts like symplectic integrators and splitting methods
     - "Splitting methods for differential equations" by Sergio Blanes, Fernando Casas, Ander Murua
     - “Geometric Numerical Integration” by Hairer, Lubich, and Wanner
  - some other works on deep learning of dynamical systems
     - Rudy SH, Kutz JN, Brunton SL. 2019 Deep learning of dynamics and signal-noise decomposition with time-stepping constraints. J. Comput. Phys. 396, 483–506. (doi:10.1016/j.jcp.2019.06.056)
     - Y. Liu, J. N. Kutz, and S. L. Brunton, “Hierarchical deep learning of multiscale diﬀerential equation time-steppers,” arXiv:2008.09768
(2019)
     - Raissi M, Perdikaris P, Karniadakis GE. 2018 Multistep neural networks for data-driven discovery of nonlinear dynamical systems. Preprint. (https://arxiv.org/abs/1801.01236)

### Questions
I don't quite understand the purpose of section 4.2. "LEARNING OF DYNAMICAL SYSTEMS PARAMETERIZED BY NEURAL NETWORK". Could the authors comment on the novel insights or advantages gained from this section compared to 4.1, or to clarify how this section extends or complements the results from 4.1?

### Soundness
2

### Presentation
4

### Contribution
3
