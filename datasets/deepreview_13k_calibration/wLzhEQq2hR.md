# Do Vision-Language Models Really Understand Visual Language?

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 8, 5

## Abstract
Visual language is a system of communication that conveys information through symbols, shapes, and spatial arrangements. Diagrams are a typical example of a visual language depicting complex concepts and their relationships in the form of an image. The symbolic nature of diagrams presents significant challenges for building models capable of understanding them.
Yet, recent studies seem to suggest that Large Vision-Language Models (LVLMs) can even tackle complex reasoning tasks involving diagrams.
In this paper, we investigate this phenomenon by developing a comprehensive test suite to evaluate the diagram comprehension capability of LVLMs. 
Our test suite uses a variety of questions focused on concept entities and their relationships over a set of synthetic as well as real diagrams across several domains to evaluate the recognition and reasoning abilities of models. %
Our evaluation of three LVLMs (GPT-4V, GPT-4o, and Gemini) shows that while these models can accurately identify and reason about entities, their ability to understand relationships is notably limited. 
Further testing reveals that the decent performance on diagram understanding largely stems from leveraging their background knowledge as shortcuts to identify and reason about the relational information.
Thus, we conclude that LVLMs have a limited capability for genuine diagram understanding, and their impressive performance in diagram reasoning is an illusion emanating from other confounding factors, such as the background knowledge in the models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper demonstrates an in-depth evaluation if Vision Language models (VLM) can understand visual digram. The authors show the results both on their synthetically generated dataset as well as real visual diagrams curated from real datasets. They curate an extensive list of possible questions to evaluate VLM’s separately on each question category.

### Strengths
The template of questions used in the paper is quite extensive. The authors also carefully evaluated each template separately showing a holistic evaluation framework. Specifically, the key observation noticed under Q1 seems interesting to me. The ability of VLM to understand and reason well about entities while struggling with relationships shows that relationships are hard to decode in general. The performance gap between real and synthetic datasets is also interesting.

### Weaknesses
1. The paper write-up could perhaps be revisited. It is difficult to read Table 6 the first time — the relative improvement could perhaps be presented more intuitively.
2. The motivation behind using ‘knowledge as a shortcut' in sections 4 and 5 was not clearly stated. Was there a chance for choosing to construct a separate knowledge graph of textual content rather than labeling the visual entities in the original diagram? Providing the rationale behind this construction would be interesting. Since ‘knowledge’ is a quite generic word, it might be useful to define more precisely what kind of knowledge they are referring to early in the paper. 

3. There are some relevant works from Chart, Graph, and 3D scene understanding that will be worth mentioning in the related works section:

        - ChartQA: https://arxiv.org/abs/2203.10244

        - Talk like a graph: Encoding graphs for large language models: https://research.google/blog/talk-like-a-graph-encoding-graphs-for-large-language-models/

        - CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning: https://openaccess.thecvf.com/content_cvpr_2017/html/Johnson_CLEVR_A_Diagnostic_CVPR_2017_paper.html

### Questions
1. Could it be possible to make the synthetic dataset public so that the reviewers have a better sense of its content?
2. The authors classified the diagram complexity based on the number of entities. Was there a reason they did not consider the number of relationship to measure complexity?

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
This paper evaluates three LVLMs on diagram understanding. The authors curated a synthetic + real diagram dataset and investigated LLM performance on entity and relation recognition. Results suggest that LVLMs may not be truly understanding diagrams.

### Strengths
- The writing is very clear. As a reader, I feel that the hypotheses, experiment designs, and results are all clearly conveyed. I especially like how the authors layer experiments based on previous results to provide deeper and deeper insights.
- Experiments are overall well-designed. The tasks seem reasonable. The combination of synthetic and real diagrams is a strength that allows controllability and real-world validity. I like how the authors pay attention to details like varying the sizes and colors of arrows in the diagrams.

### Weaknesses
1. Making counterfactual variations of diagrams and asking LVLMs about them is certainly interesting, but I think it is not surprising that this should degrade LVLM performance. When strong prior is present and the diagram contradicts that, the LVLM could simply get confused. In such cases I think it is important to test if explicitly including instructions to ignore prior knowledge and solely answer using the information in the diagram improves the performance. Take Section 5.2 as an example. When no link is present (middle panel), asking "How many food chains are there?" sounds more like the goal is to test relevant ecology knowledge instead of diagram reading, and I think the LVLM's decision to hallucinate connections is actually warranted. In other words, this case in particular feels like an unfair trick question to me.
2. This paper tested 3 LVLMs. Perhaps testing a few more would be helpful, e.g., Claude 3.5 Sonnet.
3. Even though I appreciate the inclusion of a real-world dataset, it is exclusively focused on science. A broader scope would be better.

### Questions
- "Furthermore, we demonstrate that the models primarily rely on knowledge shortcuts when answering complex diagram reasoning questions." I am uneasy with the use of "primarily". The difference between KR and KF is at most ~15%. Saying "primarily" seems wrong to me. Saying knowledge is a shortcut LVLMs exploit seems reasonable, but could the authors justify why they said "primarily"?

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
3

### Summary
The presented work examines to what degree large vision-language models (LVLM) understand diagrams. A test suite is developed that includes diagram-understanding questions for a synthetic and real-world dataset. The questions are distributed into four categories: Every question is either a recognition or reasoning question, and every question is either knowledge-required or knowledge-free. The questions are either applied to entities in the diagram or to relations between them. While LVLMs can recognize and reason about entities in synthetic diagrams, they show poor performance for entities on real-world data. Surprisingly, their performance improves on more complex, real-world diagrams. The authors provide evidence that this performance leap originates from semantic background knowledge that the LVLM bears. In a case study, the authors show that the LVLMs hallucinate some answers due to their semantic background knowledge.

### Strengths
- The paper is written well, and the figures help the reader understand the main ideas. 
- The categorization of questions is intuitive and exemplified, and the test suite allows for further research in the direction of diagram understanding. An extensive appendix supports the main text by providing additional information about the curated test suite and the research methodology.
- The findings are novel and counter-intuitive. The semantic background leakage is well-induced and confirmed by extensive experiments. It highlights a surprising weakness of state-of-the-art LVLMs that should be considered when using them.
- The findings bear opportunities for future research. Semantic background leakage may also appear in other areas besides diagram understanding. Furthermore, it should be researched how LVLMs can be trained to be more robust and effective in diagram understanding.

### Weaknesses
 The case study (Section 5.2) could be more extensive, and its design includes some shortcomings: 
- The evaluation of the middle figure needs to be revised, as the correct answers are not included in the answer options. I propose to include an additional experiment, possibly in the appendix, with correct answer options. It would be highly interesting to observe if LVLMs even deviate from correct reasoning due to their inherent semantic background knowledge.
- Another important aspect that needs to be considered in the case study is the spatial positioning of the entities. To exclude the influence of spatial positionings on the observed hallucinations, I propose to rerun the case study with swapped spatial positions. Is the "fish" consistently predicted if swapped with the other entities?

### Questions
The main text does not state how the real-world diagram set was curated. Specifically, it would be interesting which filtering criteria were applied. Did you filter diagrams only by their domain? Did you apply a limit for the maximum number of nodes/relations/edge crossing?

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
2

### Summary
This paper proposes an evaluation framework to assess LVLMs' capability in understanding diagrams. The results show that models like GPT-4V and Gemini rely primarily on their knowledge base rather than reasoning abilities when understanding relationships.
However, contributions of this paper are not particularly prominent. Is the core contribution the proposed test suite, the evaluation dataset, or the insights gained? In fact, some of these insights have already been revealed, such as “models consistently perform well on entity-related questions”, “models exhibit significant difficulty in identifying relationships”. I suggest that authors review the existing work and clearly highlight the differences between this paper and previous work, including the evaluation methods and insights gained.
Additionally, beyond the overall evaluation results, I would like to see specific results across different domain and topics (as shown in Table 2). This could lead to new discoveries and spark more valuable discussions (involving different knowledge systems). 

The Chain of Thought approach mentioned by the authors is relatively simple, as it only involves adding prompts like “think Step-by-Step.” Are there any more effective ways to use Step-by-Step prompts for this kind of chart? I suggest that the authors explore this in greater depth. In the authors’ experiments, it is mentioned that under certain circumstance, the test of LVLMs do not use any knowledge shortcuts. However, for some simple relational charts, how can we be certain that these large models have not encountered similar charts during training? This point remains uncertain.

By the way, in this work, beyond the evaluations conducted by the authors, I would like to see a model proposed by the authors specifically for understanding basic relational charts.

### Strengths
The overall contribution of the paper lies in the comprehensive nature of the experiments, including a relatively thorough consideration of chart understanding (both explicit and implicit) and other relevant aspects.

### Weaknesses
However, contributions of this paper are not particularly prominent. Is the core contribution the proposed test suite, the evaluation dataset, or the insights gained? In fact, some of these insights have already been revealed, such as “models consistently perform well on entity-related questions”, “models exhibit significant difficulty in identifying relationships”. I suggest that authors review the existing work and clearly highlight the differences between this paper and previous work, including the evaluation methods and insights gained.

Additionally, beyond the overall evaluation results, I would like to see specific results across different domain and topics (as shown in Table 2). This could lead to new discoveries and spark more valuable discussions (involving different knowledge systems).

The Chain of Thought approach mentioned by the authors is relatively simple, as it only involves adding prompts like “think Step-by-Step.” Are there any more effective ways to use Step-by-Step prompts for this kind of chart? I suggest that the authors explore this in greater depth. In the authors’ experiments, it is mentioned that under certain circumstance, the test of LVLMs do not use any knowledge shortcuts. However, for some simple relational charts, how can we be certain that these large models have not encountered similar charts during training? This point remains uncertain.

By the way, in this work, beyond the evaluations conducted by the authors, I would like to see a model proposed by the authors specifically for understanding basic relational charts.

### Questions
Additionally, beyond the overall evaluation results, I would like to see specific results across different domain and topics (as shown in Table 2). This could lead to new discoveries and spark more valuable discussions (involving different knowledge systems). 

The Chain of Thought approach mentioned by the authors is relatively simple, as it only involves adding prompts like “think Step-by-Step.” Are there any more effective ways to use Step-by-Step prompts for this kind of chart? I suggest that the authors explore this in greater depth. In the authors’ experiments, it is mentioned that under certain circumstance, the test of LVLMs do not use any knowledge shortcuts. However, for some simple relational charts, how can we be certain that these large models have not encountered similar charts during training? This point remains uncertain.

By the way, in this work, beyond the evaluations conducted by the authors, I would like to see a model proposed by the authors specifically for understanding basic relational charts.

### Soundness
3

### Presentation
3

### Contribution
2
