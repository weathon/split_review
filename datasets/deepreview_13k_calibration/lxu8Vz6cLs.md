# Predicate Hierarchies Improve Few-Shot State Classification

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
State classification of objects and their relations is core to many long-horizon tasks, particularly in robot planning and manipulation. However, the combinatorial explosion of possible object-predicate combinations, coupled with the need to adapt to novel real-world environments, makes it a desideratum for state classification models to generalize to novel queries with few examples. To this end, we propose PHIER, which leverages predicate hierarchies to generalize effectively in few-shot scenarios. PHIER uses an object-centric scene encoder, self-supervised losses that infer semantic relations between predicates, and a hyperbolic distance metric that captures hierarchical structure; it learns a structured latent space of image-predicate pairs that guides reasoning over state classification queries. We evaluate PHIER in the CALVIN and BEHAVIOR robotic environments and show that PHIER significantly outperforms existing methods in few-shot, out-of-distribution state classification, and demonstrates strong zero- and few-shot generalization from simulated to real-world tasks. Our results demonstrate that leveraging predicate hierarchies improves performance on state classification tasks with limited data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes PHIER, a state classification model that leverages predicate hierarchies to achieve few-shot and out-of-distribution generalization for robotic state classification tasks. PHIER incorporates an object-centric encoder, self-supervised losses to infer semantic relationships between predicates, and a hyperbolic distance metric to encode hierarchical structures. The approach is tested in simulated environments (CALVIN, BEHAVIOR) and in real-world settings.

### Strengths
1. Incorporates predicate hierarchies effectively for few-shot state classification.
2. Demonstrates strong generalization from simulator images to real-world images.
3. Utilizes hyperbolic space to encode complex hierarchical relationships efficiently.

### Weaknesses
1. Why does the proposed method perform worse than baseline methods on in-distribution samples? More detailed analysis and insights are needed.
2. Why are there no results for pre-trained models on ID-OOD samples or real-world samples?
3. In the ablation study, components are added sequentially; however, the order of addition matters. Further analysis with ablations that remove each component should be conducted.
4. Important details are missing, such as the process for constructing positive and negative pairs and how the predicate hierarchy is built.
5. The experimental evaluation requires improvement. While the collected real-world dataset is valuable, the sample size (100) is too small, and the scenario settings lack diversity, which may lead to overfitting. There are numerous existing VQA datasets that include object relations and state information. The proposed method should be evaluated on these larger and more diverse benchmarks.
6. The proposed method claims to generalize to unseen object-predicate combinations and novel predicates with few examples. However, the specific number of examples used is unclear, as it is not mentioned in the paper or the appendix. And is there an ablation study analyzing the effect of varying the number of examples?

### Questions
Here are questions that align with the identified limitations:

1. What factors contribute to the proposed method's lower performance compared to baseline methods on in-distribution samples? Could more detailed analysis and insights be provided?
2. Why were pre-trained models not evaluated on ID-OOD samples or real-world samples, and what impact would their inclusion have on the results?
3. In the ablation study, why were the components added sequentially without considering the effect of different orderings? Has an ablation analysis been conducted that removes individual components to assess their independent impact?
4. How were the positive and negative pairs constructed, and what methodology was used to build the predicate hierarchy? Can more detailed explanations be provided?
5. Given the small sample size (100) and limited diversity of the collected real-world dataset, how can the proposed method avoid overfitting to this specific setup? Why was it not evaluated on larger, more diverse VQA datasets that include object relations and state information?
6. How many examples are needed for the proposed method to generalize effectively to unseen object-predicate combinations and novel predicates? Is there an ablation study examining the effect of varying the number of examples?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work suggests a novel method for state classification with enhanced few-shot generalization capabilities. The method encodes latent features extracted from an Image and a query (in the form of an object conditioned predicate) onto a hyperbolic latent space using a unique loss and regularizer to enforce explicit learning of predicate hierarchies. The authors leverage the natural hierarchical structure that emerges in hyperbolic space based on previously seen predicates in the hierarchy to quickly learn and adapt to new, unseen objects and predicates.

### Strengths
- All deep learning components and encoding strategies are based on strong intuitions and deep understanding of the different latent spaces and tools used. 
- Empirical results show significant improvement upon current state of the art.
- Tested on environments with varying levels of complexity and realism.
- Well cited with a comprehensive literature review in the related work section
- The method is clearly presented bit by bit, slowly building up the method components in a readable fashion.
- Provides ablation tests that show the necessity of each component.

### Weaknesses
 - Theoretical justification of the method is relatively weak. It would be groundbreaking to show a strongly linked connection between hyperbolic space and hierarchical structure. This point is still unclear, even though the authors provide some intuition for it.
- Introduction lacks citations, making it difficult to understand which parts are novel and which belong to previous work (before diving in to the rest of the paper).
- No evidence is provided for claims on that large vision models struggle with spatial relationships, nor is there mention of multi-perspective image processing with these kinds of models (which emulates 3D and improves spatial understanding).
- The authors assume much preliminary knowledge from the reader, e.g., acronyms like CLIP, BERT, ViT, etc., are never defined. Even though these are common terms in the deep learning and NLP communities, Some readers might still not be familiar with everything which requires reference hopping and a general breaking of the reading flow.
- tested on very small datasets which makes the results less statistically significance.
- in line 228 the authors define the image encoding with a max over all object mask norms. doesn't this cause the final embedding to ignore the objects whose norm
- shouldn't the margin hyperparameter (lambda) be chosen dynamically depending on the current triplet? Otherwise this encourages a minimal margin that lead to equal distances between values that have significantly different semantic meaning.
- Why does the hyperbolic space's disc area growing exponentially mean that it is a continuous representation of discrete trees? There seems to be no connection between trees and the hyperbolic space according to the information provided in this work.

### Questions
- in line 228 the authors define the image encoding with a max over all object mask norms. doesn't this cause the final embedding to ignore the objects whose norm
- shouldn't the margin hyperparameter (lambda) be chosen dynamically depending on the current triplet? Otherwise this encourages a minimal margin that lead to equal distances between values that have significantly different semantic meaning.
- Why does the hyperbolic space's disc area growing exponentially mean that it is a continuous representation of discrete trees? There seems to be no connection between trees and the hyperbolic space according to the information provided in this work.

### Soundness
3

### Presentation
4

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
This paper proposes PHIER, a method for few-shot state classification by learning hierarchical predicate representations in a hyperbolic latent space. The proposed method consists of three main modules:

 A) an object-centric scene encoder based on CLIP. 

B) a triplet loss for predicate similarities based on rankings retrieved from an LLM. 

C) A Latent space with hyperbolic structure for encoding predicate hierarchies.


Experiments on two robotic simulation environments and a new real-world image dataset are performed to conclude the superior performance of PHIER in contrast to other supervised models or VLMs, especially in a few-shot setting.

### Strengths
- The paper is very well written, and the method is clear and easy to follow.
- Most design choices are justified and effective, as shown with ablations.
- Good experimental setup and results in simulation. The results regarding novel predicates show that the learned latent space is efficient, especially compared to baselines.

### Weaknesses
 - The ablation section needs more details
    - In its current state, is not clear what type of architecture the ablation baseline models utilize. What is the architecture of the supervised model? Just an image encoder and the predicate encoder followed by the supervised loss? This needs clarification. What is the hyperbolic linear layer replaced with? Simple MLPs?
- The network architecture is unclear from the current state of the method section. What are the trainable parameters? Where exactly do you introduce new parameters in the architecture? Only to project into the latent space and back? Including this in Figure 2, for instance, would make it easier for the reader to grasp this.
- Although the results in simulation are convincing, I have a few concerns:
    - The evaluation scenarios are all very simple and do not include any distractors.
    - You do not evaluate on unseen objects. The object-centric encoder should easily allow it to adapt to new unseen objects. Experiments in that regard could further strengthen the contribution of the paper.
    - The SORNet baseline uses an Mdetr object detector. Why do you not use your object-centric descriptor to generate the reference embeddings for SORNet? This would allow for a fairer comparison. This is a minor concern as the method does not require these representations in the first place.
    - You do not evaluate GPT4-V on the real-world benchmark. GPT4-V is trained on real-world data, presenting a strong baseline in this case.
    - It would be very interesting to see the few-shot transfer of the method to real-world tasks. You show that few-shot transfer works well in Simulation, so showing that it also works for sim to real transfer would strengthen the contribution.
    - The zero-shot results in real-world are not convincing. Although you outperform baselines by a large margin (which are frequently worse than random guessing), the success rate is still low. This is why I would recommend evaluating the method on few-shot transfer to real-world.

### Questions
- From the text, it remains unclear to me if the object-centric encoder is part of the contribution or an application of Mask CLIP. Please clarify.
- An additional visualization/analysis of the learned Poincare Ball structure as part of the Appendix would highlight the core contribution of the method and further strengthen the paper.
- Why do you choose a Bert encoder over the CLIP text encoder?
- How sensitive is the model to hyperparameters (loss weights) in different envs? How did you determine them?
- How fast is the training when you have to query the LLM for hierarchy ranking during Training? Do you use some buffer to not reprompt the LLM every time?
- Why does the  GPT4-V reasoning happen after the model gives its answer?
- Is the ID evaluation done after few shot training or before?
- How does the object-centric encoder work for environments with significant distribution shifts, such as CALVIN?

### Soundness
3

### Presentation
4

### Contribution
3
