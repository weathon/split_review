# Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
How do multi-modal generative models describe images of recent historical events and figures, whose legacies may be nuanced, multifaceted, or contested? This task necessitates not only accurate visual recognition, but also socio-cultural knowledge and cross-modal reasoning.  To address this evaluation challenge, we introduce Century -- a novel dataset of sensitive historical images. This dataset consists of 1,500 images from recent history, created through an automated method combining knowledge graphs and language models with quality and diversity criteria created from the practices of museums and digital archives. We demonstrate through automated and human evaluation that this method produces a set of images that depict events and figures that are diverse across topics and represents all regions of the world.
We additionally propose an evaluation framework for evaluating the historical contextualisation capabilities along dimensions of accuracy, thoroughness, and objectivity. We demonstrate this approach by using Century to evaluate four foundation models, scoring performance using both automated and human evaluation. We find that historical contextualisation of sensitive images poses a significant challenge for modern multi-modal foundation models, and offer practical recommendations for how developers can use Century to evaluate improvements to models and applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper is about “Century” a dataset and framework designed to evaluate the ability of multi-modal models to contextualize sensitive historical images accurately, thoroughly, and objectively. To build the dataset, images were sourced with knowledge graphs, language models, and they were processed according to museum practices, considering especially recent historical events, figures, and locations, with images that may hold socio-cultural significance. The idea is to address the representation of historical nuance in generative AI and proposes an evaluation protocol for assessing models on tasks requiring socio-cultural and historical contextualization. After the construction of the Century dataset, it is tested with recent private foundation models. The paper reports that these models have difficulties addressing the complexity of historical contextualization.

### Strengths
- The proposed interdisciplinary dataset focus on historical contextualization and represent a valuable contribution to the field, addressing a crucial gap in existing evaluation methodologies.

- The work should be well reproducible with the released dataset, search terms, and evaluation details. Every part of the work is well detailed and released. Authors have put significant effort into this.

- The paper is well written, well structured and all parts, also detailed in the appendix, are well informative.

### Weaknesses
 - the use of Wikipedia raises concerns about biases inherent of the platform. Wikipedia’s coverage of historical events is not uniform across regions or cultures, potentially leading to an overrepresentation of certain perspectives. Specifically, the reliance on Wikipedia's structured data, such as knowledge graphs, might inadvertently amplify existing biases present in the platform's content and editorial processes. This could skew the dataset towards more well-documented and Western-centric historical narratives, while marginalizing or misrepresenting the histories of less-represented regions. Anyway, the limitation is acknowledged and is anyway a first step into the right direction. 

 - the definition of "sensitive" is based on interpretations from museums and archives, which seems a good starting point. However, I wonder about whose perspectives are considered "sensitive" and who gets to define them. The current approach risks imposing a dominant cultural lens on what constitutes 'sensitivity,' potentially overlooking or misinterpreting the nuances of sensitivity as perceived by the communities directly affected by the historical events depicted. Maybe some input from the communities whose histories are represented in the images should be considered, but I understand the difficulty of doing that.

### Questions
- Since the release of new LLMs are very frequent, I wonder what could be done to further automatise the evaluation on the dataset. 

- I believe the dataset could potentially be misused to train models that generate biased or harmful content related to sensitive historical events. What do you think about this aspect?

- Could the limited representation of certain communities in the dataset be harmful for training of future models based on this dataset? I'm not sure about its inclusiveness and how to not perpetuate existing biases.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new dataset for evaluating multimodal models’ capability to describe historical and sensitive images in terms of several criteria, including factual errors and due weight. The images in the dataset are carefully chosen so that they are sensitive, controversial, and/or commemorative. The evaluation protocol includes automated evaluation and human evaluation. The paper gives some recommendations for evaluating models with the dataset.

### Strengths
I think this evaluation is important conceptually and in the application level. One expectation to a foundation model may be to generate unbiased (or not one-sided) descriptions of sensitive events, and the proposed dataset can serve as a benchmark in this regard. 

Also, the paper recommends that human evaluation is still critical even though LLMs can evaluate a target model, which is fair. According to Table 3, foundation models and humans do not look consistent, and evaluation solely by the automated protocol seems insufficient. The paper seems faithful to this evaluation.

### Weaknesses
I think the dataset is useful for the application level, while it’s not clear from the technical level what aspects of a model it tries to evaluate. The proposed evaluation task seems to require (1) identification of the event, person, etc. depicted in the image, (2) associating the identified entities with the corresponding historical event (so that it can give a contextualized description), and (3) describing the image in a fair and objective way. I think (1) involves the perceptual capability of a model, while (2) and perhaps (3) involves the knowledge the model has. (3) may also involve the criterion of goodness of generated description used in the training. The proposed protocol evaluates a model without being aware of these different aspects (the paper partly mentions this point in Section 5.1), which makes the interpretation of the result extremely hard. I understand that as the foundation model users rarely have knowledge about how the model is trained, it’s not straightforward to isolate these different aspects. However, without some ways to interpret the results (as described in Section 5.1 as a future application of the dataset), insights that the dataset will provide may be limited. 

The paper is often hard to read. I don’t see what the dataset offers (does it contain only images or some example descriptions of events?) in the main paper.

### Questions
I would like to see some discussion on the first point in the weaknesses.

### Soundness
3

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
3

### Summary
This paper introduces Century, a dataset with 1,500 images of sensitive historical images (including a new method to identify images like those in the dataset). Along with Century, the authors propose an evaluation framework to measure how well models do at “historical contextualization.”

### Strengths
S1. The authors tackle a problem that many researchers shy away from or do not even consider, as historical contextualization is a complex task and has no objective ground truth. This paper is a thorough, high-quality effort to 1) help understand our models through this lens, and 2) highlight the importance of historical contextualization abilities in large vision-language models.

S2. The paper is very well-written; the methods and results are presented in a straightforward manner and thoroughly-discussed.

S3. Century is a diverse dataset with a decent balance across regions, content, and image type. The dataset can always be more diverse and balanced along these axes, but it is a respectable collection for evaluation given that its limitations are acknowledged.

### Weaknesses
W1. The evaluations are done on closed-source models, which are helpful in illuminating their capabilities given that we don’t know much about their data or architecture. However, it would be incredibly useful to benchmark open-source VLMs alongside them, as the associations with training data, architecture, etc. and historical contextualization abilities can help the community to identify how to score better on this benchmark. Specifically, the lack of open-source model evaluations makes it difficult to isolate the impact of specific architectural choices or pre-training datasets on the observed performance. For example, are transformer-based models inherently better at this task, or is it a function of the specific data they were trained on? Without open-source benchmarks, it's hard to determine the underlying factors.

W2. I would love to see a more thorough limitations section. While the points covered are valid and important, there is so much nuance to the dataset, evaluation metrics, etc. The community would benefit from a paper that not only presented a useful dataset and benchmark for historical contextualization, but thoroughly (to a best approximation) enumerated the pitfalls one could fall into when maximizing performance on this benchmark, and described the demographic and geographic distribution of human evaluators. For instance, the paper should discuss potential biases introduced by the selection of images, the subjectivity inherent in the evaluation process, and the limitations of using a single set of human evaluators. The lack of discussion on how the evaluation process might be influenced by the evaluators' own cultural backgrounds and historical knowledge is a significant oversight.

W3. Some of the figures seem to be missing legends, or at least are not clear enough in what the colors mean (Figures 6 and 11). I assume the x-axis is labeled 1-5, but the colors and lack of x-axis label are a bit confusing.

### Questions
Q1. Is it possible to recover the geographic and demographic distribution of the human evaluators? That data seems especially important to consider for historical contextualization.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present Century, a dataset of 1,500 sensitive historical images curated from recent history. It is generated using an automated process that combines knowledge graphs and language models, guided by criteria from museum and digital archive practices to ensure a balanced representation of global events and figures. The dataset is validated through both automated and human evaluations, demonstrating its diversity and comprehensiveness. Additionally, the authors introduce an evaluation framework to measure historical contextualization along dimensions of accuracy, thoroughness, and objectivity, applying it to assess the performance of four foundational models, with both automated metrics and human feedback supporting the results.

### Strengths
The paper is well-articulated and clear, enhancing readability and accessibility.

Addressing sensitive historical images is a compelling topic with high relevance, and the proposed framework is both innovative and thoughtfully executed.

The methodology for identifying and curating sensitive historical images, integrating knowledge graphs with language models, provides a scalable approach with potential research applications across history and AI.

The Century dataset could serve as a valuable resource for researchers working on similar challenges, including those focused on historical image representation, automated content generation, and bias mitigation.

### Weaknesses
I'm a bit concerned about the dataset scale. At 1,500 images, the dataset may be too small to train deep learning models directly, potentially limiting its use in large-scale AI training scenarios. A dataset size of more than 10K images would be a good estimation for training models. 

Furthermore, as a new framework, the effectiveness of Century could benefit from comparative analysis with existing datasets or similar historical image frameworks. This would provide a clearer benchmark of its strengths and limitations. If there are not closer frameworks, some related research might also help in comparison, such as the following papers for your reference: 

Wu, Mingfang, et al. "Automated metadata annotation: What is and is not possible with machine learning." Data Intelligence 5.1 (2023): 122-138.

Wadhawan, Rohan, et al. "ConTextual: Evaluating Context-Sensitive Text-Rich Visual Reasoning in Large Multimodal Models." arXiv preprint arXiv:2401.13311 (2024).

Finally, the authors candidly discuss certain biases, particularly concerning dataset distribution and generative labeling. These limitations could impact future applications, and additional mitigative strategies would strengthen the framework's applicability.

Minor: It is unclear to me whether a dataset-centric paper with a focus on historical content aligns fully with ICLR’s primary scope, which typically emphasizes innovations in machine learning.

### Questions
Have the authors conducted any formal bias testing within the dataset? Is it possible to elaborate on potential approaches the authors have considered for addressing these biases. Understanding how these biases may clarify the power of the dataset, the impact of model outcomes, and outlining potential mitigation strategies, would further enhance the dataset’s robustness for future research.

Have the authors considered ways to expand the dataset or if they envision it being used primarily for evaluation rather than training.

### Soundness
3

### Presentation
3

### Contribution
3
