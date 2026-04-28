# Retrieval-Augmented Editing Generation: Impact of Knowledge Editing and Fine-Tuning on RAG

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3

## Abstract
The knowledge embedded in Large Language Models (LLMs) is static, tied to the time when the training data was collected. 
While Retrieval-Augmented Generation (RAG) methods are widely used to introduce new knowledge, they simply rely on retrieved information for reasoning without integrating it into the model’s parameters. This limits the model's ability for long-term knowledge retention and autonomous learning.
To overcome this, in this work, we propose the \textbf{R}etrieval-\textbf{A}ugmented \textbf{E}diting \textbf{G}eneration (RAEG) framework for open-domain question answering (ODQA) tasks. 
RAEG enhances model generation performance by first editing the retrieved paragraphs to inject necessary knowledge, followed by an augmented generation phase. This dual mechanism—combining knowledge injection and retrieval augmentation—provides complementary advantages in the reasoning process. When the injected knowledge alone is insufficient for accurate generation, the model can rely on the retrieved information to compensate, and conversely, when retrieval yields suboptimal results, the injected knowledge ensures continuity and accuracy in the response. This interplay between internalized and externally sourced knowledge reinforces the model's ability to produce correct answers, thereby enhancing overall task performance.
We explore the impact of two key methods for knowledge injection: Knowledge Editing (KE) and Parameter-Efficient Fine-Tuning (PEFT), and analyze how modifying the model's parameters influences its reasoning abilities and generation outcomes. To further improve RAEG's performance, we introduce a re-ranking mechanism to optimize the integration of external knowledge and apply parameter pruning to mitigate the potential drawbacks of parameter modifications during KE.
Evaluations on two authoritative ODQA benchmarks show that RAEG is able to further replace RAG as a competitive method.
Our data and code will be available at \url{https://github.com/XXX/XXX}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel framework, Retrieval-Augmented Editing Generation (RAEG), aimed at improving open-domain question-answering (ODQA) tasks by integrating knowledge injection techniques—Knowledge Editing (KE) and Parameter-Efficient Fine-Tuning (PEFT)—with traditional Retrieval-Augmented Generation (RAG) methods. The authors also implement re-ranking and parameter pruning mechanisms to enhance the performance of RAEG, demonstrating its effectiveness on authoritative QA datasets.

### Strengths
1. **Writing Quality**: The paper is well-structured and professionally written, with clear sections that effectively present the research problem, methodology, and findings. 

2. **Significant Research Problem**: Addressing the limitations of traditional RAG methods in handling static knowledge through the novel RAEG framework is a meaningful and timely research direction. This problem is central to enhancing large language models’ adaptability in knowledge-intensive tasks.

3. **Practical Value**: The proposed RAEG framework, which integrates knowledge editing and parameter-efficient fine-tuning for ODQA tasks, shows practical potential.

### Weaknesses
1. **Limited Experimental Comparisons with Relevant Algorithms**: The paper does not provide sufficient comparisons with recent, highly relevant algorithms that address similar issues in knowledge retention, factual accuracy, and context awareness. Key algorithms missing from the comparison include:
   - *FastMem: Fast Memorization of Prompt Improves Context Awareness of Large Language Models* (https://arxiv.org/abs/2406.16069)
   - *Trusting Your Evidence: Hallucinate Less with Context-aware Decoding* (https://arxiv.org/abs/2305.14739)
   - *DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models* (https://arxiv.org/abs/2309.03883)  
   
   These methods have shown strong results on datasets such as NQ, and a comparative analysis would provide a more comprehensive understanding of RAEG's effectiveness and positioning among existing approaches.

2. **Lack of Analysis on Computational Complexity and Efficiency**: The paper does not examine the algorithmic or time complexity associated with the proposed framework, particularly regarding the computational impact of added components like re-ranking and parameter pruning. Including an analysis of runtime and resource usage, both with and without these enhancements, would strengthen the practical evaluation by showing how these additions affect overall efficiency, which is critical for large-scale applications.

### Questions
Add experiments and analyses to address the above weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on the open-domain question answering task and proposes a framework called Retrieval-Augmented Editing Generation (RAEG) to combine RAG and knowledge editing for better answer generation. RAEG first injects new knowledge pairs into a language model (LM) and then uses RAG to generate the answer. This paper also conducts numerous empirical experiments to analyze the effects of different methods for incorporating knowledge into LMs (i.e., knowledge editing (KE) and Parameter-Efficient Fine-Tuning (PEFT)). Finally, this paper introduces a re-ranking method and a parameter pruning technique to enhance the performance of RAEG and mitigate the potential negative effects of KE on RAG.

### Strengths
1. The motivation of the paper is interesting. It identifies the limitations of current knowledge editing (KE) and retrieval-augmented generation (RAG) methods and attempts to combine them for improved incorporation of new knowledge into language models (LMs).
2. This paper conducts lots of experiments and ablation studies, providing several interesting empirical findings.

### Weaknesses
1. While the motivation for combining knowledge injection (KE/PEFT) and RAG is sound, the proposed RAEG method lacks originality and heavily relies on previous works, making it somewhat incremental. For example, the authors directly apply MALMEN [1] for KE and LoRA [2] for PEFT. Furthermore, the proposed parameter pruning method is based on RECT [3], and the re-ranking training method is also common and not novel.
2. The combination of knowledge injection (KE/PEFT) and RAG feels shallow, and the writing on the proposed RAEG is quite confusing. If I understand correctly, RAEG first trains a hyper-network to inject knowledge pairs into a language model (LM). These knowledge pairs are extracted by GPT-4 from knowledge paragraphs using prompting, which I assume are retrieved externally. Then, using this edited LM as a generator, RAEG performs standard RAG, retrieving relevant paragraphs based on the query and concatenating them to generate the answer. I find this confusing because if the new knowledge has already been injected into the LM, why is RAG used for retrieval again? Additionally, the results in Table 1 indicate that the performance of KE+RAG and PEFT+RAG is not better than directly using RAG, especially on the TQA datasets.
3. This paper resembles an empirical study, as it conducts numerous experiments and provides several findings. However, most of these findings have already been published in previous works, such as [4][5][6][7].
4. There are no recent state-of-the-art methods included as baselines in the experiments, making the effectiveness of the proposed method unclear.

### Questions
1. I don’t fully understand the motivation behind RAEG or how it works. Please refer to Weaknesses (2) above. If the new knowledge has already been injected into the LM, why is RAG used for retrieval again?
2. Is the synthetic knowledge construction based on the training data?

Typos:

1. L242, datas → data

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the limitations of static knowledge in LLMs and the reliance of current RAG methods on external information without integrating it into model parameters. To enhance long-term knowledge retention and model autonomy, the authors propose the Retrieval-Augmented Editing Generation (RAEG) framework for open-domain question answering. The paper first edits retrieved paragraphs using ChatGPT to inject necessary knowledge and then generates responses with this augmented knowledge.

### Strengths
1. This paper evaluate the effectiveness of different knowledge memory methods, such as Knowledge Editing (KE) and Parameter-Efficient Fine-Tuning (PEFT).
2. The experimental results show that PEFT achieves much better performance than the KE method.

### Weaknesses
1.This paper claims that its motivation is to evaluate the effectiveness of Knowledge Embedding (KE) and Parameter-Efficient Fine-Tuning (PEFT) in the Retrieval-Augmented Generation (RAG) scenario. However, it does not focus on evaluating the knowledge memorization capabilities and general abilities of Large Language Models (LLMs). More experiments can be added following existing work [1].

2. Existing studies have identified knowledge conflict as a key challenge in RAG modeling [1]. This paper should discuss relevant works to clarify the motivation further. It appears that the KE approach does not address the knowledge conflict problem, which suggests it may not enable LLMs to effectively leverage external knowledge.

3. The paper would benefit from a more in-depth analysis of why the KE method fails to utilize external knowledge effectively. Additionally, the reason why the KE method degrades RAG performance remains unclear and should be addressed.

4. Some works have also created RAG fine-tuning datasets [2]. The necessity of using synthesized data in this paper is unclear, and it would be beneficial to compare RA-DIT within the experiments.

5. The experiments lack comprehensiveness. Including datasets like PopQA (which features entities with low frequency) and ASQA (with more complex answers) would provide a more complete basis for the conclusions drawn.

### Questions
1. The quality of synthesized data is not evaluated.
2. The paper can be reorganized. The method part should be more detailed to make the motivation clear.
3. Some case studies should be conducted.

### Soundness
2

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
4

### Summary
This paper addresses the limitations of static knowledge in LLMs by proposing the Retrieval-Augmented Editing Generation (RAEG) framework for open-domain question answering (ODQA). RAEG improves generation performance through a dual mechanism: editing retrieved paragraphs for knowledge injection and using retrieval augmentation to complement the model’s reasoning. By leveraging Knowledge Editing and PEFT, the framework enhances the model's capacity for long-term knowledge retention and accuracy, reinforced by a re-ranking mechanism for optimization.

### Strengths
1. This paper addresses an important problem: how to effectively integrate retrieved paragraphs into the generation process of a model in RAG. Traditional approaches typically rely on context-based methods, where the retrieved paragraphs are directly provided as contextual input for the model to reference during generation. In contrast, this paper introduces a novel approach that departs from the context-based paradigm, proposing a **Knowledge Editing** mechanism to inject the retrieved paragraphs into the model’s parameters, which is novel. (However, the reviewer does not agree with the specific implementation of this work; see the weaknesses section for further details.)


2. This paper thoroughly investigates several design components for KE in the context of RAG, such as pruning, and provides a comparative analysis.

### Weaknesses
1. The reviewer is concerned about the correctness of the proposed method. The proposed method relies on a powerful LLM, i.e., GPT-4-mini, to extract knowledge information from the retrieved paragraphs in question-answer pairs. The knowledge editing step is to inject the information in the QA pairs into the less-powerful LLM, i.e., LLaMA-2. This sounds like distilling the knowledge from GPT-4-mini into LLaMA-2. In this case, the performance upper bound of LLaMA-2 would be the performance of GPT-4-mini by directly performing traditional prompt-RAG. The core issue is that the method's effectiveness is intrinsically tied to the capabilities of the larger model used for knowledge extraction, making it unclear if the gains are from the proposed method or simply from the distillation process. The paper needs to clarify the specific advantages of this approach over directly using the larger model with RAG.

2. The experimental evaluation in this paper is insufficient. Given that the KE process relies on GPT-4-mini, the proposed method should, at a minimum, be compared directly with GPT-4-mini in a RAG setting. This comparison is essential to determine whether the proposed method offers any benefit beyond what can be achieved by using the more powerful model directly. The current evaluation lacks a crucial baseline, making it difficult to assess the true value of the proposed approach.

3. The reviewer is also concerned about the efficiency of the proposed method. Would knowledge editing process be a bottleneck in the RAG process? The authors should report on this. The paper should provide a detailed analysis of the computational cost associated with the knowledge editing process, including the time and resources required for both the knowledge extraction and injection phases. Without this analysis, it is difficult to assess the practical feasibility of the proposed method.

4. Presentation Issues: 
Statement: These issues do not significantly affect my rating of the paper on its originality and significance. However, I would admit that these issues affect my judgement of the maturity of this paper.

    - Misunderstandings: Line 20: `by editing the retrieved paragraphs` sounds like you are going to edit the content of the retrieved paragraphs. I think you mean that you are going to edit the model by injecting the information of the retrieved paragraph.

    - Typos: Line 79, Generatio --> Generation

    - The example in Figure 1 is rather confusing. If the model can solve the posed question by either RAG or knowledge editting, why do we need to involve the knowledge editting step? I would like to know under what circumstances, RAG alone or KE alone cannot solve the question. This should be clearly stated in the paper or at least demonstrated by the example. 

    - The separation between Table 1 and Table 2 makes it hard to compare the results. I would suggest putting them together in one table.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Retrieval-Augmented Editing Generation (RAEG), a dual knowledge-augmented generation mechanism for LLMs that first edits the parametric knowledge given the retrieved documents, and then uses the retrieved documents to augment generation. By using PEFT for editing, RAEG consistently outperforms RAG. The authors further propose to use re-ranking and parameter pruning to improve performance.

### Strengths
This paper proposes a new approach: first injecting knowledge into the LLM, then further augmenting it with retrieved documents. This method effectively combines the strengths of both techniques.

### Weaknesses
 - RAEG requires training or updating the LLM's parameters for each query, including an LLM-powered training data generation phase. This approach is expensive and impractical for real-world applications.
- The authors use two methods to inject knowledge into an LLM: KE and PEFT. These two are not very well named — KE is a broad term, and PEFT is a method for efficient fine-tuning, and the goal of PEFT here is also editing knowledge. It’s impropriate to juxtapose these two terms.
- The authors propose RQ1 and RQ2, providing affirmative answers to both. However, the experimental results don't fully support these conclusions. For RQ1, which investigates whether KE and PEFT can shift the model's reliance from external to internally embedded knowledge, the results fail to demonstrate a clear reliance shift. Regarding RQ2, which examines the impact of knowledge injection on the LLM's original and reasoning abilities, the improved performance of PEFT+RAG over RAG alone doesn't conclusively prove that these abilities remain unaffected. The slight performance decrease of KE+RAG compared to RAG alone further suggests that the knowledge injection via KE may negatively affect the model's original abilities.
- Line 204: It’s not appropriate to cite the InstructGPT paper for gpt-4o-mini.
- See questions.

### Questions
- Line 320: Do the authors set K=1 for all RAG runs including RAEG, or only for the RAG baselines?

### Soundness
2

### Presentation
2

### Contribution
2
