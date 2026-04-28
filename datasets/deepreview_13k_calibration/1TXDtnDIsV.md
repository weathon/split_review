# Learning Mamba as a Continual Learner

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
Continual learning (CL) aims to efficiently learn and accumulate knowledge from a data stream with different distributions. By formulating CL as a sequence prediction task, meta-continual learning (MCL) enables to meta-learn an efficient continual learner based on the recent advanced sequence models, \eg, Transformers. Although attention-free models (\eg, Linear Transformers) can ideally match CL's essential objective and efficiency requirements, they usually perform not well in MCL. Considering that the attention-free Mamba achieves excellent performances matching Transformers' on general sequence modeling tasks, in this paper, we aim to answer a question -- \emph{Can attention-free Mamba perform well on MCL?} By formulating Mamba with a selective state space model (SSM) for MCL tasks, we propose to meta-learn Mamba as a continual learner, referred to as \textbf{MambaCL}. By incorporating a selectivity regularization, we can effectively train MambaCL. Through comprehensive experiments across various CL tasks, we also explore \emph{how Mamba and other models perform in different MCL scenarios}. Our experiments and analyses highlight the promising performance and generalization capabilities of Mamba in MCL.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper follows the meta continual learning (MCL) framework as outlined by Lee et al., 2024. The authors meta-train sequential models on offline meta-training sequences to enhance their sequence modelling capability. The authors propose using Mamba as the sequential model instead of transformers or attention-free variants to alleviate high computational costs while still achieving satisfactory performance. Additionally, the authors introduce a selective regularization technique for meta-training, which enhances the association between query tokens and previously correlated input tokens. Experimental results demonstrate that Mamba achieves improved generalization and robustness compared to transformer variants in MCL, while using less memory for inference.

### Strengths
- The paper is well-structured and easy to follow.
- The authors clearly explained the issue of increased compute complexity with using transformers for MCL.

### Weaknesses
In general:

- The paper shows limited novelty. The problem formulation, specifically the recasting of the continual learning problem as a sequential modelling problem in recurrent models, mirrors the previous work by Lee et al., 2024. From the technical side, the authors propose a new selective regularization technique for meta-training and claim it improves training stability and convergence. While the technique itself is novel, there are several questionable aspects regarding this technique and the authors' claims. I cannot fully credit the novelty of this technique until these issues are addressed.

- Although the authors claim better generalization and robustness when using Mamba instead of transformers based on empirical results, these results appear somewhat questionable. Furthermore, there is a lack of new insights and detailed analysis; for instance, the authors did not delve deeper into the underlying mechanisms that led to these results. This deeper analysis is crucial, especially if the primary motivation of the paper is to use Mamba (or any different model architecture) instead of transformers for the same problem settings.

Please kindly refer to the questions for more details.


**Claims on the Effectiveness of the Proposed Regularization Technique**

- For example, lines 326-329 state:
  > We apply this regularization to MambaCL and other sequence prediction models (weighted by a scalar λ) together with the MCL objective in Eq. (7), which improves the meta-training stability and convergence for all models.

- The authors do not fully support their claims about "improving the meta-training stability and convergence for all models." Specifically, there are no experiments showing learning curves (or similar alternatives) for all models during meta-training to compare results with and without this technique. 

- A seemingly related empirical evidence is presented in Figure 4. However, the results appear to pertain to a *single* model, and it is unclear, based on the figure caption and the text in lines 481-485, which specific model (i.e., Mamba, transformers) was used in this ablation study. Although the experiment demonstrates the sensitivity of meta-testing performance to the regularization strength, it lacks comprehensive evidence across multiple models to support the authors claim.


**Experiment Implementation Details**

- In the paper, it is mentioned: 
  > Following Lee et al., 2024, we set the initial learning rate to 1 × 10⁻⁴...

- Cloud the authors please provide some motivations for using the same hyperparameters as in Lee et al., 2024, given that the meta-training setups differ? Specifically, the authors used a pre-trained CLIP backbone as a visual encoder and included the proposed regularization loss across all models. 

- Moreover, were these hyperparameters adjusted for different model architectures based on some meta-validation sets, e.g., for linear transformers and Mamba? If not, wouldn't using fixed hyperparameters for all experiments and models potentially lead to sub-optimal results? If these hyperparameters are not optimal for every models, this could produce misleading results and potentially invalidate the observations.

**Meta-Overfitting in Figures 3a and 3b**

- The authors observed that transformers and their variants seem to suffer from severe meta-overfitting based on the results in Figures 3a and 3b. However, the potential underlying causes for this overfitting are quite unclear. Specifically:

  - As previously mentioned, based on the current description of the implementation details, it's unclear whether this overfitting is due to the use of improper hyperparameters, such as learning rates.

  - Additionally, it is undetermined whether this overfitting is influenced by the use of regularization terms for all models during meta-training. Would removing this regularization loss for transformers significantly reduce meta-overfitting?

- Could the authors please provide some insights into why Mamba did not suffer from the same degree of overfitting?

- While the occurrence of meta-overfitting is expected, the degree of overfitting—particularly in relation to the number of training tasks and training shots used in meta-training—exhibited by transformers and their variants in Figures 3a and 3b is somewhat surprising. Specifically, in Figure 3b, adding more training shots per class even, and almost monotonically, decreased the classification accuracy on the queries.


**Robustness in Figure 3c**

- It is somewhat unclear how the authors performed the input noise perturbation. Specifically, what does $ x_i$ in line 473 refer to? Is it the original input image to the CLIP encoder, or the extracted image embeddings that serve as inputs to the sequential learning models?

- I find it very interesting that Mamba exhibits excellent robustness to input noise, even with a standard deviation as large as 10. Could the authors potentially discuss some potential reasons behind Mamba's extreme robustness to large input noise?

**General Comments on MCL**

- Some important challenges in the MCL setup for continual learning include: 1) its application to long continual learning sequences, 2) the requirement for offline training datasets (meta-training), and 3) generalization to unseen long OOD meta-testing tasks. These challenges cannot be resolved simply by switching from transformers or their variants to Mamba.

- Are there any differences on the problem formulation and the meta-training setups between the ones in the paper and the one in MetaICL: Learning to Learn In Context, Min et al., NAACL 2022?

### Questions
I am open to discussion and willing to reconsider my score if my major concerns can be adequately addressed.


**Claims on the Effectiveness of the Proposed Regularization Technique**

- For example, lines 326-329 state:
  > We apply this regularization to MambaCL and other sequence prediction models (weighted by a scalar λ) together with the MCL objective in Eq. (7), which improves the meta-training stability and convergence for all models.

- The authors do not fully support their claims about "improving the meta-training stability and convergence for all models." Specifically, there are no experiments showing learning curves (or similar alternatives) for all models during meta-training to compare results with and without this technique. 

- A seemingly related empirical evidence is presented in Figure 4. However, the results appear to pertain to a *single* model, and it is unclear, based on the figure caption and the text in lines 481-485, which specific model (i.e., Mamba, transformers) was used in this ablation study. Although the experiment demonstrates the sensitivity of meta-testing performance to the regularization strength, it lacks comprehensive evidence across multiple models to support the authors claim.


**Experiment Implementation Details**

- In the paper, it is mentioned: 
  > Following Lee et al., 2024, we set the initial learning rate to 1 × 10⁻⁴...

- Cloud the authors please provide some motivations for using the same hyperparameters as in Lee et al., 2024, given that the meta-training setups differ? Specifically, the authors used a pre-trained CLIP backbone as a visual encoder and included the proposed regularization loss across all models. 

- Moreover, were these hyperparameters adjusted for different model architectures based on some meta-validation sets, e.g., for linear transformers and Mamba? If not, wouldn't using fixed hyperparameters for all experiments and models potentially lead to sub-optimal results? If these hyperparameters are not optimal for every models, this could produce misleading results and potentially invalidate the observations.

**Meta-Overfitting in Figures 3a and 3b**

- The authors observed that transformers and their variants seem to suffer from severe meta-overfitting based on the results in Figures 3a and 3b. However, the potential underlying causes for this overfitting are quite unclear. Specifically:

  - As previously mentioned, based on the current description of the implementation details, it's unclear whether this overfitting is due to the use of improper hyperparameters, such as learning rates.

  - Additionally, it is undetermined whether this overfitting is influenced by the use of regularization terms for all models during meta-training. Would removing this regularization loss for transformers significantly reduce meta-overfitting?

- Could the authors please provide some insights into why Mamba did not suffer from the same degree of overfitting?

- While the occurrence of meta-overfitting is expected, the degree of overfitting—particularly in relation to the number of training tasks and training shots used in meta-training—exhibited by transformers and their variants in Figures 3a and 3b is somewhat surprising. Specifically, in Figure 3b, adding more training shots per class even, and almost monotonically, decreased the classification accuracy on the queries.


**Robustness in Figure 3c**

- It is somewhat unclear how the authors performed the input noise perturbation. Specifically, what does $ x_i$ in line 473 refer to? Is it the original input image to the CLIP encoder, or the extracted image embeddings that serve as inputs to the sequential learning models?

- I find it very interesting that Mamba exhibits excellent robustness to input noise, even with a standard deviation as large as 10. Could the authors potentially discuss some potential reasons behind Mamba's extreme robustness to large input noise?

**General Comments on MCL**

- Some important challenges in the MCL setup for continual learning include: 1) its application to long continual learning sequences, 2) the requirement for offline training datasets (meta-training), and 3) generalization to unseen long OOD meta-testing tasks. These challenges cannot be resolved simply by switching from transformers or their variants to Mamba.

- Are there any differences on the problem formulation and the meta-training setups between the ones in the paper and the one in MetaICL: Learning to Learn In Context, Min et al., NAACL 2022?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses meta-continual learning using a state space model Mamba. It performs comprehensive experiments across various CL benchmarks and reports several interesting results, including comparison with Transformers and extension to Mamba mixture-of-experts.

### Strengths
1. It proposes MambaCL as a strong sequential approach to meta-continual learning. 

2. It performs thorough experiments and discover multiple interesting observations.
- The use of Mamba may be more helpful for generalization over Transformers as discussed in Fig.3.
- MambaCL is particularly effective in on fine-grained recognition tasks as shown in Table 3.
- Integration of Mamba with MoE improves the MCL performance as reported in Table 6.

### Weaknesses
1. The technical novelty is limited.
- This work is largely based on the work of (Lee et al., 2024), which first formulates the MCL problem as a sequent modeling.
- This work simply replaces Transformers of (Lee et al., 2024) with a state space model Mamba. 
- Except this replacement, there is little novelty as its application is rather straightforward, following (Lee et al., 2024). The core idea of using a sequential model for meta-continual learning is directly adopted, and the adaptation of Mamba appears to be a relatively direct substitution without significant methodological innovation. The paper does not introduce any novel training strategies or architectural modifications specific to the meta-continual learning setting that would justify the claim of technical novelty beyond the model replacement.

2. The use of Mamba instead of Transformers leads to little performance improvement as reported in Table 1-5. 
- The main benefit of Mamba over Transformer lies in fewer parameters and increased processing speed as shown in Table 7. While the computational advantages of Mamba are acknowledged, the lack of substantial performance gains in the meta-continual learning context raises questions about the practical significance of this substitution. The experiments do not convincingly demonstrate that Mamba offers any unique advantages in terms of learning ability or generalization compared to Transformers, which undermines the motivation for using Mamba in this specific application.

3. Implementation details are missing. 
- Appendix is too sketchy to fully understand how the MambaCL is implemented. 
- The code is not provided. The absence of detailed implementation information, particularly regarding the specific configurations of the Mamba model and the training procedure, makes it difficult to reproduce the results. The lack of publicly available code further hinders the verification of the claims and the adoption of the proposed method by the research community. The description of the Mamba block is insufficient, lacking specifics on how the state space model is integrated into the meta-learning framework, and how the model handles the sequential nature of the data.

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors explore a key research question: Can the attention-free Mamba model effectively handle meta-continual learning (MCL) tasks? They reframe State Space Models (SSM) and Mamba as sequence-prediction-based continual learners, training them via meta-learning across continual learning episodes. To enhance this training, they introduce a selectivity regularization technique. Extensive experiments reveal that Mamba consistently performs well in various MCL settings, significantly surpassing other attention-free approaches and often equaling or surpassing Transformer models in performance—all while using fewer parameters and computational resources. Notably, Mamba demonstrates strong reliability, generalization, and robustness in complex scenarios.

### Strengths
* It is interesting to explore how  Mamba performs in a meta-continual learning setting.

### Weaknesses
 * The conclusion of this paper is unsurprising, as Mamba's MCL performance aligns closely with its results on standard benchmarks.

* There is insufficient analysis explaining how and why Mamba outperforms other attention-free architectures and achieves comparable results to Transformer-based models.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2
