# ZooProbe: A Data Engine for Evaluating, Exploring, and Evolving Large-scale Training Data for Multimodal LLMs

- Decision: Accept
- Scores: 6, 5, 5, 6

## Abstract
Multimodal Large Language Models (MLLMs) are thriving through continuous fine-tuning by LLMs. Driven by the law that "scale is everything", MLLMs expand their training sets during version iterations. In this paper, we propose a large-scale training data engine built around an evaluating-exploring-evolving (E3) loop. Evaluating the data provides insights into its characteristics. Exploring quality rules helps identify which data enhances training. Together, these processes facilitate the systematic evolution of new, high-quality data. With the E3 loop, we introduce ZooProbe, an efficient data engine for MLLMs. First, the problem of data expansion is formalized as a tree of sampling and growth. ZooProbe introduces a small-scale model *zoo* to obtain comprehensive evaluations for child datasets. From multiple perspectives, visual, textual, and multimodal models cover over 50 dimensions of intrinsic and meta attributes, such as object and topic distribution, and higher-level properties, like annotation quality and scene complexity. ZooProbe constructs based on A$^\star$ search, modeling the heuristic function as a quality estimate from data evaluation results. It dynamically explores the rule of data quality based on the model state of the *probe* datasets. Additionally, it evolves new targeted data with identified high-quality rules. We also develop an extra heuristic quality ranker with the data utilized and discarded during the expansion. Our experiments show that ZooProbe significantly breaks the scaling law in multimodal instruction fine-tuning at scales of 260$k$ and below.
ZooProbe generates high-quality data that accelerates MLLM training and enhances performance, automating the evolution of large-scale training data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel method to efficiently and effectively grow fine-tuning datasets of MLLMs. This method is built upon an evaluate-explore-evolve loop. In this loop, it utilizes other LLMs and smaller models to extract meta and intrinsic properties of additions to existing datasets, in order to estimate the performance of the base MLLM when trained on newer datasets and perform A* search based on this estimation. This method allows MLLMs to break scaling laws in multimodal instruction fine-tuning at scales of 260k, enabling MLLMs to systematically and automatically evolve training data in data/resource-constraint situations.

### Strengths
This paper presents a systematic approach towards a challenging problem–selecting and growing datasets to maximize downstream performance during fine-tuning. While this problem is often open-ended, and ill-formed, the proposed solution effectively utilizes and combines existing methods, by gathering signals using a zoo of powerful models and a well-defined search space for A* search. The implementation of such a system is also highly complex, incoporating many models and many dimensions of the data of interest. The significant primary and ablation results also represent that an impressive technical effort by the author(s) on the proposed method.

### Weaknesses
While this paper presents some impressive results on breaking the scaling law, I have a few concerns / questions about the paper. My first concern is around the possibility of overfitting to the evaluation benchmarks of interest. While the proposed method did not explicitly and directly optimize towards the evaluation benchmarks, I wonder if the benchmarks used to compute the reward overlaps with the evaluation. Even if they do not directly overlap, the set of benchmark would affect the generalizability of the proposed method to the general capabilities of the model. I believe this weakness can be resolved by having the author(s) further clarify the benchmarks used in reward/performance computation process in the loop. Another aspect of this weakness is whether duplication was observed between the candidate dataset and the ones used by the performance computation / evaluation benchmarks, of which an overlap of these images could indicate overfitting to particular images common in the benchmarks.

The second concern is the sparseness of details in the dimensions considered as meta and intrinsic properties of the data. While the author(s) have listed a number of examples of dimensions being considered, no specific/quantitative details were provided about these dimensions, and there is only a brief ablation on the number of dimensions in the results (which I appreciate). The paper can be improved with further exploration on the usefulness of various dimensions, and/or report failure cases on the impact of specific/specific types of dimensions on the effectiveness of the proposed method.

My final concern would be the strong assumption of targetting the uniform distribution (or random perturbations that starts from the uniform distribution) for the high-quality rules. The paper can be improved by further explaining the most common perturbations that the methods have converged to, and how future method(s) might consider a different distribution to begin with.

### Questions
Directly related to my concerns above:

- What are the benchmarks used for performance computation in the reward / heuristics?
- Are there duplication in the images used for the benchmarks used for reward computation and the evaluation benchmarks?
- Can you provide more details on the dimensions used (i.e., a detailed table / number of dimensions for meta/intrinsic properties of data)?
- Which dimensions/properties contributes most/least to high performance of the method?
- Can you provide more details about the perturbed distributions, such as which of them are commonly observed, and how much does the perturbation matter (compared to targetting uniform distribution)?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents ZooProbe, a system for synthetic data generation and selection for multimodal tasks. ZooProbe is characterised by the evaluate-explore-evolve (E3) loop. Starting from some seed data, ZooProbe first assesses the quality of the data, and then employs A* search to iteratively grow the data. It also evolves the target data with rules. 

Evaluation is conducted on a number of QA datasets including AI2D, ScienceQA, MMStar, RealWorldQA, SeedBench and MMMU. Results show that, in general, ZooProbe can elicit stronger performance than a random sample baseline, sometimes substantially.

### Strengths
* Synthetic data generation has become a key technique to continue to push VLM/LLM performance. Thus, investigations in this area are timely and important. 

* The results show strong performance of the proposed technique.

### Weaknesses
 * The clarity of the paper could be improved. Throughout the paper, there are phrases and sentences that are ambiguous (I will give some examples below). These ambiguities have an impact on the paper's readability.

* The impressive evaluation results are compared on a "random sample" baseline. Stronger data synthesis baselines should be compared.

* The paper repeatedly claims that ZooProbe can "break the scaling law". It seems to mean ZooProbe is able to elicit strong performance from VLM. However, I'm not sure what that means exactly. Please clarify.

* Furthermore, this phrase ("breaking the scaling law") is hyperbolical, as it is only empirically validated on one single VLM (LLaVA) and six datasets. I suggest the authors tone it down.

* On line 107, the author mentions catastrophic forgetting. I agree that this is an important problem to be concerned with, and I'd like to see some discussions on how ZooProbe mitigates this forgetting problem.

### Questions
* The paper repeatedly claims that ZooProbe can "break the scaling law". It seems to mean ZooProbe is able to elicit strong performance from VLM. However, I'm not sure what that means exactly. Please clarify. 

* Furthermore, this phrase ("breaking the scaling law") is hyperbolical, as it is only empirically validated on one single VLM (LLaVA) and six datasets. I suggest the authors tone it down. 

* On line 107, the author mentions catastrophic forgetting. I agree that this is an important problem to be concerned with, and I'd like to see some discussions on how ZooProbe mitigates this forgetting problem.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
ZOOPROBE is a data engine designed to enhance the training of Multimodal Large Language Models (MLLMs) by evaluating, exploring, and evolving large-scale training data. The engine is built around an evaluating-exploring-evolving (E3) loop, which provides insights into data characteristics, identifies quality rules for data enhancement, and establishes a probe set for targeted rule selection tot facilitates the systematic evolution of new, high-quality data.

Experiments demonstrate that ZOOPROBE significantly beats scaling laws across scales from 10k to 260k

### Strengths
1. ZOOPROBE uses a small-scale model zoo consisting of various models to evaluate data comprehensively. These models assess over 50 dimensions of intrinsic and meta attributes, such as object and topic distribution, annotation quality, and scene complexity.
2. ZOOPROBE describes high-quality selection rules as an interpretable distribution based on the current data and model state. It uses Kullback-Leibler divergence to measure the difference in distribution and aims to achieve greater diversity in the dataset.
3. The authors have demonstrated through experiments and analysis of the results that ZOOPROBE is more effective and has lower overhead compared to other data augmentation strategies.

### Weaknesses
1. The paper presents ablation studies on the heuristic functions and evaluated dimensions, but it could benefit from more detailed analyses. For instance, it would be insightful to see how different combinations of intrinsic and meta dimensions impact the model's performance. Specifically, the interactions between different types of intrinsic dimensions (e.g., basic visual features vs. fine-grained object features) and their combined effects on model training are not thoroughly explored. Similarly, the interplay between different meta-dimensions, such as annotation quality and cognitive load, and their influence on the final model performance, needs further investigation.


### Questions
1. Could the authors elaborate on the relative importance of the various intrinsic and meta dimensions in the data evaluation process? Are there any dimensions that consistently have a higher impact on model performance?

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
3

### Summary
This paper introduces ZooProbe - an innovative multimodal large language model (MLLM) training data engine. ZooProbe implements an Evaluate-Explore-Evolve (E3) cycle system that leverages a small-scale model zoo to evaluate data quality, explore high-quality data patterns, and strategically expand training datasets. The key innovations include: 1) proposing a 50+ dimensional data description vector system covering both intrinsic (e.g., resolution, language) and meta (e.g., annotation reliability, knowledge dependency) features; 2) developing an A*-search-based framework to optimize data distribution; 3) generating new data through rule-guided approaches. Experiments demonstrate that ZooProbe significantly outperforms traditional data scaling rules across scales from 10K to 260K examples.

### Strengths
1. The paper makes a clear technical contribution through its E3 cycle framework and model zoo approach. The innovation lies in systematically addressing data quality through a small-scale evaluation system, rather than relying on traditional scaling methods. The integration of A*-search for distribution optimization is technically sound and well-motivated.

2. The empirical evaluation is thorough and convincing. The authors provide comprehensive ablation studies across different scales, with the MLLM-Scorer showing consistent improvements over baselines. The experimental design effectively validates each component of the proposed system.

3. The work addresses a significant problem in MLLM training with practical implications. By reducing computational costs and carbon emissions while improving model performance, the approach offers valuable insights for the field. The methodology generalizes well to other domains, suggesting broader impact beyond the immediate application.

### Weaknesses
1. While the paper demonstrates improvements in data efficiency, the experimental evaluation lacks comparison with recent data-centric approaches such as ActiveLLM and DataSpell. These methods also address data quality optimization but through different mechanisms. Including these comparisons would better position the work's contributions within the current landscape.

2. The scalability of the approach beyond 260K examples remains unclear. While the results are promising at the demonstrated scales, larger industrial applications often deal with datasets in the millions. The authors should either provide theoretical guarantees for scalability or acknowledge this limitation explicitly. Additionally, the sensitivity of the method to the initial model zoo composition deserves more investigation - how much does performance vary with different zoo configurations?

### Questions
1. Regarding the scalability of ZooProbe:

    a. Have you tested or analyzed the approach's feasibility on datasets larger than 260K examples?

    b. Does the A* search optimization remain tractable for much larger datasets?

    c. Are there any theoretical bounds on the computational complexity as the dataset size grows?

2. Implementation details:

    a. Could you provide more details about the stopping criteria for the E3 cycle?

    b. How is the trade-off between exploration and exploitation managed in practice?

    c. What are the key hyperparameters that practitioners need to tune when applying ZooProbe?

### Soundness
3

### Presentation
3

### Contribution
3
