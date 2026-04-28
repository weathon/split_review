# Memoization-Aware Bayesian Optimization for AI Pipelines with Unknown Costs

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Bayesian optimization (BO) is an effective approach for optimizing expensive black-box functions via potentially noisy function evaluations. However, few BO techniques address the cost-aware setting, in which different samples impose different costs on the optimizer, particularly when costs are initially unknown. This cost-aware BO setting is of special interest in tuning multi-stage AI pipelines, in which we could apply caching techniques to store and reuse early-stage outputs in favor of optimizing later stages, without incurring the costs of re-running the full pipeline. In this paper, we propose the Expected-Expected Improvement Per Unit Cost (EEIPU), a novel extension to the Expected Improvement (EI) acquisition function that adapts to unknown costs in multi-stage pipelines. EEIPU fits individual Gaussian Process (GP) models for each stage's cost data and manages the different cost regions of the search space, while balancing exploration-exploitation trade-offs. Additionally, EEIPU incorporates early-stage memoization, reducing redundant computations and costs by reusing the results of earlier stages, allowing for more iterations than existing approaches within the specified budget. In the cost-aware setting, EEIPU significantly outperforms comparable methods when tested on both synthetic and real pipelines, returning higher objective function values at lower total execution costs. This offers a significant advancement in cost-aware BO for optimizing multi-stage machine learning pipelines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method for cost-aware multi-stage BO that is also memoization-aware, meaning that the method stores the outputs of intermediate stages so as to reuse later. This allows for the proposed method to perform more function evaluation compared to other methods without memoization-awareness given the same budget.

The paper proposes a new acquisition function for this purpose, namely Expected-Expected Improvement Per Unit-cost (EEIPU). The EEIPU consists of 3 components:
- Cost awareness: the method assumes the cost is unknown, so they will build k GP models for k stages to represent the cost, then compute the expected cost by random sampling with Monter Carlo simulation.
- Memoization awareness: the proposed method stores the cost and output for each previous k-1 stages. Then, depending on the number of stored stages, the cost is discounted (but keep some overhead as a small cost), reducing the overall cost.
- Cost cooling: due to the nature of EEIPU, the proposed method may prioritize low-cost regions throughout the optimization, the author proposes to apply a cooling process (seems to base on the paper Lee et al., 2020) for the cost computation. The idea is to apply an exponential decay factor η∈[0,1], which gradually decreases with every iteration, so that eventually, the EEIPU turns back into the common EI acquisition function.

### Strengths
-	The idea of memoization is nice, it can be applied to increase the number of function evaluations for more knowledge to feed into BO process given a fixed budget.
-	The method may do well in the scenario that the budget is the running time allowed for optimization process. This has been proven by the experimental results (left columns of Figure 3,4), where given the same budget, EEIPU can obtain better outputs.
-	The paper writing is clear and easy to understand (although there is one thing regarding the problem setting I will mention in the Weaknesses section).

### Weaknesses
 - As the topic covered in this paper is quite new, it will aid more if the paper includes a problem statement to describe in detail the problem setting. It took me quite some efforts to go back and forth to understand the setup of the problem tackled in this paper.
- Please correct me if I'm wrong but it seems the application for this memoization technique is limited, as the stored data in the previous stages can only be reused when a repeated input for a certain stage is queried again (this is related to the 2nd question in the Question section).
- The number of benchmarks is too few: only 2 synthetic and 2 real-world benchmarks, and with low dimensions.
- In the synthetic benchmarks, it seems the improvement is only because the method manages to evaluate more data. Given the same number of iterations (middle column of Figure 3), even methods without cost-awareness like EI can find similar (or even some better) results. So this seems to me that the memoization only helps with increasing the evaluated data, but not really help much with the modelling of the surrogate model or the BO process.
- The novelty of the work seems to be a bit limited. The idea of memoization and how it is incorporated in the proposed method seem to be a bit simple, while the effectiveness of the memoization to help with the modelling of the surrogate model or the BO process seems to be not clear. There is no deep insights to justify the proposed techniques. Finally, the cost cooling process seems to just inspire from previous works without modification.

### Questions
Besides answering my comments in the Weaknesses section, the authors could answer my following questions:
- What are the specifications of GPs using for the cost modelling? Which priors, kernels and hyper-parameter settings are used?
- For synthetic benchmarks, what is the input space for each stage? Is it discrete? If it is continuous, I'm just wondering how exactly does EEIPU re-use the stored data? It is hard for the acquisition function to propose the exact same points in the continuous domain. From the right column of Figure 3, it seems that the amount of reusing data is approximately 40 times over a total of 80 function evaluations.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the optimization of hyperparameters for a multi-stage AI pipelines with unknown costs.  By utilizing Bayesian optimization, it solves a black-box optimization problem on the AI pipelines.  Since each stage depends on the previous stages and its computational cost varies, it needs to separately model final function evaluations and costs.  Notably, it extends the expected improvement acquisition function to the expected-expected improvement per unit cost, by calculating the expected inverse costs.  Eventually, the authors show some experimental results on several benchmarks with multiple stages.

### Strengths
* It solves an interesting problem related to multi-stage AI pipelines, defined by considering practical scenarios.
* Proposed method is well-motivated.
* Paper is generally well-written.

### Weaknesses
 * More compelling experiments can be conducted.  I think that the experiments tested in this paper seem interesting, but the scale of experiments is small compared to the common scale of the experiments in ICLR. The synthetic experiments lack sufficient complexity to convincingly demonstrate the method's advantages in realistic scenarios. Specifically, the dimensionality of the hyperparameter space and the number of stages in the pipelines are relatively low, which might not fully capture the challenges of optimizing complex AI pipelines. The real-world experiments, while more practical, are limited in number and scope, making it difficult to generalize the findings.
* I don't fully agree with the need of memoization.  Are the processes memoized really computationally expensive?  I think that the numerical analysis can be provided in order to strengthen the motivation of memoization awareness. The paper does not provide a clear analysis of the computational cost associated with each stage of the pipeline. Without this, it's hard to evaluate the true benefit of memoization. The authors should provide a breakdown of the time spent on each stage, with and without memoization, to quantify the actual savings. Furthermore, the paper does not explore alternative strategies for reducing computational costs, such as early stopping or resource-aware scheduling, which could be compared against the proposed memoization approach.


### Questions
* The reference by Mockus (1998) might be published in 1978, not 1998.
* Why should costs be positive?  Is it a mandatory condition?
* In Figure 2, why are $c_1$ and $c_2$ zero in (c) and (d)? Are they correct?  If they are correct, please add description in the rebuttal.
* Why are the best objective values at iteration 0 are different across methods?  Initialization should be identical across tested methods, such that the initial values should be same.
* The captions of tables should be located above the tables.
* I think that the authors need to update Figure 1.  Fonts for mathematical expressions are different from ones in the main article.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose Expected-Expected Improvement Per Unit Cost (EEIPU), a cost-aware BO algorithm able to handle multi-stage pipelines with independent, unknown costs. The acquisition is computed via Monte Carlo sampling to estimate the expected inverse cost which are modelled using GPs on log costs. The multi-stage pipeline is exploited via memoization of previously observed candidates and intermediate outputs. When selecting new candidates, some new candidates reuse the memoized results to avoid incurring costs computing the memoized results again. EEIPU is empirically evaluated with comparison against suitable baselines.

### Strengths
1. The paper is generally written clearly and is easy to understand.
2. EEIPU empirically outperforms previous algorithms when the assumption of a multi-stage pipeline holds.
3. The experiments section is well-designed, the segmentation and stacking pipelines are realistic.

### Weaknesses
1. The assumption of a multi-stage BO process with independent stages and observable intermediates is a very strong one that can be exploited more than this work currently does. This work only exploits this structure to memoize previously evaluated candidates to save costs expended during the BO process. This structure has been exploited to improve the modelling and guide the search, for example, see "Bayesian Optimization of Composite Functions" (Astudillo and Frazier, 2019) and "Bayesian Optimization of Function Networks" (Astudillo and Frazier, 2021). The current approach does not leverage the intermediate stage outputs to inform the search process beyond simple memoization, which is a missed opportunity to improve sample efficiency and overall performance. Specifically, the method could benefit from modeling the dependencies between stages, which could lead to more informed decisions about which candidates to evaluate and which stages to execute. 

2. Perhaps the $M$ prefixes can be sampled more intelligently than randomly, e.g., by weighting the prefixes based on the results of previous evaluations incorporating those prefixes. The current random sampling of prefixes does not take into account the potential value of exploring specific regions of the search space. A more informed approach could prioritize prefixes that have led to promising results in the past, or those that are associated with lower costs. This could be achieved by maintaining a history of prefix performance and using this information to guide the sampling process.

3. The memoization method fails if the intermediate stage outputs are noisy. While AI pipelines could be assumed to have noiseless stages, it is not inconceivable that these stages are noisy, e.g., if the stages are generative models. The assumption of noiseless intermediate stages is a significant limitation, as many real-world AI pipelines involve components that produce stochastic outputs. This lack of robustness to noise could severely limit the applicability of the proposed method in practical scenarios. The method needs to be extended to handle noisy intermediate outputs, perhaps by incorporating uncertainty estimates into the memoization process.

4. Some clarifications, see Questions section, in particular Question 2 about the experimental results.

5. Typos/inconsistencies: 1) Written as $EI \times \mathbb I^\eta$ in Algorithm 1, but $EI * \mathbb I$ and $EI * \mathbb I^\eta$ in Equations (5) and (6); 2) in Figures 3 and 4, left and center column plots are supposed to be best objective value, but the y-axis is written as $f(x^*)$ in the left plots and 'stage costs' in the center plots; 3) [()] described as 'empty prefix' and 'empty subset' in different parts of Sec. 3.2.

### Questions
1. What is the rationale of introducing the $\epsilon$-cost for stages 1 to $\delta$? Why not set to $0$?

2. There are a few peculiarities with the results for EIPS and CArBO in Figures 3 and 4. In Figure 3 bottom row right plot and Figure 4 top row right plot, EIPS and CArBO consume the exact same cost in each iteration as the non-cost aware EI. This is very strange since EIPS and CArBO are supposed to be cost-aware. In addition, in all the results shown, the non-cost aware EI outperforms EIPS and CArBO in terms of best objective value achieved against cost incurred, which is again strange given that EIPS and CArBO were designed for this very setting. Could you investigate and explain these anomalies?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper generalizes the cost-aware Bayesian optimization (BO) algorithm from single-stage to multi-stage optimization problem. To achieve this, a new Expected-Expected Improvement Per Unit-cost (EEIPU) acquisition function is proposed, and a memoization-awareness trick is considered for improving the cost efficiency. Empirical results on both synthetic and real experiments show that the proposed EEIPU outperforms conventional EI and cost-aware BO baselines.

### Strengths
- The problem in this paper is well motivated and the writing style is good. The proposed algorithm and main idea of this work are easy to follow.

- The experimental design is valid. Both synthetic functions and real-world AI pipelines are used to test the proposed algorithm.

### Weaknesses
 - The novelty of the proposed method is limited. The proposed method is a combination of cost-aware BO, unknown-cost modeling, cost cooling, and the memoization trick. All these techniques are not new and have been used in existing BO works (as shown in Table 1). The technical issues or challenges of combining them are not clearly shown in this work. The proposed EEIPU simply replaced the cost function $c(x)$ of EIPU with a total cost function $C(x)$ which is defined as the sum of $c(x)$ over multiple stages. Although the author(s) claimed that computing the expected total inverse cost $\mathbb{E}[1/C(x)]$ is not a straightforward task, the issue is resolved by conventional MC sampling which does not contribute to a non-trivial solution.

- The important baselines are not fairly compared or discussed. In Table 1, why Multi-stage BO is labeled as not cost-aware or memoization-aware? The "stock and resume" scheme of Multi-stage BO is a very similar concept to the "memoization" here and the cost has been considered in Algorithm 2 of (Kusakawa et al., 2021). As shown in Table 1, LaMBO and Multi-stage BO should be the most related works which, unfortunately, are not compared in the experiments. The difficulties of reproducing LaMBO are discussed in Section 3.4. However, it's not clear why Multi-stage BO is not tested. Also, even if both algorithms are hard to reproduce, a detailed discussion about the novelty of EEIPU compared to these two baselines is needed for showing the significance of this work. In particular, since the known and fixed cost are claimed to be the major issues of Multi-stage BO and LaMBO (Section 2), is there any difficulties in generalizing their algorithms to the unknown-cost setting? Compared to the memoization strategies shown in these two works, what is the superiority of the proposed memoization method? Are there any scenarios that can be tackled by EEIPU instead of Multi-stage BO or LaMBO?

### Questions
- At the end of Section 2, it is claimed that "In our setting, the cost at a given stage is a function of the hyperparameters provided to that stage, as well as the inputs provided from the previous stage". Can you provide more technical details or examples to support this sentence? What are the "inputs from the previous stage"? Why and how are these inputs used to model the cost function? Is it shown in any part of Section 3?  

- What's the value of $\epsilon$ used in the experiments? Is the experimental results sensitive to the settings of $\epsilon$, $M$, or $N$?

- In Fig. 3&4, why does EI outperform both EIPS and CArBO? It seems to be counter-intuitive and inconsistent with the results reported in existing works. The y-axis labels of the graphs in the middle column of Figs. 3&4 seem to be wrong. Shouldn't it be the function value instead of the stage cost? The right graphs of Fig. 3&4 each have one plot that the cumulative costs of EI, EIPS, and CarBO are almost the same. Can you provide some analyses on this observation?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
