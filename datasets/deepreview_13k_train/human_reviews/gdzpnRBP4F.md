# RLSF: Reinforcement Learning from Self-feedback for improved logical reasoning

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Large Language Models (LLMs) have demonstrated impressive capabilities in generating coherent and contextually relevant text. These models
arguably lack the ability to logically reason, an essential skill required to solving mathematical problems and programming tasks.
While step-by-step prompting approaches show some promise, they often depend on finding a suitable prompt tailored to the specific model and task.  In this work, we propose a simple, yet an effective approach to enhance reasoning capabilities by leveraging reinforcement learning (RL) and the confidence scores of a well-calibrated LLM. It involves optimising an implicit reward derived from the model's confidence levels in the answer to the reasoning task at hand.
We generate preference data and fine-tune the LLM in a similar spirit to reinforcement learning from human feedback (RLHF), but without needing any human provided labels or preferences.
Our results show that resulting reasoning abilities of an LLM improve and are transferable to other reasoning tasks. This warrants further investigation of RL as a facilitator for solving complex language tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes Reinforcement Learning from Self-Feedback (RLSF)to improve logical reasoning in LLMs by utilizing self-confidence scores instead of human feedback for model training. The authors suggest that if a language model is well-calibrated, the confidence in its responses correlates with reasoning quality. They use this self-generated confidence as a reward signal to guide reinforcement learning, aiming to improve model performance on reasoning tasks without relying on human annotations. Experimental results on Multi-Arith and GSM8K show that RLSF-enhanced models outperform baseline models in reasoning tasks.

### Strengths
-

### Weaknesses
 - The paper does not sufficiently explore related work in self-feedback or self-improving methods, such as CoT reasoning or majority-voting-based preference learning. It also lacks a comparison with these baseline methods, which could help clarify the novelty and advantage of their approach.
- The methodology section confusing and lacks specific details on the proposed model's implementation. Figure 1 depicts an inconsistency: it shows PPO as the optimization technique, while the experiments utilize DPO, introducing ambiguity regarding the methods used.
- The experimental analysis lacks sufficient depth. The paper does not demonstrate the superiority of the self-feedback-based reward model over simpler baseline methods, such as majority voting. Additionally, the high Expected Calibration Error (ECE) in the reward model suggests potential limitations in the model's capability for RL tasks, which the paper does not adequately address. 
- The proposed method is only validated on Phi-2 model. Experiments on stronger models like Phi-3, llama 3 would be helpful to demonstrate the generalization of RLSF.

### Questions
-The reward model's ECE appears high, raising concerns about the reliability of self-confidence for RL training. Could the authors address whether such a reward model is effective for reinforcement learning or provide improvements to better calibrate it?
- How to determinate if the models used in the experiments is well-calibrated? If not, can it be used for RL training, as this is the assumption of the RLSF?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes RLSF, a pipeline that trains LLM on math reasoning tasks with self-generated responses using PPO. RLSF samples the response samples through CoT decoding and ranks them according to the model's confidence in generations. By using those ranks for reward modeling, RLSF is a stand-alone pipeline without external guidance on math reasoning tasks. Along with enhancements in math reasoning tasks, RLSF generalizes over other logical reasoning tasks when trained only on math reasoning tasks.

### Strengths
1. RLSF improves the reasoning abilities of LLMs by utilizing the self-generated sequences, demonstrating strong performance in both math reasoning and logical reasoning tasks.
2. With greedy decoding, RLSF largely improves the math reasoning performance of LLMs, putting them on par with CoT decoding.
3. Some qualitative observations are presented for the reward model trained with confidence-based ranking, which is one of the paper's core contributions.

### Weaknesses
 **1. Missing references and lack of comparisons in methods for improving LLM reasoning with RL**

The paper's core contribution is self-improving the reasoning abilities of LLMs with RL(HF). While the paper leverages PPO and tests DPO as PPO's alternative in the main experiments, neither Section 2 (Related Works) nor Section 5 (Results and Discussion) addresses previous works on applying RL(HF) to LLM reasoning tasks. Some relevant previous works were not sufficiently addressed in Section 2 [1-3]. Also, [2] and [3] were proposed as specified pipelines for improving LLM reasoning abilities with DPO/PPO-based algorithms, which make them strong contenders for RLSF. Thus, incorporating some baseline experiments on related methods will strengthen the validity of RLSF.

&nbsp;

**2. Validation of reward model**

RLSF's core novelty is creating a synthetic reasoning preference dataset for reward modeling without an external labeler. The downstream performance of PPO is prone to the reward model's performance [4]. However, the paper lacks an in-depth analysis of the reward model trained with confidence-based ranking on self-generated reasoning trajectories, only having a qualitative analysis in Section 5.4. Demonstrating the performance of the reward model, such as its correlation with human preference or its ability to distinguish between correct and incorrect reasoning steps, would enhance the logic behind RLSF. Specifically, metrics like accuracy in predicting human-annotated preferences or the KL divergence between the reward model's output and a ground truth reward signal would be valuable.

&nbsp;

**3. Training configurations and hyperparameter choices**

PPO has many different hyperparameters, and its performance is sensitive to different hyperparameter choices [5,6]. However, the paper does not specify the training configurations for PPO or other baseline experiments. Also, the paper does not clearly state some ablations over different hyperparameter choices or the rationale on how they selected the hyperparameters. For example, details on the learning rate, batch size, number of PPO iterations, and the clipping parameter are essential for reproducibility and understanding the method's sensitivity. Furthermore, the paper should include a discussion on how these choices were made and what impact they might have on the final results.

&nbsp;

**4. Correlation between the performance of RLSF and the base model's reasoning ability**

The authors selected Phi-2 as a main model to test RLSF in Section 4.2 as it demonstrated the best ECE. However, in Table 1, ECE and accuracy are highly correlated in both datasets, which could raise another hypothesis that RLSF's performance could come from the strong math reasoning ability of Phi-2 in the first place. The authors should clearly show that calibration is the key, not the accuracy, as they emphasized throughout the paper. For instance, a controlled experiment where models with similar initial accuracy but different calibration scores are tested with RLSF would help isolate the impact of calibration. It would also be beneficial to show results on a wider range of models with varying initial reasoning abilities and calibration scores to further validate this point.

&nbsp;
&nbsp;

### Questions
Along with some points above, I have additional questions on RLSF:

&nbsp;


**1. Actual impact of calibration on RLSF?**

As stated by the authors, RLSF is built on top of the assumption that the initial model is well-calibrated. While the experiments with Phi-2, which is shown to be the most calibrated model out of the three models, were presented, the impact of the calibration on RLSF was not fully studied other than that. How would a less-calibrated model (e.g., Gemma-2-2B-Instruct as the least calibrated model) perform with RLSF? (this could be somewhat related to point 4 above)

&nbsp;

**2. CoT decoding with RLSF-trained model?**

While RLSF is directly compared against CoT decoding in Table 2, they are distinct methods that improve LLM in training and inference time, respectively. For this reason, CoT decoding could indeed be applied on top of an RLSF-trained model. Plus, Table 4 shows that RLSF improved the model's calibration in some tasks, implying that the RLSF-trained model could benefit even more with CoT decoding compared to the original model. Would RLSF benefit from CoT decoding regarding some insights provided in Section 5?

### Soundness
1

### Presentation
2

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
This paper proposes a novel and effective method for improving reasoning capability of large language models (LLMs) using reinforcement learning (RL). The main method proposed is similar to RL from human feedback (RLHF) where a reward model is trained from human preference data, which is then used to fine-tune the LLM using RL. The key novel idea in this paper is to use the LLM’s own confidence (token probability) of the answer tokens to train the reward model. Experiments show the RL with self-feedback method to perform competitively with more computationally expensive methods, on standard reasoning benchmarks such as GSM8K and Multi-Arith. The fine-tuned model is shown to generalize with strong performance to held-out tasks as well.

### Strengths
The method of RL with self-feedback (RLSF) using a reward model fine-tuned on the LLM’s own token probabilities is novel and likely to be of interest to the ICLR audience.

Experiments on standard logical reasoning benchmark tasks show RLSF to have competitive performance with sampling baselines while requiring less test time samples. Moreover, RLSF demonstrates significantly stronger performance on held-out tasks than the baseline methods.

The paper is well-written and the results are clearly presented. The illustrations of the reasoning traces of different methods and the distribution of rewards for reasoning traces of different quality are quite informative.

### Weaknesses
Performance of RLSF does not improve over the CoT Decoding baseline on the training tasks, Multi-Arith and GSM8K. The authors claim that the decoding cost is lower for RLSF, but this does not take into account the sampling cost incurred during data collection to train the reward model. It is possible that this approach can help improve logical reasoning beyond CoT decoding, but this is not supported by the experiments in the paper. Hence, the current results show that RLSF only provides an efficiency improvement rather than performance improvement.

RLSF requires a well-calibrated LLM to work. Experiments in the paper were done using the Phi-2 model because it is better-calibrated than Mistral or Gemma models. It is unclear how well RLSF works for poorly calibrated models or how strong this requirement is. Can the authors provide data on performance of Mistral or Gemma models with RLSF? Or provide strategies for applying it to poorly calibrated models?

The mathematical description of the answer confidence in 3.1 is quite confusing. The expression contains an index m but not variables indexed by m? What does <j mean in the subscript? Please reconsider the notation and description of the confidence definition.

### Questions
Could you describe the generalization tasks in more detail? It is not clear how much reasoning they require based on the current description.

(See also questions in the above sections)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper uses answer confidence to rank K beams for a given input prompt and trains a reward model on these rankings. The reward model is then used for standard PPO-based RL fine-tuning. Building on CoT-decoding in this way, the paper exploits the fact that more confident answers often correspond to generations with explicit reasoning, in order to fine-tune an LLM to solve reasoning problems via CoT in a self-supervised fashion.

### Strengths
The paper is well-situated within related literature. Using CoT decoding to gather data for training a reward model is a natural approach to amortising the inference cost of CoT decoding via fine-tuning. 

The test results in the domain of the fine-tuning tasks are promising, showing improvement over DPO and indicating that the fine-tuning amortises the benefit of test-time CoT-decoding.

The generalisation results show some promise with the synthetic tasks, though this is somewhat inconclusive (see Weaknesses).

Discussion of results and the strengths and weaknesses of the findings is informative.

### Weaknesses
An important baseline would be be an SFT approach, where the top-n beams in terms of confidence are accumulated across prompts into a dataset for SFT. There are many reasons why this might not do as well as the "online" RL approach used in the paper, but this comparison should ideally be made empirically.

The generalisation experiments are somewhat limited. Evaluating on more common non-math reasoning benchmarks (e.g., CommonsenseQA, MMLU, HotpotQA) would be more compelling than the synthetic tasks. This feels especially necessary given that much of the benefit of the proposed RLSF is to amortise the benefits of CoT decoding and save inference cost when generalising to new problems at test time, and given that RLSF actually does worse than greedy decoding on StrategyQA.

### Questions
Why do you think performance drops after RLSF on StrategyQA? I would be inclined to increase my score if more generalisation benchmarks are included, which show that the improvement trends on the synthetic tasks are meaningful.

Why did you jump straight to training a reward model and doing RL in this setting, rather than the SFT approach described in 'Weaknesses'? 

An enormous benefit here is the self-supervised nature. Are there problems that are less verifiable and therefore where rewards are harder to come by that might be worth applying this to?

### Soundness
2

### Presentation
3

### Contribution
4
