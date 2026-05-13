# Understanding the Role of LLMs in Multimodal Evaluation Benchmarks

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
The rapid advancement of Multimodal Large Language Models (MLLMs) has been accompanied by the development of various benchmarks to evaluate their capabilities. 
However, the true nature of these evaluations and the extent to which they assess multimodal reasoning versus merely leveraging the underlying Large Language Model (LLM) backbone remain unclear.
This paper presents a comprehensive investigation into the role of LLM backbones in MLLM evaluation, focusing on two critical aspects: the degree to which current benchmarks truly assess multimodal reasoning and the influence of LLM prior knowledge on performance. Specifically, we introduce a modified evaluation protocol to disentangle the contributions of the LLM backbone from multimodal integration, and an automatic knowledge identification technique for diagnosing whether LLMs equip the necessary knowledge for corresponding multimodal questions.
Our study encompasses four diverse MLLM benchmarks and eight state-of-the-art MLLMs. Key findings reveal that some benchmarks allow high performance even without visual inputs and up to 50\% of error rates can be attributed to insufficient world knowledge in the LLM backbone, indicating a heavy reliance on language capabilities.
To address knowledge deficiencies, we propose a knowledge augmentation pipeline that achieves significant performance gains, with improvements of up to 60\% on certain datasets, resulting in a approximately 4x increase in performance.
Our work provides crucial insights into the role of the LLM backbone in MLLMs, and highlights the need for more nuanced benchmarking approaches.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an examination of issues within multi-modal evaluation from two aspects:

	1.	To what extent answers rely solely on textual information
	2.	How much external knowledge can boost the performance of multimodal questions

The paper finds that in some current benchmarks, up to 50% of questions can be solved using only textual queries. The authors introduce a retrieval-augmented generation (RAG) method to improve the language model’s performance.

### Strengths
The idea is intuitive and easy to understand.

### Weaknesses
The issue that multimodal questions can often be solved with textual queries alone is not new; many prior works either study or are motivated by this observation (e.g., [1,2]). The paper lacks a more extensive discussion of related works that have studied this phenomenon.
* Equation 3 is confusing. From an intuitive standpoint, it doesn’t seem to hold because: 1) even without the correct knowledge, the model may still provide the correct answer, and 2) in many cases, explicit knowledge is not required (e.g., inferring relative distances between two objects in an image), so such decomposition may not apply.
* It's expected that additional information retrieved by RAG should boost the performance. It would be beneficial to discuss when RAG provides the most advantage. For instance, what types of VQA questions benefit most from RAG, and under what conditions does it perform best?
* It would be nice to provide some results on the OK-VQA dataset as well, as it also requires external knowledge which should benefit from rag.

### Questions
1. In Section 3.3, Table 2, how do you conclude that the performance cap is due to insufficient knowledge? Could it not also be attributed to limited reasoning capabilities, among other factors?
2. Additionally, the writing and notation used in the paper are unclear and need improvement, e.g.
* The connection between some proposed concepts is unclear. There is a missing link between the sections “IS VISUAL CAPABILITY NECESSARY?” and “DO MLLMS HAVE SUFFICIENT PRIOR KNOWLEDGE.”
* The indicator function $\mathbb{1}\left[ P(I, Q) \sim K \right]$ lacks a clear definition of its true conditions. The notation is poorly defined, as  $P(I, Q) \sim K$  is usually interpreted as drawing  K  from the joint distribution of  I  and  Q.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the impact of LLM backbones on the evaluation of MLLMs, concentrating on two primary aspects: the extent to which existing benchmarks accurately measure multimodal reasoning, and the effect of LLMs' prior knowledge on performance. The paper introduces several metrics to disentangle visual perception capabilities from language prior knowledge. The study is conducted on four public MLLM benchmarks and eight open-source MLLM models. Furthermore, the authors introduce a RAG pipeline to enhance the performance.

### Strengths
+ Rethinking the impact of the LLM backbone in MLLM evaluation is insightful and may advance the development of MLLM.
+ The paper is generally easy to read and follow.
+ The introduced metrics and RAG pipeline are sound.

### Weaknesses
 - W1. The author's investigation into image-agnostic questions within MLLM benchmarks confirms findings from previous research [1]. Although this analysis provides a more in-depth view, the results that some benchmarks allow high performance without image inputs are not unexpected. Similarly, it is widely recognized that an MLLM’s performance depends on LLM knowledge capacity and generally improves with LLM’s size. Therefore, the finding that “many error rates can be attributed to insufficient LLM capabilities” is not surprising.


- W2. It would be beneficial to propose how to construct the image-dependent questions. For example, this paper could create a benchmark from existing datasets that requires the use of visual information to answer the questions correctly. It would be more beneficial to the community if such a benchmark could be created along with Analysis.

- W3. The evaluation dataset is not new. I would like to know how the proposed metric works on a more recent dataset such as MMStar [1].  MMStar consists of image-dependent questions. Therefore if new issues are identified using the analysis tools in this study, new findings can be given in terms of how to create image-dependent problems. 


- W4. The solution for the LLM's knowledge lacking is also just using RAGs, so there is limited novelty.

### Questions
Please see the Weaknesses.

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
4

### Summary
This paper investigates the role of LLM backbones for MLLM in the perspective of which current benchmarks truly evaluate multimodal reasoning and the effect of LLM prior knowledge.  To achieve this, this paper introduces a modified evaluation protocol to elucidate the contribution of the LLM's backbone and an automatic knowledge identification technique to diagnose whether the LLM has the necessary knowledge for the question. This paper reveals that some benchmarks allow high performance without image inputs and many error rates can be attributed to insufficient LLM capabilities. Furthermore, this paper proposes a RAG pipeline for knowledge-based VQA tasks.

### Strengths
- S1. The analysis of the contribution of the Language side in MLLM is of great community interest and is one of the key topics


- S2. Incorporating metrics such as SR, GR, SuRD, and NeRD enables more detailed analysis. It will be an important analytical tool.

### Weaknesses
 - The analysis of visual capability necessity was already studied in the literature (as also noted by the authors), leaving only the second discovery (i.e., more language knowledge implies better multimodal performance) as the main discovery of the work. Moreover, one could argue that this second point is somewhat intuitive and is more of a confirmation of it.
- The work acknowledges using only a subset of the MMMU benchmark due to limitations in the models' support for multi-image input and the complexity of converting certain questions into corresponding knowledge reasoning tasks.
- Experiments regarding different retrieval approaches are missing, e.g., using different retrieval approaches and potentially exploiting multi-modal information.

### Questions
The role of LLM in MLLM is a very important topic, and this paper provides an analytical tool on that topic. On the other hand, as noted in Weakness, what this paper examines is merely a more comprehensive examination of what is already known, and the findings are not surprising.

I would like to know why existing evaluations are not enough and what are the novel findings through this analysis. And, also, I would like to know what would the results be if the author used newer benchmarks for evaluation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the contribution of language models in multi-modal evaluation benchmarks. The authors aim to quantify the importance of language in the performance on such datasets in two ways: (i) quantify shortcut reasoning (i.e., how much these models look at the image/how many of these questions do not require image understanding), and (ii) quantify the role of prior knowledge in answering these questions (i.e., understand whether more knowledgeable backbones provides better performance). The authors select four benchmark datasets and eight models to investigate these two aspects. As for prior works, they confirm that language models tend to exploit shortcuts, i.e., do not always use visual information to answer. Moreover, they discovered that the performance on the selected benchmarks heavily depends on prior knowledge of the language model.

### Strengths
- The work is well-presented and motivated, and the writing is clear.
- The experiments cover four multi-modal datasets and eight multimodal language models.
- The authors introduced some changes to previous evaluation protocols (i.e., options shuffling, open-ended conversion) to minimize biases.
- The two main discoveries present valuable insights into how to design new benchmarks and what to focus on when training multi-modal language models.

### Weaknesses
- The analysis of visual capability necessity was already studied in the literature (as also noted by the authors), leaving only the second discovery (i.e., more language knowledge implies better multimodal performance) as the main discovery of the work. Moreover, one could argue that this second point is somewhat intuitive and is more of a confirmation of it.
- The work acknowledges using only a subset of the MMMU benchmark due to limitations in the models' support for multi-image input and the complexity of converting certain questions into corresponding knowledge reasoning tasks.
- Experiments regarding different retrieval approaches are missing, e.g., using different retrieval approaches and potentially exploiting multi-modal information.

### Questions
- As I am not fully convinced of the novelty of this work, I would like to ask the authors how their discoveries regarding the necessity of visual information differ from prior works.
- Moreover, I would like to ask the authors whether one could infer the second discovery by evaluating the performance of different pre-trained language models with vision capabilities at different scales (e.g., LLAMA 7B, 30B, etc) without relying on retrieval.
- I expect that adding vision to a language model after pretraining shouldn't diminish its existing knowledge. This means we could evaluate the sufficiency of prior language knowledge for multimodal tasks as if they were language-only tasks. I ask the authors to discuss this and include tables linking knowledge sufficiency results from multimodal benchmarks to language model performance on language tasks, i.e., for models adding vision post-pretraining, report their performance on language benchmarks, and check for correlations between them and multimodal knowledge sufficiency.

### Soundness
2

### Presentation
3

### Contribution
2
