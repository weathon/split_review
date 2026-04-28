# Anytime Neural Architecture Search on Tabular Data

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
The increasing demand for tabular data analysis calls for transitioning from manual architecture design to Neural Architecture Search (NAS).
This transition demands an efficient and responsive \textit{anytime NAS} \atlasname that is capable of returning current optimal architectures within any given time budget while progressively enhancing architecture quality with increased budget allocation.
However, the area of research on Anytime NAS for tabular data remains unexplored.
To this end, we introduce ATLAS, the first anytime NAS \atlasname tailored for tabular data.
ATLAS introduces a novel two-phase
\filter-and-\refine
optimization scheme with joint optimization, combining the strengths of both paradigms of training-free and training-based architecture evaluation.
Specifically, in the \filter phase, ATLAS employs a new zero-cost proxy specifically designed for tabular data to efficiently estimate the performance of candidate architectures, thereby obtaining a set of promising architectures.
Subsequently, in the \refine phase, ATLAS leverages a fixed-budget search algorithm to schedule the training of the promising candidates, so as to accurately identify the optimal architecture.
To jointly optimize the two phases for anytime NAS, we also devise a budget-aware coordinator that delivers high NAS performance within constraints.
Experimental evaluations demonstrate that our ATLAS can obtain a good-performing architecture within any predefined time budget and return better architectures as and when a new time budget is made available. Overall, it reduces the search time on tabular data by up to 82.75x compared to existing NAS approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a neural architecture search (NAS) method for tabular data. The proposed method, termed ATLAS, leverages a training-free metric for multi-layer perceptron (MLP) to estimate the architecture performances at low cost. After the filtering phase using the training-free metric, it searches for a better architecture using the accurate training-based architecture evaluation. In the proposed two-phase search strategy, the switching timing is determined based on a given search budget to improve the anytime performance. The effectiveness of the proposed method is evaluated on the NAS problem of finding the best number of units in each layer of MLP.

### Strengths
- The NAS tabular data benchmark constructed in this work will be useful for the community. It would be great if the authors released the dataset publicly.
- The thoughtful experimental evaluation is conducted. The proposed training-free metric, ExpressFlow, empirically shows better correlations with the actual performance compared to several existing training-free metrics. Also, the anytime performance of the proposed method clearly outperforms the baselines.
- The paper is generally well-written and easy to follow.

### Weaknesses
 - The performance evaluation is conducted using the limited search space that decides the number of hidden units in each layer of MLP. The effectiveness of the proposed method on other architecture search spaces, such as Transformer-based architectures and other components of MLP, is unclear. Specifically, the search space is limited to varying the number of hidden units within each layer of a multi-layer perceptron, which does not explore other critical architectural choices such as different activation functions, skip connections, or normalization layers. This narrow focus makes it difficult to assess the generalizability of the proposed method to more complex and diverse neural network architectures. For example, the method's performance on architectures with attention mechanisms or convolutional layers, which are commonly used in other domains, remains unknown. Furthermore, the evaluation does not consider the impact of different optimization algorithms or learning rate schedules, which could significantly affect the performance of the searched architectures. The lack of exploration of these aspects limits the practical applicability of the proposed method in real-world scenarios where diverse architectural choices and optimization strategies are often necessary.

### Questions
- Could you comment on the applicability and expected behavior of the proposed method on other kinds of architecture search spaces other than the search space used in this paper?
- Is it possible to apply the proposed method to a situation where the additional budget will be available after the algorithm starts?

----- After the rebuttal -----

Thank you for answering my question.

The authors' responses are convincing to me. I would be happy if the discussion regarding my questions were added to the revised paper.
I keep my score to the acceptance side.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an approach called ATLAS, which focuses on Anytime Neural Architecture Search (NAS) specifically designed for analyzing tabular data, an area that has not been extensively explored in NAS research. With the aim of addressing the need for efficient NAS methods that can accommodate different time constraints, ATLAS presents a two-phase optimization strategy that cleverly combines training-free and training-based evaluations.  Experimental results demonstrate ATLAS's ability to quickly deliver competent architectures while adapting to expanded time budgets. Compared to conventional NAS methods, ATLAS achieves a remarkable reduction in search times, up to 82.75 times faster. These findings highlight the effectiveness and efficiency of ATLAS in the context of tabular data analysis, showcasing its potential for accelerating the NAS process.

### Strengths
1) The development of ATLAS as the first Anytime NAS approach specifically for tabular data is a significant advantage and the main contribution of the paper. It fills a gap in the field of neural architecture search by providing a solution tailored to tabular datasets. ATLAS's innovative approach allows for the adaptation to any given time constraint, ensuring that the best possible architecture is available within the set time frame and can improve if more time is allocated. This responsiveness to computational budget constraints is a substantial step forward for practical applications of NAS in real-world scenarios where time and resources are often limited.

2) The paper is well-written and positioned within the existing body of literature. The paper is commended for its clear writing, which concisely explains complex technical processes. It lays out the limitations of current approaches and systematically introduces the novel contributions of ATLAS, establishing its significance in the context of NAS research. The authors have ensured that the paper is not only informative but also accessible, making it a valuable addition to the academic discourse on neural architecture search.

### Weaknesses
1) A limitation of the paper is the selection of benchmark datasets that may not comprehensively represent the diversity of real-world tabular data. The features of the chosen datasets—Frappe, Diabetes, and Criteo—are relatively low in dimensionality (10, 43, and 39 features, respectively). This narrow scope could potentially limit the generalizability of the study's findings. To convincingly argue the efficacy of ATLAS across various scenarios, it would be beneficial to test it on a wider range of datasets with varying feature dimensions, complexity, and domain-specific challenges. The current dataset selection might not fully challenge the capability of ATLAS to handle higher-dimensional and more complex tabular datasets that are commonly found in practice.

2) The missing significant baselines, particularly established methods such as XGBoost and various Transformer-based models like TabTransformer and FTTransformer. Including these baselines is crucial for a comprehensive comparative analysis, especially to substantiate the necessity and superiority of NAS in the domain of tabular data. By neglecting to compare ATLAS against these well-known and widely-used methods, the paper misses an opportunity to demonstrate the practical advantage of NAS for tabular data over more traditional, yet powerful, approaches. This comparative analysis is essential to persuade the research community and industry practitioners of the added value that ATLAS and, more broadly, NAS methods may provide in tabular data applications.

### Questions
Resolve the concerns in Weakness section.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new NAS algorithms for tabular data, which is based on both zero-cost proxies for distinguishing between good and bad architectures, as well as a multi-fidelity method (Successive Halving) for allocating budget to these promising architectures selected in the first phase. Another contribution of this paper is the creation of NAS-Bench-Tabular, which comprises a search space with a total of 160k unique trained and evaluated architectures. A new zero-cost proxy, tailored for tabular data, is theoretically derived and is compared to existing zero-cost proxies previously designed for vision tasks, exhibiting better performance in the selected benchmarks.

### Strengths
- The motivation to work on anytime NAS algorithms for tabular data is valid considering the significance of the problem and domain.

- The *ExpressFlow* zero-cost proxy (ZCP) is specifically tailored to the tabular modality and is justified by a thorough theoretical derivation and later backed by empirical results.

- The authors propose and construct a new NAS benchmark for tabular data, named NAS-Bench-Tabular. The search space is exhaustively evaluated over 3 datasets. This is certainly very useful for the community, as the previous NAS benchmarks have been, and I am certain it will accelerate the research speed on NAS for tabular data.  

- The proposed ZCP is fairly compared to other state-of-the-art ZCPs that were designed mainly for the image domain and the respective architectures, and the results show that *ExpressFlow* outperforms them by a considerable margin.

- The idea to incorporate *ExpressFlow* into regularized evolution to evolve a population of architectures that optimize the ZCP and then run SuccessiveHalving to allocate budget to more promising configurations inside the evolved population is simple and effective.

- The paper is easy to follow and I really enjoyed reading it. The experimental setup and results are demonstrated clearly.

- The authors provide the code necessary to reproduce the results in the paper.

### Weaknesses
Despite the strengths I mentioned above, there are some really important points that have to be addressed, especially regarding the empirical evaluation.  

- **Benchmark needs to be more diverse for practical purposes**: I think that the creation of NAS-Bench-Tabular is very useful, however when it comes to tabular data, a lot of datasets contain just a handful of training examples (less than 1000), and more features than the datasets the authors chose. Refer to [1] (Table 9 in the appendix) for an example. Specifically, the datasets used in the benchmark seem to be biased towards larger sample sizes and relatively low dimensionality, which is not representative of many real-world tabular datasets. This limits the generalizability of the findings. Datasets with fewer samples and a higher number of features are common in domains like medical diagnostics or financial modeling, and the performance of the proposed method on these types of datasets is unknown.

- **Evaluation of ATLAS on more diverse datasets**: This paper contains multiple contributions, starting from the proposal of a new NAS benchmark for tabular data to the NAS algorithm for tabular data. While these are very useful and provide interesting insights, it can also introduce many biases. Typically, one would design an algorithm that works on benchmarks (real ones) that the community already uses in their research. Firstly designing a NAS benchmark for tabular data and then proposing a method and evaluating it only on that benchmark does not guarantee the same behavior on the real benchmarks. Therefore, I would really be interested to see how ATLAS works on commonly used OpenML tabular benchmarks (e.g. the ones from [1], Table 9), that are more diverse and lie more into the small-data regime. If the authors provide competitive results on those datasets, I am willing to increase my score. The lack of evaluation on established benchmarks makes it difficult to assess the true impact and practical applicability of the proposed method. It is crucial to demonstrate that the method performs well on datasets that are widely used and considered challenging by the community.

- **Comparison with conventional tree-based models**: To assess the usefulness of ATLAS in practice, I think the authors should compare the best found network with conventional tree-based models, as it is done in [1], [2] and [3], for instance. An easy and fair experimental setup would be: (1) Run ATLAS for a given time budget to find architecture **x**; (2) Train and evaluate **X** on the full fidelity (if not already evaluated in (1)); (3) Run tree-based models for *t* time (total runtime of (1) + runtime of (2)). The absence of such a comparison makes it hard to determine if the added complexity of NAS is justified compared to simpler, well-established methods. Tree-based models are often strong baselines for tabular data, and showing that ATLAS can outperform them is essential to demonstrate its practical value.

- **Comparison to SOTA for DL for tabular data**: A thorough comparison to neural networks that achieve SOTA for tabular data is necessary to highlight the usefulness of NAS in this domain. Similar to the point above I would recommend the authors to compare to TabPFN [3]. If the time permits, I would recommend the authors to run ATLAS on the same settings the TabPFN authors used to obtain Figure 5 in their paper. Without a comparison to state-of-the-art deep learning methods for tabular data, it is difficult to assess whether the proposed NAS approach offers a significant advantage. It is important to show that ATLAS can achieve competitive or superior performance compared to existing methods that are specifically designed for tabular data.

**Minor**

- It would be great if the authors follow the already used nomenclature when referring to zero-cost proxies, and not rename them to TRAILERs.

- In Section 2, third paragraph, it is written "The performance obtained by the training-based architecture evaluation approaches is accurate", however this is not always the case, especially when considering proxy models (less layers, channels, etc.) or performance evaluation based on the one-shot model weights (e.g. as in DARTS).

- Most of blackbox algorithms are also anytime algorithms, and they are widely used for NAS as well. Therefore, the claim that ATLAS is the first NAS anytime algorithm (in abstract) for tabular data is wrong considering that the architectural parameters have been optimized using these methods (e.g. Bayesian Optimization) and could easily be used to optimize architectural hyperparameters for tabular data networks as well. Ideally, one wants an optimization method that is modality agnostic. ATLAS is the first anytime algorithm tailored for tabular data because of *ExpressFlow* is designed for tabular data. And yes, *ExpressFlow* is the first zero-cost proxy designed for tabular data, so I would emphasize that instead.

### Questions
- Why did the authors pick those 3 datasets for their benchmark? Is it because of the large number of training examples?

- Is ATLAS performant on datasets with less than 1000 data points?

- How many data points were used to compute the rank correlation in Table 1?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The contribution of paper consists of three works. First, they construct NAS-Bench-Tabular, a DNN-based search space for tabular data. Second, they propose a novel performance proxy of neural network, ExpressFlow. ExpressFlow is based on neuron saliency, but also reflects the difference of importance with depth. Finally, they propose ATLAS, a NAS approach to tabular data.

### Strengths
To the best of my knowledge, this paper is the first NAS benchmark for tabular data. This work will reduce unnecessary redundant experimentation with NAS for tabular data. The proposed ExpressFlow and ATLAS show better performance than the existing Tabular NAS method despite having a relatively simple structure.

### Weaknesses
The search space of NAS-Bench-Tabular(5-layer DNN with different width) is too simple. This search space do not contain most of modern neural network architecture for tabular data[1].

Most of the candidate architectures get similar 97~98% accuracy on Frappe dataset. I wonder how stable the recorded accuracies are.

All three datasets are about binary classification tasks. Regression, Multi-class classification tasks are needed.

DNNs are not the dominant methodology for tabular data, and machine learning techniques such as XGBoost and CatBoost have shown competitive performance [1]. With a limited search space for DNNs, it's hard to see how ATLAS has an advantage over models like AutoSklearn[2] and AutoGluon[3].

### Questions
In general, performance proxies have the advantage of being data type-agnostic, which is also a benefit of deep learning. Why do we need a TRAILER that specializes in tabular data? And what makes ExpressFlow specializes on tabular data?

In Equation 2, aren’t Successive Halving Algorithm allocates different budget U and candidate K for each round?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
