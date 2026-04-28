# ChatKBQA: A Generate-then-Retrieve Framework for Knowledge Base Question Answering with Fine-tuned Large Language Models

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Knowledge Base Question Answering (KBQA) aims to answer natural language questions over large-scale knowledge bases (KBs), which can be summarized into two crucial steps: knowledge retrieval and semantic parsing. However, three core challenges remain: inefficient knowledge retrieval,  mistakes of retrieval adversely impacting semantic parsing, and the complexity of previous KBQA methods. To tackle these challenges, we introduce ChatKBQA, a novel and simple generate-then-retrieve KBQA framework, which proposes first generating the logical form with fine-tuned LLMs, then retrieving and replacing entities and relations with an unsupervised retrieval method, to improve both generation and retrieval more directly. Experimental results show that ChatKBQA achieves new state-of-the-art performance on standard KBQA datasets, WebQSP, and CWQ. This work can also be regarded as a new paradigm for combining LLMs with knowledge graphs (KGs) for interpretable and knowledge-required question answering.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper targets the KBQA problem. The proposed method, ChatKBQA, first generates a logical form, followed by the retrieval of entities and relations, aiming to avoid the influence of retrieval on logical form generation and to enhance retrieval efficiency. The authors fine-tune open-source LLMs using instruction tuning techniques to equip them with the capability to perceive and generate in logical form format. 
The authors use an unsupervised retrieval method for entities and relations retrieval, which conducts phrase-level semantic retrieval in the entity set and relation set of the KB for entities and relations in the logical form.

### Strengths
1. The experiment results are stronger and better than the previous SOTA.
2. An earlier work leveraging LLM to generate a logic form for retrieval. The framework looks interesting by adjusting each component for LLM.
3. Good discussion on related work.

### Weaknesses
1. The proposed method is similar to semantic parsing-based methods, which focus on translating questions into logical forms executable against KBs, such as SPARQL, query graph, and S-expression, as discussed in the related work.
2. Considering the authors replaced the backbone model with LLMs, it is hard to identify which parts play the key role in performance improvement. It would be better to have more ablation studies. For example, replacing LLM with the pre-trained model in baseline, such as T5, or fixing LLM and replacing the parsing and IR component with the baseline method.
3. Efficient fine-tuning methods seem not related to the claims in the paper. There's no need to discuss it in the methodology section.

### Questions
As mentioned in the weaknesses, which part plays a crucial role in model improvement?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces ChatKBQA, a novel generate-then-retrieve KBQA framework that leverages the power of modern fine-tuned large language models. The proposed method differs from traditional approaches in that it focuses on generating logical forms before retrieval, which overcomes inherent challenges such as retrieval inefficiencies and the misleading influence of retrieval errors in semantic parsing with the help of fine-tuned open-source LLMs and unsupervised retrieval methods. Experimental results on two standard KBQA benchmarks demonstrate that the developed framework performs better than existing methods and offers plug-and-play flexibility.

### Strengths
- The paper is clearly written and well organized, with sufficient background introduced before the detailed description of the methodology.
- The philosophy of generate-then-retrieve is simple and effective, significantly elevating the retrieval efficiency and reducing the retrieval error. The proposed framework achieves a new state-of-the-art performance in the KBQA domain.
- The authors conducted a detailed experimental analysis, showing the effectiveness of each designed module and the flexibility of the proposed approach as a plug-and-play framework.

### Weaknesses
 - Lacking analysis of the failure examples, I am curious which module caused the error when the proposed framework did not get the correct answer.
- It would be better to list the detailed statistics of the datasets, *e.g.,* number of the skeletons of logical forms involved in the training set and the test set, etc.
- Please add an analysis of the computational efficiency (complexity) of the retrieval module. As far as I understand, each entity in the generated entity list has to compute similarity with the whole entity set of the knowledge base (same for the relations).

### Questions
- Why does the beam size have such an influence on the performance?
- During the test phase, when the fine-tuned LLMs generate logical forms, can they correctly generate relations not seen in the training set? I guess they can generate the right entities even though those entities have not appeared in the training set before, as seed entities are typically included in the natural language questions. But it is not necessarily for relations, this is why I'm curious about the result that ChatKBQA w/o RR is better than ChatKBQA w/o ER.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes chatKBQA, a generate-then-retrieve KBQA framework built on fine-tuning open-source large language models (LLMs) like Llama2, chatGLM2 and Baichuan2. ChatKBQA generates logical form with fine-tuned LLMs first, then will retrieve and replace entities and relations using unsupervised retrieval. The paper shows that chatKBQA achieves SOTA on two KBQA datasets, but more details of the method should be clarified before determining whether the method truly achieves SOTA.

### Strengths
- ChatKBQA is very flexible, able to switch from different unsupervised retrieval methods, different language models and different efficient fine-tuning methods.
- Extensive comparison against baselines are done, and the authors provided results for different configuration on chatKBQA.

### Weaknesses
 - In section 4.3 and 4.4, words such as “somewhat” and “good generative ability” appears in the description yet I am concerned that even with beam search, only 77% of the result lists contain the ground truth logical forms. If the relationships and entities were replaced, how do we ensure that the plugged-in entities/relationships were the right one? In what percentage were the right entities/relationships being plugged in if no ground truth is available? The paper lacks a clear analysis of how often the retrieved entities and relations are correct, and how this impacts the final query execution. The method description needs to clarify the exact process of how the beam search results are used, and how the system decides which logical form to execute, especially when multiple candidates are available.
- In section 4.5, the authors claim that Graph-Query-of-Thoughts are a way to improve QA’s interpretability and avoid LLM’s hallucinations, which has no evidence support in the result/analysis section. This seems to be an exaggerated claim and I am not convinced. The paper does not provide any empirical evidence or analysis to support the claim that the proposed Graph-Query-of-Thoughts approach improves interpretability or reduces hallucinations. The idea is presented as a future direction, but the current results section does not validate this claim, making it seem speculative.
- Presentation of the paper needs improvement. Multiple grammatical errors, and the description of the method is confusing. Explanation of methods like QLora.etc can be moved to related work, since now it is interrupting the flow of the writing. The paper's writing quality needs significant improvement, with numerous grammatical errors and unclear descriptions of the proposed method. The inclusion of detailed explanations of techniques like QLoRA within the method section disrupts the flow and should be moved to the related work or an appendix.

### Questions
- In section 4.2, why does chatKBQA converts the SPARQL corresponding to the test set in the KBQA dataset into logical form? Why test set?
- How do you compare against chatGPT and GPT-4? The paper says that chatGPT and GPT-4 failed to generate logical form, is this zero-shot or few-shot?
- ChatKBQA seems to rely on “ground truth logical forms”, which might be a rare resource. The datasets used are outdated since the task is now a less popular task, and I am curious of how chatKBQA will be useful in an open-domain QA era.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
