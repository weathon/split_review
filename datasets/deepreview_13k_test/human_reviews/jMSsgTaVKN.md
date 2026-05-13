# Leveraging metapaths for learning from knowledge graphs in the context of vision-based classification of object states

- Decision: Reject
- Scores: 3, 5, 3, 5, 5

## Abstract
Zero-Shot Object State Classification (ZS-OSC) aims to recognize unseen object states without any visual training examples. Existing methods typically rely on Knowledge Graphs (KGs) to provide semantic information about states, but they often treat KGs as homogeneous, overlooking the rich relational knowledge encoded in their structure. We propose a novel approach to ZS-OSC that leverages meta-paths to capture complex relationships between object states in a KG. Our method learns to project semantic information from the KG into the visual space via meta-path learning, generating discriminative visual embeddings for unseen state classes. To the best of our knowledge, this is the first work to utilize meta-paths for ZS-OSC. We conduct extensive experiments on four benchmark datasets, demonstrating the superior performance of our approach compared to SoTA zero-shot learning methods and a graph-based baseline. Our ablation study further provides insights into the impact of key design choices on the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims at zero-shot object state classification (ZS-OSC). The authors propose a novel approach for ZS-OSC that leverages meta-paths to capture complex relationships between object states in a knowledge graph.

### Strengths
- Considering the relational knowledge encoded in knowledge graphs for zero-shot object state classification is promising.

### Weaknesses
- The writing is poor. The organization of introduction could be improve for a more clear motivation. The task of ZS-OSC could be first introduced.
- It could be better to first present the comparison results in the section of experiments.
- No other methods for exploiting the relational information within KGs (such as filtering mechanisms, ad-hoc KG construction, or random walks) are compared
- The improvement is not obvious. Besides, did the authors run the experiments multiple times to obtain the mean results?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The motivation of this paper is quite unclear. The essence of its method is not much different from the baseline selected by the authors. However, this paper fails to point out what makes it unique compared to other KG-based methods, or to highlight the limitations of other approaches that this paper addresses. Therefore, the motivation of this paper is quite weak, which will significantly impact my final evaluation.

### Strengths
The Presentation of this paper is good.

### Weaknesses
1. The motivation of this paper is quite unclear. The essence of its method is not much different from the baseline selected by the authors. However, this paper fails to point out what makes it unique compared to other KG-based methods, or to highlight the limitations of other approaches that this paper addresses. Therefore, the motivation of this paper is quite weak, which will significantly impact my final evaluation.

2. While an ablation study is presented, it only explores a narrow set of hyperparameters related to meta-path length, the number of softmax channels, and learning rates. Other critical factors such as embedding dimensions, network depth, and the impact of different types of meta-paths are not examined. Additionally, the study does not provide insights into the underlying reasons for the observed performance changes, limiting its usefulness in understanding the model's behavior.

3. The comparison is limited to a baseline graph-based method and a few large pre-trained models, without including other relevant state-of-the-art methods in zero-shot learning or knowledge graph utilization. The analysis of the results is superficial, lacking in-depth discussion on why the proposed method performs better and under what conditions it might fail.

### Questions
Please refer to "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper delves into Zero-Shot Object State Classification, introducing meta-path learning to enable heterogeneous modeling within a knowledge graph. Unlike existing approaches that focus solely on homogeneous modeling, this work showcases the effectiveness of the proposed methodology through experimental validation.

### Strengths
The incorporation of heterogeneous modeling is a pivotal step forward in object state classification and zero-shot object state classification. This innovative approach represents a promising direction for advancing the field.

### Weaknesses
It appears that the clarity of the paper is a critical issue, hindering comprehension even for experienced researchers in the field of computer vision. Improving the accessibility and clarity of the manuscript is crucial before considering it for publication. Here are some key areas for improvement:
1. The authors should dedicate space to formally define the zero-shot Object State Classification problem within the paper. Given its relevance in the current landscape, a comprehensive definition in the methodology section is essential. Additionally, providing detailed explanations about Object State Classification, including its inputs and outputs, would enhance understanding.
2. Although the paper elaborates on learning a meta-path-based graph network, it falls short in clearly articulating how this network is applied in object state classification and zero-shot object state classification.
3. While heterogeneous modeling is deemed critical for object state classification, the paper lacks substantial evidence to support the assertion that meta-path learning effectively introduces heterogeneous information. The motivation behind choosing meta-path learning over other techniques remains insufficiently justified. Including experimental comparisons with alternative methods could strengthen the argument.
4. The authors should address why meta-path learning specifically benefits zero-shot Object State Classification. While heterogeneous modeling is crucial for object state classification, the connection between meta-path learning and the zero-shot context needs clarification.

### Questions
In addition to addressing the above points, it is advisable for the authors to conduct a thorough limitation analysis and present qualitative results to enhance the comprehensiveness of their work.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors propose a new method for ZS-OSC that utilizes meta-paths to capture complex relationships between object states in KGs, and then projects the semantic information in KGs into the visual space to generate visual embeddings for unseen state categories for zero-shot object state classification. The method in this paper shows competitive results on four datasets.

### Strengths
+ The structure of the article is clear and logical. Especially in the experimental part, the authors clearly show the results of the ablation experiments and the corresponding analysis.

+ The proposed method shows excellent performance in several datasets. For example, it outperforms the baseline method by 5.4% and 6.5% on the MIT-States and VAW-States datasets, respectively.

### Weaknesses
- In the related work, the authors focus on the current state of research and challenges in attribute classification, while the research on state classification is skipped. We are curious about the detailed analysis of the current state of research and key challenges in state classification, otherwise, this would not justify the author's statement “This highlights a need for dedicated methods tailored to the unique challenges of state recognition”.

- As the authors note, existing ZSC methods primarily address a CZSL variant of the problem, which generalizes to unseen combinations of object and state primitives by learning the compositionality of object and state primitives from the training set. This approach is clearly more reasonable than focusing only on state classification, since isn't state classification ultimately in the service of object classification? Could the authors please clarify what is the point of focusing only on state categorization? Alternatively, are the authors trying to show that state categorization can be achieved without relying on prior knowledge of object categories? Could the authors please focus on the uniqueness of this study that distinguishes it from existing studies on ZSC, other than the introduction of meta-path learning?

- The authors are advised to elaborate on the meta-path selection process, including how meta-paths are identified based on the structure of the knowledge graph and task requirements, and how the effectiveness of different meta-paths is evaluated. The authors mention in the conclusion that the approach in this paper utilizes the structure of KGs and visual embedding to guide the learning of meta-paths, but this is not clearly reflected in the methods section.

- The authors' key rationale for introducing meta-path learning into zero-shot object state classification is that meta-path learning can effectively capture and utilize specific semantic relationships in KGs, but there is no analysis of the rationale and a lack of corresponding visual representation. In addition, I can't see the changes in the features of the GTN trained based on meta-path learning when it is used in object state classification. Case studies demonstrating how meta-path learning helps in classifying challenging examples.

- Figures are less readable. For example, the font in Figure 1 is too small to read.

### Questions
All the doubts are mentioned in the weaknesses. It should be emphasized that the authors should focus on explaining the rationale of metapaths for capturing complex semantic information. In addition, authors should prove in more forms that the introduction of meta-path learning indeed produces “informative and discriminative visual embeddings”, as this is the core point of the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a  Zero-Shot Object State Classification (ZS-OSC) method by leveraging metapaths in knowledge graphs (KGs) to capture and utilize the rich relational information encoded within their structure. The proposed method aims to recognize unseen object states without any visual training examples, addressing a key challenge in zero-shot learning. Extensive experiments conducted on four benchmark datasets demonstrate that the proposed approach outperforms a baseline method.

### Strengths
+ Leveraging meta-paths to capture complex relationships to learn a zero-shot representation seems reasonable.
+ The experimental results show the effectiveness of the proposed approach on conventional ZS-OSC.

### Weaknesses
- The related work section has a high degree of overlap with the baseline method [r1], especially in the "Zero-shot Classification" part. Additionally, there is a lack of in-depth analysis regarding ZSL, and the references are not up-to-date.
- The paper lacks experiments in a generalized ZS-OSC setting, which is more challenging and more reflective of real-world scenarios. [r1] performed the experiments.


[r1] Leveraging knowledge graphs for zero-shot object-agnostic state classification.

### Questions
- How were the experimental results for the other methods in Table 4 generated? Why do the vision-language model-based methods perform worse than the CNN-based method proposed in this paper?
- What are the practical applications of ZS-OSC? How does it differ from classical zero-shot learning or compositional zero-shot learning?
- Line 349, 'CN‘s' is so bad.
- Please follow the ICLR  standards for mathematical notations, such as Line 325.

### Soundness
2

### Presentation
2

### Contribution
2
