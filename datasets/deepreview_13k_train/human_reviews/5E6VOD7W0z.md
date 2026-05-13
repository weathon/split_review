# On Erroneous Agreements of CLIP Image Embeddings

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Recent research suggests that the failures of Vision-Language Models (VLMs) at visual reasoning often stem from \emph{erroneous agreements}---when semantically distinct images are ambiguously encoded by the CLIP image encoder into embeddings with high cosine similarity. In this paper, we show that erroneous agreements are not always the main culprit, as Multimodal Large Language Models (MLLMs) can still extract distinct information from them. For instance, when distinguishing objects on the left vs right in the What'sUp benchmark, the CLIP image embeddings of the left/right pairs have an average cosine similarity $>$0.99, and CLIP performs at random chance; but LLaVA-1.5-7B, which uses the same CLIP image encoder, achieves nearly 100\% accuracy. We find that the extractable information in CLIP image embeddings is likely obscured by CLIP's inadequate vision-language alignment: Its matching score learned by the contrastive objective might not capture all diverse image-text correspondences. We also study the MMVP benchmark, on which prior work has shown that LLaVA-1.5 cannot distinguish image pairs with high cosine similarity. We observe a performance gain brought by attending more to visual input through an alternative decoding algorithm. Further, the accuracy significantly increases if the model can take both images as input to emphasize their nuanced differences. Both findings indicate that LLaVA-1.5 did not utilize extracted visual information sufficiently. In conclusion, our findings suggest that while improving image encoders could benefit VLMs, there is still room to enhance models with a fixed image encoder by applying better strategies for extracting and utilizing visual information.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper provides a comprehensive study to analyze the answers supplied by the VLMs. Specifically, It compares the performances of CLIP and LlaVa-1.5-7B in the What’s Up and MMVP benchmarks. These benchmarks ask questions about a pair of images that contain the same objects and background but in different positions. This paper shows that the LlaVa-1.5-7B can perform better than CLIP in these benchmarks even when LlaVa uses CLIP as a visual encoder, and the average cosine similarity of the CLIP embedding of the image pair is greater than 0.95. Moreover, it provides ablation studies to explain this behavior.

### Strengths
This paper provides some interesting insights to show that the metric commonly used to measure the embedding similarity (Cosine Similarity) does not depict all aspects of vector pairs. Therefore, it suggested a complementary metric, Spearman’s rank correlation coefficient. However, table 1 only provides the average Cosine Similarity.

### Weaknesses
The paper is challenging to follow, primarily due to the absence of a clear statement of its main contributions in the Introduction. Its content closely parallels the CVPR24 paper, "Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs," raising concerns about the originality of this work. The CVPR24 paper highlights that Visual Language Models (VLMs), often relying on CLIP as the visual encoder, struggle with recognizing fine-grained details, such as object locations. It introduces the MMVP benchmark to evaluate these limitations comprehensively. I encourage the authors to clarify how their contributions provide novel insights beyond this existing research. The performance comparison between LLaVA-1.5 and its vision encoder, OpenAI-CLIP-L/336, on the MMVP-VLM benchmark is interesting. However, the analysis appears limited, as it includes only a single comparison. It would be better if the authors provided a more diverse and consistent comparison, not limited to OpenAI-CLIP-L-336 vs. LLaVA-1.5, but also EVA-01-CLIP-g vs. InstructBLIP (Vicuna7b, Vicuna13b, Flan T5xl). In this way, the authors can analyze the influence of the different Visual Encoders and the LLM architectures on the performance boost. Furthermore, while it is interesting to observe improvements in the instructional model, the gains may result from LLaVA training. It adapts the language model (LLM) to leverage the frozen vision encoder better. This could enhance the LLM’s ability to extract visual information from sequence embeddings compared to CLIP models relying on the CLS token to align with smaller and limited language models. However, despite these improvements, the overall performance remains suboptimal. Consequently, I do not find the claim that “LLaVA-1.5 can distinguish images with CLIP embeddings of high cosine similarity, indicating that erroneous agreements are not the bottleneck of their visual reasoning performance on image pairs” to be fully substantiated.

### Questions
I recommend including Spearman's rank correlation coefficient in Table 1 to enhance the analysis. Additionally, a more comprehensive study would be valuable. For example, could the authors provide Spearman's rank correlation coefficient and cosine similarity for the questions with the highest- and lowest-accurate answers?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper challenges the prevailing belief that Vision-Language Models' (VLMs) failures in visual reasoning are primarily due to CLIP image encoder's "erroneous agreements" (where distinct images have high cosine similarity). Using LLaVA-1.5-7B as an example, they demonstrate that MLLMs can successfully extract distinct information from similar image embeddings, achieving high accuracy on tasks where CLIP performs poorly. This suggests that the limitation lies not in the image embeddings themselves, but in how effectively models extract and utilize the encoded information.

### Strengths
Provides compelling empirical evidence through controlled experiments across multiple benchmarks.
Challenges and refines an important assumption in the field about VLM limitations.
Demonstrates that existing architectures might be more capable than previously thought, just requiring better utilization strategies.

### Weaknesses
The paper's scope might be too focused on LLaVA-1.5 as the primary example, potentially limiting the generalizability of findings
While the paper shows that information can be extracted from similar embeddings, it doesn't fully tackle why LLaVA-1.5 is able to do this.

### Questions
How do these findings generalize to other MLLMs beyond LLaVA-1.5?
What specific mechanisms allow MLLMs to extract distinct information from seemingly similar embeddings?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper examines the performance of LLaVA-1.5-7B on visual reasoning tasks, specifically WhatsUp and MMVP, and concludes that its suboptimal performance is not due to CLIP's visual features. While CLIP visual features effectively capture semantic similarities, they occasionally misinterpret spatial differences in object placement (e.g., "mug on the left" vs. "mug on the right"), which results in high cosine similarity (over 0.95) despite subtle image differences—referred to as "erroneous agreements." The authors show that CLIP’s visual features are accurate; instead, they attribute the performance issues to LLaVA not making effective use of these features. They further demonstrate that poor alignment between visual and textual inputs, not the visual features themselves, explains the bad performance in CLIP models for these tasks and datasets. Unlike CLIP, LLaVA does not exhibit this alignment problem, and this is shown quantitatively. Finally, the authors try better decoding strategies in Llava like M3ID such that the decoding better makes use of the visual features. They also show that  multiple image inputs works better to highlight the difference in images. They also explore performance gaps related to evaluation methods, training data, and the text encoder.

### Strengths
- This paper delivers a valuable message to the community by advocating for enhancing Multimodal LLMs and keeping the image encoder fixed. Previous research suggested that the image encoder introduced issues by producing "erroneous agreements" (similar embeddings for semantically similar but visually distinct images). However, this paper counters that claim, attributing the problem instead to the the model not utilizing these visual features effectively. 

- Interesting observation of better decoding algorithms and methods for evaluating specific tasks.

### Weaknesses
 - There is an incoherent story. The abstract initially suggests that LLaVA performs well on reasoning tasks and achieves high accuracy, yet later the paper claims LLaVA performs poorly on MMVP, contradicting the initial statement. They also mention that LLava is able to extract the correct information from the visual features, and that it does not face issues (L186, and demo image). Only later is it clarified that LLaVA performs well on WhatsUp but not on MMVP. In general, I feel there is an unclear and confusing story. 

 - WhatUp, MMVP, COCO-spatial and GQA-spatial are not really well-known datasets and publicly-agreed on to measure reasoning. I actually came to know them after reading this paper. Measuring reasoning on MMLMs are usually not done on these datasets. These datasets are not enough to reflect model reasoning and to come up with general conclusions about LLava or MMLMs in general. The authors don’t show ablation and analysis results using their ablation strategies, on important reasoning tasks such as VQA, GQA, OK-VQA, VCR and others (specifically, those that LLava reports on). I feel the scope, task and datasets are not enough to reach the standard required for ICLR.

### Questions
In general the second weakness is the biggest to me. I would like to hear what the authors say on this?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Previous works have argued that the poor performance of VLMs on simple visual reasoning tasks is due to their dependence on CLIP encoder. They show that CLIP can encode two visually different images with high cosine similarity (called erroneous agreement) and argue that many VLMs fail due because they use CLIP as their vision encoder.

In this paper the authors show that with better extraction and utilization methods, clip encoder can still be used for downstream tasks of visual reasoning. They show experiments with LLaVA-1.5 and show that it performs good on benchmarks despite using CLIP as its vision encoder.

### Strengths
1. Important analysis shown in section 4 (Investigating the performance gap)- this section answers the questions related to training data, language model and evaluation method. This analysis is important to make the claim that visual information extraction is the key factor in determining the performance gap on downstream tasks. And these other factors (eval method, language encoder, training data) are not contributing much to the improved performance.

2. Detailed benchmarking of the models on different datasets and good ablation studies.

3. They show, using a different decoding method, that even with a fixed pre-trained image encoder if we try to 'force' VLMs to attend to visual features while decoding (and not just relying on language priors), we can perform good on downstream visual reasoning tasks.  Although they used a previously proposed decoding strategy M3ID  (Favero et al., 2024).

### Weaknesses
1. The authors show that the visual feature extraction technique in LLaVA (a two layer MLP) is an important step in distinguishing between two erroneous images. But they do not provide an convincing argument on why is it an important step. An analysis on "why just adding a 2-layer MLP on top of pre-trained CLIP makes it so much better?" would have been an amazing addition to the paper. Specifically, the paper lacks a detailed investigation into the specific transformations performed by the MLP. For instance, do the two layers learn to amplify certain feature dimensions that are crucial for downstream tasks but are suppressed in the original CLIP embedding? Or does the MLP learn to disentangle features that are entangled in the CLIP space? Without such analysis, the claim that the MLP is a key factor remains somewhat superficial.

2. On Spearman's rank correlation (also asked in the questions): Since CLIP is trained using loss based on cosine similarity, I think using Spearman's rank correlation to show that two embeddings are "fully opposed" is not correct. For example, consider the example given on LN 232-233. Although the ranks of the dims are reversed giving  ρ = −1, their absolute values are pretty close. And if we assume (in an ideal world) them to be separable features, for example the embeddings could be of dog images and the features are 'ear-length' , 'fur color', 'nose-shape', both the embeddings will still show two very similar looking dogs (and not 'fully opposite') even though the embedding might have ρ = −1. The paper does not adequately address the limitations of using rank correlation in this context. While rank correlation can indicate an inverse relationship in the ordering of feature dimensions, it does not necessarily imply that the underlying semantic content of the embeddings is fully opposed. The authors should acknowledge that this is a specific interpretation of 'opposed' and that other interpretations are possible.

### Questions
Would a high negative Spearman's rank correlation show that the embeddings are quite different? 

LN 232-236 says: "While SC (fv(v1), fv(v2)) > 0.989, Spearman’s rank correlation coefficient can tell their sharp difference: ρ = −1, showing that they are fully opposed in this sense. Therefore, the difference in visual inputs might still be extracted through other means when erroneous agreements occur"

How does ρ = −1 show that the embeddings are 'fully opposed'? If the authors could show this or cite a paper that shows this, that would be great.

### Soundness
3

### Presentation
3

### Contribution
3
