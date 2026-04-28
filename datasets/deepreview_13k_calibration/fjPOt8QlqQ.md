# Exploring The Forgetting in Adversarial Training: A Novel Method for Enhancing Robustness

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
In recent years, there has been an explosion of research into developing robust deep neural networks against adversarial examples. As one of the most successful methods, Adversarial Training (AT)  has been widely studied before, but there is still a gap to achieve promising
clean and robust accuracy for many practical tasks. In this paper, we consider the AT problem from a new perspective which connects it to catastrophic forgetting in continual learning (CL). Catastrophic forgetting is a phenomenon in which neural networks forget old knowledge upon learning a new task. Although AT and CL are two different problems, we show that they actually share several  key properties in their training processes. Specifically, we conduct an empirical study and find that this forgetting phenomenon indeed occurs in adversarial robust training across multiple datasets (SVHN, CIFAR-10, CIFAR-100, and TinyImageNet) and perturbation models ($\ell_{\infty}$ and $\ell_{2}$). Based on this observation, we propose a novel method called Adaptive Multi-teachers Self-distillation (AMS), which leverages a carefully designed adaptive regularizer to mitigate the forgetting by aligning model outputs between new and old ``stages''. Moreover, our approach can be used  as a unified method to enhance multiple different AT algorithms. Our experiments demonstrate that our method can significantly enhance robust accuracy and meanwhile preserve high clean accuracy, under several popular adversarial attacks (e.g., PGD, CW, and Auto Attacks). As another benefit of our method, we discover that it can largely alleviate the robust overfitting issue of AT in our experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studied the connection between forgetting (studied in the continual learning domain) and lack of adversarial robustness. The idea is that generated adversarial examples at every epoch has its own distribution (akin to tasks in continual learning literature), and learning on the new distribution (task) in the next epoch causes forgetting. The paper has demonstrated the forgetting phenomenon in adversarial training through experiments, and based on these observations, proposed a method called Adaptive Multi-teacher Self-distillation (AMS), which utilizes self-knowledge distillation from multiple checkpoints of the model throughout training to overcome forgetting.

### Strengths
1. The idea of studying forgetting in adversarial training is interesting and might be of interest to researchers in the field.  
2. The paper is well-written, and it is easy to follow the text along with the experimental results.  
3. Experimental results cover standard benchmarks in the field.  
4. It is indeed interesting that the proposed method has been shown to be effective in mitigating robustness overfitting, and studying this direction could deepen researchers' understanding in the field.

### Weaknesses
1. The proposed loss function has multiple components, and each of them needs to be justified with ablation studies. In Section 4, where the loss function and algorithms are discussed, it is argued that "Reweighting-based Loss Correction" is needed; however, this is not demonstrated in the paper with experimental results. Specifically, the paper lacks a component-wise analysis of the loss function, making it difficult to assess the individual contribution of the reweighting term. Without this, it's unclear if the reweighting is truly necessary or if the performance gains are attributable to other parts of the loss.

2. From a memory perspective, multiple checkpoints of the model need to be stored and used for knowledge distillation, which is costly. This could be acceptable if the performance gain is notable; however, previous studies have shown higher performance gains by using only extra synthetic data (see point 5). The paper does not sufficiently address the trade-off between the memory overhead of storing multiple checkpoints and the performance gains achieved, especially when compared to methods that utilize synthetic data, which often require less memory.

3. In the "Experimental Setting," it is stated that accuracy is reported for the best checkpoint of the model with the highest "test" accuracy, which is quite problematic. This introduces a potential bias in the evaluation, as the test set should only be used for final evaluation and not for checkpoint selection. Selecting the best checkpoint based on test set performance can lead to overfitting to the test set, thus inflating the reported results.

4. The accuracy of the proposed method in Table 2 has been bolded, but for CIFAR-10, three of the baselines have higher accuracy than the proposed method; similarly for CIFAR-100. The bolding of the proposed method's results is misleading, as it suggests superior performance when, in fact, several baselines achieve higher robust accuracy on both CIFAR-10 and CIFAR-100 datasets. This misrepresentation undermines the credibility of the experimental results.

5. Related to the previous point, other recent benchmarks, such as "Better Diffusion Models Further Improve Adversarial Training" (https://arxiv.org/abs/2302.04638), are missing in the table. For example, with 1M extra adversarial examples, this baseline achieves much higher robust accuracy than the proposed method with the same number of extra examples. The absence of a comparison with this recent state-of-the-art method, which uses a similar amount of extra data, makes it difficult to assess the true performance of the proposed method relative to the current state of the field.

6. The study misses a comparable forgetting analysis in natural training. Although experiments have shown that forgetting occurs in adversarial training, it may not be specific to AT, and performing knowledge distillation only for the clean loss in TRADES might be sufficient. An experimental analysis to distinguish this could provide further insights. The paper does not explore whether the observed forgetting is specific to adversarial training or if it is a more general phenomenon that also occurs in standard training. This limits the understanding of the proposed method's contribution.

### Questions
1. The main question is, if forgetting is the problem in adversarial training (AT), why does having more data (such as synthetic data) boost robust accuracy? If the number of samples increases, there are greater differences in the distributions of samples (tasks) from one epoch to another, which should potentially increase forgetting. However, in reality, robust accuracy improves. The explanation for this phenomenon appears to be missing from the paper, especially given that almost all recent SOTA methods utilize generated data, and even in the experimental section of this paper, a version with 1M extra generated samples is employed.

2. Regarding the lack of ablation study on the loss formulation, the hyperparameter sensitivity experiments indicate that the size of the interval parameter "m" has minimal effect on robustness performance, especially with larger values. If distribution shifts from one epoch to another cause forgetting, we would expect a decline in performance with larger values of "m," as less forgetting would be recovered; however, this trend does not appear in Figure 4. Why is this the case?


I have listed my concerns and questions in the weaknesses and questions sections and would appreciate it if the authors could provide precise justifications for them. However, in its current format, I am leaning toward rejection.

### Soundness
3

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
4

### Summary
The authors approach AT from a continual learning perspective, treating adversarial samples generated with different parameters during training as tasks with distinct distributions, as models undergoing AT tend to forget adversarial examples learned in earlier stages, similar to the forgetting phenomenon in continual learning. This work introduces an Adaptive Multi-teacher Self-distillation method, which mitigates forgetting by aligning model outputs across training stages. Experiments on multiple datasets and under various adversarial attacks demonstrate that AMS enhances both clean and robust accuracy, while also alleviating robust overfitting.

### Strengths
1.	The approach of viewing AT as a continual learning problem is innovative, offering a new perspective on enhancing model robustness within AT.
2.	The paper is well-structured and clearly presents the progression from problem formulation to solution, supported by extensive experiments on diverse datasets that validate the proposed method’s robustness.

### Weaknesses
1.	The authors approach AT through the lens of continual learning but do not sufficiently establish the connection between the two, either experimentally or theoretically. For example, demonstrating how adversarial samples generated with different parameters follow distinct data distributions could strengthen the argument. Some statements appear subjective, despite the proposed method's effectiveness. Specifically, the paper lacks a rigorous analysis demonstrating that the adversarial examples generated at different training stages actually constitute distinct distributions, a crucial aspect for framing the problem as a continual learning scenario. Without such evidence, the analogy to continual learning remains weak. Furthermore, the claim that models 'forget' adversarial examples from earlier stages needs more concrete justification, such as a quantitative measure of performance degradation on older adversarial examples as training progresses.
2.	The AMS method requires tracking knowledge across multiple stages, which increases memory and computational costs, particularly with large datasets and models. The method's reliance on maintaining multiple teacher models introduces a significant overhead in terms of both memory and computation. This could be a limiting factor for practical applications, especially when dealing with large-scale datasets or complex models. The paper should include a more detailed analysis of the computational complexity and memory footprint of the proposed method, comparing it to standard adversarial training techniques.

### Questions
1.	Is the classification result shown in Figure 1 based on the training set? If so, this result may not fully illustrate the catastrophic forgetting problem; it may only indicate that newly generated samples were successfully attacked, especially given that an untargeted attack was used. If the result is on the test set, it would more convincingly suggest similarity to catastrophic forgetting in continual learning.
2.	Catastrophic overfitting[1] is a common issue in fast adversarial training, with many works focusing on its mitigation[2][3]. Have you explored whether the proposed method could address catastrophic overfitting as well, given its similarity to catastrophic forgetting in continual learning?
3.	Did the author consider dividing the epochs into stages unevenly, with each stage containing a different number of training epochs?
4.	While the method is efficient for certain datasets, it remains computationally demanding for larger datasets like the full ImageNet. Do the authors have plans to further reduce computational requirements in future work?

[1]. Wong E. et.al “Fast is better than free: Revisiting adversarial training” ICLR, 2020  
[2]. Zhang Y. et.al “Revisiting and advancing fast adversarial training through the lens of bi-level optimization” PMLR, 2022  
[3]. Wang Z. et.al “Preventing Catastrophic Overfitting in Fast Adversarial Training: A Bi-level Optimization Perspective” ECCV, 2024

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel perspective on mitigating catastrophic forgetting during adversarial training. The paper proposes Adaptive Multi-teachers Self-distillation that uses an adaptive regularizer to align the knowledge differences across stages. The evaluation is performed on multiple target models under various gradient-based attacks.

### Strengths
1. The paper is well-written with a clear storyline and a sound motivation.
2. The proposed method is reasonable and fair.
3. The experiments on three attacks are comprehensive.

### Weaknesses
1. The proposed framework shallowly touches on the training efficiency of adversarial training. It is appreciated that authors mention effective variants of adversarial training that have high training efficiency (e.g., Free-AT [1], YOPO [2]). Yet the paper's algorithm design does not fully address how such efficiency techniques are involved in the framework. Also, Line 6 of Algorithm 1 adds an initial random perturbation to the source image, which is similar to [3]. Authors are expected to elaborate on the design choice of the $0.001$ strength used in this line.

2. The scope of target models is limited. The paper only evaluates CNN-based architectures (e.g., ResNet variants), while more modern vision models based on Vision Transformers are not sufficiently evaluated. It will help to validate the framework if experiments on ViT also support the existing findings.

### Questions
Please address my concerns stated in the weakness section. Note that, although there are concerns raised, I believe none of them is severely affecting the validity of the paper. Hence I rate the initial version of the submission as a borderline accept. My final rating would be conditioned on the soundness of the authors' responses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies the adversarial learning problem from a continual learning perspective. In particular, the authors found a novel connection between catastrophic forgetting; a well-studied problem in continual learning, and adversarial training (where the model at later stages forgets the learnt adversaries from earlier stages). Based on this connection, the authors propose a novel method that distills the knowledge from multiple teachers during adversarial training. Each teacher is a previously saved checkpoint obtained through the adversarial training. Through extensive experiments on different datasets and threat models, the proposed orthogonal method shows consistent performance improvement.

### Strengths
This paper has the following strengths:

1- The connection between adversarial training and continual learning is the part that I like the most in this paper. This should open the door for further research on the intersection between these two fields.

2- The method proposed in this paper is intuitive, and more importantly is orthogonal. That is, if a stronger training algorithm is developed in the future, one would expect that this algorithm + AMS would perform better.

3- The experiments are comprehensive spanning multiple datasets, adversarial training schemes, and threat models.

### Weaknesses
Despite the strengths in this paper, there are still remaining concerns that need to be resolved.

1- Concern regarding experiments: In Table 2, it seems that S$^2$O performs better than TRADES+AMS in every aspect on CIFAR-10 (both clean accuracy and robust accuracy under all considered attacks). This then begs for the following two experiments:

1a. Can yo provide the performance of S$^2$O on the other considered datasets (e.g. CIFAR100, SVHN, TinyImageNet)?

1b. Can you provide the results of S$^2$O + AMS? Generally, how is the performance of other robust training methods when combined with AMS?

There are also a couple of other experiments missing in this paper; namely:

1c. Experiments on CIFAR10 using the 1M generated images (with and without AMS).

1.d Comparison agains AWP [A] seems to be missing in this paper.

2- Concern regarding presenting results in table: I think it is quite confusing to not make the best results in bold rather than making the proposed method's results in bold. I think an easier way to trace the results is to distinguish the best results and the runner up. Alternatively, you could present each method as (Method in one row, Method + AMS in another row highlighting the performance gain under AMS).

3- Concern about the proposed method: The results in the appendix (Table 5) show that AMS can suffer from significant performance drop under different choices of hyper parameters (namely $\lambda$). Is the choice of hyper parameters at least generalizable under different robust training methods? A simple experiment to address this concern is to fix the hyper parameters for the suggested experiment in 1.b to be $m=20, \lambda=0.5$.

Minor comments:

4- Performance gain under AMS is marginal (often ~1%).

5- How is the performance of AMS in the continual learning setting? I am curios to see if it actually outperforms the CL methods such as LwF and ER.

6- Missing reference: I find the motivational experiments of this paper (experiments on adversarial examples from previous checkpoints) are quite similar to the work of Gupta et.al [B]. I believe that the related work in this paper will benefit from a discussion on the relation between the results in Figure 1 in this work and the results in Figure 1 in [B].

### Questions
Please refer to the weaknesses section. I am happy to raise my score if my questions and concerns are resolved.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes an enhanced adversarial training algorithm that tackles this problem from the perspective of continual learning and catastrophic forgetting. It first demonstrates a forgetting phenomenon with an experiment. Then, a methodology named AMS that distills from weighted teachers (checkpoints from earlier training epochs) is proposed. Empirical experiments on SVHN, CIFAR-10/100, and Tiny ImageNet show improved robustness when adding AMS upon e.g. Madry's adversarial training and TRADES. Robust overfitting can also be mitigated with the help of AMS.

### Strengths
The work is presented in a clear and smooth way. Viewing adversarial training from a continual learning and forgetting perspective is interesting and could be of significance if it's novel (which I'm not entirely sure since I'm away from adversarial training literature for a while). It starts by exposing the forgetting problem with a concrete experiment, which justifies the validity of employing the forgetting view to some extent. The method is also presented well, with Figure 2 being quite informative. Experiments seem quite extensive.

### Weaknesses
1. AMS will inevitably incur larger time and space cost. Beyond increasing $m$, is there any other more intelligent method that can help reduce the number of teachers? For example, could there be a metric that helps identify the most informative teachers, so that throughout the training one can only keep say the most valuable $k$ teachers?

2. One straightforward approach for aggregating or maintaining learned information from previous models is Exponential Moving Average (EMA), which has been shown to help with adversarial training [1]. EMA should be considered as a baseline in my opinion.

3. An ablation study should be presented to validate the proposed reweighting-based loss correction.

4. In Table 6, it seems that distilling from more teachers (having smaller $m$) hurts clean accuracy but not robustness. Any idea why?

### Questions
Please see the questions in weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
