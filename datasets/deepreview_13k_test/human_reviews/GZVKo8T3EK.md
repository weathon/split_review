# ProvCreator: Synthesizing Graph Data with Text Attributes

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
In cybersecurity, system provenance graphs are a key primitive to support intrusion detection and program identification tasks. Recent movement towards using data-hungry graph learning models for security-critical applications has exposed significant limitations in existing provenance datasets. Imbalanced representation of programs induces bias and performance degradation in downstream models. Further, these models rely on rich numeric and textual node attributes to accurately encode program behaviors, limiting the ability of existing data augmentation techniques to address data imbalance in provenance graphs.

We present PROVCREATOR, a novel graph synthesis framework designed for feature-rich system provenance graphs. PROVCREATOR learns the joint distribution of node attributes and graph structures conditioned on program class labels, enabling targeted generation of realistic system provenance graphs to supplement underrepresented programs. Our evaluation shows that PROVCREATOR produces provenance graphs with higher structural fidelity, attribute fidelity, and downstream utility compared to those of previous graph synthesis methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
ProvCreator provides a framework designed to generate synthetic, feature-rich provenance graphs to address data imbalances in cybersecurity datasets. This is useful for intrusion detection and programming classification. Pre-existing datasets often lack representation of certain program behaviors. ProvCreator learns and generates graph structures and node attributes conditioned on program class labels, for synthetic graph generation using graph transformer-based diffusion approach for accurate synthesis. 

ML models trained on data augmented with PROVCREATOR's graphs outperform those using older graph synthesis methods in program classification and malware detection tasks. PROVCREATOR’s synthetic graphs demonstrate higher structural and attribute fidelity, ultimately supporting better model generalization and performance in security-focused applications.

### Strengths
The approach of learning both the graph structure and node attributes conditioned on program class labels sets this work apart. 
context-aware graph synthesis using diffusion is also a very interesting method. the flexibility to generate diverse text attributes tied to specific node types—addresses a gap in current provenance graph augmentation.

### Weaknesses
The need for text-based attributes conditioned on the graph's structure seems like a niche value-add, only relevant for training models that rely heavily on extremely specific node attributes to detect specific behaviors or patterns in cybersecurity applications. Your results of figure 5 and table 4 are promising in their extension of GDSS, but they are limited to two EXE files. This seems unusual - it might be more convincing to provide the results on a dataset of malware exe files, or something of that nature. 

For instance, adaptive malware or threat actors often modify behavior in subtle ways that challenge even high-fidelity graph synthesis. While this framework builds on diffusion-based methods, these methods often fall short when modeling highly dynamic and adaptive attack behaviors that are common in real-world cybersecurity scenarios. Diffusion-based approaches can struggle with capturing temporal dependencies or the evolving nature of interactions within system provenance graphs, which can limit their applicability to detecting sophisticated, adaptive threats. That’s why other work has turned to methods that incorporate temporal modeling or hybrid architectures combining diffusion processes with recurrent or attention-based networks, which could provide more flexibility for handling complex, evolving data structures. 

It's always worth addressing the limitations of static analysis, which can miss context-sensitive behavior or runtime characteristics that only emerge during execution. 

Scalability is another area that needs more attention. While PROVCREATOR shows results in generating complex, high-fidelity graphs, the paper doesn’t dive into the potential computational costs involved, especially as datasets scale up. Generating graphs with detailed structure and attributes can become resource-intensive, raising questions about runtime efficiency and memory usage in larger, real-world applications. A clearer analysis of how PROVCREATOR handles these demands, or what optimizations could be implemented to make it more scalable, would go a long way in proving its viability for real-world cybersecurity operations where resources are always a factor.

### Questions
Do you think integrating some form of temporal modeling could help address the limitations in capturing dynamic behavior?

"While our work only considers static attribute sets for each node type, PROVCREATOR’s architecture naturally allows for dynamically determined node attribute sets using flexible attribute indicators." - could you elaborate? did you do any experimentation for this?

"The original GDSS paper (Jo et al., 2022) uses a GCN as the backbone and it does not consider conditional generation. We improved the backbone model by using a graph transformer (Dwivedi & Bresson, 2020) and following the original stable diffusion (Rombach et al., 2021) paper’s approach to add the conditioning mechanism for the graph transformer. The condition is set based on the label of the process represented in the graph; details about the labels can be found in §A.1." could you please emphasize how your work significantly differs from prior work, especially from GDSS?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ProvCreator, a graph synthesis framework specifically designed for feature-rich system provenance graphs within the cybersecurity domain. ProvCreator uniquely integrates the generation of graph structures with the prediction of node attributes by learning their joint distribution, thereby addressing the issue of underrepresented programs. The evaluation demonstrates that ProvCreator produces graphs with higher structural fidelity compared to the previous work it extends and enhances performance in subprogram classification tasks.

### Strengths
1. **Originality**: This work first considered together graph structure generation and attribute generation using joint training. The evaluation showed the approach benefited in some aspects.
2. **Significance**: This work researched a critical question.

### Weaknesses
1. **Unclear motivation**: The authors did not explain the reasonableness of combining graph structure generation and attribute generation together. I would liek to see further explanation rather than only mentioning that "neighborhood structures are often statistically codependent with node attributes."

2. **Unclear approach description**: The approach should be explained in more detail in section 3. As the authors claimed that they improved the backbone model and first used joint training in this field, the overall model architecture and the formula of joint loss function should be emphasized. 

3. **Few baselines**: This work only chooses GDSS as its baseline. More previous works should be selected and compared, e.g., EDP-GNN[1], GraphEBM[2], etc. Besides, this work conducts experiments on a specific field and focuses on overcoming the data imbalance, so straightforward oversampling should also be considered as a baseline to show the meaningfulness of synthesis in this scenario.

4. **Few evaluated scenarios**: For graph similarity measures, only `svchost.exe` and `powershell.exe` in the Windows environment were evaluated. The generalization among different scenes and OSs was not proven.

5. **Questionable experiment design**: The overall performance of graph similarity was never compared with previous works because part of the baseline approach was replaced with random selection. The baseline would have more persuasiveness using previous works or self-constructed approaches from previous works, e.g., the evaluation in [3].

6. **No ablation experiment**: Ablation experiments correlated with novel aspects of this approach should be done, e.g., the adjustment of the backbone model and joint training.
----
1. Niu, Chenhao, et al. "Permutation invariant graph generation via score-based generative modeling." International Conference on Artificial Intelligence and Statistics. PMLR, 2020.
2. Liu, Meng, et al. "Graphebm: Molecular graph generation with energy-based models." arXiv preprint arXiv:2102.00546 (2021).
3. Chen, Xu, et al. "Node Attribute Generation on Graphs." arXiv preprint arXiv:1907.09708 (2019).

### Questions
1. For graph similarity measures, only `svchost.exe` and `powershell.exe` in the Windows environment were evaluated. Could you please provide some evidence of this work's generalization among different scenes and OSs?
2. It Seems like ProvCreator performed better than GDSS in the Malware Detection downstream task. Were there any correlations between the features of ProvCreator synthesized training data and newly solved test cases?

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
2

### Summary
This paper presents PROVCREATOR, a graph synthesis framework tailored for system provenance graphs, which addresses the critical issue of data imbalance in cybersecurity datasets by generating synthetic, balanced data that accurately reflects underrepresented program behaviors. By jointly learning the distribution of graph structures and node attributes conditioned on program class labels, ProvCreator not only mitigates systematic bias but also significantly enhances the performance of downstream ML models in classification and intrusion detection tasks. Furthermore, its flexible text attribute generation capability allows for the synthesis of diverse and contextually relevant attributes, making it a powerful tool for improving the reliability and effectiveness of security-critical applications that rely on rich graph attributes.

### Strengths
1. The paper addresses a critical and relevant topic.
2. The overall writing and structure are clear and coherent.
3. Experimental results demonstrate that the proposed method achieves promising effectiveness.
4. The authors provide code and data, which supports reproducibility.

### Weaknesses
1. While the paper thoroughly demonstrates the method's effectiveness, it lacks a discussion and experimental analysis of the method's efficiency and resource consumption during training. These aspects are essential for a comprehensive assessment of the method's practical utility. Additionally, I suggest that the authors include detailed parameter configurations used in the experiments to aid in replicability.
2. The paper heavily relies on domain knowledge in network security, which may make certain aspects challenging for general readers to understand. For instance, in Figure 2, the term “Given a graph class label” might benefit from further clarification. Could the authors provide specific examples illustrating the exact inputs and outputs at each stage?
3. Table 4 indicates that, in Malware classification, adding generated traceability graphs appears to degrade classification accuracy. Could the authors explain the reasons behind this performance drop and provide additional clarification?

### Questions
1. Why does the addition of provenance graphs lead to a decrease in Malware classification performance?
2. Could the authors provide an example to illustrate each step of the process described in Figure 2, including the exact form of the generated content at each stage?

### Soundness
3

### Presentation
2

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
This paper addresses a fundamental data imbalance challenge in provenance graph construction -- different variations of syscalls are not equally represented in datasets, thus making it difficult for ML to model the nuances accurately. They propose ProvCreator to synthesize provenance graphs to oversample underrepresented versions of syscalls that still look similar enough to the original data.

### Strengths
This paper attempts to solve an important challenge for domains that suffer from imbalanced datasets. It is a one-shot approach to create both the graph structure and node attributes, which should arguably be cheaper than doing it individually (no supporting evidence though). The writing is clear.

### Weaknesses
The biggest weakness of this paper is the lack of correctness verification -- do the synthetic graphs even make sense? Are they realistic? Sure, checking whether graphs look structurally similar is one part of the evaluation but for the synthetic dataset to be useful in practice, it has to be semantically correct as well, which was never verified.

The malware detection downstream task is too shallow and vague to be useful to readers. Even the task "malware detection" is vaguely defined (see questions). Malware detection is an extremely challenging task, and for a baseline to achieve 100% F1-score almost always indicates that something has gone terribly wrong.

There is a fair amount of redundancy in the text (e.g., every time node attributes are mentioned, the same example set is used, ...). Once these are removed, there will be sufficient free space to provide examples of some of these synthetically created graphs.

### Questions
- One risk with oversampling works is that they create an inflated data distribution for the classes that naturally occur infrequently in practice. Having an unrealistic class distribution has a negative impact on generalization in open world settings. In this sense, why not embrace the imbalance and develop approaches that honour true class distributions? 

- As previously mentioned, there are no experiments to show the semantic correctness of the generated graphs. Did the authors see cases where edges between nodes were created that make no sense, or some node attributes created that have no real-world significance? For instance, the port numbers could be classic example as they have semantic meaning beyond being a number. Operations valid on port 443 are not necessarily valid on port 8898. How does the attribute generation approach handle such semantic irregularities?

- In regards to malware detection, what is the exact classification task? Is it a binary class classification (malware vs svchost) or multiclass classification (malware families vs benign processes). What makes the classification that easy for a baseline to achieve 100% F1 score (as in real world, it is never this easy)? 

- As far as I understand, the synthetic graphs are simply variants of graphs that already exist (no true generative approach). In this sense, how is this pipeline any better than, let's say, an evolutionary algorithmic approach? Are there benefits to a transformer-based approach that other popular "variant-creation" approaches lack? 

- In Sec 3.1, the adjacency matrix is represented as real numbers. Why is that? What does that mean in terms of provenance graphs where a process opens a file. What does the real number represent here?

- This paper claims to develop a method purely for cybersecurity applications, yet I do not see anything in the approach that suggests its application purely to one domain. Could the authors provide clarification on this point?

### Soundness
2

### Presentation
3

### Contribution
2
