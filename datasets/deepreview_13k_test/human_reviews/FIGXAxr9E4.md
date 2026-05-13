# CLIP the Bias: How Useful is Balancing Data in Multimodal Learning?

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We study the effectiveness of data-balancing for mitigating biases in contrastive language-image pretraining (CLIP), identifying areas of strength and limitation. First, we reaffirm prior conclusions that CLIP models can inadvertently absorb societal stereotypes. To counter this, we present a novel algorithm, called Multi-Modal Moment Matching (M4), designed to reduce both representation and association biases (i.e. in first- and second-order statistics) in multimodal data. We use M4 to conduct an in-depth analysis taking into account various factors, such as the model, representation, and data size. Our study also explores the dynamic nature of how CLIP learns and unlearns biases. In particular, we find that fine-tuning is effective in countering representation biases, though its impact diminishes for association biases. Also, data balancing has a mixed impact on quality: it tends to improve classification but can hurt retrieval. Interestingly, data and architectural improvements seem to mitigate the negative impact of data balancing on performance; e.g. applying M4 to SigLIP-B/16 with data quality filters improves COCO image-to-text retrieval @5 from 86\% (without data balancing) to 87\% and ImageNet 0-shot classification from 77\% to 77.5\%! Finally, we conclude with recommendations for improving the efficacy of data balancing in multimodal systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies the societal bias issue in CLIP models and provides possible explanations and workarounds. Specifically, the representation and association biases are taken into consideration. While these biases can be somehow addressed with the data balancing strategy, other issue emerges. In this regard, this paper discusses in detail the role of data balancing in handling bias issues, and provides useful insights.

### Strengths
- The paper is well motivated and clearly written.
- Simple data balancing strategies are proposed to tackle the bias issue, demonstrating promising results.
- Comprehensive experimental results and analysis are presented, which may benefit the reader in relevant fields.

### Weaknesses
- While AB is relatively easy to mitigate, RB seems much more difficult to remove. In this regard, I would suggest the authors to shed more light on possible reasons and solutions. For example, I assume data augmentation shall be a promising workaround, and encourage the authors to explore more.

### Questions
- To me, the representation and association biases respectively correspond to the distribution shift of marginal output probability p(y) and conditional output probability p(y|x). What about another widely-discussed distribution shift in domain adaptation/generalization literature, i.e., marginal input probability p(x)? Can it also be a significant bias issue in large multimodal models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies two types of biases, representation biases (RB) and association biases (AB), in vision-language models such as CLIP. 

RB refers to that the model learns to prefer sensitive attributes (e.g., gender, age groups) in the training data. AB refers to that the model associates certain concepts with sensitive attributes. (e.g. occupations with a specific gender)

Studying such biases is an important problem in the real-world as CLIP-like models are widely used in the industrial applications. In this paper, the authors first investigate the empirical evidence of both biases and how it transfers from data to the model. They show that RB is sensitive to the latest training data distribution thus fine-tuning (FT) is an effective approach to reduce RB. However, FT is weak on AB. They then propose a data balancing algorithm to alleviate both RB and AB by estimating an optimal weight for each data example.

### Strengths
1. The empirical evidence of RB and AB is well supported in the experiments.
2. The proposed data balancing algorithm is principled with theoretical analysis.
3. The paper studies an interesting and important problem which may have a wide impact in real-world industrial applications, such as recommender systems and advertising.

### Weaknesses
1. The number of sensitive attributes in the experiments is limited to only gender and occupation.
2. Further experiments on proposed data balancing algorithm is lacking in the main text.

### Questions
1. How exactly the de-correlation between sensitive attributes and proxies is implemented?
2. In AB experiment, why adding proxies has inconsistent performance?
3. In data balancing algorithm, how to intuitively interpret $\alpha$ and $\beta$? and how $s$ is determined, is it calculating from the dataset over sensitive attributes?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study delves into the efficacy of data-balancing in reducing biases in CLIP models, highlighting its strengths and constraints. A novel data-balancing algorithm is introduced, showing success in mitigating representation biases, particularly through fine-tuning, but offering lesser impact on association biases, with a variable effect on task performance such as enhanced classification yet impaired retrieval. The research culminates with strategic guidance aimed at optimizing data balancing in multimodal learning systems.

### Strengths
1. Nice definition of various types of bias in data or model, this is a solid foundation to understand the problem

2. Given a nice definition of bias such as gender, this work shows the effect of model training with various type settings. (More or less data, fine tuning with various length of training time) 

3. Tested on various datasets and backbone designs. 

4. The proposed balancing algorithm does seem to successfully diminish bias without compromising the quality of the model.

### Weaknesses
1. I hope to see figures that are easier to interpret.

- For Figure 2 (top): It seems you intend to demonstrate that even with extra training data, bias persists. I struggled to determine which bars were being compared. A similar issue occurs with Figure 3.
- Regarding Figure 4: At first glance, without referring to the captions, all the color bars appear identical. My initial interpretation was that the results were largely uniform across the board.


2. I find myself somewhat perplexed by the conclusions drawn from the study's results. This confusion does not necessarily point to a flaw in the research but suggests that further clarification might be beneficial. I recommend referring to the detailed queries I've raised in the question section.

### Questions
1. In Section 4.1, the authors discuss various strategies, including adjusting the training set sizes and fine-tuning with or without dataset intervention. 

- While these strategies are standard in model training, the authors' approach underscores a well-known principle: merely increasing the size of a 'corrupted' dataset—say, by tenfold—will not address inherent issues. This scenario is a classic case of "garbage in, garbage out."

- Furthermore, the practice of fine-tuning a model on a specific dataset inevitably alters some pre-existing weights, adapting the model to new data characteristics. Consequently, it is not surprising that models fine-tuned on intervened sets exhibit improved bias metrics.

- In summary of this question: What's new here? 

2. This study suggests that balancing our training datasets can mitigate bias. However, it also implies that researchers must painstakingly identify what constitutes bias and determine the features requiring adjustment. I am particularly interested in the authors' insights on how their proposed framework accommodates additional features present in real-world datasets.


3. My concern extends to the interrelated nature of certain features, as highlighted in the occupation versus gender discussion in Section 4.2. While it is inappropriate to rely on stereotypes for inferring gender, assuming a 50/50 gender split across all professions disregards real-world disparities. It remains unclear how the proposed methods address "association bias."
- A link to “U.S. BUREAU OF LABOR STATISTICS” https://www.bls.gov/cps/cpsaat11.htm

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
