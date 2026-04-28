# Efficient Large Language Models Fine-Tuning on Graphs

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Learning from Text-Attributed Graphs (TAGs) has attracted significant attention due to its wide range of real-world applications. The rapid evolution of large language models (LLMs) has revolutionized the way we process textual data, which indicates a strong potential to replace shallow text embedding generally used in Graph Neural Networks (GNNs). However, we find that existing LLM approaches that exploit text information in graphs suffer from inferior computation and data efficiency. In this work, we introduce a novel and efficient approach for the end-to- end fine-tuning of Large Language Models (LLMs) on TAGs, named LEADING. The proposed approach maintains computation cost and memory overhead comparable to the graph-less fine-tuning of LLMs. Moreover, it transfers the rick knowledge in LLMs to downstream graph learning tasks effectively with limited labeled data in semi-supervised learning. Its superior computation and data efficiency are demonstrated through comprehensive experiments, offering a promising solution for a wide range of LLMs and graph learning tasks on TAGs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discusses

### Strengths
1. The idea of combining implicit GNNs and efficient LMs seems quite interesting and intuitive.
2. The summary of the related in this direction is clear and the author identifies the pain points of the current research in the area.

### Weaknesses
1. The main claim of this paper is on large language models whereas the experiments are conducted on small language models like "BERT" and "DeBERTa". Given the parameter-efficient tuning, it's not that hard to perform experiments on large models such as GPT-2 and Llama-2. 

2. The technical novelty is limited. Caching neighborhoods has been one of the common techniques to speed up GNN-LMs. 

3. Evaluations are limited on node classifications only. Given the limited scope and "old" benchmark on node classification, I don't think the contribution of the proposed idea is significant enough.

### Questions
1. Can this approach used in other applications such as link prediction and graph classification?

2. What's the performance on larger benchmarks like ogbn-mag/obgn-product, especially the computational cost?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research paper suggests an approach to fine-tuning large language models (LLMs) on text-attributed graphs. The main ideas and contributions are as follows;

- Examining the redundancy, in computing (encoding and propagation) when fine-tuning LLMs using graph networks (GNNs) in an end-to-end manner. This analysis uncovers the scalability limitations.
- Presenting an algorithm called LEADING that reduces computation redundancy by decoupling neighbors and implementing graph modeling. This allows for end-to-end training of LLM GNN to supervised LLM fine-tuning without graphs.
- Demonstrates that LEADING is more resourceful in transferring knowledge from LLMs to downstream graph learning tasks compared to existing methods in scenarios with labeling rates.
- Showing that LEADING achieves scalability and efficiency in LLM fine-tuning and significantly outperforms existing iterative or self-supervised methods that combine LLMs and GNNs.
- Providing complexity analysis and empirical evaluations to highlight the efficiency and scalability benefits of LEADING.

In summary, this paper enables end-to-end training of LLM GNN through techniques that decrease computation redundancy. This facilitates the transfer of knowledge from LLMs into graph learning tasks with both efficiency and scalability, in mind.

### Strengths
Importance of the Problem; The paper addresses an issue of tuning Language and Learning Models (LLMs) on graphs, which has implications and challenges, across various domains.

Evaluation of Existing Approaches; The authors conduct an analysis of the limitations in current methods with a particular focus on redundancies in encoding and propagation computations.

Innovative Techniques Proposed; The paper introduces techniques such as neighbor decoupling and implicit graph modeling to overcome the identified limitations. It also presents an approach for training an end to end LLM Graph Neural Network (GNN).

Clear Organization; The paper is well structured and easily comprehensible starting with an introduction followed by a summary of related work.

Clarity and Elaboration; The authors effectively communicate their ideas and techniques using visual aids while providing sufficient algorithmic details.

Experimental Results; Through experiments conducted on datasets the proposed techniques demonstrate advantages, particularly in terms of prediction accuracy when labeled data is limited as well as scalability.

Original Contributions; The analysis of computation redundancies along with the introduced techniques and the end to end training approach are acknowledged as contributions to the field.

Implications; These findings hold implications, for domains that utilize text attributed graphs. They also offer guidance on combining LLMs with GNNs.

### Weaknesses
To better understand the proposed techniques and their impact, on data efficiency it would be beneficial to delve into the underlying mechanisms through analysis or intuition.

In order to fully grasp the importance of the techniques it is advisable to conduct ablation studies that elucidate their individual contributions.

To demonstrate the scalability of the algorithm a comprehensive evaluation on a range of graph structures and larger scale datasets would be advantageous.

In the work section it would be beneficial to provide a comprehensive context by discussing existing approaches for efficient training of Graph Neural Networks (GNNs) and implicit models.

Certain parts of the explanation could benefit from in depth details or intuitive explanations especially when describing how the techniques enhance data efficiency.

By expanding the scope of the ablation study and conducting experiments valuable insights, into these proposed methods can be gained.

The conclusion section should be refined to offer a concise yet comprehensive summary of the findings and takeaways.

### Questions
1. The analysis findings indicate that there is redundancy, in encoding and propagation. It is not clear how neighbor decoupling and implicit modeling specifically contribute to improved knowledge transfer from LLMs. Could you provide some insight or analysis to explain the underlying mechanisms?

2. The ablation study seems to have limitations. It would be beneficial to conduct ablation experiments to assess the individual contributions of neighbor decoupling and implicit modeling towards the observed improvements.

3. Have you explored graphs or additional datasets beyond those that were tested? Conducting experiments on a larger scale could highlight the scalability benefits more effectively.

4. It would be advantageous to expand upon the work section by discussing approaches such as sampling methods for GNN training and explicit models like Neural ODE/DEQ providing more context and motivation for the techniques employed in your research.

5. Some sections of the paper lack sufficient details. For instance the explanation of how your techniques reduce redundancy can be vague at times. Providing details or intuitive explanations would enhance comprehension.

6. The conclusion feels somewhat abrupt. Please summarize the takeaways and contributions clearly for readers well as discussing potential future directions beyond integration, with PEFT.

7. To further strengthen the paper consider expanding the ablation study incorporating references to work conducting large scale experiments and providing additional intuition and details where necessary.

### Soundness
2 fair

### Presentation
2 fair

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
This paper introduces an efficient approach for end-to-end fine-tuning of pre-trained language models (PLMs) on text-attributed graphs (TAGs). The authors argue that existing PLM approaches for TAGs suffer from computation and data efficiency issues, and they propose the LEADING algorithm which maintains computation and memory efficiency similar to graph-less fine-tuning of PLMs. LEADING can effectively transfer rich knowledge to downstream graph learning tasks even with limited labeled data in semi-supervised learning. Experimental results show that LEADING demonstrates superior computation and data efficiency in comparison with existing approaches such as GIANT and GLEM.

### Strengths
+ Generalizing the contextualization power of PLMs to structure-rich text data (e.g., text-attributed graphs) is an important and meaningful task. The goal of improving computation and data efficiency in this task is well-motivated.

+ The ideas of removing encoding redundancy and propagation redundancy, as well as the neighbor decoupling strategy, are intuitive and well-explained.

+ The authors conduct experiments on both small and large graphs and perform comprehensive ablation studies, hyperparameter analyses, and scalability studies.

### Weaknesses
 - This work mainly studies encoder-only PLMs such as BERT and DeBERTa. I do not see how the entire study can be easily generalized to encoder-decoder and decoder-only PLMs from the perspective of either methodologies or evaluation protocols. Therefore, I do not quite agree with the term "Large Language Models" in the title because encoder-only PLMs are usually much smaller than encoder-decoder and decoder-only ones. The study is still a complete one even if only encoder-only PLMs are studied, but the used term somehow overclaims what this study has done.

- Statistical significance tests are missing. It is unclear whether the gaps between LEADING and the baselines are statistically significant or not. In fact, the gaps on arXiv are quite subtle in Table 1, therefore p-values should be reported.

- An important baseline, GraphFormers [1], is cited but not compared.

- The authors only conduct experiments in the semi-supervised node classification task. Besides, all three used datasets are from the academic domain. It is unclear whether the proposed techniques work for other tasks (e.g., link prediction) and other domains (e.g., e-commerce).

### Questions
- Could you conduct statistical significance tests to compare LEADING with the baselines on arXiv?

- Could you report the performance of GraphFormers?

- Could you conduct experiments in other tasks and on graphs from non-academic domains?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies learning from Text-Attributed Graphs (TAGs) using  large language models (LLMs). Specifically, they find that existing LLM approaches that exploit text information in graphs suffer from inferior computation and data efficiency. To address these issues, they propose the LEASUNG fine-tuning algorithm that  not only effectively adapts LLMs to downstream graph learning tasks with limited
labeled data but also exhibits strong scalability and efficiency. Extensive experiments verify the superior performance in terms of both computation and data efficiency.

### Strengths
[+] The manuscript is well-presented. The authors clearly present the motivations, the methods and the experiments.         

[+] The topic of LLMs for graph is trendy and important in graph learning community.            

[+] Extensive experiments are performed to verify the effectiveness in terms of both computation and data efficiency.

### Weaknesses
[-] The proposed method can only work for text-attributed graphs and node classification tasks. However, some recent works have validated that LLMs can process nearly all kinds of graphs and node-level/edge-level/graph-level tasks, which makes the contribution of this work being less significant.          

[-] The performance of the proposed method is not superior. For example, on Cora dataset, the proposed method equpped with LLMs are inferior to the Shallow Embedding.           

[-] The experiments are somewhat limited. Specifically, the authors only evaluate the proposed method in homophilous graphs. I notice that some concurrent works [1,2] in LLMs for graphs report the results on heterophilous graphs. So, how about the performance of the LEADING algorithm perform on heterophilous graphs?            

[-] The authors only use some small and out-of-date language models (BERT and DeBERTa). Why not try more powerful LLMs such as GPT-3.5 and LLaMA [3]?             

[-] The codes for reproducing the results are not provided.

### Questions
1. How about the performance of the LEADING algorithm perform on heterophilous graphs?          

2. Why not try more powerful LLMs such as GPT-3.5 and LLaMA?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
