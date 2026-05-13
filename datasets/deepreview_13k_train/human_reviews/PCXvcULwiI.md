# Benchmarking Structural Inference Methods for Interacting Dynamical Systems with Synthetic Data

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
In the quest to unravel the complexities of dynamical systems, the initial imperative is to unveil their inherent topological structure, a key determinant of system organization. Achieving this necessitates the deployment of robust structural inference techniques capable of deriving this structure from observed system behaviors. 
However, these methods are often tailor-made for specific domains and datasets, lacking a unified and objective framework for comparative assessment. 
In response to this pressing challenge, we present a comprehensive benchmarking study encompassing 12 structural inference methodologies sourced from diverse disciplines. 
Our evaluation protocol spans dynamical systems generated via two distinct simulation paradigms and encompasses 11 distinct interaction graph typologies. 
We gauge the methods' performance in terms of accuracy, scalability, robustness, and sensitivity to graph properties. 
Key findings emerge: 1) Deep learning techniques excel in the context of multi-dimensional data, 2) classical statistics and information-theory-based methods exhibit exceptional accuracy and resilience, and 3) method performance correlates positively with the average shortest path length of the graph. 
Our benchmark not only aids researchers in method selection for specific problem domains but also serves as a catalyst for inspiring novel methodological advancements in the field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper titled "Benchmarking Structural Inference Methods for Interacting Dynamical Systems with Synthetic Data" addresses the need for a unified and objective framework to assess structural inference methods for understanding the topological structure of dynamical systems. The authors conduct a comprehensive benchmarking study, evaluating 12 structural inference methodologies sourced from various disciplines. They use synthetic data that incorporates properties from 11 diverse real-world graph types, ensuring the realism of their evaluations. The paper's contributions include insights into the performance of various structural inference methods in terms of accuracy, scalability, robustness, and sensitivity to graph properties. Notable findings include the efficacy of deep learning techniques for multi-dimensional data and the strength of classical statistics and information-theory-based methods. The paper aims to assist researchers in method selection for specific problem domains and inspire further advancements in the field of structural inference for interacting dynamical systems.

### Strengths
The paper has several strengths, which are outlined across multiple dimensions:

1. Originality:
   - The paper contributes to the field of structural inference for dynamical systems by addressing the pressing need for a unified benchmarking framework. This is an original and valuable contribution, as it provides a systematic evaluation of various structural inference methods, which can guide researchers in selecting appropriate techniques for their specific problem domains.
   - The inclusion of diverse real-world graph types and their properties in the benchmarking process enhances the originality of the study. It brings a more realistic perspective to the evaluation, making it relevant for practical applications.

2. Quality:
   - The paper maintains high quality in terms of its methodology and experimentation. It employs rigorous benchmarking techniques and synthetic data generation to evaluate the performance of structural inference methods. The paper's thoroughness in presenting the implementation details of these methods adds to its quality.
   - The acknowledgment of limitations, ethical concerns, and potential misuse of the technology showcases a responsible approach to research, demonstrating the authors' commitment to addressing the broader impact of their work.

3. Clarity:
   - The paper is well-structured and presents its concepts in a clear and organized manner. It begins with a concise introduction, followed by detailed methods and implementation sections, and ends with a clear acknowledgment of limitations and broader impact.
   - The paper effectively communicates the assumptions made, the choice of evaluation metrics, and the rationale behind selecting specific structural inference methods. This transparency enhances the clarity of the research.

4. Significance:
   - The paper's significance lies in its potential to advance the field of structural inference for dynamical systems. By providing a comprehensive benchmarking study, it serves as a valuable resource for researchers seeking to choose the most suitable methods for their work.
   - The paper's exploration of the significance of structural inference in various domains, such as physics, chemistry, and biology, highlights the wide-ranging applications of these methods, underlining their importance in scientific research.

Overall, the paper's strengths are evident in its originality, quality, clarity, and significance. It offers a valuable benchmarking study that can guide researchers and practitioners in the structural inference field, and its responsible consideration of limitations and ethical concerns further enhances its quality.

### Weaknesses
Lack of Real-World Applications: The paper primarily focuses on benchmarking structural inference methods with synthetic data. However, it does not provide concrete examples or case studies demonstrating the practical application of these methods in real-world scenarios. Including real-world use cases and applications, with specific examples of data sets and analysis, would make the paper more relevant to practitioners who are interested in applying these methods in their work.

Incomplete Hyperparameter Exploration: While the paper mentions a hyperparameter search for some methods, it lacks a comprehensive discussion of the specific hyperparameters explored, the range of values considered, and the impact of hyperparameter tuning on the results across different graph types. Providing more detail on hyperparameter exploration, including a sensitivity analysis of how different parameter settings affect performance on different graph structures, would help researchers understand the sensitivity of the methods to parameter settings.

Limited Discussion of Algorithm Mechanisms: The paper briefly describes the structural inference methods but does not delve deeply into the underlying mechanisms of each method. A more detailed explanation of how each method works, its assumptions, and the computational complexity involved, including specific algorithmic steps and mathematical formulations, would provide a better understanding of the methods for readers who may be less familiar with the specific techniques.

Scope of Comparative Methods: The paper mentions selecting methods based on representativeness, diversity, data constraint, and computational constraint. However, it could benefit from a more thorough exploration of alternative methods from various fields, including those that may not have readily available implementations. There may be lesser-known but promising methods that could offer valuable insights into structural inference for dynamical systems, and a discussion of why these were excluded would be beneficial.

Limited Discussion of Practical Implications: While the paper acknowledges the potential misuse of structural inference methods for privacy concerns, it could further elaborate on the ethical and societal implications of these technologies. Discussing potential safeguards and ethical guidelines, with specific examples of how these methods could be misused and how to prevent it, would provide a more comprehensive perspective on the broader impact of the research.

### Questions
Here are questions and suggestions for the authors that could help in clarifying certain aspects, addressing limitations, and improving the paper.

Real-World Data Application: It would be valuable to understand if the authors have plans to extend their benchmarking study to real-world datasets in the future. Real-world data can introduce complexities that synthetic data may not fully capture, and such an extension would enhance the applicability of the research findings.

Hyperparameter Tuning Details: Could the authors provide more specifics on the hyperparameter tuning process for the structural inference methods? Details on the range of hyperparameters explored, the methodology used for tuning, and their impact on the results would offer insights into the sensitivity of these methods to parameter settings.

Comparison with Other Benchmarking Studies: Have the authors considered comparing their benchmarking results with similar studies in the field of structural inference for dynamical systems? This would help contextualize the significance and contribution of their work and provide insights into the relative performance of the methods.

Robustness of Synthetic Data: The paper mentions the use of synthetic data but does not extensively discuss the robustness of the synthetic data generation process. How sensitive are the benchmarking results to variations in the synthetic data generation parameters? Are there considerations for addressing potential biases in the synthetic data?

Interpretability of Method Outcomes: Could the authors elaborate on the interpretability of the outcomes provided by the structural inference methods? How do these outcomes translate into actionable insights for researchers in various domains, and can they be used to make informed decisions in real-world applications?

Privacy Implications: The paper mentions the potential misuse of structural inference methods for privacy invasion. Could the authors discuss potential safeguards and ethical guidelines that could be applied to mitigate these privacy concerns when implementing such methods?

Generalizability to Other Domains: The paper highlights the application of structural inference methods to fields like physics, chemistry, and biology. Could the authors provide examples of specific applications or domains within these fields where their benchmarking study can be directly applicable or where the methods might require further adaptation?

Future Directions: What are the authors' thoughts on future research directions in the field of structural inference for dynamical systems? Are there specific areas or challenges that they believe warrant further exploration or investigation?

Comparison with Additional Baselines: Considering the significance of baseline methods, could the authors consider including more diverse and representative baseline methods in their benchmarking study, even if they may require adaptation? This could enhance the comprehensiveness of the evaluation.

Impact of Synthetic Data Discrepancies: Given the mention of potential discrepancies between synthetic data and real-world data, how does the paper account for these discrepancies, and are there considerations for addressing this limitation in future research?

My questions and suggestions aim to encourage the authors to provide further insights, clarify aspects of the research, and consider potential areas for improvement and future exploration.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce a unified and objective benchmark comprising 12 structural inference methods. To overcome the challenges of collecting real-world datasets, the authors meticulously curate a synthetic dataset with over 213,444 trajectories. The benchmark not only aids researchers in method selection for specific problem domains but also serves as a catalyst for inspiring
novel methodological advancements in the field.

### Strengths
+ I appreciate the authors release the source datasets and provide a nice website.
+ Extensive experiment for the inference of dynamical systems.
+ I believe this work provides insightful findings of exploring structural inference on real-world dynamical systems.
+ Detailed introduction of implementations.

### Weaknesses
 - Why Gaussian noise. Can the authors consider other types of noises? Also, can the authors test the models' performance under Gaussian noise with different conditions.
- Complexity/running time is missing.
- I wonder can the authors consider robust testing for this paper?

### Questions
Please see the comments in Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a benchmark for a dynamic system, which is often represented as agents engaged in interactions, forming what we term an interaction graph. Motivated by the fact that the existing methods have often been assessed on distinct datasets and specific graph types, the paper presents a unified benchmark to evaluate the existing methods on the different interaction graphs. The paper also benchmarks the scalability and the robustness of the existing methods.

### Strengths
1. The paper presents the first benchmark for dynamic systems, which could facilitate future research.
2. The benchmark evaluates performances, scalability, and robustness.
3. The benchmark results could save the efforts for future research in this domain.

### Weaknesses
1. The experiments rely on some synthetic datasets. However, it is unclear if the synthetic datasets are representative enough for real-world dynamic systems. It is also unclear how reliable it is to benchmark these synthetic data, i.e., whether the observations are reliable.
2. The package is mainly based on Python and R. It is unclear whether the implementation is efficient.

### Questions
How to ensure the synthetic datasets align with the real-world dynamic systems?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a number of benchmark datasets for inferring dynamical systems from observations. Specifically, the object of interest is to uncover the adjacency matrix underlying the generation of the data. The authors then review a number of methods that have been developed for this particular task and describe their properties. To compare the different methods, the authors then apply a number of different algorithms to these benchmarks and discuss the performance between the methods.

### Strengths
The authors provide a reasonably comprehensive review of the existing methods and propose a number of relevant benchmarks datasets for reliably comparing the performance of different solutions to this problem. 

The authors try to make the datasets realistic by imposing statistics from real world datasets into the synthetic datasets that they impose. Since this is graph discovery problem, often the underlying structure is impossible to obtain a ground truth.

### Weaknesses
The proposed datasets seem a bit random. For example, the authors state that the miRNA dataset is too specific, but the springs dataset is a reasonable benchmark. The springs dataset seems very specific and maybe a bit contrived for most purposes. 

All the benchmarked methods are synthetic with some real statistics being components. It would be nice to have some real datasets, but obtaining a ground truth structure would be impossible. I think it would be good if the authors could discuss this aspect in greater detail and describe how one can make the datasets be more realistic.

### Questions
In the preliminaries section, should the vertex set be $\{V_i, 1 \leq i \leq n\}$ instead of $N$?

Are there any other datasets that could be used that have a more defined structure? For example, some of the gene regulatory network datasets are popular applications of this methodology, and I would like to see if there are any that could be used for the purposes of evaluation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
