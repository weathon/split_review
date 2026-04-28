# Automated Knowledge Concept Annotation and Question Representation Learning for Knowledge Tracing

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Knowledge tracing (KT) is a popular approach for modeling students' learning progress over time, which can enable more personalized and adaptive learning. However, existing KT approaches face two major limitations: (1)~they rely heavily on expert-defined knowledge concepts (KCs) in questions, which is time-consuming and prone to errors; and (2)~KT methods tend to overlook the semantics of both questions and the given KCs. In this work, we address these challenges and present \framework, a framework for \emph{automated \textbf{k}nowledge \textbf{c}oncept annotation and \textbf{q}uestion \textbf{r}epresentation \textbf{l}earning} that  can
improve the effectiveness of any existing KT model. First, we propose an automated KC annotation process using large language models (LLMs), which generates question solutions and then annotates KCs in each solution step of the questions. Second, we introduce a contrastive learning approach to generate semantically rich embeddings for questions and solution steps, aligning them with their associated KCs via a tailored false negative elimination approach. These embeddings can be readily integrated into existing KT models, replacing their randomly initialized embeddings. We demonstrate the effectiveness of \framework across 15 KT models on two large real-world Math learning datasets, where we achieve consistent performance improvements.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors address two primary shortcomings of existing work on knowledge tracing (KT): (1) mapping questions to knowledge concepts (KCs) being evaluated (I believe from a KC taxonomy defined by subject-matter experts) and (2) a lack of pre-trained embeddings for questions aligned with KCs when applying to KT systems. Methodologically, (1) is addressed by using a SotA LLM to produce a chain-of-thought (CoT)-based answer to a given question and annotate each step with automatically generated KCs and (2) is addressed through a contrastive learning approach to producing questions embeddings that align questions and reasoning steps with KCs produced in (1). Since the learned embeddings are application and not system specific (i.e., it is designed for this task, but not a specific KT model), they can be used as pre-trained embeddings for KT tasks. Accordingly, the authors experiment with adding these to 15 recent KT models with two widely used benchmarks for predicting student response from a sequence of retrospective student interactions, showing consistent improvements over the baseline implementations. Secondary results are provided for the amount of training data (the proposed system needs to see fewer student training examples), quality of the automated KC annotations (generated KCs are better than default annotations as evaluated by a LLM), and the value of the proposed contrastive learning procedure (it is better than embedding generation alternatives). Overall, the authors make a convincing case that the proposed improvements utilizing SotA LLMs advance the SotA for KT problems.

### Strengths
This is primarily an applied research submission as it relies on both SotA LLM capabilities (i.e., CoT, knowledge concept generation) within the target domain and existing methods for representation learning with contrastive learning (albeit with domain specific considerations). As previously stated, I think the authors make a convincing case in establishing SotA for the KT setting.

From an originality perspective: (1) other than the task specification and benchmark datasets, there is ostensibly significant methodological innovation within this domain and (2) from a ML/NLP perspective, there is very limited originality; the LLM prompts are relatively straightforward and the contrastive learning procedure follows from a relatively standard 'cookbook'. However, the existing methods are applied correctly, perform well, and introduce new methods to this domain.

From a quality perspective, overall the formulation is well-motivated, conceptually sensible, and performs well. Again, as an applied piece of research, I am convinced that this is advancing the SotA for knowledge tracing. Additionally, the developed methods produce advancements that apply to many existing KT systems (and likely future KT systems) -- and show consistent improvements when applied to existing systems. The 'secondary' experiments are solid from the perspective of supporting the chosen models (e.g., contrastive learning) and answering practical questions with respect to deployment (e.g., number of students in training).

Regarding clarity, the paper is well-motivated, rigorously presented, and easy to understand. The figures are clear overall and any ambiguities can be clarified by the prompts in the appendices. The discussion of experimental results highlights the key findings and makes specific references to table to help the reader focus on the most important quantifications.

Regarding significance, I am not an expert in education, but am convinced that this is a successful application of LLMs to this domain and a notable improvement in performance for the KT task.

### Weaknesses
Conversely, below are some of my concerns with this paper:
- From an applied perspective, the experiments are conducted on mathematical reasoning datasets. Since this work is heavily dependent on CoT and KC annotation, it isn't clear that it would work for other domains (e.g., physics, history, etc. -- lines 168-169).
- From a methods perspective, there are limited experiments (e.g., simpler embeddings as a baseline, variety in LLM quality). These aren't mandatory from an applied perspective, but would possible broaden the interest of the paper (which is another potential weakness).
- I am not an education expert, but I am guessing that evaluating KCs with another LLM isn't the standard evaluation procedure. This isn't a big deal since the primary goal of the paper is improving KT results. However, some human-in-the-loop evaluation would help strengthen this specific evaluation.

### Questions
The one clarification question I had was regarding if KCs are generally taken from a SME-generated taxonomy and this is relying on (instruction-constrained, but still open-ended) LLM generation. If there is a fixed taxonomy, it would be interesting to see references and/or summary statistics. For the LLM generated cases, it would be interesting to see the statistics of this generated set (e.g., unique labels, perplexity). Clarifying my understanding would be helpful.

The second question is any discussion regarding additional education domains, simpler embeddings, and lower-power LLMs. I don't expect full experiments, but any additional information would be helpful.

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
5

### Summary
In this paper, authors bridge the gap by emphasizing the importance of learning question embeddings and propose to automatically annotate the knowledge concepts by using BERT. The idea is somehow recognized, however, the design of both components is not satisfactory. I have commented below with some suggestions for further improvements.

### Strengths
1. Traditional methods are more like a sequential prediction task which ignores the semantic information in both Qs and KCs. This paper leverages the power of LLMs to automatically annotate the KCs for each question, and learn a better question embedding guided by the contrastive learning.
2. Figures are well-drawn for readers to follow.
3. Extensive experiments are conducted to support the claim and the importance of question embedding.

### Weaknesses
* The authors claim to have a careful negative sampling in this paper to avoid false negatives for contrastive learning. However, the auto-annotation is generated by LLMs which is difficult to control for a consistent and high-quality output all the time. There will definitely be noise introduced or similar concepts annotated in different ways during the annotation which may greatly decrease the performance during semantic learning.
> Authors cluster the similar KCs in the same cluster to reduce the impacts, however, this will still definitely affect the learning performance since they are indeed different KCs in the data level. 

> Reversely, I suggest to carefully clean the annotation by asking LLMs to bootstrap a pool or seed bank for standardized KC candidates. Each time, a new KC will be verified with the seeds we already have to avoid chaos, and a checked new one will be added into the bank.

* The design of question embedding is partially recognized for its advantages. However, there is totally nothing to do with the Student history! Seems like authors are just considering them as labels. This is a big problem where in KT tasks, student interactions are very important to guide the personalized prediction based on his/her historical performance. But in this paper, authors completely abandon the semantic or sequence guidance from student histories, which is one of the biggest problems here.

* The notations are confusing, both student and s solution steps are represented as 's'.

* BERT is not an LLM at all. The title is mis-claimed.

### Questions
N/A

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a framework named KCQRL, designed to address key limitations in traditional knowledge tracing (KT) models. KT models typically require extensive manual annotation of knowledge concepts (KCs) and often overlook the semantic content of questions. KCQRL introduces automated KC annotation using large language models (LLMs) and employs contrastive learning to create semantically rich question representations. The framework is intended to integrate seamlessly with existing KT models, enhancing performance on prediction tasks across datasets.

### Strengths
- The proposed framework’s use of LLMs for KC annotation reduces dependency on manual input, potentially streamlining the annotation process. KCQRL is presented as a flexible solution that can enhance multiple KT models. 

- The experimental results across various KT models demonstrate consistent performance gains, supporting the efficacy of integrating semantic embeddings.

- The framework shows potential for low-sample settings, which could benefit platforms with limited data.

### Weaknesses
 - The quality of KC annotations and question representations is heavily influenced by the LLM used. Reporting the effects of using different LLMs would provide insights into the adaptability of the proposed method. For example, instead of using GPT-4o, employing domain-specific LLMs might enhance the performance? 

- The framework's heavy reliance on contrastive learning to handle false negatives might reduce model interpretability, particularly when working with similar KCs. 

- Experiments focus solely on two math-focused datasets, making it unclear how well KCQRL would generalize to other subject areas or to question types that are more complex, such as open-ended responses.

### Questions
- How does KCQRL handle ambiguous or multi-topic questions that might not map clearly to a single KC?
- What steps, if any, are planned to improve interpretability of the model’s embeddings, especially with similar or overlapping KCs? 
- How does KCQRL adapt when LLMs used for KC annotations become outdated or unavailable?

### Soundness
3

### Presentation
3

### Contribution
3
