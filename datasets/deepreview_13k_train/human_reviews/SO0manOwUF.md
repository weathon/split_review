# $\texttt{UQ-Merge}$: UNCERTAINTY GUIDED MULTIMODAL LARGE LANGUAGE MODEL MERGING

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) have gained increasing popularity as a promising framework for leveraging the strong language reasoning capabilities in the vision-language domain. Given a wide range of MLLMs, model merging potentially offers a cheap way to aggregate their diverse knowledge into a single MLLM. However, directly plug-in existing model merging approaches often leads to suboptimal performance due to ($1$) inclusion of harmful models that have over-confident predictions in the target task; ($2$) the lack of specialized designs for vision-language tasks. To tackl these pain points, we conduct pioneering investigations to dissect the merging procedures and propose an uncertainty-guided MLLM merging algorithm, $\textit{i.e.}$, $\texttt{UQ-Merge}$, which $i)$ identifies beneficial candidates for merging, $ii)$ determines the merge order and the number of helpful candidates, and $iii)$ performs appropriate merging. Within our framework, we consider uncertainty quantification on both text and vision inputs to examine the MLLM prediction confidence, and then decide whether and when a MLLM needs to be included. It is worth mentioning that our vision-language uncertainty quantification does not require access to sample labels, making it more practical in various scenarios. Extensive experiments consistently demonstrate the superior MLLM merging performance of $\texttt{UQ-Merge}$ in both held-in and held-out vision-language benchmarks. For example, compared to existing state-of-the-art merging methods, $\texttt{UQ-Merge}$ brings substantial performance improvements of up to $44.3\%$ on average accuracy in $12$ datasets. Codes are available at https://anonymous.4open.science/r/UQ-Merge-7CD7.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper  presents a novel approach for merging Multimodal Large Language Models (MLLMs). The proposed UQ-Merge algorithm addresses the limitations of existing model merging techniques, which often lead to suboptimal performance in vision-language tasks due to the inclusion of overconfident, less reliable models. UQ-Merge incorporates uncertainty quantification (UQ) to identify beneficial candidates, determine merging order, and optimize merging by considering both text and vision inputs. The method uses perturbation-based uncertainty assessments, allowing for more practical applications without the need for labeled data. Experimental results show that UQ-Merge significantly improves model accuracy across multiple benchmarks, outperforming traditional single-modal merging techniques.

### Strengths
1. The concept of using uncertainty quantification (UQ) to guide the merging of multimodal large language models (MLLMs) is relatively novel.
2. The paper is generally well-organized, with clear figures illustrating the architecture and merging process, as well as tables comparing the performance of different methods.

### Weaknesses
1. The paper does not provide a baseline performance for a single model trained on the combined dataset. If a single model achieves satisfactory results, there would be no need to follow the authors' approach of fine-tuning multiple models on different datasets within the same model architecture and then merging them.
2. Experiments were only conducted on LLaVA-1.5, without considering other models such as Intern-VL, Qwen2-VL, and MiniCPM-V, which reduces the persuasiveness of the results.
3. The authors’ merging method is limited to models obtained by fine-tuning the same model architecture on different datasets, without exploring merges between different model architectures, such as combinations of Intern-VL, Qwen2-VL, and LLaVA-1.5. The applicability of the proposed uncertainty quantification across different model families is also not considered.

### Questions
Please check the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an instance-specific way to merge vision-language models during inference. They rank models based on uncertainties and iteratively merge models in order. Results demonstrate the effectiveness of their method compared with other merging baselines.

### Strengths
1. The idea of having an instance-specific merging method is intuitive and can potentially inspire other methods in a similar direction.
2. They conduct a good number of experiments, with many baselines and tasks evaluated.
3. The writing is clear. For example, the experimental sections clearly state the research questions and answers for each part.

### Weaknesses
1. The method appears time-intensive due to 1) its instance-specific nature, requiring model merging score computation for each input; 2) uncertainty scores that rely on multiple perturbations per step; and 3) an iterative merging process. Further discussion on time complexity and inference computations is necessary.
2. The approach seems heuristic, and its effectiveness isn’t immediately clear. For instance, while the authors note that current merging methods may include over-confident, potentially harmful models, it's unclear how their method mitigates this. Quantitative definitions and results supporting their hypothesis would strengthen their case. Specifically, the claim that merging models with lower uncertainty will necessarily exclude overconfident models needs more justification. If all models are overconfident and wrong, it is unclear how the merging process, even with uncertainty-based selection, would avoid producing a similarly overconfident and wrong merged model. 
3. The experimental setup raises concerns. They split the LLaVA instruction tuning datasets into groups and train models on these splits for merging. However, their best-merged model significantly underperforms LLaVA-1.5 on some tasks (e.g., VQAv2: 71.77 vs. 78.5). Additionally, some results appear within the average ± standard deviation range of baseline numbers, without clear improvements over baselines.

### Questions
1. Does your method assume that some models are poorly calibrated, and would it still be effective if all models were well-calibrated?
2. What are the oracle model merging numbers for each task?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an uncertainty-guided merging algorithm for MLLMs in vision-language tasks, addressing the limitations of existing merging methods. This approach selectively merges models based on their prediction confidence in both text and vision inputs without needing labeled data. Experiments show substantial accuracy improvements on various benchmarks.

### Strengths
- The introduction of an uncertainty-guided merging algorithm offers a novel perspective on aggregating MLLM models, addressing the specific needs of vision-language tasks.
- By avoiding the need for labeled samples in the uncertainty quantification process, the proposed method increases accessibility and applicability across diverse scenarios.

### Weaknesses
Overall Evaluation of the Work:
While the study shows promise, the methodology appears to lack a direct connection to multi-modality beyond the use of multi-modal data perturbation. This raises the question of why this approach was adopted within a multi-modal large language model (MLLM) setting, rather than being applied to a broader range of large language model (LLM) tasks. Further clarification on this choice is recommended.

- Prior work, such as that referenced in [1], has already introduced a fusion technique based on uncertainty, focusing specifically on gradient-related uncertainty as opposed to perturbed uncertainty. A detailed discussion comparing these approaches, with attention to their underlying mechanisms and potential advantages, would strengthen the analysis.
- As indicated in [2], some of the collected knowledge may lack essential commonsense elements.
- Furthermore, Itmay be needless to the visual modality in ScienceQA. This raises a concern: might perturbing images in this manner compromise the validity of the visual information?
- The omission of error metrics in Table 1 is notable. Why are those values not reported in Table 1?

### Questions
See weakness for details.

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
This paper proposes a novel approach (UQ-Merge) for merging MLLMs (i.e. LVLMs) using uncertainty quantification (UQ) to enhance model performance. The key challenge addressed is the suboptimal performance of existing model merging methods due to the inclusion of over-confident models and the lack of vision-language-specific merging designs. Therefore, they propose a strategy that uses perturbation to detect over-confidence, ranks each candidate model according to confidence, and ensures the final output merged model has the lowest uncertainty.

### Strengths
1. Their proposed UQ-merge algorithm, which selects beneficial models by evaluating uncertainty and excludes over-confident models, and merges models in a selective order based on their uncertainty scores, thereby improving the overall performance of the final merged model, is an intuitive and useful strategy.
2. Since model merge strategies for MLLMs are underexplored, this paper has promising.
3. The experiments clearly demonstrate the effectiveness of this strategy.
4. While existing merge strategies, including those for LLMs, typically rely on superficial performance metrics, this paper shows in section 4.4.1 that selecting models based on the implicit metric of uncertainty yields better results.

### Weaknesses
1. In my opinion, the main weakness lies in the question of scalability for real-world applications. First, real-world MLLM usage is often not task-specific, and evaluation test sets are not provided in large quantities or good quality. From this perspective, it would be valuable to discuss how an algorithm that measures uncertainty on specific refined datasets could be applied to real-world unseen datasets in the future or to discuss evaluation using limited test sets.
2. Measuring the uncertainty of all candidate models and repeatedly measuring the uncertainty of merged models to find good merge combinations for a single task-specific training set is very computationally costly. This will become an increasingly critical drawback as dataset quality and scale increase, and MLLM sizes grow.
3. The core of this algorithm is 'uncertainty measurement.' It heavily relies on the perturbation method, and while section 4.4.3 states 'VISION-LANGUAGE INPUT PERTURBATION IS CRUCIAL', it's disappointing that they didn't create and analyze a variety of strategies for this.

### Questions
Were there various attempts at methods for measuring uncertainty during this project? It seems like it could have been possible to try approaches other than perturbation or to experiment with different perturbation methods. A discussion about this could be a very interesting and important contribution.

### Soundness
3

### Presentation
2

### Contribution
3
