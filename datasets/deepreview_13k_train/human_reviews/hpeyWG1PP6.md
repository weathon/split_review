# TDDBench: A Benchmark for Training data detection

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Training Data Detection (TDD) is a task aimed at determining whether a specific data instance is used to train a  machine learning model. In the computer security literature, TDD is also referred to as Membership Inference Attack (MIA). Given its potential to assess the risks of training data breaches, ensure copyright authentication, and verify model unlearning, TDD has garnered significant attention in recent years, leading to the development of numerous methods. Despite these advancements, there is no comprehensive benchmark to thoroughly evaluate the effectiveness of TDD methods.
In this work, we introduce TDDBench, which consists of 13 datasets spanning three data modalities: image, tabular, and text. We benchmark 21 different TDD methods across four detection paradigms and evaluate their performance from five perspectives: average detection performance, best detection performance, memory consumption, and computational efficiency in both time and memory. With TDDBench, researchers can identify bottlenecks and areas for improvement in TDD algorithms, while practitioners can make informed trade-offs between effectiveness and efficiency when selecting TDD algorithms for specific use cases. Our large-scale benchmarking also reveals the generally unsatisfactory performance of TDD algorithms across different datasets. To enhance accessibility and reproducibility, we open-source TDDBench for the research community.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work provides a comprehensive evaluation of training data detection (TDD). The evaluation spans multiple data modalities, including image, tabular, and text, and implements 21 state-of-the-art TDD algorithms, including large language models such as Pythia-12B. This is the largest benchmark for TDD to date, offering a valuable reference for future research on this problem.

Although this evaluation extensively covers multiple data modalities and four main types of TDD methods, the insights from the evaluation are limited. It lacks in-depth analysis of the results. For example, in Table 4, the authors do not explain why performance on CIFAR-100 is noticeably higher than on other datasets, and similarly in Table 5, there is no explanation for why the target model CatBoost outperforms others on tabular data. Some explanations of the results are also unclear. For instance, in Figure 2, the results indicate that the train-test gap is higher, and the target model performs better at detecting the data used in training. The authors attribute this to overfitting of the training data, which supposedly results in high performance when the train-test gap is large. However, wouldn’t overfitting typically degrade performance since the test set is independent? This explanation should be clarified. Additionally, in Fig. 3(a), the authors state that residual connections in ResNet help alleviate excessive memorization issues, thus decreasing the detection method’s performance. This explanation is also somewhat confusing. In Table 6, the authors claim that detection performance declines when the reference model has limited knowledge of the target model’s architecture. However, this is not always true; for the learn-top3 method, all types of reference models show similar performance without any decline. Thus, the explanation appears inconsistent.

The paper also lacks necessary explanations of the TDD protocols, such as the training-test protocol when using a reference model, or how the query model operates, which would make it easier for readers to follow.

The evaluation also omits Transformer-based models, which are widely used today. For image-based applications in particular, Transformer-based methods are among the most commonly used models, making it worthwhile to evaluate these models for TDD. For large language models, instead of focusing on the Pythia models, evaluating LLaMa, as the most widely used public LLM, would be highly relevant for TDD and aligns better with real-world scenarios where TDD is a concern.

In summary, this work presents an extensive evaluation across different datasets and multiple models, providing a complementary benchmark for future TDD research. However, the lack of in-depth analysis and necessary explanations of training-test protocols across TDD methods weakens the work’s overall quality. Additionally, the omission of evaluations on Transformer-based models and widely used public LLMs, such as the LLaMa models, limits the value of this work.

### Strengths
This work provides a comprehensive evaluation of training data detection (TDD). The evaluation spans multiple data modalities, including image, tabular, and text, and implements 21 state-of-the-art TDD algorithms, including large language models such as Pythia-12B. This is the largest benchmark for TDD to date, offering a valuable reference for future research on this problem.

### Weaknesses
Although this evaluation extensively covers multiple data modalities and four main types of TDD methods, the insights from the evaluation are limited. It lacks in-depth analysis of the results. For example, in Table 4, the authors do not explain why performance on CIFAR-100 is noticeably higher than on other datasets, and similarly in Table 5, there is no explanation for why the target model CatBoost outperforms others on tabular data. Some explanations of the results are also unclear. For instance, in Figure 2, the results indicate that the train-test gap is higher, and the target model performs better at detecting the data used in training. The authors attribute this to overfitting of the training data, which supposedly results in high performance when the train-test gap is large. However, wouldn’t overfitting typically degrade performance since the test set is independent? This explanation should be clarified. Additionally, in Fig. 3(a), the authors state that residual connections in ResNet help alleviate excessive memorization issues, thus decreasing the detection method’s performance. This explanation is also somewhat confusing. In Table 6, the authors claim that detection performance declines when the reference model has limited knowledge of the target model’s architecture. However, this is not always true; for the learn-top3 method, all types of reference models show similar performance without any decline. Thus, the explanation appears inconsistent.

The paper also lacks necessary explanations of the TDD protocols, such as the training-test protocol when using a reference model, or how the query model operates, which would make it easier for readers to follow.

The evaluation also omits Transformer-based models, which are widely used today. For image-based applications in particular, Transformer-based methods are among the most commonly used models, making it worthwhile to evaluate these models for TDD. For large language models, instead of focusing on the Pythia models, evaluating LLaMa, as the most widely used public LLM, would be highly relevant for TDD and aligns better with real-world scenarios where TDD is a concern.

In summary, this work presents an extensive evaluation across different datasets and multiple models, providing a complementary benchmark for future TDD research. However, the lack of in-depth analysis and necessary explanations of training-test protocols across TDD methods weakens the work’s overall quality. Additionally, the omission of evaluations on Transformer-based models and widely used public LLMs, such as the LLaMa models, limits the value of this work.

### Questions
- in Table 4, the authors do not explain why performance on CIFAR-100 is noticeably higher than on other datasets
- in Table 5, there is no explanation for why the target model CatBoost outperforms others on tabular data
- in Figure 2, the results indicate that the train-test gap is higher, and the target model performs better at detecting the data used in training. The authors attribute this to overfitting of the training data, which supposedly results in high performance when the train-test gap is large. However, wouldn’t overfitting typically degrade performance since the test set is independent? 
- in Fig. 3(a), the authors state that residual connections in ResNet help alleviate excessive memorization issues, thus decreasing the detection method’s performance. This explanation is confusing.
- In Table 6, the authors claim that detection performance declines when the reference model has limited knowledge of the target model’s architecture. However, for the learn-top3 method, all types of reference models show similar performance without any decline. The explanation appears inconsistent.
- The paper also lacks necessary explanations of the TDD protocols, such as the training-test protocol when using a reference model, or how the query model operates.
- Why the evaluation omits Transformer-based models, especially for image datasets
- Why chose Pythia instead of LLaMa as the most widely used public LLM

### Soundness
2

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
Motivated by the limitations of the previous benchmarks on training data detection (TDD), the paper proposes a new benchmark that covers three different modalities (tabular, text, and image) and includes evaluation of latest methods. The paper gives several insights on the recent TDD methods with respect to TDD.

### Strengths
1. The paper analyzes the latest methods' limitations and strengths carefully. Particularly, the correlation between train-test performance gap and TDD performance is interesting.

### Weaknesses
1. The proposed benchmark is not truly large-scale as it considers regular-sized datasets.

2. The proposed benchmark is not significantly different from the existing ones except that it covers different modalities. It would be more interesting if the paper does not follow data split rules from the existing benchmarks but explore something completely new. Another missing aspect is the size of data points that are evaluated under TDD.

3. The claim that TDD outperformance comes at a cost of computational expense is a bit controversial particularly due to Fig. 2(a); learning-based can achieve the best performance although it requires significantly less computation than the model-based ones.

### Questions
Please refer to the above weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces TDDBench, a comprehensive benchmark designed for Training Data Detection (TDD), which is for determining if specific data was used to train a model. This can be used to address issues like data privacy, copyright verification, and model unlearning. TDDBench includes 13 datasets covering image, tabular, and text data and benchmarks 21 TDD methods across four detection paradigms. The findings in this paper highlight that model-based methods outperform others but require significantly more resources. The benchmark reveals that existing TDD methods struggle, particularly with text and tabular data, and emphasizes the need for further research to enhance TDD effectiveness.

-----

Have gone through the responses, and I appreciate the authors' efforts. I keep my ratings.

### Strengths
The benchmark is comprehensive. The TDDBench covers multiple data modalities and includes a wide range of datasets, algorithms, and model architectures, making it one of the most inclusive TDD benchmarks available.

The writing and formatting are decent.

### Weaknesses
It will be great if the authors can propose a novel method to improve the performance based  on the analysis in their benchmark experiments.

It  lacks  an important discussion about the TDD and different training methods. There are supervised learning, self-supervised learning, unsupervised learning. Would  TDD method generalizable to different training methods?

### Questions
If a model is initialized with ImageNet pretrain  weights and then optimized with a different dataset  A. When using an  image example from ImageNet dataset as the input of the TDD  method to  test a model, should the  outcome to  be Yes  or  No?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper benchmarks 21 different TDD methods across four detection paradigms and evaluate their performance from five perspectives: average detection performance, best detection performance, memory consumption, and computational efficiency in both time and memory.

### Strengths
1. The paper is written well and is easy to understand.

2. The studied problem is very important.

3. The benchmark is comprehensive

### Weaknesses
1. It might be useful to include some discussion and experimental results on the defense of the training data detection algorithms

2. The authors can consider elaborating more on the takeaway messages from their experimentations and include more discussions on the current limations of the detection algorithms and the possible future directions at the end of the paper

3. It might be better to discuss the differences between the proposed benchmark with an existing benchmark. That will be useful.

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
3
