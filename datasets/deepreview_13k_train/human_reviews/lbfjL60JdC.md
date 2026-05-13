# Wait, That's Not an Option: LLM Robustness with Incorrect Multiple-Choice Options

- Decision: Reject
- Scores: 5, 3, 5, 5, 5

## Abstract
Decision-making under full alignment requires balancing between reasoning and faithfulness - a challenge for large language models (LLMs). This study explores whether LLMs prioritize following instructions over reasoning and truth when given \textit{misleading} instructions, such as \textit{Respond solely with A or B}, even when neither option is correct. %In order to measure the actual impact of post-tuning schemes,
We introduce a new metric called \textbf{reflective judgment}, which sheds new light on the relationship between the pre-training and post-training alignment schemes. In tasks ranging from basic arithmetic to domain-specific assessments, models like GPT-4o, o1-mini, or Claude 3 Opus adhered to instructions correctly but failed to reflect on the validity of the provided options. Contrary, models from the Llama 3.1 family (8B, 70B, 405B) or base Qwen2.5 (7B, 14B, 32B) families exhibit improved refusal rates with size, indicating a scaling effect.
We also observed that alignment techniques, though intended to enhance reasoning, sometimes weakened the models' ability to reject incorrect instructions, leading them to follow flawed prompts uncritically. Finally, we have also conducted a parallel human study revealing similar patterns in human behavior and annotations. We highlight how popular RLHF datasets might disrupt either training or evaluation due to annotations exhibiting poor reflective judgement.8\textwidth]{images/main.png} % Adjust width as needed
        \caption{Reflective Judgment Score measures a model’s ability to avoid selecting an incorrect option by either providing the correct answer or indicating that none of the given options is correct. The figure shows this score averaged across the proposed BAD dataset. For example, Llama 3.1-405B and Qwen2.5-32B achieve high Reflective Judgment Score—Llama 3.1-405B often responds with statements like, \textit{The correct answer is not among the options. The correct calculation is ... So, neither A nor B is correct.} In contrast, most closed models, such as GPT-4o or Gemini 1.5 Flash, tend to adhere to flawed options.}
        \label{fig:first_figure}
        \vspace{-10pt}
    \end{figure}
\end{center}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces the concept of "reflective judgment" in LLMs, defined as their ability to recognize and reject incorrect multiple-choice options rather than blindly following instructions. The authors evaluate various LLMs using both a BAD and a subset of MMLU, comparing their performance across different model sizes and training approaches. The study includes a parallel human study and analysis of how alignment techniques affect reflective judgment capabilities.

### Strengths
The paper identifies an important aspect of LLM behavior that warrants investigation - the tension between instruction-following and critical evaluation.

The experimental setup is systematic, testing multiple hypotheses: 1) Impact of model size on reflective judgment. 2) Effect of alignment techniques. 3) Relationship with chain-of-thought reasoning

The inclusion of a human study provides valuable comparative insights into how humans handle similar decision-making scenarios.

### Weaknesses
The dataset and evaluation design present several fundamental limitations. The BAD dataset's restriction to basic addition operations significantly constrains the generalizability of the findings. The binary choice format (A/B) represents an oversimplified decision-making scenario that may not reflect real-world complexity. Furthermore, the MMLU subset of 400 questions may not be sufficiently representative of broad domain knowledge, and the evaluation lacks complex reasoning scenarios where reflective judgment would be most crucial.

While the human study is appreciated, I feel these type of experiments could be biased. The human study's small sample size of 50 participants restricts the statistical significance of the findings. The experimental design does not control for question order effects, and the exploration of prompt variations is limited. The absence of ablation studies makes it difficult to isolate which factors contribute most significantly to reflective judgment capabilities.

The concept of "reflective judgment" needs stronger grounding in existing literature, and the paper provides insufficient exploration of how different contexts might affect this capability. The analysis of why alignment techniques impact reflective judgment remains superficial, leaving important questions about the relationship between alignment and critical thinking unanswered.

While the findings show significant improvements (>85%) with chain-of-thought reasoning, the paper does not adequately investigate the underlying mechanisms. The interaction between model architecture and reflective judgment capabilities remains unexplored, and the potential trade-offs between helpfulness and critical thinking need deeper examination. The relationship between model size and reflective judgment, while observed, lacks theoretical explanation.

The paper notably lacks practical solutions or mitigation strategies. While it identifies important challenges in maintaining reflective judgment during alignment, it does not propose concrete approaches to address these issues. The absence of practical recommendations for improving model training and evaluation methods limits the immediate applicability of the findings. Without suggested solutions, the paper's contribution to advancing the field remains primarily diagnostic rather than prescriptive.

### Questions
Could you provide grounding for the "reflective judgment" concept in existing literature?

What mechanisms might explain the relationship between model size and reflective judgment ability?

How might the findings generalize to more complex reasoning tasks beyond arithmetic?

Could you elaborate on why alignment techniques appear to impair reflective judgment?

What design considerations would be important for a more comprehensive evaluation dataset?

How do different chain-of-thought prompting strategies affect reflective judgment?

Could you propose potential solutions for maintaining reflective judgment during alignment?

### Soundness
2

### Presentation
3

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
The paper introduces the concept of "reflective judgment" in LLMs, which measures the ability to disobey instructions and reject answering or providing correct answers when given multiple-choice questions with only incorrect options. 

The authors construct a simple dataset (Basic Addition Dataset (BAD), and present evidence that larger models and base models (before instruction tuning or alignment) exhibit better "reflective judgment". They also include limited experiments on the MATH dataset.

They also include a human study, where they find that the majority of human raters chose to follow instructions over applying "reflective judgment".

### Strengths
* Presentation: The paper is generally well written and easy to follow.
* Novelty: The authors study whether models can abstain in a multiple choice setting, where abstention creates a conflict because it would violate the given instructions.
* Broad evaluation:  The authors evaluate a large number of both open and closed LLMs, across different model sizes and training stages.
* Human study: The inclusion of a human study provides interesting insights into human responses in the same setting.

### Weaknesses
 * Framing: I am not convinced the framing of the research question is useful. Whether a model limits its response to a set of options, or whether it rejects all available options, should depend on context and prompt (both underexplored, see below).
* Main dataset is very simple: The Basic Addition Dataset (BAD), consisting only of simple addition problems, is too narrow to draw strong conclusions about the general reflective judgment abilities of LLMs.
* Unclear impact of instruction tuning:  While the paper claims that instruction tuning hinders reflective judgment, the results are mixed. DeepSeekMath-7B exhibits decreased performance after instruction tuning, but Qwen2.5 does not. The paper doesn't sufficiently disentangle the effects of instruction tuning from alignment.
* Weak analysis of prompt variations: The analysis of prompt variations is superficial and lacks a deeper exploration of why certain prompts elicit more reflective responses.
* Limited exploration of CoT impact: While the paper notes the positive impact of CoT on reflective judgment in some cases, it lacks an investigation of the limitations and observed drawbacks of CoT in o1.

### Questions
1. Can you eloborate on the general framing of the research question of your paper. Specifically, you seem to suggest that "reflective judgment" is generally desirable. If you believe that's the case, can you more clearly justify it?
2. Can you further explore the relationship between instruction tuning, specific kinds of alignment and specific prompt formats and disentangle their individual effects on "reflective judgment" by also including a qualitative analysis? In other words, analyse whether certain prompts elicit an appropriate "reflective" responses if the model was trained to respond that way?
3. Can you provide a more detailed discussion about limitations and observed drawbacks of CoT in "reflective judgment".

### Soundness
2

### Presentation
3

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
The paper proposes the issue that large language models (LLMs) prioritizing instruction-following over critical reasoning. In this paper, They evaluate different LLMs through two datasets: Basic Addition Dataset (BAD) and MMLU Subset, where the given multiple-choice options are incorrect. Different LLMs were tested under different conditions (easy, standard, hard) that varied in instruction complexity. The authors measured Reflective Judgment Score (RJscore), defined as the proportion of instances where models demonstrated reflective judgment by refusing or correcting erroneous options.

### Strengths
1. the idea is interesting
2. they propose a new metric called Reflective Judgment metric  and also conduct a human study

### Weaknesses
1. I didn't see the difference between Reflective Judgment and refusal mechanism, in some sense I think they are the same. The authors should emphasize the differences between these two.

2.the data used to test different LLMs are quite limited. there are two weak points here: 1. The task (maybe I missed somewhere in the paper) lacks a version where partial given multiple-choice options are incorrect and partial given multiple-choice options are correct. 2. The  subset of MMLU and synthetic data (BAD), which may not fully generalize to diverse scenarios

3. overemphasize on the model size. Although larger models show better reflective judgment, this focus on scaling may overlook other aspects which may lead to these results.

### Questions
can you please explain how you obtain the confidence region in figure 2?

### Soundness
3

### Presentation
2

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
This paper tests the tendency of a language model to disobey instructions and not give incorrect answers when the model is asked a forced-choice question. It finds that commercial language models tend to adhere to the instructions more often and provide an incorrect answer, compared to other models.

### Strengths
The question of how a model behaves when confronted with a conflict between following instructions and providing false information is important. They compare several different models and see how they respond in terms of the tradeoff between instruction-following and accuracy.

### Weaknesses
I do not agree with the paper's claim that it is generally better to disobey instructions than to give false information, for two reasons:
1. There are cases where the answer is "close enough", e.g., "What is the capital of France? (A) Pariis (B) London"
2. There are many LM uses (e.g., a classifier where a developer needs to parse an LM response programmatically) where a valid response (ideally the response closest to the truth) is better than a response that does not follow instructions. It wasn't clear which types of LM uses the present paper is interested in, or if it is meant to cover all uses.
3. Users can instruct the language model to respond with a "non-of-the-above" option. If they do not, they may prefer instruction following over accuracy.

Instead, there really is a trade-off between instruction following and accuracy. There are many such trade-offs that a language model designer faces. The paper would be more interesting if it explored these trade offs, or even the one that it covers more thoroughly. For example:
* Q1. Is the model less likely to provide incorrect information in high-stakes contexts, like asking for medical advice, than in a low-stakes context like asking which of two jokes is funnier?
* Q2. Is the model more likely to answer when there is an answer that is nearly correct versus all completely wrong?

It seems that the most interesting finding currently is that the commercial API models seem to follow instructions really well, which makes sense because a developer would often prefer to have an incorrect answer than a non-answer. Maybe users would also prefer instruction-following.

### Questions
Suggestion: remove the term "reflective judgment." Instead, the paper could be reframed as an analysis of the tradeoff between accuracy and instruction-following.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an eval for testing whether models question the answer options they've been given, vs. are okay with picking one of the answer choices even if both are wrong. The idea of models questioning the task is called reflective judgment, which the authors produce evals to test current LLMs on. They find wide differences in how models behave on this eval, and compare the results to humans, who are more likely to show reflective judgment than many LLMs.

### Strengths
- I would have guessed that some of this could even be easily/quickly fixed by adding a line to the prompt, but it seems like that doesn't fix the issue, which is interesting/surprising to me
- Human eval is helpful for comparison. 
- It's nice to know where models are on this eval (e.g.: Figure 2 is nice) even if I'm not sure if the authors' claims in the paper are about whether lower RL score = right being better (see discussion in weaknesses). It's definitely an interesting behavior to keep track of, regardless of what your stance on the behavior is.

### Weaknesses
 - Generally, the paper would benefit from more analysis/insight into why this happens.
- The concept of sycophancy described/analyzed in (https://arxiv.org/abs/2310.13548) and (https://arxiv.org/abs/2212.09251) could be the source of the behavior — it would be worth adding some discussion (and maybe analysis) on whether you think this is driving the behavior.
- I'm not sure about the motivation - if the instructions are worded strongly in favor of just picking one of two options, it seems ok to just pick the lesser wrong of two options. For models that do COT (like o1), I'd even guess they explicitly are reasoning this way, which seems ok to me.
  - It's also kind of reasonable for a model that's unsure/unconfident in the answer to have a prior in favor of the human being correct. Maybe it's an issue if the model clearly already/confidently knows the answer, and is more likely to show this behavior even in cases where its confident of a different answer, in which case I'd frame this more like a sycophancy-related problem. If it's sycophancy-related, that could be quite interesting. Could be interesting to filter q's down to subsets where the model gave an answer with a confidence below vs. above some threshold, to understand this better
- Moreover, this should be easy to fix with post-training if it is problematic, and not like a fundamental issue. (Though it can still be ok to point out issues that are easily fixed, this just reduces the impact of the contribution to me). It's possible that this issue goes away with better post-training / instruction following training (and some of the results suggest this might be the case), in which case the importance of the contribution would be much less to me (since the issue would soon go away as models continue to scale).

Minor feedback:
-Not sure what "aligned" means here (vs. "instruction tuned"), on page 5. Would be easier to read Table 3 as a plot/figure.

### Questions
-I wonder if the "easy" setting doesn't work as well because of (1) dropping answers breaks some questions (like all/none of the above questions), or (2) because it's easier to correctly answer questions if you see the answers.
-Is this effect caused by undesirable sycophancy or some other phenomenon (over-reliance on priors that humans are correct)?
- Looking at Fig 3, it actually seems like prompting (the "easy" setting) doesn't fix the issue as much as I might've expected. It would be nice to show log-prob based trends (or just show log-p of getting the right answer overall on the dataset), esp. for a series to see if there’s a power law trend. This would help to know if the gap between settings in log-p space is going down over time

### Soundness
2

### Presentation
3

### Contribution
2
