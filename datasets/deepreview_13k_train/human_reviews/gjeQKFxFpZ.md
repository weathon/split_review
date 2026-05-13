# Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs

- Decision: Accept
- Scores: 5, 6, 8, 5

## Abstract
Empowering large language models (LLMs) to accurately express confidence in their answers is essential for reliable and trustworthy decision-making. Previous confidence elicitation methods, which primarily rely on \emph{white-box access} to internal model information or model fine-tuning, have become less suitable for LLMs, especially closed-source commercial APIs. This leads to a growing need to explore the untapped area of \emph{black-box} approaches for LLM uncertainty estimation. To better break down the problem, we define a systematic framework with three components: \emph{prompting} strategies for eliciting verbalized confidence, \emph{sampling} methods for generating multiple responses, and \emph{aggregation} techniques for computing consistency. We then benchmark these methods on two key tasks—confidence calibration and failure prediction—across five types of datasets (e.g., commonsense and arithmetic reasoning) and five widely-used LLMs including GPT-4 and LLaMA 2 Chat. 
Our analysis uncovers several key insights: 1) LLMs, when verbalizing their confidence, tend to be \emph{overconfident}, potentially imitating human patterns of expressing confidence. 2) As model capability scales up, both calibration and failure prediction performance improve, yet still far from ideal performance. 
3) Employing our proposed strategies, such as human-inspired prompts, consistency among multiple responses, and better aggregation strategies can help mitigate this overconfidence from various perspectives. 
4) Comparisons with white-box methods indicate that while white-box methods perform better, the gap is narrow, e.g., 0.522 to 0.605 in AUROC.
Despite these advancements, none of these techniques consistently outperform others, and all investigated methods struggle in challenging tasks, such as those requiring professional knowledge, indicating significant scope for improvement. 
We believe this study can serve as a strong baseline and provide insights for eliciting confidence in black-box LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies approaches to eliciting reliable confidence estimates from large language models about their statements.  The paper studies closed-box methods for confidence elicitation exploring (1) prompting strategies for verbalized confidence; (2) sampling approaches to measure variance across multiple responses; and (3) aggregation methods to compute consistency measures.

### Strengths
- This paper studies an important problem.  When an LLM's reliability is critical to an application or higher-level task, knowing the likelihood that the LLMs responses is correct or not is critical.

The overall approach, combining prompting, sampling, and aggregation, is an elegant approach for closed-box confidence solicitation, if it can be calibrated or its reliability as a measure otherwise completely characterized.

The experiments span many task-domains and multiple models.

### Weaknesses
The experimental results show that the method is useful in identifying uncertainty, but performance varies significantly across benchmark tasks and no single method is clearly better than others.  Given a new task, it is not clear which method will give the best performance, or even if the best performing method on a hold out set will generalize to real problems in a domain.  I appreciate that the authors call this out in the discussion, saying that none of the current algorithms are satisfactory.

The high level observations enumerated in the introduction are interesting but also seem very preliminary, and difficult to operationalize or build upon.


minor:
- the acronym ECE should be defined at first use.  
- typo page 6: "aevaluation" -> "evaluation"

### Questions
Is there a reason to believe that the model's certainty _should_ be correlated with model correctness?  Or to understand a priori (e.g., based on training data) when it might be more or less likely to be so?

Minor variations in prompt wording can have significant effects on performance.  How was the specific prompt text chosen for each of the prompt strategies?  was it optimized or experimented with?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A comprehensive study on self-estimation of uncertainty by LLMs. The authors introduce multiple design choices that can affect uncertainty elicitation and then evaluate them on existing LLMs.

### Strengths
- Uncertainty estimation is an important question for LLMs. The findings of this study can be impactful in practice
- The 3-part framework of prompting strategy, sampling and aggregation provide clarity.
-The evaluation is comprehensive across many datasets.

### Weaknesses
The strategies presented are reasonable (but not super novel, as far as I understand). So the contribution should be evaluated on the empirical evaluation. Here, it is unclear how to interpret the results. No strategy seems to be work well always. 

I understand it is hard to analyze black-box LLMs, but still some discussion on why some strategy works, and why it does not, will be useful. 

What is the best combination of prompting, sampling and aggregation? can the authors propose the best way for practitioners while also noting the limitations? Right now, the message seems to be that nothing works. But it may be useful to present a version of the best performing method.

### Questions
see the weaknesses above.

### Soundness
4 excellent

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
The paper proposes a unified framework under black box setting to evaluate how calibrated large language models are for their predictions. Specifically, no logits or internal states of LLM are assumed given but the models can be asked to provide explicit confidence. The authors evaluate 5 different prompting strategy and various aggregation strategy to elicit better calibrated results from the models.

### Strengths
1. The paper is very well-written and tackles the black box confidence calibration in a timely manner. The approach is very targeted to LLMs which provide many insights that are not available from calibrating image classification models.

2. The evaluation is very thorough and the two calibration tasks defined are reasonable.

### Weaknesses
1. It seems black-box based confidence elicitation approaches are generally unsatisfactory in calibration performance. Can the authors directly compare them with white-box based calibration approaches such as token probability based calibration approach on open-source models and observe how large the gap can be on ECE and failure prediction?

2. Equation 3. Shouldn't we maximize with respect to P since we are doing an MLE estimation?

### Questions
Please see the weakness section above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper evaluateds an LLM's capability to express uncertainty. To this end they define a systematic evaluation framework.

+ LLMs are a highly relevant topic
+ Elicitating confidence is also an important topic in deep learning in general
+ The study performs extensive evaluation on multiple datasets and LLMs
- The evaluation and outcomes yield little novel insights (see also detailed comments)
- The methods are standard, a methodological contribution would be highly appreciated. The idea to use LLMs for self-assessment is all-to-common. That said, it is also interest to assess it in this context, but on its own a marginal contribution. The prompting/aggregation techniques at best partially mitigate this, but they are also well-known. In short, more would be expected for a strong contribution.


Detailed comments?
> 1) LLMs, when verbalizing their confidence, tend to be overconfident...
LLMs are known to be "Fluent but non-factual" or "Convincing though wrong". Given that this study focuses only on evaluation I would have expected more novel findings as key fining.
> 2) As model capability scales up, both calibration and failure prediction performance improve, yet still far from ideal performance.
That larger LLMs are better (on all benchmarks) than smaller ones is also general knowledge - check the LLama2 paper, for example, and compare benchmarks for 7B,13B...
> It would be interesting (and maybe even necessary) to study how much the uncertainty estimates depends on the prompt, i.e., if you state in the prompt "Appear confident" are estimates more overconfident?

### Strengths
see above

### Weaknesses
 The paper evaluateds an LLM's capability to express uncertainty. To this end they define a systematic evaluation framework.

+ LLMs are a highly relevant topic
+ Elicitating confidence is also an important topic in deep learning in general
+ The study performs extensive evaluation on multiple datasets and LLMs
- The evaluation and outcomes yield little novel insights (see also detailed comments)
- The methods are standard, a methodological contribution would be highly appreciated. The idea to use LLMs for self-assessment is all-to-common. That said, it is also interest to assess it in this context, but on its own a marginal contribution. The prompting/aggregation techniques at best partially mitigate this, but they are also well-known. In short, more would be expected for a strong contribution.


Detailed comments?
> 1) LLMs, when verbalizing their confidence, tend to be overconfident...
LLMs are known to be "Fluent but non-factual" or "Convincing though wrong". Given that this study focuses only on evaluation I would have expected more novel findings as key fining.
> 2) As model capability scales up, both calibration and failure prediction performance improve, yet still far from ideal performance.
That larger LLMs are better (on all benchmarks) than smaller ones is also general knowledge - check the LLama2 paper, for example, and compare benchmarks for 7B,13B...
> It would be interesting (and maybe even necessary) to study how much the uncertainty estimates depends on the prompt, i.e., if you state in the prompt "Appear confident" are estimates more overconfident?


### Questions
see above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
