# MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
We present \textbf{\mmprons}, a new family of multimodal large language models (MLLMs) designed to enhance capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. Building upon the MM1 architecture, \mmpro adopts a data-centric approach to model training, systematically exploring the impact of diverse data mixtures across the entire model training lifecycle. This includes high-quality OCR data and synthetic captions for continual pre-training, as well as an optimized visual instruction-tuning data mixture for supervised fine-tuning. Our models range from 1B to 30B parameters, encompassing both dense and mixture-of-experts (MoE) variants, and demonstrate that careful data curation and training strategies can yield strong performance even at small scales (1B and 3B). Additionally, we introduce two specialized variants: \mmprons-Video, designed for video understanding, and \mmprons-UI, tailored for mobile UI understanding. Through extensive empirical studies and ablations, we provide detailed insights into the training processes and decisions that inform our final designs, offering valuable guidance for future research in MLLM development.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new set of multimodal LLM, MM1.5 as a result of a detailed data-centric pretraining experimentation. The experimented pretraining scheme includes 3 stages: (i) large-scale pretraining with text-only and image-text data, (ii) high-resolution continuation with OCR data and synthethic captions, (iii) supervised finetuning (instruction tuning). This work performs both model-centric and data-centric ablation analysis on the first two pretraining stages.

### Strengths
Clarity: The paper is well written and easy to follow.
Significance: Multimodal model development is currently a trending topic, and this work employs a data-centric analysis that offers valuable insights for future researchers. Apart from the most commonly-used models, the examined model is able to comprehend about the referred objects and process multiple images.

### Weaknesses
A drawback of this study is that it serves as a comprehensive ablation analysis without offering any novel methodologies or tasks/benchmarks. I don't have any suggestion to improve this aspect at this point, but it should not be any problem.

### Questions
- Have you performed ablation studies on skipping the second stage completely?
- As far I have seen, Refer&Ground data requires 2x general purpose data. How could one make this more data-efficient?
- I am having trouble to interpret Table 1. So, as long as a person trains their model using multiple images, they could achieve significant performance gain on text-rich and refer&ground tasks. The dynamic image splitting makes less difference according to this table.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the MM1.5 model family and provides a comprehensive recipe for training multimodal large language models. It systematically explores the impact of data mixture ratio, training strategy, and model architecture, offering valuable findings for future research in multimodal large language models.

### Strengths
1. This paper conducts thorough experiments to explore the design of data, training, and architecture.
2. This paper provides several empirical guidance for training MLLMs. The data mixture ratio during the pre-training stage (50:10:40 for image-text, interleaved image-text, and text-only data) could be particularly important, as it highlights the significance of text understanding in complex multimodal scenarios.
3. This paper is clearly and concisely written, making each concept easy to understand.

### Weaknesses
This paper currently resembles a technical report more than academic research. It employs several well-known techniques (e.g. MoE, Dynamic Res) and mainly investigates the data mixture ratio at each training stage. While the empirical findings are valuable, additional theoretical insights would be beneficial. I have two concerns below: 
-  Why does the optimal ratio of text-only data change between the pre-training and SFT stages? Does the role of text-only data differ across these stages?
- Given a collection of multimodal data, is there a theoretical guideline for determining the optimal mixture ratio between multimodal and text-only data?

### Questions
My questions are listed in weaknesses and I look forward to the authors addressing these issues.

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
5

### Summary
This paper presents a set of MLLMs, MM1.5, scaling from 1B to 30B and also explore MoE variants (1B and 3B).
MM1.5 is built upon MM1, upgraded with stronger capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning, through extensive empirical studies and ablations on data mixture in three stages of training and high-resolution image processing.
MM1.5 shows strong performance and significant improvements over MM1 on various benchmarks.
MM1.5 provides detailed insights into data mixture and other engineering choices in training a large-scale MLLM capable of general understanding, text-rich image understanding, visual reffering and grounding, and multi-image reasoning.

### Strengths
1. This paper conducts extensive empirical studies and ablations on continual pre-training, dynamic high-resolution image processing, and curation of our supervised fine-tuning datasets, which can provide insights and experience for future research on large-scale MLLMs.
2. This paper presents a set of MLLMs, not only scaling from 1B to 30B but also exploring MoE variants (1B and 3B), which can provide important scaling insights for future research on large-scale MLLMs.
3. This paper shows strong performance and significant improvements over MM1 on various benchmarks.
4. This paper also explores two SFT variants of MM1.5, i.e., MM1.5-Video and MM1.5-UI, which shows strong performance on video and UI benchmarks.

### Weaknesses
1. Although this paper presents detailed empirical ablations on several important engineering decisions in data mixture and high-resolution image processing, it does not provide strong new insights or findings compared to previous works. The ablations on SFT data mixture, continual pre-training, and dynamic high-resolution image processing are not novel and have been explored in previous works.
2. Specifically, data-specific hyperparameters from detailed ablations for data mixture (pre-training, continual pre-training or SFT) may not be quite practical for other researchers to follow, as they are highly dependent on the specific dataset, model size, model architecture, and training setup.
3. Lack of in-depth analysis on the underlying reasons for the phenomenon observed in the extensive ablations. Simple assumptions or hypotheses about ablation results are not sufficient. The ablation decisions are pushed by empirical results step by step, but the underlying reasons for the phenomenon observed in the ablations are not well analyzed.
4. This paper does not claim any form of open-sourcing, no matter model weights, code or data, which may limit the reproducibility and practicality of this paper, especially considering the first two weaknesses mentioned above.

### Questions
1. In Figure 2, it seems that Refer&Ground data will downgrade the performance of all other categories. Although it will greatly improve the performance of Refer&Ground and Figure 3 shows that MMBase score will only slightly decrease, the other categories of MMBase score will decrease in fact. What is the reason for this phenomenon? Is it fair to use such an average score, MMBase, between different categories to evaluate the model's performance? Similar questions can be raised for Figure 5.
2. With full respect this paper for its exploration and contribution to engineering decisions (very important for MLLM), but in the table of experimental results (Tables 4, 7-11), the authors seem to be selectively presenting some models that are weaker than their own. Take Table 7 as an example, authors selectively show the results of LLaVAOneVision-0.5B, InternVL2-2B and Cambrian-34B. But the selected three models have their corresponding model family, which can provide a more comprehensive comparison in different model scales. In addition, authors quote Qwen2-VL, but do not compare with it in these tables. The reviewer fully understands that most of the powerful models from the MLLM era are not comparable (training data, training details, evaluation details, etc.), but don't support such selective comparisons, which are not conducive to the reader's understanding of how the field is progressing and comparing.

### Soundness
3

### Presentation
3

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
The paper introduces a new family of multimodal large language models (MLLMs), ranging from 1 to 30B parameters, including MoE models. They build on top of MM1 and focus on data curation for **continual pretraining** and **supervised fine-tuning** (SFT), providing several ablations for the choice of data mixture(s) and summarize their findings in a recipe.

To run their ablations, they use the following setup:

- Static image splitting, splitting large images into four sub-images, plus an overview image, for both SFT and continual pretraining.
- They use either single image or multi image data, and enable splitting only when processing less than three images for a single sample.
- They use a custom (non-disclosed) CLIP text encoder and LLM as their backbones.

For evaluation, they consider general, text-rich, refer & ground, knowledge, and multi-image tasks and report two metrics:

- Category average score: average score for all benchmarks in a given category.
- MMBase score: average score on general, text-rich, and knowledge categories.

## Supervised fine-tuning

SFT is conducted using a large amount of datasets, categorized as follows:

- Single image
	- General
	- Text rich
	- Refer & Ground
	- Science
	- Math
	- Code
- Multi-image
- Text only

They first focus on the impact of single data categories, finding that text-rich data is crucial for text-rich tasks and that good refer & ground capabilities only emerge if the model is trained on appropriate data.

They then focus on optimising for the sampling ratio between the general category and other categories (for single image data), and find that the right mixture of science and math data can significantly improve performance. They also find that doubling the sampling probability of refer & ground data provides a good tradeoff between general performance and refer & ground performance.

Once the single-image data ratios are fixed, they integrate text-only and multi-image data. They find that text-only data has a minor impact and fix its ratio to 0.1. They pick a similar ratio for multi-image data, as it improves the multi-image score significantly while also slightly improving the MMBase score. A larger quantity of multi-image samples decreases the MMBase score. Finally, they fix the single-image ratio to 0.8.

They combine these results to produce three data mixtures:

- Base: general, text-rich, science, math, code.
- Single image: base + refer & ground.
- All: single image + multi-image and text only.

As expected from the previous findings, the single-image mixture unlocks the refer & ground capabilities, while the multi-image one largely improves the multi-image capabilities. The **all** mixture is the best on average (although the base mixture performs best on tasks that are not refer & ground and multi-image).

## Continual pretraining

The paper explores continual pretraining using ~50M OCR high-resolution (1344 x 1344) sampled across four datasets. Once continual pretraining is complete, they perform SFT using the Base mixture. Their findings are:

OCR data must be high-res. Downsampling images to the encoder input dimension (378 x 378) can cause the model to lose up to 2% in average score and even perform worse than when no continual pretraining is performed! OCR data improves performance, but only if it has a high enough resolution.

- They also experiment with data with synthetic captions and find that they improve performance compared to a baseline without continual pretraining. Still, they perform worse than only using OCR data, even when combined.
- In the appendix, they show that self-training with synthetic captions can improve performance compared to an OCR-only baseline.

## Dynamic Image Splitting

These experiments use the single image mixture and start from an MM1 checkpoint without continual pretraining.

The authors claim that static image splitting has inherent issues, as low-res images are also split, and splitting non-square images can result in sub-images that consist only of padding. Thus, they experiment with dynamic image splitting, picking a grid that minimizes the amount of padding. In addition to the sub-images, they include the resized original image for additional context and optionally positional indicators for sub-images.

Based on their results, they claim that:

Dynamic image splitting outperforms static splitting for text-rich tasks. Image resolution, the number of sub-images, and the number of image tokens are important. Moreover, it greatly improves performance on tasks whose images have unusual aspect ratios.

- These benefits come at a relatively small cost (< +10%) in terms of encoded images
- Positional indicators are useful for specific tasks but not necessary in general
- Placing the overview image after the sub-images improves performance

## Final Results

Given the findings illustrated in previous sections, the authors propose a three-step recipe (MM1 pretraining, continual pretraining, and SFT) to train 1, 3, 7, and 30B models, plus 1 and 3B MoE models.

Their models improve over similarly-sized models, sometimes by large margins, and the performance scales well as models grow in parameters. MoE models often outperform their dense counterparts. This is particularly evident for 1B models, where the MoE variant often improves by over 5% compared to its dense counterpart. Their models also provide significant improvements in refer & ground and in-context learning tasks.

### Strengths
The paper is well-written and provides novel, valuable, and actionable findings for the MLLM community. While the backbones to replicate the experiments are not publicly available, the authors release as many details as possible regarding their datasets, data mixtures, hyper-parameters, and data processing strategies (e.g., dynamic image splitting, positional indicators, and overview image position).

Moreover, the models trained using the data curation strategies illustrated in the paper significantly outperform a model with the same architecture but a simpler data curation method (MM1) and several current state of the art models, especially in refer & ground, multi image and in-context learning tasks, across various sizes.

### Weaknesses
While there are clear benefits in using dynamic image splitting for processing input images, I am not fully convinced it leads to better performance overall, as when comparing similar setups in terms of images and tokens in Table 1 static image splitting works best. I am wondering if it would outperform dynamic image splitting when $n = 10$ and 1440 total tokens are processed.

I am also unsure why the final recipe used indices to indicate the positions for sub-images, even though Table 3 shows that separators work better overall. Could you please clarify this choice?

Presentation-wise, I only have a couple of minor remarks:

1. In section 2.2.1 (in the second paragraph), the authors claim that "adding the code category results in a slight increase in the text-rich score" (i.e., ~1.54%), and that "adding text-rich data can significantly improve the performance on [...] and knowledge benchmarks" (i.e., ~1.78%). I would maybe slightly rephrase either of those sentences.
2. Bolding the best results in tables would make it easier to identify the best configuration(s).
3. Maybe introducing the continual pretraining ablations first and following up with supervised fine-tuning would improve readability. The paper would then follow the recipe logically.

### Questions
- If I understand correctly, in section 2.2.2, using a data ratio of 1:2, e.g., for general and science categories results in a sample from the general category (68x the size of science) being 34x more likely to be picked compared to a science sample when building a batch, correct?
- Is dynamic image splitting used in both continual pretraining and supervised fine-tuning?
- Why were the 7B models not compared with similarly sized open-source models such as LLava 1.5 7B?

### Soundness
4

### Presentation
3

### Contribution
3
