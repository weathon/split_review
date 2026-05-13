# Are Models Biased on Text without Gender-related Language?

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
Gender bias research has been pivotal in revealing undesirable behaviors in large language models, exposing serious gender stereotypes associated with occupations, and emotions.
A key observation in prior work is that models reinforce stereotypes as a consequence of the gendered correlations that are present in the training data. In this paper, we focus on bias where the effect from training data is unclear, and instead address the question: \textit{Do language models still exhibit gender bias in non-stereotypical settings?}
To do so, we introduce \textbf{UnStereoEval} (USE), a novel framework tailored for investigating gender bias in stereotype-free scenarios.
USE defines a sentence-level score based on pretraining data statistics to determine if the sentence contain minimal word-gender associations.
To systematically benchmark the fairness of popular language models in stereotype-free scenarios, we utilize USE to automatically generate benchmarks without any gender-related language. 
By leveraging USE's sentence-level score, we also repurpose prior gender bias benchmarks (Winobias and Winogender) for non-stereotypical evaluation.
Surprisingly, we find low fairness across all $28$ tested models. 
Concretely, models demonstrate fair behavior in only $9\%$-$41\%$ of  stereotype-free sentences, suggesting that bias does not solely stem from the presence of gender-related words.
These results raise important questions about where underlying model biases come from and highlight the need for more systematic and comprehensive bias evaluation.
We release the full dataset and code at \url{https://ucinlp.io/unstereo-eval}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on examining gender bias in large language models, particularly in non-stereotypical settings. It restricts the evaluation to a neutral subset of sentences with no strong word-gender associations. Authors find that 23 language models under test exhibit 60-95% gender bias indicating the presence of gender associated words might not be the only source of bias.

### Strengths
* The paper addresses an important area in the field of language technology
* The analysis in Section 4 is thorough considering various factors that can be impacting the results.
* The presentation is clear with visualizations and tables used appropriately making it easier for the reader to understand the work

### Weaknesses
 * I am not very convinced with the correctness of generated sentences. As authors themselves mention in the limitations, the generation doesn't involve a human in the loop. Additionally, the generation is limited to a single model (ChatGPT) and having diversity in the models for a model-based benchmark construction would be a better and more fair way to go about it.

* The definition of bias is also not very clear. Since it is a non-stereotypical setting, we see the models favour male gender over female(with models assigning at least 1.65× more probability mass to male versions). What are the real world impacts of it? Does this lead to incorrectness in any manner? 

* What are some possible reasons of models behaving in this manner (spurious correlations)? 

* What are some instances where LMs prefer female. Can we find patterns to such instances. Are these because of implicit biases not fully discovered through word-gender associations? I think woking more towards this direction can lead to interesting findings.

### Questions
* Can the authors please provide examples of sentence variation of changing the fairness threshold?
* Can the authors include results as in Table 1 from Ours-10 and other benchmarks? (Preferrably in the appendix)

Please refer the weaknesses section for other questions.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tries to understand biases in LLMs, especially in non-stereotypical settings. To be more specific, they create a new benchmark where each sentence is free of pronounced token-gender correlation. Evaluating several LLMs, they demonstrate that many LLMs show clear gender preferences, demonstrating biases in the neutral setting.

### Strengths
The idea is straightforward, and the authors make the flow easy to follow. The authors did the analysis with different model families and demonstrated models show clear gender preference.

### Weaknesses
Since LLMs have gender bias is not new, I'm curious about what new aspects this paper is adding. It will be great if the authors provide more details about why we need to care about this neutral setting. And a deeper understanding of under which case models prefer certain gender will also make the paper stronger.

### Questions
- In the results, do you see under which cases/scenarios, a certain gender is preferred by a model?
- For all the models evaluated in this paper, are they all trained on PILE dataset? If not, does the PMI result hold for all of them?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
There is consensus in the literature that language models are
gender-biased in stereotypical contexts. This paper investigates
whether gender bias persists in non-stereotypical contexts as well. By
investigating the preference for one gender versus the other in
neutral contexts, it appears that gender preference/bias manifests in
neutral contexts as well. The same stays true when removing words that
are highly correlated with gender from existing benchmarks (Winobias
and Winogender) and testing on this neutral subset. The paper analyzes
a large number of models and gender-preference seems to be true across
the board.

### Strengths
An interesting analysis of gender preference in neutral contexts
A comprehensive analysis for many models

### Weaknesses
My main concern with the analysis relates to the little correlation
that exists between intrinsic measures of bias and bias in downstream
tasks. As such, I am not sure whether or how this property would
influence the fairness or the potential harms in a downstream
task. See more details in the Questions section.

While I find the analysis interesting, I
am not sure whether analyzing intrinsic measures of bias is useful or
impactful. There have been several papers that show issues with
intrinsic bias measures: they are not robust and there is little to no
correlation with bias measured for a downstream task. I recommend some
of the following papers:

https://aclanthology.org/2022.trustnlp-1.7.pdf shows how simple
rephrasing of sentences with different lexical choices but the same
semantic meaning lead to widely different intrinsic bias scores

https://aclanthology.org/2021.acl-long.150.pdf shows that intrinsic
bias measures do not correlate with bias measured at the NLP task
level

https://aclanthology.org/2022.naacl-main.122/ describes more issues
related to bias metrics

https://aclanthology.org/2021.acl-long.81/ lists several issues with
current datasets/benchmarks for bias auditing

Weaknesses

It is not clear how the findings presented in the paper could be used
in studying the fairness and potential harms of a downstream task

### Questions
In the light that there is no or little correlation between intrinsic
bias measures and bias observed in a downstream task, how do you think
the analysis of gender bias/preference in neutral contexts is useful
for understanding either fairness or potential harms in downstream
tasks? Based on the findings in the paper, what can we conclude for
downstream tasks? Is there some insight that could be useful in a
downstream task?

I think a similar analysis could be performed in a downstream task by
either studying the behavior of counterfactuals or by transforming the
sentences in a task to be gender-neutral.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies gender bias in language models under non-stereotypical settings. The authors construct cloze-style evaluation datasets, both out of Winobias and Winogender and additional ones using OpenAI models, filtered (and constructed) for sentences that have low word-gender associations. These word-gender associations are calculated from the PILE dataset. They find that, in 20+ models, that models have low fairness scores (e.g. log probabilities for male words is higher than female words), and that fairness scores generally do not change significantly even as the gender-word association constraints is relaxed in evaluation datasets. This is true regardless of factors such as model size and deduplication of training data.

### Strengths
The authors carefully construct evaluation datasets to be gender-bias free and introduce checks for quality and cleanliness for OpenAI-generated datasets. Additionally, they conduct a detailed analysis of how fairness dataset construction affects fairness metrics.

### Weaknesses
While the need to test for stereotypical or harmful bias is more directly obvious, this paper would benefit from emphasizing the importance of building non-stereotypical evaluation data. Additionally, while there is discussion on model size and deduplication, it may be worth seeing how pretraining dataset statistics with respect to # female nouns with # male nouns affect fairness metrics (the hypothesis being models trained on more male nouns will have less differences in fairness as gender correlation in evaluation datasets differs).

### Questions
1. Could the authors please clarify the purpose of v(w) in equation 2? PMI already takes into account p_data(w). 
2. Could the authors please elucidate on the generated dataset contents (in terms of topics of sentences generated)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
