# VISCON: Identifying and Benchmarking Vision Hallucination for Large Vision-Language Model

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 3, 5, 5

## Abstract
Large Vision-Language Models (LVLMs) have demonstrated exceptional capabilities in a variety of vision-language tasks, but suffer from "vision hallucinations" - a tendency generating text inconsistent with the image. This issue hampers their practical use in real-world applications.
    To effectively evaluate and detect these hallucinations, we introduce VISCON (VISual Concept cONsistency), a benchmark framework comprising a benchmark image dataset and quantitative evaluation pipelines to assess vision hallucinations in LVLMs. VISCON extends beyond previous hallucination metrics by offering: a) diverse image styles across multiple visual domains, b) evaluation of a broader range of visual concepts, including objects, attributes, and relationships, and c) high annotation density from detailed scene-graph annotations to reduce false negatives. These improvements enable comprehensive analysis of hallucinations related to both domain shifts and concept types and offer more accurate hallucination evaluation. 
To detect vision hallucinations, we propose two innovative evaluation pipelines within VISCON: an Earth Mover's Distance (EMD)-based pipeline and an "Evaluate-By-Edit" pipeline. The EMD-based pipeline measures the distributional similarity between the reference visual concepts and those mentioned by LVLMs, robust against vocabulary shifts between annotations and natural language responses. The Through extensive experiments on six leading LVLMs, VISCON reveals crucial insights into the nature of vision hallucinations. Our findings indicate that factors such as image domain shifts, complexity of visual concepts and model response length significantly influence the occurrence of hallucinations in LVLM responses. Additionally, human evaluations confirm that VISCON aligns with human preferences better than established hallucination metrics. "Evaluate-By-Edit" focuses on the edit distance between the original LVLM response and a hallucination-reduced version revised according to the rich visual concept annotations, providing an interpretable analysis of hallucinated content. Importantly, our method directly evaluates captioning responses, unlike previous metrics that query the existence of individual visual concepts. This approach is more challenging, as it requires models to handle multiple concepts simultaneously, providing better discrimination of LVLM performance.
Through extensive experiments on six leading LVLMs, VISCON reveals crucial insights into the nature of vision hallucinations. Our findings indicate that factors such as image domain shifts, complexity of visual concepts and model response length significantly influence the occurrence of hallucinations in LVLM responses. Additionally, human evaluations confirm that VISCON aligns with human preferences better than established hallucination metrics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the issue of visual hallucinations in LVLMs by proposing a new evaluation dataset. This dataset spans various image styles and task types. Unlike traditional VQA formats that employ discriminative assessments, this work allows models to generate open-ended responses. To directly evaluate the quality of these generative outputs, the authors propose two new evaluation pipelines and metrics.

### Strengths
1. It explores the impact of different image styles on visual hallucinations.
2. The approach allows models to produce open-ended responses instead of simple yes/no answers. To enable evaluation within these generative outputs, two specialized pipelines and corresponding metrics have been designed.
3. The issue of visual hallucinations is a significant challenge for LVLMs, and research that reflects this problem from multiple perspectives and dimensions is valuable.

### Weaknesses
1. The motivation for creating a hallucination dataset needs clarification. This dataset does not specifically emphasize hallucination evaluation. While distinguishing between visual hallucinations and errors can be challenging, the paper should at least specify the targeted sources of hallucination rather than broadly adding data and task types. It’s important to clarify why the community needs this dataset.

2. A new hallucination dataset should provide novel insights. The lower performance on attributes and relationships compared to objects is expected and not unique to this dataset. More interesting conclusions, like the impact of domain shift and response length, are only briefly discussed. A deeper analysis of these factors is needed for a dataset paper.

3. It’s also worth noting that if the performance drop is simply attributed to insufficient training (L432-L434), it raises questions about the dataset’s significance. In fact, based on Table 2, the performance differences across image styles seem minimal, suggesting that adding relevant training data could easily address this issue.

4. The link between image style and hallucinations needs further exploration. While a key contribution of this paper is testing hallucination across varied image styles, merely noting that style transformations (e.g., line drawings) cause performance drops is insufficient. Such drops are expected, given the limited training data for alternative styles, which seems more about training gaps than hallucinations. By contrast, POPE’s setup is more convincing, as it attributes hallucinations to textual context coexistence—a persistent issue regardless of training data expansion.

5. The paper lacks analysis on the sources of hallucinations. While POPE links hallucinations to high term co-occurrence and designs its pipeline around this, this paper's dataset mainly supplements existing data with new task types and styles. If the dataset only broadens existing types without addressing specific hallucination issues—especially if more training data could improve performance—its contribution may be limited. 

6. The comparison with related work is insufficient. Some existing work, such as AMBER[1], PhD[2], FaithScore[3], has already expanded hallucination task types and evaluation formats, including attributes, relationships, and open-ended assessments. What is the unique contribution of your work compared to these existing studies?

7. The description of the two metrics designing and pipeline diagram is unclear. I recommend clarifying why both two metrics are needed and how they complement each other. Given the use of LLMs in the pipeline, why not directly use LLMs for end-to-end judgment?

8. The paper also lacks a clear presentation of the data format—images, prompts, and labels are hard to understand from text alone. Figure 1 devotes much space to visual hallucinations, which is widely understood, and may be unnecessary. Figures 2 and 3 are also hard to follow. For instance, in Figure 2(a), how is the sunflower image derived from transforming the motorcycle’s style? In L262, what is the meaning of the dissimilarity matrix? What is your specific computing method for d_{EDIT}?

### Questions
1. The link between image style and hallucinations needs further exploration. While a key contribution of this paper is testing hallucination across varied image styles, merely noting that style transformations (e.g., line drawings) cause performance drops is insufficient. Such drops are expected, given the limited training data for alternative styles, which seems more about training gaps than hallucinations. By contrast, POPE’s setup is more convincing, as it attributes hallucinations to textual context coexistence—a persistent issue regardless of training data expansion.

2. The paper lacks analysis on the sources of hallucinations. While POPE links hallucinations to high term co-occurrence and designs its pipeline around this, this paper's dataset mainly supplements existing data with new task types and styles. If the dataset only broadens existing types without addressing specific hallucination issues—especially if more training data could improve performance—its contribution may be limited. 

3. The comparison with related work is insufficient. Some existing work, such as AMBER[1], PhD[2], FaithScore[3], has already expanded hallucination task types and evaluation formats, including attributes, relationships, and open-ended assessments. What is the unique contribution of your work compared to these existing studies?

4. The description of the two metrics designing and pipeline diagram is unclear. I recommend clarifying why both two metrics are needed and how they complement each other. Given the use of LLMs in the pipeline, why not directly use LLMs for end-to-end judgment?

The paper also lacks a clear presentation of the data format—images, prompts, and labels are hard to understand from text alone. Figure 1 devotes much space to visual hallucinations, which is widely understood, and may be unnecessary. Figures 2 and 3 are also hard to follow. For instance, in Figure 2(a), how is the sunflower image derived from transforming the motorcycle’s style? In L262, what is the meaning of the dissimilarity matrix? What is your specific computing method for d_{EDIT}?

Ref:
[1] An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination Evaluation
[2] PhD: A Prompted Visual Hallucination Evaluation Dataset
[3] FaithScore: Fine-grained Evaluations of Hallucinations in Large Vision-Language Models

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
They introduce VISCON, a new benchmark framework aimed at evaluating vision hallucinations in Large Vision-Language Models (LVLMs) like GPT-4V and LLaVA. VISCON alleviates limitations of existing metrics by incorporating a diverse dataset with comprehensive visual concept annotations (objects, attributes, relationships) and includes two evaluation pipelines: an Earth Mover's Distance (EMD)-based approach for robust similarity assessment and an "Evaluate-By-Edit" pipeline for refining interpretability. Applying VISCON to six leading LVLMs, the study reveals insights into hallucination trends related to image domain shifts and response length, showing VISCON’s enhanced alignment with human judgments over existing methods.

### Strengths
1. VISCON includes a wide range of images across various styles and domains, enhancing the robustness and applicability of the evaluations.
2. Evaluating hallucination from multiple aspects of visual concepts—objects, attributes, and relationships—for a thorough assessment.
3. The paper introduces two metrics (EMD-based and “Evaluate-By-Edit” pipelines) for assessing hallucinations.

### Weaknesses
1. VISCON seems to directly use annotated scene graphs from VisualGenome and PROCTHOR. However, when the original images are stylized into other styles (e.g., line), the information may also change (e.g., the color of objects), which means the annotations should be adjusted accordingly. It should be clearly stated how the authors handled these changes or if they simply used the same annotations as in the original images.
2. In Table 2, there is too little differentiation in performance between models in terms of Earth Mover’s Distance (EMD). Some models (like GPT-4V) even outperform humans in the real-world original column of Table 2. However, GPT-4V still has many hallucination issues [1], which suggests this metric may not adequately capture the true performance gap between different models.
3. In lines 358-360 of the paper, the authors mention that there are some inconclusive queries in edit distances, though they believe these cases are rare and that edit distance still provides a reliable lower bound for estimating hallucination. This conclusion would benefit from further validation through qualitative or quantitative results to demonstrate the robustness of their metric.

### Questions
Please kindly refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
VISCON is a benchmark framework designed to evaluate vision hallucinations in Large Vision-Language Models (LVLMs) by assessing their consistency in generating text aligned with images. It includes a diverse dataset and two innovative pipelines: an Earth Mover’s Distance (EMD)-based method for distributional similarity and an "Evaluate-By-Edit" approach to gauge response alignment with annotated visual concepts. Extensive experiments on six LVLMs show that VISCON offers insights into hallucination factors, such as domain shifts and visual complexity, while providing results that better align with human evaluation than previous metrics.

### Strengths
1. **Comprehensive Evaluation Framework**: VISCON introduces a structured evaluation framework that includes diverse image styles and evaluates a broad range of visual concepts (objects, attributes, and relationships), enhancing its utility in analyzing vision hallucinations comprehensively.
2. **Innovative Metrics**: The Earth Mover's Distance-based pipeline and "Evaluate-By-Edit" method provide novel approaches to measure concept consistency, making VISCON more robust to vocabulary shifts and complex visual relationships, which are limitations in previous hallucination metrics.
3. **Alignment with Human Evaluation**: Extensive experiments reveal that VISCON aligns more closely with human preferences compared to established metrics, demonstrating its relevance and potential for real-world application.

### Weaknesses
1. **Limited Benchmark Validation**: The effectiveness of VISCON’s metrics has not been validated on a broader set of benchmarks, limiting confidence in its general applicability across various datasets. Specifically, the evaluation lacks comparisons with other dense annotation benchmarks that also assess attributes and relationships, which are crucial for establishing the robustness of VISCON's approach.
2. **Lack of Clarity in Pre-defined Rules**: The framework lacks clarity around the pre-defined rules and dataset selection process, particularly in ensuring attribute consistency after stylization. For example, it's unclear how the framework handles cases where stylization might alter the perceived color or material of an object, potentially leading to inconsistencies in the evaluation of attribute hallucinations. This lack of transparency could impact the reliability of results.
3. **Insufficient Benchmark Comparison**: While VISCON emphasizes dense annotation, its benchmark is relatively small and its validation relies primarily on comparisons with POPE and MSCOCO, rather than a broader set of dense annotation benchmarks like Reefknot and it previous work, limiting the robustness of its claims. The absence of comparisons with benchmarks that also focus on detailed visual concept annotations makes it difficult to assess the unique contribution of VISCON.

### Questions
**Metric Validation**: Have VISCON’s metrics, Evaluate-By-EMD and Evaluate-By-Edit been tested on other dense annotation benchmarks?

**Benchmark Consistency**: What criteria were used to ensure the reliability and consistency of annotations across diverse visual domains? For example, how does VISCON handle potential changes in attributes after stylization, and could clarifying these processes enhance the benchmark’s reliability?

**Insufficient Benchmark Comparison and Size**: VISCON’s validation relies primarily on comparisons with POPE and MSCOCO, and its benchmark dataset is relatively small. Would expanding VISCON's benchmark and comparing it with a broader set of dense annotation benchmarks like Reefknot or previous related datasets enhance the robustness?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the evaluation of hallucination in large vision-language models. It proposes an evaluation benchmark and an automatic pipeline to conduct quantitative evaluation. The benchmark comprises of real world images and 3D rendered images, which are further augmented by image stylization. The benchmark includes two modes: an Earth Mover’s Distance and an Edit Distance. The evaluation reveals some interesting phenomenon in LVLMs.

### Strengths
1. The benchmark is curated and annotated comprehensively by considering various image domains, styles, and dense annotations (concepts).
2. The evaluation pipeline provides new perspectives to this venue.
3. The experiments and analysis are sufficient.

### Weaknesses
1. There are more related works that haven’t been discussed and compared, especially those that are also using Visual Genome and are also considering more concepts beyond object categories, e.g., Table 1 in [1].
2. Visual Genome is a widely used dataset to curate benchmark. In this work, the authors involve 3D rendered images into this benchmark. However, the rendered images are all constrained in indoor room scene. This would inevitably restrict the domain of the data, which actually somehow contradict with the main claim of the paper.
3. Since the visual concepts are come from the scene-graph annotation from Visual Genome, as stated in line 101, how do the authors ensure their generated annotation is more comprehensive than other works that also use visual genome scene-graph? Although there are some comparison for this aspect, it is not clear how does it achieved.
4. I wonder would the evaluation framework, especially the Edit Distance version, prefers short captions? For example, the model can be very lazy, simply describing the main objects to avoid making mistakes. Is the framework robust to such cases? I noticed that there are some discussions regarding caption lengths in Figure 5, but it appears to be hard to read without sufficient explanations. It's better to investigate this issue in detail.
5. The EMD is based on an embedding space of a text encoder. However, as discussed by previous works[1], some text encoders, e.g., CLIP text encoder, has significant bias to object categories, while lacking capabilities on telling attributes and relations. Besides, for most text encoders, distinguishing similar visual concepts with small difference is a very challenging task, while such kind of cases are very typical in visual hallucination. The authors should better cover more implementation details and investigations on this aspect, as it may fundamentally invalidate the assumption of EMD.
    - How does the text encoder perform on attributes and relations compared to objects?
    - How well does it distinguish between similar visual concepts?
    - What investigations have you done to ensure the validity of the EMD assumption given these potential limitations?
6. Similarly, in Edit Distance, how to ensure the refined captions are reliable?
7. In general, the method, including EMD and Edit Distance, seems to be proposed out of thin air without enough motivation. Could you give some motivation about the design? Why do you think it is good?

### Questions
Refer to weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel framework, VISCON, which comprises a benchmark dataset and quantitative evaluation pipelines designed to detect hallucinations in the outputs of existing Large Vision-Language Models (LVLMs). Compared to previous benchmarks, such as POPE, VISCON encompasses a wider variety of image styles across multiple visual domains and a broader range of visual concepts. Additionally, it proposes two innovative evaluation pipelines, namely EMD and Evaluate-By-Edit. Extensive experiments validate the efficacy and robustness of VISCON in assessing the hallucination potential of LVLMs.

### Strengths
1. The motivation behind this study is clear, and the method for dataset collection and evaluation is intuitive. 
2. Compared to previous benchmarks, VISCON encompasses a broader range of visual concepts, such as object relations, enabling a more comprehensive evaluation. This is crucial, as prior works often generate numerous false negative samples.
3. The experiments are exhaustive and easy to follow, effectively verifying the robustness of this type of hallucination evaluation.
4. Overall, the paper is well-written and easy to read.

### Weaknesses
1. The evaluation pipeline is quite complex and tedious. For instance, in the case of EMD, the process begins with extracting visual concepts from the detailed caption using GPT-4. Following this, it is necessary to obtain the text embedding for each visual concept before the final evaluation. I am concerned that such a long may hinder its adoption within the community.
2. This type of evaluation can be easily manipulated. For example, if a model is trained to generate short captions, even when given the prompt, "describe the image in detail," it may hallucinate less than a model that generates longer captions. Consequently, the performance of such a model might be overestimated.
3. I am unable to find detailed statistics about the evaluation dataset constructed by this paper. Additionally, there is a lack of information regarding the detailed procedure for constructing the evaluation dataset, including aspects like annotation and sanity checks.

### Questions
See weakness

### Soundness
3

### Presentation
4

### Contribution
3
