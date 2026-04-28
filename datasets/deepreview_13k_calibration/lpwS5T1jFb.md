# Time Can Invalidate Algorithmic Recourse

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 5, 5, 8

## Abstract
Algorithmic Recourse (AR) aims to provide users with actionable steps to overturn unfavourable decisions made by machine learning predictors.
However, these actions often take time to implement (\eg getting a degree can take years), and their effects may vary as the world evolves.
Thus, it is natural to ask for recourse that remains valid in a dynamic environment.
In this paper, we study the robustness of algorithmic recourse over time by casting the problem through the lens of causality.
We demonstrate theoretically and empirically that (even robust) causal AR methods can fail over time except in the -- unlikely -- case that the world is \textit{stationary}.
Even more critically, unless the world is fully deterministic, \textit{counterfactual} AR cannot be solved optimally.
To account for this, we propose a simple yet effective algorithm for temporal AR that explicitly accounts for time.
Our simulations on synthetic and realistic datasets show how considering time produces more resilient solutions to potential trends in the data distribution.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper raises an interesting point: because it takes time to implement the recourse, the distributions of the features may shift. Thus, in the future, after the recourse has been correctly implemented, the new feature is still possible to get invalidated by the classifier.

To resolve this problem, the paper proposes to estimate the future distribution of the features, and then solve a min-max iterative algorithm to find the recourse (Algorithm 1).

### Strengths
1. The paper studies an interesting phenomenon: the temporal dimension of algorithmic recourse. It is a relevant problem since implementing recourses can take a long time. Thus, we need to have a mechanism to take the time-horizon (in this paper is $\tau$) into the recourse problem.

### Weaknesses
The main downsides of this approach are

1. It requires an estimator $\tilde P(X^t)$. I would argue that in most practical settings, this distribution is never available. If it is available, it could be easily misspecified as well. Specifically, the paper does not address the challenge of estimating the conditional distribution $\tilde P(X^{t + \tau} | X^t = x^t)$ which is crucial for the proposed method. The paper assumes this distribution can be learned, but it is unclear how this would be achieved in real-world scenarios where data is often limited and non-stationary. The reliance on an accurate estimator is a significant limitation that undermines the practical applicability of the proposed approach.

I believe there is a big gap between what the authors think are practical, and what I think are practical. It is extremely unclear to me how I could use the proposed method in a real-world deployment. The problem is complex when time is taken into account, and having access to a stochastic model $\tilde P$ in my opinion is the most difficult barrier. 

2. It omits the feedback loop: the robust recourse proposed in this paper will lead to a time-horizon of interest longer than $\tau$. To see this, suppose that a non-robust recourse recommends the loan applicant to get a Master’s degree. The robust recourse will recommend a larger cost action such as to get a PhD degree. However, getting a PhD degree takes even more time, and one needs to stretch the time horizon of interest longer. Nevertheless, this feedback effect is not taken into account in this paper. The paper assumes that the recourse action is implemented and its effects are fully realized at time $t + \tau$, but in reality, the time it takes to implement the recourse action may vary and could be influenced by the recommended action itself. This creates a feedback loop that is not captured by the current model, potentially leading to inaccurate or suboptimal recourse recommendations.

3. Algorithm 1 is a robust approach where $x$ can take any possible values in the support of $\tilde P(X^{t + \tau} | X^t = x^t)$, which can be really conservative. This can be reflected by the high costs reported in Appendix C. The authors should conduct a multi-objective analysis, for example, by studying the trade-off of cost-validity. The algorithm optimizes for the worst-case scenario, which may lead to overly conservative and costly recourses. A more nuanced approach would consider the probability distribution of future states and explore the trade-off between the cost of the recourse and its likelihood of success. The current approach does not provide a mechanism to balance these competing objectives.

Some minor concerns:

1. Regarding the exposition, the paper constantly switches between the sub-population recourse and the counterfactual recourse, making it a bit hard to follow. It would be better if the authors can separate the two cases and treat them in a clear, explicit manner. This will help the readers to distinguish the characteristics of the two cases.

2. The authors even forget to state that the stochastic process should be stationary in Proposition 3.

3. The last paragraph on page 4: ``However, this does not prevent invalidation if the user implements this updated recourse later on.” I do not fully understand this argument. And on the contrary, I believe that the naive approach seems to work best! With the complexity of the problem, a simple “recompute” with proper recalibration may be the best solution. The authors should (at the very least) benchmark against this naive solution.

4. Should the right-hand side of equation (7) and (8) be smaller than 1? Could the authors please provide explicit conditions for these bounds to be meaningful?

### Questions
I hope the authors can address some of the weaknesses highlighted above

### Soundness
2

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
3

### Summary
This work investigates the temporal robustness of Algorithmic Recourse (AR), focusing on how AR methods often lose validity over time due to non-stationary data environments. The authors propose a time-aware causal recourse approach, "Temporal Sub-population Algorithmic Recourse (T-SAR)," designed to adapt to dynamic conditions by forecasting recourse stability. They theoretically and empirically demonstrate that both conventional and robust AR techniques struggle to maintain relevance over time, especially in non-deterministic environments, where optimal solutions are typically unattainable. The proposed T-SAR method shows promising results in maintaining recourse validity under various temporal trends and uncertainties.

### Strengths
The concept of Temporal Sub-population Algorithmic Recourse (T-SAR) adds a unique dimension by incorporating time-awareness, which is relatively novel in the field of causal AR. The theoretical contributions are well-grounded in causal inference, and the authors provide a robust theoretical framework that explains why existing AR models may fail over time. By addressing the challenges of AR in non-static environments, this work highlights an important area for improvement in AR techniques. The emphasis on time-sensitive solutions could stimulate further research in ensuring AR methods remain effective as conditions change.

### Weaknesses
The explanation of how temporal sensitivity interacts with causality is unclear. For instance, while the paper mentions the impact of time on causal interventions, it doesn’t sufficiently explain how different timing of interventions might lead to varied results, especially in non-stationary environments. This leaves readers uncertain about the long-term implications of time on AR effectiveness, as the dynamic causal effects of time-sensitive actions are only superficially addressed. 
The paper assumes precise trend estimation, which is unrealistic in many real-world applications where trend data is noisy and unreliable. This assumption affects T-SAR’s practical applicability, as trend inaccuracies could lead to degraded performance. Although the paper mentions non-stationary conditions, it lacks a thorough discussion of the limitations that could arise if the trend estimator is flawed.



### Questions
1.	Proposition 1 states that achieving optimal counterfactual recourse depends on zero variance in exogenous factors.  In cases where variance is unavoidable, how significant is the impact on the effectiveness of T-SAR recommendations? Could you quantify this impact and discuss alternative methods to ensure robust recourse.
2.	Proposition 3 claims that optimal recourse remains valid as long as the stochastic process is stationary. However, real-world processes rarely exhibit perfect stationarity. Could you discuss specific non-stationary scenarios where T-SAR might underperform? Are there any adaptive features in T-SAR to account for non-stationary processes, or must stationarity be a prerequisite for its application?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of algorithmic recourse in the time series setting. Previous works on algorithmic recourse neglect the impact of time evolution on the variables. The authors theoretically analyze the validity of original algorithmic recourse in non-stationary and uncertain world and the stability of recourse over time. Based on the theroretical analysis, the authors propose a simple yet effective algorithm to produce the AR that can counteract the time. The experimental results on synthetic datasets and real-world datasets shows that the AR generated by the proposed method (T-SAR) can remain valid across time steps.

### Strengths
This paper investigate an important but not studied problem, that is the influence of time on algorithmic recourse. This paper explore the problem from the pespective of both theory and empirical examinations. Extensive theoretical analysis is sound and comprehensive. The empirical improvement in experiements is significant, showing the effectiveness of the proposed method.

### Weaknesses
1. The presentation of the paper could be further improved. The problem formulation is not clear and kind of vague. I guess the problem is to determine the intervention $\theta$ at time $t$ and implement it at a later time $t+\tau$ instead of determining intervention at $t+\tau$. However, it is not distinguished in the manuscript. And the notation $do(\theta)$ is confusing, because it is not clear that at which time step the intervention $\theta$ is conducted.
2. I think in the field of algorithmic recourse, the key component about label is the classifer $h$. After $h$ is trained, the true label makes no effect on the generation of AR, since the AR is computed to reverse the predicted label instead of true label. I guess it is needed to adjust the statement in the theoretical analysis.

3. I still have mains concerns about Question 3. How to construct the a structural causal model is not clear in this paper. Therefore, the causality constraints on $\theta$ has not been elborated. The Algorithm 1 does not show the \textbf{design} of exploiting the causal structure.

### Questions
1. I think some notations are confusing. For example, in E.q.(9) the $B(\mathbf{x}^t;\tau)$ refers to the future feature after time $\tau$. However, in line 388, the example of $B(\mathbf{x}^t;\tau)$ is not relevant to time interval $\tau$. 
2. I want the authors to explain the sentence "However, this does not prevent invalidation if the user implements this updated
recourse later on." in line 208.
3. I want to know how the causality play the role in the proposed method.
4. Did the authors examine whether the produced recourse is compatible with the causal relationship among variables.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors argue that some features based on which decision are made might change over time and theoretically study the robustness of algorithmic recourse in this context. They find that algorithmic recourse can be invalidated by non-stationary and exogeneous noise over time. Upon their theoretical findings, the paper proposes a novel algorithm that explicitly incorporates time in the recourse computation and empirically shows that the proposed algorithm suggests recourses with higher validity over time.

### Strengths
- the paper is well-written and easy to follow
- the theoretical insights are novel and important for practical applications of algorithmic recourse
- proofs and derivations are complete and correct
- the empirical evaluation demonstrates the advantages of the proposed algorithm incorporating time explicitly

### Weaknesses
 - Def. 1 could be discussed a bit more in detail. It is not immediately clear what $P$ and $Q$ refer to in the definition. Although it is mentioned a bit further below, it would increase the clarity of the paper if $Q$ and $P$ are briefly described in Def. 1.
- Eq. 5: It is unclear how $\theta$ and $\Delta$ are related. Since $\Delta$ denotes a set of interventions, the notation is not intuitive. The authors should describe their relationship in a brief sentence.
- in lines 338-340, the authors write: "The upper bound is also useful for non-linear classifiers $h$ since we can represent their decision function close to a realization $\mathbf{x}^t$ with a local linear approximation." While I agree that non-linear functions can be approximated using a set of linear functions, it is not immediately clear why the upper bound from Theorem 6 should be useful for non-linear approximators in general. Having a set of linear functions approximating some non-linear function requires somehow merging/combining the upper bounds of the linear functions. Doing this is generally non-trivial since each linear function only considers a local subspace; thus, straightforward solutions like taking the $\max$ of all upper bounds would not work in general to obtain a global upper bound, would it?
- Fig. 3: I agree that the uncertainty clearly has a negative effect on validity. However, one cannot directly see the effect of time in this plot. An additional time-specific plot would be beneficial to underline the statement made in Fig. 3.
- Experimental Setup (4.2): A brief discussion on how the structure of the approximate SCM was obtained, as well as on how good the approximations of the structural equations were, would be beneficial.

### Questions
- Def. 4: Is $P(Y^t | \mathbf{X}^t)$ assumed to be stationary here (since it was mentioned that only covariate-shift-like distribution shifts are considered in Sec. 3.1)? Because if so, distinguishing different $h^t$ would not make sense in my opinion.
- line 364: Why could the proposed algorithm not be used for CAR? 
- Fig. 5: Why is the standard deviation so high on Loan for T-SAR?

### Soundness
3

### Presentation
3

### Contribution
3
