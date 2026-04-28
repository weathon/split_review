# Reward Model Ensembles Help Mitigate Overoptimization

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
\vspace{-2pt}
Reinforcement learning from human feedback (RLHF) is a standard approach for fine-tuning large language models to follow instructions. As part of this process, learned reward models are used to approximately model human preferences. However, as imperfect representations of the ``true" reward, these learned reward models are susceptible to \textit{overoptimization}. \citet{gao2023scaling} studied this phenomenon in a synthetic human feedback setup with a significantly larger ``gold" reward model acting as the true reward (instead of humans) and showed that overoptimization remains a persistent problem regardless of the size of the proxy reward model and training data used. Using a similar setup, we conduct a systematic study to evaluate the efficacy of using ensemble-based conservative optimization objectives, specifically worst-case optimization (WCO) and uncertainty-weighted optimization (UWO), for mitigating reward model overoptimization when using two optimization methods: (a) best-of-n sampling (BoN) (b) proximal policy optimization (PPO). We additionally extend the setup of \citet{gao2023scaling} to include $25\%$ label noise to better mirror real-world conditions. Both with and without label noise, we find that conservative optimization practically eliminates overoptimization and improves performance by up to $70\%$ for BoN sampling. For PPO, ensemble-based conservative optimization always reduces overoptimization and outperforms single reward model optimization. Moreover, combining it with a small KL penalty successfully prevents overoptimization at no performance cost. Overall, our results demonstrate that ensemble-based conservative optimization can effectively counter overoptimization.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the overoptimization in the reward model for the RLHF problem and applies several methods to reduce the overoptimization in RLHF. Overall the reviewer believes this submission is above the acceptance bar, but it has some writing issues that can be further improved.

### Strengths
1. The experimental results look promising.
2. The overoptimization problem is a novel and important problem to the LLM community.

### Weaknesses
1. [Major] There are some writing and presentation issues in the manuscripts. While this manuscript extensively refers to [1] in the writing, the reviewer would recommend the authors update the paper so that the current submission does not require the readers to read [1] to understand the submission thoroughly. See detailed comments in [Questions].
2. [Minor] For paragraph Supervied Fine-tuning in Section 4.3, the hyperlink `(see Section 4.1 for details)` seems to be broken. In addition, the reviewer cannot find any more details in section 4.1 for splitting the AlpacaFarm dataset, perhaps the authors can clarify this?

### Questions
1. What does the KL divergence in the x-axis in Figure 2 mean? The reviewer understands [1] also contains similar figures that study the gold score against the KL divergence, and the reviewer believes the authors are using a similar setting. However, the reviewer is unclear which KL divergence is Figure 2 referring to. The authors could either update the caption of Figure 2 or provide a better description of the x-axis to improve the readability.
2. Figure 3 and Figure 4 also have the same issue discussed – perhaps the authors can clarify what is the KL divergence in both figures and why they scale differently. E.g., in Figure 3 the x-axis is from 0-8, while in Figure 4, the x-axis is from 0-150. The reviewer understands that [1] has similar figures, but it will be better if the authors clarify this, so that other readers do not need to refer back to [1] for understanding this submission. Similarly in Figure 5 - 7.

[1] Gao, Leo, John Schulman, and Jacob Hilton. "Scaling laws for rew

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the issue of reward model overoptimization in Reinforcement Learning from Human Feedback (RLHF), a technique used to fine-tune large language models. Overoptimization occurs when learned reward models, imperfect representations of true human preferences, lead to undesirable behavior. This paper builds on previous work by Gao et al. (2023) who demonstrated the persistence of overoptimization even with large “gold” reward models and extensive training data. The paper explores the effectiveness of ensemble-based conservative optimization (WCO and UWO) in mitigating overoptimization when using BoN sampling and PPO optimization methods. Additionally, the research extends the previous setup by introducing 25% label noise to better simulate real-world conditions. The findings reveal that conservative optimization significantly reduces overoptimization, improving performance by up to 70% for BoN sampling. For PPO, ensemble-based conservative optimization outperforms single reward model optimization and minimizes overoptimization when combined with a KL penalty, without sacrificing performance. In summary, the authors show that ensemble-based conservative optimization presents a promising approach for addressing the challenge of overoptimization in RLHF, leading to more robust and reliable fine-tuning of large language models.

### Strengths
1. This paper provides extensive empirical evidence that suggests that ensemble-based methods can improve robustness of RMs and reduces overoptimization, which makes the claims of the paper well-supported.

2. The paper studies the important problem in RLHF, i.e. reward overoptimization, and presents various methods that clearly mitigate such a challenge. I think the paper is of value to the RLHF community.

### Weaknesses
1. While the empirical results are quite comprehensive in the paper, the model size seems a bit small with the biggest RM being 1.3B. Given Figure 8, it seems that the gain of the ensemble-based methods diminishes as the model size increases. It would important to investigate if ensemble-based methods have little gain with even bigger models, which are more commonly used by users.

2. From Figure 9, it seems that with bigger dataset size (46K), ensemble-based methods are not that much better than the single RM. Is it expected that with even more data, which in practice is usually true, the difference between ensemble-based methods and single RM will further shrink? It would be helpful to further study this perspective.

### Questions
Please clarify and investigate the two questions presented in the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of reward model optimization in training of LLM chatbots: when optimizing a learned reward model initially improves the chatbot's performance under "true" human preferences but eventually the performance decreases as the learned reward ceases to be a good proxy. The authors propose training an ensemble of reward models instead of a single one to mitigate this. The ensemble is trained from different random seeds and then the optimization target is either the mean of the reward models' outputs, the minimum (WCO), or the mean minus a variance penalty (UWO). A number of experiments are performed on best-of-n (BoN) and PPO optimization of reward models using these optimization targets and they are compared to using the output of a single reward model. The results suggest that using an ensemble of reward models

### Strengths
The paper addresses a very important problem—one of the main bottlenecks to improving RLHF training and safety of LLM-based chatbots is making reward models more robust. The solution technique is not particularly novel, as pessimistic optimization using an ensemble has been widely used in model-based RL, offline RL, preference learning, etc. However, I don't know of prior work that has specifically evaluated this technique for RLHF on LLM-based chatbots. Thus, I view the primary contribution of this paper as a systematic empirical study of applying this existing technique to a new problem. I think this is an important contribution but it does mean the experiments should be carefully executed.

In general, the experiments do seem to be well-done, exploring the effects of using the different ensemble-based optimization objectives in a variety of settings. Using WCO and UWO seem to pretty consistently help; while they don't allow for completely removing KL regularization in PPO, they do allow PPO to reach a higher final gold reward.

The writing is in general quite clear and the paper is easy to follow.

### Weaknesses
In terms of the experiments, one weakness is that the PPO experiments seem to be mostly done with a single random seed, while due to the high noise in RL training it is best to use a few random seeds (see https://arxiv.org/abs/2108.13264, https://arxiv.org/abs/2304.01315). Specifically, the reported results could be highly dependent on the particular random initialization and environment interactions, making it difficult to draw robust conclusions about the effectiveness of the proposed ensemble methods. The absence of multiple runs makes it unclear whether the observed improvements are statistically significant or simply due to chance. It is important to demonstrate the consistency of the results across different seeds to ensure the reliability of the findings.

Another weakness of the results is that it's hard to know how to interpret the gold reward. How much better is an LLM with an average gold reward increase of 0.5 vs. 0.4?  The paper lacks a clear, interpretable metric that directly reflects the quality of the generated text from a user perspective. While the gold reward is a proxy for human preference, it is not immediately clear how changes in this metric translate to actual improvements in the chatbot's performance. AlpacaFarm and others use a win-rate which is more interpretable—it might be helpful to report that for your results as well so that it's easier to understand exactly how much better using an ensemble is.  Without this, it's hard to assess the practical impact of the proposed method.

The way the PPO results are presented analogously to Gao et al. also feels a bit strange. According to Figures 4 and 5, the ensemble-based optimization objectives only outperform a single reward model at the very end of PPO training. I'm not sure why it's important to see all the intermediate KL and reward values when early-stopping is not generally used with RLHF PPO training. The intermediate values are not as relevant as the final performance. I found Figure 7 to be the best comparison of the different optimization objectives. It would be particularly interesting to see a variation of Figure 7 where each the sqrt(KL) and gold reward is plotted for each combination of (optimization objective, KL coefficient) since the KL coefficient is the actual "knob" used to adjust how much optimization is occurring in practice (not the amount of training time).

Here is one paper that should probably be included in the related work as they also evaluate using ensembles of LLM-based reward models: https://arxiv.org/pdf/2203.07472.pdf. Their paper is focused on active learning, not reward optimization, so it's not directly comparable, but it does relate to your conjecture that "uncertainty estimates from the ensemble may also help improve sample efficiency of human feedback in this setup" on page 9.

Small issues/typos:
* Bottom of page 5: in two places you say "for PPO, WCO, and UWO" but the second comma should be removed

### Questions
Related to the weaknesses above:
 * What are the results of running PPO across 3-5 random seeds for the various optimization objectives? How much variance is there across seeds?
 * How much does the gold reward increase from using an ensemble correspond to in terms of win rate or other measures of quality?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors tackles the over-optimization issue in RLHF with reward model ensembles. This is achieved by training multiple reward models, each with identical data but different random seeds. These reward models are then used for ensemble-based optimization objectives, including worst-case optimization (WCO) and uncertainty-weighted optimization (UWO) for best-of-n sampling (BoN) and PPO (proximal policy optimization). Combined with a 25% label noise to mirror real-world settings, the authors show UWO and WCO can effectively mitigate overoptimization.

### Strengths
* **Simple yet elegant approach**: the authors only used different random seeds to train the reward function, yet it can significantly improve gold score performance, especially with BON.
* **Reproduced overoptimization with OSS (open-source software) models**: the authors are the first to study and reproduce RM overoptimization with open-source models.
* **Experiments across multiple model sizes / data sizes**: the authors conducted a comprehensive analysis, which offers insights.

### Weaknesses
 **Lack of account for random seeds**: the results do not look smooth for Figure 4 / Figure 8. The results could be improved by running with at least 3 random seeds and recording the error bars.

> we use the complete dataset of 46, 000 prompts for reward model training and train all the reward models for 5 epochs. 

>We use all the available training data for the training of every reward model as
training on lesser data results in higher validation loss and poorer performance (Lakshminarayanan
et al., 2017). Unless stated otherwise, we train an ensemble consisting of five reward models.

Why train for 5 epochs? What is the training and the validation accuracy of the reward model? In Figure 15, can you show me the epoch as the x-axis? Steps can be confusing as it is related to the batch size / gradient accumulation / how you log.

> we only evaluate BoN for a maximum of nmax = 12, 500 samples , which roughly equals 8.4 nats of KL

Why nmax? Does this mean for some of them he use less than 12500 samples?

> we train for 3000 PPO steps.

How many episodes?


> Figure 3

Why do you have two y-axis? Do the proxy RM and the gold RM have different RM scales? How are these scales defined?


> Figure 6 and 7 

Figure 6 and 7 seem contradictory? KL penalty = 0 gets 0.15 gold score, but in figure 7 KL penalty = 0 gets 0.03 gold score?

> Figure 8

Why does PPO underperform BoN in 1.3B setting according to Gold Score? Gao et al (2023) show 1.2B PPO outperforms 1.2B BoN

> Appendix C

How does these two KL distance calculation Gold RM performance?


> We train a fixed number of proxy reward models using
identical data and hyperparameters but with different random seeds

But I assume data shuffling is different? There are really multiple random seeds:

* query dataset seed
* reward model seed
* policy model seed


> Figure 4
Why is single RM experimented with KL=150 but not the other types?

### Questions
> we use the complete dataset of 46, 000 prompts for reward model training and train all the reward models for 5 epochs. 

>We use all the available training data for the training of every reward model as
training on lesser data results in higher validation loss and poorer performance (Lakshminarayanan
et al., 2017). Unless stated otherwise, we train an ensemble consisting of five reward models.

Why train for 5 epochs? What is the training and the validation accuracy of the reward model? In Figure 15, can you show me the epoch as the x-axis? Steps can be confusing as it is related to the batch size / gradient accumulation / how you log.

> we only evaluate BoN for a maximum of nmax = 12, 500 samples , which roughly equals 8.4 nats of KL

Why nmax? Does this mean for some of them he use less than 12500 samples?

> we train for 3000 PPO steps.

How many episodes?


> Figure 3

Why do you have two y-axis? Do the proxy RM and the gold RM have different RM scales? How are these scales defined?


> Figure 6 and 7 

Figure 6 and 7 seem contradictory? KL penalty = 0 gets 0.15 gold score, but in figure 7 KL penalty = 0 gets 0.03 gold score?

> Figure 8

Why does PPO underperform BoN in 1.3B setting according to Gold Score? Gao et al (2023) show 1.2B PPO outperforms 1.2B BoN

> Appendix C

How does these two KL distance calculation Gold RM performance?


> We train a fixed number of proxy reward models using
identical data and hyperparameters but with different random seeds

But I assume data shuffling is different? There are really multiple random seeds:

* query dataset seed
* reward model seed
* policy model seed


> Figure 4
Why is single RM experimented with KL=150 but not the other types?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
