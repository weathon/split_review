# Dual Caption Preference Optimization for Diffusion Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
Recent advancements in human preference optimization, originally developed for Large Language Models (LLMs), have shown significant potential in improving text-to-image diffusion models. These methods aim to learn the distribution of preferred samples while distinguishing them from less preferred ones. However, existing preference datasets often exhibit overlap between these distributions, leading to a conflict distribution. Additionally, we identified a performance issue in previous optimization methods, where using the same prompt for preferred and less preferred images, known as the irrelevant prompt issue, restricts model performance. To address these challenges, we propose Dual Caption Preference Optimization (DCPO), a novel approach that utilizes two distinct captions to mitigate irrelevant prompts. To tackle conflict distribution, we introduce the Pick-Double Caption dataset, a modified version of Pick-a-Pic v2 with separate captions for preferred and less preferred images. We further propose three different strategies for generating distinct captions: captioning, perturbation, and hybrid methods. Our experiments show that DCPO significantly improves image quality and relevance to prompts, outperforming Stable Diffusion (SD) 2.1, SFT-Chosen, Diffusion-DPO and MaPO across multiple metrics, including Pickscore, HPSv2.1, GenEval, CLIPscore, and ImageReward, fine-tuned on SD 2.1 as the backbone.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work first presents the conflict distribution issue in preference datasets, where preferred and less-preferred images generated from the same project exhibit significant overlap. For this issue, they introduce the Captioning and Perturbation methods: generate a caption based on the image and the prompt, create three levels of perturbation from the prompt. They also explore the irrelevant prompt issue in previous DPO methods and propose Dual Caption Preference Optimization (DCPO) to improve diffusion model alignment. Lastly, they show promising results compared to the existing methods.

### Strengths
1. The paper is well-organized and easy to follow. Figures are clear to read, such as Figure 2. 
2. The story is complete: they propose hypothesis and then use experimental results to verify them in Sec 3.3 with clear ablation studies. 
3. The problem setup is clear. They also provide enough details to reproduce the work.

### Weaknesses
1. My biggest concern is about the generalization of the approach method in the development of diffusion models. For example, in Figure 2, it is easy to distinguish the preferred and less-preferred image as the latter one even does not align with the original prompt. What if the model's development is already beyond the alignment stage? The current positive/negative samples are only about alignment, what about more advanced difference if both have enough alignment?

2. Line 188-189, could you explain more details on how to get the preferred and less-preferred images? Human annotation?

3. It would be beneficial to highlight the difference between medium and strong permutation. Do we have a way to quantify the difference between them? Are they controllable generated? Why do we need medium permutations? Would weak/strong be enough?

4. In terms of GPT-4o evaluation, does it matter for showing the images together or showing them separately? And how about the order of showing them to GOT-4o if showing separately?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper propose an improved method for aligning text to image diffusion models using human labeled preference datasets. Instead of using the original caption that is used to generate the preferred and less preferred image pair, the method propose to generate new captions from the generated images or original captions so as to increase/decrease the text image alignment for the generated images, which make the the distribution difference between preferred and less preferred data larger than using original captions.

Experiments using diffusion DPO method are conducted in various versions of caption image combinations, which show adding perturbed captions for less preferred image helps finetuned model get better performance on automatic metrics, including itemized metrics such as HPSv2, as well as side by side metrics using GPT-4o as judge.

### Strengths
The paper is well written with right amount of details in both main text and appendix. The proposed method is clear, and relativly straightforward to implement. 

On a popular open source diffusion model ( SD 2.1), several experiments are done to ablate the design details of the proposed approach. The used set of metrics are comprehensive, including both single side evaluation such as HPSv2, as well as side by side evaluation such as the one using GPT4-o as judge.

### Weaknesses
The motivation behind the proposed approach is not clear to me.
For the conflict distribution challenge, when the distribution overlap becomes larger, the dataset is proposing a harder problem for the model to optimize, but it isn't necessary an issue as long as the two distributions are not identical. When the diffusion models's quality gets better, the two distribution will inevitably become more and more similar,  as both preferred and less preferred images from an optimized model will be closer to real human preference.  So it's more of the nature of the task itself, unless the task is defined differently.

From the description of L175-L180, the irrelevant problem is hardly a problem either. It is an inherently part of the objective in Eqn (1), where one way of minimizing Eqn(1) is to decrease $\log(p_{\theta}(x_{0:T}^l|z^l)$, which makes the model less likely to generate the less preferred image. So to me this is a desired behavior instead of a problem. 

By changing the captions, authors changed a prefer/less prefer pair into two separate samples. In this sense it is no longer the original DPO problem, yet there is no clear connection between the original DPO formulation and the new problem e.g. is the new one an upper-bound of the original so minimizing the new problem potentially minimize the original one? or why solving the new problem will necessarily give better results than original DPO?

The change of captions made the problem closer to the KTO problem referenced in the paper, where text-image data are labeled by like and dislike binary labels. Please describe the connection and difference between the modified problem represented by the new data and the KTO problem formulation above.

It is great to conduct extensive experiments on SD 2.1, but the paper will be stronger if there are experiment results on other diffusion models, even if the experiments are not as complete as on SD 2.1.

### Questions
Despite the experiments suggests the proposed approach is better, it is unclear to me why this would be the case, any proofs or intuitions will help reader better understand it.

Several papers appear multiple times in the References section, please dedupe.

### Soundness
2

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
The paper presents a preference optimization technique called Dual Caption Preference Optimization (DCPO). This method aims at improving text-to-image diffusion models. DCPO tackles issues inherent in current preference datasets, namely conflict distribution and irrelevant prompts, by introducing separate captions for preferred and less preferred images. This dual-caption approach is implemented through three methods: captioning, perturbation, and a hybrid method, all aimed at enhancing the clarity of distinctions between preferred and non-preferred images. Experimental results demonstrate that DCPO outperforms existing models across several benchmarks and metrics, including Stable Diffusion 2.1 and Diffusion-DPO.

### Strengths
1. The dual caption framework is reasonable. DCPO introduces a dual-caption system that effectively addresses the problem of overlapping distributions in existing datasets.
2. This paper achieves better performance. Demonstrated improvements across multiple metrics (e.g., Pickscore, CLIPscore) and benchmarks (e.g., GenEval) show that DCPO enhances image quality and relevance significantly.
3. The experimental results are analyzed in detail. The paper includes extensive quantitative and qualitative analysis, supporting the effectiveness of DCPO with various baselines and ablation studies.

### Weaknesses
1. The proposed method depends on the caption quality. The quality of generated captions significantly affects performance, and challenges remain in creating effective captions for less preferred images without straying out-of-distribution.
2. While DCPO demonstrates quantitative improvements across several metrics, the qualitative results (e.g., Figure 1) indicate that the visual distinctions between images generated by DCPO and baseline methods are not significant. This subtle difference may limit the perceived impact of DCPO in practical applications.
3. The DCPO has limited generalizability compared to real-world large-scale datasets. Although leveraging preferred and non-preferred images is a novel approach for enhancing diffusion models, high-quality, large-scale datasets from real-world settings often provide stronger improvements in model performance. This reliance on real-world data diminishes the relative advantage of DCPO, potentially limiting the distinctiveness of its contributions in scenarios where comprehensive datasets are available.
4. The LAION-2B and MSCOCO datasets are widely regarded benchmarks for image generation tasks, yet they are not discussed or evaluated within this study. The absence of experiments or comparisons involving LAION-2B raises questions about DCPO’s general applicability.

### Questions
Please address my concerns above.

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
2

### Summary
This paper introduces Dual Caption Preference Optimization (DCPO) to enhance text-to-image diffusion models by aligning them with human preferences. Traditional methods face issues like overlapping distributions and irrelevant prompts. DCPO addresses these using two distinct captions for each image, mitigating conflicts in preference data. The authors introduce the Pick-Double Caption dataset to support this approach. They apply three strategies—captioning, perturbation, and hybrid methods—to generate unique captions. Experiments show DCPO improves image quality and prompt relevance. DCPO outperforms prior models on multiple metrics, validating its effectiveness.

### Strengths
As a reviewer from a broader field, I am not very familiar with the specific domain of this paper. Therefore, I am reviewing this paper from a generalist’s perspective. The strengths of this paper are:

1. It provides sufficient theoretical support for the motivation, which aligns well with the characteristics of ICLR papers.
2. The issues raised seem quite reasonable.
3. Extensive quantitative and qualitative experiments support the arguments presented.

### Weaknesses
However, I still have a few concerns:

1.  The issues of conflict distribution and irrelevant prompts seem like two aspects of the same problem—both involve a single prompt (C) corresponding to two different images, which can lead to unstable optimization. Therefore, I think they could be consolidated into a single issue. The core problem seems to stem from the ambiguity introduced when a single prompt is used to guide the generation of two distinct images, potentially leading to conflicting gradient updates during training. This is further exacerbated when the two images are visually similar, making it difficult for the model to discern the subtle differences that the preference signal is trying to capture.
2.  When comparing generated images, the improvements achieved by the proposed method could be highlighted more clearly; otherwise, it’s often not immediately obvious, as in Figure 1. The visual differences between the images generated by the baseline and the proposed method are often subtle, making it difficult to assess the effectiveness of the approach. This lack of clear visual distinction makes it challenging to appreciate the practical impact of the proposed method.
3.  In fact, the explanations of conflict distribution and irrelevant prompts in the abstract and introduction are quite obscure and difficult to understand. I had to reread these sections several times, only gaining clarity after reading the methods section. This part may need reorganization. The initial explanations of these issues lack clarity and concrete examples, making it hard to grasp the core challenges that the paper aims to address. The abstract and introduction should provide a more intuitive and accessible explanation of these problems to better engage the reader.

### Questions
The issues of conflict distribution and irrelevant prompts seem like two aspects of the same problem—both involve a single prompt (C) corresponding to two different images, which can lead to unstable optimization. Therefore, I think they could be consolidated into a single issue.

### Soundness
3

### Presentation
3

### Contribution
2
