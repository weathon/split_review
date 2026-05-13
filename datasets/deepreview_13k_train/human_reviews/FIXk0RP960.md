# Does RLHF Scale? Exploring the Effects of Data, Model, and Method

- Decision: Reject
- Scores: 5, 3, 6, 8

## Abstract
This study explores the scaling properties of Reinforcement Learning from Human Feedback (RLHF) in Large Language Models (LLMs). 
Although RLHF is considered an important step in the post-training of LLMs, its scaling potential is still largely unknown. 
We systematically analyze key components in the RLHF framework—model size, data composition, and inference budget—and their impacts on performance.
Our findings show that increasing data diversity and volume improves reward model performance, helping process-supervision models scale better. 
For policy training, more response samples per prompt boost performance initially but quickly plateau. 
And larger reward models offer modest gains in policy training. 
In addition, larger policy models benefit less from RLHF with a fixed reward model. 
Overall, RLHF scales less efficiently than pretraining, with diminishing returns from additional computational resources.
Based on these observations, we propose strategies to optimize RLHF performance within computational limits.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates key components in the RLHF framework, such as model size, data composition, and inference budget, assessing their scalability. The findings reveal that RLHF scales less efficiently than pretraining, with performance gains diminishing despite increased computational resources.

### Strengths
1.	This paper addresses a critical gap in current LLM post-training research by examining the scalability of RLHF.
2.	The experiments comprehensively cover various aspects of RLHF, including model size, data composition, and inference budget.
3.	The conclusions drawn are strongly supported by robust experimental results, providing clear insights into the limitations and potential of RLHF scalability.

### Weaknesses
1. RLHF encompasses a broad range of concepts, yet this paper does not cover all aspects of the literature. For instance, the impact of training data composition for the reward model on RLHF scalability is not explored.

2. While there are numerous RLHF approaches, such as DPO, RPO, and KTO, this paper focuses solely on PPO and GRPO. This limited scope challenges the claim of exploring the impact of methods comprehensively. 

3. The study is primarily centered on reasoning tasks, such as math and coding, and does not extend to other important areas like general instruction-following tasks, which limits the generalizability of the findings.

4.  Discussion about potential hypotheses for why RLHF doesn't scale as well as pretraining and  experiments that could help isolate the cause are no presented.

### Questions
What is the reason that RLHF does not scale?
For instance, In Section 4.2.1, why the performance does not always improve when the number of responses increase?

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
The paper proposes a sequence of experiments to show if the current RL recipe can scale.
The experiments range from reward modelling, testing different reward model sizes to generating more samples at training time or RL algorithm choice. They identify several problems with the current approach and conclude that scaling it is not feasible.

### Strengths
The paper showcases clearly the different shortcomings of the actual RLHF recipe to train LLMs.
The paper is a good technical report that reviews what are the different degrees of freedom in the mainstream RLHF recipe.
It explains that reward modelling is probably the main bottleneck towards scaling up RL methods.
The paper in its current state is more a technical report than a research paper in my opinion. My rating is based on this and not on the underlying quality of the document which is good.

### Weaknesses
My main concern with the paper is the lack of novelty and originality. There are no new findings obtained through the run experiments:
 - reward hacking is a known problem
 - the different RL approaches and reward normalization schemes are known
 - using N generations and how the performance plateaued is known

No solution is proposed to the main bottleneck which is reward modelling. If one wants RL to scale, it is also imperative to get rid of the anchor model as it constraints the optimal set of possible solutions. It is only used here to avoid the shortcomings of reward hacking. The authors should expand on this a little bit more. The authors do raise the point that increasing the reward value at training time does not correlate with improving performance with downstream tasks which shows that RLHF in its current state is not a proper training regime.
In addition, authors could have found potential directions of future research in the RL literature. To properly scale, especially in sparse environments RL methods need an exploration bonus or a way to understand their uncertainty about the environment. This is independent from a learnt reward model and could potentially scale. Authors should have at least tried to see if they could find a method to scale the diversity of outcomes in the obtained generations or if using different inference mechanisms (in addition to the sampling N parallel answers) could help scaling.

### Questions
I provided my list of suggestions in the previous section.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work investigates the training scaling properties of RLHF for LLMs in the context of reasoning questions. They investigate two main settings: how does scaling effect the policy in RLHF assuming a fixed SFT model, and how does scaling the policy effect performance assuming a fixed RM and training strategy? They find that scaling up data, model size and training time often produces improvements, but these sometimes see diminishing returns at the high end of scaling up, even on a logarithmic x-axis. They additionally find that process supervision produces performance boosts over outcome supervision in-distribution but these improvements sometimes fail to generalise. Using these insights, the paper recommends practical ways in which increased compute can results in better performance for RLHF training for reasoning questions.

### Strengths
The paper performs extensive experiments across a range of scales and settings, making the results much more likely to be robust and generalisable. The topic is important and timely, and hasn't been investigated to this level of rigour before, making this a significant and original contribution. The paper is fairly well written and easy to understand. The research questions are well-scoped and investigated well. Overall, it makes a worthwhile contribution to our understanding of scaling properties in RLHF training.

### Weaknesses
# Paper framing

The paper title and introduction claims to address RLHF broadly construed, but the experimental setting is mostly focused on improvements in code and reasoning questions rather than more a more general chat setting. This is fine as a focus of the paper, but I think it would be beneficial to be clearer earlier in the paper that the RLHF setting considered is perhaps different from the standard one readers would expect (RLHF for dialogue).

# dataset and evaluation choice leads to lack of generality in conclusions

The paper uses a mix of datasets both for training and evaluation. However, it's unclear what the relationship between the training and evaluation datasets is, which means the results are harder to interpret. For example, when we see diminishing returns to scaling various properties, is that because these properties are not producing performance in-distribution in a clean manner, or because that in-distribution performance is not translating to the out-of-distribution evaluations being measured. In general, when measuring scaling trends like done in this paper, it's common practice to disentangle these two hypotheses by evaluating on in-distribution (but held out) data, but that is difficult in this setting given the heterogeneous nature of the RLHF training mixture. I believe the results in the paper are still interested and likely to be generalisable to some extent, but this experiment design decision does hamper the usefulness and transferability of the results to other settings. This is exemplified in the results in figure 2 - some benchmarks benefit from scaling of the properties investigated and some do not, but we don't know whether this is a generalisation failure or an optimisation failure, as we don't have in-distribution performance.

Additionally, it is difficult to calculate scaling trends for evaluation metrics such as those computed, as they're likely non-monotonic with respect to underlying metrics of performance. When observing that pretraining scaling predictably improves loss, this is easy as loss is grounded in the training procedure. However, evaluations based on metrics not directly optimised for means that it's difficult to explain diminishing returns to scale for that metric as scaling not working well, or whether that metric gets more difficult to improve the higher it is. Again, matching training and evaluation metrics and data more closely would address this problem.

This could be addressed firstly by making this limitation clear in the paper. It would also be beneficial to perform in-distribution evaluations of these models, where in-distribution means that both the input data and the reward function are matched to those that generated the training data for the policy and reward model respectively.

# contextualising results with respect to related work

Some of the key findings listed in the introduction are similar to those found in the literature. It would be beneficial to explicitly state where your results confirm previous findings, or disagree with them, or go beyond them.

# Unclear statements about comparison to pretraining scaling

In several places the paper claims that their results show that scaling RLHF is less effective that scaling pretraining. However, this comparison isn't made formal and hence I think this claim should be made more precise, or dropped from the paper. I don't think you can compare scaling in your setting (where training and evaluation objectives and data are different) to the pretraining scaling regime (where they are the same) without being clearer how this is done.

# Smaller issues

* One of your conclusions is that larger policy models benefit less from RLHF when using a fixed size reward model. However, this is confounded by the improved starting point of larger policy models, as the initial SFT is likely better. Combined with the issues above about the metric not being linear, this conclusion doesn't seem valid to me.
* You say "Recently, OpenAI-o1 (openai, 2024) has revealed the potential for scaling reinforcement learning at inference time and significantly boosts the reasoning abilities of LLMs." (line 135). However, o1 also scales RL at training time as well.
* when scaling responses per prompt, you're effectively scaling the batch size for training, but you're not also scaling the learning rate, which likely leads to worse performance than is achievable. In general larger batch sizes can accomodate larger learning rates and hence be more performant, and I think it would make more sense to adapt this hyperparameter to the setting to get more compelling results.
* It would be beneficial to have error bars or confidence intervals of some kind on most of the plots, to understand how noisy these results are. For example, in figure 2, MMLU and AlignBench move by neglible amounts, which could easily be noise in evaluation rather than a real trend.

### Questions
It would be beneficial to get more details on the process supervision technique in the paper, so that it is somewhat self-contained, rather than just referencing another work without detailed explanation.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how policy model performance changes as components of RLHF are scaled. Specifically they look at the effects of sampling multiple responses from the policy model for a given prompt, reward model parameter count, RLHF training example count and policy model parameter count. They also compare policy model performance when RLHF is done with PPO versus GRPO, and with process supervision versus outcome supervision.

For each component of RLHF, they plot policy model performance on a downstream task (e.g., MATH, GPQA, etc.) at different scales. Where appropriate, trends are fit to policy model performance.

The paper concludes that RLHF generally does not scale as well as pre-training, and that larger policy models do not seem to benefit as much from RLHF. Despite this, when scaled some of the components of RLHF do yield superior performance, such as sampling from the policy models multiple times, however this benefit is shown to plateau quickly.

### Strengths
**Originality**: To my knowledge this is the first work to directly study the scaling properties of RLHF. The studied techniques have largely appeared in the literature, but I am not aware of equivalently detailed studies of their scaling.

**Clarity**: The writing is generally clear. I did not find any part of the paper confusing. I expect Section 3 to be sufficient for someone not familiar with RLHF to read and have the necessary context for the rest of the paper.

**Quality**: The paper considers a reasonable number of datapoints for most experiments and uses well-respected benchmarks for downstream policy model performance. I think the paper studies RLHF scaling well and that the results do support the points in Section 4.4.

**Significance**: How well RLHF scales is likely of great interest to the broader ML community. RLHF/RLAIF have become extremely common place, and as it is more feasible now for non-commercial projects to do more intensive post-training I think this work is significant.

### Weaknesses
 - The paper claims to study how RLHF scales, but they make some unconventional choices in how they design their RLHF pipeline. Notably, they use a single reward model for reasoning and human preference data. This weakens the results, as they do not directly assess RLHF as it is usually implemented.
- A very minor point: The paper mentions GRPO but never gives the expanded version of the acronym.

### Questions
- Would it be possible to run some smaller experiments without the unified reward model from section 3.1? If downstream policy model performance is similar even at smaller scales it would help show that your results track meaningfully to the case where separate reward models are used.
- Will you open source the reward models, corresponding policy models and the SFT model you use? I can see these models being useful for other work that studies how RLHF scales.

### Soundness
3

### Presentation
3

### Contribution
3
