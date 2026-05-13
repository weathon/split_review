# Unsupervised Federated Graph Matching with Graphlet Feature Extraction and Separate Trust Region

- Decision: Reject
- Scores: 6, 8, 8, 6

## Abstract
Graph matching in the setting of federated learning is still an open problem. This paper proposes an unsupervised federated graph matching algorithm, UFGM, for inferring matched node pairs on different graphs across clients while maintaining privacy requirement, by leveraging graphlet theory and trust region optimization. First, the nodes' graphlet features are captured to generate pseudo matched node pairs on different graphs across clients as pseudo training data for tackling the dilemma of unsupervised graph matching in federated setting and leveraging the strength of supervised graph matching. An approximate graphlet enumeration method is proposed to sample a small number of graphlets and capture nodes' graphlet features. Theoretical analysis is conducted to demonstrate that the approximate method is able to maintain the quality of graphlet estimation while reducing its expensive cost. Second, we propose a separate trust region algorithm for pseudo supervised federated graph matching while maintaining the privacy constraints. In order to avoid expensive cost of the second-order Hessian computation in the trust region algorithm, we propose two weak quasi-Newton conditions to construct a positive definite scalar matrix as the Hessian approximation with only first-order gradients. We theoretically derive the error introduced by the separate trust region due to the Hessian approximation and conduct the convergence analysis of the approximation method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper works on unsupervised federated graph matching. It proposes UFGM, where clients first train locally, then send encrypted node embeddings to the central server for aggregation. Theoretical analysis shows it can maintain good performance without expensive costs. Experiments show its performance.

### Strengths
1. The proposed method can solve such federated unsupervised graph matching problems.
2. Theoretical analysis is provided.
3. Experiments show its performance.

### Weaknesses
1. The challenges and applications of applying federated training on unsupervised graph matching are not clear.
2. The technical advancement of the method is unclear. Traditional graph-matching algorithms with encrypted aggregation on the server side can solve such a problem. Such encryption can be a huge computation and communication cost during training.
3. The algorithm comparison is unreasonable. There is an unreasonable number of comparison methods. All these federated methods are used for supervised training and should not be compared methods with unsupervised training.

### Questions
1. What is the key takeaway of the theoretical analysis? Can it guide the experiments?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript works on the first federated learning mechanism for graph matching with privacy maintainance that supports effective and efficient graph matching at the client and server level, by designing a fast approximate method for graphlet feature extraction for pseudo supervised learning, and by combining separate trust region algorithm with data encryption that satisfy with the privacy requirement of the federated learning. Specifically, the new method samples a small number of graphlets to capture graphlet features of each node as pseudo training data. At last, the method separates model optimization from model evaluation in the federated learning. In the empirical studies, results show it can achieve better performance than all federated learning baselines in all tests and obtain close or better performance than centralized graph matching method.

### Strengths
+Using graphlet feature extraction to generate pseudo training data is helpful to maintain the privacy constraint in the federated learning as well as leaverage the power of supervised learning for better quality.

+The incorporation of separate trust region into the federated learning algorithm for graph matching is interesting. The fact that convergence is also achieved in theory is well-done.

+The theoretical analysis of the approximation error and the convergence analysis seems novel and interesting. These theoretical resluts guranttee the effectiveness of federated graph matching in the context of unsupervised learning.

+The proposed task is well-motivated, the experiment result is promising, and the authors compare several different types of baselines to validate the superior performance of the proposed techniques.

### Weaknesses
-It seems the scope of the proposed method is specific as it seems to only be designed for federated graph matching. I wonder how hard it will be to generalize the proposed method to general federated learning. Specifically, the reliance on graphlet features and the trust region algorithm may not be directly applicable to other types of data or learning tasks commonly encountered in federated learning, such as image or text classification. The method's effectiveness might be limited to scenarios where graph-structured data is inherently present and where the notion of node matching is meaningful. It is unclear how the core ideas could be adapted to settings involving non-graph data or different types of federated learning objectives.

-I can understand the limitations on the experimental side, however, it would be great to hear from authors regarding how the performance of the centralized variant of the proposed federated graph matching approach (i.e., no federated learning)? Does this approach have much better performance? It would be beneficial to understand the performance gap between the federated and centralized versions of the proposed method. This comparison would help to quantify the cost of privacy preservation in terms of performance. Furthermore, it would be useful to know how the performance of the proposed centralized method compares to other state-of-the-art centralized graph matching methods. This would help to establish the overall effectiveness of the core graph matching approach, independent of the federated learning aspect.

-Experiment figures are hard to follow due to small font size.

### Questions
See the weaknesses

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper is the first unsupervised federated graph matching solution for inferring matched node pairs on different graphs across clients while maintaining the privacy requirement of federated learning. The technical contributions of this work are very extensive/impressive. A key to the federated graph matching method is to secure data privacy. It proposes the data encryption and unsupervised learning to provide strong privacy protection. To enhance the matching quality, it develops the graphlet feature extraction and separate trust region for pseudo supervised learning for the problem of federated graph matching. Both theoretical and experimental analyses are shown to demonstrate the computation effectiveness of the proposed method. The paper is well-organized, contains enough information in a limited number of pages, and is easy to understand.

### Strengths
1.	Solving the graph matching problem in the environment of federated learning is of great importance in social networks and financial crime detection.
2.	The paper is the first to explore the potential of introducing federated learning to graph matching.
3.	Theoretical analysis about graphlet estimation and separate trust region within this work is novel and requires numerous technical developments.
4.	The experiments in the paper are extensive and convincing. The experimental results justify the effectiveness of the proposed method.
5.	The paper evaluates both centralized and federated variants of the method and most of federated results achieve comparable results to centralized baselines.

### Weaknesses
1.	The scale of the experiment is a bit small. What will the performance look like on large-scale dataset?
2.	Another concern is the benchmark comparison. Authors claim it is the first algorithm for federate graph matching, so it is better to emphasize how innovative compared with peer works.
3.	A minor issue is that the small font in the figure legend decreases the paper's readability.

### Questions
Scalability test and more discussions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for unsupervised federated graph matching, i.e. matching node pairs that correspond to the same entity across different networks. The authors focus on the unsupervised setting in that it complies better with the privacy requirement. To address the problem of no ground truth matched pairs, the authors compute graphlet degree vectors of each node and use it to match cross network nodes. In addition, to ensure that clients do not know the matching information, the authors design a separate trust region algorithm, such that servers know the matching but does not know embeddings, and for clients vice versa. Some acceleration techniques are used to speedup the computation of Hessians (used in the trust region algorithm) and graphlet degree sampling. 

Experiments are done over real-world network pairs, where the proposed method outperforms various FGL baselines. Parameter analysis experiments are also done.

### Strengths
1. The studied problem is new, novel and challenging. Graph node matching is an important task, and when it is put in federated learning, the authors made a good observation that supervised methods may compromise privacy. The observation is valid, and thus the studied problem, unsupervised federated graph matching, is of good practical value. 

2. The design is also reasonable and practical. To ensure that the pseudo-matching information is not disclosed to clients, the authors design a separate trust region algorithm to split optimizations between client and server. Also, some acceleration techniques are proposed with theoretical results (although I did not thoroughly check their correctness). 

3. The paper is well organized and states its design rationale in a clear manner. I have no problem following the paper. 

4. Experiments are extensive considering the fact that the work does not have many baselines. The results are promising.

### Weaknesses
1. Despite the promising result, I have some questions regarding the fundamental assumption of this paper. The assumption is that, nodes across networks with similar graphlet degree vectors are likely to be the same nodes. However, as graph structures are different in different networks, it may well happen that a node's structure changes a lot, e.g. an author who changes his main research focus, leading to significant alterations in their co-authorship network. The paper does not provide any quantitative analysis of how often this assumption holds true in real-world networks, nor does it discuss the potential impact of structural changes on the accuracy of the pseudo-labels generated. This is a critical point, as the entire method relies on the quality of these pseudo-labels.

2. I wonder whether a split-learning technique can achieve the goal of the separate trust region algorithm. From my understanding, the separate trust region algorithm is designed so that the pseudo matchings are kept at servers and not exposed to clients. This may well be achieved with some kind of split learning, where clients maintain their graph feature encoders, and a matching unit is trained at the server with the pseudo labels. In this case, there would be even no requirement of the Hessian matrices. The authors do not provide a clear justification for the necessity of using the separate trust region algorithm and the Hessian, especially considering the computational overhead associated with Hessian calculations. A comparison with a split learning approach would be beneficial.

3. I wonder what the effect is of the number of pseudo labels to the overall algorithm. Intuitively, this seems like a tradeoff, as when you include more pseudo labels, they tend to be less accurate and bring noise to the overall learning. The paper lacks an ablation study that systematically explores the impact of varying the number of pseudo-labels on the final matching performance. This is important to understand the sensitivity of the method to the quality of pseudo-labels.

4. I also wonder what are the effects of the monte-carlo markov chain sampling methods and the quasi-Newton methods on the overall method runtime/efficiency. The authors made no experiments to analyze the effectiveness either design. Specifically, it is unclear how the choice of MCMC sampling parameters affects the quality of graphlet degree vectors, and how the quasi-Newton approximation impacts the convergence speed and final matching accuracy compared to using the exact Hessian. An analysis of these choices is needed to better understand the method's efficiency.

5. It seems that the loss function is operated on the 'encrypted' embeddings $\hat{v}$ instead of $v$. At this time, a normal non-singular matrix $K$ may just twist some dimensions of the vectors, while shrink some other dimensions. Or in other worlds, a normal non-singular matrix $K$ does not preserve distance (which is exactly the loss function). Thus, how does the loss work on encrypted vector embeddings when they are applied a transformation that does not maintain distance is a little beyond me. Do you need orthogonal ones (those that maintain distance)?

### Questions
Q1. How accurate are the pseudo labels from graphlet degrees? 

Q2. How necessary is the Hessian matrix? What if we use some sort of split learning? 

Q3: What is the effect of the number of pseudo labels?

Q4: What are the effects of the MCMC and the quasi-Newton method on the overall efficiency?

Q5: Does a random non-singular method suffice in privacy-preservation and loss computation? Or do we need an orthogonal one?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
