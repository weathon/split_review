# LoRA-Ensemble: Efficient Uncertainty Modelling for Self-attention Networks

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Numerous crucial tasks in real-world decision-making rely on machine learning algorithms with calibrated uncertainty estimates. However, modern methods often yield overconfident and uncalibrated predictions. Various approaches involve training an ensemble of separate models to quantify the uncertainty related to the model itself, known as epistemic uncertainty. In an explicit implementation, the ensemble approach has high computational cost and high memory requirements. This particular challenge is evident in state-of-the-art neural networks such as transformers, where even a single network is already demanding in terms of compute and memory. Consequently, efforts are made to emulate the ensemble model without actually instantiating separate ensemble members, referred to as implicit ensembling. We introduce LoRA-Ensemble, a parameter-efficient deep ensemble method for self-attention networks, which is based on Low-Rank Adaptation (LoRA). Initially developed for efficient LLM fine-tuning, we extend LoRA to an implicit ensembling approach. By employing a single pre-trained self-attention network with weights shared across all members, we train member-specific low-rank matrices for the attention projections. Our method exhibits superior calibration compared to explicit ensembles and achieves similar or better accuracy across various prediction tasks and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper creates ensembles by starting from a base model and adapting each member independently using LoRA adapters. Each LoRA module adds a small, low-rank learnable matrix to the MLP of Transformers. Experiments on datasets like CIFAR-100, HAM10000, ESC-50 show that these ensembles can give better performance and calibration.

### Strengths
* S1. Creating lightweight ensembles, requiring fewer resources at training time and test time is a good and relevant direction.

* S2. The approach of using LoRA in ensembles is sound and has good potential.

### Weaknesses
 * W1. The approach is simple, ensembling is a classic technique and LoRA is one of the most used ways to fine-tune a pre-trained model in the context of large models. Having a simple method is usually a good aspect, but when the method is straightforward we need a higher bar for results and investigations. In this paper, experiments are mostly made on small datasets and it doesn’t seem like we gain that much from them. Also, combining ensembling and LoRA has been investigated in the context of LLMs [A]. It doesn’t seem like this paper has any additional insights. The authors can also check the reviews of [A] on Openreview for additional related work.

* W2. Small scale experiments. The experiments in this paper are rather on a small scale. Given the simplicity of the method, we need to evaluate it more thoroughly. 

* W3. More baselines are needed. It seems like adding a LoRA module to Single Network gives an important boost, comparable to the ensembling (3% vs 5.9% on Cifar100 classification, 4.8% vs 6.5% on AURPC in OOD detection). It seems that benefits come from adding more learnable parameters, either by LoRA or by ensembling. Thus a single Single Network with a bigger LoRA module (similar number of parameters as the LoRA ensemble) would be a good baseline. Training single, or ensemble method with the same number of parameters would also represent good additional baselines.

### Questions
Did the authors did any comparisons where they fix the number of parameters, or computational budget (at training or testing) between LoRA ensembles and other baselines? Such comparisons would be very relevant.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors address the challenge of overconfident and uncalibrated predictions in machine learning algorithms, specifically in state-of-the-art neural networks like transformers. They propose a parameter-efficient deep ensemble method called LoRA-Ensemble, which is based on Low-Rank Adaptation (LoRA). This method emulates the ensemble model without the need for separate ensemble members, making it computationally and memory efficient. By training member-specific low-rank matrices for attention projections in a single pre-trained self-attention network, LoRA-Ensemble achieves superior calibration compared to explicit ensembles and performs well across various prediction tasks and datasets. The authors demonstrate the effectiveness of LoRA-Ensemble in different classification tasks, including image labeling, skin lesion classification, sound classification, and out-of-distribution detection.

### Strengths
1.	Improved uncertainty calibration: the authors demonstrate that LoRA-Ensemble achieves superior calibration compared to explicit ensembles. This means that the predicted probabilities of the model align more closely with the true probabilities, resulting in more reliable and accurate predictions. 
2.	Computational and memory efficiency: One strength of the LoRA-Ensemble method is its ability to emulate an ensemble model without the need for separate ensemble members. This makes it computationally and memory efficient compared to explicit ensemble methods, which require training and storing multiple models.

### Weaknesses
1.	Theoretical analysis is lacking regarding the relationship between the LoRA ensemble and probability distribution. It would be beneficial to provide a theoretical proof of how the LoRA ensemble can approximate the underlying distribution more effectively. Specifically, a derivation or at least a strong argument connecting the low-rank updates to the approximation of a more complex, potentially multimodal, posterior distribution would be valuable. The current work lacks a clear explanation of why the low-rank adaptation encourages the exploration of diverse solutions, rather than converging to a single, potentially suboptimal, mode.
2.	Additionally, the analysis on why the LoRA ensemble can prevent the degeneration of ensemble members into a point estimate is missing. It would be helpful to include a discussion on how the diversities of ensemble members are maintained through random initialization. The paper should delve into the specifics of how the random initialization of the low-rank matrices interacts with the pre-trained weights and the optimization process to ensure that each member explores a different region of the loss landscape. A more detailed analysis of the loss landscape and the trajectories of individual ensemble members would be beneficial.
3.	Lack of evaluation on large-scale datasets. LoRA may face overfitting issues, especially when applied to complex tasks. It would be valuable to assess its performance on larger datasets, such as ImageNet-1K, to gain a better understanding of its capabilities in such scenarios. The current evaluation is limited to relatively small datasets, which may not fully reflect the challenges of real-world applications. The paper should include experiments on datasets with a greater number of classes and more complex data distributions to demonstrate the robustness and scalability of the proposed method.

### Questions
While it is reasonable to use CIFAR100 as the in-distribution data and CIFAR-10 as the out-of-distribution data, it would be more comprehensive to include additional out-of-distribution datasets as well. Additionally, it would be beneficial to provide a detailed comparison with existing benchmarks, such as OpenOOD[1], which is widely used for evaluating out-of-distribution detection methods. 
[1] OpenOOD: Benchmarking Generalized Out-of-Distribution Detection. arXiv:2210.07242 [cs.CV]

### Soundness
2

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
2

### Summary
The paper introduces LoRA-Ensemble, an method for parameter-efficient ensebmling for self-attention networks. Key idea is to have different low-rank matrices for each ensemble component keeping the backbone frozen. The LoRA matrices are applied only to the self-attention layer making the proposed approach parameter efficient. The proposed method is computationally efficient, improves over traditional ensemble methods, and improves both the accuracy and calibration for multiple classification tasks.

### Strengths
- The paper is generally well written and easy to follow. 
- The proposed ensemble method: LoRA-Ensemble is intuitive, and simple. It can easily be extended to different transformer-based classification tasks. 
- LoRA-Ensemble improves both the predictive accuracy and the calibration performance on the considered classification tasks. 
- Propoed method is empirically validated and is parameter/computation efficient.

### Weaknesses
 - Limited Theoretical insights and empirical validation: The proposed approach is heuristic and is only empirically validated on limited datasets that are relatively simple. Though challenging, the work could be strengthened with some theoretical analysis and guarantees for the proposed technique.  Alternatively, the work could be significantly strengthened by carrying out experiments on more challenging vision datasets of Fine-Grained Visual Classification tasks (see Visual Prompt tuning by Jia et al), Visual Task Adaptation Benchmark/VTAB ( A large-scale study of representation learning with the visual task adaptation benchmark, Zhai et al ), and/or tasks beyond classification (maybe for segmentation/object detection).

- Paper formatting and presentation could be improved: For eg. Table 2, Table 3, Table 7 all overflow.

- For codes, it would have been helpful if codes were included as supplementary material, or at an annonymized github link.

- Post-hoc and other calibration techniques be introduced to further improve the calibration/under-confidence issue, and miscalibration in the baseline models. Discussion and empirical analysis of calibration techniques seems to be missing. 

- Some important works in  epistemic uncertainty estimation are missing: The authors miss literature on Evidential Deep Learning (A Comprehensive Survey on Evidential Deep Learning and Its Applications), and second order based UQ  (Second-Order Uncertainty Quantification: A Distance-Based Approach). These works propose computationally efficient alternatives for UQ, can be extended to DL approaches, and can enable UQ a single forward pass as they do not involve the computational overhead of ensemble. Discussion, and comparison with these works could further strengthen the work.

### Questions
Please see and address the comments on the weakness section. Additionally, here are some clarifying questions I have. 
- Considering the relatively simple datasets, how would the approach scale to large datasets such as imagenet?
- For OOD experiment with Cifar100, it would be interesting to see performance on SVHN as the OOD dataset. I think SVHN is more realistic OOD for Cifar100/Cifar10 comapred to using CIfar10 as OOD for Cifar100.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a novel method for uncertainty estimation in neural networks based on the low-rank adaptation (LoRA) approach. In a nutshell, the method trains several sets of low-rank matrices (commonly used for adaptation/fine-tuning of a pretrained model) and, during inference, runs predictions using all of them, then averages the outputs. Experiments on several benchmarks across various domains demonstrate that the proposed method outperforms several popular ensembling approaches, including (in some cases) deep ensembling. The method improves the final model's performance (e.g., in terms of accuracy), aleatoric uncertainty (measured by calibration metrics), and epistemic uncertainty (in terms of OOD detection quality). At the same time, the method induces significantly lower computational and memory overhead, as well as faster training, compared to conventional ensembles. The proposed approach is relatively simple to use with various attention-based architectures, although it is somewhat limited to them.

### Strengths
* The paper is clearly written and easy to follow. The idea is intuitive and easy to grasp. The related work section provides an adequate discussion of existing approaches to both LoRA and uncertainty estimation for deep learning. The analysis narrative, with the presented drawbacks of existing methods (such deep ensembles), is very clear and easy to understand

* The method is straightforward to apply, requiring only a (potentially pretrained) model and the training of a number of LoRA adapters. During inference, predictions from these adapters are averaged, making implementation efficient and compatible with existing architectures

* The approach is significantly more efficient than traditional (deep-)ensembling, offering reduced computational and memory overhead while maintaining strong performance

* The method demonstrates strong results across a wide range of benchmarks, showing its versatility. This includes performance on image classification tasks (such as CIFAR and HAM10000), as well as on audio classification (ESC-50).

### Weaknesses
 * The method is primarily limited to attention-based models, restricting its applicability across model architectures.

* A potential limitation is the method's similarity to existing method BatchEnsembles, as both approaches utilize low-rank adapters to create ensembles. Given this mentioned similarity a question arises: what advantages does the proposed method offer over directly applying BatchEnsembles to attention heads?

* Experiments demonstrates mixed results, making it unclear whether the method consistently outperforms existing approaches. For example, in CIFAR experiments it’s unclear where the significant performance improvement over a single model (without a LoRA adapter) comes from. The calibration performance in terms of ECE may also stem from discrepancies in accuracy. Similarly, ESC-50 experiments show that deep ensembles outperform the proposed method.

* In addition to the previous point, the authors do not compare against other compute-efficient ensembling approaches. In the appendix, they mention that existing methods cannot be applied to Transformer architectures, as these differ significantly from MLP and CNN-based models. However, BatchEnsembles or Masksembles (and not mentioned PackedEnsembles [1]) could be viewed as approaches that apply perturbations to trainable model weights (matrices), therefore the impossibility to apply them to Transformers is unclear.

* An important limitation is the absence of experiments on text data, despite LoRA’s popularity and proven effectiveness within this domain.

### Questions
* How effective is using a mixture-of-experts approach as an “ensemble” for uncertainty evaluation, and how does it compare to this method in terms of efficiency and uncertainty quality?

* Given the method’s focus on attention-based models, how well does it work for MLPs or CNNs?

* What specific advantages does this method offer over applying BatchEnsembles to attention heads?

* The appendix suggests existing efficient ensembling methods don’t apply to Transformers. What specifically prevents methods like BatchEnsembles, Masksembles, or PackedEnsembles from being effective here?

### Soundness
3

### Presentation
3

### Contribution
2
