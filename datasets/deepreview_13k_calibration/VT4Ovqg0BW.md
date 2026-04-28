# Functional-level Uncertainty Quantification for Calibrated Fine-tuning on LLMs

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
\begin{enumerate}
From common-sense reasoning to domain-specific tasks, parameter-efficient fine tuning (PEFT) methods for large language models (LLMs) have showcased significant performance improvements on downstream tasks.  However, fine-tuned LLMs often struggle with overconfidence in uncertain predictions, particularly due to sparse training data. This overconfidence reflects poor epistemic uncertainty calibration, which arises from limitations in the model's ability to generalize with limited data. Existing PEFT uncertainty quantification methods for LLMs focus on the post fine-tuning stage and thus have limited capability in calibrating epistemic uncertainty. To address these limitations, we propose Functional-Level Uncertainty Quantification for Calibrated Fine-Tuning (UQ4CT), which captures and calibrates functional-level epistemic uncertainty during the fine-tuning stage via a mixture-of-expert framework. We show that UQ4CT reduces Expected Calibration Error (ECE) by more than $25\%$ while maintaining high accuracy across $5$ benchmarks. Furthermore, UQ4CT maintains superior ECE performance with high accuracy under distribution shift, showcasing improved generalizability.

\end{enumerate}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel method called Functional-Level Uncertainty Quantification for Calibrated Fine-Tuning (UQ4CT), aimed at addressing overconfidence in large language models (LLMs) during fine-tuning, especially in scenarios with limited or sparse data. Traditional parameter-efficient fine-tuning (PEFT) approaches often fail to accurately calibrate epistemic (model-related) uncertainty, leading to overly confident predictions. To overcome this, UQ4CT incorporates a Mixture-of-Experts (MoE) framework with LoRA (Low-Rank Adaptation), enabling dynamic, prompt-dependent expert selection that captures and calibrates functional-level uncertainty throughout the fine-tuning process. The paper’s main contributions are:
1. A new approach to quantify epistemic uncertainty at the functional level during fine-tuning, using MoE to dynamically adjust uncertainty based on input.
2. A calibration loss function that aligns uncertainty with predictive correctness, encouraging expert exploration for incorrect predictions and reinforcing correct predictions.
3. Empirical results showing that UQ4CT reduces Expected Calibration Error (ECE) by over 25% across multiple benchmarks while maintaining high accuracy, demonstrating robustness both within distribution and under distribution shifts.

### Strengths
The paper introduces a novel approach by integrating functional-level epistemic uncertainty directly into the fine-tuning process of LLMs, departing from conventional post hoc calibration. The unique combination of MoE with LoRA enables dynamic, prompt-dependent uncertainty modeling, addressing both parameter efficiency and overconfidence in fine-tuned models. The proposed calibration loss function further aligns model confidence with predictive accuracy, reducing overconfidence in a novel, functional manner.
The paper is validated with comprehensive experiments across multiple benchmarks, supported by baseline comparisons and ablation studies.
The paper is well-structured and accessible, with clear explanations and effective use of visual aids, making complex concepts understandable.
UQ4CT addresses a critical need for reliable uncertainty estimation in high-stakes applications by enhancing calibration and robustness under distribution shifts. This advancement strengthens the foundation for trustworthy AI, especially in domains where reliable predictions are essential despite sparse data.

### Weaknesses
UQ4CT’s calibration loss relies on clear correctness metrics, limiting its applicability to tasks with definitive right or wrong answers. This restricts its use in open-ended tasks, such as generative dialogue or summarization. To broaden applicability, future work could explore calibration methods based on human feedback scores or soft accuracy measures instead of binary correctness. Specifically, the current implementation struggles with tasks where the notion of a single 'correct' answer is not well-defined, such as creative writing or complex reasoning where multiple valid outputs exist. The reliance on a binary correctness signal means the model cannot effectively learn to quantify uncertainty in these scenarios, potentially leading to miscalibrated confidence even when the generated output is reasonable or acceptable. Furthermore, the method does not account for the nuances of semantic similarity, where a generated response might be semantically close to a valid answer but not an exact match, which would be penalized as incorrect, thus skewing the uncertainty calibration.

The use of MoE for dynamic expert selection, while effective, could lead to scalability issues with larger models or multi-task scenarios due to increased computational demands. While the parameter-efficient nature of LoRA helps, the overhead of routing inputs to different experts and managing multiple sets of LoRA parameters could still become a bottleneck, especially when dealing with very large models or a large number of tasks. The paper does not provide a detailed analysis of the computational cost associated with the MoE architecture, particularly in terms of memory usage and inference time, which are critical factors for practical deployment. Additionally, the paper does not explore the potential for interference between experts when applied to multi-task scenarios, where different tasks might require conflicting expert activations, potentially degrading performance.

### Questions
1. Since UQ4CT’s calibration relies on binary correctness, how might this approach be adapted for tasks where “correctness” is less definitive, such as open-ended text generation or summarization? 
2. Could the authors elaborate on any experiments or initial explorations in applying UQ4CT to such tasks? 
3. Exploring approaches that rely on alternative correctness signals, such as soft scoring or feedback-based calibration, might broaden the applicability.

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
3

### Summary
This paper proposes a new approach called Functional-Level Uncertainty Quantification for Calibrated Fine-Tuning (UQ4CT) to calibrate the functional-level epistemic uncertainty via the LoRA MoE architecture.

### Strengths
1. This paper introduces a unique uncertainty quantification (UQ) method for fine-tuning large language models (LLMs) using a Mixture-of-Experts (MoE) approach
2. In this paper, UQ4CT reportedly achieves a 25% reduction in Expected Calibration Error (ECE) across multiple benchmarks, which is a substantial improvement.

### Weaknesses
1. The novel calibration loss function is mentioned as one of the contributions. However, the paper lacks detailed theoretical analysis to illustrate why this specific design especially the loss is effective for uncertainty calibration. Specifically, the paper does not provide a formal definition of the functional-level uncertainty being targeted, nor does it rigorously show how the proposed loss function minimizes this defined uncertainty. The connection between the loss and the desired calibration property is not theoretically established.
2. Although the paper compares UQ4CT with other PEFT-based uncertainty quantification techniques, a more comprehensive comparison with non-PEFT-based methods might provide a clearer view of its advantages and limitations. The paper should include a wider range of baselines, especially those that do not rely on parameter-efficient fine-tuning, to better contextualize the performance of UQ4CT. This would help to understand if the observed improvements are due to the specific PEFT approach or the core uncertainty quantification method.
3. The whole framework is built on LoRA, and can it be applied to more general settings? The paper does not discuss the limitations of using LoRA and whether the proposed method can be generalized to other fine-tuning techniques or even to full fine-tuning scenarios. The reliance on LoRA might restrict the applicability of the method.
4. There are a lot of hyper-parameters, such as the number of top gate routers (why use 2 in this paper), and N, s, L. How to set them in practice and is there any theoretical insight for these choices? The paper lacks a detailed discussion on how these hyperparameters influence the performance of UQ4CT. The choice of these parameters seems arbitrary without clear guidelines or theoretical justification, making it difficult to reproduce or apply the method effectively.

### Questions
Please refer to the weakness part. 
For example: 
1. Can the authors add some theoretical analysis?
2. Can more baseline methods be compared?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel calibration method for LLMs that is applicable already during the fine-tuning stage of the model. This is achieved by leveraging the specific nature of the LoRA MoE architecture, using the weights of the Top-K router layers to quantify the functional epistemic uncertainty. The epistemic uncertainty calculated this way is used with the predictive accuracy in a specific loss function (as one part of a triple loss function for the overall loss). The authors claim to reduce ECE substantially while not impairing the predictive performance, but even resulting in better predictive performance and making it more robust to e.g. distribution shift. These findings are backed by two experiments: First, they show ECE decrease across 5 MCQA benchmarks while maintaining better (or at least on par) accuracy compared to the baselines. Second, they use a subset of the benchmarks to create distribution shift scenarios to prove the robustness of their approach.

### Strengths
The experiments are outlined very clearly and explained and motivated comprehensively. This makes the paper easy to follow and understandable to the reader. The additional experiments (distribution shift and ablation) are well-motivated and contribute to the overall experimental setup.
- The problem tackled in this research is widely known and highly problematic, yet there is no definite and generally applicable solution to it. Hence this work, tackling it effectively for LoRA MoE architectures is an important contribution to the field in general.
- Not only do the authors introduce a method that can substantially improve the model calibration, but it also shows strong model performance in terms of accuracy.

### Weaknesses
 - The ablation study/studies could be more elaborated, i.e. e.g. examining what the influence of the different terms in the loss is, or how sensitive performance is to the hyperparameters alpha and beta in the loss. I think such examinations are important to understand what’s going on and how brittle such triple losses are. Specifically, the interplay between the accuracy loss, the epistemic uncertainty term, and the load balancing term needs to be better understood. For example, how does the model behave when the load balancing term is removed, or when the epistemic uncertainty term is weighted more heavily than the accuracy term? Furthermore, the sensitivity to the hyperparameters alpha and beta should be examined more rigorously, perhaps by performing a grid search or similar analysis to understand the optimal range of these parameters.
- The approach is specifically tailored to the nature of the LoRA MoE architecture as it critically depends on leveraging the weights of the Top-K Routing layers of the MoE. While this seems to work pretty well here, one might also consider this a limitation of the approach in general since it is not generally applicable. This reliance on the specific architecture limits the broader impact of the work, as it cannot be directly applied to other model architectures without significant modifications. It would be beneficial to discuss the potential for extending this approach to other architectures or to acknowledge this limitation more explicitly.


### Questions
- In Equation (5): What exactly do M’ and a’ refer to? I believe this is not explicitly specified anywhere
- Why did you place the “Related work” section after your methodology? I think it introduces important concepts to the reader who would thus benefit from reading this before your explanations in the “Methodology” section.
- L. 326: I personally think it’s not optimal to call something “significant” that you actually did not formally test with a statistical test. Maybe it’s better to use a formulation like “notable” or “substantial”?
- L 359: Just to be sure, what do you mean by “bin size of 15”? I think it is more common to communicate this in terms of “number of bins (of equal size usually”? 
- L. 447 More of a comment than a question, but I think a sole subsubsection (5.4.1) does not really make sense, probably you should rather just add this subsubheading to the heading of subsection 5.4.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method for epistemic uncertainty quantification in the context of LoRA fine-tuning, which is also compatible with a mixture-of-experts setup. The authors introduce a specialized training loss, designed to capture the difference between predictive accuracy and functional-level epistemic uncertainty. When applied to the Llama2 model, the proposed method shows improvements across a variety of datasets.

### Strengths
The pipeline and method developed in this paper appear well-founded, and the paper is generally well-written.

### Weaknesses
The biggest weakness of this paper is the limited experimental effort. Specifically, the experiments are conducted on only one LLM, and there is very little ablation or other study to investigate the additional properties of this UQ method. While I don’t consider the number of pages a deterministic measure of effort, the brevity of the experimental section does suggest a lack of thoroughness in the design of experiments.

Additionally, beyond the lack of comprehensiveness, the paper offers very little empirical or theoretical insight into why this approach is effective. I also find that the paper lacks depth overall.

### Questions
1. In equation (9), what is the term $\mathcal{L}_b$? I don't think this is a good practice to put it in the reference. It should be at least written in the appendix.

2. In table 1 and 2, what is the numeric values in the subscript?

### Soundness
3

### Presentation
2

### Contribution
2
