# Hierarchical Multi-Grained Reasoning for Object Concept Learning

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Human beings can easily understand object concepts involving attributes and affordances. Recently, to simulate this ability, Object Concept Learning (OCL) has been introduced as a new task to recognize attributes and affordances related to a given object. 
OCL is essentially a many-to-many mapping problem: While an object may possess multiple different concepts, a concept can also belong to multiple different objects. 
In this regard, the prevailing method of learning discriminative representation---which is effective in the single-mapping cases---often fails in OCL.
Inspired by the reasoning mechanism of human beings, in this paper, we propose Hierarchical Multi-Grained Reasoning (HGR) for OCL, aiming to infer object-related concepts from coarse-to-fine and counterfactual grains.
Specifically, we first propose a coarse-to-fine hierarchical reasoning module that exploits multi-step learnable prompts to progressively localize object-relevant concept information. Subsequently, multiple counterfactual samples are selected to strengthen the relations between objects and concepts, which further improves the reasoning performance. In the experiments, our method is evaluated on multiple benchmarks. Significant performance gains and extensive visualization analysis demonstrate the superiorities of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This submission proposes Hierarchical Multi-Grained Reasoning approach for object concept learning. They first presents a coarse-grained prompt generation strategy to enhance attribute and affordance description, and then incorporates augmented samples as a reasoning approach to obtain fine-grained representations. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well organized, and easy to understand.
2. The experiments demonstrate the effectiveness of the proposed method.
3. Multi-grained representations and fine-grained representations for object concept learning look like reasonable.

### Weaknesses
1. I am confusing about the reasoning description in Section 3.2. The discussion of this paper majorly relies on that attribute and affordances are causal relationship, which slightly confuse me. Let's pick up the example in Fig. 5. Do you think "Furry" is the cause of the affordance "shear", "Small" is the cause of affordance "Carry"? I'd like to admit that the definition of attribute is ambiguous. Maybe you can find some attribute is the cause of a particular affordance. However, a lot attributes of the object are not causally related to affordance. From this point, the motivation of the core part in this paper is questionable.
2. Multi-grained representation and augmented representation for robust representation are common in deep neural networks.
3. Assuming the neural network might implicitly utilize the possible causal relationship behind the affordance, while the visualized illustration indicates the selected attributes are not the reason of corresponding affordance. The paper neither demonstrates the causal relations.
4. I think the causality behind affordance is interesting. However, this paper does not demonstrate convincible causal relation. From my point, it is merely correlation.

### Questions
I have a questions, do you think current MLLM model can easily address affordance and attributes recognition?

Please also refer to the weaknesses.

### Soundness
2

### Presentation
2

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
This paper focus onobject concept learning (OCL) task and introduces a multi-component model to extract attribute and affordance concepts while do causal reasoning among them. The model employs coarse and fine-grained modules to capture global and local (within the GT box) features, which are then fed into a slot-attention-based concept extractor to predict attributes and affordances. A GNN is then utilized to learn the causal relationships between attributes and affordances. The method is evaluated across various benchmarks, showing superior performance.

### Strengths
- The writting is clear, making the method very understandable.
- The proposed model and its implementation are robust and self-contained.
- I would appreciate that the authors conducted extensive experiments on multiple benchmarks and the ablation study is thorough. The proposed method also significently outperforms the baselines.

### Weaknesses
1. the proposed method appears to be a modern implementation of OCL baselines. The Coarse-to-Fine Hierarchical Reasoning is the global and local feature embedders implemented in CLIP-style. The Visual Concept Extraction is the attribute/affordance classifier implemented with slot attention. And the causal inference module is purely a GNN. While all components are straightforwardly implemented, this may diminish the novelty of the method.
2. The causal component is implemented by an GNN supervised by causal annotations. This trivialize the causal inference part to a supervised learning task. The apporach primarily learns correlations between annotated labels thus would be doubted in the field of causality. And the partial annotations in OCL also leads to biased supervised learning of causal relations. As OCL suggests that causal annotations are primarily built for evaluation rather than training, a "real" causal inference module is essential in this context. (As we can see, HGR is not evaluated on zero-shot causal inference task).
3. The model size seems considerably larger than that of the baselines. A comparison would be appreciated.
4. Additional baselines is needed for comparison, as the vanilla CLIP alone is too simple. And It would be beneficial to compare against the multimodal LLMs (e.g. GPT4o). However, given the time and budget constraints, this may not factor into my final assessment.

### Questions
Major questions have been listed in the Weaknesses part.

Minor typos: Figure 1: "clolful". And "[P][T][P]" does not seem to correspond with the equation 1 below.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper designs an object concept learning method leveraging hierarchical and counterfactual structure to achieve better many-to-many mapping in the OCL problem. The proposed method first mimics the human coarse-to-fine reasoning process to learn category-independent attributes and affordances, then introduces counterfactual supervision to strengthen relationships between them. The method comprises four modules: Coarse-grained Prompt Generation, Fine-grained Prompt Formation, Visual Concept Extraction, and Concept Connectivity with Counterfactual, realizing coarse-to-fine hierarchical reasoning and counterfactual relation-enhancing respectively. The paper conducts experiments on multiple tasks, including Object Concept Learning, Multi-task Indoor Scene Understanding, and Weakly Supervised Affordance Grounding. The results show that the proposed method has a certain performance advantage compared to the SOTAs.

### Strengths
1. The paper observes the relationship between attributes and affordances, and proposes a reasoning framework between them to solve the OCL problem. Experiments demonstrate that reasoning between the two indeed aids in the recognition of the two types of concepts.
2. The paper contains a lot of visualization contents for intermediate results and experiments, making the results intuitive and easy to understand.

### Weaknesses
1. Multi-label recognition is not a new problem. It does not demonstrate how the proposed method addresses the many-to-many problem. Specifically, the paper lacks a clear explanation of how the hierarchical reasoning framework and counterfactual supervision directly tackle the combinatorial explosion inherent in many-to-many mappings between objects and concepts. The method seems to rely on a complex pipeline, but the core mechanism that enables it to handle the mapping complexity is not sufficiently highlighted.
2. The proposed method utilizes a large amount of supervised information, including ground-truth bounding boxes, as well as causality annotations between attributes and affordances. This reliance on strong supervision limits its applicability in real-world scenarios where such annotations are scarce or unavailable. The paper does not adequately address the challenge of generalizing to settings with less or no supervision, which is a critical aspect for practical use.
3. Regarding the problem definition: How are C_\alpha and C_\beta selected in Section 3.2.1? Are \alpha and \beta here consistent with h_\alpha and h_\beta in Eq.1? A more accurate and detailed supplementary explanation is needed here. The description of the concept initialization and update process is vague, making it difficult to understand how the method effectively learns and refines concept representations. The lack of clarity in this crucial step raises concerns about the reproducibility and robustness of the approach.
4. The expression for concept distinctiveness loss in Eq. 9 is problematic; the summation expression does not include j. This should be more rigorous. The lack of a proper index in the summation makes the loss function ill-defined and raises concerns about the correctness of the implementation. This oversight needs to be addressed to ensure the validity of the proposed method.
5. Some minor issues: In Figure 1, "clolrful" seems to be a typo for "colorful," and there is an incorrect duplicate of k_alpha in Line 470.

### Questions
1. Please clarify the difference between object concept learning and multi-label object recognition. Is it feasible to treat concepts directly as categories?
2. Does choosing the same k for attributes and affordances affect the generalizability of the method? If k concepts are sampled from the complete dataset, is the model capable of recognizing all concepts?
3. What is the necessity of using GRU and concept update in Visual Concept Extraction?
4. It is recommended to place the names of the SOTA methods in Sec. A.1 within the main text. Otherwise, it's difficult to associate the methods in the Table 1 with the references.

### Soundness
2

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
The paper presents a promising new approach to OCL that leverages hierarchical reasoning and counterfactual samples to enhance model performance. The paper is well-written, and the results are compelling.

### Strengths
The paper introduces a novel Hierarchical Multi-Grained Reasoning (HGR) framework for Object Concept Learning (OCL), which is a significant step forward in addressing the many-to-many mapping challenge in OCL. The coarse-to-fine hierarchical reasoning module and the counterfactual relation-enhancing module are innovative components that show promise in improving reasoning accuracy.

### Weaknesses
1. The distributions of attribute and affordance concepts are usually imbalanced. For example, most clocks are round, and few clocks are square. A natural question is how the imbalance ratio influences the model performance. Does the proposed method work under extremely imbalanced cases?
2. The authors mainly compare the results with one work, which makes the results not very convincing. It is unclear if the performance gains are specific to the chosen baseline or if they generalize to other methods.
3. The authors employ ground-truth bounding boxes to achieve fine-grained visual content learning. However, what should we do if these annotations are unavailable? The reliance on ground-truth bounding boxes limits the practical applicability of the method in real-world scenarios where such annotations are often costly or impossible to obtain.
4. The authors mainly conduct experiments on natural images. The generalization to other domains (eg, medical data) is not clear. Also, the authors do not include a limitation section.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
