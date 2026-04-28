# Training on the Test Task Confounds Evaluation and Emergence

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We study a fundamental problem in the evaluation of large language models that we call \emph{training on the test task}. Unlike wrongful practices like training on the test data, leakage, or data contamination, training on the test task is not a malpractice.  Rather, the term describes a growing set of \new{practices that utilize knowledge about evaluation tasks at training time.}
We demonstrate that training on the test task confounds both relative model evaluations and claims about emergent capabilities. We argue that the seeming superiority of one model family over another may be explained by a different degree of training on the test task. 
To this end, we propose an effective method to adjust for 
the effect of training on the test task on benchmark evaluations.
Put simply, to fine-tune
each model under comparison on the same task-relevant data before evaluation. 
We then
show that instances of emergent behavior disappear gradually as models train on the test task.
Our work promotes a new perspective on the evaluation of large language models with broad implications for benchmarking and the study of emergent capabilities

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper defines *training on the test task* as a potential problem for evaluating LLMs, which could be common practice and strictly speaking not data contamination. They show that doing so may allow a model to achieve better results on a benchmark while not having better abilities overall. They suggest that further fine-tuning all models can help with better comparison across models, and show that doing so restores clearer scaling trends.

### Strengths
* They test their method on on a large set of base models with different sizes. This also allows them to compare scaling on benchmarks.
* The proposed method is promising for better evaluations/comparisons and light on compute, requiring only fine-tuning.

### Weaknesses
 * They only do so for pre-trained base models. In practical settings, we often look at the benchmarks of fine-tuned chat models, or models further fine-tuned off base-models (e.g. LLama derivatives). It is not clear whether their findings would apply to already-finetuned models.
* They classify 'old' models as before November 2023, which seems somewhat arbitrary. I understand that choosing Nov 2023 reveals some sort of improvement given the same compute, but this could be due to reasons other than training on the test task. More justification is needed on why the improvement gap is a good heuristic for whether a model was trained on the test task. Alternative analysis on whether much more models after Nov 2023 include instruction data in the pre-training set could similarly justify why Nov 2023 is a good cut-off point.
* Ultimately, benchmarks are used to understand how good a model is at a general skill, like mathematical reasoning for MMLU and GSM8K. This method proposes to 'fight fire with fire' by fine tuning all models on the test task. Would your method merely reliably measure how well models performs on a specific benchmark, rather than how well models are at the ability it's meant to measure?

### Questions
* Ultimately, benchmarks are used to understand how good a model is at a general skill, like mathematical reasoning for MMLU and GSM8K. This method proposes to 'fight fire with fire' by fine tuning all models on the test task. Would your method merely reliably measure how well models performs on a specific benchmark, rather than how well models are at the ability it's meant to measure?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores an interesting phenomenon: training on the test task, which differs from training on the test data. Training on test tasks implies that task-relevant data is included in the pretraining stage of a language model. The paper highlights how newer models benefit from training on the test task, but when fine-tuning older models on task-relevant data, this performance advantage disappears.

### Strengths
- This paper explores an ever-increasingly important area of LLMs: the "science of evaluations."
- It explores the implications of task-specific training for language models, providing evidence that training with task-specific data is beneficial. They find that many models from November 2023 gain advantages from this type of training. Additionally, they show that task-specific training is more likely responsible for recent boosts in model performance when FLOPs are held constant.
- The paper's implications (as stated in the discussion) suggest that training on task-specific data may be beneficial across models.
- The experiments and the paper are logical and well thought through.

### Weaknesses
 - How was November 2023 chosen as the cutoff? I wonder what would have happened if you had chosen November 2022. How would the results be affected?
- It is unclear how much hyperparameter tuning might affect results when training on task-specific data. How much could hparam tuning affect the results? How was the initial sweep in Appendix A.2 chosen? Although a full sweep might be expensive, additional clarity on how these were chosen will alleviate my concern. 
- Lack of consideration of instruction-tuning models. How do you think instruction tuning models might impact this study as often the newer datasets are comprised of examples to explicitly increase benchmark performance [1]? 
- Only a couple of main evaluation datasets are explored in the paper.

### Questions
- Do you the authors think LLMs should be part of the title as only LLMs are explored in the paper?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper argues that newer language models only appear to be better on metrics like MMLU than earlier, iso-compute language models because of the presence of data in distribution to MMLU in the pretraining set. The paper demonstrates this by showing that when these models are finetuned on MMLU/GSM8K before evaluation, the performance differences between different model families go away. The paper also shows that emergent behaviors are less common under this new evaluation protocol.

### Strengths
- The paper is very clearly presented and argues persuasively. The figures are easily understood at a glance.
- The conclusion argued for is surprising and novel, and has broad implications for evaluation methodology of LLMs and emergent behaviors in LLMs.

### Weaknesses
 - The p-values for signficance in figure 1 overestimate significance because of correlation due to models being from only a few model families.
- The paper never actually directly checks the hypothesis of more in-distribution data being the cause of higher MMLU performance out of the box, despite arguing for it via implication from the finetuning result.

### Questions
I'd be interested to see (on open source models with available datasets, or by sampling unconditionally from base models) whether there is more MMLU-like data in model families which appear to do better on MMLU when using the naive evaluation method.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
### Paper Summary
This paper asks if recent open-source models are in fact better than previous models: Does exposure to task data during pre-training explain the difference in model performance? (Yes). The authors find evidence that the difference on task performance can be explained by exposure to these tasks during the end of pre-training, not that more recent models are fundamentally better LLMs.

### Review Summary
There could be some world where this paper is simply stating the known fact that most models adjust the type of training data towards the end of pre-training to include task-relevant data, and that that inclusion improves performance. However, I think this paper does a good job of showing that this inclusion in particular seems to be making a key/big difference in models' improved performance, and that the inclusion during pre-training itself (while its being mixed with other data) doesn't seem to have an outsized impact on the ability to answer task-relevant questions.

### Strengths
The authors have a number of nice (creative/thoughtful) experiments showing how older models do equally well when given more task data, that changing the style of the question (not content) also closes the gap between models, and finally, that, when given more data, model families all seem to follow the same scaling law.

The figures are all great/clean/pretty/legible!

The writing is also all clear/careful!

### Weaknesses
* some could say that this is an obvious finding / direct outcome of how models recently have been trained. I don't hold this view. I find it interesting that there is not an additional/additive benefit found in recent models (from adding task related data in the end of pretraining), and interesting that the results are so stark. [i don't read your paper as saying that there is no gain/improvement in recent models, but rather, that performance doesn't extend beyond what fine-tuning directly upon the task in question would yield]
* figure 3 is unclear. the added information/gain of figure 3 vs figure 1 is unclear, esp. when looking at figure 3 alone (without referring to the text). to start, if I understanding things correctly, I think the colors of the points/lines should not be the same as the other figures as the underlying data is different from the other figures. the shared colors (to me) is misleading.

* line 244, "These results provides..." --> "These results provide..."
* line 259, "contrast Figure 3 and Figure 1 Quantitatively..." --> "contrast Figure 3 and Figure 1. Quantitatively..."
* consider turning "What does MMLU test for?" into an active statement / takeaway.
* line 429 R^2 is formatted differently than line 430
* line 37, end of second paragraph. I was tripped up by "of some" and "of others". I now believe it is "of some models" / "of other models". I would guess the elisions were made to shorten/clean the paragraph? When I first read it I thought it was a typo that meant "to some people" / "to other people" (like different people will interpret this phenomena differently.)

### Questions
*  I didn't fully follow the final paragraph in section 4.2. Would your results not give an answer to your posed question? (i.e., doesn't task-training explain the improvements, and fall outside the scaling laws?)
* What eq do you fit in figure 8 bottom? Switching the equation used in the top row the one used in the bottom row didn't seem to be motivated in the text. Doesn't eq 1 also a capture a log-linear relationship? Spelling a bit more out here would help.
    * Giving a hint in the caption of figure 8 that the data are the same in both rows might help
    * Labelling the rows within the figure (not only the caption) might also help (like you do in figure 4).

### Soundness
3

### Presentation
4

### Contribution
3
