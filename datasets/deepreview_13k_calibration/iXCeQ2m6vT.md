# Mind the GAP: Glimpse-based Active Perception improves generalization and sample efficiency of visual reasoning

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 8, 6, 6, 6

## Abstract
Human capabilities in understanding visual relations are far superior to those of AI systems, especially for previously unseen objects. For example, while AI systems struggle to determine whether two such objects are visually the same or different, humans can do so with ease. Active vision theories postulate that the learning of visual relations is grounded in actions that we take to fixate objects and their parts by moving our eyes. In particular, the low-dimensional spatial information about the corresponding eye movements is hypothesized to facilitate the representation of relations between different image parts. Inspired by these theories, we develop a system equipped with a novel Glimpse-based Active Perception (GAP) that sequentially glimpses at the most salient regions of the input image and processes them at high resolution. Importantly, our system leverages the locations stemming from the glimpsing actions, along with the visual content around them, to represent relations between different parts of the image. The results suggest that the GAP is essential for extracting visual relations that go beyond the immediate visual content. Our approach reaches state-of-the-art performance on several visual reasoning tasks being more sample-efficient, and generalizing better to out-of-distribution visual inputs than prior models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on understanding visual relations. This remains a challenging problem for current vision models. To deal with this challenge the paper leverages active vision where the learning of visual relations is grounded in actions that we take to fixate objects and their parts by moving our eyes. The proposed approach with glimpse-based active perception demonstrates promising performance on a range of visual reasoning tasks.

### Strengths
* The paper provides interesting insights into visual reasoning problems.
* The proposed glimpse-based active perception is relatively novel and interesting.
* The proposed approach shows promising performance on a range of visual reasoning problems.
* The paper considers diverse visual "sensors" and downstream architectures.

### Weaknesses
 * While the proposed approach is somewhat novel it is similar to prior work such as "AdaGlimpse: Active Visual Exploration with Arbitrary Glimpse Position and Scale, ECCV 2024" which also focus on what and where to look.

* Current state of the art vision-language models such as LLaVA (NeurIPS 2024) keep the visual features from the target image in the context window. This means that they can actively attend to the image as many times are necessary to extract visual features. It would be interesting to compare the proposed approach to current SOTA VLMs such as LLaVA.

* Prior work such as "Look, Remember and Reason: Grounded reasoning in videos with language models, ICLR 2024" used surrogate tasks to decide what and where to look at. It would be beneficial to include a discussion of this related work.

* Synthetic data: Three out of the four datasets used for evaluation are based on synthetic datasets. It would be beneficial to include more real world datasets such as GQA or Super-Clevr.

### Questions
* The paper should include a broader discussion of related work (see above).
* The paper should better motivate the choice of evaluation datasets.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel method for visual reasoning, called Glimpse-based Active Perception (GAP). Based on that the human eye selectively concentrates on salient and/or task-relevant parts of a scene, the authors devise a method that extracts salient regions of an image and feeds them into downstream architectures to enforce perception of salient regions only. Firstly, a saliency map is built based on error neurons, which marks salient regions as those that differ significantly with their surrounding neighbours. Secondly, salient regions are extracted from the image, using the saliency map, with either the multi-scale or log-polar glimpse sensor. Lastly, these salient regions and their locations are fed into either Transformer or Abstractor to perform visual reasoning tasks, each dubbed as GAP-Transformer and GAP-Abstractor. By forcing the downstream architectures to concentrate on salient regions only, the GAP-Abstractor achieves SOTA or comparative-to-previous-SOTA performance on the conventional visual reasoning benchmarks, OOD benchmarks, and real-image-based OOD benchmarks.

### Strengths
- Authors propose a well-motivated method: 
  - They explain the motivation behind GAP logically, linking back to the human perception model throughout their method section. 
  - Ie. They explain that they concentrate on salient regions since "humans use active vision"; They explain that they use the concept of error neurons since "the activity of neurons is influenced ... also by stimuli that come from the surroundings of those receptive fields". 

- The proposed method attains strong performance on benchmarks:
  - Especially compared to previous work that do not use pretraining as GAP, GAP-Abstractor outperforms them by large margins. 
  - Authors also infer on four datasets, each with different purposes (testing visual reasoning only vs OOD generalization too) and different domains (binary figures vs real-world images). 

- The paper is well-written and easy to follow with both textual and visual explanations. 

- This paper introduces a novel and logical method to field of Visual Reasoning, which is of great importance since visual reasoning is required for a range of real-life tasks, and thereby contributes to the community.

### Weaknesses
 - Authors do not make it explicit or clear that different sensors (multi-scale or log-polar) have been used across different datasets for the same downstream architectures (ViT/Abstractor). Ie. For SVRT, GAP-Abstractor used the multi-scale sensor but for SVRT #1-OOD it used the log-polar sensor. This should be made clear in the main paper, instead of referring to the Appendix. 
  - Also, in Appendix D, authors do not explain why each sensor works better or worse for each downstream architecture-dataset pair. Since the performance depends on the type of sensor and since authors have proposed to use both, authors should explain where each sensor may be a better choice. 

- References are missing in Tables and Figures. 
- Explain what the tasks RMTS and ID are, at least briefly, in Section 5.4 before explaining the results.

### Questions
- Can the authors provide an explanation to why GAP-Abstractor perform worse on 'straight lines' and 'rectangles' compared to other classes? 
- Since the authors explained that "glimpsing behavior can be distracted by spurious salient locations such as edges of shades or regions of high reflection", would performing GAP (finding salient regions) on feature maps, instead of images, where these spurious features are probably less influential, increase performance? Can authors provide results? 
- Please explain why each sensor works better or worse for each downstream architecture-dataset pair.

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
The authors develop a system equipped with a novel Glimpse-based Active Perception (GAP) that sequentially glimpses at the most salient regions of the input image and processes them at high resolution. Their approach reaches state-of-the-art performance on several visual reasoning tasks being more sample-efficient, and generalizing better to out-of-distribution visual inputs than prior models.

### Strengths
1. The paper introduces a novel "Glimpse-Based Active Perception" (GAP) model inspired by human active vision. 
2. The proposed approach reaches state-of-the-art performance on several visual reasoning tasks being more sample-efficient, and generalizing better to out-of-distribution visual inputs than prior models.

### Weaknesses
1.  The images in the four selected datasets seem relatively simple, with very clean backgrounds. Have you considered comparing your proposed model with baseline models on more realistic image datasets, such as the COCO dataset?
2. Given that the GAP mechanism involves multiple steps (e.g., saliency map generation, inhibition of return), have you compared its computational performance with other baseline models?
3. Why can GAP-Abstractor improve OOD generalization of same-different relation and more abstract relations?

### Questions
1. Have you explored alternative methods for computing the saliency map, given that GAP's effectiveness largely depends on the map's accuracy in identifying key image regions?
2. What is the impact of using a hard versus a soft mask M(x_t)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an architecture that performs visual perception based on local glimpses. It uses a saliency map to determine glimpse positions, and then feeds an encoding of the appearance and of the location of the glimpses to an existing downstream architecture - a Transformer or the recently proposed Abstractor. The glimpse extraction is hardcoded while the downstream architecture can be trained. The architecture is evaluated on reasoning tasks that rely on local structure and spatial relations.

### Strengths
The paper explores an architecture that make explicit the positions and not just appearance of local image regions. These types of architecture are interesting because of the potential capabilities they can enable, and because of their relation to human vision. The paper is well written and fairly easy to follow. The proposed architecture is very simple.

### Weaknesses
The proposed architecture can be viewed as a local feature extractor that encodes local image regions and their positions. There is very extensive prior work in this area, which makes the novelty somewhat limited. The proposed architecture is evaluated on two types of toy task (including some variants of those tasks): SVRT with/without OOD setting and ART/CLEVR-ART. All tasks use simple synthetic images with highly local structure in entirely uncluttered scenes, and their solutions seems to strongly rely on positions of objects. One would expect any architecture that makes those positions explicit to do exceptionally well on these specific tasks. Training sets for these tasks are also extremely small and will thereby favor architectures that are based on hardcoded (not trained) feature extraction. Given the extensive prior work on foveated vision, how do existing methods perform on these tasks?

### Questions
I'm not sure about the term "active", since the architecture relies on a fixed (and not adaptive or recurrent) scheme to extract local features? 

Why is the dataset size for results in Table 1 restricted to 500/1000 training examples? This seems arbitrary. Figure 4 seems to suggest that the training set is larger? 

Can the SVRT #1-OOD experiment be extended to other subsets than SVRT #1? 

Is there a reason why the results in Table 3 (on a subset of ART) do not include all models considered previously (e.g. Attn-ResNet?) 

It would be very beneficial to include a modern vision-language model in the evaluation, as these models have become very good at solving similar reasoning tasks. 

Some additional related work: 

"Learning to combine foveal glimpses with a third-order Boltzmann machine", Larochelle et al. 2010 

"Multiple Object Recognition with Visual Attention", Ba et al. 2014 

"Show, Attend and Tell: Neural Image Caption Generation with Visual Attention", Xu et al. 2015

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper discusses how to improve the performance of visual reasoning by simulating the active perception of humans, especially when dealing with unknown objects. By expressing the relationship between different image parts with the position generated by glimpse-based active perception and the visual parts around them, this approach reaches a better sampling efficiency and generalization performance.

### Strengths
1. It is really inspiring to simulate human's active perception to improve the performance of visual reasoning, which is a contribution to the community of visual reasoning.
2. The approach achieves better sampling efficiency and generalization performance.
3. The authors provide extensive experiment results and analysis.

### Weaknesses
1. For the discussion of generalization ability, the paper focuses on the OOD data of the specific benchmarks. However, what we hope to achieve is the ability that models can deal with totally different tasks like humans, although it is really though. This paper lacks the analysis of it. Specifically, the paper does not address how the learned glimpse patterns and relational reasoning would transfer to tasks with different visual primitives or require different types of reasoning, such as those involving temporal dynamics or physical understanding. The current evaluation is limited to variations within a single task family, which does not fully capture the desired level of generalization.
2. Recently, many LLM-based approaches are gaining higher performance on the reasoning tasks like VQAs. More analysis of the relationship between pure abstract reasoning like this approach and LLM-based reasoning is desirable. The paper does not explore how the explicit spatial reasoning performed by the glimpse-based approach compares to the implicit reasoning capabilities of LLMs, which often rely on large-scale pre-training and knowledge retrieval. A comparative analysis, perhaps by examining the types of errors made by each approach, would be beneficial.

### Questions
1. What concerns me most is the generalization ability of this approach, although it is inspiring and fancy. Could you give me some clues that this approach can deal with tasks across different domains to reach the authentic reasoning ability?
2. Many people assume that LLM-based reasoning is closest to the generalization due to its rich knowledge. I suppose this approach would also be helpful to the LLM community. Would you conduct some analysis on the relationship between this approach and LLM-based reasoning?

### Soundness
3

### Presentation
3

### Contribution
2
