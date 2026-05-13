# Deep Temporal Deaggregation: Large-Scale Spatio-Temporal Generative Models

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Many of today's data is time-series data originating from various sources, such as sensors, transaction systems, or production systems.
	Major challenges with such data include privacy and business sensitivity. Generative time-series models have the potential to overcome these problems, allowing representative synthetic data, such as people's movement in cities, to be shared openly and be used to the benefit of society at large.
	However, contemporary approaches are limited to prohibitively short sequences and small scales. Aside from major memory limitations, the models generate less accurate and less representative samples the longer the sequences are. This issue is further exacerbated by the lack of a comprehensive and accessible benchmark.
	Furthermore, a common need in practical applications is what-if analysis and dynamic adaptation to data distribution changes, for usage in decision making and to manage a changing world: What if this road is temporarily blocked or another road is added?
	The focus of this paper is on mobility data, such as people's movement in cities, requiring all these issues to be addressed. 
	To this end, we propose a transformer-based diffusion model, TDDPM, for time-series which outperforms and scales substantially better than state-of-the-art. This is evaluated in a new comprehensive benchmark across several sequence lengths, standard datasets, and evaluation measures.
	We also demonstrate how the model can be conditioned on a prior over spatial occupancy frequency information, allowing the model to generate mobility data for previously unseen environments and for hypothetical scenarios where the underlying road network and its usage changes. This is evaluated by training on mobility data from part of a city. Then, using only aggregate spatial information as prior, we demonstrate out-of-distribution generalization to the unobserved remainder of the city.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new task—out-of-distribution generalization—for synthetic trajectory generation, which current models in the literature cannot address. To enable this generalization capability, the paper proposes using a heatmap as a conditioning constraint in a generative denoising diffusion model. Experiments on both unconditional trajectory generation and generation for new environments and hypothetical scenarios are conducted to evaluate its effectiveness. Additionally, the generation performance is analyzed under private heatmap scenarios.

### Strengths
1. This paper addresses a novel task, enabling the synthetic trajectory generation model to generalize to new areas.
2. A heatmap is used as a novel conditioning mechanism to achieve this generalization capability in the trajectory generation model.
3. Extensive experiments are conducted to evaluate the proposal.

### Weaknesses
1. Additional metrics, such as Density Error, Trip Error, Length Error, and Pattern Score (as used in the TrajDiff paper), should be considered for evaluation.
2. The proposed method splits regions for training, but it is unclear whether the model can correctly generate cross-region trajectories under these conditions. The lack of explicit mechanisms to ensure smooth transitions between regions could lead to artifacts or discontinuities in generated trajectories that span multiple regions. This is a critical concern for real-world applicability, where trajectories often traverse diverse areas.
3. In Table 2, the reasons why the model trained on 25% outperforms the model trained on 100% in most cases should be explained more clearly. The potential impact of data distribution and noise characteristics on model performance needs further investigation.
4. As an ablation study, it would be helpful to include results when the model does not use the conditioning component for the unconditional trajectory generation task. This would isolate the contribution of the conditioning mechanism.
5. Providing information on hyperparameters and including a complexity analysis would improve the paper. The absence of this information makes it difficult to assess the practical feasibility and scalability of the proposed method. A comparison of computational cost with baseline methods is also needed.
6. Typo:  "ell(..." should be "l(..." on Page 5.

### Questions
Same as the weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents TDDPM, a model for generating high-fidelity, privacy-preserving trajectory data in complex environments. TDDPM leverages a denoising diffusion approach to deaggregate spatial data into individual trajectories, allowing realistic time-series generation that generalizes to unseen areas. By conditioning on spatial aggregates, it achieves strong out-of-distribution performance. The model also uses k-anonymity for privacy and introduces a new benchmark for evaluating synthetic trajectory data, making it a valuable tool for urban planning and autonomous driving applications.

### Strengths
(1) The demonstration of proposed method TDDPM is detailed. 
(2) The authors describe the motivation and background of generating out-of-distribution trajectories in detail.

### Weaknesses
1. The contributions of TDDPM are unclear. The authors should clearly claim the contributions in the end of introduction.
2. In Table 1 and Table 2, standard deviation of KL and JS divergence are not reported.
3. This paper lacks an ablation study part. Experiments should be added to verify the effectiveness of proposed two steps mentioned in Section 4.
4. The experiment setting is confusing. The authors claim that TDDPM could achieve out-of-distribution generalization in Abstract. More analysis should be added to demonstrate the diffirence between the synthetic dataset and Geolife/Porto.
5. Line 308 to line 325 seems making no sense.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose TDDPM, a spatiotemporal generative model for trajectories. It aims to address two issues, (1) shortage of publicly available trajectories data; (2) model should conduct predictions about unobserved parts in space. To address these issues, TDDPM applies occupancy frequency marginal distribution as local information and hierarchical occupancy frequency mixture. The authors demonstrate the effectiveness of TDDPM on real-world datasets, showing improvements in forecasting accuracy compared to baseline models.

### Strengths
1. The paper focuses on the privacy issues of spatio-temporal trajectory data, as well as enhancing the prediction about unobserved parts in space. This is a very valuable and meaningful research topic.
2. The paper provides detailed visualizations and What-if analysis.

### Weaknesses
1. This paper proposes a privacy-preserving for generating synthetic trajectory samples, however, its contribution to privacy protection is limited. The paper uses only k-anonymity to protect local information in Section 5.3, which is a straightforward design. The application of k-anonymity, while simple, lacks a rigorous analysis of its effectiveness in the context of trajectory data. Specifically, the paper does not explore the trade-offs between the level of k-anonymity and the utility of the generated data. It also fails to consider more advanced privacy techniques such as differential privacy, which could provide stronger privacy guarantees.
2. There are no baselines in Section 5.2 and Section 5.3. The author should demonstrate how other methods perform in the Generalization experiment and with k-anonymity. The absence of baseline comparisons in these sections makes it difficult to assess the true performance of the proposed method. Without comparing against existing methods, it's unclear whether the results are significant or simply reflect the inherent properties of the dataset. The paper lacks a clear explanation of why existing trajectory generation methods cannot be adapted for out-of-distribution generalization or k-anonymity experiments.

### Questions
Could you provide brief descriptions of your baselines?

### Soundness
2

### Presentation
1

### Contribution
2
