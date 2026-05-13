# Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs

- Decision: Accept
- Avg Score: 8.50
- Scores: 8, 10, 10, 6

## Abstract
Large Language Models (LLMs) generate text by sampling the next token from a probability distribution over the vocabulary at each decoding step. However, popular sampling methods like top-\( p \) (nucleus sampling) often struggle to balance quality and diversity, especially at higher temperatures, leading to incoherent or repetitive outputs. To address this challenge, we propose \textbf{min-\( p \) sampling}, a dynamic truncation method that adjusts the sampling threshold based on the model's confidence by scaling according to the top token's probability. We conduct extensive experiments on benchmarks including GPQA, GSM8K, and AlpacaEval Creative Writing, demonstrating that min-\( p \) sampling improves both the quality and diversity of generated text, particularly at high temperatures. Moreover, human evaluations reveal a clear preference for min-\( p \) sampling in terms of both text quality and diversity. Min-\( p \) sampling has been adopted by multiple open-source LLM implementations, highlighting its practical utility and potential impact.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the Min-p Sampling method, which dynamically adjusts the probability threshold based on the model's confidence level. This method aims to enhance creativity without sacrificing coherence. The method is validates through experiments on benchmark and human evaluations, showing better coherence and diversity compared to other sampling methods. The method has been widely adopted in the open-source community.

### Strengths
- New sampling method: This paper proposes the Min-p Sampling method for better control over the diversity of generated outputs compared to fixed threshold methods like top-p.

- Conducted experiments: The authors conducted experiments across tasks, ablation studies, and human evaluation.

- High reproducibility: The author released the implementation, code, and repo with implementation guidelines, which enhances the reproducibility.

- Wide Applicability: The proposed method can be easily integrated with existing open-source LLMs, and the authors show the broad potential applications that can be applied.

- The ablation study shows that min-p sampling is barely impacted by the output length, which is interesting.

### Weaknesses
 - The experiment is limited to Mistral models and fails to demonstrate applicability with other models. It would be more comprehensive and interesting to see results from additional models, such as LLaMA3.

- The effectiveness of min-p sampling highly depends on the base probability thresholds. As shown in Table 6 (ablation study results), the choice of thresholds significantly impacts LLM performance. This indicates that optimal performance requires careful tuning, which could limit the method’s potential effectiveness and ease of use in applications.

- The paper claims that the experiment is intended to demonstrate that min-p sampling balances creativity and coherence (line 290); however, metrics relevant to creativity are missing. Diversity is not enough for creativity assessment. LLMs-as-judge approach is widely used for creativity assessment. Please consider adding such an experiment.



### Questions
- The paper exceeds the 10-page limit. Please be careful with submission guidelines, as the paper could otherwise face desk rejection.

- Does min-p sampling make it more difficult to control LLMs, such as for lexically constrained generation?

- Details on the human evaluation are missing. What is the inter-annotator agreement rate? How many participants were recruited? The paper mentions receiving 70 initial responses; does each response contain one participant's evaluation for all data points? The paper claims that participants were recruited from Prolific. I would like to see the survey template, as it is important for reviewers to evaluate the effectiveness of the human evaluation.

- The paper states that min-p sampling has "Extensive human evaluations further confirmed a strong preference for min-p sampling over top-p, highlighting its practical advantages in real-world applications" (line 510). Could you provide some examples of real-world applications? In what scenarios would min-p sampling be preferable to other sampling methods? The paper has not included a relevant discussion on this.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
[UPDATE] Based on the rebuttal I have increased my score (8->10), but kept the rest of the review unchanged

The authors propose a new sampling mechanism, which is a minor but important twist to the popular nucleus-sampling (`p`). Instead of having a fixed threshold `p`, this proposal has `p` be dependant of the probability of the most probable token. The intuition is that in cases that the model is confident only few tokens are kept as support set, while that set is extended when the confidence is low

### Strengths
* Sampling is one of those areas were the model per se needs to be complemented with an outside algorithm, allowing for creativity on how to set this up. This work proposes an original twist to a popular choice

* The proposal is simple, appealing and 

* has good empirical results, both as measured on benchmarks and (more important) by adoption of the community

### Weaknesses
The new 10p limit has not been handled wisely in my opinion, and the paper could do more with less text. In particular, Sect 4 could be removed without much loss to the overall apper

Having experiments on a 123B has to be commended. The paper would be stronger however if the authors could show that the results hold on different model families (eg, llama and mistral), as otherwise it is not clear if this method provides gains on one family only

### Questions
* You claim a widespread open-source usage. Could you review the usage of those and classify them by model family?

* Fig 1: different from what the caption reads, (b) seems to refer to top-k and (c) to top-p

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
Simple but effective and highly influential contribution to LLM research

### Strengths
This paper presents compelling evidence that its single contribution, min-p sampling, is highly effective.  The usage of it in 54,000 Github repositories alone is very impressive.  In addition to that, they produced theoretical reasoning why their method works, LLM-generated statistics with explanations about how to interpret these statistics, additional statistics which involved human participants, examples of seeing how the logits are transformed under different distributions which give additional insight into why this method is better than existing methods, and code to try out the method.  It is a very simple paper, but it clearly makes the case for its own importance.

### Weaknesses
The one contribution of this paper, min-p sampling, is extremely simple and not mathematically "deep" at all - no theorems were presented, and the code implementation literally (was provided and) took less than one page.  However, I think that having such a paper in a conference proceeding is not a bad thing.

### Questions
It seems clear that the advantage of this approach is that it lets you "turn up the heat" - use temperature values that otherwise would provide gibberish.  Can you be more specific about what this particular change (going to higher temperature) - as opposed to min-p as a technique - is inherently something you'd want to do (are there benefits beyond diversity, and can you cite evidence for these benefits)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel dynamic truncation method called min-p sampling, which adeptly adjusts the sampling threshold based on the model’s confidence by scaling according to the top token’s probability. This approach presents a significant advancement over traditional sampling methods like top-p and top-k, demonstrating improved balance between the quality and diversity of generated text.
The authors conducted experiments across three datasets, yielding compelling results that underscore the effectiveness of min-p sampling. The findings indicate that this method not only enhances the quality of text generation but also fosters greater diversity, which is a critical aspect in natural language processing tasks.
The writing in this paper is clear and accessible, making the concepts relatively easy to understand. The methodology is straightforward and provides a meaningful contribution to the field. Overall, this paper presents insights and a potential solution to the challenges of text generation, which may be of interest to researchers and practitioners.

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed min-p sampling makes an effective balance between coherence and diversity in text generation.

### Weaknesses
Please refer to Questions.

### Questions
Q1: In Table 2, the experimental results on the GPQA Main and GSM8K datasets demonstrate that Min-p sampling achieves better accuracy compared to other sampling methods when the temperature is set to 1 or higher. Additionally, it appears that all sampling methods perform better at lower temperature values. 

We are particularly interested in the ceiling performance of these methods on these two datasets. However, when the temperature is set to 0.7, min-p sampling does not show a significant advantage over top-p sampling. If the temperature is further decreased (e.g., to 0.5 or 0.3), will the performance of top-p sampling continue to improve? Furthermore, does min-p sampling still maintain a significant advantage over top-p sampling at these lower temperature settings?

Q2: Figure 1 shows that top-p sampling can ensure diversity in generation but may result in incoherent content. On the other hand, top-k sampling can ensure generation of high probability text but may lose diversity. Can a combination of top-p and top-k sampling compensate for their respective shortcomings and better balance coherence and diversity? Would min-p sampling be more effective than the combined method of top-p and top-k sampling?

### Soundness
3

### Presentation
3

### Contribution
3
