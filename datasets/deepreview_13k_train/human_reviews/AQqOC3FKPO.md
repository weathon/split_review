# Unconstrained Salient and Camouflaged Object Detection

- Decision: Reject
- Scores: 3, 3, 5, 8

## Abstract
Visual Salient Object Detection (SOD) and Camouflaged Object Detection (COD) are two interrelated yet distinct tasks. Both tasks model the human visual system's ability to perceive the presence of objects. The traditional SOD datasets and methods are designed for scenes where only salient objects are present, similarly, COD datasets and methods are designed for scenes where only camouflaged objects are present. Scenes where both salient and camouflaged objects coexist, or where neither is present, are not considered. This simplifies the existing research on SOD and COD. In this paper, to explore a more generalized approach to SOD and COD, we introduce a benchmark called Unconstrained Salient and Camouflaged Object Detection \textbf{(USCOD)}, which supports the simultaneous detection of salient and camouflaged objects in unconstrained scenes, regardless of their presence. Towards this, we construct a large-scale dataset, \textbf{CS12K}, that encompasses a variety of scenes, including four distinct types: scenes containing only salient objects, scenes with only camouflaged objects, scenes where both salient and camouflaged objects coexist, and scenes without any objects. In our benchmark experiments, we find that a major challenge in USCOD is distinguishing salient objects from camouflaged objects within the same model. To address this, we propose a USCOD baseline called \textbf{\ourmodel}, which freezes the SAM mask decoder for mask reconstruction, allowing the model to focus on distinguishing between salient and camouflaged objects. Furthermore, to evaluate models’ ability to distinguish between salient and camouflaged objects, we design a metric called Camouflage-Saliency Confusion Score (\textbf{CSCS}). The proposed method achieves state-of-the-art performance on the newly introduced USCOD task. The code and dataset will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a USCOD benchmark to bridge the difference between salient and camouflaged object detection. The authors explains that, although there are many works highlighting COD and SOD individually, USCOD tries to generalize the scenario by detecting both camouflaged and salient objects. To achieve that, the authors propose a new dataset CS12K, a new evaluation metric to understand the semantic difference between COD and SOD and present a baseline method USCNet. In USCNet, the authors considers the SAM com-
ponents including SAM encoder and mask decoder. Along with it, the authors proposes attribute specific prompt generation for saliency, camouflaged, and background prompts.

### Strengths
+The authors propose a new dataset CS12K which combines both salient and
camouflaged scenarios.
+The authors present a thorough experimental validation under all the
mentioned scenarios and outperform in all.
+The authors also present a new metric to distinguish between the salient
and camouflaged regions in the image

### Weaknesses
- This work tackles only extremes, salient or camouflaged objects. What about intermediate scenarios, for e.g., non-salient or less-salient objects. What about objects with complex backgrounds? If we are trying to generalize, it should cover the entire range, not just the two extremes.  

- The scenario of multiple objects seems missing from the dialogue. Although the authors have proposed the dataset by collecting most of the images from previous benchmark datasets, the presence of multiple camouflaged/salient objects (as per real-world scenario) seems to be missing from the dataset or model itself.

- Salient and camouflaged objects belong to different distributions based on their visual appearance and structural complexity. However, the loss function or the network does not cater to that. Is there a way to analyze this difference in the distribution of salient and camouflaged objects so that it does not impact the final prediction?

- Although the authors leverage the SAM-adapter idea, it's strange that they haven't compared with it, which does provide COD results. Also, please provide results with other recent COD and SOD works. Some of them are listed below:
1) CamoFocus [1]
2) CamoDiffusion [2]
3) CamoFormer [3]
4) PGT [4]

- It is unclear how the static prompt queries (SPQ) are generated. Moreover, the operation to predict the coarse operation is also poorly explained. It is hard to see the role of combining dynamic prompt queries (DPQ) and static prompt queries. Moreover, the motivation for the DPQ method is also unclear; authors should explain the reason why a learning component is required for DPQ calculation. Additionally, authors should explain the motivation and how they employ self-attention with salient, camouflaged, and background queries and further generate the prompts for the same.

- In line 355, the authors state that they employ self-attention, while in line 352, they mention cross-attention. This statement is contradictory and unclear.

- In table 5, there seems to be some ambiguity in the results. Specially for ICEG, the results in the manuscript provides different results than what the paper has provided (in all combined settings). Some light on this issue is required.

### Questions
Could you please address the issues raised in the weakness section?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work aims to solve the unconstrained salient and camouflaged object detection problem. It is a challenging task, that needs to jointly detect the potential salient and/or camouflaged objects in the image. To this end, they propose the first joint salient and camouflaged object detection dataset, CS12K. They also propose a solution, USCNet, for the task. The experimental results shown their effectiveness, in particularly in scenes containing both salient and camouflaged objects.

### Strengths
1. They propose a great USCOD dataset, CS12K. Different from previous SOD/COD dataset, CS12K includes images containing both salient and camouflaged objects jointly. It is more challenging and may be practical in some scenes.

2. They conduct sufficient experiments to proof the effectiveness of their approach.

### Weaknesses
1. The motivation of this work is unclear. I am curious that why we need to jointly detect salient and camouflaged objects without any pre-defined prompts? I cannot see critical problems if using the pre-defined prompts. May the authors add more explanations regarding this?

2. The novelty of this work is very limited. I cannot see the technique novelty. One APG is proposed, but the APG design is not novel, since using different type of prompts for different task setting is usual. The idea of the proposed method is not novel as well. May the author highlight it? 

3. The contribution of this work is insufficient. While it proposes a great dataset, the motivation is unclear, and the idea and method are not novel to me. I believe the contribution is not enough.

### Questions
1. In L088-L091, "The visual prompt of EVP, as part of the model, needs to be retrained according to the datasets of different tasks and requires pre-defining the category of the detection task. Similarly, the task prompts in VSCode and Spider also need to be pre-defined. Similarly, the task prompts in VSCode and Spider also need to be pre-defined." The "Similarly" here is confusing. Do VSCode and Spider need to be retrained? Or only require pre-defined prompts? Thanks for classify this!

2. If VSCode and Spider do not need to be retrained, I am curious about their evaluation protocols, as well as that of EVP (Liu 2023). How are the prompts set for scenes A, B, C, and D? I cannot find any details regarding this, but I believe it is critical since it directly relates to the fairness and necessity of using the same type of prompt for the USCOD task. Thus, I hope the authors can make the evaluation protocols clearer (this is important).

3. Regarding the CSCS metrics, based on the formulation, it seems they only consider the confusion between salient and camouflaged pixels, while the false positives and false negatives between salient/camouflaged pixels and the background are not considered. Therefore, we still need to look at mIOU to understand the quality of the method. However, mIOU can also reveal aspects such as the confusion between salient and camouflaged pixels. Thus, I wonder why we still need CSCS metrics?

4. If the paper is accepted, will the dataset be released in its “full version”? By this, I mean the version containing the entire training set (8,400 images and the corresponding masks) and the testing set (3,600 images and the corresponding masks), along with the scene types.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses both salient object detection (SOD) and camouflaged object detection (COD). Specifically, the authors first introduce a benchmark called Unconstrained Salient and Camouflaged Object Detection (USCOD) and construct a large database, CS12K. They then propose a SAM-based baseline to tackle USCOD.

### Strengths
1. The construction of the CS12K dataset has contributed to the further development of this task.
2. This paper proposes a new metric for simultaneously evaluating saliency and camouflage detection.
3. The writing is good and easy to read.

### Weaknesses
1. Is the comparison with other models fair? Were the other models compared using the same training data as this model?
2. The model design in this paper does not look very novel. Specifically, this paper proposes an adapter prompting strategy based on a cross-attention mechanism, which is very similar to [1]. 
3. The authors repeatedly state that distinguishing salient and camouflaged objects within the same image is challenging. However, theoretically, as salient and camouflaged are antonyms, it should not be excessively difficult to differentiate between them.

### Questions
1. Is the comparison with other models fair? Were the other models compared using the same training data as this model?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a new benchmark: USCOD, where both salient and camouflaged objects are considered during detection. Towards this, the authors construct a new dataset CS12K, containing four types of occasions, and proposes a new baseline for this benchmark. Furthermore, they design a new metric called CSCS to evaluate the performance of this task.

### Strengths
- The authors point out the current limitation of SOD and COD tasks, and introduce a new challenging task USCOD, combining SOD and COD together, which can improve the generalizability of both tasks.
- The authors carefully construct a new dataset for USCOD, which can contribute to this certain area.
- The competitive experiments demonstrate the essential to specially design datasets and networks for USCOD.

### Weaknesses
 - More details about the CS12K are expected. For example, when manually annotating, how is the object judged to be as salient or camouflaged? What specific criteria were used to differentiate between these two attributes during the annotation process, and how was consistency maintained across different annotators? Furthermore, what is the distribution of object sizes and complexities within each category (salient vs. camouflaged)?
- The loss function of the proposed method is not stated clearly. In equation (4), is there some difference when calculating loss for salient and camouflaged objects? If not, the different difficulties of COD and SOD may make the optimization less effective. It is unclear whether the loss function accounts for the inherent class imbalance between salient and camouflaged objects, and how this might affect the training process. The lack of clarity on the specific loss terms for each object type makes it difficult to assess the effectiveness of the optimization strategy.
- Also, when evaluating, there can be some factors influencing the actual performance. For example, the different difficulty of the two tasks: if the model performs well at SOD but poor at COD, will it achieve the same score on CSCS with another model which performs averagely at both tasks? Or will the size [1] and number [2] of objects influence the evaluation? The authors are expected to conduct some discussion on the evaluation. The current evaluation metric, CSCS, does not explicitly address the potential for a model to achieve a high score by performing well on one task while neglecting the other. It is also unclear how the metric handles cases with multiple objects of varying sizes and complexities within a single image, and whether it is robust to such variations.

### Questions
1. How do you judge whether an object is salient or camouflaged? Does this process align with popular datasets?

2. When evaluating and optimizing, do you give equal treatment to salient and camouflaged objects?  If so, why not give different weights to the two types of objects considering their difference in difficulty?

3. In the metric CSCS, I did not see the $P_{CB}$ and $P_{SB}$, which reflects the false positive rate to some extent. Can you explain the reason why $P_{CB}$ and $P_{SB}$ are not considered?

### Soundness
3

### Presentation
3

### Contribution
3
