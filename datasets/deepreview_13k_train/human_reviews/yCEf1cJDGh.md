# Truthful Aggregation of LLMs with an Application to Online Advertising

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
The next frontier of online advertising is revenue generation from LLM-generated content. We consider a setting where advertisers aim to influence the responses of an LLM to align with their interests, while platforms seek to maximize advertiser value and ensure user satisfaction. The challenge is that advertisers' preferences generally conflict with those of the user, and advertisers may misreport their preferences. To address this, we introduce MOSAIC, an auction mechanism that ensures that truthful reporting is a dominant strategy for advertisers and that aligns the utility of each advertiser with their contribution to social welfare. Importantly, the mechanism operates without LLM fine-tuning or access to model weights and provably converges to the output of the optimally fine-tuned LLM as computational resources increase. Additionally, it can incorporate contextual information about advertisers,  which significantly improves social welfare. Through experiments with a publicly available LLM, we show that MOSAIC leads to high advertiser value and platform revenue with low computational overhead. While our motivating application is online advertising, our mechanism can be applied in any setting with monetary transfers, making it a general-purpose solution for truthfully aggregating the preferences of self-interested agents over LLM-generated replies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an auction mechanism, MOSAIC, to aggregate the preferences of multiple self-interested advertisers over LLM-generated replies. The authors claim that this mechanism can converge to the outputs of the optimally fine-tuned LLM as computational resources increase, without requiring fine-tuning or access to model weights. The authors also present context-aware versions of MOSAIC, which accelerates convergence and yields high advertiser value and platform revenue. Experiments with a publicly available LLM demonstrate that MOSAIC achieves high advertiser value and platform revenue with minimal computational overhead.

### Strengths
1. The paper is well structured, offering clear explanations of the problems addressed and the key terms used.
2. The proposed mechanism has a firm theoretical grounding.
3. The proposed mechanism seems to demonstrate strong applicability to real-world scenarios, especially in the realm of online advertising with LLM-generated content.

### Weaknesses
1. The novelty of this paper is limited and the scientific contribution seems to be not obvious. The proposed mechanism addresses the problems using conventional approaches. The authors can strengthen the differences between their proposed mechanism and the algorithms used in standard RLHF and the rejection sampling.
2. The experiments are insufficient. There are no comparative analyses between MOSAIC and other mechanisms, which makes it difficult to comprehensively assess its performance. The experiments are restricted to the use of Llama-2-7b-chat-hf, lacking generalizability across different LLMs. It would be nice to compare with other mechanisms mentioned in the related work and evaluate across different LLMs like Llama-3-8B, T5, and Mistral-7B.

### Questions
1. Could the authors provide the specific prompts utilized in the experiments detailed in the paper? Additionally, could you further discuss how different prompts might affect the mechanism's performance?
2. Could the authors extend their experiment to include comparison with other mechanisms from similar studies?
3. Given the paper's claim that the proposed mechanism can operate without LLM fine-tuning or access to model weights, could the authors extend the experiments to include utilization of various closed-source models?

### Soundness
2

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
This paper proposes a mechanism called MOSAIC, that aggregates multiple advertising LLMs (represented by reward functions) and try to find a distribution on replies that maximizes the total rewards of advertisers together with a KL-divergence regularization term on user preference $\pi_{ref}$. MOSAIC takes the reward functions as input, and output a (stochastic) reply to the user.

MOSAIC first samples $M$ candidate replies from arbitrary general and pre-defined distribution $\pi_{gen}$. After this, MOSAIC computes the distribution on replies (regarding the distributions as mechanism allocation) and sample one reply from this distribution as final output. The mechanism payments are computed by Rochet payment (1987). As $M$ tends to infinity, MOSAIC is guaranteed to converge to VCG mechanism.

In experiments, the paper specifies reward functions and $\pi_{gen}$ by LLM distributions and contextually prompting LLMs, respectively. Experiments show that contextual-prompting MOSAIC performs far better than naive MOSAIC with $\pi_{gen} = \pi_{ref}$, with the log-probability of reply close to  optimal distribution.

### Strengths
The author provides  an example throughout the paper, making the model easy to understand. The aggregation of LLMs is an important topic, while the introducing of regularization of user preference is novel. The idea of approximating VCG is also interesting.

### Weaknesses
Major Issues:

* I think the main drawback of this paper is that MOSAIC is only an approximation of VCG mechanism. Moreover, such approximation
n is natural and not challenging to discover and define. Specifically, VCG outputs the distribution on full reply space, while MOSAIC
 first discretizes the full space into finite points and then outputs a distribution on finite points. This operation is simple a
nd do not change the nature of VCG mechanism. Therefore, I believe that the contribution of MOSAIC is not significant.
* The other contributions of this paper, eg, context-aware LLM in Line 237 $\pi_{con}$, and payment offset in Line 335, are case-by-case operations and do not bring significance on the mechanism itself. These ideas are also natural. Besides, the payment contribution is a direct application of Rochet payment (1987). Overall, I believe that the contributions are incremental and limited.
* Regarding the experiments, the authors only compare the contextual-prompting MOSAIC with naive MOSAIC. There is no comparison
 with baselines, thus I cannot evaluate whether the performance of MOSAIC is acceptable from these experiments. A suggestion is
 to compare MOSAIC with VCG mechanism directly when VCG is applicable.

Besides, the presentation needs improvement. For example,

* In Line 419, it appears $\pi_i$. However, $\pi_i$ is only mentioned in Line 146. The definition of $\pi_i$ should be better placed between its first use, i.e., just before Line 419.
* In Section 1.2, the authors mentioned 7 contributions of this paper. However, these contributions are incremental, or only the technical details appeared in this paper.
* In the paragraph of Line 242, the notation $\pi_r$ have never defined before these appearances. I think it should be $\pi_{ref}$.
* In line 313-314, I think that the term $\log (\frac{\pi_{ref}}{\pi_{gen}})$ should be included in the $\exp(\cdot)$.
* In the appendix, the sections are titled with "Details from Section xx", "Omitted Proofs from Section xx". It is conventional to use 'in' instead of 'from'.

### Questions
* In equation (1) in line 152, why do you define KL-divergence of the two distributions and why $\pi_{ref}$ is on the right hand? Will other choices fail?
 * In the paragraph between line 196 and 201, the author says, "*The VCG allocation rule requires calculating the exact optimal solution to the optimization problem, which is intractable for choosing an LLM to maximize Equation (1) and is even difficult for choosing a single optimal sequence. If a sub-optimal solution is chosen, VCG’s strategyproofness is no longer guaranteed (Nisan & Ronen, 2007; 1999; Lehmann et al., 2002).*"
  * In my understanding, choosing an LLM to maximize Equation (1) is equivalent to choosing an LLM that satisfies (2). Since we already have access on $\pi_{ref}$, when $r(x,y) = \sum_i r_i(x,y)$ is upper bounded given $x$, it's feasible to sample from (2) by rejection sampling. Besides, we can also use $\pi_{con}$ replacing $\pi_{ref}$ to decrease variations. In this sense, I do not find the advantage of using MOSAIC rather than using VCG directly. Could you make some clarifications on this concern?
  * Even in the case that $r(x,y)$ is not upper bounded and VCG can not be implemented, it's possible that sub-optimal solutions are chosen and strategyproofness still hold, MOSAIC is exactly one example. Besides, I think MOSAIC will also behave badly in this case because the probability of large value of $r(x, y)$ is small, and it's likely to sample $M$ candidates $y_1,...,y_M$ with all $r(x,y_i)$s are small.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors studied a setting in which the advertisers would like to influence the LLMs to generate their preferred contents and the platform would need to satisfy both advertiser preference and user utilities. The authors proposed an auction mechanism called MOSAIC that enjoys a number of advantages, including ensuring that truthful reporting is a dominant strategy for advertisers. The authors also suggested that the proposed mechanism is equipped with technical feasibility and practicality. To validate their claims, the authors provided both theoretical results and numerical experiments with a publicly available LLM.

### Strengths
- The paper is well written and organized.
- LLM and its application to online advertising, especially the domain of ad auctions, is a novel area to be studied with practical relevance.
- The theoretical results provided appear sound. The authors also clearly stated the difference between their proposed mechanism and previous auction mechanisms such as VCG.
- The numerical experiments (and the motivating example) provide interesting insights.

### Weaknesses
 - I wonder if the authors can provide more explanations for why the ref LLM is not performing as well as the context-aware LLM. I understand that the authors have provided some intuitive explanations in Sections 4, but the ref LLM still appears to be an intuitive choice based on Corollary 4.1. Would it be possible to gain more insights into this difference from a theoretical point of view? Does the authors have any preliminary insights for how to introduce contextual information into the current model? 
- The current framework does not consider a number of constraints that could impact the advertisers' decision-making process, such as each advertiser's budget and/or ROI constraints, or the maximum length of the LLM output. I wonder if the authors can comment on whether their mechanism can incorporate any of the above features.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces MOSAIC, an auction mechanism designed for aggregating advertiser preferences within the outputs of large language models (LLMs), particularly for applications in online advertising. The authors address the challenge of balancing the interests of multiple advertisers with user-centric content by creating a mechanism that incentivizes truthful reporting from advertisers. MOSAIC uses an approach that combines an allocation rule based on importance sampling, allowing it to converge to the optimal output distribution as computational resources increase, without requiring direct model fine-tuning.

### Strengths
The paper introduces MOSAIC which effectively combines the preferences of self-interested advertisers while maintaining user-centric content. This is achieved without requiring direct access to LLM weights, which adds flexibility and broad applicability.

The mechanism ensures that truthful reporting is a dominant strategy for advertisers, thanks to its carefully constructed payment and allocation rules. This strategy-proofness is backed by theoretical proofs.

The design is computationally efficient, using only API access and avoiding expensive fine-tuning.

### Weaknesses
1. There is no real-world testing or application with actual advertiser data to validate the effectiveness of MOSAIC in practical applications.

2. Although MOSAIC is designed to be efficient, it may still face scalability challenges as the number of advertisers or candidate replies grows. An analysis of how the mechanism handles these scenarios under different computational limits would strengthen the paper. Specifically, the paper lacks a detailed analysis of how the computational cost scales with the number of candidate sequences and advertisers, especially in terms of memory usage and runtime. While the mechanism is described as linear, the constants involved could be significant and should be explored. For example, the importance sampling step might become a bottleneck with a large number of candidates.

3. Given that the mechanism optimizes for advertiser rewards and alignment with a reference LLM, there’s a risk of unintentional bias in the final output. The paper does not fully explore the potential for the mechanism to amplify existing biases in the reference LLM or introduce new biases based on the reward functions of the advertisers. A more detailed discussion of how the choice of reference LLM and advertiser reward functions can impact the fairness and diversity of the generated content is needed.

4. MOSAIC relies on advertisers truthfully reporting their preferences and reward functions, yet it does not fully address how misreporting could impact results. While the mechanism is claimed to be strategy-proof, the paper does not discuss the potential for advertisers to engage in sophisticated misreporting strategies, such as colluding to manipulate the outcome or reporting noisy preferences to obscure their true goals. A more thorough analysis of the robustness of the mechanism under different misreporting scenarios is needed.

### Questions
1. The paper claims that MOSAIC’s allocation rule converges to an optimal distribution as computational resources increase. How does the rate of convergence depend on the number of candidate sequences?

2. The allocation rule is based on importance sampling to estimate the probability distribution over sequences. What is the mathematical form of the variance for this estimator?

3. How does the choice of the hyperparameter \tau in front of the KL term quantitatively influence the trade-off between advertiser reward maximization and alignment with the reference LLM?

4. The strategyproofness guarantee hinges on honest reporting by advertisers, but how robust is MOSAIC if advertisers engage in complex forms of gaming or misreporting? 

5.  In scenarios with advertisers holding strongly opposing interests, does MOSAIC risk generating responses that conflict with each other?

### Soundness
2

### Presentation
3

### Contribution
2
