# Symbolic regression via MDLformer-guided search: from minimizing prediction error to minimizing description length

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
Symbolic regression, a task discovering the formula best fitting the given data, is typically based on the heuristical search. These methods usually update candidate formulas to obtain new ones with lower prediction errors iteratively.
However, since formulas with similar function shapes may have completely different symbolic forms, the prediction error does not decrease monotonously as the search approaches the target formula, causing the low recovery rate of existing methods.
To solve this problem, we propose a novel search objective based on the minimum description length, which reflects the distance from the target and decreases monotonically as the search approaches the correct form of the target formula.
To estimate the minimum description length of any input data, we design a neural network, MDLformer, which enables robust and scalable estimation through large-scale training.
With the MDLformer's output as the search objective, we implement a symbolic regression method, SR4MDL, that can effectively recover the correct mathematical form of the formula.
Extensive experiments illustrate its excellent performance in recovering formulas from data. Our method successfully recovers around 50 formulas across two benchmark datasets comprising 133 problems, outperforming state-of-the-art methods by 43.92\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a search objective based on the principle of minimum description length, which aims to streamline and enhance symbolic regression tasks. The authors generate a targeted training dataset and employ neural network techniques to develop a symbolic regression function. By using neural networks in this way, the approach is intended to improve both the efficiency and effectiveness of modeling complex data relationships through symbolic regression.

### Strengths
1. This paper is well-written, with the authors presenting the algorithm process and their perspectives clearly and comprehensively.
2. Figures 1 and 2 effectively illustrate the authors' viewpoints in a clear and intuitive way.
3. The proposed method demonstrates efficiency and achieves state-of-the-art performance compared to baseline methods.

### Weaknesses
1. This paper demonstrates limited innovation. The proposed method comprises three main parts: the first part provides a conventional description of neural network structure; the second generates a dataset, but the symbolic formula generation method follows that of Kamienny et al. (2022). The third part introduces two loss functions in the training process, with the first being the standard mean square error. Overall, the paper offers little originality.
2. Could larger datasets be used for experimentation? The datasets in this study are relatively small, such as Strogatz (14 problems) and Feynman (119 problems).
3. The proposed method relies on training with a substantial dataset (1.3 billion), while other methods have not been trained on datasets of this scale. This raises the question of whether the method’s effectiveness is largely attributable to the extensive volume of training data.

### Questions
1. In Table 1, the second-best methods are DSR (Petersen et al., 2021) and AIFeynman2 (Udrescu et al., 2020). These methods from 2020 and 2021 not only outperform those from 2022, 2023, and 2024 significantly but also achieve results up to four times greater. Could this discrepancy be due to variations in experimental settings?
2. The proposed method is trained on an extensive dataset (1.3B), while the other methods were trained on considerably smaller datasets. Could an ablation study be conducted, where all methods are trained on the same dataset to enable a more direct performance comparison?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Existing symbolic regression frameworks operate by searching through the space of functions as vectors, minimizing a norm on the input-output behavior of the function. This paper instead approximates a search on the syntactic space of functions by computing a proxy metric for the minimum description length of the function necessary to take a given set of subcomponents and compute the full function. To do this, a synthetic dataset of functions is created and used to train a model that predicts a matching between functions and I/O behavior. The same dataset is then used to finetune this model to predict minimum description length. Overall, the model generally outperforms existing baselines, with particularly good relative performance in the case of noise.

### Strengths
This paper has a very elegant approach to the problem of symbolic regression, taking a principled approach towards the search process. Despite the theoretically intractable nature of the objective function selected, in practice it seems that a transformer is able to learn it well enough to make this search strategy better than existing strategies relying on end-to-end behavior. The resulting framework is more robust to noise than existing frameworks and more generalizable to a variety of domains. The results seem quite strong, with the only unfavorable result being underperformance relative to AIFeynman2 on the Feynman dataset in the absence of noise, which seems like a fairly narrow and understandable failure case.

### Weaknesses
Firstly, the datasets being evaluated on seem relatively small and thus potentially prone to being covered by the dataset. However, this seems to be a relatively standard convention that the related work follows, so I am not particularly concerned about this.

Secondly, the example in Figure 6 seems to suggest that there are very few alternate formulas that could be selected, and yet the recovery rate of this algorithm on the Feynman dataset is below 50%. Is this example atypical or is the search tree large even when heavily pruned? An explanation either way would be helpful (e.g., raw fractions for what the 4%, 0.2%, etc., are might clarify this if e.g., 4% is still 100 possibilities).

MInor:

Figure 6 and description: the blue sector description should probably say “all T that are lower according to the model than T^*” and emphasize that these are incorrect search paths -- it is a bit confusing to read otherwise. The caption does this better than the label on the  graph itself or the paragraph describing the figure.
471-472: “finding that nearly few” I think you mean “very few” or “nearly none”.
482: “for each of the three wheres” I think you mean “for each of the three strategies”
Figure 7: there are no axis labels for the right axis for d e and f.

Extremely minor nit: for figure 7 when you have two axes you color the left axis labels black and the right axis green, while the lines are blue and green. The axis labels should either both be black or blue and green.

### Questions
You say you sample D in line 215, which makes sense, since you need D to create the formula. However, you again sample D in line 221. However, here, shouldn’t D be the dimensionality of f?

I assume that the auxiliary loss on line 252 is computed per-batch? If so, this should be noted. If not, I would like more details on how this is done.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a fundamental challenge in symbolic regression: the traditional search objective, namely prediction error, is non-monotonic, which limits the effectiveness of the search process. The authors propose a novel approach by training a neural network called MDLformer to tackle this. This model introduces a new objective function to efficiently guide the formula search. The experimental results demonstrate that the proposed method significantly outperforms existing approaches.

### Strengths
- The overall idea of this paper is intuitive and reasonable. The traditional search objective, i.e., prediction error, cannot effectively capture the distance between the target and current formulas.
- The experimental results are promising. The proposed method significantly outperforms existing methods, demonstrating that a more sophisticated objective can help improve the recovery rate.

### Weaknesses
 - The evaluation dataset is limited. Unlike existing studies, this paper aims to introduce a neural network to guide the search process. As a result, it is crucial to comprehensively assess whether this model can generalize well on other tasks. However, the two datasets used in this study are relatively small. For instance, the Strogatz dataset only includes 14 problems, which is insufficient to effectively capture the performance of each method. Therefore, incorporating additional datasets [1] is necessary to thoroughly evaluate the proposed approach.
- The proposed MDLformer model requires an in-depth discussion. Firstly, the method generates synthetic data to train the model. How do the authors ensure that this synthetic data generalizes effectively across various downstream tasks? Secondly, with 131 million data points generated, how does the model’s performance change as the data scale increases, and does it eventually reach performance convergence?
- The technical section should be clear and self-contained. Although the concept of Minimum Description Length (MDL) originates from existing studies, further clarity is needed on its technical details, such as how it is computed in the proposed method. At present, the technical content is somewhat difficult to follow.

### Questions
- The data contamination problem should be further discussed. The authors generate 131 million data points, which poses a potential risk of overlap between training data and testing data. Does the generated data introduce contamination problems, and how can this problem be avoided in the data generation process?
- Some related studies should be discussed. Many recent studies [1] focus on adopting neural networks for symbolic reasoning. The authors should provide a brief discussion about the differences and advantages of the proposed method.

[1] A-NeSI: A Scalable Approximate Method for Probabilistic Neurosymbolic Inference. NeurIPS 2023.

### Soundness
3

### Presentation
2

### Contribution
3
