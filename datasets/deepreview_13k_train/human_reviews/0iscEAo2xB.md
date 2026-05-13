# Comparing Targeting Strategies for Maximizing Social Welfare with Limited Resources

- Decision: Accept
- Scores: 6, 5, 6, 10

## Abstract
\noindent Machine learning is increasingly used to select which individuals receive limited-resource interventions in domains such as human services, education, development, and more. However, it is often not apparent what the right quantity is for models to predict. In particular, policymakers rarely have access to data from a randomized controlled trial (RCT) that would enable accurate estimates of treatment effects -- which individuals would benefit more from the intervention. Observational data is more likely to be available, creating a substantial risk of bias in treatment effect estimates.  Practitioners instead commonly use a technique termed "risk-based targeting" where the model is just used to predict each individual's status quo outcome (an easier, non-causal task). Those with higher predicted risk are offered treatment. There is currently almost no empirical evidence to inform which choices lead to the most effect machine learning-informed targeting strategies in social domains. In this work, we use data from 5 real-world RCTs in a variety of domains to empirically assess such choices. We find that risk-based targeting is almost always inferior to targeting based on even biased estimates of treatment effects. Moreover, these results hold even when the policymaker has strong normative preferences for assisting higher-risk individuals. Our results imply that, despite the widespread use of risk prediction models in applied settings, practitioners may be better off incorporating even weak evidence about heterogeneous causal effects to inform targeting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors compare the utility of targeting interventions based on estimated treatment effects with the utility of targeting based on predicted risk. The former is the method of choice from a utilitarian perspective. But practitioners and policy makers often choose the latter due to its simplicity and in cases where the normative goal is to assist those in greatest need.

### Strengths
(1)

The comparison of these two targeting strategies is an important problem. I'm glad to see that the authors study this question. Despite its significance, there hasn't been much reliable insight so far. I'd love to see more work in this direction!  I'm weighing this strongly in my evaluation.

(2)

The paper is very clearly written. The authors narrate a compelling story about the advantages of targeting based on treatment effect estimates, even if they are biased.

### Weaknesses
(1)

As compelling as the story is, I find the results less than conclusive. Looking at Figure 1, it looks like the confidence intervals around treatment effects are generally strongly overlapping across the entire x-axis of baseline risk. The one exception is the STAR dataset, where the lowest and highest point estimate have barely non-overlapping confidence intervals. As a result, another story consistent with the data is that effects are generally not so heterogeneous as conventional wisdom from the econometrics literature has it. The wide confidence intervals could be due to either a lack of statistical power or a genuine lack of strong correlation between baseline risk and treatment effect heterogeneity. The paper does not sufficiently distinguish between these two possibilities, which weakens the overall argument.

(2)

The results in Figure 1 are actually a fair bit more favorable towards risk-based targeting than the introduction of the paper had me believed. Treatment effects generally increase with risk. Targeting the 80th to 90th percentile of risk generally seems to capture high treatment effects across all datasets. So, another story could be that we should exclude the most extreme values of risk from targeting, but other than that risk-based targeting sort of works. The paper downplays this aspect, which is a missed opportunity to provide a more nuanced view of the tradeoffs between risk-based and treatment-effect based targeting.

(3)

I found it rather confusing to have unnormalized utility values on the y-axis. After all the sample size is rather arbitrary and does not correspond to the population-level utility obtained if the policy maker were to implement the given approach. Along the same lines, I found it difficult to reconcile Figure 1 and Figure 2. See question below.

(4)

It would've been great to include datasets with real world confounding rather than the simulated confounding. My experience is that existing CATE estimation methods don't do very well in non-RCT settings. Might there be an advantage to risk-based targeting in non-RCT data? The current simulation setup, while useful for isolating specific effects, does not fully capture the complexities of real-world data where confounding is often more intricate and less structured.

### Questions
Visually, it seems difficult to reconcile the large difference between, say, Figure 2 top left panel and Figure 1 top left panel. It seems that on the TUP dataset, high risk is close to maximizing treatment effect, the highest values being around percentile 80. However, Figure 2 shows utility 15000 vs 5000 for treatment effect based vs risk vased. Can you explain?

Similarly, treatment effects for NSW seem to be largely constant around 1000, but Figure 2, second row left panel shows a massive advantage for treatment effect based targeting. This seems to be about a factor 7 (1.75 vs 0.25). Where do these large effect differences come from given that the treatment effect curve is essentially constant? None of the treatment effects seem to differ by more than a factor 2.

I tried to figure this out by looking through the code, but I couldn't find code that generated Figure 2. So, I don't actually know where it came from and what it shows. Maybe I missed it. On that note, it would be very helpful to clean up and document the code for the final version. As is, it's very hard to follow.

### Soundness
3

### Presentation
3

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
The paper explores targeting strategies for allocating limited resources to maximize social welfare in areas like
human services, healthcare, and education. Specifically, it compares risk-based targeting, which prioritizes
high-risk individuals, with treatment-effect-based targeting, which uses machine learning models to estimate who
might benefit the most from interventions. Using five real-world randomized controlled trials (RCTs) across diverse
domains, the paper concludes that even biased estimates of treatment effects generally outperform risk-based
targeting. This finding suggests in addition to the widespread reliance on risk-based approaches, policymakers
could incorporate treatment effect estimation when feasible.

### Strengths
Scope: The work’s target is evident in its cross-domain empirical evaluation, making it applicable to multiple policy
areas. The paper introduces innovative use of biased treatment effect estimates to assess targeting efficacy.
Quality: Methodologically, the paper is solid, employing credible RCT data and a robust approach to measuring
treatment effect heterogeneity. The use of doubly robust estimation and varying social welfare functions adds
depth to the analysis.

### Weaknesses
Grammatical errors: there are notable grammatical errors in spelling and following the formatting of ICLR
instructions.

Scope of Treatment Effect Estimates: The reliance on simulated confounding could be more thoroughly justified; real-world application requires consideration of domain-specific biases that could vary across different policy areas
Potential Ethical Implications: Since the work could influence resource allocation in sensitive domains, further discussion on ethical considerations regarding inequality and bias would strengthen its impact and application.

### Questions
Modeling Real-World Confounding: Could the authors expand on how their confounding
approach aligns with real-world biases encountered in observational data? A discussion on potential limitations in modeling confounding factors might aid readers in interpreting results for specific applications.

Ethical Implications: How might the authors' conclusions address ethical concerns,
particularly in terms of balancing fairness (people at the most rish) with effectiveness
when treatment effect targeting benefits some groups more than others? Because the paper concludes that a treatment-effect-based method is preferable to a risk-based method, it raises
the natural question of whether individuals at the highest risk should be prioritized, or if those with the greatest
potential treatment outcome should be targeted instead.

Data Quality: Could the authors provide more information on the reliability and source of the
Acupuncture Dataset?

Confidence Interval Estimation: In Equation (5), a biased estimator is used. Could the authors
justify why this choice was made? Was it primarily for computational efficiency, or are there
other reasons for using a biased estimator in this context?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper compares ''risk-based targeting'' and ''treatment effect-based targeting'' across five datasets from RCTs in different domains. In risk-based targeting, the planner targets individuals based on their baseline risk, which is the expected outcome in the absence of treatment. This approach, commonly used by practitioners, does not account for causal effects. In contrast, treatment effect-based targeting involves first estimating the Conditional Average Treatment Effect (CATE) and then prioritizing individuals accordingly, often with the help of machine learning. A key concern is that these methods may introduce bias in the presence of unobserved confounding. The paper aims to provide empirically grounded guidance for navigating this tradeoff.

First, the paper investigates the extent to which baseline risk serves as an effective proxy for targeting. To do this, treatment effects are estimated at different levels of baseline risk, revealing a surprisingly complex and not necessarily monotonic relationship between treatment effect and baseline risk. Second, the paper examines the potential additional gains from targeting based on treatment effect. Both utilitarian and Nash welfare are used to compare these mechanisms, showing that targeting based on estimated treatment effect can be up to three times more effective in nearly all cases. This remains true even when confounding is introduced into the CATE estimation and when the policymaker's preference for risk-based targeting is encoded in the social welfare function.

### Strengths
This is an important issue, and I’ve personally never found a clear guideline on how best to approach it. I found the study original and of good quality.

The paper does a commendable job of incorporating datasets from diverse domains. 

It also simulates the impact of unobserved confounders and considers the possibility of policymaker bias toward risk-based targeting.

### Weaknesses
My main concern is the reliability of comparing the estimated welfare from risk-based versus treatment effect-based targeting. The issue with the latter approach, particularly in resource-scarce settings, is that it first estimates CATE, then selects individuals with the highest estimated CATE given the available budget, and finally estimates the welfare of treating these individuals using the same estimated CATE. Even if the CATE is unbiased, this procedure can lead to severely biased welfare estimates in resource-constrained settings. This is because the selection process introduces a form of 'selection bias' where the individuals chosen for treatment are not a random sample, but rather those with the highest *estimated* treatment effects. This can lead to an overestimation of the true welfare gains, as the estimated CATEs are likely to be noisy, and the highest estimates may not correspond to the highest true effects.

In Figure 1, the paper provides treatment effect estimates for each baseline risk percentile, along with confidence intervals. What exactly are we looking for here? If the goal is to rule out a monotonic relationship between baseline risk and treatment effect, none of the figures offer statistically significant evidence to support this. The confidence intervals are quite wide, and the point estimates do not show a clear monotonic trend in any of the datasets. It's unclear if the observed variations are meaningful or simply due to noise in the estimation process. The lack of statistical significance makes it difficult to draw any strong conclusions from this figure.

I also think the results should intuitively depend on the budget but this is not discussed in the paper. For instance, if the budget is very small, treatment effect-based allocation can be even more effective in exploiting heterogeneity. Conversely, if the budget is very large, the advantage of treatment effect-based targeting might diminish as most individuals can be treated anyway. The paper should explore how the relative budget size impacts the performance of the two targeting mechanisms. 

Overall, the writing is strong. I noticed the following minor typos: page 2 (potentially-based -> potentially-biased), page 4 (policy -> policy), page 5, second equation, page 7, Equation 4.5 is referenced which does not exist

### Questions
Feel free to further discuss the first two weaknesses mentioned above.

I have seen papers, such as [1], that discuss the complexities of estimating allocation welfare under budget constraints. The issue is that these constraints introduce dependencies between individual estimations, complicating the evaluation process. How is this relevant to your setting?

Shouldn't the results also depend on how many individuals are treated in each scenario? My intuition (supported by studies like [2]) suggests that the relative budget plays a significant role in determining which type of allocation mechanism is optimal.

Since you studied a wide range of settings, did you find any recommendations that vary across these contexts? For instance, are there conditions under which risk-based targeting performs better?

Could you elaborate on the choice of outcome of interest in the TUP dataset? It seems there’s an implicit assumption that individuals who show a larger increase in expenditure are more deserving of intervention. Why should this be the case? In contrast, a risk-based approach might assume that those who would have lower expenditures in the absence of interventions are more deserving. Could this actually be a more appropriate assumption?

[1] Improved Policy Evaluation for Randomized Trials of Algorithmic Resource Allocation
[2] Allocation Requires Prediction Only if Inequality Is Low

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper studies a common risk-based approach to treatment allocation applied to a diverse range of treatments with randomized controlled trial data available. The authors find that allocating treatment according to risk (ie, bad outcomes under the no-treat baseline) produces worse outcomes than allocating according to conditional average treatment effect estimates, even when CATEs are biased or the decision maker has a preference for treating high-risk individuals.

### Strengths
This is a simple, well-executed paper making a very important point. As the authors note, most algorithmic decision making approaches are based on risk or some manipulation of risk in pursuit of fairness goals. This paper demonstrates the problem with that approach across a wide range of interventions.

The authors anticipate the key criticisms of the policy based approach (that RCT data is hard to find and so CATEs may be biased, and that equity preferences might provide a non-utilitarian reason to prefer risk-based targeting), and provide compelling evidence that even under significant confounding or equity preferences one should still prefer allocations based on CATEs.

### Weaknesses
The weakest part of this paper is probably the discussion of Fig 1. The authors cite a "unique trend for each dataset" (in CATE conditional on risk score) as evidence that the risk-based policy is flawed. Visually, to me, the trends look pretty similar: they look like there is basically no relationship between CATE and risk for most RCTs studied. This is still evidence for the risk-based policy being flawed (so it doesn't invalidate the claim being made), but I think it's a more accurate way to describe the results. I think Fig 2 is more compelling than Fig 1 anyway, so it probably make sense to lead with that result for the most impactful paper.

### Questions
Fig. 2 is great, almost telling the story of the paper without the audience needing to read anything else. What would make it even better is replacing "Percentage of data removed" with something like "Higher values mean more confounding in CATE estimates". Currently readers have to read the methodology to understand the x axis, but a better label would mean they could understand the x axis without knowing exactly how the confounding was introduced, and read the methodology if they wanted more details.

### Soundness
4

### Presentation
4

### Contribution
4
