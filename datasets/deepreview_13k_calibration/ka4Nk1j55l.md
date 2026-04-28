# GIVE: Structured Reasoning with Knowledge Graph Inspired Veracity Extrapolation

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 8, 5

## Abstract
Existing retrieval-based reasoning approaches for large language models (LLMs) heavily rely on the density and quality of the non-parametric knowledge source to provide domain knowledge and explicit reasoning chain. However, inclusive knowledge sources are expensive and sometimes infeasible to build for scientific or corner domains. To tackle the challenges, we introduce Graph Inspired Veracity Extrapolation (GIVE), a novel reasoning framework that integrates the parametric and non-parametric memories to enhance both knowledge retrieval and faithful reasoning processes on very sparse knowledge graphs. By leveraging the external structured knowledge to inspire LLM to model the interconnections among relevant concepts, our method facilitates a more logical and step-wise reasoning approach akin to experts' problem-solving, rather than gold answer retrieval. Specifically, the framework prompts LLMs to decompose the query into crucial concepts and attributes, construct entity groups with relevant entities, and build an augmented reasoning chain by probing potential relationships among node pairs across these entity groups. Our method incorporates both factual and extrapolated linkages to enable comprehensive understanding and response generation. Extensive experiments on reasoning-intense benchmarks on biomedical and commonsense QA demonstrate the effectiveness of our proposed method. Specifically, GIVE enables GPT3.5-turbo to outperform advanced models like GPT4 without any additional training cost, thereby underscoring the efficacy of integrating structured information and internal reasoning ability of LLMs for tackling specialized tasks with limited external resources.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work aims to enhance RAG by systematically integrating external knowledge from KGs and leveraging the model's internal knowledge. It induces potential relations between different entity groups, identifies intermediate nodes for multi-hop reasoning, and employs a guided reasoning process that combines affirmed knowledge, counters potential inaccuracies, and incorporates ground-truth data.

### Strengths
1. The authors provide a clear motivation and a good introduction to the problem.
2. Using LLMs to generate divergent thinking on additional entities and relationships to mitigate the sparsity problem in KG-RAG is a valuable approach worth exploring.
3. The performance of the method is overall positive.

### Weaknesses
1. Limited novelty, as leveraging triple-based reasoning in RAG and iterative self-checking are already common practices.
2. There are relatively few evaluation datasets and baselines. (See Questions)



### Questions
1. Using LLMs for selection will inevitably be constrained by the input length. Considering the case where there are a large number of 2-hop path combinations between two nodes, this method seems only suitable for very sparse knowledge graphs (where there are few 2-hop path combinations on average).
2. There are relatively few evaluation datasets, and the experiments are based on scenarios involving incomplete domain-specific knowledge graphs. It remains to be seen whether it can also be competitive against baselines in open-domain benchmarks with larger KG.
3. ToG assumes that it is based on a relatively large and complete knowledge graph. Considering the issue of corpus graph sparsity, could it be compared with methods like GraphRAG(From Local to Global: A Graph RAG Approach to Query-Focused Summarization)?
4. In addition to Questions_2, it's necessary to quantify the sparsity of the knowledge graphs mentioned in this paper.

### Soundness
2

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
3

### Summary
This paper introduces GIVE, a novel framework that enhances LLM's reasoning capabilities by leveraging sparse knowledge graphs. Rather than relying on direct knowledge retrieval, GIVE uses KG structure as "inspiration" for LLMs to conduct structured reasoning. The framework operates by decomposing queries into key concepts, constructing entity groups, and building connections within and across these groups through a combination of KG guidance and LLM knowledge.
The paper's main contribution is a new paradigm that bridges parametric (LLM internal knowledge) and non-parametric (external KG) memories for structured reasoning, while preventing hallucination through counterfactual knowledge incorporation. GIVE employs a progressive answer generation approach that combines affirmative, counter-factual, and expert knowledge to produce reliable responses. Through extensive experiments on both biomedical and commonsense reasoning tasks, the authors demonstrate that GIVE enables GPT3.5-turbo to outperform more advanced models like GPT4 on biomedical reasoning using only a sparse knowledge graph, without additional training.

### Strengths
The paper exhibits several notable strengths in its motivation, methodology, and empirical findings.

**Clear Motivation**: The authors identify a critical gap in current retrieval-based reasoning approaches for LLMs, which typically require dense, high-quality knowledge sources. This requirement poses a significant challenge in specialized domains like healthcare where comprehensive knowledge bases are expensive or impractical to build. The paper's focus on enabling effective reasoning with sparse knowledge graphs addresses a real-world constraint in deploying LLMs for domain-specific applications.

**Novel and Intuitive Method**: The proposed GIVE framework presents an elegant solution by treating knowledge graphs as inspiration rather than mere information sources. The method intuitively mimics human expert reasoning by first identifying relevant concepts, building semantic groups, and then discovering relationships both within and across these groups. The progressive answer generation strategy, which incorporates affirmative, counter-factual, and expert knowledge, provides a natural way to prevent hallucination while leveraging both the LLM's internal knowledge and external information.

**Interesting Findings**: The experimental results reveal several compelling insights. Most notably, GIVE enables GPT3.5-turbo to outperform GPT4 on biomedical reasoning tasks using only a sparse knowledge graph of 135 nodes, demonstrating that structured reasoning can compensate for model size. The ablation studies also reveal an interesting correlation between performance and expert knowledge ratio, suggesting that even a small amount of expert knowledge can effectively guide LLM reasoning when properly structured.

### Weaknesses
 **Limited Scope and Comprehensive Evaluation**: While GIVE is presented as a general framework applicable across domains, the empirical evaluation heavily focuses on medical QA tasks with sparse KGs. The experiments on CommonsenseQA with denser KGs are limited to GPT-3.5-turbo and lack comprehensive comparisons with competitive baselines. Despite claiming effectiveness "in retrieving information from both sparse and dense KG," there isn't sufficient experimental evidence demonstrating how GIVE helps bridge the performance gap between smaller and more advanced LLMs across different KG densities. A more thorough evaluation across different model sizes and KG configurations would better support the framework's generalizability claims.

**Scalability and Computational Analysis**: The paper's experiments primarily focus on sparse KGs with relatively small numbers of entity groups (m) and entities per group (n), typically less than 5 for biomedical datasets. While the authors mention potential optimizations through batch pruning, the paper lacks a thorough analysis of how the method scales with increasing m and n when applied to larger or denser KGs. The computational complexity of O(rm²n²) could become significant with larger KGs, and the paper would benefit from a detailed cost comparison with existing methods like RAG and ToG. This analysis is crucial for understanding the practical applicability of GIVE in real-world scenarios with larger knowledge bases.

**Knowledge Conflict Resolution**: The paper does not adequately address how GIVE handles conflicts between LLM's internal knowledge and KG-sourced information. While the progressive answer generation approach incorporates both knowledge sources, there isn't a clear mechanism or analysis of how the system resolves contradictions when they arise. This becomes particularly important in specialized domains where LLM's pre-trained knowledge might conflict with domain-specific KG information, potentially affecting the reliability of the reasoning process. A systematic approach to knowledge conflict resolution would strengthen the framework's robustness.

### Questions
1. **Comprehensive Evaluation and Generalization**
   - Could you provide additional experimental results comparing GIVE's performance across different LLM sizes (e.g., GPT-4, GPT4o-mini, Llama) on CommonsenseQA with the full ConceptNet?
   - What is the performance gap between smaller and larger LLMs when using GIVE with denser KGs? This would help substantiate the claim about GIVE's effectiveness across different KG densities.

2. **Scalability and Efficiency**
   - Could you provide an analysis of how computational costs scale when applying GIVE to denser KGs? Specifically, how does GIVE's running cost compared to RAG and ToG in the current setting and in a denser KG setting?
   - What is the practical upper limit for m and n on a large KG where GIVE remains competitive against RAG (probably with pruning as mentioned)?

3. **Knowledge Conflict Resolution**
   - How does GIVE handle cases where the LLM's internal knowledge directly contradicts the KG information? Is there a way to evaluate the reliability of conflicting information from different sources?
   - Could you provide examples of how the progressive answer generation approach handles such conflicts in practice?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces GIVE (Graph Inspired Veracity Extrapolation), a structured reasoning framework aimed at enhancing the factual reliability of large language models (LLMs) when working with sparse knowledge graphs (KGs). Recognizing the limitations of LLMs in specialized or scientific domains where comprehensive KGs are infeasible, GIVE leverages both internal and external knowledge sources. It decomposes queries into core concepts, creates entity groups for each query, and induces reasoning chains by identifying potential relationships among these groups. The framework incorporates both factual and counterfactual connections to mitigate hallucination risks in reasoning. Experiments on biomedical and commonsense QA benchmarks demonstrate that GIVE enables LLMs, such as GPT-3.5-turbo, to surpass even more advanced models like GPT-4 without additional training costs

### Strengths
The paper is clear and well-organized, making the technical contributions easy to follow.

Given the increasing reliance on LLMs for knowledge-intensive tasks, addressing the factuality of LLM outputs in specialized domains is a critical area of research.

The GIVE framework introduces an innovative approach by combining structured KG-inspired reasoning with parametric and non-parametric memories, presenting an original solution to a well-recognized problem in LLM performance.

### Weaknesses
The framework appears quite complex, combining multiple distinct modules into a single system. This layered approach raises concerns about the simplicity and elegance of the solution, as well as its general applicability.

Although the paper includes a few ablations, the complexity of the approach warrants a more thorough exploration of each module's contribution to overall performance. For instance, it would be valuable to have a clearer understanding of how each step (e.g., inner-group and inter-group connections, counterfactual relations) affects the final results.

How does GIVE perform in comparison to GraphRAG or similar frameworks that incorporate KG information into LLM-based reasoning? Since GraphRAG is specifically designed for KG integration, this would be a valuable comparison to include.

Why do some baselines without external knowledge outperform those with retrieval? It raises the question of whether the implementation of the baselines was correct. Could the authors clarify if there might be any explanation for these results?

GIVE is tested on specialized datasets, but commonly used benchmarks such as TruthfulQA and Natural Questions (NQ) are not included. Testing GIVE on these datasets would provide a broader perspective on its generalizability and effectiveness in widely used tasks.

The paper compares GIVE primarily against RAG and ToG. However, there is a substantial amount of literature on KG-enhanced LLMs. Adding comparisons with other KG-based enhancements would strengthen the experimental results and help position GIVE more accurately within the state of the art.

### Questions
How does GIVE perform in comparison to GraphRAG or similar frameworks that incorporate KG information into LLM-based reasoning? Since GraphRAG is specifically designed for KG integration, this would be a valuable comparison to include.

Why do some baselines without external knowledge outperform those with retrieval? It raises the question of whether the implementation of the baselines was correct. Could the authors clarify if there might be any explanation for these results?

GIVE is tested on specialized datasets, but commonly used benchmarks such as TruthfulQA and Natural Questions (NQ) are not included. Testing GIVE on these datasets would provide a broader perspective on its generalizability and effectiveness in widely used tasks.

The paper compares GIVE primarily against RAG and ToG. However, there is a substantial amount of literature on KG-enhanced LLMs. Adding comparisons with other KG-based enhancements would strengthen the experimental results and help position GIVE more accurately within the state of the art.

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
This paper presents a novel framework called GIVE (Graph Inspired Veracity Extrapolation), aiming at improving the reasoning ability of LLMs in knowledge-intensive tasks with sparse KGs. GIVE obtains similar entities for queried entities to construct relevant entity groups, then finds inter-group and inner-group connections with LLMs. By using LLMs to extrapolate probable relationships, GIVE addresses the limitation of traditional RAG methods when reasoning on domain-specific sparse KGs. Experiments on biomedical and commonsense datasets demonstrate the effectiveness.

### Strengths
S1. GIVE focuses on an important and practical issue. Traditional RAG approaches show poor performance on reasoning-rich tasks when domain knowledge cannot be easily obtained and domain-specific KGs are hard to construct and maintain. The idea behind GIVE could promote the application of LLMs in specialized domains with scarce data.

S2. Massive experiments are designed to support the authors' claim. As shown in Section 4, four datasets from two different domains are involved to demonstrate the effectiveness of GIVE. From Appendix, many ablation studies and detailed analysis are performed, showing robustness. The attached prompt templates also ensure that GIVE is easy to reproduce.

S3. The organization is good. The organization of Section 3 is clear and easy to follow.

### Weaknesses
W1. In general, this paper is well-written. However, some parts are very brief and hard to comprehend. It is better to present more details with some equations in Section 3.3 and 3.5.

W2. Limited evaluation and incomplete analysis. While massive experiments are conducted, there are still some experiments needed to enhance robustness. As for efficiency, comparison of LLM calls is not comprehensive enough. Details are listed in Questions.

### Questions
Q1. Could you provide a definition of "sparse"? From Section 4.1.1, we can see that each node in UMLS connects to about 87 nodes in average. In my opinion, UMLS is a "small" KG with only 135 nodes, but it's not a sparse KG if you take the degree of nodes into account.

Q2. The authors mentioned that KBQA datasets are unsuitable because GIVE is designed for reasoning with sparse KGs. I wonder whether GIVE works for KBQA with incomplete KGs if some edges are removed, just like EmbedKGQA (https://aclanthology.org/2020.acl-main.412), one of related works mentioned in Section 2.

Q3. The authors evaluate efficiency based on the number of LLM calls. How about the context length? Could you provide the averaged number of input tokens to solve one question for GIVE.

Q4. About multi-step reasoning. I wonder why only 2-hop paths are selected? Do you experiment with longer paths?

### Soundness
2

### Presentation
2

### Contribution
3
