# Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
As the modern tools of choice for text understanding and generation, large language models (LLMs) are expected to accurately output answers by leveraging the input context.
This requires LLMs to possess both context-faithfulness and factual accuracy.
Extensive efforts have been made to enable better outputs from LLMs by mitigating hallucinations through factuality enhancement methods.
However, they also pose risks of hindering context-faithfulness, as factuality enhancement can lead LLMs to become overly confident in their parametric knowledge, causing them to overlook the relevant input context.
In this work, we argue that current factuality enhancement methods can significantly undermine the context-faithfulness of LLMs.
We first revisit the current factuality enhancement methods and evaluate their effectiveness in enhancing factual accuracy.
Next, we evaluate their performance on knowledge editing tasks to assess the potential impact on context-faithfulness.
The experimental results reveal that while these methods may yield inconsistent improvements in factual accuracy, they also cause a more severe decline in context-faithfulness, with the largest decrease reaching a striking 69.7\%.
To explain these declines, we analyze the hidden states and logit distributions for the tokens representing new knowledge and parametric knowledge respectively, highlighting the limitations of current approaches.
Our finding highlights the complex trade-offs inherent in enhancing LLMs.
Therefore, we recommend that more research on LLMs' factuality enhancement make efforts to reduce the sacrifice of context-faithfulness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper discusses the trade-offs between enhancing factual accuracy and maintaining context-faithfulness in large language models (LLMs). The authors argue that current methods aimed at reducing hallucinations and improving factual accuracy in LLMs tend to undermine the models’ ability to remain faithful to the given context. Through a series of evaluations, they find that while factual accuracy might show inconsistent improvement, context-faithfulness suffers significantly, with notable declines observed—up to 69.7%. The analysis of hidden states and logit distributions highlights the limitations of the current approaches, emphasizing the complex balance required between factual knowledge and context adherence. The authors suggest that future research should focus more on minimizing the adverse effects on context-faithfulness when developing methods for enhancing factuality in LLMs.

### Strengths
- The findings presented in the paper are interesting and insightful, bringing the trade-off of faithfulness and factuality to the community’s awareness.
- The analysis conducted in this paper is rich and sufficient.
- The paper is overall well written.

### Weaknesses
 - If I understand it correctly, Algorithm 1 assumes there is one token difference between S_new and S_para. Is there any rationale behind this assumption? Additionally, if this is true, I wonder if the findings in section 5 generalize to settings where S_new and S_para different by more than 1 token?

- I do not find other critical flaws in the paper other than some typos. For example, a closing parenthesis is missing from equation 2. In Figure 3, the legend of the green bar should be “Factuality”. There are some other few types like repeating words across the paper but these do not hinder the understanding of the paper.

### Questions
- In algorithm 1, how did you obtain S_new and S_para? Are they both contained in the MQUAKE-STUBBORN dataset?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to analyze the trade-off between context-faithfulness and factuality enhancement. They first revisist factuality enhancement method and assess their effectiveness. Then, they perform experiments to show that these methods might have a severe decline in context-faithfulness. They finally provide analysis on hidden states and logic distributions to explain the limitation of current methods.

### Strengths
1. The papers provides valuable insight on the dual trade-off between factuality enhancement and context-faithfulness, recommendation future research to reduce the sacrifice of context-faithfulness.

 2. The authors employ a comprehensive experimental setup, testing various methods such as contrastive decoding and representation editing.

3. The presentation of the paper is well-organized and clear, facilitating easy comprehension of experimental findings and details.

### Weaknesses
1. In Algorithm 1, the None checks for P_new and P_para mean that once these variables are assigned a value, the algorithm stops capturing additional tokens. This setup results in identifying only the first differing token between S_new and S_para, while ignoring any subsequent distinctions. Is this interpretation correct? If so, this approach seems limited because of ignoring the subsequent tokens. Please correct me if I make it wrong.

2. While the paper effectively highlights the issue of reduced context-faithfulness with factuality enhancement, it could benefit from a forward-looking research agenda or recommendations for addressing this challenge. Practical suggestions or potential strategies for mitigating these trade-offs would strengthen the contribution and provide guidance for future work

### Questions
See the weakness above

### Soundness
3

### Presentation
3

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
This work proposes to examine the effect of "factuality enhancement" approaches that better exploit LLM parametric knowledge, specifically representation editing and contrastive decoding approaches. Experiments find that they could lead to better factuality and worse context faithfulness, while analysis of model internals provide some indicators.

### Strengths
+ exploring the interplay between parametric knowledge and context faithfulness is promising
+ the experiments are comprehensive

### Weaknesses
 - I'm not sure if I could agree with the framing of "factuality enhancement" methods in this work. In the abstract, the authors claim that "factuality enhancement can lead LLMs to become overly confident in their parametric knowledge" (lines 17-18). However, retrieval-augmented generation is also a way of "factuality enhancement", and that certainly steers models away from parametric knowledge to varying extents. Although the broad term of "factuality enhancement" is employed, the investigated approaches are just a narrow subset.

- Following up on the previous point, the included approaches "representation editing" and "contrastive decoding" are not representing broad walks of "factuality enhancement approaches", but rather approaches that specifically steer the models to better tap into parametric knowledge. As models better rely on internals, they are naturally less faithful to external contexts, hence the conclusion that "models become less context-faithful after you apply these approaches" become trivial. Essentially: if you use approaches that emphasize model internals, they will certainly be less reliant on external context, which is not a surprising/consequential finding.

- Aside from representation editing and contrastive decoding, some earlier prompting-based approaches also claim to better elicit and employ parametric knowledge to enhance factuality, such as [1-2]. I'm not sure if they should be included as baselines, but I wonder if they might change the conclusion as to context faithfulness.

- Section 2.1 is somewhat trivial and don't need to appear in the main paper.

- Again, the authors claim that "Current methods for enhancing factuality do not modify the underlying structure or parameters of LLMs." (lines 188-189) Why would factuality SFT [3] and factuality DPO [4] approaches not count as "current methods for enhancing factuality"? Readers might say that this is twisting the definition of "methods for enhancing factuality" to fit a pre-defined conclusion.

- typo on line 499: "Knowledge Conficts"

- Let's say if indeed "factuality enhancement" and "context-faithfulness" are two conflicting objectives. I wonder if this might be fixed by inference-time approaches that enhance context-faithfulness such as [5]. Essentially, take an LLM, do some "factuality enhancement" which might harm context faithfulness, and then apply things like [5] to patch it and get the best of both worlds.

- The model internal analysis part is great and potentially useful. I wonder if the authors could offer some crisp conclusions/takeaways in addition to presenting some numbers and figures. In the abstract it says "To explain these declines, we analyze the hidden states and logit distributions for the tokens representing new knowledge and parametric knowledge respectively, highlighting the limitations of current approaches." In the conclusion it says "By examining the logits distribution and hidden states, we gained insights into the underlying causes of this decline", which are both very vague. What are "the limitations of current approaches"? What are "the underlying causes of this decline"? Most importantly, I wonder if the authors have some actionable next steps or potential fixes as validated by this internal analysis part.

- Perhaps there is a way to tone down the definition of "factuality enhancement" and make the claims/findings more rigorous or better scoped. This would be essential in making a decision about this submission.

### Questions
please see above

### Soundness
2

### Presentation
3

### Contribution
3
