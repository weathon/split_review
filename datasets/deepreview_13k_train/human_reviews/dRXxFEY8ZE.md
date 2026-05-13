# $\texttt{BirdSet}$: A Large-Scale Dataset for Audio Classification in Avian Bioacoustics

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Deep learning (DL) has greatly advanced audio classification, yet the field is limited by the scarcity of large-scale benchmark datasets that have propelled progress in other domains. While AudioSet aims to bridge this gap as a universal-domain dataset, its restricted accessibility and lack of diverse real-world evaluation use cases challenge its role as the primary resource. Therefore, we introduce \texttt{BirdSet}, a large-scale benchmark dataset for audio classification focusing on avian bioacoustics. \texttt{BirdSet} surpasses AudioSet with over 6,800 recording hours~($\uparrow\!17\%$) from nearly 10,000 classes~($\uparrow\!18\times$) for training and more than 400 hours~($\uparrow\!7\times$) across eight strongly labeled evaluation datasets. It serves as a versatile resource for use cases such as multi-label classification, covariate shift or self-supervised learning. We benchmark six well-known DL models in multi-label classification across three distinct training scenarios and outline further evaluation use cases in audio classification. We host our dataset on Hugging Face for easy accessibility and offer an extensive codebase to reproduce our results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is an excellent,  comprehensive and carefully curated dataset of bird sounds. The paper also provides an excellent review of the existing literature, and provides baseline code showing use of the data. The benchmark testing tasks are a bit simple, but demonstrate the breadth of the dataset.

### Strengths
Careful curation of the dataset - types of collections, varying types of birdcalls from same species; includes both soundscapes, and individual recordings; comparisons with other datasets.
Inclusion of benchmark code for future researchers to use as a baseline.
Permissive licensing
A large scale project

### Weaknesses
too many uncommon acronyms which require a reader to keep going back and forth - such shortening of the length was unnecessary. The acronyms are used in the figures as well. Figures and captions are supposed to stand on their own.

### Questions
Please rewrite with clarity and minimizing acronyms.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents BirdSet, a new large-scale benchmark dataset specifically for multi-label audio classification within avian bioacoustics. It significantly extends the scope of existing audio datasets by including approximately 10,000 classes, covering over 6,800 hours of training data, and incorporating 400 hours across eight distinct test datasets. BirdSet addresses several real-world machine learning challenges, such as covariate shift, label noise, and task shift, providing a unique resource for evaluating model robustness in audio classification under diverse conditions. The benchmark includes evaluations of six prominent deep learning models across three different training approaches: training on the full BirdSet, training on a subset containing only classes relevant to the downstream tasks, and training on a small subset for each downstream dataset individually.

Additionally, the authors facilitate accessibility by hosting BirdSet on Hugging Face, where they provide Python code to load the data. They also offer scripts for reproducing the experiments in the paper​.

### Strengths
1. Originality

BirdSet represents a novel contribution to multi-label audio classification. With close to 10,000 classes BirdSet provides a benchmark to develop scalable methods capable of handling extreme class diversity with large imbalance. BirdSet also addresses critical machine learning challenges such as covariate shift, where the testing distribution diverges from the training distribution reflecting real-world environmental shifts in field data.


2. Clarity

The paper is clear and well-organized, with a logical presentation of BirdSet’s structure, design choices, and challenges. The descriptions of covariate and domain shifts, as well as the evaluation protocols and training setups, are concise and well-articulated.


3. Significance

BirdSet can enable the development of new self-supervised learning, active learning, and few-shot learning approaches that are resilient to covariate and domain shifts—capabilities that are increasingly relevant for practical deployment of models in real-world applications. Moreover, its emphasis on multi-label classification reflects real-world scenarios in bioacoustics and similar domains, driving advancements that can translate to other fields beyond audio.


In summary, BirdSet is highly original, well-curated, and impactful dataset that serves as both a resource and a benchmark. It encourages tackling challenges related to robustness to distribution shifts, and multi-label classification, with methods that can be developed that extend across deep learning domains more broadly.

### Weaknesses
I didn’t find any weaknesses in this paper.

### Questions
I see significant potential in BirdSet, and I wonder if it would be feasible to define few-shot tasks within the downstream tasks to address few-shot multi-label classification?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes BirdSet, which is a dataset, or more specifically, a collection of 11 different sub-datasets. BirdSet attempts to unify 
avian bioacoustic evaluation on focal and soundscape recordings under one roof, providing a large, unified, accessible test bed for testing audio classification approaches.

### Strengths
1. Well written and easy to read.
2. Thoroughly explains the challenges experienced not only in avian bioacoustics, such as covariate shift and mismatch in focal and soundscape recordings, but also in curating, and developing a dataset of such a size and scale. 
3. The pain points addressed in the paper are very real: poor availability and accessibility of AudioSet, lack of a unified benchmark suite for evaluating segment and event-based bioacoustics tasks, and mismatch between train and test time for avian bioacoustics, are all pressing challenges. 
4. A good variety of baseline models were evaluated.

### Weaknesses
To me, the paper, in several places, tries to pose BirdSet as a replacement for AudioSet and that it should be the exemplary benchmark for evaluating audio classification models, with statements such as "Avian bioacoustics exemplifies challenges in audio classification...", and how curated datasets like AudioSet and ESC-50 do not represent real-world complexities. Pain points mentioned w.r.t. AudioSet are all very real, but AudioSet is a much broader dataset than BirdSet. Several people, in industry and academia have found AudioSet useful: a blanket statement saying AudioSet is not useful in real-world scenarios is plain wrong.
Some statements straight up downplay AudioSet: for instance, line 37-38: where AudioSet poses "... concerns regarding transferability to real-world environmental domains". Whereas the paper cited simply shows that AudioSet pretrained models perform "well enough": of course models trained on in-domain bioacoustics data will fare better for bioacoustic evaluation!

Also, as per Table 3, AST and EAT models, which are pretrained on AudioSet, seem to perform quite well in the DT setting (cross-domain transfer setting) versus their LT and MT counterparts. For EAT, DT performance matches MT and outperforms LT scenarios.

BirdSet will be a tremendous contribution to the fields of audio classification and avian bioacoustics, I have no doubt, but I think the current language of the paper comes off as "posturing" a tad bit too much.

### Questions
In the context of how the paper is currently phrased, more direct comparisons, for instance, linear evaluation on cross-domain data between models trained on BirdSet and AudioSet on a variety of downstream tasks, spanning bioacoustics and other audio domains would be needed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces BirdSet, a large-scale audio classification dataset for avian bioacoustics, with around 520,000 recordings from nearly 10,000 bird species. It includes over 6,800 hours of training data and 400 hours of evaluation data from diverse regions. The dataset supports tasks such as multi-label classification and self-supervised learning, with standardized training and evaluation protocols. A comprehensive literature review identifies key challenges in bioacoustics and provides research guidelines. The paper benchmarks multiple deep learning models and offers a codebase for reproducibility.

### Strengths
1. The introduction of *BirdSet* fills a notable gap in audio classification by providing a large-scale, domain-specific dataset for avian bioacoustics.
2. The paper is well-structured and clearly articulates the challenges in avian bioacoustics and audio classification more broadly. 
3. The paper provides a thorough empirical evaluation using six well-known deep learning models, covering various training scenarios, including large-scale training and fine-tuning.

### Weaknesses
1. The literature review in Section 2 is quite extensive, occupying a significant portion of the main paper. While the analysis is comprehensive, it might be more beneficial to allocate more space to the dataset description and details, rather than using five pages for the related work. Specifically, the current balance seems to prioritize a broad overview of the field over a deep dive into the specifics of the dataset itself, which is the core contribution of the paper. For example, details on the recording conditions, the variability in signal-to-noise ratio across different recordings, and the distribution of recording lengths for each species could be more thoroughly discussed.

2. The results focus mainly on the multi-label classification benchmark, with limited exploration of other use cases. Given the dataset’s availability of precise event timestamps, it would be valuable to include benchmarks for sound event detection, which is a crucial task in bioacoustics. Additionally, providing results for other mentioned use cases such as few-shot learning, domain adaptation, or self-supervised learning would strengthen the paper and demonstrate the versatility of the dataset. The current evaluation is somewhat narrow, focusing primarily on a single task, which limits the assessment of the dataset's full potential.

### Questions
Please refer to the weaknesses above for the questions.

### Soundness
4

### Presentation
4

### Contribution
4
