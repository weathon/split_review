# ScImage: How good are multimodal large language models at scientific text-to-image generation?

- Decision: Accept
- Avg Score: 5.33
- Scores: 5, 3, 8

## Abstract
Multimodal large language models (LLMs) have demonstrated impressive capabilities in generating high-quality images from textual instructions. However, their performance in generating scientific images—a critical application for accelerating scientific progress—remains underexplored. In this work, we address this gap by introducing \ourmodel{}, a benchmark designed to evaluate the multimodal capabilities of LLMs in generating scientific images from textual descriptions. \ourmodel{} assesses three key dimensions of understanding: spatial, numeric, and attribute comprehension, as well as their combinations, focusing on the relationships between scientific objects (e.g., squares, circles). We evaluate five models, GPT-4o, Llama, AutomaTikZ, Dall-E, and StableDiffusion, using two modes of output generation: code-based outputs (Python, TikZ) and direct raster image generation. Additionally, we examine four different input languages: English, German, Farsi, and Chinese. Our evaluation, conducted with 11 scientists across three criteria (correctness, relevance, and scientific accuracy), reveals that while GPT-4o produces %hig-quality results 
outputs of decent quality for simpler prompts involving individual dimensions such as spatial, numeric, or attribute understanding in isolation, all models face challenges in this task, especially for more complex prompts.%and specific scientific objects.%We will publicly release \ourmodel{} along with reference images upon acceptance.
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduced a benchmark, ScImage, for evaluating models for generating scientific images from textual descriptions. This paper thoroughly investigated the existing datasets and benchmarks for scientific image generation, and pointed out there is no systematic evaluations for scientific text-to-image models. This paper evaluated 5 state-of-art models with 2 generation modes: text-image and text-code-image, while text-code-image includes TikZ and Python as coding language. The benchmark emphasizes comprehension along three dimensions: numeric, spatial and attribute. It contains a 404 hundreds queries in 101 templates. Human evaluation is based on correctiveness, relevance and scientific style. It is good including agreements analysis of the human annotations to make sure human evaluation is reliable. The 5 models are compared over these criteria, and compilation failure is pointed out as a drawback of text-code-image models. Detailed analysis is made on types of understanding, object categories, multilingual prompts, and different programming languages. A qualitative analysis is conducted and highlighted some typical failures about understanding physical world. The findings underscore the further exploration on generating scientific images with LLMs. The paper summarized some limitations, such as not utilizing chain-of-thought, not developing automatic metrics and potential ethic issues. 
Overall, the paper is well written, and has the potential to contributes a new benchmark for evaluating models capability to generate scientific image, which enables more comprehensive analysis towards models, especially LLMs.

### Strengths
1. Originality: The paper presents a potentially valuable contribution by introducing a new benchmark, ScImage, specifically focused on evaluating scientific image generation from text descriptions. While benchmarks for general text-to-image generation exist, few are tailored for scientific image generation, where precision in spatial, numeric, and attribute comprehension is critical. This benchmark addresses a gap in the current evaluation landscape, particularly for multimodal LLMs.

2. Quality: The paper presents a clear structure and coherent organization. While it contains several commendable elements, there are areas where improvement is needed to enhance the overall quality of the research. Addressing these aspects could significantly strengthen the findings and their implications.

3. Clarity: The paper is clearly structured, with each section flowing logically into the next. The figures and examples enhance comprehension by illustrating key points effectively.

4. Significance: The benchmark’s potential to foster progress in scientific image generation could be significant, as this area has notable applications in research, education, and communication. By evaluating models on the specific demands of scientific image generation, such as spatial accuracy and numeric precision, this benchmark could aid in developing more capable multimodal models tailored to scientific needs.

### Weaknesses
There are some problems, which must be solved before it is considered for publication. If the following problems are well-addressed, I believe that the essential contribution of this paper are important for evaluating LLMs' capability of text to image generation.
1. Your manuscript needs careful editing and particular attention to spelling, for example, in Figure 7, "Llame" should be "Llama".
2. Concerns with Dataset Construction:  I question the methodology used in constructing the dataset. The dataset appears to be generated from templates, producing a variety of prompts but lacking ground truth. Additionally, the dataset's size is relatively small, with only around 400 examples, which contrasts starkly with related datasets mentioned in the paper that typically consist of tens of thousands of examples. This raises concerns about the quality of the generated prompts and whether the dataset is sufficient to adequately evaluate the model. I suggest to add a quality analysis to the dataset. For example, evaluating a subset of the dataset with domain experts to make sure the generates prompts make sense, and performing some analysis to ensure the diversity and representativeness despite of the small size of dataset.
3. Concerns with Evaluation Approach:  I am also skeptical about the evaluation methodology, as it relies solely on human assessments. The authors justify this choice by referencing limitations of automated evaluation metrics, particularly in the context of scientific figures where metrics like CLIP Score and FID Score may fall short. For example, they mention issues noted by the MMVP benchmark with automated evaluations, especially in accurately identifying specific directions like "up" and "down." However, citing one bad case is insufficient to conclude that automated evaluation is unreliable. I would suggest to provide more detailed and comprehensive reasoning for the necessity for human evaluation over automated metrics in this specific context.
4. Lack of Depth in Result Analysis:  The results section primarily describes the scores obtained by each model but lacks a deeper analysis of these results. I would suggest to add the possible explanation to the observed phenomenon, the underlying problem of the models, and how the results indicates the directions for improvement. That could offer valuable insights for future research, enhancing the paper’s overall impact and utility.

### Questions
Data Construction:
1. Can you provide a detailed explanation of the rationale behind constructing the dataset solely from generated prompts based on templates? What considerations were made regarding the lack of ground truth in this dataset? Additionally, have you considered using real-world scientific data to construct the prompts, which would provide a more robust basis for evaluation?
2. Given that the dataset is relatively small, with only around 400 entries, how do you justify its representativeness and reliability compared to other related datasets that typically contain tens of thousands of examples?
3. You mentioned that you are only using the most commonly encountered types listed in the taxonomy. How did you decide which ones are the most commonly encountered?

Human Evaluation:
You mentioned that automated evaluations can be unreliable, particularly in recognizing precise directions in text and images. Can you elaborate on the specific limitations of current automated metrics, especially in the context of evaluating scientific graphs? Why do you believe that a single bad case is sufficient to justify the exclusive reliance on human evaluation?

Evaluation Guideline:
I suggest revising the evaluation guidelines to recommend using the same prompt for generating images with different scores, rather than using different prompts for different scores. How would you justify this approach, and do you believe it could lead to a more reliable assessment of the generated images?

Result Analysis: 
In the results section, there is a description of the experimental data but a lack of in-depth analysis of the results. Could you clarify the reasoning behind the evaluation results? How do you believe that this level of analysis contributes to the significance of your findings and their applicability to future research in this area?

### Soundness
2

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
4

### Summary
This work presents a novel benchmark dataset designed to evaluate the multimodal capabilities of large language models (LLMs) in generating scientific images from textual descriptions. The dataset encompasses a wide variety of formats, including 2D/3D shapes, charts, graph theory representations, matrices, tables, and more, with a focus on assessing spatial, numerical, and attribute comprehension. The evaluation process involved 11 scientists who reviewed the performance of models such as GPT-4, LLaMA, and Stable Diffusion.

However, the dataset primarily consists of query templates, which limits its applicability to other models, as the evaluation heavily relies on human (scientist) assessments. Furthermore, the technical details provided are not sufficiently rigorous, with multimodal models and Stable Diffusion collectively categorized as large language models, resulting in imprecision and lack of clarity. Additionally, several relevant prior works are inadequately cited or discussed, which detracts from the comprehensiveness of the study.

### Strengths
1. This dataset includes a wider variety of image types compared to previous work that primarily focused on charts and bar graphs.
2. The evaluation was conducted by 11 scientists, ensuring high-quality assessment. However, this dependence on human evaluation limits the benchmark dataset's scalability for testing additional models.
3. The study also evaluates various textual description languages and coding languages/packages, making the analysis comprehensive.

### Weaknesses
1. The paper lacks a thorough introduction to related work on the interpretation of scientific images, such as [1, 2, 3]. Furthermore, the distinctions between this work and ChartMimic remain unclear. To enhance clarity, Table 8 in the appendix should be included in the main body to better illustrate how this study compares to previous research.

2. The dataset primarily consists of query templates, which limits its generalizability for evaluating other models due to the heavy reliance on human (scientist) assessments. 

3. Given the focus on scientific images, it is crucial to evaluate the model’s understanding of domain-specific scientific knowledge embedded within these images, rather than solely assessing spatial, numerical, or attribute-based features (e.g., color, size, shape). Images from domains such as biology, chemistry, physics, and materials science contain nuanced, domain-specific information that should be considered to provide a more complete assessment.

### Questions
1. How does this benchmark dataset differ from ChartMimic, and why should it be discussed extensively in the main body?
2. How can this benchmark be used to evaluate other models? Is evaluating only GPT-4 and LLaMA sufficient, or should more multimodal LLMs be tested?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new benchmark, ScImage, which evaluate models abilities of scientific text-to-image generation, in both code-based and multimodal modes. This benchmark is multilingual, containing 4 languages. This benchmark emphasizes models' spatial understanding, numeric understanding, and attribute binding abilities. The authors use human evaluation for images generated by 5 models, where gpt-4o outperformed all other models.

### Strengths
- The authors introduce ScImage, which contributes to evaluation of models' scientific image generation capabilities.
- ScImage includes a wide range of tasks, which could provide comprehensive evaluation of models' image generation abilities.
- The authors provide detailed query construction process and templates, which could help creation of new queries.
- The authors provide example queries and example outputs of models, which facilitates understanding the benchmark.

### Weaknesses
 - The authors use human evaluation to assess models' performances on this benchmark. It is good to know how humans rate the outputs, but it is less scalable if using human evaluation. If other people would like to test their models on this benchmark, they would need to also hire professional human evaluators, which would be expensive given that this benchmark contain more than 400 instances. It would be good if the authors could explore automated metrics that have high correlation with human evaluation results, or provide a crowdsource platform where human eval could be less costly, or use llm-as-a-judge methods to automatically evaluate model outputs.
- The authors provide limited number of models' results on this benchmark. It would be good to see how other open source models perform on this benchmark, such as

### Questions
- How should people evaluate other models' performances on this benchmark without needing human evaluators? For example, using image-image similarity between the generated model output with a oracle image for each task could provide a basic idea on how well the model output is. Additionally, llm-as-a-judge could potentially evaluate the model outputs as well.

### Soundness
2

### Presentation
3

### Contribution
3
