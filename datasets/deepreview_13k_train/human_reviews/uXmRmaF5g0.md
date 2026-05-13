# LORA-MaOO: Learning Ordinal Relations and Angles for Expensive Many-Objective Optimization

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Many-objective optimization (MaOO) simultaneously optimizes many conflicting objectives to identify the Pareto front - a set of diverse solutions that represent different optimal balances between conflicting objectives. For expensive MaOO problems, due to their costly function evaluations, computationally cheap surrogates have been widely used in MaOO to save evaluation budget. However, as the number of objectives $M$ increases, the cost of using surrogates increases rapidly as many optimization algorithms need maintain $M$ surrogates. In addition, a large $M$ indicates a high-dimensional objective space, increasing the difficulty of maintaining solution diversity. 
It is a challenge to reach diverse optimal solutions with a relatively low cost of using surrogates for MaOO problems. 
To handle this challenge, we propose LORA-MaOO, a surrogate-assisted MaOO algorithm that learns $M$ surrogates from spherical coordinates, including an ordinal-regression-based surrogate that learns the ordinal relations between solutions (denoted as radial surrogate) and $M$-1 regression-based surrogates that trained on angular coordinates (denoted as angular surrogates).
In each optimization iteration, model-based search is completed with a single radial surrogate, while $M$-1 angular surrogates are used only once for selecting diverse candidates. Therefore, the frequency of using angular surrogates is largely reduced, lowering the cost of using surrogates. 
In addition, we design a clustering method to quantify artificial ordinal relations for non-dominated solutions and improve the quantification of dominance-based ordinal relations. These ordinal relations are used to train the radial regression surrogate which predicts how desirable the candidate solutions are in terms of convergence. The solution diversity is maintained via angles between solutions instead of pre-defined auxiliary reference vectors, which is parameter-free. Experimental results show that LORA-MaOO significantly outperforms other surrogate-assisted MaOO methods on most MaOO benchmark problems and real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
MaOO often faces the issue of higher costs with the number of objectives increases. This paper addresses this problem by proposing LORA-MaOO, a surrogate-assisted MaOO algorithm that learns surrogates from spherical coordinates. The LORA-MaOO attains competitive experimental results on the multi/many-objective benchmarks DTLZ, WFG5, and the neural architecture search benchmark NASbench201, while necessitating a comparatively low runtime. However, the experimental section has several issues, such as limited improvement in performance and a lack of Intuitive explanation.

### Strengths
1.	The paper is easy to read, with the background information and proposed framework explained clearly.
2.	Authors conducted extensive experiments to test their method.
3.	The problem of MaOO is clear.

### Weaknesses
1. The presentation of the paper is bad. In the abstract, the authors provide too much detail about proposed method. However, more description about issue, behind reason, and necessary explanation are more important than details.
2. The title of Section 3 is too long.
3. The Figure 1 is not clear. Same questions can be found in, Figure 2, Figure 3, and Figure 4. 
4. Figure 2 is too big. This is illegal to rules of ICLR.
5. This paper lacks a comprehensive comparison about costs. The main goal of the paper is to reduce costs. However, the authors did not provide any experiments about costs.
6. Provide a more thorough discussion of the generalization ability, robustness, and potential applications of the proposed approach.
7. The format of references is not correct.
8. The main limitation of this paper is that proposed method lacks theriacal analysis, ablation study, and visualization.
9. Exploring the reasons behind the success of these techniques and providing intuitive explanations would contribute to the overall scientific contribution of the work.

### Questions
see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a learning ordinal relations and angles (LORA) model-based method for expensive many-objective optimization (MaOO). The key contributions are 1) separate surrogate model buildings, which include one ordinal regression-based model for convergence and a set of surrogate models based on angular coordinates for maintaining diversity, and 2) a non-parametric approach to select diverse solutions for expensive evaluations. Experimental results show that the proposed method (LORA-MaOO) can outperform other surrogate-assisted evolutionary algorithms on different test problems.

### Strengths
+ Expensive many-objective optimization is important for real-world applications.

+ The proposed LORA-MAOO method can outperforms other surrogate-assisted methods on different test problems.

### Weaknesses
 **1. Motivation on the Cost of Surrogate Model**

The key motivation of this work is to reduce the cost of using surrogate models for expensive optimization. However, in the expensive optimization setting, the cost of building and using surrogate models (e.g., a few minutes) could usually be trivial compared with the truly expensive solution evaluation cost (e.g., days or weeks, or huge financial cost). A detailed and convincing discussion is needed to support the claim that reducing the cost of using surrogate models is important for expensive optimization.

**2. Solution Selection Method**

The non-parametric solution selection approach is another main contribution of this work. However, its advantages over existing methods are not clearly discussed. For example, can we use the crowding distance in NSGA-II to replace the proposed angle-based diversity criterion to select candidate solutions? Many other diversity-based indicators have been proposed in the multi-objective optimization community but have not been discussed or compared in this work.

In addition to the computational complexity, what other advantages does the proposed method have compared with hypervolume?

No theoretical analysis is provided for the proposed solution selection method.

**3. Hypervolume-based Method**

In Section 2.2, this work claims that "the time complexity of computing HV increases exponentially with the number of objectives, which may limit the application of MOBO methods on MaOOPs". However, many efficient hypervolume-based methods have already been proposed for many-objective optimization (e.g., [1,2]). All these methods are not discussed and compared with in this work.

[1] An Expensive Many-Objective Optimization Algorithm Based on Efficient Expected Hypervolume Improvement, IEEE Transactions on Evolutionary Computation 2023.

[2] Surrogate-Assisted Environmental Selection for Fast Hypervolume-Based Many-Objective Optimization, IEEE Transactions on Evolutionary Computation 2024.

**4. Pareto Front Approximation for Expensive Many-Objective Optimization**

The proposed method aims to find a set of solutions to approximate the Pareto front of the many-objective optimization problem. However, in the expensive optimization setting, a small set of evaluated solutions is clearly inadequate to approximate the Pareto front well for problems with many optimization objectives (e.g., 10). A more reasonable choice is to find specific trade-off solution(s) as in [3].

A more detailed discussion on how a small set of evaluated solutions could be useful for many-objective optimization in practice will be very helpful in motivating this work.

[3] The Kalai-Smorodinsky Solution for Many-Objective Bayesian Optimization, JMLR 2020.

**5. Experiments**

- The comparison with some expensive many-objective optimization methods such as [1,2] is missing.

- To better understand the proposed method's performance, it could be very helpful to compare it with MOBO methods on multi-objective optimization problems (2 and 3 objectives) with the found approximate Pareto front.

- According to the results in Table 4, the proposed method does not show a clear advantage in the run time. Is it contradictory to the motivation for reducing the cost of using surrogate models for expensive optimization?

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a surrogate assisted strategy to solve (expensive, black-box) many objective optimization (MaOO) problems.
LORA-MaOO is based on the idea of making use of ordinal relations and angels to build surrogate models during optimziation which can be used to identify promising candidate points to evaluate next.
Compared to existing approaches, LORA-MaOO uses spherical coordinates to separate the concepts of convergence (to the true Pareto front) and diversity (of solutions) into distinct surrogate models.
LORA-MaOO learns one ordinal-regression based surrogate (on radial coordinates) that tries to reflect quality w.r.t convergence, i.e., to the true Pareto front, and M-1 regression surrogate models (on angular coordinates) that try to reflect diversity of solutions.
To improve the training of the ordinal surrogate they propose to create artificial ordinal levels via a clustering approach.
During the sequential optimization procedure, LORA-MaOO identifies one candidate point for next evaluation via Expected Improvement on ordinal values, and one candidate point for next evaluation based on the angles between candidate solutions and the reference points taking the point with the largest minimum angle with any point in the reference set.
In a benchmark study, LORA-MaOO is compared to 6 other baselines and competitors on 5 benchmarks of the DTLZ family (with 3, 6, 10 objectives each), 9 benchmarks of the WFG family (with 3, 6, 10 objectives each), and NAS-BENCH 201 with 5 or 8 objectives.
In general, LORA-MaOO performs well and outperforms most competitors on some benchmarks with respect to quality of solutions and diversity and with respect to runtime being slightly better compared to other surrogate assisted approaches that leverage multiple surrogates.
The paper also presents results of an ablation study on the hyperparameters of LORA-MaOO (i.e, the minimal number of ordinal levels; dominance coefficient; ratio threshold of reference points and the clustering number for reproduction).

### Strengths
The introduction of MaOOP and their characteristics and challenges is done well and LORA-MaOO is inspired by these challenges in a reasonable way, although motivated heuristically.
The general idea of multiple surrogate models based on spherical coordinates is apparently novel to some extent and interesting and so is the separation of quality vs. diversity when proposing candidate points.
In general, the paper has a clear defined structured and is written reasonably well.
Multi Objective Opimization problems and also MaOOP are a relevant field that is also connected to the ML and DL community, as the authors try to demonstrate based on the NAS-Bench-201 benchmarks.

### Weaknesses
While the idea of LORA-MaOO of using multiple surrogates based on spherical coordinates and having one ordinal model that captures quality whereas M-1 models capture diversity is somewhat reasonable, it is mostly inspired in a heuristic way, as is the definition of the criteria used to select each of the two candidate points from the two different modeling approaches during a proposal step.

LORA-MaOO does perform well on the benchmarks presented in the paper, however, improvements do depend on benchmarks and number of objectives at hand and especially anytime performance can vary.
Overall, improvements appear to be rather mild on average.
Gains in efficiency mostly come from leveraging the different modeling approaches during the candidate prediction step (i.e. one candidate point based on the ordinal regression model, on radial coordinates, and one candidate point based on the M-1 regression models, on angular coordinates) which results in speed up during inference, however, LORA-MaOO still requires the training of M independent models.
Further, it is not discussed if and how multi-task modeling approaches could be useful here, especially for the M-1 regression models on angular coordinates.

The actual proposal step of LORA-MaOO is a two-step procedure: One candidate is proposed based on quality criteria of the ordinal regression model on radial coordinates, One candidate is proposed based on diversity criteria of the M-1 regression models on angular coordinates.
While this seems to be reasonable it is a heuristic approach that tries to capture this trade-off in improving quality vs. increasing / maintaining diversity.
Maybe designing an adequate acquisition function jointly on both surrogates could add in adding some technical depth to the proposed method.

One strong downside is that the paper does not have a strong direct connection to the ML and DL community but would be better suited within the black-box optimization community.
While the authors try to motivate relevance by benchmarking also on NASBench201, these benchmarks feel very much constructed and in my opinion are not suited as many objective problems:
For example, the 5 objectives for the first NASBench201 benchmark on CIFAR-10 presented in the paper are accuracy, number of flops, number of parameters, latency and energy cost. However, these objectives are usually strongly correlated, especially number of flops and number of parameters as well as latency and energy cost, because they are mostly tied to the complexity of the neural architecture.
In essence there is only one trade-off in this benchmark (accuracy vs. proxy measures of model complexity).
Generally, performance of LORA-MaOO compared to the limited number of competitors run on this benchmark is not convincing.
Moreover, applicability of LORA-MaOO to real-world NAS problems is strongly limited because it operates in the full-fidelity black-box setting and the authors do not discuss extensions to grey-box multi-fidelity variants, i.e., speeding up the costly evaluation of architectures by terminating the evaluation of poor-performing architectures after a low number of epochs trained which is the de-facto standard nowadays when trying to make NAS more sample- and cost-efficient.

Overall, due to limited direct relevance to the ML and DL community which is the main target audience of ICLR and limited improvements over baselines and competitors as well as mostly heuristic motivation of the algorithm and its component, I have a hard time recommending acceptance.

### Questions
What I felt was missing in the introduction is some background on expensiveness and black-box nature of the problems. The paper surely feels to be positioned in this expensive black-box setting but this is not made clear in the abstract or introduction. Could the authors maybe improve that?

2.1 Why is ParEGO listed under 2.1 and not 2.2? As far as I know, it can be considered a standard example for a scalarized MO BO approaches?

2.2 The connection between MOBO and SEAEs is not well established, can the authors maybe revisit that?

EQ (3) Can you elaborate on the $\max(f_\{in}(x))$ part when defining $g_{\lambda,i}$ - is this actually added to all $g_{\lambda,i}$ and increases them by the same amount, i.e., a flat penalty? Because the $\max$ is taken over all $j = 1, ..., M$ objectives?

EQ (2) Is there any particular reason to denote the normalized objective as $f_{in}(x)$?
It is not initially clear what the $n$ would stand for especially when looking at $f_{jn}$ in EQ(3)?

EQ (4) Within the extension coefficient: The assignment formula $v_{i} = 1 - (i-1/N_{o}-1)$ assumes each ordinal level to represent an equal increment of quality from the reference set. Can you discuss this assumption? E.g. what about solutions near the reference boundary vs. solutions further away?

Can you provide some details with respect to estimated runtime overhead of the clustering approach to introduce artificial ordinal levels?

Overall LORA-MaOO still trains M surrogate models in total; can the authors elaborate on the claim that LORA-MaOO is more efficient with respect to surrogate modeling compared to other approaches?
In Line 287 this is discussed to some extent, i.e, the ordinal surrogate being used for one candidate whereas the regression surrogates are used for the other candidate, however, this still requires to train M models and only inference is sped up?
Also based on Figure 4, efficiency gains with respect to runtime are not substantial and competitors such as PAREGO, CSEA and REMO naturally are more efficient than LORA-MAOO due to their different modeling approaches.

Was there any specific reason to present DTLZ in the main paper but not WFG (except for limited space)?

As you are comparing LORA-MaOO to 6 competitors on many benchmarks of the DTLZ and WFG family via Wilcoxon signed-rank tests: Have you corrected for multiple comparisons? Based on the table caption in Table 1 you state that you test at an $\alpha$ level of $0.05$. However, as you are repeatedly comparing the same methods on similar benchmarks there is some multiple comparison testing issue that should be considered when performing the Wilcoxon signed-rank tests. Otherwise you risk false positive results.

Was there a specific reason to exclude ParEGO as an MO BO baseline in the NASBench201 benchmarks?

Some further minor comments/questions:

L107: I would rather write "scalarized" instead of "aggregate" objective

L109: In ParEGO the Tchebycheff scalarization is newly performed within each step of BO and not pre-defined and constant. Maybe the authors can revisit that section and correct this?

L214: "is" appears to be missing ("that used for training")

Eq(3) There appears to be some space missing between $\lambda$ and $\max$

LORA-MaOO is likely not a good idea name for the method due to the very popular LoRA method in the context of LLMs so people might draw wrong conclusions about the paper based on the title and name of the method.

Writing quality is somewhat decreasing in the experimental setup section, i.e., missing verbs in L346 and L353.
Can the authors maybe revisit that section?

In 4.2 results of the ablation study are presented first before presenting the main results in 4.3.
Maybe reversing the order would be better for the flow of the paper.
Also, the ablation study is in essence meta-configuration of LORA-MaOO (i.e., Hyperparameter optimization) but on (partially) the same benchmarks, LORA-MaOO is then compared to competitors; this may result in overfitting to the benchmarks. Can the authors comment on that?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an evolutionary algorithm assisted by ordinal surrogate and angular surrogate for solving expensive many-objective optimization problems. The authors introduce two strategies, ordinal surrogate and angular surrogate, to maintain the convergence and diversity. Additionally, the authors propose a improved method to quantify dominance-based ordinal relations. Extensive experiments on benchmark and neural architecture search problems are conducted to demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper proposes a  novel ordinal-regression-based surrogate model that is used to learn ordinal landscapes of expensive many-objective optimization problems. This is a very interesting topic.
2. Extensive experiments on benchmarks and a practical case are employed to verify the effectiveness of the proposed method.
3. This paper clearly introduces the proposed method. The paper will provide a link which claims the code availability after the paper is accepted.

### Weaknesses
1. The clarity of the motivation requires substantial improvement. In the abstract, the authors point out that the challenges of many-objective optimization algorithms include the cost of surrogate models and maintaining solution diversity. "Learning surrogates from spherical coordinates" is intended to overcome the aforementioned challenges. Firstly, "spherical coordinates" are not clearly explained in the abstract. Secondly, the term "M − 1 regression-based surrogates" is not sufficiently clear in context. Furthermore, the advantages of ordinal surrogate and angular surrogate compared to existing methods are not adequately explained. The simple description, "which lowers the cost of using surrogates and thus enhances the optimization efficiency," is not convincing.
2. In the motivation of the Introduction, what are the advantages of ordinal surrogate compared to existing methods? Additionally, what are the advantages of angular surrogate compared to methods introducing reference vectors? In fact, reference vectors can be generated from a probability distribution, which is not a complex method. The motivation behind the "non-parametric diversity maintenance strategy" mentioned in the text is unconvincing.
3. The statement, "This framework provides flexibility to use only a subset of surrogates during the optimization and thus reduce the cost of using surrogates," should be supported by evidence. Compared to what other methods does it reduce the cost of using surrogates?
4. In Section 3.3.1, the initial population is comprised of two components (as stated in Lines 1-9 of Algorithm 3). What is the rationale behind this design? "The remaining initial solutions are mutants of current reference points." The motivation behind this design should be clearly articulated. Furthermore, its effectiveness should be demonstrated through ablation experiments.
5. The statement, "Some HV-based MOBO methods are not compared as they failed to solve many objectives," is somewhat absolute. Furthermore, reference vector-based methods should be included as baselines. The work titled “Pareto Set Learning for Expensive Multi-Objective Optimization” should be included in the comparison.
6. The effectiveness of ordinal surrogate and angular surrogate should be further analyzed. Specifically, the accuracy of the regression model should be clearly demonstrated.
7. How can the superiority of angular surrogate in maintaining diversity, as compared to decomposition-based methods, be experimentally or theoretically demonstrated?
8. The time complexity should be briefly analyzed, especially for calculating ordinal values (Alg. 2).

Minor issues:
1. There is a missing space after "It is a challenge to reach diverse optimal solutions with a relatively low cost of using surrogates for MaOO problems."
2. In the introduction, the description of "Pareto front" is inaccurate. "A set of non-dominated solutions that represent different optimal balance between conflicting objectives." should refer to the Pareto set, not the Pareto front.
3. In the "Connection to SAEAs" section, the descriptions of "SAEA" and "MOBO" are not rigorous. The former refers to surrogate-assisted evolutionary algorithms, while the latter refers to multi-objective Bayesian optimization. Firstly, the former can be applied to both multi-objective and single-objective problems. Secondly, the main difference between the two lies in the method of solution generation. Thirdly, it is not rigorous to distinguish between them based on whether a probability model is used.
4. In Figures 1 and 2, certain content is not visible due to obscuration. The size of the images should be adjusted accordingly.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2
