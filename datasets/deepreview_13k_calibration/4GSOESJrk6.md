# DreamBench++: A Human-Aligned Benchmark for Personalized Image Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Personalized image generation holds great promise in assisting humans in everyday work and life due to its impressive function in creatively generating personalized content.
However, current evaluations either are automated but misalign with humans or require human evaluations that are time-consuming and expensive.
In this work, we present \dreambench, a human-aligned benchmark automated by advanced multimodal GPT models.
Specifically, we systematically design the prompts to let GPT be both human-aligned and self-aligned, empowered with task reinforcement.
Further, we construct a comprehensive dataset comprising diverse images and prompts.
By benchmarking 7 modern generative models, we demonstrate that \dreambench results in significantly more human-aligned evaluation, helping boost the community with innovative findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a new T2I evaluation benchmark, DREAMBENCH++, which is introduced as a human-aligned benchmark for personalized image generation, addressing the limitations of current evaluations that are either misaligned with human judgment or time-consuming and expensive. The researchers systematically design prompts to make GPT models both human-aligned and self-aligned, enhanced with task reinforcement, and construct a comprehensive dataset of diverse images and prompts. By benchmarking 7 modern generative models, this paper demonstrates that DREAMBENCH++ achieves significantly more human-aligned evaluation, contributing to innovative findings in the field.

### Strengths
I appreciate that the authors engage a lot of effort to build a new benchmark, including design prompt, collecting images, and conducting experiments among several existing T2I models. The paper is written well and clear, the figure is informative, which is good.

### Weaknesses
1. I am confused about the motivation of building this new benchmark actually. As stated on line 084-085, "can we comprehensively evaluate these models to figure out which technical route is superior and where to head?", it's hard for reviewers to understand what distinguishes your benchmark compared with other existing benchmarks. Does DREAMBENCH++ assess more skills than existing T2I benchmarks? Does DREAMBENCH++ include more samples or higher quality images? A comparison table (DREAMBENCH++ v.s. existing benchmarks) is necessary to convince reviewers how the new benchmark can benefit T2I community.

2. Nowadays, there are several existing T2I benchmarks, for example, DALL-EVAL [1] and HRS-Bench [2]. So a new benchmark alone may not contribute enough in this field. It would be good to contribute one technical contribution to somehow address the challenge which is emphasized in the newly built benchmark.

### Questions
1. Can you do specific comparisons between DREAMBENCH++ and existing benchmarks like DALL-EVAL and HRS-Bench. For example, a comparison table showing the number of samples, types of skills assessed, and evaluation metrics used in each benchmark is necessary. This would help clarify the unique contributions of DREAMBENCH++.

2. May I ask if the authors have considered developing new evaluation metrics, proposing improvements to existing personalized T2I models based on benchmark insights?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a new benchmark for personalized text-to-image generation, including a dataset with a greater number of images and prompts compared to DreamBench, and an automatic evaluation method that assesses two key aspects of the task: (i) concept preservation and (ii) prompt following, using multimodal large language models like GPT. This new evaluation method addresses the limitations of previous DINO and CLIP and achieves higher human alignment.

### Strengths
It fills a gap in human-aligned and automated evaluation of the personalized text-to-image generation task by introducing LLMs. The dataset and evaluation metric is clearly described in detail.

### Weaknesses
1. The new dataset aims to include a larger variety of images but the source of these images is still relatively narrow (only 3 websites). The new dataset can still be biased due to the preference of these websites, and there is no sufficient evidence to show its diversity (only the visualization of t-SNE). It is unclear if the t-SNE visualization adequately captures the semantic diversity of the dataset, as t-SNE is primarily a dimensionality reduction technique for visualization and may not preserve all relevant semantic relationships. A more rigorous analysis, such as calculating the average distance between images from different categories in a high-dimensional feature space, would be more convincing.
2. It is claimed that the method is transferable to other foundation models. It is not straightforward because the method is specifically designed for GPT4 and no experiment showed its transferability. The evaluation method relies heavily on the specific capabilities of GPT-4, such as its ability to understand complex prompts and assess image quality. Without empirical evidence demonstrating that other models can achieve similar performance, the claim of transferability remains unsubstantiated. The prompt engineering for GPT-4 might not directly translate to other models, potentially requiring significant modifications and re-tuning.
3. The dataset only contains 1 image for every instance. Although multiple images are claimed to be unnecessary, the results in Fig. 9 show serious overfitting when using only 1 reference image. The use of a single reference image per instance raises concerns about the robustness of the evaluation. The observed overfitting in Fig. 9 suggests that the models are memorizing the reference image rather than learning generalizable concepts. This limitation makes it difficult to assess the true personalization capabilities of the models.
4. There are other key aspects that need evaluation. For example, a common problem of fine-tuning-based methods is overfitting. We generally don't want the generated images to be too similar to the reference image except for the identity of the object. It is worth trying to evaluate the overfitting problem using GPT. The evaluation framework should explicitly address the trade-off between concept preservation and generalization. Overfitting is a critical issue in personalized generation, and the current evaluation method does not adequately capture this aspect. A metric that quantifies the degree of similarity between the generated image and the reference image, while also assessing the diversity of the generated content, would be beneficial.

### Questions
How are the numbers calculated? Can you specify how you used Krippendorff’s alpha value? And where does the number of 54.1% and 50.7% come from? I noticed that the CLIP and DINO scores fairly correlate with human scores.

### Soundness
2

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
The paper presents DREAMBENCH++, a human-aligned benchmark for evaluating personalized image generation models using advanced multimodal models like GPT-4o for automated, human-like assessments. It addresses the misalignment and cost issues of traditional evaluation methods by focusing on prompt following and concept preservation with a diverse dataset. DREAMBENCH++ demonstrates superior alignment with human evaluations, offering a comprehensive and unbiased framework to advance personalized image generation research.

### Strengths
This paper proposes a metric that closely aligns with human preferences for evaluating personalized generated images and introduces a suitable benchmark. Compared to existing benchmarks, it constructs a much more diverse and extensive dataset and demonstrates evaluation results that are better aligned with humans than CLIP and DINO.

### Weaknesses
- For text-to-image generation models, there are many metrics, including TIFA[1], that improve upon CLIP. It is necessary to demonstrate alignment with humans not only compared to CLIP and DINO but also in comparison with these existing studies.

[1] Hu, Yushi, et al. "Tifa: Accurate and interpretable text-to-image faithfulness evaluation with question answering." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

- The prompts used for GPT-4o are abstract. Studies that evaluate generated images using VQA typically ask absolute questions, such as the presence, location, or number of objects, to fully leverage GPT-4o’s performance. However, the prompting approach in this paper treats GPT-4o like a human, and the justification relies only on citations from other studies. In practice, some degree of hallucination occurs when GPT-4o evaluates images, which the paper overlooks, making this a significant drawback. The lack of specific, quantifiable prompts for GPT-4o introduces variability in its evaluations, making it difficult to ascertain the consistency and reliability of the automated scoring process. This is particularly problematic when assessing nuanced aspects of personalized image generation, where subjective interpretations can significantly influence the outcome.

-The scoring system from 0 to 4 is ambiguous. Some images may have around 10 objects, with 1 or 2 that do not match, while others may have all objects correct but differ in style. What are their scores? While GPT-4o might provide consistent evaluations, humans are less likely to be consistent. To address this, a larger user study should have been conducted, but only seven people participated, with each instance evaluated by at least two annotators. This means some images were reviewed by just two people, making the number of annotators insufficient.



### Questions
Please see the weakness part. In addition,

- Why is the comparison scheme considered unsuitable in lines 198-199 if the scoring results are sensitive? Was "comparing" mistakenly written as "scoring"?

- Stable Diffusion often generates noisy backgrounds effectively and frequently. Why did the authors judge it as unsuitable for personalized generation and remove it?

- Are the example prompts shown in Figure 4 intended for personalized editing with those specific prompts?

- In Table 1, the highest-scoring model is consistent across Human, GPT, DINO-I, CLIP-I, and CLIP-T. Can DREAMBENCH++ really be said to be more aligned with humans than DINO or CLIP?

- Contrary to the authors' claim, Figure 6 does not clearly show that DINO or CLIP prefer shape and overall styles. Also, do the authors believe that favoring shape and overall styles is not aligned with human preference?

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
This paper contributed a benchmark and a dataset for evaluating personalized image generation task, also an automated evaluating metric using GPT to address the issues of cost inefficient human evaluation, and also the lack of diversity in previous dataset/benchmark works. It included 7 models ( 3 more than prior works), and developed an semi-automated dataset creation pipeline. It also expanded dataset to 5x of images and 54x of prompts, and proposed the use of automated evaluating metric (GPT), with different settings studied (e.g. COT and ICL). The main goal of this work is to comprehensively evaluate these models to figure out which technical route is superior and where to head.

### Strengths
S1) Fruitful discussion in diversity study, showcasing that models are good at certain types of generation. (e.g. all models generally perform better in Animal and Style due to sensitivity to facial details and diverse object categories). This aligns with the goal to figure out which model is superior in certain types of generation.

S2) Well-organized study in showcasing the impact of prompt design including COT, ICL, Internal thinking etc.. when comes to automated evaluation with GPT.

### Weaknesses
W1) In Section 3.2 the authors claimed that "Table 1 results show that DreamBench++ aligns better with humans than DINO or CLIP models...", which is not very convincing. While it makes sense to show that the ranking order from GPT is more correlated to Human compared to DINO-I and CLIP-I, It is expected to show the correlation (Spearman / Pearson). I would suggest the authors to add a table regarding correlation between Human and GPT, and between Human and DINO/CLIP, supporting the claim. Also It seems a bit odd to use Krippendorff's Alpha to compare human ratings are other rating (GPT/DINO/CLIP) in Table 4. The two scales are inherently different and the meaning of ratings are different. Spearman / Pearson correlation would be a better metric for cross-scale reliability. Krippendorff's Alpha would be suitable for H-H as showing the inter-rater reliability.

W2) The paper would have been much stronger if the authors included a section to discuss which model performs the best in certain types of generation and how is it associated with certain technical route. This will be more aligned to the purposed goal "figure out which technical route is superior and where to head."

W3) Minor confusion when reading the table 1 and 3 directly. For example, Table 3 does not mention what exactly are the score values are. Please extend table captions to explain what are the values in the revised version.

W4) Please highlight the best model in each categories from Table 2 in the revised version. Maybe a leaderboard showcasing the best models in each category.

### Questions
Q1) Any design rationale on the score scale? Why not use a score in scale from 0 to 1? This would be more aligned with the range of traditional metrics (e.g. CLIPScore, LPIPS, DINO etc.)?

Q2) How do the authors verify that the automated evaluation with GPT results are making sense (such that the reasoning fully reflects the score)?

Q3) Please share the analysis of the costs and time needed for the human annotation, and how many data instance were annotated in total. Will the human annotated data be released?  

Q4) Authors might want to consider adding more models for comparison, including DisenBooth(ICLR 2024), EZIGEN (ArXiv 2024), 

---
I believe this study will interest a broad audience. However, the contribution feels somewhat limited, and the discussion does not fully align with the claimed goal in the introduction. If W1 and W2 can be addressed, I would likely consider raising my score.

### Soundness
3

### Presentation
3

### Contribution
2
