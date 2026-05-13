# Reasoning of Large Language Models over Knowledge Graphs with Super-Relations

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
While large language models (LLMs) have made significant progress in processing and reasoning over knowledge graphs, current methods suffer from a high non-retrieval rate. This limitation reduces the accuracy of answering questions based on these graphs. Our analysis reveals that the combination of greedy search and forward reasoning is a major contributor to this issue. To overcome these challenges, we introduce the concept of super-relations, which enables both forward and backward reasoning by summarizing and connecting various relational paths within the graph. This holistic approach not only expands the search space, but also significantly improves retrieval efficiency. In this paper, we propose the ReKnoS framework, which aims to Reason over Knowledge Graphs with Super-Relations. Our framework’s key advantages include the inclusion of multiple relation paths through super-relations, enhanced forward and backward reasoning capabilities, and increased efficiency in querying LLMs. These enhancements collectively lead to a substantial improvement in the successful retrieval rate and overall reasoning performance. We conduct extensive experiments on a variety of datasets to evaluate ReKnoS, and the results demonstrate the superior performance of ReKnoS over existing state-of-the-art baselines, with an average accuracy gain of 2.92% across nine real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a novel framework, ReKnoS, designed for reasoning over knowledge graphs using super-relations—groups of related connections within a particular domain. A super-relation encompasses various specific relations, effectively summarizing and linking different sections of the graph to support a more holistic exploration of the data.

Using super-relations, the framework represents multiple relation paths under a single super-relation, enhancing reasoning efficiency. This approach eliminates the need to discard numerous paths, thereby expanding the search space and significantly improving retrieval rates.

### Strengths
1. The paper is well-written, with clear and visually appealing graphs. The structure is easy to follow, and complex ideas are effectively explained.

2. The concept of super-relation reasoning is both novel and intuitive, making it easy to understand and engaging. The score-based entity extraction and selection approach is clever, and the entire system, built on LLMs, is practical and straightforward to deploy.

3. Extensive experiments demonstrate the performance improvements achieved by incorporating super-relations into the model.

4. Include efficiency analysis to further demonstrate the strength of the method.

### Weaknesses
There are no major issues with the paper. However, it would be helpful to place Figure 4 on the first page to provide an early overview of super-relations right from the beginning.

### Questions
1. For the reasoning component, could a smaller, fine-tuned language model be used to improve efficiency for individual, straightforward tasks? For instance, in a task where only three relations must be selected from a set of candidates to answer a question, would this approach impact performance?

2. Could these methods be applied to scenarios beyond question answering? For example, might they be used in code generation, where large datasets from GitHub could be structured into a knowledge graph format?

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
3

### Summary
The paper introduces ReKnoS, a framework for reasoning over knowledge graphs (KGs) using super-relations. In ReKnoS, super-relations are defined as groups of semantically similar relations within a specific field. The framework uses large language model (LLM) reasoning, similar to prior works such as Jiang et al. (2023b) and Sun et al. (2024). However, instead of relying on standard KG triplets, ReKnoS prompts the LLM to generate candidates with super-relations. This adjustment allows the reasoning process to cover a wider range of paths within the KG, potentially reducing misdirection issues. Additionally, the inclusion of super-relations supports flexible forward and backward reasoning, expanding the search space and potentially improving the accuracy of reasoning paths.

The paper is clearly written, with well-organized assumptions and a helpful discussion of preliminaries in Section 3 that clarifies design choices. I have a few observations and suggestions below:

1. The concept of super-relations as an abstraction over relations is creative and intuitive. However, its application seems limited to the Wikidata KG. The paper would benefit from discussing whether these improvements could apply to other domains and types of KGQA. Additionally, the reliance on the availability of super-relations is a limitation worth addressing.

2. The evaluation results in Table 1 show some improvement in six out of nine datasets. However, in three cases, the ReKnoS results are mistakenly bolded despite not being the highest values. This may indicate that improvements could be result of randomness within the margin of error, which is not reported in the paper. This small performance gains might also be achievable through hyperparameter tuning, a more thorough analysis would clarify the results in Table 1.

3. The scoring mechanism described in Section 4.2 appears somewhat arbitrary and lacks clarity. It is also not clear how scores are calculated and the prompt example in Lines 243–247 does not mention any scoring criteria. Furthermore, the paper does not present any evidence to indicate whether these scores align with human judgments, which would be beneficial for validating the approach.

### Strengths
For detailed discussion please check the "Summary".

### Weaknesses
1. The concept of super-relations as an abstraction over relations is creative and intuitive. However, its application seems limited to the Wikidata KG. The paper would benefit from discussing whether these improvements could apply to other domains and types of KGQA. Additionally, the reliance on the availability of super-relations is a limitation worth addressing. The experiments with Freebase do not fully address this concern, as much of Freebase's knowledge is already included in Wikidata, making it unclear if the method generalizes to KGs without pre-existing super-relation hierarchies. Further analysis on the limitations of the super-relations would clarify the reliance on them.

2. The evaluation results in Table 1 show some improvement in six out of nine datasets. However, in three cases, the ReKnoS results are mistakenly bolded despite not being the highest values. This may indicate that improvements could be the result of randomness within the margin of error, which is not reported in the paper. These small performance gains might also be achievable through hyperparameter tuning, a more thorough analysis would clarify the results in Table 1.

3. The scoring mechanism described in Section 4.2 appears somewhat arbitrary and lacks clarity. It is not clear how scores are calculated, and the prompt example in Lines 243–247 does not mention any scoring criteria. The paper does not clarify whether it uses explicit scoring criteria or human-crafted examples, making it difficult to understand the approach. Furthermore, the paper does not present any evidence to indicate whether these scores align with human judgments, which would be beneficial for validating the approach. It is unclear how the LLM aligns with human scoring criteria, and how specific scores, like 0.80 versus 0.90, are assigned without clear guidelines.

### Questions
Suggestions for Improvement:
1. Consider adding qualitative results to illustrate the benefits of super-relations in ReKnoS, such as examples where super-relations enhanced answer accuracy in specific datasets.
2. The focus on the GrailQA dataset as motivation for super-relations in Figures 1 and 2 limits the argument for the generalizability of ReKnoS. Including results from additional datasets in these figures would strengthen the paper.

Questions for the Authors:
1. Given that the use of super-relations could increase the chance of hallucination in LLMs (e.g., by suggesting relations not present in the KG), did the authors observe any instances of this effect?

### Soundness
2

### Presentation
3

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
This paper proposes the ReKnoS framework that aims to reason over knowledge graphs with super-relations. To be specific, ReKnoS introduces the concept of super-relations by summarizing and connecting various relational paths within the graph, which enhances the forward and backward reasoning capabilities, and increases the efficiency in querying LLMs. Extensive experimental results demonstrate the effectiveness of the proposed method in increasing the retrieval rate and overall reasoning performance.

### Strengths
1. This paper introduces the non-retrieval rate, providing a new insight for evaluating the retrieved path.
2. The idea behind introducing the super-relations is interesting, which not only expands the search space but also improves the retrieval efficiency.

### Weaknesses
1. It would be beneficial to include some subgraph-based reasoning methods (e.g., SR, UniKGQA and so on) introduced in Section 2 to conduct a comprehensive evaluation of the proposed method.
2. In Table 3, I have some questions regarding the average number of calls for StructGPT. From my understanding, this method may not require such a high number of LLM calls. It would be helpful to verify this to ensure accuracy.
3. It would be beneficial to conduct experiments for retrieval rate analysis between the proposed method and other baseline methods, which would better demonstrate the superiority of the proposed method.

### Questions
Please see **Weaknesses** above.

### Soundness
3

### Presentation
3

### Contribution
2
