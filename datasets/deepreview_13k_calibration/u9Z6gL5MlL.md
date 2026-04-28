# Back to Fundamentals: Re-Examining Memorization in Deep Learning Models

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
In supervised training, memorization is the ability of deep learning models to assign arbitrary ground truth labels to inputs in the dataset. Due to the computa- tional difficulty of identifying existing memorized points, researchers often induce artificial memorization i.e, force the model to memorize the newly introduced points (via Noisy Label or Noisy Input). However, in this work, we show that this artificial proxy exhibits fundamentally different characteristics than the mem- orization real points (or natural memorization). To demonstrate this deviation, we re-examine two key findings derived from artificial memorization and com- pare them against natural memorization i.e., over-parametrization and increased training time increases memorization. We show that both these factors have the opposite effect i.e., they reduce natural memorization. Additionally, we find that memorization and train-test gap are strongly correlated (Pearson score 0.99). As a result, memorization is not necessary for generalization. Since real world models suffer from natural memorization (instead of the artificial one) our findings sug- gest the research community should focus on natural memorization, instead of the artificial proxy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on memorization in supervised classification models. The author state that it is often difficult to measure real/natural memorization since the only methods available rely on removing specific data points from the training set to be able to study wether this specific data point is memorized or not by the model. Intuitively, if the model is trained on enough data, removing any given data point should not impact the model's prediction over this data point if the model was able to generalize. However, if removing the data point induces a wrong answer, it is often considered that this data point could only have been memorized by the model. Such setup is often costly, so researchers often use proxies (coined as artificial memorization) to avoid training thousand of models. Those proxies mostly rely on the addition of noise to approximate natural memorization phenomena. Based on the literature on artificial memorization, it is often considered that increasing the model size or the number of epochs lead to a greater risk of memorization. The authors challenge this hypothesis by shedding light on the relationship between the double descent phenomena (in which the test error rate can start to get lower after having increased) with natural memorization. They especially show that by training longer and with more capacity, the memorization can actually decrease after having increased significantly (which seems to be in contraction with the finding from the artificial memorization literature).

### Strengths
- The paper is well motivated and well written.
- The authors introduce the interesting concept of "transient memorization" about data points that can be memorized under certain models by not by others. This is interesting to know that smaller models will memorize those point easily, while bigger models will generalize to them.

### Weaknesses
 - The abstract start by stating that memorization is the ability of "deep learning models to assign ground truth labels to inputs". I would be cautious about such statement since a generative model that do not learn from any ground truth labels, could memorize its inputs simple because the model is just train to reconstruct the input.  So I would definitively not constrained the definition of memorization in deep learning to having ground truth labels. Instead, I would recommend the authors to specify directly that they are interested in supervised scenarios to avoid any misunderstanding.
- Not really sure that Figure 1 is even needed in the first place, most of the readers will know what unstructured noise is.
- Incorrect statement. The authors wrote "Double descent experiments have been conducted on artificial data ... " Some double descent experiments like in 1) have been conducted on dataset like cifar10.
- Experiments are being conducted on only two very similar datasets CIFAR10/CIFAR100. Even if the compute cost can justify such limited experiment setup, I would be more cautious about the claim being made (such as "we show that this understanding is incorrect", "Those does not apply..."). I would advise to downplay a bit them by specifying something like "Given our experimental results on CIFAR10 and CIFAR100, we challenge the idea that artificial memorization might always be a good proxy for...". And maybe add as future work, that more experiments might be needed to confirm those results.

### Questions
- Any insights on the relationship between weights-decay and memorization. Since increasing the model's capacity can reduce memorization, do having a stronger weight decay could increase memorization?
- Are your results still holding when using data augmentations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper considers memorization in DNNs. Going back to the original definition via expensive leave-one-out trials, the authors question whether artificial memorization experiments as proxies for 'natural memorization' are valid. To that end, they adopt an alternative, efficient method for natural memorization. Using that, they test the two main findings of artificial memorization: that longer training and larger models increase memorization. In a set of experiments, they empirically find the opposite trend.

### Strengths
- The topic of memorization is highly relevant not only to address data privacy, but also to get a better understanding of generalization and effective model design.
- The submission is generally well-written, identifies a clear question and then takes a straight path to answering it. 
- The experiments are well-suited to test the findings of previous work (size and training length correlate with memorization).
- The findings are interesting, and spark new questions for further research.

### Weaknesses
 - As far as I can tell, the submission has no original method contribution, it re-uses definitions for and methods to measure memorization from previous work. It presents the empirical test if findings from artificial proxies hold in settings for natural memorization.
- Further, the limited experiments also limit the empirical significance of the submission. To me, it seems that the experiments show the necessary signal to dis-prove the abovementioned correlations of model size and training duration with memorization, but stop there. I would encourage the authors to test the generality of their findings, e.g. by varying architectures more systematically (in both depth and width), changing the dataset and task. Their test setup may also allow to vary a broader range of hyperparameters that do affect performance and generalization gap, s.t. they can test the relation to memorization on a broader basis. Lastly, I would appreciate a test of how far the findings carry over to realistic training regimes, e.g. with data augmentation. 

I encourage the authors to continue work on the submission, and provide broader experiments and insights into what could drive memorization or how their results, e.g. on generalization gap, might be reconciled with existing work. As it currently is, I believe it does not suffice to recommend acceptance.

### Questions
No further questions, please refer to weaknesses.

### Soundness
2

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
4

### Summary
This paper re-evaluates memorization in deep learning by distinguishing "natural memorization" (memorization of real data) from "artificial memorization" (induced with noisy data or labels), arguing that the latter fails as an accurate proxy for real-world behaviors. The authors find that over-parameterization and longer training reduce natural memorization, as larger models learn complex patterns and generalize better over time. They also introduce "transient memorization," where certain data points shift between memorization and generalization depending on conditions like model size or training stage. By exploring the relationship between train-test gaps and memorization, the study suggests that models with smaller train-test gaps tend to memorize less.

### Strengths
**1. Novelty:** The paper challenges the existing reliance on artificial memorization by demonstrating significant differences between artificial and natural memorization. This is valuable, given the application of artificial memorization as a proxy in prior studies.

**2. Results on Over-Parameterization:** The finding that increased model complexity can reduce memorization, contrary to popular belief, is useful. It aligns with ongoing discussions about the balance between capacity and generalization, especially given the risks of overfitting in high-parameter models.

### Weaknesses
 **1. Transient Memorization as a New Phenomenon:** I believe the authors have grouped two distinct phenomena into one category, which reduces its impact

 a. Dynamics-wise: This refers to the authors' claim that they observe a new phenomenon where certain data points are memorized and then generalized. While forgetting during training is already known (see Toneva et al., 2018), the evidence presented here is novel enough to stand as a new insight.

 b. Model-wise: The authors suggest that "since shallow models do not have enough capacity to learn the rare patterns corresponding to smaller sub-populations, they instead memorize them in an attempt to classify them correctly." However, the claim that larger models memorize less due to their improved learning capacity is too generic to be presented as novel.
      
To strengthen the paper, I recommend splitting transient memorization into these two distinct forms. The model-wise transient memorization could be more appropriately discussed when exploring the role of over-parameterization.

**2. Insufficiency of Memorization Thresholds:** The fixed memorization threshold of 25% is applied across various experiments without sufficient justification. This raises concerns about arbitrary cutoffs potentially affecting results, especially when claiming that natural memorization behaves differently across sub-populations. While I believe the results are fundamentally correct, presenting a histogram showing the distribution of memorization scores would add significant value. For instance, memorization scores are often bimodal [2], with many samples showing either zero or high scores. A histogram representation would illustrate how this bimodality changes (a) as training progresses and (b) as model size changes, thereby substantially strengthening the paper.

**3. Train-Test Gap and Memorization:** The paper proposes that reducing the train-test gap decreases memorization. However, the empirical support for this claim is limited to two architecture families (VGG and ResNet) tested on CIFAR datasets. While I understand that using ImageNet would be computationally prohibitive, exploring other tasks (e.g., language or segmentation tasks) could provide stronger evidence for the generalizability of this finding.

### Questions
1. Could transient memorization be split into distinct dynamics-wise and model-wise categories to better capture its nuances? Specifically, does collapsing both dynamics-wise and model-wise memorization under the umbrella of transient memorization risk obscuring important insights about model behavior?

2. Could architectural variations other than ResNet and VGG affect the train-test gap and memorization dynamics? For instance, do transformer-based architectures show similar relationships, or might they reveal new insights regarding the impact of model complexity on memorization? Mostly because transformers are hard to train on small datasets, thus pre training may have a significant effect on the results.

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
The paper discusses the definition and the measurement of memorization in the previous work. It states that a number of papers in the literature measure memorization for artificial data points introduced in the dataset. The paper discusses that the conclusions made for the artificial data points do not apply to the natural data points in the training dataset. Specifically, the paper states that the claims made in the literature about memorization on model size and training time do not hold for the natural training data points. The authors ground those claims based on the experimental results for VICReg and ResNet models trained on CIFAR10 and CIFAR100 datasets.

### Strengths
+ The paper questions important aspects of memorization definition and measurement. It discusses the memorization measurement for natural data points vs data points that are artificially introduced via noisy labels or noisy inputs.
+ The paper cites and discusses a number of important works on memorization in literature.
+ Transient memorization proposed by the authors  is an interesting phenomenon.

### Weaknesses
 + The story of the paper is not very clear. More specifically, the paper relies on Feldman and Zhang’s measurement of memorization and states that transient memorization happens for smaller sub-populations. The smaller sub-population, however, could be the long tail. This contradicts the study proposed in Feldman and Zhang. Feldman and Zhang specifically discuss that long tail is being memorized for the final checkpoint not for intermediate epochs.
+ Overall the experiments for the artificial data points are missing. The paper doesn't give the full picture and doesn't show clear differences between natural and artificial data points based on the experimental results. Currently the experiments are conducted only for the natural data points.
I'd suggest running experiments for artificially inserted / noisy labels and inputs in CIFAR and show that for VGG and ResNet memorization is indeed different for those data points as opposed to the natural data points. Previous literature might have a different experimental setup. The authors should run the experiments for their experimental setup and datasets when comparing with their approach. 

+ The study of relationship between model size and number of epochs doesn't seem very novel. There is work on that especially on the large language models.
E.g. Carlini, et.al. discuss that the memorization increases with the capacity of the model
https://arxiv.org/pdf/2202.07646

### Questions
1. There are papers that study the relationship between model's size and the training dynamics with respect to memorization (especially large language models ). Have you considered looking into that ? Are the claims made here true only for vision classifiers ?

### Soundness
2

### Presentation
2

### Contribution
2
