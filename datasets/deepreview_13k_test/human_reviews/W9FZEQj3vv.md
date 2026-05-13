# Variational Best-of-N Alignment

- Decision: Accept
- Scores: 6, 6, 3, 8

## Abstract
\beston (\bon) is a popular and effective algorithm for aligning language models to human preferences.
The algorithm works as follows: at inference time, $N$ samples are drawn from the language model, and the sample with the highest reward, as judged by a reward model, is returned as the output. 
Despite its effectiveness, \bon is computationally expensive; it reduces sampling throughput by a factor of $N$. 
To make \bon more efficient at inference time, one strategy is to fine-tune the language model to mimic what \bon does during inference. 
To achieve this, we derive the distribution induced by the \bon algorithm. 
We then propose to fine-tune the language model to minimize backward KL divergence to the \bon distribution.
Our approach is analogous to mean-field variational inference and, thus, we term it variational \bon (\vbon).
To the extent this fine-tuning is successful and we end up with a good approximation, we have reduced the inference cost by a factor of $N$. 
Our experiments on a controlled generation task suggest that while variational \bon is not as effective as \bon in aligning language models, it is close to \bon performance as \vbon appears more often on the Pareto frontier of reward and KL divergence compared to models trained with KL-constrained RL objective.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The best-of-N alignment strategy has proven very useful in generating text with high-rewards that still has a high probability under the reference model. Several studies have shown that BoN often outperforms models simply fine-tuned with RLHF. However, this improvement in BoN comes at computational overhead during inference. 

This paper proposes Variational BoN (vBoN), a scheme that converts BoN from an alignment-via-inference algorithm to an alignment-via-fine-tuning algorithm. Basically, vBoN  derives the probability distribution induced by the BoN algorithm and then approximates this distribution by minimizing the reverse KL divergence between the language model and the BoN distribution. The model is optimized for the vBoN objective using the PPO algorithm. 

The proposed objective is evaluated on controlled generation and summarization tasks, showing performance close to that of the BoN algorithm while being as cost effective as inference on the original reference model.

### Strengths
vBoN is a novel and effective approach converting BoN from an alignment-via-inference algorithm to an alignment-via-fine-tuning algorithm. Models fine tuned with the vBoN objective achieves high reward values closer to the BoN approach, while achieving probabilities closer to the reference model. Importantly, it is as cost-effective as inference on the original reference model. In comparison , the original BoN approach is N times more expensive.

Provided theoretical connections showing how vBoN is compared with other alignment objectives

### Weaknesses
Section 2 and 3 can be improved significantly by improving the notations and explanations and by bringing important details from Appendix to the main part of the paper. Currently I often find these two sections a bit confusing as well as a bit hard to appreciate some of the claims the authors have made in the paper. For example, in Eq 4, F(r(y)) will be defined as F(r(y) ) = P (r(y) < r(y) ), using Eq 5?  With this I am not sure how the vBoN objective is insensitive to applying any monotonically increasing function to the reward values?

Another important weakness of the paper is the current evals in the paper. Despite using the standard benchmarks for controlled generation and summarization, the evaluation chose not to report on standard metrics along with rewards and proximity to reference model comparisons.

### Questions
Please see my comments in the Weakness part of the reviews.

Why BoNBoN is called with that name? Please explain.

“We visualize the win rate vs. KL curves in Fig. 6a, and Fig. 6b the average rewards of generations under πθ vs. the KL divergence”. Please mention that these figures are in the appendix.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a novel optimization objective for reinforce ment learning in large language models: vBo𝑁. Inspired by the Bo𝑁 method during the inference phase, the authors have designed an innovative loss to aid model alignment training. Building on this, the authors have transformed the proposed loss into the easily optimizable vBo𝑁 by relaxing the optimization lower bound. The authors validated the potential of vBo𝑁 optimization on two tasks using the IMDB movie review dataset and the Reddit TLDR dataset, and compared it with other contemporary methods such as PPO and DPO, demonstrating the unique potential of the vBo𝑁 method.

### Strengths
- The authors conducted rigorous and thorough theoretical derivations in the paper, clarifying the process from the motivation behind the vBo𝑁 proposal to its transformation into an optimizable objective. This is highly beneficial for readers interested in optimization theory and can provide new insights for tackling more complex optimization problems.
- The vBo𝑁 method is highly effective. Moreover, despite the substantial theoretical derivations, the illustrations used by the authors to present results and compare methods are clear and easy to read, helping readers to quickly grasp the potential of vBo𝑁 for their applications.

### Weaknesses
- Less Persuasive Experiments: While we understand that conducting RLHF is always exceedingly costly, for instance, PPO requires maintaining four sets of model parameters, the fact that the validation of the vBo𝑁 method was only focused on movie review completion and text summarization datasets makes it lacks persuasiveness. We would like to understand the potential applications of vBo𝑁 in broader and more challenging tasks, such as code generation, mathematical problem solving, and multi-step reasoning. The experimental section of the paper is not as solid as the theoretical section.
- Lacking Efficiency Testing: One of the motivations behind the vBo𝑁 method is to address the additional overhead of the Bo𝑁 method during inference, which vBo𝑁 resolves by introducing additional training. Therefore, I believe that an analysis of the training costs of vBo𝑁 is a crucial issue that must be discussed in the paper. Based on the experimental results, I could even accept that the training efficiency of vBo𝑁 is slightly inferior to methods like PPO. Moreover, beyond absolute costs, relative costs are also worth considering, such as a comparison of the performance of vBo𝑁 and PPO under the same computational-power/time/data con straints. If the authors could address either of these two aspects, or preferably both, it would significantly enhance the completeness and the soundness of the paper.
- Several key symbols and terms in the formulas are not defined, making it challenging for readers to understand the equations' meaning. A glossary would greatly improve readability.
- In the "Summarization" section, the authors refer to the reward models with different names ("pythia-2.8B reward model" and "pythia-6.9B model"), but it’s unclear if these models differ in architecture or purpose (see Section 6).
- The experiments focus solely on summaries from the “relationship” and “relationship advice” subreddits for training and then evaluate performance on in-distribution and out-of-distribution Reddit posts.
- This paper provides inadequate detail when introducing the advantages and disadvantages of other alignment methods (such as RLHF and direct preference optimization). In particular, it lacks sufficient background information and details on how these methods are applied to text generation or summarization tasks , which may make it difficult for readers to understand the relative advantages of the methods proposed in this paper.
﻿
Others
-  In the paper, the authors refer to the input of the LLM as a ‘string’. Switching to the term ‘token’ would align better with most readers’ pref erence and expectations, especially there is no cross-tokenizer-aspect that requires natural language level operations in vBo𝑁.
- For those practitioners who are more focused on practical implementa tion, including a pseudocode for the vBo𝑁 alignment would enhance the readability of the paper. Moreover, vBo𝑁 does include more complex op erations beside the usual training pattern. I’d like to suggest authors to include one in the paper, even in the appendix.

### Questions
- "It is invariant to applying any monotonically increasing function to rewards" might not be entirely correct. Although monotonicity and insensitivity to reward scale are indeed related, the exact nature of this relationship is still unknown.
- The extent of the loss introduced by using the Monte Carlo estimator to maximize the lower bound of Equation (6) compared to the original formula remains unclear.
- The models used in the experiments by the authors are relatively outdated. I 'm curious if this method could achieve similar results on more recent models, such as the LLaMA-3 series.
- The trend of vBoN changes relatively smoothly with temperature adjustments; what causes this smoother trend?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a more direct preference-align method vBoN for LLMs based on the Best-of-N approach. The authors construct a new fine-tuning objective function using the scoring results from a reward model. By directly aligning the output distribution of the LLMs to the output distribution of the Best-of-N method, the authors aim to simplify the BoN inference process and achieve better alignment efficiency compared to other preference alignment methods. Experiment results are demonstrated to try to validate the claims.

### Strengths
The motivation of this article is quite clear, and it includes several experiments to support its claims. Additionally, the overall structure of the article is fairly complete, including some theoretical derivations.

### Weaknesses
1. The effectiveness of the vBon method is questionable. Although vBon utilizes reward model scoring to depict a target distribution closer to BoN, it requires a large number of samples (controlled by N or M in the article) to generate the corresponding preference data. The efficiency of this method is not high when the sample size is large.
2. The paper is hard to follow. Some definitions lack explanation and need clarification from the authors, such as the function F(.) used in Equations 4 and 5. 
3. There is a lack of more convincing experiments to show the significant enhancement of alignment efficiency.

### Questions
1.Refer to the weakness 1 and 3, would you please further explain the efficiency of the method?
2.Refer to the weakness 2, would you please clarify the definition of your objective?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to "distill" the gains from the best-of-N (BoN) inference-time alignment algorithm during finetuning, thereby improving a LLM's alignment without incurring the (linear in N) inference-time costs of BoN. They do this by deriving the distribution induced by the BoN algorithm, then defining the finetuning objective (which they call vBoN) to minimize the model's reverse KL divergence to this distribution. On the theoretical front, they derive some lower bounds for this vBoN objective and show that these lower bounds resemble the standard KL-constrained RL objective. Through experiments on controlled sentiment generation and summarization, they empirically show that PPO using the vBoN objective is the most effective technique for alignment via finetuning (though inference-time BoN still outperforms all finetuning-time alignment methods).

### Strengths
1. Clear motivation: vBoN is naturally motivated from the goal of reaping the gains of BoN without incurring the inference-time computational overhead.

2. Strong theoretical grounding, and compelling comparison of vBoN lower bounds with the standard KL-regularized RL objective.

3. Sound experimental setup: The win rate/average rewards vs KL curves in Figure 2 show a clean comparison against several important baselines, and the breakdown of how often each method appears on the Pareto front was also a nice statistic to report. The ablation and analysis to understand sensitivity to number of samples for the logF() approximation in the vBoN objective (Figure 3 and Table 1) were also clean and well-presented.

### Weaknesses
1. It is stated in the paper that, under some basic simplifying assumptions, the optimal distribution under the KL-regularized RL objective and the vBoN objective are asymptotically equivalent (Section 1, equation (2), Section 4). The paper also shows that lower bounds for the vBoN objective closely resemble the KL-constrained RL objective, and that models finetuned to maximize these lower bounds perform very similarly to those finetuned to maximize the vBoN objective. On the other hand, the paper shows that models finetuned to maximize the vBoN objective substantially outperform models finetuned to optimize the KL-constrained RL objective. This empirical evidence in some sense challenges the theoretical observations. Why, then (and under what conditions), is vBoN better than KL-constrained RL?

2. The paper demonstrates the effectiveness of vBoN on two tasks: Sentiment control (which is somewhat of a toy task) and Summarization (which is less of a toy task). However, several important baselines (e.g., DPO and BoNBoN) are only reported for the sentiment control task, and not for the summarization task. Why weren't these baselines included for the (less toy) summarization task?

See additional questions in the "Questions" section.

### Questions
1. The sentence right below equation (6) (the vBoN objective) states that "This is an entropy-regularized objective, where we...*discourage* the model from having low entropy". And this can be seen clearly in the objective (to be maximized) as well. However, in the text below equation (9), which is a lower bound for the vBoN objective, it is mentioned that L1(\theta) further *encourages* the model to have low entropy. Can you provide an interpretation of why this L1 lower bound encourages low entropy, while the original vBoN objective encourages high entropy?

2. Legend labels, as well as axis labels and numbers, are missing from Figure 4, which is one of the more important figures in the paper. Legend labels are also missing from Figures 5 and 6.

3. The abstract mentions that finetuning with the vBoN objective is "analogous to mean-field variational inference", but this parallel is not discussed in the main text of the paper. 

4. In Section 5, the BoN-SFT baseline is considered, but its performance is not competitive since it has high KL divergence from the reference model. Was a KL-constrained version of BoN-SFT considered?

5. Like vBoN, both the the BoNBoN and BOND (Sessa et al, 2024) methods attempt to convert BoN to a finetuning-time alignment method. Why was BoNBoN, but not BOND, reported as a baseline in Section 5?

Nit: There is a typo at the end of Section 5, where the references to Fig. 6a and Fig. 6b should instead refer to Fig. 2a and Fig 2b.

### Soundness
3

### Presentation
3

### Contribution
3
