# METRIS: Multi-Expressions for Transformer-based Referring Image Segmentation

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Referring image segmentation (RIS) aims to precisely segment a target object described by a linguistic expression. Recent RIS methods have introduced Transformer-based networks that use vision features as query and linguistic expression features as key-value to find target regions by referring to the given linguistic information. Since the Transformer-based network predicts based on the guidance information that guides the network on which regions to pay attention, the capacity of this guidance information has a significant impact on segmentation results in Transformer-based RIS. However, existing methods rely only on linguistic tokens as the guidance elements, which are limited in providing the visual understanding of the fine-grained target regions. To address this issue, we present a novel Multi-Expression guidance framework for Transformer-based Referring Image Segmentation, METRIS, which allows the network to refer to the visual expression tokens as the guidance information alongside the linguistic expression tokens. The introduction of visual expression can complement the capability of linguistic guidance by effectively providing the target-informative visual contexts. To generate the visual expression from vision features, we introduce a visual expression extractor that is designed to endow with the target-informative visual guidance ability and to acquire rich contextual information. This module strengthens the adaptability to the diverse image and language inputs, and improves visual understanding of the fine-grained target regions. Extensive experiments demonstrate the effectiveness of our approach across the commonly used RIS settings and the generalizability evaluation settings. Our method consistently shows strong performance on three public RIS benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper propose a new model for referring image segmentation. The authors propose a visual expression extractor to selectively model the shared representation between visual and language modality. The proposed model achieve new state-of-the-art on various referring image segmentation benchmarks.

### Strengths
+ The paper is overall easy to understand

+ The proposed model achieve decent performance on various referring image segmentation benchmarks

+ The authors provide various analysis such as generalization and various ablation studies.

### Weaknesses
 - The contribution is limited. The authors argue that previous methods cannot capture the target-informative visual understanding, but I believe they can do via cross-attentions. And actually, the proposed method is a set of cross-attentions. I think the proposed method consists of several cross-attentions and token selection that is popularly used in the recent literatures in various fields.

- The ablation studies are not through. To show the effectiveness of the proposed component, I recommend the authors to add more cross-attention mechanism to keep the number of total learnable parameters similar.

- Comparison with recent SOTA methods is missing. For example, [ref1] produces better results on RefCOCO test A. [ref2] produces better results on many benchmarks. And, [ref3] is also worth to be mentioned in the paper

### Questions
1. I'm curious why the proposed method is strong on unseen classes. the proposed method learns to attend/correlate for seen categories, so may be overfitted to seen classes and may not be generalized to unseen categories. More motivations and analysis on unseen classes would be great.

### Soundness
3

### Presentation
3

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
This submission focuses on the problem of Transformer-based referring image segmentation (RIS) and introduces the idea that Transformer-based RIS methods utilize guidance information to guide the prediction of referring regions. However, the submission proposes that existing guidance approaches rely solely on linguistic tokens. To address this limitation, they propose a visual expression extractor that generates visual expression tokens as a complement. Experiments are conducted on three public RIS benchmarks.

### Strengths
- The submission is well-written and easy to follow. Additionally, the figures and tables are well-prepared and clearly illustrate the motivations and methods.
- The idea of using visual tokens to complement guidance is straightforward.
- Experiments are conducted on multiple common benchmarks and across different settings.

### Weaknesses
 - From both the ablation study and comparisons (noting that some SOTAs are not included), the performance improvement of the proposed METRIS is limited and does not effectively demonstrate its effectiveness.
    - In Table 1, the improvement of METRIS over the previously best-performing methods is quite limited:
        - mIoU metric. The submission does not report the results for CGFormer, but the performance of this submission is only comparable to that of CGFormer. And the comparison between CGFormer and the submission is listed below:
            
            CGFormer  76.93 78.70 73.32 68.56 73.76 61.72 67.57 67.83 65.79
            
            METRIS       76.97 78.89 73.63 68.63 73.88 61.94 67.85 67.97 65.86
            
        - oIoU metric. The improvement of the proposed METRIS relative to LQMFormer is minimal.
    - In Table 1, some of the latest SOTAs, such as those[1,2] published in CVPR 2024 for RIS, are not included or compared. The performance of METRIS is lower than that of these methods.
        
        [1] Prompt-Driven Referring Image Segmentation with Instance Contrasting
        
        [2] Mask Grounding for Referring Image Segmentation
        
    - In Table 6, the baseline itself achieves good results, and the improvement over the baseline is quite limited.
- The novelty and technical contribution are insufficient.
    - Previous methods, even when utilizing "linguistic tokens," incorporate visual-language alignment and querying modules that effectively embed visual information within those tokens. They are referred to as "linguistic tokens," but they effectively function like visual tokens due to the visual-language alignment and querying modules. This paper merely makes the use of visual tokens explicit to provide further supplementation, which is an incremental gain.
    - Essentially, this approach adds attention between linguistic and visual tokens to aggregate visual information, which is a common practice in the vision-language domain.
- Table 6 does not include results for RefCOCO+ validation, while Table 7 presents results for the visual expression extractor only for RefCOCO+ validation. Both tables need to provide complete results to better understand the role of the visual expression extractor within the overall framework and the contribution of its individual modules.
- The qualitative results provide a comparison; however, they do not sufficiently demonstrate that the improvements are attributable to the visual tokens. A more in-depth comparison and analysis are required.
- Minor (does not affect rating): The figures appear blurry. Please use vector graphics or high-resolution images.

### Questions
- Visual tokens may encompass multiple regions, some of which could be referring regions and others that are not. Could the non-referring regions potentially act as distractions?

### Soundness
2

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
5

### Summary
This paper introduces a novel Multi-Expression guidance framework for Transformer-based Referring Image Segmentation, called METRIS, designed to improve segmentation accuracy by incorporating both visual and linguistic expressions as guidance. METRIS enhances segmentation using a visual expression extractor, which provides detailed visual context to complement linguistic guidance.

### Strengths
1. The proposed visual expression extractor enhances the adaptability to diverse image and language inputs and improves visual understanding of the fine-grained target regions.
2. The source code is attached, which can help the reviewers to check more model details.

### Weaknesses
- The SOTA comparison with [1] is missing in Table 4. Combining Tables 1 and 5 could save space, allowing for the inclusion of additional methods for comparison.
- The performance of this method does not achieve state-of-the-art compared to PolyFormer, published in CVPR 2023, as seen in Table 8.
- The contrastive loss in Equation (4) appears similar to the loss in CRIS, so the citation should be added in the appropriate place.
- The motivation for this work is unclear; it appears that visual expressions are sampled through filtering and thresholding strategies, which are then reframed as a “guidance set” from my perspective. 

Other minor issues:
- In Line 225, the source of the relevance score map $s$ is not explained. 
- The font size in Figures 1 and 2 is too small, causing the text to blur when zoomed in.
- Ablation: removing steps 1, 2, and 3 from the visual expression extractor could further demonstrate the effectiveness of the proposed method.

### Questions
See weakness.

### Soundness
2

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
This paper introduces a Multi-Expression guidance framework for Referring Image Segmentation (RIS) that enhances Transformer-based networks. Unlike traditional RIS methods that rely solely on linguistic tokens for guidance, METRIS overcomes this limitation by incorporating visual expression tokens alongside linguistic ones, enabling the network to access more informative visual contexts. A visual expression extractor is introduced to generate semantic visual expressions, enhancing adaptability to diverse image and language inputs. Extensive experiments demonstrate that METRIS improves visual understanding and consistently outperforms state-of-the-art methods across three public RIS benchmarks.

### Strengths
- This paper produces the target-informative visual expression for Transformer-based referring image segmentation.
- This paper presents a visual expression extractor designed to provide target-oriented visual guidance and capture rich visual contexts of fine-grained target regions, thereby enhancing adaptability to diverse scenarios.
- Experiments on three public RIS benchmarks demonstrate its effectiveness.

### Weaknesses
 - I'm a bit confused about the motivation behind the paper. The task involves segmenting the target object area given a query, but the paper combines target information with text input. Doesn’t this amount to leaking explicit prior information—essentially guiding the model to find the corresponding location in the image? This seems to weaken the inherent difficulty of the task.
- Collecting informative visual regions based on all word tokens, including meaningless ones like "the" and "an," seems inappropriate. These tokens do not carry relevant information for identifying the target object and may introduce noise into the process. It would be more effective to focus on meaningful tokens that contribute to understanding the target context.
- It seems that the operations in the paper are quite complex. How does the complexity of this method compare to existing approaches?

### Questions
- I'm a bit confused about the motivation behind the paper. The task involves segmenting the target object area given a query, but the paper combines target information with text input. Doesn’t this amount to leaking explicit prior information—essentially guiding the model to find the corresponding location in the image? This seems to weaken the inherent difficulty of the task.
- Collecting informative visual regions based on all word tokens, including meaningless ones like "the" and "an," seems inappropriate. These tokens do not carry relevant information for identifying the target object and may introduce noise into the process. It would be more effective to focus on meaningful tokens that contribute to understanding the target context.
- It seems that the operations in the paper are quite complex. How does the complexity of this method compare to existing approaches?

### Soundness
3

### Presentation
3

### Contribution
3
