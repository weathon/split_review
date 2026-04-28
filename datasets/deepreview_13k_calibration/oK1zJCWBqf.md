# Soft Preference Optimization:  Aligning Language Models to Expert Distributions

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 5, 8, 5, 6

## Abstract
We propose Soft Preference Optimization (SPO), a method for aligning generative models, such as Large Language Models (LLMs), with human preferences, without the need for a reward model. SPO optimizes model outputs directly over a preference dataset through a natural loss function that integrates preference loss with a regularization term across the model's entire output distribution rather than limiting it to the preference dataset. Although SPO does not require the assumption of an existing underlying reward model, we demonstrate that, under the Bradley-Terry (BT) model assumption, it converges to a softmax of scaled rewards, with the distribution's ``softness" adjustable via the softmax exponent, an algorithm parameter. We showcase  SPO's methodology, its theoretical foundation, and its comparative advantages in simplicity and alignment precision.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an offline alignment objective composed of the preference loss and regularization loss. In the preference loss, it uses a temperature parameter to control the "softness" of the preference; in the regularization loss, it uses KL under different prompts (than preference prompts). Theoretically, it shows the connection to the reward models. Empirically, it shows improved win rates against SFT among baselines

### Strengths
* The paper studies the important question of what regularization data for the alignment methods
* The proposed objective is interesting and has connection to the reward model

### Weaknesses
I think the main weakness is that the proposed method is a combination of many components, and it's difficult to assess the utility of each one
* First, the preference loss rewritten as $log \sigma(log \pi_\theta(y_1) - log \pi_\theta(y_2))$ is similar to the DPO loss, but without calibration using $\pi_0(.)$. The DPO has the calibration terms because of the KL regularization using in-distribution dataset. The paper can't convince me that getting rid of the calibration terms brings any advantage in itself (either theoretically or empirically). I think the calibration term could be important when for example $y_1$ is much more/less likely than $y_2$ under $\pi_0$. Maybe the author could consider an ablation experiment comparing the two objectives (you can also use $\alpha$ in both cases too). 
* Second question is when might out-of-domain regularization helps. Again, I am not convinced if, and when, such regularization helps. 

Besides, 
* I can't confidently assess the method's utility just looking at win rates in the experiments. A method could do very well in win rate by having a huge KL from the SFT --- maybe plotting KL vs win rate gives more convincing arguments. 
* The paper says RLHF uses out-of-domain prompts --- is that true?

### Questions
I put my questions in the weakness

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces SPO (Soft Preference Optimization), a method for aligning language models with human preferences without requiring a reward model. SPO operates by optimizing model outputs directly using a loss function that combines preference loss with regularization across the full output distribution. While SPO doesn't require reward model assumptions, the authors prove it converges to a softmax of scaled rewards under the Bradley-Terry model, with adjustable softmax temperature. The method differs from predecessors like DPO in two ways: its preference loss formulation, and its application of regularization across the entire output distribution rather than just the preference dataset.

### Strengths
1. The paper presents a well-structured framework for preference loss without relying on Bradley-Terry/Plackett-Luce model assumptions. The development from basic to general algorithm is logical and easy to follow.
2. The framework shows impressive versatility by handling multiple data types (pairwise, best-of-n, and ranked preference data), demonstrating a comprehensive approach to preference optimization.
3. The introduction of global regularization rather than in-dataset regularization is a novel and well-justified approach that shows better empirical results.
4. The theoretical foundations are solid, with clear proofs and convergence guarantees for each variant of the algorithm.

### Weaknesses
1. The experimental evaluation has several limitations:
* The experimental evaluation would benefit from broader model and dataset coverage. While the current results on Llama-2-7B and AlpacaFarm are present, only one setting might be not enough. Here are some suggestions for reference:  
The baseline performance is concerning, with several methods showing negative results on length-controlled win rates, suggesting potential issues with the experimental setup or hyperparameter tuning. You may want to consider including models from different families such as Mistral-7B to show architecture-agnostic performance. To mention but not significant problem, llama-2-7B is currently not among the most capable open-source LLMs according to leaderboards like AlpacaEval. Showing results for llama-3-8B might make the results more significant. Additionally, evaluating on diverse datasets like UltraFeedback (~3 times larger than the alpacaFarm dataset) would verify generalizability across different instruction-tuning distributions.  These additions would provide stronger evidence for the method's broad applicability.

* Specific concerns are raised about the baseline performance that warrant further investigation. The baseline methods has at most 51.94% on the LC Win-rate against SFT, which seems unusually poor given their reported performance in original papers. Since you are fine-tuning starting from the SFT model, that means all the preference optimization baseline methods nearly not improve the quality at all, even worse the performance for R-DPO, CPO, SimPO, IPO.    
                                           Is there any specific reason? While there could be various reasons, one possibility is suboptimal hyperparameter choices. I recommend using similar hyperparameter settings as successful implementations in previous work (e.g., Meng et al. 2024, SimPO paper reported strong performance with their specific configuration), to ensure a fair comparison of these baseline methods.

2. Could you clarify the evaluation dataset sizes for each experiment? This information is particularly relevant when examining the global regularizer results, where some improvements show modest gains (e.g., from 59.9% to 60.8%). Given these subtle differences, I recommend including statistical significance testing to strengthen the results' interpretation.

### Questions
1. Regarding the preference representation: While your method defines $p(y_w > y_l | x)$ without depending on BT/PL model assumptions, isn't it effectively equivalent in expressivity? Please correct me if I am wrong. It seems that $\pi_\theta(y_w | x)^\alpha$ could be seen as an alternative parametrization of $\exp(\frac{1}{\beta}r_\phi(y_w, x))$, where $\alpha$ and $\beta$ serve similar roles, and $r_\phi$ and $\pi_\theta$ map to equivalent functions. Could you clarify if/how your formulation provides additional expressivity?
2. How does the choice of $\alpha$ interact with different types of preference data (pairwise, best-of-n, ranked)? Is there a principled way to select optimal $\alpha$ values for different scenarios or data distributions?

### Soundness
1

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
3

### Summary
This paper introduces Soft Preference Optimization (SPO), a technique to fine-tune a LM to fit a dataset containing the preferred response to a given query, given some alternative, or given a ranking of possible responses. The main contribution of this paper is to model the preference probability $P_{\pi_\theta}(y_1 \succ y_2)$ as $\frac{\pi_\theta(y_1)}{\pi_\theta(y_1) + \pi_\theta(y_2)}$ and then fit the preference data using a log-likelihood loss plus a regularization term, which here is taken to be the commonly used KL divergence to the original model.

The model is further extended to include an (inverse) "temperature" parameter $\alpha$ to regulate the entropy of the resulting distribution, and a weighting function $\mu$ that is intended to down-weight preference data given on poor-quality samples (as judged by the model itself).

Also, a generalized loss to accommodate best-of-n preference data and ranked preference data is provided. 

The model was evaluated on win-rates against a SFT-based competitor, comparing positively to a number of competitive baselines on pairwise data and also to DPO on best-of-n and ranked data. For the latter task, a dataset was generated which is provided in the anonymous link.

Finally, a (biased, low-variance) estimator of the KL is proposed using token-level subsequences of the samples, which I think is another contribution of this paper, although I am not 100% sure of that.

### Strengths
* S1: The paper proposes a simple and elegant model to fit preference data, including pairwise, best-of-n, and ranked data. The model is so simple in fact that it is surprising it had not been proposed before. (*1)
* S2: It also includes an extensive theoretical analysis of the optimal solution to the proposed loss when the preference data is sampled from Bradley-Terry or Plackett-Luce models (*2)
* S3: The presentation is very clear
* S4: The empirical evaluation is sufficiently convincing of the competitiveness of the method

(*1) In the related work, the authors do acknowledge a similar proposal in CPO by Xu et al.
(*2) I have not carefully checked the calculations of the theorems proofs.

### Weaknesses
None that I can think of

### Questions
1. 
> Moreover, SPO has an advantage over DPO and RLHF in avoiding determinism. In cases where the
preference dataset is comparable to pre-training data size, regularization (DKL) becomes unnecessary,
and RLHF and DPO loss functions tend to produce deterministic models; that is they tend to return a
single high-quality response per query.

Doesn't that depend on the value of the $\beta$ parameter? See, for instance, Theorem 1 in https://arxiv.org/abs/2206.00761. You can see that as $\beta$ becomes large, the optimal distribution reverts to the original model.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Soft Preference Optimization (SPO), a generative model approach that aligns with human preferences without a reward model. SPO directly optimizes the model output by combining a natural loss function with a preference loss and a regularization term, covering the entire output distribution. It was theoretically proved that under the assumption of the Bradley-Terry model, SPO could converge to the Softmax distribution, and the output softness was adjusted by the algorithm parameters. Experiments on AlpacaFarm benchmark show that SPO outperforms SimPO, DPO and other alignment algorithms. The authors claim the advantage of SPO in avoiding determinism compared to DPO and RLHF.

### Strengths
1. This paper introduces the concept of Soft Preference Optimization (SPO) and elaborates on its theoretical foundations. The authors not only outline the goals and motivations behind SPO but also explore its distinctions from existing approaches, such as Direct Preference Optimization (DPO). The mathematical proofs presented in the paper are rigorous, particularly those of the main theorems detailed in the appendix. These proofs not only substantiate the effectiveness of the SPO method but also establish that SPO can converge to an optimal softmax distribution under specific conditions. Such rigorous mathematical derivations lay a solid foundation for the scientific validity and credibility of the SPO approach.

2. In the experimental section, SPO outperforms some current baseline alignment methods, demonstrating its effectiveness in tasks such as instruction following. Moreover, SPO significantly outperforms other baselines in its ability to focus on the best data.

### Weaknesses
1.The paper presents Soft Preference Optimization (SPO) as a novel method for aligning generative models with human preferences without relying on a reward model.  While the theoretical foundation is well-elaborated, the experimental section lacks a comprehensive evaluation of SPO across a broader range of pairwise alignment datasets and benchmarks.  A more extensive set of experiments is necessary to substantiate the claim that SPO can effectively focus on optimal data alignment without sacrificing performance in other areas.  It is crucial to include more experimental results and analyses to demonstrate that SPO enhances model alignment while maintaining or improving performance in related tasks.


2. The authors highlight the differences between SPO and existing approaches like Direct Preference Optimization (DPO) and Reinforcement Learning from Human Feedback (RLHF).  While it is noted that SPO introduces a superior regularization term to prevent overfitting on preference data, the paper does not sufficiently address whether this approach might come at the expense of other model capabilities.  DPO, being a reward-model-free algorithm, is already designed to balance alignment with human preferences and model performance.  Therefore, it is essential for the authors to conduct additional experiments that validate whether SPO's emphasis on diversity and alignment comes at the cost of the model's ability to perform well on a broader range of tasks.  A thorough analysis comparing SPO against DPO and other baselines in terms of overall model performance, as well as alignment, would significantly strengthen the paper's contributions and claims.

3. The experimental section of the paper, while demonstrating the effectiveness of Soft Preference Optimization (SPO), does not include an ablation study on the hyper-parameters used within the SPO framework. By including such analysis, the paper would offer a more complete picture of the method's robustness and the sensitivity to hyper-parameter tuning, which is valuable for both theoretical understanding and practical application.

### Questions
1. Does the performance of the SPO come at the expense of other capabilities?

2. Diversity and accuracy are inherently trade off, but why is there no discussion of this in the experimental section of the article?

### Soundness
2

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
The authors propose Soft Preference Optimization (SPO), which optimizes two key components: (1) a preference loss function aimed at maximizing the likelihood of favoring the chosen response over the rejected one, and (2) a KL-divergence regularization term applied to the model's samples. The authors extend SPO to handle other types of preferences, such as best-of-n and ranked preferences. They conduct experiments using various types of preference data, including pairwise, best-of-n, and ranked preferences. The ablation study further validates the choice of the regularization term and the additional weight function used in the objective.

### Strengths
The approach of integrating preference loss with explicit regularization makes sense. The experimental results across different preference settings appear promising.

### Weaknesses
1. While the authors claim that reward-model-free alignment methods offer advantages, these methods, which solely optimize a preference dataset, may overfit or overestimate out-of-distribution data. This can result in degraded performance during inference. Therefore, to convincingly demonstrate the effectiveness of the proposed method, it is crucial to compare it against RLHF approaches like PPO. This can be achieved by replacing the preference loss with an on-policy loss term for a fair comparison.

2. The derivation of Theorem 1, as well as the subsequent theorems, does not account for the regularization term, which is typically present in the analytic solutions of PPO or DPO. This omission compromises the theoretical results, given that the proposed method essentially optimizes a combination of two loss terms.

3. The design of $\mu$ lacks intuition despite its complication, e.g., subtracting the average in a batch. Also the effect of $\gamma$ would be clearer with an ablation study of sweeping this hyper-parameter.

4. Missing data on the top of page 9: "improved win-rate from xx% to xx%".

5. Missing reference to related alignment methods [1,2,3] that match the model's output distribution.

### Questions
1. Could the authors provide a more detailed empirical comparison between PPO and SPO? Since SPO requires on-policy data sampling to compute the KL-regularization, introducing additional complexity that is typically avoided by off-policy alignment methods. Thereby, the key difference in performance between PPO and SPO might stem from the first term in Eq.(1). Would optimizing on off-policy preference data offer a significant advantage over on-policy sampled data, as in PPO, and could this be further explored? For example, training both methods on the same preference dataset, then evaluating them on a held-out test set (in-distribution) and a separate dataset from a different domain (out-of-distribution) respectively.

2. Could the authors provide a clearer interpretation of the solution obtained by SPO when regularization is applied under the BT assumption and show how the regularizer affects the convergence properties of the algorithm, as this represents the actual objective being optimized. 

3. Could the authors conduct a more thorough analysis of the weighting function by breaking down its individual components and performing an ablation study, as it would help to justify the necessity of its complex form.

### Soundness
3

### Presentation
2

### Contribution
2
