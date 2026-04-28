# Learning Personalized Story Evaluation

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5

## Abstract
While large language models (LLMs) have shown impressive results for more objective tasks such as QA and retrieval, it remains nontrivial to evaluate their performance on open-ended text generation for reasons including (1) data contamination; (2) multi-dimensional evaluation criteria; and (3) subjectiveness stemming from reviewers’ personal preferences. To address such issues, we propose to model personalization in an uncontaminated open-ended generation assessment. We create two new datasets Per-MPST and Per-DOC for personalized story evaluation, by re-purposing existing datasets with proper anonymization and new personalized labels. We further develop a personalized story evaluation model PERSE to infer reviewer preferences and provide a personalized evaluation. Specifically, given a few exemplary reviews from a particular reviewer, PERSE predicts either a detailed review or fine-grained comparison in several aspects (such as interestingness and surprise) for that reviewer on a new text input. Experimental results show that PERSE outperforms GPT-4 by 15.8% on Kendall correlation of story ratings, and by 13.7% on pairwise preference prediction accuracy. Both datasets and code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes datasets and LLaMA-2 based models (PerSE) for evaluating story generation in a personalized manner. This is motivated by an analysis in GPT4 evaluations which shows a marked bias toward known plot lines. The paper presents two kinds of evaluation setups, one based on predicting the rating a reviewer would assign a generated text in independence from other generations. And a pairwise aspect based evaluation that considers pairs of generations and predicts which of the two would be selected by a reviewer for a specific aspect (interestingless, surprise etc). The proposed datasets leverage existing datasets of movie reviews and pairwise annotated aspects to train PerSE. The paper then presents an analysis of the proposed models.

### Strengths
- The paper fills an important gap in the evaluation of text generation systems - one that is likely to be important in the near future as personalized generation becomes more important.
- The experiments presented are comprehensive and largely convincing.

### Weaknesses
 - The paper could benefit from a discussion of some factors about the practicalities of using an approach like PerSE for evaluation; for example, what happens if there isn't training data for PerSE in a domain? How biased is PerSE toward LLaMa generations? others asked in the questions below.
- The paper could benefit from clarifications regarding some of its analysis and experiments.
- What is the rationale for expecting that movie review data of MPST is not a part of pretraining data for LLaMA? Is this likely to lead PerSE models to be biased similarly to GPT4 (albeit to a lesser extent due to personalization)?
- Consider adding a citation/link for the MPST dataset.
- I found the extended analysis of Sec 3.1 in A.1.2 to be significantly easier to understand than the writing of Sec 3.1. Please consider rewriting this section for clarity and to stand alone in the main body of the paper.
- Relatedly, model based evaluations have been found to contain self-biases (https://arxiv.org/abs/2212.10020) - consider discussing or experimentally demonstrating the extent to which PerSE is likely to prefer generations from a LLaMA based text generation model.
- Sec 5.1: How are the k examples from a reviewer's historical reviews used for training and evaluation selected? Is this a random set of k examples for the reviewer or is something else done?
- Do I understand correctly that the DOC dataset contains generations from an existing system? If so, please discuss the implications of training PerSE on generated stories and its ability to judge generations from other systems. In a future use of PerSE do you envision that researchers will train a personalized evaluation model on the ratings from a small set of annotators?
- Continuing from my previous question - it seems like the paper primarily proposes a method for rating prediction and posits that this may be used for personalized story evaluation. Please discuss how you envision this actually being used for text generation evaluation in much more depth. For example, what happens when there is no training data for training a model like PerSE in a specific domain? Why does it make sense to use a model pretrained on one set of users to evaluate text generated for a (hypothetical) other set of users? - it seems the most sensible for the text generation model to be trying to personalize text to the specific users on who the evaluation model is trained.
- It is not clear to me that the the bias present in GPT4 for known plots immediately motivates a personalized evaluation - please consider rethinking/rewriting this motivation. For example, is there a simple bias correction one could apply to ratings produced from GPT4 so that known plots receive smaller scores?

### Questions
- What is the rationale for expecting that movie review data of MPST is not a part of pretraining data for LLaMA? Is this likely to lead PerSE models to be biased similarly to GPT4 (albeit to a lesser extent due to personalization)?
- Consider adding a citation/link for the MPST dataset.
- I found the extended analysis of Sec 3.1 in A.1.2 to be significantly easier to understand than the writing of Sec 3.1. Please consider rewriting this section for clarity and to stand alone in the main body of the paper.
- Relatedly, model based evaluations have been found to contain self-biases (https://arxiv.org/abs/2212.10020) - consider discussing or experimentally demonstrating the extent to which PerSE is likely to prefer generations from a LLaMA based text generation model.
- Sec 5.1: How are the k examples from a reviewer's historical reviews used for training and evaluation selected? Is this a random set of k examples for the reviewer or is something else done?
- Do I understand correctly that the DOC dataset contains generations from an existing system? If so, please discuss the implications of training PerSE on generated stories and its ability to judge generations from other systems. In a future use of PerSE do you envision that researchers will train a personalized evaluation model on the ratings from a small set of annotators?
- Continuing from my previous question - it seems like the paper primarily proposes a method for rating prediction and posits that this may be used for personalized story evaluation. Please discuss how you envision this actually being used for text generation evaluation in much more depth. For example, what happens when there is no training data for training a model like PerSE in a specific domain? Why does it make sense to use a model pretrained on one set of users to evaluate text generated for a (hypothetical) other set of users? - it seems the most sensible for the text generation model to be trying to personalize text to the specific users on who the evaluation model is trained.
- It is not clear to me that the the bias present in GPT4 for known plots immediately motivates a personalized evaluation - please consider rethinking/rewriting this motivation. For example, is there a simple bias correction one could apply to ratings produced from GPT4 so that known plots receive smaller scores?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors present a study on the interesting problem of personalized evaluation of open-ended story generation. Concrete methods are proposed to create two personalized datasets of story evaluation from existing datasets such as IMDB plots, in order to resolve the problem of data contamination in Large Language Models (LLM) evaluation models. The story evaluation datasets are generated for comprehensive personalized evaluation with proper anonymization and new personalized labels. More importantly, a personalized story evaluation model based on LLM is developed to infer reviewer preferences and provide a personalized evaluation. Experiment results show the LLaMA instruction-tuning based implementation achieves a high correlation with the reviewer’s judgment, outperforming GPT-4 in terms of specific metrics such as Kendall correlation of story ratings and pairwise preference prediction accuracy.

### Strengths
1. This paper is well written with concrete examples. For example, many examples of premises, plots and preference evaluations are given to explain personalized evaluation of story generation. 

2. The problem of personalized story evaluation is under-explored and hence the novelty of this paper is high. The study in this paper may inspire many further research works in this domain. 

3. Comprehensive experiments are conducted to illustrate the effects of major factors in modeling personalized story evaluation. And the metrics to evaluate the models are diverse.

### Weaknesses
1. There are missing technical details such as how exactly an anonymized plot is summarized.  

2. The datasets generated seem to be in a small scale. To show the proposed methods are scalable and widely applicable, it'd be great if much larger scale datasets could be used.

### Questions
1. What is the significance of the comparison results between PERSEcomp-13b and PERSEcomp-7b in Table 4? Providing t-test results can be useful.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The research introduces PERSE, a model for personalized story
evaluation. It leverages reviewers' preferences and generates
personalized reviews for stories. Two new datasets are created to
address contamination in story evaluation. PERSE outperforms GPT-4,
demonstrating its effectiveness. The study also explores
personalization challenges in LLMs and introduces instruction-tuning
to improve model reasoning about reviewers' preferences.

### Strengths
The key strength of this research lies in its
investigation of the contamination issue in GPT-4 and its proactive
response by creating two new datasets, Per-MPST and Per-DOC. These
datasets are designed to mitigate contamination problems in story
evaluation, making this study a valuable contribution to personalized
text generation assessment.

### Weaknesses
The current text leaves room for confusion regarding the roles of
different models and lacks clarity in explaining the basis of metrics
for evaluation. Here are the three identified weaknesses:

Lack of Clarity in Model Attribution in contribution statements: The
paper needs to explicitly specify that "Current LLMs" refer to models
like ChatGPT-4, and it should distinguish that the pronoun "they" in
"with instruction-tuning on several thousands of data, they can"
pertains to the proposed method based on LLaMA-2. Failing to do so may
lead to ambiguity, making it difficult to understand the paper's
contributions.

Ambiguity in Metric Basis: While the paper mentions reporting
prediction accuracy as the primary metric for comparative evaluation,
it doesn't make it clear what this accuracy is based on. The reference
to "prediction accuracy" needs to be explicitly linked to the
mentioned Pearson correlation or other relevant metrics, providing a
clear understanding of what's being measured.

Limited Diversity in Baseline Models: The paper primarily relies on
LLM-based approaches for score prediction, neglecting the inclusion of
various other methods commonly used in the field, such as matrix
factorization and other score (rating) prediction techniques. To
provide a more comprehensive evaluation, it would be beneficial to
incorporate these alternative baseline models for a more thorough
comparison.


By addressing these issues, the paper can enhance its clarity and
comprehensiveness, making the contributions and methodology more
apparent to readers.

### Questions
Ambiguity in Metric Basis: The paper mentions "prediction
accuracy" as the primary metric for comparative evaluation. Could you
please clarify what specific metrics this "prediction accuracy" is
based on? Is it linked to the previously mentioned Pearson
correlation, or are there other relevant metrics involved? Providing
this clarification will enhance the understanding of the evaluation
process.

Limited Diversity in Baseline Models: The paper predominantly focuses
on LLM-based approaches for score prediction. Are there any specific
reasons for not including a wider range of commonly used methods in
the field, such as matrix factorization or other score prediction
techniques, as part of the baseline models for comparison? Including
these alternatives could potentially offer a more comprehensive
evaluation. Could you share your insights on this choice?


PERSE is a method fine-tuned on the LLAMA-2 using proposed
datasets. However, chatGPT-4, while being a formidable model, does not
undergo fine-tuning in the same way. Do you think it would be fairer
to apply fine-tuning to chatGPT-4 via OpenAI's API to ensure a level
playing field?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To perform personalized story evaluation, this paper creates two new datasets based on existing datasets. And the authors also proposes a personalized story evaluation model to infer reviewer preferences and provide a personalized evaluation. Experiments results on the constructed datasets verify the effectiveness of the proposed method.

### Strengths
1.The experiments are relatively adequate.  
2.The citation work is up to date.

### Weaknesses
 1.The description of the paper is too fragmented and less logical.  
2.The dataset construction section is too cursory, it is recommended to refine it and provide a flowchart.  
3.The description of evaluation model is too simple and a framework diagram is necessary.  
4.The authors need further clarity on the practical implications of the research work as well as specific application scenarios.

### Questions
See above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
