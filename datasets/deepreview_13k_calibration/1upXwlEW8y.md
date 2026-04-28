# Prompt Optimization with Logged Bandit Data

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 3, 8, 8

## Abstract
We study how to use naturally available user feedback, such as clicks, to optimize large language model (LLM) pipelines for generating personalized sentences using prompts. Naive approaches, which estimate the policy gradient in the prompt space, suffer either from variance caused by the large action space of prompts or bias caused by inaccurate reward predictions. To circumvent these challenges, we propose *Direct Sentence Off-policy gradient* (DSO), which estimates the policy gradient by leveraging similarity among generated sentences, substantially reducing variance while suppressing the bias. Empirical results on our newly established suite of benchmarks, called *OfflinePrompts*, demonstrate the effectiveness of the proposed approach in generating personalized descriptions for movie recommendations, particularly when the number of candidate prompts is large.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a new policy gradient-based prompt optimization. The goal is to learn a policy that is able to generate prompts with good responses (as in good rewards). This paper proposed a new DSO that is better than the traditional policy gradient and IS-based method. Some experimental results provided by this paper show that the new method is able to outperform others.

### Strengths
1. The idea of learning a policy to generate good prompts is new to me.
2. The proposed method clearly addressed the weakness of IS.

### Weaknesses
1. The experimental session is the major weakness of this paper. This paper only contains a synthetic experiment and a single model experiment on a single dataset witha  simulated reward function. Experimental results on more datasets and models will make the paper more convincing.

2. The following work should be discussed in the related work since they study prompt optimization with human feedback by learning a reward function and hence related.

https://arxiv.org/abs/2402.00396
https://arxiv.org/abs/2405.17346

An similar line of work on prompt optimization should also be discussed:

https://arxiv.org/abs/2306.03082
https://arxiv.org/abs/2310.02905
https://arxiv.org/pdf/2402.09723

### Questions
1. Can the author describe the main insight for the theorems in this paper? and how they are reflected in the performance of the new approach? There seems to be some disconnection between the theoretical section and empirical verification.

2. How does your method perform in a normal prompt optimization setting? like [1]?


[1] https://arxiv.org/abs/2306.03082

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses prompting policy optimization for large language model (LLM) pipelines by leveraging logged user feedback, such as clicks, to generate personalized sentences. The authors propose a novel method called Direct Sentence Off-policy gradient (DSO), which uses similarity between generated sentences to estimate the policy gradient. While this approach relies on importance sampling, it can reduce the variance of importance weights by treating them in a sentence space rather than the prompt space. Experiments on a synthetic task and an LLM-based task for personalized movie descriptions are shown to claim the effectiveness of the proposed DSO method.

### Strengths
* Using similarity in the generated sentence space to control the bias-variance tradeoff through importance weights is an interesting approach.
* The paper evaluates the proposed method on two types of tasks, synthetic and LLM-based tasks, demonstrating applicability in varied settings.
* Theoretical analysis provides insights into the characteristics of DSO, although some detailed proofs could not be fully verified by the reviewer.

### Weaknesses
 **Lack of clarity in algorithmic steps**:
The specific steps for implementing the algorithm are unclear. It seems that gradient estimation would require sampling from both the prompt policy and the LLM. If this understanding is correct, how many samples would need to be generated per data point? Should this match the $m$  samples used to estimate $\pi_0(\phi(s_i)|x_i)$?

**Notation abuse and lack of clarity in definitions**:
This paper has some notation abuse, which leads to ambiguity. For example, the authors introduce $\pi_\theta(a|x, s)$ or $\pi_\theta(a|x, \phi(s))$ as a conditional distribution over prompts given the generated sentence $s$ in  Section 4 and Appendix D.1. However, this is problematic because $\pi_\theta$ is originally defined as a prompt selection policy and should not depend on $s$, which the LLM generates after selecting $a$. Additionally, while the expressions are somewhat interpretable, there is a lack of consistency in function arguments throughout the paper. For instance, $\pi_\theta(s|x)$ is used without explanation as $\sum_a \pi_\theta(a|x) p_{LLM}(s|x, a)$. To improve clarity, the authors should avoid redefining $\pi_\theta$ with different inputs and instead provide explicit auxiliary definitions where needed, along with a rationale for introducing these conditional probabilities.

**Unpractical setting  in Full-LLM Experiment with MovieLens**:
The LLM-based experiment in Section 7 lacks realistic user personalization. As shown in Figures 10 and 12, the prompt policy reduces user information to a single word (from a set of only 1000 words) before feeding it to the LLM. This simplistic representation raises concerns about whether the Full-LLM experiment setup can effectively capture real-world personalization. Without a richer prompt (e.g., short sentences) to convey nuanced user information, it is unclear if this approach offers any advantage over simply passing user attributes directly to the LLM. Consequently, this setup might be better categorized as a toy task rather than a realistic evaluation of the proposed method's applicability in real-world tasks.

**Concerns regarding the formulation of baseline approaches**:
The problem formulation in this work is novel; however, applying existing methods, particularly the regression approach, seems overly naive for this setup. Since the LLM that generates $s$ is available in this setup, it would be more appropriate for the reward predictor to take $(x, s)$ as input instead of $(x, a)$. Otherwise, the reward predictor would have to learn the LLM's inherent randomness (noise), which seems inefficient. Using $(x, s)$ would allow the reward predictor to avoid this redundancy and better capture the generated sentence features. A Nadaraya-Watson kernel regression (using the same kernel as in DSO) or a neural model like DistilBERT could be employed as the reward predictor to improve adaptability. In connection with the above, in the numerical experiments, using $(x, a)$ as the reward predictor's input in the regression approach may be unfair as a baseline comparison against DSO. DSO leverages (multiple) generated sentence(s) $s’$ for each context $x$ sampled from $\pi_\theta$ and the LLM. Thus, any observed performance gap between DSO and the regression approach may simply be due to this difference in formulation rather than any inherent advantage of DSO.

**Organization of the paper**:
The structure of the paper could be improved. For instance, details of the synthetic experiment setting and Section 4.2 (not cited in the main text) could be moved to the appendix, as these sections may be of lower priority for understanding the main contributions. Shifting these sections would allow more space for core elements like detailed algorithmic steps, problem setup, and full LLM experiment details in the main text.

### Questions
**Figure 6 Interpretation**:
It seems that each bar in Figure 6 represents the results across 5 random seeds. Given the variation across seeds, can we still conclude that the proposed method (DSO) consistently outperforms the regression baseline? The performance between DSO and regression appears similar when accounting for this variability.

**Minor comments**
* Line 391: $\sigma_o$ should be $\sigma_s$?
* Line 989: MSE loss should be $\sum_{i=1}^{n} (r_i - \hat{q}(x_i, a_i))^2$ instead of $\sum_{i=1}^{n} (r_i - \hat{q}(x_i, a_i))$.
* Line 1075: $\nabla_{\theta} \pi_{\theta}$ should be $\nabla_{\theta} \log \pi_{\theta}$?
* In Section 3.1, the classification of "conventional approaches" into "regression-based methods" and "importance sampling (IS)" feels somewhat unclear. It may be more intuitive to categorize these as "reward predictor-based approaches" and "reward predictor-free approaches." This distinction clarifies that IS methods directly use observed rewards, whereas regression-based methods estimate rewards across all actions.

### Soundness
2

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
The paper presents Direct Sentence Off-policy gradient (DSO) for optimizing large language model (LLM) pipelines using logged user feedback such as clicks. DSO addresses the challenges of high variance and bias in policy gradient estimation by leveraging the similarity among generated sentences. The paper provides theoretical analysis on the source of bias and variance reduction of DSO. Experiments on both synthetic environment and a proposed benchmark (OfflinePrompts based on MovieLens-10M) demonstrate the effectiveness of this method. OfflinePrompts is a new benchmark suite,to demonstrate DSO's effectiveness in generating personalized movie descriptions. This is an additional contribution of the paper by providing a practical solution for leveraging naturally logged feedback for prompt policy optimization in language generation tasks.

### Strengths
- The algorithm DSO motivated by utilizing the information behind the sentence embedding is generally sound.
- The theoretically anslysis highlights the benefit of such algorithimic designs by indicating the source of bias and variance of such algorithms.
- The introduction of the OfflinePrompts benchmark suite is a valuable resource for the research community, facilitating further development and testing of off-policy learning methods for language generation

### Weaknesses
The experiments for real-world validation is insufficient. (Indeed, we lack good benchmarks for this task.) How well does the real-world performance align with the score/reward in the simulated environment (OfflinePrompts)? I found Figure 11 in the appendix indicates the positive correlation between the simulated rewards and the click feedback from users. Is there other statistics (such as the accuracy)? I am curious on the click rate improvement using the policy trained by DSO in real-world settings.

How well the sythetic environments represent the real case? I note that there are some gaps between the sythetic environments and the target task. For example, reward is real-valued in synthetic case but it is binary in the real case (click or not); the policy is parameterized by an estimated reward function in the sythetic case.

### Questions
How well the sythetic environments represent the real case? I note that there are some gaps between the sythetic environments and the target task. For example, reward is real-valued in synthetic case but it is binary in the real case (click or not); the policy is parameterized by an estimated reward function in the sythetic case.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces a new method for offline prompt policy learning for LLMs. The main challenge in this setting is the distribution shift between the logged data and the target data. Importance sampling can correct the distribution shift but only at the cost of potentially very high variance. The key idea behind the new method is to exploit similarity relations between sentences to reduce the variance. The bias-variance trade-off of the new method is analyzed theoretically and the method is tested on synthetic data and a LLM movie description task.

### Strengths
* The method is well-motivated and the theoretical analysis supports the desired variance reduction. Intuition for the analysis is provided. 
* Ablations w.r.t to differences in the setting (dataset size, number of actions, reward noise) and w.r.t to the hyperparameters (kernel type, kernel bandwidth) of the method are carried out.
* Plan to open-source a benchmark for offline prompt policy learning

### Weaknesses
 * Figure 6: there are 5 bars for each method. I was/am a bit confused about what the difference between these bars is. For now, I assume these are the results from the 5 random seeds, ordered by performance. But I think it would be good to have a label for this or mention it in the Figure caption. 
* Literature on contextual bandits/kernelized bandits is left out.
* The performance gain (in particular compared to regression) seems much stronger in the synthetic setting than in the full-LLM experiment.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
