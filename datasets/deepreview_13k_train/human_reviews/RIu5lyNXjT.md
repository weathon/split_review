# Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
As large language models (LLMs) are adopted as a fundamental component of language technologies, it is crucial to accurately characterize their performance. Because choices in prompt design can strongly influence model behavior, this design process is critical in effectively using any modern pre-trained generative language model. In this work, we focus on LLM sensitivity to a quintessential class of meaning-preserving design choices: prompt formatting. We find that several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings, with performance differences of up to 76 accuracy points when evaluated using LLaMA-2-13B. Sensitivity remains even when increasing model size, the number of few-shot examples, or performing instruction tuning. Our analysis suggests that work evaluating LLMs with prompting-based methods would benefit from reporting a range of performance across plausible prompt formats, instead of the currently-standard practice of reporting performance on a single format. We also show that format performance only weakly correlates between models, which puts into question the methodological validity of comparing models with an arbitrarily chosen, fixed prompt format.
}. Furthermore, we present a suite of analyses that characterize the nature of this sensitivity, including exploring the influence of particular atomic perturbations and the internal representation of particular formats.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores a very interesting question, which is the impact of different prompt formats of LLMs on the accuracy of downstream tasks. The authors found that this impact is significant to some extent and present a new algorithm called FORMATSPREAD, which can estimate the performance spread of different prompt formatting choices. FORMATSPREAD efficiently searches the space of plausible prompt formats within a specified computational budget.

### Strengths
- The issue discussed in this paper, i.e., LLM evaluation should not be limited to a single specific prompt, has good informativeness for the community.
- This paper is well written and easy to understand. 
- The proposed construction of grammar rules for different prompt formats and the design of sensitivity evaluation are quite ingenious.

### Weaknesses
As the authors claim that LLMs are extremely sensitive to subtle changes in prompt formatting, with performance differences of up to 76 accuracy points, which is quite surprising. It is necessary to conduct a more in-depth analysis of these somewhat counterintuitive conclusions. For example, 
1. Is the difference in  prompt formats the only influencing factor, or do other confounders exist, such as the content length of in-context, different tokenize methods, or even the specific phrasing within the prompt itself beyond the structural format? The analysis should consider not just the length of in-context examples but also the variability in length across different examples within the same prompt, as this could introduce another source of variance. Furthermore, the impact of different tokenization methods should be explored, considering that different tokenizers might break down the same prompt into different token sequences, potentially leading to varying model interpretations.
2. It is difficult to predict the impact on specific task sensitivities. How can we analyze which types of tasks are more susceptible to prompt format influences, rather than just conducting sensitivity evaluations? This requires further explanation. For instance, are tasks that rely more on logical reasoning or those that require more factual recall more sensitive to prompt format changes? A more granular analysis of task types and their inherent characteristics is needed to understand this sensitivity.

### Questions
1. Add more analysis about cofounders, such as content length in the examplars, different tokenize methods, etc.
2. Add further explanation of which specific tasks are more susceptible of changes in prompt formatting.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors claim that in recent trends, LLMs are the inevitable choice for language technologies; their sensitivity to prompt formatting results in critical issues. The sensitivity remains critical even after increasing model size, usage of in-context learning, and instruction-tuning. Given this situation, authors suggest evaluating the performance of LLMs with various prompt formatting, not with a single prompt format. The authors also report that format performance across LLMs has a low correlation, which supports the multi-prompt format evaluation of LLMs. To facilitate the multi-prompt format, the authors propose an analysis method, FORMATSPREAD, that evaluates a set of plausible prompt formats for a given task. The proposed method induces the concept of semantically equivalent formats and measures the performance gap among LLMs queried with the different formats but in a semantically equivalent set, procured by the help of Bayesian Optimization.

### Strengths
- Focus on the subject that has not taken much attention from the community but should be addressed for robust application of LLMs
- Evaluating LLMs over the prompt distribution provides a more informative understanding of the model's performance and robustness than evaluating only with a single prompt.
- The proposed method can be utilized on API-gated models, with no need for access to model weights.

### Weaknesses
 - The authors cast the problem of searching prompt space as a bandit problem. However, many current important applications of LLM assume multi-turn conversation between the user and LLM, which is highly dependent on the conversation history.
- In Algorithm 1, the formulation assumes the reward of each arm is success or failure, but in the NLP field, there are many important tasks where the output of LM cannot be determined between success or failure (for example, a task needs human alignment). Does the formulation still hold for the tasks that cannot be evaluated in discrete value?

### Questions
- As the search space of the prompt is intractable, a good initial point (in this case, a prompt) would be crucial for successful entire optimization (as authors assume non-adversarial user). How can we be convinced that we start from a good initial point?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the sensitivity of large language models (LLMs) to prompt formatting choices and investigates the impact of prompt design on LLM performance in few-shot (especially few-shot classification) settings. The authors find that even subtle changes in prompt formatting can have a significant effect on model behavior, with performance differences of up to 76 accuracy points. This sensitivity remains even when the model size or the number of few-shot examples is increased. 
The authors argue that evaluating LLMs with a single prompt format is inadequate and propose reporting a range of performance across plausible formats. 
They also demonstrate that format performance weakly correlates between models, questioning the validity of comparing models using a fixed prompt format. To facilitate systematic analysis, the authors introduce an algorithm called FORMATSPREAD, which quickly evaluates a sampled set of prompt formats for a given task. The paper emphasizes the importance of reporting and considering prompt format variations when comparing models and highlights the impact of formatting choices on model behavior by extensive experiments.

### Strengths
1. The paper investigates a critical issue for Large Language Models (LLMs), specifically the impact of formatting on the few-shot examples used in prompts.

2. The assertion that "The performance of Large Language Models (LLMs) is highly sensitive to prompt formatting choices, especially in few-shot settings," is substantiated by numerous experiments on few-shot classification tasks (e.g., Super-Natural Instructions) and short text generation tasks, such as identifying the second letter of a word, performing arithmetic, or responding with a synonym for a given word.

3. In Section 3, the authors formally define the "grammar" of plausible prompt formats, thereby making the problem formulation more rigorous.

### Weaknesses
1. The paper primarily substantiates its core claim that "Performance of large language models (LLMs) is highly sensitive to prompt formatting choices, particularly in few-shot settings," through experiments in classification tasks. However, the scope of the experiments does not extend to the frequently utilized capability of LLMs for long text generation. While short text generation tasks (such as identifying the second letter of a word, adding numbers, or responding with a synonym) are discussed in the appendix, these do not fully capture the important aspect of long text generation. Hence, I suggest that the authors either explicitly state that these findings are specifically under the context of classification tasks or conduct additional experiments on long-text generation to avoid any potential overclaim or misleading interpretation.

2. For Figure 2, I recommend that the authors include the Pearson correlation coefficient directly on the figure for a more comprehensive representation of the data.

Overall, I believe this paper studies an important question. If the authors can address my concerns, I would consider increasing my score.

### Questions
1. In Section 3.2, the performance spread is quantified as the difference between the maximum and minimum values. I suggest that a more comprehensive approach would be to report both the range (max - min) and the standard deviation, providing a fuller understanding of the data distribution.

2. In the experimental section, the authors explain that classification tasks were selected for their ease of automatic evaluation. I am curious about the challenges associated with measuring performance for text generation tasks, especially considering the benchmarks that have been proposed recently.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
