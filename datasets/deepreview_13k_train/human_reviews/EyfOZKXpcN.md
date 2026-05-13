# Improving Language Models via Plug-and-Play Retrieval Feedback

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Large language models (LLMs) exhibit remarkable performance across various NLP tasks. However, they often generate incorrect or hallucinated information, which hinders their practical applicability in real-world scenarios. Human feedback has been shown to effectively enhance the factuality and quality of generated content, addressing some of these limitations. However, this approach is resource-intensive, involving manual input and supervision, which can be time-consuming and expensive. Moreover, it cannot be provided during inference, further limiting its practical utility in dynamic and interactive applications. In this paper, we introduce \textsc{ReFeed}, a novel pipeline designed to enhance LLMs by providing automatic retrieval feedback in a plug-and-play framework without the need for expensive fine-tuning. \textsc{ReFeed} first generates initial outputs, then utilizes a retrieval model to acquire relevant information from large document collections, and finally incorporates the retrieved information into the in-context demonstration for output refinement, thereby addressing the limitations of LLMs in a more efficient and cost-effective manner.
Experiments on four knowledge-intensive benchmark datasets demonstrate our proposed \textsc{ReFeed} could improve over +6.0\% under zero-shot setting and +2.5\% under few-shot setting, compared to baselines without using retrieval feedback.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose to leverage the outputs of LLMs (i.e., the generated initial answers) to retrieve relevant documents for refining LLM outputs and quality. They also present two modules to enhance the performance by diversifying retrieval feedback and ensembling initial and post-feedback outputs. Experiments are conducted on several conventional QA benchmark datasets. The experimental results demonstrate the proposed method can improve the performance of different LLMs in both close- and open-book settings. The authors also conducted some ablation studies to show the effectiveness of each component.

### Strengths
* S1: The proposed framework is an easy-to-use and plug-and-play blackbox retrieval-augment approach.
* S2: The improvements over baseline methods are significant across different datasets and settings.
* S3: Each proposed component is validated through the ablation study

### Weaknesses
 * W1: Some important details are missing, e.g., how to conduct de-duplication; 
* W2: Not applied to the state-of-the-art LLMs (e.g., GPT-4).
* W3:Lack of discussions and analysis on how hyper-parameters affect the performance.

### Questions
* Q1: Following W1, I would encourage the authors to describe the methods with details and motivation, especially when each component is shown effective individually. For instance, I wonder how the de-duplication is done to ensure diversity; and why BM25 is chosen instead of other retrieval methods (of course not just answering "other methods also just used it").

*Q2: Following W2, I would really like to know how the proposed method can be applied to state-of-the-art models like GPT-4. Although it might not be reproducible for a certain metric number, it can still give some signs about the performance upper bound. Similarly, I wonder if the method can be applied to a conventional smaller neural language model (e.g., BART and T5) since the proposed is a plug-and-play method.

*Q3: Following W3, there are still several hyper-parameters (e.g., k in the module-1) in the proposed method. I wonder how they affect the performance (instead of "because other papers use this number").

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses factualness in QA systems. The idea of REFEED is as follow: 1) generate an output, 2) use retrieve relevant information from large document collections. 3) Integrate the latter into the prompt and refine the answer. The pipeline is plug-and-play and does not require any fine-tuning. The overall approach is more efficient and cost-effective than human feedback.

More in depths, REFEED generates multiple diverse outputs. For each, REFEED uses retrieval conditioned on the input and output instead of the input only, which makes it different than standard RAG approaches. The retriever (e.g., BM25) identifies the top-k relevant documents and remove duplicates. During refinement, the retrieved documents are integrated into the prompt along the outputs. However, there is a likelihood that the retrieved documents are misaligned with the output. The authors circumvent this problem by taking the average language modeling probability to rank the generated outputs before and after incorporating the retrieved documents. Then by comparing the different, the authors pick the first or refined output.

The experiments are based on single-hop QA, TriviaQA, multi-hop QA, and WoW. The models used are davinci-002 and davinci-003. The baselines are fair. The performance in the zero/few-shot experiments are convincing. The ablation study highlights the necessity of the multiple-output generation and the ensemble proposed to identify whether a refined output is better. Finally, the authors show how their approach can be integrated into chain-of-prompt and even improved the results.

Overall, this is a good paper, well written and structured. The idea, while simple, is novel. My only concern would be whether the proposed approach would work for other models than davinci-002/3 (see also related question regarding the calibration). I would ask the authors to experiment with one or two others LLMs (e.g., T5).

POST-REBUTTAL: Thank you for your answers. I will keep my current rating.

### Strengths
- Simple but effective method
- Strong results

### Weaknesses
 - It is unclear whether the proposed approach would work with another backbone than davinci
- I'm skeptical that taking average probabilities of the output before and after the refinement would work in all models

### Questions
- How would verify that the LLM is well-calibrated in order to decide whether a refinement is more plausible or not? If the model is not well-calibrated, how would you proceed?
- How would the approach generalize for other models than davinci?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents ReFeed, a retrieve-then-read pipeline for knowledge-intensive tasks. This pipeline involves three processes: generate the initial output only given the question, retrieve supporting documents using the question and the initial output, and finally refine the previous output. The authors further propose two enhancements: diversifying retrieval feedbacks and ensembling initial and post-feedback outputs.

### Strengths
The proposed method is straightforward and effective.

### Weaknesses
 - The paper's novelty is in question, as the process of using an initial output for retrieval and then refining it does not appear to be a novel approach, and the absence of citation to related work, such as [1], raises concerns. Additionally, the paper lacks in-depth insights into the understanding of retrieve-then-read pipelines. The paper altogether seems more like a system report that shows the effectiveness of each trick, not an academic research.
- Typos
    - In Section 4.3.1, the second paragraph contains several sentences that are missing the subject.
    - In Section 4.3.2, the paragraph labeled "Module-1 …" mentions "as shown in 4", which should be corrected to "as shown in Figure 4”.

### Questions
How are the two enhanced modules integrated together?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel pipeline, REFEED, to provide LLMs with automatic retrieval feedback in a plug-and-play manner, without the need of expensive fine-tuning.
REFEED includes advanced modules to improve the proposed pipeline, specifically diversifying the initial generation outputs and ensembling initial and post-feedback outputs.
That is, REFEED first generates initial outputs, then utilizes a retrieval model to acquire relevant information from large document collections. 
Then, the retrieved information is incorporated into the in-context demonstration to refine the initial outputs, which is more efficient and cost-effective than human feedback or fine-tuning.

### Strengths
* REFEED is simple architecture that improves large language model in a plug-and-play framework. 
* This architecture and a retrieval method allows REFEED a practical and efficient solution without the need for expensive fine-tuning.
* To produce more reliable and accurate answers and mitigate the risk of misleading retrieval feedback, REFEED has equipped with two newly introduced modules, diverse answer generation and an ensemble approach.

### Weaknesses
 * While REFEED looks promising approach to improve large language model in a plug-and-play framework, 
its goals are not specifically clarified.
Because of the wide range of goals, it is necessary to compare and discuss with other approaches, such Prompt tuning, Chain-of-Thought (CoT), Tree of Thoughts (ToT), and, Retrieval Augmented Generation (RAG) have not been described.
Figure 1, 2, and 3 can be interpreted as a kind of RAG.
* Backbone language models are limited, and it is difficult to determine whether the effect is due to the approches or the emergent nature of the language model.
* Reproducibility, limitations, and lack of qualitative evaluation do not confirm its validity. Table 1 is inadequate because the settings are not clear.

### Questions
* Pease explian why you chose text-davinci-003 and Code-Davinci-002 (Codex) as the backbone language models?
* Can REFEED avoid generating incorrect or hallucinated information?
* See Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
