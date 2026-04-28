# Mechanistic Insights: Circuit Transformations Across Input and Fine-Tuning Landscapes

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 8, 1

## Abstract
Mechanistic interpretability seeks to uncover the internal mechanisms of Large Language Models (LLMs) by identifying circuits—subgraphs in the model’s computational graph that correspond to specific behaviors—while ensuring sparsity and maintaining task performance. Although automated methods have made massive circuit discovery feasible, determining the functionalities of circuit components still requires manual effort, limiting scalability and efficiency. To address this, we propose a novel framework that accelerates circuit discovery and analysis. Building on methods like edge pruning, our framework introduces circuit selection, comparison, attention grouping, and logit clustering to investigate the intended functionalities of circuit components. By focusing on what components aim to achieve, rather than their direct causal effects, this framework streamlines the process of understanding interpretability, reduces manual labor, and scales the analysis of model behaviors across various tasks. Inspired by observing circuit variations when models are fine-tuned or prompts are tweaked (while maintaining the same task type), we apply our framework to explore these variations across four PEFT methods and full fine-tuning on two well-known tasks. Our results suggest that while fine-tuning generally preserves the structure of the mechanism for solving tasks, individual circuit components may not retain their original intended functionalities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript studies how transformer circuits discovered by the edge pruning algorithm (Bhaskar et al., 2024) change under ablated prompts and various types of fine-tuning methods (e.g., BitFit, LoRA, full). The manuscript proposes a framework to study the functionalities of various discovered circuits. Empirical results are observed after prompt ablation and fine-tuning on GPT-2 small, where statistically significant variations in structures of discovered circuits.

### Strengths
- Transformer interpretability is a novel field with very interesting results and of great relevance to the audience of this venue
- Very detailed analysis, both quantitative and qualitative, explaining the framework

### Weaknesses
 - The paper reads like an exposition on a series of analyses performed on a particular transformer on a set of prompts. The main result only showed that the proposed "perturbation" (both parameters and input data) has caused statistically significant variation in the discovered circuit from Bhaskar et al. I failed to see the significance of such variation, nor did the author do a good job explaining them: intuitively, such variation is either naturally straightforward, or an artifact of edge pruning, and not inherently offering insights on why they are occurring, and how that may lead to either better designs of the network architecture, data pipeline, or training algorithm. Granted that the authors have spent painful details qualitatively measuring logit clusters and rendering individual circuits from their experience, but it is very difficult to reason about the significance of these particular observations from the experiments.
- Hence, the claim that this is a novel framework that accelerates circuit discovery and analysis is very weak since the analysis appears to be superficial, and the framework appears to be a set of procedures that the authors elected to apply.
- The work also builds heavily on edge pruning - it may better be characterized as a technical report, as an application of Bhaskar et al., rather than a novel contribution.
- Finally, the experiments are only performed on a small transformer. It would be more convincing for the authors to provide additional experiments that may suggest that the proposed "framework" can indeed scale to larger networks.

### Questions
What is the main takeaway from applying the proposed framework on various versions of a transformer / a transformer on a set of ablated prompts? Beyond that, "the discovered circuits are different" and that "particular circuits appear to form different attention groups and logit clusters."

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new framework for circuit analysis consisting of three stages: circuit selection and comparison, attention grouping, and logit clustering.

The stages are detailed as follows:

- **Circuit Selection and Comparison**: Circuits are evaluated using various metrics (e.g., KL divergence, Kendall's tau, etc) to determine their faithfulness to the original model at different sparsity levels. The optimal circuit is chosen using the elbow method, balancing sparsity and performance based on the selected metric.

- **Attention Grouping**: The prompt is divided into multiple parts, and attention patterns are computed for each part. Heads are considered to be attending to a specific component if their attention to it is above the mean of the top-k highest attention values. Groups are then formed based on whether the heads attend to the same group of tokens.

- **Logit Clustering**: Different heads are clustered based on their logit patterns. The idea is that heads with similar logit patterns likely up-weight or down-weight similar tokens. 

The authors validate this method by applying it to analyze structural changes in circuits under various conditions. Specifically, they examine changes in circuit structure when prompts are modified (e.g., using animals instead of people) and when fine-tuning on specific tasks.

### Strengths
- The experimental section is well-chosen and provides several results that may interest the community. For example:
  1. Fine-tuning can lead to changes in circuit sizes, with variations depending on task complexity (sometimes larger, sometimes smaller).
  2. Fine-tuning can retain significant parts of circuits, sometimes strengthening their effects.
  3. The size of the circuits for IOI varies quite a bit with the ablated version with the animals version being much simpler, though still retaining a great deal of the components. 

- The paper addresses a timely and relevant topic in circuit interpretability. The authors take a step toward automating circuit interpretation, an area often overshadowed by circuit discovery.

### Weaknesses
 **Minor Weaknesses**
- The paper could benefit from clearer writing. It is sometimes difficult to follow. For example, on a first reading I had a hard time understanding what the authors proposed as part of their framework. Additionally, more mathematical descriptions would improve clarity. For instance, it’s unclear what exactly is being clustered in the logit clustering—whether it is the direct head output or the dot product between the unembedding matrix and logits. The paper right now has very little mathematical formulas and I think  adding more could aid the reader in understanding the method on top of the verbal descriptions.

- There are errors in the submission, such as missing content in Appendix A and Appendix D.

**Important Weaknesses**
- Some of the methodological contributions  of the framework seem small. For example, the circuit discovery and selection stage appears more like a simple check than a significant step in the framework, despite being principled. The use of the elbow method, while principled, is a fairly standard approach and does not represent a significant methodological contribution in itself. The metrics used for circuit evaluation, such as KL divergence and Kendall's tau, are also established techniques, and their application here, while necessary, does not introduce novel methodology.

- The attention grouping methodology has potential issues. Grouping heads across different layers can be misleading, as information may shift from one token to another one across layers. For example, a head might attend to token \( t \) in layer \( l \), but this information could shift to token \( t+1 \) in layer \( l+1 \), where another head attends to it. In this case, it would be incorrect to assign these two heads to different clusters as they are attending the same information (although at different positions). Hence, while attention patterns are useful, they are not be sufficient for rigorous analysis. The method does not account for the flow of information across layers, which is a crucial aspect of transformer networks. The approach of using the mean of the top-k attention values as a threshold is also somewhat arbitrary and lacks a strong theoretical justification. It is unclear how the value of k is chosen and how sensitive the results are to this parameter.

- Building on the previous point, while logit clustering and attention grouping are interesting, they appear more suited to exploratory analysis than to a formal interpretability framework. They function more as heuristics, which, while not inherently negative, differs from the authors' claims in the paper. The clustering of logits, while potentially informative, does not provide a causal understanding of the circuit's behavior. It identifies heads that produce similar outputs, but it does not explain why they do so or how they contribute to the overall computation. The paper lacks a clear definition of what constitutes a 'functionality' of a node and how the proposed method can be used to rigorously identify it.

### Questions
- Could the authors provide more detail on what exactly is clustered in the logit clustering?
- How do the authors envision these methods integrating into the current interpretability workflow?

### Soundness
2

### Presentation
2

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
The authors build on previous circuit discovery methods to identify circuits for two commonly used template-specific tasks: IOI, and GT. They advance previous methods, which specialized on localization, by clustering relevant nodes into groups of similar functionality. For the IOI task, they test the generalization of found circuits to other subject domains, from human first names to animals (referred to as ablation). They further compare circuits found in the base model to circuits identified to a single model before and after task-specific fine-tuning.

### Strengths
In general, successful circuit discovery provides explanations for localization and functionality of circuit components. Existing circuit discovery methods mostly focus on localization (except for supervised methods like DAS). They are often template specific and sensitive to changes in the task. This paper addresses two key problems of existing work, which is relevant to the current state of the field:
1. Insight on node functionality
2. Variation of templates

- In my opinion, the main novelty is clustering attention heads by functionality. I think that further work on circuit discovery for templated tasks should use this method.
- This enabled a novel discovery of behavior shift during finetuning which could explain task-specific accuracy gains.
- The paper is well and clearly written, and provides useful descriptions of intuitions
- The figures generally support key points in the text well.

### Weaknesses
## Main critiques that can be addressed in this paper:
- In Table 4, the meaning of the “shared” column is unclear. My current interpretation is that it represents the intersection of nodes (or edges) between model A and B. However, this interpretation is inconsistent with the provided data, as often edges(A) + edges(B) < shared(A,B). This discrepancy needs clarification.
- The circuit selection process could benefit from a more rigorous quantitative description. While the authors mention identifying the ‘knee’ of the KL divergence curve, the exact methodology remains vague. It is unclear whether the authors visually inspected the curve or employed a more formal quantitative measure that balances faithfulness and sparsity. A detailed explanation of the 'knee point' identification method, potentially including a mathematical formulation or algorithmic steps, would significantly enhance the reproducibility and rigor of the approach.
- The section on logit clustering lacks sufficient technical details regarding the aggregation of multiple IOI samples within a batch. Specifically, the method for averaging logits across samples needs to be explicitly stated. Providing a formula or a detailed description of this aggregation process would improve the clarity and reproducibility of the logit clustering technique.

## Further critiques that mainly point towards future work.
- The scope of the ablation studies is currently narrow. While the finding that animal IOI circuits are mostly a subset of human IOI circuits is novel, it does not provide sufficient evidence to conclude that the identified circuits represent the model's complete IOI capability. To better assess the generality of the discovered circuits, future work should explore a wider range of templates. For instance, varying the IOI template to include verbs in the present progressive tense (e.g., “The kind grandmother is baking cookies for her grandchildren, delighting the grandchildren.”) could provide a more comprehensive understanding of the model's IOI capabilities beyond the specific templates used in this study.
- The inability of GPT-2 small to perform IOI for cities and colors is a limitation. While the authors acknowledge this in the appendix, future research should focus on studying more capable models that can handle a wider range of inputs. This would allow for a more thorough investigation of IOI circuits across different domains.
- While studying GPT-2 small is a natural choice due to its use in previous work, the authors could further leverage this by explicitly highlighting the parallels and differences between their findings and previously identified circuits. This would provide a clearer picture of how the current work builds upon and diverges from existing research.
- The authors should acknowledge the limitations of the Logit Lens, particularly its potential for imprecision or misleading results due to residual stream drift. While GPT-2's tied embedding and LM-head weights might mitigate this issue to some extent, a discussion of these limitations would enhance the paper's transparency. The authors' approach of tying inThis method still depends on templated dataset and the manual investigation.
- The current work primarily focuses on clustering attention heads. A more detailed discussion of how MLPs are treated compared to previous methods would be beneficial. Additionally, exploring the potential application of Logit Clustering to MLPs could be a valuable avenue for future research. Are there specific reasons why this approach might be unsuitable for MLPs?

## Notes
- 307 “irrelevant” seems imprecise since the mentioned tokens (eg. M) provide useful grammatic informatic. Alternative: syntactically relevant or semantically irrelevant?
- Cite logit lens blogpost
- The authors mention “intended” functionalities of LLM attention heads. It would be interesting to include a discussion about the confidence level associated with these intended functionalities. Given that the same heads can participate in different circuits and potentially fulfill different roles, a quantitative assessment of how much the results determine the one specific intention would be valuable.
- Circuit diagrams (in most papers look) like a big blob, the field could improve on circuit visualizations
- In the appendix, the section headers don’t align with figures which appear on other pages further down. I can’t really make use of the appendix table of contents.

### Questions
## Notes
- 307 “irrelevant” seems imprecise since the mentioned tokens (eg. M) provide useful grammatic informatic. Alternative: syntactically relevant or semantically irrelevant?
- Cite logit lens blogpost
- The authors mention “intended” functionalities of LLM attention heads? I’d be curious about a confidence assessment of how much the results determine the one specific intention in the authors’ opinion. I’m a bit skeptical, since same heads can fulfill different roles in different circuits
- Circuit diagrams (in most papers look) like a big blob, the field could improve on circuit visualizations
- In the appendix, the section headers don’t align with figures which appear on other pages further down. I can’t really make use of the appendix table of contents.

## Typos
065 what IS coming next
523 PATH patching

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
In their work, authors address the question of discovery and interpretability of model circuits responsible for problem solution, focusing on fine-tuning procedures like PEFT. Authors present a pipeline of edge pruning and circuit discovery starting from full model, leading to circuits identification for further analyses. Authors take two tasks, Indirect Object Identification (IOI) and Greater Than (GT), perform PEFT on GPT2 small base model and run the proposed circuit identification and analysis routines on control and fine-tuned models. Authors use performed analysis to compare various PEFT forms.

### Strengths
Question of interpretable circuit identification is an important direction, as it holds promise to reveal causes of model failures to solve certain problem types, also hinting how to fix model function and learning.

### Weaknesses
It is not clear from the presented work how the proposed circuit identification should help to better understand model function. Examples of interventions to improve model behavior based on conducted circuit analysis are missing. There is no comparison conducted to other SOTA methods for circuit identification and analysis. It is in general hard to understand from the paper what are the merits of proposed method and how it relates to already existing works.

### Questions
Is there any way to demonstrate how introduced methods can provide concrete invervention for model improvement which leads to better task performance on the 2 tasks that are studied? An example of such intervention based on derived circuits could give hints or proof of concept how presented method can be useful.

### Soundness
2

### Presentation
2

### Contribution
1
