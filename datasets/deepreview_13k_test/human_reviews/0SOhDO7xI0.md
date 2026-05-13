# DeepDRK: Deep Dependency Regularized Knockoff for Feature Selection

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Model-X knockoff has garnered significant attention among various feature selection methods due to its guarantees for controlling the false discovery rate (FDR). Since its introduction in parametric design, knockoff techniques have evolved to handle arbitrary data distributions using deep learning-based generative models. However, we have observed limitations in the current implementations of the deep Model-X knockoff framework. Notably, the ``swap property'' that knockoffs require often faces challenges at the sample level, resulting in diminished selection power. To address these issues, we develop ``Deep Dependency Regularized Knockoff (DeepDRK),'' a distribution-free deep learning method that effectively balances FDR and power. In DeepDRK, we introduce a novel formulation of the knockoff model as a learning problem under multi-source adversarial attacks. By employing an innovative perturbation technique, we achieve lower FDR and higher power. Our model outperforms existing benchmarks across synthetic, semi-synthetic, and real-world datasets, particularly when sample sizes are small and data distributions are non-Gaussian.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the problem of feature selection from the perspective of Model-X knockoff owing to its guarantee of false discovery rate (FDR) control.  Realizing the diminished selection power caused by the swap property that knockoffs need, the authors proposed a  Deep Dependency Regularized Knockoff (DeepDRK), which is a distribution-free deep learning method that strikes a balance between FDR and power.  Experiments on synthetic, semi-synthetic, and real-world data verify the effectiveness of the proposed DeepDRK method.

### Strengths
1. This paper is well-written and easy to follow.
2. This paper has a clear motivation for diminished selection power caused by the swap property that knockoffs need.
3. Comprehensive experiments on synthetic, semi-synthetic, and real-world data are conducted, which verify the effectiveness of the proposed DeepDRK method.
4. To me, such a distribution-free deep learning method that strikes a balance between FDR and power is new and novel.

### Weaknesses
I don't see any major weakness in this work.

### Questions
I have no more questions. I am not an expert in this field, but I feel this paper is good from the perspective of general machine learning.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed “Deep Dependency Regularized Knockoff (DeepDRK)”, a distribution-free deep learning method that strikes a balance between FDR and power. It leverages transformer architecture and several loss functions for training to generate Knockoff.

### Strengths
1. It introduces knockoff Transformer to generate knockoff with different regularizations. And it uses multi-swappers to ensure to swap property of generated knockoff.
2. Experimental results show the effectiveness of the proposed method compared to other deep model based knockoff methods.

### Weaknesses
1. Some arguments of the proposed method is not validated with corresponding experimental results. For example, “multi-swapper” is used to better achieve swap property. But there are no experiments to justify the how swap property changes when changing from single swapper to multi-swapper. I think authors should also introduce how to empirically measure the swap property. Since the proposed method relies on regularization to enforce the swap property, which is not guaranteed by design.
2. The proposed method uses many regularization terms. Some of the regularization terms have ablation studies, but others are not. For example, L_swapper and L_ED are not included. The effect of $\alpha$ in Eq.~(9) is also not investigated. Moreover, there are four hyperparameters require tuning, making the proposed method hard to tune. 
3. The regularization terms largely come from existing papers; I think authors should better justify what is their contribution on top of existing papers.

### Questions
Since most dataset is not very large, but the model size is quite large. Did authors try to change the model size to see how it impacts the performance? Maybe the model could be smaller.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes DeepDRK, a new model-X knockoff based methods which adopts a two-stage framework to generate knockoff variables. A ViT (called knockoff transformer in the paper) is trained by minimizing a swap loss plus a dependency regularization loss in the training stage, while its output is further perturb through a row-permuted version of the original covariate to reduce the dependency between knockoffs and original covaraites. Experiments on synthetic, semi-synthetic and real data demonstrates the effectiveness of DeepDRK.

### Strengths
1. Writing is good and it is easy to follow
2. The idea of leveraging distribution-free methods while avoiding overfitting is well motivated.
3. Experiment results are impressive.

### Weaknesses
1. Ablation study is not very thorough. 
- The loss in DeepDRK contains five terms, SWD, REx, cosine similarity w.r.t. swappers, SWC and the entry-wise decorrelation term. The necessity of introducing these five losses is under-explored in the paper.
- The necessity of DRP is unclear. There lacks comparison of $\tilde{X}_{\theta}$ and $\tilde{X}_{\theta}^{DRP}$ in empirical performance.
2. Experiments need further analysis and explanation. 
- It is clear that DeepDRK performs better than other baseline methods. But the reason has not been analyzed clearly and adding some intermediate results will be helpful. It is unclear how well the knockoffs generated by DeepDRK following the swap property and avoid overfitting compared to baseline methods.
- The results w.r.t. the Gaussian mixture seems inconsistent with that in the original DDLK paper (DDLK performs the worst in this paper while it performs better than deep knockoffs and knockoffgan in the original paper).

### Questions
To avoid overfitting, why introducing a post-training perturbation instead of modifying training strategy like early stopping or tuning hypermeters?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors develop a distribution-free deep learning method for knockoff generation which strikes a balance between FDR and power, called “Deep Dependency Regularized Knockoff” (DeepDRK). In DeepDRK, a “multi-swapper” adversarial training procedure is proposed to enforce the swap property, while a sliced-Wasserstein-based dependency regularization (together with a novel perturbation technique) is introduced to reduce reconstructability. Experiments on real, synthetic, and semi-synthetic datasets are carried out to show the good performance.

### Strengths
1) Proposed a distribution-free deep learning method for knockoff generation which strikes a balance between FDR and power.
2) A DeepDRK pipeline is provided to increase readability.
3) A number of experimental results are provided on simulated, semi-simulated and real datasets to illustrate the performance of the proposed method.

### Weaknesses
1) Though it enjoys theoretical result that a no free lunch situation for selection power when there is exact reconstructability in Appendix B, it seem that there is no theoretical guarantees on the power or explanations for that how the sliced-Wasserstein-based dependency regularization together with a novel perturbation technique introduced to reduce reconstructability can promote selection power.
2) It is not clear that how to enforce the swap property by the “multi-swapper” adversarial training procedure.
3) The motivation behind feature selection is high-dimensional data settings, which in my understanding means that the number of features is larger than the number of examples in the dataset. However, none of the simulated experiments include such scenario. 

Examples of writing problems:
-“Similar observations can be found in Figure 4.” seems to be “Similar observations can be found in Figure 5.” in the paragraph “Results” of section 4.4.
-“Among them, model-specific ones such as AEknockoff (Liu & Zheng, 2018) Hidden Markov Model (HMM), knockoff (Sesia et al., 2017)” seems to be “Among them, model-specific ones such as AEknockoff (Liu & Zheng, 2018), Hidden Markov Model (HMM) knockoff (Sesia et al., 2017)” in the first paragraph of section 2.2.

### Questions
(1) More explanations for the proposed method striking a balance between FDR and power.
(2)The diagram of DeepDRK pipeline and code library are given, but the algorithm for training objective (4) is not provided.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
