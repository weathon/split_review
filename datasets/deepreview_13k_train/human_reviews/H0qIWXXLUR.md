# Learn Your Reference Model for Real Good Alignment

- Decision: Accept
- Scores: 8, 3, 8, 5, 6

## Abstract
Despite the fact that offline methods for Large Language Models (LLMs) alignment do not require a direct reward model, they remain susceptible to overoptimization. This issue arises when the trained model deviates excessively from the reference policy, leading to a decrease in sample quality. We propose a novel approach of offline alignment methods, called Trust Region (including variants TR-DPO, TR-IPO, TR-KTO), which dynamically updates the reference policy throughout the training process. Our results show that TR alignment methods effectively mitigate overoptimization, enabling models to maintain strong performance even when substantially deviating from the initial reference policy. We demonstrate the efficacy of these approaches not only through toy examples that exhibit reduced overoptimization, but also through direct, side-by-side comparisons in specific tasks such as helpful and harmless dialogue, as well as summarization, where they surpass conventional methods. Additionally, we report significant improvements in general-purpose assistant setups with the Llama3 model on the AlpacaEval 2 and Arena-Hard benchmarks, highlighting the advantages of Trust Region methods over classical approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Recent literature on Offline RL LM fine-tuning methods, such as DPO, IPO, KTO etc, involve avoiding training an explicitly reward model (RM) and directly optimizing the LM from the offline preferences. However, these methods tend to over-optimize the data, such that, the probabilities of both the chosen and rejected responses from the preferences decrease compared to the reference LM and rather assign higher probability to out-of-distribution (OOD) responses. The paper tries to address this main over-optimization issue of current Offline RL approaches but bringing in ideas from Trust Region optimization. Their key idea is to modify the existing offline RL methods by making the reference LM in their training objective a moving target. Thereby, they hypothesize that the current policy will make more reasonable updates, that fix the over-optimization issue (i.e. the likelihood of chosen responses increases while rejected response still decreases). To make the reference policy moving target, they propose two simple strategies:
1. Soft Update: weighted interpolation between previous reference LM and current updated LM that is being trained. After the update, the gradients are no longer propagated from the new reference LM.
2. Hard Update: After every $\tau$ steps, the current policy is copied over the reference policy.

To support their intuition, they derive the second-order derivative of the DPO objective and show that it leads to a curvature-less loss region. Their hypothesis is that this curvature-less loss landscape leads to a decrease in the probability of the human-preferred responses, ultimately leading to OOD responses.

Their experimental setup involves comparing baseline offline RL objectives: DPO, IPO, and KTO with their Trust Region counterparts, TR-DPO, TR-IPO, and TR-KTO. They use the Anthropic HH and Reddit TL;DR dataset for preliminary evaluation with Pythia models and further experiment with Llama-3 8b models on AlpacaEval 2 and Arena-Hard benchmarks. 

Overall, their results suggest that TR version of offline RL works on average better than without for both soft and hard update rules with specific parameters (0.5 or 0.6 interpolation parameter for soft update and $\tau = 512$ steps for hard update).

### Strengths
- Work on a well-motivated and well-known problem of overoptimization in DPO-like Offline preference optimization methods.
- They give a new perspective on the issue with DPO objective by analyzing the second-order derivative.
- A simple solution to fix the issues with offline methods that have encouraging results across many datasets and model families.

### Weaknesses
 - Although the intuition about the curvature-less landscape is interesting, I am not able to understand from this why would the chosen probability decrease. From my understanding, DPO and the like only focus on the margin and not the raw values and potentially decreasing both of them (the rejected likelihood faster than chosen) is the easiest way to reduce the loss according to gradient update. 
- The TR solution to fix the overoptimization in online RL makes sense because the samples are drawn from the reference policy during optimization. It is unclear why this would help in the offline setting since subsequent reference LMs will be further out of distribution compared to the offline preference dataset.


### Questions
- Does the intuition about the curvature less loss hold also for other DPO-like objectives (example, IPO and KTO)?
- I really like the likelihood analysis of the toy dataset example in Figure 2. However, I didn't see a similar analysis for the experiments with practical datasets. Does TR-DPO and others actually increase chosen preference likelihood in real datasets? If yes, I'd appreciate it if the authors included comparison plots of DPO vs TR-DPO with real data.
   - Follow-up for toy dataset analysis: Even with TR methods, I initially see a drop in chosen probs, followed by recovery and almost memorization towards the end of optimization. Do the authors have an intuition for why this initial drop in chosen likelihood happened?
- In my experience with offline RL objectives, the overoptimization is heavily correlated with increased length. Do authors have numbers comparing the average output length of TR methods vs baseline objectives? I would trust the results much more if I see the evidence that TR methods are not susceptible to length hacking.
- Of course, it is hard to evaluate all methods within an experiment setup, but I wonder if the authors are aware of this previous work which also attempts to solve the drop in chosen likelihood problem "Noise Contrastive Alignment of Language Models with Explicit Rewards" (chen et al. 2024) https://arxiv.org/pdf/2402.05369.

### Soundness
3

### Presentation
4

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
This paper proposes an enhancement to offline alignment methods for Large Language Models (LLMs), addressing the challenge of overoptimization, where a model diverges excessively from its initial reference policy, degrading alignment and sample quality. The authors introduce the Trust Region (TR) approach, which updates the reference policy dynamically during training. They implement this via soft and hard updates within three variants: TR-DPO, TR-IPO, and TR-KTO. The results show moderate performance improvements on tasks like dialogue alignment and summarization,

### Strengths
1. The paper tackles a well-known issue in offline alignment—overoptimization—which is relevant for applications involving LLM alignment with human preferences. The focus on dynamically updating reference policies is a step toward mitigating this issue, offering a more stable alignment during training.
2. The experimental setup is comprehensive, involving multiple datasets (task-specific and general-purpose) and benchmarks.
3. The structure and explanation of the TR approach, including its soft and hard update methods, are clearly presented. This makes the methodology easier to understand and potentially reproducible for future research.

### Weaknesses
1. Despite the theoretical motivation, the empirical gains presented by the TR approach are relatively minor. In many cases, improvements over baseline methods (DPO, IPO, KTO) are modest, which may limit the practical significance of the proposed approach. Specifically, while the authors report win rate improvements, the absolute gains in terms of actual task performance (e.g., ROUGE scores for summarization, or turn quality in dialogue) are not substantial enough to demonstrate a clear practical advantage. The reported improvements could be within the margin of error or due to hyperparameter tuning rather than the core methodology itself. A more rigorous statistical analysis, including confidence intervals and effect sizes, would be necessary to validate the significance of these improvements.
2. The approach of updating the reference policy is somewhat incremental in nature, as it primarily modifies existing alignment methods (DPO, IPO, KTO) rather than introducing a fundamentally new framework for offline RLHF alignment. This limits the originality of the contribution, especially given the relatively minor performance improvements reported. The core idea of using a trust region is not novel in reinforcement learning, and the application to offline alignment, while relevant, does not introduce a paradigm shift. The modifications to DPO, IPO, and KTO are relatively straightforward, and the paper lacks a deeper theoretical analysis of why these specific modifications are effective, beyond the general intuition of mitigating overoptimization.

### Questions
1. While the TR approach appears to mitigate overoptimization initially, a more detailed analysis of its performance in long-term deployments would be valuable. Specifically, could the authors provide empirical results on how the approach maintains alignment stability over extended training iterations?

### Soundness
3

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
5

### Summary
The authors proposed a new offline paradigm for aligning large language models using preference optimization methods. They explored the overoptimization problem in state-of-the-art preference optimization methods and showed that the current methods suffer from this issue. To overcome this problem, they updated the reference models with the weight of the policy model on safe and hard settings. They showed that this method outperforms the vanilla across different metrics.

### Strengths
The main strengths of this paper are comprehensive experiments and analysis of various benchmarks and models. Also, they achieved impressive performance with a simple change on the optimization part, which means updating the weight of the reference model during the optimization part.

### Weaknesses
This paper showed impressive improvement on different benchmarks; however, I have multiple concerns about this paper.


1.  **Lack of generalizability**. The authors called their method a new paradigm for offline alignment techniques. However,  some new methods, like SimPO, CPO, and TPO, achieve impressive performance compared with DPO, IPO, and KTO by removing the reference model. So, I am curious how we can call it a new paradigm.

2.  **Lack of novelty**. The ORPO method, motivated by maximizing the likelihood of a bad response during the SFT, proposed another method to overcome the issue. They showed that this method can also resolve the overoptimization, and the log probability of the chosen response increases during the optimization (refer to Figure 7 in the ORPO paper).


3.  **Lack of explanation**. In paper, the authors to satisfy their hypothesis, they did some experiments on OOD trajectory probability, as shown in Figure 2. However, this experiment is not clear and I am wondering which data is used as out-of-distribution (OOD).



4.  **Huge discrepancies and a lack of exploration of hyper-parameters for different methods**. The results reported for LLama3-Base on AlpacaEval 2 and ArenaHard for DPO, IPO, and KTO in the SimPO paper and this paper are very different. The discrepancy on ArenaHard for IPO is more than 11%, and for DPO, it is more than 5%. I refer the authors to Table 4 in the SimPO paper []. Also, It seems the authors didn’t choose the best hyperparameter for DPO. In Appendix D.1 they selected 1.0e-6 for llama as the learning rate for DPO, while learning 5.0e-7 is the best for DPO. We refer to the SimPO paper because the DPO model they fine-tuned has better performance than this paper.


5.  **Lack of efficiency analysis**. This method needs to keep the reference model in Memory during the optimization. To improve the efficiency of the DPO, KTO, and IPO, the value of the reference model can be calculated before training. So, I think efficiency analysis shows different aspects of this method. Reporting the Peck GPU memory and run-time is helpful.


6. Recent papers like Zephyr and SimPO showed that preference optimization methods not only need more steps for optimization but also, after one epoch, will be overfitting on data. However, the proposed method requires large steps for hard update settings.

### Questions
I have a couple of questions and suggestions. I appreciate the authors answering the following:


1. The same dataset generated by llama3-instruct-8b was prepared by the SimPO paper before. I suggest the authors to fine-tuned the LLaMA3-8b-SFT (https://huggingface.co/princeton-nlp/Llama-3-Base-8B-SFT) with their method on this UltraFeedback (https://huggingface.co/datasets/princeton-nlp/llama3-ultrafeedback) and report the AlpacaEval and ArenaHard.
 
2. most of the analysis on KL divergence is on Pythia 2.8. I am happy to see some analysis on LLama3 models to verify the observation.

3. I suggest the authors evaluate the llama3 models on the MixEval (https://github.com/Psycoy/MixEval/?tab=readme-ov-file) benchmark, too.

### Soundness
2

### Presentation
4

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
The paper introduces a novel paradigm for aligning Large Language Models through offline methods. The authors propose Trust Region (TR) methods, including TR-DPO, TR-IPO, and TR-KTO, which dynamically update the reference policy during the training process. The paper claims that these methods effectively mitigate overoptimization, allowing models to maintain strong performance even with significant deviations from the initial reference policy. The efficacy of these approaches is demonstrated through toy examples and specific tasks such as dialogue and summarization, where they outperform conventional methods. Additionally, the paper reports significant improvements on general-purpose assistant benchmarks using the Llama3 model.

### Strengths
1. The paper introduces a novel Trust Region (TR) approach that significantly mitigates the issue of reward overoptimization in offline learning of Large Language Models. By dynamically updating the reference policy during the training process, the proposed method potentially offers a more robust alignment technique.

2. The paper conducts a comprehensive set of experiments across various tasks and models. The authors have meticulously detailed their experimental procedures and published their parameters, which not only supports the credibility of their findings but also allows for reproducibility by other researchers in the field. 

3. The paper demonstrates a strong understanding of the underlying issues in offline alignment methods and provides a clear motivation for the proposed Trust Region methods. The authors have effectively communicated the problem of overoptimization and how their approach can mitigate this through updating the reference policy, which is a conceptual strength of the paper.

### Weaknesses
1. The methods proposed in this paper—soft and hard updates for the reference policy—are fundamentally extensions of existing approaches rather than novel contributions. Soft updates, which involve a weighted average of the current and previous model parameters, are commonly used in reinforcement learning to stabilize training and do not introduce new mechanisms or insights; similarly, hard updates, which periodically replace the reference policy with the current policy, reflect established practices without significant advancement. While the introduction of Trust Region (TR) methods suggests a framework, it does not provide a substantial departure from conventional strategies, as the core mechanics of updating the reference policy remain similar to existing techniques. The paper lacks a clear demonstration of how these TR methods offer a fundamentally new approach to the problem of overoptimization, rather than simply applying existing techniques in a new context.

2. The claim that this update will "increase the curvature of the loss landscape" is not backed by theoretical support. While the authors suggest that updating the reference policy can help the model escape overoptimized regions, the mechanism for alleviating overoptimization remains unclear. The paper lacks a rigorous mathematical analysis to support the claim that dynamic updates to the reference policy will lead to a more favorable loss landscape. The suggestion that moving away from the SFT policy is "not inherently bad" could be misleading, as potential negative consequences, such as a degradation in the model's ability to follow instructions or a decrease in the quality of generated text, are not addressed.

3. The paper relies heavily on automatic evaluation methods, such as GPT-4, to assess model performance. Using a single model (like GPT-4) as a judge in evaluations could introduce bias, as it may not fully capture the nuances of human evaluation. The paper would be strengthened by including human evaluation or a discussion on the reliability of the evaluation methods used. The paper does not adequately address the potential limitations of using a single LLM as an evaluation metric, such as the possibility of the evaluation model being biased towards certain types of responses or failing to recognize subtle differences in quality.

### Questions
1. What is the mechanism for alleviating overoptimization? Please investigate it more clearly.

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
The paper, titled Learn Your Reference Model for Real Good Alignment, presents a new method for aligning large language models (LLMs) by introducing the Trust Region (TR) approach. This method dynamically updates the reference policy throughout training to reduce overoptimization issues in offline alignment methods. Three key variations are proposed: TR-DPO, TR-IPO, and TR-KTO, which improve upon existing alignment methods by better managing the divergence from the reference policy.

### Strengths
+ The introduction of Trust Region methods to continuously update the reference policy reduces overoptimization issues, maintaining model performance even when deviating from the initial reference model.
+ The methods outperform existing baselines in tasks like summarization and dialogue alignment, showing significant improvements in win rates on benchmarks such as AlpacaEval 2 and Arena-Hard.

### Weaknesses
 - The paper also lacks defense performance against well-known jailbreak methods, such as GCG and GPTFuzzer.
- The paper does not deeply analyze the potential trade-offs between this additional cost and the performance gains.
- More on questions.

### Questions
The paper relies heavily on automatic evaluation methods using GPT-4 as a proxy for human judgment, which could raise concerns about the robustness of the evaluation.

### Soundness
3

### Presentation
2

### Contribution
3
