# Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction

- Decision: Accept
- Scores: 5, 6, 6, 6, 6

## Abstract
Despite recent progress in Retrieval-Augmented Generation (RAG) achieved by large language models (LLMs), retrievers often recall uncorrelated documents, regarded as "noise" during subsequent text generation. To address this, some methods train LLMs to distinguish between relevant and irrelevant documents using labeled data, enabling them to select the most likely relevant ones as context. However, they remain sensitive to noise, as LLMs can easily make mistakes when the selected document is noisy. Some approaches increase the number of referenced documents and train LLMs to perform stepwise reasoning when presented with multiple documents. Unfortunately, these methods rely on extensive and diverse annotations to ensure generalization, which is both challenging and costly. In this paper, we propose **Backtracking Correction** to address these limitations. Specifically, we reformulate stepwise RAG into a multi-step decision-making process. Starting from the final step, we optimize the model through error sampling and self-correction, and then backtrack to the previous state iteratively. In this way, the model's learning scheme follows an easy-to-hard progression: as the target state moves forward, the context space decreases while the decision space increases. Experimental results demonstrate that **Backtracking Correction** enhances LLMs' ability to make complex multi-step assessments, improving the robustness of RAG in dealing with noisy documents.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Backtracking Correction (BC), a novel approach for training large language models (LLMs) to detect noisy retrieved documents.

Backtracking Correction reformulates the task as a multi-step decision-making process, optimizing the model by iteratively correcting errors from the final reasoning steps back to the initial steps, thereby improving the model's ability to assess the relevance of retrieved documents and enhance the robustness of RAG against noisy inputs. 

Experimental evaluations on multiple open-domain question-answering datasets demonstrate that Backtracking Correction outperforms multiple baselines without relying on additional data or extensive annotations.

### Strengths
+  The proposed Backtracking Correction method offers a novel approach to training LLMs for RAG tasks without relying on extensive external annotations, which could potentially reduce the cost and complexity of developing such systems.

### Weaknesses
 + The paper needs additional ablation studies and analysis for the proposed algorithm, especially for the efficiency claim and the scaling problem in term of chain length.
+ The experimental results are not consistently significant, with three out of four benchmarks (excluding SQuAD) showing either comparable performance or underperformance relative to baselines.

### Questions
+ Does BC implied a conditional depedency between the relevancy of the retrieved documents?
+ Could you provide the exact performance numbers for figure 3?
+ Could you include an efficiency analysis comparing the BC method to the baselines?
+ In section 4.2, the author claim that BC does not use extra data or annotations. Can you elaborate. Is BS's backbone trained from scratch? Does the training process of BC still require label of the reasoning chain as training data?
+ Can you elaborate on the learned ability of "summarizing the consistent or conflicting points" from BC?
+ Can you elaborate on the following claim that "the training data and reference models in Backtracking Correction are dynamic, while those in DPO are static"?

### Soundness
3

### Presentation
2

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
In the RAG setting, it is sometimes required to distinguish whether each document is relevant or irrelevant, and stepwise reasoning may be utilized for this purpose. However, training an LLM for this task poses challenges such as the need for extensive annotation. This paper proposes Backtracking Correction, which reformulates the stepwise reasoning of RAG as a decision process for each document. It separates the decision process of the multiple documents into context space (given the correct decision) and decision space (model output) starting from the final state, enabling an easy-to-hard progression.

### Strengths
- It is very well-written, and the figures are well-illustrated, making it easy to follow.
- A well-defined problem with a reasonable proposed method.

### Weaknesses
There are some concerns with the experimental setup.
- Fair comparison with baselines: Why weren’t the base models of Backtracking Correction (LL2-7B-base, LL3-8B-base) used as baselines? Non-chat base models could also have been fine-tuned. Including the base models in the baseline or incorporating chat models into Backtracking would ensure a fair comparison.
- "Without relying on additional data or annotations." Lines 411-416 mention that competitive performance can be achieved without additional training data (e.g., chat models). However, the model used to obtain the original annotation itself is a chat model. Is there a reason why the model used for SCS original annotation (line 326) and the backbone model were set differently?
- (Very minor) There is a typo "err" in the abstract, and it does not match the abstract on OpenReview.

### Questions
- Please refer to the mentioned weaknesses.
- Also, as the number of documents increases, the binary decision tree is likely to grow very rapidly. Is there a way to sample better paths without considering all paths in the decision space during training?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an interesting Backtracking Correction method to enhance LLMs' capability on RAG QA. Specifically, they employ Self-play algorithm to correct LLM's own CoT errors in a backward manner, and leverage the reward difference between the corrected and original outputs to train LLMs.  The authors present positive results by comparing their proposed algorithm comparing with Proprietary LLMs, SFT without retrieval, and previous SOTA SFT retrieval methods. An example and some analysis presented to help readers understand how their method work.

### Strengths
1. The idea of the paper is quite interesting in that it leverages the self-play algorithm to produce corrected CoT, which mitigates the lack of annotations problems.
2. The paper is well structured so it is relatively easy to follow despite the complexity (though it can be made clearer - see my comments below).
3. Results are in general in favor of the proposed method and some further analysis presented to help readers understand the improvements.

### Weaknesses
1. The overall structure of the paper is clear. However, some important details are missing.
- I think some notations are not clearly defined. For example, in Section 3.3, what exactly are $\Pi_{ref}$ and $o_t^-$?
- In Eq. 6, there appears to be inputs and outputs after the chain of equations, what are those? If this is an iterative process, I suggest using an actual example to illustrate better.
- Some math derivations are not immediately clear. For example, Eq. 10 and Eq. 12. I suggest the authors to add more details here or use the appendix to elaborate more.

2. Experiments can be more thorough.
- In Table 1 and Figure 3, we could conclude that this methods works for Llama-2-7b models, but does it work for other models? Adding experiments here will make the paper stronger. 
- Similarly, most QA datasets are short-form factoid QA, would this method generalizes to other more complicated RAG-QA tasks, for example: https://arxiv.org/abs/2407.13998?

3. The authors show 1 example in Table 2, which is helpful, but I encourage them to dive deep by analyzing more examples and showing readers exactly how exactly correction of CoT works.

### Questions
- The naming of backtracking is a bit unintuitive. A typical backtracking algorithm starts with T=0, explore all path, and then backtrack. Here you don't have the initial explorations. Have you considered a less confusing name?
- Have you tried to shuffle the order of the documents and try your method there? How would that change the results?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on issues with RAG models having difficulties when encountering irrelevant documents and in particular, in sequential decision making processes where documents are classified as relevant or irrelevant before a final answer is produced. The authors explain issues with existing methods for chain and label based supervised fine tuning and instead propose a backtracking correction method. Overall the paper is well written and, for the most part well presented. 

While the proposed method shows some modest gains, Its hard to determine the full benefits as there is only one comparison of the same model being trained with backtracking vs baselines. It would be informative to see more comparisons of models in the `Fine-tuned w/retrieval `section of table 1 also evaluated using backtracking.  Additionally, it would be useful to see a bit more detail on the experimental setup and some analysis or detail on how much more expensive the backtracking method is to use.

### Strengths
- Overall, the paper is well written, organized, and presented with informative figures
- the presented method demonstrates some gains over baseline methods

### Weaknesses
 - only a single model is shown comparing baseline training methods against the proposed method with modest gains
- evaluation datasets are all fairly old and most certainly appear in the training data of many of the investigated models
- the presentation of sec 3.3 is overly complex and may benefit from some editing, subsections, or the addition of a simple figure

### Questions
- what is the wallclock train time of the different methods?
- does the method improve over baseline training setups for other models? Only llama2 7B is shown in fig 3 but llama3-8b was also trained with backtracking as could many of those found in fine-tuned w/ retrieval section of table 1
- what is the accuracy of relevance /irrelevance classification with different methods? afaict only end-to-end answering performance is shown

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Backtracking Correction, a novel method to enhance RAG by transforming it into a multi-step decision-making process. BC optimizes models through error sampling and self-correction, starting from the final step and backtracking to previous states, simplifying the learning of reasoning chains and improving robustness against noisy documents.

### Strengths
1.BC's backtracking algorithm provides a fresh perspective on training LLMs for RAG, simplifying complex reasoning into manageable steps, which is innovative in the context of handling noisy information in document retrieval.  
2.By eliminating the need for extensive annotations, BC lowers the barrier for training complex LLMs, making it more accessible and cost-effective compared to methods relying on detailed reasoning chain annotations.  
3.The paper demonstrates BC's effectiveness through extensive experiments, showing improved performance over strong baselines, including fine-tuned LLMs and proprietary models, highlighting the practical value of the proposed method.

### Weaknesses
1.The paper lacks an adequate exploration of BC's limitations in processing larger datasets and executing more complex reasoning tasks, like multi-hop reasoning. Including a thorough discussion on these aspects could significantly strengthen the analysis. Specifically, the paper does not explore how the backtracking mechanism scales with an increasing number of documents or the depth of reasoning required for multi-hop questions. This is a critical omission, as the computational cost of backtracking could become prohibitive for large datasets or complex queries. Furthermore, the paper does not provide any analysis of how the performance of BC degrades when the reasoning chain involves multiple steps, which is essential for understanding the practical applicability of the method.
2.While BC is proposed as a simplified approach, the backtracking process might still be computationally expensive, especially for environments with limited resources, which could hinder its adoption. The paper does not provide a detailed analysis of the computational complexity of the backtracking algorithm, nor does it offer any strategies for mitigating the computational overhead. This lack of analysis makes it difficult to assess the practical feasibility of BC in resource-constrained environments. A comparison of the computational cost of BC with other RAG methods would be beneficial.
* The numbering of the equations contains errors, which has resulted in confusion in their citations throughout the paper.

### Questions
1.Could the authors share additional insights into the error analysis of the model, particularly in the context of multi-step reasoning questions? A breakdown of errors by reasoning step or a comparison of error types between BC and baseline methods would be meaningful.   
2.What impact does an increase in the number of documents have on BC's performance? It would be beneficial to see experiments demonstrating how performance metrics change as the number of retrieved documents increases.   
3.Can Backtracking Correction effectively handle extreme cases where all retrieved documents are either highly relevant or entirely irrelevant? Evaluating BC's performance in these scenarios could provide valuable insights.  
4.How does Backtracking Correction manage documents that have ambiguous relevance to the query? Furthermore, what effect does this ambiguity have on the model's final output? A detailed analysis of these cases would enhance the understanding of BC's robustness.

### Soundness
3

### Presentation
3

### Contribution
3
