# TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 10, 5, 5

## Abstract
Direct Preference Optimization (DPO) has been widely adopted for preference alignment of Large Language Models (LLMs) due to its simplicity and effectiveness. 
However, DPO is derived as a bandit problem in which the whole response is treated as a single arm, ignoring the importance differences between tokens, which may affect optimization efficiency and make it difficult to achieve optimal results.
In this work, we propose that the optimal data for DPO has equal expected rewards for each token in winning and losing responses, as there is no difference in token importance. 
However, since the optimal dataset is unavailable in practice, we propose using the original dataset for importance sampling to achieve unbiased optimization. 
Accordingly, we propose a token-level importance sampling DPO objective named \texttt{TIS-DPO} that assigns importance weights to each token based on its reward.
Inspired by previous works, we estimate the token importance weights using the difference in prediction probabilities from a pair of contrastive LLMs. We explore three methods to construct these contrastive LLMs: (1) guiding the original LLM with contrastive prompts, (2) training two separate LLMs using winning and losing responses, and (3) performing forward and reverse DPO training with winning and losing responses.
Experiments show that \texttt{TIS-DPO} significantly outperforms various baseline methods on harmlessness and helpfulness alignment and summarization tasks. We also visualize the estimated weights, demonstrating their ability to identify key token positions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents TIS-DPO (Token-Level Importance Sampling for Direct Preference Optimization), a novel approach designed to enhance the optimization of Large Language Models by assignig different weights to tokens based on their predicted rewards. It aims to achieve unbiased optimization by approximating an ideal dataset where each token has equal expected rewards.

Rely on the previous work TDPO (Token-level Direct Preference Optimization), this method estimates token importance weights using differences in prediction probabilities between pairs of contrastive LLMs. Three approaches are explored for constructing these contrastive models:
- Guiding the original LLM with contrastive prompts.
- Training separate LLMs on winning and losing responses.
- Performing forward and reverse DPO training.

Extensive experiments are conducted to evaluate TIS-DPO on tasks related to harmlessness, helpfulness, and summarization. Results indicate that TIS-DPO significantly outperforms several baseline methods, demonstrating improvements in both safety and response quality.

### Strengths
- TIS-DPO introduces a token-level importance sampling method that addresses the limitations of treating all tokens equally in Direct Preference Optimization (DPO), enhancing optimization efficiency.
- The proposed method is evaluated across multiple datasets, showing its robustness and versatility in different contexts and tasks.
- By using actual dataset with importance sampling instead of taking that dataset as an ideal dataset, the method is more practical for real-world applications where optimal data distribution is typically unavailable.

### Weaknesses
 - The proposed method involves steps for constructing contrastive LLMs and tokeniwse importance weights estimating, which increases computational costs and training time compared to simpler baseline methods.
- The Hoeffding inequality is applied in the proof of Theory 1, which requires that the summation variables (i.e. token rewards) be i.i.d., but tokens in a sentence dose not conform to the condition of being i.i.d. along with their observed rewards. This casts doubt on the validity of the theoretical analysis, as the core assumption is violated.
- TIS-DPO(S/D) distributes the sentence "value" to the token level and in addition estimates token importance via reward evaluator driven by the same sentence "value". The potential cost is that the method may be more sensitive to the noise in data annotation. For example, if there is a certain proportion of noise in the training set, let's assume that some of the triples $(x, y_w, y_l)$ are mislabeled in reverse order as $(x, y_l, y_w)$ which are common in the real world. Then TIS-DPO(S/D) may be more affected than DPO. Can you add 20% of noise (i.e. swapping the chosen and reject of a triple) into the training data and compare the performance degradation of TIS-DPO(S/D) versus DPO?



### Questions
1. TIS-DPO(D) in Table 1 shows a significant improvement in performance far exceeds expectations, which seems a probable risk of overfitting. Can you conduct cross-validation to prove that there is no overfitting?
2. The experimental results of other methods on the Anthropic-HH dataset in Table 1 were not found in the cited papers, such as TDPO. Were all the comparative experiments were reproduced?
3. As quite a few hyperparameters have been introduced on top of DPO and TDPO, are there any sensitivity test on the newly added hyperparameters $k$, $\mu$, $L$ and $U$ in Eq. 19?

P.S.
- Zeng2024a and Zeng2024b are different versions of the same paper.
- Conflict usage of $\mu$ in Theorem 2, eq. 14 and eq. 19.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The paper makes a key claim that "the most stable form of DPO loss occurs when tokens in winning and losing responses have identical expected rewards." And the best way to estimate the unavailable ideal DPO dataset is to use importance sampling. The paper did a thorough proof combining prior works of Zeng et al. to show a token-level DPO objective, and then enhance it with importance sampling to assign importance weight on each token of actual data distribution to approximate the data distribution of ideal equal importance DPO dataset. 

It then proposes 3 ways to estimate the token-wise weighting by contrasting LLM likelihood of 1. a prompt-based method. 2 SFT two models to desirable and undesirable. 3. DPO two models to desirable and undesirable. Experiment results show 1 doesn't work, and 3 works surprisingly well, significantly exceeding sequence level DPO baseline on HH, PKUSafe, and Summarization dataset.

### Strengths
* Very novel idea of using contrastive LLM likelihood as token-level weights for importance sampling. 

* Very important area of research to improve the popular off-line alignment DPO algorithm. 

* Great insight about limitation of sequence level DPO, thus introducing the need for nuanced token-level optimization 

* Surprisingly good improvements against DPO baseline using token-level importance sampling based TIS-DPO. 

* Very thorough proof and derivation process for the TIS-DPO objective

### Weaknesses
 * “Although Rafailov et al. (2024a) demonstrate that DPO possesses a certain degree of token-level interpretability,” It would be helpful to point to the exact section or figure of this analysis. 

* The strength of the method could benefit from more thorough experiment on stronger alignment datasets. HH and Summarization are commonly used but relatively poor quality data, compared with some newer alignment datasets like Ultrafeedback and HelpSteer2. 

* It is clear that TIS-DPO has significant strength in aligning models to safety and slight improvement to helpfulness. I am curious to see the dynamic of using TIS-DPO to align stronger models like Gemma2-9B or Llama-3-8B. 

Overall, great paper, excellent intuition, and solid experiment results.

### Questions
Could you explain why or provide some intuition as to why the the improvements is much better for safety alignment than helpful alignment?

Also, it would be great to have some empirical experiments to see whether TIS-DPO is leading to faster convergence (which may be  case based on the limited experiment setup shown in paper) or in fact better convergence, leading to meaningfully better aligned models. Could you expand on this, and how you may design experiments to illustrate it?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new approach, Token-level Importance Sampling DPO (TIS-DPO), to improve the efficiency and effectiveness of Direct Preference Optimization (DPO) for Large Language Models (LLMs). The authors propose that optimal data for DPO should have equal expected rewards for each token in winning and losing responses. They use importance sampling with the original dataset to achieve unbiased optimization and estimate token importance weights using the difference in prediction probabilities from contrastive LLMs. Experiments demonstrate that TIS-DPO outperforms baseline methods in harmlessness, helpfulness alignment, and summarization tasks.

### Strengths
1. The paper presents a clear and well-structured method, TIS-DPO, which addresses a limitation of traditional DPO by considering the importance of individual tokens.

2. The experimental results show improvements over various baselines, indicating the practical value of the proposed method.

### Weaknesses
1. Lack of In-depth Analysis: The paper lacks a detailed analysis of why the three proposed methods for constructing contrastive LLMs can effectively measure token importance during training. Specifically, the paper does not provide a clear justification for why the difference in prediction probabilities between these contrastive models would correlate with token importance for DPO. Furthermore, the paper does not explore the potential biases introduced by each contrastive model construction method, nor does it offer a theoretical explanation for the observed performance differences among these methods. The absence of such analysis makes it difficult to understand the underlying mechanisms and limitations of the proposed approach.

2. Fixed Token Importance: The token importance weights are generated before training and remain fixed throughout the process. However, as the model evolves during training, the importance of tokens may also change, which could affect the effectiveness of the method. For example, tokens that are initially crucial for distinguishing between winning and losing responses might become less important as the model learns, and vice-versa. The paper does not address this potential issue of static weights, which may lead to suboptimal performance as the model's understanding of the task evolves.

3. Scalability and Generalizability: The paper does not thoroughly address the scalability and generalizability of the proposed method. It is unclear whether every model would require its own set of token importance weights or if the one set of weights can be generalized to different models and tasks. The paper lacks experiments to validate the transferability of the importance weights across different model architectures, sizes, or training datasets. This raises concerns about the practical applicability of the method in diverse scenarios.

4. Limited Experimental Scope: While the method shows effectiveness in improving harmlessness and helpfulness, the experiments do not cover other critical areas such as code and mathematics, where token-level importance might be even more crucial. The paper does not provide any evidence that the proposed method can improve performance in these domains, which are essential for evaluating the general applicability of the approach. Further experiments in these domains would strengthen the validation of the method.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes TIS-DPO (Token-level Importance Sampling for Direct Preference Optimization), which is built upon standard DPO by assuming that different tokens within a response have varying levels of importance. Specifically, the importance of tokens in the completion is estimated based on 2 separate reward models. The authors demonstrate that on two datasets the proposed method  outperforms baseline methods.

### Strengths
- The paper proposes a new perspective of preference learning based on DPO by considering token-level importance.
- Nice appendix.
- The experimental evaluation is comprehensive, spanning 2 datasets, different metrics including MT-bench and win rates, and multiple baselines (DPO, PPO, IPO, TDPO, KTO) .

### Weaknesses
 - Questionable Motivation. Even though we assume you can accurately estimate the token importance, the token-level DPO approach seems misaligned with how preference data is collected, where annotators make holistic judgments about complete responses, not token-by-token evaluations. 
- The accuracy and reliability of token-level importance estimation are not thoroughly validated 
- The approach assumes tokens can be evaluated independently, which ignores crucial context dependencies in language.
- Introducing reward models for token importance estimation seems to contradict DPO's core advantage of avoiding reward modeling. Should we compare against PPO, where the rewards are estimated?
 - The additional cost of training and maintaining contrastive LLMs for weight estimation is not analyzed. No discussion of the computational trade-offs compared to standard DPO. The scalability implications for larger models are not addressed
-  Introduction of new hyperparameter μ adds complexity. Limited analysis of hyperparameter sensitivity. No clear guidance for hyperparameter selection in different scenarios
- Missing analysis of how sequence length affects performance. No investigation of the relationship between token position and estimated importance.
- Table 2 presentation should have been corrected.

### Questions
- Why is the DPO result missing in Table 1?
- How many LLMs are needed in your training process? Is it 3?
- Will your proposed method be sensitive to sequence length in better or worse completions, where longer sequences may have higher rewards?
- Regarding the win rate, I understand that GPT-4 is the evaluator model - which model is being used as the competitor?
- In Table 1, is there any reason why the win rate increases significantly while the MT-bench score is not improved comparably?

### Soundness
2

### Presentation
2

### Contribution
2
