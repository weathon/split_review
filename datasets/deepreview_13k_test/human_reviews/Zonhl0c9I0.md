# SELF-EVOLVED REWARD LEARNING FOR LLMS

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Reinforcement Learning from Human Feedback (RLHF) is a crucial technique for aligning language models with human preferences, playing a pivotal role in the success of conversational models like GPT-4, ChatGPT, and Llama 2. A core challenge in employing RLHF lies in training a reliable reward model (RM), which relies on high-quality labels typically provided by human experts or advanced AI system. These methods can be costly and may introduce biases that affect the language model's responses. As language models improve, human input may become less effective in further enhancing their performance. In this paper, we propose Self-Evolved Reward Learning (SER), a novel approach where the RM generates additional training data to iteratively improve itself. We conducted extensive experiments on multiple datasets such as HH-RLHF and UltraFeedback, using models like Mistral and Llama 3, and compare SER against various baselines. Our results demonstrate that even with limited human-annotated data, learning from self-feedback can robustly enhance RM performance, thereby boosting the capabilities of large language models (LLMs).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript introduces an approach to improving sample-efficiency of RLHF. The method enables using only a fraction of the original data through an iterative approach of labelling and ranking of the preference data based on the dynamics of the training process. The authors provide theoretical support of their empirical results, as well as extensive experiments (multiple models, multiple datasets).

### Strengths
The manuscript, in my opinion, has several strengths that make it interesting to the ICLR audience.

* Tackles an important problem, namely of sample efficiency, for RLHF methods. The cost of human annotations is rather high and therefore studying ways to reduce the dependency on the entire datasets is useful overall.

* The recipe is well presented and supported theoretically. Although the steps seem obvious at first, the subtlety of amplifying the differences (second step) during the training loop seems rather novel and not extensively studied before. Effectively, it introduces the ability for the model to provide signal as to what samples provide most utility at current training stage.

* The extensive results, which utilize multiple models and multiple datasets. The performance across all these combinations of setups seems to support that the recipe is effective and general.

### Weaknesses
The main weakness in current practices is the longer-term importance of annotated human datasets. The recipe introduces significant compute costs, trading off annotation costs for accelerators (through the recipe steps). However, the manuscript does not study the relationship between the two. If we assume human-annotated data goes away for preference labelling - having datasets created by LLMs for training other LLMs - do the benefits of the recipe still outweigh the costs?

I would like to understand the authors' position on this aspect, as well as a better comparison between labeling costs and accelerator costs of their recipe. Where does a tie come in (e.g. at the K=4 loops used in the paper, or for what value of K)?

### Questions
Please refer to the weakness comment.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach called Self-Evolved Reward Learning (SER), which leverages an RM to autonomously curate its training data for continuous improvement. The authors conduct experiments across various models and datasets, demonstrating that the SER approach can train the reward model well using only 15% of the labeled data, which results in performance comparable to an RM trained on the full labeled dataset, both in terms of evaluation capability and integration within PPO training.

### Strengths
**Motivation:** Given the high costs associated with acquiring human-annotated data for reward model training, the development of self-training approaches is highly beneficial. Such methods can leverage a minimal amount of human annotations for initial model training and subsequently enhance performance through self-improvement.

**Soundness:** The paper's various training strategies, which are based on different statuses, are well-conceived and intuitively sound.

**Substance:** The authors have conducted extensive experiments across multiple models and datasets, effectively demonstrating the efficacy of their Self-Evolved Reward Learning (SER) approach.

### Weaknesses
**Clarity:** The paper lacks clarity in several places, with some descriptions being particularly confusing. For instance:

- **Lines 206-211:** It remains unclear how the status is determined, given that $p_i^1$ and $p_i^2$ are both single numbers. How are these individual numbers used to decide the training status? Additionally, how are the thresholds $\tau_\text{high}$, $\tau_\text{low}$, and $\tau_\Delta$ established?

- **Lines 248-249:** The method for determining the $\Delta$ term is not explained.

- **Section 3.2 (Theoretical Analysis in Appendix A):** This section appears to offer only speculative insights into how the algorithm might function, rather than providing concrete proofs.

- **Lines 325-326:** The statement "Larger parameter models can achieve higher self-improvement benefits" seems inconsistent, as Llama 13B appears to exhibit lower benefits compared to Llama 8B and Mistral 7B.

- **Section 4.1.2 (Fine-grained Analysis):** The paper does not clearly define what Loop0, Loop1, Loop2, and Loop3 training entail. What data are these loops trained on, and do they use the same subset of data? How is the transition to the next loop decided? Furthermore, why is the strategy of learning status 2 employed in Loop 3 not earlier?

**Meaningful Comparisons:** In Figure 4, the comparison using GPT-4 as a judge seems to employ an unconventional prompt for evaluating model responses (Appendix D.4). Why not use the AlpacaEval or MT-bench LLM-as-a-judge prompts, which have been shown to correlate well with human judgments?

**Implications:** The paper currently focuses on improving reward models that are not well trained (i.e., trained on only a small subset of the complete human-annotated dataset). Ultimately, the goal is to continuously enhance strong reward models with minimal human annotation. It is unclear whether this approach can be applied to strong reward models and whether these models have the potential for continuous self-improvement. Exploring this line of experimentation would be valuable.

### Questions
See questions in the weaknesses part.

### Soundness
3

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
The paper proposed a self-improvement RM training strategy to circumvent the challenges of collecting human preference data. The RM is initially warmed up using only 15% human preference, then it’s improved iteratively through a series of self-labeling and retraining. During the self-labeling the current RM is used to score unlabeled data (i.e., prompt and answer pairs), then two data filtering strategies are devised based on the predicted probability differences between answer pairs. The goal is for the RM to (1) first learn from pairs with clear distinction (trained on very high- and very low-scored response pairs) before (2) switching to refining its understanding of subtle differences (trained on pairs that are more similar). When no improvement is seen on this current data, training stops and new data is collected. 

The author tested their approach on multiple datasets including HH-RLHF, UltraFeedback as well as several model sizes and families including Llama and Mistral. They also evaluate how the improved RM helps during PPO.

### Strengths
- Promising results on improving the RM performance matching or exceeding the baseline train on the full human labeled data
- The curriculum learning style for the RM which encourage learning from easy and then hard pairs seems an interesting finding in the context of RM optimization

### Weaknesses
- The Experimental design is very narrow, and limited. (see questions for more details). E.g, I would expect to see results on downstream/standard benchmarks. However currently only preference accuracy is reported.
- Some claims in the results section are unsupported (mixed results which are generalized) → see detail below
- The paper clearly benefits from some rewriting and reorganization. In its current form several details are missing which makes it uneasy to follow.

### Questions
1. Are the pairs of responses generated from the same base LLM? Or are the authors using the response pairs in the existing dataset. While the author mentioned generating two responses from the LLM (line 173), it is not clear which model they use to generate responses and if they do this on-policy data generation for all the iterations? More details on this is appreciated. 
2. Line 174-175: how generating two responses on-policy from the LLM "enriches" the training data with diverse answer qualities? What aspect of this setup is unique or does it guarantee quality/diversity?
3. Intuitively, what does the RM learn from its highly confident labeled data during stage 1? In other words, when the RM is too confident about a preference label (irrespective of whether it may be incorrect), what training signals it is gaining from it? Did authors try some ablations to test the contribution of each data state?
4. How the number of training steps differ in SER vs Full dataset in Table 1?
5. One would expect to see the performance of your PPO'ed model on downstream standard benchmarks like AlpacaEval, MMLU, BBH, MATH, CODEX, etc. So technically, start from a pre-trained base model doing supervised finetuning on some existing instruction-tuning data , then try doing PPO using your RM vs the baseline RM (trained on full data, e.g. on UltraFeedback) and compare performance over standard benchmarks. This will more realistically show the effectiveness of your approach as opposed to just narrowly evaluating models in their ability to choose the preferred response.
6. Line 343: The scaling claims are somewhat unsupported, based on Table 1 13b> 7b> 8b. more experiments specifically within the same model family is needed to make informative scaling trend conclusions.
7. Section 4.1.2, there's no explanation as to what Loop 1-3 refers to in section 4.1.2 and figure 2. It is not clear if loop is referring to one iteration of RM training (including both state 1 and 2), or something else? Line 373 states that "loop 2 is the least significant across all iterations" which makes me think loop != iteration
8. Line 418: does that mean Loop 1 and Loop 2 did not include data strategy of status 2? In general more details on the training is nice in the main paper.
9. Section 4.2: it would make sense to try PPO on a more general purpose preference dataset like ultrafeedback and see how it transfers to downstream tasks and not just alpacaeval style evaluation
10. Suggestion: the authors refer to their models as SER, or self RLHF. It’s nice to stick to one name and be consistent with it.

### Soundness
3

### Presentation
2

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
This paper proposes self-evolved reward learning where the reward model is used to obtain more training data for iterative improvement. The algorithm is straightforward: (1) generate two responses per prompt and label using RM, (2) only keep response pairs where reward difference is large -- there are two filtering strategies (Status 1 and Status 2) and the authors alternate between them, (3) train RM with the filtered data; then, iterate the above. Finally, use RM for LM training. Findings: Only 15% human-annotated data is needed so that the new model archives performance similar to training on the entire human-annotation dataset; experiments are done on a few models (7B to 13B).

### Strengths
The self-improvement paradigm could save lots of resources. 

I appreciate the fact that the authors not only tested on reward modeling benchmarks but also LMs (by doing PPO). 

Experiments are done on multiple models and multiple model sizes.

### Weaknesses
On baselines:
- It’s unclear how specifically the authors trained “Loop 0” and “Full dataset” baseline models. What is the loss function? How are hyperparameters tuned? 
- Have the authors tried regular scalar-valued reward functions as baselines? 

On eval: Have the authors tested on common benchmarks like RewardBench (so we can easily compare to other scalar and generative RMs)?

In real LLM training, the same dataset would always contain examples of multiple domains. In the same dataset, lots of examples could be on simple helpfulness prompts, and lots of examples are on coding/reasoning prompts. In this case, how would thresholding work? Would the model first learn simple prompts and then coding/reasoning/complicated prompts? Or would the model give up on coding/reasoning/complicated prompts?

Eq. (3) can be clearer:
- It looks like Status 1 and Status 2 can be achieved at the same time? In that case, does S=Status1 or Status2? 
- Do we have a different S at every i? 
- Do we need to recompute Delta_p (avg through every i) after each gradient step? 
- When would the model hit “Stop”? What if the “otherwise” case never happens? An explanation in natural language would be great.

Details are lacking on data generation/filtering
- How specifically are responses generated?
- What percentage of data are filtered at different point in training? 
- Are there more conclusive evidence that alternating between status are beneficial? How are hyperparameters tuned -- based on what metrics? 


Other misc issues: 
- Eq. (4): missing right bracket
- Table 1 caption mentions “Our method” but I don’t see “Our method” in the table. Do you mean SER?
- Serious misuse of \citet and \citep. Most of the citations on the first page and the second page, for example, should be in \citep.

———

UPDATE: increased score to 5 but still concerned about paragraph 3 (and hopefully more detailed result on paragraph 2) above.

### Questions
Are Llama models base models or instruction-tuned models?

### Soundness
1

### Presentation
2

### Contribution
2
