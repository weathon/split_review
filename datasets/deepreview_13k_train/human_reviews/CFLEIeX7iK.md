# Neural Solver Selection for Combinatorial Optimization

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Machine learning has increasingly been employed to solve NP-hard combinatorial optimization problems, resulting in the emergence of neural solvers that demonstrate remarkable performance, even with minimal domain-specific knowledge. To date, the community has created numerous open-source neural solvers with distinct motivations and inductive biases. While considerable efforts are devoted to designing powerful single solvers, our findings reveal that existing solvers typically demonstrate complementary performance across different problem instances. This suggests that significant improvements could be achieved through effective coordination of neural solvers at the instance level.
In this work, we propose the first general framework to coordinate the neural solvers, which involves feature extraction, selection model, and selection strategy, aiming to allocate each instance to the most suitable solvers. To instantiate, we collect several typical neural solvers with state-of-the-art performance as alternatives, and explore various methods for each component of the framework. We evaluated our framework on two extensively studied combinatorial optimization problems, Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP). Experimental results show that the proposed framework can effectively distribute instances and the resulting composite solver can achieve significantly better performance (e.g., reduce the optimality gap by 0.88\% on TSPLIB and 0.71\% on CVRPLIB) than the best individual neural solver with little extra time cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers a new perspective on solving the Combinatorial Optimization (CO) problem using deep learning. Given an instance, a deep learning framework is trained to select the best suitable solver for this instance from a state-of-the-art solver pool. The general idea is (1) feature extraction of the input instance, (2) selection based on several criteria, e.g., top k, and the output of a trained classifier/ranking model.  (3) run the instance on the select solver(s). 

The experiment results show that the proposed method can improve the current single solver performance with few efforts. It also shows the ability to generalize. The key idea behind this paper is similar to this paper: Bai Y, Zhao W, Gomes C P. Zero Training Overhead Portfolios for Learning to Solve Combinatorial Problems[J]. arXiv preprint arXiv:2102.03002, 2021. Since the CO problems are typically too hard, so a single sovler cannot capture the entire problem structure. So, different solvers have their own advantages, then we can leverage this to improve the performance.

### Strengths
(1) Since the CO problems are typically too hard, a single solver cannot capture the entire problem structure. Different solvers have their own advantages, which we can leverage to improve performance.
(2) The experiment results show the ability to generalize.

### Weaknesses
See questions.

### Questions
(1) Do you have any results on TSP-10000 or large instances? Trying to train your selection model on TSP-1000 and see how it can be generalized to TSP-10000 is critical.
(2) Are the instances training the selection model generated from the same distribution of the testing instances?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel framework for selecting the most suitable neural solver for different instances of combinatorial optimization problems (COPs). The framework effectively combines graph feature extraction through attention mechanisms and hierarchical encoders, as well as multiple solver selection strategies, including Greedy, Top-k, and Rejection-based approaches. The experimental results demonstrate the superiority of the proposed method over traditional approaches on tasks like TSP and CVRP. Overall, the paper offers valuable insights to instance-specific solver selection.

### Strengths
1. The paper introduces a novel combination of hierarchical graph encoders and multiple selection strategies, which together enhance solver performance for different combinatorial optimization problem instances.
2. The experimental results cover a range of combinatorial optimization tasks and demonstrate improvements in performance compared to using a single solver.
3. The proposed Adaptive Solver Selection Framework for selecting solvers based on instance characteristics is flexible.

### Weaknesses
1. The current selection strategies include Greedy selection, Top-k, Rejection-based, and Top-p. While these strategies have demonstrated effectiveness in different experimental settings, the basis for choosing the most suitable strategy for different types of instances is not clear. For example, what kind of instances would make Top-k more suitable than Top-p? 
2. The paper could benefit from including more graphical representations.

### Questions
1. The paper mentions that the hierarchical encoder can better leverage the hierarchical structural features in COPs. However, the intuitive interpretation of these hierarchical features is unclear. How do these structures correspond to specific instance properties of problems such as TSP or CVRP?
2. The paper mentions the use of graph features and instance scale as inputs for the selection model, while the specific features of different neural solvers are not directly involved in the learning process. Would the absence of these solver-specific features limit the generalization ability of the selection model?
3. During the score calculation phase, how exactly does the MLP relate to different solvers? In other words, how are the features of different solvers reflected in the MLP, and how does this ensure that the classification results are correlated with the solvers' features?
4. In the Top-p selection strategy, the paper defines a threshold probability $p$ to decide which solvers to retain. Is this threshold set adaptively based on the problem's features, allowing for optimal performance? 
5. The introduction of a hierarchical encoder adds complexity to the model. How does this impact the overall training efficiency and inference speed of the model? Is there any quantitative analysis showing the trade-off between the hierarchical encoder's added complexity and the model's performance improvements?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a neural solver selection framework to efficiently select a subset of suitable neural combinatorial optimization (NCO) solvers to handle each problem instance at the inference time. Three key components (feature extraction, training loss, and selection strategies) have been proposed and investigated in detail for solver selection. Experimental results show that the proposed framework can achieve promising performance on the traveling salesman problem (TSP) and the capacitated vehicle routing problem (CVRP) with little extra time cost.

### Strengths
+ This paper is well written and easy to follow.

+ Algorithm selection is an important strategy for classic (combinatorial) optimization, and it has not yet been well studied for NCO. This work is a timely contribution to this important research direction.

+ The proposed algorithm selection framework can achieve promising performance on different TSP and CVRP instances.

### Weaknesses
 **1. Connection to Neural Combinatorial Optimization (NCO) and Novelty**

Although this work's main motivation is to propose a neural solver selection framework for NCO, it seems that the proposed solver selection approach is actually agnostic to NCO. It is more like an independent learning-based solver selection method that can be used for other solvers, including the traditional ones. What makes the proposed method specific for NCO? The paper does not sufficiently leverage the unique characteristics of NCO solvers, such as their internal architectures or training dynamics, in the selection process. For example, the features extracted are based on problem instances and not the neural solvers themselves. A more compelling approach would involve incorporating solver-specific features into the selection model.

On the other hand, algorithm selection is already a popular research direction in the optimization community. As correctly mentioned in this paper, many (learning-based) algorithm/solver selection methods have already been proposed and widely used in practice (for example, see [1] for TSP algorithm selection). Many of them can be easily adapted to select NCO solvers. What is the novelty/contribution of the proposed framework over the existing algorithm selection methods? The paper needs to clearly articulate how its approach differs from and improves upon existing methods, especially in the context of NCO.

**2. Discussion/Comparison with Existing Algorithm Selection Methods**

I think the claim "[the traditional method] has never been explored in the area of neural combinatorial optimization" is far from enough to truly distinguish the proposed method from the traditional algorithm selection method. A detailed discussion/comparison with traditional algorithm selection methods is needed. The paper should provide a thorough analysis of how the proposed method compares to existing techniques, both learning-based and non-learning-based, in terms of methodology and performance. 

What are the advantages/disadvantages of the proposed method compared with existing (learning-based and non-learning-based) algorithm selection methods? What is the performance of existing algorithm selection methods with NCO solvers? What is the performance of the proposed method with classic solvers? These questions remain unanswered, making it difficult to assess the true contribution of the work.

**3. Novelty of the Key Components**

The proposed framework has three key components, namely feature extraction, selection model, and selection strategies. However, it seems that these components and the proposed structures are quite common in the NCO and algorithm selection community. The novelty and unique contribution of these components should be highlighted with solid evidence. For instance, the graph neural network used for feature extraction is a standard architecture, and the selection strategies are also not particularly novel. The paper should demonstrate how these components are specifically tailored for NCO and provide a detailed justification for their design choices.

**4. Generalization Performance**

Although experimental results show the proposed framework has good performance with problem distribution/scale shifts, it is unclear why it can achieve good out-of-distribution generalization performance as a learning-based method. The paper should provide a more in-depth analysis of why the proposed method generalizes well across different problem distributions and scales. It is important to understand the underlying mechanisms that enable this generalization, rather than simply observing the results.

**5. Experiments**

In the experiments, only a single summary table is provided for each comparison. I think a complete table with separate results for different instances (e.g., with different numbers of nodes), as widely used in other NCO papers, could be very helpful to better understand the performance of the proposed method. The lack of detailed results makes it difficult to assess the method's performance across various problem instances. 

As mentioned above, a detailed comparison with existing (learning-based and non-learning-based) algorithm selection methods is also needed.

### Questions
See weaknesses.

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
This paper introduces a framework for selecting the most appropriate neural solvers for TSP and CVRP at instances level. The framework enhances performance by allocating each problem instance to the most suitable solvers from a pool of available neural solvers via graph encoding and tailored selection model and strategy.

### Strengths
The paper is generally well-structured and easy to follow. The writing is clear and the presentation of the idea is concise. The idea of selecting neural solvers at instance level is interesting and of practical significance.

### Weaknesses
1. The novelty of this work is somewhat limited because the idea of ranking different existing solvers for individual instances is not technically innovative, and the framework seems to highly rely on previous solvers, graph encoders, as well as established losses and selection strategies.
2. To gain the supervision for training requires executing multiple solvers on the same training set, which is probably time-consuming. Furthermore, given such computational overhead, it is believed that a tediously sequential performing of them on the targeted dataset can have been already done for simple selection of the optimal result. Thus, further clarification is needed on the necessity of this proposal.
3. The OPT in the evaluation is somewhat misleading. I suggest the authors solving the test instances with exact solvers or powerful heuristics like Gurobi, LKH3, HGS, etc, as reference solution for the computation of optimality gaps, which also better aligns with previous works. 
4. Additionally, adding such heuristics (in point 3) in your selection zoo is worth considering for further experimental results. If the neural solvers achieve comparable performance as the learning-free methods, the significance of this work is further strengthened.
5. More mainstream solvers should be included, such as [1-7]. They are a set of representing (but not limited to) neural works for routing problem solving, including supervised-, reinforced-, unsupervised-, meta-reinforced-, divide-and-conquer-, and neural-heuristic-mannered approaches. It is acceptable the authors include a subset of them into the framework, but this would benefit the completeness for your empirical evaluation.
6. The authors are also suggested to evaluate their framework on the conventionally used uniform TSP dataset (like those consistent test files through [1,2,4,5,7, etc.]). And please report the origianal objective for the COPs in addition to currently only the gap.
7. The claim in the title is broader than what is done within the paper. If the framework is to be a neural solver selection of combinatorial optimization, can it be readily applied to more complex problems beyond TSP and CVRP? And what is the solution at larger-scaled (e.g., $N\ge 1000$) instances where most neural solvers struggle to produce satisfactory results compared to the traditional heuristics?

### Questions
Please see the weaknesses part for questions and suggestions.

### Soundness
3

### Presentation
3

### Contribution
2
