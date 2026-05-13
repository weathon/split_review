# Integration of neural solver and problem-specific solver through bilevel approach: a case study of min-max capacitated vehicle routing problem

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
In real-world operations with combinatorial structures like vehicle routing problems, similar optimization problems have to be solved repeatedly with slight parameter variations. 
A key challenge in such scenarios is achieving both high solution quality and fast computation time, while traditional methods like heuristics or branch-and-bound struggle to achieve both simultaneously.
In contrast, problem-specific solvers can effectively balance solution quality and computation speed for specific problems. 
However, since real-world problems have more complex structures, they can handle only subproblems.
To enhance the applicability of the problem-specific solvers, we propose a framework that integrates a problem-specific solver and a neural solver. 
Our framework decomposes the optimization problem into subproblems so that some of which can be solved by problem-specific solvers, such as the traveling salesperson problem. 
For the remaining portions of the problem, we utilize the similarities of the problems and design a neural solver.
By integrating two solvers, we can utilize the strengths of the problem-specific solver in balancing solution accuracy and computation speed, as well as the neural solver’s ability to infer a solution from the similarity of optimization problems.
Based on the case study with the min-max capacitated vehicle routing problem, we demonstrate that it outperforms the state-of-the-art solver regarding both high solution quality and short computation time.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a learning framework that integrates a neural solver and a problem-specific solver, aiming to solve combinatorial optimization problems in a bilevel optimization approach. This integration decomposes optimization problems into more manageable subproblems which can be addressed with existing problem-specific solver.  Specifically, in the context of the min-max Capacitated Vehicle Routing Problem, the framework utilizes a neural network for upper-level task assignments and leverages existing TSP solvers for lower-level routing, demonstrating the effectiveness of the integrated framework within CVRP configuration.

### Strengths
- 1. __Integration of a surrogate network:__ 

A surrogate network to support training process through learning from problem-specific solver is a commendable approach.

- 2. __Consideration of city maps:__ 

The use of city maps in case studies enhance the practical relevance.

- 3. __Presentation on the results:__ 

The visual presentation of the test results across three cities is clear with specific highlights, aiding in understanding the performance of the proposed framework on the targeted problem.

### Weaknesses
- 1.__Related work review:__ 

The literature review should be more targeted, focusing on problem decomposition and task assignment methods rather than just on general bi-level approaches, as it does not align with the paper's main contributions, which focus on problem decomposition and task assignment before delegating the subproblem to problem-specific solver. Since decomposing the problem into subproblems is not a completely new approach, especially in routing problem, emphasizing works related to assignment or decompose methods and highlighting their comparisons would help clearly position the work and show its targeted improvements.

- 2. __Experiments:__

•  (1) The experiments should include comparisons with representative decomposition methods to provide context and validate the propose learning framework.

•  (2) Given that Google OR-Tools is an integral part of the framework, presenting results from using Google OR-Tools alone as a baseline can highlight the framework’s capability to enhance outcomes. This demonstration is crucial when addressing more complex routing scenarios with additional constraints or applying the framework to other configurations beyond routing problem. As author states, this framework is designed to handle broader applications, it is important to show this capability because we cannot expect or require all scenario achieve SOTA result as in this simple CVRP scenario.

•  (3)  Considering conducting experiments integrating the framework with other TSP solvers to showcase the adaptability of the method.

- 3. __The framework:__

__Flexibility for more constraints in routing problem:__ in routing problem, multiple stakeholders are involved which brings multiple constraints and objectives that need to be satisfied or balanced. Typically, they are presented across the entire process. When the problem is formulated as a bi-level optimization problem, these constraints will present in different stage. However, the constraints that lead to different VRP variants mainly lies in the lower level, which focuses on route planning, such as delivery sequencing or pairing requirements.  Hence, within the framework, for a new variant, a new specific solver is typically needed, thus a corresponding surrogate network is needed. This reliance on specific solvers for routing can limit the framework's applicability when transitioning to different problem variants.

Besides, for more complicated scenarios, since the problem-specific solver ability and efficiency cannot be guaranteed as in basic CVRP, it is crucial to discuss how the framework ensures efficiency during training.

__Generality for more applications beyond routing:__ Since the author mentions the framework has broader potential application scenario not just limited within VRP. In numerical experiments, it is recommended to include at least one example of applying the framework to a different problem scenario to validate the approach's generalizability beyond CVRP.

### Questions
__1.	Regarding the results:__

As shown in Table 3 - the discussion on generality, since utilizing the corresponding training data does not perform the best on the corresponding testing data, how can one determine to train on which data set to achieve the best performance? 

__2.	Regarding the framework:__

-	In different problem-specific scenarios, the efficiency of the problem-specific solver may vary, particularly in more complex cases. How to balance training time to ensure it remains efficient, as constraints and specific demands become more complicated?

-	How does the surrogate model produce solutions? Is it a once-off output or does it succeed the sequential decision mode?

-	Since the author mentions the framework has broader potential application scenario not just limited within VRP, can it be assumed that when applying to other scenarios, the component network may need to be replaced to capture the appropriate representation of the problem configuration? If yes, then how does the framework perform when applied to other application scenarios, such as stability during training? 

__3.	Regarding the training process:__

-	During training, are the two trainable modules trained jointly, or is the lower-level module pre-trained as a reward model for the upper-level module? If they are trained jointly, how does this affect the distribution of loss between the two models.

-	What is the sampling strategy used for feeding the problem-specific solver? How to evaluate whether the sampling is sufficient to ensure robust performance without compromising efficiency?


__4.	Regarding the experiments:__

-	It is noticed that the comparison result is derived based on conducting local search on the output of each method, instead of directly comparing. To what extent does this operation effect the evaluation.

-	As mentioned in above concerns, when integrating different problem-specific solvers, are there any specific criteria or requirements for their selection to ensure both efficiency and performance?

### Soundness
2

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
4

### Summary
Real-world combinatorial optimization problems are too complex for both heuristic and exact methods. Therefore, this paper proposed a bilevel optimization framework that utilizes a neural solver to leverage the similar structure of real-world problems and thus facilitate the problem decomposition. A problem-specific solver is called to solve decomposed subproblems. This framework can acquire the upper-level solution quickly and improve computational efficiency. In experiments on min-max CVRP, the proposed framework exhibits superior performance to the pure problem-specific solver LKH-3.

### Strengths
1.	The paper targets real-world applications of VRP and utilizes realistic map data to generate training instances. 
2.	The proposed learning-based decomposition method is sound and can outperform pure problem-specific solvers on min-max CVRP.

### Weaknesses
1.	Bilevel optimization for vehicle routing is not a novel idea. Many related works (e.g., [1,2,3]) in the field of neural combinatorial optimization have explored it using different machine-learning techniques. More importantly, these methods also utilize a neural solver for upper-level problems and a problem-specific solver (i.e., LKH-3) for lower-level problems, quite like the proposed bilevel formulation. However, this paper lacks comparisons with these related works and does not even discuss them. 
2.	The technical contribution of this paper is limited. For example, utilizing a neural network to predict a probability map for decomposition has been studied in the GLOP method [2]. Training a surrogate network to predict the quality of subproblem solutions is also similar to the idea of L2D [1]. Moreover, the introduction of LinSatNet for ensuring constraints is also a direct adaption of existing methods, since it has been applied to similar combinatorial problems in the original paper. 
3.	The proposed framework is only applied to one problem, limiting the assessment of its versatility. 
4.	The experimental comparison of this paper is too simple to evaluate the effectiveness of the proposed framework. The authors did not compare the proposed method with any other learning-based bilevel method [1, 2, 3] or end-to-end method [4]. 
5.	Typos: In line 307, “…… ofthe cost estimation ……” requires a blank. 

Refs

[1] Li, Sirui, Zhongxia Yan, and Cathy Wu. "Learning to delegate for large-scale vehicle routing." Advances in Neural Information Processing Systems 34 (2021): 26198-26211.

[2] Ye, Haoran, et al. "Glop: Learning global partition and local construction for solving large-scale routing problems in real-time." Proceedings of the AAAI Conference on Artificial Intelligence (2024): 20284-20292.

[3] Zong, Zefang, et al. "RBG: Hierarchically solving large-scale routing problems in logistic systems via reinforcement learning." Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (2022): 4648-4658.

[4] Zheng, Zhi, et al. "DPN: Decoupling Partition and Navigation for Neural Solvers of Min-max Vehicle Routing Problems." Forty-first International Conference on Machine Learning. 2024.

### Questions
Some concepts in this paper are unclear or strange to me. Please see questions 1 and 2.

1.	The concept of the “cost estimation network” is hard to understand. This network is trained to predict the probability map of vehicle assignment. How is it related to “cost estimation”?

2.	The concept of “feature matrix” in Section 3 is unclear. This feature matrix seems important because it connects the upper-level and lower-level solutions, but it does not have any formal definition. In the case study section, this concept corresponds to the vehicle assignment matrix. However, it is difficult for me to understand its meaning under general combinatorial optimization. Could you explain it more clearly?

3.	In line 292, does the problem instance Z only contain coordinates? Why don't you consider the node demands?

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
In this paper, the authors propose a bilevel optimization framework for solving the CVRP. The approach innovates by incorporating an NN-based model to optimize the upper-level problem of the bilevel scheme. Experiments show that the proposed paradigm has promising behavior.

### Strengths
S1. Bilevel optimization is a relevant paradigm in which using neural solvers to approach one of both problems makes sense. This might definitively improve the overall computational complexity of the process. The idea is interesting.

S2. Good effort in using realistic instances. Literature is full of experiments using artificial instances. I was happy to see this point. However, the authors should note that a random sampling of the delivery points in the map does not resemble real human behaviors. However, I give value to the approach.

### Weaknesses
W1. Throughout the paper, there are statements that in my opinion are wrong, or not properly supported. For instance, in the abstract and introduction, the authors clearly say that heuristic algorithms do not find a good balance between accuracy and computational time. I assume that the authors are including in the same family any metaheuristic algorithm that has been proposed. I would like the authors to note that metaheuristic algorithms are still nowadays in optimization the first option (easy to implement, quick execution time (seconds-minutes), and reasonably good quality solutions) when the problems have exponential complexity. Although the recent advances in DL about optimization show a very promising path, they are not a feasible alternative (the architectures proposed are in general very specific for certain problems). There might indeed be real optimization problems where results could be needed within a few second-time intervals, and for such cases, DL-based methods look better suited. But, the authors do not approach such a case study, but a CVRP formulated in bilevel form. Sorry, but if you access Google Scholar, you will find a huge amount of papers approaching the CVRP using metaheuristic algorithms. If you are going to limit the comparison to LKH-3, please provide a reference that shows that such an algorithm is better than anything previous, otherwise, you need to expand your experiments considering other algorithms too.

W2. Related to the previous case, the authors argue that real world problems sometimes are complex. However, at some point in the introduction appears the TSP. I would expect that the authors would take a real problem, and try to solve it. However, as in a great number of papers (if not all of them), one more time TSP is used. Si uno no conociese el mundo real y mirase a la literatura en ML, pensaría que casi todos los problemsa que hay ahí fuera son el TSP o relacionados (en este caso, el VRP dentro tiene un TSP). ¿Por qué los autores no seleccionan un problema real, con datos reales, donde se pueda aplicar la idea del bilevel? ¿Un problema donde haya que dar soluciones cada segundo? ¿donde los heurísticos no puedan aplicarse? La motivación del paper no es convincente, y tengo la sensación que este paper alimenta la espiral que he mencionado arriba sobre el TSP.

W3. After reading the paper, I wonder if all the complexity involved is worth it. The results are indeed better than those of the LKH, but at the same time, the LKH is a much simpler algorithm and does not require training. However, the idea that the authors put forward, “using neural approaches in bilevel optimization schemes” I think it can have a long way to go. In my opinion, they should go deeper into the idea, and not focus so much on obtaining bold values in the tables. For example, what is the necessary training level of the NN for the framework to work, and how does it compromise the performance of the NN in the upper problem, for the bilevel scheme to work? Bilevel optimization existed before this paper, how does this new approach improve the paradigm? I think it is essential to do convergence analysis, and of course, go beyond the TSP.

### Questions
Q1. LKH was used for comparison, however, there exist other bilevel approaches for the CVRP. Why not compare the proposed bilevel scheme with other bilevel schemes?

Q2. Related to the previous question, the authors limited the execution time of the experiments to 120. Maybe 120 is very little for the LKH, however, there are metaheuristic algorithms that in that time interval can achieve very good results in the VRP. Why not consider them? I think it is necessary to put in context the benefits of the proposed framework.

Q3. The authors used instances of size 100. However, when one thinks of a real CVRP problem, it is expected that in a single day of a transportation company, thousands of packages will need to be delivered. What happens in the performance of the compared algorithms when the size of the instances is increased?

Q4. In Problem 2.1., the authors define x and y-type variables, but I feel x variables are not needed since they can be calculated from y variables. Am I right?

Q5. In section 3, the authors say "When we solve similar problems repeatedly, high-quality solutions share a similar structure...". This statement is not true. It is indeed a necessity by which an approximation algorithm works (similar solutions have similar quality), but there are also works in complexity theory (also for the TSP) in which it is shown that there are phase transitions in the complexity of the instances within little variations.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a two-layer optimization method combining neural networks with problem-specific solver to efficiently solve the min-max capacity vehicle routing problem. The customer nodes are assigned by first dividing them using neural networks and then solving them using a specific problem solver. While the approach shows potential, there are significant issues that need to be addressed.

### Strengths
1. A surrogate network is used to solve the problem that the lower-level problem can’t backpropagate.

### Weaknesses
1. There have been a number of papers that use a similar two-layer optimization approach, where the customer nodes are first divided into subsets and then solved with a solver [1]. Therefore, it is underperforming in terms of innovativeness.
2. In the experiments, the proposed method was only compared with LKH, not with the state-of-the-art learning-based methods. Therefore the advancement of the proposed method is not proved.
3. The use of module components in the framework is not specifically discussed and analyzed, which affects the reader's readability.

[1] Generalize learned heuristics to solve large-scale vehicle routing problems in real-time. ICLR 2023.

### Questions
1. What are the main advantages of this article over previous two-layer optimization frameworks used to solve path problems?
2. In the experimental section, there is a need to add comparative methods.

### Soundness
2

### Presentation
2

### Contribution
3
