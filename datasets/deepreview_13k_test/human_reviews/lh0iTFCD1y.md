# LUMA: A Benchmark Dataset for Learning from Uncertain and Multimodal Data

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Multimodal Deep Learning enhances decision-making by integrating diverse information sources, such as texts, images, audio, and videos. To develop trustworthy multimodal approaches, it is essential to understand how uncertainty impacts these models. We propose  LUMA, a unique benchmark dataset, featuring audio, image, and textual data from 50 classes, for learning from uncertain and multimodal data. It extends the well-known CIFAR 10/100 dataset with audio samples extracted from three audio corpora, and text data generated using the Gemma-7B Large Language Model (LLM). The LUMA dataset enables the controlled injection of varying types and degrees of uncertainty to  achieve and tailor specific experiments and benchmarking initiatives. LUMA is also available as a Python package including the functions for generating multiple variants of the dataset with controlling the diversity of the data, the amount of noise for each modality, and adding out-of-distribution samples. A baseline pre-trained model is also provided alongside three uncertainty quantification methods: Monte-Carlo Dropout, Deep Ensemble, and Reliable Conflictive Multi-View Learning. This comprehensive dataset and its benchmarking tools are intended to promote and support the development, evaluation, and benchmarking of trustworthy and robust multimodal deep learning approaches. We anticipate that the LUMA dataset will help the ICLR community to design more trustworthy and robust machine learning approaches for safety critical applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper uses CIFAR image data, generates text and spoken word labels for these using a well described process, and creates a multimodal data set. It then describes software controlled processes and software to add noise to each of the three modalities. The datasets for the three modalities, noise tools, and benchmark code is made available.

### Strengths
Well known datasets from vision, text and audio are combined to create a multimodal dataset which contains the image, text and spoken word description of the image. There is a systematic process to add noise to each modality. Code is made available to add this noise.  The dataset for each modality is evaluated separately using baseline classifier models.Gender, Cultural and Racial Bias in labels are carefully avoided.

### Weaknesses
It is totally unclear how much use this dataset for a practical multimodal learning task. Also, this level of image with short caption or spoken word descriptions are largely bypassed by existing multimodal models.  Having spoken word labels (with varying amounts of noise) to low quality CIFAR images (with varying amounts of noise) does not appear to be very useful.

### Questions
The dataset is one-way in the sense that the images get you text and speech labels; and then noise is added. I cannot imagine how this would be used beyond relatively small academic exercises.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces a multimodal benchmark, integrating paired data for image, audio, and text to support the development of more reliable multimodal approaches. The image data includes samples from both CIFAR and generated data from diffusion models. For audio data, it features recordings of individuals pronouncing the corresponding class labels. For text data, large language models (LLMs) generate explanations for the associated content. By utilizing and fusing information from all modalities, the benchmark enables predictive analysis while controlling for data diversity, modality-specific noise, and the inclusion of out-of-distribution samples. Finally, it provides results using a pre-trained model with three uncertainty quantification methods: Monte-Carlo Dropout, Deep Ensembles, and RCML. This work paves the way to build a more trustworthy and robust model.

### Strengths
(1) Careful Data Collection Design: The data collection process for image, audio, and text modalities leverages generative models to augment existing data while incorporating mechanisms to ensure the quality of the benchmark dataset. This aligned, multimodal dataset for classification serves as a valuable resource for a wide range of research applications.

(2) Open-Source Python Package: This work includes a robust, open-source Python package, enabling other researchers to easily build upon and extend its functionalities. Typically, it has functions to generate multiple variants of the dataset with controlling the diversity, the amount of noise for each modality, and adding out-of-distribution samples.

### Weaknesses
(1) Simplistic Task Design: The classification tasks in this benchmark are relatively simple and may not align with the complexities of recent multimodal research. Although the work emphasizes uncertainty analysis rather than state-of-the-art multimodal models, the current focus of the multimodal research community is on more challenging tasks that better represent real-world applications. As a result, this benchmark may have limited contributions to the fields of trustworthy and robust machine learning. For instance, contemporary audio and vision models likely achieve very high accuracy on the benchmark’s classification tasks.

(2) Limited Depth of Analysis: The benchmark relies on relatively small pre-trained models, whereas larger and more powerful models might yield different insights and conclusions. As a benchmark paper, a more comprehensive analysis of various baselines, noise-handling methods, and technical details for uncertainty estimation would strengthen the work. Currently, it primarily explores late fusion-based multimodal methods with fixed pre-trained models, which narrows the scope of its conclusions and limits potential findings in robust machine learning. There are still one page space that more analysis results should be filled in. More analysis like why only RCML actually consistently raises the estimates under increased label noise and why RCML is diffferent from DE ad MCD can be further discussed.

### Questions
Diffusion models and LLMs for image and text generation, were used during the benchmark’s data collection. However, Gemma-7B, a relatively weak model, was employed in this process. It would be insightful to understand the potential impact of using a more powerful model, such as GPT-4o, to conduct the generation and whether there is a huge difference in data quality. Additionally, further analysis of the generated data could enhance the benchmark’s robustness. Currently, only audio data has dedicated visualization results in the paper. It would be beneficial to see more visualization and analysis for the text and image modalities as well.

Moreover, more additional information and details about the evaluation metric, uncertainty measurement setting, collected data examples can be introduced in the main section of the paper to help people understand more easily.

### Soundness
3

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
4

### Summary
The paper presents LUMA, a multimodal dataset designed explicitly for benchmarking uncertainty in multimodal learning algorithms featuring audio, image, and text data. The author sources images from CIFAR 10/100, audio samples (consisting of label information) from diverse labeled speech corpora such as LibriSpeech, Spoken Wikipedia, and Common Voice, and text generated synthetically via Gemma-7B Instruct LLM. The authors also provide a Python package to customize uncertainty levels through controlled noise generation across all the modalities. Additionally, the paper introduces baseline models incorporating Monte Carlo Dropout, Deep Ensemble, and Reliable Conflictive Multi-View Learning.

### Strengths
1. This paper introduces a novel benchmark, LUMA, designed to measure uncertainty across multiple modalities: audio, image, and text. Additionally, the LUMA dataset allows for controlled manipulation of different types and levels of uncertainty.

2. The authors provide baseline pre-trained models along with three uncertainty quantification methods—Monte Carlo Dropout, Deep Ensemble, and Reliable Conflictive Multi-View Learning—offering a solid starting point for benchmarking.

### Weaknesses
1. The choice of data sources for specific modalities is unclear. For instance, it’s not evident why CIFAR-10/100 was used for images rather than ImageNet, which includes 1,000 labels and could provide greater diversity for benchmarking. I suggest that the authors clarify this decision in the main paper.

2. To convert text labels into audio, the authors propose a complex approach involving mapping labels to utterance transcriptions and segmenting using forced alignment. However, a simpler alternative might be to synthesize text labels directly with state-of-the-art Text-To-Speech models. Did the authors compare their approach with synthetic audio generation as described in Section 3.2?

3. The paper is difficult to follow. For example, Section 4 covers quantitative results of various baselines on LUMA but combines details on uncertainty algorithms, results, and analysis without clear distinctions, making it challenging to understand. Additionally, critical information on model architecture and uncertainty algorithms seems to be either buried in the Appendix or missing. Clearer organization in the main text would improve readability.

4. The paper lacks error analysis and qualitative results. If these are included in the Appendix, I suggest mentioning them in the main paper for accessibility.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper attempts to build a benchmark dataset for Multimodal Uncertainty Quantification (MUQ). It creates the LUMA dataset which contains multimodal data. At the same time, it builds baseline models on this new dataset.

### Strengths
Overall, the paper is clearly written. However, there are some limitations.

### Weaknesses
1. This paper lacks practical applications in real-world scenarios. Both the data and the noise are in a simulated environment, which is very different from real-world applications. At the same time, it collects images from CIFAR, audio using keyword spotting techniques, and text using LLM to generate short descriptions. However, I cannot imagine that there is multimodal data containing these types of data in real-world scenarios.
2. All sample noise and label noise are simulated, but no real noisy data is used. Therefore, this dataset is far from real-world scenarios.
3. Section 4 only covers three baselines: MCD, DE, and RCML. Please cover more approaches.
4. This paper contains some minor grammatical errors. Please proofread this article:
a)	described in the section 3.4.1, => Section 
b)	73 Additional recordings of => 73 additional
c)	Please abbreviate words only once.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
