# Truly Safe & Truly Helpful: Achieving Harmonious Balance for Large Language Model

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
With the advancement of Large Language Models (LLMs), ensuring their safety has become a paramount concern. Alignment techniques, such as Reinforcement Learning from Human Feedback (RLHF), aligning LLM outputs with human values and intentions, greatly enhance the models' safety and utility. Normally, it is a common sense that alignment relies on the quality and quantity of safety data. However, our extensive experimental analysis reveals that integrating a large volume of safety-related data into the alignment process does not fully address all safety concerns, for instance, those arising from unknown safety knowledge, but degrades the models' general ability. To tackle this challenge, we investigate the root causes of LLM harmfulness, focusing on two key dimensions: inadequate safety alignment and insufficient safety knowledge. We delineate the boundaries of what can be achieved through alignment versus other security policies. In response, we introduce a fine-grained data identification strategy and an adaptive message-wise alignment approach, designed to obtain optimized alignment results with minimal safety data, thereby balance the models' safety and general performance. Furthermore, to mitigate the lack of comprehensive safety knowledge, we propose a harmful token filtering mechanism to be applied during the inference phase. Our experimental results indicate that our proposed approaches significantly enhance both the safety and the general performance of LLMs, thus laying the groundwork for more dependable and versatile applications in natural language processing.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes three approches to improve the tradeoff between alignment and helpfullness in LLMs: (1) identify data in different categories, (2) mask the gradients of the less significant segments, and (3) decode with additional filtering process. Experiments show that the proposed approches improves the alignment and the helpfulness compared to baselines.

### Strengths
- The topic of LLM alignment is interesting and important.
- The structure of the paper is clear.

### Weaknesses
 - The writing of the paper is not clear enough, making it hard to follow. For example, the paper fails to mention the references to the supplementary materials.
- The paper is missing lots of details, making it hard to understand the proposed approches and justify the advantages of the methods. For example, the detailed settig of figure 2 is missing. What are dataset a and b? How do we define the safety score? What is the real-world data? etc. In algorithm 1, how are the forbidden words defined? How did the authors collect the 260k data? Section 4.3 is missing lots of details as well.
- The contribution of the paper is limited. The paper seems like 3 different tricks combined together without correlations for mutual improvements. The 3 tricks, including seperating data categories, masking gradients, and adding loss during decoding are all studied in previous work.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies alignment of LLMs, through the lens of different types of harmful data. An optimal data distribution is found empirically, in terms of the number of harmful data points from each type. This is combined with adaptive preference optimization and token-filtering during inference to improve upon current methods of alignment. The authors conduct a thorough evaluation of their proposed methods relative to existing ones and find an improvement in safety while generally maintaining similar levels of helpfulness. The empirical results presented in the paper on the dynamics of LLM alignment during training and the effects of different types of harmful data are insightful.

### Strengths
- Topic of interst: Alignment that incorporates properly both safety and helpfulness is important.
- Interesting experimental results on safety vs helpfulness due to finetuning - for example, saturation of safety score and drop of helpfulness score as more safety training data is introduced.
- Categorization of types of harmful data, their impact on the model, and a proposal for adjusting their distribtution (ratio to general training data) to achieve better performance.
- Strategy of highlighting segments based on a reward during training is an interesting approach. The experiments show a significant increase in safety with the adaptive approach compared to existing approaches, while maintaining similar levels of helpfulness.
- Risk token filtering looks like an interesting approach to safety at inference time - given that adversarial attacks can be very short, and specific words can trigger unsafe behavior, this seems like a good approach to study.

### Weaknesses
 - Safety score on explicit harmful data remains low - while the adaptive approaches are higher than the baselines, they do not significantly improve. Just as a reference, it would be interesting to see the performance of more well-known models of similar size on this metric, e.g. llama-3-8B.
- Partial results on token filtering - It seems the results on token-filtering are only reported in average safety and average "precision", without reference to the full results (not in the main text or appendices). It is hard to understand exactly what the results are based on these reports. Specifically, it's unclear what constitutes a 'true positive' or 'false positive' in the context of token filtering, and how these are aggregated to produce the reported average precision. Furthermore, the lack of detail makes it difficult to assess the trade-offs between safety and potential over-filtering.
- (Minor) - typos - there are quite a few in the paper (e.g. figure 2 - "Number of safety training data" -> "Number of examples(?) in safety training data", line 394 - "More data does not means no safe" -> "More data does not mean not safe"). 
- (Minor) - in line 387, there is a reference to a figure 5 (which does not exist), I assume it is for figure 3.
- Related works - There are additional works on balancing helpfulness and harmlessness that can be mentioned, e.g. [1,2,3].
- Overall I am impressed with the results of the paper, which provide very interesting insights, but feel that the technical issues mentioned above accumulate, so they need to be addressed.

### Questions
- For reference, how would more well-known models of similar sizes perform on the safety metrics?
- Is there a way to improve the safety score on explicit harmful data?

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
This work first proposes to distinguish safety knowledge from safety values. Then, it proposes a pipeline including data preparation, training, and external risk filtering. Using this pipeline, this work claims that a better trade-off between safety and harmfulness can be obtained.

### Strengths
- The notions of safety knowledge and safety value are novel.
- This work proposes a comprehensive pipeline which covers pre-processing, alignment, and post-processing. This could act as a mature solution for the industry.
- Extensive experiments are conducted to verify the three steps.

### Weaknesses
 - As they are mostly defined in natural language, the concepts of safety knowledge and safety value are not very clear. I also checked the examples in the appendix; but did not understand the difference between the first (EHD; Political) and the second (IHD; Political). *To better distinguish these notions, it would be helpful to provide concrete examples in the main manuscript.*
- It is unclear how the proposed method/pipeline serves to make a better trade-off between safety and helpfulness. For example, in Figure 2 and Figure 3, it is unclear how different safety data distributions affect the helpfulness.
- There are several unconvincing claims:
1, line 238, ‘This highlights ... restrict their safety’
2, line 356, ‘RAG ... assesss contextual harm’
3, line 391, ‘This indicates ... the knowledge it possesses’

### Questions
- How is Equation (13) connected to other contents in the manuscript?
- How is RAG used in section 3.3? From Equation (14), it is unclear how RAG works.
- Is there anything wrong with the “More data does not means no safe” in line 394. I do not understand how it is connected to the following analysis.
- How are ‘anti-risk-intent’ and ‘anti-risk-fact’ defined in line 382?

### Soundness
2

### Presentation
2

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
The paper proposed a few different things:
1. Safety training data preparation
2. message-wise alignment training
3. a harmful token filtering mechanism applied during the inference phase.

Starting with the claim that safety concerns in LLMs can be due to (1) inadequate safety alignment or (2) insufficient safety knowledge.
The paper argues that safety alignment training is to teach the model to better interpret the internal reason of a risk, rather than learning new safety knowledge. As simply increasing the quantity of safety data (with high quality and diversity) does not consistently lead to significant improvement in models’ safety.
Split into 
- EHD (explicit harmful data): factual risk data; influenced by internal knowledge 
- IHD (implicit harmful data): intentional risk data, wo explicit risky content; valuable data for safety alignment
- MHD (mixed): explicit risk content and malicious intent; impacted by both knowledge and alignment
Safety scores on different datasets saturated at different levels.

Adaptive message-wise PPO training applies a masking function where only samples in $Y_w$ (chosen set) with higher than baseline reward or in $Y_l$ (rejected set) with lower than baseline reward. This masking can be applied to PPO, DPO, etc.

Harmful token filtering at inference time can be done by:
1. search tokens at inference time based on a safety reward model's score
2. a RAG framework with a dataset of harmful entities and try to avoid generating them at inference time.
 
Experiments were conducted on each of these three things and conclusions feels a bit hand-wavy:
- Facts and intent reinforce mutually in safety alignment.
- More data does not means no safe.
- Truly safety requires truly understanding.
- Adaptive methods brings great general performances.

### Strengths
The idea of splitting safety alignment and safety knowledge is interesting.
It is also an interesting idea to split data according to different safety features and then evaluate or train the model on each or experiment with different mixtures.
However, more work should be done here.

### Weaknesses
Overall, this paper feels like a collection of random ideas. The common theme might be about this claim around safety alignment behavior vs safety knowledge, but the experiment design is not clear enough. And other parts on adaptive training or inference time filtering feels a bit off topic.

Other than the data categorization idea, I don't quite understand how other two parts are connected. I'm also not convinced by the results of applying adaptive masking is necessary; e.g. is it possible the lifting is just due to better quality data points?

The harmful token filtering at inference time part should be cut.

### Questions
This paper needs a major rewrite.

### Soundness
2

### Presentation
1

### Contribution
2
