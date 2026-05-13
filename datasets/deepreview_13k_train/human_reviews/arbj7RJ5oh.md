# Neural Slot Interpreters: Grounding Object Semantics in Emergent Slot Representations

- Decision: Reject
- Scores: 6, 3, 3, 8, 3

## Abstract
Several accounts of human cognition posit that our intelligence is rooted in our ability to \textit{form} abstract composable 
concepts, \textit{ground} them in our environment, and \textit{reason} over these grounded entities. This trifecta of human 
thought has remained elusive in modern intelligent machines. In this work, we investigate whether slot representations 
extracted from visual scenes serve as appropriate compositional abstractions for grounding and reasoning. We present the 
Neural Slot Interpreter (NSI), which learns to ground object semantics in slots. At the core of NSI is an \textit{XML}-like 
schema that uses simple syntax rules to organize the object semantics of a scene into object-centric schema primitives. 
Then, the NSI metric learns to ground primitives into slots through a structured objective that reasons over the intermodal 
alignment. We show that the grounded slots surpass unsupervised slots in real-world object discovery and scale with scene 
complexity. Experiments with a bi-modal object-property and scene retrieval task demonstrate the grounding efficacy and 
interpretability of correspondences learned by NSI. Finally, we investigate the reasoning abilities of the grounded slots. 
Vision Transformers trained on grounding-aware NSI tokenizers using as few as ten tokens outperform patch-based tokens on 
challenging few-shot classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The current manuscript tackles the problem of grounding object-centric semantics in the slot representations that emerge via a visual reconstruction task. Towards this, it proposes a schema, called visXML, to represent the scene semantics in a structured form, and aligns it with the emergent slots via a contrastive loss within a given batch. The proposed approach, called Neural Slot Interpreter (NSI), results in a more grounded representation and outperforms some of the existing methods on bi-modal objective-property and scene retrieval tasks, in addition to outperforming patch-based tokens on few-shot classification tasks.

### Strengths
(S1) The problem tackled is interesting as it builds on top of existing object-centric slot learning to ground object concepts in them.

(S2) The proposed approach to use a visXML-based schema and measure scene-schema similarity is intuitive and simple to understand.

(S3) The manuscript is mostly well-written with sufficient motivation, relevant discussion of the literature, and clear technical details to understand the proposed approach, spread across the main and the appendix. I thoroughly enjoyed reading the manuscript.

### Weaknesses
 (W1) Insufficient comparisons to prior work. The experiment tables do not report any numbers from the literature (e.g., [A, B, C, D]). 
* In particular, [A] reports performance on slot discovery for MS COCO dataset as 35.27 (mBO_i) and 46.28 (mBO_c), while current approach reports 28.12 and 32.10 respectively. 
* Further, if [C] is the Ungrounded baseline, the numbers do not match with those shown in the literature, mBO_c of 31.1 [C] vs 26.5 (reported in Appendix E.1.1). Request the authors to include necessary comparisons and fix these inconsistencies.

(W2) Limited experimentation on real world datasets. Though the results on synthetic datasets like CLEVr Hans, CLEVrTex, and MOVi-C motivate the problem, the real-world applications are more guided by experimentation on real world datasets. This also helps understand the efficiency of the approach beyond the sim2real domain difference. While the paper includes results on MS COCO, results on PASCAL VOC (often reported in prior works in the area) are missing. Without these results, the quantitative benefits of the proposed approach are unclear.

(W3) A minor concern is the lack of relevant pointers in the main, when referring to modules from prior work. For instance, it is unclear how slots are obtained in Sec 3.2.1 without reference to either the appendix A.1 or prior work. Request the authors to go through the manuscript carefully to provide these details.

### Questions
Request the authors to address the weaknesses to demonstrate the quantitative benefits of the current approach compared to all existing methods (even if it does not have superior performance).

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
The paper presents the Neural Slot Interpreter (NSI), a model that aims to bridge the gap between visual perception and object-based reasoning by grounding object semantics in emergent slot representations. NSI organizes visual scenes using an XML-like schema (visXML) that assigns semantics to specific object-centered slots, allowing structured grounding through a contrastive learning objective.

### Strengths
The paper introduced a novel contrastive learning technique to align slot representations with visXML representations, which are essentially object-centric symbolic representations associated with the scene.
The evaluation was performed on a variety of tasks: (1) object discovery, (2) scene-property retrieval, (3) few-shot scene classification, and (4) object detection. The results demonstrate the efficacy of NSI.

### Weaknesses
The main weakness of the paper, to me, is the unclarity of the problem setting. VisXML, based on my understanding, is essentially some kind of symbolic scene representation similar to works such as http://nsd.csail.mit.edu/papers/nsd_cvpr.pdf I think, in order to obtain such kind of representations, one needs to train models with supervision on object masks/bounding boxes, and object labels (or maybe off-the-shelf models like large vision-language models or object segmentation models can already do the job). If that's the case, why do we still need to learn object-centric representations? Why don't we just directly supervise the learning of object segmentation etc. using these visXML labels...? I could imagine ways that combined supervised and unsupervised learning could help, but I don't think the paper shows sufficient evidence about their advantages.

Concretely, the paper should compare with a baseline that directly uses VisXML to do all these tasks.

Also, VisXML should not be listed as a contribution. See the NSD paper cited above.

### Questions
I don't have particular questions about the paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the problem of grounding concepts to objects within images by training on paired images and object descriptions. It proposes an architecture built upon unsupervised object discovery models. During training, object features are first extracted by an object discovery module, and then these features are aligned with object property features through contrastive learning. Experiments demonstrate that the proposed method outperforms baseline models in object segmentation performance. Additionally, the learned representations benefit downstream applications, such as concept retrieval and concept reasoning.

### Strengths
1. The paper is easy to follow.
2. The paper includes the necessary details for reproducing the results.

### Weaknesses
 - Using semantic grounding to enhance object discovery is not novel. For instance, [1] leverages question-answering and captions paired with images to improve the object discovery capabilities of Slot Attention. Author should also consider discussing other related works in concept grounding in images, such as [2] and [3].
- The experimental setting is somewhat unrealistic, as the paper assumes access to all objects and their attributes for every training image. In particular, the use of object position information (such as bounding boxes and 3D locations) during training significantly undermines the experimental results, as it contradicts the core motivation of object discovery. According to Figure 15, the proposed model performed worse than baseline models when trained without object position information.
- Referring to the semantic representation in the paper as VisXML is confusing, as there are no recursive structures involved. Only objects and their attributes are considered, which is not a substantial contribution.

### Questions
- Figure 7 shows only 100 grounding examples can have similar benefits on the downstream reasoning task compared with annotating the full dataset.  Does object discovery performance have the same trend? 
- Can the model handle cases where only a subset of the objects in every image are annotated?

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
This work focuses on grounding slots – tokens that have a learned correspondence to objects in images. The authors build upon prior work, specifically Slot Attention and DINOSAUR. Their contribution is in using datasets of object properties to further ground slots computed with Slot Attention. They do so by proposing a novel contrastive loss. This loss pairs object representations based on object properties with object representations based on visual slots and then applies a standard InfoNCE objective over correct and incorrect pairings. The correct pairings are computed by greedy assignment based on the feature vector dot product. The model is evaluated in unsupervised object segmentation, object and scene retrieval and few-shot classification across synthetic and real-world datasets.

### Strengths
1. The authors propose to use visXML descriptions of objects and their properties to better ground object slots in Slot Attention. This is a novel combination of the spatial biases in Slot Attention and the semantic biases in object-centric annotations.
2. The authors propose a nearest neighbor slot to semantic embedding assignment mechanism that is shown to lead to better representations than hungarian matching. The key insight is to assign object properties to slots without enforcing an exclusive 1-to-1 mapping.
3. The paper includes a number of evaluations of the quality of the learned slot representation, including unsupervised segmentation, scene retrieval and few-shot classification. Each experiment has reasonable baselines.

### Weaknesses
1. It is not clear to me why the object properties get concatenated and processed with an MLP in Equation 3. Do we assume that each object has the same set of properties? Are there any missing properties? Some kind of permutation-invariant model (e.g., a Transformer or a graph neural network) would be more flexible with respect to these questions. Specifically, the concatenation of potentially heterogeneous property vectors followed by an MLP seems like a brittle design choice. If objects have different numbers or types of properties, this would require padding or a fixed schema, which is not explicitly discussed. The lack of permutation invariance at this stage could also lead to inconsistent representations if the order of properties changes.
2. As far as I understand, the Transformer used in Equation 4 processes an entire scene. Doesn’t this result in a loss of distinction between individual objects to a certain extent, as we are presumably computing self-attention across all objects in the scene? I suppose this decision is already ablated in NSI-Schema Agnostic, which performs worse, but I am still curious about the rationale here. Would a per-object Transformer instead of a scene-level Transformer work? The concern is that the global context provided by the scene-level transformer might overshadow the individual object representations, making it difficult to isolate and manipulate individual object slots. The ablation study only shows that not using the schema transformer is worse, but does not explore the alternative of a per-object transformer.
3. The matching mechanism in Equation 6 might fail due to bad initialization, especially since Slot Attention is also sensitive to initialization. I would like to see a discussion of this. The greedy assignment based on the dot product could easily converge to a suboptimal matching, especially if the slot representations are not well-formed early in training. This could lead to a cascading effect where the contrastive loss is trained on incorrect pairings, further degrading the quality of the learned representations. A more robust matching strategy might be needed, or at least a more thorough analysis of the sensitivity of the current approach to initialization.
4. The $S_{xx}, S_{xy}, S_{yx}$ notation in Equation 7 can be confusing.

### Questions
Points 1 and 2 in Weaknesses.

Given the recent improvements in token-based visual encoders, do we still need Slot Attention? Couldn’t we just use the tokens from ViT-CLIP or DINOv2, compress them into a smaller set of tokens using a cross-attention layer (like in Perceiver and PerceiverIO) and treat these tokens as slots? It is possible that your schema based loss makes the spatial biases that Slot Attention encodes redundant. So, your method could potentially be used without Slot Attention, which would overcome the scaling limitations and instabilities of SA.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes neural slot interpreters, which provide an XML-like schema that uses simple syntax rules to organize the object semantics of a scene into object-centric schema primitives. It can learn to ground primitives into slots through an objective that reasons over the intermodal alignment. Experiments demonstrate that NSI tokenizers can achieve fewer tokens than other patch-based tokens.

### Strengths
1. This paper provides a contrastive learning objective that learns from image-schema pairs. This specific contrastive learning algorithm looks novel.

2. The proposed structured learning seems to benefit and outperform pure slot attention learning.

3. The experiment combining with vision transformers demonstrates slots as a better representation than patches.

### Weaknesses
1. The XML representation looks unnecessary, given a strong LLM model. Nowadays, multi-modal LLMs develop really fast, so as long as you have any testified representation, those language models can help you structure it into XML. In other words, the advantage of the proposed representation over the naive text representation (e.g., a caption model or a CLIP model) is very marginal.

2. The proposed experiments are limited in scale. CLEVR is too small to verify such an idea generally. The authors should experiment and report numbers on ImageNet. Also, ViT is not the SOTA, and it's interesting to see whether slot-based representations are better than patch-based ones.

3. Those slots are not accurately defined and it seems that those are just vector embeddings. Therefore, the reviewer doubts the motivation to research such slot-like representations.

4. The writing is not very clear. In fact, the methods are not explained very well (see questions below).

### Questions
1. What's the motivation for using two losses in Eq. 10? Those equations are introduced but not explained well. What's the connection of such a loss to contrastive losses used in prior works?

2. The bi-level architecture should be explained in the main text. What motivates learning the slot attention rather than learning a simple tokenizer? It seems that the authors wish to present a new tokenizer but it is neither simple nor scalable (to some other architecture).

3. What's the novelty of this work against general compositional learning works? The slot representations are not very well-defined and it's hard to claim novelty there.

### Soundness
3

### Presentation
2

### Contribution
1
