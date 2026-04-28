# BioNAS: Incorporating Bio-inspired Learning Rules to Neural Architecture Search

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
Bio-inspired neural networks have gained traction due to their adversarial robustness, energy efficiency, and for being biologically plausible. While these bio-inspired networks have shown significant progress, they still fall short in terms of accuracy and are hard to scale to complex tasks. In this paper, we propose to use neural architecture search to further improve state-of-the-art bio-inspired neural networks. We
achieve this thanks to BioNAS, a framework for neural architecture search that explores different bio-inspired neural network architectures and learning rules. The novelty of BioNAS lies in exploring the use of different bio-inspired learning rules for the different layers of the model. The motivation for this choice comes from recent work in the field suggesting that different learning mechanisms might be used in different
regions of the human brain. Using BioNAS, we get state-of-the-art bio-inspired neural network performance achieving an accuracy of 94.86 on CIFAR10, 76.48 on CIFAR-100 and 43.42 on ImageNet16-120, surpassing state-of-the-art bio-inspired neural networks. We show that a part of this improvement comes from the use of different learning rules instead of using a single algorithm for all the layers. We release BioNAS to the community and make the code available via this link (https://anonymous.4open.science/r/LR-NAS-DFE1)

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores a method that combines bio-inspired learning rules with Neural Architecture Search (NAS) to optimize the performance of neural networks. The authors propose BioNAS, a framework capable of automatically searching for the best architecture and learning rules. Through a series of experiments, particularly on the CIFAR-10 and CIFAR-100 datasets, the paper demonstrates the advantages of BioNAS in terms of accuracy and adversarial robustness, comparing it with existing backpropagation training methods.

### Strengths
The integration of bio-inspired learning rules with NAS is a fresh perspective that could significantly contribute to the field of neural network optimization. The paper is well-organized and clearly written, making it accessible for readers with varying levels of expertise in NAS and bio-inspired techniques.

### Weaknesses
Is there an analysis of energy consumption.

### Questions
Whether it is applicable to larger datasets.

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
5

### Summary
This paper proposes a neural architecture search framework, BioNAS, that supports certain types of biologically plausible learning algorithms. The framework is built upon existing NAS framworks DARTS and EG-NAS, and incorporates different feedback alignment techniques from BioTorch. The authors compare the performance of their BioNAS generated networks against some previous works and claim they can get state-of-the-art bio-inspired network performance on several benchmarks.

### Strengths
Adversarial attacks on generated bio-inspired networks are introduced to illustrate the advantage of their framework.

### Weaknesses
Although the direction of this work is interesting, my major concern is that this work appears to be prelimilary, and some of the key conclusions are *overclaimed*.  

Major Weakness
1. The authors claim that their proposed BioNAS is designed for bio-inspired networks, but currently only several variants of FA algorithms are supported, making this work less significant, and their claim should be toned down. Specifically, the framework's reliance on feedback alignment (FA) variants, while a valid starting point, does not fully capture the breadth of bio-inspired learning. The absence of other prominent biologically plausible algorithms, such as Hebbian learning, predictive coding, or target propagation, significantly limits the scope of the framework and its applicability to the broader field of bio-inspired neural networks. The current implementation appears to be more of a specialized NAS for FA-based networks rather than a general BioNAS framework.
2. The proposed BioNAS is implemented by adding operations backended by BioTorch to existing NAS frameworks, which does not show much novelty nor effort. The core contribution seems to be the integration of BioTorch's FA implementations into existing NAS frameworks like DARTS and EG-NAS. This approach lacks significant novelty, as it primarily involves adapting existing code rather than introducing a new architectural or algorithmic concept. The effort appears to be more focused on implementation rather than on fundamental research innovation.
3. The authors claim that they can get state-of-the-art bio-inspired network performance on several benchmarks, but for CIFAR-10 they only compare against two previous Hebbian-based results, and for CIFAR-100 and ImageNet16-120 no previous results of bio-inspired algorithms are shown. The performance claims are not sufficiently supported by comprehensive comparisons. The lack of comparisons against a wider range of bio-inspired algorithms, especially on CIFAR-100 and ImageNet16-120, makes it difficult to assess the true performance of the proposed BioNAS framework. The limited baselines on CIFAR-10 also raise concerns about the robustness of the claims.

### Questions
Questions:
1. How might other forms of bio-inspired learning algorithms (e.g., Hebbian, predictive coding, target propagation) be integrated in the proposed framework?
2. Does the distribution of different learning algorithms in the generated networks show interesting patterns? And if so, what might be the (intuitive) explaination for generating such patterns, what might be the advantages for such patterning, and can such patterns be generalized to different network architectures to produce competitive performance?

### Soundness
1

### Presentation
2

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
This paper presents BioNas, a neural architecture search algorithm tailored for bio-inspired neural networks. BioNas focuses on biologically plausible learning algorithms and simultaneously optimizes both the network architecture and the learning rule. The proposed framework achieves state-of-the-art performance on the CIFAR-10 and CIFAR-100 datasets, demonstrating its effectiveness in enhancing bio-inspired model design.

### Strengths
The authors utilize a more bio-plausible learning rule instead of the commonly used BP algorithm, which is interesting.

The authors provide strong empirical support for their approach by conducting extensive experiments across multiple datasets and varied settings.

### Weaknesses
The motivation of combining FA approaches and NAS is not clear. While the concept of applying different learning rules to train SNNs is intriguing, the combination of NAS and FAs in this context raises questions. NAS traditionally involves exploring a vast space of candidate models to find an optimal architecture with significant computational cost. Its primary aim is to achieve high performance without regard to training efficiency, which contrasts with the efficient and light weight bio-inspired learning rules. The authors do not clearly articulate why a computationally expensive search is necessary when the goal is to leverage the efficiency of bio-inspired learning rules. Furthermore, the paper does not explore the potential trade-offs between the computational cost of NAS and the efficiency gains of the bio-inspired learning rules, which is a critical aspect that needs to be addressed.

The novelty is limited, as the BioNAS framework closely resembles DARTS and EG-NAS. The primary difference introduced here is the addition of various existing learning rules to the search space. However, the paper does not sufficiently demonstrate how this addition leads to fundamentally different architectures or learning dynamics compared to standard NAS with backpropagation. The paper lacks a detailed analysis of the architectural differences discovered by BioNAS and how these differences relate to the chosen learning rules. The authors should provide a more in-depth analysis of the searched architectures and their properties, particularly in relation to the different learning rules used during training.

One important concern is whether the authors have verified if there is a gradient obfuscation issue within their model. The observation that the multi-step PGD attack performs worse than the single-step FGSM attack may indicate potential gradient masking or unsuccessful attacks [1]. This issue can often lead to misleading conclusions about a model’s robustness. The authors should provide a more thorough analysis of the adversarial robustness of their model, including a detailed investigation of potential gradient obfuscation issues and a more comprehensive evaluation using a wider range of attack methods and parameters.

### Questions
One important concern is whether the authors have verified if there is a gradient obfuscation issue within their model. The observation that the multi-step PGD attack performs worse than the single-step FGSM attack may indicate potential gradient masking or unsuccessful attacks [1]. This issue can often lead to misleading conclusions about a model’s robustness.

[1] Athalye, Anish, Nicholas Carlini, and David Wagner. "Obfuscated gradients give a false sense of security: Circumventing defenses to adversarial examples." ICML 2018.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper uses the NAS method to search for suitable edge and learning rules of the network cell, constructing a biologically inspired neural network that achieves the comparable performance of the network trained by end-to-end backpropagation algorithm. Simultaneously, this paper demonstrates that the mixed biologically inspired learning rules can reduce gradient variance and enhance the network’s white-box adversarial robustness.

### Strengths
This paper introduces the different learning rules into the network search method for the first time. Experiment results show that mixed learning rules can effectively improve the performance of the network and its white-box adversarial robustness. I think the integration of NAS with various learning methods represents a promising approach.

### Weaknesses
1. This paper does not detail how to simultaneously search for cell architecture and the learning rules. And the search space is much larger than the original DARTS and EGNAS; the search time will increase about threefold. Therefore, if DARTS and EGNAS adopt the same search time as this paper, will their performance be improved?

2. Different rows (training methods) in Table 2 use different network structures, but they need to use the same network structure for comparison.

3. This paper lacks the theoretical analysis that adopting the mixed learning rule can enhance the white-box adversarial robustness.

### Questions
1. Are the attack image gradients for the white-box attack method calculated by end-to-end backpropagation or the searched learning algorithm?

2. Methods such as FA use a new matrix to replace the weight matrix in the back propagation process, which also needs end-to-end learning. Why are these training methods related to bio-inspired?

3. After the search is completed, does the subnet undergo random weight retraining or inherit the supernet's weight for fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
2
