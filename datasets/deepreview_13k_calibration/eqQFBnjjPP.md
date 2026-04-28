# ExDBN: Exact learning of Dynamic Bayesian Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Causal learning from data has received much attention in recent years. One way of capturing causal relationships is by utilizing Bayesian networks. There, one recovers a weighted directed acyclic graph, in which random variables are represented by vertices, and the weights associated with each edge represent the strengths of the causal relationships between them. This concept is extended to capture dynamic effects by introducing a dependency on past data,  which may be captured by the structural equation model, which is utilized in the present contribution to formulate a score-based learning approach. A mixed-integer quadratic program is formulated and an algorithmic solution proposed, in which the pre-generation of exponentially many acyclicity constraints is avoided by utilizing the so-called branch-and-cut (``lazy constraint'') method. Comparing the novel approach to the state of the art, we show that the proposed approach turns out to produce excellent results when applied to small and medium-sized synthetic instances of up to 25 time-series. Lastly, two interesting applications in bio-science and finance, to which the method is directly applied, further stress the opportunities in developing highly accurate, globally convergent solvers that can handle modest instances.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents ExDBN, a novel approach for learning Dynamic Bayesian Networks (DBNs) through a mixed-integer quadratic programming formulation. By employing a branch-and-cut algorithm to ensure acyclicity, the method achieves a globally convergent solution, especially effective for small and medium-sized datasets. Synthetic and application-focused benchmarks in biomedicine and finance demonstrate ExDBN's improved reliability compared to existing methods like DYNOTEARS.

### Strengths
- The paper proposes a mathematically rigorous approach, leveraging mixed-integer programming to enhance global convergence.
- The lazy constraint strategy for acyclicity constraints is innovative and may reduce computational load.
- The benchmark experiments, including applications in biomedicine and finance, demonstrate ExDBN’s potential practical relevance.
- Data generation is explained well, detailing both the DAG and time-series structures used, which aids reproducibility.

### Weaknesses
 - Novelty and contribution are marginal, as the proposed method offers limited improvements over existing techniques.
- The paper includes three pages of bulky and sparsely populated figures that disrupt the flow and readability. Merging figures or including only key results would improve coherence, while additional figures could be moved to an appendix.
- There is limited comparison with other methods, potentially weakening claims about ExDBN's performance advantages.
- Results are presented without adequate explanation or interpretation, leaving readers with limited understanding of the findings' significance.
- Shortcomings and limitations of the proposed method are not discussed, which reduces transparency and leaves gaps in critical evaluation.
- The proposed method lacks solid grounding; the choice of mixed-integer programming is not fully justified, and its advantages over alternative approaches are unclear.
- For readers unfamiliar with mixed-integer programming, an introductory section on the topic would improve accessibility.
- Key results and findings are not emphasized in the abstract, reducing its effectiveness in capturing the study's contributions. It is mentioned "we show that the proposed approach turns out to produce excellent results." This is a qualitative description. I would help capture the readers attention if you quantitatively highlight how ExDBN out performs DYNOTEARS.
- Several key related works are not cited, including foundational and recent contributions, which leaves the literature review incomplete. Relevant missing citations include:
     - "Learning the Structure of Dynamic Probabilistic Networks" by Nir Friedman, Kevin Murphy, and Stuart Russell
     -  "Learning Dynamic Bayesian Networks from Data: Foundations, First Principles and Numerical Comparisons" by Vyacheslav Kungurtsev et al.
     -  "GRACE-C: Generalized Rate Agnostic Causal Estimation via Constraints" by Mohammadsajad Abavisani et al.
     -  "Divide-and-Conquer Strategy for Large-Scale Dynamic Bayesian Network Structure Learning" by Hui Ouyang et al.

### Questions
- How does ExDBN perform when the assumptions regarding data distribution or noise are violated?
How does ExDBN handle missing data or noisy measurements, which are common in practical applications?
- Could you elaborate on the computational requirements of ExDBN compared to DYNOTEARS, especially for high-dimensional datasets?
- Have you considered applying ExDBN to datasets with nonlinear dependencies to test the flexibility of the mixed-integer programming formulation?
- What strategies might practitioners use to select regularization parameters in the absence of known ground truth?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper describes an exact score-based algorithm for inferring dynamic Bayes networks from sample data that maximizes the likelihood of the data. The dynamic Bayes network has both inter-temporal edges (guaranteed to be acyclic by virtue of all of the edges pointing forward in time) and intra-temporal edges which are assumed to be acyclic. The proposed branch-and-bound-and cut algorithm is an exact algorithm that is made compuationally feasible on larger numbers of variables than competitor algorithms by virtue of not adding all of the cyclicity constraints at the beginning of the search, but by eliminating cyclic graphs as they arise during the search. This saves time by eliminating the precomputation of a super-exponential (in the number of vertices) cyclicty constaints. The algorithm is tested on simulated data, where it generally was faster than the alternative DynoTears and had less variance in the results output. It was also applied to real data sets from biomedicine and finance.

### Strengths
The major strengths of the paper is that it describes an exact algorithm for searching for linear dynamic Bayesian networks with Gaussian or non-Gaussian noise, that maximizes the likelihood, and takes greatly reduced time relative to other algorithms. I did not see any technical problems with the paper. The problem was explained clearly, and the modification to previous algorithms was described clearly.

### Weaknesses
There were  a number of weaknesses in the simulation study and in the exposition. The simulation study did not do anything particularly unusual, but it did not use best practices. 

According to the paper, "We generated data in a manner similar to that described in Zheng et al. (2018a) and Pamfil et al. ... Note that we used slightly different generator than in Pamfil et al. (2020) on which DYNOTEARS algorithm perform worse than in original article. We adapted ER and SF generators from Zheng et al. (2018a) for dynamic networks. (2020)." However, the simulations in Zheng et al. (2018a) have been justly criticized in a number of articles. It has been noted that the output of NOTEARS was very sensitive to a number of different features of the data that could be primarily due to the simulation method, rather than being generally true of real data. For example, NOTEARS is sensitive to scaling (i.e. choice of units of measurement), and that the performance of  NOTEARS declined extensively when the data was normalized (Kaiser and Sipos, 2022). It has also been suggested that the performance of continuous optimization algorithms benefit from error terms of equal variance (Ng et al. 2024), the similarity of the order of the variance or R2 of variables to their place in the causal order (Reisach et al., 2021, 2023). The paper does not specify how the variance of the error terms was generated so it is hard to tell whether these problem would  apply in their simulations. The worries about the simulations also affects the authors justification for only comparing ExDBN to DYNOTEARS (because of its superior performance over competitors), but the judgement about superior performance was based on the DYNOTEARS simulation, which is questionable. The authors also make recommendations about heuristic choices of search parameters, based upon the simulation results. They also seem to choose which search parameters to compare to DYNOTEARS under various circumstances based on earlier simulations (or they are only presenting the search parameters with the best results) based on simulations. These are all also questionable unless the generalizability of the simulation results can be confirmed. 

There is a lot of emphasis on the speed of ExDBN. The authors state that their algorithm does not suffer much from the curse of dimensionality. However, while there are scattered remarks about execution times,  there are no tables or graphs of execution times.

The choice of coefficients for the intra and inter temporal edges is described but not justified. The intra temporal edge coefficients are in a fairly narrow range which is not explained.

The authors mention that "c > 0 is the maximal admissible magnitude of any weight". I am unclear about whether this means that c is input as a parameter for the search. If it is, does it affect the speed of the search significantly? How should the value of c be chosen? Presumably, one could just stick in some enormous number, but if that affects the speed or some other aspect of the algorithm that would not be a good idea. Also, they did specify a range for the linear coefficients in their simulations. Was the true value of c given to the algorithm in the simulations?

In the analysis of the financial data, they compare their algorithm to a heuristic algorithm from Ballester. They emphasize that their algorithm is not heuristic, but they do not say how long the Ballester algorithm took or how the results of the Ballester algorithm compared to their results. They also did not describe using DYNOTEARS on the finance data.

The authors compare DYNOTEARS and ExDBN on some biological data. From their description, it is hard to compare exactly how long either algorithm took, and how they compared with respect to the different evaluation scores. Also, they should explain what a duality gap is. 

As the authors note, they did not test the algorithm on non-Gaussian noise.

Minor points:
The G score used in the simulations is undefined. After defining SHD and F1 scores, the authors describe two possible scores relating to the strengths of the edges - neither is identified as the G score. I think it is the one in equation (17), but it should be stated explicitly.

The graphs presenting the simulation results are a little confusing. I think that the x axis in each case is the number of variables, but this caption appears only in some scattered subset of the graphs. In their key explaining what each line and color means, they show the min and the mean  as solid and dotted black lines, even though there aren't any solid or dotted black lines in the graphs. What they mean is that whatever the color the line is, the solidity denotes whehter it is min or mean. 

There is no description of the branch and bound and cut algorithm (which is referred to in the abstract as the branch and cut algorithm). There is just a reference to a Ph.D. thesis for the branch and bound algorithm, and then a description of the cut part of the algorithm. Some minimal description of the branch and bound algorithm would be helpful.

It would be helpful to have some description of the "mild" conditions for identification of W.

The authors state that "It should be noted, that naturally the worst possible value and the mean can together be used to bound the variance with respect". Respect to what?

On line 88, "manor" is mispelled.

### Questions
How were the variances of the error terms in the simulations chosen?
How were the ranges for the linear coefficients chosen?]
What were the exact runtimes for each of the algorithms?
Was the true value of the maximum linear coefficient bound c given to the algorithm in the simulations?
How does the choice of c affect the performance of the algorithm?
How should the value of c be chosen?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an exact dynamic Bayesian network structure learning algorithm named ExDBN based on a mixed-integer quadratic program. The authors formulate the structure learning problem as a mixed-integer program and propose a new acyclicity constraint named lazy constraint. The proposed constraint helps tackle the curse of dimensionality since it does not require pre-generation in front of structure learning.

### Strengths
1. The paper proposes a novel acyclic constraint for score-based structure learning algorithms.
2. The authors conducted plenty of experiments to validate their proposed algorithm.

### Weaknesses
1. This paper contains numerous writing errors that severely affect readability.
2. Although the authors claim that their algorithm is an exact learning algorithm, there is no theoretical proof or analysis of their method. Specifically, while the use of a mixed-integer program (MIP) is mentioned, there is no discussion of the specific properties of the objective function or constraints that guarantee convergence to a global optimum within the context of Bayesian network structure learning. The paper lacks a formal proof that the proposed formulation is indeed an exact method for structure learning.
3. There are no ablation studies to show the effectiveness of the proposed lazy constraints. It is unclear how much the lazy constraints contribute to the performance of the algorithm compared to a standard MIP approach without these constraints. The paper does not provide any empirical evidence to support the claim that lazy constraints are beneficial.
4. There is a lack of comparison with other exact BN structure learning algorithms. The paper does not position itself within the existing literature on exact Bayesian network structure learning. There is no discussion of how the proposed method compares to other exact methods in terms of computational complexity, scalability, or solution quality.

### Questions
1. In the experiments, why is only one set of the hyperparameters of ExDBN being evaluated? How did you choose the hyperparameters for each scenario?
2. What is MIP GAP? Could you please clarify this term in more detail?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
A mixed-integer quadratic programming model is formulated, and an algorithmic solution is proposed that circumvents the need for pre-generating an exponential number of acyclicity constraints. This is achieved through the branch-and-cut (or 'lazy constraint') method, which also addresses the curse of dimensionality by dynamically handling the acyclic constraints during the solution process.

### Strengths
1- Structure learning, particularly for dynamic Bayesian networks and time series, is an essential first step in applying Bayesian inference. Therefore, the problem addressed in this paper holds significant practical value.

2- The numerical results for comparison accuracy are sufficient.

### Weaknesses
1- In general, convergence in mixed-integer programming cannot be guaranteed.  For the proposed algorithm which is based on mixed-integer programming, are there any theoretical guarantees or empirical evidence of convergence for their specific formulation? The soundness and correctness of the proposed algorithm need to be formally proven.

2- While the main idea is well presented, the authors have not clearly conveyed the details of the proposed method.

3- One of the key contributions of the proposed method appears to be reducing computational burden through the branch-and-cut (or 'lazy constraint') method. However, there is no comparison or analysis provided regarding this computational burden. As is well-known, the computational cost of mixed-integer programming is a significant challenge to its practical application. It would be better if authors compare the runtime of the proposed algorithm with existing methods or analyze the number of constraints generated during the solution process.

4- Several alternative methods for DBN structure learning were neither mentioned nor compared, such as constraint-based algorithms like PCMCI and PCMCI+, or noise-based approaches like TiMINo, VarLiNGAM, and oCSE. Additionally, methods like the Temporal Causal Discovery Framework (TCDF) leverage deep neural networks with attention mechanisms within dilated depthwise convolutional networks to learn complex nonlinear causal relationships between time series. Why do authors only choose the DYNOTEARS method for comparison?  Comparison with some other methods could indicate the improvement of the proposed method on the numerical results.

5- The authors could use statistical tests, such as the Wilcoxon signed-rank test, to compare numerical results.

6-There are some typographical errors. For instance, some variables, such as $\Gamma_{DAG}$ ​ in (6), are not defined. Additionally, the variable $c$ is used to represent two different quantities in (9) and (12).

### Questions
1- How can we select the parameters $\lambda$, $\eta$, and REG? 

2- What is the termination condition for the proposed algorithm, and how can we appropriately determine it?

3- How does the proposed method differ from or improve upon existing techniques for learning dynamic Bayesian networks, and what specific challenges their method addresses that previous approaches could not? Please, clarify your contributions.

### Soundness
3

### Presentation
3

### Contribution
2
