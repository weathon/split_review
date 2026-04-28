# Towards Assessing and Benchmarking Risk-Return Tradeoff of Off-Policy Evaluation

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 5, 8

## Abstract
\textbf{Off-Policy Evaluation (OPE)} aims to assess the effectiveness of counterfactual policies using only offline logged data and is often used to identify the top-$k$ promising policies for deployment in online A/B tests. Existing evaluation metrics for OPE estimators primarily focus on the ``accuracy'' of OPE or that of downstream policy selection, neglecting risk-return tradeoff in the subsequent online policy deployment. To address this issue, we draw inspiration from portfolio evaluation in finance and develop a new metric, called \textbf{SharpeRatio@k}, which measures the risk-return tradeoff of policy portfolios formed by an OPE estimator under varying online evaluation budgets ($k$). We validate our metric in two example scenarios, demonstrating its ability to effectively distinguish between low-risk and high-risk estimators and to accurately identify the most \textit{efficient} one. Efficiency of an estimator is characterized by its capability to form the most advantageous policy portfolios, maximizing returns while minimizing risks during online deployment, a nuance that existing metrics typically overlook. Employing SharpeRatio@k and SCOPE-RL, we conduct comprehensive benchmarking experiments on various estimators and RL tasks, focusing on their risk-return tradeoff. These experiments offer several interesting directions and suggestions for future OPE research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is concerned with defining an appropriate measure for off-policy evaluation. The authors argue that commonly used metrics such as MSE and rank correlation are insufficient because they fail to properly account for risk/return tradeoffs. To remedy this it’s proposed that ideas from portfolio optimization be used. In particular, the authors propose the use of the Sharpe ratio to measure efficiency. A number of empirical results are provided which demonstrate the properties of the Sharpe ratio @ k metric, and compare it to other metrics such as rank correlation and regret.

### Strengths
This paper tackles an important problem–off policy evaluation is a critical aspect of deployment of RL systems in many real world contexts. The authors' proposal to use ideas from portfolio optimization is an interesting one, and the proposal to use Sharpe @ k is both intuitive and simple. The authors do a nice job of evaluating their work empirically and demonstrating the properties of the proposal.

### Weaknesses
My biggest issue with this paper is that the work is very limited in scope which limits the benefit to the larger community. While the proposal to use ideas from portfolio theory is interesting, the authors focus on a fairly simple definition and don't describe the properties and behavior of the proposed approach theoretically. It would be useful if the authors described the proposal in slightly more generality. For example, are there rank-based analogs of the current approach? It would also be useful if there was a full discussion of the necessary assumptions/conditions for Sharpe@k to be applicable in a real world setting. It would also be useful if the authors highlighted cases where current metrics could be preferable. In general, it would seem that the appropriateness of a given evaluation metric is entirely task dependent, a discussion of this could be useful.

### Questions
It would be useful if the authors could give a description of the settings in which one would prefer Sharpe@k generally. Also, would be useful if the authors could characterize the necessary assumptions on the reward distributions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the risk-return tradeoff between different OPE evaluations. Existing methods evaluate the superiority of an OPE estimator via various “accuracy” measures. However, the paper argues that merely looking at the accuracy may not be sufficient as two OPEs with similar accuracies may have different risk implications in practice. 

To fix this issue, the paper proposes to use concepts from portfolio evaluation in finance and develops a new metric called SharpeRatio@k. This metric helps distinguish between conservative and high-stakes OPE estimators. The key idea behind this is to regard the set of top-k candidate policies selected by an OPE estimator as its “policy portfolio”. The paper constructs a policy portfolio that is “efficient”, i,e, it contains policies that improve the performance of behavior policy without including poorly performing policies. Finally, the paper evaluates typical OPE estimators using the proposed metric using a number of continuous control benchmarks.

### Strengths
– I think the main strength of the paper lies in identifying how the portfolio evaluation concepts in finance can be applied to evaluation of OPEs. I’m not an expert in finance, and can’t speak to the novelty of the idea, but assuming it is novel, this certainly sounds interesting to me.

– The paper is well-organized, is a pleasure to read and explains difficult concepts well enough. 

– I also really liked the use of toy examples throughout the paper to drive home the key concepts. 

– Experiments section is thorough; it compares several of commonly used OPE estimators and also identifies several directions for future OPE research.

### Weaknesses
– I felt the figures and toy examples could use more explanation. For example, it wasn’t clear in Fig 2 what the red dots are, black dots are and how to interpret the axes. 

– Related work: In the section on “Risk Measures and risk-Return Tradeoff in Statistics and Finance”, the paper discusses the Sharpe,1998 paper in length (relevant for the Sharpe ratio used in current paper). However, there are only two other related works identified in this entire section. I’m not an expert in this domain but I suspect there has to be more prior research done in this space – and if that is true, the existing related work section seems a little thin. 

– Other minor suggestions: 

1.  In the abstract, the sentence “We first demonstrate, …” is a bit too long and unwieldy and hard to understand easily. 

2.  Contributions paragraph talks about “top-k policy deployment” without any prior context on what that means. Difficult to follow.

### Questions
– In description of Fig 2, I found the sentence “X underestimates the performance… Y overestimates ” confusing – I was wondering if it should be the other way around. If the current sentence has to be true, then my understanding of the interpretation is that black policies suffer an underestiation (i.e. even though x-axis value is high, y-axis value is lower than ground truth) and so the top-k ends up picking next best policies. Is this correct or am I missing something? 

– top-k policies are considered in several resource allocation setups where there are limited resources and some index is computed so that resource can be allocated to the top k indexes 
(For e.g. [1] “Restless Bandits: Activity Allocation in Changing World”, P Whittle; [2] https://arxiv.org/abs/2110.02128). Can the method be using for designing robust top-k selection/resource allocation policies in this context? I also wonder how it compares to existing robustness in bandits work such as [3] https://arxiv.org/abs/2107.01689 and whether those ideas can be applied to the OPE evaluation setting discussed in the current paper.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new Off-line policy evaluation technique that account for the risk-return tradeoff as usually done in the financial literature when evaluating a portfolio. 
Namely the papers proposes a new evaluation metric (SharpeRatio@k) that measure the risk/return tradeoff of OPEs.
The paper is complemented by empirical analysis to evaluate the effectiveness of the method.

### Strengths
The paper studies the important problem of offline policy evaluation and propose a risk-aware method for selecting OPE estimators. The idea of incorporating the variance of the estimators seems novel and worth investigating. Moreover the paper is fairly well structured and clearly written.

### Weaknesses
My biggest concern is about the technical contribution of the work. While the idea seems novel it also sound quite natural and simple and bears concern about the actual interest that would spark in the community. Moreover the introduction of Sharpe ratio like measure in OPE it seems poorly motivated by the authors who should try to sell better the motivations for the idea



### Questions
1) Way is it important to consider the std of the estimators in assessing OPEs? In finance, big swings might prompt the activation of risk measures, and thus one usually prefers loosing some performance points in favour of more stable results. Way is this important in OPE?
2) Is there any provable theoretical advantages of using your method compared to others?
3) Seems like $\hat J(\pi; D)$ was never defined explicitly.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new metric for off-policy evaluation, names SharpeRatio@K. This metric measures the risk-return tradeoff and efficiency of policy portfolios formed by an OPE estimator under varying online evaluation budgets (i.e. top-K policies selected by the estimator). Via examples, the paper demonstrates that existing metrics (MSE, regret@1, rank correlation) fail to differentiate policies with different risk-return tradeoffs while the proposed new metric does. The authors evaluated SharpeRatio@K via benchmark experiments using various existing OPE estimators regarding their risk-return tradeoff. The authors also developed open-source software for using the proposed metric.

### Strengths
- Overall the paper has a good clarity and is well-organized. I found the examples on over/under-estimation, conservative / high-stakes estimation to be helpful for understanding the benefit of the proposed metric.
- Given that in practice, OPE is more often used as a screening process for selecting top-K policies to deploy in A/B tests, the risk-to-return ratio can be a useful and meaningful metric for comparing OPE estimators. The proposed metric based on Sharpe Ratio to be natural and easy-to-evaluate.
- The benchmark experiments / open-source software provide good evidence that SharpeRatio@K is capable of measuring the risk-to-return efficiency of various OPE estimators, and facilitate the usage of such metric in future research.

### Weaknesses
The benchmark results show that SharpeRatio@k can sometime diverge significantly from the conventional metrics in terms of estimator selection. Additional discussion should be added on how practitioners may consolidate the insights given by the different metrics evaluated under certain scenarios. Specifically, the paper should address situations where an estimator performs well under SharpeRatio@K but poorly under MSE or regret@1, and vice-versa. It's unclear how a practitioner should weigh these conflicting signals. For example, if an estimator has a high SharpeRatio@K due to low variance but has a high regret@1 because it consistently underestimates the best policy, should it be preferred over an estimator with lower SharpeRatio@K but lower regret@1? The paper needs to provide more guidance on how to interpret these discrepancies and make informed decisions in practice. Furthermore, the current discussion lacks a clear articulation of the trade-offs between risk and return in the context of OPE, and how these trade-offs should be considered when selecting an estimator.

### Questions
- The classic sharpe ratio uses the mean return of the portfolio as the numerator instead of the best policy's return. Is there a particular reason that the best return is used in the proposed metric?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
