# 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Referred Object Grounding

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
A 3D scene graph represents a compact scene model, storing information about the objects and the semantic relationships between them, making its use promising for robotic tasks. When interacting with a user, an embodied intelligent agent should be capable of responding to various queries about the scene formulated in natural language. Large Language Models (LLMs) are beneficial solutions for user-robot interaction due to their natural language understanding and reasoning abilities. Recent methods for creating learnable representations of 3D scenes have demonstrated the potential to improve the quality of LLMs responses by adapting to the 3D world. However, the existing methods do not explicitly utilize information about the semantic relationships between objects, limiting themselves to information about their coordinates. In this work, we propose a method 3DGraphLLM for constructing a learnable representation of a 3D scene graph.
The learnable representation is used as input for LLMs to perform 3D vision-language tasks. In our experiments on popular ScanRefer, RIORefer, Multi3DRefer, ScanQA, Sqa3D, and Scan2cap datasets, we demonstrate the advantage of this approach over baseline methods that do not use information about the semantic relationships between objects.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
3DGraphLLMs proposes to improve referential grounding performance of LLM based methods by supplying an explicit spatial graph representation of the scene as an input to the LLM (in addition to the task and the object information). Specifically, the paper proposes to model relationships between objects using an off-the-shelf 3D scene graph model. Crucially, these relationships are only modelled among k nearest neighbors of the object to reduce the number of input tokens to the LLM. To prevent very neaby object proposals to be considered as neighbors, the paper use heurestics such as ignoring boxes that are too close to each other (1cm threshhold). The proposed model is tested on ScanRefer and Multi3DRefer grounding datasets and obtain better performance than other LLM based grounding models.

### Strengths
The paper is well-written and easy to follow. It adds onto an interesting line of work in using LLMs for 3D referential grounding, The ablation study is well-designed and covers several of the relevant questions about design choices.

### Weaknesses
The quantitative numbers of the papers are weak:
- The LLM used by this paper is the recent LLAMA3-8B-Instruct while other baselines use different and older LLMs. for eg. Chat3Dv2 and Grounded 3D LLM uses Vicuana-7B (based on LLAMA 2). This makes the comparison unfair with prior models. 
- The paper does not report results on other benchmarks like ScanQA, SQA3D and Scan2Cap while still training on it, and showing ablations on it. The paper mentions that the focus is on visual grounding tasks, and that is why the evaluations are only shown in these benchmarks; however the key idea of using scene graph representation might also help for these other spatial reasoning tasks and if not, should atleast be reported for completeness in my opinion. 
- The boost in performance by using the proposed scene graph technique is only around 1-2% (Table-4) in the setup when models uses masks from a detector like Mask3D (which represents the realistic setup). This boost comes at a cost of additional complexities of making the scene graphs and querying the LLMs with additional tokens (additional ~800 tokens per query). 
- The paper claims to achieve SOTA results on ScanRefer and Multi3DRefer benchmarks in the introduction. These claims do not look correct -- as per Table-2, 3D Vista and M3DRef-CLIP outperforms the proposed model on ScanRefer. Besides several stronger baselines like BUTD-DETR [1] and PQ3D [2] outperform 3DGraphLLMs by large margins. Perhaps, the intention was to say that 3D GraphLLMs is SOTA LLM-based visual grounding model -- the claim in introduction may likely need to be revised appropriately. 3DGraphLLMs outperformM3DRef-CLIP baseline on Multi3DRefer benchmark. However, the baseline is trained on much lesser data compared to 3DGraphLLMs.

### Questions
The improvement from using 3DGraph representations seems somewhat marginal when compared in apples-to-apples setting with the predicted masks (Table-4). The results in Table-2 look good in the first glance, but due to the use of a stronger base LLM by the proposed method,  the results are hard to interpret directly. I would be happy to increase my rating if provided with more evidences / reasons of 3DGraphLLMs helping the grounding tasks (while not hurting the QA and captioning tasks by also reporting numbers on those).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel method called 3DGraphLLM, which combines semantic graphs and large language models (LLMs) for 3D referred object grounding in scenes. The method constructs a learnable representation of a 3D scene graph to be used as input for LLMs to perform 3D referred object grounding tasks. Experiments demonstrate its advantages over baseline methods that do not utilize semantic relationships between objects on popular datasets like ScanRefer, RIORefer, and Multi3DRefer.

### Strengths
1. This paper notes that the semantic relationship between object pairs within a 3D scene is beneficial for visual grounding and other tasks such as visual captioning and visual question answering. It proposes 3DGraphLLM, which constructs a learnable representation of a 3D scene graph and uses it as input to a large language model (LLM) to perform the 3D referred object grounding task.

2. The authors have identified some technical issues (such as the domain gap between 3Rscan and ScanNet, and the presence of duplicate objects in the nearest neighbors), and I believe this paper is technically thorough.

3. The authors provide relatively sufficient and convincing experimental results.

### Weaknesses
1. In the Edge Feature Encoder, the important issue is raised that the semantic relationships recognition methods are all trained on 3RScan scenes, while the visual grounding tasks are typically tested on ScanNet scenes. I believe this is indeed a challenge. The authors claim that the solution is to use VL-SAT due to its good generalization in the new domain. I am very familiar with VL-SAT, and currently, there is no evidence showing that this method has good generalization in the new domain to address the mentioned challenge. Specifically, the generalization ability of VL-SAT across different 3D scene datasets, particularly from 3RScan to ScanNet, is not well-established in existing literature. The claim that VL-SAT inherently bridges this domain gap requires more substantial empirical backing, given the differences in data acquisition and scene characteristics between these datasets.

2. Similarly regarding VL-SAT, the authors seem to have used the VL-SAT pre-trained on 3RScan to test on the ScanNet dataset (e.g., ScanRefer, Multi3DRefer, etc.). This is equivalent to the results of RIORefer->ScanRefer in Cross3DVG. In Figure 5, when the number of nearest neighbors = 2, the Acc@0.5 reaches an astonishing 49.0, which not only significantly surpasses the result of RIORefer->ScanRefer in Cross3DVG (13.34) but also shows a remarkable difference compared to the RIORefer->RIORefer test result (20.21) given in Cross3DVG. This could be explained by 1) using GT instance segmentation yields better results, and 2) 3DGraphLLM performs exceptionally well on RIORefer, surpassing the Expert model. However, 1) based on the results in Table 4, it is difficult to foresee such a significant gap, and 2) the performance of the model on similar datasets like ScanRefer and Multi3DRefer indicates that it is challenging to significantly exceed the existing SOTA Expert model. The discrepancy between the reported results and the expected performance based on existing benchmarks raises concerns about the experimental setup or potential overfitting on the RIORefer dataset. I hope the authors can provide some explanations regarding the above points and present more experimental results on RIORefer during the rebuttal period. A reasonable response to this weakness would make me consider raising my score.

3. Table 4 needs to be completed (i.e., providing the results of 3DGraphLLM-2 with OneFormer3D segmentation when the minimal distance = 1cm), as this is crucial for validating the effectiveness of the minimal distance strategy. Without this data, it's difficult to assess the impact of the minimal distance filtering on the overall performance when using predicted instance segmentation masks.

4. The results of VL-SAT are based on training with 160 objects and 27 relationships. I would like to know how much these 27 relationships help in ScanRefer. As far as I know, these 27 relationships do not seem to have a strong correlation with the descriptions in ScanRefer. I understand that this is essentially due to the limitations of dataset annotations, but I hope the authors can explore whether the annotations in the 3D Scene Graph Generation dataset are related to the descriptions in visual grounding. Specifically, it is unclear how the 27 relationships, which are primarily spatial and geometric, align with the more diverse and complex descriptive language used in ScanRefer. This mismatch could limit the effectiveness of the edge features derived from VL-SAT.

### Questions
1. Please address the questions in Weaknesses 1. I have concerns about the generalization between the two datasets.

2. Please respond to the questions in Weaknesses 2. I would like to see more experimental results on RIORefer and hope the authors can explain the significant differences in the results I mentioned in Weaknesses 2.

3. I hope the authors can answer the questions in Weaknesses 4, as I believe the correlation between the two datasets is very important.

### Soundness
3

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
The paper considers the problem of generating a learnable representation of a 3D scene to be processed by Large Language Models (LLMs). Compared to existing object-centric latent scene representations, the proposed approach incorporates an additional relational edge encoding. Both node (objects) and edge (relations) encodings are obtained by passing the off-the-shelf point cloud encoder outputs through a trainable projection head. Experiments show that this modification improves the performance on visual grounding tasks across multiple datasets.

### Strengths
1. The idea to add object semantic relationship into the latent scene representation for LLMs is well-motivated.
2. The proposed approach is simple and effective.

### Weaknesses
The proposed modification introduces a parameter of minimum distance for filtering the nearest neighbors. It requires manual tuning, as is set to be 1 cm as in the paper. This requirement might potentially make it hard to apply this approach to new domains, such as a tabletop scene or a larger multi-floor multi-room indoor scene. Specifically, the 1cm threshold is highly dependent on the scale and density of the point clouds, and it's unclear how this parameter should be adapted for scenes with varying object sizes and inter-object distances. For example, in a tabletop setting, objects might be much closer than 1cm, requiring a smaller threshold, while in a large indoor scene, objects might be further apart, potentially requiring a larger threshold to capture meaningful relationships. This lack of adaptability is a significant limitation.



### Questions
1. What is the difference between the “3DGraphLLM-0” (in table 3, 4) and “Chat-3D v2” baseline (in table 2)? It is said in Section 4.4 that they are equivalent (“The 3DGraphLLM version with zero nearest neighbors…, equivalent to the Chat3Dv2 approach..”). However, under the ScanRefer benchmark, the 3DGraphLLM-0 (in table 4) outperforms Chat3Dv2 (in table 2) by more than 10% margin in $Acc\@0.25$. Similarly, why is the performance of 3DGraphLLM-0 under GT segmentation not consistent in table 3 and 4? 
2. The proposed approach uses Uni3D for object encoding and VL-SAT for edge encoding. Since VL-SAT also contains an object encoder, which might be even more compatible with its own edge encoder,  why is the Uni3D encoder used instead?
3. What are the common failure cases of the method?

### Soundness
3

### Presentation
3

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
This paper proposes 3DGraphLLM, a multimodal language model that takes into account the object relationships in a 3D scene and achieves better performance in referred object grounding tasks. 3DGraphLLM takes as input a scene point cloud, segmented into object instances using an off-the-shelf 3D object segmentation model. The features for each 3D object and their relationships are also extracted by pretrained models, projected to LLM token space, and input to the LLM as part of the prompt. The LLM and the projectors are finetuned on the training sets of 3D datasets. Experiments show that 3DGraphLLM outperforms baselines and several ablation studies show the effectiveness of design decisions.

### Strengths
1. 3DGraphLLM converts object relationships to LLM token space and incorporates them into the prompt for 3D grounding tasks. In this way, the LLM receives more complete information about the 3D scene graph and gets a better understanding of the 3D environment. 
2. Most design decisions have ablation studies and their effectiveness is verified. 
3. The paper is well-written and easy to follow.

### Weaknesses
1. LLMs are known for capturing a significant amount of common sense knowledge and show out-of-distribution generalization ability. However, in the design of 3D GraphLLM, I cannot see how such power of LLMs is being utilized or demonstrated at all, and thus **what's the point of using a pretrained LLM there?** Ideally, by using an LLM, I expect to see that in addition to taking the new modality (3D scene graph) as input, the adapted LLM also shows that its common sense knowledge is also being exploited in a non-trivial way, e.g. out-of-distribution generalization, achieving tasks other than grounding. At least I want to see if the entire model is trained from scratch (without pretraining on text), and whether the performance will be worse.

With the above being said, I'm very concerned that in Table 2, the proposed method has worse performance than the expert models on ScanRefer, which seems to suggest that the LLM pretraining is not really helping.

2. The proposed method relies heavily on the performance of the underlying 3D segmentation and scene graph generation models used to encode 3D objects and relationships into features. Even if the LLM is able to generalize OOD, it's still limited to these models and cannot recover from their failures.

This concern is verified by Table 4, where using GT segmentation, 3DGraphLLM is better than the baseline by 5.6 percent, but less than 2.0 percent using predicted instance segmentation.

3. Why is the flat graph representation object-centric (i.e. obj1, obj1-NN1, obj1-NN2, obj2, obj2-NN1, obj2-NN2...), instead of further flattened (i.e. obj1, obj2, obj3, ..., rel1, rel2, rel3, ...)? In the latter format, the set of relationships to keep can still be limited to the k-NN of each object instead of the dense graph. I'm asking because in Table 1 (L273), seems the $F_1^v$ is being repeated k times. The repetition will be even greater if one object is considered as NN of other object nodes. Therefore, there seems to be still a lot of waste in the proposed tokenization scheme.

4. This paper proposes to train the model in a two-stage manner (first on GT instance segmentation, then on predictions), but this is not being ablated.

5. The design minimum distance filter suggests that there are duplicate detections in the 3D detection results. I think these duplicates should be handled using filtering techniques like 3D NMS rather than the proposed naive minimum distance filter on the scene graph edges.

### Questions
Please see the "Weakness" section.

### Soundness
3

### Presentation
3

### Contribution
2
