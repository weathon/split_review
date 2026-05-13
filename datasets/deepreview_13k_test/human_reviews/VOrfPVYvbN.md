# Domain Bridge: Generative Model-based Domain Forensic for Black-box Models

- Decision: Reject
- Scores: 3, 5, 3, 5, 6

## Abstract
In forensic investigations of machine learning models, techniques that determine a model's data domain play an essential role, with prior work relying on large-scale corpora like ImageNet to approximate the target model's domain. Although such methods are effective in finding broad domains, they often struggle in identifying finer-grained classes within those domains. In this paper, we introduce an enhanced approach to determine not just the general data domain (e.g., human face) but also its specific attributes (e.g., wearing glasses).
   Our approach uses an image embedding model as the encoder and a generative model as the decoder. Beginning with a coarse-grained description, the decoder generates a set of images, which are then presented to the unknown target model. Successful classifications by the model guide the encoder to refine the description, which in turn, are used to produce a more specific set of images in the subsequent iteration. This iterative refinement narrows down the exact class of interest.
   A key strength of our approach lies in leveraging the expansive dataset, LAION-5B, on which the generative model Stable Diffusion is trained. This enlarges our search space beyond traditional corpora, such as ImageNet. Empirical results showcase our method's performance in identifying specific attributes of a model's input domain, paving the way for more detailed forensic analyses of deep learning models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a systematic workflow for refining image labels with, e.g., attributes. The proposed method combined several existing models (CLIP, Stable Diffusion, etc) and was evaluated on standard image datasets, such as CIFAR10, Places365, and CelebA.

### Strengths
Using (pretrained) generative models to enrich the outputs of target models with expanded descriptions can be potentially useful for fine-grained training and improving the understanding of datasets.

### Weaknesses
- The writing in the paper is relatively easy to follow but academically informal. There are numerous bullet points that could be replaced with more formal descriptions, which would lend a more scholarly tone to the paper. This would help elevate it beyond its current format, which resembles a technical report. For example, Sec 4.1.2 could have been made as an algorithmic procedure. 

- The effectiveness of the proposed method doesn't seem entirely convincing. Tables 1 and 2 show only marginal improvements over the original class labels, with some cases being identical. The evaluation could benefit from additional qualitative results to provide a more comprehensive assessment. Furthermore, it's unclear how the corpus baselines are implemented, and proper citation and referencing would be helpful in this regard.

- In Sec 6.3, the concept of model cloning is introduced without proper context. If the purpose of model cloning is to create a generative process that replicates the original dataset, the evaluation in Table 3 appears insufficient, as it only measures generation quality but not diversity. Metrics for distribution shift should be included, and the choice of the four scenarios should also be justified (e.g., it's unclear how scenario 1 serves in evaluating the proposed method).

- Table 4 indicates that the proposed method exhibits a strong bias in generating correlated attributes that are unrelated to the source labels. While the use of the proposed method to uncover implicit bias in target models is intriguing, it appears independent of the problem the method aims to address, and Table 4 does not seem to provide conclusive evidence to support this claim.

### Questions
- Is the objective (1) being used in any part of the experiments? 

- It appears that the bullet points under Table 3 might not align correctly with the table. Should the third and fourth points be switched?

- Can the proposed method generate longer descriptions beyond only two layers of BST?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presented a approach for forensic investigation of machine learning models, which determines not just the general data domain but also its specific attributes. And the overall framework combines Stable Diffusion, clip, and GPT4 technologies to design the domain search technique.

### Strengths
-  The paper digs in on specific attributes within the domain.
- The method makes clever use of lpretrained generative models and language models.
- The experiments validate the method across different scenarios.

### Weaknesses
- The algorithm part is not very clear.
- The experimental data set is relatively small.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors consider an inverse problem: given a black-box model with known classes they want to identify specific attributes of these classes; moreover, they want to generate examples of images belonging to the classes.

To solve the problem the authors proposed a combination of Stable Diffusion model, CLIP model, and some heuristics. They demonstrated on a number of examples how the proposed approach work.

### Strengths
- the authors evaluated how the combination of existing tools such as Stable Diffusion and CLIP works when refining  attributes of the classes of the initial black-box model. This information can be useful as a reference point in future applications which consider combinations of Stable Diffusion and CLIP for image description or data augmentation

### Weaknesses
- actual practical usefulness of the proposed approach is not clear. The authors just provided some general comments that the proposed approach can be useful for assessment of black-box models. However, they did not provide any specific applied scenario/use case, for which a refinement of the attributes of the the initial black-box model classes is a vital thing

- description of the algorithm, discussed in 4.1.2, is too vague. It is not enough for reproducibility, as there are many things that should be defined, e.g. Description Grouper, clustering algorithm, how to select depth of the tree, etc. The authors did not provide any code

- the authors consider very old classifiers, e.g. GoogLeNet, etc. to demonstrate efficiency of the proposed approach. At the same time, on recent models from hugging face the approach did not demonstrate significant efficiency

### Questions
- how to tune coefficient lambda in (1)?

- Search process looks like a manual process, see Example A.1, page 11. "Terminate if after several iterations, the majority of generated images are consistently classified as the target class by M, and no significant, ...". "Several" - how many? "Majority of generated images" - how many? "No significant" - what significance?

- What if the original training sample, used to train Stable Diffusion, does not include images, used to train the black-box model? To what extent the proposed approach is robust?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a method to determine the data domain and specific data attributes of a black-box model. Specifically, this method utilizes a set of well-pretrained models and iteratively refines the description for generating a more specific set of images if the generated images are successfully classified. The experiments show the effectiveness of the proposed method.

### Strengths
- This paper delves into a crucial yet underexplored domain, which involves understanding the data domain of an undisclosed target model. In contrast to prior methods, the authors extend their contribution beyond merely providing image classes. They also delve into more intricate data attributes. An additional strength of the proposed method lies in its independence from a specific search dataset due to the utilization of a set of well-pretrained large models. Moreover, the inclusion of textual descriptions for the target model's classes represents a unique advantage of this approach.
- Experiments show the effectiveness of the proposed method.

### Weaknesses
- Technical Contribution is limited. This paper primarily offers a heuristic search algorithm for discovering the optimal description.
- The experiments in this paper exclusively employ the corpus-based method as the sole point of comparison. This limited range of comparison experiments may not provide a comprehensive assessment. Furthermore, the corpus-based method is not extensively introduced or detailed.
- Potential for Quantitative Measurements. It might be beneficial to include more quantitative measurements that directly illustrate the overlap between the predicted data and the ground truth training data.

### Questions
- See the weaknesses above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to generate a description with more detailed attributes for analyzing the learning knowledge of black-box models. Specifically, the authors leverage the Breadth-First Search (BFS) manner to identify the optimal description heuristically and iteratively. In each iteration, they generate images based on the text embedding of one node and then utilize CLIP Interrogator to remap images into textual descriptions. The description with the highest relevance is selected. The authors conducted multiple experiments to demonstrate that their method could generate more detailed descriptions.

### Strengths
This paper is well-written and easy to understand.    
The authors introduce a well-designed framework to search the optimal descriptions by integrating CLIP, CLIP Interrogator, diffusion models, and LLM models together. 
Compared to the corpus-based approach, the proposed method achieves better performance in determining the correct domain.

### Weaknesses
For the experiments, Table 1 and 2 showcase that the proposed method produces the description with extra properties. For example, "bird" is changed to "bird sitting on a branch". Does the black-box model predict "bird" based on both "bird" and "branch"? The authors should provide more analyses into why the proposed method generates this redundant description.  
Additionally, Table 4 indicates that the proposed method is affected by the biases of diffusion models. Thus, will adopting more diffusion models improve performance?  
Besides, the authors should conduct experiments on large-scale datasets, which may lead to complex decision boundaries and be more challenging.

### Questions
1. The proposed method initializes root nodes with labels of ImageNet-1k. How about sorting these labels using CLIP?  
2. Why did Scenario 4 achieve better performance than the original accuracy? Does it suggest that the black-box models are overfitting to the crafted description?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
