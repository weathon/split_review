# Evidence-Enhanced Triplet Generation Framework for Hallucination Alleviation in Generative Question Answering

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
To
address the hallucination in generative question answering (GQA) where the answer can not be derived from the document, we propose a novel evidence-enhanced triplet generation framework,
EATQA, encouraging the model to
predict all the combinations of ⟨Question, Evidence, Answer⟩ triplet
by flipping the source pair and the target label
to understand their logical relationships, i.e.,
predict Answer(A), Question(Q), and Evidence(E) given a QE, EA, and QA
pairs, respectively. Furthermore, we bridge the distribution gap to distill the knowledge from evidence in inference stage. Our framework ensures the model to learn the logical relation between query, evidence and answer, which simultaneously improves the evidence generation and query answering. In this paper, we apply EATQA to LLama and it outperforms other LLMs-based methods and hallucination mitigation approaches on two challenging GQA benchmarks. Further analysis shows that our method not only keeps prior knowledge within LLM, but also mitigates hallucination and generates faithful answers.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes EATQA (Evidence-Enhanced Triplet Generation Framework), designed to reduce hallucinations in Generative Question Answering (GQA). EATQA leverages a structured approach by generating triplets of Question, Evidence, and Answer (QEA) and using these to reinforce logical consistency. The model is trained on three main tasks: evidence generation, question answering, and query restoration, which improve the alignment between evidence and answers. Tested on MultiRC and QASPER datasets, EATQA achieves state-of-the-art results, effectively reducing hallucination and enhancing answer fidelity by distilling knowledge directly from evidence during inference.

### Strengths
1. The paper presents a comprehensive methodology and demonstrates a strong experimental setup. EATQA's effectiveness is validated across two benchmarks, MultiRC and QASPER, where it outperforms prior state-of-the-art models. The paper provides detailed comparisons with competitive LLMs, proving the reliability and effectiveness of the proposed method. Ablation studies further establish the significance of each component in the framework, such as the impact of removing evidence generation or query restoration on performance.
2. The authors provide a clear exposition of EATQA’s architecture and its underlying principles. The paper is well-organized, with clear definitions of the three primary tasks (evidence generation, question answering, and question restoration). Figures, such as the model overview and template instructions, aid in visualizing the complex relationships within the triplet generation framework. Additionally, the equations and methodological breakdown make it accessible to readers familiar with GQA and hallucination mitigation research.

### Weaknesses
1. Limited innovation: The paper's proposed three training losses lack technical depth, and this multi-task approach has already been proposed and used in many scenarios. Although there are improvements on two benchmarks, the method does not provide new insights or thoughts for the readers. The core idea of generating intermediate evidence to enhance answer fidelity, while practically useful, does not introduce a novel theoretical framework or a significant departure from existing multi-task learning paradigms. The specific implementation of the evidence generation task, which involves selecting sentences from the original document, is a form of extractive summarization, a well-explored area. The query restoration task, while contributing to the overall framework, is also not a novel concept, and its integration with evidence generation and question answering is not theoretically groundbreaking.
2. Insufficient baseline models: The discussion of baseline models for retrieval-enhanced methods in the paper is not comprehensive enough. The paper should include more recent and diverse retrieval-augmented models, especially those that incorporate more advanced retrieval mechanisms beyond basic methods. The comparison should also include methods that use different types of knowledge sources, such as structured knowledge graphs or external knowledge bases, to provide a more complete picture of the current state-of-the-art.
3. Limited generalizability: The paper does not conduct experiments on a broader range of datasets, making it difficult to demonstrate the method's generalizability, especially in scenarios where large models are fine-tuned, such as in different types of multi-hop QA scenarios like NQ, TQ, StrategyQA, and MusiQA. The current evaluation is limited to two datasets, which may not fully capture the complexities of real-world question-answering scenarios. The method's performance on datasets requiring more complex reasoning or different types of evidence would be crucial for assessing its robustness and applicability.
4. Non-standard writing format: There are many citation format errors, images are not in vector format, and there are issues with the image formatting.

### Questions
See the weaknesses section.

### Soundness
2

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
3

### Summary
This paper proposes EATQA to address hallucination issues in GQA. It is an unified triplet generation approach that can capture logical relationships between question, evidence, and answer.

### Strengths
The method is well-motivated and the paper is easy to follow. The experiments show the proposed method has great improvements.

### Weaknesses
1. The method is based on gold evidence annotations when training. It may limit its applicability to datasets without such annotations.

2. The improvement margins on some baselines, e.g., CAD and RHO, are relatively modest.

3. Is the computational costs and inference time comparison to baselines missing?

### Questions
How does the method perform on datasets without gold evidence annotations?

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
3

### Summary
The paper proposed an evidence-enhanced triplet generation framework, EATQA, to address a hallucination issue in generative question answering (GQA). The EATQA encourages the model to predict Answer (A), Question (Q), and Evidence (E), given QE, EA, and QA pairs, respectively. that is, all the combinations of ⟨Question, Evidence, Answer⟩. to understand their relationships. The paper applied it to LLama, that outperformed other LLM-based methods and hallucination mitigation approaches on two GQA benchmarks.

### Strengths
The proposed triplet generation framework showed significant improvement on two widespread document-based GQA datasets, MultiRC and QASPER, yielding state-of-the-art performance on the datasets.

### Weaknesses
1. First, the paper was not necessarily written in good English. It should receive a native check. Further, it is partly difficult to understand. The authors incorrectly used LaTeX cite commands, that makes the draft more difficult to read. It is better to check the whole draft more carefully again. 

2.  While the proposed framework could yield better performance in GQA tasks, the evaluation in hallucination alleviation was not necessarily thorough enough, that makes it difficult to judge whether the proposed framework is really good in the hallucination alleviation.  The analysis in Sec. 5.4 did not necessarily directly evaluate the degree of hallucination alleviation. Furthermore, no comparisons with previous related work were shown. It is better to show how well the proposed framework can alleviate hallucination directly and clearly, in comparison with related work.

3. In the analysis in Sec. 5.3, no explanation was provided for the performance in Table 6. If it is the evaluation for generated evidences, how reference evidences can be obtained because it was mentioned that evidence annotation is unavailable in the datasets? it is also not described how the scores were calculated. 

4. The analysis in Sec. 5.2 seems to contribute to fewer useful findings. In my understanding, since the document length is proportional to the number of sentences, just a table might be enough from Tables 4 and 5.

5. It is better to clearly describe how the authors fixed hyperparameters in the experiments.

### Questions
1. What was the value for a hyperparameter \alpha_{kl} and how did the authors fix it?

### Soundness
2

### Presentation
2

### Contribution
3
