# A new perspective on applying mesoscience to explore the model generalizability

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
The black-box nature is one of bottlenecks constraining machine learning (ML) models, especially, neural networks, from playing a more important role in the field of engineering. The decision-making process of the model often lacks transparency and is difficult to interpret, which limits its use in the high-risk domain. Thus, explaining the generalizability of ML models is a crucial topic in the field of AI. However, there has been no unified understanding of this issue. This work attempts to introduce the concept of compromise in competition (CIC) in mesoscience into the explanation of the generalizability of ML models. In this work, a scale decomposition method is proposed from the perspective of training samples, and the CIC between memorizing and forgetting, refined as dominant mechanisms, is studied. Empirical studies on computer vision (CV) and natural language processing (NLP) datasets demonstrate that the CIC between memorizing and forgetting significantly influences model generalizability. Additionally, dropout, L2 regularization, etc., aimed at mitigating overfitting, can be uniformly reinterpreted through the CIC between memorizing and forgetting. Collectively, this work proposes a new perspective to explain the generalizability of ML models, in order to provide inherent support for further applications of ML in the field of engineering.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a metric to understand model generalizability and identify memorized points. The method leverages model training dynamics, specifically tracking how predictions for examples change throughout training. The authors demonstrate this approach by adding label noise to training datasets in both computer vision and natural language processing tasks.

### Strengths
- This work addresses an important problem.
- Approach is simple.

### Weaknesses
 - There is a substantial body of prior work that addresses similar questions. The authors should discuss these studies and compare at least representative methods in the experiments.
- It is unclear what new insights this paper provides regarding model training dynamics compared to existing research. The proposed method seems to overlap substantially with approaches like Maini et al. (2022), Garg and Roy (2023),  Siddiqui et al. (2022); the authors should clarify the novelty of this work in comparison.
- The experimental results are very limited, particularly given that this is an empirical study rather than a theoretical one. No deep model architectures, also, TextCNN seems like an unusual model choice for NLP experiments.

### Questions
- How do these observations scale with model size? Do larger models, such as BERT or even large language models (LLMs), exhibit similar patterns?
- There is extensive research exploring training dynamics in the context of spurious correlations such as Nam et al. (2020). Would it be possible to extend the experiments to examine these phenomena beyond just noisy labels?
- The authors could consider comparing against memorization measures that do not rely on training dynamics such as Feldman & Zhang (2020)
- Are the findings consistent when using the same architecture but a different optimizer? what about changes in the learning rate?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work proposes using concepts of mesoscience to explain generalization in deep learning, along with main phenomena like forgetting and memorization. In particular, it studies the (compromise in) competition of forgetting and memorization to describe how generalization happens in neural networks. Experiments are conducted using several small-scale architectural setup with prediction tasks like cifar, mnist and trec (for text).

### Strengths
S1: The introduction of mesoscience for explaining DL phenomena is interesting and can be promising.

S2: The authors consider a variety of architectures. Even though they are simple, they are different enough from each other and represent different setups of interest for the topic.

### Weaknesses
W1: As in its current state, the paper is more of an application of mesoscience to reach conclusions that are largely known in the field. While there is value in exploring the application, in terms of findings, it is hard to see the novelty of the results. For example, the tension between memorization and forgetting has been studied in depth in the past years, as is the effect of regularization and dropout. 

W2: The paper does not sufficiently engage with comparing its results with previous work that falls roughly in the area of the science/physics of deep learning. Below there is some representative work in this area:

Physics of language models: Part 3.3, knowledge capacity scaling laws
Learning and generalization in overparameterized neural networks, going beyond two layers
The implicit and explicit regularization effects of dropout
Grokking: Generalization beyond overfitting on small algorithmic datasets

### Questions
As a suggestion for future versions of the work, showing a finding that has not been sufficiently explored in the field would be a more convincing result. In general, for any field to adopt a new method/approach there needs to be sufficient motivation from a results novelty point of view.

In addition, given that the concept of mesoscience is not familiar to the ML audience, a more comprehensive background section on the approach along with examples would make the work more approachable.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes analyzing model generalization (test loss) by examining subsets of training examples that are memorized or forgotten throughout the training process. By observing the ratio between M (memorized examples) and F (forgettable examples), the authors attempt to explain the behavior of the test loss. They conduct toy experiments using simplified datasets and FC and CNN models.

### Strengths
The idea proposed by the paper is very simple to grasp. 

The "Dominant Mechanisms" section is well-written, incorporating numerous citations from other fields and providing helpful intuition and motivation.

### Weaknesses
 **Poorly Presented:** The main weakness of this paper lies in its overly verbose and unclear presentation. Although the proposed idea, experiments, and analysis are straightforward, the authors have made the text unnecessarily wordy and complex. I have provided many suggestions below to help improve the clarity and conciseness of the writing.

**Ignoring S2:** Although the authors state their focus on the S3 subset, the size of the S2 subset is also significant (e.g., how many examples are memorized?). This aspect should be included in the analysis, as it would be valuable to understand how it impacts the results.

**Trivial Findings:** I find the results to be trivial, offering no new insights into deep learning or learning processes, as they can be explained by basic principles (e.g., variance reduction with larger sample sizes). I do not understand why the authors emphasize "mesoscience", and how looking at different scales of examples makes a difference (beyond the trivial variance reduction). If the authors wish to increase their score, they should include here (rebuttal) a clear paragraph that explicitly explains the findings, clarifies why they are not trivial, demonstrates their generalizability, and highlights their novelty compared to previous results.

**Toy Experiments and Cherry-Picking:** While it is acceptable for papers like this, which do not aim for a SOTA model or propose a new training method, to rely on toy experiments (e.g., simplified datasets, toy models, a limited number of models), the results here appear cherry-picked. It’s unclear whether the findings can be generalized, as the authors use different models to demonstrate each result. If the authors had provided a theorem on the relationships between M, F, and generalization, toy experiments might be sufficient. However, without this, I would expect robust findings, which is not the impression this paper gives.

### Questions
Introduction: I recommend adding two additional paragraphs—one to describe the methodology and experimental setup, and another to discuss the results and key findings.

Figure 1: Use the caption to describe the components in the figure, keeping in mind that many readers will look at the figure first to get an initial understanding of the paper before reading the text. The caption is an excellent place to briefly introduce your method and provide readers with a high-level overview of what to expect in the following sections.
At this point, I do not understand the Figure or any sentence written in the Figure. Please use the caption.

Figure 2 a: How many epochs did you use for training the models? Is it possible that the number of training steps (i.e., gradient updates) varies with each batch size? Specifically, could smaller batch sizes result in a greater number of gradient updates?

Figure 2b: The x-axis and the variable w are unclear. Please clarify these elements in the caption. The reader should not have to assume what the plot represents; it should be explained explicitly.

Line 157: The statement "mimicking the integrative process of neuronal activity in the brain" is inaccurate. If you intend to make this claim, you should support it with a citation from neuroscience research that validates it (although such a citation is unlikely to exist). You can write "inspired by..."

Suggestion for Figures: Please save the Figures in PDF format (in PowerPoint, you can print -> PDF the relevant slide, and then use a free online crop program). 

Subsection 2.4: This subsection is difficult to follow. Please revise it to make your points clearer. Explicitly state what the reader should focus on and what inferences can be drawn. Currently, the subsection is too complex, and the figure caption lacks meaningful details, making it challenging for readers to follow your explanation. Additionally, you haven't defined CIC—please provide a formal (preferably mathematical) definition and follow it with a few sentences explaining this definition in simple, understandable terms.

Line 262: What do you mean by "stability condition"? Additionally, does your conclusion—“it is evident that on the element scale, there is no stability condition”—apply to every element or only to the two specific points you selected? Please ensure transparency here.

Figure 5: What is the purple line? what is the black line? Use the caption...

Subsection 2.4: The conclusion here is unclear. It appears to simply restate the well-known fact that a larger sample size results in a smaller variance for the mean statistics. Please clarify if there is an additional insight beyond this.

Figures: What does "(-)" stand for?

References (Bib): Please avoid citing published papers as "arXiv" papers. You can use resources like DBLP or Semantic Scholar to find BibTeX citations that include the appropriate journal, conference, or venue instead of referencing arXiv.

### Soundness
1

### Presentation
1

### Contribution
2
