# Towards Best Practices of Activation Patching in Language Models: Metrics and Methods

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Mechanistic interpretability seeks to understand the  internal mechanisms of machine learning models, where  localization---identifying the important model components---is a key step. Activation patching, also known as causal tracing or interchange intervention, is a standard technique  for this task \citep{vig2020investigating}, but the literature contains many variants    with little consensus on the choice of hyperparameters or methodology. In this work, we systematically examine the impact of   methodological details in activation patching, including evaluation metrics and corruption methods. In several settings of localization and circuit discovery in language models, we find that   varying these hyperparameters could lead to disparate interpretability results. 
 Backed by  empirical observations, we     give conceptual arguments for why certain metrics or methods may be preferred. 
 Finally,  we provide recommendations for the best practices of activation patching going forwards.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper delves into the realm of mechanistic interpretability, a burgeoning and promising domain within large language models. It primarily centers on activation patching, aiming to identify activations that hold a causal influence over the output. A notable aspect of this work is its pioneering stance in systematically studying the generation of corrupted prompts and the evaluation metrics for patching effects, which previously lacked standardization. Specifically, the paper scrutinizes two methodologies for generating corrupted prompts: 1) Gaussian Noising (GN) and 2) Symmetric Token Replacement (STR). Furthermore, it explores two evaluation metrics: 1) probability and 2) logit difference, alongside investigating the impact of sliding window patching.

### Strengths
The endeavor to understand the internal mechanisms of large language models through activation patching is pivotal. This paper stands out by empirically examining various methodologies, bridging the gap where variations across different papers have made it challenging to ascertain the more effective approach. By embarking on this comprehensive investigation, the paper makes a substantial contribution towards standardizing methods, which is invaluable to the mechanistic interpretability community.

### Weaknesses
I am not very familiar with the details of the existing activation patching methods. Therefore, I am not sure whether the methods included in the paper are diverse and representative enough for the mechanistic interpretability community. It's unclear if the chosen corrupted prompt generation techniques, Gaussian Noising (GN) and Symmetric Token Replacement (STR), are sufficiently comprehensive to cover the range of corruptions that might be relevant for activation patching analysis. Specifically, the paper does not explore other potential corruption methods such as adversarial perturbations or targeted token substitutions that might reveal different causal relationships. Moreover, while the paper examines probability and logit difference as evaluation metrics, it does not delve into the limitations of these metrics, such as their sensitivity to the specific prompt or the potential for masking effects due to averaging over multiple positions. The investigation into sliding window patching is also somewhat limited in scope, without exploring different window sizes or strategies for aggregating the patching effects.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors explore how the method of corruption and type of evaluation can cause conflicting take-aways from activation patching. Specifically, they look at two ways to add corruption to a token embedding: gaussian noise (adding noise to the embedding) or symmetric token replacement (replacing a token with a semantically related token). They find that gaussian noise can cause the input to be OOD, thus breaking the internal mechanism. When looking at logit difference vs. probability, they find that probability can overlook negative model components. Finally they look at sliding window patching, and find that it can inflate logit plots.

### Strengths
I like the motivation of this paper: I think its important to understand how hyperparameters can change the results of interpretability methods.

The authors go over several different types of hyperparameter (corruption method, evaluation method, sliding window) and convincingly show that these design choices can result in different interpretations. I liked the Name Mover analysis, which made it easier to understand how gaussian noise could be causing issues for activation patching. 

Finally, I appreciated Section 6, which gives recommendations on how activation patching should be performed.

### Weaknesses
My biggest concern is relevance to the community: other than Meng et. al, are there other papers using gaussian noise? It's not clear to me that this is a wide-spread issue. 

Moreover, the recommended course of action (STR) can be more difficult to actually implement (as it requires having semantically similar substitutions). To be of most relevance to the community, it would be great if the authors suggested an approach that had the flexibility of gaussian noise without introducing as much bias.

Clarity: Table 1 and in particular the part about negative detection was a bit hard to parse. I would make the discussion around those results more clear.

### Questions
How much does different substitutions for STR or different samples of noise (for gaussian noise) change the interpretation? Are the methods at least consistent within themselves?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors study the effects of different activation patching techniques on the mechanistic model interpretability and make several recommendations. They study and compare the selection of the hyperparameters, evaluation metrics and input corruption techniques for activation patching based model interpretability. The paper studies two approaches, Gaussian Noise (GN) and Semantic Token Replacement (STR), for corrupting the inputs. Based on those studies the paper recommends using STR input corruption technique since it produces in-distribution samples as opposed to the GN approach which produces OOD samples. In terms of the evaluation metrics, it recommends logit difference since it is more granular and allows to detect model activations (components) that have negative impact on model performance.

### Strengths
1) The abstract and introduction are well and clearly written. The problem statement and contributions are easy to follow from those 2 sections.
2) The paper performs thorough experimentation on sliding window techniques, localizing factual recall and circuit discovery.

### Weaknesses
1) The work overall is very interesting but it feels a bit light on the novelty. Perhaps proposing additional novel methods for input corruption and improvements for the activation patching techniques can help to increase the novelty in this paper.
2) The way the paper is written it might be a good fit for a workshop.
3) Some terminology could be explained in the paper. E.g. Name Mover
It seems that the paper requires prior knowledge of another paper Wang et.al. Some concepts such as: 0.10 negative detection is not very clear.
4) It might be good to describe clearly what 0.10 negative detection is under the `Negative detection of 0.10 under GN` section.  


Minor comments:
1) “use its own the method of generating” -> “use its own method of generating” ?

### Questions
1) What are some of the novel contributions of the paper ? 
2) How was the content of Table 1 computed ?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
