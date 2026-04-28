# Beyond Graphs: Can Large Language Models Comprehend Hypergraphs?

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 3, 8

## Abstract
Existing benchmarks like \texttt{NLGraph} and \texttt{GraphQA} evaluate LLMs on graphs by focusing mainly on pairwise relationships, overlooking the high-order correlations found in real-world data. Hypergraphs, which can model complex beyond-pairwise relationships, offer a more robust framework but are still underexplored in the context of LLMs. To address this gap, we introduce \texttt{LLM4Hypergraph}, the first comprehensive benchmark comprising 21,500 problems across eight low-order, five high-order, and two isomorphism tasks, utilizing both synthetic and real-world hypergraphs from citation networks and protein structures. We evaluate six prominent LLMs, including GPT-4o, demonstrating our benchmark's effectiveness in identifying model strengths and weaknesses. Our specialized prompting framework incorporates seven hypergraph languages and introduces two novel techniques, \textit{Hyper-BAG} and \textit{Hyper-COT}, which enhance high-order reasoning and achieve an average 4\% (up to 9\%) performance improvement on structure classification tasks. This work establishes a foundational testbed for integrating hypergraph computational capabilities into LLMs, advancing their comprehension.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces LLM4Hypergraph, a benchmark designed to evaluate large language models' (LLMs) understanding of hypergraphs, which can capture complex, multi-way relationships beyond pairwise correlations found in traditional graphs. The benchmark includes 21,500 problems across low-order, high-order, and isomorphism tasks using both synthetic and real-world hypergraphs. The study evaluates six prominent LLMs and introduces novel prompting techniques to enhance LLMs' performance on hypergraph tasks.

### Strengths
Originality: The paper proposes a new benchmark and prompting techniques tailored for hypergraphs, addressing a gap in the assessment of LLMs' capabilities.
Quality: The benchmark is comprehensive, covering a wide range of tasks and hypergraph types, which strengthens the validity of the findings.
Clarity: The paper is well-organized, with clear explanations of the hypergraph languages and prompting frameworks.
Significance: The work is significant as it pushes the boundaries of LLMs' understanding of complex data structures, which has implications for various real-world applications.

### Weaknesses
The paper could benefit from a deeper analysis of the limitations of the current LLMs in handling hypergraphs, beyond performance metrics. While the benchmark is comprehensive, it may lack diversity in terms of the types of real-world hypergraphs used, which could affect the generalizability of the findings.

### Questions
How do the prompting techniques generalize to other complex data structures beyond hypergraphs?
Could the authors elaborate on the potential scalability issues of the prompting techniques with increasingly large and complex hypergraphs?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper provided a new benchmark to evaluate the LLM's ability to understand hypergraphs and developed a new prompting framework to improve the hypergraph comprehension. The prompting framework demonstrated that CoT and BAG, adapted to hypergraphs, can improve the LLM's performance on hypergraph tasks, especially for high-order tasks such as Vertex Set Connection Checks and Vertex-Set--in-Hypergraph Checks using synthetic hypergraphs.

### Strengths
The paper is easy to read and the experiments are comprehensive and thorough.

### Weaknesses
 **Main arguments**:
1. The paper adapts existing benchmarks and prompting techniques for hypergraphs. While the results offer some insights into the extent to which LLMs understand hypergraphs, they largely mirror findings for simple graphs---specifically, that CoT and BAG can enhance LLM performance. The only notable point is that using suitable language to describe hypergraphs can aid LLM comprehension, which is novel but trivial.
Given that the proposed techniques are naive adaptations of existing techniques and new insights specific to hypergraphs are not found, the contribution of the paper is incremental and not significant.
2. The paper lays out a main motivation by the underexploration of (i) investigating the LLM's ability to understand hypergraphs and (ii) developing prompting framework for hypergraph understanding and argue that they are promising research directions. This is not a strong motivation, i.e.,  "underexploration" alone does not justify the promising research directions. More specific question is: why is prompting a promissing research direction for hypergraph understanding in light of other techniques such as function calling?
3. Unsupported claim 1: In abstract, ``our specialized prompting framework incorporates seven hypergraph languages and introduces two novel techniques, Hyper-BAG and Hyper-COT, which enhance high-order reasoning and achieve an average 4% (up to 9%) performance improvement on structure classification tasks.'' This is not sufficiently supported by the empirical results. The performance improvement for Hyper-COT is 4\% on average. However, for the Hyper-BAG, it is 2\% for low-order hypergraphs and 2.8\% for high-order hypergraphs.

**Minor arguments**:
1. Give the stochastic nature of the LLMs and the graph data, it is crucial to report the variation of the results across different runs (e.g., confidence intervals, standard deviations), given the performance gain of the proposed prompting techniques (Hyper-BAG and Hyper-COT) is slim.
2. Unsupported claim 2: The paper claimed in the supporting information (B.4) that the benchmark represents the first instance that includes isomorphism checks. This is not precise. Isomorphism checks are a special case of Maximum Common Subgraph (MCS) problem, which is included in the existing benchmark cited in the paper (GraphArena Tang et al. (2024)). The author used "in this domain" to limit the scope of their claim, and it is crucial to spell out the "domain" (e.g., general graphs, or hypergraphs specifically) to be more precise.
3. The paper did not provide descriptions about real-world graphs used in the experiments and their selection criteria.

### Questions
1. Why is prompting a promising research direction for hypergraph understanding in light of other techniques such as function calling?
2. What are the empirical graphs used in the experiments? What are the selection criteria?
3.  Some tasks involve computing tasks whose answers are numbers. How does the accuracy is computed for these tasks? Is it an exact match? Or allow some error under a certain threshold?
4. Does the BAG and CoT outperform beyond statistical variations attributed to the variations of individual graph data and stochatic behaviors of LLMs?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces LLM4Hypergraph, the first benchmark aimed at evaluating the ability of LLMs to understand hypergraph data. The authors design a series of tasks of varying difficulty levels and evaluate six different LLMs. Then, they identify their strengths and weaknesses. While this work represents a first step and provides a comprehensive study, there are several areas where improvement is needed.

### Strengths
- This paper proposes the first benchmark for evaluating LLMs on hypergraphs.
- The authors thoroughly address questions about hypergraphs.
- The problems are well-structured and clearly categorized according to their objectives.
- The code is released for reproducibility.

### Weaknesses
 - The motivations for this research are not sufficiently discussed. Why is it important to enable LLMs to understand hypergraph structures? Are there potential practical use cases? Are there any motivations beyond the fact that similar research has been done with graphs?
- The datasets used in the study are not comprehensive. To be specific:
  - The definition of "hypergraph size" is unclear. Is it referring to the number of nodes, the number of hyperedges, or the sum of hyperedge sizes?
  - The specific sizes of the hypergraphs (both real-world and synthetic) are not mentioned in the main content. How large are the synthetic hypergraphs used for evaluation?
  - According to the appendix, even the so-called "large-scale hypergraphs" only contain 15 to 20 vertices, which is too small to meaningfully capture higher-order structures typically expected in hypergraphs. The analysis should consider the density of the hypergraphs, not just the number of nodes, as the number of potential hyperedges grows exponentially with the number of nodes. Also, the prompt length should be analyzed with respect to the number of nodes and the density of the hypergraph.
  - The synthetic hypergraphs are not sufficiently representative. There are other synthetic hypergraph models (e.g., configuration models) available. The current use of pyramid, grid, and wheel structures, while demonstrating the LLM's ability to understand basic patterns, lacks real-world representativeness.
  - It is unclear how the random walk approach for sampling sub-hypergraphs from real-world hypergraphs (Appendix A.2) ensures that the sampled hypergraphs "retain the intricate and authentic correlations inherent in the original data."
- The definition of task "difficulty" is unclear.
- The authors may consider discussing/citing the recent work "When LLM Meets Hypergraph: A Sociological Analysis on Personality via Online Social Networks" (CIKM 2024) in the related work.

**In summary**, this paper makes a valuable contribution to LLMs and hypergraph analysis. However, the benchmark datasets lack comprehensiveness and have room to consider additional synthetic hypergraph generators. Also, the paper lacks detailed statistics on real-world hypergraphs. Scalability is also a concern; if large-scale hypergraph handling poses challenges for LLMs, these limitations should be clearly discussed.

### Questions
- How does the performance of LLMs depend on the hypergraph domains (e.g., emails, coauthorship)?

### Soundness
3

### Presentation
3

### Contribution
3
