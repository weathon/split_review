# Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Large language models (LLMs) have demonstrated impressive reasoning abilities, but they still struggle with faithful reasoning due to knowledge gaps and hallucinations. To address these issues, knowledge graphs (KGs) have been utilized to enhance LLM reasoning through their structured knowledge. However, existing KG-enhanced methods, either retrieval-based or agent-based, encounter difficulties in accurately retrieving knowledge and efficiently traversing KGs at scale.
    In this work, we introduce graph-constrained reasoning (\ourmethod), a novel framework that bridges structured knowledge in KGs with unstructured reasoning in LLMs. To eliminate hallucinations, \ourmethod ensures faithful KG-grounded reasoning by integrating KG structure into the LLM decoding process through KG-Trie, a trie-based index that encodes KG reasoning paths. KG-Trie constrains the decoding process, allowing LLMs to directly reason on graphs and generate faithful reasoning paths grounded in KGs. Additionally, \ourmethod leverages a lightweight KG-specialized LLM for graph-constrained reasoning alongside a powerful general LLM for inductive reasoning over multiple reasoning paths, resulting in accurate reasoning with zero reasoning hallucination. Extensive experiments on several KGQA benchmarks demonstrate that \ourmethod achieves state-of-the-art performance and exhibits strong zero-shot generalizability to unseen KGs without additional training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes graph-constrained reasoning (GCR). GCR integrates KG structure into the LLM decoding process through KG-Trie, a trie-based index that encodes KG reasoning paths. It leverages a lightweight KG specialized LLM for graph constrained reasoning alongside a powerful general LLM for inductive reasoning over multiple reasoning paths.

### Strengths
1, The proposed method achieves the 100% faithful reasoning. All the supporting reasoning paths can be found on KGs as shown in Figure 5.

2, The proposed method requires less average LLM tokens and small numbers of LLM calls during inference as shown in Table 2.

### Weaknesses
1, The construction of KG-Trie may be computationally expensive in the pre-processing. Although the inference of the proposed method is efficient, the overhead of the preprocessing seems time-consuming. The BFS in formula 3 extract all 
-length edges around the 
 in the preprocessing stage. In a large graph with millions of entities and edges, this will be expensive. These steps (formula 3-5) need to be done for every entity since we do not know the query entity in advance. In this paper authors choose 
. In multi-hop reasoning on KGs a larger 
 is needed which brings more preprocessing overhead. Can the authors explain the time complexity of preprocessing with both theoretical analysis and empirical results?

2, Missing graph reasoning baselines. In the experiments in Table 1 the graph reasoning baselines are included. However, some SOTA link prediction GNN methods like NBFNet[1] and ULTRA[2] are not in the table. These methods can be applied on Freebase and ConceptNet and should be included.

3, Experiments on more datasets are needed to show the superiority of the proposed method. In Table 1 only two datasets WebQSP and CWQ are included. On CWQ, GCR performs well. However on WebQSP, GCR only shows a small margin over GNN-RAG + RA. In Table 6 only two datasets CSQA and MedQA are includes. And the improvements on MedQA is not signifcant. More experiments on more datasets will make the proposed method more convincing.

### Questions
Please refer to the questions mentioned in the Weaknesses part.

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
4

### Summary
The paper introduces graph-constrained reasoning (GCR), a novel framework that bridges structured knowledge in KGs with unstructured reasoning in LLMs. To eliminate hallucinations, GCR ensures faithful KG-grounded reasoning by integrating KG structure into the LLM decoding process through KG-Trie, a trie-based index that encodes KG reasoning paths.

### Strengths
The approach is interesting. 
The experiments show strong results. The paper is well written though the organization of the approach description can be improved.

### Weaknesses
1. The authors should give some cases in which GCR has a Faithful Reasoning Path and RoG does not. The key reason that GCR outperforms RoG was not fully explained. RoG seems a simplified version of GCR.

2. The tokenizer-level decoding method may lead to entities or relationships that cannot be recognized in KGs, which in turn invalidates the model. Meanwhile, the tokenizer-level decoding will remarkably 
 increase the runtime compared to the methods of the same type (see Table2).

3. Is the definition of faithful reasoning in section 5.2 sound? This definition is a bit broad since some wrong paths can also lead to right answers as many papers point out. 


4. The construction of KG-trie is still time-consuming and takes up space if you want to cover all the questions.

### Questions
1. The motivation for using BFS and Tokenizer in E.4 is not clear. Can use DFS and word-level Tokenizer work?

2. The authors used simple scenarios in their experiments, but is the model as efficient as it claims when there are many candidate paths and it takes multiple hops to reach the target entity?

3. Can the author analyze the reasons for unfaithful reasoning in GCR and give some examples?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Graph-Constrained Reasoning (GCR) that stores KG paths in a Trie structure as constraints to guide the decoding process of LLMs and only generates reasoning paths that are valid in KGs. GCR combines a lightweight KG-specialized LLM for graph-constrained reasoning with a powerful general LLM for inductive reasoning, achieving good performance and zero-shot generalization on various KGQA benchmarks.

### Strengths
1. The motivation is clear and the proposed method is technically sound.

2. The manuscript is well-organized and easy to follow.

3. Extensive experiments have verified the effectiveness of the proposed method.

### Weaknesses
1. Preprocessing all paths appears to be both costly and potentially redundant. Could you discuss the space complexity involved in this process? Additionally, how do you plan to control the length of the reasoning paths to optimize efficiency?

2. Instead of using a Trie to constrain the LLM step by step, what are the implications of performing a post-validation with graph querying for the beam-search paths? How do these two approaches differ in terms of time and space complexity?

3. Given that the proposed method has achieved zero reasoning hallucination, analysing the error cases would provide deeper insights and make the results more convincing. Could you include such an analysis in the discussion?

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a graph-constrained reasoning (GCR) framework to enable LLMs to produce faithful reasoning and reduce hallucinations. The key idea of GCR is to convert vanilla KG into a KG-trie and enable LLMs to perform graph-constrained decoding. Experiments on various KGQA reasoning benchmarks and several LLMs demonstrate the effectiveness of the proposed GCR.

### Strengths
1. The conversion of a KG into KG-trie and the introduction of graph-constrained decoding are reasonable.

2. Extensive experiments on the various KGQA benchmarks demonstrate the effectiveness of GCR.

3. The results of zero-shot generalizability for reasoning on unseen KGs are interesting.

### Weaknesses
1. What is the time cost of the construction of a KG-trie? Furthermore, since the construction of a KG-trie is query-dependent, the offline pre-constructed KG-trie strategy may not be effective when a new input query is introduced. Additionally, the beam search method for constructing a KG-trie may be time-consuming.

2. Real-world KGs are often incomplete and contaminated. Therefore, when entities are absent from the KG or when the reasoning paths generated by Figure 3 (Lines 220-228) contain unreliable logical pathways, how does GCR work? Will GCR still contribute positively to the results under these circumstances?

3. The results of the zero-shot generalizability improvement in Table 6 for MedQA are not particularly significant. I am curious about the additional time cost associated with implementing GCR compared to vanilla ChatGPT and GPT-4o-mini.

4. The authors may want to discuss or summarize more KG-enhanced methods for reducing knowledge  hallucinations including [A, B].

### Questions
1. The reasoning path in a KG-trie may consist of multiple paths. In cases where several valid reasoning paths exist within the KG-trie, how does GCR operate?

2. Given that the knowledge stored in KGs often exhibits redundancy, can we ensure that all generated reasoning paths are strongly relevant to the question posed? Is there a risk of introducing irrelevant information?

3. In line 917, the beam size is set to 10 for graph-constrained decoding. Is the beam size sensitive to graph-constrained reasoning, and if so, what aspects of GCR are influenced by the beam size?

4. If a KG is temporal and dynamic, how can the pre-constructed KG-trie strategy be effectively employed?

### Soundness
2

### Presentation
2

### Contribution
2
