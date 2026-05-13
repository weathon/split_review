# SEBRA : Debiasing through Self-Guided Bias Ranking

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Ranking samples by fine-grained estimates of spuriosity (the degree to which spurious cues are present) has recently been shown to significantly benefit bias mitigation, over the traditional binary biased-vs-unbiased partitioning of train sets. However, this spuriousity ranking comes with the requirement of human supervision. In this paper, we propose a debiasing framework based on our novel Self-Guided Bias Ranking (Sebra), that mitigates biases via an automatic ranking of data points by spuriosity within their respective classes. Sebra leverages a key local symmetry in Empirical Risk Minimization (ERM) training -- the ease of learning a sample via ERM inversely correlates with its spuriousity; the fewer spurious correlations a sample exhibits, the harder it is to learn, and vice versa. However, globally across iterations, ERM tends to deviate from this symmetry. Sebra dynamically steers ERM to correct this deviation, facilitating the sequential learning of attributes in increasing order of difficulty, ie, decreasing order of spuriosity. As a result, the sequence in which Sebra learns samples naturally provides spuriousity rankings. We use the resulting fine-grained bias characterization in a contrastive learning framework to mitigate biases from multiple sources. Extensive experiments show that Sebra consistently outperforms previous state-of-the-art unsupervised debiasing techniques across multiple standard benchmarks, including UrbanCars, BAR, and CelebA.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper aims to rank samples by the degree of spuriosity and debias accordingly. The authors propose an unsupervised framework, Sebra, which ranks samples automatically by spuriosity in their classes. An important assumption of this paper is the negative correlation between spuriosity and the ease of learning a sample via ERM. Further, they dynamically steer ERM to satisfy this assumption during iteration training and sequentially learn samples in increasing order of difficulty. Experiment results show superiority of Sebra over other unsupervised debiasing methods.

### Strengths
- The motivation of this paper is simple and clear: biased samples are harder to learn.
- The design of methods is well described and easy to understand.
- Performance improvement is significant.

### Weaknesses
 - The method parts are a little too long and not eye-catching, written in a way that follows the authors' thought processes. I would prefer it to be more concise and add more examples or illustration figures.

- Some sentences are way too long to understand, e.g., lines 340-343. Also, plz pay attention to distinguishing \cite and \citep.

- Class labels are required in this method.

### Questions
- Can this method be extended to semi-supervised, especially when encountering new classes?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors mainly aim to address spurious correlations by ranking instances according to the extent of biases automatically and conducting contrastive learning with these rankings. Specifically, based on the observation that the extent of biases is proportional to learning speed, they modify the learning process of ERM to progressively capture biases according to their extent. This modification process consists of three phases: selection, upweighting & training, and ranking. Then, with acquired rankings, they conduct contrastive learning to debias models by constructing negative pairs with similar levels of spurious correlations and positive pairs with different levels of spurious correlations. In experiments, the authors demonstrate the effectiveness of their method.

### Strengths
* The proposed method can acquire the ranking of instances based on the extent of spurious correlation without human annotations.
* The authors show that their ranking is similar with the ground truth ranking and the overall framework mitigates performance gaps.
* The paper is well-written.

### Weaknesses
 - The paper lacks a detailed discussion on the utility of ranking instances according to the strength of spurious correlation. In this paper, the ranking is used for debiasing models via contrastive learning, yet it remains unclear how this approach offers high-level advantages over debiasing methods that do not utilize ranking. It would enhance the paper to discuss potential applications of their fine-grained spuriosity rankings beyond the contrastive learning framework. For example, the recent method, B2T [1], can identify and mitigate biases without human supervision by leveraging keywords. Since keywords are natural language, humans can interpret identified biases as well. Would the authors clarify the advantages over B2T?
- The experimental validation of the proposed method is not convincing. First, the comparison does not include recent debiasing methods [1, 2, 3]. Additionally, the model is validated only on a few datasets within the visual domain. The paper would be strengthened by including experiments on other widely-used datasets for spurious correlation, such as Waterbird, and NLP tasks like MultiNLI and CivilComments. Finally, the metrics are not commonly used in the spurious correlation domain, so reporting worst-group accuracy would enhance comparability.

### Questions
* Would the authors provide how much additional training time is required compared to training ERM. It would be helpful if you could provide a breakdown of the time spent on ranking and contrastive learning separately. Although there is a discussion in the appendix, specific values are not provided.

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
This paper proposes a bias mitigation method by ranking data points based on the assumption that the harder a data point is to learn, the less spuriosity it has and the overall ranking process is achieved by selecting and upweighting the samples that have not yet been learned, which relive the need of human supervision compared to existing method used to identify biased features.

### Strengths
- The paper addresses the bias mitigation problem by introducing a fine-grained estimation method instead of the traditional binary biased-*vs*-unbiased partitioning approach, providing a more precise way to evaluate spuriosity and the combination of the contrastive learning framework is a nice attempt to further reduce the reliance on the few unbiased samples compared to existing methods by utilizing all the samples in the dataset.
- The intuition behind the proposed method is clearly with the definitions and theorems. Although I think the assumption (assumption 1, Hardness-Spuriosity Symmetry) is strong, it still demonstrates a clear logic explaining why the ranking mechanism is designed in this way.

### Weaknesses
 - The proposed method heavily relies on the assumption 1 (Hardness-Spuriosity Symmetry), which states that samples with large losses (difficult to learn) are likely to be less spurious. This raises concerns about the method’s effectiveness when the samples are outliers or have label noise issues. Specifically, if the large loss is caused by these samples, then utilizing them for training would adversely affect the performance on the downstream tasks. The paper should include a more thorough discussion of this potential issue, perhaps by analyzing the distribution of losses and how it relates to the spuriousness of the samples. It is not clear how the method differentiates between samples that are hard to learn due to genuine complexity versus those that are hard due to being outliers or mislabeled.
 - The proposed method has three parameters to optimize, so when the dataset has high dimensionality, the optimization process may become very slow, and potential convergence issues should be discussed. The paper should provide a more detailed analysis of the computational complexity of the optimization process, especially in relation to the dimensionality of the input data and the size of the dataset. It would be beneficial to see empirical results demonstrating the scalability of the method with respect to these factors.
 - The overall writing of this paper is not very straightforward, as it repeats the main concepts too many times (e.g., the concept of spuriousness, the assumption, selection, upweighting.....) and the method section (3.1 to 3.3) has very weak connections, making each part appear independent of the others, which weakens the logical flow when introducing the method. I suggest the authors consider merging some of the repeated content (or summarize when it repeat) and adding some transitional words between sections to improve coherence.

### Questions
- When selecting points that have not yet been learned, which are defined by large loss, how can the method avoid selecting data points that are outliers or affected by label noise issues?

- Is Assumption 1 (Hardness-Spuriousness Symmetry) supported by any literature or empirical evidence?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work introduces SEBRA (Self-Guided Bias Ranking) to reduce bias in machine learning models without human intervention. Typically, models can develop biases by over-relying on spurious patterns in the data. SEBRA works by identifying these spurious patterns and ranking data points based on how likely they are to contain these misleading cues. During training, SEBRA adjusts the order in which samples are learned, focusing first on those with stronger biases and gradually moving to unbiased samples. This method allows the model to better distinguish between real patterns and biases, resulting in a more accurate and fair model.

SEBRA further incorporates this ranking into a contrastive learning framework, which contrasts data points with strong biases against those with fewer biases, enhancing the model’s ability to learn unbiased representations. Tests across datasets such as UrbanCars, CelebA, and BAR show that SEBRA outperforms other debiasing methods, particularly when multiple sources of bias are present.

### Strengths
The paper is easy to understand, especially for readers unfamiliar with the area. The approach is interesting and addresses a problem of importance.

The proposed algorithm seems simple, intuitive yet effective. 

The illustration of results in the appendix is quite helpful in building intuition.

### Weaknesses
The findings in the SEBRA heavily rely on Assumption 1, termed the Hardness-Spuriosity Symmetry, which states that the difficulty of learning a sample and its spuriosity (presence of misleading features) are inversely correlated. SEBRA uses this assumption to rank and prioritize samples in training, guiding the model to focus on samples with high spuriosity initially. The approach optimizes a ranking objective derived from this assumption, implying that SEBRA's effectiveness in reducing bias is largely contingent on this assumption holding true in practice. If assumption 1 does not hold, SEBRA’s ranking mechanism and bias-mitigation strategy might lose validity, as the model's ranking would no longer accurately reflect the spuriosity of samples. This reliance on a single assumption, without rigorous theoretical backing or extensive empirical validation across diverse datasets, is a significant weakness. The paper needs to provide more robust justification for this core assumption, as the entire method hinges on its validity. 

Please add more references in the related work section.

### Questions
Can you delve on the motivation a bit? Why is this kind of de-biasing important?

Is Assumption 1 a part of known literature or is it something discovered during the behavioral exploration of this work? If it is a known fact in debiasing literature, please cite relevant works.

### Soundness
3

### Presentation
3

### Contribution
2
