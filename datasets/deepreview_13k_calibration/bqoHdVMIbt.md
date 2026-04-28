# Multimodal Unsupervised Domain Generalization by Retrieving Across the Modality Gap

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
\vspace{-0.5em}

Domain generalization (DG) is an important problem that learns a model which generalizes to unseen test domains leveraging one or more source domains, under the assumption of shared label spaces. However, most DG methods assume access to abundant source data in the target label space, a requirement that proves overly stringent for numerous real-world applications, where acquiring the same label space as the target task is prohibitively expensive. For this setting, we tackle the multimodal version of the \emph{unsupervised domain generalization} (MUDG) problem, which uses a large \emph{task-agnostic unlabeled} source dataset during finetuning.
Our framework does not explicitly assume any relationship between the source dataset and target task. Instead, it relies only on the premise that the source dataset can be accurately and efficiently searched in a joint vision-language space.
We make three contributions in the MUDG setting. 
Firstly, we show theoretically that cross-modal approximate nearest neighbor search suffers from low recall due to the large distance between text queries and the image centroids used for coarse quantization.
Accordingly, we propose \emph{paired k-means}, a simple clustering algorithm that improves nearest neighbor recall by storing centroids in query space instead of image space.
Secondly, we propose an adaptive text augmentation scheme for target labels designed to improve zero-shot accuracy and diversify retrieved image data.
Lastly, we present two simple but effective components to further improve downstream target accuracy. 
We compare against state-of-the-art name-only transfer, source-free DG and zero-shot (ZS) methods on their respective benchmarks and show consistent improvement in accuracy on 20 diverse datasets

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Multimodal Unsupervised Domain Generalization (MUDG), a novel framework that leverages large-scale unlabeled datasets (like LAION-2B) to improve model generalization on target domains. The paper makes three main contributions: (1) proposing paired k-means algorithm to improve cross-modal retrieval accuracy by updating centroids in query space rather than image space; (2) designing an unsupervised text augmentation scheme that adaptively selects appropriate descriptors for target labels; and (3) introducing a clustering-based sample selection strategy and diversity-preserving loss function to construct more representative training datasets. The method demonstrates significant improvements over existing zero-shot learning and source-free domain generalization baselines across 20 diverse datasets.

### Strengths
1. The paper proposes a novel MUDG framework that effectively leverages large-scale unlabeled datasets for domain generalization through cross-modal retrieval and adaptive text augmentation.
2. The paired k-means algorithm effectively addresses the modality gap in cross-modal retrieval, supported by rigorous theoretical analysis and empirical validation.
3. Extensive experiments across 20 diverse datasets demonstrate significant improvements over state-of-the-art baselines in zero-shot learning and domain generalization, showing strong practical value.

### Weaknesses
1. While the paper introduces MUDG as a new paradigm beyond UDG, it would benefit from a visual comparison/illustration showing the differences between DG, UDG, and MUDG. Moreover, the necessity and practical benefits of this new task definition are not sufficiently justified - authors should more explicitly demonstrate why existing frameworks like UDG are inadequate and how MUDG addresses real-world challenges.
2. In this paper, authors explore a way to retrieval task-agonistic source dataset to assist in model learning in the target domain. What is the intuition behind this operation? Is the assumption reasonable?
3. The writing of the Introduction Section is confusing: authors present a group of operations and six contributions in the section of introduction. However, what is the core challenge and the corresponding solution method proposed in this paper?

### Questions
For detailed questions and suggestions, please refer to the Weaknesses section

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
This paper presents a novel approach to multimodal unsupervised domain generalization (MUDA), where the source data is both unlabeled and task-agnostic. First, it theoretically examines the issues with existing cross-modal approximate nearest neighbor search methods. Next, it proposes a paired k-means algorithm to enhance neighbor search efficiency. Finally, we introduce a text augmentation scheme aimed at improving zero-shot accuracy.

### Strengths
1.The paper introduces the MUDG setting and presents a novel paired k-means algorithm to address the cross-modal nearest neighbor problem.

2.The paper provides a thorough theoretical analysis demonstrating the limitations of existing cross-modal nearest neighbor methods, supported by extensive experimental validation

3.Figures are effectively used to illustrate empirical observations, the improvements brought by paired k-means, and the visualization of Voronoi cells, enhancing the understanding of the proposed method.

### Weaknesses
1.The paper compares MUDG setting to zero-shot (ZS) and source-free domain generalization (SFDG) setting in Tables 1. ZS and SFDG impose more stringent conditions, while MUDG relies on task-agnostic source data, making it less practical in some contexts. Therefore, comparing MUDG methods with SFDG or ZS methods may not be entirely fair.

2.The paper lacks a comparison of the computational resources and time required by its proposed method in relation to other SFDG and ZS methods. Since this setting involves large-scale datasets during training, it may significantly increase the computational resources and time needed

3.In Table 2, the proposed method shows only a slight increase of 0.6% compared to the second-best method.

4.In the ablation experiments (Table 5), when adaptive augmentation is used alone, there is a drop of about 1%, with some datasets not even reaching that. This indicates that the paired k-means method, which is the main contribution of this work, is not effective.

### Questions
In Table 3, there are no MUDG methods included. Could you combine the PromptStyler method with the proposed methods for a fair comparison?

### Soundness
2

### Presentation
3

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
This paper presents a novel approach to multimodal unsupervised domain generalization that leverages a large unlabeled source dataset for finetuning, without requiring a direct relationship with the target task. Key contributions include (1) a theoretically derived paired k-means algorithm that enhances nearest neighbor recall, (2) an adaptive text augmentation scheme to improve zero-shot accuracy, and (3) two additional components that boost target accuracy. Experimental results demonstrate consistent accuracy improvements across 20 diverse datasets.

### Strengths
This paper is well-motivated and appears to be reproducible based on the author's code. The author discusses the challenges of cross-modal retrieval from a theoretical perspective and proposes methods to address the issue of low recall. Additionally, the author proposes an adaptive text augmentation scheme to tackle unsupervised domain generalization in multimodal contexts. Comprehensive analyses, comparative experiments, and insightful visualizations highlight the appropriateness of the method's genuine effectiveness.

### Weaknesses
1. While the methodology appears to be fundamentally solid, my primary concern regarding this paper is the clarity of expression and how it affects overall readability. Several figures in the paper, such as Figure 1, present ambiguous meanings, and others, like Figures 4 and 5, lack sufficient quality. Additionally, there are issues with the details in the descriptions, including an overuse of abbreviations and numerous typos in the introduction. These factors contribute to a challenging reading experience for the audience.
2. I believe a more detailed introduction to the task setting and motivation is necessary. Although the author mentions that MUDG is more practical, it seems to be primarily a combination of text-image representation and UDG. Could the author elaborate on specific application scenarios?
3. In terms of retrieval, I’m curious why only the first-level k-means is utilized instead of employing a fine quantization scheme at the second level. What are the implications of this choice, and might it impact the recall rate?
4. In Table 2, the proposed method does not seem to achieve superior performance across many datasets. Given that MUDG is being addressed so specifically, what could explain the lack of a more significant effect? What might be the underlying reasons for this?
5. Lastly, regarding the key hyper-parameters listed in Table 9, how are these parameters determined? Are they sensitive to variations, and how do they influence the performance of the method? This aspect warrants further discussion.

### Questions
See 'weakness' for details. A more thorough introduction to the motivation and clarification of the methods are needed. If the author can improve the presentation of the paper in the next version, I would be happy to raise my score!

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies multimodal unsupervised domain generalization (MUDG), where only task-agnostic source data and target label names are required. Accurate yet diverse retrieving image samples that match the specific text description for a certain class name becomes the crux. Towards the former, the authors propose paired k-means, maximizing the probability of a text query and its closest image sample belonging to the same Voronoi cell by updating the centroids to be in the query distribution. As for the latter, the authors develop a heuristic augmentation strategy. Experiments under various evaluation protocols demonstrate the effectiveness of the proposed method.

### Strengths
- This paper is well-written overall, and the motivation is quite reasonable.
- Each proposed component is supported by sufficient theoretical and empirical analysis.
- Experiments are sufficient.

### Weaknesses
 - Table 1 should be placed before Figure 1 as Table 1 was mentioned before Figure 1.
- The bottom right subfigure of Figure 1 was an illustration. Could you provide a quantitative comparison between good augmentation and bad ones (such as using t-SNE visualization)?
- Ablations in Tables 4 and 5 can not reflect the effectiveness of each component, as the improvements are marginal. Could you report the results of statistical testing to see if the improvements are significant or not?

### Questions
I have no further questions. Please refer to the "Weaknesses" section.

### Soundness
4

### Presentation
3

### Contribution
4
