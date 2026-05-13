# Leveraging free energy in pretraining model selection for improved fine-tuning

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
Recent advances in artificial intelligence have been fueled by the development of foundation models such as BERT, GPT, T5, and Vision Transformers. These models are first pretrained on vast and diverse datasets and then adapted to specific downstream tasks, often with significantly less data. However, the mechanisms behind the success of this ubiquitous pretrain-then-adapt paradigm remain underexplored, particularly the characteristics of pretraining checkpoints that lend themselves to good downstream adaptation. We introduce a Bayesian model selection criterion, called the downstream free energy, which quantifies a checkpoint's adaptability by measuring the concentration of nearby favorable parameters for the downstream task. We demonstrate that this free energy criterion can be effectively implemented without access to the downstream data or prior knowledge of the downstream task. Furthermore, we provide empirical evidence that the free energy criterion reliably correlates with improved fine-tuning performance, offering a principled approach to predicting model adaptability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel free energy strategy for pretraining model selection to improve fine-tuning performance on downstream tasks. The work is grounded in extensive theoretical analysis, progressively examining the relationships between downstream task performance, downstream free energy, and pretraining free energy. It demonstrates that estimated pretraining free energy is a suitable proxy for selecting pretraining checkpoints without accessing downstream task data. Experiments are conducted under both full meta-test fine-tuning and few-shot meta-test fine-tuning settings, showing that strategies resulting in lower pretraining free energy (e.g., larger learning rates, smaller batch sizes, increased momentum) also yield better performance on downstream tasks.

### Strengths
1. The paper introduces a novel proxy, pretraining free energy, to identify the most suitable pretraining checkpoint for downstream tasks. This proxy does not rely on downstream task data, offering broader applicability.
2. The paper provides rigorous theoretical analysis, systematically proving constraints based on hypotheses, from downstream task performance to downstream free energy, and finally to pretraining free energy.
3. Based on the asymptotic pretraining free energy strategy, the paper provides some observations that would be helpful for pretraining.

### Weaknesses
1. The experimental section is overly simplistic, focusing solely on the CIFAR-FS dataset, without addressing cases where the downstream data distribution differs from the pretraining data distribution. Additionally, experiments use only a ResNet-18 model, which is relatively small in scale. Testing the theory on larger models, such as ViTs, would strengthen the study.
2. Previous work has explored pretrained model selection using proxies like neural collapse. The lack of comparison with existing methods weakens the persuasiveness of the results.
3. The paper’s presentation quality needs improvement; for instance, in Section 6, "Full meta-test fine-tuning" and "Few-shot meta-test fine-tuning" should be presented as parallel points. Additionally, consistency in cross-referencing formats and symbol representations is needed.

### Questions
1. The experiment section concludes that strategies such as larger learning rates, smaller batch sizes, and increased momentum yield better downstream transfer performance. However, these findings have already been established in prior work. Does the theory proposed offer additional insights or applications?
2. In L182, the paper assumes that the classification head $v$ of the pretraining task and $u$ of the downstream task share the same dimensionality. How is this assumption specifically applied in the theoretical analysis?
3. Can the proposed method be applied to unsupervised pretraining processes and situations where downstream tasks differ from the pretraining tasks?

### Soundness
3

### Presentation
2

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
The authors propose to look at a free energy criterion to select the best possible pre-trained checkpoint for  later downstream tasks. They show a strong correlation between the proposed metric and the transfer accuracy on a downstream task. An theoretical derivation is made that claims that the pretraining free energy bounds the downstream free energy, which in turn gives a bound for the test error. A taylor expansion similar to the one in Lau et al. is used. Practically the free energy depends on the loss of the downstream dataset and a local learning coefficient, a way of measuring the complexity of a model. In a next step the downstream free energy is related to the pretraining free energy based on the work by Yamazaki et al., so that without access to the downstream data the best checkpoint can be determined for the downstream task.

### Strengths
* The paper aims to study a relevant problem, i.e. understanding when models will perform well on different data. 
* I appreciate the quest for finding a theoretical basis, rather than simply performing millions of experiments to find a relation by accident.
* Overall, the paper is clear and in most parts easy to follow, even though it is mathematically a bit heavy, so that is not an easy task.

### Weaknesses
* I’m not confident that the relation that is given between the downstream energy and the pretraining free energy is very meaningful. It must rely on the similarity of both data distributions, as it is always possible to find a random distribution that has a much higher loss than that of the pretraining (e.g. change the labels). This relation is included in the comparison in proposition 5.3 by the quantity D. This relation is from Yamazaki et al, but importantly, they do not consider entirely different distributions. They look at how the test error is bounded by the training error when train and test distributions are different, but assume that both distributions have the same input domain. Especially when using two datasets that contain different classes, D will practically be infinite since: $r^0(y|x) = \frac{r^0(x, y)}{r^0(x)}$, and when $r^1(x, y) > 0 \implies r^1(x) > 0 \implies r^0(x) = 0$, when $r^0$ and $r^1$ are distributions over different domains. This is practically always true when considering image distributions. E.g. the domain of images of a car is completely different than that of images of a horse, unless they are both in the same image (which is not true for most image classification datasets). This not the case in Yamazaki et al., see for instance their numerical example in section 3.5, which looks at this quantity when $r^0$ and $r^1$ are normal distributions with a slightly different mean and standard deviation. $D$ is no longer used after line 353 because it is a constant, so it shouldn't be optimized. While that is true, constants shouldn't be ignored in the conclusion. E.g. when $f(x) < g(x) + 10e5$, optimizing $g$ instead of $f$ will bound $f$, but $f$ may still be as a large as $10e5$, even when $g(x) = 0$.


* There is no comparison to other measures that promise to do the same things. There are various other techniques in the related work (e.g. Liu et al, Galanti et al., Munn et al.), which should have been used to compare to. Similarly, there is no comparison to any other simple baseline, such as simply using the training loss.


* There are various observations made in Section 5.1 based on the proposed derivation. Although they seem plausible, there is no empirical validation of these observations. It would have been insightful to show examples where these observations are validated. 


* On a high level, this relation says that if the pretraining error is low then the model will transfer better. This may be true when the pretraining dataset is larger and more complex than the downstream task, which other studies have also shown (e.g. [a]). This setting is also the one that is tested in the single experiment that is proposed, where the pretraining task is a larger part of CIFAR100. I do not believe that this relation is meaningful when the relation is reversed, and the pretraining task is significantly easier than the downstream tasks. There is only a single test of the proposed principle, with a single dataset configuration. Given the doubts I have with the theoretical validation (see above), the principle would need a lot more empirical proof to be convincing. 


[a] Kornblith, S., Shlens, J., & Le, Q. V. (2019). Do better imagenet models transfer better?. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 2661-2671).

### Questions
* Do you have an idea what the value of the constant $D$ is in practical scenarios, like the one you tested in Figure 2?
* Did you compare the proposed metric to other quantities the aim to predict how well a model transfers?
* Is there empirical validation of the observations in section 5.1?
* Did you test the proposed relation on more dataset (and combinations thereof) than the one currently in the paper?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the adaptability of pretrained models through the lens of free energy. The authors validate the connection between downstream free energy and adaptability, subsequently proposing the concept of pretraining free energy, which relies solely on pretrained data. The effectiveness of this criterion in controlling downstream free energy is demonstrated, positioning it as a novel measure of downstream adaptability.

### Strengths
1. This paper presents a measure of downstream adaptability that relies solely on pretrained datasets.

2. The motivation of the method is clear and the manuscript is overall good.

### Weaknesses
1. The adaptability of pretrained models is often closely related to downstream tasks/datasets [1]. While this work proposes pretraining free energy as a general selection criterion, it lacks comparative analysis with prior research that typically utilizes a limited number of downstream dataset samples without access to pretrained data [1][2][3]. Such comparisons would strengthen the claims made in this paper.

2. There are concerns regarding the validity of the theoretical assumptions. Assumptions 5.1 and 5.2 do not specify their practical applicability or provide references for similar assumptions.

3. The experimental setup is limited, as validation experiments are conducted exclusively with ResNet-18 on the CIFAR-FS dataset. A broader exploration of various architectures and datasets would provide a more comprehensive evaluation of the proposed method.

[1] Not All Models Are Equal: Predicting Model Transferability in a Self-challenging Fisher Space

[2] Etran: Energy-based transferability estimation

[3] LEAD: Exploring Logit Space Evolution for Model Selection

### Questions
1. Intuitively, downstream adaptability is expected to vary across specific downstream task (e.g., between checkpoints A and B, adaptability may vary across tasks 1 and 2, where A performs better on task 1 and B on task 2, as referenced in past works). However, the proposed pretraining free energy seems to serve as a general  model selection criterion, raising questions about its rationale and necessity, since model selection is often focused on specific downstream tasks.

2. Assumption 5.2 appears overly generalized. It may not hold when two distributions overlap insufficiently or when higher-order statistical moments differ significantly. For example, in a simple case where $r_i(y|x)$ is the same,   $r_0(x)\sim N(0, 0.1), r_1(x)\sim N(0, 1)$, the described ratio diverges as x increases.

3. The distinction between the downstream free energy strategy proposed by the authors (line 245) and existing free energy criteria is unclear. If there is no substantive difference, Section 4.1 may be better suited as theoretical background rather than constituting a novel contribution of this paper.

4. The experimental results presented are insufficient. They rely on a single dataset and model architecture without exploring other transfer learning scenarios, such as cross-domain transfer learning, which would provide a more robust validation of the observation and proposed method.

### Soundness
3

### Presentation
3

### Contribution
2
