# Knowledge-localized Unlearning for Faithful Forgetting in Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Large language models are exposed to privacy risks since they are trained on large text corpus, which may include sensitive or private information. Therefore, existing studies have attempted to unlearn undesirable knowledge exposed without permission from a language model. However, they are limited in that they have overlooked the complex and interconnected nature of knowledge, where related knowledge must be carefully examined. Specifically, they have failed to evaluate whether an unlearning method faithfully erases interconnected knowledge that should be removed, retaining knowledge that appears relevant but exists in a completely different context. To resolve this problem, we first define a new concept called superficial unlearning, which refers to the phenomenon where an unlearning method either fails to erase the interconnected knowledge it should remove or unintentionally erases irrelevant knowledge. Based on the definition, we introduce a new benchmark, FaithUnBench, to analyze and evaluate the faithfulness of unlearning in real-world knowledge QA settings. Furthermore, we propose a novel unlearning method, KLUE, which identifies and updates only knowledge-related neurons to achieve faithful unlearning. KLUE categorizes knowledge neurons using an explainability method and updates only those neurons using selected unforgotten samples.  Experimental results demonstrate that widely-used unlearning methods fail to ensure faithful unlearning, while our method shows significant effectiveness in real-world QA settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the issue of "unfaithful" unlearning knowledge from the LLMs, including failing to erase the knowledge it should remove and unintentionally erasing irrelevant knowledge. A new benchmark, FaithUnBench, is proposed for analyzing and evaluating the faithfulness of unlearning in the knowledge QA settings, consisting of Paraphrased QA, Multi-hop QA, and Same-answer QA datasets. The authors also present an approach to mitigate the issue. In particular, it identifies and updates only the knowledge-related neurons based on selected unforgotten samples.

### Strengths
* Present a dataset for faithful unlearning knowledge from LLMs, targeting at different categories of unfaithful issues
* Experimental results demonstrate the effectiveness of the approach, with further detailed analysis

### Weaknesses
 * The approach relies on the world knowledge graph, which is restricted to the triple-based QA settings

### Questions
* Have you tried larger p value for the experiments in section 5.6? It seems that the tendency is still going up.
* Have you compared different prompting templates for MCQA? Furthermore, apart from the convenience for evaluation, have you compared it with other ways of prompting?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors define superficial unlearning and construct a new benchmark, FaithUnBench, to analyze and achieve faithful unlearning.
Furthermore, the authors propose a novel knowledge-localized unlearning method, KLUE, to mitigate superficial unlearning and
reveal that our method outperforms other unlearning methods, dramatically mitigating superficial
unlearning.

### Strengths
This article contributes a dataset and an effective method to the community.

### Weaknesses
1. There is no comparison of the proposed dataset with previous datasets, such as MUSE, WMDP, KnowUnDo, TOFU.
2. In the Faithful Unlearning setting, some knowledge related to current entities should not be forgotten. Has this consideration been taken into account in the constructed dataset? For example, in Figure 1, changing Tom Cruise's nationality should not affect the answer regarding his notable works. Intuitively, the unlearning process is more likely to damage content related to Tom Cruise rather than affect another person's nationality.

### Questions
The goal of unlearning is to completely forget specific knowledge. Has the author considered the following scenario: testing whether the knowledge has truly been forgotten by asking about it in a different language?

### Soundness
3

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
4

### Summary
To study the impact of machine unlearning on other related knowledge, the authors define a new concept called superficial unlearning. Based on the definition, they propose FaithUnBench to reveal that existing unlearning methods do not ensure faithful unlearning. To achieve faithful unlearning, the authors propose KLUE to update only knowledge-related neurons via the gradient ascent method.

### Strengths
1. It is interesting to evaluate the faithfulness of unlearning using Multi-hop QA and Same-answer QA.

2. It is reasonable to precisely update by localizing certain parameters to reduce the side effects of unlearning.

### Weaknesses
1.There is a lack of detailed comparison with existing datasets. For example, RWKU [1] also adopts 200 popular real world entities as the unlearning target knowledge and also considers the impact on related knowledge.

2.The proposed localization method is overly simplistic. How can neurons that express unrelated knowledge be avoided during localization? Additionally, neuron localization is not the only method for localizing key parameters. How does it compare with other localization methods?

3.There is a lack of more in-depth analysis. For example, in the analysis of the distribution of localized neurons, whether there is a certain distribution pattern for the neurons corresponding to different knowledge.

### Questions
1.There is a lack of quality assessment for the constructed benchmark. How can the noise introduced by GPT-4o be avoided?

2.Why can the problem of superficial forgetting be solved by neuron localization? Some case studies can be done on Multi-hop QA to check if MAf is really reduced rather than MAt being increased due to fewer updated model parameters.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the issue of superficial unlearning in language models, which refers to the phenomenon where an unlearning method either fails to erase the interconnected knowledge it should remove or unintentionally erases irrelevant knowledge. To investigate the phenomenon of superficial unlearning, this paper introduces a new benchmark, FaithUnBench, to evaluate unlearning methods in real-world knowledge QA settings. Then, it proposes an unlearning method, which identifies and updates only knowledge-related neurons to achieve faithful unlearning.

### Strengths
1.This paper explores a promising direction: the timely issue of removing sensitive or private information from language models.

2.This paper defines the problem of superficial unlearning and constructs a benchmark for a more in-depth analysis and evaluation of unlearning methods.

### Weaknesses
1.The choice of evaluation metrics is unreasonable. Why is the UA of all baselines equal to 0.33 (only GA on Gemma2 is 30.30)? Does this suggest that the unlearning dataset is simple enough and more rigorous testing methods need to be designed? For instance, WMDP [1] also uses multiple-choice QA to evaluate the unlearning effect, yet existing unlearning methods struggle to reach the level of random guessing.

2.The implemented baselines are relatively few, and more models (LLaMA3) and unlearning methods (such RMU [1] and NPO [2]) need to be compared.

### Questions
1.What is the form of the data to be removed? Is the Base QA used as the training data? This is easier compared to unlearning the Harry Potter books.

### Soundness
2

### Presentation
3

### Contribution
2
