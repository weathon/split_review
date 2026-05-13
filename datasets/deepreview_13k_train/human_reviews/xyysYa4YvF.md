# Interpretable Boundary-based Watermark Up to the condition of Lov\'asz Local Lemma

- Decision: Reject
- Scores: 5, 6, 1

## Abstract
Watermarking techniques have emerged as pivotal safeguards to defend the intellectual property of deep neural networks against model extraction attacks. Most existing watermarking methods rely on the identification of samples within randomly selected trigger sets. However, this paradigm is inevitably disrupted by the ambiguous points that exhibit poor discriminability, thus leading to the misidentification between benign and stolen models. To tackle this issue, in this paper, we propose a boundary-based watermarking method that enhances the discernibility of trigger set, further improving the ability in distinguish benign and stolen models. Specifically, we select trigger samples on the decision boundary of base model and assigned them labels with the least probabilities, while providing a tight bound based on the Lov\'asz Local Lemma. This approach ensures the watermark's reliability in identifying stolen models by improving discriminability of trigger samples. Meanwhile, we provide theoretical proof to demonstrate that the watermark can be effectively guaranteed under the constraints guided by the Lov\'asz Local Lemma. Experimental results demonstrate that our method outperforms the state-of-the-art watermarking methods on CIFAR-10, CIFAR-100 and ImageNet datasets. Code and data will be released publicly upon the paper acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel boundary-based watermarking method to protect deep neural networks against model extraction attacks. The authors decompose the probability of successfully identifying a stolen model into the trigger set accuracy and probability that each trigger can differentiate models. Their method optimizes both components.

### Strengths
- Novel boundary-based trigger selection strategy that optimizes distinguishability between benign/stolen models
- Theoretical analysis proving guarantees under Lovász Local Lemma constraints on watermark-related parameters
- Strong empirical results on CIFAR-10/100 and ImageNet demonstrating state-of-the-art trigger accuracy and p-values
- Ablations showing the effectiveness of the proposed trigger selection and labeling approach
- Well-written and clearly presented, with good coverage of related work

### Weaknesses
 - Theoretical guarantees rely on achieving the Lovász Local Lemma parameter constraints, but it's unclear how difficult this is in practice or how to set the α values. Also, other hyperparameter sensitivities and computational costs are not deeply explored, and more ablation studies are needed to prove this idea. Specifically, the paper lacks a clear methodology for determining the critical α value, and how this value changes with different model architectures and datasets. The paper also needs to explore the sensitivity of the method to the number of perturbed models (s), the perturbation range (δ), and the boundary thresholds (a and b). The computational cost of generating perturbed models and selecting boundary samples is also not thoroughly analyzed.
- Limited evaluation of large-scale datasets and widely-used production models. The paper's experiments focus primarily on CIFAR-10, CIFAR-100, and ImageNet datasets with ResNet34 and VGG11 classifier architectures. However, it lacks evaluation on much larger scale datasets such as LAION or ImageNet-21K, which would further demonstrate the method's scalability and robustness, and also closer to real-world scenarios. Additionally, the paper does not test the proposed watermarking method on widely used production models like CLIP or SAM (Segment Anything Model).
- Some low-level methodological details are lacking, e.g. how exactly are boundary samples selected, how are labels assigned when multiple have the same low probability. The paper does not provide a clear algorithm for boundary sample selection, particularly when multiple samples fall within the defined thresholds. It is also unclear how the method handles cases where multiple samples have the same, or very similar, low probabilities, and how labels are assigned in such situations. This lack of clarity makes it difficult to reproduce the results and understand the practical implementation of the method.

### Questions
- How sensitive is the method to the various hyperparameters, e.g. number of perturbed models s, perturbation range δ, boundary thresholds a and b? Guidelines for setting them would help practitioners.
- The theoretical guarantees require satisfying the Lovász Local Lemma constraints on watermark-related parameters. How difficult is this to achieve in larger scale model like VIT-high or SigCLIP? Are there techniques to guide the optimization of the α values?
- The results focus on CIFAR and ImageNet with a ResNet architecture. How well does the method generalize to other datasets and tasks? Additional results there would strengthen the work.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel boundary-based watermarking technique for protecting neural networks from model extraction attacks. Previous watermarking approaches rely on randomly selected trigger sets, which may fail to differentiate between benign and stolen models due to ambiguous trigger points. This method instead selects boundary samples as triggers, assigns them rare labels, and applies the Lovász Local Lemma to achieve a theoretically tight bound that guarantees watermark efficacy. Experimental results on CIFAR-10, CIFAR-100, and ImageNet datasets show that this approach outperforms state-of-the-art techniques in both trigger set accuracy and p-value tests, enhancing its ability to identify stolen models.

### Strengths
- The paper is well-written, well-organized, and easy to follow, which makes the contributions and results accessible to readers.

- Model extraction is a relevant issue for DNNs in production, making this approach practical and valuable.

- The paper introduces a boundary-focused approach that addresses limitations in previous watermarking methods, providing a robust solution against model extraction attacks.

- The use of the Lovász Local Lemma gives theoretical backing, strengthening the reliability of the watermark and adding rigor to the approach.

- The method is tested on CIFAR-10, CIFAR-100, and ImageNet, demonstrating its generalizability and effectiveness across multiple datasets and outperforming existing techniques.

### Weaknesses
 - The process involves multiple perturbations, decision boundary identification, and label selection, which may introduce computational overhead or complexity in real-world deployments.

- While the method is robust for certain types of attacks, the paper does not fully address how it might respond to adaptive adversaries who could circumvent boundary-based triggers.

- The paper doesn’t explore how well this method would work with very large models or different architectures, which could affect its scalability.

- The method may need a lot of computational resources, which could make it difficult to deploy in practical settings.

### Questions
- How would this method hold up against attackers who try to avoid boundary-based watermarks specifically?

- How does the computational cost of this method compare to other watermarking techniques?

- How realistic is it to use this approach in real-world applications where resources might be limited?

- Did the authors try their method with larger networks and other architectures, such as ResNet-101, ResNet-152, DenseNet, ConvNeXt, MobileNetV2, and VGG?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper presents a watermarking approach to defend the intellectual property of deep neural networks against model extraction attacks. The method relies on two-step procedure – generation and certification of trigger sets. The method is compared to several baselines; the efficiency of the method is illustrated against distillation-based model extraction attacks.

### Strengths
The paper is accurately written and provide some experimental results on model fingerprinting task. The method proposed relies on the construction of perturbed models to generate and certify the trigger set, that is known to be effective.

### Weaknesses
1) The idea to use perturbed models for trigger set generation and certification is not new, what notably limits the novelty of the paper.

2) The author listed several other watermarking approaches but did not choose them for comparison (for example, see Mikhail Pautov, et. al, Probabilistically robust watermarking of neural networks, IJCAI-2024).

2) The method leads to notable degradation of the performance of the fingerprinted model even on simple datasets (CIFAR10/100), making the feasibility of the approach questionable.

3) The method is tested only against distillation-based attacks; only the models of the same architecture are considered to be included in perturbed set; overall, it leaves doubts about the efficiency against other extraction attacks.

4) Crucially, the paper provides no study / results about the false positive detection of benign models. If a non-fingerprinted model is often detected as fingerprinted, it indicates inappropriate choice of the trigger set.

5) No code is provided.

The paper has high degree of similarity with the previously published work, and has no comparison with it. I doubt that the paper brings enough novelty: the idea is known, the experimental results are notably below the sota ones.

### Questions
1) Why did the author choose not to compare their results with the already published work? A brief comparison shows that the method proposed in the paper yields worse both trigger set and benign accuracy. 
2) Does method work in case of other model extractions attacks?
3) What is known about the FPR of the method? How can one guarantee that the method does not detect fingerprinted model as the non-fingerprinted one?

### Soundness
2

### Presentation
2

### Contribution
1
