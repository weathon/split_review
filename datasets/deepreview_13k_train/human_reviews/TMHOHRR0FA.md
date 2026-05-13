# Rethinking the "Heatmap + Monte Carlo Tree Search'' Paradigm for Solving Large Scale TSP

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
The Travelling Salesman Problem (TSP) remains a fundamental challenge in combinatorial optimization, inspiring diverse algorithmic strategies. This paper revisits the ``heatmap + Monte Carlo Tree Search (MCTS)" paradigm that has recently gained traction for learning-based TSP solutions. Within this framework, heatmaps encode the likelihood of edges forming part of the optimal tour, and MCTS refines this probabilistic guidance to discover optimal solutions. Contemporary approaches have predominantly emphasized the refinement of heatmap generation through sophisticated learning models, inadvertently sidelining the critical role of MCTS. Our extensive empirical analysis reveals two pivotal insights: \textbf{1}) The configuration of MCTS strategies profoundly influences the solution quality, demanding meticulous tuning to leverage their full potential; \textbf{2}) Our findings demonstrate that a rudimentary and parameter-free heatmap, derived from the intrinsic $k$-nearest nature of TSP, can rival or even surpass the performance of complicated heatmaps, with strong generalizability across various scales. Empirical evaluations across various TSP scales underscore the efficacy of our approach, achieving competitive results. These observations challenge the prevailing focus on heatmap sophistication, advocating a reevaluation of the paradigm to harness both components synergistically.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper suggests a novel approach to solving the traveling salesman problem (TSP) by leveraging neural combinatorial optimization techniques, focusing on Monte-Carlo tree search (MCTS) that utilizes a probability distribution in the form of a heatmap for city-to-city edges. Although existing studies have also explored methods combining heatmaps and MCTS, this paper highlights that optimizing MCTS parameters within the conventional 'heatmap + MCTS' framework can enhance performance. Building on this insight, the authors propose a new, parameter-free algorithm for heatmap generation called GT-Prior. Experimental results from TSP-500, TSP-1000, and TSP-10000 demonstrate that performance improvements can be achieved through MCTS parameter optimization in current heatmap-based methods. Furthermore, the GT-Prior algorithm, when integrated with MCTS, achieves performance that is comparable to or slightly better than traditional approaches.

### Strengths
The paper is well-written and easy to follow. It provides a detailed explanation of MCTS algorithm parameter tuning for the TSP problem, dedicating significant effort to the experimental performance improvement and analysis of existing heatmap algorithms through MCTS parameter optimization. The newly proposed GT-Prior algorithm effectively captures the characteristics of the TSP problem and demonstrates a simple yet competitive performance compared to traditional heatmap generation algorithms.

### Weaknesses
As the authors mentioned, heatmap-based MCTS algorithms have been studied in the past. It would have been more impactful if the proposed MCTS algorithm in this paper had shown new technical contributions beyond parameter tuning. Although the study included an analysis of parameter importance using SHAP, it would have been more informative if the paper had elaborated on how these results were applied and their overall significance. Additionally, it is a limitation that the experiments were conducted solely within the TSP domain. It would have been more compelling if additional experiments had been performed across various CO domains, such as the Maximal Independent Set (MIS). Furthermore, while the paper addresses large-scale problems like TSP-1000 and TSP-10000, including real-world experiments using datasets like TSPLIB would have strengthened the work.

### Questions
1. Previous MCTS studies have employed parameter tuning methods like grid search. What fundamentally differentiates the parameter tuning approach in this paper from those in prior research?

2. Would it be possible for GT-Prior to be extended and applied to other combinatorial optimization domains, such as CVRP or MIS, beyond the TSP problem?

### Soundness
3

### Presentation
3

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
The paper revisits the “heatmap + Monte Carlo Tree Search (MCTS)” approach for the Travelling Salesman Problem (TSP). It argues that excessive focus on heatmap refinement in previous research has overshadowed the significant impact of MCTS configuration. Through empirical evaluation, the authors demonstrate that tuning MCTS parameters is critical for solution quality, and a basic k-nearest neighbor-based heatmap performs comparably to complex models.

### Strengths
1, The paper highlights the often-overlooked role of MCTS in improving solution quality, shedding light on its critical impact in the TSP solution process.

2, By introducing a simple, training-free k-nearest neighbor-based heatmap algorithm, the paper demonstrates a practical approach that achieves performance comparable to state-of-the-art models.

3, Experiments across varying TSP scales reinforce the findings, with clear evidence supporting the role of MCTS tuning.

### Weaknesses
1, It would have been beneficial if the paper addressed a broader range of combinatorial optimization (CO) problems rather than focusing solely on TSP.

2, MCTS is a very powerful algorithm, and previous studies have shown significant performance improvements when MCTS is added. Considering this, the paper’s finding that ‘MCTS has a large impact and careful tuning improves performance’ doesn’t feel particularly novel. It would be helpful to include a discussion on the advantages of MCTS over other local search algorithms (e.g., 2-opt) to clarify why MCTS is chosen. Additionally, an analysis of the synergy between MCTS and the heatmap approach would add value, especially considering that, as seen in Table 2, algorithms like Dimes and UTSP perform worse than Zero when MCTS is used.

3, MCTS involves numerous hyperparameters and appears highly sensitive to these settings, which could make practical implementation challenging and less accessible.

### Questions
1, The paper currently addresses only the TSP problem. Do you anticipate that similar results would be achieved if this approach were applied to other CO tasks, such as CVRP? Or are these findings specific to TSP? I’m curious to know if the method generalizes well to tasks beyond TSP.

2, The experimental setup in Section 5.3 (“GENERALIZATION ABILITY”) could be clarified. For example, for DIMES on TSP-1000, it is unclear whether the original (ORI.) setup uses a model and MCTS tuned for TSP-500 or TSP-1000. Similarly, does the generalization (GEN.) setting use MCTS tuned specifically for TSP-1000, or is it using MCTS tuned for TSP-500? Adding a table or flowchart to illustrate the training and testing configurations, specifying the problem sizes for model training, MCTS tuning, and evaluation, would greatly enhance clarity.

### Soundness
3

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
This paper emphasizes the importance of tuning the hyperparameters of MCTS in the heatmap+MCTS strategy for solving TSP. It conducts experiments to analyze the impact of each hyperparameter setting in MCTS. Additionally, it proposes a method to generate the heatmap at a very low computational cost and verifies its performance through experiments.

### Strengths
- This paper experimentally shows that significant performance improvements can be achieved in solving TSP using heatmap+MCTS strategy by tuning the hyperparameters of MCTS.

- The proposed GT-Prior method demonstrates relatively superior results while consuming less computational cost compared to existing methods.

### Weaknesses
 - One major part of this paper, the hyperparameter tuning of MCTS, lacks novelty. In this paper, the authors simply tuned the existing hyperparameters of MCTS without introducing new hyperparameters or proposing a new tuning method, and in doing so, confirmed that it is possible to improve the accuracy of solving TSP. The authors claim that previous studies have not paid attention to the values of MCTS hyperparameters and emphasize the need for careful tuning of MCTS hyperparameters. In previous studies proposing new heatmap generation methods, it seems that MCTS hyperparameters were intentionally left untuned to allow for a fair comparison of the heatmap's performance. While this paper’s confirmation that tuning MCTS hyperparameters can improve TSP solution accuracy has some value, it is not novel that tuning hyperparameters can enhance solver performance. Therefore, simply finding better values for existing hyperparameters through traditional tuning methods is considered to lack novelty.


- The newly proposed GT-Prior heatmap generation method in this paper suggests a way to create a heatmap with minimal computation. Although this method showed the best performance in TSP-10000, it yielded worse results than existing methods (DIFUSCO, SOFTDIST) in TSP-500 and TSP-1000. Additionally, since the GT-Prior method statistically calculates the likelihood of inclusion in the optimal solution based on a ranking of **distances between nodes**, it is likely difficult to apply this method to problems other than TSP, especially those with complex constraints.

### Questions
- In line 360, it is mentioned that 3,000 optimal solutions were used to calculate $\hat{P}_N()$ for TSP-500 and TSP-1000, while only 128 optimal solutions were used for TSP-10000. Given that TSP-10000 is larger in scale, I would expect more instances to be used than for the smaller TSP problems, yet only 128 were used. What is the reason for this? Similarly, I would like to know the authors' opinion on whether it is appropriate to calculate $\hat{P}_N()$ based on statistics from only 128 instances for TSP-10000. 
- Additionally, please confirm whether the $\hat{P}_N()$ used in the experiments in Table 2 and Table 3 was generated using the same number of instances.

### Soundness
2

### Presentation
2

### Contribution
1
