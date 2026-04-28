# What Kind of Pretraining Data Do Large Language Models Rely on When Doing Reasoning?

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 8, 5

## Abstract
The capabilities and limitations of Large Language Models (LLMs) have been sketched out in great detail in recent years, providing an intriguing yet conflicting picture. On the one hand, LLMs demonstrate a general ability to solve problems. On the other hand, they show surprising reasoning gaps when compared to humans, casting doubt on the robustness of their generalisation strategies. The sheer volume of data used in the design of LLMs has precluded us from applying the method traditionally used to measure generalisation: train-test set separation. To overcome this, we study what kind of generalisation strategies LLMs employ when performing reasoning tasks by investigating the pretraining data they rely on. For two models of different sizes (7B and 35B) and 2.5B of their pretraining tokens, we identify what documents influence the model outputs for three simple mathematical reasoning tasks and contrast this to the data that are influential for answering factual questions. We find that, while the models rely on mostly distinct sets of data for each factual question, a document often has a similar influence across different reasoning questions within the same task, indicating the presence of procedural knowledge. We further find that the answers to factual questions often show up in the most influential data. However, for reasoning questions the answers usually do not show up as highly influential, nor do the answers to the intermediate reasoning steps. When we characterise the top ranked documents for the reasoning questions qualitatively, we confirm that the influential documents often contain procedural knowledge, like demonstrating how to obtain a solution using formulae or code. Our findings indicate that the approach to reasoning the models use is unlike retrieval, and more like a generalisable strategy that synthesises procedural knowledge from documents doing a similar form of reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the role of pretraining data in shaping large language models' (LLMs) abilities in reasoning tasks compared to factual question-answering. By analyzing two models of different sizes (7B and 35B parameters) across reasoning and factual queries, the authors aim to understand how LLMs generalize when tackling reasoning tasks and whether they rely on specific retrieval of information or broader procedural knowledge. The study applies influence functions to rank the most impactful pretraining documents for different queries, examining if reasoning draws from procedural patterns rather than specific facts.

Empirically, the study finds that reasoning tasks rely on a more distributed set of documents, often containing procedural content like code snippets or mathematical explanations, while factual questions frequently rely on specific documents containing direct answers. Code-based documents, in particular, emerge as influential for reasoning, likely due to their structured, step-by-step nature. Additionally, reasoning tasks across similar queries show correlated influence scores, suggesting a reliance on shared procedural knowledge. The larger 35B model also shows less variation in influence across documents, hinting at improved data efficiency. Together, these findings imply that LLMs approach reasoning by aggregating procedural knowledge rather than retrieving isolated factual data, shedding light on different generalization strategies in LLMs.

### Strengths
1. The paper tries to tackle an intellectually significant question: how do LLMs generalize reasoning abilities from pretraining data to solve completion questions? This exploration into the mechanics of LLM reasoning generalization is both timely and meaningful, given the increasing focus on interpretability and robustness in AI. 
2. The findings provide intuitive insights, showing that LLMs draw on a broad range of abstractly related documents when solving reasoning questions, as opposed to the more targeted document reliance seen in factual questions. This highlights the importance of procedural knowledge and coding data for reasoning tasks, an observation that aligns with broader intuitions about reasoning and learning in LLMs.
3. A key technical strength lies in the revision and adaptation of EK-FAC influence functions. The authors refine this method to assess the influence on model accuracy, which is essential for examining how specific documents impact LLM performance in reasoning versus factual tasks.

### Weaknesses
1. The overall style resembles a blog post, presenting intriguing observations over a cohesive scientific narrative. For example, the conclusion/discussion section takes more than 1 page to explain everything again. The paper could either prioritize the revised EK-FAC function or convert the observations into some actionable strategies to improve LLMs. Additionally, reorganizing the paper to integrate findings more succinctly could create a more cohesive narrative.
2. Although the paper acknowledges computational constraints, the scale of data and task complexity could be expanded to strengthen the conclusions. The study’s focus on basic arithmetic and simple mathematical queries limits its generalizability to broader reasoning tasks that are common in real-world applications. Also, the study examines only a subset (5 million documents) of the total pretraining data, which may exclude influential documents crucial to understanding the LLMs’ full generalization strategy.
3. The paper predominantly examines positively influential documents, yet negatively influential documents could offer essential insights into reasoning limitations and biases. Understanding negative influences would allow the authors to identify pretraining data that hinders reasoning or introduces procedural noise, shedding light on inherent biases that might restrict generalization. Only focusing on the positively influential documents might bias our judgements towards cherry-picking conclusions.

### Questions
1. Could you further explain why calculating document gradients with the base model and the query gradients with the fine-tuned model? Could this discrepancy cause any potential problems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the generalization strategies employed by LLMs when performing reasoning tasks compared to factual recall. The authors examine the influence of pretraining data on two LLMs of different sizes (7B and 35B parameters) by using influence functions to rank documents based on their impact on the likelihood of model outputs for reasoning and factual questions. They find that for reasoning tasks, LLMs do not rely heavily on direct retrieval of answers from pretraining data but instead use a broader set of documents that contain procedural knowledge relevant to the task. This suggests that LLMs generalize by learning how to perform reasoning steps rather than memorizing specific solutions. In contrast, for factual questions, the influential documents often directly contain the answers. The authors also note the overrepresentation of code in influential documents for reasoning, indicating its importance in teaching procedural knowledge to the models.

### Strengths
- The paper provides an important insight of LLMs, namely how models generalize beyond their training data, which is crucial for advancing reasoning capabilities of LLMs.
- The use of influence functions to study generalization in LLMs offers a good perspective on how models might learn to reason.
- The experiments are well-executed, and the analysis and explanation for drawing the findings are reasonable.

### Weaknesses
 - The study only looks at a subset of the pretraining data, which might not capture less frequent but highly influential documents. 
- Findings are based on two models from the same organization, potentially limiting the generalizability across different architectures or training regimes.
- There's no cross-validation with other methods of understanding model behavior which could corroborate the findings.

### Questions
- Could you elaborate more on how you define "procedural knowledge" in the context of your findings? How does this relate to the concept of learning algorithms or routines within the training data?
- Given the high influence of code documents, how might this skew the model's reasoning capabilities, especially in non-coding contexts?
- With these insights, what are the potential adjustments or enhancements in training strategies for LLMs to improve their reasoning generalization?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper applies the EK-FAC influence function to LLMs in an investigation of which documents, from a representative sample of LLM pretraining data, are used by a given model to answer basic mathematical reasoning questions. The EK-FAC influence function is used to produce a score for a given triple (prompt, completion, document) and these scores provide a basis to rank documents as more or less useful in generating the completion for the given prompt. Due to intense computational requirements, this technique is applied on a small sample of 80 prompt/completion pairs, but in great detail, examining several hundred documents at the top of the ranking for each pair. Several key findings emerge, including that models employ documents for reasoning responses in a different manner than for factual responses, and that such mathematical reasoning responses often rely on documents describing verbal procedures or code.

### Strengths
1. This paper presents a series of interesting and novel investigations into the influence of documents from pretraining in model responses. Most research in model interpretability is done by examining or modulating model parameters and activations, since it is usually computationally intractable to trace model responses back to pretraining samples; this is frontier research, and I was excited to read it.

2. The paper presents insights into which documents are used to answer mathematical reasoning questions, and crucially provides comparisons between two models within the same family, and also to a secondary task in factual question answering. The latter comparison was especially useful and cleanly conveyed the points made: specifically, that factual responses often rely on a specific document, but evidence is shown that reasoning responses may draw on a breadth of documents, possibly aggregating heterogeneous information into one response.

3. The experiments were extremely narrowly defined, but the authors caveat this early and often throughout the paper. Additionally, even in this narrowly scoped setting approximations must be made in order to be computationally tractable, and the authors honestly qualify discussions with reasonable alternate hypotheses and give sub-experiments to explore what is the most likely hypothesis. This kind of writing is very thoughtful and I appreciated that the authors made reasonable decisions and honestly qualified the claims, which were well supported.

### Weaknesses
1. As mentioned above, the experiments were very narrowly scoped. Only 80 questions were analyzed in total, and this 80 was further broken down into smaller sub-groups. Moreover, the questions were very simple mathematical problems using small numbers, requiring only short reasoning hops, and not resulting in fractional-valued answers. The experiments were performed only on two models within one model family, and one model is not available publicly. The authors do note all of these things, and some (not all) of these decisions seem to be made due to computational constraints, which is understandable. However, it would have been nice if these experiments were at least reproduced on fully public models such as Llama.

2. The description of EK-FAC was brief and not as clearly described as the later experiments and results, which were very clear. It would be nice to have a little more motivation about the individual components in the given formulas, since this methodology underlies all of the later experiments. Further, the discussion section at the end of the paper (sec 5) was very dense and a bit confusing. Maybe this could be restructured? The alternating hypotheses in the paragraph starting on L490 were particularly hard to follow.

3. (This is a minor point) Some of the mystique surrounding "reasoning" in LLMs may be because as a field we have conflated many types of problems into one, in the fervor of "AGI". Though this paper often discusses general reasoning, it looks specifically at mathematical reasoning, and it could be made more clear that these studies are distinct from linguistic reasoning, logical reasoning, spatial, etc etc. Analyzing linguistic reasoning provenance would be fascinating using this method, but would require different experiments.

### Questions
I have no serious questions for the authors, but if they have time:
1. Can this methodology be applied to model false-positives? It would be interesting to explore how pretraining documents may relate to hallucinations in generative responses, given prior research which points to cases of memorization.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the influence of specific pretraining data on the reasoning abilities of large language models (LLMs), focusing on how models rely on different types of documents when responding to reasoning versus factual queries. The paper applies influence functions to identify pretraining documents that impact performance on simple reasoning tasks. Results show that factual questions often depend on a smaller set of documents containing the answer, whereas reasoning questions are more influenced by documents with procedural knowledge.

### Strengths
1. The proposed method is straightforward, well-explained, and includes sufficient detail, making it easily reproducible.
2. This research addresses a crucial question: identifying what training data impacts LLM reasoning abilities, an area closely tied to model generalization and interpretability. It contributes to our understanding of LLMs.
3. The paper presents intriguing findings, highlighting distinctions in how LLMs handle factual versus reasoning tasks. For instance, factual questions frequently retrieve specific information, while reasoning tasks benefit from procedural knowledge.

### Weaknesses
1. The experimental setup is limited, potentially compromising the reliability of conclusions. Specifically: (1) only 80 queries were used for analysis, (2) the study included only three types of reasoning tasks, potentially limiting representation to other reasoning tasks, (3) there was no exploration of how different prompt formulations of the same query affect results, and (4) keyword-based methods for determining whether documents contain answers may be insufficiently accurate.
2. The analysis may lack granularity, as it considers only each document’s influence on the overall completion without examining its impact on individual reasoning steps. This might affect the conclusions.
3. While Appendix A.1 reports that influence scores are higher for certain documents, their similarity to random selections raises questions about whether influence functions reliably indicate actual influence.

### Questions
1. Why were these two specific LLMs chosen, instead of more widely used and capable models?
2. Using both fine-tuned and base models in the same experiment could lead to unreliable results due to differences in parameter initialization, potentially affecting influence calculations.
3. Since LLMs rely on embedded representations, even if keyword matching fails to find an answer, does it conclusively mean the document is not similar to the answer?
4. Could examples of retrieved documents for reasoning tasks be provided to offer insights into how they influence the model's approach to reasoning?

### Soundness
3

### Presentation
3

### Contribution
2
