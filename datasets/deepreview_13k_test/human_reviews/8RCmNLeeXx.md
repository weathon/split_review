# Forking Paths in Neural Text Generation

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Estimating uncertainty in Large Language Models (LLMs) is important for properly evaluating LLMs, and ensuring safety for users. However, prior approaches to uncertainty estimation focus on the final answer in generated text, ignoring intermediate steps that might dramatically impact the outcome.
    We hypothesize that there exist key \textit{forking tokens}, such that re-sampling the system at those specific tokens, but not others, leads to very different outcomes.
    To test this empirically, we develop a novel approach to representing uncertainty dynamics across individual tokens of text generation, and applying statistical models to test our hypothesis. 
    Our approach is highly flexible: it can be applied to any dataset and any LLM, without fine tuning or accessing model weights.
    We use our method to analyze LLM responses on 7 different tasks across 4 domains,  spanning a wide range of typical use cases. 
    We find many examples of forking tokens, including surprising ones such as %an open parenthesis character `\textit{(}' instead of `\textit{by}', 
    punctuation marks, suggesting that LLMs are often just a single token away from saying something very different.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper poses an intriguing question: are there time steps $t$ that, if altered, would significantly impact the sequence completion $x_{>t}$? The authors find that such points, referred to as "forking tokens" in their work, do indeed exist. Additionally, they propose a method to automatically detect these forking tokens using a change point detection (CPD) model. More specifically, they derive a time series $y_t = \text{Dist}(o_0, o_t)$, where $o_0$ and $o_t$ represent the expected answer distributions when tokens are changed at time steps 0 and $t$, respectively. They then train two models, $p(\tau = t | y)$ and $p(m \geq 1 | y)$, to predict the likelihood of a forking token occurring at time $t$ and the number of forking tokens, respectively. The authors demonstrate several interesting cases of their method across extensive datasets.

### Strengths
1. The research question in this work is compelling because forking tokens are important for understanding model behaviors and steering model generation.  
2. The approach of detecting forking tokens with CPD models is also innovative.

### Weaknesses
The core contribution of this paper is already intriguing, so the following weakness is likely minor.

The method section is somewhat difficult to follow. In Section 2.2, I struggled due to insufficient explanation of the connection between the definition of $o_t$ and the subsequent detection method at the beginning of Sec. 2.2. While the high-level concept in lines 247–259 is more understandable, some details remain unclear. For instance, defining $\tau_{i-1}$ and $\tau_i$ as the start and end of segment $i$ made it difficult to interpret $\tau$ in $p(\tau = t | y)$. It may affect the reproduce of their method.

### Questions
It is also interesting to note that most forking tokens detected are entities. However, certain entities that may be important to humans, such as "June 19, 1972" in Figure 4 (lines 276–277), were not detected by the algorithm. Is there an explanation for this?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes the Forking Tokens Hypothesis, that there exist some tokens the prefix such that changing them will lead to dramatic differences in the suffix. They use this hypothesis to study uncertainty estimation in the model's output sequences. Technical-wise, they use Bayesian change point detection and survival analysis to identify the location and number of forking tokens.

### Strengths
1. The paper formulate a interesting and (I think) novel hypothesis about forking tokens, that there are a few sparse but critical tokens that will determine the trajectory of the generation, and uncertainty estimation should depend on these critical tokens. 
2. The estimation method (finding the critical forking token) seems statistically motivated and sound.

### Weaknesses
1. I think the method section is written in a very unclear way. For example, the Bayesian formulation in line 258 can be better described. The Gibbs sampling step is also very unclear. There seem to be lots of details missing. A related question: why use linear regression for the CPD? The math in the survival analysis part makes sense, but still lacks all the execution details: what is d? and what are the pros and cons of these two approaches? 
2. I agree that the forking theory is interesting, but I think the motivation of the paper is to use it for better uncertainty estimation. but no experiment directly ties these two parts together. It would be great to add an experiment about using the forking tokens to recalibrate the model, and yield higher calibration score. Otherwise, I don't quite buy the connection between forking theory and uncertainty estimation.

### Questions
see the weakness section.

### Soundness
2

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
2

### Summary
This article innovatively proposes to analyze the uncertainty of language model generation by analyzing the intermediate steps of LLM decoding. Around the defined forking tokens hypothesis, the authors have built a pipeline and designed CPD to study the uncertainty behavior of language models in different inference tasks. The experimental results demonstrate some very interesting conclusions and provide a comprehensive discussion on the impact of this method on future work.

### Strengths
* The assumption in this article is quite important, and the pipeline constructed to validate the assumption and the evaluation metrics are very interesting
* The experimental analysis in this article is detailed and comprehensive.
* The assumption in this article is very interesting and significant.

### Weaknesses
The evaluation of the uncertainty of language models designed in this article requires sampling a large number of generated results for different tokens and conducting evaluation analysis. Therefore, the cost of evaluating a single sample is also enormous, which may affect the scalability of this work. However, this does not negate the innovativeness of this work.

### Questions
No question

### Soundness
3

### Presentation
2

### Contribution
3
