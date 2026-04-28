# LLM Table Reading: Bridging the Semantic Gap Between Text and Table

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
The rise of Large Language Models (LLMs) has revolutionized numerous domains, yet these models still exhibit weakness in understanding structured tabular data.
Although a larger context window of next-generation LLMs promises them to accommodate a larger volume of table contents, it does not inherently improve the model's capability to understand the underlying structure and semantics of tabular data.
To bridge the semantic gap between **T**ext and **T**able caused by structural variance, we propose TNT, a table-language model that features multi-modal table representations to empower LLMs to effectively and efficiently abstract structure-enriched semantics from tabular data. 
TNT also introduces a scalable and efficient training pipeline, featuring novel self-supervised learning tasks, to integrate abstract tabular knowledge into the language modality.
Extensive experimental results on the most iconic table understanding task of NL2SQL demonstrate a (much) better table understanding of TNT, which achieves up to **14.4%** higher execution accuracy compared with traditional text-based table serialization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new module for LLMs to better understand the tabular data. The new module, TNT, is inspired by the multi-modal LLMs and encodes the tabular information through a BERT-size encoder. The encoded dense features will be transformed by an adapter and then be inserted during the decoding stage of LLMs. 

When building the whole pipeline, TNT first pre-trains the encoder and then trains the encoder and the LLM together in an alignment task. Finally, it conducts instruction-tuning for the specific tasks.

The performance on NL2SQL improves remarkably with the newly proposed method.

### Strengths
1. Table understanding is important to LLMs. And it is vital to find an efficient and effective way to enable LLMs to understand the information represented in the tabular structure.
2. The proposed method can potentially solve really huge tables regardless of the context size.
3. The whole training pipeline is well explained and is inspiring to related work.

### Weaknesses
 - The authors only conduct their experiments on three datasets, all focused on text-to-SQL, which extremely limits the scope of this paper, which undermines their claim in the title as `bridging the semantic gap between text and table`. To be more specific, the authors could have conducted their experiments on more datasets from table QA, table-to-text datasets, etc. Even in the domain of text-to-SQL, they do not conduct any experiments on BIRD benchmark.
- The performance improvement is not significant compared to the SFT baseline. For instance, in Table-2, Llama-3-8B-Instruct achieves 73.0 on Dev while TNT achieves 73.2. This holds for test and other models as well, the improvements are around 0.2, 0.7, 0.6, etc., which makes me wonder whether the improvement indeed is significant.
- The overall performance on Spider is low compared to the state-of-the-art method. On the Spider leaderboard: https://yale-lily.github.io/spider, the best performed method is 91.2 on test set. Even consider the fact that the authors are using the 8B model, the RESDSQL-3B + NatSQL [1], which is a 3B method, achieves 79.9 on the test set, higher than the number reported in the paper (79.0). In addition, RESDSQL-3B + NatSQL came out in 2023.

### Questions
I am curious to see the performance of TNT over tables of different sizes compared with baselines. This will better support the claim that a longer context may not perfectly solve the table understanding by LLMs.

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
4

### Summary
The paper proposes TNT, a multi-modal inspired, efficient training pipeline for structure-enriched table semantics learning, given the current limitations of LLMs in understanding structured data. The proposed method shows improved performance on NL2SQL tasks.

### Strengths
1. The proposed technique is built upon three pressing challenges of tabular data understanding: the structural information, the varying sizes, and generalize across tables. The proposed TnT method consists of modules that target corresponding modules, such as table encoder and abstract table representation. 

2. The training objectives, especially the “multi-task feature alignment” covers potential usage for multiple common table-related tasks, which presumably enhances task generality in downstream.

### Weaknesses
1. Lack of baseline comparison: There have been some efforts in training a general table-oriented LM, such as TableGPT and TableLLaMa. Particularly, it would be informative to compare TableLLaMa as a baseline, to the LLaMa version of TNT method proposed. Currently the baselines are purly out-of-the-box model checkpoints and two training variants (SFT and TNT), so it is kind of obvious that further training would bring increases. Adding additional baselines (such as TableLlama) to prove the effectiveness of the proposed training  recipe would be informative.

2. Lack of table tasks: the only evaluated task is NL2SQL. However, to prove that the proposed model is general across tabular-related tasks, it is highly recommended to evaluate a series of most common tabular tasks, such as table fact verification, table-based analysis generation, and table-based question answering. Particularly because the proposed method TNT claims to apply to bi-directional table structures, it would be helpful to actually test on some benchmarks that features bi-directional tables, such as HiTab and AIT-QA.

### Questions
1. What is the unique importance of the “column-wise contrastive learning” task? Previous pre-training have tackled objectives at varied granular levels, such as table-level, row-level, sub-table level, cell level; what make the column-wise objective stand out in this work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a so-called TNT model, which comprises three major components, a table encoder similar to the image encoder that encodes the table; a table-language adaptor, which maps the representations from the table encoder to LLM's textual space; and the standard LLM decoder.
To train these components, the paper conducts encoder pre-training, table-language feature alignment, and instruction tuning.
The authors conduct experiments on three text-to-SQL datasets, including Spider, Spider-DK, and Spider-Realistic (the latter two are variants built upon the standard Spider dataset).
The authors have improved the performance compared to the standard supervised fine-tuning on the three datasets and conducted ablation studies.

### Strengths
- There seems to be lots of training efforts done by the authors, as they need to pre-train the encoder, align it with the decoder and instruction-tune the model.
- There is some improvement compared to the standard supervised fine-tuning on these datasets.
- There are ablation studies conducted to help understand the contributions of each component.

### Weaknesses
- The authors only conduct their experiments on three datasets, all focused on text-to-SQL, which extremely limits the scope of this paper, which undermines their claim in the title as `bridging the semantic gap between text and table`. To be more specific, the authors could have conducted their experiments on more datasets from table QA, table-to-text datasets, etc. Even in the domain of text-to-SQL, they do not conduct any experiments on BIRD benchmark.
- The performance improvement is not significant compared to the SFT baseline. For instance, in Table-2, Llama-3-8B-Instruct achieves 73.0 on Dev while TNT achieves 73.2. This holds for test and other models as well, the improvements are around 0.2, 0.7, 0.6, etc., which makes me wonder whether the improvement indeed is significant.
- The overall performance on Spider is low compared to the state-of-the-art method. On the Spider leaderboard: https://yale-lily.github.io/spider, the best performed method is 91.2 on test set. Even consider the fact that the authors are using the 8B model, the RESDSQL-3B + NatSQL [1], which is a 3B method, achieves 79.9 on the test set, higher than the number reported in the paper (79.0). In addition, RESDSQL-3B + NatSQL came out in 2023.

## References
[1] Li, Haoyang, et al. "Resdsql: Decoupling schema linking and skeleton parsing for text-to-sql." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 11. 2023.

### Questions
- Why do you limit your studies to text-to-SQL datasets, especially the Spider dataset and its variants? How does TNT perform on other table-related tasks? 
- Why do you claim `bridging the semantic gap between text and table` in your title? Do you consider it as an over-claim considering the scope of your experiments?
- Have you checked the performance listed on Spider leaderboard and include those papers in the related works section?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper discusses the limitations of Large Language Models (LLMs) in processing structured tabular data, highlighting that broader context windows in next-generation LLMs do not necessarily enhance their capability to comprehend the structural and semantic aspects of tables. To address this gap, the authors introduce TNT, a table-language model designed to integrate the structural information of tables into LLMs. TNT features a robust and scalable training framework, employing contrastive learning to merge tabular data knowledge with linguistic modalities efficiently. The efficacy of TNT is especially showcased through its performance on the NL2SQL task, where it significantly outperforms traditional text-based table serialization methods, achieving up to 14.4% higher execution accuracy.

### Strengths
* The idea of treating tabular inputs as a distinct modality is interesting, however, it may somehow be overlapped with conventional text features encoding since the majority of tables are plain text, and the only difference is that tabular data has structure which may inherently be unaligned with the current autoregressive nature of LLMs.
* The motivation for addressing non-semantic column names is sound, although I have concerns about whether these ambiguity issues can be easily resolved by adding schemas or by retrieving relevant documents as supplementary information in LLMs' inference stage.
* The paper is well-written and easy to follow.

### Weaknesses
W1: I suggest you rephrase the InfoNCE loss mentioned in Section 4.1 and Figure 4 in case not all readers are familiar with contrastive learning.

W2: The performance of the proposed TNT seems to be limited, especially when considering the leaderboard of Spider (https://yale-lily.github.io/spider). It seems like when equipping GPT-3.5 with chain-of-thoughts or self-consistency can already achieve quite similar or even better performance than the proposed TNT. If so, the major benefits of TNT is that it can support the non-semantic column names; however, maybe this can be easily solved by adding schemas or by retrieving relevant documents as supplementary information. And I also have concerns whether this can be easily solved with more advanced models using inference like GPT-4 or O1 models as well.

Several relevant papers should be included in the references:

* Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding (https://arxiv.org/abs/2401.04398)
* TAP4LLM: Table Provider on Sampling, Augmenting, and Packing Semi-structured Data for Large Language Model Reasoning (https://arxiv.org/abs/2312.09039)
* StructGPT: A General Framework for Large Language Models to Reason over Structured Data (https://arxiv.org/abs/2305.09645)
* Large Language Models are Versatile Decomposers: Decompose Evidence and Questions for Table-based Reasoning (https://arxiv.org/abs/2301.13808)

### Questions
Q1: What is the metric used in Figure 1 (what does Ex(%) refer to?) and what do set1 and set2 refer to?

Q2: For the contrastive learning, it's not very clear how the positive and negative pairs are collected. I'm thinking whether you mean that (1) you first sample two snapshots $S_i$ and $S_i^{'}$ using random row sampling, then for each snapshot, you calculate the embeddings for each column, for example denoted as $c_j$ and $c_j^{'}$, and then you consider the positive pair as ($c_j$, $c_j^{'}$) if they share the same column, and consider the pair of $c_j$ with other column embeddings as negative pairs?

Q3: Perhaps a question of rigor. I'm curious about whether the proposed method can be applied to some more challenging tasks like HiTab, which are hierarchical tables. It seems the proposed column-based contrastive learning cannot be simply applied to hierarchical tables.

Q4: What are the datasets used for instruction-tuning mentioned in Section 4.3?

Q5: What are the distributions of the datasets you used for pre-training? It seems the portion of anonymized column prediction samples is quite relevant to why TNT performs better on non-semantic versions of datasets.

Q6: What does "original" refer to in Table 2? Does it mean few-shot inference or some other prompting methodologies? This question is critical since I refer to the leaderboard of Spider (https://yale-lily.github.io/spider). It seems like when equipping GPT-3.5 with chain-of-thoughts or self-consistency, it can already achieve quite similar or even better performance than the proposed TNT. If so, the major benefits of TNT is that it can support non-semantic column names; however, maybe this can be easily solved by adding schemas or retrieving relevant documents as supplementary information. And I also have concerns whether this can be easily solved with more advanced models using inference like GPT-4 or O1 models as well.

Q7: For Table 3, it's puzzling why the performance trends on the development set do not match those on the test set. For example, when only instruction tuning (IT) is used, omitting column embeddings, the scores are 31.7 on the dev set versus 50.5 on the test set. However, when both feature alignment (FA) and IT are applied, the performance is nearly the same on the dev set at 31.9 but improves to 53.4 on the test set.

Q8: For the hybrid table representation mentioned in line 210, is there any ablation study? Is "dtype" an essential property for LM understanding, especially for the NL2SQL task?

### Soundness
3

### Presentation
3

### Contribution
2
