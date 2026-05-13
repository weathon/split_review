# Learning to Solve Bilevel Programs with Binary Tender

- Decision: Accept
- Scores: 6, 6, 3

## Abstract
Bilevel programs (BPs) find a wide range of applications in fields such as energy, transportation, and machine learning.
        As compared to BPs with continuous (linear/convex) optimization problems in both levels, the BPs with discrete decision variables have received much less attention, largely due to the ensuing computational intractability and the incapability of gradient-based algorithms for handling discrete optimization formulations.
        In this paper, we develop deep learning techniques to address this challenge.
        Specifically, we consider a BP with binary tender, wherein the upper and lower levels are linked via binary variables.
        We train a neural network to approximate the optimal value of the lower-level problem, as a function of the binary tender.
        Then, we obtain a single-level reformulation of the BP through a mixed-integer representation of the value function.
        Furthermore, we conduct a comparative analysis between two types of neural networks: general neural networks and the novel input supermodular neural networks, studying their representational capacities.
        To solve high-dimensional BPs, we introduce an enhanced sampling method to generate higher-quality samples and implement an iterative process to refine solutions.
        We demonstrate the performance of these approaches through extensive numerical experiments, whose lower-level problems are linear and mixed-integer programs, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper employs neural networks to help solve the bilevel programs with binary tenders. Specifically, they adopt neural networks to approximate the optimal value of the lower-level problem as a function of the binary tenders. In order to train the neural networks, the authors also introduce an enhanced sampling method to generate high-quality samples. Lastly, numerical experiments were conducted to demonstrate the performance of these approaches.

### Strengths
This paper gives a good attempt of incorporating ML (especially neural networks) methods to facilitate the solution of traditional mathematical optimization problems, which in my opinion is an area that deserves more attention from the community. Overall, this paper is clearly written, easy to understand, and the theoretical results in Section 3 are very neat. I also find it to be very impressive that I cannot find any typo throughout this paper and the propositions also appear to be of their own independent interest.

### Weaknesses
Main concern:
1. The lack of ablation study, especially on the enhanced sampling part. For instance, why do you want to solve the quadratic programming problem (5) to get the samples? I understand that matrix Q is selected to be PSD is for the polynomial-solvability, but what is the main reason of solving the quadratic program in the first place? If we replaced this enhanced sampling with some other more naive sampling methods, how would it affect the experiment results? The justification for using a quadratic program to generate samples is not sufficiently clear. While the authors mention that the PSD property ensures polynomial solvability, the core motivation for using a quadratic objective over, say, a linear one, remains vague. It's not evident why a quadratic program is necessary to obtain feasible points in the interior of the feasible region, especially given that the feasible region itself is not limited to a finite set of points. A more thorough explanation of why this specific approach was chosen over simpler alternatives is needed.
2. Limitation of the experiment setup and analysis: 
   (a) Instance dimension up to 60 is too small.
   (b) The selection of the lower level problem is LP and MILP, which both have linear lower level objective function. At least you could have tried some simple nonlinear functions like quadratic function.
   (c) The experimental results do not support the conclusion well. I list some of the points in the next Questions section.

### Questions
Major questions:
1. In Figure 5 and Figure 6, the computational time of MiBS increases very fast with the increase of n. My question is, even though the MiBS solver might take a long time to reach optimality, have you considered to set a time limit, and compare the relative error of the best found solution given by the solver at time limit with your approaches?
2. In your Conclusion section you mentioned: "we demonstrated that the enhanced sampling helps reduce average relative error". However, the whole point of your sampling method is simply to get enough data points for training the neural network. In order to claim that your proposed enhanced sampling can bring some extra benefits, you need to at least compare with other non-trivial sampling methods.
3. In Conclusion section: "The computational time of using ...... is significantly shorter than that of MiBS ......" I admit that this is true, but your methods also do not reach optimality, for fair comparison you either need to have enough samples for exactly learning the value function (so that your approach can also produce a true optimal solution), or you need to compare the best feasible solution found by MiBS within a given time limit. 

Minor question:
1. I suggest to give an exact definition for "binary tender". As far as I know, I do not think this is a well-known term in the community.
2. Still about the definition of "binary tender". On Page 2 "we assume that the entries of x appearing in the lower-level formulation are binary-valued". However, in Appendix C, about the instance generation for the experiments, I notice that the binary constraint on x is enforced in the upper-level instead of the lower-level formulation.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the Bilevel programs (BPs)  with discrete decision variables. A neural network is trained to approximate the optimal value of the lower-level problem, as a function of the binary tender. Then a single-level reformulation of the BP through a mixed-integer representation of the value function can be obtained. Moreover, an enhanced sampling method is proposed for high-dimensional BPs.

### Strengths
1. This work proposes an approximation-based method for Bilevel programs (BPs)  with discrete decision variables, which is interesting.

2. an input supermodular neural network (ISNN) is proposed, which ensures a supermodular mapping from input to output.

3. an enhanced sampling method is proposed for solving high-dimensional BPs.

### Weaknesses
1. The author should conduct some complexity analysis, such as time complexity [1], to show the effectiveness of the proposed method. Specifically, a detailed analysis of how the runtime scales with the size of the input (number of binary variables) and the depth/width of the neural network would be beneficial. It is not clear if the proposed method offers any computational advantage over existing methods, especially for large-scale problems.

2. This work employs neural networks to learn and approximate the value function $\phi(x)$. However, training the neural networks is more computationally complex than directly approximating the lower-level optimization problem [2]. What is the advantage of the proposed method over the polyhedral approximation in [2]? The authors should elaborate on the specific scenarios where the neural network approach is expected to outperform polyhedral approximations, considering factors like problem structure, dimensionality, and desired solution accuracy. A discussion on the potential for overfitting with neural networks, and how this is addressed, would also be valuable.

3. Since one of the key contributions in this work is to employ neural networks to learn and approximate the value function $\phi(x)$, I suggest the authors clearly discuss the existing approximation-based methods (i.e., which approximate the lower-level optimization problems and reformulate the bilevel optimization problems as single-level optimization problems, for instance, polyhedral approximation) in bilevel optimization since I can't find any discussion about the approximation-based methods in bilevel optimization. The current discussion lacks a comprehensive overview of the landscape of approximation techniques for bilevel optimization, making it difficult to assess the novelty and contribution of the proposed method. A more thorough literature review is needed to position this work within the existing body of research.

4. Training the neural networks to approximate the value function $\phi(x)$ may introduce some variance which will lead to the solution of the resulting single-level problem far away from the original bilevel optimization problems. Can you provide a more theoretical guarantee for the proposed method? Specifically, it is unclear how the approximation error of the neural network impacts the optimality of the solution to the bilevel problem. A rigorous analysis of the error propagation from the neural network approximation to the final solution is needed, including bounds on the suboptimality of the obtained solution.

### Questions
I have some questions about the complexity, the comparison with the existing approximation-based methods in bilevel optimization, and the theoretical guarantee of the proposed method. Please see the Weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors explore the use of machine learning techniques to solve complex bilevel programs with binary variables. They introduce a sampling algorithm for obtaining high-quality sample data for train neural networks. Two neural networks ( general neural networks (GNN) and input supermodular neural network  (ISNN) are proposed to estimate the lower-level value function based on upper-level decisions. These estimates are used to enhance the optimization process by adding optimality cuts to a single-level problem.

### Strengths
- The authors propose a machine learning-based algorithm for solving bilevel programs with binary variables in the outer level problem. 

- The authors are able to provide some theoretical analysis for proposed neural networks with binary inputs. 

- The paper is easy to follow.

### Weaknesses
1) The numerical experiments lack sufficient evidence to demonstrate the advantages of the proposed algorithm. It appears that the algorithm can only achieve optimality for test instances with n = 10. The authors solely conduct comparisons with the baseline method MiBS based on computational times, without assessing solution quality, such as the optimality gap. The lack of optimality gap reporting makes it difficult to assess the practical performance of the proposed method, especially for larger instances where finding the true optimum is computationally challenging. The comparison should include a measure of how close the solutions are to the optimal values, not just the computation time.

2) The test instances are only from the authors’ synthetic generated ones. Some public datasets like MIBLP-XU and IBLP-FIS in Tahernejad et al., 2020 should be used. The absence of experiments on established benchmark datasets limits the generalizability of the findings. Using only synthetic data makes it hard to know how the method would perform in real-world scenarios.

3) This method should only be suitable when functions $f$ and $g$ are linear or MILP-representable because one needs to solve Eq (5) and (12) to optimality. The requirement to solve these problems to optimality is a significant limitation, as it restricts the applicability of the method to problems where these subproblems can be efficiently solved. This assumption is not clearly stated and limits the scope of the proposed approach.

4) The cost to solve a single instance of Problem (5) is very expensive because it is at least as hard as a mixed-integer quadratic program (MIQP). The computational burden of solving the MIQP in (5) is a major bottleneck, especially during the sampling phase. The authors should provide a more detailed analysis of the computational complexity of solving (5) and discuss how this impacts the overall scalability of the algorithm.

### Questions
1) What is the stopping criterion for Algorithm 2 so that the generated point $(x,y)$ is guaranteed to be feasible to Problem 1? That is, $x,y$ is satisfied $x \in X(y), y \in Y(x), g(y,x) \ge \max_{z \in Y(x)}  g(z,x)$ 

2) What is the definition of ``relative error” in Figures 4 and 7? How do you define an error when an optimal solution cannot be found, for example, for large-scale problems with n = 60?

3) Why relative errors can be negative (as in Fig. 7)?

4) Why we need to care of supermodularity of an ISNN? I notice that ISNN requires more neurons compared to GNN (i.e., the lower bound value for $N_{nr}$ in Eq. (8) vs Eq. (7))

5) Do we have to solve $\max_{y \in Y(\hat{x})} g(y, \hat{x})$ to optimality in Algorithm 1?

6) For feasibility purpose, why do we need the second term $h^T x$ in Eq. (5)?

7) I don’t fully understand the notation ``GNN representability” in Prop 1 (ii). This statement “we measure the GNN representability by the number of parameters it trains” seems to be not mathematically sound. 

8) The architecture details of GNN of ISNN should be reported.

9) The name of section 3.3 seems to be incomplete. 

10) I don’t see any part of Figures to support the claims “achieving relative error less than 5%,”, “the relative error of instances with n = 30, 50, 60 is larger than 15%.”

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
