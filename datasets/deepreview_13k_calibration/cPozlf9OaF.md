# Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Large language models (LLMs) have shown remarkable capabilities in natural language processing; however, they still face difficulties when tasked with understanding lengthy contexts and executing effective question answering. These challenges often arise due to the complexity and ambiguity present in longer texts. To enhance the performance of LLMs in such scenarios, we introduce the Long Question Coreference Adaptation (LQCA) method. This innovative framework focuses on coreference resolution tailored to long contexts, allowing the model to identify and manage references effectively. The LQCA method encompasses four key steps: resolving coreferences within sub-documents, computing the distances between mentions, defining a representative mention for coreference, and answering questions through mention replacement. By processing information systematically, the framework provides easier-to-handle partitions for LLMs, promoting better understanding. Experimental evaluations on a range of LLMs and datasets have yielded positive results, with a notable improvements on OpenAI-o1-mini and GPT-4o models, highlighting the effectiveness of leveraging coreference resolution to bridge context gaps in question answering.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes to disambiguate mentions in a document by replacing pronouns with corresponding disambiguated entities identified by coreference resolution so that a large language model (LLM) can easily leverage a long context document for better contextual understanding. One of the crucial problem for an LLM is to understand a long context to respond to a query, but ambiguities in mentions in a document can easily impact the understanding to derive an answer. This work employs a BERT-based model to identify coreference resolution as a preprocessing step to modify a document-wise context to disambiguate mentions. Experiments are carried out on diverse tasks demanding long context understanding, e.g., LongBench, and show large gains when compared with other methods. e.g., RAGs.

### Strengths
- A simple method to resolve ambiguity of mentions in a document so that an LLM can easily leverage the contextual information to generate a response. The use of a BERT-based model is a limitation in that it cannot handle longer contexts, but this work proposes a method to combine coreference resolution results for sub-documents using a simple statistics, i.e., whether a mention is within a cluster or not, to compute a distance metric.

- Experiments show gains when compared with other methods considering long contexts, e.g., RAGs. Analysis is also interesting enough to quantify the gains of the proposed method.

### Weaknesses
 - It is not clear how the errors in coreference resolution might have an impact to the end performance since coreference resolution itself is a rather challenging task.

### Questions
I'd like to know how the errors in coreference resolution might have an impact to the end performance. Probably it is possible to inject noises in coreference clusters to see how that will impact to the end performance.

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
4

### Summary
This paper investigates LLM performance in question answering and summarization tasks with very long
inputs (128K). The hypothesis put forward is that preprocessing the input with coreference 
resolution allows the model to understand the long context better, in particular to identify 
and manage references effectively. The proposed method  encompasses
four key steps: resolving coreferences within sub-documents, computing the distances between mentions,
 defining a representative mention for coreference, and
answering questions through mention replacement. Experimental evaluations on a range of LLMs and
datasets yield overall improvement.

### Strengths
- The idea of performing coreference resolution before attempting to do the task at hand, makes sense and is corroborated
by empirical results showing improvements across models and datasets. 

-  The paper is well-written and the proposed method easy to follow. 

- The proposed coreference approach seems intuitive and could be also used during LLM pertaining or fine-tuning.

### Weaknesses
 - The technical contribution is somewhat limited. Coreference merging is interesting, however, without empirical evaluation it is not possible to tell whether it actually works (only down-stream evaluation results are presented, see my questions below).

- What is the main contribution of this paper, is it the algorithm in Section 3.2?

-



### Questions
- Please explain what I am supposed to be seeing in Figure 2. Your caption is not very informative either. 

- It would been useful to see  an actual example for the method in Section 3.2. 

- Please present the prompts you use for the various tasks (e.g., QA, summarization), in the appendix. 

- What is the accuracy of your coreference algorithm with the mention merging computation? How accurate is your approach? 
 I understand that the input is very long, but perhaps you could perform some manual evaluation on shorter documents. It would be interesting to see what the degree of noise is, and how much better your results would be if coreference was perfect. 

- Please describe Maverick in more detail, ILCR readers may not be familiar with what it does. 

- I would have liked to see if results improve further with fine-tuning (e.g., using Lora). 

- What is the computational complexity of the coreference preprocessing step?
- RAG and RECOMP are not incompatible with your method, could you not run coreference on the retrieved segments? 

- It would be good to analyze why you observe performance improvements. Is it because you identify named entities more accurately? 

- Existing work (e.g., https://aclanthology.org/2024.lrec-main.145.pdf) shows that LLMs are not very good at coreference resolution, however, it would have been more reasonable to give the LLM some examples (my understanding is you try to perform coreference in a zero-shot setting). 

-  Is your Avg column in table 1 averaging across Rouge, Accuracy, and F1? 

-

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the LQCA method, which aims to enhance the performance of LLMs in understanding lengthy contexts and executing effective question answering. The LQCA method focuses on coreference resolution within long contexts, systematically processing information to replace ambiguous or complex references with clearer mentions, thereby improving the model's comprehension. The paper claims that this approach leads to significant improvements in question answering performance on various LLMs and datasets, particularly on models like OpenAI-o1mini and GPT-4o.

### Strengths
The paper addresses an important issue in natural language processing, which is the difficulty LLMs face in dealing with long contexts.

The proposed LQCA method is a novel approach that combines coreference resolution with question answering in long contexts.

### Weaknesses
While the paper demonstrates improvements in performance, it does not provide a comprehensive comparison with alternative methods that also aim to improve long-context understanding.

The paper could benefit from a more detailed discussion on how the LQCA method handles cases with highly ambiguous references, which could be a common occurrence in real-world applications.

There is a lack of analysis on the computational overhead introduced by the LQCA method, which is crucial for understanding its scalability and practical applicability.

### Questions
How does the LQCA method perform compared to other state-of-the-art approaches in terms of accuracy and efficiency, especially when dealing with extremely long or complex texts?

How does the LQCA method handle highly ambiguous contexts where multiple interpretations of coreferences are possible?

What are the potential impacts of incorrect coreference resolution on the quality of question answering, and how does the LQCA method address these issues?

Can the authors provide more insights into the computational overhead introduced by the LQCA method and its scalability for even longer contexts?

### Soundness
3

### Presentation
2

### Contribution
3
