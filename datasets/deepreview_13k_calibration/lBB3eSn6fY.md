# Gaussian Mixture Counterfactual Generator

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 5, 8, 8

## Abstract
Generating synthetic control arms is a key challenge in clinical research, particularly in crossover trials where placebo data becomes unavailable after patients switch to active treatment. The absence of placebo data complicates estimating long-term efficacy and safety. To solve this, we propose a Gaussian mixture model that generates counterfactual data without needing control data for training. This method handles time-varying, continuous doses and estimates effects between treatment switchers and an extended placebo group, providing valuable insights for treatment effects, evidence generation, and decision-making.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles a difficulty in learning counterfactual data -- control group data may be missing or scarce. The authors propose a Gaussian mixture counterfactual generator and demonstrate it performance in numerical examples.

### Strengths
Introducing the Gaussian mixture counterfactual generator is relatively clear to the readers.

There are interesting numerical results demonstrating the effectiveness of the proposed method.

### Weaknesses
I have the impression that the methodology is not well motivated. Both the static state analysis and Gaussian mixture model jumped in abruptly. In addition, from equation (3), we do not see a clear dependency of $\mathbf{s}$ on $\mathbf{x}$ and $\mathbf{a}$. However, in Section 4, the dependence appears without discussion.

It is unclear how to find the parameters $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ in Gaussian mixture.

I am not convinced why does the proposed method tackle the difficult situation of scarce or no control group data.


### Questions
Is there a particular reason to consider the static state analysis (SSA) for counterfactual distribution learning? For causal effects, I believe there are many other methods, such as doubly-robust methods, IPTW, marginal structural models.

What is $k$ -- the number of components in Gaussian mixture -- used in experiments? How do you find the parameters in Gaussian mixture?

The kernel matrix in equation (11) is unclear to me.

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
3

### Summary
Creating synthetic control arms is challenging in crossover trials where placebo data is lost after switching to active treatment, complicating long-term efficacy and safety assessments. We propose a Gaussian mixture model that generates counterfactual data without control data, accommodating time-varying doses and comparing treatment switchers to an extended placebo group, aiding treatment evaluation and decision-making.

### Strengths
Completed work: The article is clearly written, and the charts used for the presentation are visually appealing.

Clear motivation: I find the problem setting of the crossover trial is quite novel and worth thinking.

Well-organized structure: The article has a clear structure which separately introduces two key problems in the model section, followed by a detailed explanation of the methods.

Sufficient experiments: The experiments are extensive and thorough, as sufficient support for method.

### Weaknesses
I genuinely believe this is a well-completed work that explores a very important method. However, since I am not an expert in this field, there are certain aspects that I don’t fully understand.

First, from my understanding of causality problems, it’s important to ensure three basic assumptions such as consistency, overlap, and unconfoundedness. These assumptions are crucial to establish causal problem, and I couldn’t find explicit statements or discussions around them in the paper. Further explanation or a discussion on how the proposed method addresses or bypasses these assumptions would be helpful for clarity. Specifically, the paper should clarify how the consistency assumption is met, given the counterfactual nature of the generated data. For the overlap assumption, it would be beneficial to understand how the method ensures that there are sufficient data points in the treatment and control groups to make meaningful comparisons. Lastly, the unconfoundedness assumption, which is critical for causal inference, needs to be explicitly addressed, detailing how the method handles potential confounders that might affect both the treatment assignment and the outcome.

Second, while I believe this work addresses a significant and valuable problem, the paper lacks a clear articulation of the novelty of the proposed method. Explicitly positioning the contributions within the landscape of related methods would make it easier to understand the unique aspects of this approach and its value compared to existing solutions. The paper should clearly differentiate its approach from existing methods for synthetic control generation, such as those based on propensity scores or matrix completion. It would be helpful to see a detailed comparison highlighting the specific limitations of these methods in the context of the crossover trial setting and how the proposed Gaussian mixture model overcomes these limitations. A more thorough discussion of related work would help to establish the unique contribution of this paper.

Third, in Section 4, the authors frequently present conclusions within framed boxes. While this can be visually helpful, it consumes a considerable amount of page space, which could be better utilized. The authors may want to consider presenting these conclusions in a more compact form, such as lemmas or theorems, which would make it easier for readers to follow the logical progression without compromising on readability.


### Questions
In line 161, it states, “Now the problem is to estimate a set of parameters $\mathbb{Q} = [ W, \pi_k, \mu_k, \Sigma_k, \Phi_k]$. However, the paper does not provide a clear explanation of the meaning of $\Phi_k$. Could the authors clarify what this parameter represents and its role within the estimation problem? A brief explanation or reference could help in understanding its role in the proposed model.

In Section 3.3, there are subscripts “cf” and “f” used to label variables $x$. However, it’s unclear what these subscripts signify and how they differ from each other. Could the authors elaborate on the distinctions between “cf” and “f” and provide some context as to why they are used?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper considers causal inference for cross-over trials (and some other types of settings). Cross-over trials are settings in which at some fixed point partway through the trial, the placebo group recieve treatment. Causal inference in these settings is complicated by the fact that in later periods there is no longer a placebo group with which to compare treated outcomes. This renders counterfactual prediction methods like synthetic control (Abadie and Garbanzal 2003) inapplicable. In order to simulate counterfactual no-treatment outcomes in later periods, the authors suggest the use of novel method based on Gaussian mixture models. For each individual, the path for all variables, including the treatment and outcome, are drawn from a Gaussian model that depends on an individual-specific and time-invariant state-vector s. In order to simulate counterfactuals, the researchers propose (implicitly) drawing s from its conditional distribution under a counterfactual path for the treatment variable that is not seen in the data and drawing other variables conditional on this s and the counterfactual treatment path.

 As I understand it, the method is essentially an imputation approach. We do not observe individuals who are never treated in the data, but by imposing a sufficiently restrictive model for the relationship between all variables including treatment, we can impute outcomes under treatment paths that are never observed. This reminds me of other linear factor model approaches to counterfactual imputation, for example https://arxiv.org/abs/2006.07691. The efficacy of such methods will clearly depend on the setting.

### Strengths
I found the paper to be very well-motivated and well-written, and it the approach is mostly well-explained. I think the method is reasonable and the simulation results are encouraging (particularly those in Appendix C). I think this is a common and important problem in empirical work and a particularly difficult one for causal inference. I think there is a good chance that applied researchers will apply this method.

### Weaknesses
The notation $\Psi_0$ at the top of page 4 is never defined. I was also unclear on how the likelihood is specified, presumably this is under an assumption that the noise vector is assumed to be independent standard Gaussian?

One section in which the explanation could be sharpened is 4.1. Personally, I found the manner in which counterfactuals are formulated to be quite counter-intuitive. I would typically think of a counterfactual for some individual in terms of the path of the outcome under a counterfactual path for the treatment but with that individual's static state s, which might be interpreted as unobserved individual characteristics, and other covariates, kept fixed. Here, the counterfactual is modeled as a change in the state that is compatible with the prior factual history of treatment and the counterfactual future treatment path. Now, I think this is a reasonable way to proceed but this could use some more elaboration. In particular, I think it might help to more clearly relate this model to the large literature on linear factor models for causal inference.

I found it rather odd that treatment is modeled as some linear combination of factors with an additive noise term. In fact, treatment is binary in most cases discussed and it can only take one of a small number of paths in the factual data. Some more discussion of this would be helpful. The model as specified seems to imply that the noise term $\eta_a^{(t)}$ is independent of $W_a^{(t)}s$, but if treatment is binary, then the noise term would have to be dependent on $W_a^{(t)}s$ to ensure that the left hand side of equation (2) is either zero or one. This dependence is not accounted for in the model.

In the simulation results in Section 5.1, the average path of the outcomes for untreated individuals is almost completely flat. The imputed no-treatment counterfactual paths are likewise flat on average and this matches the ground-truth in the simulation. This is something of a trivial example: there are no systematic changes in outcomes over time that cannot be attributed to treatment. I found the example in Figure 4 in Appendix C in which there are richer trends at play, much more convincing and personally I would put these in the main body of the paper instead. 

If I understand correctly, the simulation adheres to the modeling assumptions of the authors. I wondered whether their methods would provide a good approximation and thus an effective inference method under alternative models that do not exactly adhere to their specification. Perhaps some kind of dynamic and slightly non-linear model.

### Questions
More a suggestion than a question. Although this may be beyond the scope of the current work. In my view, one thing that makes Abadie's synthetic control method (and related methods) convincing is the availability of placebo tests. What I mean by this is that, in SCM, one can pretend the treatment date was say, a month before the actual date, and impute counterfactual untreated potential outcomes for the treated group over this month. Because the treated group was indeed untreated in this period, these can be compared with the ground-truth, helping to validate (or invalidate as the case may be) the efficacy of the method. It seems like such validation approaches could also be applied in the context of the method suggested here? I think this may help researchers to assess whether their particular empirical setting is suitable for the authors' approach.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Problem: counterfactual data may not exist in the extended phase of a crossover trial, so synthetic control methods cannot be used to assess treatment efficacy with respect to a no-treatment baseline.
Significance: makes it difficult to assess long-term efficacy and safety of treatments in this setting.
Solution: the authors propose a model (the Gaussian Mixture Counterfactual Generator) to generate the synthetic controls.

### Strengths
- a, to my knowledge, novel approach to a real problem.
- technically sound , though perhaps missing important assumptions
- illustrative experiments

### Weaknesses
The main weakness of this paper is the lack of formal assumptions explaining when this method will yield accurate results. From the results presented it seems like the fidelity of the generated controls will depend on how well the model estimates the dose response function, and how well it can extrapolate to the 0 dose condition. At least this seems sensible to me after reviewing the linear relationship in Figure 1 and the non-linear relationship analysis in Figures 2, 5, and 6.

The empirical results could be strengthened by including simulated but realistic placebo models. Perhaps adding toxicity models for dose responses.

### Questions
Can you formalize a condition/assumption that would cover the failure mode illustrated in Figure 5? I think this will be a necessary addition for me to consider this paper for acceptance, and I think it is doable.

Are there realistic placebo models that you could incorporate into your synthetic experiments?

Is your non-linear dose response function a realistic one? Are there other functions like toxicity models that you could add?

In the absence of a formal condition on the dose response and perhaps placebo or 0 dose models, i would also accept a more thorough empirical evaluation. If the answers to the above questions are affirmative, then those experiments could be added, along with varying the number of patients. This would allow practitioners to have a fuller picture of when this approach might be appropriate for their problem.

### Soundness
2

### Presentation
2

### Contribution
2
