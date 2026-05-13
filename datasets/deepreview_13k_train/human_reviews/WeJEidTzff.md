# A Large-scale Dataset and Benchmark for Commuting Origin-Destination Flow Generation

- Decision: Accept
- Scores: 5, 8, 6, 8

## Abstract
Commuting Origin-Destination~(OD) flows are critical inputs for urban planning and transportation, providing crucial information about the population residing in one region and working in another within an interested area. Due to the high cost of data collection, researchers have developed physical and computational models to generate commuting OD flows using readily available urban attributes, such as sociodemographics and points of interest, for cities lacking historical OD flows \textemdash commuting OD flow generation. Existing works developed models based on different techniques and achieved improvement on different datasets with different evaluation metrics, which hinderes establishing a unified standard for comparing model performance. To bridge this gap, we introduce a large-scale dataset containing commuting OD flows for 3,333 areas including a wide range of urban environments around the United States. Based on that, we benchmark widely used models for commuting OD flow generation. We surprisingly find that the network-based generative models achieve the optimal performance in terms of both precision and generalization ability, which may inspire new research directions of graph generative modeling in this field. The dataset and benchmark are available at https://anonymous.4open.science/r/CommutingODGen-Dataset-0D4C/.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a large-scale dataset called LargeCommuingOD for commuting Origin-Destination (OD) flow generation and provides a benchmark for evaluating models in this domain. The key contributions are:

1. Construction of a comprehensive dataset covering 3,333 diverse areas across the United States, including metropolitan areas, towns, and rural regions. The dataset spans 9,372,610 km² and contains commuting OD flows, sociodemographic data, and point-of-interest distributions for each area.

2. Development of a benchmark framework to evaluate and compare different commuting OD flow generation models, addressing the lack of standardized evaluation in existing research.

3. Benchmarking of 9 existing models, including physical models, classical machine learning approaches, and graph neural network models, using the new dataset.

4. Introduction of a preliminary adaptation of graph diffusion models called WEDAN (Weighted Edges Diffusion condition on Attributed Nodes) for commuting OD flow generation.

5. Analysis of model performance in terms of precision and generalizability across different urban environments.

The paper demonstrates that network-based generative models, particularly those leveraging graph diffusion techniques, achieve the best performance in both precision and generalization ability. This finding suggests new research directions in graph generative modeling for commuting OD flow generation.

The authors argue that their dataset and benchmark provide a valuable resource for researchers in urban planning, transportation, and related fields, enabling more comprehensive evaluation and development of commuting OD flow generation models.

### Strengths
Originality:
1. The creation of a large-scale, comprehensive dataset (LargeCommuingOD) for commuting Origin-Destination (OD) flow generation covering 3,333 diverse areas across the United States is highly original. This dataset significantly expands on previous efforts in terms of scale and diversity.

2. The paper introduces a novel adaptation of graph diffusion models called WEDAN (Weighted Edges Diffusion condition on Attributed Nodes) for commuting OD flow generation, exploring a new paradigm in this field.

Quality:
1. The dataset construction process is rigorous, combining multiple reliable data sources including the U.S. Census Bureau, American Community Survey, and OpenStreetMap.

2. The analysis is thorough, examining both precision and generalizability of the models across different urban environments.

Clarity:
1. The paper is well-structured, clearly defining the problem, describing the dataset, and presenting the benchmark results.

2. Figures and tables effectively illustrate the dataset characteristics and model comparisons.

### Weaknesses
1. **Limited Exploration of Model Interpretability**: The paper emphasizes model performance but lacks a thorough examination of model interpretability, particularly for the network-based generative models that achieve the best results. Understanding the reasons behind their success could offer valuable insights for urban planners and policymakers.

2. **Insufficient Exploration of Edge Cases**: The paper would benefit from a more in-depth analysis of how the models perform in extreme or atypical urban environments within the dataset. This could reveal potential limitations or areas for improvement.

3. **Lack of Discussion on Model Fairness and Bias**: Given the diverse nature of the dataset, an analysis of potential biases in the models' predictions across different urban environments (e.g., rural vs. urban, high-income vs. low-income areas) would be beneficial.

4. **Basic Benchmark Methods**: Many of the selected benchmark methods are too basic. The paper should include more advanced models based on transformers and diffusion, such as those discussed in [this paper](https://arxiv.org/abs/2411.04453) and [this one](https://arxiv.org/abs/2402.15398).

5. **Questionable Significance of Claims**: Are the claims regarding the significance of the research truly justified? Without this dataset, researchers in the field might only need about a week to conduct their own benchmarks. Additionally, there are already open-source frameworks, like LibCity, that have collected these benchmarks (see [LibCity](https://github.com/LibCity/Bigscity-LibCity)).

### Questions
What do the authors see as the most promising directions for future research based on their findings? Are there specific areas where they believe the dataset and benchmark could be most impactful?

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
5

### Summary
Commuting OD flows are critical inputs for urban planning and transportation, while the high data collection cost results in a lack of high-quality datasets. This paper introduces a large-scale dataset containing commuting OD flows for 3,333 areas including a wide range of urban environments around the United States. Based on this dataset, authors further benchmark widely used models for commuting OD flow generation. They find that, owing to the rich information contained in the constructed OD dataset, a generative method that considers each OD matrix collected from a county/city as a network and learns to generate it given conditional information can significantly outperform other methods. This may point to a new direction in this domain, which relies on collection of high-quality OD datasets.

### Strengths
+ Commuting OD data is valuable in building smart cities, while the data is generally lacked in many areas around the world. The synthetic data generation technique is a promising solution for this problem, requiring high-quality and high-volume data for training ML models. This paper makes a good contribution towards this objective.
+ According to Table 1, the constructed dataset is more useful than existing ones, in terms of size and richness. The data analysis is sufficient, as in Figure 2-4.
+ The benchmark is designed in a reasonable manner. It covers a wide range of mainstreaming approaches in this field, and evaluate the model performance in a comprehensive way, including both flow generation accuracy and property distribution similarity.
+ The observation based on benchmark results is insightful. Based on the constructed large-scale OD dataset that is unseen in previous works, authors demonstrate the powerfulness of graph generative modeling in terms of generating OD flows for diverse cities. This may point to a new direction in this domain.

### Weaknesses
 + The presented results are informative, but the explanations are rather insufficient. For example, Figures 6 and 7 should be explained in detail. Specifically, the trends observed in Figure 6 regarding model performance across different city sizes (CPC and RMSE) are not thoroughly analyzed. The reasons behind the performance variations, such as the impact of flow heterogeneity and the prevalence of short-distance commuting, should be explicitly discussed. Similarly, the discussion of Figure 7 lacks depth. The implications of training on different city types (monocentric, polycentric, and others) for model transferability are not fully explored. The underlying reasons why models trained on specific city types fail to generalize to others need to be more clearly articulated.
+ Although authors discuss the limitations of the constructed dataset, the spatial scale (limited to the United States) and temporal scale (one year) can degrade its usefulness in applications. The lack of geographic diversity limits the generalizability of the findings, and the single-year data restricts the analysis of temporal trends and the impact of long-term changes in commuting patterns. This significantly reduces the potential for applying the models to regions outside the US or for studying the evolution of commuting patterns over time.

### Questions
+ Can authors demonstrate that models developed based on this US dataset can manage to transfer to other countries?
+ In Figure 1, why Commuting Flows are processed to generate Regional Socio-demographics?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper constructs a large-scale dataset (LargeCommuingOD) containing commuting OD flows for 3,333 diverse areas around the United States covering 9,372,610 km2 including a wide range of urban environments. Based on the LargeCommuingOD, the authors benchmark the existing widely used models for commuting ODflow generation. These efforts make up for the lack of comprehensive dataset and the absence of unified and systematic evaluation. Furthermore, this paper find out that network-based modeling for commuting OD flow supported by their dataset gives a promising performance. Thus, training on a large number of commuting OD networks can help the generative models to capture universal as well as distinct mobility patterns at city level, and therefore enhance the generalization ability.

### Strengths
S1. This paper constructs dataset covers 3,333 areas around the United States, providing a much broader spatial scale comparing to existed datasets.
S2. The dataset constructed in this paper covers metropolitan areas, towns, and rual areas, which is more comprehensive then existing datasets the focuses on usually a single type of urban environment.
S3. Based on the LargeCommuingOD, the authors benchmark the existing widely used models for commuting ODflow generation, which makes up for the absence of unified and systematic evaluation.

### Weaknesses
W1. Please clarify whether WEDAN is a newly proposed model, or the idea of it has already been proposed somewhere else.
W2. In Sec. 2.2, the link of the released dataset is given in plaintext, which may violate the anonymous policy.

### Questions
Please refer to Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a large-scale dataset, LargeCommutingOD, which captures commuting origin-destination (OD) flows for 3,333 diverse regions across the United States, spanning 9,372,610 square kilometers and encompassing a variety of urban environments. Compared to existing datasets, LargeCommutingOD offers broader and more comprehensive coverage and is made publicly available. The authors benchmark several baseline models using a standardized evaluation protocol, uncovering that network-based generative models could be a promising avenue for future research in this domain.

### Strengths
1. The authors present a large-scale and comprehensive dataset, LargeCommutingOD, which includes commuting OD flows for 3,333 regions, covering 9,372,610 square kilometers across diverse urban environments in the United States. This dataset provides more extensive coverage than existing resources and is openly accessible, promoting transparency and reproducibility.
2. By comparing LargeCommutingOD to previous datasets, the authors demonstrate that it captures a broader range of urban characteristics and types, further supporting its utility for various research purposes.
3. The authors implement and evaluate several baseline models to demonstrate the feasibility and relevance of their dataset. Notably, they identify that network-based generative models show considerable potential, which opens avenues for further investigation.
4. Upon reviewing the proposed code, I observed that the authors have implemented a comprehensive set of baselines, which could even serve as a robust library for OD flow generation. I hope the authors can commit to releasing this code if the paper is accpeted.

### Weaknesses
1. Given the dataset's coverage of 9,372,610 square kilometers and its focus on approximately 3,000 regions, the OD metrics may primarily reflect macro-level commuting patterns rather than fine-grained dynamics within individual cities. This limitation may restrict the dataset's applicability for studies requiring detailed intra-city analyses, such as understanding traffic patterns within a specific neighborhood or the impact of local events on mobility. The dataset's spatial resolution, while broad, might not be sufficient for researchers interested in micro-level urban dynamics.
2. The OD matrix, denoted as $\mathbf{F} \in \mathbb{R}^{N \times N}$ where $N$ exceeds 3,000, may be sparse. Providing a visual representation, such as a heatmap of the OD matrix, would clarify its density and structure, which could help readers better understand the data distribution. Furthermore, it is important to understand if the sparsity is uniform across all cities or if it varies based on city size or other characteristics. This information is crucial for selecting appropriate modeling techniques.
3. The authors included a non-anonymized GitHub link (https://github.com/tsinghuafib-lab/CommutingODGen-Dataset) in the submission, potentially compromising anonymity. And the authors have specified that only their names need to be anonymized.

### Questions
Please explain the questions.

### Soundness
3

### Presentation
3

### Contribution
3
