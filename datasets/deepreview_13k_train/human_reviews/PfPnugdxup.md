# From Molecules to Materials: Pre-training Large Generalizable Models for Atomic Property Prediction

- Decision: Accept
- Scores: 5, 5, 8, 5

## Abstract
Foundation models have been transformational in machine learning fields such as natural language processing and computer vision. Similar success in atomic property prediction has been limited due to the challenges of training effective models across multiple chemical domains. To address this, we introduce \methodname{} (\method{}), a supervised pre-training strategy that simultaneously trains on multiple datasets from different chemical domains, treating each dataset as a unique pre-training task within a multi-task framework. Our combined training dataset consists of $\sim$120M systems from OC20, OC22, ANI-1x, and Transition-1x. We evaluate performance and generalization by fine-tuning over a diverse set of downstream tasks and datasets including: QM9, rMD17, MatBench, QMOF, SPICE, and MD22. \method{} demonstrates an average improvement of 59\% over training from scratch and matches or sets state-of-the-art on 34 out of 40 tasks. Our work highlights the potential of pre-training strategies that utilize diverse data to advance property prediction across chemical domains, especially for low-data tasks.
    Please visit \url{https://nima.sh/jmp} for further information.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the possibility of pre-training a foundation-style model over multiple chemical domains to generate transferable atomic representations for downstream fine-tuning tasks. The Joint Multi-domain Pre-training (JMP) strategy utilizes data from multiple chemical domains and achieves state-of-the-art results across many targets of various datasets. The paper establishes a comprehensive set of fine-tuning benchmarks across various chemical domains and tasks.

### Strengths
- Comprehensive set of fine-tuning benchmarks: The paper establishes a comprehensive set of fine-tuning benchmarks across various chemical domains and tasks, which enables researchers to evaluate the performance of their models against a standardized set of benchmarks.

- State-of-the-art results: The Joint Multi-domain Pre-training (JMP) strategy achieves state-of-the-art results across many targets of various datasets, which demonstrates the effectiveness of the proposed approach.

- Large and diverse molecular datasets: The paper highlights the importance of large and diverse molecular datasets in enabling the development of accurate and efficient models for atomic property prediction.

- Different model sizes: The paper provides multiple model sizes with pretrained checkpoints that can benefit real-world deployment at different resource levels and potentially accelerate research progress in related fields.

### Weaknesses
 - The paper claims that the proposed pre-training method is model-agnostic. However, the only evaluated architecture backbone is GemNet-OC. It would be better to have a variant pre-trained using other types of model backbones, such as a graph transformer or a simpler GNN, to conduct further comparison and analysis. This would more convincingly demonstrate the general applicability of the pre-training strategy.

- The novelty is a bit limited. I admit that this paper contributes on providing the empirical evidence that pre-training cross-domain molecule data can benefit multiple downstream tasks. However, the techniques used in this paper are either introduced by other literature or very simple and straightforward. No novel methods/theories are introduced. The core idea of multi-domain pre-training is not new, and the specific implementation details lack significant innovation. I would recommend this paper submit to more domain-related or comprehensive journals.

- This paper claims that many previous efforts on pretraining molecules focus on a specific domain which ignores the information provided by other domains and generalizability. It would be better to provide more empirical evidence that compares the proposed model with other pre-training methods. The comparison should include methods that also leverage multi-domain data, if available, or at least show a clear advantage over single-domain pre-training baselines.

- More supervised SOTA should be compared. E.g., for the materials domain, there are two more recent papers [2, 3] that can be reported against the proposed method. The current comparisons are not sufficient to establish a clear state-of-the-art performance, especially considering the rapid advancements in materials property prediction.

- I understand the concerns of releasing the code and models before acceptance. However, in terms of reproducibility, it would be better to provide an anonymized repo including some demo models for testing purpose. This would allow other researchers to verify the claims and build upon the work more easily.

### Questions
- Can you provide more details about the scaling strategy of the model architecture? The message-passing paradigm suffers from over-smoothing a lot and it is notorious of hard to make the network deep. I would like to understand more about this and how this method overcome the issues.

- Since for larger foundation models, we would like to include far more parameter. But the molecular graphs often just include a very small number of vocabularies. A better strategy could be adding full attention mechanism to make the parameter space larger. And the model would be a transformer-based architecture or so-called "graph transformer". Did the authors try this in their experiments? How did the two frameworks perform?

- This paper claims that they can deal with OOD challenge and cross-domain adaption better and they can benefit drug discovery, etc. So I would like to see more results on how this method perform on other therapeutics data [4], e.g., the molecule property predictions (toxicity, solubility, lipophilicity, etc.) on MoleculeNet [5].

[4] Huang, K., Fu, T., Gao, W. et al. Artificial intelligence foundation for therapeutic science. Nat Chem Biol 18, 1033–1036 (2022). https://doi.org/10.1038/s41589-022-01131-2

[5] Wu, Zhenqin, et al. "MoleculeNet: a benchmark for molecular machine learning." Chemical science 9.2 (2018): 513-530.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper pretrains a large generalizable model for atomic property prediction, which outperforms SOTA methods on many downstream tasks.

### Strengths
1. The model achieves exceptional performance.
2. The experiments conducted in this study are comprehensive and thorough, covering various aspects such as hyper-parameter settings, ablation studies, and downstream tasks.
3. The authors carefully study the balance between different datasets and pre-training tasks, ensuring a comprehensive analysis of their impact.

### Weaknesses
1. The disscussion of the correlation between pre-training tasks and downstream tasks is missing. I am wondering what kinds of downstream tasks can be promoting by pre-training? 
2. The main contribution of this work is implemental and not suprising.
3. This paper confuses the prediction of atomic properties with the prediction of molecular properties.

### Questions
1. Does the use of JMP contribute to the prediction of molecular properties? If so, what specific types of molecular properties show improvements?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors explore the application of machine learning in predicting atomic properties across a wide array of applications, from healthcare to climate change. The authors introduce Joint Multi-domain Pre-training (JMP), a supervised pre-training strategy that leverages a vast dataset comprising approximately 120 million examples from multiple chemical domains. The primary goal of JMP is to generate transferable atomic representations that can be fine-tuned for diverse downstream tasks, addressing the challenge of generalizing across the extensive and complex space of molecular interactions.

### Strengths
Innovative Approach: The paper introduces Joint Multi-domain Pre-training (JMP), a novel supervised pre-training strategy that leverages a massive dataset from multiple chemical domains. This approach is innovative in its attempt to generate transferable atomic representations for a wide array of downstream tasks, addressing the challenge of generalizing across diverse molecular interactions.

Creative Combination of Ideas: The authors draw inspiration from successful practices in Natural Language Processing (NLP) and Computer Vision (CV), creatively applying the concept of large-scale pre-training to the domain of atomic property prediction. This cross-disciplinary innovation enhances the originality of the work.

Broad Applicability: The paper’s contributions have broad applicability across various domains, ranging from drug discovery to material science. The ability of JMP to generalize across diverse chemical domains signifies its potential to drive advancements in multiple fields.
Addressing a Critical Challenge: The paper tackles the critical challenge of generating transferable atomic representations in the vast and complex space of molecular interactions. By addressing this challenge, the paper makes a significant contribution to the field of machine learning for atomic modeling.

Computational Efficiency: The computational efficiency achieved through JMP, with over 12x faster fine-tuning compared to training from scratch, is a notable strength. This efficiency is crucial for practical applications, making the paper’s contributions highly significant.

### Weaknesses
Need for Broader Ablation Studies:
Issue: While the paper includes ablation studies to analyze the impact of different JMP components, these studies could be broadened to provide a more comprehensive understanding of the model’s behavior and the contributions of individual components.

### Questions
N/A

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a supervised pre-training strategy named JMP, which pretrains GemNet-OC on various small molecule data from multiple chemical domains. The pre-trained network acts as a foundational model, further finetuned for downstream atomic property prediction tasks. The authors’ major contribution is demonstrating that by pretraining exclusively on small molecules, the network can be finetuned on large molecule datasets, achieving state-of-the-art results. The primary technical advancements concentrate on refining each component of the standard deep learning pipeline, including data preprocessing and hyperparameter tuning. Experiments across 40 fine-tuning benchmarks are conducted to showcase the effectiveness of the method.

### Strengths
+ The paper is articulate and easily comprehensible. The authors provide an essential level of detail in describing their pipeline, facilitating a clear understanding of the processes. Although source code is not provided, the comprehensive details included in the paper should enable straightforward reimplementation.

+ The experiments presented in the paper are exhaustive and meticulous. A diverse array of molecular property datasets, encompassing both large and small molecules, has been utilized for the experiments. The authors have conducted extensive ablation studies, offering valuable insights into the influence of various hyperparameters used in the pipeline.

### Weaknesses
 - My primary concern lies in the paper’s technical contribution. The concept of building a foundational model for molecular property prediction tasks isn’t novel. A significant challenge is bridging the substantial domain gaps across various chemistry domains. The authors seem to emphasize that the proposed pipeline can effectively bridge the molecule size gap, allowing it to work efficiently on larger molecules even when only pretrained on smaller ones. However, molecule size is just one of several apparent factors—and likely among the simpler ones—causing the domain gap. More complex factors, such as intrinsic differences in the distribution of graph structures, the diversity of chemical bonding motifs, and issues related to data availability, are not addressed in the paper. Consequently, it is challenging to be convinced that the proposed method significantly contributes to foundational models or represents "an important step for universal ML potential," as claimed in the introduction.

- The improvement brought by the proposed method appears to be mainly attributed to hyperparameter tuning. The network architecture itself isn’t novel, and the loss function closely resembles commonly used ones, albeit with slight modifications to some coefficients. My overarching impression is that the authors engage extensively in manual hyperparameter tuning, which doesn’t offer substantial insights to propel further research advancements. While I acknowledge the empirical enhancements demonstrated through comprehensive experiments, it is still challenging to bestow a favorable overall evaluation on the paper.

### Questions
1. In Sect. 4.1, concerning Data Normalization, the authors have chosen to normalize the property values per dataset. A lingering question is how the output of the NN is transformed. Is the transformation still dependent on each specific dataset? If that is the case, it seems impractical for real world applications where a novel molecule is given, and it would be indeterminable as to which "dataset" it inherently belongs to and how to transform its output.

2. Regarding Dataset Size Imbalance, I was wondering if the authors considered utilizing loss reweighting as opposed to data reweighting. By loss reweighting, I am referring to the approach of uniformly sampling the data but adjusting the coefficients of each sample to p_d (ensuring normalization across each batch).

3. I devoted a significant amount of time attempting to digest whether each term in Eq.1 is a novel contribution or a previously introduced one. It would be beneficial if the authors could provide clearer definitions of each symbol used, elaborate more distinctly on the novel improvements introduced in this paper, and add a period to the end of the equation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
