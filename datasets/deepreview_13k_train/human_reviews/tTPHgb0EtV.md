# Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Harmful fine-tuning issue \citep{qi2023fine} poses serious safety concerns for Large language models' fine-tuning-as-a-service. While existing defenses have been proposed to mitigate the issue, their performances are still far away from satisfactory, and the root cause of the problem has not been fully recovered. To this end, we in this paper show that \textit{harmful perturbation} over the model weights could be a cause of alignment-broken of harmful fine-tuning. In order to attenuate the negative impact of harmful perturbation, we propose an alignment-stage solution, dubbed Booster. Technically, along with the original alignment loss,  we append a loss regularizer in the alignment stage's optimization. The regularizer ensures that the model's harmful loss reduction before/after simulated harmful perturbation is attenuated, thereby mitigating the subsequent fine-tuning risk.     Empirical results show that Booster can effectively reduce the harmful score of the fine-tuned models while maintaining the performance of downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors propose a method to alleviate the influence of attacking fine-tuning for breaking the LLM alignment. Specifically, the authors add a regularizer on the training loss so that the model can find an optimal point that keeps good performance while being robust to harmful fine-tuning --- not easy to fit the harmful data if trained on it, so-called harmful perturbation. The results show that the proposed method improves significantly over the baselines on harmful scores (e.g. 14.50 -> 4.80).

### Strengths
1. The research topic on tackling harmful fine-tuning is important and timely because of the urgent need to ensure the trained LLM can resist alignment attacks.

2. The proposed approach is intuitive and clear, based on the clear definition of harmful perturbation. The experimental results improve significantly over the baselines, demonstrating the effectiveness of the proposed approach.

3. The writing is very clear and easy to follow. The formulas and pseudo-code clearly describe the algorithm and Figure 3 demonstrates how the proposed method works.

### Weaknesses
1. In line 375, Booster initially has a relatively low harmful training loss. What is the reason for this? Does it mean that the model sees the harmful data in advance and trains it a little bit before the testing stage?

2. Adding more samples of the datasets can make it more clear how the model works and beat the baselines.

### Questions
See above.

### Soundness
3

### Presentation
4

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
The paper addresses the vulnerability of fine-tuned large language models (LLMs) to harmful data, which can compromise their safety alignment and degrade service quality. It proposes a new alignment-stage solution called Booster, which introduces a regularizer to reduce the impact of harmful perturbation—where optimization over harmful data decreases the model's safety.

### Strengths
1. The paper presents a novel approach, Booster, that effectively minimizes harmful perturbation during the alignment stage, thereby improving the safety and reliability of fine-tuned language models. The method is simple yet effective.

2. Its computational efficiency, requiring only three forward/backward passes per optimization step, makes it suitable for practical applications with frequent fine-tuning requests.

### Weaknesses
The addition of a regularizer introduces trade-offs in terms of the balance between aligning the model and minimizing harmful loss. Finding the right balance can be challenging and might lead to varying results depending on the specific application or dataset. Specifically, the paper does not explore how the regularization parameter affects the model's performance on diverse downstream tasks. The optimal value for this parameter might vary significantly depending on the task, making it difficult to apply the method in practice without extensive task-specific tuning. This could limit the generalizability of the proposed approach, as a single set of hyperparameters might not be suitable for all scenarios. Furthermore, the paper lacks a detailed analysis of the sensitivity of the method to the choice of the regularization parameter, which is critical for practical deployment.

### Questions
N/A

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
This paper proposes Booster, an alignment-stage method for defensing harmful fine-tuning attack. Harmful fine-tuning attack refers to the attack to fine-tune an aligned LLM with a dataset mixed with benign and adversarial instances, where the fine-tuned model will loss its safety alignment ability. The proposed method, Booster, use a harmful dataset during alignment stage to teach the LLM to attenuate the effects of the harmful samples in the fine-tuning dataset. This is done by a minimax loss. Based on experiments on four datasets and three LLMs, they show that the proposed method outperforms other baseline methods. Analysis are conducted to understand the effectiveness of the proposed method under different scenarios

### Strengths
- This paper proposes a new method of defending harmful fine-tuning attacks at the SFT stage
- The proposed method is shown to be effective on the datasets evaluated in the paper
- Thorough analyses are conducted to understand how Booster works under different alignment and task-specific fine-tuning scenarios.

### Weaknesses
 - Section 3.2, which seems to be the motivation part of the paper, is not easy to follow for the following two reasons
    - The term *harmful score* is not properly defined
    - How the **Derived Insights** are derived from the observations is highly unclear. The causal relation between the first part of the sentence (*Because harmful fine-tuning data is considered to be inseparable from the benign data*) and the rest of the sentence (harmful perturbation is indeed inevitable in the user fine-tuning stage) cannot be justified by Figure 2. It is also unclear whether the experiment shown here relates to the proposed method.
- The experiment settings and results are weak. The paper uses SST2, AGNews, GSM8K, and AlpacaEval for the experiments. However, **all the experiments, except the experiments in Table 3, only reports the results of SST2**. Considering that SST2 is a very simple task for LLMs nowadays, only reporting the results for SST2 is a major weakness. Moreover, considering that GSM8K and AlpacaEval are more widely adopted for evaluating current LLMs, the results of **Booster in Table 3 are not convincing: Booster has a very high harmful score on AlpacaEval while Booster’s harmful score is not better than two baselines on GSM8K**. This makes me doubt the effectiveness of the proposed method on more challenging tasks.
- Presentation can be improved. In the first two paragraphs, the paper does not mention what is the dataset reported here. This makes it hard for me to evaluate the experiments at first. The notations with tilde are not defined in the paper.

### Questions
What would be the results like if we directly remove the last term in equation (3)? (The term of gradient after the model takes one-step normalized update)

### Soundness
3

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
4

### Summary
This work introduces Booster, an alignment-time method to attenuate harmful perturbations and mitigate the risks brought by harmful fine-tuning. They propose a loss regularize in the alignment tuning and combine it with the original alignment loss to optimize the LLM. They conduct experiments in several different benchmarks and find Boost consistently outperforms previous methods in terms of harmlessness and performance. Additionally, further analysis demonstrates Boost is robust, computationally efficient and compatible with other alignment-stage solution.

### Strengths
* This paper is well-written, with appropriate tables and figures to demonstrate their idea and motivation.
* Alignment-time harmfulness prevention is quite interesting to me. This once-for-all method for harmful content prevention sounds promising and efficient.
* Boost demonstrates decent performance in various benchmarks and experiment settings.

### Weaknesses
 * Limited metrics. This work only reports harmful scores and fine-tuning accuracy. However, one intuitive limitation of alignment-time harmfulness prevention methods is they could hurt aligned LLMs' performance. The author should consider adding this experiment and testing the aligned LLMs with and without Boost directly.
* Section 3.2 is not convincing enough. The authors try to validate the concept of harmful perturbation in Section 3.2. However, the Figure 2 they used to demonstrate this is something too simple and not convincing enough. The figure only shows the loss decreasing with more training steps, which is expected for any training process, and does not specifically demonstrate the concept of harmful perturbation.

### Questions
I suggest adding one experiment to test the aligned LLMs with and without Boost directly, to demonstrate potential robustness or limitation of the alignment-time method against harmful fine-tuning.

### Soundness
3

### Presentation
3

### Contribution
3
