# Quantile-Optimal Policy Learning under Unmeasured Confounding

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
We study quantile-optimal policy learning where the goal is to find a policy whose reward distribution has the largest $\alpha$-th quantile for some $\alpha \in (0, 1)$. We focus on the offline setting whose generating process involves unobserved confounders. Such a problem suffers from three main challenges: (i) nonlinearity of the quantile objective as a functional of the reward distribution,  (ii) unobserved confounding issue, and  (iii) insufficient coverage of the offline dataset. To address these challenges, we propose a suite of causal-assisted policy learning methods that provably enjoy strong theoretical guarantees under mild conditions. In particular, to address (i) and (ii), using causal inference tools such as instrumental variables and negative controls, we propose to estimate the quantile objectives by solving nonlinear functional integral equations. Then we adopt a minimax estimation approach with nonparametric models to solve these integral equations, and propose to construct conservative policy estimates that address (iii). The final policy is the one that maximizes these pessimistic estimates. In addition, we propose a novel regularized policy learning method that is more amenable to computation. Finally, we prove that the policies learned by these methods are $\tilde{O}(n^{-1/2})$ quantile-optimal under a mild coverage assumption on the offline dataset. To our best knowledge, we propose the first sample-efficient policy learning algorithms for estimating the quantile-optimal policy when there exists unmeasured confounding.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the problem of identifying the policy whose reward distribution with the largest $\alpha$-quantile. The authors are particularly interested in the setting when there is unmeasured confounding i.e. not all variables that affect the choice of the actions in the offline datasets are recorded in the dataset. The general setting of unmeasured confounding is difficult and often impossible and the authors focus on two cases --  (a) instrumental variables, and (b) negative controls. The proposed approach effectively combines conditional moment restrictions (popular in econometrics) with pessimism based policy optimization (popular in offline reinforcement learning). The authors provide theoretical guarantees and statistical rate of the proposed method under reasonable assumptions on the data generating process.

### Strengths
1. I think the authors study an important problem as the issue of unmeasured confounding / partial observability is quite common in offline reinforcement learning. The proposed method also combines causal inference techniques with pessimism based policy optimization methods from offline reinforcement learning.

2. The theoretical results are interesting and provide statistical rates under the two settings -- (a) instrumental variables, and (b) negative controls. However, the results are proven under strong assumptions (see comments in the next section).

### Weaknesses
1. Since the paper deals with causal inference with unmeasured confounding, it should include experiments on real-world datasets. Handling real-world datasets introduces many challenges e.g. discrete outcomes, missing covariates etc. The current experimental setup considers a simulation based setting that considers linear functionals, one-dimensional context, and is too simple to demonstrate the effectiveness of the proposed method. The simulation environment uses a simple linear model, which does not capture the complexities of real-world scenarios where non-linear relationships and high-dimensional feature spaces are common. The lack of experiments on real-world datasets makes it difficult to assess the practical applicability of the proposed method. 

2. The authors make several strong assumptions in order to prove theoretical results. First, it is assumed that the parameter $\eta_n = O(n^{-1/2})$ but this is only true for simple classes of functions (as shown in appendix E) and is not true in general. This assumption is crucial for the convergence rate analysis, and its violation could significantly impact the theoretical guarantees. Second, assumption 4.7 assumes that the conditional density is continuous and it eliminates all causal inference problems with discrete outcomes. This is a significant limitation as many real-world datasets involve discrete outcomes, and the proposed method would not be applicable in such cases. Third, I believe assumption 4.9 is quite strong and there is no justification as to why it should be true. The assumption requires a specific relationship between the instrumental variable and the unobserved confounder, which is difficult to verify in practice and may not hold in many real-world scenarios.

3. Overall, I found the paper hard to follow. Many steps require further explanation and the assumptions require further justification. The connection between the theoretical results and the proposed algorithm is not clearly explained, making it difficult to understand how the theoretical guarantees translate into practical performance. The paper would benefit from a more detailed explanation of the technical steps and a more intuitive presentation of the theoretical results.

### Questions
1. Can you please justify why assumption 4.9 should be true?

2. Solving offline reinforcement learning requires some type of coverage condition on the data e.g. single-policy concentrability. In the paper, I haven't seen any explicit mention of such coverage conditions. Can you please clarify what you assume regarding the overlap between the optimal policy and the data-generating policy?

### Soundness
3

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
The paper studies offline reinforcement learning with three main differentiators: 

1. the objective (cumulative rewards) is measured in $\alpha$-quantile, rather than expectation.

2. observations have latent confounders.

3. how to define sufficient coverage in this setting. 

The proposed method runs in two steps: (1) perform causal inference to get a nonparameteric model and (2) apply pessimism principle. Then for the practical use, a policy optimization method is proposed. It is claimed that this is the first sample-efficient policy learning algorithm in this setting.

### Strengths
- This new setting sounds interesting, and authors did a good job of motivating the setting relatively well (though also see weakness on this point). 

- The writing quality is in general quite good, except the technical part (also see weakness on this point).

### Weaknesses
 - The authors motivated the unmeasured confounders with a healthcare example, and quantile optimization with job training programs. However, these are distinct cases, and I wonder whether there is one *unified* motivating example that requires both.

-  Section 4, while highly technical, is the most important part of the paper as the main contribution of the paper claims novel methodologies. Such section must be written with extra care on the clarity even though it conveys complex ideas. As it stands now, it is almost impossible to decipher this section. Here are a few main points that call confusions:

 1. How strong is Assumption 4.1? What would this imply if you bring it to the tabular setting for instance?

 2. Theorem 4.5 -- again, if you could explain this in the tabular setting, that might help a lot. 

 3. Presentation became overly complicated by combining the quantile-objective formulation and nonparametric approaches, which I began to doubt why such complication was necessary in this work, and what does it have to do with novelty of the proposed method. 

 4. I think not many readers, even the experts in RL, can go through the subsections here. 


- I think the experimental section could have been reinforced in the main text. The experimental setup is not clear: what are the "p% of random noises"? Does it mean a random exploration?       
 
- It is also not very clear what the plots are saying: small regret if sample size grows large? Why is that surprising?



### Questions
- It is confusing whether we have two datasets, one with intervention and the other without intervention. If Z is an instrumental variable, does it appear in the dataset?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates offline learning with partial observability under a quantile-based objective. The proposed algorithm uses minimax optimization and incorporates the principle of pessimism. Under various assumptions (including identifiability, compatibility of function approximation, coverage of the dataset, etc.), convergence rate of the proposed algorithm is provided.

### Strengths
It is interesting to see how the tricks from the theory of offline RL also apply in this setting.

### Weaknesses
Readability of this paper.

1. The notations are horrible. Letter W is both NCO variable and a function of (D,h). $\mathcal{O}$ stands for both observation space and big-O notation.

2. The bounds hide most dependency on the parameters, which makes it difficult how assumptions influence the results. For example, the dependency hidden in $o_p(\cdot)$ is never properly specified.

3. The assumptions are stated messily and lack sufficient explanation. For example: (1) It is not clear to me why the identifiability condition of Assumption 4.1 is reasonable, as E[W(D,h)|X,Z] takes expectation over A and can be under-determined. (2) I understand \eta_n corresponds to the complexity of the function class Q, but Condition 4.4 is stated in a unclear way. (3) Assumption 4.10 seems to assume certain coverage condition of the dataset, and should be made clearer (e.g. provide a simpler and sufficient condition for 4.10, possibly in terms of the concentrability). (4) Assumption 4.9 is also difficult to interpret.

4. It is not clear why the parameter eps_{\lambda_n} is introduced.

**Contribution.** It is hard to accurately evaluate the contribution of this paper given its readability  However, it seems to me that most tricks of this paper have already appeared in previous work. It could be beneficial to provide a more detailed comparison to previous works, e.g., Lu et al. 2022, and maybe also the paper of https://proceedings.mlr.press/v162/guo22a/guo22a.pdf.

### Questions
See the discussion of weakness.

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
This work examines quantile-optimal policy learning, focusing on the whole distribution of rewards rather than just the mean. The authors consider a complex setting, addressing challenges such as the nonlinearity of the quantile objective, issues with unobserved confounding, and limited coverage in the offline dataset. They propose using causal inference tools, including instrumental variables (IVs), and adopt a minimax estimation approach with nonparametric models. Computationally, they provide two algorithmic solutions: the solution set algorithm and a regularized version, with the latter offering computational advantages. Theoretically, they analyze the regret rates of the policies derived from both algorithms. Lastly, they conduct a straightforward simulation to assess the performance of the regularized algorithm.

### Strengths
1. This work considers reward distribution and unobserved confounding, a challenging yet highly practical setting, especially as unobserved confounding is prevalent in real applications.
2. The algorithms leverage the Pessimism Principle within minimax estimation to address issues arising from insufficient sample size. Furthermore, the authors introduce a regularized version to handle computational difficulty.
3. Theoretical results are substantial. The authors discuss both IV and NC scenarios in detail and provide in-depth regret analyses for the policies obtained from the two algorithms. The theoretical derivation is comprehensive.

### Weaknesses
1. The motivation for studying quantiles in policy learning is not clear. The authors use an example of income in a job training program to illustrate the relevance of analyzing reward distribution, which has merit but remains insufficient. In particular, the related works section lacks any mention of quantile policy learning literature. Although work in this area is limited, introducing relevant studies on quantile treatment regimes and quantile treatment effects would help clarify the significance of studying quantiles in policy learning.
2. The experiments lack persuasiveness.
- The authors should compare quantile policy learning with standard policy learning. For instance, using job training program example to highlight the benefits of studying the median rather than the mean would strongly emphasize the advantages of the proposed method, yet this is regrettably absent.
- The authors only evaluate the performance of the regularized algorithm through simulations without comparing it to the solution set algorithm, making it difficult to illustrate the computational advantage of the regularized version. While the solution set algorithm may be computationally intractable, its performance could be evaluated in a simplified experiment.
- The simulated DGP is overly simple, with one-dimensional contexts and IVs, and only a single quantile (0.2) selected, which is insufficiently compelling.
3. Readability is lacking. The theoretical analysis in Section 4 is overly detailed, occupying excessive space. The authors could condense Section 4, such as simplifying the paragraph following Condition 4.4, and instead elaborate on experimental results in Section 5 to improve readability. Additionally, symbols and indices are overly complex, and further simplification is advisable.
4. Numerous typos and errors exist in the writing. Here are a few examples:
- Line 061: "we can'' should be "which can''
- Line 066: "our methods works" should be "our method works''
- Line 087: "he'' should be "the''
- Line 112: The notation $O\in\mathcal O$ appears inconsistently, as in Line 361, $\mathcal O (\eta_n)$
- Line 139: "$\pi$'' should be "$\hat{\pi}$"
- Section 3.4 uses ":='', whereas Section 3.5 uses "=''
- Line 294: "the challenge two'' should be "challenge (2)''
- Line 312: Consider changing "function class $\mathbb{F}$'' to "$\mathcal{F}$'' for notational consistency
- Different notations for order: $\mathcal O$ and $\tilde{\mathcal O}$
- Certain theorems lack periods, such as Corollary 4.6
- Line 446: "$l_2$ norm'' should be "$\ell_2$ norm''
- Line 506: The values of $p$ are 20, 50, 70, while in Appendix I (Line 1699), they are 30, 50, 80.
The authors should take a thorough proofreading of the manuscript.
5. Theoretical results in Section 4 rely on the strong Condition 4.4. While the authors mention in Appendix E that Condition 4.4 is satisfied when $\eta_n = \mathcal O(n^{-1/2})$ and both $\mathcal{H}$ and $\Theta$ are linear spaces. However, they do not discuss Condition 4.4 under more complex cases, nor do they consider whether Condition 4.4 can hold without the assumption of $\mathcal{H}$ and $\Theta$ as linear spaces.

### Questions
Could the authors provide a more detailed motivation for studying quantiles, like in which situations quantile policy learning offers a clear advantage over standard policy learning (mean)? Additionally, the authors could supplement the experiment part to highlight the advantages of QPL over standard policy learning.

### Soundness
3

### Presentation
2

### Contribution
2
