# Less is More: Adaptive Coverage for Synthetic Training Data

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Synthetic training data generation with Large Language Models (LLMs) like Google's Gemma and OpenAI's GPT offer a promising solution to the challenge of obtaining large, labeled datasets for training classifiers, especially when rapid model deployment is critical, such as classifying emerging social media trends or combating new forms of online abuse tied to current events. While prior research has examined the comparability of synthetic data to human-labeled data, this study introduces a novel sampling algorithm based on the maximum coverage problem to select a representative subset from a synthetically generated dataset. Our results demonstrate that training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset. This ``less is more'' approach not only improves accuracy but also reduces the volume of data required, leading to potentially more efficient training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to take better usage of LLM generated synthetic training data, Specifically, how to downsample large synthetic datasets to select the most informative and diverse subset of data points for training machine learning models. The paper proposes a novel binary search algorithm that determines the optimal configuration for max coverage sampling. The main idea is to first embed the data into a latent space and construct a similarity graph where nodes represent data points and edges are weighted by pairwise cosine similarity. On this graph,   a greedy max-coverage approximation algorithm is applied to  prune edges through a binary search procedure to identify the best k ”representative” samples for fine-tuning a model on various downstream tasks.

### Strengths
It is an important task for selecting LLM-generated samples.

### Weaknesses
W1: The selection process begins with constructing a similarity graph, which incurs significant computational cost due to its quadratic complexity relative to the number of data points. According to the evaluation results, this costly approach only marginally outperforms simpler methods like k-means clustering. This raises the question of whether the additional computational expense is justified, and if such a complex selection process is truly necessary.

W2: The selection process operates independently of any machine learning model training, which means it does not necessarily guarantee an “optimal” subset for the intended learning tasks. This raises concerns about its effectiveness in selecting subsets that are truly beneficial for model performance.

W3: The writing should be improved. There are a lot of minor mistakes, such as “cu- rated dataset”, “Chen et al.” (without year in citation),” (Algorithm ??)”

### Questions
Q1: It remains unclear how this selection process addresses key issues associated with LLM-generated synthetic data, such as deviations in distribution from real-world data and imbalanced class distributions. How does this method ensure that the selected subset effectively mitigates these potential issues in synthetic datasets? Further clarification is needed on this point.

Q2: There is no comparison with the closely related work (Chen et al)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper claims an idea that training a classifier on the contextually sampled subset achieves superior performance compared to training on the entire  dataset and creates a novel sampling algorithm named Adaptive Coverage Sampling to select the representative subset from a synthetically generated dataset. In the paper, the author theoretically proves the effectiveness and correctness of ACS and demonstrates it through empirical experiments.

### Strengths
In order to select a good representative subset from the data set, the author uses a new binary search algorithm to determine the threshold of cosine similarity between data points. Two data points are connected if the similarity between them is greater than the threshold. At the same time, a concept  'coverage' is creatively proposed to represent the probability that the points on the graph are adjacent to or overlap with the selected points. The point selection method that maximizes this coverage makes the final selected data subset.

This method of choosing a representative subset is of great originality. Then, the author explains the process and effectiveness of ACS, which is logical and concise. What's more, the research on the selection of synthetic data is also very meaningful.

### Weaknesses
Firstly, i think it mains a question that how to determine the value of k (percentage of data) when trying to get a representative subset of the whole dataset. In another word, if i want to use this method to choose a representative subset of a synthetic dataset, what percent should i retain? 

Secondly, there lacks a legend to explain the meaning of the dotted lines in the figures on section 5, I read this section several times just to find your result of models trained on whole dataset.

### Questions
According to my understanding of your paper, the execution process of ACS is to first determine the value of coverage, then calculate the similarity threshold through binary search according to the value of coverage, then build the similarity graph, and finally select the data points by greedy method. But i can't see what the value of coverage you use for the experiment on section 5, can you explain it?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose Adaptive Coverage Sampling (ACS), a novel method designed to optimize synthetic training data selection，which can identify a representative, diverse subset from large synthetic datasets, improving training efficiency and model accuracy. They use a max coverage sampling algorithm with binary search on similarity graphs to achieve an optimal coverage threshold. The experiments demonstrate that ACS can significantly improve performance on downstream tasks such as sentiment analysis and relation extraction, using only a fraction of the synthetic data.

### Strengths
1.	This study addresses an important and common issue in synthetic data applications, optimizing synthetic data usage by focusing on selecting representative subsets.
2.	The authors present a comprehensive empirical analysis of their ACS method.
3.	The experiments are conducted extensively, spanning multiple tasks such as sentiment analysis and relation extraction, and analyzed in detail, which demonstrates the versatility of ACS.

### Weaknesses
1.	It would be beneficial for the paper to include an ablation study analyzing the impact of the two constraints used in ACS. Specifically, the paper should investigate the effect of varying the maximum outdegree parameter and the minimum similarity threshold on the performance of the model. This would help clarify the role each constraint plays in the sampling process and its contribution to overall model performance. For example, how does the model performance change when the maximum outdegree is significantly reduced or increased, and what is the impact of varying the similarity threshold between 0.5 and 0.9? 
2.	The paper only compares ACS with a few basic sampling approaches (e.g., random and k-means). Including more relevant baselines, such as Alpagasus, could provide a more comprehensive view of ACS’s advantages and limitations. Furthermore, it would be beneficial to compare against other state-of-the-art active learning or data selection techniques to better contextualize the performance of ACS.
3.	While the authors mention that ACS enhances data diversity, the experiments focus mainly on accuracy and F1 score. Providing qualitative or quantitative analyses of diversity, such as using metrics like the average pairwise distance between selected samples or visualizing the distribution of the selected data points in the feature space, would strengthen the paper, giving more insight into the diversity aspect of the sampled subsets. It's not clear how the method ensures diversity beyond the coverage metric.
4.	The paper contains some minor typos, such as “Algorithm?? ” on line 341 and 'Pegasus' should be replaced with 'Alpagasus' on line 133.

### Questions
1.	For a new downstream task, how should one set key hyperparameters such as similarity threshold, maximum nearest neighbors, and coverage values? 
2.	How does the proposed method's computational complexity scale with larger datasets?
3.	See the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel sampling strategy, called ACS, for selecting a subset of high-quality samples from a large set of synthetically generated dataset. The main motivation for the strategy is that there is often a lot of redundant samples when generating samples from the large language models, which causes problems for the training (e.g., overfitting on too obvious examples). To deal with this, the method is designed as a maximum coverage problem -- a similarity graph is constructed based on the sample embeddings, the edges are pruned according to a novel binary search procedure and the best k samples are generated. The authors show that this approaches outperforms other baselines and leads to comparable or higher performance than training on the full synthetic dataset.

### Strengths
The authors propose a graph-based solution using a maximum coverage, which is a novel solution for the problem of sampling a set of high-quality samples. In addition, the method is theoretically grounded.

The authors explicitly take randomness into consideration by repeating the fine-tuning of the models over multiple initialisations. This is also clearly shows the strength of the sampling strategy -- it leads to a significantly lower deviation in the fine-tuning results over the baselines, which may point to the fact that the samples are indeed high-quality and the performance is not simply a result of randomness.

The code of the full method is released, which allows for easy replication of the results.

### Weaknesses
There are two main weaknesses of the paper.

1. **Insufficient comparison with existing baselines**

The proposed sampling strategy is compared with 2 baselines -- random selection and k-means clustering. However, there are many strategies for selecting a subset of high-quality samples, such as the core-set selection strategies [1], active learning strategies [2], or some specific that perform similar selection (e.g., identifying and removing noisy samples) such as dataset cartography [3] or datamodels selection [4]. Even though these strategies were designed for human-labelled datasets, I believe they could be used for LLM generated datasets as well -- but may lead to lower performance if not prioritising the specific of synthetic samples.

Comparing with these additional strategies would significantly increase the findings regarding the proposed ACS strategy -- for example by better understanding the benefits of the strategy (e.g., it focuses on dealing with the redundancy which the other strategies may not achieve).

2. **Rather poor presentation/writing**

The writing in the paper is all over the place and would significantly benefit from a major revision of the writing, as there are many inconsistencies, redundant information and hard to follow parts.

First, the experimental setup is discussed in multiple places (Section 3.3; 4.2 and again in 5.1.2), but is not consistent -- one Section mentions $BERT_{large}$ , while other mentions $BERT_{base}$ ; or one mentions that the experiments are repeated 25 times, while other mentions that they are repeated only 5 times.

The introduction of the ACS sampling strategy would benefit from being in its own Section -- currently it is introduced as part of the baselines.

The motivation of the paper is focused on LLM generated text samples and the methodology mentions the fine-tuning of BERT, but Section 4 deals with MNIST (image) dataset and introduces different model. In addition, there is no mention how the synthetic samples were generated for the MNIST dataset (or whether it was even done)

There is a reference to an Algorithm, but no algorithm is provided in the paper (line 341).

The results in Section 4.2 repeated a few times and could be rewritten to be more concise.

The legend in all figures is incomplete and makes the figures hard to interpret. For example, in Figure 2 there are multiple coloured lines, but there is no explanation (in the Figure caption or text) what they represent. Similarly, in Figures 3 and 4 there are dashed green and red lines, but no explanation is provided about what they represent -- I can only assume what they represent based on the results description.

The claims in some places (mainly motivation) are not supported by evidence -- for example line 81. I would suggest adding more references to such claims, mainly when comparing with existing works. In addition, there are parts that would benefit from more explanation -- for example line 287, where a similarity of 0.707 is used because it is a cosine of 45 degrees -- why is this relevant for designing what similarity to use?

It is not clear whether the authors generate the synthetic samples using GPT-3.5, or just use already pre-generated synthetic dataset from other works -- Section 5 mentions both using data from previous work but also reusing their methodology for generating the samples


Also related to the previous weaknesses, the related work is missing many of the existing works on sample selection (e.g., [1, 2, 3, 4]).

**Additional weaknesses and suggestions**

The benefit of ACS strategy is evaluated using only 2 (or 3) rather simple datasets -- I would suggest to include more datasets that may be also more complex. For example, using the GLUE or SuperGLUE benchmark datasets or other commonly used datasets in the text domain.

(minor impact) The synthetic samples are generated only from a single closed large language model (GPT3.5). I would suggest to evaluate the benefit of the ACS strategy on samples generated from open-source models (LLaMA, Mistral, Zephyr) -- also focusing on multiple models to show better generalisability of the results.

### Questions
Did you generate the samples or just reusing the synthetic dataset from other works?

Was there any effort on checking the quality of the generated samples? 

Is there any reason why the existing strategies for selecting a representative subset of samples cannot be used for subsampling the synthetic datasets?

### Soundness
2

### Presentation
3

### Contribution
2
