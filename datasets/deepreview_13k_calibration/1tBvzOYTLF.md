# RevisEval: Improving LLM-as-a-Judge via Response-Adapted References

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
With significant efforts in recent studies, LLM-as-a-Judge has become a cost-effective alternative to human evaluation for assessing the text generation quality in a wide range of tasks.
However, there still remains a reliability gap between LLM-as-a-Judge and human evaluation. One important reason is the lack of guided oracles in the evaluation process. 
Motivated by the role of \textit{reference} pervasively used in classic text evaluation, we introduce \textsc{RevisEval}, a novel text generation evaluation paradigm via the response-adapted references.
\textsc{RevisEval} is driven by the key observation that an ideal reference should maintain the necessary relevance to the response to be evaluated.
Specifically, \textsc{RevisEval} leverages the text revision capabilities of large language models (LLMs) to adaptively revise the response, then treat the revised text as the reference (\textit{response-adapted reference}) for the subsequent evaluation. 
Extensive experiments demonstrate that \textsc{RevisEval} outperforms traditional reference-free and reference-based evaluation paradigms that use LLM-as-a-Judge across NLG tasks and open-ended instruction-following tasks.
More importantly, our response-adapted references can further boost the classical text metrics, \eg, BLEU and BERTScore, compared to traditional references and even rival the LLM-as-a-Judge.
A detailed analysis is also conducted to confirm \textsc{RevisEval}'s effectiveness in bias reduction, the impact of inference cost, and reference relevance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes an interesting method “RevisEval” which explores a new approach to performing reference-based evaluation by modifying references based on the responses to be evaluated. The authors show that this improves the reliability of LLM-based evaluators as compared to using static references, by hypothesizing that an effective reference must be closely relevant to the response to be evaluated. Authors show many interesting observations and analysis across various standard NLG tasks as well as open-ended generative tasks and also evaluate various metrics (both standard and LLM-based). Authors also show that these adapted references can even boost the efficacy of standard metrics.

### Strengths
1. The paper motivates the problem very well by identifying the issues with current reference-based evaluation paradigms. The idea of dynamically generating contextually relevant references is creative and interesting. It aims to address very important and quite relevant aspects of using LLM as evaluators. 
2. Extensive experiments have been conducted across different tasks as well as various metrics have been evaluated. The authors also show the generalizability of their approach to different metrics.
3. The paper also considers and accounts for the various biases present in LLM Evaluators and also considers the cost of conducting evaluations (which is often ignored in a lot of works)
4. Many interesting insights have been reported by the authors, including using these contextually relevant references to improve the standard n-gram and model-based metrics.

### Weaknesses
While I agree with the motivation behind the paper, I am not sure about the soundness of the  methodology followed to generate the reference answers:
1. Using the response itself to generate an "adapted reference", the evaluation might indirectly validate the response’s content and structure. This may lead to artificially inflated evaluations, as the evaluator is essentially comparing the response against a modified version of itself, which serves as the reference. This is particularly concerning because the adapted reference is derived from the response, potentially creating a circular validation where the response is favored simply due to its similarity to the modified reference. The risk is that the evaluation becomes less about the intrinsic quality of the response and more about its alignment with a self-generated reference.
2. If the response contains subtle errors, the adapted reference “might” effectively validate or normalize these errors. These is no study around whether the reviser indeed accounts for or corrects for these errors. This is a critical gap, as the revision process could inadvertently mask genuine flaws in the response. For instance, if a response contains a minor factual inaccuracy or a subtle logical fallacy, the adapted reference might inadvertently correct or overlook these errors, leading to an overly optimistic evaluation. The lack of investigation into this aspect raises concerns about the reliability of the evaluation method, especially in scenarios where detecting subtle errors is crucial.
3. While this approach may work well for evaluations of standard NLG tasks as well as some open-ended tasks that care about the language generation capabilities, but for evaluations that care about the factual accuracy of the responses (something where LLMs are overall known to hallucinate), this simple revision may not be robust. The concern is that the revision process might not be equipped to handle factual inaccuracies effectively. In tasks where factual correctness is paramount, the adapted reference might not be able to identify or correct hallucinations, potentially leading to inaccurate evaluations. This limitation raises questions about the generalizability of the approach to tasks that require high levels of factual precision.

### Questions
1. While the overall paper is well-written, mentioning what the numbers mean in each table and how they have been calculated in the captions or in the text may improve the readability of the paper to a general user. For eg:  mentioning that the values in Table 2 is the accuracy against human preferences... 
2. As mentioned in the weaknesses, please provide details of any experiments that were conducted to study the soundess of this approach for factual responses (where the generated response contains errors which get normalised in the adapted reference).

### Soundness
1

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Recently, LLM-as-a-Judge has been gaining popularity for evaluating language generation tasks, but still has a few reliability challenges compared to human evaluation. This paper proposes RevisEval, a text evaluation method that can be used for LLM-as-a-Judge methods as well as more traditional reference-based evaluation metrics, such as BLEU and BERTScore. The core of the method is to use LLMs to revise the response (system output) based on the human reference, called reponse-adapted references, which is then used as a new reference in the downstream evaluation, be it LLM-as-a-Judge or traditional evaluation metrics. Through experiments, the authors showed that 1) the proposed method RevisEval showed improved correlation with gold standard compared to reference-free and baseline reference-based evaluation methods, and 2) on preference tasks, RevisEval outperforms baselines including fine-tuned LLM-as-a-Judge models, 3) the proposed method reduces the positional bias compared to reference-free methods as well as conventional reference-based method.

### Strengths
* Simple yet effective method — the core idea of the proposed method, RevisEval, is very simple—simply "rewrite" the response based on the human-written reference (and the rubric) and use it as a new reference. The method is also effective for many settings including LLM-as-a-Judge and traditional reference-based metrics. It is easy to imagine that the proposed method is used in evaluation of many NLG tasks going forward.
* Good ablation studies — the paper provides a wide set of ablation studies to show the proposed method's effectiveness. It shows evaluation results on scoring tasks as well as pairwise preference benchmarks. I also liked the bias analysis (Section 4.5) as well as the detailed analysis of concrete examples (Section 5).

Overall, the paper is overall well written and provides enough evidence that the proposed method is simple, effective, and widely applicable.

### Weaknesses
No major weakness as far as I see. Here are some minor weakness points:

* Unclear names—personally I find "response-adapted references" very confusing. It sounds like the method adapt references based on response, but actually it's the other way around. It is actually reference-adapted responses, but I'm not sure if this is a better way of describing it (I don't have any better ideas).

* Unclear description of the experiment settings—the main body of paper benefits a bit of description about the benchmarks. It is based on Tigerscore, but the paper provides very little information re: the specific datasets used and their sizes. Importantly, I think the variety and the quality distribution of responses matter a lot for the evaluation of evaluation methods, and a few sentences about the quantity and the quality of the benchmark datasets would be very helpful.

* Future prospect—this is a bit hypothetical, but the very reason why RevisEval works at all is that current LLMs are in general better at generation rather than discrimination, as the authors state in Section 4.4. Does this mean that in the future, if we have more powerful LLMs at discrimination, would the proposed method still be useful, since future LLMs can simply "guess better" using the reference and the response?

* Applicability — the paper already shows experimental results on a wide range of tasks and benchmarks, but I'm suspecting they are all English tasks (only exception is the source sentences of MT, which are in Chinese). It doesn't have to be done in this paper, but it would be valuable to test the effectiveness of RevisEval in a wider range of tasks (e.g., image captioning) and languages.

### Questions
* How would the proposed method work for multiple references? For open-ended text generation tasks, including MT, multiple references are often used.
* What's the metric used in Table 2? Accuracy?
* Figure 3 — it looks like which metrics are most effective (and closest to GPT-4 performance) vary based on the specific metrics used. Would you provide some general guidelines which metric(s) are most effective in general when combined with RevisEval? Or simply doing majority voting is a good strategy?
* In the last paragraph of Section 4.2 — "significantly" is used two times. Are they used in a statistical sense? If not, they are simply very subjective adverb and I would advise against using it in this context
* Same for the section title of 4.3 — what do you exactly mean by "activating?" I would rephrase with something simpler, e.g, "Improving"
* What are some examples of future work of RevisEval? The conclusion section only provides the summary of the findings.

### Soundness
4

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
The work proposes a simple and straightforward evaluation method that involves modifying and enhancing the output text to be evaluated, using it as the reference for further evaluation, motivated by the potentially unsatisfactory quality of traditional references. They experiment with various setups, including using strong and weak LLMs as revisors and employing both traditional evaluation metrics and LLM-based evaluators.

### Strengths
The proposed method is intuitive and reasonable, with a straightforward implementation that advances previous work using LLMs to generate references for evaluation. They also consider a comprehensive range of experimental setups, baseline methods, and evaluation benchmarks to verify the effectiveness of their method, resulting in solid experimental analyses.

### Weaknesses
Given that previous studies have already utilized LLMs to generate higher-quality references as replacements for traditional references (Tang et al., 2024), the innovation and contribution of this method are somewhat diminished. I believe they could further enhance the analysis by more comprehensively comparing these two approaches for generating references (generation as reference vs. revision as reference). Additionally, I suggest exploring the use of more refined response-adapted references, such as having the revisor focus on specific dimensions during evaluation, to allow for a richer and more diverse discussion.

The experiments in this work are thorough, but they may be somewhat distracting. First, the main experimental results presented in Tables 1 and 2 involve some inconsistent demonstrations; for example, both tables include the "Open-Source LLM-as-a-Judge" part, but the types of methods involved seem different. In Table 1, it’s unclear whether "Ref-Based" refers to references generated by the corresponding LLMs or the original references, which is important. And Sections 4.3 and 4.4 may not be as critical and could be moved to the appendix, given the availability of stronger evaluation methods; this would allow space for more in-depth experiments and analysis.

### Questions
Please refer to Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a simple solution to enhance reference-based evaluation of LLM-as-a-Judges. Instead of using pre-made references, the work introduces a novel evaluation paradigm, "Revise-and-Evaluation," where an LLM revises the provided input to generate a reference answer. The authors note that this method is effective in creating a reference similar to the response in terms of style and different artifacts, effectively accounting for the quality of the answer only. The methodology can be expanded to classical evaluation methodologies like BLEU, ROUGE, and more. The methodology is tested on diverse benchmarks.

### Strengths
1. The paper proposes a simple and straightforward solution to improve reference-based evaluation. The methodology is easy to implement and shows promising improvement in quality on different benchmarks. 

2. The methodology shows strong robustness, naturally controlling for style, and shows nice performance on adversarial benchmarks like LLM Bar, despite relatively small training.

### Weaknesses
 1. While the improvements look promising, there are some questions about the effectiveness of the proposed solution. Recent meta-evaluation works like Reward Bench [1] show that reward models are much more powerful than LLM-as-Judges in proxying human responses. Does the proposed methodology have a benefit against RMs? 

 2. Automated evaluators are also widely used as a proxy for human preference in RLHF. An additional step to generate revisions makes the whole process slower and expensive. Hence, while the performance may be promising, it seems like it limits the usage of automated evaluators. Where do you expect this methodology to be used? 

 3. Mandating a revision step before evaluation assumes that the revising model can refine the answer better. What if the question-response pair is too difficult for the model to revise? Will the methodology still be effective?

### Questions
1. While the improvements look promising, there are some questions about the effectiveness of the proposed solution. Recent meta-evaluation works like Reward Bench [1] show that reward models are much more powerful than LLM-as-Judges in proxying human responses. Does the proposed methodology have a benefit against RMs? 

2. Automated evaluators are also widely used as a proxy for human preference in RLHF. An additional step to generate revisions makes the whole process slower and expensive. Hence, while the performance may be promising, it seems like it limits the usage of automated evaluators. Where do you expect this methodology to be used? 

3. Mandating a revision step before evaluation assumes that the revising model can refine the answer better. What if the question-response pair is too difficult for the model to revise? Will the methodology still be effective?


[1] https://arxiv.org/abs/2403.13787

### Soundness
2

### Presentation
2

### Contribution
2
