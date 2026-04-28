# NESTLE: An Efficient and Robust Data Valuation Framework for Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 8, 5

## Abstract
The training and fine-tuning of large language models (LLMs) heavily rely on a large corpus of high-quality data. Nevertheless, the internet's extensive data is often of varying quality, and collecting high-quality data is exceedingly expensive. To facilitate data engineering and trading, the quantification of data value, also known as data valuation, is emerging as a critical topic. Traditional approaches for data valuation typically depend on model retraining. However, with the increasing model sizes and expansive data volumes of LLMs, these conventional methods are encountering significant declines in valuation precision, efficiency, and transferability. To alleviate these problems, we propose NESTLE, which is an efficient and robust framework for data valuation of LLMs. To accurately estimate the data value distribution across different target domains, we develop a training-free mechanism based on gradient tracing to simulate the data influences. To further tackle the dynamical value adjustment when multiple data providers coexist, we draw inspiration from the Shapley value theory and devise an accelerated strategy for estimating marginal contributions of data through gradient additivity. Extensive experiments demonstrate that our proposed framework NESTLE is capable of accurately and robustly providing accurate estimates of data value with a minuscule cost across a wide range of real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces NESTLE, a data valuation framework. It combines gradient tracing with Shapley value concepts, enabling efficient, valuation across diverse domains and multiple data providers. Extensive experiments demonstrate that the proposed framework is capable of accurately and robustly providing accurate estimates of data value with a much lower cost over benchmarks.

### Strengths
- By using gradient tracing instead of traditional retraining, this method is more efficient and requires less computational power
- The framework’s low-cost gradient-based method scales well with model and dataset sizes, and it shows promising results across domains
- The method is capable of evaluating data from multiple providers

### Weaknesses
 - The paper may benefit from rigorous writing, e.g., on page 2, the authors listed the design principles for a good data valuation framework, essentially a set of axioms, however, there’s no theoretical analysis to formally state that the proposed method satisfy these axioms. A theoretical justification would significantly enhance this paper

- The technical writing can be improved to enhance its readability.
    - Many notations are not defined, e.g., U and N on page 1 line 50, ηa_ bar in Eq (5), beta in eq (6)
    - References look odd, e.g., Kevin Fu Jiang, Weixin Liang, James Y. Zou, and Yongchan Kwon. Opendataval: a unified benchmark for data valuation. *In Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine (eds.),* Neurips, 2023a.

- Clearly state the computational requirement (see below) and contrast with existing work



### Questions
- Does this method provide fairness guarantees of Shapley values?
- Could you elaborate on the memory requirements for caching in relation to some common LLMs, as mentioned in line 218?
- In line 223, the calibration mechanism for the Adam-style optimizer requires the second-order moment. Could you describe the complexity and computational requirements involved?
- Based on Table 6, it appears that the absolute data value is less relevant than the relative value. For instance, even when 100% of the data is already in the training set, it retains a data value of 0.53. How could this be effectively applied in practice?
- To complicate matters, the non-comparable nature of value magnitudes across different LLMs means that some datasets may rank higher for certain models, making it more challenging to draw definitive conclusions. Any thoughts?

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
The goal of the paper is to calculate fair values of the data that comes from different providers. The paper first describes the two broad approaches, that is, the influence function based and Shapley values based approaches. The paper combines aspects from the two approaches. It first uses the gradient information from the influence based procedures to compute the value of the data. This computation is based on the Taylor series expansion and seems to be heavily inspired by existing influence functions (e..g., Koh and Liang). Then noting that multiple providers may have the same utility, leverages SVs to compute the fair valuation of the data. The paper leverages the "additivity property of gradients" to speed up the computation of Shapley values. The result is a method that can compute valuation of fine-tuning data of pretrained models while also accounting for redundancy of data provided by different sources.

### Strengths
1. Valuation of fine-tuning data is an important problem and will likely be highly relevant given that fine-tuning LLMs with domain specific data is a common use-case.

2. The paper sets up the problem and the context quite nicely. It also explains the evaluation desiderata in Section 3.1 very well.

### Weaknesses
The main points where the paper can be significantly improved are (i) lack of novelty, (ii) insufficiently justified assumptions and (iii) unsuitability of the experimental setup. See below for details.

1. The technical novelty of the paper is somewhat limited. The Taylor expansion which underpins the gradient mechanism is already quite well-known in the influence function literature. The usage of Shapley values is also quite common in data valuation literature. The contribution of the paper seems to be a fast way to compute them but the paper does not provide sufficient detail on that computation (more on this point below).

2. Eq. 5: Given that the loss is a mere proxy for the task accuracy, it is not clear how reliable the result of “summing up this formula in all the iterations in which $s_i$ was used to update the parameters” is. For instance, according to [Guo et al](https://arxiv.org/pdf/1706.04599), the accuracy and loss do not always go hand in hand. Does this difference between loss and accuracy, and the non-convexity of deep models have any effect on the reliability of the influence estimate? I think the paper would be greatly strengthened by adding some clarifications here.

3. Eq. 6: The insight that the other parameters of the Adam optimizer should also be considered makes sense on a high level. However, the equation is discussed in a very standalone manner and leads to more questions than answers. Why the first two moments? What is meant by “calibration”? How does the equation generalize to related optimizers like AdamW and SGD+Momentum?

4. The treatment of “domains” in the paper is a bit hand-wavy. Are domains so easy to define in the era of LLMs where the number of tasks one could perform with a LLM is virtually unlimited. Similarly, the update strategy seems to implicitly assume that we have similar number of data points from each domain (the way the losses for each data points are summed up over the iterations). Some domains, however, may contribute much less data and may have a higher loss. Does the paper suggest to train on these domains for longer? How does this impact the loss summation strategy?

5. The text below Eq. 7 is very difficult to parse. The phrase “the required number of training iterations is 7 when there are 3 clients” seems completely out of place. This reviewer is not aware where the additivity property of gradients originates from. A reference would be very helpful. What is the intersection of gradients? How exactly using Eq. 8 removes the need for using all $2^n - 1$ coalitions?

6. Eq.s 7 and 8 also seem to assume that influence is additive across the data points from a single provider. That however is not the case, see [Koh et al](https://arxiv.org/abs/1905.13289).

7. The paper needs to spend a bit more time describing the datasets and why they are 1) appropriate and 2) sufficient for evaluating the proposed method. Are these generation tasks? Why were BLEU and ROUGE-* metrics used? Why not consider semantic similarity metrics?

### Questions
1. Please see weaknesses 1-6.
2. Given that gradients seem to be a gross approximation of the retraining procedure, how does this affect the quality of Shapley Values?
3. Section 3.1: Does one contributor always contribute data from one domain only?
4. Line 165: on the value of k and k’ not increasing: does it mean that after a provider introduces a duplicate dataset, the original as well as the duplicate would get the same score? Doesn’t it contradict line 79 which says that providers with highly similar data should be penalized?
5. Did the authors check that the evaluation datasets are not a part of the pretrained model training set?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces NESTLE, which is a framework that:
- tackles estimating the value of (or, as I interpret it – the information present in) a data point with respect to (wrt) a pool of points
- represents the value of data using model gradients
- can change the data value efficiently wrt multiple pools of data

### Strengths
- Interesting problem statement
- Addresses inherent weaknesses by (1) reducing gradient caching costs and (2) adapting gradient computation to the Adam optimizer
- Added an analysis for runtime, which makes the efficiency claims stronger
- Figure 1 provides cool insights into the delta of value added to datasets as they get larger, demonstrating that large datasets are not necessary for fine-tuning models

### Weaknesses
 - Comparison with multiple data providers (Table 4) is not complete. It would be better if the value estimation were also done on other baselines. The current comparison only shows the performance of NESTLE against LOO and FedCE, but lacks a broader comparison with other data valuation methods, particularly those that also leverage gradient information. This makes it difficult to assess the relative strengths and weaknesses of NESTLE in a comprehensive manner.
- A more thorough analysis on previous works using model gradients for estimating data value would be great, and motivate the paper’s solution much better. A few papers that come to mind are:
1. S. K. Choe et al: “What is Your Data Worth to GPT? LLM-Scale Data Valuation with Influence Functions” 
2. M. Xia et al: “LESS: Selecting Influential Data for Targeted Instruction Tuning”
 The current discussion of related work is insufficient, and does not adequately position NESTLE within the existing literature on gradient-based data valuation. The paper should delve deeper into the specific differences and advantages of NESTLE compared to these methods, especially considering that influence functions are a well-established approach for similar tasks. The motivation for using model gradients is not fully justified without a detailed comparison with these existing methods.
- A nitpicky thing: wrap your citations in parentheses (maybe use `\citep` in latex).

### Questions
I just have one question on top of the suggestions mentioned above: the problem you are trying to solve sounds a lot like active learning. Do you have any experiments in which you compute the value of data, treat the high-valued data as an information-rich subset of the full data, and fine-tune a model on the subset? What are the results?

### Soundness
3

### Presentation
3

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
The paper proposes NESTLE, a framework for conducting data valuation using its influence on the change of the loss. This results in calculating the gradient inner product between the gradient on the dataset and the gradient of the particular data point. To resolve the comupational issues, the authors propose to project the gradients to a lower dimensional space. For dealing with multiple data provider, the authors propose to use concepts in Shapley value to define the marginal gain in each data source. Experiments are conducted to showcase the effectiveness the proposed method.

### Strengths
The paper is well presented. The idea of using gradient inner product to evaluate the influence of the training data is clear and intuitive. To deal with the multi-source setting, using Shapley value to think through this is interesting.

### Weaknesses
My main concern is that the proposed way for calculating the value/influence of a data point in model training (in the single source setting) is almost identical to that proposed in LESS: https://arxiv.org/pdf/2402.04333. For multi-source provider case, the adjustment using the marginal utility of adding a data source is interesting, but unclear to me whether it suffices to be enough contribution.

As it was motivated at the beginning of the paper, one cares about data valuation because of training needs. However, in the experiment section, the evaluation metrics for the proposed methods seem to be sentence statistic based, lacking the connection to model training. Thus, it is hard to assess whether the proposed method will be effective in training.

### Questions
See weakness above. Could you comment on given that there are existing influence-based data selection work (like LESS), how should one value the proposed framework? In addition, if BLEU scores can be used to assess the quality of data valuation, then perhaps one can use it for data valuation directly?

### Soundness
3

### Presentation
3

### Contribution
2
