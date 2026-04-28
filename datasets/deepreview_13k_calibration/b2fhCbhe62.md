# EmoGrowth: Incremental Multi-label Emotion Decoding with Augmented Emotional Relation Graph

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Emotion recognition systems face significant challenges in real-world applications, where novel emotion categories continually emerge and multiple emotions often co-occur. This paper introduces multi-label fine-grained class incremental emotion decoding, which aims to develop models capable of incrementally learning new emotion categories while maintaining the ability to recognize multiple concurrent emotions. We propose an Augmented Emotional Semantics Learning (AESL) framework to address two critical challenges: past- and future-missing partial label problems. AESL incorporates an augmented Emotional Relation Graph (ERG) for reliable soft label generation and affective dimension-based knowledge distillation for future-aware feature learning. We evaluate our approach on three datasets spanning brain activity and multimedia domains, demonstrating its effectiveness in decoding up to 28 fine-grained emotion categories. Results show that AESL significantly outperforms existing methods while effectively mitigating catastrophic forgetting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel framework, EMOGROWTH, designed for incremental multi-label emotion decoding. The authors address the challenge of real-world emotional dynamics by tackling multi-label class incremental learning (MLCIL), where emotions are represented as evolving, multi-label categories. The proposed approach leverages an augmented emotional relation graph (ERG) and integrates knowledge from affective dimensions, addressing both past-missing and future-missing partial label problems. Through comprehensive experiments on three datasets, the study demonstrates EMOGROWTH's effectiveness in improving emotion decoding accuracy and mitigating catastrophic forgetting in MLCIL scenarios.

### Strengths
1.	The introduction of the Augmented Emotional Relation Graph and the integration of affective dimensional knowledge are novel and valuable contributions to addressing the MLCIL problem in affective computing.
2.	The framework effectively mitigates catastrophic forgetting—a common issue in incremental learning—by employing knowledge distillation and label disambiguation.
3.	The framework is rigorously tested across three distinct datasets with multiple incremental learning protocols, providing strong evidence of its effectiveness.

### Weaknesses
1.	Since the authors claim to have introduced "the problem of multi-label class incremental emotion decoding" as part of their contributions, they should provide a more detailed explanation of this problem. Currently, the example in Figure 1 and the associated description make the concept challenging to grasp. Specifically, the notion of how the model evolves across tasks while maintaining a single set of parameters for all emotion categories is unclear. The description lacks a concrete explanation of how the model's parameters are updated to accommodate new emotion categories without catastrophically forgetting previously learned ones. The example in Figure 1, while illustrating the multi-label and incremental aspects, does not clearly show the technical challenges of parameter sharing and knowledge retention in this specific context.

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
## Summary:
This paper introduces the problem setting of multi-label class incremental learning (MLCIL) for emotion detection and classification. While, MLCIL has been studied for other tasks, this is the first proposal for emotion decoding. The key components of the approach are:
1. An **emotional relational graph (ERG)** is maintained across all training tasks. This ERG maintains emotion label co-occurence relations and uses it alongside a Graph Isomorphism Network (GIN) based graph autoencoder (GAE) to build and update node (emotion) embeddings. GIN essentially uses sum aggregation over neighboring nodes to build representations of each node. The autoencoder loss used here is a pairwise decoder loss. Adjacency matrix is used with self-loops (by adding the identity matrix) when calculating this loss. 
2. Cross attention between the input and the emotion embeddings (both with their own MLP weights) is used for the final multiclass embeddings per input example in Training task b. This is what is called **semantic-guided feature decoupling** in the paper. 
3. **Past-missing partial label problem** is discussed where the new data in task b is missing old labels. Here the paper aims to go beyond the soft-labeling that can be done by the existing model from task (b-1). The approach proposed is to start with these soft-labels from (b-1) but then use standard iterative label propagation (LP) on this which uses the pairwise similarity between two samples in D_b to determine the degree to which labels in C_(b-1) should co-occur with labels in C_(b). This co-occurence information between past labels and new labels forms the sub-matrices R and Q (derived from R using Bayes' rule). The  final adjacency matrix A of task b is formed by using the four submatrices: adjacency matrix of task (b-1), R, Q and co-occurence within labels of task b obtained trivially.
4. The paper claims that the **Future-missing partial label problem** is best solved by grounding all emotion embeddings to external knowledge about the emotion categories and how they are anchored in an affective space formed by the two dimensions: arousal and valence. This is done by distilling a student from two teachers: (i) the past model from Task (b-1) and (ii) the relationships between the labels as denoted on the external knowledge i.e. the affective space. 

Finally, the loss used to train the model is a weighted combination of the GAE loss from (1), cross entropy loss from (2) for task b and the two KL divergence losses from the two teachers during distillation in step (4). 

The results show significant improvements compared to various baselines and substantial progress towards a fully supervised oracle upper-bound baseline in many cases. Ablation studies are done to evaluate the value of the emotion embeddings based attention modeling, label disambiguation method for soft-labeling and the distillation. Various qualitative analyses is presented such as T-SNE visualizations and ERG visualization to show how the intended relationships amongst emotions are being successfully captured. While ablation studies are done, the paper is missing some simple yet strong baselines for each of the components and the overall system (as outlined below). 

## Overall Recommendation:
In its current state, despite some comprehensively presented experiments and analyses, the overall recommendation is leaning towards a reject. The main reason for this is that while there are several complex steps and ablations to fully remove each step, simpler component wise baselines such as encodings of emotions from their descriptions (or standard dimensions such as commonsense definitions, arousal and valence models, etc.) are not compared. This could heavily simplify this complex pipeline presented and make for a strong end to end system not even requiring some of the other components. Without this, readers will not truly understand the returns of this complex approach that needs high investment. If this can be addressed, the decision can be reconsidered.

### Strengths
1. The paper introduces a complex new problem (MLCIL) for emotion detection in multimodal settings. Their main test settings are video, audio and brain images. For such settings, note that emotion detection is hard enough for today's cutting edge LLMs also. And MLCIL adds further complexity to the setting. Given the importance of this in HCI and robotics this is a 
2. The emotion embeddings graph pipeline is a novel end-to-end contribution: building embeddings with ERGs and GAE, using it for cross attention with the input, using the same graph to solve for past-missing partial labels and finally grounding them with a distillation teacher on a prior-knowledge affective space. A similar pipeline can be used for MLCIL on any other label dimension outside (not just emotions) in theory. In fact, this may be even more useful for labels that are domain specific and not well understood by text models today unlike emotion words. The only emotion specific component in this pipeline is the affective space "domain/task knowledge". This can be swapped for other label specific domain knowledge if needed. 
3. The paper presents the description comprehensively with detailed formalisms to understand the setup. 
The experimental results are also presented with comprehensive data statistics, in both protocols/settings for class incremental learning (CIL) and with a very useful oracle upper bound (supervised training on all data). Also, an ablation study shows the incremental benefit of each component. This is especially useful since each component is fairly complex and the return on investment is critical for the readers to understand the tradeoff.  
4. T-SNE, visualizations of the ERG and parameter sensitivity are additionally presented to build intuition on what the model has achieved.

### Weaknesses
1. L159-160 make an unsubstantiated claim where it is unclear why emotion embeddings pipeline needs the complexity of the graphs. A critically missing baseline here is to build emotion embeddings directly from encoding a description of each emotion (name, definition, examples or some combination of these). These could then be used for cross attention directly in the "semantic-guided feature decoupling" stage since your emotion weights already align these embeddings to your specific data distribution. It would be interesting to see the need for label propagation then compared to soft labels from task (b-1).
2. The paper mentions the use of relation based knowledge distillation to use domain knowledge about emotions in the affective space in section 2.5. Here, when you ablate, you simply remove this component fully. A simpler baseline would be to use SoTA embedding models that potentially have an implicit understanding of the emotions on such 2D spaces like the affective space. Specifically, models that are trained on large amounts of text and explicitly model the arousal and valence dimensions could be used as a baseline for comparison. This would help isolate the contribution of the proposed relation-based knowledge distillation.
3. While the description and formalism is clear in itself, the ordering of the components is somewhat confusing. Specifically, the ERG is introduced first and it includes the adjacency matrix. However, then the section on "semantic-guided feature decoupling" breaks the flow. While I understand that you need the emotion embeddings for that section and then _s_ for subsequent section, consider providing a big picture view of the pieces first and then the individual details. The figure is useful for this and maybe this big picture view should be aligned to that figure.

### Questions
1. As mentioned above, what is driving the conclusion in L159-160?
2. Would it be possible to encode emotions from the start as a combination of arousal and valence vectors? And if so, would it avoid the relational knowledge distillation component?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the partial label problem and inadequate label semantics mining. The authors propose a graph-based framework for improving incremental multi-label emotion decoding.

### Strengths
+ The task is meaningful and practical.
+ Experiments  on three datasets show the effectiveness of AESL.

### Weaknesses
 - Some imprecise claims in the contribution.
- The description of the proposed methods, figure, and tables is not clear, which makes it difficult to follow.
- Inadequate experiments to explore why the well-designed framework work. Lack of comparison with recent methods in this task.



### Questions
1. Miss some related references.

- [1] Multi-View Multi-Label Fine-Grained Emotion Decoding From Human Brain Activity.

2. More explanation of Figure 3 is necessary. For example, 
- what is the V-A (teacher 2)?
-  Is the teacher 2 tuned or frozen? 
- What is relation between the left distillation framework and the right discrete emotion category?


3. What is the complexity analysis of this method?

4. Lack of comparison with recent methods in this task.

5. Lack of experiments or necessary discussions to explore why the well-designed framework work. 

6. Can you give some case studies or badcases to illustrate the strength and limitations of AESL

### Soundness
3

### Presentation
2

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
This paper presents the Augmented Emotional Semantics Learning (AESL) framework, to tackle the challenges of multi-label class incremental learning in emotion decoding for dynamic human-computer interaction. AESL addresses the complex nature of human emotions by integrating an augmented emotional relation graph and domain knowledge from affective dimensions, which aids in mitigating catastrophic forgetting and improving the adaptability of emotion recognition systems. The framework's effectiveness is demonstrated through evaluations on three datasets.

### Strengths
The authors introduce an augmented Emotional Relation Graph (ERG) module with graph-based label disambiguation, which generates soft labels for existing emotion classes and constructs a new ERG by integrating previous data.
The ERG module is interesting and intuitive.


Although knowledge distillation isn't a new technique, the authors have developed a relation-based knowledge distillation framework that integrates the KD, which looks reasonable.


The experimental section of the study appears thorough and solid in terms of content and effort.

### Weaknesses
Overall, while the methods in the paper are interesting, there might be quite many potential issues with the presentation.

1. The introduction might be somewhat verbose. The reviewer suggests that the first and second paragraphs should be combined. The authors extensively set the stage for HCI, yet the focus of the paper is on emotion classification. It's unclear why this emphasis was placed. Therefore, the reviewer hopes that the authors can further explain and clarify this matter.

2. A major issue with the paper is the deliberate removal of the related work section from the main texts, which is certainly inadvisable. Furthermore, the authors have not conducted a thorough survey of the most relevant works on incremental learning. The reviewer strongly suggests that the authors include the complete related work section in the main text.

3. There are way too many citation format problems: e.g., line 080, “Wang et al. (2023a)” -> “(Wang et al. 2023a)”. The reviewer hopes that the authors thoroughly check all related issues and fully polish the paper presentation.

4. On line 484, the title “Parameter Sensitivity.” is disconnected from its paragraph. Please address these issues as well as similar ones.

The reviewer might consider raising the evaluation if the authors can address these concerns with more discussions.

### Questions
The entire process is unsupervised. How can the authors prove that the constructed Augmented Emotional Relation Graph is accurate? Although extensive quantitative comparisons have been conducted, it appears that there has been no in-depth analysis or explanation regarding this aspect.

For other questions, refer to the weaknesses mentioned above.

### Soundness
3

### Presentation
3

### Contribution
3
