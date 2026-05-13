# MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
Visual preference alignment involves training Large Vision-Language Models (LVLMs) to predict human preferences between visual inputs. This is typically achieved by using labeled datasets of chosen/rejected pairs and employing optimization algorithms like direct preference optimization (DPO).
Existing visual alignment methods, primarily designed for single-image scenarios, struggle to effectively handle the complexity of multi-image tasks due to the scarcity of diverse training data and the high cost of annotating chosen/rejected pairs.
We present \textbf{M}ulti-\textbf{I}mage \textbf{A}ugmented \textbf{D}irect \textbf{P}reference \textbf{O}ptimization (\textbf{MIA-DPO}), a visual preference alignment approach that effectively handles multi-image inputs.
MIA-DPO mitigates the scarcity of diverse multi-image training data by extending single-image data with unrelated images arranged in grid collages or pic-in-pic formats, significantly reducing the costs associated with multi-image data annotations.
Our observation reveals that attention values of LVLMs vary considerably across different images. We use attention values to identify and filter out rejected responses the model may have mistakenly focused on.
Our attention-aware selection for constructing the chosen/rejected pairs \textbf{without} relying on (i) human annotation, (ii) extra data, and (iii) external models or APIs.
MIA-DPO is compatible with various architectures and outperforms existing methods on five multi-image benchmarks, achieving an average performance boost of 3.0\% on LLaVA-v1.5 and 4.3\% on the recent InternLM-XC2.5.
Moreover, MIA-DPO has a minimal effect on the model's ability to understand single images.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents MIA-DPO, a multi-image DPO dataset construction approach for LVLMs without annotations from human or external models. The paper collects prompts from existing single-image dataset like LLaVA 665k, augmenting each data with unrelated images, which derives synthetic prompts of multiple images. Taking advantage of transformer's attention scores, rejected samples can be automatically filtered out to build pairwise preference answers for DPO. In addition, some post-selection methods are proposed for data cleaning. Experiment shows improvements on most multi-image and single-image benchmarks, and the capability to overcome hallucinations duo to the interference from unrelated images in prompts.

### Strengths
- The paper is clearly written. Most details are provided, so it should be easy to reimplement. 

- The proposed method is well-motivated. Hallucination suppression is an important topic in LVLMs. The paper presents a straight-forward way to address hallucinations from unrelated images in multi-image scenario, which seems very easy to follow and does not rely on human annotations. 

- Experiments are well organized. Extensive evaluations show the effectiveness of the proposed method. An interesting phenomenon is, although the synthetic DPO prompts appear highly biased, improvements are still obtained on **general** single-image and multi-image evaluations.

### Weaknesses
## Significance

My biggest concern is, the proposed synthetic method is designed to deal with the interference from unrelated images, however, which seems only a **corner case** in LVLMs. In practice, typically all images in the question prompt contribute to the final answer. It is a great challenge (but more important) to generate preference data for such *real* multi-image prompt at scale without much cost. The paper does not involve the topic. Therefore, I think the title "Multi-Image Augmented Direct Preference Optimization" may somewhat overclaim the contribution. 

To improve the work, I think the authors may defend their contributions by analyzing the root of the improvements on general benchmarks. For example, an interesting topic may be "does the proposed synthetic DPO dataset also help to suppress more general hallucinations other than those in Line 212?"; if yes, why?


## Experiment

I feel some empirical results are weak because: 
 
- According to Table 3, parts of the improvements are resulted from data cleaning (especially on MMMU and BLINK), which is not the unique technical contribution of the paper.

- In Eq 5, the NLL term plays a role of supervised fine-tuning with only chosen answers. It is an important baseline (i.e. fine-tuning with isolated NLL term) which can reflect the effectiveness of rejected samples, but not provided in the experiment.

### Questions
* In Eq 4, please clarify how to calculate R(y) in details. Is the summation of attention values computed over all layers, attention heads and tokens subject to the given image/region?

### Soundness
3

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
3

### Summary
This paper introduces MIA-DPO, a visual preference alignment approach for LVLMs that handles multi-image tasks. The authors propose extending single-image data with unrelated images and using attention patterns to detect hallucinations, allowing construction of chosen/rejected pairs without human annotation or external APIs. The method shows promising results on both multi-image and single-image benchmarks.
Overall, I believe this is a solid paper that addresses an important and under-explored problem. It makes meaningful contributions to visual preference alignment for multi-image scenarios, though there are some aspects that need clarification.

### Strengths
* While there's been significant work on visual preference alignment for single images, multi-image alignment remains largely unexplored despite its real-world importance. The authors identify key challenges like data scarcity and high annotation costs.
* Rather than collecting new multi-image data (which would be expensive), they augment existing single-image data through sequence, grid collage, and pic-in-pic formats. Using attention patterns to select rejected samples is an elegant way to avoid costly human annotation or API calls.
* The authors test on 5 multi-image benchmarks and 7 single-image ones, showing clear improvements (+3.0% on LLaVA-1.5, +4.3% on InternLM-XC2.5) while maintaining single-image performance. The ablations examining different components are thorough.

### Weaknesses
However, I have several concerns that I think should be addressed:
My main concern is about the attention-based selection method. While using attention patterns to detect hallucinations is interesting, the threshold selection feels somewhat ad-hoc. The authors set different thresholds based on image counts (0.7/0.6/0.5/0.5 for 2/3/4/5 images), but there's limited justification for these specific values. I wonder if these thresholds could be learned automatically rather than manually set.
The relationship between augmentation strategies and model performance isn't fully explored. While the authors try three formats (sequence, grid collage, pic-in-pic), there's limited analysis of how different ratios of these formats affect results. Some discussion of which formats work better for what types of queries would be valuable.
The ablations, while informative, don't completely isolate the impact of different components. It would be interesting to see how model size affects the attention patterns and overall performance. Additionally, some analysis of failure cases would help understand the method's limitations.

### Questions
Have you analyzed how sensitive the results are to the attention thresholds? What happens if you use uniform thresholds across different image counts?
For the post-selection filtering, how did you choose the specific metrics (perplexity, length ratio, edit distance)? Were other metrics considered?
Your method improves most on the Mantis benchmark (+11.1%). Any insights into why the gains are particularly large there?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors address the performance limitations of existing Large Vision Language Models(LVLMs) in multi-image tasks, identifying the difficulty of constructing multi-image preference data at low cost as a critical constraint. To tackle this issue, the authors propose Multi-Image Augmented Direct Preference Optimization (MIA-DPO), which can efficiently scale single-image training data to multi-image data without relying on human annotations or external APIs. In terms of data construction, MIA-DPO designs three expansion methods—Sequence, Grid Collage, and Pic-in-Pic to extend single-image data into multi-image version. Additionally, to address the common visual hallucinations of sequence confusion and element interference in  multi-image tasks, a hallucination detection mechanism based on attention values is designed for the constructed multi-image data. The authors conducted ablation experiments on LLaVA-v1.5 and InternLM-XC2.5, and the results demonstrate that the proposed MIA-DPO can enhance performance on multi-image tasks such as MVBENCH without compromising single-image metrics like MMMU.

### Strengths
1. Research on visual hallucinations in large vision-language models is significant as it can improve the general capabilities of these models.
2. This paper presents an efficient pipeline for constructing and filtering multi-image preference data, which can generate large amounts of multi-image preference data at a low cost, making it highly applicable.
3. The paper analyzes the prevalent sequence confusion and element interference phenomena in large vision-language models for multi-image tasks from the perspective of attention, identifying that the key influential factor of these multi-image hallucinations is incorrect attention distribution.

### Weaknesses
1. The authors mention at the beginning of the paper that existing multi-image SFT methods can degrade performance on single-image tasks while improving multi-image performance. However, they do not compare their approach with these methods in the experimental section.
2. Although the MIA-DPO method can easily convert data into SFT format, the authors do not compare the performance changes of the model after SFT using the same source data.
3. When evaluating the model's single-image performance, only MMMU is used, without assessing performance on other widely recognized benchmarks such as MMStar, MMBench, and OCRBench.
4. For evaluating the model's multi-image performance, the authors could use the Sequence, Grid Collage, and Pic-in-Pic methods to construct multi-image VQA test sets from existing single-image VQA data, directly assessing improvements in sequence confusion and element interference.
5. While handling more images is crucial for large vision-language models, the paper does not analyze whether MIA-DPO can still provide stable benefits when the number of simultaneously appearing images increases significantly (e.g., 10+ images).

### Questions
1. How does the model's performance change on other single-image or multi-image metrics before and after applying MIA-DPO? (Refer to Weaknesses)
2. Can MIA-DPO still provide stable benefits when the number of images is expanded? (Refer to Weaknesses)
3. Can experiments be conducted on more advanced open-source large vision-language models or those explicitly supporting multi-images, such as the Qwen-VL series and Tarsier?

### Soundness
2

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
3

### Summary
This paper proposes MIA-DPO, a method for improving the Large Vision Language Modle (LVLM) with multiple images. The main idea of MIA-DPO is finding the rejected prompts by using attention from pretrained LVLM and using the DPO training to fine-tune the LVLM for multiple image settings. Through the proposed MIA-DPO, the paper achieves better performance on multiple image settings than the baseline LVLM, without needing 1) The data for the multiple image setting and 2) external sources such as human/ChatGPT for creating feedback in the RLHF/RLAIF methods.

### Strengths
- The motivation of this paper is clearly stated, which helps the reader a lot in understanding the idea.

- The proposed **Attention Aware Selection** can alleviate the problem of multiple image prompt datasets requirement and the need for external human/module in RLHF/RLAIF approaches.

- The experiments show the effectiveness of the method against the baselines.

### Weaknesses
**Clarification**:
- Can the authors provide a more specific way to compute $A_{target}$ and $A_{sum}$ in L306? In L306-L307, the paper states that "$A_{target}$ be the amount of attention directed toward the target defined in $x$", however, as defined in L150, $x$ consists of $v$ and $t$, and as mentioned in Figure 2, only the attention on the given images $v$ is considered. 
- Which are the layers used to extract the attention $A_{target}$ and $A_{sum}$?
- In section 3.3.3, what are the parameters we need to optimize in the proposed method?

**Experiments**:
- In Table 1 and Table 2, why do the authors not include "RLHF", "HA-DPO" and "POVID" in InternLM-XC2.5?
- In Table 1, why LLaVA-RLHF, HA-DPO, and POVID are worse than LLaVA?

### Questions
All the concerns and questions are listed in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2
