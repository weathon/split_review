# Sloth: scaling laws for LLM skills to predict multi-benchmark performance across families

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
Scaling laws for large language models (LLMs) predict model performance based on parameters like size and training data. However, differences in training configurations and data processing across model families lead to significant variations in benchmark performance, making it difficult for a single scaling law to generalize across all LLMs. On the other hand, training family-specific scaling laws requires training models of varying sizes for every family. In this work, we propose Skills Scaling Laws (SSLaws, pronounced as \texttt{Sloth}), a novel scaling law that leverages publicly available benchmark data and assumes LLM performance is driven by low-dimensional latent skills, such as reasoning and instruction following. These latent skills are influenced by computational resources like model size and training tokens but with varying efficiencies across model families. \texttt{Sloth} exploits correlations across benchmarks to provide more accurate and interpretable predictions while alleviating the need to train multiple LLMs per family. We present both theoretical results on parameter identification and empirical evaluations on 12 prominent benchmarks, from Open LLM Leaderboard v1/v2, demonstrating that \texttt{Sloth} predicts LLM performance efficiently and offers insights into scaling behaviors for downstream tasks such as coding and emotional intelligence applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a novel scaling law to predict the performance of various LLM families on multiple benchmarks.
The authors borrow methodologies from Exploratory Factor Analysis to improve a previously proposed scaling law.
Factor Analysis allows the model to find interpretable latent factors to help the scaling model generalize.
Furthermore, a learnable activation function is used instead of the sigmoid, leading to an improved fit.

The experimental results reported in the article show:
 - The proposed scaling law is as performant as previously proposed approaches.
 - The proposed scaling law is able to extract (possibly) explanatory factors for the various benchmark results.

### Strengths
The proposed method is uses an interesting mixture of scaling laws and interpretability to propose an improved benchmark prediction model.  The use of a latent subspace "identifying" key skills to solve task is similar to what was proposed in Ruan et al, but the usage of exploratory factor analysis allows for a more insightful understanding.

### Weaknesses
1) The paper presentation can be sometimes confusing and/or unpolished. There are some terms are used without a proper introduction (e.g. interaction term), thus hindering the overall article. In general, I feel that the overall presentation could be improved.

2) To my knowledge, the model families seems to not be clearly stated in the main paper, they can only be speculated from looking at figure 17 in the appendix. How are models from the leaderboard categorized into a family? Furthermore, where are model size and training token information taken from?  

3) The use of a neural-network to model the activation function σ can lead to overfitting and poor generalization, especially considering the few data used for training (to my understanding it is trained on benchmark evaluations). I would have preferred a more focused experiment on showing if using a trainable activation can lead to a worse generalization.

4) I find the tables, plots, and in general the experiments to be somewhat lacking; In previous work, to show the capabilities of their respective work Ruan et al, and Owen make use of plots, showcasing the extrapolation capabilities of their models (e.g. Figure 4 in Ruan et al). I think that the proposed work would benefit from using more of these visualizations (some are shown in the appendix, but are otherwise not included in the main discussion).

### Questions
1) Why was logistic regression used for Figure 7 instead of the learned activation σ? Is there something that I am missing?
2) In line 137 and 138 you state that "(Ruan et al) is not well-suited for performance prediction from compute" why is that the case? can you expand on this?
3) How are the level curves in Figure 5 computed? Can you give an intuitive explanation?

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
In this paper, the authors propose fitting scaling laws on existing benchmark data for various LLM families, utilizing results from OpenLLM v1 and v2. Unlike prior work on LLM scaling laws, which generally explores scaling across parameters and data, this paper primarily focuses on latent skills, such as reasoning abilities, that can be simultaneously evaluated by multiple benchmarks like GSM8K and MATH. In contrast to previous works on benchmark scaling laws (e.g., Owen, 2024; Ryan et al., 2024), which fit Equation 2.2 using the number of training tokens and parameters, this study introduces a lower-dimensional assumption to reduce the number of parameters required for fitting. The final objective function is presented in Section 3.3. Empirical results indicate that the proposed method, SLOTH, demonstrates improved predictive accuracy in terms of prediction error.

### Strengths
Overall, the paper is well-structured and easy to follow. The authors propose a model mapping s (LLM size) and t (number of training tokens) to benchmark performance. Additionally, they employ several techniques to reduce the model’s parameter count while maintaining flexibility. The experimental results appear promising.

### Weaknesses
I have several concerns:

1. If an LLM’s skill is knowledge-based, I agree that the proposed model would likely offer good predictive accuracy, as such skills depend on training tokens and model size. However, when it comes to reasoning skills (focusing specifically on mathematical reasoning), my experience suggests that these skills heavily rely on post-training factors, such as the extent of computation on reinforcement learning during fine-tuning. Such hidden factors are difficult to capture using the model’s inputs alone, and to my knowledge, these are not commonly reported by open-source models. The model's reliance on only size and training tokens seems insufficient to capture the nuances of reasoning ability, which can be significantly altered by the specific fine-tuning methods and data used, potentially leading to inaccurate predictions for models with similar pre-training but different fine-tuning regimes.

2. It appears that some LLM benchmarks may be contaminated, whether intentionally or not. This raises the question: can we fully trust benchmark values as indicators of skill? The presence of contaminated benchmarks introduces a significant confounding variable, making it difficult to ascertain whether the observed scaling laws truly reflect underlying capabilities or are merely artifacts of data leakage. This issue undermines the reliability of the benchmark data used for fitting the model, potentially leading to spurious correlations and inaccurate predictions.

3. Finally, how can this scaling law be practically applied? Does it offer guidance for pre-training or post-training phases? The paper does not clearly articulate how the proposed scaling law can be used to guide practical decisions in model development. Without specific examples of how the scaling law can inform choices about pre-training data, model size, or post-training fine-tuning strategies, its practical utility remains unclear. It is not evident how the model can help in resource allocation or in predicting the performance of models on tasks beyond the benchmarks used for fitting.

### Questions
See my comments on the weakness

### Soundness
2

### Presentation
3

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
This paper focuses on predicting performance of down-stream tasks across LLM families and benchmarks by leveraging their intrinsic interactive structures. Specifically, this paper applies factor analysis models in Economics to explore low-dimensional latent skills (e.g., reasoning and instruction following) as key predictors of performance. Extensive experiments demonstrate the effectiveness of the proposed model compared with a set of baselines.

### Strengths
1. The idea of adopting factor analysis models in Economics to analyze multi-benchmark performance across model families is intriguing.
2. The authors provide the theoretical justification to consolidate the proposed method.
3. The authors conduct experiments across several downstream tasks to validate the effectiveness of the proposed method.

### Weaknesses
The paper is well-structured and effectively conveys its main points. How to understand and predict multi-benchmark performance is an important problem within the domain of Large Language Models (LLMs) and the authors propose the corresponding method to address this problem. I have the following suggestions to further improve the manuscript of this paper:

1. The authors conduct experiments using only three open-source dense LLMs, showing competitive performance on several benchmarks. Recently, the sparse Mixture-of-Experts (MOE) LLMs have achieved impressive results across various tasks and represent an essential model family in the LLM landscape. The authors should address how the proposed method could be adapted for MoE architectures, given their distinct structural characteristics compared to dense models. Additionally, the authors should perform experiments with sparse MOE LLMs (e.g., Mixtral[1], DeepSeekMoE[2]) to comprehensively assess the predictive abilities of multi-benchmark performance across LLM families.
2. As illustrated in Figure 5, reasoning ability is primarily influenced by model size rather than the number of training tokens. I recommend that the authors discuss how their model might be extended or modified to account for the effects of instruction tuning separately from pre-training. Recent studies, including Skywork-Math [3] and OpenMathInstruct-2 [4], demonstrate a clear scaling law with instruction data, showing that model performance significantly improves as the amount of supervised fine-tuning (SFT) data increases. This finding appears to contradict the observations reported in the current experiments. Therefore, I suggest that the authors address any limitations in their current approach that might explain this discrepancy in findings compared to recent studies on instruction data scaling.

### Questions
1.	Could you involve a broader range of LLMs, specifically sparse MOE LLMs like Mixtra and DeepSeekMoE, to provide a more holistic demonstration of the proposed method’s effectiveness? 
2.	See the second point in the Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel approach to model LLM performance on different benchmarks starting from the number of training tokens and model size. This "scaling law" can be fitted by using existing benchmark results across various LLMs of different families. They assume some of the parameters of the scaling laws are shared across model families, while others are family-specific. Previous work assumed all parameters are either shared or family-specific, which can be respectively too unrestrictive or lead to too many parameters, and thus impossible to fit with limited observation data. Moreover, in contrast to previous work, they assume that model size and number of training tokens independently affect performance, and they also have the option of learning the shape of the sigmoid function used to transform (modelled via a neural network). The experiments included in the paper confirm the strong predictive power of the obtained scaling law.

### Strengths
## originality
- The introduced scaling law has elements of novelty over previously presented ones, in particular that in Ruan et al 2024 and Owen 024.
- The latent skills interpretation is interesting.

## quality
- The experiments presented in Section 4 are extensive.

## clarity
- The text is well-written

## significance
- Leveraging information across model families is indeed beneficial to predict performance for families for which a few observations are available.
- removing the assumption of relying on model size and training tokens only their product is meaningful.

### Weaknesses
 - I don't think the paper gives a proper characterisation of Ruan et al 2024. In particular, the introduction and abstract seem to claim that assuming "LLM performance is driven by low-dimensional latent skills [...] influenced by computational resources" is a significant novelty of the paper, while that was actually the key value proposition of Ruan et al. 2024. Moreover, Section 2.2 claims that Ruan et al only uses two parameters per model family directly connecting compute to observed performance; however, my understanding of the method in Ruan et al. 2024 is that it is closer to what is presented in this paper in 3.1, i.e., Ruan et al. also learns a set of low-dimensional capabilities for each LLM, which is then transformed into model performance using "loading factors" specific to each benchmark. 
- The paper could provide more clarifications on the choices made to come up with the model in Sec 3.1, see questions below. 
- The notation in Sec 3.2 is confusing (see questions below). Moreover, it is unclear how much assumption 3.1 is realistic or verifiable.
- Some of the choices related to how the results are presented in Sec 4 seem arbitrary, as they are not explained (see questions below)
- Finally, I don't understand where the name "Sloth" comes from: I am not a native speaker, but it seems weird to pronounce "SSLaws" as Sloth, even though I see the joke.

### Questions
Related to Sec 3.1: 
- why was that specific model used in economics taken as inspiration?
- why is the skill slope shapred across family and the intercept fixed, and not the converse? The choice by the authors seems to be counterintuitive to me, as saying that increases in model size and number of training tokens give the same improvement, and the only thing that changes is the startin value of each skil. 
- why does x(s,t) not include log(st)?

Related to Sec 3.2: 
- how is the design matric defined?
- what is the dimension p?

Related to Sec 3.3: 
- What is the Huber loss?

Related to Sec 4: 
- why does Fig 2 show average over benchmarks while figure 1 does not?
- What is the substantial difference that makes their method so that (as stated in Sec 4.4): "Unlike Ruan et al. (2024)’s observational scaling law, Sloth can be used to estimate the latent skills of hypothetical LLMs and then used to predict the performance of those LLMs in downstream tasks"? I thought that was also possible for Ruan et al, as long as the model belongs to a family for which a few other models were already observed, which seems to be a necessary condition for the method in this paper too.

### Soundness
2

### Presentation
3

### Contribution
2
