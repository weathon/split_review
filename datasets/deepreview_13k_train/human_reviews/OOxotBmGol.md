# Large Language Models to Enhance Bayesian Optimization

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Bayesian optimization (BO) is a powerful approach for optimizing complex and expensive-to-evaluate black-box functions. Its importance is underscored in many applications, notably including hyperparameter tuning, but its efficacy depends on efficiently balancing exploration and exploitation. While there has been substantial progress in BO methods, striking this balance remains a delicate process. In this light, we present \texttt{LLAMBO}, a novel approach that integrates the capabilities of Large Language Models (LLM) within BO. At a high level, we frame the BO problem in natural language, enabling LLMs to iteratively \emph{propose} and \emph{evaluate} promising solutions conditioned on historical evaluations. More specifically, we explore how combining contextual understanding, few-shot learning proficiency, and domain knowledge of LLMs can improve model-based BO. Our findings illustrate that \texttt{LLAMBO} is effective at zero-shot warmstarting, and enhances surrogate modeling and candidate sampling, especially in the early stages of search when observations are sparse. Our approach is performed in context and does not require LLM finetuning. Additionally, it is modular by design, allowing individual components to be integrated into existing BO frameworks, or function cohesively as an end-to-end method. We empirically validate \texttt{LLAMBO}'s efficacy on the problem of hyperparameter tuning, highlighting strong empirical performance across a range of diverse benchmarks, proprietary, and synthetic tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach for enhancing Bayesian optimization using LLMs. The approach targets several sub problems in BO such as

1) Selecting initial points for warm starting. LLMs being effective at transferring knowledge are can produce a more promising initial set when provided with the problem setup.
2) Surrogate modeling, where the LLM is used to provide prediction and uncertainty estimates for a new design provided past observations.
3) For sampling new candidates to observe.
4) Finally all the steps are augmented for an end-to-end BO approach.

Experimental results on benchmark datasets are promising. Traditional BO work have mainly focussed on black box optimization from scratch, and works on transfer learning are relatively recent. As such the work in this paper is interesting and strongly relevant to the BO community.

### Strengths
To summarize, this paper successfully demonstrates the utility of LLMs in Bayesian optimization. The paper makes several strong contributions
- The paper demonstrates the utility of the LLM in all stages of BO from warm starting to candidate selection, and effectively utilizes the power of LLMs in knowledge transfer to novel problems.
- Experimental results show improved performance on several benchmark problems. Experimental evaluation is reasonably extensive including several public and private datasets.

### Weaknesses
An obvious weakness of this method is that it has only been evaluated on relatively simple benchmark datasets. The great utilization of this approach would be to select sophisticated neural architectures for novel datasets. However, it is understandable that this may be out of scope for the current work.

It is not clear why an LLM should have any domain knowledge about hyper-parameter tuning to start with. When provided with past observations as part of the input prompt, it is true that the model may be able to generalize (#). However does the model have any additional knowledge about hyper-parameter tuning as a part of its training data?

Is it obvious that comment (#) is true? What is the mechanism behind the LLM being able to parse numbers and compare them to get a decent understanding of the loss domain?

### Questions
It is not clear why an LLM should have any domain knowledge about hyper-parameter tuning to start with. When provided with past observations as part of the input prompt, it is true that the model may be able to generalize (#). However does the model have any additional knowledge about hyper-parameter tuning as a part of its training data?

Is it obvious that comment (#) is true? What is the mechanism behind the LLM being able to parse numbers and compare them to get a decent understanding of the loss domain?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces LLAMBO, an interesting approach that integrates large language models (LLMs) into Bayesian optimization (BO). The authors highlight the challenges of efficiently balancing exploration and exploitation in BO and propose LLAMBO as a solution to enhance various components of model-based BO. LLAMBO leverages the contextual understanding, few-shot learning proficiency, and domain knowledge of LLMs to improve surrogate modeling, candidate sampling, and zero-shot warm-starting. The authors empirically validate LLAMBO's effectiveness in hyperparameter tuning, demonstrating strong performance across diverse benchmarks.

### Strengths
1. Generally, this paper is well written and easy to follow.
2. This paper has well shown the feasibility of introducing LLM into BO for further performance improvement through extensive empirical experiments.
3. This paper has conducted extensive experiments to show how and why the performance is improved.

### Weaknesses
1. The proposed method may failed to deal with high dimensional optimization problems due to the limited token of LLM.
2. This paper mainly compares with the LLAMBO with standard BO algorithms whereas many neural network-based BO algorithms have been developed recently to improve the modeling of standard BO algorithms, e.g., [R1]. This paper may also compare with it to further support the advantages of using LLM for BO.

### Questions
1. In page 8, could the author explain why a negative alpha will help improve the average regret? Intuitively, a negative alpha indicates that the sampling candidates usually perform no better than the best one when compared with the existing candidates, which therefore indicates that no improvement should be made through a negative alpha.
2. What's the dimension of the empirical experiments that have been conducted in this paper? Any high-dimensional ones?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper devises a method to enhance Bayesian optimization using a large language model.  By employing GPT-3.5, the authors investigate GPT-3.5's abilities to warm-start Bayesian optimization, model a surrogate function, and sample query points, and eventually conduct the entire process of Bayesian optimization.  In this paper various scenarios are conducted using in-context learning and prompt engineering, and some important messages discovered by the authors are delivered.

### Strengths
* It solves an interesting topic in Bayesian optimization or active search.  Many optimization researchers were curious about the topic handled in this work.
* Many questions on how it works and which factor makes it work are answered and discussed.
* Extensive analyses are provided.
* Paper is generally well-written.

### Weaknesses
 * I think this is timely work, but I am not sure that it can be presented at ICLR, which is a conference that focuses on representation *learning*.  This work did not do learning explicitly.  I am leaning towards a positive side, but it should be carefully discussed with authors, reviewers, and area chairs.  I think that this paper is more suitable for a natural language processing conference such as ACL, EMNLP, or others.
* Standard deviation (or confidence interval) is not reported for every experiment.  I think this is an important component for this kind of studies.  If some results are statistically meaningless, the analyses are not much meaningful.
* I am curious about how the authors design prompt templates.  Since I tried similar experiments, I could understand why some sentences are included.  However, the analysis on prompts and prompt designs, and potentially failure cases, should be included in the paper.  For example, if you do not include "Do not recommend values at the minimum or maximum of allowable range, do not recommend rounded values" in the prompt, what happens?

### Questions
* In prompt examples, do colors have some consistent indication?  For example, texts in orange have some meaning?  I think you can make consistency across examples and it can help understand the prompt examples.
* Why is no context for warm-starting Bayesian optimization better than random, sobol, or hcube?  The results of no context should be similar to the random initialization methods.
* In discriminative surrogate modeling, a method of LLAMBO utilizes both Monte Carlo sampling and shuffling of examples, or it only uses the shuffling?
* Could you elaborate how $\alpha$ is used in candidate point sampling?
* Could you explain the details of end-to-end demonstration of LLAMBO?  I think it is missing in the paper including the appendices.
* As I mentioned earlier, I would like to see the design process of prompts.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present the new approach LLAMBO, which integrates large language models into Bayesian optimization for the case of hyperparameter optimization. The integration is done by translating knowledge about the problem, algorithm, and optimization history into natural language prompts. The modular approach comprises a warmstarting component, a candidate sampler, and a surrogate model. Two alternatives for the surrogate model are contrasted: a generative and a discriminative variant. The authors claim strong empirical performance to be shown in experimental evaluations. Each component is evaluated separately, and an evaluation of using all components together for an end-to-end approach in comparison to existing methods is carried out additionally.

### Strengths
Novelty & Significance: To the best of my knowledge, the approach is the first of its kind to integrate LLMs into the process of HPO/BO in this all-encompassing manner and could be interesting for the community to build upon.

Quality: In fact, the authors discuss many very interesting approaches for how to combine LLMs and BO. Eventually, they show that by combining all these approaches, they get a very strong system overall. Although I have some concerns regarding some details, the wealth of ideas in this paper and the corresponding experiments are impressive.

In the limited evaluation, the approach shows very promising results.

Clarity: The paper is written up nicely and illustrated with many figures and plots, making it relatively accessible.

### Weaknesses
### Approach
My main criticism is that the authors used an LLM that models data as a sequence of tokens. However, when passing HPO data to an LLM, they face the problem that this data has no sequential structure (see Section 4.1). They get around by permutating the data and thus even derive some kind of uncertainty. However, this seems flawed to me. The authors mention the SMAC method which is built on a random forest. Although random forests are not great for deriving uncertainties, the bootstrapping of random forests is at least statistically motivated. I missed any good argument as to why non-sequential data should be fed into a sequential model and then applying a hack trying to fix it again.

Furthermore, it is well known that the strength of LLMs is based on good prompts. Therefore, I would actually expect some kind of insights and ablation studies on how to do the prompts for this problem. Reading the exemplary prompt templates, I strongly wonder whether the authors came up with these prompts in their very first trial. 

### Clarity

The paper is very dense and includes many nice results. However, the main paper (without appendix) should still be self-contained. However, the authors decided to move the discussion of related work into the appendix. I oppose that decision and deem it very important to have a discussion of related work in the main body of the paper s.t. readers can very well understand how to situate the paper. As a concrete proposal, I recommend moving the generative surrogate model into the appendix since it does not perform better than the discriminative model anyway.

### Experiments

First of all, all papers using closed-sourced GPT models have an inherent flaw: We know nothing about how these models are trained exactly, e.g., training data. Therefore, we lack any scientific understanding of how to use them. The authors tried to get around this by using some private and artificial datasets, but how does this relate to the training distribution used for the GPT model? We cannot make any real claim regarding meta-data leakage. 

Furthermore, since GPT-3.5 is not publically available and might even be updated from time to time, the chance of reproducibility of these results is more or less not given at all. I strongly recommend using (at least) publicly available LLMs such as Llama 2.
There are many further doubts I will raise as questions below. These might translate to direct weaknesses if not properly answered in the rebuttal. 

Some answers could relate to the use of Bayesmark. This benchmark library includes many rather simple HPO benchmarks, i.e., low-dimensional, continuous spaces and traditional ML models. Given state of the art in HPO, I would not consider these reasonable benchmarks anymore. In fact, quite some of the results in this paper conflict with insights into comparing HPO tools (see questions). Therefore, I suspect that results might look very different, if the authors would have used more challenging benchmarks (e.g, from HPOBench).

There are several further points that diminish the strength of the presented experimental results and undermine soundness:

* All plots use iterations instead of wall-time on the x-axis, which does not allow the reader to draw any conclusions on the overhead incurred through querying the LLM, which might negate any benefits incurred by its inclusion depending on the benchmark.
* No uncertainty is shown in any plot, even though results are averaged over several runs/ seeds.
* Especially in the end-to-end demonstration, the number of iterations chosen is very small, and it would be interesting to see how the curves continue.
* No fully random baselines were provided (warmstarting and end-to-end).
* There are some results that seem contradictory to previously observed behaviors of approaches (see questions)
* Accessibility: Often, only colors indicate which curves belong to which approach, and colors like red and green are mixed.

### Minor Points
* P. 15 (Appendix): 2. Candidate Point Sampler H, is "]" intentional?
* In Appendix E, Figure 16 the description hints to two graphs but only one is shown.
* In Figure 8, all curves start at the same point in iteration 0. This is a bit strange in comparison to the warmstarting, where there are clearly different starts depending on the methods. While this is probably due to all methods using the same warmstarting point, it seems puzzling to not include this at the start of the graph or make it clear from the description.
* In the plots, when regret or performance over time (iterations) is shown, the functions should be step functions since there are no interpolations in-between possible.

### Questions
1. How were the Hyperparameters of LLAMBO selected?
1. How were the hyperparameters of the other optimizers selected?
1. Which versions of the libraries for the other optimizers were used?
1. Which exact version of GPT-3.5 was used?
1. In Figure 7, for three of the four plots, the random approach does not seem to do anything, which seems questionable. Could you elaborate on why this might be the case?
1. Why was the end-to-end variant of LLAMBO not evaluated with its own warmstarting component?
1. In Figure 3, SMAC's random forest surrogate seems to beat the GP-based surrogate model, which based on previously published results seems unlikely given that we talk about a small-dimensional, continuous space. Could you elaborate on why this might be the case?
1. In Figure 8, SMAC seems to do nothing for the first few iterations, which, especially in comparison to the previous evaluation of the surrogates (e.g. vs GP) seems strange, could you elaborate on why this might be the case?
1. The performance of HEBO looks surprisingly bad compared to SMAC based on previously published results, could you elaborate on why this might be the case?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
