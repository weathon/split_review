# L2P-MIP: Learning to Presolve for Mixed Integer Programming

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Modern solvers for solving mixed integer programming (MIP) often rely on the branch-and-bound (B&B) algorithm which could be of high time complexity, and presolving techniques are well designed to simplify the instance as pre-processing before B&B. However, such presolvers in existing literature or open-source solvers are mostly set by default agnostic to specific input instances, and few studies have been reported on tailoring presolving settings. In this paper, we aim to dive into this open question and show that the MIP solver can be indeed largely improved when switching the default instance-agnostic presolving into instance-specific presolving. Specifically, we propose a combination of supervised learning and classic heuristics to achieve efficient presolving adjusting, avoiding tedious reinforcement learning. Notably, our approach is orthogonal from many recent efforts in incorporating learning modules into the B&B framework after the presolving stage, and to our best knowledge, this is the first work for introducing learning to presolve in MIP solvers. Experiments on multiple real-world datasets show that well-trained neural networks can infer proper presolving for arbitrary incoming MIP instances in less than 0.5s, which is neglectable compared with the solving time often hours or days.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an innovative framework for Learning to Presolve (L2P) within the context of Mixed Integer Programming (MIP) solving using deep learning. To my knowledge, deep learning methods to solve MIPs haven’t explored L2P. Therefore, this work introduces a novel area of research. The proposed framework is well-conceived, offering a new perspective on presolving, and the evaluation suggests that deep learning can tailor presolving strategies to individual MIP instances, potentially enhancing solver efficiency.

### Strengths
1. **Novel Area of Research:** The paper investigates a novel and promising application of deep learning to improve MIP solving, a problem that has not been significantly explored before.

2. **Framework Development:** The authors have developed a new framework to systematically address the identified research gap. This framework could serve as a foundational benchmark for future research in this area.

3. **Empirical Evaluation:** The proposed framework has been rigorously evaluated, with results demonstrating its potential utility for the MIP solving community, which could lead to more targeted and efficient presolving methods.

### Weaknesses
1. **Lack of Detail in Methodology:** The manuscript does not adequately detail critical components of the proposed methods, such as the loss function and the domain of labels—information which is relegated to the Appendix. Specifically, the paper lacks a clear description of the range and nature of the values used for labels in the priority, max-round, and timing tasks. Furthermore, the loss functions used for each of these tasks are not clearly defined in the main text. Moreover, key metrics like the PD integral lack a clear mathematical definition, making it difficult to assess the validity of the results.

2. **Reporting of Metrics:** The paper uses the arithmetic mean to report solving times, which could be skewed by outliers. The geometric mean is a standard in the MIP community for its robustness to extreme values, and its absence is felt in the current reporting. This choice obscures the true performance distribution and could lead to misleading conclusions about the method's effectiveness, especially given the potential for high variance in MIP solving times.

3. **Comparison and Ablation Studies:** The presolving time is only provided for the L2P method. For a comprehensive understanding of efficiency, it would be beneficial to see these times for other compared methods, including FBAS and SMAC3, to ascertain whether the proposed method introduces any overhead. Additionally, the specific benefits of KRL are not clear. While an ablation study is mentioned, the impact of KRL is not sufficiently isolated and quantified. A more granular ablation study to evaluate the impact of KRL, perhaps by comparing performance with and without KRL across different problem instances, would be informative.

4. **Experimental Details:** The number of instances evaluated in Table 1 is unclear. More detailed comparisons, including the time taken during the Running Step for each method, would strengthen the results section. In Table 4, the metric used and the number of instances in each problem family should be stated for clarity. The paper also lacks a clear description of the datasets used, including the number of instances for each dataset and how they were generated or selected, which is crucial for reproducibility.

### Questions
1. **Default Parameters:** For reproducibility, could the default parameters (42 x 3) be listed explicitly in the Appendix (Table 5)?

2. **Neural Network Representation:** Figure 3 is unclear as it suggests that a neural network is derived from an MLP, which is already a type of neural network. Could this be clarified?

3. **Graph Embedding Features:** How are these computed and what aggregation mechanism is used? Is there an aggregation of embeddings across all variables?

4. **Priority Label Input:** Have the authors considered using Priority Label as an input, akin to teacher forcing, and could this approach be compared with the current methodology?

5. **Dynamic Loss Averaging:** More details on this, including how weights are adjusted based on convergence, would be beneficial. If a library function is used, please reference it.

6. **Section Clarity:** In Section 4.2, the fifth sentence needs grammatical correction. Additionally, could Section 4.3 further elaborate on the potential privacy issues mentioned?

7. **PD-Integral:** A mathematical description of the PD-integral and its expected range would greatly aid in understanding its application and interpretation.

8. **Table Details:** In Table 4, the metric used and the number of instances in each problem family should be stated for clarity.

**Typos and Corrections:**

1. **Appendix Repetition:** There is a paragraph repeated in Appendix A.1 that should be corrected.

2. **SA Method clarification:** In Appendix A.2, following Equation 4, it seems that $\Delta_y$ should correspond to the time to solve the instances, as this is the primary optimization concern. Please confirm if this is the case.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes Learning to Presolve (L2P) for Mixed Integer Programming (MIP). The presolving of the MIP solver is a routine that simplifies the MIP instance, enabling the succeeding main solving routine (e.g., B&B) to operate more efficiently. Current presolving routines are hard-coded and rely on expert knowledge, making them unable to account for instance-wise differences in MIP problems. L2P employs a supervised learning method to predict the best presolver routine while using the result of a powerful yet time-consuming search method as the training label.

Using the trained model, L2P proposes tailored presolving routines for each instance in fractions of a second. Such tailored routines lead to a significant improvement in MIP solving performance. The proposed L2P consistently demonstrates performance gains in various MIP datasets while requiring a negligible amount of presolving parameter suggestions.

### Strengths
- The writing is easy to follow and effectively conveys the necessary information to understand the manuscript.
- L2P addresses an understudied aspect of MIP by proposing appropriate presolving parameters on an instance-wise basis.
- L2P consistently demonstrates performance improvements in empirical experiments.

### Weaknesses
 - While the current L2P model shows satisfactory improvements over the baselines, further performance gains may be achievable by leveraging more modern neural network architectures. For example, the authors used GCNN as the backbone of the feature-extracting GNN, which could potentially be replaced with graph-formers in a drop-in replacement manner.
- It may be beneficial to include some related work in the literature review and experiment section. For example, I had the opportunity to review a paper titled "Accelerate Presolve in Large-Scale Linear Programming via Reinforcement Learning," which addresses the same problem but in the LP domain.

### Questions
- Has the performance gain observed from SCIP also been found with other MIP solvers such as GUROBI and CPLEX?
- Regarding the training of the L2P model, how crucial are KRL and dynamic loss averaging? Do they significantly affect the overall trend of the results?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a learning-based approach for selecting the priority, max rounds, and timing of presolvers for MIP solving. They do this by obtaining high quality presolver settings using simulated annealing for several training instances, then training a neural network to predict the high-quality setting for unseen test instances. The network architecture first predicts the priority then based on the priority prediction makes predictions for the max rounds and timing. They evaluate on a variety of settings that demonstrate their method gives improved performance over other hyperparameter prediction methods especially on hard MIP instances. The authors further perform an ablation study to determine the effectiveness of different components of their model and sensitivity to data collection method. Lastly, they investigate their resulting predictions to identify the impact of setting the individual hyperparameters. The paper is overall well written and they tackle an interesting problem of using machine learning to assist in presolving MIP instances.

### Strengths
The main strength of this work is that they tackle a new problem in learning-accelerated optimization, namely learning to improve presolving of MIP instances. Additionally, their results seem to give improved performance over baseline hyperparameter tuning methods and improve runtime of optimization solvers overall. Furthermore, the authors conduct extensive evaluation of their approach to better understand where the performance improvement comes from and how sensitive performance is to modification of their approach. Lastly, the authors evaluate their approach on a variety of domains that are used in real-world settings including sustainable corridor optimization, maritime inventory routing, load balancing, and item placement which have practical impacts, and which the authors demonstrate improved performance.

Additionally, the authors release their code both as a way to benchmark against their approach, but also as a way to enable others working in the space of predicting performant presolver parameters.

### Weaknesses
One weakness is that their approach doesn’t go beyond tuning the hyperparameters of the presolving methods. While their approach does give good performance and is a good first step towards using learning for presolving, it would be interesting to see methods that dive deeper, such as using machine learning to determine new effective methods for presolving. This is a significant limitation as the space of possible presolving techniques is vast, and limiting the approach to only tuning existing parameters may miss out on potentially more impactful strategies. For example, the authors could explore learning which constraints are most effective to preprocess, or learning new constraint propagation rules, rather than just tuning the order and timing of existing ones. Furthermore, the current approach does not address the potential for learning instance-specific presolving techniques, which could be more effective than a single model applied across all instances.

### Questions
Simulated annealing also generates several examples of parameters and their values during the search process; however, that seems to be currently thrown away. Is there a way to use something like contrastive learning to learn from this thrown away data?
Similarly, is there some way to benefit from the fact that the “shape” of the parameter settings is the same throughout the experiment and don’t change from one instance to the next? Is it possible to re-evaluate several performant hyperparameter settings from one instance on a new instance to quickly collect data?

For hard/anonymous instances why is the 55% bolded when the other methods also have 55%?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
MIP solvers make use of various presolving methods to improve their performance, and the parameters for these methods can be tuned for the specific problem instance for maximal effectiveness. The authors propose a deep neural net model that will select those parameters by analyzing the MIP problem structure. This neural network is trained using the solutions found from simulated annealing (SA). The SA takes too much running time to be used for practical cases, but the trained neural net, whose output will mimic the result of the SA, can get the job done very fast, allowing for both good speed and good performance.

### Strengths
This is an excellent pioneering work on applying a learning approach to the presolving stage of MIP solvers. The results are strong, and the proposed method may be readily applied to practical cases.

### Weaknesses
Reports on the details of the neural net training procedures are missing. For example, what are the sizes of the training set/test set? How many epochs were used for training? How much time used? How long did it take to prepare the SA solutions in each case?

Perhaps the most important aspect of this method in terms of practical usefulness is the number of training data needed for the neural net to adequately learn the distribution of the problem set. Is there a rule of thumb on estimating the size of required training data?

It would be nice to see some ablation test results that will display the increase in the performance of the L2P+MIP and eventual saturation as more and more training data is used in constructing the neural net model.

Finally, the paper should include a discussion on the results for the 'Hard: Load Balancing' and 'Hard: Anonymous' problems. The observation that L2P outperforms SA seems counterintuitive and warrants further investigation. This could potentially indicate a flaw in the experimental methodology.

### Questions
Questions are described in the weakness section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
