# PGLearn - An Open-Source Learning Toolkit for Optimal Power Flow

- Decision: Reject
- Scores: 8, 3, 3, 6, 6, 8

## Abstract
Machine learning techniques for Optimal Power Flow (OPF) problems have recently garnered significant attention, reflecting a broader trend of leveraging machine learning to approximate and/or accelerate the resolution of complex optimization problems. These developments are necessitated by the increased volatility and scale in energy production for modern and future grids. However, progress in ML for OPF is hindered by the lack of standardized datasets and evaluation metrics, from generating and solving OPF instances, to training and benchmarking machine learning models. To address this challenge, this paper introduces PGLearn, a comprehensive suite of standardized datasets and evaluation tools for ML and OPF. PGLearn implements realistic data generation procedures that capture both global and local variability, ensuring that datasets are representative of real-world conditions. In addition, it supports multiple OPF formulations, including AC, DC, and second-order cone formulations. Standardized datasets are made publicly available to democratize access to this field, reduce the burden of data generation, and enable the fair comparison of various methodologies. PGLearn also includes a robust toolkit for training, evaluating, and benchmarking machine learning models for OPF, with the goal of standardizing performance evaluation across the field. By promoting open, standardized datasets and evaluation metrics, PGLearn aims at democratizing and accelerating research and innovation in machine learning applications for optimal power flow problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors proposed a library that generates datasets to standardize ML for OPF research. While each study in the literature shows improvement over earlier models, it is hard to fairly compare the model performance across different studies. 

The authors proposed a library that constructs input output pairs to different formulations of the OPF problem (AC-OPF, DC-OPF and second order cone relaxation of AC-OPF) on large middle to large sized test cases. They also address data augmentation issues in the literature that results in a narrow demand range and implement a procedure that captures global larger demand characteristics. The library also contains solvers implemented in efficient libraries to find the corresponding optimal solutions and evaluation metrics to measure model accuracy and computational cost.

### Strengths
1. A typical ML for OPF study goes through the steps of generation of input parameters (e.g. demand), finding corresponding solutions, model training and evaluation. The he authors contribute the literature with a toolkit that standardizes all these processes.
2. I think main contribution of the study is that the proposed library improves  comparability and fair assessment of existing models. Many studies in the literature show improvement over some baselines but are not able to compare against the state of the art. The library enables researchers to compare their approaches with previously reported benchmarks without implementing each specific model.
3. Another contribution is the data augmentation procedure that potentially generates different load characteristics.
4. The library also implements widely solved formulations of OPF using efficiently written solvers.

### Weaknesses
1. There are not many systems implemented in the library and most of them are large systems. Researchers may want to work on smaller systems for proof of concept or visualizing the model behaviour. It would be nice to add them.
2. While the proposed data augmentation method generates wider range of demand dynamics than sampling random factor and multiplying the base load, I am not sure this approach captures the global dynamics. The demand characteristics can differ widely within the hours of a day or among different seasons, which can result in different constraints to bind at the solution. This is mentioned as a limitation, but I think more detailed demand scenarios should be considered to train more reliable NN models.

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors argue that the numerous datasets used in the benchmarking of ACOPF codes, incl. the Grid Optimization Competition with $9M+ in prize money (https://gocompetition.energy.gov/) and Google DeepMind OPFData (https://arxiv.org/pdf/2406.07234), have minor issues, and need to be replaced by their benchmark. The authors consider 65,536 of samples generated for instances on up to 9241 buses (the Pegase project instance), which are smaller than the OPFData (Lovett et al., 2024) with instances on up to 13,659 buses, but bigger than those of PowerModels (Coffrin et al., 2018) on up to 118 buses with 10,000 samples. The authors consider correlated demand perturbations, but do not consider diurnal variations, or similar.

### Strengths
The writeup is reasonably clear.

### Weaknesses
The instances on up to 9241 buses (the Pegase project instance) are smaller than those of the Deepmind OPFData (Lovett et al., 2024) with instances on up to 13,659 buses. 

While considering correlated demand perturbations may improve the realism somewhat, the authors should ideally consider real-world time-series capturing diurnal variations, or similar. Likewise, they could consider time-varying production limits, which are readily available to all market participants in Europe via the ENTSO-E Transparency Platform (https://transparency.entsoe.eu/). 

The supplementary material contains no code, so the code could not checked for reproducibility or usefulness.

### Questions
Have you considered the use of the ENTSO-E Transparency Platform (https://transparency.entsoe.eu/)?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work describes a pipeline for sampling training data of Optimal Power Flow-machine learning tasks. It proposes a unified framework for sampling training data samples for OPF problem based on pre-defined grid models.The proposed  PGLearn implements realistic data generation procedures that capture load-side variability, and a set of OPF formulations are implemented.

### Strengths
* The idea of performing standard sampling of OPF data is constructive and shall help the power systems and machine learning community. 
* The paper calls for a standard implementation and testing of Machine learning for OPF problems, which are important.
* The paper brings our descriptions on a set of metrics on algorithm evaluation.

### Weaknesses
 * The proposed method is still limited to user-defined synthetic settings, while the scalability to other grid models/data distributions, other power system tasks, or settings other than supervised learning are not discussed. Specifically, the method relies on a two-step approach using uniform noise, which fails to capture the complex spatiotemporal correlations inherent in real-world load data. This significantly limits the practical applicability of the generated datasets.
* The contribution is limited to dataset creation and standard testing. No algorithm insights nor new findings of learning to solve optimal power flow problems are reported. The paper does not benchmark a wide range of ML algorithms for OPF, thus failing to demonstrate the utility of the proposed framework for algorithm development.
* Data augmentation is treated as the sole solution for tackling the non-standardized implementation problem for ML-OPF. Are there any other choices, such as sim-to-real transfer, multi-task or meta learning? The paper does not explore alternative approaches to address the challenges of non-standardized implementations, limiting the scope of the work.
* Though the paper claimed considering the correlation between samples, only uniform noises are added in a two-step approach. Uniform sampling is still far away from the real-world load data correlations. And the paper omits the discussion on how the proposed data augmentation approach resembles realistic settings. The lack of realistic load data, which exhibits complex correlations, undermines the practical relevance of the generated datasets.
* The design of standard grid testbed models were rooted in abstraction and representation of real-world transmission grids. However, the paper falls short in explaining in details how the real-world data distribution can be applied to construct dataset for PGLearn. The paper does not provide a clear methodology for incorporating real-world data distributions into the PGLearn framework, limiting its applicability to practical scenarios.
* In the demand sampling part, " The power factor at each node is kept constant, i.e. the active and reactive power at each load is scaled by the same amount." This is not a very realistic setting, as power factor is having variations, and has a big impact on the OPF solutions. This simplification in demand sampling, which assumes a constant power factor, introduces unrealistic constraints that deviate from real-world power system behavior.
* There is no inclusion nor analysis of contingencies in OPF problems. Essentially the introduction mentions renewable uncertainties multiple times, while the proposed method does not address such uncertainty issues. The paper fails to adequately address the impact of contingencies and renewable uncertainties, which are critical aspects of real-world OPF problems.
* The PGLearn module is limited to implementations of few methods by similar group of authors. A more thorough literature review and inclusion of methods are recommended: Zhang, Ling, Yize Chen, and Baosen Zhang. "A convex neural network solver for DCOPF with generalization guarantees." IEEE Transactions on Control of Network Systems 9, no. 2 (2021): 719-730. Zhou, Min, Minghua Chen, and Steven H. Low. "DeepOPF-FT: One deep neural network for multiple AC-OPF problems with flexible topology." IEEE Transactions on Power Systems 38, no. 1 (2022): 964-967. Owerko, Damian, Fernando Gama, and Alejandro Ribeiro. "Unsupervised optimal power flow using graph neural networks." In ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 6885-6889. IEEE, 2024. The limited inclusion of diverse ML algorithms for OPF restricts the scope and impact of the proposed framework.
* It seems the results on the four accuracy metrics and computation metrics are not reported for the implemented methods.

### Questions
I have the following questions regarding the current paper:

* Could the authors point the link to the anonymousrepo? And in these two repos, are the proposed four accuracy metrics and computation metrics realized?
* PGLearn generates a bunch of data in terms of primal and dual solutions. But some more interactive representations shall be considered, e.g., generator/line value w.r.t capacity, prediction error, visualization of solution on grid, correlation between nodes and etc.

Some minor issues and questions:
* in Introduction, "The increased volatility and scale of energy generation in modern and future grids..." Shall be power generation in the scope of OPF. Similarly in the second paragraph: " account for uncertainties in renewable energy generation and/or demand..."
* In Introduction, "previously intractable applications such as real-time risk analysis", yet in this work, there is no discussion on how ML can help with OPF risk.
* "inherent volatility of wind and solar generation creates OPF problems that are, or will be, orders of magnitude larger that today’s instances." Why the increase of volatility will make the OPF instances larger? 
* The PGLib-OPF seems to be an important reference. Could the author explain more on "PGLib-OPF only provides a single snapshot per grid"? Does that mean only one data sample is provided for each power grid model?
* In Appendix A.2.2, the authors mentioned the bus-pair variables were changed to branch on each variable. Could the authors explain more why this has marginal impact on the relaxation? And does this mean the ML model is learning the newly defined variables instead?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces PGLearn, a suite of standardized datasets and evaluation tools designed to advance ML applications in OPF problems. It tries to provide the standard genration of varied data and evaluation metrics by providing realistic datasets that reflect real-world conditions and support multiple OPF formulations.

### Strengths
1. The dataset is timely and important given the current active research in ML for OPF
2. The presentation is clear and easy to follow

### Weaknesses
1. For my best understanding, the paper mainly focus on the dataset introduction, it does not deliver the technical advances in the search field
2. While the datasets aim to capture real-world conditions, unforeseen variability in actual grids, such as sudden changes in renewable generation or unexpected load fluctuations, may still limit the applicability of the models trained on these datasets. The paper's approach to demand scaling, while useful, may not fully capture the complex spatio-temporal correlations present in real-world grid data.
3. It only focus on OPF problems, which may not be fit for the general audience of the ML community. The lack of broader applicability to other optimization problems may limit its impact within the wider ML community.

### Questions
1. The authors are suggested to include a general review on the ML for OPF papers, e.g., how ML are generally applied to OPF problems. There have been several literature review papers on it.

2. The authors are suggested to state clearly whether the kit contains the function to train/test different ML models? If so, please clarify how to integrate the numerious DNN models and approaches; if not, how should the mentioned Metrics be calculated? Is it still done based on the user side to mannually do so?

3. It is also useful to add a set of adversial samples in the dataset for robustness testing under the worst case scenario

4. Can the suite allow users to self-define the problem and use e.g., API calls, to load the generated dataset? It can be helpful if user have some uncommon reformulated OPF formulations and other general optimization formulation

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents PGLearn, a set of datasets and evaluation tools for optimal power flow (OPF), which builds upon the learnings of existing open-source initiatives. Their main contribution relies on including a different data generation process that considers local and global variability, better representing the actual use cases. It supports different formulations of the OPF problem, namely AC, DC, and second-order cone formulations. The motivation behind this resource is to standardize the performance evaluation among the OPF community, which seems to be fragmented and lacking reproducibility between contributions.

### Strengths
- The paper revisited the OPF problem and identified a gap in the existing approaches, such as the sampling strategy. Then, they proposed a better method that considers the correlation between loads and better represents real-life scenarios.
- Including the primal and dual solutions is another novelty, as few existing datasets include the dual, which is something specific research directions need.
- The authors propose a complete pipeline to interact with PGLearn containing standardized datasets, existing optimizers, data augmentation schemes, distinct OPF formulation, and metric calculation.
- The paper is well structured and clear and introduces their contribution smoothly.
- The authors stated clearly the limitations of their contribution

### Weaknesses
 - Algorithm 1, the notation of what you return could be misleading as you used both $(p^d,q^d)$ for referenced demand and sampled demand. It looks as if you are returning the same reference value at the end of the algorithm.
- The sampling strategy needs tuning the $\epsilon$ and global range. You could add more detail on how to pick the values, giving a case or detail why did you choose the quantities you set.
- The supplementary material is not self-explanatory for someone outside of the OPF domain; I can understand each file from what I read in your paper's appendix, but you could have added basic instructions. Without instructions, it is just a folder with h5 files.
- For a work like yours, you should've added an anonymized version of your code to assess how you implemented what you described only with words in the main paper
- If putting the code is restrictive at this stage, you could also give an idea of the workflow of PGLearn so readers can get an idea of what kind of interaction they can have with your dataset.

### Questions
- When you mention having over 1000000 OPF samples, are they all precomputed with your dataset, or do you provide a method to access the results (h5 files)?
- Can you please provide me with step-by-step instructions on empirically using the supplementary material to check your contribution?
- How can you ensure that your sampling strategy stays within normal ranges? Why did you choose the values you picked?
- In section 5.1, what is the main difference between the Optimality gap and the Distance to optimal solution?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper tackles an important issue in the field of machine learning for Optimal Power Flow (OPF) problems by introducing PGLearn, a standardized suite of datasets and evaluation tools. This addresses the lack of uniformity in data and metrics that has hindered progress in this area.

### Strengths
•	The paper presents robust procedures for generating realistic datasets.
•	It offers support for multiple OPF formulations, including AC, DC, and second-order cone models.
•	The dataset is structured in the N-1 contingency format which can be used to enhance power systems reliability.
•	Standardized datasets are made publicly accessible for broader use.
•	A comprehensive toolkit is provided for training, evaluating, and benchmarking machine learning models for OPF.
•	The limitations of the dataset are clearly documented and reported for transparency.

### Weaknesses
•  The input data is generated using a uniform sampling procedure, but in the future to extend the work for Unit Commitment or multi-period OPF, time series data should also be incorporated. For instance, the recent paper "PowerGraph: A Power Grid Benchmark Dataset for Graph Neural Networks" provides an OPF dataset that uses time series data to model input demand.


### Questions
• Could you provide comments on the results of benchmarking the datasets using the provided metrics across different machine-learning methods? A leaderboard would be the easiest way to access and interpret these results.

### Soundness
3

### Presentation
3

### Contribution
3
