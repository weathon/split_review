# SAM-CP: Marrying SAM with Composable Prompts for Versatile Segmentation

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
The Segment Anything model (SAM) has shown a generalized ability to group image pixels into patches, but applying it to semantic-aware segmentation still faces major challenges. This paper presents SAM-CP\footnote{This work was done when Pengfei Chen <chenpengfei20@mails.ucas.ac.cn>
was an intern at Huawei Inc. \\ \textsuperscript{*} Corresponding author: Zhenjun Han <hanzhj@ucas.ac.cn>.}, a simple approach that establishes two types of \textbf{c}omposable \textbf{p}rompts beyond SAM and composes them for versatile segmentation. Specifically, given a set of classes (in texts) and a set of SAM patches, the Type-I prompt judges whether a SAM patch aligns with a text label, and the Type-II prompt judges whether two SAM patches with the same text label also belong to the same instance. To decrease the complexity in dealing with a large number of semantic classes and patches, we establish a unified framework that calculates the affinity between (semantic and instance) queries and SAM patches and merges patches with high affinity to the query. Experiments show that SAM-CP achieves semantic, instance, and panoptic segmentation in both open and closed domains. In particular, it achieves state-of-the-art performance in open-vocabulary segmentation. Our research offers a novel and generalized methodology for equipping vision foundation models like SAM with multi-grained semantic perception abilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SAM-CP, which integrates composable prompts for versatile segmentation. It utilizes two levels of queries—semantic and instance—to assign unlabeled patches from SAM with appropriate labels.

### Strengths
- The overall architecture designs are well-grounded. The two types of prompts for semantic and instance understanding are intuitively designed to support different segmentation tasks.

- SAM-CP models the two types of prompts with separated queries for better efficiency. The quantitative results on open-vocabulary segmentation also demonstrate the effectiveness of this query-based approach.

- Thorough analysis is provided for the advantages and limitations of the proposed method.

### Weaknesses
 - The running time might be a potential issue due to the two-level prompt design (especially if an iterative approach is used). A comparison of running time performance with the original SAM and other segmentation models would be informative.

- Experiments: The current baselines do not include models based on SAM. Therefore, it's unclear whether the performance improvements come from the composable prompts or the internal capacity of SAM. Adding baselines building on SAM that perform instance [1] and semantic [2] segmentation can be incorporated to further demonstrate the effectiveness of the proposed composable prompts.

- The figures are low-resolution and notably blurry. Replacing them with high-resolution versions would improve readability and presentation quality.

- The performance of SAM-CP on closed-domain segmentation is not superior over other baselines.

### Questions
The design of SAM-CP relies solely on SAM's final predictions, disregarding intermediate features from SAM that could potentially enhance the decoder's performance. It would be valuable to include discussions on this aspect and to investigate whether integrating SAM's intermediate features with the proposed decoder could yield improved results.

### Soundness
3

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
4

### Summary
This paper proposes a framework that combines SAM and CLIP for open-vocabulary universal segmentation.

### Strengths
1. The proposed model keeps the zero-shot abilities of CLIP. This is supported by experiments on open-vocabulary segmentations.
2. The ablation studies are sufficient and well explain the design choice of loss functions.
3. This method is easy to follow, with many intuitive figures and visualizations.

### Weaknesses
1. The experiments on open-vocabulary segmentations (Table 1) are not well supportive. SAM-CP combines SAM and CLIP but is only comparable to FC-CLIP that is built with CLIP only. Also, the experiments on closed-vocabulary segmentations (Table 2) do not best address the potential of combining SAM and CLIP since it is worse than CLIP-only X-Decoder and supervised SOTA MaskDINO. The open-vocabulary results are especially concerning given the architectural complexity introduced by integrating SAM, which should ideally yield a more substantial performance gain over a CLIP-only baseline. The fact that it only achieves comparable results raises questions about the effectiveness of the SAM integration.
2. The advantages of the proposed framework are not well discussed or presented. The performances are only comparable to previous SOTA. This paper should look for more perspectives to highlight its advantages, e.g. efficiency, part segmentation (also see Question 1), few-shot capabilities, out-of-domain generalizations, etc. The paper needs to articulate the specific scenarios where SAM-CP would be preferred over existing methods, given its comparable performance. Without a clear advantage, the motivation for using this approach is weak.
3. It could be more convincing if this paper can compare to other SAM-based methods on the same settings and show its advantages. For example, [1] and [2] also work on open-vocabulary segmentation with SAM. A direct comparison with other SAM-based methods is crucial to establish the novelty and superiority of the proposed approach. Without this comparison, it's difficult to assess whether the method offers any real improvement over existing SAM-based techniques.
4. As already discussed and illustrated in the paper, SAM-CP fails at small objects since there are no prompts on small objects. The efficiency is limited by SAM. The reliance on SAM's prompting mechanism, particularly the fixed grid of point prompts, inherently limits the method's ability to detect and segment small objects. This is a significant limitation that needs to be addressed or at least more thoroughly discussed.

### Questions
1. SAM can generate fine-grained masks for part, e.g. head, hand, body. Does SAM-CP have the potential to work on open-vocabulary part segmentation? Quantitative experiments and comparisons to related works like HIPIE would enhance the applicability of this work.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents SAM-CP that extends SAM by incorporating composable prompts to improve segmentation. SAM-CP utilizes Type-I prompts to align SAM-generated patches with text labels and Type-II prompts to merge patches belonging to the same instance based on the text information. Experimental results show that SAM-CP performs well in open-vocabulary segmentation and shows some improvement in semantic discriminativity across various segmentation types.

### Strengths
1. This work presents a method for improving SAM for versatile segmentation.

2. SAM-CP considers segmentation tasks from a novel perspective, introducing two types of composable prompts: Type-I for matching SAM patches with text labels and Type-II for merging patches belonging to the same instance.

3. The dynamic mechanism offers novel design insights for handling cross-attention computations.

4. Generally, the paper is well-written.

5. The figures and tables are informative.

### Weaknesses
1. Prompt I classifies each SAM-segmented patch, potentially leading to ambiguities. For example, without contextual information, it’s challenging to determine if a patch representing clothing on a person should be classified as part of the person or as an independent clothing item. The proposed CP lacks a clear strategy to handle the inherent ambiguity in segmentation without surrounding context. This is particularly problematic when dealing with complex scenes where objects are occluded or have intricate relationships.

2. The performance gains are not significant, such as mIoU for the COCO->ADE20K and COCO->Cityscapes settings in Table 1. The improvements, while present, do not demonstrate a substantial leap in performance that would justify the added complexity of the proposed method. This raises questions about the practical utility of SAM-CP in scenarios where marginal gains are not sufficient.

3. Table 2's comparison may be unfair due to the use of SAM, which is trained on a significantly larger scale. This complicates attributing improvements directly to the proposed method. The comparison does not isolate the contribution of the proposed composable prompts from the pre-existing capabilities of SAM, making it difficult to assess the true effectiveness of SAM-CP.

4. Although SAM-CP's speed heavily relies on SAM, the paper lacks a clear analysis of the computational efficiency of the proposed non-SAM modules. It is crucial to examine whether these modules actually enhance efficiency. Without a detailed breakdown of the computational cost of the non-SAM components, it's unclear if the method introduces any bottlenecks or if it truly offers a practical advantage in terms of processing time.

5. Other Issues:
- Figure 1's many colors and mixed visual elements are hard to read. The visual clutter makes it difficult to understand the proposed method's workflow and the interaction between different components.
- The description of patches needs greater specificity. For example, as vaguely mentioned in Line 139, it's not specified if the patches are segments from SAM's segment-everything mode or just features from SAM's backbone. The lack of clarity regarding the nature of the patches makes it difficult to reproduce the results and understand the method's implementation details.

### Questions
1. I would like to know if SAM-CP has effective strategies for addressing the aforementioned issues of segmentation ambiguity?

2. Although the speed is influenced by SAM's computational efficiency, can you provide a detailed analysis of the speed of non-SAM modules and compare it with other SAM-based methods? Alternatively, could replacing SAM with a lightweight variant like EfficientSAM provide sufficient performance and computational efficiency for comparison with non-SAM methods?

3. Does SAM-CP offer any advantages in training time compared to other SAM-based methods?

4. Since SAM's segmentation results may not always be precise, the Affinity matrix used by the Unified Affinity Decoder could potentially accumulate errors. How is this issue addressed?

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
**Objective**

SAM-CP proposes a method to further refine the output of the Segment Anything Model (SAM). The aim is to transform SAM’s original, class-agnostic, variance-scale patches into two more informative segmentation types: Semantic Segmentation and Instance Segmentation.

**Proposed Framework**

The training framework operates as follows:

- Input: The framework takes the initial class-agnostic segments (CA-segments) from SAM, along with category text.
- Processing:
SAM Patches: The SAM patches are first processed through self-attention.
Queries: Queries (which can be target categories in text or instance queries) are processed through self-attention, then used to refine the features by performing cross-attention with the SAM patches.
Affinity Calculation: The resulting  N  patch features and  M  query features are used to calculate affinity for instance grouping.
Semantic Classification: Finally, the learned features are compared with CLIP text input features for semantic classification.

The entire pipeline is trained in a fully supervised, end-to-end manner.

**Results**

Experiments show that this framework achieves state-of-the-art (SOTA) results when trained on one dataset and tested on another.

### Strengths
1. I believe this task is important. Transforming the class-agnostic SAM into a usable semantic and instance segmentation is a valuable pursuit. This directly connects to the question of how to leverage the advance of large-scale vision foundation models into practical application.

2. The proposed method demonstrates strong performance on commonly used open-world segmentation frameworks, achieving state-of-the-art (SOTA) results when trained on one dataset and tested on another. This includes benchmarks such as: COCO → ADE20K; ADE20K → COCO; COCO → Cityscapes

3. The overall experinement and results presentation is good.

### Weaknesses
# At a higher level:
The advantage of SAM lies not only in its ability to segment an entire image but also in its prompt-based segmentation, which introduces more accurate masks.
I think this method uses SAM only as an initial “superpixel” generator, which somewhat overlook SAM’s full potential.

# Generalization:
The proposed method requires training on specific datasets to learn how to merge patches, which seems to be not very generalizable.
This approach may not translate well from natural images to medical images, or even from natural images with large object segments to tasks requiring finer, more detailed segmentation. Is this the case in this setting. Would like to hear author feedback on this point.

# Splitting and Merging:
The proposed method only focuses on merging, which to some degree simplifies the problem. I believe splitting is equally important as merging, though it seems it is not within the scope of this method.

# Comparison with Other Methods:
Most of the results are compared with pre-SAM methods. I wonder how this method compares with other SAM-based semantic segmentation/instance segmentation methods, such as Grounding SAM and SEEM etc. It would be interesting to see a comparison with other SAM-based methods and discuss the advantage of such approach.

### Questions
1. At line 150, the authors state that the two prompts can be iteratively called when finer-level segmentation is required. I’m not entirely sure I understand this; my impression is that granularity is determined by SAM’s results. Could the authors clarify this point?

2. How do the authors view this approach in comparison to SAM-based generalized segmentation? Most other approaches appear to be training-free and straightforward to use. It would be interesting to discuss the advantages that SAM-CP offers.

### Soundness
3

### Presentation
3

### Contribution
2
