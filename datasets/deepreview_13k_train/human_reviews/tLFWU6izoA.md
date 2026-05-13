# Diffusion Feedback Helps CLIP See Better

- Decision: Accept
- Scores: 6, 5, 6, 8, 8

## Abstract
Contrastive Language-Image Pre-training (CLIP), which excels at abstracting open-world representations across domains and modalities, has become a foundation for a variety of vision and multimodal tasks.
However, recent studies reveal that CLIP has severe visual shortcomings, such as which can hardly distinguish orientation, quantity, color, structure, \etc.
These visual shortcomings also limit the perception capabilities of multimodal large language models (MLLMs) built on CLIP.
The main reason could be that the image-text pairs used to train CLIP are inherently biased, due to the lack of the distinctiveness of the text and the diversity of images.
In this work, we present a simple post-training approach for CLIP models, which largely overcomes its visual shortcomings via a self-supervised diffusion process.
We introduce \ours, which uses the \textbf{{D}}\textbf{{I}}ffusion model as a \textbf{{V}}isual \textbf{{A}}ssistant for CLIP.
Specifically, \ours leverages generative feedback from text-to-image diffusion models to optimize CLIP representations, with only images (without corresponding text). 
We demonstrate that \ours improves CLIP's performance on the challenging MMVP-VLM benchmark which assesses fine-grained visual abilities to a large extent (\eg, 3-7\% ↑), and enhances the performance of MLLMs and vision models on multimodal understanding and segmentation tasks. 
Extensive evaluation on 29 image classification and retrieval benchmarks confirms that our framework preserves CLIP's strong zero-shot capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to improve some CLIP's shortcoming cases, e.g., understanding the quantity,color,structure of images, since CLIP is trained by focusing on the high level semantic features. Motivated by this issue, the paper proposed to leverage a diffusion model to assist the improvement of CLIPs and inject the CLIP features as a condition into the diffusion model. The design brought a significant performance gain on the MMVP-VLM benchmark as well as the Llava 1.5 and segmentation tasks without impairing the other benchmarks.

### Strengths
1. the paper is well written and easy to follow.
2. The improvement on the MMVP-VLM benchmark is significant.
3. The experiment is well designed and comprehensive.

### Weaknesses
1. The hypothesis of this paper is not well explained, and the solution is a little bit ad-hoc. In detail, the failure of CLIP on several typical cases mentioned in the paper should be better studied and analyzed instead of just citing a few papers and mentioning very shortly. Are the failure cases caused by the architecture design, training strategy or just the lack of training data is unknown. Only given such analysis, we can start to think of a solution to improve. On the contrary, the paper just proposed to use diffusion model to help CLIP output more detail or low-level features directly, which is less convincing to me.

2. Several settings of this paper are also ad-hoc. For instance, in L225 - L241, the paper discussed the 'Visual Recap Density'. It seems for different CLIP variants, the density is way different, and I can hardly find any relationship across them. A more scientific way to decide the density should be considered. Similar thing for the times of the condition is used. The paper chooses 2 (N=2). I'm curious how this number is determined and how the performance will change for different numbers, e.g., N=10, 100.

3. From my understanding, the paper used CC3M dataset to tune a pretrained CLIP. I wonder whether the gains on the benchmarks are just brought by tuning the CLIP with CC3M or the diffusion model?

4. The rows 3-4 in Table 6 is confusing. When the textual condition is used, how the vision encoder can be trained?

### Questions
See the weakness above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript introduces DIVA, a fine-tuning framework to enhance CLIP's fine-grained visual capabilities using a text-to-image diffusion model. DIVA tunes CLIP through diffusion loss with a frozen diffusion model conditioned by the CLIP outputs. To be specific, DIVA introduces a heuristic design for CLIP output-conditioned diffusion model, which leverages randomly dropped CLIP output sequences. Throughout experiments, it demonstrates improvements in extensive benchmarks including MMVP-VLM.

### Strengths
- Learning a good discriminative representation from image generation loss is now new, but I think it still has a big potential and should be studied. In this regard, the proposed idea of fine-tuning a pre-trained discriminative model (CLIP) via a pre-trained generative model (Diffusion) is interesting and demonstrates its potential.

- The authors evaluate DIVA across various benchmarks, including multimodal understanding such as MMVP-VLM, the backbone of LLaVA, zero-shot classification, and segmentation.

### Weaknesses
 - Overall, this manuscript lacks detailed motivations and explanations. It is unclear why this approach is needed - e.g., Why does CLIP need diffusion feedback and how does it help? Why this particular approach is superior to others?

- The training process involves sampling multiple random states of the diffusion process for each image, which can be computationally expensive. There is insufficient discussion on whether this cost is justified and whether the gains are significant enough under these costs.

- The proposed diffusion's condition design (section 3) is quite heuristic and overall improvements are not consistent and even not significant in many cases. For example, none of the cases in Tables 1, 2, 4, 5, 7, and 8 show consistent improvements in all metrics. Moreover, many metrics indicate the improvements are marginal so I am uncertain that the proposed method effectively works and can generalize well across different types of visual challenges..

- There is a lack of analysis on potential trade-offs when using diffusion models as feedback. The paper does not clearly address whether the alignment between the CLIP's text encoder and visual encoder might degrade over time, potentially affecting performance, despite there being no consideration of the text encoder in the proposed training framework.

### Questions
Please see the weakness section.

### Soundness
2

### Presentation
2

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
The paper utilizes the diffusion model to improve CLIP features' spatial and visual understanding. As CLIPs are only trained with global visual token, it lacks the ability to understand fine-grained visual concepts. At the same time, the diffusion model is trained to model the image distribution, thus it inherently has a better visual understanding. Given this idea, the paper tries to fine-tune CLIP model with a diffusion model guidance. 

In details, the proposed method sends the global token and random-sampled local tokens as a condition to a diffusion model. The gradient back from the diffusion loss is used as guidance to optimize the CLIP model. Based on this, the paper presents detailed ablation studies and shows improvement for visual understanding.

### Strengths
1. The paper follows a clear intuition on how to improve the CLIP model with better visual understanding. The utilization of diffusion model to improve CLIP model is overall a nice idea.

2. The paper presented a method to use both the global tokens and local tokens to improve the visual encoder. The paper also found that the percentage of used local tokens is important and conducted experiment to validate that. 

2. The paper analyzes the method on multiple tasks and thus the improvement is better shown.

3. The paper shows ablation studies for key designs of the method (some are actually the analysis of the method).

### Weaknesses
Weaknesses: 

- The paper's clarity of the method needs to be improved. Usually, the presentation (i.e., writing) of the paper would not be directly treated as weakness and some of them are put in suggestions below. However, the ambiguity in current method description does affect the reader's understanding of the paper method, and affect the assessment of the paper during review. Thus the reviewer put it as a weakness to highlight it and hope that it can be improved during rebuttal. I list some points here:
  
   1. For Sec 3.3, it is unclear how the "visual features combined with the empty text’s embeddings" are actually used. Is this simply an expansion of the context? The text needs to be more specific about how these are combined and fed into the diffusion model.
   2. From my current understanding, the visual features (patches) are feed as the text embeddings to the diffusion model pipeline. It would be better to have any analysis on the validity of doing this (at least have some discussions regarding this as it is not an natural operation). Specifically, what is the justification for treating visual patch embeddings as text embeddings, and what are the potential implications of this design choice on the diffusion model's behavior?
   3. What would be the positional embedding for the patches when feeding into the text encoder? It's unclear if the positional information of the patches is preserved or how it's encoded when they are treated as text embeddings.
   4. In Sec 3.3 ("visual reacp density"), it would be better to illustrate the reason why the random selection schemas are different for different methods. The paper should provide a clear explanation for why different CLIP models require different sampling strategies for local patches, and how these strategies are determined.


- The paper lacks the details of the evaluation protocol. As the detailed inference method can largely affect the results, it's crucial to have a detailed description of how the method is evaluated on the MMVP dataset. 
   1. Given this, it would be hard to evaluate the validity of the ablation studies, which also affect the review of the paper. The paper needs to specify the exact procedure for evaluating the model on the MMVP dataset, including how the image-text matching is performed and how the accuracy is calculated. Without these details, the results are difficult to interpret and reproduce.

- The analysis needs to be improved in presentation:
   
   1. For some comparisons, the difference between baseline and proposed methods are close (e.g., 0.4 in absolute value). For these small differences, it's hard to understand its improvement. Some variance or significances analysis would be appreciated. Also, highlighting these numbers with gray colors would be helpful to readers. The paper should include statistical significance tests to validate the improvements, especially when the differences are small. Reporting variance or standard deviation would also help in understanding the robustness of the results. 
   2. In Table 3, some baseline and the proposed methods have the same score, but only the proposed methods are bold. It would be confusing to readers. The paper should ensure consistency in formatting and avoid highlighting results that are not statistically significant or better than the baseline.

### Questions
- The paper has highlighted that the CLIP is trained with limited length. Most diffusion models are also only trained with limited token lengths and have the same problem. Would it be possible that the golden fraction of local patch sampling rate (in Table 6) is just because of this?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
CLIP faces challenges related to fine-grained visual perception. To address this, the authors propose fine-tuning the CLIP image encoder by leveraging the spatial awareness of diffusion models. They use the visual tokens and the $[CLS]$ token from the CLIP image encoder as conditions for the diffusion models, backpropagating the gradients to update the CLIP encoder. The fine-tuned models are evaluated across several challenging benchmarks that require fine-grained visual perception, yielding promising results.

### Strengths
- Utilizing diffusion models to enhance CLIP's dense representation presents a novel perspective that will likely interest the community.

- The proposed method is intuitive and straightforward to implement, making it compatible with various existing vision-language models

- The experiments are comprehensive, demonstrating significant improvements across various benchmarks.

- The paper is well-written and easy to follow.

### Weaknesses
 - Given that no explicit alignment constraint between the image and text encoders is applied during the fine-tuning process and only the image encoder is updated, I am concerned about the potential for misalignment between the image and text encoders. 

- The visual recap operation varies across different models, potentially necessitating careful tuning of hyperparameters. Is there a general strategy applicable to all models, or must it be tailored to each specific model?

### Questions
- The proposed method significantly enhances the spatial awareness of CLIP. I wonder if this improvement extends to other multimodal tasks, such as open-vocabulary dense prediction tasks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces DIVA, a self-supervised framework designed to enhance CLIP's ability to perceive fine-grained visual details by leveraging generative feedback from text-to-image diffusion models. The framework incorporates a novel visual dense recap scheme, conditioning the diffusion models with CLIP's dense visual features and using image reconstruction loss for optimization. The results show that DIVA significantly improves CLIP's visual perception and its performance on multimodal and visual understanding tasks, as demonstrated on the MMVP-VLM benchmark. Additionally, DIVA maintains CLIP’s strong zero-shot capabilities across 29 image classification and retrieval benchmarks, proving its effectiveness in optimizing CLIP's discriminative representations.

### Strengths
--The paper presents an innovative approach by being the first to leverage generative feedback from text-to-image diffusion models to optimize the visual encoder of CLIP, aiming to addressing its limitation in fine-grained visual perception.

--The experiment part is extensive, validating their approach using the MMVP-VLM benchmark and demonstrating robust improvement. The integration with MLLM shows its impact, while experiments across 29 image classification and retrieval benchmarks confirm that the original capabilities of CLIP are preserved.

--The paper is clearly written, with well-explained methods and detailed descriptions of the proposed framework and experimental results.

### Weaknesses
--Disruption of Visual-Language Alignment: Optimizing CLIP’s visual encoder may disrupt the inherent visual-language alignment of CLIP. Although the authors validate that CLIP’s original capabilities are retained through experiments on 29 datasets, these tests are somewhat limited, as they only cover image classification and unimodal retrieval (text or image retrieval). Because the text encoder is not fine-tuned, the retrieval results for text remain unchanged, making text-retrieval experiments redundant to some degree. Moreover, the paper lacks experiments on tasks that rely heavily on cross-modal alignment, an area where CLIP excels, such as cross-modal retrieval. If such disruption occurs, it would be valuable to explore methods for preserving cross-modal alignment, such as applying a reconstruction loss to the visual class token to maintain the original feature.

--Part Token Selection Strategy: The method involves inputting tokens from CLIP’s visual encoder, including the global (class) token and a subset of local tokens, as conditions for the diffusion model generation. Although the authors state that using only the global token or a combination of the global token with all local tokens yields suboptimal results than global + part local tokens, they do not clarify how the proportion of local tokens is determined. Additionally, this proportion appears to vary across different datasets and between training and inference, raising concerns about the method’s generalizability. Furthermore, the strategy for selecting part tokens could impact the results, and using a simple random selection might not be optimal.

--Empty Text Conditions: In Table 6, the conditions for the diffusion model include an empty text condition. It would be interesting to explore whether incorporating text descriptions corresponding to the images could further enhance the results.

--Minor typo: There is an extra word "for" at line 350.

### Questions
1. It is crucial to also verify that the original cross-modal alignment capability of CLIP can also be preserved.

2. What criteria were used to decide the proportion of local tokens? Could you provide an analysis or ablation study to support this choice?

3. How does the varying proportion of local tokens across different datasets and between training and inference affect the method's generalizability?

4. Is there any other local token selection strategy that might yield better results?

5. Would incorporating image-associated text in the diffusion model conditions improve the performance observed in Table 6?

### Soundness
3

### Presentation
4

### Contribution
3
