# Why context matters in VQA & Reasoning: Semantic interventions for VLM input modalities

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
The various limitations of Generative AI, such as hallucinations and model failures, have made it crucial to understand the role of different modalities in Visual Language Model (VLM) predictions. Our work investigates how the integration of information from image and text modalities influences the performance and behavior of VLMs in visual question answering (VQA) and reasoning tasks. We measure this effect through answer accuracy, reasoning quality, model uncertainty, and modality relevance. We study the interplay between text and image modalities in different configurations where visual content is essential for solving the VQA task. Our contributions include (1) the Semantic Interventions (SI)-VQA dataset, (2) a benchmark study of various VLM architectures under different modality configurations, and (3) the Interactive Semantic Interventions (ISI) tool.
The SI-VQA dataset serves as the foundation for the benchmark, while the ISI tool provides an interface to test and apply semantic interventions in image and text inputs, enabling more fine-grained analysis. Our results show that complementary information between modalities improves answer and reasoning quality, while contradictory information harms model performance and confidence. Image text annotations have minimal impact on accuracy and uncertainty, slightly increasing image relevance. Attention analysis confirms the dominant role of image inputs over text in VQA tasks. In this study, we evaluate state-of-the-art VLMs that allow us to extract attention coefficients for each modality. A key finding is PaliGemma's harmful overconfidence, which poses a higher risk of silent failures compared to the LLaVA models. This work sets the foundation for rigorous analysis of modality integration, supported by datasets specifically designed for this purpose. The code is available at \url{https://gitlab.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work investigates the impact of different modalities – image and text – on the performance of Visual Language Models in Visual Question Answering (VQA) tasks. 
The authors examine how the combination and interplay of these modalities affect accuracy, reasoning quality, model uncertainty, and attention attribution. 
They collect a novel dataset (SI-VQA) with controlled interventions and an interactive tool (ISI) for manipulating image and text inputs to study VLM behavior. 
This work sets the foundation for further analysis of modality integration in VQA, hightlighting the crucial role of context in guiding future model developments.

### Strengths
1. This work introduces the SI-VQA dataset, which is designed to require image-based answers, ensuring that visual content is essential for solving VQA tasks. This setup allows researchers to analyze how different modalities (image, text, context) influence the model’s accuracy, reasoning, and uncertainty​.

2. Comprehensive Benchmarking of VLMs: This work establishes a robust benchmark by evaluating various state-of-the-art VLMs under diverse modality configurations. This benchmarking approach highlights the contributions and limitations of each modality, as well as the strengths and weaknesses of different VLM architectures.

3. This work introduces the ISI Tool, enabling researchers to perform semantic interventions on VLM inputs, which supports fine-grained analysis of VLM behavior.

### Weaknesses
1. There are some concerns about the dataset.
2. The work lacks comparisons with other current datasets.
3. The work lacks supporting evidence for its claims.
4. The work lacks formal definitions of certain terms.

### questions:
 Here are the corrected versions of the reviews:

1. The proposed dataset contains only 100 samples, which is quite limited in this domain.

2. The answers are limited to "Yes" or "No." Moreover, the paper does not specify the distribution of "Yes" versus "No" answers in the dataset. This leads to the following two concerns:

   - **Model Bias**: If the dataset is heavily skewed toward one answer (e.g., mostly "Yes" answers), it could introduce bias in the models, potentially leading them to favor that answer even when the visual information suggests otherwise.

   - **Impact of Interventions**: Without knowing the baseline distribution of answers, it is challenging to isolate the true effect of the semantic interventions (complementary context, contradictory context, image annotations) on the models' performance. For example, if the dataset already has a majority of "Yes" answers, an intervention that improves performance on "Yes" questions might not necessarily reflect a genuine improvement in the model's ability to understand the visual information.

3. Even though each sample is well-annotated (i.e., an image, a corresponding question with a ground truth Yes/No answer, a text-annotated version of the image, a contradictory context, and a complementary context), there are no comparisons between the proposed dataset and state-of-the-art (SOA) datasets regarding its advantages in Image-dependent Answers and Content Domain Diversity.

4. Regarding the claim that image text annotations have minimal impact on accuracy, or even decrease accuracy, the authors list some potential reasons for this, e.g., VLMs may already extract relevant information from images. It would be helpful to provide some qualitative or quantitative results to further support these explanations.

5. The term "modality relevance" is first mentioned in the abstract. However, there is no formal definition provided for it.

### Questions
Here are the corrected versions of the reviews:

1. The proposed dataset contains only 100 samples, which is quite limited in this domain.

2. The answers are limited to "Yes" or "No." Moreover, the paper does not specify the distribution of "Yes" versus "No" answers in the dataset. This leads to the following two concerns:

   - **Model Bias**: If the dataset is heavily skewed toward one answer (e.g., mostly "Yes" answers), it could introduce bias in the models, potentially leading them to favor that answer even when the visual information suggests otherwise.

   - **Impact of Interventions**: Without knowing the baseline distribution of answers, it is challenging to isolate the true effect of the semantic interventions (complementary context, contradictory context, image annotations) on the models' performance. For example, if the dataset already has a majority of "Yes" answers, an intervention that improves performance on "Yes" questions might not necessarily reflect a genuine improvement in the model's ability to understand the visual information.

3. Even though each sample is well-annotated (i.e., an image, a corresponding question with a ground truth Yes/No answer, a text-annotated version of the image, a contradictory context, and a complementary context), there are no comparisons between the proposed dataset and state-of-the-art (SOA) datasets regarding its advantages in Image-dependent Answers and Content Domain Diversity.

4. Regarding the claim that image text annotations have minimal impact on accuracy, or even decrease accuracy, the authors list some potential reasons for this, e.g., VLMs may already extract relevant information from images. It would be helpful to provide some qualitative or quantitative results to further support these explanations.

5. The term "modality relevance" is first mentioned in the abstract. However, there is no formal definition provided for it.

### Soundness
2

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
5

### Summary
This paper explores the impact of contextual information on Visual Question Answering (VQA) and reasoning within Vision-Language Models (VLMs). The study introduces the Semantic Interventions (SI)-VQA dataset and the Interactive Semantic Interventions (ISI) tool to evaluate how image and text modalities interact to affect model performance, accuracy, and uncertainty. The methodology involves benchmarking multiple VLM architectures under different configurations, integrating complementary or contradictory text with images. Experimental results indicate that integrating complementary information enhances model accuracy and reasoning quality, whereas contradictory information significantly degrades performance. Moreover, VLMs show a bias toward image inputs over textual context, with PaliGemma exhibiting notable overconfidence, leading to increased silent failures compared to LLaVA models. The study emphasizes the crucial role of modality integration and provides tools for better understanding VLM behavior in multimodal tasks.

### Strengths
1)	The impact of context and different modalities on VQA has always been a noteworthy topic. This paper's discussion, incorporating VLM, is insightful for future researchers.
2)	The experimental design in this paper is very thorough, with detailed consideration given to seven different input configurations.
3)	Some of the findings in the experimental results of this paper are very interesting and offer valuable insights for the design and application of future VLMs.
4)	This paper has released the dataset and the ISI tool.

### Weaknesses
1) My primary concern is that the paper mainly describes the observed phenomena in the experimental results without providing sufficient analysis of why these results occur (though there is some experimental analysis). In particular, the paper does not explain how these results could be useful for advancing future VQA work or analyze what could be done to address some of the issues identified in the results. Additionally, some of the findings are not particularly novel, making the paper seem more like an experimental report.
2) As the authors pointed out in the paper, the SI-VQA dataset has too few samples, with only one hundred entries. Although the authors believe these data are representative, they should at least analyze why the results from these one hundred samples are convincing. Is it because these one hundred samples are of high quality and diversity?

### Questions
1)	It appears that image text annotations have little effect on some of the model's metrics; for example, the results of Q+I_A+C_+ in Figure 2a are not optimal. Could the authors analyze the reason for this phenomenon?
2)	I don't quite understand why the initial hypothesis is introduced in Section 5.1, as it doesn't seem to be strongly related to the main part of the experiments.
3)	Could the authors explain specifically how GPT-4o is used as an evaluator of reasoning ability? Since the SI-VQA dataset has only 100 samples, why didn’t the authors consider using human evaluation instead? Would that provide more accurate results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the limitations of Generative AI, particularly in Visual Language Models (VLMs), focusing on how the integration of image and text modalities affects performance in visual question answering (VQA) and reasoning tasks. They use only 100 samples to gain some conclusions in the paper, such as "complementary information between modalities improves answer and reasoning quality".

### Strengths
1. This paper is well-written and easy to understand.
2. The experimental analysis is comprehensive.
3. The conclusions drawn are intuitively credible.

### Weaknesses
1.  The dataset contains only 100 samples, and the conclusions drawn lack novelty; they are basic findings that have been established in previous multimodal research. The importance of multimodal complementarity is widely recognized in the field, so the conclusions of this article lack originality.

2. Overall, this article is a fairly good technical report that provides a comprehensive experimental analysis.

### Questions
Are there any other interesting conclusions or exploratory directions for uncovering the importance of multimodal complementarity?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents to evaluate the robustness of VLLMs.
In particular, there are two dimensions that the advocated evaluation protocol considers: 
1) modality bias - whether VLLMs make predictions based on the linguistic relations;
2) context - whether the context helps in reasoning. 

Based on this idea, this paper collects a new dataset and then evaluates various VLLMs, including LLaVA, and Pali-Gemma.
Besides, the authors also provide some analysis from the dimension of semantic entropy and attention distribution.

### Strengths
- The studied problem - the robustness of VLLMs, is practical and interesting for the research community.
- The authors adopt two different families of models for evaluation, including both LLaVA and Pali-Gemma.
- There are some more dimensions that are considered by this paper, like semantic entropy and attention distribution.

### Weaknesses
 - The biggest limitation of this paper lies in its limited dataset size.
Specifically, there are only 100 instances of the collected dataset.
From this point of view, most of the conclusions from this work might be plausible and not stand.
Additionally, we cannot name a scale of such a dataset as ``comprehensive``.
- The authors are suggested to test larger model sizes, such as 13B models - LLaVA-1.5-vicuna-13B.
- It seems like there is a strong connection between this work and several well-studied problems such as modality bias (language prior) in VQA [1][2], and visual commonsense reasoning (VCR) [3].

### Questions
See the weakness part for a detailed explanation.

### Soundness
1

### Presentation
2

### Contribution
1
