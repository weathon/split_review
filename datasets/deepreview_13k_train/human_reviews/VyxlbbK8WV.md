# Uncovering Self-Emergent Similarity in Deep Vision Networks: A Systematic Framework

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
Similarity is a key construct in psychology, neuroscience, linguistics and computer vision. Similarity can manifest in various forms, including visual, semantic, and contextual similarity. Among these, semantic similarity is particularly important. Not only it serves as an approximation of how humans categorize objects by capturing connections and hierarchies based on shared functionality, evolutionary traits, and contextual meaning, but also offers practical advantages in computational modeling via the lexical structures such as WordNet. Unlike human polls, WordNet-defined similarity is constant and interpretable, making it an important baseline for evaluation. As in the domain of deep vision models there is still a lack of a clear understanding about the emergence of similarity perception, we introduce Deep Similarity Inspector (DSI). It is a systematic framework to inspect and visualize how deep vision networks develop their similarity perception during training and how it aligns with semantic similarity. Our experiments show that both Convolutional Neural Networks' (CNNs) and Vision Transformers' (ViTs) develop a rich similarity perception during learning with 3 phases (initial similarity surge, refinement, stabilization), while clear differences are found in their dynamics. Both CNNs and ViTs, besides the gradual mistakes elimination, improve the quality of mistakes being made (the mistakes refinement phenomenon).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper describes a group of methods for evaluating similarity between classes in DNNs, called Deep Similarity Inspector. The authors evaluate the evolution of these metrics over training for a variety of network types and identify 3 stages of similarity over training (surge, refinement, stabilization).  They note differences in this evolution between CNN, ViT, and hybrid models, showing that CNNs peak quickly and refine, while ViTs develop similarity more slowly, and remain stable, but note that all models follow this 3 stage process. The paper compares these networks similarity to that of WORDNET similarity as a proxy for human semantic understanding.

### Strengths
Originality: DSI is an original contribution as far as I am aware. 

Quality: The quality is generally good. The authors offer multiple measures of similarity, rather than just one for evaluating similarity in networks. They also evaluate multiple network types (CNN, ViT, and hybrid)

Clarity: The paper is overall clear in the purpose and execution of the experiments reported.

Significance: This is an important contribution to explainable AI. In addition, though not discussed by the authors, I believe these metrics could offer a unique metric to evaluate models during training (i.e. nothing that a model has moved into similarity stage 3 could be a signal for training nearing completion, or variations in the stages could inform hyper parameter tuning).

### Weaknesses
While the proposed formulation of similarity proposed is novel to my knowledge, the authors fail to compare their method to very similar ways of measuring similarity including methods like adversarial examples.

A major goal of the paper appears to be based on aligning networks with human psychology, yet WordNet is the only source of measuring human similarity perception. I feel there needs to be additional methods of comparing this to human perception, given the focus on human semantic alignment. On the other hand, I believe the similarity metrics themselves have merit outside the context of human alignment, especially in explainability, and as a general tool for evaluating model training. Given the lack of human-comparison in the results, it was confusing to read an abstract and introduction so focused on human perception, especially when I believe there are other, potentially stronger applications.

While the clarity of the experiments are good, the explanations of the individual metrics would benefit from intuitive explanations in addition to the mathematical descriptions provided. This is especially important given that the authors are introducing these concepts for the first time in this paper.

It is unclear how robust this method is to contexts outside of vision such as audio or even robotics. I don’t see why this method couldn’t be applied in another modality, but this discussion is completely absent from the paper.

The paper does not discuss the computational cost of computing these metrics, limiting the understanding of how easily it can be incorporated into a training pipeline.

### Questions
What is the computational cost of computing the proposed metrics during training? Is this something that could be cheaply calculated alongside the loss graph to aid in everyday training?

Could this metric be formulated as part of a loss function to improve accuracy or robustness? Does higher dissimilarity correlate with higher adversarial or other types of robustness? 

Is there another measure of human similarity that could be compared to in addition to wordnet? This would strengthen the paper significantly - I see this as the biggest weakness of the paper given the strong human motivation in the abstract and introduction. Alternatively, the introduction and abstract could be modified to discuss the importance of the contributions in the context of model evaluation rather than human similarity.

L83-86: Please phrase this differently - ‘the real questions are’ suggests that these questions posed by the authors are the only meaningful or important inquiries in our field. The previous approaches cited are also important and valuable. A simple rephrase such as  “We focus on the related questions of…” would fix this, and acknowledge there are a broad spectrum of important questions in machine learning, and the authors are most interested in focusing on those in this paper.

Relatedly, the authors say there are only 2 (Bial et al 2017, Huang et al 2021) works that examine whether the similarity perception of deep object recognition models aligns with human judgements. First, this paper does not evaluate human judgements directly, only via wordnet. Furthermore, there are many more studies that compare object recognition with humans and measure related metrics of similarity. Adversarial examples for example measure similarity perception through the effectiveness of perturbations, and many previous works have measured this in both humans and models (ie Elsayed, et al 2018 Adversarial Examples that Fool Both Computer Vision and Time-Limited Humans.).  I suggest the authors broaden their literature review to include this and other examples of the many ways that similarity is measured in humans and models, and more fairly situate their contribution in the context of the field.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper develops a framework for evaluating how semantic similarity perception emerges in learned visual representations. The motivation is to draw parallels and insights in to the emergence of similarity perception in humans. The authors primarily evaluate the task of supervised object recognition and compare the effects of architecture on similarity emergence. The main methodological contributions are new numerical, semantic similarity metrics, which reduces the need for difficult to scale qualitative measures. The primary finding is that over time models learn to make fewer and better mistakes. This learning is initially quick, then starts to refine and stabilize, with CNNs generally developing semantic similarity perception faster than ViTs.

### Strengths
The work at a high level is generally clear. The construction of the network, confusion, and semantic similarity matrices which are used to plot different curves during training seem technically reasonable. The goal of understanding developing qualitative measures of semantic similarity, particularly in the context of human cognitive science, is valuable from my perspective and is motivated well in the introduction. I agree that many approaches comparing to humans are very data-dependent, limiting their applicability, and think the use of WordNet is an interesting approach.

### Weaknesses
My biggest concern with this work is the focus on supervised object recognition training. Both from the perspective of computer vision and deep learning-based models of human vision, there are many other more powerful training objectives for visual learning. Self-supervised approaches, in particular, learn strong semantically meaningful representations (like DINO) and have been shown to produce strong candidate models of the visual processing (SimCLR for example is used in Margalit et al. 2024). While these models could additionally be trained downstream on a supervised objective, the proposed method would not be able to measure earlier effects during training where the bulk of similarity perception is likely to emerge. Relying on object classifiers limits the applicability of the proposed method to more powerful representation learning frameworks, especially for during training analyses. 

In addition, regardless of the task, the training results presented using the proposed metrics do not appear particularly significant in my view. From the training loss and accuracy alone, it should be clear that the models rapidly get better at similarity and then stabilize. For similar reasons, it is unsurprising that CNNs learn similarity more quickly than ViTs, which are known to need large amounts of data to perform well on these small supervised tasks.

Finally, the connection to human cognition presented is weak, in my opinion. The only measure grounded in human studies is the use of WordNet for the semantic similarity measure. While this is a clever idea, there are no direct links to cognitive science results beyond this. In addition, WordNet is not grounded in work visual perception, being primarily language. In a study looking at representational similarity in classifiers, I believe it would be stronger to make connections to datasets and models that use human judgements or interpretations on images, or to instead evaluate vision models that more explicitly learn text relations, such as CLIP. 

Minor: there are many metrics and acronyms presented which can be a bit confusing to keep track of.

### Questions
Can you elaborate on the choice of training objectives and models? In addition, do you see any use for your metrics on larger pre-trainined models, or the exploration of factors other than architecture such as model size?

Can you explain what insights your metrics contribute beyond what standard training metrics such as loss and accuracy yield?

Do you view your work as primarily trying to contribute new techniques for building cognitive science models? Can you elaborate if so? In your opinion, does your work bring insights into representation learning more broadly?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores how vision models learn the similarity structure within the data over the course of training. The authors focus on image classification tasks. To achieve this, the authors propose a set of measurements specifically designed to quantify the similarity between different classes in the data as perceived by the network. The basic structure of the measurements is comparing two NxN similarity matrix over the classes. The similarity matrices can come from different stages of training or different ways to measure similarity.  They apply these measurements over the course of training for several models to identify different phases of similarity learning. The authors also provide a similarity measure to compare model perceived class similarity with WordNet (as a proxy for human-perceived class similarity). The authors find some interesting properties from analyzing several models, these will be detailed in the strengths section.

### Strengths
I find that the works major strengths are in question selection, experimental design and results. 

The authors ask an interesting question about how class similarity perception evolves during training and how it relates to task performance. 

Through studying this question, the authors discover some interesting properties, specifically, they show that networks go through three phases while learning the similarity between classes. In the first stage, models discover the coarse structure of similarity between classes, followed by a stage in which models start to perceive differences between similar groups, and finally a stage where the where similarity is roughly static and the model has stabilized. 

Additionally, the authors discover that model's initially make errors according to the perceived similarity structure, but over time model mistakes diverge (they make mistakes between less similar classes) and do not follow the similarity structure as closely. Finally, the authors discover an interesting pattern of "bumps" in the alignment between WordNet similarity and model similarity.

### Weaknesses
The primary contributions of this work are in the question and experimentation, since the methods are derived from previously developed methods (as cited by the authors themselves).

Therefore, my assessment of the work is focused on the experimental design and results. I will first summarize my primary concerns and then provide more detailed criticisms. While I find the results provided by the authors to be interesting, I believe the phenomena discovered to be under-explained, and I would like the authors to go one step deeper to understand the some of the properties discovered in the paper.

(W1) In particular, this paper could be significantly strengthened by providing an experiment to concretely explain the decrease in errors only IDM (Fig. 6b). The authors hypothesize that this decrease is due to less typical samples or noise from mislabelled data, but provide no experiments to test these hypotheses. See Q2.

(W2) I am not convinced of the value of the WordNet experiments, see Q1. However, provided there is value, a closer inspection of the cyclical nature of the bumps would be interesting. I prioritize this less than (W1).

(W3) The difference in curves between mean weights similarity for ResNet18 and MobileNetV2 and the other models is surprising and poorly explained (Fig 1a). I prioritize this less than (W1).

(W4) I was not able to find a place where the authors clearly stated whether the experiments were conducted with training data or test data. Assuming the results are using test data, the results are missing the same plots for the training data. Is some of the phenomena we see due to overfitting on the training data?

(W5) Please provide a detailed description of how WordNet similarity is computed in the appendix.

(W5) Additionally, I also find some significant weaknesses in writing style.
Line 053 - "This makes similarity barely explored to this day" is too strong of a statement.
Line 202-215 - Dissimilarity Metric (DM) is not precisely defined please provide an equation.
There is a tendency to anthropomorphize models, for example the word "strive" is used as if the model has a goal (Line 419, 503, 516). Also, "stick to it" (Line 505).

(W6) Minor weaknesses in writing:
Line 223-224: took two passes to understand.
Line 199 - should be indirect similarity?
Line 268 - "WordNet" leaf
Line 211 - SCSM used again, use a different term

### Questions
(Q1) I am not sure of the value of semantic similarity comparisons using WordNet, considering language based similarity and visual similarity should have significant differences. Can the authors speak more about the value of this experiment and how it can be interpreted?

(Q2) Related to (1), I am also surprised that the authors do not measure similarity using euclidean/cosine distance over each sample which by my understanding would be a direct and functional method of measuring similarity. Why is this not included? Wouldn't this metric allow you to inspect which samples specifically deviate from the model's perception of similarity.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work performs a quantitative analysis in an attempt to understand when semantic similarity emerges in different vision networks. The focus is mostly on models that are trained to perform classification and similarity is defined based on different ways of assessing class confusion. The authors outline different ways of generating class similarity/confusion matrices and different metrics for comparing models based on these matrices. Results are present across different CNN and ViT models trained on datasets such as mini ImageNet.

### Strengths
[S1] The work is exploring a very interesting set of questions, and multiple experiments are conducted to investigate them. 

[S2] Some of the observations and insights wrt to when similarity emerges in different models are interesting.

### Weaknesses
 [W1] Evaluation
* The evaluation hinges on the assumption that category level labels are a good proxy for visual similarity. As noted on line 379, there can be many other semantic relationships present that are not captured by this. In addition, there can also be fine-grained sub-category level differences, e.g., the female of one bird species might look more like the female of another, but the males could be very different. This restriction to category labels and the hierarchy of WordNet is a big limitation as it may not be a good proxy for visual similarity, or at least visual similarity as perceived by humans.  
* There are also other factors that will impact how similarity is encoded in a network that are not explored, e.g., network capacity, how the weights are initialized, or nuances of how the networks are trained.   

[W2] Missing explanations
* While the experiments are extensive, there are cases where the analysis is lacking. For example, ResNet18 and MobileNetV2 in Fig 1 (a) are outliers but this is not explained or discussed sufficiently.   

[W3] Missing Related Literature
* There is a body of work that seeks to develop methods for comparing the representations learned by networks, e.g., CKA by Kornblith et al., ICML 2019. 
* Line 91 states that the authors are only aware of two papers that “examine whether the similarity perception of deep object recognition networks aligns with human judgement”. There is in fact a lot more uncited work on this topic, e.g., see the dataset collected by Roads and Love CVPR 2021 that enriches ImageNet with human similarity labels. There is also work on trying to predict human similarity judgements from pre-trained vision networks, e.g., Attarian et al. NeurIPS Workshops 2021, and work using generated images for similarity assessment DreamSim Fu et al. NeurIPS 2023.   
* Finally, there is also work in computer vision that addresses the fact that there might be more than one “notion” of similarity used to compare image instances, e.g., CSN from Veit et al. CVPR 2017. 

[W4] Paper Readability and Structure
* There are a lot of acronyms that require the reader to revisit earlier sections of the paper to understand what is being presented, e.g., Fig 2 caption notes “SAI(NCSM, CCSM)”. The captions of the figures could be improved to make parsing these details easier.   
* Research question 1 (L273), as worded, seems to be two different questions combined? It also overlaps with research question 3. The text of these questions could possibly be refined to make them clearer.   

Minor additional comments that do not require a response during the rebuttal:
* The paper would benefit from a clear definition of “similarity” in the introduction   
* Use \citep{} instead of \cite  
* L618 this paper is incorrectly cited as NeurIPS 2024, and not 2023
* L1299 and elsewhere use ``bad’’ instead of ”bad” in latex

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2
