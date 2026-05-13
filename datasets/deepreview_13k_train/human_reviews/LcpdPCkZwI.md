# Federated Adapter on Foundation Models:  An Out-Of-Distribution Approach

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
As foundation models gain increasing attention from both academic and industrial communities, Federated Foundation Models (FedFM) have emerged as a privacy-preserving approach for collaboratively fine-tuning models in federated learning (FL) frameworks using distributed datasets across multiple clients. A key challenge for FedFM, given the versatile nature of foundation models, is addressing out-of-distribution (OOD) generalization, where unseen tasks or clients may exhibit distribution shifts leading to suboptimal performance. 
Although numerous studies have explored OOD generalization in conventional FL, these methods are inadequate for FedFM due to the challenges posed by large parameter scales and increased data heterogeneity, where large parameter scales would result in high computational and communication costs while increased data heterogeneity like cross-domain would lead to suboptimal performance of the aggregated global model on individual client distributions. To bridge this gap, we propose a new method, called FedOA, to enhance the OOD generalization of FedFM under these conditions.
Specifically, our method employs adapter-based parameter-efficient fine-tuning methods for efficient learning, and introduces an additional personalized model with a feature distance-based regularization to ensure distribution alignment and provide OOD generalization guarantees for each client. Theoretically, we demonstrate that the conventional aggregated global model in FedFM inherently retains OOD generalization capabilities, and our proposed method enhances the personalized model's OOD generalization through regularization informed by the global model, with proven convergence under general non-convex settings.
Empirically, the effectiveness of the proposed method is validated on benchmark datasets across various NLP tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the personalization and out-of-distribution generalization of adapter-based foundation models during federated fine-tuning. To tackle the data heterogeneity across local clients, the proposed framework targets at develops a personalized (fine-tuned) model for each local client, with the guidance of a global fine-tuned model. The global model is fine-tuned using the conventional federated learning scheme (i.e., minimizing the weighted empirical loss), while the personalized models are fine-tuned with a constraint that penalizes the distance between global representations and personalized representations. A theoretical analysis of the convergence rate of the proposed algorithm FedOA is provided, and its empirical performance is evaluated on four NLP datasets.

### Strengths
1. The proposed algorithm is straightforward and can be easily integrated with existing federated learning methods.

2. In designing the distance-based regularization term for training personalized models, the structural heterogeneity across the parameter-efficient fine-tuning (PEFT) methods used by local clients is taken into account.

3. This paper provides a theoretical guarantee on the convergence rate of the proposed algorithm.

### Weaknesses
1. The novelty and contributions of this paper are limited. The proposed method, FedOA, is based on the existing federated foundation model scheme, FedIT [1], with the primary distinction being the introduction of a distance-based regularization term for training personalized models.

2. The conclusion in Theorem 1 follows straightforwardly from the theoretical results presented in prior work [2]. Furthermore, minimizing the weighted empirical loss (i.e., objective (2) on page 3) does not ensure that the global model captures invariant representations. Consequently, the generalization performance of the proposed method cannot be guaranteed.

3. Since minimizing objective (2) on page 3 does not ensure that the extracted features satisfy Assumption 1, the conclusions in both Theorem 1 and Theorem 2 do not hold for the proposed algorithm. Regarding how to ensure that the invariance constraint in Assumption 1 is satisfied, it is recommended to refer to the literature on invariant learning, such as [3][4], for further details.

4. Additional details on the structure of the adopted PEFT framework should be included in the main text to aid understanding.

5. In the evaluation section, performance under partial client participation and scalability with a large number of clients is not assessed, which is significant for the applicability of the proposed algorithm in practical federated learning scenarios.

6. It appears that the setup of the test dataset for each client is not discussed in the experimental section.

### Questions
Please refer to weaknesses 1-6 outlined in the previous section.

### Soundness
2

### Presentation
2

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
The paper addresses the challenge of out-of-distribution (OOD) generalization in Federated Foundation Models (FedFM), which are affected by distribution shifts, large parameter scales, and data heterogeneity, leading to suboptimal client performance. To tackle these issues, the authors propose FedOA, an invariant learning-based approach that employs adapter-based fine-tuning for efficiency and incorporates a personalized model with feature distance-based regularization to improve OOD generalization across clients. The paper provides theoretical guarantees on OOD generalization and convergence in non-convex settings, and empirically demonstrates that FedOA outperforms existing methods on benchmark NLP tasks.

### Strengths
(a) The paper is well-written with a clear structure and logical flow, making it easy to understand the key contributions, motivation, and main theoretical and experimental findings. Additionally, the appendix provides well-organized details on the experimental setup and proofs of theorems.

(b) This work includes a rigorous theoretical convergence analysis for the proposed method and conducts evaluations on advanced NLP federated learning tasks using large language models.

(c) The ablation study is comprehensive, covering key hyper-parameters as well as detailed convergence and generalization analyses.

### Weaknesses
 (a) The connection between the proposed invariance-based FL regularization and its motivation could be clarified. It is not evident how the approach specifically addresses the challenge of large parameter scales in federated learning with foundation models, as the parameter scale issue seems to be tackled largely through the integration of parameter-efficient fine-tuning rather than through the regularization method itself.

(b) The evaluation dataset is limited in size and scope, covering only a few domains, which may not sufficiently showcase the method’s effectiveness in more diverse or large-scale federated learning environments.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes FedOA to tackle the out-of-distribution issue in federated learning with foundation models (i.e., LLM in their narrative). Their method employs adapter-based parameter-efficient fine-tuning methods for efficient learning, and introduces an additional personalized model with a feature distance-based regularization to ensure distribution alignment and provide OOD generalization guarantees for each client. Some theoretical results are also presented.

### Strengths
- Federated learning with foundation models is meaningful, so the topic is interesting.
- The presentation of this paper is good, especially the figures.

### Weaknesses
 - **Foundation models**. This paper mention that the method is for foundation models, however it is not well motivated and well justified.
  - The authors mentioned that _"A key distinction between FedFM and conventional FL lies in the scale of parameters involved"_, which I agree. But according to the theoretical analysis, I didn't see any assumptions or results that can be distinguished from conventional FL to reflect the "foundation model properties".
  - The authors mentioned that previous conventional methods cannot perform well in FedFM, however, the authors even didn't compare the conventional FL baselines in the experiments. As far as I concern, previous methods can be adapted in FedFM and also have good performances, a good reference is [1]. Instead of the full models, previous methods can be adopted in the adapter too.
  - The wording "foundation model" should be used in more careful and appropriate ways. If you are claiming your work is for foundation models, at least you should conduct experiments in various foundation models in both CV and NLP tasks with models like LLM, Diffusion models, Vision transformers, CLIP, etc. However, this paper only has experiments in LLaMA-2, which is not sufficient for LLM itself. Or, the authors can claim they target FedLLM, but they should clearly present the challenges and tailored methods for LLM instead of roughly speaking "foundation models."
- **Lack of important literature**. There are places in this paper where the authors' claims are not (or less) correct, ignoring some important literature in federated learning.
  - In lines 185-187, the authors mentioned, "However, existing methods for personalization in conventional FL often fall short in terms of generalization (Jiang & Lin, 2023; Xie et al., 2024), making them less effective for the versatile applications required in FedFM." However, there are some important works that discuss the relationship between generalization and personalization, and in some sense, both can be improved simultaneously by one method. You can refer to FedRoD [2] and FedETF [3].
  - The authors mentioned invariant learning in federated learning as their motivation. However, the most important literature is missing here. The authors should refer to DFL [4], cite it, discuss it, and compare it.
- **Technical novelty**. The main methodology of this paper is to use the global prototype as a regularization for local features. However, similar ideas already existed [5]. Therefore, the technical novelty is marginal here.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1
