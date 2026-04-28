# Dreamweaver: Learning Compositional World Models from Pixels

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Humans have an innate ability to decompose their perceptions of the world into objects and their attributes, such as colors, shapes, and movement patterns. This cognitive process enables us to imagine novel futures by recombining familiar concepts. However, replicating this ability in artificial intelligence systems has proven challenging, particularly when it comes to modeling videos into compositional concepts and generating unseen, recomposed futures without relying on auxiliary data, such as text, masks, or bounding boxes. In this paper, we propose Dreamweaver, a neural architecture designed to discover hierarchical and compositional representations from raw videos and generate compositional future simulations. Our approach leverages a novel Recurrent Block-Slot Unit (RBSU) to decompose videos into their constituent objects and attributes. In addition, Dreamweaver uses a multi-future-frame prediction objective to capture disentangled representations for dynamic concepts more effectively as well as static concepts. In experiments, we demonstrate our model outperforms current state-of-the-art baselines for world modeling when evaluated under the DCI framework across multiple datasets. Furthermore, we show how the modularized concept representations of our model enable compositional imagination, allowing the generation of novel videos by recombining attributes from different objects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a neural architecture called Dreamweaver designed to discover hierarchical and compositional representations from raw videos. The core contribution of this work is  a novel Recurrent Block-Slot Unit (RBSU) to decompose videos into their constituent objects and attributes. Through experiments, the author showed that Dreamweaver can learn a disentangled representation and generate new videos by recombining attributes from different objects.

### Strengths
1. Developed a new module Recurrent Block-Slot Unit (RBSU) to decompose videos.

2. Well-written, easy to follow

3. Experimental results show that Dreamweaver can learn different attributes and freely combine them to generate varied videos.

### Weaknesses
1. Missing related works:  Some related works [1,2,3] also discuss how to use RNNs for composition video generation or use slot attention to learn disentangled representations. The authors could also include these in the related work section.

2. Insufficient comparison: This paper claim to be the first work that can learn both static and dynamic composable concepts in an unsupervised way. But I think Slotformer and Slotdiffusion[3] can do the same decomposition and are not inclued for comparsion. The authors could additionally supplement this part with experiments or explain why it is unfair to compare with SlotFormer and similar methods.

3. Better datasets: CLEVR and Sprites are still too simple. The authors could experiment on more complex datasets, such as Kubric[4] , to better demonstrate the effectiveness of the method.

### Questions
All of my question are provided in the Weaknesses section

### Soundness
2

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
This paper presents a neural network model named Dreamweaver, designed to learn compositional world representations from videos in an unsupervised manner, without the need for auxiliary data such as text or labeled masks. It utilizes a novel Recurrent Block-Slot Unit (RBSU) to extract modular representations of objects and their attributes, including both static and dynamic attributes. By training to predict future frames rather than reconstructing them, Dreamweaver can generate future video sequences based on learned compositional features and performs exceptionally well in world modeling and compositional reasoning tasks across various datasets.

### Strengths
1. Dreamweaver learns compositional world representations without relying on auxiliary data such as text or labeled masks.

2. The proposed RBSU captures both static factors (such as shape) and dynamic factors (such as motion direction), allowing the model to generate new video sequences by recombining learned object attributes.

3. Dreamweaver performs well in new object configurations and arrangements outside the training set, demonstrating strong adaptability.

4. By predicting future frames, Dreamweaver enhances its ability to represent dynamic concepts, outperforming models trained using reconstruction objectives.

### Weaknesses
1. The architecture of Dreamweaver relies on complex Recurrent Block Slot Units (RBSUs) and self-regressive Transformer decoders, requiring significant computational resources and memory, especially when processing long video sequences or higher resolution videos. The use of recurrent units, while allowing for temporal modeling, introduces inherent sequential processing bottlenecks that limit parallelization and scalability. Furthermore, the self-regressive nature of the Transformer decoder, which generates tokens one by one, further exacerbates the computational burden, especially for longer sequences. This makes the model potentially impractical for real-time applications or large-scale datasets.

2. Due to the use of Discrete VAE (dVAE) for image token representation, Dreamweaver may be limited in video generation quality, particularly in applications that require fine visual details. For example, in the Moving-Sprites experiment shown in Figure 4, when objects in the video overlap, the shapes in the generated video frames may become slightly distorted. The dVAE, by design, compresses image information into discrete tokens, which can lead to information loss and artifacts, especially when dealing with complex scenes or subtle variations in object appearance. This limitation is particularly noticeable in dynamic scenes where precise object boundaries and textures are crucial for accurate representation.

3. Although the model can generalize to simple object configurations out of distribution, its generalization ability may be limited in complex scenes. The model's performance on real-world videos with high visual complexity is unknown. The reliance on synthetic datasets for training, while providing a controlled environment, may not adequately prepare the model for the variability and unpredictability of real-world scenarios. The model's ability to handle occlusions, lighting changes, and diverse object appearances in real-world videos remains a significant open question.

### Questions
Although the model can predict short-term dynamic scenes, as the prediction time extends, the generated frames may gradually deviate from the true trajectory. For example, in the Dancing-CLEVR example 3 shown in Figure 4, the last frame's blue sphere is slightly deformed and enlarged. How does the model's performance change as the prediction time increases?

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
3

### Summary
1. The authors propose a novel method Dreamweaver for learning composable concepts(static and dynamic) from videos in an unsupervised way.
2. The authors introduce motion into existing 2d and 3d static datasets at two different complexities (simple and advanced)
3. The authors demonstrate the effectiveness of their method on their datasets along three axes of comparison; concept discovery, compositional generation and out-of-distribution generalisation.

### Strengths
1. The authors are the first to introduce a method to learning dynamic composable concepts from videos in an unsupervised way on top of static composable concepts while maintaining disentanglement.
2. The authors introduce a novel module Recurrent Block Slot Unit to model dynamic concepts.
3. Instead of the traditional reconstruction objective, the authors use a predictive objective to model dynamic concepts better.
4. The authors demonstrate the effectiveness of their method on their datasets along three axes of comparison; concept discovery, compositional generation and out-of-distribution generalisation.

### Weaknesses
1. The compositional imagination evaluation only has qualitative results which while interesting is not very informative about the model's performance relative to the other baselines. Some comparative, quantitative results should help here. For example, the authors can holdout a set of combinations in their dataset during training and evaluate the fidelity and consistency of the imagined results for these unseen combinations using standard generation quality evaluation metrics like FVD (Cobbe et al 2019), FID (Heusel et al 2017) etc.

2. The OOD results contain novel factor combinations. But do they contain entirely unseen object shapes, dynamics etc. ? if no, unless there is a specific challenge prohibiting such an evaluation, these results should also be informative about the model's out of distribution generalisation. For example, generalisation to entirely new object shapes, object textures/colors and object motion could be evaluated.  

3. The authors have only evaluated their results on their own datasets. Some results on existing datasets like MOVI or CLEVRER should be very interesting to have and would help contextualise the model's performance. Such an evaluation should provide insights into the challenges of extending the proposed approach to more complex scenes with more diverse objects, motions and occlusions. If there are technical challenge prohibiting such evaluations, the authors should clearly explain what those issues may be.

### Questions
see weaknesses.

### Soundness
3

### Presentation
2

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
This paper studies the problem of discovering shared visual concepts from videos and recomposing the concepts to unseen videos. The authors propose a novel neural architecture, Dreamweaver, operating on video object-centric representations. In Dreamweaver, a novel Recurrent Block-Slot Unit (RBSU) decomposes videos into objects and attributes and a multi-future-frame prediction loss captures disentangled representations to form both dynamic and static concepts. Experiments demonstrate that Dreamweaver can outperform current SOTA baselines on DCI scores of multiple datasets. The visualization experiments are conducted to show the compositional imagination ability of Dreamweaver as well.

### Strengths
The paper is well-written. The authors propose a method that learns a list of static and dynamic abstract concepts from videos. The learned concepts are interpretable, and Dreamweaver can imagine unseen videos by applying the learned concepts to new objects. The authors conduct extensive experiments to show the effectiveness of the proposed method compared with baselines.

### Weaknesses
My major concern is the generalizability of the proposed method. Several design choices prevent Dreamweaver from discovering latent rules beyond the datasets used in the paper. Dreamweaver assumes the videos only involve single-object moving, which significantly constrains the possible dynamic Dreamweaver can represent. It is unclear how the architecture can be modified to relax this assumption. The model also assumes a predefined set of prototypes that will be seen during training. The only generalization we would see in the test split is a novel combination of prototypes and objects, which is not surprising in slot-based architectures trained on synthetic datasets.

### Questions
1.	Did the authors try increasing the number of prototypes? I notice that currently, the datasets use different numbers of prototypes. Is the number of prototypes an important hyperparameter for Dreamweaver? The assumption of knowing the number of prototypes in the dataset makes the setting less realistic. Hence it would be important to show whether the method can have reasonable performance when the predefined number is not equal to the total number of rules in the dataset.
2.	Could Dreamweaver be extended to discover and simulate multi-object physical concepts like object collision? It seems that the objects cannot interact with each other in current settings.

### Soundness
3

### Presentation
4

### Contribution
2
