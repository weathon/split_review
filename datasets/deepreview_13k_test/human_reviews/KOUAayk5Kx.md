# Defying Multi-model Forgetting: Orthogonal Gradient Learning to One-shot Neural Architecture Search

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
One-shot neural architecture search (NAS) trains an over-parameterized network (termed as supernet) that assembles all the architectures as its subnets by using weight sharing, and thereby reduces much computational budget. However, there is an issue of multi-model forgetting about supernet training in one-shot NAS that some weights of the previously well-trained architecture will be overwritten by that of the newly sampled architecture which has overlapped structures with the old one. To overcome the issue, we propose an orthogonal gradient learning (OGL) guided supernet training paradigm for one-shot NAS, where the novelty lies in the fact that the weights of the overlapped structures of current architecture are updated in the orthogonal direction to the gradient space of these overlapped structures of all previously trained architectures. Moreover, a new approach of calculating the projection is designed to effectively find the base vectors of the gradient space to acquire the orthogonal direction. We have theoretically and experimentally proved the effectiveness of the proposed paradigm in overcoming the multi-model forgetting. Besides, we apply the proposed paradigm to two one-shot NAS baselines, and experimental results have demonstrated that our approach is able to mitigate the multi-model forgetting and enhance the predictive ability of the supernet in one-shot NAS with remarkable efficiency on popular test datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new method called Orthogonal Gradient Learning (OGL) to overcome multi-model forgetting in one-shot NAS. It updates weights of overlapped structures in the orthogonal direction to the gradient space of previously trained architectures. This avoids overwriting well-trained models while training new architectures sequentially. A PCA-based projection is used to find orthogonal directions without storing all past gradient vectors. OGL is integrated into RandomNAS and GDAS one-shot NAS baselines. Experiments show OGL reduces forgetting, leading to better final architectures and stronger supernet predictive ability.

### Strengths
**Strengths**:

- Original idea of using orthogonal gradient updates to avoid catastrophic forgetting in NAS.

- Technically sound approach grounded in theory with clear algorithm design and experimental methodology.

- Strong empirical results demonstrating reduced forgetting and improved search performance compared to baselines.

- The PCA-based projection to compute orthogonal gradients is creative and helps address a key limitation.

- OGL seems widely applicable to enhance different one-shot NAS methods as shown by results on two baselines.

### Weaknesses
**Weaknesses**:

- Theoretical analysis is limited, more formal convergence guarantees could strengthen the approach.

- Certain details like schedule for gradient space updates are unclear. Sensitivity to hyper-parameters not fully studied.

- Experiments focus on small CNN search spaces, evaluating on larger spaces like transformers could be useful.

- Qualitative analysis into why and how OGL architectures differ from baseline NAS would provide more insight. 

- Extending OGL to other architecture search domains like hyperparameter optimization could further demonstrate generality.

### Questions
see Weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work focus on solving the problem of multi-model forgetting in neural architecture search (NAS) . To address this problem, the authors propose an Orthogonal Gradient Learning (OGL) for one-shot NAS-guided supernet training. This method updates the weights of the overlapping structures of the current architecture in directions orthogonal to the gradient space of these structures in all previously trained architectures.

The authors provide experimental evidence supporting the effectiveness of the proposed paradigm in mitigating multi-model forgetting.

### Strengths
the authors propose the Orthogonal Gradient Learning (OGL) . This method updates the weights of the overlapping structures of the current architecture in directions orthogonal to the gradient space of these structures in all previously trained architectures.

The authors provide experimental evidence supporting the effectiveness of the proposed paradigm in mitigating multi-model forgetting.

### Weaknesses
The proposed orthogonal gradient learning (OGL) guided supernet training method may be sensitive to hyperparameters. The paper should conduct a more detailed analysis of the impact of hyperparameters on the robustness of the method.

This paper mentions the theoretical support for the proposed approach, but the assumptions made in these theoretical proofs and their relevance to actual NAS scenarios should be detailed.

### Questions
This paper aims to reduce the computational budget in NAS; it should provide a more complete analysis of the computational cost introduced by the OGL approach, as this can be an issue in resource-constrained environments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the main objective of the research is to train a supernet effectively to overcome the problem of multi-model forgetting in one-shot Neural Architecture Search (NAS). To address this issue, the authors propose a method called Orthogonal Gradient Learning (OGL) to update the weights of the current architecture in a way that they become orthogonal to the constructed gradient space. A series of experiments are conducted in this paper on multiple datasets to evaluate the effectiveness of OGL in addressing the multi-model forgetting problem.

### Strengths
（1）The logic of this paper is clear and it is easy to read.
（2）OGL offers a fresh perspective for one-shot NAS, especially in addressing the multi-model forgetting issue. Compared to existing suboptimal methods, it exhibits superior performance across multiple datasets.

### Weaknesses
（1）Figure 4: (a) is quite messy, and the curves for different network architectures cannot be clearly distinguished and compared. Please provide a more intuitive explanation and presentation method.
（2）Although RandomNAS-OGL has a slight advantage in test error rate in Table 2, PDARTS is superior in terms of model size and computational complexity.All things considered, I believe the latter is more superior than your model. Please find a better approach to optimize your model.
（3）The storage and computational overhead are issues you need to consider at the moment, as they will greatly limit you in real-world application scenarios.
（4）When comparing performance, many methods were not reprouced or their true performance metrics were not obtained. Therefore, I believe your comparison is lacking and not comprehensive.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
