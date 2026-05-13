# EasyTPP: Towards Open Benchmarking Temporal Point Processes

- Decision: Accept
- Scores: 1, 3, 3, 8

## Abstract
Continuous-time event sequences play a vital role in real-world domains such as healthcare, finance, online shopping, social networks, and so on. To model such data, temporal point processes (TPPs) have emerged as the most natural and competitive models, making a significant impact in both academic and application communities. Despite the emergence of many powerful models in recent years, there hasn't been a central benchmark for these models and future research endeavors. This lack of standardization impedes researchers and practitioners from comparing methods and reproducing results, potentially slowing down progress in this field. 
In this paper, we present EasyTPP, the first central repository of research assets (e.g., data, models, evaluation programs, documentations) in the area of event sequence modeling. 
Our EasyTPP makes several unique contributions to this area: 
a unified interface of using existing datasets and adding new datasets; 
a wide range of evaluation programs that are easy to use and extend as well as facilitate reproducible research; 
implementations of popular neural TPPs, together with a rich library of modules by composing which one could quickly build complex models.
We will actively maintain this benchmark and welcome contributions from other researchers and practitioners. 
Our benchmark will help promote reproducible research in this field, thus accelerating research progress as well as making more significant real-world impacts.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors contribute the EasyTPP package for temporal point processes (TPPs). TPPs have been of increasing interest to the machine learning community in recent years, with many deep learning-based TPP models being able to outperform classic parametric TPP models in prediction tasks. There have not been many software packages implementing many different TPP models, which has made it difficult to compare and evaluate different models across standardized benchmark data sets and evaluation metrics. The EasyTPP package implements many recent TPP models and can be used with either PyTorch or TensorFlow. The authors utilize the package to benchmark these TPP models across a variety of data sets and prediction tasks.

*After author rebuttal:* I have read through the other reviews and author rebuttal and still strongly support the paper. I further expand on my reasoning in a reply to the author comment titled "Technical Contribution and Broader Impact."

### Strengths
- Addresses a major need in the machine learning community interested in TPPs--the lack of a standardized benchmarking tool. Most researchers are piecing together implementations from other papers in order to make comparisons. Existing software packages, such as PoPPy are out of date and not maintained. The proposed EasyTPP package could fill a major need for the community.
- Implements a comprehensive list of models and evaluation metrics, together with several representative data sets.
- The authors perform a thorough comparison of existing models using their EasyTPP package, which should also be useful to researchers in the area.

### Weaknesses
 - The authors compare against the classical Multivariate Hawkes Process (MHP) but don't specify what type of kernel they use (I assume exponential) or structure of the excitation matrix. It would be useful to know the specific parameterization of the MHP, as different choices can lead to vastly different performance. For example, are the excitation matrix parameters shared across event types, or are they independent? The choice of kernel (e.g., exponential, Gaussian, power-law) also significantly impacts the model's behavior and should be explicitly stated.

Minor concerns:
- Some typos, e.g. Multivariate Hakwes Process (MHP)

### Questions
1. Is there an easy way to incorporate marks into your package? From the description in the paper, it seems like you can easily handle different event types through a multivariate TPP, but I don't see any discussion of marks. In many application settings, we can have a feature vector for each event, which can be modeled as a mark.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a software package that abstracts the implementation of several temporal point process models.

### Strengths
1. Good motivation

### Weaknesses
1. Lack of technique contribution
2. Unclear presentation

### Questions
1. This paper lacks technical innovation. I don't think a software-level abstraction is a good fit for ICLR.
2. The description of the system design and interface lacks details.
3. It's unclear what points the authors intend to demonstrate in the experiment section.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To promote reproducible research in this field, this article proposes an open and central benchmark for point process research. The benchmark provides a complete pipeline and software interface. The effectiveness of this benchmark is demonstrated by the unified comparison of various model results.

### Strengths
1. The most important contribution lies in providing a simple and standardized framework to allow users
to apply different TPP models to any datasets, which promotes reproducible research in this field.

### Weaknesses
The main concern is contribution. Considering the quality of the ICLR community, although it is particularly urgent to propose a unified comparison and processing framework for point processes, the contribution is still limited.

### Questions
Would you mind elaborating further on the broader impact this benchmark will have on the community?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an end-to-end benchmarking package for neural temporal point process models. The package contains 6 diverse real-world datasets, 1 synthetic dataset, 8 recent models, and support for both Tensorflow and PyTorch. The paper itself serves as a useful exposition of the field, tasks, types of models, proposed package, and detailed empirical results.

### Strengths
This paper is a welcome contribution to TPP modeling at a timely moment when significant neural point process approaches have been published yet many open questions still remain. The proposed package has all the hallmarks of usefulness:

1) Reproducible workflows via modular API.

2) Diverse models and datasets.

3) Supports top-2 ML languages equally (this is rare among benchmarking frameworks).

4) Open-source repository and datasets.

The paper is overall well-written.

### Weaknesses
There are some presentation/exposition gaps/weaknesses:

1) The accuracy plots would be more useful as tables.

2) The "temporal event sequence" topic is not well-defined.

3) The processing of sequence data is not adequately described.

I elaborate on these weaknesses in questions to the authors.

### Questions
My questions align with the three specific shortcomings I identified:

1) For reproducibility purposes, it would be useful to the community to know the exact accuracy values (and confidence bounds) from the various methods. Therefore in my opinion all plots showing empirical results should be replaced with tables. Is this possible in the camera-ready version?

2) I may have missed this in my reading, but in Fig 1, I don't quite know what is meant by "Temporal event sequence" as opposed to "temporal point process". Furthermore, isn't a Hawkes process a version of a temporal point process? It seems that these publication sets may overlap somewhat. I'm wondering if this is clarified in the text, or if the authors can clarify.

3) In Section 4's "Data Preprocess" section, the authors write "to feed the sequences of varying length into the model, we pad all sequences to the same length, then use the "sequence_mask" tensor to identify which even tokens are padding." These masks are not defined, and are referenced no where else in the manuscript, so in my opinion this passage carries almost no information. To my understanding (which may be incorrect), some TPP datasets consist of a single sequence, and some models may process the sequence recurrently, i.e. each state embedding h_t depends only on the previous embedding h_{t-1}. For these models, why are variable-length sequences needed? On the other hand, datasets with events of multiple types (and models that can handle multi-type events) will need variable-length sequences. It would be very useful to the reader if the authors could describe these multiple scenarios, and specifically how EasyTPP handles each one at the implementation level.

If given satisfactory answers to the above, I am willing to raise my score.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
