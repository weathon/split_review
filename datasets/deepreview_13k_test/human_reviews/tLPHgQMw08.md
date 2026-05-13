# Risk-Aware Distributional Intervention Policies for Language Models

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
Language models are prone to occasionally undesirable generations, such as harmful or toxic content, despite their impressive capability to produce texts that appear accurate and coherent. In this paper, we present a new two-stage approach to detect and mitigate undesirable content generations by rectifying activations. First, we train an ensemble of layer-wise classifiers to detect undesirable content using activations by minimizing a smooth surrogate of the risk-aware score. Then, for contents that are detected as undesirable, we propose layer-wise distributional intervention policies that perturb the attention heads minimally while guaranteeing probabilistically the effectiveness of the intervention. Benchmarks on several language models and datasets show that our method outperforms baselines in reducing the generation of undesirable output.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses challenge of guiding language generation away from undesirable outputs (e.g., non-truthful responses) towards more desirable ones (e.g., truthful responses). The proposed method tackles this by intervening at the head level within a transformer model. This involves: (1) training a linear classifier to detect when an undesirable output is being generated for each head, and (2) applying an affine transformation to shift these detected head's outputs towards desirable ones. The classifier is trained using supervised learning, with a hyperparameter to balance false-positive and false-negative. Then, the method employs a distribution-matching loss to ensure that the transformation minimally diverges from the original activation while ensuring that the classifier (trained in (1)) confidently identifies activation vectors as 'desirable'. This approach tradeoffs the degree of the shift introduced and the confidence of the classifier.

### Strengths
(1) Interesting and significant application.
(2) Introduce a trade-off between preserving original information and matching the 'desirable' distribution makes sense to me.
(3) Strong results on QA

### Weaknesses
I mix here aspects which I perceive as weakness is some aspects which are not entirely clearly to me and which I would like authors to clarify

1) The proposed RADIANT approach builds on ITI by Li et al. (2023), and the differences are the 'risk-aware' optimization for learning probes, the constraint that affected heads are in the same layer, and the specific optimization objective. The first two differences are clear, and the ablation studies suggest they have tangible benefits. However, I’m less certain about the intuition behind the optimization objective itself. For instance,  I understand that the step size in the 'truthfulness direction' as defined in ITI might not always be appropriate (e.g., it’s unclear why that specific size is optimal or whether a good hyperparameter alpha can be consistently set across all heads) and the idea of taking the smallest step to meet the probabilistic constraint (as in RADIANT) aligns with my intuition; I find it compelling.  But the part I find puzzling is the requirement to match as closely the covariance of the original 'undesirable' (non-intervened) activations with the 'corrected'  activations. This objective seems to differ fundamentally from a similar regularization term in MiMiC by Singh et al. (2024), which aims to match intervened data with 'desirable' data. There, the goal is clear: it ensures that the data distributions are indistinguishable by any classifier; this makes sense to have this constraint on the distribution level. Here, though, I don’t quite understand why enforcing a distributional similarity between the undesirable activations and intervened steps is better than simply making the smallest step necessary for every activation (with the step size define according to the probabilistic constraint). Could the authors clarify the rationale behind this assumption?

(2) The paper includes comparisons with ITI but lacks an explicit comparison with MiMiC. Given that MiMiC has been available on arXiv for 7 months before the ICLR 2025 deadline, such analysis may be expected. The authors claim that MiMiC does not preserve semantics (and I tend to believe i), but I would like to see empirical confirmation of this in the paper.

(3)  The evaluation primarily focuses on QA tasks (TrustfulQA in the main paper + two other QA datasets in appendix).  Is not the idea more broad than that? I would have like the approach to be applied to a broader range of generation tasks, and types of interventions.

(4)  MiMiC ensures that a broad class of classifiers cannot distinguish post-intervention activations from desirable ones, implicitly implying that furrther layers cannot see the differnce. In contrast, this method optimizes protection against only specific classifier trained in the first stage. Is this a limitation? Consequently, it’s possible that a different classifier could still distinguish the activations. Could this  affect the robustness of the intervention?

(5) Why uniformly weighting divergences in mean and variance in objective (3). Why this specific way of measuring the divergence between distributions?  (Though I have a more general question, why define this objective in terms of proabilities)

(6) Section 3 is a bit dense, and giving some intuitions up-front would make it a more enjoyable read.

### Questions
See above, all my comments are at the same time questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Language models are prone to occasionally undesirable generations. This paper proposes a two-stage framework RADIANT to improve the language model output in the inference stage. In the first stage, RADIANT trains an ensemble of layer-wise classifiers to detect undesirable content using activations by probing the language model. In the second stage, for contents that are detected as undesirable, the method proposes layer-wise distributional intervention policies that perturb the attention heads minimally with a simple linear map.

In this paper, various experiments and comparisons on TruthfulQA are conducted to verify the effectiveness of the proposed method RADIANT.

### Strengths
The strengths of this paper can be listed as follows:
1. The optimal headwise interventions method proposed in this paper is motivating. The method has achieved a good performance both in theory and experiments.
2. The paper has conducted detailed experiments on TruthfulQA dataset to compare RADIANT with different kinds of baselines.

### Weaknesses
The weaknesses of this paper can be listed as follows:
1. **Bad paper writing.** I think there exists a big problem in paper writing. The organization of the paper is rather confusing. For example, some settings in Section 2 can be explained in the experimental settings in Section 4 or Appendix. I also don’t like the description in Section 3. The paper puts together too many symbolic definitions, which takes me a lot of time to understand. In addition, the presentations of the experimental results in table 1, table 2 and table 3 are redundant. The information can be summarized in one table instead. 
2. **Limited experiment datasets.** The experiments in the paper mostly focus on TruthfulQA without considering other tasks to show the effectiveness of RADIANT on other datasets. As the paper discussed controllable text generation, I think many tasks in controllable text generation can be used to conduct experiments, such as sentiment controllable generation, detoxification, etc.
3. **Limited baselines.** The baselines listed in this paper are limited. I think this type of method like RADIANT that intervene the generation stage needs to be compared with the controllable decoding method, for example, Dexperts (https://aclanthology.org/2021.acl-long.522/).

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces RADIANT, a novel two-stage approach for detecting and mitigating undesirable content in language models. The method involves training layerwise classifiers to identify harmful outputs and employing headwise distributional interventions to adjust model activations. RADIANT offers a resource-efficient solution with probabilistic guarantees for effectiveness.

### Strengths
The paper introduces a novel two-stage method, RADIANT, for detecting and mitigating undesirable content in language models. This method combines layerwise classifiers and headwise interventions.

The method is empirically validated on several benchmarks, including TruthfulQA, demonstrating its effectiveness compared to existing baselines.

### Weaknesses
1. The proposed method, RADIANT, appears to offer minimal modifications compared to the Inference-Time Intervention (ITI) method. The main difference lies in the selection of attention heads between RADIANT and ITI. This slight variation may not constitute a significant advancement over existing methods.

2. The paper does not sufficiently compare RADIANT with other related methods in the field. The following works should be considered for comparison:

[1] Truth Forest: Toward Multi-Scale Truthfulness in Large Language Models through Intervention without Tuning

[2] Non-Linear Inference Time Intervention: Improving LLM Truthfulness

[3] Enhanced Language Model Truthfulness with Learnable Intervention and Uncertainty Expression

3. The paper lacks results from Supervised Fine-Tuning (SFT) as a baseline, which is important for benchmarking. Referring to the experimental settings used in ITI and including SFT results would allow for a more comprehensive comparison.

3. A major limitation is the narrow focus on a limited number of datasets. Most experiments are conducted on the TruthfulQA dataset, with minimal generalization to only two additional datasets. This raises concerns about whether the effectiveness of RADIANT is universally applicable or specific to TruthfulQA. More tests on a variety of datasets would strengthen the paper.

4. The method for determining the crucial hyper-parameter remains ambiguous. It's unclear whether the hyper-parameters $\alpha$ and $ \Gamma $ are universally applicable or requires case-by-case optimization. Considering the improvement provided by RADIANT, selecting an appropriate hyper-parameter is vital, as suggested by Table 6 and Table 7.  However, the paper fails to explain how this selection should be done.

5. It seems that the method may be limited to the LLaMA family of models. Conducting experiments on LLMs from other families could demonstrate the broader applicability of RADIANT.

6. RADIANT shows an increase in CE and KL divergence compared to ITI, suggesting that the method deviates from the initial distribution. This could indicate potential adverse effects on the model's performance on other tasks. The paper should address this concern and discuss how RADIANT impacts overall model performance.

### Questions
1. What are the cost differences between ITI and RADIANT as presented in Table 5? 

2. How is the difference between generation accuracy and probe accuracy used in the evaluation?

3. The equations and symbols presented in the paper can be challenging to follow without clear explanations of each component and its role in the method. Providing detailed descriptions and context would improve readability and comprehension.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for detecting and mitigating undesirable content generation, which includes a set of classifiers and an intervention strategy. The intervention strategy is derived by the authors based on statistical theory and has shown promising results on the LLaMA model.

### Strengths
1. This paper proposes a novel intervention strategy to mitigate undesirable content generation, which is a significant research problem.
2. The authors propose three criteria for layer-wise intervention and conduct corresponding mathematical modeling and statistical analysis.
3. The authors demonstrate the effectiveness of this method through experiments.

### Weaknesses
The derivation of the intervention method in this paper is based on the assumption that distributions P and Q follow a normal distribution. Can the authors verify that the activation values sampled at each layer in LLMs indeed follow a normal distribution? If P and Q follow other distributions, can the method in this paper be correspondingly adapted?

### Questions
1. When combining Few-shot prompting with the RADIANT method, will the accuracy of the classifier obtained in the first stage change? Is it necessary to retrain the classifier?
2. How does the accuracy of the first-stage classifier affect the effectiveness of the second-stage intervention method? The paper uses a Linear Logistic Classifier as the classifier in the first stage; if a more accurate classifier is used, can the intervention effectiveness be further improved?
3. As shown in Figure 1 of the paper, there are significant differences in classifier accuracy across different model layers. Is it possible to only select certain model layers for the second-stage intervention?

### Soundness
3

### Presentation
3

### Contribution
3
