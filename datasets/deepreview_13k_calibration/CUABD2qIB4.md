# OCCAM: Towards Cost-Efficient and Accuracy-Aware Classification Inference

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Image classification is a fundamental building block for a majority of computer vision applications.
With the growing popularity and capacity of machine learning models, people can easily access trained image classifiers as a service online or offline. However, model use comes with a cost and classifiers of higher capacity usually incur higher inference costs. 
To harness the respective strengths of different classifiers, we propose a principled approach,  
\ours, to compute the best classifier assignment strategy over image classification queries (termed as the \textit{optimal model portfolio}) so that the aggregated accuracy is maximized, under user-specified cost budgets.
Our approach uses an \textit{unbiased} and \textit{low-variance} accuracy estimator and effectively computes the optimal solution by solving an integer linear programming problem.
On a variety of real-world datasets, \ours achieves $40\%$ cost reduction with little to no accuracy drop.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the trade-off between classification accuracy and inference cost by proposing a framework that combines small and large models. The authors introduce OCCAM (Optimization with Cost Constraints for Accuracy Maximization), a framework that optimally assigns classifiers to queries within a cost budget, leveraging the insight that some “easy” queries can be accurately classified by smaller models. OCCAM uses a statistical accuracy estimator and solves an integer linear programming problem to create a model portfolio that minimizes costs while maintaining accuracy.

### Strengths
- The paper demonstrates statistical guarantees to compute optimal assignments with weak assumptions. 

- Experimental results on classification datasets show  up to 40% cost reduction with
no significant drop in classification accuracy.

### Weaknesses
 - Limited scope of experiments with pretrained classifiers:
The paper's most significant weakness is the limited number of pretrained classifiers used in the experiments. This scope may not provide a comprehensive evaluation of the proposed method and could affect the generalizability of the results.


- Insufficient clarification on related work:
The paper lacks adequate clarification on how it builds upon or differentiates from existing research in the field. Providing a clearer context within the related work section (as highlighted in the Questions) would strengthen the paper by situating it more effectively within the current academic discourse.

### Questions
- How does OCCAM fit into the literature of routing for Mixture-of-experts?

- What is the reason for K = 40 being the maximal value?

- How does OCCAM perform in scenarios with more than 7 classifiers? E.g. model selection literature [1] use more than 100 pretrained models for ImageNet.



[1] Mohammad Reza Karimi, Nezihe Merve Gürel, Bojan Karlaš, Johannes Rausch, Ce Zhang, and Andreas Krause. Online active model selection for pre-trained classifiers. In International Conference on Artificial Intelligence and Statistics (AISTATS), pp. 307–315. PMLR, April 2021.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers minimizing model inference cost by finding the best instance-classifier assignment. A novel method is proposed and there are some new ideas. However, the problem formulation ignores the extra cost induced by the proposed method, which is not discussed in the main text or evaluated in experiments. This is a critical point that might make the proposed method meaningless in some situations.

### Strengths
1. The paper presents a new method to find the best instance-classifier assignment to minimize inference cost.
2. The proposed method for accuracy estimation is asymptotically unbiased and the assignment problem can be solved with ILP solvers. 
3. Good results are show on a specific evaluation setting.

### Weaknesses
1. The problem formulation seems to be unreasonable. The paper aims to find the best instance-classifier assignment to minimize the overall classification inference cost. However, the problem formulation ignores the extra cost for finding the best assignment itself. Specifically, the cost of computing the nearest neighbors and solving the ILP is not considered in the objective function. If the combined cost of these steps is larger than the saved cost in inference from that assignment, there is no point using the proposed method. The paper should explicitly model these costs and demonstrate that the overall cost is reduced.
2. The running time and cost of the ILP Solver is not discussed. This is important as it impacts the applicability of the method in practice. The paper should provide a detailed analysis of the time complexity of the ILP solver and report empirical running times for different problem sizes. It is crucial to understand how the solver scales with the number of instances and classifiers.
3. The sample size can be as large as 40000, which might presents considerable cost in nearest cost, which however, is also not discussed or reported in experiments. The paper should provide a detailed analysis of the time complexity of the nearest neighbor search and report empirical running times for different sample sizes. The cost of this search could be significant, especially with high-dimensional image representations, and needs to be quantified.

### Questions
1. what is the time complexity and empirical running time of the ILP solver? 
2. what is the cost of nearest neighbor search in the sample? 
3. Overall, what is the extra cost induced by the method? Would the gain from reduced inference time be significantly larger than the induced extra cost?

### Soundness
3

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
The authors propose a method for choosing a good set of classifiers that try to maximize classification accuracy while maintaining some cost constraints. Their method is based on estimating the expected accuracies of each classifier in the portfolio using nearest neighbor in a suitable embedding space, and then apply integer programming to find out the best classifier for each test example. Experiments show their method beats several state-of-art methods when tested on several image classification benchmarks.

### Strengths
- This problem of choosing a good set of classifiers to maximize accuracies under computational budget constraints is a very relevant and practical problem given the rising costs of running neural-network-based classifiers. 

- Empirically the method performs very well under various cost reductions when compared to other algorithms such as Frugal-MCT and single best, having higher accuracies at the same cost reduction levels. 

- The authors also provide theoretical justifications for their accuracy estimates of different classifiers for a new test sample, under the assumption of Lipschitz continuity and well-separatedness.

### Weaknesses
 - Choosing the hyperparameter \lambda for different datasets seems difficult. It is set to 100 for Imagenet-1K and 5 for other datasets, which is a large range. This can impact the practical performance of the method. The lack of a principled method for selecting \lambda, and the sensitivity of the results to this parameter, raises concerns about the robustness of the approach. The wide range of values suggests that the optimal \lambda is highly dependent on the dataset characteristics, and without a clear methodology for choosing it, the method's practical applicability is limited.

- The results for unbiasedness and low-variance in Lemma 4.5 and 4.6 are asymptotic. In practice since we are training neural networks for embeddings, the underlying metric space and nearest neighbor function DEPENDS on the training set. For example, the data can be r-separated on the training set since the neural network embedding is trained on it, but not so on a separate validation set. If the samples S_1, ..., S_k in Section 4.2 comes from the training set, the estimates for accuracy can be biased. If they come from a separate validation set then we need a fairly well-represented validation set to estimate the accuracies, which can be a limitation of the method. The reliance on asymptotic results and the potential for bias due to the training set dependence of the embedding space are significant concerns. The assumption of i.i.d data may not hold in practice, and the method's performance could degrade when applied to datasets with different distributions.

- There is a big gap of costs between SwinV2-S and SwinV2-T with no intermediate models. This makes the 10%, 20%, and 40% cost reduction in Table 2 all use the same model for single best and the results for 10% and 20% cost reduction weak for single best since there is no model with intermediate costs available. This lack of granularity in the cost dimension makes it difficult to evaluate the true effectiveness of the proposed method against the single best baseline, especially at lower cost reduction levels. The absence of models with intermediate costs limits the ability to properly assess the single best baseline's performance.

### Questions
- Why are the results for Random the same for all cost reduction levels in Table 2 and Table 4, if it solves the same ILP problem as in Equation 4?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a method for cost-efficient classifier selection at inference time.
The proposed method uses an estimator of classifier accuracy, which is based on the assumption of well-separated classification instances (images) and utilizes samples of classification accuracy from the classifiers.
Given such an estimator, the construction of an optimal model portfolio is stated as an Integer Linear Programming problem. 
The method is evaluated using established image classifiers and standard benchmark data.

### Strengths
- The proposed method is well-motivated and of great practical relevance for users of image classification services.

- The method sound under assumptions of well-separated instances and the findings are supported both empirically and theoretically

### Weaknesses
 - The proposed method relies on precomputed samples of the classifiers under consideration. These are assumed to be given without any cost. However, this is typically not the case. In order to be able to use it in practice, these samples need to be collected which results in expenditure. A good contribution would be to analyse the following question:
Given a user-specified budget, how many samples should be acquired in order to maximize accuracy while adhering to the budget with overall cost (samples for accuracy estimation + classification instances).

- Additionally, the use of the nearest-neighbor based accuracy estimator as well as the ILP solver are assumed to incur no cost, which does not hold in practice. Specifically, the nearest neighbor search has a computational cost that scales with the size of the sample set and the dimensionality of the image representations. Similarly, solving the Integer Linear Program, while often efficient, is not free and its cost can become significant as the number of classifiers and the complexity of the constraints increase.

- The considered problem setting is an instance of the (per-instance) Algorithm Selection (AS) problem (Rice 76). That is, given an instance of an algorithmic problem domain and a set of algorithms suitable to solve said instance, select the algorithm that optimizes a performance metric. For the submitted study, the problem domain is image classification, the problem instances are images, the algorithms are image classifiers and the performnace metric is a multi-criteria with cost and accuracy. There is a substantial corpus of literature concerned with AS and also the idea of using algorithm portfolios has been examined. Although the manuscript considers a very specific instantiation of this problem, I think a reference should be given. 

Minor remarks:
- p 1. line 37: "On the other (hand)"

### Questions
- Is it possible to have a strong (the strongest) baseline by solving the ILP not with an estimator of accuracy but the true classification likelihoods, as an upper bound of achievable performance given a predefined budget?

- To me it seems like the proposed method quite naturally translated into an online setting. It particularly seems to resemble a contextual multi-armed bandit problem, in which each classifier is an arm and the context is given by the classification instances. The reward would be multi-criteria containing costs as well as performance. Would such an extension to online learning make sense?

- The work considers an order of image classifiers, from cheap and less accurate to costly and more accurate. While the classifiers certainly can be ordered wrt accuracy, is there not also a kind of performance complimentarity, i.e. one classifier is better at classifying certain images while another classifier is better suited for other images? I think this may be another strength of OCCAM. Even in (hypothetical) settings in which classifiers have the same cost and the same accuracy on average, OCCAM may be able to identify the better classifer on a per-instance level, effectively outperforming the single best classifier. I am not sure whether these phenomena are present for the considered classifiers and data, however, the possibility should be discussed.

### Soundness
3

### Presentation
3

### Contribution
2
