# UnSTAR: Unlearning with Self-Taught Anti-Sample Reasoning for LLMs

- Decision: Reject
- Scores: 8, 5, 5, 5, 5, 5

## Abstract
The key components of machine learning are data samples for training, model for learning patterns, and loss function for optimizing accuracy. Analogously, unlearning can potentially be achieved through anti-data-samples (or anti-samples), unlearning method, and reversed loss function. While prior research has explored unlearning methods and reversed loss functions, the potential of anti-samples remains largely untapped. In this paper, we introduce \name: \underline{Un}learning with \underline{S}elf-\underline{T}aught \underline{A}nti-Sample \underline{R}easoning for large language models (LLMs). Our contributions are threefold: first, we propose a novel concept of anti-sample-induced unlearning; second, we generate anti-samples by leveraging misleading rationales, which help reverse learned associations and accelerate the unlearning process; and third, we enable fine-grained targeted unlearning, allowing for the selective removal of specific associations without impacting related knowledge—something not achievable by previous works. Results demonstrate that anti-samples offer an efficient, targeted unlearning strategy for LLMs, opening new avenues for privacy-preserving machine learning and model modification.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper focuses on the idea to use anti-samples coupled with reasoning tuning to enable target machine unlearning. Given a question, the methods utilizes language models to generate incorrect answers and paraphrased questions. The model is then fine-tuned on this as well as induced explanations for incorrect answers. This ensures unlearning quality while only modify the model at "reasoning" step. So the model retain good performance on each individual concepts.

### Strengths
The unlearning method is able to achieve targeted unlearning (e.g. dissociation between two concepts) without harming the representation/knowledge of both concepts. 

The encourage of reasoning seems to be an effective way to combat adversarial attacks.

### Weaknesses
It seems that the method is significantly more involved than other unlearning methods. There is a lack of comparison of time cost for it.

It also lacks comparison to other representation-based unlearning algorithms such as RMU.

Although the unlearning method is able to achieve targeted unlearning (e.g. dissociation between two concepts) without harming the representation/knowledge of both concepts, the practical use case for such fine-grained unlearning is not immediately clear. While the method's ability to encourage reasoning is a strength, the lack of real-world application for this level of targeted unlearning is a concern. The use of anti-samples, while effective, is not novel in itself, as similar techniques have been explored in other works, such as those involving token substitution. The core novelty seems to lie in the fine-grained reasoning unlearning, but this is not clearly motivated by a practical need.

### Questions
Any reason to use harmonic mean to combine evaluation metrics?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper offers a new perspective on existing LLM unlearning algorithms by focusing on the data perspective. It proposes a data-driven algorithm that can help LLMs unlearn and provides comprehensive and diverse evaluation metrics to ensure completeness and diversity during assessment.

### Strengths
1. This paper considers the problem of transferring learning to unlearning from a macro perspective on LLM learning. It divides the learning methods into three steps and successfully summarizes other methods within these steps, thus uncovering a new approach to tackle unlearning.
2. This paper evaluates a comprehensive range of LLM algorithms in its main experiments and designs various evaluation metrics (particularly metrics related to Response Quality and Hallucination Avoidance), offering more perspectives for understanding LLM unlearning.
3. This paper provides several reasonable constraints when designing prompts to ensure the feasibility of using LLMs for regeneration.

### Weaknesses
It appears that the completion level of this paper is not very high. It only includes a comparison of algorithms under different metrics and an analysis of iterations. Although it presents a good method, it still requires some analysis regarding the algorithm’s time complexity. For more detailed weaknesses or questions, please refer to the “Questions” section.

Regarding the algorithm: I noticed that, both in Algorithm 1 and in the steps provided on page 4, the number of iterations mainly depends on the total number  $N$  of generated Paraphrased Questions and Incorrect Answers. The while loop continues until  $Q^*$  is empty. Is it possible that within the same  $Q^*$ , there are several instances where  $\hat{a} = a$ ? If so, does this mean that for the same question, you would fine-tune using all the found tuples $(q^*, \bar{a}, r)$ multiple times? If that is the case, what is the expected average number of repetitions? And what is the relationship between this expectation and  $N$?

Regarding the experiments, I am curious about the impact of  N  on the experimental results. Given that this algorithm involves extensive data regeneration and fine-tuning, could the authors compare the time required for different algorithms and examine whether there is a trade-off between time and performance, or if this algorithm is a “free lunch”?

Regarding the randomness, for the task of data regeneration, the main challenge lies in uncontrollability. How did the authors address the randomness introduced by the LLM algorithms?

Regarding the writing format issues: Line 106 mentions “random labels” (?), and Lines 356-357 reference a paper that cannot be found.
5. No code sources.

### Questions
1. Regarding the algorithm: I noticed that, both in Algorithm 1 and in the steps provided on page 4, the number of iterations mainly depends on the total number  $N$  of generated Paraphrased Questions and Incorrect Answers. The while loop continues until  $Q^*$  is empty. Is it possible that within the same  $Q^*$ , there are several instances where  $\hat{a} = a$ ? If so, does this mean that for the same question, you would fine-tune using all the found tuples $(q^*, \bar{a}, r)$ multiple times? If that is the case, what is the expected average number of repetitions? And what is the relationship between this expectation and  $N$?

2. Regarding the experiments, I am curious about the impact of  N  on the experimental results. Given that this algorithm involves extensive data regeneration and fine-tuning, could the authors compare the time required for different algorithms and examine whether there is a trade-off between time and performance, or if this algorithm is a “free lunch”?

3. Regarding the randomness, for the task of data regeneration, the main challenge lies in uncontrollability. How did the authors address the randomness introduced by the LLM algorithms?

4. Regarding the writing format issues: Line 106 mentions “random labels” (?), and Lines 356-357 reference a paper that cannot be found.
5. No code sources.

### Soundness
3

### Presentation
3

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
the paper observes that recent progress with anti-sample reasoning could be efficiently used for unlearning purposes. It creates anti-samples by (1) paraphrasing and (2) falsifying arguments for unlearning.

### Strengths
- I really liked how accurate and targeted the unlearning could be in terms of concepts, i.e. you can be very selective. 
- Paper figures and visualizations are easy to follow
- Writing is clear and expressive enough
- Really good and intuitive example with Harry Potter, I think it transfer the idea very clearly

### Weaknesses
 - I am not sure if the novelty of the method is sufficient. Authors have described the existing problem of unlearning and existing method of using STAR and combined these methods together. It does not seem like there are any challenges to this method, however I am happy to be convinced otherwise. 
- Evaluation is not as strong as it only uses one dataset for unlearning and Figure 2 does not split performance by subgroups. Figure 3 is also not clear if it contributes anything to the discussion
- There was no discussion on what constitutes  challenges to unlearning using this method, especially given that the task performance is 100% it would be interesting to study where this method fails --> are all unlearning tasks could be solved with UNSTAR?
- Most importantly the paper does not discuss any membership attacks which are much stronger to test unlearning performance.

### Questions
Overall, while I really like the trick to unlearn using anti-samples, I struggle to believe that evaluation is sufficient to prove this claim under more realistic assumptions (MIA, harder cases). Additional evaluation might significantly strengthen the paper.

Also would be good to justify that the method in STAR is challenging to apply in the domain of unlearning and emphasize authors contributions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a UNSTAR -- a method to unlearning in Large Language Models (LLMs), which leverages "anti-samples" – data designed to induce unlearning by neutralizing or reversing learned associations. The paper evaluates UNSTAR and show that it succeeds in fine-grained targeted unlearning.

### Strengths
+ Unlearning is an important topic

### Weaknesses
 + Adhoc non-comparable evaluation methods
+ Missing references to prior work
+ I am confused with the base definition and the goal



### Questions
+ I am slightly confused regarding the context and the setting in which this work is situated. Classical unlearning, as well as, a lot of works in the related section considers a very different setting -- unlearning for privacy. For example work by Bourtoule et al. (2021) is not comparable to anything in the llm unlearning space, I am also not sure what guarantees are being pursued (e.g. see discussion in [1]). Without defining a precise evaluation metric and what exactly is the reason for that metric I am not sure how one is to assess performance. This performance also matters a lot e.g. [2] show that posing the question is a slightly different way poses a significantly different result. Note that it should also make meaningful sense relative to the overall goal of unlearning. 
+ Random relabeling has been explored in prior literature e.g. [3], which should definitely be discussed. If the papers argument is that the random relabeling is not the random, but is semantic then clear separation from [4] is required. I do not understand how or what is semantically different between wroks. 
+ Ironically, there is a broken citation in the related work section next to the random relabeling. It would be great to see comparison in performance to it, alongside an investigation how it is different if at all. 
+ Related work subsection for unlearning is almost a direct copy of a section from [5]. In both phrasing, citations, and the order in which things appear. I am not claiming this is plagiarism, but it is very close in my eyes.  
+ Table 2 shows how semantically close the responses are. Does that make the task easier? How to verify that it did in fact unlearn the related knowledge.
+ If you change the decoding strategy, what happens with the results? Or if you noise the policy very slightly? I dont understand how to think about hallucination/adversarial eval that is ran in a greedy decoding strategy. 
+ Given that the results are very similar to that of WHP+ and RWHP, yet the impact on the model is different I am left wondering if we are just comparing apples to oranges. 
+ Eval claims to use (Anil et al., 2024; Schwinn et al., 2024) for adversarial evaluations. Both these works are not references in the manuscript, but are clearly copied verbatim from [5]. Yet, the paper does not go into any details, as is discussed in appendix of [5].
+ Adversarial eval details are missing and are not replicable in any way. 

[1] "Ununlearning: Unlearning is not sufficient for content regulation in advanced generative ai" by Shumailov et al
[2] "Inexact Unlearning Needs More Careful Evaluations to Avoid a False Sense of Privacy" by Hayes et al
[3] "Random Relabeling for Efficient Machine Unlearning" by Li and Ghosh
[4] "Who’s Harry Potter? Approximate Unlearning in LLMs" by Eldan and Russinovich
[5] "Revisiting Who’s Harry Potter: Towards Targeted Unlearning from a Causal Intervention Perspective" by Liu et al

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents UNSTAR, a method for unlearning in large language models (LLMs) through the use of anti-samples. While previous research has focused on unlearning methods and reversed loss functions, this work explores the potential of anti-samples, which are generated using misleading rationales to reverse learned associations and accelerate the unlearning process. UNSTAR enables fine-grained, targeted unlearning, allowing specific associations to be removed without affecting related knowledge. The results demonstrate that anti-samples offer an efficient and precise approach to unlearning.

### Strengths
1. This work chooses an interesting data-centric angle to solve LLM unlearning. Reshaping the data for more effective unlearning is promising and well-motivating.

2. This work can achieve fine-grained LLM unlearning by destroying unwanted associations within the forget data, which is an underexplored problem in LLM unlearning.

3. The paper writing is well-organized and easy to follow.

### Weaknesses
1. Achieving LLM unlearning from a data perspective is interesting, but the proposed anti-sample has marginal novelty. In my view, it is nearly the same as refusal response or random labels in terms of unlearning. The difference is only to use evidently incorrect words. The anti-sample generation process is quite naïve and lacks technical novelty with the prompt “Generate 20 words similar to this word”. It is more appealing if the generation process is iterative like prompt engineering.

2. In terms of specific methodology, quite a few details are unclear. For example, how UnStar adjusts the prompt to generate Semantically Divergent Questions and Near-Correct Incorrect Answers when the existing generation is semantically too close to the original. In addition, in line 7 of Algorithm 1, what does that mean ‘do similar steps for retain set Qr’?

3. The Reinforcement Learning Style Policy Gradient Approximation is weird, what do the authors want to express? In the claim of lines 270-273, any preference optimization-based unlearning can achieve this separate gradient computation. I don’t think UnStar offers any unique approximation to RL policy learning.

4. testing UnStar on only one dataset is not enough for the experiments. Besides, most implementation details of UnStar and baseline approaches are lacking (cannot be found even in the appendix). There are no statistical error bars or similar metrics. More important, there is no ablation study.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel approach to unlearning QA pairs in large language models by constructing and using anti-examples. The author evaluated the effectiveness of this framework on the WPU dataset across different types of QA knowledge.

### Strengths
1. The paper introduces a new unlearning method.

2. The paper is easy to follow, with each concept and idea illustrated by examples.

### Weaknesses
1. I am concerned that intuitively constructing anti-samples may exacerbate hallucination issues, which we aim to avoid in practice. Could the author comment on this concern? (I recognize that the experiments show a score related to hallucination avoidance, but in principle, why would this approach not lead to significant hallucination problems?)

2. The experimental section is not that convincing. First, the paper does not specify important experimental details, such as dataset size, training settings, or the hyperparameters of each unlearning baseline. Prior literature [1,2] has shown that unlearning methods can behave quite differently depending on parameters and tasks. Second, I question the relevance of some metrics used, such as the GPT Privacy Score, GPT Quality Score, and GPT Rejection Rate. Are these metrics widely accepted in the privacy field? It would be helpful if the author could provide more justification. Lastly, the paper focuses on only one dataset and setting (without any ablation studies), which may limit its impact.

### Questions
See Weaknesses.

Suggestions:

1. In Line 107, there is a typo in the reference to the random label method.

2. In Eq. (1), $p_\mathcal{M}$ refers to the conditional probability of only “answers - $a$,” correct? How is $r$ sampled from the distribution, or does this notation refer to probability $p$? The notation could be made more rigorous.

### Soundness
2

### Presentation
3

### Contribution
2
