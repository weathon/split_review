# Iterative Substructure Extraction for Molecular Relational Learning with Interactive Graph Information Bottleneck

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Molecular relational learning (MRL) seeks to understand the interaction behaviors between molecules, a pivotal task in domains such as drug discovery and materials science. Recently, extracting core substructures and modeling their interactions have emerged as mainstream approaches within machine learning-assisted methods. However, these methods still exhibit some limitations, such as insufficient consideration of molecular interactions or capturing substructures that include excessive noise, which hampers precise core substructure extraction.
To address these challenges, we present an integrated dynamic framework called Iterative Substructure Extraction (ISE). ISE employs the Expectation-Maximization (EM) algorithm for MRL tasks, where the core substructures of interacting molecules are treated as latent variables and model parameters, respectively. Through iterative refinement, ISE gradually narrows the interactions from the entire molecular structures to just the core substructures.
Moreover, to ensure the extracted substructures are concise and compact, we propose the Interactive Graph Information Bottleneck (IGIB) theory, which focuses on capturing the most influential yet minimal interactive substructures. In summary, our approach, guided by the IGIB theory, achieves precise substructure extraction within the ISE framework and is encapsulated in the IGIB-ISE}
Extensive experiments validate the superiority of our model over state-of-the-art baselines across various tasks in terms of accuracy, generalizability, and interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To alleviate the problems in current methods of molecular relational learning: insufficient consideration of molecular interactions and failure to capture high-quality substructures, this paper introduces an IGIB (Interactive Graph Information Bottleneck)-ISE (Iterative Substructure Extraction) method. Their work achieves better performance than current SOTA models in terms of accuracy, generalizability, and interpretability.

### Strengths
1.	This paper has good clarity. It is well-written with a clear structure. In a concise but informative style, readers would find it easy to understand the key concepts, backgrounds, and methods.
2.	Their work also brings new insights into the MRL area. They noticed the inefficiency of current methods, where using the complete profile of an interacting molecule could not only be unnecessary but also comprises generalizability. And they proved the effectiveness of their method through experiments. 
3.	In general, they bring new ideas to the MRL area: Interactive Graph Information Bottleneck (IGIB). Bottleneck-based methods are widely used in many areas and receive satisfactory results. In this paper, they integrated it into the ISE framework for further optimization. It is also the method that leverages the model’s performance to outperform all baselines.

### Weaknesses
1.	(General Assumption) Most molecule interactions may depend on each molecule’s substructures, but does this apply to all molecule interactions? If not, the assumption at line 161 is somewhat arbitrary, where some edge cases could be ignored by this model. This assumption needs to be further justified. Specifically, the model does not account for interactions that may be driven by the overall shape or charge distribution of the molecule, rather than specific substructures. For example, van der Waals forces or interactions with large, flexible molecules might not be well-captured by a substructure-focused approach.
2.	(Time and Space Complexity) While the model outperforms all the baseline models, it spends much more time processing DDI Datasets. Compared to CMRL, with around 1% accuracy improvement, this model costs 5.8 ~ 7.1x more time and 6.4 ~ 9x more space. This may lead to expensive computation. The trade off between the performance and computing cost needs to be examined. The iterative substructure selection process, while potentially beneficial for accuracy, introduces significant computational overhead, making the model less practical for large-scale datasets or real-time applications. The memory usage is also a concern, as it limits the size of the molecules and datasets that can be processed.
3.	 (Ablation Experiment) Most experiments are designed well, but the experiment in line 1224 is less persuasive. Among all the datasets for the drug-drug interaction prediction task, ChChMiner has the fewest data points. Besides, since molecular interaction prediction tasks are different from DDI, a separate experiment would be good. The ablation study should be more comprehensive, including a wider range of datasets and tasks to fully assess the contribution of each component. The current ablation study is insufficient to draw strong conclusions about the generalizability of the model's components.
4.	 (Improvement) While IGIB-ISE achieves good performance, ISE fails to outperform all Category II methods in Table 1 (line 324) and some Category II methods in Table II (line 378). Also, the improvement of IGIB-ISE is not that noticeable in the classification task. The fact that ISE does not consistently outperform all baselines suggests that the substructure extraction process may not be universally effective. The limited improvement in classification tasks, despite the focus on substructure extraction, raises questions about the model's ability to capture the relevant features for classification.

### Questions
1. Please justify your assumption stated at line 161.
2. For Line 1224 Figure 5, why do you only choose to conduct the ablation study on the ChChMiner dataset? Ablation studies on larger datasets are needed.
3. Following your design, IGIB-ISE should effectively identify the core substructure of molecules, why did the model not improve the classification accuracy more? As it reduces redundant information, why does it occupy a larger space? More analysis is needed to identify factors that may limit the improvement. What are the potential enhancement may be introduced to address these limitations?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper describes a method to improve molecular relational learning using information theoretical loss functions on a subgraph of the molecules. The technical contribution lies in the coupling of graph information bottlenecks with expectation maximization. The results show the approach's superiority both in deductive and inductive scenarios. The method is well-motivated, and the experiments are solid.

### Strengths
(S1) The paper solves a timely problem and presents a sound solution that fully exploits the relationships among substructures.

(S3) Due to its substructure alignment, IGIB-ISE outperforms previous techniques on several datasets.

(S3) The method is well-motivated and builds on previous graph information bottlenecks, ELMO and expectation maximization.

### Weaknesses
(W1) Missing explicit objective function: The paper first explains the solution and then reaches the objective in Equation 8. I find this presentation counterintuitive. Why not present the objective first and then explain how to compute it?

(W2) In the modelling of the graph there is no feature vector associated with nodes/edges. Are the graphs without attributes? Molecules should have information about the type of bonds among atoms.

(W3) Notation without introduction: The paper uses notation without introducing it. Examples include:

- $\mathbf{Y}_\mathcal{G}$
- Line 216: the symbol *, is it a matrix multiplication?
- $\||$ in line 218

(W4) If sim is symmetric cosine similarity, what is the need for computing both $sim(F_1, F_2)$ and $sim(F_2, F_1)$?

(W5) It is not clear how Eq. 5 ensures that the two structures are aligned since $H_1$ and $H_2$ refer to two different embeddings spaces, or is the alignment enforced by the two matrices $I_{12}, I_{21}$? Please explain and motivate.

(W6) What is the Gumbel sigmoid and how does it help in this case?

(W7) It is not clear whether Eq. 16 is a lower bound on Eq. 8 or what is the relationship with Eq. 8? Is that an approximation or a heuristic? This aspect should be clarified in the text.

(W8) In Figure 4, the focus of the network substantially changes over iteration. This seems to indicate that the method struggles with convergence. Is that expected or is it a sign of instability?

### Questions
In general, the paper is a solid contribution but the presentation should improve. Please answer to my questions above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Iterative Substructure Extraction (ISE) framework for molecular relational learning, addressing how molecules interact through their core substructures. The framework combines an Expectation-Maximization algorithm for iterative refinement with a new Interactive Graph Information Bottleneck (GIB) theory to ensure extracted substructures are minimal yet influential. Through experiments on datasets covering both regression and classification tasks, the combined IGIB-ISE approach demonstrates improved accuracy and interpretability compared to existing methods for predicting molecular interactions.

### Strengths
- The paper presents a novel approach to molecular interaction learning. Rather than handling entire molecular structures or extracting substructures independently, it introduces an iterative refinement process guided by molecular interactions. 

- Using EM algorithms for substructure extraction is creative, treating substructures as latent variables that get refined through iterations. This is a fresh perspective on the molecular interaction learning problem.

- This work has a substantial potential impact on drug discovery and materials science. The ability to identify and understand interacting substructures between molecules is crucial for these fields.

### Weaknesses
The discussion of the limitations of Category II methods is confusing.

- It is understandable that core substructures often play a crucial role in molecular interactions. But, Figure 1 (a) does not deliver a relevant message to support this argument. 
- In addition, from Figure 1 (a), it is unclear why integrating the complete profile of an interacting molecule into the substructure generation can be overwhelming. 
- It's unclear why Category II carries the risk of compromising generalizability. After reading the cited paper [1], it's still very confusing. There is no clear evidence from [1] to support this statement. 
- It's unclear why the authors mention "Activity Cliffs" here.

Limited Discussion of Method Robustness.

Technical Clarity Issues.

- Line 160, what is Y_G? Should it be Y?
- In Tables 6-7, your method should be named ISE-IGIB or IGIB-ISE?

Computational Overhead.

- Tables 6 and 7 show IGIB-ISE takes more than 700% execution time and 1000% memory compared to one baseline DSN-DDI, with around 1.5% DDI performance improvement. I don't appreciate such results. The authors do not sufficiently address this limitation or propose potential optimizations. 
- The experiments focus on relatively small molecules. There is no discussion or analysis of how the method scales with molecular size, which is important for applications involving larger molecules.
The memory requirements (Table 6-7) suggest potential scaling issues.

### Questions
**1. The discussion of the limitations of Category II methods is confusing.** 
- It is understandable that core substructures often play a crucial role in molecular interactions. But, Figure 1 (a) does not deliver a relevant message to support this argument. 
- In addition, from Figure 1 (a), it is unclear why integrating the complete profile of an interacting molecule into the substructure generation can be overwhelming. 
- It's unclear why Category II carries the risk of compromising generalizability. After reading the cited paper [1], it's still very confusing. There is no clear evidence from [1] to support this statement. 
- It's unclear why the authors mention "Activity Cliffs" here. 

**2. Limited Discussion of Method Robustness.**
As an interactive method, what happens if the EM algorithm finds optimal solutions during iteration? The lack of guidelines for selecting optimal iteration numbers based on dataset characteristics leaves important practical questions unanswered.

**3. Technical Clarity Issues.** 
- Line 160, what is Y_G? Should it be Y?
- In Tables 6-7, your method should be named ISE-IGIB or IGIB-ISE?

**4. Computational Overhead.** 
- Tables 6 and 7 show IGIB-ISE takes more than 700% execution time and 1000% memory compared to one baseline DSN-DDI, with around 1.5% DDI performance improvement. I don't appreciate such results. The authors do not sufficiently address this limitation or propose potential optimizations. 
- The experiments focus on relatively small molecules. There is no discussion or analysis of how the method scales with molecular size, which is important for applications involving larger molecules. 
The memory requirements (Table 6-7) suggest potential scaling issues.

[1] Mechanisms of drug combinations: interaction and network perspectives

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a framework called ISE to improve MRL by focusing on the interaction between core substructures of molecules. The model iteratively refines the core substructures using the EM algorithm. Additionally, the IGIB theory is proposed to capture minimal but most influential substructures, enhancing the efficiency and generalizability of the extraction process. Through extensive experiments, the IGIB-ISE framework demonstrates superior performance compared to existing methods in terms of accuracy, generalizability, and interpretability for molecular interaction prediction tasks.

### Strengths
1. This paper introduces an innovative method for core substructure extraction using the EM algorithm, which effectively captures molecular interactions.

2. IGIB theory ensures a precise and compact extraction of interactive substructures.

3. The method is extensively validated across various molecular relational learning tasks, including drug-drug interaction and solvation energy prediction, showing clear improvements over state-of-the-art methods.

### Weaknesses
1. **Some parts of this work is very similar to [1]**. The key idea and many formulas are similar. For example, they all utilize similar methods to extrapolate core substructures (Section 3.4 in this paper and Section 3.2 in [1]). The only difference here seems to be this paper extrapolates the core substructure from a pair of graphs while [1] extrapolates the core substructure from one graph.

1. The framework is validated on interactions between two molecules. It does not extend to more complex scenarios like multi-molecule interactions, which are important in real-world biochemical environments.

2. The method requires more iterations, increasing resource consumption and time. This may limit its scalability for very large datasets or complex molecular systems.

### Questions
1. Can the authors validate the interactions between multi-molecule interactions?

2. Why the interaction is computed as $H_1=F_1^{(1)}||F_1^{(2)}$?

3. The way to extrapolate the core substructure is **very similar to [1]**. What's the difference between this paper and [1]?

4. What's the complexity of the method? Can you compare the training and inference time with baselines?

5. Can you validate your method on larger datasets?

[1] Capturing substructure interactions by invariant Information Bottle Theory for Generalizable Property Prediction

### Soundness
3

### Presentation
2

### Contribution
2
