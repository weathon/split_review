# A General Framework for User-Guided Bayesian Optimization

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
The optimization of expensive-to-evaluate black-box functions is prevalent in various scientific disciplines. Bayesian optimization is an automatic, general and sample-efficient method to solve these problems with minimal knowledge of the underlying function dynamics. However, the ability of Bayesian optimization to incorporate prior knowledge or beliefs about the function at hand in order to accelerate the optimization is limited, which reduces its appeal for knowledgeable practitioners with tight  budgets. To allow domain experts to customize the optimization routine, we propose \mname{}, the first Bayesian-principled framework for incorporating prior beliefs beyond the typical kernel structure, such as the likely location of the optimizer or the optimal value. The generality of \mname{} makes it applicable across different Monte Carlo acquisition functions and types of user beliefs. We empirically demonstrate \mname{}'s ability to substantially accelerate optimization when the prior information is accurate, and to retain approximately default performance when it is misleading.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces ColaBO, which allows domain experts to customize the BO optimization process by integrating prior beliefs, such as information about the probable location of the optimum or the optimal value. Through empirical experiments, it shows that ColaBO speeds up optimization when prior information is accurate and maintains reasonable performance even when the prior knowledge is misleading.

### Strengths
The framework's adaptability and flexibility to incorporate prior knowledge into the optimization process. The method maintains reasonable performance even when the prior knowledge is misleading, demonstrating its robustness in different scenarios.

### Weaknesses
Test functions used to evaluate the proposed framework were quite limited, only a restricted set of test functions was employed.

### Questions
Besides the likely location of the optimizer or the optimal value, what other forms of prior knowledge would generally be useful?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a setting where BO is applied to tackle black-box optimization problems where good prior knowledge is available. However, the conventional GP prior might fall short in effectively incorporating this knowledge. Therefore, the authors propose a new approach to inject it, mainly based on reweighing the prior of the GP with the user-defined prior and deterministic update of the GP posterior. Empirically, two instances of the framework is tested in synthetic and hyperparameter tuning tasks.

### Strengths
1.	The paper considers a novel black-box optimization setting where good prior knowledge exists and proposes a framework to handle this problem.
2.	Based on sampling, this framework is compatible with all Monte Carlo acquisition functions.
3.	With acquisitions to be Log Expected Improvement and Max-Value Entropy Search, the proposed models work well in synthetic and hyperparameter tuning tasks when well-located prior to the optimal location is available, while the drop in performance is not obvious compared to the benchmark models.

### Weaknesses
1.	Although the empirical performance of ColaBO looks promising in the synthetic task and hyperparameter tuning task, the theory developed in the work is limited. Therefore, how the method performs statistically is a concern, given that there are many approximations, such as the Monte Carlo acquisition and the RFF sampling. Specifically, the paper lacks a rigorous analysis of how the re-weighting of the GP prior affects the convergence properties of the Bayesian optimization process. The use of RFF introduces approximation errors, and the paper does not provide any bounds on these errors or how they propagate through the optimization. Furthermore, the Monte Carlo approximation of the acquisition function introduces another layer of approximation, which could lead to suboptimal decisions, and this is not addressed theoretically.
2.	The empirical section can be further enhanced by testing the algorithms on more challenging tasks, for example, higher-dimensional problems. The paper primarily focuses on the low-dimensional tasks, which might not provide a strong basis for demonstrating the algorithm’s performance in realistic problems, where the dimensions might be much higher. The current experiments do not explore the behavior of the algorithm as the dimensionality of the search space increases, which is a critical aspect of evaluating the scalability of the proposed method. Furthermore, the paper does not investigate the impact of the prior's dimensionality on the performance of the algorithm. It is unclear how the method will perform when the prior is defined over a subset of the input dimensions, or when the prior is high-dimensional itself.
3.	The presentation of the work can be improved. Initially, the authors define $\pi(\cdot)$ in Eq. 3 with input from $\mathcal{X}$, but it later becomes $\pi(f)$. Moreover, the notations become messier after Eq. 4, making it more challenging to follow. Also, while rejection sampling seems to be an important step in the model, the way it works is not introduced in the paper. Similar for RFF. The paper lacks a clear explanation of how the rejection sampling is implemented, including the proposal distribution and the acceptance criteria. The description of RFF is also too brief, and it does not provide sufficient details for the reader to understand how the feature mapping is constructed and used in practice. The lack of clarity in these key steps makes it difficult to reproduce the results.
4.	Given the authors’ claim that this is a general framework for BO to incorporate prior, the paper should present concrete examples to demonstrate its generality. For example, the authors could show how the examples in the second paragraph of the introduction section can be solved effectively within the proposed framework. The paper does not provide a clear mapping between the user-defined prior and the specific problem settings. It is not clear how different types of prior knowledge, such as constraints or preferences, can be incorporated into the proposed framework. The paper should provide more concrete examples and guidelines on how to apply the method to different types of prior information.

### Questions
1.	What is the difference between $f^*$ and $f_*$? What is $x_*$?
2.	Is there any reason the authors in favor of rejection sampling compared to other sampling methods? What is the efficiency of using rejection sampling here?
3.	How $\beta$ is determined? 
4.	In Figure 5, even though ColaBO-MES is injected with a poorly located priors, it still performs better than MES, how do the authors interpret that?
5.	The authors show in Eq. 5 that $p(f|D, \pi) \propto \pi(f)p(f|D) $. Does this proportionality still hold in Eq. 6? 
6.	To indicate where the optimum is located within the prior, couldn’t we achieve it by simply defining the prior mean function in GP properly? For instance, assigning higher values to points where the users believe to be good and low values to the rest.
7.	Why do the authors consider log EI instead of EI?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach to user (or prior) guided Bayesian optimization. Unlike previous approaches where the acquisition function was modified to incorporate priors, the paper proposes to sample from a modified posterior of the Gaussian process. This is achieved by combining rejection sampling with the recent line of work on path-wise conditioning.

### Strengths
* The proposed technique is original and interesting. It certainly appears more principled than previous approaches to incorporating expert knowledge.

### Weaknesses
* The mathematical derivation is too informal in some places, affecting clarity. I believe this needs to be improved. For instance, $\pi$ here represents a belief over functions. Then why is Eq. (4) a function that receives a point $x \in \mathcal{X}$? Shouldn't it be a probability distribution over functions? Also, Def 3.1 introduces a conditioning on $\pi$. I found this quite confusing. Is $\pi$ a density? a function? or a random variable?
* There are concerns about the fairness of the experiments. The authors state that "ColaBO and πBO are initialized with the mode of the prior followed by 2 Sobol samples, whereas LogEI and MES are conventionally initialized with D + 1 Sobol samples." Shouldn't logEI and MES also have been initialized on the mode of the prior? If we assume that such prior information is present in user-guided BO methods, it is fair to assume that conventional BO methods also have access to this information. 
* The evaluations are okay but not extensive (especially compared to the piBO paper). I think this is an important point, given that the utility of user-guided BO methods can only be judged empirically on a case-study basis. This connects with my next concern.
* The paper lists a couple of different types of function priors in Section 3.1 but only seems to evaluate one type of such prior. It is, therefore, hard to judge how general this framework is for incorporating prior knowledge. Especially since the users state in the contributions that one can "incorporate arbitrary user knowledge."

* The contribution statement is too general except for item 2. For instance, 1 and 3 can be applied to any user-guided BO method. I expect some more technical details about what this method offers to the field of user-guided BO.
* The derivation of importance sampling in Eq. (10) is unclear. $\pi(f) p(f | D)$ is an unnormalized density, but the integral is taken over it. Then, the equality with Eq. (9), doesn't hold since the expectation is not normalized.
* In Section 3.3, the authors introduce a tempering scheme based on the number of datapoints. Furthermore, they draw connections with generalized Bayesian inference (GBI). I think the authors should make it clear that the connection is very loose. A major characteristic of GBI is to find a statistically principled way to come up with the temperature, which is not the case here. It is particularly misleading as, in the last sentence of Section 3.3, the paper states that tempering is done so in a "principled Bayesian manner."

* Couldn't the name collaborative Bayesian optimization be misleading as to making people to think this method involves multiple users?
* Section 1 first sentence: Please cite classic papers that introduced BO for historical context.
* Figure 9-12: The boundary of the error bands makes it hard to distinguish between the plots. Please consider improving the visibility here.
* Section 2.1 equation: Generally, we aim to minimize the expectation of f or the regret. Saying that we minimize f, in the presence of noise, is too informal.
* Section 2.2 second from the last sentence: I think replacing "standard method" with "classic method" would be better here since we have an influx of more efficient methods.
* Eq (2): Has the "equivalent in distribution" sign been defined anywhere?
* Section 3.1 second paragraph second sentence: the sentence is incomplete.
* References: please consider making the reference more consistent and check the entries. Carl et al 2022b has a typo: joint entropy eearch -> joint entropy search; Jones et al. 2018 is missing the journal entry; Kingma and Welling 2013 was published in ICLR’14.

### Questions
* Given that the authors rely on GP posterior sampling, an obvious thing that could have been tried is Thompson sampling. Have the authors tried to include it?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission provides a unifying framework for encompassing user beliefs in Bayesian Optimization (BO) beyond the usual priors on kernel  hyperparameters. Previous approaches offered to augment BO with expert beliefs $\pi$, like optimum value or location, but mostly focused on doing so at the acquisition function level. Here, the authors propose to integrate this at the surrogate level. Instead of the classical Gaussian Process prior $p(f)$, they introduce a user belief over functions $\pi(f) \propto \frac{p(f|\pi)}{p(f)}$. Thus, $p(f|\pi)$ can be obtained by reweighting samples from $p(f)$ proportionally to their probability of occurring under $\pi(f)$. 

As the user belief is assumed independent of the data-generating mechanism, the resulting posterior $p(f|\mathcal{D},\pi)$ is naturally proportional to the user belief $\pi(f)$ and the likelihood $p(f|\mathcal{D})$. It is therefore non Gaussian for nontrivial user beliefs, an issue circumvented by the authors using a decoupled sampling scheme. Likewise, classical acquisition functions like Expected Improvement or Maximum Entropy Search are not tractable anymore, which led the authors to leverage and tailor their Monte-Carlo version to this specific case. 

In the end, the proposed method, *ColaBO*, is then evaluated on a range of synthetic and real-world benchmarks, and demonstrates convincing performances against its competitors, particularly for misleading user beliefs.
As these benchmarks contain hyperparameter tuning of Deep Learning models, I believe this submission completely falls into the scope of ICLR.

### Strengths
- To the best of my knowledge, this is the first attempt to integrate user prior beliefs directly at the level of the surrogate rather than at the acquisition function level. The approach is novel and encompasses multiple ways for the user to incorporate its expertise: knowledge of function optimum value, optimum location, and preferences.
- I like Figures 1 and 2, they nicely illustrate the benefits of incorporating user beliefs and how this impacts the GP posterior and the acquisition function landscape.

### Weaknesses
I cannot think of any salient weakness in this work. *ColaBO* relies on several approximations due to non-Gaussianity of the posterior and these can probably be made more efficient, as mentioned in the limitations.

### Questions
I do not have questions.

Typos or similar:

- Can you clarify what "DoE" means in "[...] we consider a smaller optimization budget of $10D$ iterations, and initialize all methods that utilize user beliefs with only one DoE sample, that being the mode of the prior".
- Figure 6: The y-axis gives "Accuracy" but performances are decreasing over the BO trial. It probably should be something like 1-accuracy?
- A.3: "by using a sampling an offset direction $\boldsymbol{\epsilon}$ - > "by sampling an offset direction $\boldsymbol{\epsilon}$"?
- Concusion: "[...] or pre-trainedp" -> pre-trained

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
