# Progressively Label Enhancement for Large Language Model Alignment

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 5, 3

## Abstract
Large Language Models (LLM) alignment aims to prevent models from producing content that misaligns with human expectations, which can lead to ethical and legal concerns. 
   In the last few years, Reinforcement Learning from Human Feedback (RLHF) has been the most prominent method for achieving alignment.
   Due to challenges in stability and scalability with RLHF stages, which arise from the complex interactions between multiple models, researchers are exploring alternative methods to achieve effects comparable to those of RLHF.
   However, these methods often rely on large high-quality datasets.
   Despite some methods considering the generation of additional data to expand datasets, they often treat model training and data generation as separate and static processes, overlooking the fact that these processes are highly interdependent, leading to inefficient utilization of the generated data.
   To deal with this problem, we propose {\ours}, i.e., Progressively Label Enhancement for LLM Alignment, a framework that dynamically adjusts the model’s training process based on the evolving quality of the generated data.
   Specifically, we prompt the model to generate responses for both the original query and the query guided by a set of carefully designed principles, and then utilize a dynamic threshold to determine the appropriate training approach for both responses based on their corresponding reward scores. 
   Experimental results demonstrate the effectiveness of {\ours} compared to existing LLM alignment methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new method for aligning large language models. 

The method proposed in the paper is PLE, i.e. Progressively Label Enhancement for LLM Alignment. This framework can dynamically adjust the model's training process based on the evolving quality of the generated data. 

Specifically, the method designs a set of principles and uses these principles to guide the model to generate good responses, and then designs a ranking loss and a re-weight loss to train the language models. 

On the dataset of HH, the proposed is demonstrated to be better than PPO, and DPO, these commonly used methods.

### Strengths
Guiding the language model with a set of principles is a straightforward yet effective approach for generating high-quality responses. This simplicity suggests promising potential for broader application of this method in the future.

### Weaknesses
1. **Lack of Ablation Study**: The training loss comprises a ranking loss and a re-weighting loss; however, the paper does not include an ablation study to analyze the individual contributions of these losses to the model’s performance. It is unclear how much each loss contributes to the final performance, and whether one loss is more critical than the other. Without this analysis, it's difficult to understand the necessity of both components, and if a simpler loss function could achieve comparable results. For example, it would be beneficial to see results with only the ranking loss, only the re-weighting loss, and with both, to quantify their impact.

2. **Limited Scope of Principle-Based Evaluation**: While using principles proves effective in generating quality responses, the evaluation is limited to alignment tasks. This narrow focus leaves the generalizability of the approach uncertain. Testing across a wider range of tasks, such as mathematical reasoning, summarization, and controlled text generation, would provide stronger evidence of the method’s broader applicability. The current evaluation only shows the method's effectiveness on a specific type of task, which may not translate to other tasks. It is important to test the method on a diverse set of tasks to demonstrate its robustness.

3. **Lack of Systematic Study on Principle Design**: The paper does not systematically examine the design of principles or how different principles impact the model’s overall performance. The paper does not provide any analysis on how the choice of principles affects the model's behavior. For example, it is not clear if some principles are more important than others, or if some principles conflict with each other. A systematic study on the design of principles is needed to understand the method's limitations and potential for improvement.

### Questions
Why GPT-4 is not used for annotation when calculating the win rates?

### Soundness
2

### Presentation
2

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
This paper proposed progressively label enhancement for LLM alignment, where the authors prompt the model to generate responses for both the original query and the query guided by a set of carefully designed principles, and then utilize a dynamic threshold to determine the appropriate training approach for both responses based on their corresponding reward scores.
The central idea lies in that at the earlier stage of training, the method tries to use pairs with larger reward margin, as the training proceeds, the reward margin can be decreased.

### Strengths
1. prompting with principles is interesting and important; 
2. the idea of changing training data progressively using reward function is interesting;
3. there are positive performances in the experiment.

### Weaknesses
1. the method does not seem sound to me, there are a few questions left unclear:
1) Essentially, this is a PPO method? so why does EQ 2 have no regularization terms (the KL term between \pi_{sft} and \pi_{\theta};
2) in Eq 7 and the line 15 of the algorithm, the tau seems to be a constant all the time, where you should have \tau_{t+n} = \tau_{t}*\alpha?
3) in the loss functions, normally we are optimizing with mini-batch, which sums all the log probability together in a mini batch (because samples are IID), so a better formulation should be like log\pi_{\theta}? Instead, the authors directly used the probability distribution, which is weird for me. 
2. About evaluation:
1) the authors only tested the method with a base model of LLama3 8B, where I believe more base models should be verified, for instance , chatglm-x, qwen-x, and particularly with larger sizes to see if the claims still hold on larger models;
2) the authors only experimented with one dataset, of course more datasets should be validated with;
3) the authors measured the winrate and reward scores over baselines, but it is more interesting to see the results on other benchmarks, for instance, IFEval, MATH, BBQ, and other typical benchmarks.

### Questions
See my comments in weaknesses. 
note: I did not check into the details the theoretical analysis.
Minor comment:
DPO is not short for direct policy optimization, it is for direct preference optimization.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a novel language model alignment method by adaptively adjusting the training process based on the generated data quality, which is computed by determining whether a reward score of principle-guided response is higher than the generated response. The authors provide a theoretical analysis to show that the proposed method would lead to a convergence to the optimal model. The experiments are conducted on a single dataset, and the method is shown to achieve a higher performance than the baseline methods (vanilla SFT, DPO, PPO, RAFT).

### Strengths
* Proof of the convergence is provided in the work, showing evidence of the effectiveness of the proposed method on the theoretical aspect.

* This paper considers the training process along the data quality together, giving a novel perspective compared to prior alignment works that consider training and data generation as two separate processes.

* The paper is clear and easy to understand.

### Weaknesses
 * The experiment is only conducted on a single dataset and a single model variant. The paper could be strengthened by a series of post-training analyses.

* Although the method is shown to have better performance on the Helpful and Harmless (HH) dataset, it would be useful if the authors could present a complexity comparison between the baselines, which may seem to be more efficient than the proposed method.

### Questions
* Sec 4.1.: `Language model alignment requires a large amount of high-quality data` Consider LIMA, for example, only contains 1k examples, although its base model (65B) is larger than the model used in this work. 

* How are the principles integrated into the response generation? How many of such generations are required?

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
This paper proposes the Progressively Label Enhancement (PLE) framework to improve LLM alignment with human expectations. PLE dynamically adjusts the training process by weighting both principle-guided and original responses based on their reward scores, enhancing data utilization efficiency. Experiment results show that PLE outperforms existing studies.

### Strengths
1. The proposed approach is well-motivated.  
2. The proposed approach is novel.  
3. The approach show good performance.

### Weaknesses
1. Although the approach is new, the high-level idea of using prompt to instruct LLM to generated human preferred answer and using reward to optimize the LLM is not new.  
2. The paper evaluates model performance using a reward model. It would be better more details of the reward model can be provided. Also, it is possible that the reward model has bias. It would be better that the authors can discuss the effect of the reward model. Otherwise, trying multiple reward models may address the issue.  
3. Some details of the experiments are missing. For the results of SFT, PPO, DPO in Table 2, are they the results obtained by the LLM trained by the authors? or they are the results of the instruct version of LLaMA-3 released by Meta? If they are the results obtained from the author, I'm curious about the results of directly evaluating the instruct version of LLaMA-3.

### Questions
1. It would be better to make the font size of Figure 1 larger.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the decoupling of data generation and model training in current RLHF methods by proposing PLE (Progressively Label Enhancement for LLM Alignment). PLE dynamically adjusts the training process based on the quality of the generated data to maximize its utility. Specifically, the contributions of the paper are as follows:

1. The authors are the first to identify that previous alignment methods overlooked the coupling of data generation and training. They introduce PLE to combine these two stages, demonstrating reasonable performance compared to baselines in experiments.

2. The authors theoretically prove that, through a progressively updated threshold strategy, PLE can bound the error rate between the trained model and the optimal model.

### Strengths
The authors identify the decoupling issue between data generation and model training in current methods, and propose PLE to improve data utilization. Through both automatic and human evaluation on the HH dataset, they demonstrate that PLE outperforms baseline approaches. The authors theoretically prove that with a progressively updated threshold strategy, PLE can bound the error rate between the trained model and the optimal model.

### Weaknesses
1. The authors provide comparative experiments with 4 baselines on the HH dataset and include training curves comparing principle-guided responses with original responses, but I believe the experiments remain insufficient despite the theoretical proof.

- Additional evaluations on datasets like IMDb (as seen in DPO), the Reddit TL;DR summarization dataset, and UltraFeedback would offer valuable insights into model performance on diverse data using PLE. 
- It would also be beneficial to test generalization capabilities on out-of-distribution data—for instance, training on UltraFeedback and evaluating on HH.
- Including additional evaluation metrics, such as MSSTR and Distinct-n(as seen in RAFT), could enhance the credibility and robustness of the results.

2. The paper lacks sufficient motivation for introducing progressive approaches and label enhancement methods. Additionally, the experimental results show somewhat minor improvements over the baselines and lack the comprehensiveness needed to justify these components(see weakness 1 for suggestions).

### Questions
1. When training baselines like SFT and DPO, it appears that the authors used preference responses from the HH dataset. I’m curious how the baselines would perform if principled guided responses were used as preference responses for training instead.

2. A few potential typos:

    a. For PLE, is the full name “Progressively Label Enhancement for LLM Alignment” as stated on line 21, or “Selective Label Enhancement for Language Model Alignment” as on line 156?

    b. In line 333, “Reward-based Fine FineTuning (RAFT)”—it seems this is not the full name of RAFT.

3. Could the authors expand the experiments on the effects of different components of PLE (e.g., varying loss functions) or hyper-parameters? This would provide deeper insights into which parts contribute most effectively.

4. For Figure 3, how many iterations were trained in total? Are there only 8 iterations in the entire training process?

### Soundness
2

### Presentation
2

### Contribution
2
