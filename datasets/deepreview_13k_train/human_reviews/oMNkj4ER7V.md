# A Unified Framework for Bayesian Optimization under Contextual Uncertainty

- Decision: Accept
- Scores: 6, 5, 5, 8

## Abstract
Bayesian optimization under contextual uncertainty (BOCU) is a family of BO problems in which the learner makes a decision prior to observing the context and must manage the risks involved. Distributionally robust BO (DRBO) is a subset of BOCU that affords robustness against context distribution shift, and includes the optimization of expected values and worst-case values as special cases. By considering the first derivatives of the DRBO objective, we generalize DRBO to one that includes several other uncertainty objectives studied in the BOCU literature such as worst-case sensitivity (and thus notions of risk such as variance, range, and conditional value-at-risk) and mean-risk tradeoffs. We develop a general Thompson sampling algorithm that is able to optimize any objective within the BOCU framework, analyze its theoretical properties, and compare it to suitable baselines across different experimental settings and uncertainty objectives.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends the distributionally robust Bayesian optimization (DRBO) framework to a more general framework called “BO under contextual uncertainty” (BOCU). BOCU targets the problem of maximizing some uncertainty objective that takes the context distribution into account. Example problems include worst-case sensitivity, mean-risk trade-offs, DRBO, robust satisficing. The paper develops a general Thompson sampling algorithm that can optimize any objective within the framework. The paper also derives Bayesian regret bound for their developed framework. Finally, some experiments are conducted to illustrate the sublinear regret properties of the framework.

### Strengths
+ The paper is very well written and easy to understand. The problem settings, the previous works, the concepts are all well described.
+ The paper tackles an interesting problem which is to unify different problems (with the same theme of BO under contextual uncertainty) into one framework. The paper also proposes a general method that can solves this unified framework with different objectives. Theoretical analysis is also conducted to guarantee the performance of the proposed method.
+ The proposed method seems to be sound and reasonable to me.
+ The experiments (though a bit limited) are also conducted in order to understand the behaviours of the proposed method and to confirm the theoretical analysis.

### Weaknesses
To me, the main weaknesses of the paper are in the experimental evaluation. I list in the below some weak points that I found from the experimental evaluation:
+ The problems used in the evaluation (GP, Hartmann 3, plant growth simulator, COVID epidemic model) have quite low dimensions, ranging from 2 to 5. This raises concerns about the scalability of the proposed method to higher-dimensional problems, which are common in real-world applications of Bayesian optimization. The performance on low-dimensional problems might not be indicative of performance in more complex scenarios. For example, the curse of dimensionality can significantly impact the efficiency of Gaussian Process based methods, and it is unclear if the proposed method can handle this.
+ I found the analysis regarding the experiments could be further elaborated. Currently, there is only one paragraph explaining a lot of results in one figure (Figure 2), I have to think a lot in order to understand what the reported results convey. The discussion lacks detailed insights into the specific behaviors of the algorithm under different conditions. For instance, it would be beneficial to see a more in-depth analysis of how the algorithm's performance varies with different uncertainty objectives, and how the choice of kernel impacts the results. The current analysis does not provide sufficient information to understand the strengths and weaknesses of the proposed method in different scenarios.
+ For the COVID infection problem, I found the results of DRO are not too good. I’m just wondering what are the issues of these cases? It is unclear why the DRO method performs poorly compared to other methods. A more detailed investigation into the specific challenges of the COVID infection problem and why the proposed method struggles with it would be beneficial. It would also be useful to see a comparison of the optimization trajectories for different methods to understand how they converge to their final solutions.

### Questions
Apart from my comments and questions in the Weaknesses section, the authors could answer the additional following questions:
+ In Theorem 4.1, are the assumptions used common assumptions used in this particular research topic? What are the implications of these assumptions? Is it possible for these assumptions to be occurred in practice?
+ Also, from Theorem 4.1, is the maximum information gain \gamma_T bounded as in the standard BO algorithms? Which kernels will guarantee this maximum information gain to be bounded?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A framework for Bayesian optimization under contextual uncertainty unifies various formulation of Bayesian optimization, including distributionally robust optimization, stochastic optimization, robust optimization, robust satisficing, worst-case sensitivity, and mean-risk tradeoff.  The authors provide theoretical analyses on regret bounds and experimental results to compare several Bayesian optimization algorithms.

### Strengths
* This work serves the comprehensive understanding of Bayesian optimization under contextual uncertainty.
* Paper is well-organized.

### Weaknesses
 * Paper is hard to follow.  For example,

The sentence "While standard BO assumes that the learner has full control over all input variables to the objective function, in many practical scenarios, the learner only has control over a subset of variables (decision variables), while the other variables (context variables) may be randomly determined by the environment" is too complex.  There are two whiles in one sentence.

The sentence "We assume that, at every iteration, some reference distribution $\boldsymbol p$ is known that captures the learner's prior knowledge of the distribution governing $\boldsymbol c$" is grammatically wrong.

"a probability vector in $\mathbb{R}^n$" should be "a probability vector in $[0, 1]^n$" for readability and understandability.

I think there are other grammar and presentation issues.  Please revise your submission carefully.

* I think that some assumptions are too strong.  For example, the assumptions on finite sets of $\mathcal{X}$ and $\mathcal{C}$ are not practical.  Moreover, I do not understand why $\boldsymbol p$ is known at the beginning of the optimization.  This assumption is not practically meaningful.

* Since theoretical results are built on the assumptions on finite sets of $\mathcal{X}$ and $\mathcal{C}$, they are limited.

* Reasoning and justification behind experimental results are not appropriately provided.

### Questions
* Table 1 can have a column for the corresponding references.  It would help understand and compare diverse algorithms

* Could you explain the intuition and meaning of knowing $\boldsymbol p$ at the beginning?

* I am not sure that the ICLR paper format allows it, but the table captions should be located on top of the tables.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies robust BO when there is context uncertainty, and designs a TS algorithm based on a general framework that incorporate a large number of risk-sensitive learning objectives. The authors substantiate its efficacy with theoretical analysis and validate the algorithm's performance and adaptability through experiments.

### Strengths
The paper is clear and easy to follow. The propose method is solid and with decent theoretical and numerical evidence.

### Weaknesses
The significance is of question to me - though it is good to have a unified form for multiple previously proposed objectives, the unification achieved in this paper seems straightforward (adding two parameters) and the additional technical challenge (e.g., in algrotihm design or analysis) is unclear, and it is not clear whether those new objectives are really of significance for practitioners.

Is the first-derivative objective only previously proposed for GP, or is also applicable in other areas? Is 3.1 only novel in GP literature, or for the first time also in other areas?

Why finite context and action space? These read very limited. Are they also required by prior works?

### Questions
1. Is the first-derivative objective only previously proposed for GP, or is also applicable in other areas? Is 3.1 only novel in GP literature, or for the first time also in other areas? 

2. Why finite context and action space? These read very limited. Are they also required by prior works?

### Soundness
3 good

### Presentation
3 good

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
Many problem settings in Bayesian optimization (BayesOpt) require robust solutions to the optimization problem, where the decision maker needs to choose solutions that work well under different contexts that are not controllable.
This paper presents a formulation that generalizes many different BayesOpt settings related to robust optimization, and proposes using Thompson sampling as the optimization policy.
The authors first show a regret bound of this policy that is sublinear given specific assumptions and subsequently demonstrate the empirical performance of the policy under various optimization settings.

Edit: After the rebuttal, I've increased my score from 6 to 8.

### Strengths
The paper is well-written and has a clear exposition.
I enjoyed reading through the formulation of the distributionally robust optimization problem and how it generalizes to previously proposed settings, especially by incorporating the right derivative of the objective.
This general framework allows relating many problem formulations that have been proposed in the literature.
As explained in the paper, by setting the hyperparameters, one can even realize novel optimization formulations that "interpolate" the previously proposed formulations at the extremes, which allows more expressiveness in designing optimization objectives that fit a user's preference.
The proposed TS seems to work well across the experiments.

### Weaknesses
The authors can consider inspecting why in various cases (in the Infection problem for DRO), TS-BOCU has almost linear regret. It would be interesting to see if there are types of problems that the policy tends to perform badly on. (Perhaps this is connected to the insight that the algorithm resulting from setting $\alpha, \beta > 0$ tends to be more robust?)

I am a bit confused about the assumption that $\mathcal{X}$ and $\mathcal{C}$ are finite: Is it necessary for the theoretical guarantee (since Section 4.1 mentions that the result can be extended to infinite sets)? In the experiments (for example, with the Hartmann functions), are you constraining the search spaces to be finite? My understanding is that  the algorithm can run on continuous search spaces too.

I think the paper can benefit from extending the discussion at the end of Section 3.1 and offer guidance for setting $\alpha$, $\beta$, and $\epsilon$ in practice.

### Questions
- Instead of having both $\alpha$ and $\beta$, can't we follow the formulation of mean-risk tradeoff and only vary the weight for the $\delta(\mathbf{x})$ term, unless, for example, $\alpha = \beta = 1$ gives a different objective than $\alpha = \beta = 0.5$ (assuming the same $\epsilon$)?
- As I understand, if $\epsilon_t = d(\mathbf{p}_t, \mathbf{p}^*)$ does not approach $0$ with probability $1$, we don't obtain the sublinear regret result.
How does this might affect performance in practice?
Can we still perform well if $\mathbf{p}_t$ is sufficiently different from $\mathbf{p}^*$?
Are there situations where $\mathbf{p}^*$ is very hard to learn?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
