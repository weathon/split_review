# Improving Reasoning Ability of Large Language Models via Iterative Uncertainty-based Preference Optimization

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6, 6, 5

## Abstract
Direct Preference Optimization (DPO) has recently emerged as an efficient and effective method for aligning large language models with human preferences.
However, constructing high-quality preference datasets remains challenging, often necessitating expensive manual or powerful LM annotations. Additionally, standard DPO exhibits suboptimal performance in complex reasoning tasks, such as mathematical and code reasoning.
In this paper, we introduce an approach to collect preference pairs through iterative sampling and execution feedback, tailored to the current learning state (e.g. well-learned, mis-learned, and unlearned) of the policy model.
To alleviate the failures of DPO and improve its applicability in reasoning tasks, we propose IUPO, an iterative uncertainty-based preference optimization method that achieves fine-grained preference control by assessing model confidence.
We validate our approach across three reasoning tasks, incorporating five established reasoning datasets and one self-curated dataset. Our experimental results demonstrate an overall improvement of 3.6% over the standard DPO method. 
Furthermore, our approach exhibits promising generalizability involving weak-to-strong (8B to 70B) and cross-model (Llama to Mistral) generalizations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduce Iterative Uncertainty-based Preference Optimization (IUPO) to improve the reasoning abilities (math and coding specifically in this paper) of large language models. Previous DPO always fail in complex reasoning tasks which require long reasoning chains because of the scarcity of high-quality preference data and the inherent limitation including coarse-grained (response-level) preference signal and decrease in preferred probability. To tackle these challenges, the authors propose the IUPO which automatically generates preference data (for math and coding) by compare the generated results with ground truth and additionally apply uncertainty measure to improve the models' confidence. Results on 6 datasets and plenty of analysis seem to show the improvements of IUP.

### Strengths
1. The proposed IUPO works well for code and math settings.

2. The introduced modification of DPO based on uncertainty makes sense.

### Weaknesses
However, there are several limitations:
1. It seems that the answer extractor and executable environment are specifically tailored for code and math setting. As a results, can this framework be generalized to other reasoning tasks such as spatio/commonsense reasoning or even planing task?

2. Also, since the preference creation process are relied on the accuracy of the answer extractor, what is the extraction accuracy? Will the extraction quality affect IUPO a lot?

3. Are the models learned with IUPO on math and code data be generalized to other reasoning settings? The author might want to present some out-of-domain evaluations if the claim is to improve the reasoning abilities.

### Questions
1. How would you select the number of iterations? Are there any creteria?

2. What do you think of the computation overhead vs performance gains? It seems that 3 or more iterations might results in extensive computation overhead while the performance improvements seems to be marginal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes IUPO: an iterative method for preference optimization in LLMs. The method works by iteratively (i) collecting preference data through response sampling and execution feedback from a virtual environment and (ii) optimizing the LLM with a modification of DPO that integrates an "uncertainty score". The approach has been tested on SQL, code, and math tasks and shows an overall 2.1/3.6% improvement over standard preference optimization approaches.

### Strengths
- The experiments are thorough and well-executed
- The approach has an overall 2.1/3.6% improvement over standard preference optimization approaches on SQL, code, and math tasks.
- The paper is well-structured and well-written:
	- The algorithm proposed is simple and clear
	- The author proposed a nice overview of the current limitations of DPO
- The code is released with the paper; it's well-structured and documented.

### Weaknesses
 - (Major) The uncertainty definition used is not mathematically grounded and lacks a rigorous definition and connection with common uncertainty estimators; it seems more like an ad-hoc heuristic used to boost performance than a proper estimator. Specifically, the method calculates the difference between the top two token probabilities, which is not a standard approach for uncertainty estimation. This choice lacks theoretical justification and does not align with established methods such as token entropy or variance of predictions.
- (Major) The data-collection procedure for IUPO requires Execution Feedback from a virtual environment. This drastically limits the applicability of the method to tasks with an execution environment available (e.g., coding, SQL). The generalizability of the approach to most tasks that do not have this virtual environment available is unclear. 
- (Major) The proposed method does not introduce exceptional variations compared to DPO. The method just introduces (i) a different way of sampling data and (ii) a minor modification of the DPO loss with the "uncertainty score" computed. The core optimization process remains largely similar to DPO, with the uncertainty component acting as a heuristic adjustment rather than a fundamental change.
- (Medium) The paper is well-written, but the main section of your method (Section 3.3) is not very clear (see also Questions section):
	- The definition of uncertainty $\Delta_t$ is not clear (see Questions)
	- The section uses inconsistent mathematical notation that makes it hard to follow. For example the subscript in  $\Delta_t$ is used to indicate the token in the sequence but in the following equations the functional form $\Delta(\cdot)$ is used without explaining how the uncertainty for the full sequence is computed.
	- Equation 3 is quite cryptic and several details are left to the reader (e.g., the definition of relative distance $k$ and window size $K$)
	- The "formal analysis" (Equations 6-7) is almost entirely derived from [Pal et al. (2024) Equations 4-6](https://arxiv.org/pdf/2402.13228#page=20.55), however I believe there are several missing pieces in the explanation that make it hard to follow in your paper
	- It is not clear how IUPO addresses every issue raised in 3.2
- (Medium) I believe the experimental part is missing an ablation of DPO with the uncertainty-based preference optimization (without the Iterative data collection part). It's not clear the role of the uncertainty score if used in standard DPO training.

### Questions
- Why did you choose Equation 2 to model uncertainty instead of other approaches? The choice of subtracting the top two tokens seems quite arbitrary and not grounded. I got that Wang and Zhou inspire it, but that paper has not been peer-reviewed. Can you elaborate a little bit on this choice? 
- Why do you call $\Delta_t$ "uncertainty"? If the second token is lower it means that the model is less uncertain, but $\Delta_t$ is actually higher (the opposite of uncertainty).
- "Specifically, we mine tokens with uncertainty measure below a fixed threshold τ and adjust the confidence of tokens within their subsequent window K:" + Equation 3. I did not fully get what you meant by "mine." Can you elaborate a little bit?
- "where ∆(·) is a set of uncertainty measures for all tokens in response." It is not clear to me the definition of this set. "Since ∆t is less than 1, the probability of the token after the difference with preferred in πθ(yl|x) will decrease, and the corresponding gradient will be lower, thus alleviating the decrease in the preferred probability issue." Could you elaborate?
- There are probably several typos in: Equations 4-8 $\mathcal{L}_{UPO}$ ; L323 "U-DPO" ; Figure 6 "UDPO"; Figure 5 BIRD "IU-DPO"
- Why is the weak to strong generalization experiment (Table 3) performed just on the Text-to-SQL task and without comparing it with DPO and DPOP?
- It's not clear how Figure 5 is computed. From my understanding you compute $\Delta_t$ for each token but how is this measure aggregated over the length and the dataset? This is not explained in the paper (I suppose mean). Again it is counter intuitive that $\Delta_t$  is called uncertainty while larger $\Delta_t$  means more confidence in the generation. 
- "Since the parameters θ of models are numerous, we focus on the logits $\theta_j$ , which is input to softmax". What is $\theta_j$ ?
- Why did you set the threshold $\tau$ to 0.3? What is the rational behind?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Iterative Uncertainty-based Preference Optimization (IUPO) as an enhancement over Direct Preference Optimization (DPO) for large language models in complex reasoning tasks. IUPO incorporates iterative response sampling and execution feedback, specifically optimizing policy with token-level uncertainty measures. The experiments demonstrate improvements over DPO, showing IUPO’s benefits in reasoning tasks across models and datasets.

### Strengths
1. IUPO represents an advancement by using uncertainty measures for token-level adjustments, potentially enhancing fine-grained optimization.
2. The results demonstrate IUPO's effectiveness in improving reasoning abilities, specifically surpassing DPO on various benchmarks.
3. The paper includes a range of experimental analyses, including model confidence evaluations and the impact of iterations, which help illustrate IUPO's capabilities and limitations.

### Weaknesses
1. The enhancement over DPO, while valuable, is relatively modest, especially on hard tasks like math. It appears incremental given that DPO's limitations are well-documented, and similar iterative techniques exist in the literature.
2. Some contributions, particularly the automatic generation of preference data, lack clarity in their novelty relative to existing data generation techniques.
3. The data collection settings required the final answer is auto-verifiable by either comparing to the gold answer or code execution. In such case, a clear and robust reward is already available and it is not clear why DPO is still necessary here.

### Questions
1. Continue on the weakness 3: given that your settings required to have an online automatic verifier to provide reward signal, you are able to directly apply policy gradient here. Without the need of training a reward model, the policy gradient algorithm is not much harder than DPO but have much better performance. One thing I am kinda confused by all the DPO papers nowadays is why they always get rid of the discussion with policy gradient method, especially in this kind of settings without the need of a reward model?
2. Can you explain Figure 4 step 2? What's the meaning of circle N and circle 1? If that means the number of iteration, why you are sampling from the N-th iteration and 1-st iteration for the well-learned type?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduce an strategy for collecting preference pairs data through iterative sampling and execution feedback and a variant of the DPO(Direct Preference Optimization) algorithm named IUPO(Iterative Uncertainty-based Preference Optimization).
The authors claim that the IUPO method achieves fine-grained preference control by assessing model confidence and alleviates the distribution shift problem in offline DPO.
Moreover, the authors conduct experiments across three reasoning tasks to demonstrate the effectiveness and generalization of IUPO.

### Strengths
1. IUPO method is interesting and the "Formal analysis" part clearly demonstrates how the IUPO improves the DPO through uncertainty.
2. The proposed method achieves a good performance on reasoning tasks in text-to-SQL, code and mathematical, offering an overall improvement of 3.6% over the standard DPO method.
3. The motivation is clear, the analysis is coherent and well-reasoned, and the logic is sound.

### Weaknesses
1. Comparing IUPO only with DPO and DPOP may seem insufficient. Could the author compare the proposed algorithm with more relevant methods, such as KTO?
2. The article does not mention anything related to training cost. I would like to know how much the training cost for three iterations increases compared to a single iteration? Does the IUPO have the advantage in training cost compared to other methods?
3. There are some minor issues in the appendix: 1) In the caption of Table 7 and Table 8, the meanings of "tick" and "cross" have been reversed  2) On line 907, the format of the equal sign "=" is inconsistent with other lines of equal signs.

### Questions
See "Weakness"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to address three main limitations of the DPO algorithm identified by recent works: (1) preference signals only on outcomes are too coarse-grained, (2) decreasing the rewards for both preferred and nonpreferred outputs, and (3) offline. The paper proposes a new preference data collection method and a new variant of the DPO algorithm to address this. For the data collection, given an instruction, the paper uses two models (before and after SFT) to collect three pairs of outputs, and iteratively uses them in the preference learning stage. For the preference learning algorithm, the paper proposes to augment DPO with token-level uncertainties that aims to down-weight the gradient of the uncertain tokens.

Experiments on text2sql, code generation, and math reasoning are conducted with Mistral-7B and Llama3-8B. Promising results are achieved compared to DPO and SFT baselines.

I will seriously consider revising my current negative score if the authors can help me understand some technical details in the response (details below).

### Strengths
- The proposed data collection method and the IUPO algorithm are interesting and novel to the best of my knowledge
- Motivation is clear
- Comprehensive and interesting analysis

### Weaknesses
 - Some key technical details are missing, which makes it difficult for me to understand the algorithm and evaluate it. Specifically, the $\odot$ operator in Eqs 4 and 5 are never explained. My guess from the context is that it denotes the elementwise product between two vectors; however, $\pi_{theta}$ should be a scalar (probability) and it is unclear to me how this works. Maybe the authors can help me understand this
- Can the authors comment on how the proposed algorithm relates to https://arxiv.org/abs/2404.12358 and https://arxiv.org/abs/2406.06887, and whether or not the paper should compare to them?
- It would be interesting to explore whether DPO can benefit from the 3-iteration training
- Probably due to LLM revision, some of the wording choices read strange and inaccurate to me. For example, "unfortunate instances" (line 150), the "precision and clarity" of the preference signals (line 138), "coincides with" (line238). I strongly recommend a thorough proof read.

### Questions
Can one go beyond 3 iterations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a method called Iterative Uncertainty-based Preference Optimization (IUPO) to enhance the reasoning capabilities of large language models (LLMs). The authors address the limitations of Direct Preference Optimization (DPO), particularly its suboptimal performance in complex reasoning tasks such as mathematical and code reasoning, due to the scarcity of high-quality preference data and the limitations of its alignment method.

### Strengths
1. IUPO automates the generation of preference data, which is typically a labor-intensive process. It does this by leveraging existing model responses and execution feedback, eliminating the need for additional manual annotations or more powerful models.
2. IUPO employs an iterative approach to continuously update preference data, ensuring that the data remains relevant and in-distribution for the policy model. This iterative optimization is shown to be more effective than simply increasing the volume of preference data.
3. This paper conducts comprehensive experiments across three reasoning tasks using established and self-curated datasets, showing an overall improvement of 3.6% over the standard DPO method.

### Weaknesses
1. The application of reinforcement learning algorithms for tuning SFT models with LoRA (Low-Rank Adaptation) might be somewhat trivial, given that LoRA adds some parameters. Could you demonstrate the performance advantage of your reinforcement learning algorithm under full-parameter fine-tuning settings?
2. In terms of algorithmic performance, there are currently many algorithms that surpass the DPO(such as IPO and KTO). Relying solely on experimental validation with DPO may be somewhat insufficient and narrow. It would be advantageous to include some theoretical guidance or comparisons with other reinforcement learning algorithms to enhance the analysis.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
