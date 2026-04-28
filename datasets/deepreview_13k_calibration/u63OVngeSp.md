# Deriving Causal Order from Single-Variable Interventions: Guarantees & Algorithm

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8, 6, 8

## Abstract
Targeted and uniform interventions to a system are crucial for unveiling causal relationships. While several methods have been developed to leverage interventional data for causal structure learning, their practical application in real-world scenarios often remains challenging. Recent benchmark studies have highlighted these difficulties, even when large numbers of single-variable intervention samples are available. In this work, we demonstrate, both theoretically and empirically, that such datasets contain a wealth of causal information that can be effectively extracted under realistic assumptions about the data distribution. More specifically, we introduce the notion of \emph{interventional faithfulness}, which relies on comparisons between the marginal distributions of each variable across observational and interventional settings, and we introduce a score on \emph{causal orders}. Under this assumption, we are able to prove strong theoretical guarantees on the optimum of our score that also hold for large-scale settings. To empirically verify our theory, we introduce \textsc{Intersort}, an algorithm designed to infer the causal order from datasets containing large numbers of single-variable interventions by approximately optimizing our score. \textsc{Intersort} outperforms baselines (GIES, DCDI, PC and EASE) on almost all simulated data settings replicating common benchmarks in the field. Our proposed novel approach to modeling interventional datasets thus offers a promising avenue for advancing causal inference, highlighting significant potential for further enhancements %in downstream tasks, such as causal discovery and active learning, 
under realistic assumptions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors considered the problem of recovering a causal order in structural causal models (SCM) under the causal sufficiency assumption (it seems that is the case but it is not clearly mentioned in the paper). They assumed that they have access to observational data and some single-variable interventional ones and used the changes observed in the marginal distributions of variables to recover a causal order. The authors introduced a notion of faithfulness (interventional faithfulness) and showed that a causal order can be recovered by maximizing a score (defined in (1)) if we have single-variable interventions on all the variables in the system. They proposed a heuristic algorithm (called INTERSORT) aiming to improve the score. The experimental results showed that in some specific settings, the proposed algorithm has a better performance compared to some of the previous work.

### Strengths
Originality/Quality: The authors asserted at the end of the Related Work section that they are proposing the first algorithm to infer the causal order from the interventional data. I do not think this is true. First, (Tian and Pearl, 2013) is one of the earliest works using the changes in marginal distributions due to intervention in inferring some orders among the variables in the system (See Section 4 there). Second, there are extensive works on recovering an equivalence class of models from the observational and interventional data (whether the intervention locations are known or not). A few works are cited in the paper (such as GIES and DCDI). These works can also provide some information about the causal orders that are encoded in the recovered equivalence class. 

Clarity: The paper is generally well-written.

Significant: Based on what was mentioned, I think that the authors should carefully compare their methods with previous work (such as (Tian and Pearl, 2013) when $\epsilon=0$). Moreover, from the experimental results, it is not clear that the proposed algorithm indeed improves SOTA.

### Weaknesses
Comparison with previous work: I think there is no clear comparison with previous work (especially with (Tian and Pearl, 2013)) and discussion about the advantages of the current approach. 

Theoretical result in a very limited setting: I think the assumption of having single-variable intervention on all the variables is very restrictive (what can we say in theory about the recovered causal order if a portion of variables are intervened on?). Moreover, the proposed algorithm is designed under the causal sufficiency assumption (which as far as I checked, is not clearly mentioned in the paper). 

The notion of interventional faithfulness: I think this assumption is an extension of "influentially" in (Tian and Pearl, 2013). The connection to that definition is not discussed in the paper.

Theoretical guarantee about INTERSORT: Although the authors used the term "approximation algorithm" in line 359, there is no theoretical guarantee about the quality of the output of INTERSORT.

### Questions
1. What are the main differences between the current work and (Tian and Pearl, 2013) in terms of faithfulness assumption and methodology?

2. In lines 65-68, the authors are giving the advantage of knowing the order. Did they mean that the number of candidates is divided by 4 if we know that the target gene is in the middle of the causal order?

3. In eq. (1), in the second term, why is there a coefficient of $d$?

4. In Lemma 4, based on the chosen $p_e$, it seems that the graph is disconnected with high probability. Can the authors elaborate more on this?

5. In line 283, the authors argued that the expected error is growing with the order $O(d)$ and they mentioned that it is a strong guarantee. I think the upper bound on the expected error is $d^2$. Therefore, I am not sure this is indeed a strong result.

6. The pseudocode in Algorithm 1 is somehow useless. The most important parts (SORTRANKING and LOCACLSEARCH) are not described there.

7. Evaluating empirically does not imply the quality of the output of the algorithm in theory. I suggest removing the term "approximation algorithm" in line 359.

8. What is the computational complexity of the proposed algorithm? It is also good to compare the algorithms in terms of runtime empirically.

9. In Fig. 2, in some settings (such as NN 30 variables or GRN with a fraction of 23.33%), other methods have better performance. I think it is good to elaborate more on these cases in the experiment section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the concept of "interventional faithfulness," which relies on comparisons between the marginal distributions of each causal variable across observational and interventional settings, and also develops a scoring function for ranking causal orders of variables. Based on this concept, the authors 1) provide strong theoretical guarantees on the optimum of the proposed score and 2) propose INTERSORT to infer causal order from datasets containing large amounts of single-variable interventions. INTERSORT outperforms existing methods in various simulations, demonstrating the potential of the new theory for advancing causal inference in domains like biology.

### Strengths
* The paper introduces a new definition of faithfulness with both theoretical guarantees and empirical results.
* It is well-written and clear.
* Numerical experiments are designed in a sensible manner that adequately supports the claims.
* This is an important and highly relevant contribution to the community, with developed theory that has the potential to further advance causality.

### Weaknesses
 * It’s unclear how the findings would generalize to different settings, such as different distributions over random interventional variables, or in the case of having discrete causal variables. The paper does not explore the sensitivity of the method to the specific choice of interventional distributions, which could significantly impact the observed marginal changes and thus the inferred causal order. Furthermore, the applicability to discrete causal variables is not empirically validated, leaving a gap in understanding how the method performs when the underlying variables are not continuous. This is particularly relevant as many real-world systems involve discrete or categorical variables.
* Empirical experiments are conducted on a limited set of underlying models. The experiments primarily focus on linear, Random Fourier Features, and neural network models, which may not fully represent the complexity of real-world causal systems. The lack of experiments on more diverse models, such as those with non-linear relationships or with different noise structures, limits the generalizability of the empirical findings. Additionally, the single-cell data experiment, while relevant, is still a specific case and does not cover the breadth of potential applications.

### Questions
1. Are there scenarios where the proposed method cannot be applied? In other words, are there real-world systems that do not satisfy e-interventional faithfulness or its relaxations?
2. How could INTERSORT be extended to handle a large number of nodes? I presume for calculating distance, one could replace Wasserstein with e.g. MMD, but what would be the main bottleneck of the algorithm aside from the distance metric?
3. Could the authors elaborate on how the proposed framework could be extended to derive causal order over a subset of variables?
4. Do the authors have any intuition on how this framework might be used to develop better causal discovery algorithms?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Learning the topological ordering of the causal graph behind a set of variables is useful in a variety of scientific domains. For instance, when gene expressions are correlated, the causal order can help discern the structure of the regulatory network. This paper proposes a novel approach for ordering variables using many single-variable interventions. Strong theoretical guarantees and diverse empirical evaluations are presented.

### Strengths
This paper presents an original solution to a significant problem: a method for directly learning the causal order using interventional data.
 * Although technically dense, the paper is surprisingly easy to read and well-organized.
 * The theoretical guarantees for optimality under a reasonable faithfulness assumption appear solid.
 * The approximation algorithm is computationally tractable and validated with a variety of benchmarks.

### Weaknesses
 * The majority of the analysis assumes access to oracle statistical distances between interventional distributions. Little attention is paid to the estimation of these distances using samples, and how they affect the sorting algorithm. Specifically, the paper does not address how the choice of distance metric (e.g., Wasserstein, KL divergence, total variation) impacts the accuracy and robustness of the learned causal order, especially in the presence of finite sample sizes. The theoretical guarantees provided may not hold in practice if the estimated distances deviate significantly from the true distances. Furthermore, the paper lacks discussion on the computational cost associated with estimating these distances, which can be substantial for high-dimensional data.
 * The main score objective (Equation 1) is difficult to understand and not explained much. The paper does not provide sufficient intuition behind the specific form of the scoring function, making it hard to grasp why it is suitable for capturing the desired causal ordering. The lack of a clear explanation of the score's components and their respective roles in the overall objective hinders a deeper understanding of the method's underlying principles.

Minor comments
 * Please define all the terms on like 152, like the noise variable $N_j$.

### Questions
Are there useful heuristics for choosing which variables to intervene on ($\mathcal{I}$)?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed INTERSORT, an algorithm for causal discovery with interventional data, to find a casual relationship with distribution change after intervention. Theoretically, the upper bound of the error is provided for the optimal causal order. Experimental results on simulated and real-world datasets verify the effectiveness of the proposed method.

### Strengths
The score of causal order is designed to identify causal relationships with the help of distribution change engendered by intervention. Theoretically, the upper bound of the expected error is provided for the optimal causal order.

### Weaknesses
1. If setting the threshold following the Remark in Line 203, then it means every pair with distribution change after perturbation will be considered. Why not directly set it to 0, which means detecting distribution change directly?
2. The selection processes also have a large distance, however, this is not a causal relationship. Moreover, selection is common in gene regulatory networks. In your method, how to guarantee the ones you find are causal relations?
3. In eq. (1), what does the second part mean? I scratch my head to understand it. Could you provide descriptions of the symbols used in the equation?
4. In Algorithm 1, how many kinds of permutations will be considered. Usually, it will be non-traversable with an increase in the number of variables.
5. In the part of Distribution with intervention, ' the structural assignment is replaced by a new random variable independent of the parents' means the hard intervention right? Moreover, the author also mentioned that distribution after intervention can be accessed, do you have assumptions about the distribution of intervention? and why you need the distribution needs to be accessed.

### Questions
1. If setting the threshold following the Remark in Line 203, then it means every pair with distribution change after perturbation will be considered. Why not directly set it to 0, which means detecting distribution change directly?
2. The selection processes also have a large distance, however, this is not a causal relationship. Moreover, selection is common in gene regulatory networks. In your method, how to guarantee the ones you find are causal relations?
3. In eq. (1), what does the second part mean? I scratch my head to understand it.
4. In Algorithm 1, how many kinds of permutations will be considered. Usually, it will be non-traversable with an increase in the number of variables.
5. In the part of Distribution with intervention, ' the structural assignment is replaced by a new random variable independent of the parents' means the hard intervention right? Moreover, the author also mentioned that distribution after intervention can be accessed, do you have assumptions about the distribution of intervention? and why you need the distribution needs to be accessed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new method to infer the causal order of an (unknown) causal graph from interventional data. For this purpose, the authors introduce a new assumption (interventional faithfulness), a theoretically grounded score on causal orders, and a practical algorithm called intersort approximating the proposed score. Intersort is evaluated on simulated data.

### Strengths
- The proposed method is the first to estimate the causal order from interventional data
- The paper contains several novel and theoretically grounded contributions, including the causal score as well as the algorithm to approximate it
- Promising empirical results on simulated data

### Weaknesses
 - As common in causal discovery, the method relies on generally untestable assumptions (e.g., epsilon interventional faithfulness)
- The method relies on estimating distributional distances (e.g., Wasserstein distance) which can be statistically challenging. Specifically, the estimation of Wasserstein distances, especially in higher dimensions or with limited samples, can be unstable and sensitive to the choice of parameters. The paper does not discuss the impact of these estimation errors on the final causal order inference.
- No experiments using real-world data are provided. I understand that benchmarking methods are challenging due to unknown causal ground truth, however, I think it would be nice to sketch an application of the method on real-world data and potentially obtain insights
- The related work on causal discovery could be expanded, particularly concerning methods that also leverage interventional data or focus on learning causal order rather than full graphs.

Minor 
- Appendix B seems to be missing
- There is some weird formatting on page 16 (Appendix C and D intersect)
- There is no text in Appendix F.1/ F.2 so it is hard to understand which figures belong to which section. Also, Appendix G intersects with F2

### Questions
- What would be an application in which one would only be interested in inferring the causal order and not the full graph/Markov equivalence class?
- How exactly is the algorithm implemented? E.g., which p-Wasserstein distance is chosen? Which algorithm is used to compute the distance?

### Soundness
3

### Presentation
3

### Contribution
3
