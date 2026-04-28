# Babel-ImageNet: Massively Multilingual Evaluation of Vision-and-Language Representations

- Decision: Reject
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Vision-and-language (VL) models with separate encoders for each modality (e.g., CLIP) have become the go-to models for zero-shot image classification and image-text retrieval. 
They are, however, mostly evaluated in English as multilingual benchmarks are limited in availability.
We introduce Babel-ImageNet, a massively multilingual benchmark that offers (partial) translations of ImageNet labels to 100 languages, built without machine translation or manual annotation. We instead automatically obtain reliable translations by linking them -- via shared WordNet synsets -- to BabelNet, a massively multilingual lexico-semantic network.
We evaluate 11 public multilingual CLIP models on zero-shot image classification (ZS-IC) on our benchmark, demonstrating a significant gap between English ImageNet performance and that of high-resource languages (e.g., German or Chinese), and an even bigger gap for low-resource languages (e.g., Sinhala or Lao). 
Crucially, we show that the models' ZS-IC performance 
highly correlates with their performance in image-text retrieval, validating the use of \bin{} to evaluate multilingual models for the vast majority of languages without gold image-text data.
Finally, we show that the performance of multilingual CLIP can be drastically improved for low-resource languages with parameter-efficient language-specific training. 
We make our code and data publicly available: \url{\repourl}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Babel-ImageNet, a benchmark that translates English ImageNet labels into 92 languages using BabelNet. Furthermore, the paper evaluates eight different publicly available multilingual CLIP models on this benchmark. Experimental results indicate that there is a high correlation between the zero-shot performance of image classification and their performance in image-text retrieval, thereby validating the high quality of Babel-ImageNet.

### Strengths
1) The multilingual ImageNet benchmark, which supports 92 languages, serves as an excellent platform for evaluating multilingual CLIP models, particularly for those languages that are under-resourced.
2) The assessment of eight different multilingual CLIP models also provides valuable insights.

### Weaknesses
My concern is about the simplicity of the method, which merely translates English ImageNet labels using BabelNet. While the resulting benchmark proves useful, the method's contribution appears to be limited.

### Questions
Have you considered using GPT-4/ChatGPT to prompt the model to translate English ImageNet labels? Perhaps combining GPT-4/ChatGPT with WordNet could yield better results.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a robust and machine-translation-free method to create non-English labels for the ImageNet-1k dataset in 92 different languages. When used to evaluate VL models, the new Babel-ImageNet dataset showed score correlated with retrieval performance on multilingual image-text datasets. Finally the paper used the dataset to evaluate models with parameter efficient tuning toward multilingual capability.

### Strengths
- The proposed translation method is robust and the claimed error rate from manual inspection is low.
- The translation covers 92 languages, including many medium and low resource languages.
- When evaluating multilingual models, the performance on Babel-ImageNet correlates well with the text to image retrieval performance on multilingual image-text datasets, suggesting the usefulness of this dataset as an alternative evaluation method for multilingual models

### Weaknesses
From a significance and usefulness perspective, the unique advantage of this dataset over the multilingual image-text datasets for model evaluation is unclear. It is not surprising that the performance of models on multilingual ImageNet classification is correlated with multilingual text to image retrieval. My concern is that Babel-ImageNet might not be as good as the multilingual image-text datasets as the former contains much less detailed description for the image, and that other image-text datasets support image-to-text retrieval as well for which Babel-ImageNet could not cover.

The section 6 discussion might be a good opportunity to set up such a comparison if the models there could be evaluated on the multilingual image-text datasets as well. If the authors can show that Babel-ImageNet better reflects the model quality improvement, that would make a strong argument.

### Questions
Can you show some cases where Babel-ImageNet has wrong non-English labels? Are there any systematic errors?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Zero-shot image classification and image-text retrieval evaluation primarily focusses on English only. Curation of high quality evaluation datasets in other languages is expensive and time consuming. This paper proposes e Babel-ImageNet, a massively multilingual
benchmark that offers partial translations of 1000 ImageNet labels to 92 languages, built without resorting to machine translation or requiring manual annotation. It leverages the connection between ImageNet classes, which are derived from WordNet synsets, and BabelNet, a massively multilingual lexico-semantic network, also (in part) derived from WordNet. 

Babel-ImageNet thus allows us to evaluate models in languages not covered by other evaluation datasets and it additionally expands the retrieval-focused evaluation with the zero-shot image classification task in languages included in the established datasets.

The paper proposes a computationally efficient approach for improving multilingual CLIP models for low-resource languages. This modular language specialization approach yields large performance gains (>20% for some of the low-resource languages).

### Strengths
This paper introduces an extensive image-text evaluation benchmark on a large set of languages which motivates research in the largely unexplored multilingual VL representation learning space. Also, the technique is free from any machine translation or similar techniques that can introduce errors in the evaluation data. This makes it more robust and suitable for adoption. This evaluation corpus should be extremely helpful for furthering research in this area.

### Weaknesses
None.

### Questions
None.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The purpose of this work is to introduce Babel-ImageNet, a multilingual benchmark for vision-and-language (VL) models that is designed to evaluate their performance in zero-shot image classification and image-text retrieval across several languages. Babel-ImageNet provides translations of (up to) 1000 ImageNet labels in 92 languages without relying on machine translation or manual annotation, just on a multilingual knowledge base. The study evaluates several multilingual CLIP models on the proposed benchmark and shows significant performance disparities, with low-resource languages showing (as expected) the greatest performance gap. Additionally, the paper presents an approach for enhancing the performance of multilingual CLIP models in those low-resource languages.

### Strengths
- The study goes beyond traditional monolingual evaluation, offering a comprehensive analysis of 8 multilingual CLIP models across 92 languages. 
- The paper is well-motivated and, in general, clear enough to follow through;
- It provides a practical and parameter-efficient approach that significantly improves model performance, making multilingual models more relevant and accessible for underrepresented linguistic communities;
- The dataset/benchmark contribution targets a relevant issue (the overall imbalance between high and low-resourced languages);
- The authors already provide the code for reproducibility purposes;

### Weaknesses
 - BabelNet reliance. This work relies entirely on BabelNet and assumes that the mapping between WordNet and other resources is high quality. However, BabelNet is automated and has a known percentage of error, potentially affecting the label mapping [1];
- Using WordNet synsets for translations may introduce limitations, as not all concepts or words have direct equivalents in WordNet or BabelNet, potentially impacting the completeness of translations for some languages.
- While the paper emphasizes the creation of the benchmark and model evaluation, it could benefit from a deeper analysis of why certain languages perform poorly according to the chosen metrics and explore potential solutions to address these disparities;
- Considering that the paper belongs to the "datasets and benchmarks" area, the methodology employed (mapping from ImageNet to WordNet and then to BabelNet) is expectedly straightforward.  However, I think there's also some weakness in the data cleaning and validation since the obtained multilingual data is used to evaluate models, but those same benchmarks cannot be used to assess the quality of the data itself;
- The paper's process of removing words with identical English counterparts in the class label translation and cleaning may not be fully justified, as there can be legitimate shared words between the English and language-specific vocabulary;

### Questions
- There's a missing reference to another text-image dataset produced by *manual* annotation over BabelNet synsets [1]. In general, I'm curious about the possible usage of this dataset as a proxy to evaluate at least the Babel-ImageNet methodology part that performs prompt translation. I'd like to kindly ask the authors what they think about it or if they have alternative ideas toward strengthening data validation, which I think is the strongest weakness in this current version of the manuscript;
- Not a direct weakness, so I'm listing it here: multiple usages of the verb "demonstrate" (e.g., "we demonstrate that OpenCLIP performance strongly correlates with the distribution of languages in LAION5B" ). Personally, given the empirical nature of this work, I wouldn't suggest using such a theoretical-related term;

Given the doubts about the data validation, I'm starting the discussion period leaning toward rejection. However, I'm open to changing my assessment in light of the rebuttal discussions and the reviews of my colleagues.

[1] Fatality Killed the Cat or: BabelPic, a Multimodal Dataset for Non-Concrete Concepts. Agostina Calabrese, Michele Bevilacqua, Roberto Navigli. ACL 2020

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
