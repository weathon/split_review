# The Hidden Cost of Waiting for Accurate Predictions

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Algorithmic predictions are increasingly informing societal resource allocations by identifying individuals for targeting. Policymakers often build these systems with the assumption that by gathering more observations on individuals, they can improve predictive accuracy and, consequently, allocation efficiency. An overlooked yet consequential aspect of prediction-driven allocations is that of timing. The planner has to trade off relying on earlier and potentially noisier predictions to intervene before individuals experience undesirable outcomes, or they may wait to gather more observations to make more precise allocations. We examine this tension using a simple mathematical model, where the planner collects observations on individuals to improve predictions over time. We analyze both the ranking induced by these predictions and optimal resource allocation. We show that though individual prediction accuracy improves over time, counter-intuitively, the average ranking loss can worsen. As a result, the planner's ability to improve social welfare can decline. We identify inequality as a driving factor behind this phenomenon. Our findings provide a nuanced perspective and challenge the conventional wisdom that it is preferable to wait for more accurate predictions to ensure the most efficient allocations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considered resource allocation based on predictions of ranking among individuals. The resources are interventions to prevent individuals from experiencing undesirable outcomes. The authors examined the tension between relying on earlier, possibly noisier predictions to intervene before undesirable outcomes, and waiting to intervene with more precise allocations after gathering more observations.  Through statistical analysis, they showed that individual prediction accuracy could improve with more observations, but the overall ranking performance does not necessarily improve. Moreover, they identified inequality, which is the variance of individual failure probabilities, as a driving factor leading to this counterintuitive behavior. When the planner needs to allocate resource at once, an upper bound on the optimal allocation time was given in the paper. When the planner can allocate resources over time, an algorithm that is provably optimal with respect to the total utility is developed.

### Strengths
1. The paper studied a novel problem of ranking prediction guided resource allocation. The connection between prediction quality and downstream decision performance is an important concept that is not well understood yet. The paper contributed new insights towards the gap. 

2. The paper highlighted interesting tradeoffs between waiting for observations to improve prediction accuracy and losing vulnerable individuals due to waiting. The connection to inherent inequality in the population further enriched these results.  

3. The paper provided rigorous theoretical derivation of all the results. The problem formulation, despite necessary simplification, is general enough to represent broad application contexts.

### Weaknesses
1. The visualizations in Section 5.3 effectively illustrate the theories discussed in the section on sequential allocation. Sections 3 and 4 would benefit from similar empirical support. Incorporating experiments or even basic numerical examples would make the theoretical results more accessible and intuitive. For example, in Section 4, an experimental validation of the derived upper bound on the optimal timing would offer a concrete sense of how these bounds apply in practice. Specifically, the paper could benefit from showing how the derived bound changes with different levels of inequality and budget sizes. This would help to ground the theoretical findings in more practical scenarios.

2. The writing in Sections 3, 4, and 5, while necessarily technical, sometimes read dense. It would be helpful to have clearer explanations of the formulas. In addition, discussing the intuition and the logic of complex derivations behind key theorems and algorithm would also help with the overall flow and clarity. For example, in Section 3, the explanation of why ranking performance does not necessarily improve with individual prediction accuracy could be further elaborated. Similarly, in Section 4, the rationale behind the specific form of the derived upper bound could be made more explicit.

3. Additional explanations could clarify specific aspects of the formulation. For instance, the paper focused on predicting failure probabilities as a basis for resource allocation; however, it might also consider scenarios in which qualification probabilities are predicted instead, and resources are allocated based on those rankings. A discussion on why the study emphasized failure probability as opposed to other potential metrics would be informative. In addition, resource allocation problems often involve various constraints beyond following the ranks among individuals. A discussion of whether such constraints could be incorporated—and if not, why they were excluded—would add to the completeness of the paper. For example, the model assumes a uniform cost for intervention, but in practice, interventions may have varying costs, and this could impact the optimal allocation strategy. The paper should discuss the implications of this assumption and whether it limits the applicability of the results.

### Questions
1. In the derivation of Section 4.1, a measure of inequality is introduced in Definition 4.1. What are the connections, if any, between this measure of inequality and the variance of individual failure probabilities as adopted in Section 3? 

2. In the studied budget allocation setup, are all individuals assumed to require the same budget? If so, can these budgets be viewed as available slots to an opportunity, e.g. the number of students that can be enrolled in a support program, and will assigning different budgets to different individuals affect the presented results?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a stylistic framework for analyzing the utility of intervention strategies when information about individuals is revealed in an online / stepwise manner. In particular, suppose a mechanism designer has access to some intervention budget $B$ over a set of _active_ individuals $\mathcal{A}$. At each time step $t$, each individual $i$ may drop out of the active pool $\mathcal{A}_t$ based on sampling from a Bernoulli distribution with probability $\tilde{p}_i$. The goal of the mechanism designer is to intervene with the high risk individuals (those at high risk of dropping out of the active pool). The challenge is that there is a tradeoff between the available amount of information on each individual (which improves via waiting for more time to pass), and the effectiveness and/or ability to intervene. The latter is impacted by two facts (1) high risk individuals benefitting most from interventions may drop out of the pool earlier; and (2) utility / welfare is higher when intervening at individuals earlier in the time horizon (the authors assume a concave welfare utility modeling function based on individual probabilities $p_i$).

With the general framework setup, the authors tackle three specific settings.
1. Section 3: Bounding the _ranking risk_ for ranking all individuals at each time step based on their probability of dropping out of the active pool.
2. Section 4: When the mechanism designer can intervene upon the $B$ individuals most at risk, but only at one specific point in time, how do we find the optimal point, and how good is it?
3. Section 5: If the mechanism designer can spread out its intervention budget over the time horizon (i.e., intervene at different points in time), how can the optimal strategy be calculated / computed in a tractable manner?

To adress the first point, the authors derive an exact characterization of when the ranking risk improves with information collection (Theorem 3.1). At a high level, this charectizeration shows that the ranking risk improves only if the impact of individuals dropping out of the population is dominated by some function of the information gain, modulo constant factors. 

To address (2), the authors show in Theorem 4.3 that (under the fully effective treatment assumption) the best time to intervene with the entire budget $B$ depends on the total time horizon $T$, the number of individuals, budget, and amount of inequality amongst the individuals (captured by a parameter $G$ for a $G$-decaying distribution). Higher inequality means that the intervention must be applied earlier in order to be most effective. A similar characterization is made for the more general setting where interventions are not 100% effective, but decay with time or depend on the underlying probabilities (Theorem 4.5).

Finally, the authors move to the more complex setting where the budget may be distributed across different points of time $t$. They demonstrate that a naive approach of computing the best policy in the resulting MDP is intractable, but by using particular structure of the problem, can be simplified into searching over a much smaller number of parameters (Theorem 5.1). That is, the optimal intervention will have a specific structural form, whose parameters can be efficiently optimized over (Lemma 5.2).

Lastly, the authors run some experiments on real data from the national eduational longitudinal study. An important takeaway echoed in each of the sections is that it is often beneficial to intervene earlier — with noisier data — than it is to wait until better information is collected.

### Strengths
This paper is extremely well-written, concise and clear, and also makes progress on a very important problem: how does information gain (in terms of improving accuracy of machine learned predictors) trade off with the potential harms / opportunity costs of intervention delays? 

Originality: The stylistic framework seems reminiscent of an over time version of Shirali et al. — who ask about the utility of individual predictions when faced with intervention budgets — but most technical details are different. I believe the online ranking / budgeting setting of this work is quite natural, realistic, and novel.

Clarity: I found the writing precise and clear throughout.

Significance: Although the results are within a stylistic framework, the paper presents another datapoint (in addition to Shirali et al.) supporting the fact that accurate individual level predictions may not or should not be the end-all be-all goal when maximizing the effectiveness of interventions in school, healthcare, etc. These works together are surprisingly counter-intuitive, given that most of the work within the areas of algorithmic fairness and individual level predictions focuses on obtaining accurate predictions. This paper suggests that when viewed from a higher level within the _context_ of decision making and budgeted intervention, the accuracy of individual level predictions may matter far less than one might think. Overall, this work has the potential to guide much future research in the direction of what is actually most impactful within the context of real decision making and intervention systems. Because of this, I believe this work will be highly significant within the next few years.

I also agree with the authors and think there are numerous potential directions that can build upon this work. For example, the fair ranking community has proposed alternatives to simply ranking individuals by their probability of dropping out (e.g., Singh et al. 2021). Whether or not this is the correct thing to do is certainly context dependent, but one can imagine similar characterizations for when information gain may hurt or help when applying interventions in non-welfare maximizing ways (in the interest of fairness).

Singh et al. 2021: Fairness in ranking under uncertainty.

### Weaknesses
The only weaknesses I have are minor, although I have not carefully checked the proofs of the statements. First, I believe that the independence in Assumption 4.2 and line 102 should be discussed more. In particular, imagine the mechanism designer is potentially intervening on a pool of students who are all enrolled in a particular “catch-up” class for low performing students. Since all students have the same teacher, we may expect that their observations may be correlated. For example, if the teacher is really good, then maybe nobody drops out of the pool and no intervention is necessary (the opposite also holds true). The assumption of independent Bernoulli trials for dropout events, while simplifying the analysis, may not accurately reflect real-world scenarios where external factors or shared environments can induce correlations in individual outcomes. This could lead to an underestimation of the variance in dropout rates and potentially flawed intervention strategies. Furthermore, the assumption that intervention effects are independent may also be unrealistic. For instance, if interventions involve group activities or shared resources, the effectiveness of an intervention on one individual could influence the outcomes of others. This interdependency could lead to an overestimation of the overall impact of the intervention strategy. 

Similarly, I think assumption 4.4 can also be discussed in more detail. I understand that this is a technical assumption, but perhaps a note in the appendix about what kind of utilities this can capture, or some common examples, may be useful. I may have missed this somewhere though!

Minor comments
1. Typo: line 807 “particular, Our model”
2. Are there possible citations for line 266-267: “For instance, consider housing vouchers or dropout prevention programs, which have been found to be very effective.”?

### Questions
How should I think about $\gamma$ in Assumption 4.2 and the reliance on $\gamma$ for Theorem 4.3?

### Soundness
4

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
5

### Summary
The authors study the tension between allocating resources based on early, noisy observations versus waiting for additional observations, with the risk of individuals dropping out or "failing." The paper focuses on (i) how ranking loss changes with more observations and (ii) identifying the optimal timing for resource allocation. Section 3 analyses the variation in ranking loss with increasing observations, Section 4 finds the optimal timing for a full-resource allocation, and Section 5 extends this to multi-step, budgeted allocations, introducing an algorithm to compute the optimal over-time allocation.

### Strengths
- Sections 4 and 5 are well organised, covering one-time allocation and then extending this to over-time allocation.
- The experiments in Section 5.3, with visualisations for one-time and over-time allocations offers useful insights on how larger budgets allow earlier allocations.

### Weaknesses
 - Algorithm 1 scales exponentially with $T$; while this improves over naïve iteration, calling it “efficient” might be misleading. The experiments with NELS data used small $T$ values, but $T$ could be large with fine-grained data. Can you discuss practical limitations with larger T values?
- (Minor, organisational) Section 3 could benefit from a restructuring:
   1. Thoerem 3.1 can be moved to just before "approximating ranking risk", with a sentence on how the ranking risk can improve only if the change in population from failure is less than the gain in observations.
  2. The computations for “dynamics of ranking risk” were tedious to parse and could be moved to the appendix in the interest of readability.
- (Minor, related works) The paper does a good job covering related works in the appendix. The authors reference Abebe et al. (2020), which investigates optimal subsidy allocation to minimize failure probability. A useful addition to this line of work is Heidari & Kleinberg [1] and Acharya et al. [2], which examine welfare-optimizing policies under finite time horizons to support low-income groups. Additionally, Azizi et al. [3] (2021) on safe exits for homeless youth could complement Kube et al. (2023), which is already cited.

### Questions
Please address the first bullet point in the weaknesses section.
Also, the runtime for Algorithm 1 is with the general utility class (Sec 4.2); could it be faster with fully effective treatments?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies the problem of resource allocation by considering the trade-off between allocation efficiency and gathering further observations. In particular, the problem is relevant in the context of societal resource allocations, where we are tasked to identify the individuals to intervene (e.g., housing benefits). The authors propose a theoretical framework to study this issue and show that waiting to acquire more observations indeed increases the predictive accuracy, but it also reduces the average ranking loss. Lastly, the authors validate their theoretical findings on a simple semi-synthetic experiment.

### Strengths
The authors study an interesting problem related to allocating resources to maximize the overall utility, by trading-off acquiring information to improve the predictive accuracy and the allocation timing. This topic is not in my main research area, so I cannot comment on the novelty of the approach.

### Weaknesses
The authors tackle this problem from a statistical point of view, rather than the classical ML formalization. Thus, the theoretical framework might be considered too simple and lacking grounding in a realistic scenario. The authors simplify and put many assumptions in place to derive their theorems and bounds, but I believe some of them might not be considered reasonable. Some examples:
- $o^t_i$ is essentially a binary variable. A more realistic assumption would have been to consider $o^t_i$  is a feature vector $x \sim P(X)$, which could incorporate richer information about the individuals. The current binary representation severely limits the model's ability to capture complex dependencies and nuances in real-world data.
- $\tilde{p}$ is an increasing function. While this might hold in some scenarios, it is not universally true. For instance, in educational settings, a student might perform poorly on an early exam due to anxiety, but this does not necessarily imply a higher probability of dropping out. The assumption of a monotonically increasing $\tilde{p}$ needs more justification and examples of real-world scenarios where it holds.
- $\tilde{p}$ are assumed to be known, while in practice we might have access only to an (reasonably good) estimator. This is a significant limitation as the performance of the proposed framework would heavily rely on the accuracy of this estimator, which is often difficult to obtain in practice. The impact of estimation error on the theoretical results is not discussed.

The experiment's description could be expanded. It is not clear what is meant by “failure”, or “inequality” in the context of students. Moreover, the observation model is also not clear. Providing more examples with other realistic datasets might strengthen the overall message. 

Algorithm 1 is not “efficient” in a computational sense. As shown by Lemma 5.2 and Theorem 5.3, the complexity is exponent in time $T$. Even if $T$ is manageable in a real setting (references?), I would not consider it as “efficient” in the broad sense (e.g., polynomial in $T$) and I would suggest the authors rephrase it in the manuscript. 

(Very) Minor nitpicking:
- I would have preferred to see a small “related work” section in the main paper, citing at least the most important/relevant works in the area. It helps position the paper in the literature, and it helps unfamiliar readers to understand the relevance of the contribution.

### Questions
I have no questions for the authors.

### Soundness
2

### Presentation
2

### Contribution
2
