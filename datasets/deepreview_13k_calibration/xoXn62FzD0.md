# Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
A wide range of LLM applications require generating text that conforms to syntactic or semantic constraints. Imposing such constraints nontrivially alters the distribution over sequences, usually making exact sampling intractable. In this work, building on the Language Model Probabilistic Programming framework of Lew et al. (2023), we develop an approach to approximate inference for controlled LLM generation based on sequential Monte Carlo (SMC). Our SMC framework allows us to flexibly incorporate domain- and problem-specific constraints at inference time, and efficiently reallocate computation in light of new information during the course of generation. We demonstrate that our approach improves downstream performance on four challenging domains---Python code generation for data science, text-to-SQL, goal inference, and molecule synthesis. We compare to a number of alternative and ablated approaches, showing that our accuracy improvements are driven by better approximation to the full Bayesian posterior.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Controlling LLM generation to follow logical, syntactical or semantical (soft) constraints is a challenging task. The authors propose to unify controllable generation as sampling from the un-normalized distribution p_{LM}(x) \phi(x) where \phi is an energy function specifying the constraints. The authors propose to leverage sequential Monte Carlo to sample from the desired un-normalized conditional distribution. The authors conducted extensive evaluation of their approach on various downstream tasks with different combinations of constraints and  have demonstrated significant improvement compared to the LLM baseline. One important ablation study has suggested the positive correlation between approximation accuracy and generation quality, motivating for further research on improving the sampling algorithm or the proposal distribution.

### Strengths
This work solves one important problem with some of the widely adopted constrained/structured generation such as Guidance, SGLang and Outlines: that is, these framework achieves control by masking out next-tokens that would violate the constraint, leading to biased sampling (compared to the ground-truth conditional distribution). By leveraging sequential Monte Carlo, the proposed technique is able to approximate unbiased sampling in a relatively practical/scalable way. Empirical evaluations demonstrate strong performance on challenging real-world problems.

### Weaknesses
Some detailed analysis/case study on the sample complexity of SMC would provide more insights, especially how much better SMC is compared to naive importance sampling.

### Questions
What are the other (potentially better) proposal distributions? E.g. LLM fine-tuned/prompted with task-specific supervision.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors apply sequential Monte Carlo to tackle semantic parsing problems involving global constraints. They introduce an enhanced SMC approach, incorporating efficient stochastic approximations of full token-masking distributions and semantic potential to boost performance across five diverse datasets. Additionally, they estimate the KL divergence between each method’s output distribution and the global product-of-experts distribution, demonstrating that the latter is well-calibrated.

### Strengths
The authors propose adapting SMC methods to novel semantic parsing tasks, resulting in notable performance improvements. 

The author conduct a interesting analysis and shows that resampling improves the approximation of the global product-of-experts distribution and approximation quality are consistent with those observed in downstream accuracy evaluation.

### Weaknesses
In terms of experiments: 
- The authors do not emphasize their unique algorithmic contributions within the experiments. The authors could also report the performance of LM with grammar constraint, weight correction and resampling as a regular SMC baseline to further show the effectiveness of semantic potential. Additionally, the authors lack a detailed comparison between their method and the highly relevant SMC method in https://arxiv.org/pdf/2306.03081, and should report it as a baseline, e.g., including without-replacement resampling. 
- For ablation studies, how the number of particles will affect the final performance should be analyzed.

There is no mention of the computation cost, it would be very useful if the authors could evaluate the efficiency of the proposed algorithm.

Also minor writing issues for clarity, the authors should specify what is meant by "some" in lines 41-44 and clarify the specific applications referenced in lines 157-158.

### Questions
See weaknesses. 

Also minor writing issues for clarity, the authors should specify what is meant by "some" in lines 41-44 and clarify the specific applications referenced in lines 157-158.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper concerns inference-time approaches for controlled generation with language models. Building on [Lew et al 2023], the authors develop a method based on sequential Monte-Carlo. The method proceeds segment-by-segment, first extending the segment (e.g. generating a next-token) subject to a token-level score (e.g., arising from a grammar constraint), then reweighting the candidates based on a partial sequence score (e.g., whether the code-so-far has a runtime error), then determining the next set of candidates by resampling candidates based on their weights.

The authors evaluate the method using prompted Llama 3 (base or instruct, varied by task) on 4 tasks. In each task, they construct task-specific token-level and partial-sequence level potentials, and provide an ablation of each of their three proposed components. The authors study the divergence between the target distribution and the distribution induced by running the algorithm, finding that each component leads to a lower KL divergence. Additionally, they provide a nice visualization of the sampling distributions and target distributions for their molecular generation task, and show that samples from their method improve along various dimensions. 

In general the paper is written quite precisely, and several intuitive ideas (e.g., token masking or filtering out a sequence if its code doesn't run) are placed into a probabilistic framework.

### Strengths
Originality
- To my knowledge, the extension of sequential Monte-Carlo to the task settings in the paper, and the specific generation receipe (re-weighting, resampling) are new. However, I am not closely familiar with [Lew et al 2023] or its subsequent papers (which are mentioned several times by the authors). Therefore, my evaluation of novelty may be slightly off. 
- Placing ideas such as token-masking, filtering out partial sequences, and selecting partial sequences to explore next in a probabilistic framework is a nice contribution (with the same caveats in the point above).

Quality
- The experimental evaluation presents a controlled study that ablates each component in the model.
- Derivations and the divergence analysis seem to be of high quality.

Clarity
- Once the reader becomes familiar with the terminology, the paper is written clearly and precisely. 

Significance
- The method could potentially be useful in settings where token-level and partial-sequence level constraint functions are available (e.g., those in the experiments). This has some generality (though could also be viewed as a limiting factor).
- Placing more domains and settings into the probabilistic framing from [Lew et al 2023] helps to further the probabilistic perspective on sequence generation.

### Weaknesses
My primary concerns were on the experimental validation. The paper performs a self-contained, controlled experiment using one Llama 3 model on a set of tasks. As a result, it was unclear how the findings generalize to other models, or how they compare in terms of performance to other methods in the literature.

1) For example, taking the example of DS-1000, the absolute numbers are quite low: the DS-1000 paper reports up to 39.2 performance (with Codex-002) versus 28.5% here (with Llama 3). These are *not* comparable since they use different models, but it would be nice to see how this method performs for models closer to the state of the art. Similarly, Lever [1] reports numbers on Spider from previous work that range from 67.0% to 81.9% [1]. The reason this is important is that the exact experiment setup can lead to different conclusions on the performance of methods, so it was concerning that the absolute numbers seemed low. However, the authors could potentially clarify this.

2) It was also unclear why 10 particles was selected, since in these sampling methods the number of samples can impact performance, and we often want to understand how performance varies with the sampling budget. How does the method vary as the number of particles varies? Is there a sample-and-rerank approach that could outperform this method if it drew a large number of samples?

### Questions
Please see the questions in the Weaknesses above.

### Soundness
3

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
3

### Summary
The paper introduces a Sequential Monte Carlo (SMC) approach for constrained generation in language models to address semantic and syntactic constraints that traditional methods fail to handle effectively. The novel elements include integrating domain-specific constraints via potential functions, weight correction to mitigate the bias from locally greedy decoding, and adaptive resampling that focuses computational effort on promising sequences. The method was tested on four challenging tasks: Python code generation, text-to-SQL translation, goal inference, and molecular synthesis. The experiments compared the SMC-based approach to several baselines and showed that incorporating weight correction and semantic potentials significantly improved performance, while adaptive resampling further enhanced results by reallocating resources to better particles. The total SMC method outperformed the ablated SMC variants on the selected task.

### Strengths
-Good motivation from analysis of weight formulations for importance sampling.

-Benchmarks validate claims that the proposed algorithmic components improve downstream performance. Additionally, authors chose a sensible set of benchmarks.

-Weight correction and resampling seem to be novel components.

### Weaknesses
-The method was not benchmarked against alternative methods. While the ablation study is useful, how does the method compare against other SMC-based techniques such as the ones cited in the related works section that are particularly relevant to this work? E.g. comparisons against the method in Lew et al. and Zhao et al. would be beneficial. There are other non-SMC-based methods that could also be benchmarked against.

-Only Llama 3.1 8-B was evaluated. The manuscript would benefit from benchmarks on additional LLMs to see if results are consistent across similar sized LLMs. I would be curious to see if the benefits are as substantial on larger models, but I understand the authors may have limited computational resources for such analyses.

-There is a lack of theoretical grounding as to the benefits of the components. E.g., a theorem rigorously showing the reduction in KL-Divergence shown in Figure 2 would strengthen the manuscript.

-Notation can be difficult to follow at times. Exposition can be a bit drawn out in certain places, e.g. section 2. I appreciate the authors trying to point out the inefficiencies in each component of MC in order to justify their approach, but I think the exposition would benefit from a condensed explanation of, e.g., the computational burdens of IS.

-Is there a difference between the right part of Figure 1 and Table 2? I would suggest the authors keep only one to avoid redundancy.

-Why was the instruct version of Llama 3.1 used for the SQL task but not the others?

### Questions
-Is there a difference between the right part of Figure 1 and Table 2? I would suggest the authors keep only one to avoid redundancy.

-Why was the instruct version of Llama 3.1 used for the SQL task but not the others?

### Soundness
3

### Presentation
3

### Contribution
3
