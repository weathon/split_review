# Effective LLM Knowledge Learning Requires Rethinking Generalization

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Large language models (LLMs) are trained on a substantial amount of documents that contain extensive world knowledge. However, it is still not well-understood how knowledge is acquired via autoregressive pre-training and extracted via question-answering. This lack of understanding greatly hinders effective knowledge learning, especially for continued pre-training on up-to-date information, as this evolving information often does not have diverse repetitions like foundational knowledge. In this paper, we focus on understanding and improving LLM knowledge learning. We found and verified that knowledge learning for LLMs can be deemed as an implicit supervised task hidden in the autoregressive pre-training objective. Our findings suggest that knowledge learning for LLMs would benefit from methods designed to improve generalization ability for supervised tasks. Based on our analysis, we propose to diversify training documents’ formats as data augmentation to grow in-distribution samples. This data augmentation method does not present the risk of altering the facts embedded in documents as text paraphrasing. We also introduce sharpness-aware minimization as an effective optimization algorithm to better improve generalization. Moreover, we adapt our method to instruction tuning for generalization to various phrasings of questions. Extensive experiment results validate our findings and demonstrate our methods’ effectiveness in improving knowledge learning in both the continued pre-training and instruction tuning stages. This paper offers new perspectives and insights to interpret and design effective strategies for LLM knowledge learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores how LLMs acquire and generalize knowledge through training, addressing the previously unclear process of knowledge acquisition in autoregressive pre-training and its extraction in question-answering. The authors reveal that knowledge learning in LLMs functions as an implicit supervised task embedded within the autoregressive pre-training objective. Their key findings are:
1. They propose a way to generate in-distribution training samples by diverse document formatting. This automatic augmentation method mitigates the risk of altering facts in documents.
2.  They verify the hypothesis that that training documents and knowledge-based questions align in distribution, making knowledge learning a supervised problem.

### Strengths
1. The authors proposed to apply Sharpness-Aware Minimization and document formatting-based data augmentation, the authors provide practical methods to improve LLM generalization on knowledge learning.

2. The paper introduces an new perspective by framing knowledge learning in LLMs as an implicit supervised task.

3. The paper is well-structured and clearly written,

### Weaknesses
1. Comparison with Paraphrasing: While the authors propose formatting-based data augmentation to prevent factual alterations, it would be useful to include a direct comparison with paraphrasing, as it remains a widely used method. A quantitative analysis would help clarify if the formatting approach is comparably effective or if paraphrasing has advantages under certain conditions. Even if paraphrasing risks altering facts, seeing how the two methods differ in terms of model performance could demonstrate the benefits and limitations of each. Could an ablation study be conducted to compare their formatting-based augmentation against paraphrasing on a subset of data where paraphrasing is safe? This would provide quantitative evidence of the relative effectiveness of both approaches.

2. The significant of the finding is not clear, especially relative to established concepts like the “reversal curse” and related works is well taken. Both [1] and [2] delve into the issue of the knowledge learning problem and found that training on one single knowledge statement is not enough for the model to capture the knowldege. Differentiating their contribution more clearly would be helpful. Could you explain how the framing of knowledge learning as a supervised task either differs from or builds upon the insights in these prior works? It would be useful to have a dedicated paragraphs or evaluation to directly compare your findings with [1] and [2]

3.  The adaptation to instruction tuning may not provide a strong motivation for using the proposed method, as instruction tuning primarily focuses on learning the format rather than acquiring knowledge. Could you provide empirical evidence showing how your method impacts knowledge acquisition during instruction tuning, beyond just format learning? 

[1] The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"
[2] Physics of Language Models: Part 3.1, Knowledge Storage and Extraction

### Questions
Why does the combination of SAM and data augmentation provide such a significant improvement, whereas using only one of these methods does not?

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
2

### Summary
This paper explores how LLMs acquire and retrieve knowledge through autoregressive pre-training. The authors found that knowledge learning for LLMs is an implicitly supervised problem. This observation is valuable. They propose a data augmentation method to increase in-distribution samples and introduce sharpness-aware minimization as an optimizer. Experiments validate the supervised nature of LLM knowledge learning and demonstrate the effectiveness of the proposed methods.

### Strengths
1.I think this is an worth-investigating topic. It is still not understood how knowledge is acquired via autoregressive pre-training. This lack of understanding greatly hinders effective LLM knowledge learning. The paper provides insights into how LLMs acquire knowledge through auto-regressive pre-training. The authors verify that knowledge learning for LLMs is an implicitly supervised problem, which is a novel finding.

2.They propose a data augmentation method and introduce sharpness-aware minimization as an optimizer to improve knowledge acquisition.

3.The analysis is extended to the instruction tuning phase, highlighting the importance of generalization on different questions with the same answer.

4. Extensive experiments and ablation studies validate the findings and demonstrate the effectiveness of the proposed methods.

### Weaknesses
1.In Figure 1, it appears that the text within the figure is excessively large in relation to the size of its corresponding captions.

2.What would happen if the number of tokens remained constant in the data augmentation experiment? If it performs worse than before, does it mean that a decrease in the overall knowledge contained will lead to poor knowledge acquisition?

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work suggests that knowledge acquisition for large language models (LLMs) can improve through strategies aimed at strengthening generalization in supervised tasks. The approach presented involves text paraphrasing in document format and the use of sharpness-aware minimization (SAM). Experimental results indicate that these methods support effective knowledge learning and can be adapted for instruction tuning. Additionally, training on paraphrased documents appears to facilitate knowledge extraction, an observation consistent with previous research.

### Strengths
- The study shows that knowledge learning performance can significantly improve through simple data augmentation, such as controlling spaces or adding special characters around sentences. This is an intriguing and noteworthy observation.
- The paper is easy to follow due to its clear writing.

### Weaknesses
- **Application of SAM**: Is there a particular reason SAM is expected to perform well in knowledge learning? From my reading, it seems this work merely applies SAM in a knowledge learning context without providing new insight into its specific relevance for knowledge learning.
- **Limitations of Observations**: As the authors mention, the effectiveness of rephrasing data has been previously reported (e.g., [1], [2]). Therefore, the observation in Section 3.3 is not novel, although it is valuable to validate their experimental setup.
- **Lack of Analysis**: There is insufficient analysis of the effectiveness of each data augmentation method. Additionally, comparing their approach to other paraphrasing methods, such as EDA or LLM-based paraphrasing, would clarify the unique advantages of their method.

References

[1] Allen-Zhu et al., Physics of language models: Part 3.1, knowledge storage and extraction

[2] Ovadia et al., Fine-tuning or retrieval? comparing knowledge injection in llms

### Questions
- In Lines 395–397 and 466–468, the authors suggest that performance improvements might not be due solely to extended training steps. To verify this, it would help to include a graph with training steps (not epochs) on the x-axis and accuracy on the y-axis, comparing performance with and without their method.
- Which data augmentation approach is most effective? Section 4.1 introduces various formatting variants, so an ablation study could clarify which variant contributes the most to performance.
- It would be beneficial to compare the proposed method with EDA or LLM-based paraphrasing. While the method presented here is impressively simple and effective, further validation is needed to establish it as the most effective approach. Although LLM-based paraphrasing may have reliability issues (as noted in Line 285), including an evaluation of it here would be informative.

### Soundness
3

### Presentation
2

### Contribution
2
