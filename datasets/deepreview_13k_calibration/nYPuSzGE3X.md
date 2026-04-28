# InversionGNN: A Dual Path Network for Multi-Property Molecular Optimization

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Exploring chemical space to find novel molecules that simultaneously satisfy multiple properties is crucial in drug discovery. However, existing methods often struggle with trading off multiple properties due to the conflicting or correlated nature of chemical properties.  To tackle this issue, we introduce InversionGNN framework, an effective yet sample-efficient dual-path graph neural network (GNN) for multi-objective drug discovery.  In the direct prediction path of InversionGNN, we train the model for multi-property prediction to acquire knowledge of the optimal combination of functional groups.
Then the learned chemical knowledge helps the inversion generation path to generate molecules with required properties. 
In order to decode the complex knowledge of multiple properties in the inversion path, we propose a gradient-based pareto search method to balance conflicting properties and generate Pareto optimal molecules. 
Additionally, InversionGNN is able to search the full Pareto front approximately in discrete chemical space. Comprehensive experimental evaluations show that InversionGNN is both effective and sample-efficient in various real-world discrete multi-objective settings including drug discovery.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The article introduces InversionGNN, a dual-path graph neural network designed for multi-objective molecular optimization in drug discovery, addressing the challenge of balancing conflicting molecular properties. It  combines a direct prediction path, which learns chemical relationships between substructure and properties, with an inversion generation path that uses gradient-based Pareto optimization to generate molecules achieving trade-offs. The authors demonstrate the effectiveness of InversionGNN by empirical analysis on synthetic tasks and multi-objective drug discovery.

### Strengths
- The paper addresses an important problem, and the overall presentation is good, including writing and visualizations.

- The proposed gradient-based Pareto inversion module aligns with the intuition of multi-objective optimization (MOO) and offers strong interpretability.

- The experimental analysis is thorough, validating the model’s extensive exploration of the Pareto front in MOO from multiple perspectives, not limited to the molecular domain. Additionally, the ablation study provides interesting insights, such as showing that InversionGNN's incremental addition of substructures aligns better with weighted vectors.

### Weaknesses
 - My main concern is the claimed superiority of InversionGNN in molecular design results. On close examination of Table 1, it appears that DST, the most competitive baseline, performs nearly on par with InversionGNN across various metrics. Since the primary enhancement in InversionGNN is the gradient-based Pareto inversion module, this raises the question of whether the impact of this module is limited and whether the tokenization approach of the scaffolding tree is actually more critical for molecular design.

- The time complexity analysis is insufficient. In practical applications, QP-solving complexity can be significant. While the paper suggests that computing the non-dominating gradient is negligible in theory, I recommend adding a comparison of computation times across methods to provide clearer insights.

- The motivation behind oracle budget selection is not well-explained. What was the rationale for the oracle call budgets chosen for each baseline? The authors should consider controlling for a consistent budget across models to ensure fair supervision signals, which would also facilitate comparative analysis.

- The definition of the neighborhood set is somewhat ambiguous. How is the neighborhood set specifically defined in the context of molecular design?

### Questions
Please refer to the questions mentioned in the Weaknesses.

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
3

### Summary
The paper presents the InversionGNN framework, which aims to optimize molecular properties for drug discovery using a dual-path GNN approach. It consists of a Direct Prediction Path, where a GNN is trained to predict multiple chemical properties, leveraging learned chemical knowledge to enhance understanding of optimal functional group combinations and an Inversion Generation Path that employs a gradient-based Pareto optimization method to generate molecules that meet specified properties, addressing challenges posed by conflicting or correlated objectives. Key contributions include the integration of property prediction knowledge into molecular optimization processes and a novel relaxation technique that adapts gradient-based Pareto optimization for discrete chemical spaces, facilitating the exploration of diverse Pareto-optimal solutions. Empirical evaluations show that InversionGNN is both effective and sample-efficient, outperforming existing methods in multi-objective drug discovery scenarios by successfully balancing trade-offs among various chemical properties.

### Strengths
①The introduction of a dual-path GNN effectively combines property prediction with molecular generation. This approach enhances the integration of learned chemical knowledge into the optimization process, allowing for more informed and effective molecular design.

②The method demonstrates significant sample efficiency in exploring the chemical space. By leveraging gradient-based Pareto optimization, InversionGNN can identify high-quality molecules with fewer oracle calls compared to traditional methods, making it a practical choice for real-world applications where computational resources may be limited.

③The paper includes extensive experimental evaluations across various real-world datasets and multi-objective settings. These experiments provide robust evidence of the method's effectiveness and its ability to generate diverse Pareto-optimal solutions, validating its utility in drug discovery scenarios.

④The theoretical analysis, including Theorem 4.2, offers insights into the convergence properties of InversionGNN. This foundation not only strengthens the claims made about the method's effectiveness but also provides a framework for future research in multi-objective molecular optimization.

### Weaknesses
①The assumptions underlying Theorem 4.2 are not clearly articulated or justified within the text. Possible assumptions that could be relevant include the continuity and differentiability of the objective functions, the boundedness of molecular sizes, and the stability of the optimization process under varying conditions. The absence of a discussion on these assumptions raises concerns about the robustness of the theoretical claims presented. Without a thorough examination, it becomes challenging to assess the practical applicability of the results in real-world scenarios. Furthermore, the theoretical framework predominantly focuses on the specific architecture and objectives of InversionGNN. This narrow focus limits the generalizability of the findings, as it does not consider how the proposed method may perform under different conditions or with various types of optimization problems. Expanding the theoretical discussion to include a broader range of contexts could enhance the credibility and utility of the results.

②The majority of experiments in this paper compare InversionGNN only with I-LS, which is a very simplistic linear scalarization model. Demonstrating that InversionGNN outperforms I-LS does not provide significant insights into its effectiveness or practical advantages. Additionally, many experiments only contrast InversionGNN with older methods, while comparisons with more recent advancements, such as HN-GFN, are limited to just two lightweight experiments. The primary experiments lack comprehensive comparisons with contemporary approaches, which could better contextualize the performance of InversionGNN and underscore its contributions to the field.

③The paper lacks thorough experimental evaluations against SOTA methods in multi-objective optimization. A detailed comparative analysis with current leading techniques would provide a clearer understanding of InversionGNN's strengths and weaknesses. By not including such comparisons, the paper misses an opportunity to establish a more compelling case for the novelty and superiority of InversionGNN in the context of existing literature. Including SOTA comparisons could significantly enhance the paper's contributions and relevance to researchers in the field.

### Questions
Why doesn't InversionGNN make an all-encompassing and detailed comparison with HN-GFN, but rather such a detailed comparison with I-LS.

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
2

### Summary
This paper introduces InversionGNN, a method for multi-objective molecular optimization. InversionGNN comprises two paths: a direct prediction path and an inversion generation path. In the direct prediction path, a graph neural network (GNN) is trained to incorporate chemical knowledge. In the inversion generation path, the discrete molecular optimization problem is reformulated as a locally differentiable Pareto optimization problem, allowing the model to capture complex multi-property relationships. Experimental results demonstrate the effectiveness of InversionGNN on multi-objective molecular optimization benchmarks.

### Strengths
- Comprehensive Literature Review: The authors present a thorough review of the relevant literature, situating their work well within the existing field.
- The paper is well-organized.
- Extensive Experiments: The authors conduct a wide range of experiments, supporting the robustness of their results.

### Weaknesses
 - Clarity of Main Concepts: The core ideas are difficult to grasp, especially for those without a background in multi-objective optimization. I recommend adding more intuitive explanations at the start of Section 4 to clarify the fundamental concepts.
Missing Preliminaries on Differentiable Scaffolding Trees: The paper would benefit from an additional preliminary section on differentiable scaffolding trees to provide context for these methods.
- Unclear Terminology and Contribution: Key terms like “inversion generation path” and “dual-path” lack sufficient explanation. What exactly does "inversion" mean in this context, and how does it contribute to the model's novelty? Please clarify the role and purpose of the "dual-path" structure.
- Differentiation from Vanilla GCN: The distinction between the "Direct Prediction Path" and a standard Graph Convolutional Network (GCN) is unclear. Section 4.2 could be revised to explicitly highlight how this path diverges from a traditional GCN and its specific contributions to the model.
- Role of Relaxation Techniques: It is not clear how the relaxation techniques, which reformulate the discrete molecule Pareto optimization problem into a locally differentiable one, aid in capturing trade-offs among conflicting or correlated properties. Additional explanation on how this helps to balance multiple properties would improve understanding.

While this paper shows promise, I am not an expert in multi-objective optimization, and some core concepts remain unclear to me. I will finalize my score after reviewing feedback from another reviewer with more expertise in this area.

### Questions
See Weaknesses Section

### Soundness
2

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
The authors propose a molecular multi-objective optimization algorithm, inversionGNN, which proposes direct prediction paths and inversion generation paths to solve conflicting attribute optimization problems in chemical space. However, some issues need to be further addressed.

### Strengths
The method proposed by the authors, inversionGNN, a multi-objective molecular optimization method, is performed in a discrete space, which is different from the traditional latent space-based optimization methods and is methodologically innovative.

### Weaknesses
The authors' motivation for proposing the algorithm in their article by suggesting a conflict in the molecular properties is not specific enough. Also, in the article, it is suggested that the viewpoint of existing methods does not take into account the effect of substructure on molecular properties. Still, in the method introduction and experimental setup of inversionGNN, the authors do not address the effect of substructure on molecular properties either. At the same time, I don't quite understand what the significance of these tasks above the ablation experimental setup is. The authors should highlight the ablation experimental setup, what would be the impact if the current direct prediction path is not used, and what would be the extent of the impact on the current method if another proxy model is used.

### Questions
1. In the introduction, the authors suggest that substructures have an effect on molecular properties, so does inversionGNN take into account the effect of substructures on molecules?
2. in a multi-objective optimization task, how are the weights for multiple objectives balanced, or is the direct prediction path just viewed as a multi-classification task to bootstrap the Pareto front search?
3. what is the specific significance of the tasks designed by the authors in the ablation experiments, while the reader should be more interested in seeing how the direct prediction paths and inversion generation paths proposed by the authors affect the method.
4. Could the authors elaborate on how the surrogate oracle (used in Eq. 3) is trained and validated? Specifically, what types of data and target objectives are used for this model, and how is its accuracy assessed across diverse molecules?
5. The motivation for the thesis needs to be clear and is currently presented as too generalized. The flowchart of the methodology needs to be further improved so that the reader can understand the whole process.

### Soundness
2

### Presentation
2

### Contribution
2
