# Measuring the Impact of Equal Treatment as Blindness via Distributions of Explanations Disparity

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
Liberal political philosophy advocates for the policy of \emph{equal treatment as blindness}, which seeks to achieve fairness by treating individuals without considering their protected characteristics directly. However, this policy has faced longstanding criticism for perpetuating existing inequalities. In machine learning, this policy can be translated into the concept of \emph{fairness as unawareness}, and be measured using disparate treatment metrics such as Demographic Parity (a.k.a. Statistical Parity). Our analysis reveals that Demographic Parity does not faithfully measure whether individuals are being treated independently of the protected attribute by the model. We introduce the Explanation Disparity metric to measure fairness under \emph{equal treatment as blindness} policy. Our metric evaluates the fairness of predictive models by analyzing the extent to which the protected attribute can be inferred from the distribution of explanation values, specifically using Shapley values. The proposed metric tests for statistical independence of the explanation distributions over populations with different protected characteristics. We show the theoretical properties of "Explanation Disparity" and devise an equal treatment inspector based on the AUC of a Classifier Two-Sample Test. We experiment with synthetic and natural data to demonstrate and compare the notion with related ones. We release \texttt{explanationspace}, an open-source Python package with methods and tutorials

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses an important issue which is that notions of fairness like DP do not accurately capture if a model is using a protected attribute to make decisions. Thus, this work introduces the Explanation Disparity metric to measure fairness under the equal treatment as blindness policy. This metric evaluates fairness differently, by analyzing if a sensitive attribute can be inferred from distribution of explanation values, S(f(X)) such as the Shapley value. They propose tests to see if the explanation distributions for different groups are different, provide a theoretical analysis of their metric, and perform experiments to demonstrate how their notion compares to other common notions of fairness.

### Strengths
1) The authors raise a very interesting and compelling point that even if DP = 0 (i.e. the model predictions are independent of Z, it it may be the case that that different groups are treated "differently" meaning the model implements a different decision rule for different social groups as illustrated in example 4.1. This necessitates a different notion of fairness that really captures if a model "looks" at the sensitive attribute to make its decision.

2) I enjoy the theoretical analysis and use of simple statistical techniques (two-sample tests) to decide whether or not a model uses sensitive attributes Z to make predictions.

### Weaknesses
1) To me, it is not well motivated why one should want the explanations to be independent of the Z.  Why not any function of the model predictions? Why is picking the model explanations S the right thing to do?

2) While example 4.1 is compelling, are there not more effective ways to better understand how Z plays an impact in the decisions. Instead of testing for if S(f(X)) is independent of Z, why not measure the variance f(X) with respect to Z. The work in this paper

https://proceedings.neurips.cc/paper_files/paper/2023/file/16e4be78e61a3897665fa01504e9f452-Paper-Conference.pdf

I believe addresses a similar issue to what the authors are saying. In this work to better understand if a feature U is important in the process of generating Y, they measure how the variance of Y with respect to U. Similarly why not do something like this to measure whether a function if the variance of f(X) changes as a function of Z. In the example in lines 160-162. Conditional on group (male or female) the variance of the predictions should be very small vs not conditioning on the group. In this case you have effectively identified that Z is used in generating predictions.

3) if the goal is to see if Z is "used" in the decision making process, why not consider counterfactual notions of fairness. Would these values not resolve the issue given in example 4.1?

4) Overall I think the problem that is trying to be addressed here is important however I encourage the authors to look into 

https://proceedings.neurips.cc/paper_files/paper/2023/file/16e4be78e61a3897665fa01504e9f452-Paper-Conference.pdf

and other works on counterfactual fairness and compare their method with these. I would be willing to raise my score if these concerns/questions are addressed effectively.

### Questions
Line 56 - 57: "We show that DP may indicate fairness, even when groups are being treated..."
- What do you mean indicate fairness? DP is a measure of fairness so if DP = 0, its fair if ones uses the definition of DP to define fairness. 
- What do you mean by "when the groups are being treated differently by the model? Do you mean DP is not 0? In that case how could DP indicate fairness if DP is not 0? I am not sure what this sentence is trying to say and I would appreciate if the authors could elaborate on this

Could the authors explain why example 4.2 is compelling and interesting? I understand what is happening but I am not sure what this implies in the context of algorithmic fairness. As I see it, the input data data depends on the protected feature, yet we don't observe this phenomena when looking at model outputs or explanations. Are you trying to say that this is not good because we would like to be able to measure the dependence between X and Z? Even if we could, how does that help since we can't change the features. From a fairness standpoint, is it not more important that our model doesn't discriminate based on Z?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Motivated by the political advocation for fairness, this paper studies demographic parity and investigates whether a protected attribute is indeed safe under demographic parity. The authors achieve this goal by proposing (a) the "explanation disparity" metric that  measures the independence of the protected attribute based on explanation distributions, and (b) the "equal treatment inspector" workflow. Specifically, the formal relationships between demographic parity and explanation disparity are carefully studied, and the conclusions are supported with experiments.

### Strengths
1. This paper is well-motivated, introducing real-world political motivations.

2. The proposal of the idea "explanation distribution" and relevant concepts is indeed novel. Definitions 3.1 and 3.2, although simple, explain the intuition well.

3. Shapley value is a well-known concept for tasks like this and applying it is a credible approach. 

4. This paper is theoretically rigorous and the claims/statements are well-justified with rigor.

### Weaknesses
Methods using Shapley value are usually expensive in terms of computation; the authors also mentioned this in page 32 by comparing it with earlier work. However, I did not find any arguments that this issue does not exist in this framework.

### Questions
Please see the weaknesses part. Please let me know if I missed such argument.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new notion of fairness and methods to evaluate whether it holds.

Definition: We want to evaluate whether a model $f$ makes fair decisions on a dataset $\mathcal{D}_{\mathbf{X}}$. Let $\mathcal{S}(f, \mathbf{x})$ be an *explanation* of the model's output on input $\mathbf{x}$. (They use Shapley values for this explanation.) Then the model achieves "explanation disparity" if $\mathcal{S}(f, \mathbf{X}) \perp Z$ where $Z$ are protected attributes.

In words, ED requires that the model cannot use protected attributes (or anything correlated with protected attributes) to make decisions. They argue that ED is a step towards addressing some of the limitations of demographic parity and equal opportunity:
1. Equal opportunity can use variables that are correlated with protected attributes to make unfair decisions. ED prevents this.
2. Demographic parity can use protected attributes to make decisions. ED prevents this.

They then introduce a method to test whether ED holds: They train a second model to use the explanations to predict the protected attribute. If the model has accuracy significantly above 50% than they conclude ED likely does not hold.

They show that ED is a stronger form of fairness than demographic parity (the proof is very slick, using the completeness axiom of Shapley values).

### Strengths
* The idea to use Shapley values to measure fairness is really elegant and natural. I think this should become a standard fairness metric!

* ED addresses the limitation of equal opportunity, preventing a model from using proxies for protected attributes to entrench biases in the data.

* ED addresses the limitation of demographic parity, preventing a model from using protected attributes to achieve the same statistical outcome.

### Weaknesses
I think the paper should be accepted, but with a substantial rewrite. I previously reviewed this paper and I think the new version obscures the main ideas. In particular:

* The definition is simple to state but first appears on page 5. There is a lot of writing in the first few pages that seems to presuppose that we already know what the definition is, so it's somewhat wasted for the reader to read. I would suggest shortening the introduction and stating the definition by at most the second page, putting the philosophical foundations section into the appendix, and substantially shortening the prior work. You should get to the main section by page at most 2.5.

* I would break up section 4 into two sections. One section should be how you suggest measuring ED. The other section should describe the theoretical properties of your estimator. I struggled with the examples 4.1 and 4.2 because I wasn't sure what I was supposed to take away. You should state them as "There is a setting where ED does blah while other metrics do bleh" so that the takeaway is clear.

* After these changes, you should have lots more space in the main body! And you should fill it with experiments from the appendix! I think the most compelling use-case of your metric is that we have a model making decisions that satisfy equal opportunity or demographic parity but *your method can exactly pinpoint what variables that it's using which are correlated with protected attributes*. I would love to see this experiment in the rebuttal response!

### Questions
Why is your definition called explanation disparity? Doesn't explanation *parity* make more sense?

What's going on in Figure 2? Are you using your classification method to predict whether shapley values are independent of protected attributes (for ED), whether outcomes are independent of protected attributes (demographic parity), etc?

I'm also confused about Figure 3. Could you please explain?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes to assess the fairness  of black box models using their explanations. They first present philosophical contents on fairness and their relationships with mathematical definitions. Then they provide a definition of fairness as a notion of independence between the sensitive attribute and its explanation. In the last part the author present a test based on the AUC. Finally simulations are provided both on a toy model and some data.

### Strengths
Taking into account the explanation to measure fairness of a model makes sense. Equal treatment ensured by measuring if the explanatory ways are the same for all type of  individuals is a way to understand some causal properties. Beyong simple measures of fairness it is definitely a good way to follow.

### Weaknesses
-The first major  drawback is the lack of novelty of the paper : using Shapley values to detect different treatments is done in some papers before. We point out for instance [1] and references therein.
-The second major drawback is that the authors claim to assess the fairness of the model while they only use Shapley values. First we could question the choice of focusing on Shapley values which are usefull to understand but are maybe not suitable to conduct sceond level analysis here. We refer for instance to [2]. Moreover nothing is done to assess whether Shapley values are indeed good representative of the behaviour of the model and comparisons with other explanations should be conducted if we want to take a serious analysis on bias. Finally what is discussed in this paper is more an analysis of some indexes computed from a model than of a model itself. Hence conclusions on the behaviour of the models should be drive with great care, which is not done in this paper. 
- The last major drawback is that contrary to what is stated (ligne 256-257) no statistical test is done in the paper. H0 is stated as an independence property but in a statistical framework which correspond to testing whether  AUC differs from 1/2. So the test should be studied, how to ensure the level of the test and study the power of the test. No theoretical results support the proofs

The paper lacks regorous writting : l322, l 325, l1062, l 1092 ... the authors mix the defintion of the expectancy and the propbability distribution. The writting is very confusing and in some cases wrong since P(Z=1|W) makes only sense (is non zero) only if Z has not continuous denstiy w.r.t Lebesgue measure, hence the mixing between continuous and discrets attribute and values of target function should be treated with care. 

Finally the authors discuss counterfactual fairness and conclude that demographic parity is equivalent to counterfactual fairness. This may not be true, there are some implications but CF is stronger than counterfactual fairness. See for instance in [3].

[1] Escriva, E., Lefrere, T., Martin, M., Aligon, J., Chanson, A., Excoffier, J. B., ... & Monsarrat, P. (2024). Effective data exploration through clustering of local attributive explanations. Information Systems, 102464.
[2] Huang, X., & Marques-Silva, J. (2024). On the failings of Shapley values for explainability. International Journal of Approximate Reasoning, 109112.
[3] De Lara, L., González-Sanz, A., Asher, N., Risser, L., & Loubes, J. M. (2024). Transport-based counterfactual models. Journal of Machine Learning Research, 25(136), 1-59.

### Questions
The authors question "true to the model , true to the data ? " my question is "true to the explainability method ? "

### Soundness
1

### Presentation
2

### Contribution
1
