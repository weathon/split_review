# ECoFLaP: Efficient Coarse-to-Fine Layer-Wise Pruning for Vision-Language Models

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
Large Vision-Language Models (LVLMs) can understand the world comprehensively by integrating rich information from different modalities, achieving remarkable advancements on various multimodal downstream tasks.  However, deploying LVLMs is often problematic due to their massive computational/energy costs and carbon consumption. Such issues make it infeasible to adopt conventional \textit{iterative global pruning}, which is costly due to computing the Hessian matrix of the entire large model for sparsification. 
Alternatively, several studies have recently proposed layer-wise pruning approaches to avoid the expensive computation of global pruning and efficiently compress model weights according to their \emph{importance} within a layer. However, they often suffer from suboptimal model compression due to their lack of a global perspective. To address this limitation in recent efficient pruning methods for large models, we propose \textit{\textbf{E}fficient \textbf{Co}arse-to-\textbf{F}ine \textbf{La}yer-Wise \textbf{P}runing (\textbf{ECoFLaP})}, 
a two-stage \emph{coarse-to-fine} weight pruning approach for LVLMs. We first determine the sparsity ratios of different layers or blocks by leveraging the global importance score, which is efficiently computed based on the zeroth-order approximation of the global model gradients. Then, the model performs local layer-wise unstructured weight pruning based on globally-informed sparsity ratios. 
We validate our proposed method across various multimodal and unimodal models and datasets, demonstrating significant performance improvements over prevalent pruning techniques in the high-sparsity regime. \blfootnote{Our project page and code are available at 
\url{https://ecoflap.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents the Efficient Coarse-to-Fine Layer-Wise Pruning (ECoFLaP) method for Large Vision-Language Models. The method utilizes zeroth-gradient optimization to determine layer-specific sparsity ratios and applies layer-wise unstructured weight pruning. Experimental results demonstrate improvements on some benchmarks.

### Strengths
-- Pruning is a crucial topic for efficient large models.

-- The proposed method is interesting to me.

-- Extensive experimental results demonstrate some improvement compared to previous methods.

### Weaknesses
Overall, the paper leans more towards an engineering-focused approach. The proposed method appears to be a straightforward combination of existing techniques without offering mathematical insights or clear motivations. The paper requires significant revisions to improve its writing quality.

-- The paper claims that pruning multi-modal large models differs from other large models, but lacks mathematical or experimental support for this assertion.

-- The use of layer-wise pruning due to the computational cost of calculating the inverse of the Hessian is common in other large model pruning approaches.

-- The assumption of having sufficient GPU resources in the pruning scenario is not adequately discussed.

-- While zeroth-gradient optimization is effective for efficient fine-tuning of large models [1], its motivation and suitability in a pruning scenario, considering challenges like slow convergence and sensitive hyper-parameters, remain unclear.

-- The use of calibration datasets in experiments raises concerns about fairness and the significance of employing zeroth-order optimization to save memory if calibration datasets are used for fine-tuning.

The paper suffers from poor writing quality and contains noticeable typos:

1. that finds adaptive sparsity per layer by leveraging the global importance score approximated via first-order gradients. (should be zeroth-order gradients)

2. Note that our proposed method is computationally efficient by leveraging the first-order gradient to obtain a global importance score without Hessian operations (should be zeroth-order gradients)

### Questions
Please refer to my detailed comments in the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenges of deploying Large Vision-Language Models (LVLMs) due to their high computational and energy costs. Traditional global pruning methods are costly, and recent layer-wise pruning approaches lack a global perspective. To overcome this, the paper introduces Efficient Coarse-to-Fine Layer-Wise Pruning (ECoFLaP), a two-stage approach that leverages global importance scores for determining sparsity ratios and then performs efficient layer-wise weight pruning. The computation of global importance scores is achieved using the zeroth-order approximate gradient through a forward-forward algorithm.   ECoFLaP demonstrates significant performance improvements in both multimodal and single-modal models, particularly in high-sparsity scenarios. Notably, it achieves these improvements while using only 40% of GPU memory compared to backpropagation and maintaining competitive accuracy.

### Strengths
+ Global pruning indeed faces challenges in sparsity allocation, particularly for multi-modal models. The paper provides a thorough and persuasive analysis of the motivation behind this issue.
+ The method presented in the paper is straightforward yet proven to be effective, and the experiments conducted are comprehensive.
+ The manuscript is readily understandable and offers sufficient experimental details for reproducibility.

### Weaknesses
 - There is a need for a more detailed description of Algorithm 1.
- Several metrics are used for importance scores, including weight magnitude, the multiplication of gradient and weight magnitude, gradient only, and sensitivity analysis. It would be beneficial to provide a comprehensive comparison of these metrics.
- There are some typos in this paper: (1) In Section 4.1, "and then convert the scores to sparsity by three steps" should be "and then convert the scores to sparsity by four steps"? (2) In Section 4.2, "like less than 5B parameters" should be "Like less than 5B parameters"?

### Questions
- The sparsity ratios in the experiments cover a range from 0.1 to 0.6. Is it possible to extend this range to include a wider spectrum of sparsity ratios?
- Can this method be combined with SparseGPT?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to develop an efficient pruning methods for BLIP like multimodal models. Unlike previous layer-wise pruning methods, this paper proposed a global importance score which can be efficiently approximated using the global model gradients. Layer-wise weight pruning then was applied on the multimodal model. The proposed methods were compared with recently developed pruning methods and consistently improve upon existing methods on accuracy with the same level of sparsity.

### Strengths
1. This paper is easy to consume and logically smooth.
2. The scope of this paper is well defined, which is to prune Blip-like multimodal architecture. Challenges of pruning Blip-like models were presented clearly.
3. The key idea of using zeroth-order approximated gradient makes computing the global important score efficient, which is useful.

### Weaknesses
1. In addition to the numerical comparison, can you show some example results that compare the before and after results? 
2. While it is not easy to measure the real performance improvement, can you discuss about it with the proposed pruning method?
3. Based on the importance score, what are important layers? What's the distribution of scores across all layers?

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article primarily addresses the task of model compression for Large Vision-
Language Models (LVLMs). Traditional iterative global pruning methods involve
computationally expensive operations, while layer-wise pruning approaches lack a
global perspective, potentially resulting in suboptimal performance after pruning. This
paper proposes a two-stage coarse-to-fine weight pruning approach for LVLMs, which
utilizes the global importance score for unstructured pruning.

### Strengths
1. This paper introduces a layer-wise pruning method for LVLMs that utilizes
global importance scores. The global importance score is obtained by
approximating the first-order gradients of the model parameters. By
considering the global perspective, this approach aims to effectively identify
and prune less important weights in each layer of the LVLM model.
2. This paper clearly highlights the challenges dealing multimodal compression
compared to single-modal model compression. The modularization of
multimodal models makes compression more challenging, and the paper
provides visualizations of gradients that effectively demonstrate the imbalance
in magnitude and gradient distributions between vision and language models.
3. Experimental results have shown that this method is effective across various
backbones and modal models.

### Weaknesses
1. The method in this paper is relatively simple, and novelty is insufficient.
2. The paper's writing could be improved as it lacks a theoretical analysis in the
method introduction section to explain the effectiveness of the proposed method.
Additionally, there is a scarcity of formulas in the paper, and many details are
not adequately clarified.
3. The experiments conducted were not comprehensive enough.
a) The validation of the models in the experiments was also insufficient. Only
the compression effects on the BLIPs model were tested, and the widelyused
CLIP model, which is a mainstream multimodal model, was not
evaluated. Furthermore, the comparison with the UPop model was only
conducted on the NLVR2 and COCO Caption datasets, without
comparisons on other datasets such as Flickr30k and VQA2.0.
b) The ablation study experiments were somewhat simplistic and did not
substantiate the fundamental reasons for the effectiveness of the proposed
method. It would be beneficial to enhance the content of the ablation study
experiments to provide a more detailed analysis and strengthen the overall
credibility of the article.
4. Some minor mistakes:
For example, “and then convert the scores to sparsity by three steps: (1)
Compute the total parameters that need to be selected based on p, (2) Normalize
the scores, (3) Compute the parameters that should be picked for each layer, (4)
Obtain the sparsity for each layer based on the number of parameters to be
picked and the parameters of this layer. ”
The phrase "three steps" in this sentence can also be changed to "four steps."

### Questions
See the weakness parts.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
