# From Loops to Oops: Fallback Behaviors of Language Models Under Uncertainty

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Large language models (LLMs) often exhibit undesirable behaviors, such as hallucinations and sequence repetitions.
We propose to view these behaviors as fallbacks that models exhibit under uncertainty, and investigate the connection between them.  
We categorize fallback behaviors --- sequence repetitions, degenerate text, and hallucinations --- and extensively analyze them in models from the same family that differ by the amount of pretraining tokens, parameter count, or the inclusion of instruction-following training.
Our experiments reveal a clear and consistent ordering of fallback behaviors, across all these axes: 
the more advanced an LLM is (i.e., trained on more tokens, has more parameters, or instruction-tuned), 
its fallback behavior shifts from sequence repetitions, to degenerate text, and then to hallucinations.
Moreover, the same ordering is observed throughout a single generation, even for the best-performing models; as uncertainty increases, models shift from generating hallucinations to producing degenerate text and then sequence repetitions. 
Lastly, we demonstrate that while common decoding techniques, such as random sampling, might alleviate some unwanted behaviors like sequence repetitions, they increase harder-to-detect hallucinations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper looks at “fallback” behaviors in large language models in the face of epistemic uncertainty, specifically focusing on repetitive text, degenerate phrasing, and hallucinations. They set up scenarios to control the presence of epistemic uncertainty and characterise the outputs of various LLMs, evaluating how the number of parameters, amount of pretraining data, instruction-following training, and decoding impact the type of fallback behavior exhibited. They observe what they call a “fallback hierarchy” where as models become more uncertain (or if they are weaker to begin with), they rely more on basic degenerate behaviors. They posit that fallback behaviors are interconnected, based on the observation that models transition from one behavior to another as uncertainty decreases. Importantly, they find that larger, more sophisticated models also exhibit fallback behaviors in the face of uncertainty, even if they may be more sophisticated fallback behaviors and that some techniques claimed to mitigate degenerate behaviors have other adverse effects or only a limited ability to help

### Strengths
* The work offers a thorough analysis across various LLM families of different types of frequently-observed degenerate behavior
* The experimental setup seems like a reasonable way to control for epistemic uncertainty
* There are interesting empirical findings about the prevalence and characteristics of degenerate outputs from modern LLMs

### Weaknesses
 * The contributions of the work are limited: 
    * empirical observations are made but no insights about what the source of these behaviors are or how they can be fixed are given
    * The analysis is limited to the presence of epistemic uncertainty, but there are other scenarios in which degenerate behaviors occur (e.g. when adversarial prompts are given or in the face of aleatoric uncertainty) so we’re still far from a comprehensive empirical analysis of degenerate behaviors 
* The setups are rather contrived and since the work's results are only empirical, its not clear what the practical implications of them are
* While the authors claim to explore the impact of decoding on these fallback behaviors, they seem to only look at greedy decoding and temperature sampling. They also seem to only explore one prompt as a “mitigation” technique
* Some claims don’t feel adequately supported. E.g., “fallback behaviors… emerge…unavoidably under uncertainty” Even though a comprehensive set of prevention techniques weren’t explored

### Questions
I don’t understand what is meant in the sentence “Moreover, introducing randomness reduces the number of correct facts, which could be attributed to the random skipping of correct facts that have low confidence in the model.” Could you clarify?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies how LLMs behave in the face of epistemic uncertainty, claiming that the LLMs “fall back” to various strategies, such as hallucinations, degenerate text, and more when this occurs. The study explores these fallback strategies across several model parameters, including model size, pretraining tokens, instruction tuning, and decoding algorithms.

The paper presents some interesting findings such as:

1. Larger models tend to be more factual but are more likely to hallucinate as a fallback strategy rather than generate repetitive or poorly formatted text.
2. As the number of pretraining tokens increases, the number of factual responses also increases, though the model may hallucinate more frequently.
3. Instruction tuning makes the model's fallback strategies more complex without significantly changing the percentage of factual answers.
4. Increasing the sampling temperature slightly reduces factuality but decreases repetitiveness and occasionally enhances creativity.


The authors conduct experiments on several different models, checkpoints, and datasets.

### Strengths
The paper analyzes fallback mechanisms when the model encounters uncertainty—an important and timely issue. The experimentation is extensive, with tests on multiple models across various datasets to validate its conclusions. The findings are interesting and hold significant value for other researchers working on LLM hallucinations. Some of the conclusions seem less surprising (although empirical verification of them is still useful)

While the paper has notable strengths, there are some concerns (see weaknesses). I am open to raising my score once these issues have been addressed.

### Weaknesses
1. **Presentation Improvements**

   - The paper’s presentation could be refined. In its current form, it may take considerable time for readers to extract the main takeaways.
   - There are multiple task settings, and results can sometimes be difficult to interpret due to the variety of datasets used for each claim. Standardizing these settings could improve clarity.
   - In some cases, important results are presented only in the appendix, which can be frustrating for readers. Additionally, the graph captions could be more informative (for instance, specifying the dataset used for Figures 3 and 4).
   - Terminology is sometimes inconsistent—for example, the term "stronger models" is used, but it’s unclear what this means.

2. **Experimentation Concerns**

   - Why are instruction-tuned models tested only on TriviaFacts? Although list-based questions may simplify evaluation, this limits conclusions to a single, small, self-created task (hence weakening the claim) 
   - Some parameters are analyzed independently, even though they often co-occur. For example, model size could be varied specifically within instruction-tuned models. This approach sometimes leads to inconsistencies. In Figure 21, llama-3-8B-inst is shown to be more factual (% factual) and hallucinates significantly more than llama-3-70B-inst—contradicting the earlier finding that larger models tend to produce more factual answers while hallucinating more. This also appears inconsistent with broader findings, such as in the Llama-3 report, where llama-3-70B is generally noted as more accurate.
   
   These outliers and inconsistencies warrant further discussion.

   - The paper does not mention that the 70B model is quantized (FP8). Comparing a quantized model to a full-precision model can introduce inconsistencies and this should be mentioned.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper mainly analyzes the fallback behaviors of large language models (LLMs), which include sequence repetitions, degenerate text, and hallucinations. This paper conduct various experiments to explore the fallback behaviors in models from the same family that differ by  the amount of pretraining tokens, parameter count, or the inclusion of instruction-following training. It further discuss factors influencing the fallback behaviors of a LLM, such as sampling methods, simplifying the question and prompt engineering. The experiments reveal the following phenomenon:
1. Increasing model strength through extra pretraining, more parameters, or instruction tuning shifts fallback behaviors from simple to complex, i.e., from repetitions to hallucinations.
2. While LLMs have some internal capability to avoid hallucinations, this fallback behavior is inherent to their generation scheme and is likely unavoidable with current decoding methods. 
3. As models generate longer texts, they shift in their fallback behavior, first generating hallucinations and eventually producing degenerate text.

### Strengths
•	This paper provides a controlled analysis of LLM undesired behaviors, showing that strengthening models increases hallucinations over degenerate text and repetitions.
•	This paper demonstrates that during generation, LLMs undergo a phase shift from correct answers to hallucinations and then repetitions.
•	This paper indicates that methods to reduce text degeneration, like sampling, increase errors and hallucinations.

### Weaknesses
•	This paper seems to overclaim its contribution and conclusion. According to the datasets this paper used, the LLMs need to recall multiple facts that are related to the same topic. The other QA circumstances are ignored, including the simple QA like Natural Questions, multi-hop question answering like HotpotQA, open-ended long-formed question answering but beyond biography like ELI5. Also many other knowledge intensive tasks are also not discussed, which is also related with the epistemic uncertainty.
•	According to the paper, the fallback behaviors include sequence repetitions, degenerate text, and hallucinations. But degeneration is not discussed in the metric and experiment results.
•	The experiment setting of FQAMP seems not reasonable. If forcing uncertainty is essential, it is more natural to replace the subjects with a low popularity names. If replacing with made-up names and requiring LLMs to abstain, it is an OOD problem but not an uncertainty problem.

### Questions
•	If this paper focuses on “epistemic uncertainty” and do not explore other types of uncertainty, why this paper is titles “under epistemic uncertainty”.
•	Is the TRIVIAFACTS dataset evaluated? The question mentioned in the paper, which is “The following 25 colors are in the Olympic rings.” seems to mislead LLMs to repeat and hallucinate.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies different fallback behaviors of LLMs that occur under uncertainty,
For this, the authors construct settings where the model is expected to be uncertain.
They evaluate various models differing in both size and how long they are trained and compare greedy vs. sampling-based decoding methods.
The authors find that "stronger" models (trained longer, more parameters) exhibit more complex fallback behaviors which means that more hallucinations are produced.

### Strengths
- The idea of "epistemic uncertainty by construction" is an interesting way of circumventing problems with quantification of uncertainty.

- Overall, the paper seems methodologically sound.

- The paper is very well-written and easy to follow.

- The ideas presented in the paper can help guide further works on combating (unwanted) fallback behaviors of LLMs

### Weaknesses
 - Epistemic uncertainty as a whole is a quite rich concept that might warrant a larger discussion. In particular, the authors focus mainly on uncertainty about facts but mostly neglect other forms / sources of uncertainty that are also often seen as contributing to epistemic uncertainty. An example is L417-419: verbatim recollection is hypothesized to be more present in OOD settings than factual uncertainty but OOD settings are often also thought to give rise to epistemic uncertainty, because not enough training data is observed in the domain, leading to a lack of knowledge. For example, the authors could discuss the relation of epistemic uncertainty and aleatoric uncertainty [1] and the sources of epistemic uncertainty further [2]

- The main dataset is comparably small with only 95 items but also highly curated. Similarly, the other datasets are also fairly small, usually around 100 examples

- Some statements are a bit imprecise, for example: what is meant with internal capability to avoid hallucinations (L303) and what backs it up experimentally?

### Questions
Below are some questions and comments:

- Footnote 2 is a bit hard to understand without having read later parts of the paper

- it's not immediately clear to me why Datasets 1-3 have different levels of epistemic uncertainty, could you clarify this?

References

[1] Hüllermeier, Eyke, and Willem Waegeman. "Aleatoric and epistemic uncertainty in machine learning: An introduction to concepts and methods." Machine learning 110.3 (2021): 457-506.

[2] Baan, Joris, et al. "Uncertainty in natural language generation: From theory to applications." arXiv preprint arXiv:2307.15703 (2023).

### Soundness
3

### Presentation
4

### Contribution
3
