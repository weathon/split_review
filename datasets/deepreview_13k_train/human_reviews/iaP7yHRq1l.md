# THE ROBUSTNESS OF DIFFERENTIABLE CAUSAL DISCOVERY IN MISSPECIFIED SCENARIOS

- Decision: Accept
- Scores: 5, 6, 8, 3

## Abstract
Causal discovery aims to learn causal relationships between variables from targeted data, making it a fundamental task in machine learning. However, causal discovery algorithms often rely on unverifiable causal assumptions, which are usually difficult to satisfy in real-world data, thereby limiting the broad application of causal discovery in practical scenarios. Inspired by these considerations, this work extensively benchmarks the empirical performance of various mainstream causal discovery algorithms, which assume i.i.d. data, under eight model assumption violations. Our experimental results show that differentiable causal discovery methods exhibit robustness under the metrics of Structural Hamming Distance and Structural Intervention Distance of the inferred graphs in challenging scenarios, except for scale variation. We also provide the theoretical explanations for the performance of differentiable causal discovery methods. Finally, our work aims to comprehensively benchmark the performance of recent differentiable causal discovery methods under model assumption violations, and provide the standard for reasonable evaluation of causal discovery, as well as to further promote its application in real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work aims to empirically study the behavior of causal discovery algorithms, with a particular focus on optimization based methods. The authors approach this problem by generating a set of graph structures using erdos renyi and scale free graph generation algorithms, and then considering a set of scenarios of misspecification with respect to the generated data. These results are compared across a large representative set of causal discovery algorithms. Results are mixed overall, but generally show preferable performance for optimization and additive noise models.

### Strengths
This paper is addressing a very important, and generally understudied, problem within causal discovery. Because causal discovery relies on a set of untestable assumptions in order to provide the accompanying theoretical guarantees on structure recovery (and as a result entailed causal estimands), it's critical to have an understanding of the relative merit of these algorithms under violations of assumptions. The authors do a nice job of compiling a large set of candidate algorithms, and considering multiple misspecification scenarios. The paper also presents a substantial number of empirical results both in the main text and the supplement. While the paper contains little theoretical content, its direction represents work that is valuable to the community, allowing practitioners to reason over the behavior of current state of the art outside of the context of work that is advocating for a specific approach.

### Weaknesses
 * Erdos Renyi and scale free networks are both fairly unrepresentative of the structures encountered in real world settings. It would have been preferable to either have a much wider range of graph generation algorithms, or used a semi-synthetic approach where the structure of known, real world networks, are used and synthetic data drawn using those implied conditional independencies to augment the current results.
* Overall, I would have liked to have seen more discussions on the implications of the findings of the experiments in practice. The authors do a commendable job of trying to assess a number of scenarios, but the accompanying discussion is limited and there, to my reading, isn't a discussion summarizing the findings or broader implications for practice. Including discussion and analysis along these lines would substantially improve the value to the community.
* It isn't clear how significance is being computed here. The simulations appear to only use 10 iterations per setting. There also aren't any uncertainty bounds given. See below for more questions on this front.

### Questions
Following up from above:
* Are the presented results the mean over 10 trials? 
* Is significance being computed? If so how? 
* It seems strange that many algorithms seem to have the same value for SHD and SID in the latent confounder setting. Can the authors provide some intuition for this? 
* The degree of these graphs is fairly limited. Did the authors try denser settings? If so can these results be described as well?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Causal discovery algorithms frequently depend on unverifiable causal assumptions, which are often challenging to fulfill in real-world data. This study conducts an extensive empirical evaluation of the performance of various mainstream causal discovery algorithms across eight types of model assumption violations. The work finds that differentiable causal discovery methods demonstrate unexpected robustness in challenging conditions. Furthermore, they offer theoretical insights into the observed performance of differentiable causal discovery methods.

### Strengths
1. This paper addresses one of the most critical challenges in causal discovery: the applicability of causal discovery methods to real-world data. Overall, the paper is well-structured and clearly written. 

2. The experiments are extensive, covering eight types of model assumption violations, twelve causal discovery methods, and varying graph sizes.

### Weaknesses
1. In the synthetic experiments, each type of model assumption violation is considered in isolation. However, in real-world datasets, multiple issues may arise simultaneously. How do the causal discovery methods perform when these issues are combined, e.g., confounding effects + measurement errors + heterogeneity? 

2. Additionally, if you were to recommend the single most reliable causal discovery method for real-world datasets, what would it be? 

3. Although this paper aims to address real-world problems, no real-world datasets can be found in the study.

### Questions
(See weaknesses above)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a comprehensive study of the performance of various causal discovery algorithms under eight types of model assumption violations. Notably, the differentiable causal discovery algorithm demonstrates the greatest robustness across different metrics. The paper also includes a degree of theoretical discussion regarding the performance of differentiable causal discovery methods.

### Strengths
This paper presents an extensive empirical study of twelve leading causal discovery methods across eight scenarios involving model assumption violations. The benchmark provides strong evidence for the robustness of differentiable DAG learning algorithms.

### Weaknesses
 * The paper does not include experiments on real-world data. Since the focus is on evaluating various DAG learning algorithms under assumption violations, real-world data would be a natural and valuable addition. Including real-data applications could strengthen the study’s relevance.

* Some algorithms are challenging to train and may require longer training times, which could partly explain their strong performance. A comparison of running times across algorithms would help clarify this aspect.

* Including the standard error of each result would improve the analysis by indicating the stability of each algorithm across different datasets.

### Questions
* Recent work [1] has shown that methods like NOTEARS and DAGMA can achieve scale invariance if the correct loss function is applied and optimization reaches the global optimum. In this paper, differentiable causal discovery performs poorly on scaled datasets; however, this recent work [1] suggests that such issues can be addressed. I believe this insight adds valuable perspective on differentiable causal discovery and warrants an appropriate discussion in the paper.



[1] Deng, C., Bello, K., Ravikumar, P. and Aragam, B., 2024. Likelihood-based Differentiable Structure Learning. arXiv preprint arXiv:2410.06163.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The present paper provides an extensive benchmark on causal discovery with a focus on differentiable algorithms in misspecified scenarios. This is an interesting effort to better understand the behavior of these methods from an empirical perspective, as the previous benchmark in similar misspecified settings (Montagna et al., 2023) almost did not cover any of the differentiable methods tested in this paper.

### Strengths
The misspecifications and the differentiable algorithms subject to testing are well chosen, and the experimental setting is clearly explained. Section 4.1.2. provides interesting theoretical explanations about the empirical performance of differentiable-based methods in the case of a few misspecified scenarios.

### Weaknesses
## Main points
1. I don’t understand why the linear vanilla model is defined with Gaussian noise terms, which are notably non-identifiable. This may be an interesting choice in the light that non-standardized SCMs may still be identified in fact by differentiable causal discovery methods, even in these setting - e.g. exploiting equal variance effects, as studied in Peters et al., 2012 (Identifiability of Gaussian structural equation models with equal error variances). Yet, it is limiting that the only linear setting is that with Gaussian noise, due to the very well-known identifiability limitations affecting almost every algorithm in the list (with the exception of PC and GES).
2. An additional, strong limitation of this work, is that it limits the benchmarking to non-standardized data: this is problematic specifically when testing occurs on differentiable-based algorithms, which notoriously degrade their performance when variance does not increase in the causal order. The authors’ experimental design choice, then, undermines most of the conclusion that one might draw from the experimental outcomes: looking at the linear Gaussian experiments (non-identifiable), the competitive performance of differential-based methods is clearly symptomatic that they are using the variance-induced *shortcuts* in non-standardized data (which is not surprising, as the authors seem to be aware given that they cite Reisach et al., 2021 and Ng et al., 2024 as references) (see the discussion on noise ratio in section 4.2.1 to understand what I mean by *shortcuts*). In light of the good performance of differentiable-based methods on vanilla linear data, all the conclusions that one can derive from these experiments boil down to the following question: given a misspecified scenario, does the noise ratio (discussed in section 4.2.1) ensure that the optimal solution for a differentiable based methods is the correct one? But this is not testing these algorithms’ robustness, it is more testing the properties of the misspecified datasets. Hence, conclusions of *counter-intuitive robustness* (L19) of differentiable based methods in the misspecified settings are wrong (in the sense that they are not surprising if the noise ratio allows it, as in the vanilla linear case). Moreover, they are partial, given that benchmarking occurs on a very limited class of SCMs, those with cumulating variance along the causal order, which we know to enable causal discovery with differentiable based methods. Testing should be performed on the class of standardized causal models, to gain meaningful conclusions about robustness.
3. The SHD outcomes of Tables 2 and 3 are odd/off: e.g. in reference to the R2-sortnregress line of table 2, 50 nodes, you have SHD values of 388, 100, 346, 552, 549, 442, … How is this possible? In SHD, each error (edge addition, removal, or direction flip w.r.t. ground truth) counts as one, or counts as two if the direction flip is counted twice (because we have both a false positive and a false negative): in the latter case, for a fully connected graph with 50 nodes and 2 edges per nodes, the maximum achievable SHD is 200. Hence, I believe something fishy is going on with the SHD values proposed in the table (SHD beyond the possible bound appears all over Table 2 and Table 3). Could you explain this?
4. In Table 2 the latent confounding columns SHD values have a weird behavior: it looks like all methods simply output an empty graph, i.e. for ER-2 graphs with 10 nodes, an empty graph gives you SHD 20, for 20 nodes you get SHD 40, and 50 nodes you get SHD 100: these are exactly the values you get for almost any run, which is suspicious, also in the light of results from Montagna et al., 2023, which already tested the nonlinear confounded setting, and whose result disagree with yours (in their paper there is some robustness displayed by some methods under confounded setting, while no algorithms seem to give the results agreeing with what the authors show). Comments on this point are needed.
5. L343: authors say that on nonlinear data differentiable CD achieves optimal (what do you mean by optimal?) or competitive performance, whereas this is very bad assuming that SHD is bounded by the number of edges, which should be the case according to the description of SHD in section 3.4. One example (which generalizes to other nonlinear cases): on the vanilla model, 10 nodes, the differentiable methods achieve SHD around 10, on 20 nodes SHD around 30, on 50 nodes SHD between 70 and 85, which are all very bad. Hence, the analysis of the authors is incorrect.
6. Authors only present pointwise SHD, without any deviation from multiple experiments or confidence interval, which should instead be provided

## Minor points
1. Reading Tables 2 and 3 is hard, as there are many lines packed in a small space, in a small font. Consider moving it to the appendix?
2. In the introduction, I believe that authors are unnecessarily overselling the value of differentiable causal discovery methods, or at least they don’t seem objective: they define differentiable causal discovery a *ground breaking* *advancement* (L47), whereas in my direct and undirect experience (readings) they are not groundbreaking in the sense they don’t perform generally better than traditional methods or many other approaches to causal discovery. Later, they talk about their *transformative potential in the realm of causal inference* (L53), which is also unsupported by evidence, to the best of my knowledge.
3. Again in the introduction, they say that causal sufficiency and absence of measurement error are *generally imperative* (L54) and they are *fundamental prerequisites for guaranteeing validity and reliablility of the causal inference* (L56-57). They are not imperative, nor fundamental prerequisites: these assumptions are not necessary for identifiability, as methods for causal discovery under confounding effects and measurement error exist, as the authors themselves mention. 

   In reference to this and the previous point: using expressions like *immense potential, imperative need, etc.,* makes unnecessarily strong statements, I would advise against it.
4. L134: the citation to Lachapelle, 2019 (GRAN-DAG paper) when introducing identifiability is wrong. They just propose an algorithm and no identifiability statement. I would remove it, the citations coming after are those that are on point.
5. The paper claims that Montagna et al., 2023 misspecifications are limited in scope, yet 6/9 scenarios covered here (e.g. those in the graphs of Figure 1) are covered there.

### Questions
1. Why did the authors limit their theoretical analysis of section 4.2.1 to measurement error and unfaithful datasets? I believe that in the light of the theoretical analysis in Ng, 2024 (Structure Learning with Continuous Optimization: A Sober Look and Beyond), it would be of great interest if this theoretical study was carried over all the scenarios. This is not a criticism to the paper, but a suggestion of what I believe would be a good contribution in connection to this work.
2. L64: the authors say *true mechanisms remain unclear when applied to real data*. This sentence is obscure to me, could they clarify?

### Soundness
1

### Presentation
3

### Contribution
2
