# MediConfusion: Can you trust your AI radiologist? Probing the reliability of multimodal medical foundation models

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Multimodal Large Language Models (MLLMs) have tremendous potential to improve the accuracy, availability, and cost-effectiveness of healthcare by providing automated solutions or serving as aids to medical professionals. Despite promising first steps in developing medical MLLMs in the past few years, their capabilities and limitations are not well-understood. Recently, many benchmark datasets have been proposed that test the general medical knowledge of such models across a variety of medical areas. However, the systematic failure modes and vulnerabilities of such models are severely underexplored with most medical benchmarks failing to expose the shortcomings of existing models in this safety-critical domain. In this paper, we introduce \methodname{}, a challenging medical Visual Question Answering (VQA) benchmark dataset, that probes the failure modes of medical MLLMs from a vision perspective. We reveal that state-of-the-art models are easily confused by image pairs that are otherwise visually dissimilar and clearly distinct for medical experts. Strikingly, all available models (open-source or proprietary) achieve performance below random guessing on \methodname{}, raising serious concerns about the reliability of existing medical MLLMs for healthcare deployment. We also extract common patterns of model failure that may help the design of a new generation of more trustworthy and reliable MLLMs in healthcare.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MediConfusion, a benchmark specifically designed to assess and expose failure modes in multimodal large language models (MLLMs) used in medical visual question answering (VQA) tasks. The benchmark highlights that current state-of-the-art MLLMs, including both open-source and proprietary models, struggle significantly with distinguishing visually dissimilar yet clinically distinct medical images, often performing below random guessing on the dataset. MediConfusion is created by identifying “confusing image pairs” from the ROCO radiology dataset, where image pairs appear distinct to medical professionals but prove challenging for MLLMs due to limitations in visual feature space alignment.

The authors reveal key failure patterns among MLLMs, such as difficulties in differentiating between normal and pathological anatomy, recognizing lesion characteristics, and identifying medical devices and vascular conditions. The benchmark leverages radiologist oversight to ensure clinical relevance and accuracy in the question-answer pairs, aiming to guide future MLLM improvements in medical contexts. By exposing these systematic vulnerabilities, the paper underscores the critical need for more reliable and trustworthy AI systems in healthcare applications.

### Strengths
Originality: The paper addresses a critical gap in the assessment of medical MLLMs by introducing MediConfusion, a novel benchmark explicitly designed to test the reliability of these models in healthcare. While prior benchmarks focus on overall performance in typical medical scenarios, this work innovatively emphasizes systematic failure modes by identifying “confusing image pairs” that challenge models with subtle, clinically important distinctions. The benchmark not only probes weaknesses but also highlights specific visual reasoning failures, which is a unique contribution to medical AI evaluation.

Quality: The dataset creation is rigorous, combining automated techniques with expert radiologist validation to ensure that each question is clinically relevant and accurately represents medical knowledge. The experimental design is robust, systematically evaluating a range of state-of-the-art models (both general and medical-domain MLLMs) and comparing their performance against baseline expectations. The detailed breakdown of common model failure patterns enhances the paper’s depth, providing actionable insights for improving MLLM robustness in medical settings.

Clarity: The paper is well-structured and presents its findings in a clear, logical manner. Descriptions of the dataset creation process, evaluation methods, and results are easy to follow, with visual aids (e.g., figures illustrating confusing image pairs) that help readers understand the complexity of the visual tasks posed to models. The breakdown of error types further clarifies the distinct challenges MLLMs face, enhancing the reader’s comprehension of the benchmark’s significance.

Significance: The benchmark’s focus on failure modes has broad implications for the deployment of MLLMs in healthcare. By surfacing limitations that could compromise patient safety, the work serves as a foundational tool for future research aimed at increasing AI reliability in clinical practice. Additionally, MediConfusion highlights the limitations of current visual encoders and training paradigms in handling medical data, offering a clear research direction for building more robust and trustworthy models. The benchmark’s significance is further bolstered by its potential as a standard for evaluating and guiding improvements in medical AI systems.

### Weaknesses
Limited Dataset Size: While the MediConfusion benchmark is rigorous, the dataset size (352 questions across 9 categories) may be relatively small to capture the full spectrum of medical image complexity. Expanding the dataset with a broader range of confusing image pairs, potentially covering additional anatomic regions and diagnostic subtleties, could improve its generalizability and make it more comprehensive for model evaluation across diverse medical contexts.

### Questions
1.	Dataset Diversity and Expansion: Could you elaborate on the decision to limit the benchmark to the ROCO dataset? Do you have plans to expand MediConfusion to include other datasets, such as ultrasound or nuclear imaging, to capture a broader range of diagnostic tasks? Additional dataset diversity might reveal new model weaknesses or challenges in different medical imaging modalities.
	2.	Impact of Prompt Engineering: Given the importance of prompt phrasing in VQA tasks, did you experiment with alternative prompt formats or styles (e.g., framing questions in different ways or including detailed instructions)? If so, what impact did this have on model performance, and could further prompt optimization improve reliability? Insights here could guide future research on prompt refinement in medical VQA.
	3.	Future Directions for Medical MLLM Improvements: Given the identified failure patterns (e.g., difficulties with spatial reasoning or lesion characteristics), do you have specific recommendations for architectural or training adjustments that could address these weaknesses? For example, do you see value in integrating spatial attention mechanisms or training models on more anatomically detailed data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper evaluates reliability of medical VLMs. The authors introduce MediConfusion, a benchmark comprising 352 pairs of “confusing” medical images. Each pair consists of images that are visually distinct yet similar in feature space. The authors leverage GPT-4 to generate questions for which the answers differ between the two images. The benchmark data is further evaluated by a radiologist. Experimental results indicate that MediConfusion poses significant challenges to several existing VLMs, highlighting areas for improvement and setting the stage for future research.

### Strengths
1. The paper addresses a well-motivated and underexplored problem in the medical domain.
2. The benchmark creation process is robust, with manual evaluation by a radiologist enhancing its credibility.
3. The experiments are comprehensive, demonstrating that MediConfusion presents substantial challenges to current VLMs, with promising potential for inspiring future research.

### Weaknesses
While this work provides valuable insights, it appears to closely follow the Multimodal Visual Patterns (MMVP) benchmark framework, potentially limiting its novelty. Many findings align with known challenges in general VLMs. Specifically, the reliance on feature similarity metrics like DINO and BiomedCLIP, while useful for identifying confusing pairs, doesn't fully address the nuances of medical image interpretation. The benchmark, while manually validated by a radiologist, might still inherit biases from the selection process, potentially skewing the evaluation towards specific types of medical images or pathologies. The lack of a more diverse set of medical imaging modalities, beyond those commonly found in existing datasets, could also limit the generalizability of the findings.

### Questions
1. Are there confusing pairs that appear visually similar but differ in feature space?
2. How would the Mixture-of-Features method from "Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs" apply to medical VLMs?
3. What are the limitations of the confusing pairs identified here? Could there be potential biases?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper evaluates the reliability of medical Multimodal Large Language Models in healthcare. The authors present MediConfusion, a new VQA benchmark that highlights distinguishing similar medical xray images. They find that all tested MLLMs, open-source and proprietary, perform below random chance on MediConfusion, indicating serious reliability issues.

### Strengths
- The idea of using the same question with similar images could offer a interesting way to probe model weaknesses.

- With the help of an expert-in-the-loop pipeline, the paper thoroughly examines why models struggle to differentiate between visually similar medical images.

- The evaluation metrics are comprehensive, particularly accommodating models unable to directly answer multiple-choice questions.

### Weaknesses
 - The motivation is not clear. The authors claimed that "existing benchmark datasets are focused on evaluating the medical knowledge of MLLMs across large evaluation sets, heavily biased towards common or typical scenarios." What are the common and typical scenarios? Could you provide a more detailed discussion about this limitation of existing benchmarks and how the proposed benchmark in this paper can overcome the limitations?
- The results show that all available models (open-source or proprietary) achieve performance below random guessing on MediConfusion. It would be better if the authors conducted more experiments to find the reasons. For example, by using different sim_med and sim_gen thresholds and compare the model performance, we can identify whether the models can differentiate easy image pairs or they even cannot differentiate any image pairs. 
- The writing style needs refinement. For instance, the phrase "stress-tests the visual capabilities of state-of-the-art models" is unclear and may confuse readers. The motivation and innovative aspects of the benchmark remain vague until "image pair" is mentioned at the end of Section 2, and even then, it is not clarified that the task is framed as multiple-choice questions. It would be easier for the readers to better understand this paper if the writer could clarify these designs in the introduction section.
- The rationale for focusing on the medical domain is unclear. The methods do not appear specific to this field, resembling a rephrasing of existing VQA datasets where answers are scrambled, and models are tasked with similar image comparisons. Could you explain what is the specific design of this benchmark considering its medical context? What is the difference between two similar medical images and two similar general images?
- The choice to format the task as multiple-choice is questionable. Have you considered open-ended QA or report generation of CXR images? Additionally, given the relatively small dataset (352 questions), this benchmark may lack the scale needed to effectively assess MLLM capabilities. Could you justify that 352 questions are sufficient for the evaluation?

### Questions
- Does the proposed benchmark dataset only contain 352 image pairs?

- The authors only evaluate the models on the similar pair images. Can the models work well on different image pairs? For example, to use different sim_med and sim_gen thresholds and compare the model performance.

### Soundness
3

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
3

### Summary
The paper introduces MediConfusion, a challenging medical Visual Question Answering (VQA) benchmark that exposes the vulnerabilities of current medical multimodal large language models (MLLMs) by highlighting their failure modes. Despite promising progress, existing models—open-source and proprietary—struggle significantly, even performing below random guessing in certain tests. This suggests major reliability issues in deploying these models for healthcare. The benchmark was guided by clinician experts, using adversarial examples to stress-test models, offering a valuable resource for the research community to design more trustworthy MLLMs. Personally I like this paper because it hits on a crucial gap in medical AI that’s often overlooked.

### Strengths
1. The paper brings a novel perspective by focusing on the systematic failure modes of medical multimodal models—something that hasn’t been extensively explored before. The fact that state-of-the-art models performed at or below random guessing levels is a striking finding. I can see this dataset becoming a benchmark everyone wants to use as soon as the paper is out, as it offers a strong challenge to prove model reliability.

2. The presentation and writing are clear and well-structured.

### Weaknesses
1. One significant limitation is that it feels almost obvious to train a model using both public data and this new dataset to demonstrate improved performance over current models. It’s surprising this wasn’t attempted—even for a dataset paper. Adding such experiments could have strengthened the impact by showing how incorporating MediConfusion directly improves model reliability.

2. The authors might also want to discuss the importance of the image encoder in these models. For example, both LLaVA and LLaVA-med use encoders trained on everyday images, which could be a reason why LLaVA-med performs even worse than LLaVA. If the encoder isn’t well-suited for medical images, it limits the model's ability to learn effectively. Highlighting the role of specialized image encoders could have added valuable insights into improving model reliability in the medical domain.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
4
