# MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
The rapid development of Multimodal Large Language Models (MLLMs) is making AI-driven scientific assistants increasingly feasible, with interpreting scientific figures being a crucial task. However, existing datasets and benchmarks focus mainly on basic charts and limited science subjects, lacking comprehensive evaluations. To address this, we curated a multimodal, multidisciplinary dataset from peer-reviewed, open-access Nature Communications articles, spanning 72 scientific disciplines. This dataset includes figures such as schematic diagrams, simulated images, macroscopic/microscopic photos, and experimental visualizations (e.g., western blots), which often require graduate-level, discipline-specific expertise to interpret.
We developed benchmarks for scientific figure captioning and multiple-choice questions, evaluating six proprietary and over ten open-source models across varied settings. The results highlight the high difficulty of these tasks and the significant performance gap among models. While many open-source models performed at chance level on the multiple-choice task, some matched the performance of proprietary models. However, the gap was more pronounced in the captioning task. Our dataset also provide valuable resource for training. Fine-tuning the Qwen2-VL-2B model with our task-specific multimodal training data improved its multiple-choice accuracy to a level comparable to GPT-4o, though captioning remains challenging. Continuous pre-training of MLLMs using our interleaved article and figure data enhanced their material generation capabilities, demonstrating potential for integrating scientific knowledge. The dataset and benchmarks will be released to support further research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MMSci, a multimodal, multidisciplinary dataset collected from open-access scientific articles published in Nature Communications. Spanning 72 scientific disciplines, the dataset of 131K articles includes high-quality, peer-reviewed articles and figures, primarily within the natural sciences. The authors create challenging benchmarks with 1K tasks and settings to evaluate Large Multimodal Models (LMMs) in understanding advanced scientific figures and content. The dataset supports both text and images, offering a mix of multiple-choice and open-ended questions with sub-figures distinction focus. Their evaluation reveals significant challenges for current LLMs, including open-weights models and even closed-source models. The model finetuned on the training part yield high quality results.

### Strengths
* Comprehensive and Quality: The dataset is large-scale and diverse, covering 72 disciplines. It features high-quality source material, which enhances its utility and applicability.
* Challenging Benchmarks: The benchmarks are thoughtfully designed to assess models’ abilities in understanding complex scientific figures and content, revealing limitations in current models.
* Demonstrated Improvement: The fine-tuning of the LLaVA model using their dataset shows tangible improvements, achieving performance comparable to high-level models.

### Weaknesses
 * Dataset Curation Details: The paper should provide more detailed information about the data annotation process to enhance transparency and reproducibility. Specifically, information about quality control stages would be valuable. The current description lacks specifics on how the regex extraction was validated to ensure all figures and structures were captured correctly, and what measures were taken to handle edge cases or errors in the extraction process. 
* Model Size Comparison: The paper compares large closed-source models (GPT-4V, Gemini-Pro, etc.) with relatively small open-weight models limited to 8B parameters. A broader analysis including larger models (e.g., Qwen2-VL-72B) would be beneficial, especially given the near-random performance of some smaller models. The lack of comparison with similarly sized or larger open-source models makes it difficult to assess the true potential of the proposed dataset and benchmarks.
* LLM Evaluation Sample Size: The LLM-based evaluation reports final scores using only 100 randomly selected samples, which limits the statistical significance of the results. This small sample size may not accurately reflect the models' performance across the entire dataset, and could lead to unreliable conclusions about the effectiveness of the proposed approach.

### Questions
* Quality Control: Could the authors provide more details on how post-collection dataset quality is evaluated? Specifically, what steps are taken to ensure regex extraction captures all figures and structures correctly?
* Downstream Applications: Beyond material generation tasks, have the authors explored how the finetuned model perform on other scientific tasks? (so does this dataset develops other LLMs abilities)
* Data Leakage: Do the authors evaluate potential data leakage between training and test sets? For example, similar images with different sub-charts might appear across different samples.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces MMSci, a dataset with high-quality and interleaved image-text data sourced from Nature Communications. The training set contains 742k figures from 131k articles, while the benchmark consists of several thousands of examples on a pre-defined set of tasks such as figure captioning and multiple-choice-based fig2cap and cap2fig matching. The authors conducted extensive experiments highlighting both the strengths and limitations of existing models and assessed the impact of finetuning VLMs on the training set. While the dataset is novel with comprehensive analysis, several issues require attention (see below).

### Strengths
- I believe that this is a novel dataset in the scope of scientific figure understanding that utilizes a different source than most existing works use (i.e., articles from nature communications instead arxiv preprints). This adds significant value to scientific figure understanding research by providing a different dataset distribution.
- The authors conducted extensive experiments to evaluate different models' performance on different tasks with different metrics, which lead to a very comprehensive result in terms of models' strengths and shortcomings. Further, authors verified that the training portion of the datasets brings significant advantage in improving the models’ semantic and stylistic patterns in generating captions for scientific figures in the nature communications distribution, and can potentially improve performance on text-only tasks such as material generation.
- The authors include a well-structured list of benchmark examples in the supplementary material, enhancing transparency and accessibility for the audience.

### Weaknesses
 - The current taxonomy comparison is misleading and can be improved. MMSci claims to cover 72 subjects, compared to CharXiv's 8 or SciCap's 1, but uses a more granular approach (e.g., "Cell Biology" as a separate subject from "Microbiology"). For consistency, authors should consider grouping these into five broader subjects (per Table 6) to better align with the definitions in other datasets.
- The entire benchmark only consists of permutations (e.g., matching subfigures to subcaptions), which could bias pre-trained models toward memorizing associations instead of correctly perceiving details in the image and retrieving the relevant knowledge correctly. There are no original questions in the benchmark.
- QA tasks focus on figure-caption matching, which may not require fine-grained domain knowledge required to analyze details within a figure but differences across figures (same for differences across captions given a subfigure). While captioning tasks do necessitate some scientific knowledge, the QA tasks might prioritize memory over understanding (e.g., recognizing details irrelevant to figure like "2.5 mm x 2.5 mm" in Figure 3, caption part b).
- The human baseline is not well designed. The authors recruited computer science graduate students to provide the human baseline in order to answer a set of challenging natural science questions that mostly require knowledge that is incompatible with computer science. It is unknown to what accuracy a model should achieve in order to match a human expert with domain-specific knowledge, and it is also unknown to what extent these multiple-choice questions make sense to human experts equipped with domain-specific knowledge. 
- For captioning tasks, the model finetuned on in-domain data achieved significantly higher score on the ROUGE metric yet underperforms its baseline counterpart in FActScore. Authors briefly explained that the fine-tuned model learned the semantic and stylistic details, but it seems that this training data also produce a negative impact on the model’s capability in retrieving correct knowledge i.e., FActScore. Authors should discuss the main effect of the training dataset more extensively (what is the impact on the model after being finetuned on the training set).

### Questions
- While the authors contrast its data contribution to ScienceQA, SciBench and MMMU, I believe that the authors should also discuss relevancy to MMStar [1] (which largely resolved the weaknesses mentioned in L178)?
- L359: Can authors verify the statement by evaluating the top 5 models on a different evaluator?
- Figure 4 is very confusing and the overlapping of performance from different models makes the comparison very hard to understand. Can authors use use a better way to visualize this or use a table instead?
- For figure 6, the gap between MMSci+MMC4 (Vis+Text) and MMSci+MMC4 (Text) seems to be small. Can authors additional provide standard error? Also, given many figures appear to have small texts, have authors verified the readability of figures after being downscaled to 336^2 (L452 where you stated the use of CLIP ViT-L/14-336)?
- An additional experiment that can be very helpful to understand the impact of your training dataset is to evaluate existing VLMs model finetuned on your dataset on other knowledge-based benchmarks such as MMMU (which also examines specific sub-divisions in natural science) to see whether the model is only fitting to the nature communication distribution or generalizing to a variety of distributions that requires retrieving knowledge based on multimodal input. Could authors provide an additional experiment on this?

-----
Update on 12/03:

The authors' latest response has reasonably addressed one of my concerns regarding potential benchmark quality issues by providing additional evidence. This evidence shows that top performers achieved very high accuracy and that there is significant variance among evaluators. Consequently, I have raised my score to 5.

### Soundness
1

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
The paper introduces a large diverse dataset of images and captions extracted from Nature Communications articles spanning 72 disciplines. They evaluate performance of multimodal LLMs on 2 types of tasks: (1) Figure captioning and (2)  Figure<-->caption matching tasks such as figure to caption matching, sub figure to caption matching, and caption to sub-figure matching.
The paper also includes a case study in materials science that demonstrates the value of the dataset to tune a LLaMA 2-7B model to generate or in-fill new material structures that are valid and stable.

### Strengths
* The paper introduces a large and diverse dataset capturing many domains that is missing in existing image caption datasets.

* A variety of open and closed models are used in the evaluations.

* The paper is written in a manner that is easy to follow.

### Weaknesses
The main weaknesses are that considering the diversity in the data, the tasks do not seem to go beyond standard tasks; and even on the figure captioning tasks, the analysis is lacking, particularly in terms of representation of strong evaluations from domain experts. 

1. The tasks are somewhat standard - Figure captioning, and matching figures/sub-figures to appropriate captions. It would have been nice to see some unique tasks created from this nice dataset showcasing the diversity of images/plots. e.g. some variety of interleaved image-text tasks such as Question Answering from images could have been considered.
2. It would have been nicer to have more detailed analysis of model responses for a few images (3-5) in about 10 domains. Where experts weigh-in on model responses even for just the figure captioning task to evaluate the strengths and weaknesses of models in the different domains. Especially on the variety showcased in Figure-2, e.g. 10 examples from each category in figure-2 analyzed by domain experts.
3. Some metrics for figure captioning are missing e.g. BLEU, CIDEr, SPICE (https://github.com/tylin/coco-caption) are metrics often used in figure captioning evaluations, and it would be good to include these. ROUGE is primarily a recall based metric, while it’s relevant, in itself it’s not a sufficient signal particularly for captioning.
    * Other LLM based metrics to consider using: LAVE (https://arxiv.org/pdf/2310.02567), L3Score (https://github.com/google/spiqa), PrometheusVision (https://github.com/prometheus-eval/prometheus-vision). L3Score is particularly interesting because you get the confidence from GPT-4o in addition to the generated response.
4. The results for the materials science case study is hard to interpret.

   4.1 What is the baseline LLAMA-2-7B performance? (without any tuning?) Many numbers in Table 5 and Figure 6 already seem quite high so it is hard to understand what baseline you are starting from and how much room for improvement there was (and from the presented results, it doesn’t look like that much, which perhaps may not be correct)

   4.2 How well do proprietary models perform on this task? Are there any proprietary models that generate reasonable responses worth evaluating?

   4.3 In Table 5, the “Stable DFT” column numbers for LLAMA models (from Gruver et. al.) appear to not be consistent with numbers reported in Gruver et. al. Why is that?

Minor

5. Related to point-2 Figure 4 is extremely difficult to follow. Perhaps reduce the materials science case study and include more detailed analysis of model responses and a discussion.
6. Figure 3 can be improved to clearly highlight the tasks and also the ground truth caption.
7. Other papers to consider citing in related works:
    * the papers proposing different relevant metrics noted in Weakness-3.
    *  https://openaccess.thecvf.com/content/WACV2024/papers/Tarsi_SciOL_and_MuLMS-Img_Introducing_a_Large-Scale_Multimodal_Scientific_Dataset_and_WACV_2024_paper.pdf

Initial rationale for rating of 5 is primarily due to weakness 1 and 2.

### Questions
Identical to weaknesses.

Weaknesses 3 and 4 should be easy to address in the rebuttal.

Weakness 2 is really key to making this task and dataset more valuable I hope you will consider involving domain experts to analyze responses from a few different questions.

---
---

**Discussion Phase**

The authors have provided detailed responses and additional analysis that address my main concerns. The human expert evaluations, additional scoring metrics, and the improvements to the materials science case study are all good additions and address my main concerns and have increased my score.

---
---

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a curated dataset derived from peer-reviewed Nature Communications articles that spans 72 diverse scientific fields. The dataset encompasses a rich diversity of figure types, including schematic diagrams and experimental visualizations. Through experimental benchmarks, the authors evaluate MLLM (Multimodal Language Model) performance on tasks like scientific figure captioning and multiple-choice question answering. The results, presented across both proprietary and open-source models, underscore the significant challenges MLLMs face when managing complex scientific content. Additionally, the paper highlights the dataset’s potential for pre-training in material science.

### Strengths
- The paper is well-structured and written in a clear, accessible manner.
- The dataset, MMSCI, is vast, comprising over 131k articles and 742k figures. It spans 72 scientific fields, providing a wide array of figure types from research articles.
- The multiple-choice question task is well-designed, utilizing authenticated labels from the articles, which is a reasonable and realistic setting.
- The pre-training experiment is a strong demonstration of MMSCI’s value, showcasing the dataset’s utility.

### Weaknesses
 - The MMSCICAP (Scientific Figure Captioning) task seems flawed. Providing only the abstract rather than figure-specific sentences—or even the entire relevant section—may undermine the task’s grounding. Abstracts alone should suffice only for captioning teaser figures; otherwise, the lack of figure-paired text may contribute disproportionately to the task’s difficulty.
- Multidisciplinarity is highlighted as a key feature, yet the experiments lack in-depth analysis on performance variation across disciplines. What factors contribute to these variations across different subjects? For example, why does Astronomy and Planetary Science yield high accuracy while disciplines with more data, like Materials Science, perform less well?
- Given the depth of scientific tasks, testing models like GPT-o1 or LMMs with enhanced reasoning abilities (e.g., chain-of-thought) could yield crucial insights for LMM development. While the dataset may not encompass all perspectives, enhanced reasoning capabilities could offer a more generalized solution to the complex nature of scientific reasoning.
- Line 230 mentions a figure caption but should clarify the “right” side to avoid confusion, as the caption does not appear on the “left” side.
- Minor typos:
  - Line 98, “Figure types” is preferable to “figures types.”
  - Consistency is needed in terminology: “Materials Science” appears in Figure 4(a) but “Material Science” in line 438.

### Questions
- How does GPT-o1 or other LMMs with advanced reasoning techniques (e.g., chain-of-thought) perform on these tasks?
- What factors drive the performance differences among disciplines?
- Why does Astronomy and Planetary Science show high accuracy compared to Materials Science, which has more articles and figures in the dataset?

### Soundness
2

### Presentation
3

### Contribution
2
