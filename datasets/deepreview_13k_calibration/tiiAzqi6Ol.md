# Compositional Preference Models for Aligning LMs

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 3, 6, 6

## Abstract
As language models (LMs) become more capable, it is increasingly important to align them with human preferences. However, the dominant paradigm for training Preference Models (PMs) for that purpose suffers from fundamental limitations, such as lack of transparency and scalability, along with susceptibility to overfitting the preference dataset. We propose Compositional Preference Models (CPMs), a novel PM framework that decomposes one global preference assessment into several interpretable features, obtains scalar scores for these features from a prompted LM, and aggregates these scores using a logistic regression classifier. 
\ptdyIII{Through these simple steps,}
CPMs allow to control which properties of the preference data are used to train the preference model and to build it based on features that are believed to underlie the human preference judgement.
Our experiments show that CPMs not only improve generalization and are more robust to overoptimization than standard PMs, but also that best-of-$n$ samples obtained using CPMs tend to be preferred over samples obtained using conventional PMs.
Overall, our approach demonstrates the benefits of endowing PMs with priors about which features determine human preferences while relying on LM capabilities to extract those features in a scalable and robust way.%

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a compositional preference model for LLM alignment. In contrast to standard monolithic preference models that assign a single scalar value to preference judgments. the model uses a number of features associated with individual scalar values (assigned by an LLM as an automatic evaluator) that are then linearly combined into an overall score.  The authors argue that this provides an inductive bias to the model that makes it more robust to overfitting and reward hacking and results in better generalization and human interpretability. The technique is evaluated with respect to consistency of responses for models trained on different subsets of the training data), comparison against reference PMs from the literature, robustness to overoptimization, and alignment of LLMs trained with the proposed model as opposed to a standard PM.

### Strengths
The core idea of the paper is simple yet powerful and addresses known weaknesses in traditional monolithic preference models; it should be of broad interest to the ICLR audience. The presentation is clear and -- with the exception of human alignment evaluation (see below) -- the evaluations are convincing.

### Weaknesses
For alignment with human preferences, another  LLM (Claude-2) was used rather than genuine human ratings. Although there is more effort associated with a human evaluation study,  and the literature you cite has shown some (imperfect) degree of correlation between human ratings and LLM scores, I really consider human evaluation a must here - otherwise, you are measuring alignment between different LLMs, which can simply result from similar training procedures or similar preference models used.



### Questions
1. It looks like the feature evaluator LLMs (Flat-T5 and GPT3.5) were used out of the box with prompting for assigning feature scores, without fine-tuning or in-context learning. I would have like to see the comparison against fine-tuned versions for each feature. 
2. How does the robustness of the CPM change with an increasingly larger list of features?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces compositional preference models (CPMs), a new method for aligning language models (LMs) with human preferences. CPMs break down preference scores into multiple features to improve robustness and generalization. This decomposition is accomplished by prompting an LM to assign a value to the answer based on a specific preference type. Experimental findings demonstrate that CPMs effectively mitigate overoptimization in preference modeling.

### Strengths
1. Modeling human preferences from different types of judgments is a promising research topic.
2. Experimental results demonstrate that the suggested CPMs indeed improve both robustness and generation.
3. The paper is generally easy to read.

### Weaknesses
1. Although CPMs offer a practical method for breaking down preferences by stimulating LMs, I consider it too simplistic and unrealistic to capture intricate human preferences. For instance, easy-to-understand answers and answers with enough details may contradict each other. I have reservations about whether logistic regressors can accurately represent this intricate pattern.
2. In terms of the experimental setup, CPMs prompt much more than standard PM, which raises concerns about their comparability. I recommend that the author include another standard PM baseline that uses a similar prompt budget as CPMs. For instance, prompting the LM $n$ times (where $n$ represents the number of pre-defined preference types for CPMs) through sampling and selecting the final preference score via majority voting.

### Questions
1. How is the encoder for $x$ parameterized in logistic regression?

### Soundness
2 fair

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
This paper proposes Compositional Perference Models (CPMs), a new perferene model framework that decomposes one global perference assessment into several interpretable features, using a prompted LM to score these features, and finally aggregates these features together with their scores using a logistic regression classifier. Experiments show that CPMs improves generalization and robustness than standard PMs. The main contributions include: (1) new CPMs that allows more transparent supervision; and (2) better results at dimensions of model/overoptimization robustness, generalization, and perference alignment.

### Strengths
(1) new CPMs that allows more transparent supervision; 
(2) better results at dimensions of model/overoptimization robustness, generalization, and perference alignment.

### Weaknesses
1. prefer to see detailed investigations of applying CPMs to different stages of (1) inference only (2) sft, and (3) peft.
2. not quite clear of the scalability of the usage of current 13 features to novel langauges/tasks, further investigations are preferred.

### Questions
1. in Table 5 and Table 6, scores from 1 to 10 are used, and did you try other ranges such as 1 to 5, and how did you decide to use a range of 1 to 10? Also, does different features require different scopes/ranges of scores? In addition, when changing from numbers to words (bad, good, better, best...), how shall the results change?
2. any comparison of between supervised fine-tuning (SFT) and PEFT when using the CPMs? Or, any comparison of the usage of resources under different model alignment frameworks? So, (1) inference only stage controlling, (2) sft, (3) peft, any investigations on these directions of using CPMs?
3. page 3, there are 13 features used, any detailed analysis of overlapping or diversities among these features?or when applying your method to other languages/tasks, how shall we reuse these features or how shall we design new features (any common rules?)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces ‘compositional preference models’ (CPMs) that re meant to overcome issues of transparency and scalability found in regular preference models. CPMs decompose preferences into interpretable features, and subsequently aggregates them (with LR). Generally, results show improvement in generalization and avoidance of over-optimization, which are not themselves ’transparency and scalability’.

### Strengths
- Although a minor strength, the collection of papers in sections 1, 2, and 6 are sufficient, relatively recent, and relevant.
- The compositional extension, though simple, is technically a novel contribution that appears to provide several benefits.
- The setup for best-of-$n$ sampling seems fair. The full set of 25.6K responses, and code, would be appreciated.
- the use of a separate LLM for evaluation is appreciated.

### Weaknesses
 - Although somewhat minor, the use of logistic regression will naturally cause some confusion, especially to those who want an end-to-end trainable model for this task. Other models should have been attempted, particularly those that allow for non-linear interactions between the compositional features. The authors should consider models such as gradient boosted trees or neural networks, which could potentially capture more complex relationships in the data.
- Section 3.1 should be more informative as to the nature of features _c_ and how their set is identified, selected, or defined. This should include both the specific list in Sec 4.1 as well as guidance for other tasks, in general. The current description lacks sufficient detail on how these features are derived from the input text and what criteria were used for their selection. A more rigorous explanation of the feature engineering process is needed, including the rationale behind the chosen features and how they relate to the underlying preference being modeled. This should also include a discussion of potential biases introduced by the feature selection process.
- Although another minor weakness, at least one other LLM  should have been used for extraction (e.g., one of the Llamas). This would help to establish the robustness of the feature extraction process and mitigate any potential biases associated with a single model. The authors should also consider evaluating the impact of different prompt variations on the extracted features.
- Very minor, but please correct the various issues with your references including capitalization and completeness (e.g., Amodei suffers from both — use brackets around {AI} and provide full paper details)

### Questions
- The definition of ‘model robustness’ in Sec 4.2 seems incomplete — surely a factor is the domain or scenario in which the model is to be deployed or evaluated, too?
- Would it be possible to re-arrange the columns of Fig2a and Fig2b so Standard comes left-most (first)?\
- Would there be value in actually performing human evaluations, despite the findings of best-of-n sampling in related work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
