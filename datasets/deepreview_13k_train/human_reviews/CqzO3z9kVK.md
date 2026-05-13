# Knowledge Fusion by Evolving Language Models

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Fine-tuning pre-trained language models, particularly large language models, demands extensive computing resources and can result in varying performance outcomes across different domains and datasets.
	This paper examines the approach of integrating multiple models from diverse training scenarios into a unified model. 
	This unified model excels across various data domains and exhibits the ability to generalize well on out-of-domain data. 
	We propose a knowledge fusion method named \ourapproach, inspired by evolutionary algorithms, which does not need further training or additional training data.
	Specifically, our method involves aggregating the weights of different language models into a population and subsequently generating offspring models through mutation and crossover operations. 
	These offspring models are then evaluated against their parents, allowing for the preservation of those models that show enhanced performance on development datasets.
	Importantly, our model evolving strategy can be seamlessly integrated with existing model merging frameworks, offering a versatile tool for model enhancement. 
Experimental results on mainstream language models (i.e., encoder-only, decoder-only, encoder-decoder) reveal that \ourapproach outperforms previous state-of-the-art models by large margins.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of knowledge fusion across multiple models, which would help with modularity and promises to improve performance on in domain and out of domain tasks. 

The presented method is based on evolutionary algorithms, where multiple models are initially trained and then evolved and recombined into new models over multiple rounds. Development sets are needed to guide the evolution process across rounds. The method can be combined with model merging approaches, which in contrast, perform knowledge fusion across a single round.

The experiments are performed on the same experimental setups as in the paper introducing RegMean, including the same setups, data sets and initializations.  Results show that the evolutionary algorithm performs better than other methods like greedy soup and mostly better than Fisher-weighted averaging, albeit usually lower than the best model merging method. However, when combined with model merging approaches like RegMean and Fisher-weighted averaging, it leads to significantly better results than evolution or merging alone.

The novelty of the paper is the experimental results and application of existing approaches in evolutionary algorithms to this problem of knowledge fusion. The experimental setup and algorithm are not novel.

### Strengths
The results are positive and consistent.

Solid evaluation setup.

The interpretation of the results is quite intuitive regarding removing the models with low performance, which was observed also as a weakness in past work.

Sensitivity analyses conducted.

### Weaknesses
The limitation of having enough development data for each domain for the evolution could be a strong constraint for the data privacy setup, which could limit the applicability of the method and was an important selling point for model merging. This just needs to be highlighted better in the paper.

It would have been good to test the approach also with encoder-decoder (like in the RegMean paper) or with decoder-only architectures, to establish more generality.

### Questions
The paper should be checked for typos

e.g. Table 1  Faderated > Federated

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to evolve models with mutation and crossover operations over a set of trained models. The algorithm can be built upon different model merging strategies such as Fisher-weighted averaging and RegMean and improves performance over merged models without mutation.

### Strengths
- The idea of applying mutation algorithms to create a merged model out of existing models is inspiring and we see clear performance improvement over counterparts without mutation.
- I appreciate combination of mutation algorithms with different model merging approaches
- Ablation studies and hyperparameter sensitivity analysis in Sec 5.4 is quite useful.

### Weaknesses
 - In my perspective, the major issue is the presentation of the paper.

I find the design of the diagrams, tables, and experiment setups overly similar to a paper authors cited [1], namely Figure 1, Table 2, Table 3. At first glance, I was very confused because of the similarity; until I realized that the submission indeed proposes novel ideas and present interesting new results. 

I believe whether the similarity matters is subjective, as it is inevitable for follow-up studies to apply the same experiment setups. Therefore, I would like to hand over the issue to the Area Chair. At the same time, I hope to hear from authors about any plans to modify layouts of Figure 1, Table 2, Table 3 to avoid potential confusion.

There are also other minor writing issues in the paper, like, citations should not be in parenthesis when the authors are included in a sentence.

- Issue with the evaluation

The authors assumes a setup where a develop set is available to evaluate the performance of merged and individual models. In this case, an intuitive baseline is to tune the coefficient $\alpha$ of models to be merged, Merged = $\alpha$ Model1 + $(1-\alpha)$ Model2 , like as Matena et al. or [2]. Especially in the setup of merging only two models, I don't see a reason how the proposed approach can outperform coefficient search.

### Questions
- What is the performance of merged models with simple average / regmean / fisher-weighted averaging when you apply coefficient search? Does the proposed approach improve over coefficient search?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors introduce a novel approach to knowledge fusion called model evolution, which draws inspiration from evolutionary algorithms. This technique involves pooling the weights of various language models into a population and then generating new models through mutation and crossover operations. The performance of these new models is subsequently assessed, and those exhibiting superior performance are retained. This approach not only attains results comparable to prior merging methods but can also be used in conjunction with them to achieve even better performance.

### Strengths
The motivation is clear and the research question is very interesting: The fusion of knowledge and strengths from individual language models is crucial as it can enhance the performance of a single model with minimal computational and time costs. The author has devised a novel method utilizing evolutionary algorithms for model merging.

### Weaknesses
1. The paper suggests the direct application of existing evolutionary algorithms for knowledge fusion, which is of limited novelty, yet it lacks an explanation for why evolutionary algorithms can ensure convergence to an optimal result. Furthermore, there is a significant concern regarding the substantial search cost incurred during the evolution process.

2. Absence of experiments involving natural language generation and other model architectures (e.g., encoder-decoder or decoder-only): All experiments are based on the encoder-only model for natural language understanding tasks. It would be valuable to observe experiments using encoder-decoder or decoder-only models, especially in natural language generation tasks.

3. The presentation of this paper is subpar. In addition to language issues, numerous crucial concepts are not explained clearly.

### Questions
1.   What are the implementation details of combining evolver with other model merging methods?
2.   What are the details of Avg. *f*1*..*N, Best. *f*1*..*N, Domain-Specific, and MTL? Especially, what is the difference between Best. *f*1*..*N and Domain-Specific?
3.   Seems that cannot find the details of Section 5.1.3 in Appendix B.
4. It appears that the search cost during the evolutionary process is substantial. While the authors have conducted an analysis of time consumption, I am left wondering about the magnitude of this time cost when compared to other methods. Additionally, I'm interested in understanding how to ensure convergence to an optimal result.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a knowledge fusion method inspired by evolutionary algorithms, which doesn't require additional training or data. The method involves aggregating language model weights into a population and generating offspring models through mutation and crossover operations.The proposed method outperforms previous approaches on various settings.

### Strengths
+ The paper introduces a novel knowledge fusion method inspired by evolutionary algorithms. This approach doesn't require additional training or data, making it unique in the realm of NLP research.
+ The paper conducts rigorous evaluation experiments, providing empirical evidence that their proposed method significantly outperforms previous approaches.

### Weaknesses
 + The motivation is unclear. Authors mentioned in the introduction part that multi-task learning is one of the two main-stream knowledge fusion methods but it suffers from high annotation cost and complex algorithm. However, I can't see why multi-task learning would be more data-hungry than first training individual models on each dataset and then merging them into a single one. As for the second limitation, still, I am not convinced that multi-task learning would be more complex than existing model merging algorithms.  Moreover, the author postulate that model merging is an optimization problem. However, there seems to be no further explanation, e.g., what is the goal of the optimization "problem"? 
+ Table 1 is Confusing. What do you mean by "round" and "key step"? More explanation is in need.
+ The structure of the submission still have rooms for improvement. For example, 3.1 is not necessarily a preliminary or premise to understand the method. Therefore I would suggest moving this part to related work. Besides, the experiments in Section 5.4 Ablation Study are not ablation experiments but hyper-parameter analysis, strictly speaking.
+ Missing related work. The task arithmetic  should be discussed, with EDITING MODELS WITH TASK ARITHMETIC as a representative example.

### Questions
See the weakness above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
