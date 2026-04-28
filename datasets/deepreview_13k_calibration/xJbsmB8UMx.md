# SALMON: Self-Alignment with Instructable Reward Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Supervised Fine-Tuning (SFT) on response demonstrations combined with Reinforcement Learning from Human Feedback (RLHF) constitutes a powerful paradigm for aligning LLM-based AI agents.
However, a significant limitation of such an approach is its %
dependency on high-quality human annotations, making its %
application to intricate tasks challenging due to difficulties in obtaining consistent response demonstrations and in-distribution response preferences.
This paper presents a novel approach, namely
\textsc{\method{}},
to align base language models with minimal human supervision, using only a small set of human-defined principles, yet achieving superior performance.
Central to our approach is an \emph{instructable reward model}. 
Trained on synthetic preference data, this %
model can generate reward scores based on arbitrary human-defined principles. 
By merely adjusting these principles during the RL training phase, we gain full control over the preferences with the instructable reward model, subsequently influencing the behavior of the RL-trained policy models, and reducing the reliance on the collection of online human preferences.
Applying our method to the \texttt{LLaMA-2-70b} base language model, we developed an AI assistant named \texttt{Dromedary-2}. 
With only 6 exemplars for in-context learning and 31 human-defined principles, \texttt{Dromedary-2} significantly surpasses the performance of several state-of-the-art AI systems, including \texttt{LLaMA-2-Chat-70b}, on various benchmark datasets.
We have open-sourced the code and model weights to encourage further research into aligning LLM-based AI agents with enhanced supervision efficiency, improved controllability, and scalable oversight.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new self-alignment technique called SALMON, where we can leverage AI feedback with minimal human supervision to align language models with human preference. With those synthetic preference data generated with SALMON, the authors train a new model named Dromedary-2, which achieves state-of-the-art performance on various benchmark datasets.

### Strengths
- The methods that the authors propose only need to change the way of generating synthetic data, without much of modification of following RLHF procedure, which makes the technique more general and easy to adapt to other tasks
- The methods can be quite helpful when we need more domain-specific preference data (e.g., code, agents) when there is no such public available data.
- The authors demonstrate the advantage of the new method by finetuning with QLORA on 70B models, demonstrating its ability to improve model performance.

### Weaknesses
 - It would be good to show that the methods can also be leveraged to improve the performance of smaller models such as 7B or 33B, making the method easier for other topics or tasks. 

- I believe this method could potentially be adapted to some other tasks such as code generation. But I am not sure if it is possible, it would be good if the authors could comment on this.

### Questions
Please see my questions above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes SALMON, a method for training reward models that generate scores based on certain guiding principles. First, an instruction-tuned SFT model is used to generate preferences conditioned on a principle. This dataset is then used to train a principle conditioned reward model, where the reward model is trained with many subsets of principles, enabling it to generalize to new principles as well. This instruction tuned reward model is then used in a RLHF loop to fine-tune the SFT model. The resulting model Dromedary-2-70b, tuned from llama-2-70b, shows strong performance on several benchmarks, such as MTBench.

### Strengths
- The paper is generally well-written, though addressing some questions related to preference collection should improve the clarity further.
- A relevant and timely problem to address. Preference data needs to be extensively collected to keep reward models in-distribution with the current RL policy.
- The performance of the model is impressive, and the recipe for AI feedback seems quite interesting.

### Weaknesses
 - Some lack of novelty compared to Constitutional AI; The paper emphasizes constitutional AI focuses more on safety, but the technique itself is very much amenable for building a more “helpful” constitution too. But, the system laid down is distinct enough to warrant interest from the community.

- The paper claims that using principles to avoid reward hacking. Perhaps, the work “reward hacking” is a bit overloaded, but I don’t see any reason that SALMON rewards cannot be hacked to give degenerative responses or undesirable responses, if trained long enough using RL.

- What I do not completely understand is why train a separate reward model at all? The SFT-Model acting as a judge can already be used as a reward model. The scores for SFT-model can be aggregated for many principles as well (it might require multiple passes, but they can be batched potentially).

Overall, it seems that the final reward model ends up using several “hacks” which somewhat go against the main message of the paper:
- The reward model training claims to bypass human preference collection, but ends up pre-training on Anthropic HH-RLHF and SHP preference. Importantly, HH-RLHF and SHP contribute ~320k preference pairs to pre-training, while the SALMON reward uses only ~9.8k prompts (unclear how many preference pairs that yields, given that it can be combined with a large number of principles). How well does SALMON do without without the Preference Model Pre-training?
- Prior works deem the tendency of RLHF to produce lengthier responses as a negative. It is somewhat unfortunate that such a length bonus needs to be explicitly included as a symbolic reward. Can you also elaborate how this reward is included?

While I appreciate the performance of Dromedary-2-70b, the paper lacks several experiments and ablations that give more insight into why the method works. Some quantitative experiments that show how well the SFT model labels the preference in accordance to the principle are severely needed, and ablations of training the model without the “hacks”, and only with the “hacks” would show the importance of SALMON technique.

### Questions
- What happens if the answers are indistinguishable based on the principle? For example, when asking for a concise answer (but not necessarily correct, ethical or honest) — would it make sense to have an option for “no preference” when collecting preference from the model?
- For every user prompt and output pairs, are preferences collected using every principle? What is the size of the final preference dataset that is generated by the Self-aligned SFT model?
- Moreover, since the preference is computed based on the difference between logprobs, it would make sense to look at log probability of semantically equivalent answers [1]. The highest log probability can be misleading by itself.
- Why is the preference label decided by the principle with the most pronounced difference? Why not use the sum of scores, for example?
- Can you quantitatively evaluate the preferences generated by the SFT-Model, especially conditioned on the principles? How sensitive is the SFT model to the principle? For example, does using the negative principle flip the preference?
- How does the model perform when using just the SALMON reward without the symbolic bonuses, especially without the length bonus?
- A discussion on more recent works on alignment from scratch can be added such DPO, ReST SliC-HF etc

[1] Surface Form Competition: Why the Highest Probability Answer Isn't Always Right. Holtzmann et al.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides SALMON, a novel method for Large Language Model (LLM) alignment. The main idea of SALMON is self-alignment with principle-following reward models. The current prevailing method for LLM alignment is Reinforcement Learning with Human Preferences (RLHF), and it mainly consists of three phases: (1) supervised fine-tuning (SFT) on human demonstration data, (2) reward mode (RM) training on human preference data, and (3) RL fine-tuning with human-guided RM. Unlike RLHF, SALMON consists of (1) few-shot in-context learning (ICL), (2) RM training on AI preference data, and (3) RL fine-tuning with AI-guided RM. Since SALMON is based on RLAIF, it can be more efficient and scalable than RLHF. More specifically, SALMON based on Llama-2-70B only uses 6 demonstration annotations and zero preference annotations to achieve 7.4 MT-Bench score. In contrast, Llama-2-Chat based on SFT and RLHF uses about 27K demonstration annotations and about 1.4M preference annotations to achieve 6.9 MT-Bench.

### Strengths
- S1. First of all, this paper well-written and well-organized.

- S2. It is very interesting that SALMON (one of RLAIF methods) can significantly reduce human annotation costs than a prevalent RLHF method.

- S3. Unlike other RLAIF methods, SALMON can control preference scores by using a principle-following reward model (i.e., changing a principle to follow).

### Weaknesses
 - W1. One of main contributions of this paper is a principle-following reward model that can control reward scores according to principles. In addition to the overall alignment scores, can the authors measure a quantitative result of the principle-following reward model? Specifically, how well does the reward model adhere to the specified principles, and what is the variance in reward scores when different principles are applied to the same input? It would be beneficial to see metrics demonstrating the model's ability to distinguish between responses that align with different principles.

- W2. Even though Llama-2-70B with SALMON can provide better alignment score (7.4 MT-Bench score) than Llama-2-70B with RLHF (PPO) (6.9), there is still large gap to GPT-4 (9.0) and ChatGPT (7.9). It is important to acknowledge the gap in performance compared to state-of-the-art models. While the comparison to Llama-2-Chat is relevant, the absolute performance relative to top-tier models is a crucial consideration for practical applicability.

- W3. This paper compares SALMON with PPO-based RLHF. However, enhanced RLHF methods such as DPO (Direct Policy Optimization) and P3O (Pair-wise Policy Optimization) has been proposed and shown that they can achieve better reward score than PPO-based RLHF. It would be better to compare SALMON with recent RLHF methods. The lack of comparison with DPO and P3O, which have demonstrated superior performance over PPO, limits the assessment of SALMON's relative effectiveness within the current landscape of alignment techniques.

- W4. It would be interesting to provide comparison in perplexity score to see if SALMON is better to maintain the token distribution of the reference LLM than PPO-based RLHF methods. Analyzing the perplexity would provide insights into whether SALMON introduces significant deviations from the original language model's token distribution, which is important for maintaining the model's general language capabilities.

### Questions
- Q1. Regarding W1 above, what is the main advancement of SALMON compared to Constitutional AI? 

- Q2. Regarding W2 above, if better base LLMs than Llama-2-70B are used, can SALMON further reduce the gap to GPT-4 and ChatGPT? Or, is SALMON specialized on Llama-2 family LLMs?

- Q3. Regarding W3 above, if some enhanced RLHF methods such as DPO and P3O are used instead of a PPO-based method, is SALMON sill provide better performance than those methods? If not, can SALMON increase its alignment performance by additionally using human demonstration data or AI (or human) preference data?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a principle-following reward model trained on a set of human-specified principles, which is then used to learn human-aligned behaviors via the corresponding RL policy.

### Strengths
The paper is fairly easy to understand.  The approach seems to be a novel way to align RL policies using LLMs.

### Weaknesses
I believe the underlying assumption is that the specified principles (and examplars) are capable of completely specifying aligned behaviors. In reality, this may not be the case, and additionally, specifying an exhaustive list of principles may not be practical. Further results could have also been included (described later).

It is not entirely clear how the principles and exemplars affect the policy learning. I would have liked to see more experiments where the alignment of policies are evaluated after training with say, just the examples, just the 31 principles, different fractions of the 31 principles, with certain types of principles excluded etc.,

What happens in scenarios where two or more principles are in conflict with each other?

Perhaps related to the previous point, would it be possible to impose a hierarchy of principles during training? I imagine such hierarchies may be important in many practical circumstances.

Is there any way to guarantee that the set of specified principles would indeed lead to an aligned policy? In other words, is the set of principles general enough to be applicable to any scenario?

In pg 7 - It is not clear what a power RLHF trained model is

Pg8 – In 4.1.2 ‘police’ should be ‘policy’

### Questions
1.	It is not entirely clear how the principles and exemplars affect the policy learning. I would have liked to see more experiments where the alignment of policies are evaluated after training with say, just the examples, just the 31 principles, different fractions of the 31 principles, with certain types of principles excluded etc.,  

2.	What happens in scenarios where two or more principles are in conflict with each other?

3.	Perhaps related to the previous point, would it be possible to impose a hierarchy of principles during training? I imagine such hierarchies may be important in many practical circumstances.

4.	Is there any way to guarantee that the set of specified principles would indeed lead to an aligned policy? In other words, is the set of principles general enough to be applicable to any scenario?

5.	In pg 7 - It is not clear what a power RLHF trained model is

6.	Pg8 – In 4.1.2 ‘police’ should be ‘policy’

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
