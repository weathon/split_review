# Physics-informed GNN for non-linear constrained optimization: PINCO, a solver for the AC-optimal power flow

- Decision: Reject
- Avg Score: 2.60
- Scores: 3, 5, 1, 3, 1

## Abstract
The energy transition is driving the integration of large shares of intermittent power sources in the electric power grid. Therefore, addressing the AC optimal power flow (AC-OPF) effectively becomes increasingly essential.
The AC-OPF, which is a fundamental optimization problem in power systems, must be solved more frequently to ensure the safe and cost-effective operation of power systems. Due to its non-linear nature, AC-OPF is often solved in its linearized form, despite inherent inaccuracies. Non-linear solvers, such as the interior point method, are typically employed to solve the full OPF problem. However, these iterative methods may not converge for large systems and do not guarantee global optimality. This work explores a physics-informed graph neural network, PINCO, to solve the AC-OPF. We demonstrate that this method provides accurate solutions in a fraction of the computational time when compared to the established non-linear programming solvers. Remarkably, PINCO generalizes effectively across a diverse set of loading conditions in the power system. We show that our method can solve the AC-OPF without violating inequality constraints. Furthermore, it can function both as a solver and as a hybrid universal function approximator. Moreover, the approach can be easily adapted to different power systems with minimal adjustments to the hyperparameters, including systems with multiple generators at each bus. Overall, this work demonstrates an advancement in the field of power system optimization to tackle the challenges of the energy transition. The code and data utilized in this paper are available at \url{https://anonymous.4open.science/r/opf_pinn_iclr-B83E/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a GNN-based approach to address the ACOPF problem, with the primary aim of reducing the computation time required by traditional interior-point solvers to enable faster ACOPF solutions. It leverages a physics-informed loss function incorporating penalties for both equality and inequality constraints. The grid model is represented as a graph, having real and reactive power demand, along with node type as inputs. Experimental results are provided, comparing the proposed approach with the MIPS solver across both single and multiple load scenarios.

### Strengths
-- Attempting to solve a very relevant problem in the form of ACOPF.
-- Idea of using PINNs and GNN together is a strength.

### Weaknesses
— The authors’ claim of being the first to use a PINN for solving the ACOPF problem must be clarified against the various existing works [1]-[2]. There are several works already using PINNs, in both supervised and unsupervised learning settings. There exists a substantial body of work under end-to-end learning that relates to this area, for example: [1]-[2].

— The issue mentioned above seems to stem from an incomplete literature review. For example, [1] presents a survey on end-to-end learning methods for constrained optimization, the general class of optimization problems to which ACOPF belongs. Many works listed there use PINNs in either supervised or unsupervised fashions. Additionally, several key references such as [2]-[4] are not discussed in the paper. Furthermore, the use of GNNs for the ACOPF problem is also not a unique contribution, as noted by the authors themselves. Authors should clearly discuss the limitations of these works and highlight how their work differs from them and provide advantages. 

— Experimental studies: The results presented are limited in terms of the number of experiments and comparative analysis. No comparisons are made to existing ML methods.   Authors must compare the results with various ML methods. For example, the cost difference with the proposed method is significantly higher than that achieved by various ML methods for ACOPF.

— If the model is completely unsupervised, why are only 500 demand samples used?

— What are the specifications of the computing hardware cluster (ETH Euler Clusters), and how long are the models trained?

— How does the model shown in Figure 1 differ from existing PINN models? If it does not differ, appropriate citations should be provided.

— In the abstract, the authors highlight the limitation of interior-point methods in achieving global optimality. While this is correct due to the NP-hard nature of ACOPF, how does the current method address this limitation?

--The authors mention that the MIPS equality loss reaches up to 20 MW in case of 118-Bus system Table 2. What does this imply?  Does it mean that MIPS is unable to find a feasible solution? In general, interior point methods yield feasible but potentially suboptimal solutions. Authors should clarify and explain the reasons behind high loss via MIPS, and under what conditions MIPS is failing to converge to any feasible solution.

### Questions
— If the model is completely unsupervised, why are only 500 demand samples used?

— What are the specifications of the computing hardware cluster (ETH Euler Clusters), and how long are the models trained?

— How does the model shown in Figure 1 differ from existing PINN models? If it does not differ, appropriate citations should be provided.

— In the abstract, the authors highlight the limitation of interior-point methods in achieving global optimality. While this is correct due to the NP-hard nature of ACOPF, how does the current method address this limitation?

--The authors mention that the MIPS equality loss reaches up to 20 MW in case of 118-Bus system Table 2. What does this imply?  Does it mean that MIPS is unable to find a feasible solution? In general, interior point methods yield feasible but potentially suboptimal solutions. Authors should clarify and explain the reasons behind high loss via MIPS, and under what conditions MIPS is failing to converge to any feasible solution.

### Soundness
1

### Presentation
1

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
- This paper introduces PINCO, a physics-informed graph neural network (GNN) designed to approximate solutions for the frequently employed Alternating Current Optimal Power Flow (AC-OPF) problem in power transmission networks. By leveraging existing independent tools like physics-informed NNs and GNNs, PINCO distinguishes itself from prior approaches by better adhering to the inequality constraints of the AC-OPF problem, thereby enhancing solution feasibility in a data-driven framework.

### Strengths
- The paper is clear in its exposition and is well-structured that makes the contributions and methodology easy to follow.
- Prior work is clearly acknowledged, and the authors effectively situate their approach within the existing body of research
- The authors make effective use of established methodologies to tackle the AC-OPF problem through an unsupervised learning approach with a focus on ensuring feasible AC-OPF solutions
- Experimental results do highlight feasible AC-OPF solutions quantified via the Equality Loss at the expense of slightly higher cost difference (which is inevitable given the data-driven model).
- The authors also showcase the additional benefits such as faster inference times

### Weaknesses
 - *Novelty*: The novelty of this approach appears limited, as it primarily relies on well-established tools like GNNs and PINNs. The work could further benefit from clearer differentiation that goes beyond simply combining existing frameworks. For e.g., did the authors explore architectural modifications to the GNN tailored to the characteristics of power transmission networks, or a customized optimization technique designed for AC-OPF? This could significantly enhance the paper’s originality within the ML domain.

- *Scope*: The current approach also presents practical concerns in real-world applications. In practice, power system operators frequently adjust network topology due to maintenance, unplanned outages, and other operational needs, leading to variations in the grid adjacency matrix for a *given* power system test case. Based on the paper’s description, the proposed model would need re-training from scratch for each such new grid adjacency matrix, which presents a notable limitation. Did the authors explore methods to make their model more adaptable to changing topologies for a given test case (even if the cost of the OPF solution is relatively high)? Developing a more flexible framework that can accommodate such variations within a single model would make the approach far more practical than showcasing the performance results across multiple IEEE benchmark systems.

### Questions
- Could the authors elaborate on the ML-specific challenges encountered when modeling more than one generator per electrical bus? Is there a fundamental challenge that has prevented past approaches from addressing such cases, or is this simply a modeling choice that the authors address by introducing artificial nodes?

- When solving the IEEE 118-bus problem, any node can be designated as the reference node by including the reference bus angle as an equality constraint in the OPF optimization problem. Could the authors clarify why phase angle comparisons are not included in their evaluation?

- The comparisons in Figure 3 could benefit from additional context. While the differences between the MIPS solver and the proposed solution are shown, it’s not immediately clear how these absolute differences inform the effectiveness of the model, given that the OPF objective is primarily centered on minimizing generator operating costs. Could the authors clarify the purpose of Figure 3 and what specific insights they intended to convey through these comparisons?

- To enhance interpretability, it might be useful to include visualizations that track the evolution of equality loss and relative cost differences throughout training. This could provide more relevant insights into how well the model aligns with the OPF objective over time.

- As noted in the weaknesses, the current formulation focuses on a *single* fixed network topology for each power system case. However, in real-world applications, system operators often encounter dynamic topologies due to changes in operational conditions. Formulating the OPF learning problem to accommodate time-varying grid topologies is more relevant and such a formulation would also give rise to ML modeling challenges that could inspire innovative techniques tailored to real-world needs, potentially making a stronger contribution to both the ML and power systems communities.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper considers a physics-informed graph neural network, PINCO, to solve the AC-OPF problem. Using standard test cases, it shows that proposed method is faster than standard nonlinear solvers. Some generalization properties are discussed.

### Strengths
- ACOPF is an important problem in grid operations. 
- The paper is easy to read, and the results seem correct.

### Weaknesses
 - In my opinion the main weakness of the paper is that the result isn't that good. In the sense that the main goal of the paper is to find feasible solutions, and I don't think that goal is accomplished.
- In Figure 3, the violations of $P, \theta, Q,$ and $V$ are shown. But the violations can be pretty large, especially for $Q$ and $V$. One of the reasons ACOPF is ran is to handle the V/Q constraints, and having a 10% error is not great. 
- Table 2 reports the "equality constraint" violations when the input load scenarios changes. But this violation can be 16 MW, which is again not a small number. I don't think operators would be likely to accept these types of violations. Although the nonlinear solver can be slow, but the problem can be resolved when the load changes. 
- The approaches in the paper is based on generic methods, and can be applied to any constrained optimization problem. It would be good to see if there is anything special about the ACOPF when applying the method.

### Questions
There has been a lot of work on ACOPF (some are cited in the paper). The authors should compare against some of these, in addition to standard solvers. 
What happens when the problem is infeasible? Presumably the neural network would still output something, but would one be able to tell that there is actually no solution?

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
This paper presents PINCO, a neural architecture for solving the AC-OPF problem. PINCO is a combination of GNN + PINNs with hard constraints. Numerical tests show the usefulness of the proposed model.

### Strengths
+ A new model combining the GNNs and PINNs for solving AC-OPF
+ Promising numerical performance relative to MIPS solver

### Weaknesses
 - Both GNNs and PINNs have been used for solving AC-OPF, and the paper directly combines the two without much novel design in the architecture.
- Insufficient comparison against other numerical solvers for AC-OPF of distribution systems including e.g., using GNNs, PINNs, SDP relaxation and SOCP relaxation, and linear-OPF initialized Newton-Raphson method in terms of performance.

### Questions
Q1. Any specific design in the GNN+PINN architecture?
Q2. Solvers using GNNs or PINNs shall be included as baselines to show the usefulness of having both in a single architecture.
Q3. It is not clear why the proposed PINCO would improve upon the PINNs with hard constraints approach? This shall be clarified as well as evidenced using numerical comparison against a number of benchmark test systems.
Q4. Physics-informed GNN based power system state estimation (PSSE) was among the first use of NN architecure for power systems and they shall be discussed as a motivation of using deep learning for power systems.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper presents a graph neural network architecture for solving AC Optimal Power Flow models.
The paper describes a physics-informed loss for training the model in a self-supervised manner, and conducts numerical experiments on systems with up to 118 buses.

### Strengths
The proposed methodologies has two positive aspects
* it uses a graph-based architecture, which supports changes in grid topology (however this capability was not demonstrated)
* it uses a self-supervised training scheme that does not require the (expensive) use of an optimization solver to generate data

However, neither of these are new, and the paper suffers from multiple limitations (see below).

### Weaknesses
Limitations of the methodologies / experiments:

* The paper incorrectly states that previous works do not handle multiple generators per bus.
  * _Confidence-Aware Graph Neural Networks for Learning Reliability Assessment Commitments_ (https://doi.org/10.1109/TPWRS.2023.3298735) consider graph neural network architectures for unit-commitment problems, and present an encoder-based mechanism for handling multiple generators per bus
  * _CANOS: A Fast and Scalable Neural AC-OPF Solver Robust To N-1 Perturbations_ (https://arxiv.org/abs/2403.17660) does support such features:
    _We also use artificial edges to connect the subnodes to their respective bus (these do not model any physical equipment)._
  * It should be noted that handling multiple generators at a single bus is not a hard task, as they can easily be aggregated into a single generator; an aggregated solution can then be disaggregated in closed-form.

* I believe the augmented Lagrangian in Eq. (5) is incorrect, specifically the term $\mu_{k} g_{j}(w_{u}^{k})^2$.
  Assuming inequality constraints are of the form $g(w) \leq 0$, this quadratic term effectively drives all inequality constraints towards being binding (i.e. $g(w) = 0$), which is not theoretically sound. For example, consider the simple problem $\min_{x} x$ subject to $x \leq 0$. The augmented Lagrangian would be $L(x, \lambda, \mu) = x + \lambda \max(0, x) + \mu x^2$. This formulation will always have a finite solution, even though the original problem is unbounded. This is because the quadratic penalty term forces the solution towards $x=0$, regardless of the objective function.

* The paper argues that the use of a graph neural network supports changes in the grid topology, but does not present experiments that corroborate this claim

* The paper claims that the proposed model can achieve "zero violation of inequality constraints." This is not a substantial achievement, given that said inequality constraints are either simple variable bounds (which can be enforced via a bounded activation function) or simple l2 norm constraint (which can also be enforced by a simple scheme). The complexity of AC-OPF is in satisfying _both_ equality and inequality constraints. It is straightforward to enforced either set of constraints separately (i.e. only equality or only inequality constraints).

* Numerical experiments consider AC-OPF instances on systems with up to 118 buses. This is 100x smaller than real-life instances, which comprise (at least) in the order of 10,000 buses.

  It should be noted that several works have trained ML models to predict AC-OPF with systems of that scale:
  * _Spatial Network Decomposition for Fast and Scalable AC-OPF Learning_ (https://doi.org/10.1109/TPWRS.2021.3124726)
  * _Compact optimization learning for AC Optimal Power Flow_ (https://arxiv.org/abs/2301.08840): up to 30,000 buses
  * _CANOS: A Fast and Scalable Neural AC-OPF Solver Robust To N-1 Perturbations_ (https://arxiv.org/abs/2403.17660): up to 10,000 buses, and also uses graph neural network architectures

* Training times appear to be very large (10 to 24 hours as reported in Section 5). Given that the paper only considers very small artificial systems, it is not clear that the proposed scheme would scale to real-life systems. A reasonable target would be at most 6-8hrs of training time on a systems with about 10,000 buses.

* Numerical experiments do not compare against any existing ML methodology for AC-OPF problems.

Issues about the paper:
* Not all notations are properly defined. For instance, the formalism of equality and inequality constraints is not defined before the Augmented Lagrangian presented in Eq. (5). Similarly, this equation uses a parameter $w^{k}_{u}$ that is not defined.
* the paper does not present the data distribution used to train the model. It should be noted that generating data by perturbing individual loads independently is not realistic, as it leads to a very narrow variability in total demand.

  Note that there are open-source datasets and data generators for AC-OPF problems, e.g.:
  * OPFData (https://arxiv.org/html/2406.07234v1) is an open-source dataset of AC-OPF instances and their solutions
  * OPFGenerator (https://github.com/AI4OPT/OPFGenerator) is an open-source instance generator for various OPF formulations

* In addition to the comments, above, the paper sometimes makes misleading claims. For instance, at lines 88-89, it is stated that "INCO allows for solving the AC-OPF **without violations**." This claim is not substantiated by the results reported in Section 4 (Tables 1 and 2).

### Questions
In the absence of a fundamentally new architecture or training scheme, to be accepted, this paper should:
* conduct numerical experiments on systems with at least 10,000 buses...
* ... with a more realistic data distribution than independently perturbing individual loads;
* demonstrate the proposed architecture's ability to handle varying topologies;
* achieve training times of at most 8hrs (this is the kind of timeline that would be needed for practical applications);
* achieve low constraint violation (in the order of $10^{-4}$ relative violation) and optimality gap (no more than $0.1$% worse than Ipopt);

It should be noted that each of the above bullet has been addressed in the literature, at least individually.
For instance, there exist works that scale to 10,000-bus systems, works that consider more realistic data distributions, works that achieve low constraint violations, etc...

### Soundness
2

### Presentation
1

### Contribution
1
