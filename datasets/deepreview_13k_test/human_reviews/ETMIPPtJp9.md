# FiDeLiS: Faithful Reasoning in Large Language Model for Knowledge Graph Question Answering

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Large language models are often challenged by generating erroneous or `hallucinated' responses, especially in complex reasoning tasks.
To mitigate this, we propose a retrieval augmented reasoning method, \ours{}, which enhances knowledge graph question answering by anchoring responses to structured, verifiable reasoning paths. \ours{} uses a keyword-enhanced retrieval mechanism that fetches relevant entities and relations from a vector-based index of KGs to ensure high-recall retrieval. Once these entities and relations are retrieved, our method constructs candidate reasoning paths which are then refined using a stepwise beam search. This ensures that all the paths we create can be confidently linked back to KGs, ensuring they are accurate and reliable.
A distinctive feature of our approach is its blend of natural language planning with beam search to optimize the selection of reasoning paths. Moreover, we redesign the way reasoning paths are scored by transforming this process into a deductive reasoning task, allowing the LLM to assess the validity of the paths through deductive reasoning rather than traditional logit-based scoring. This helps avoid misleading reasoning chains and reduces unnecessary computational demand. Extensive experiments demonstrate that our method, even as a training-free method which has lower computational costs and superior generality, outperforms established strong baselines across three datasets. The code of this paper will be released at \codelink{}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a retrieval augmented reasoning method called FiDeLiS for knowledge graph question answering. The method uses Path-RAG to retrieve relevant entities and relations from KG, and conducts a deductive-reasoning-based beam search to generate multiple reasoning paths leading to final answers. The experiments are conducted on three benchmark KGQA datasets, including WebQuestionSP (WebQSP) , Complex WebQuestions (CWQ) and CR-LT-KGQA, and proves its effectiveness. In addition, the paper also conducts extensive experiments for deep analysis and discussion.

### Strengths
Two components of the proposed method, Path-RAG and Deductive-verification Beam Search, are proven to be effective for KGQA.

Extensive experiments are conducted on three benchmarks, including ablation study, analysis experiments and case study.

### Weaknesses
The novelty of the paper is still limited. Although the paper proposes two useful components including Path-RAG and DVBS for KGQA, and also demonstrates their effectiveness, however, the main method still follows the paradigm of ToG (Think on Graph).

In the experiments, (1) the important hyper-parameters such as beam width and depth are different when comparing the proposed method and ToG, which will make the comparison unfair. The paper sets the default beam width as 4 and depth as 4, but ToG sets them as 3 in their paper. However, the paper doesn’t mention it. According to Figure 2, ToG would obtain higher performance when setting beam width and depth as 4, although it may be still worse than the proposed method. (2) According to the ablation study in Table 2, replacing Path-RAG with ToG would result in substantial performance declines, the performance would be comparable to or even worse than that of ToG. Does that means the improvement of the method mainly relies on Path-RAG?

Some parts of the paper should be made more clear. For example, after Retrieval in Path-RAG, we can obtain entities $E_m$ and relations $R_m$, and then iteratively construct reasoning step candidates to extend the reasoning paths based them. In addition, DVBS is designed to prompt LLMs to iteratively execute beam search on the reasoning step candidates. Thus, are the reasoning step candidates are all from $E_m$ and $R_m$? does beam search only execute on the candidates? 

Some typos and mistakes.

Line 203, two based.

In Figure 2 (d), wrong figure.

In Section 3.4, there is no results for ToG in Table 6, so how to obtain the conclusion that the proposed method shows superior efficiency compared to the ToG.

### Questions
See the weaknesses.

### Soundness
3

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
4

### Summary
This paper introduces FiDeLiS, a retrieval-augmented reasoning framework that enhances LLM performance in KGQA tasks. The framework addresses the challenge of ensuring reliable reasoning by anchoring LLM responses to verifiable reasoning paths within knowledge graphs. FiDeLiS consists of two main components: Path-RAG, which retrieves relevant entities and relations from knowledge graphs using a keyword-enhanced mechanism, and DVBS, which constructs reasoning paths using a combination of natural language planning and beam search. A key innovation is the transformation of path scoring into a deductive reasoning task, moving away from traditional logit-based scoring. Through comprehensive experiments across three datasets, the authors demonstrate that FiDeLiS achieves competitive performance compared to existing baselines while being training-free and computationally efficient. The work contributes to making LLM reasoning more reliable and interpretable in knowledge-intensive tasks.

### Strengths
1. The proposed method effectively addresses the reliability issue in reasoning by ensuring each step in the reasoning path can be traced back to the original KG, providing verifiable and interpretable results.
2. The introduction of deductive reasoning verification mechanism offers an innovative solution to the reasoning termination problem, which has been a significant challenge in existing approaches.

### Weaknesses
1. There are minor writing issues (e.g., redundant "based" in line 203, "questins" misspelling in line 790) that should be addressed.
2. The paper lacks in-depth analysis of why deductive reasoning verification is more suitable for this task compared to traditional logit-based scoring methods. A theoretical or empirical comparison would strengthen this claim.
3. The core assumption in constructing reasoning paths (that earlier timesteps t have reasoning step candidates St with higher semantic similarity to the query, as reflected in Equation 3) needs more thorough analysis. The paper should investigate whether this assumption holds for problems of varying complexity and whether over-reliance on semantic similarity between reasoning steps and queries might lead to errors.

### Questions
- Regarding Algorithm 2, does Path-RAG maintain the same retrieval strategy when obtaining the next possible reasoning step candidates St? Does it incorporate previously formed reasoning steps to aid in retrieval?
- How sensitive is the method to the quality of the knowledge graph? It would be valuable to see an analysis of performance across KGs of varying quality or completeness.
- How does the method handle questions that require commonsense reasoning during the inference process? The current description focuses on constructing reasoning steps from existing KG relations, but real-world questions often require combining structured knowledge with commonsense reasoning.

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
This paper introduces a novel method combining LLMs and KGs, primarily consisting of two modules: Path-RAG and DVBS. Specifically, Path-RAG is responsible for retrieving relevant information from knowledge graphs, while DVBS selects the most promising reasoning paths through beam search. I am pleased to see the experimental performance across three KGQA datasets, where the authors' method shows improvements in both accuracy and efficiency. Additionally, the authors conducted extensive ablation experiments, which enhances the paper's soundness.

### Strengths
- The authors' writing is clear, with well-explained methodology.
- The authors achieved state-of-the-art performance across multiple KGQA datasets, demonstrating consistent performance improvements.

### Weaknesses
(The following weaknesses represent my second version, which incorporates feedback from the Associate Program Chairs)

- The paper's primary contribution appears incremental, as it primarily combines existing retrieval and ranking mechanisms without introducing fundamentally new theoretical insights or technical innovations - the authors should clarify what specific technical advances differentiate their approach from previous retrieval-augmented systems.

- Path-RAG appears to be a complex retrieval mechanism, and given that most entities and relations are connected in the knowledge graph, it's unclear how this approach is beneficial. In my view, Path-RAG might be more useful in cases where entities and relations are not directly connected. However, the paper doesn't address how the system handles multi-hop reasoning chains. Additionally, the scoring function is influenced by $alpha$, but it's unclear how $alpha$ is determined. Only qualitative results seem to be provided.

- The paper only compares with GoT, missing some new baseline methods, including KG-CoT[1], ToG2[2], and GNN-RAG[3]. the authors should either include these comparisons or provide compelling justification for their exclusion.

- Furthermore, there are areas for experimental improvement. The experimental methodology would benefit from evaluation on more recent language models (such as open-source alternatives or current SOTA models) to demonstrate the robustness and generalizability of the proposed approach across different model architectures.



---

[1]  KG-CoT: Chain-of-Thought Prompting of Large Language Models over Knowledge Graphs for Knowledge-Aware Question Answering

[2] Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation

[3]  GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning

### Questions
Can you provide a justification or explanation for the concept of "deductive verification"? I have several concerns regarding the proposed method's ability to perform deductive verification, which is a significant claim within the paper. The model appears to lack a structured knowledge base or set of rules from which it can draw conclusions, which would be necessary for true deductive verification. Given this, I am skeptical of the term "deductive verification" being used in this context.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for extracting knowledge from a Knowledge Graph to enhance model reasoning capabilities. The core innovation of this paper lies in the Deductive-Verification Guided Beam Search, which enhances efficiency by allowing the model to select the top-k reasoning steps and implement pruning during path extension.

### Strengths
1. The application of this approach demonstrated significant improvements across various metrics on three KGQA datasets.
2. This study substantiates that knowledge graphs can to a certain degree mitigate the hallucination problem in model reasoning within open-domain question answering.

### Weaknesses
1. Several sections of the manuscript do not adequately convey essential information. For example, the title lacks precision in capturing the central elements of the study, and the abstract does not sufficiently highlight the primary research questions or issues.
2. In the experiments, comparing Fine-tuned LLM with GPT-4 seems unfair.
3. The Vanilla retriever compared in Section 3.3 is a relatively simple retriever.

### Questions
In retrieving specific knowledge from a knowledge graph, this paper proposes a method based on keyword extraction from the question and similarity assessment. However, Section 3.3 only compares embedding models. Does the accuracy of keyword extraction significantly impact the effectiveness of the retrieval approach?

### Soundness
3

### Presentation
3

### Contribution
3
