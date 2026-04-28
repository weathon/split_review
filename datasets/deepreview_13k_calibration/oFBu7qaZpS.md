# Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Retrieval-augmented generation (RAG) has improved large language models (LLMs) by using knowledge retrieval to overcome knowledge deficiencies. However, current RAG methods often fall short of ensuring the depth and completeness of retrieved information, which is necessary for complex reasoning tasks. In this work, we introduce Think-on-Graph 2.0 (ToG-2), a hybrid RAG framework that iteratively retrieves information from both unstructured and structured knowledge sources in a tight-coupling manner. Specifically, ToG-2 leverages knowledge graphs (KGs) to link documents via entities, facilitating deep and knowledge-guided context retrieval. Simultaneously, it utilizes documents as entity contexts to achieve precise and efficient graph retrieval. 
ToG-2 alternates between graph retrieval and context retrieval to search for in-depth clues relevant to the question, enabling LLMs to generate answers.
We conduct a series of well-designed experiments to highlight the following advantages of ToG-2: 1) ToG-2 tightly couples the processes of context retrieval and graph retrieval, deepening context retrieval via the KG while enabling reliable graph retrieval based on contexts; 2) it achieves deep and faithful reasoning in LLMs through an iterative knowledge retrieval process of collaboration between contexts and the KG; and 3) ToG-2 is training-free and plug-and-play compatible with various LLMs. Extensive experiments demonstrate that ToG-2 achieves overall state-of-the-art (SOTA) performance on 6 out of 7 knowledge-intensive datasets with GPT-3.5, and can elevate the performance of smaller models (e.g., LLAMA-2-13B) to the level of GPT-3.5’s direct reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Think-on-Graph 2.0 (ToG-2), a RAG framework that integrates both unstructured text and structured knowledge graphs in a tightly coupled manner to improve retrieval quality and reasoning accuracy for LLMs. ToG-2 addresses key limitations of current RAG methods, which often fail to retrieve sufficiently deep and contextually rich information for complex reasoning tasks. By alternating between context retrieval and KG-based retrieval, ToG-2 effectively links and enriches information sources, guiding LLMs in producing more reliable and contextually informed answers. On various tasks (multi-hop KBQA, multi-hop complex document QA, slot filling, and fact verification), ToG-2 achieves satisfying performance in comparison with different RAG baselines (text-based, KG-based, and hybrid).

### Strengths
+ The proposed tight-coupling approach is well-motivated. It uses KGs to guide the retrieval of document contexts while simultaneously treating these documents as entities in the KG, thereby creating a feedback loop that enhances both retrieval depth and context fidelity.

+ The iterative retrieval process is intuitive. It mimics human reasoning by continuously refining the search for information based on initial retrieval results.

+ Experiments are comprehensive. Six datasets across four different tasks are examined. Baselines using CoT, text-only RAG, KG-based RAG, and hybrid RAG are compared. Besides performance comparison, the authors also conduct ablation studies, efficiency analysis, and case studies to verify some of their design choices.

### Weaknesses
 - Statistical significance tests are not conducted. It is not clear whether the gaps between ToG-2 and the baselines are statistically significant or not in Table 1. In fact, the improvement is subtle in some columns. Also, the statistical significance of ablation studies should be considered.

- The quality and completeness of the KG used in ToG-2 can significantly influence its retrieval accuracy and reasoning performance. The effect of KG quality on the performance of ToG-2 is not accurately quantified. Although the authors add a ToG-FinQA dataset in their experiments with a newly built KG, the quality of this KG is also unknown. It would be valuable to explore the performance of ToG-2 with incomplete WikiData.

### Questions
- Could you conduct a statistical significance test (e.g., two-tailed t-test) to compare ToG-2 with the baselines in Table 1, and report the p-values?

- Could you study the effect of KG quality on the performance of ToG-2 by using incomplete WikiData as KG (e.g., with 10%, 20%, or 50% of the entities/relations)?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript presents a framework designed to augment the reasoning capabilities of Large Language Models (LLMs) through the integration of knowledge graphs. The framework addresses several limitations inherent in current methodologies by implementing three key strategies: hybrid knowledge exploration, knowledge-guided graph search, and knowledge-guided context retrieval. The objective is to mitigate issues such as constrained knowledge retrieval and the scarcity of informed knowledge within LLMs.

### Strengths
- The manuscript adeptly delineates the constraints of LLMs in reasoning through complex queries and proposes a systematic and coherent methodology to surmount these limitations.

- The incorporation of hybrid knowledge, derived from both knowledge graphs and wiki documents, constitutes an intuitive approach to enhancing the inferential competencies of LLMs, which, to the best of my knowledge, is a novel contribution to the field.

- Table 1 offers a comparative analysis with appropriately set benchmarks, demonstrating the superiority of the proposed ToG 2.0 model as a new SOTA solution. The authors further substantiate this claim through empirical experiments.

- The figures and graphics were well done and helped with understanding the methodology of the paper substantially.

### Weaknesses
 - The incremental contributions of ToG 2.0 over its predecessor, ToG, are noteworthy but not transformative.
> Specifically, the core improvements include the addition of context-retrieval and context-guided entity pruning to ToG's existing Relation exploration and Entity exploration.


- Although  LLM costs is not normally a point of significant concern for the soundness/rigor of a work. However, the methodology is financially demanding, as processes such as Knowledge Exploration, Relation Pruning, Relation Discovery, Entity Pruning, and Reasoning all necessitate frequent calls to the LLM API. The associated high costs may deter further exploration by researchers within the Graph RAG community.
> Constructively, it is suggested that the authors elaborate on a refined cost analysis and contemplate the implementation of optimizations to reduce API calls. Such measures would effectively address the raised concerns about `extensive utilization of LLM APIs’ and simultaneously provide pragmatic suggestions for further enhancement.


- I harbor reservations regarding the efficiency of this approach. Empirically, processes that require extensive utilization of LLM APIs are inherently time-consuming. As evidenced by the time expenditures for Relation Pruning (RP), Entity Pruning (EP), and Reasoning detailed in Table 3, the task at hand is laborious. The documentation lacks clarity on whether Table 7 provides the RP, EP, and reasoning times for each individual sample. If it does, then for multi-hop Knowledge Graph (KG) reasoning tasks, compounded by the size of the dataset, the task becomes significantly time-consuming when juxtaposed with direct LLM-only methods or Text-based RAG approaches. Additionally, ToG 2.0 necessitates grounding in the vast corpus of external Wikipedia data. 
> I contend that evaluating the efficiency of this method solely in comparison to ToG 1.0 lacks impartiality.

### Questions
- What about total runtime and API call counts compared to other baselines like direct LLM methods and text-based RAG approaches ?
- Table 7 should clarify whether it reports the reasoning time for each discrete query or for each RP and EP iteration, given that multi-hop reasoning entails successive RP and EP cycles.

- The question also arises: Why does ToG outperform ToG 2.0 in the Creak dataset? To make it more actionable, more detailed analysis of the performance on the Creak dataset should be provided, including potential reasons for this discrepancy and its implications for the method's strengths and limitations.

### Soundness
3

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
5

### Summary
This paper introduces Think-on-Graph 2.0 (ToG-2), a novel hybrid retrieval-augmented generation (RAG) framework that aims to enhance large language model (LLM) reasoning by combining structured knowledge from knowledge graphs (KGs) with unstructured knowledge from texts. The key innovation is the "tight-coupling" approach between KG-based and text-based RAG, where KGs guide deeper context retrieval while textual context enables more precise graph retrieval. The framework iteratively performs knowledge-guided context retrieval and context-enhanced graph retrieval to obtain comprehensive information for LLM reasoning. The authors demonstrate ToG-2's effectiveness through extensive experiments across multiple knowledge-intensive datasets, showing state-of-the-art performance on 6 out of 7 benchmarks and the ability to elevate smaller LLMs' reasoning capabilities to be comparable with larger models.

### Strengths
1. Technical Innovation: The tight-coupling approach between KG and text-based RAG is novel and well-motivated, addressing limitations of previous hybrid approaches.

2. Comprehensive Evaluation: The experimental validation is thorough, covering multiple datasets and including detailed ablation studies. The creation of ToG-FinQA shows commitment to robust evaluation.

3. Implementation Details: The paper provides detailed implementation guidance and pseudocode, making it reproducible.

4. Analysis Depth: The manual analysis and runtime studies provide valuable insights into the framework's behavior and efficiency.

### Weaknesses
1. Scalability Analysis: While runtime comparisons are provided, there could be more discussion about the framework's scalability with very large knowledge graphs or document collections.

2. Error Analysis: Though there is some manual analysis of error cases, a more systematic categorization of failure modes could be valuable.

3. Hyperparameter Sensitivity: While some hyperparameters are studied (width and depth), a more comprehensive analysis of other parameters' impact would be helpful.

4. ToG-FinQA Dataset: While valuable, the dataset is relatively small (97 QA pairs). A larger dataset would strengthen the domain-specific evaluation.

### Questions
1. How does the performance of ToG-2 scale with significantly larger knowledge graphs or document collections?

2. Could you provide more details about the failure modes of the system and potential strategies to address them?

3. How sensitive is the system to the quality of the initial entity linking step? What happens when entity linking fails?

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
ToG-2 is an iterative RAG framework that combines unstructured and structural knowledge from the input to answer the given question. Concretely, ToG-2 extracts multiple entities from the query, extracts their neighboring entities, filters out these entities via relation pruning to extract a set of candidate entities, and identifies (and prunes) retrieved entity context candidate entity. Experiments show that ToG-2 achieves state-of-the-art on the majority of datasets.

### Strengths
State-of-the-art performance is achieved on all but one dataset

ToG-2 conducts extensive experimentation to verify their novelty

### Weaknesses
1. Figures

The main figure, as well as the introduction, indicates that ToG-2 is distinctly different from Text-based RAG, KG-based RAG, and Hybrid (text- + KG-based) RAG. Upon inspection, it appears that ToG-2 is just a fancy version of Hybrid RAG in that entities are selected based on a n-order neighborhood of the entities identified in the query. While ToG-2 is no doubt different from previous Hybrid RAG approaches, it should still be considered a Hybrid RAG approach.

The caption of the main figure should give a description of the flow of the methodology. Given that there are multiple modules in ToG-2, and that important information of these modules are not depicted (more in the following comment) an explanation of the information flow is necessary.

While the main figure provides a nice overview of ToG-2, it is missing important detailed information. For example, relation/entity scoring and the prompts used aren’t able to be determined by looking at the main figure. Consider creating another figure that depicts these details.

2. Experiments

No analysis of threshold scores for relation pruning (“The relations with a low score will be pruned” on page 5, lines 230-231). How much would performance vary if the threshold is changed? What does the distribution of relation scores from the LLM look like? These are questions that should’ve been answered. Considering that ToG-2 is a multistage pipeline, and that relation pruning is one of the first steps in the pipeline, analysis here is vital given that error from this module will propagate through your remaining modules. Furthermore, there isn’t any mention (let alone the reasoning) of the threshold score used in ToG-2. In the code, the score that is used is 0.2 (https://anonymous.4open.science/r/ToG2/wiki_func.py, line 38). This should have been mentioned in the manuscript and not have been identified solely by investigating the repository.

Table 6, the influence of each module (which should be in the main content), indicates that the removal of relation pruning increases performance across all datasets (the increase in performance in from row 2 to row 3). This appears to nullify the contribution that relation pruning offers.

Experiments involving LLMs should’ve been repeated multiple times given that LLMs have been shown to vary greatly based on the prompt.

3. Grammatical/formatting errors

On page 1, line 40, there is a space missing between “issues” and “(Zhao et al., 2024)”

The query in the main figure “Where was one of the runners born who almost broke Craig Virgin’s Illinois Boys Cross Country record?” should be re-worded for clarity. Consider stating “What was the birthplace of one of the runners who almost broke Craig Virgin’s Illinois Boys Cross Country record?”.

Consider removing the word “and” on line 228, page 5 between equations 2 and 3, as the current format is an unorthodox way of introducing two equations simultaneously.

“Figure 2” needs a space between “Figure” and “2” on page 5, line 239.

The “a” in “Given a topic entities” in line 241, page 5 should be removed.

The citations in section 4.2 are in double parenthesis. This needs to be fixed.

The title of section 4.5.3 “Width&Depth Settings” is missing a space between “Width” and “&” as well as “&” and “Depth”.

The ablation study comparing the performance when removing different modules (Table 6) should be put in the main content, not in the appendix.

### Questions
Did the authors notice that ToG-2 performs better without relation pruning (when topic pruning and retrieval feedback are also removed) than when only topic pruning and retrieval feedback are removed?

It is mentioned that “ToG-2 selectively explores entities neighboring the current topic entities on the KG, using the newly encountered entities to refine the retrieval scope, thereby enhancing both efficiency and accuracy.” (lines 161-180, pages 3-4). How is ToG-2 able to enhance/improve efficiency if there are more entities considered (via neighbors in the knowledge graph) compared to just the entities extracted from the query?

In figure 3b, the performance of ToG-2 when using BGE-Ranker decreases as the number of entities considered increases (from 38% to 33% when the number of entities jumps from 3 to 5). This seems to be counter-intuitive, as the larger the entity space, the more likely it would increase performance (which is the case when using LLMs). Why would this be the case?

Why not consider a dynamic number of candidate topic entities (dynamic based on the iteration)? Logically, it’s more likely that first order neighbors of an entity in the query would be more important than entities in the second order neighborhood (although this assumption might be invalid when dealing with very granular inputs).

What is “CMB” with respect to relation pruning (equation 3, tables 11 & 12)?

### Soundness
3

### Presentation
3

### Contribution
3
