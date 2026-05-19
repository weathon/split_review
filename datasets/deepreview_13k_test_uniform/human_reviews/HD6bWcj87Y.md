# Data Shapley in One Training Run

- Decision: Accept
- Scores: 10, 6, 8, 6

## Abstract
Data Shapley provides a principled framework for attributing data's contribution within machine learning contexts. However, existing approaches require re-training models on different data subsets, which is computationally intensive, foreclosing their application to large-scale models. Furthermore, they produce the same attribution score for any models produced by running the learning algorithm, meaning they cannot perform targeted attribution towards a specific model obtained from a single run of the algorithm. This paper introduces \emph{In-Run Data Shapley}, which addresses these limitations by offering scalable data attribution for a target model of interest. In its most efficient implementation, our technique incurs negligible additional runtime compared to standard model training. This dramatic efficiency improvement makes it possible to perform data attribution for the foundation model pretraining stage for the first time. We present several case studies that offer fresh insights into pretraining data's contribution and discuss their implications for copyright in generative AI and pretraining data curation.\blfootnote{$^\mathbf{\star}$Correspondence to \textbf{Jiachen T. Wang} and \textbf{Ruoxi Jia} (email: \texttt{tianhaowang@princeton.edu}, \texttt{ruoxijia@vt.edu}).}

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper introduces In-Run Data Shapley, a novel principled way of attributing the data contribution for deep learning models within one training run. A classical Data Shapley technique requires retraining which is computationally prohibitive in practice for large models, and more importantly, it quantifies data contribution for a general learning algorithm, and not for a particular model at hand. Related to this, data contribution for a single model is of crucial importance for properly investigating fairness and copyright implications.

In-Run Data Shapley is powered by the fact that model training is performed iteratively, and Shapley values can be derived analytically for each model update step via gradient dot products or gradient-Hessian-gradient products between training and validation data. The authors propose an efficient method to approximate In-Run Data Shapley values during one training run via first- and second-order Taylor expansions, and compute these values in one and two backpropagation, respectively, inspired by the ghost clipping technique. This incurs negligible computational overhead, making In-Run Data Shapley highly usable in practice. Furthermore, the authors empirically evaluate their approach on Pile dataset, highlighting several important insights re: data curation and cleanliness of the dataset, dynamic data contribution throughout the entire training process, and the degree of data contribution in copyright issues.

### Strengths
The proposed method is novel, efficient and promising. The presentation of the paper is very clear and succinct; technical contributions are clearly stated and rigorously developed. The authors carefully position their work and acknowledge several limitations which they claim will be a part of future work. Empirical evaluation is thorough and the paper raises important observations re: societal implications of the large model training.

### Weaknesses
I do not see any major weaknesses of the paper.
Minor (typo): line 500 - sentence "The results of this experiment..." appears twice in a row

### Questions
I would like to know the authors' opinion of applying the general idea of In-Run Data Shapley to other use-cases in machine learning, such as hyperparameter importance during the HPO run. More generally, do the authors envision transferring this idea to other domains, especially in the case where gradient information is not available?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new technique called "in-run data shapley" to eleminate model retraining for assessing data contributions. This seems a new angle to assess the data attribution and importance. The results shows that this can provide efficiency improvement, and help make more insights for data contribution. The paper also identifies and discussed potential implications for copyright in genAI and pretraining data curation.

### Strengths
1. The motivations, problem statement and objectives and contributions are provided clearly. 

2. The mathematical induction and proof seem solid.

3. The results and implications of the new concept/techniques are described clearly.

### Weaknesses
Compared with the introduction, background, methods and mathematical induction, which are presented clearly, the results and analyses are a bit weak. It would be better to provide concrete examples with more deep analyses.

### Questions
1. Could you please provide an example on how your method used in-run data Shapley to calculate the data contribution? Is it possible to provide a figure? Even using a simple example data set would be very helpful. This cannot be replaced with a loss-time curve. 

2. Is it possible to extend the method to regression and classification problems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel approach called In-Run Data Shapley that eliminates the need for model retraining to evaluate data contributions in machine learning. By leveraging gradient updates within a single training run, the authors develop a computationally efficient method suitable for large-scale models, such as foundation models like GPT-2. The work introduces efficient algorithms using Taylor expansions and techniques inspired by differential privacy to minimise runtime overhead. The study also demonstrates the practical utility of In-Run Data Shapley in data curation and understanding the impact of pretraining data.

### Strengths
* The introduction of In-Run Data Shapley is a significant advancement over existing retraining-based methods, offering a scalable solution to data attribution in large models.
* The case studies, particularly in data curation and copyright implications, highlight the real-world relevance of the proposed method.
* The closed-form derivations for the Shapley values using first- and second-order Taylor approximations are mathematically sound and well-explained.

### Weaknesses
* The method's requirement for validation data to be available before training might limit its applicability in scenarios where such data is not readily available.
* Even though the authors address memory concerns using gradient accumulation, the practicality of this approach in extremely large models with limited resources is not fully explored.
* The first- and second-order Taylor approximations are empirically validated, but there is limited discussion on how these approximations might affect the reliability of the data attribution scores, especially in more complex models.

### Questions
* The method requires validation data to be available before training. Can the authors elaborate on the potential limitations of this requirement and discuss scenarios where this may not be feasible? Are there alternative approaches that could make In-Run Data Shapley applicable when validation data is not pre-available?
* How does the use of first- and second-order Taylor approximations affect the reliability of the Shapley values in practice, especially in highly non-convex or complex loss landscapes? Can the authors provide additional empirical results or theoretical analysis to quantify these approximation errors in diverse settings?
* While the paper demonstrates efficiency improvements, how does the proposed method scale when applied to models even larger than GPT-2 or to models with different architectures, such as transformer-based models with sparse attention mechanisms? Can the authors provide insights or preliminary results on this?

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
4

### Summary
The paper introduces in-run Shapley, a data valuation method for SGD based models that estimates data values in one training run across different update steps. 

The authors further provide enhanced ways of computing these data values with first and second order approximations. 

The method is evaluated on the PILE dataset for GPT-2 and Pythia 4.10 against influence functions and outperforms them.

Remark: Thanks to the clarifications provided by the authors during rebuttal, I have raised Soundness from 2 to 3, Contribution from 3 to 4, and the overall score from 5 to 6.

### Strengths
The paper introduces an interesting and to me novel method to estimate data values in a single training run. This makes data valuation feasible to large scale data sets. Furthermore, the method is evaluated on such a data set.

### Weaknesses
The evaluation is performed against influence functions only. This way it is unclear whether the method only outperforms leave-one-out (approximated by influence functions) or is also better than the standard data Shapley value. 

Other data valuation/pruning methods are dismissed due to scalability issues (Sec 5.3.1). However, to my understanding, both Memorization (Socher et al., 2022, Feldman and Zhang (2020)) and Supervised Prototypes (Socher et al., 2022) should be applicable to larger models and have been implemented on ImageNet scale by Socher et al. I'm uncertain if this generalizes to LLMS, but it should be discussed if not feasible.

It is specifically indicated that TRAK wouldn't scale to LLMs, yet according to my understanding, TRAK can function with checkpoints from a limited number of models (see Appendix "E.3 Proxies for model ensembles in compute-constrained settings" of the TRAK paper).
Given the evaluation of in-run Shapley on large datasets, I would elevate my vote if the authors either compare their method to the ones mentioned above or provide reasons why those methods don't scale to the dataset.

Minor Remarks
--------------------
OpenDataVal is a recent benchmark for data valuation. Although it is designed for small-scale data, it offers ready-to-use implementations of various algorithms and could be employed to benchmark In-Run Shapley against other methods. This would enhance the paper by demonstrating whether In-Run Shapley performs comparably or even superior to the standard Shapley value.
Some references are missing:
* Toneva et al. (2019) demonstrated that data points learned early in training and not forgotten in later epochs are less important to model performance than points that are frequently forgotten. The former can be omitted to reduce dataset size.. This reminds of the method introduced in the paper. 
* Nguyen et al. (2023) proposed "A Bayesian Approach To Analysing Training Data Attribution In Deep Learning" to tackle the noise issue when training multiple models. This problem, referred to as "instability," is also mentioned in this paper but without citing Nguyen et al.

There are a few spelling mistakes especially in Sec. 5.3.3:
* In "data set," the word "set" is missing.
* The sentence "The results of this experiment have important implications for the current discussion on the copyright of generative AI." is repeated.

Sources
-----------
Remark: the reviewer is not the author of any of the papers below.
* Socher et. al (2022): Beyond neural scaling laws: beating power law scaling via data pruning
* Feldman and Zhang (2020): What neural networks memorize and why: Discovering the long tail via influence estimation
* Toneva et. al (2019): An Empirical Study of Example Forgetting during Deep Neural Network Learning
* OpenDataVal (2023): OpenDataVal: a Unified Benchmark for Data Valuation
* Nguyen et. al (2023): A Bayesian Approach To Analysing Training Data Attribution In Deep Learning

### Questions
I want to confirm whether I have understood the definition of the in-run Shapley value for a data point $z$. It is the “cumulative contribution of the data point $z$ across all gradient update iterations within a single training run”. Does this mean that in each gradient update (e.g., for each batch) the Shapley data value w.r.t. to this batch is computed and averaged at the end? This would mean that for each batch $b$ the marginal contribution of $z$ would be estimated on all possible subsets of $b$. 

If so, I would be interested in an intuition how this value is related to the standard Shapley data value. This could be done conceptually but also by experimental evidence, e.g., by comparing the method to other visiting Shapley based estimates, as suggested above.

### Soundness
3

### Presentation
3

### Contribution
4
