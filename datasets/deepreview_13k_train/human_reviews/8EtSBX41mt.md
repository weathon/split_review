# Can LLMs Separate Instructions From Data? And What Do We Even Mean By That?

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Instruction-tuned Large Language Models (LLMs) show impressive results in numerous practical applications, but they lack essential safety features that are common in other areas of computer science, particularly an explicit separation of \emph{instructions} and \emph{data}. This makes them vulnerable to manipulations such as indirect prompt injections and generally unsuitable for safety-critical tasks. Surprisingly, there is currently no established definition or benchmark to quantify this phenomenon. 
In this work, we close this gap by introducing a formal measure for instruction-data separation and an empirical variant that is calculable 
from a model's outputs. We also present a new dataset, \dataset, that allows estimating the measure for real-world models. 
Our results on various LLMs show that the problem of instruction-data separation is real: all models fail to achieve high separation, and canonical mitigation techniques, such as prompt engineering and fine-tuning, either fail to substantially improve separation or reduce model utility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of whether LLMs can separate instructions from data, which is important to the safety of LLMs. Specifically, this paper first introduces a formal measure for this problem, then proposes a new benchmark (i.e., SEP) to evaluate LLMs’ performance on this problem, and then conducts a study on the mitigation strategies of this problem.

### Strengths
- The paper explores an interesting and important research direction.
- The paper proposes a new benchmark, namely SEP, to evaluate the problem of instruction-data separation.

### Weaknesses
 - There is a lack of detailed analysis on the evaluation results of different LLMs on SEP. For example, while authors report an abnormal phenomenon where better or larger models do not show stronger separation scores, they fail to provide either any detailed analysis or any explanation on the potential reason for this phenomenon.
- The study of mitigation strategies is not comprehensive. For example, while several existing fine-tuning techniques that target instruction-hijacking problems [1,2] can be naturally utilized to handle the problems in SEP, authors only include the vanilla fine-tuning technique in the study.

### Questions
None beyond the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper motivates and formalizes the problem of instruction-data separation in LLMs - the ability to distinguish between instructions to be executed and data to be processed. The authors propose both a theoretical formal measure for instruction-data separation and a practical empirical metric for evaluating it. They introduce SEP, a carefully constructed dataset for testing instruction-data separation, and evaluate 9 popular LLMs using their methodology. Their results reveal that instruction-data separation is a significant problem in current LLMs, does not improve with model scale. These findings motivate the need for further research to address this limitation of LLMs.

### Strengths
- The results are properly caveated and presented with appropriate skepticism.
  - I appreciate that the authors explain their results with skepticism. E.g. pointing out that the results of GPT-4 may be impacted by the fact that GPT-4 created the SEP dataset (page 8); acknowledging that the set of prompt templates was not exhaustive (page 9); etc.

- Well written.
  - The paper was a pleasure to read. It was logical and easy to follow.
  - I appreciate that each definition or result has coherent discussion following it.
  - The problem of instruction-data separation is also well motivated.

### Weaknesses
 - Some technical details are lacking.
  - See questions 1-3 below.

- Results are hard to make sense of.
  - As acknowledged by the authors, SEP performance varies widely between models (even between models of different scales from the same model family), as does the impact of the mitigations.
  - It is hard to draw conclusions from the results (Table 4, 5) as a result. The lack of clear patterns or trends makes it difficult to understand what factors contribute to better instruction-data separation in general.

### Questions
1. What was the fine-tuning training objective?
    - I am specifically wondering if there was a dual objective to both achieve good separability and also good utility, or if only one of these was incentivized in the fine-tuning procedure.

2. How were the "artificial" system prompts (used for Gemma and Starling) determined?
    - I'm wondering whether there was some trial and error / evaluation on some validation set to, in an effort to get a system prompt that behaved in a certain way. This (limited) optimization pressure could introduce some bias in the resulting "artificial" system prompt.

3. What is a task vs a subtask? (section 4)
    - In general I thought that the dataset creation methodology could have included more details.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the ability of large language models (LLMs) to distinguish between instructions and data within a given prompt. To evaluate this, the authors created a dataset where each sample contains {Task Prompt, Data Prompt, Probe Instruction, and Witness}. A perfect model would follow only the instructions from the task prompt while ignoring any instructions from the data prompt. If the model mistakenly follows the probe instruction, a "witness string" will appear in its output. By comparing the model’s behavior when the probe instruction is part of the task prompt versus when it appears in the data prompt, the authors assess its ability to separate instructions from data. Two evaluation metrics are introduced: the separation score and the utility score. The dataset and these metrics were used to evaluate GPT-3.5, GPT-4, and seven other models, ranging from 2B to 8B parameters. The paper also discusses three potential ways to improve model performance: prompt engineering, prompt optimization, and fine-tuning.

### Strengths
1. The paper is well-structured, with clear problem definitions, case studies, and experimental results.
2. The study is comprehensive, covering problem definition, evaluation metrics, dataset creation, experimental evaluation, and potential methods for performance improvement.
3. The dataset and reasonable metrics proposed provide an effective way to evaluate the instruction-data separation capabilities of LLMs.

### Weaknesses
1. One core contribution of the paper is the dataset; however, there are some questionable aspects regarding how it was built. As shown in Table 1, the "probe instruction" is appended to the end of the "data prompt," though they bear no semantic connection. Intuitively, this kind of example may not occur in real-world settings, creating input prompts that seem somewhat artificial. This raises concerns about whether the evaluation results truly reflect the model's ability to handle instruction-data separation in real-world usage. Moreover, the dataset creation process, as detailed in Appendix A, seems quite straightforward, being largely based on existing data and GPT-4, which furthers the aforementioned concern.
2. Some experimental setups and conclusions warrant more scrutiny:
    - **Experimental Setup**: In Tables 4 and 5, the baseline “Original” assigns the system prompt to the instruction argument, while the user prompt is treated as data. This setup seems problematic because it blends multiple instructions from the user and the system without clearly distinguishing what should be treated as instructions versus data, which may lead to input ambiguity. I suspect this confusion contributed to the low score for GPT-4 (20.8%) in Table 4. A more suitable baseline might be **PromptEng** method.
   - **Some conclusions appear misaligned with experimental results**: 
       - In Line 450, the authors suggest fine-tuning significantly reduces utility, making it impractical. However, this conclusion seems premature. The poor performance of fine-tuning could be due to inadequate data quality or other subtle issues. Based on the current results, it’s too early to definitively state that fine-tuning is not a viable solution.
       - In Lines 461 and 497, the authors speculate that GPT-4's superior performance may be due to "principled differences in model architecture or training." However, the experimental data doesn’t robustly support this since models larger than 8B parameters were not included. Model size is a crucial factor that hasn’t been sufficiently considered. Including models like LLaMA3-70B, Qwen2.5-72B, or Mistral 8*7B would lend more solid support to the conclusions.

### Questions
1. What’s the primary difference between studying "separation of instructions and data" and "prompt injection"? Why is it important to study them separately? What are the potential consequences if we don’t?
2. This is an open-ended question to encourage the author to share their perspective. In what practical scenarios do you think the ability to separate instructions from data is especially critical? The paper doesn’t seem to delve deeply into this consideration.

### Soundness
2

### Presentation
3

### Contribution
2
