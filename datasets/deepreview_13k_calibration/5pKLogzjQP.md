# Purify Perturbative Availability Poisons via Rate-Constrained Variational Autoencoders

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Perturbative availability poisoning attacks seek to maximize testing error by making subtle modifications to training examples that are correctly labeled.
Defensive strategies against these attacks can be categorized based on whether specific interventions are adopted during the training phase.
The first approach is training-time defense, such as adversarial training, which can effectively mitigate poisoning effects but is computationally intensive.
The other approach is pre-training purification, *e.g.,* image short squeezing, which consists of several simple compressions but often encounters challenges in dealing with various poison types.
Our work provides a novel disentanglement mechanism to build an efficient pre-training purification method that achieves superior performance to all existing defenses.
Firstly, we uncover rate-constrained variational autoencoders (VAEs), demonstrating a clear tendency to suppress poison patterns by minimizing mutual information in the latent space. We subsequently conduct a theoretical analysis to offer an explanation for this phenomenon.
Building upon these insights, we introduce a disentangle variational autoencoder (D-VAE), capable of disentangling the added perturbations with learnable class-wise embeddings.
Based on this network, a two-stage purification approach is naturally developed. The first stage focuses on roughly suppressing poison patterns, while the second stage produces refined, poison-free results, ensuring the effectiveness and robustness across various scenarios and datasets.
Extensive experiments demonstrate the remarkable performance of our method across CIFAR-10, CIFAR-100, and a 100-class ImageNet-subset with multiple poison types and different perturbation levels.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to build a purification framework to defend against data poisoning attacks, by using the proposed disentangle variational autoencoder (D-VAE). The experiments show that it achieves remarkable performance on CIFAR-10/100 and ImageNet-subset.

### Strengths
- The experiments show that the proposed D-VAE outperforms other state-of-the-arts.

### Weaknesses
My concerns are as follows.
- The math symbols should be unified. In Section 3.1, $\mathbf{x}$ represents the clean data, while in the rest of the paper, it represents the poisoned data.
- I'm really confused about the proposed method. It would be helpful if the authors could provide more information in Section 3.2. Specifically, please give a detailed description and analysis of Figure 2. The current version is hard to understand, to me.
- I'm confused about the poison recovering part in Eq. 14 and Figure 1. It seems the first two items in Eq.14 are contradictory. Are you aiming to decrease the L2 error between the reconstruction error and a tensor output by the network? I cannot understand the meaning of this term, to me.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper deals with availability poisoning attacks: adversarially modified data is laid as a trap; when ingested into a training pipeline, they negatively impact the model’s performance. The authors propose D-VAE, a variational autoencoder method that disentangles the adversarial perturbation from the underlying original data with a one encoder, two decoder architecture; once disentangled, a model can be trained normally on the reconstructed base image. Experiments are conducted on CIFAR-10, CIFAR-100, and a subset of ImageNet, and compare against training-time defenses and pre-training techniques, against a number of poisoning attacks. Results show that the disentangled perturbations are indeed poison patterns, and that training on the reconstructed base images is less degraded than the baselines.

### Strengths
## S1. Disentangled Poison Patterns
One thing I was curious about was how faithfully the disentangled poison pattern is decomposed from the input. From Figure 1, it looked like it was vaguely doing the right thing, but was better for some (OPS, LSP) than others (NTGA). As such, Section 4.2 was helping in showing that the disentangled poison patterns are in fact quite effective. However, I still think it’d be interesting to quantify how far off the disentangled perturbations are from what the actual poison pattern is (or at least visualize the residuals); this would help answer whether the model is actually doing disentanglement, or itself somehow learning to produce orthogonal poison patterns.

## S2. Main results: Clean Test Accuracy
The paper includes experiments on CIFAR-10, CIFAR-100, and ImageNet, comparing the proposed D-VAE approach with a number baselines, defending against a variety of attack types. There also additional results on other model architectures and with larger bounds. These results are pretty thorough, and the proposed approach consistently outperforms the baselines, sometimes by fairly large margins.

## S3. Ablation Study
The ablation study on the two-stage procedure for this method is good for illustrating that both stages are important for purification.

### Weaknesses
# W1. Motivation, necessity
a) Viability: The paper does not adequately address the practical likelihood of an attacker successfully injecting a sufficient quantity of poisoned samples into a training dataset. The assumption that *all* training data is poisoned, as implied in Section 5.1, is highly unrealistic. Even poisoning one-fifth of the data, the lower limit explored in Tables 7 and 8, is improbable in most real-world scenarios. A more thorough discussion of realistic threat models is needed, including quantitative analysis of the percentage of data that must be poisoned to achieve a successful attack under various conditions.
b) If the availability poisoning attack is successful, it will result in a noticeably degraded model performance, which should alert the model trainer. This would likely prompt an investigation into the training data, potentially revealing the attack.
c) The paper does not explore simpler methods for detecting poisoned data. For instance, monitoring loss spikes during training and discarding samples associated with unusually high loss could be a more efficient defense mechanism. This is particularly relevant for large foundation models, where recent trends emphasize high-quality data and checkpoint restarts upon loss spikes, which might already mitigate this type of attack without requiring complex reconstruction methods like the one proposed.

# W2. Computation requirements
This method necessitates running D-VAE on every sample, as it's impossible to know beforehand which samples are poisoned. This introduces a substantial computational overhead, particularly in large model settings where ingesting vast amounts of online data is common. The proposal in Section 3.5 to run D-VAE twice further exacerbates this issue, making the method even more computationally expensive. Additionally, the need to tune both KLD limits, which appear to vary between datasets as indicated in the "Model Training" paragraph, adds another layer of complexity and hyperparameter tuning. In contrast, JPEG compression offers a simpler and computationally cheaper alternative, as images are often stored in compressed formats.

# W3. Technical notation
The technical notation throughout the paper lacks the rigor expected of an academic publication. Numerous terms are introduced without proper definitions, descriptions are often confusing, and there are instances of naming collisions and entities with multiple variables defined:
- Eq 3: ${kld}_{limit}$ is not defined.
- Eq 3: $z$ is not defined in the text.
- Eq 4: x_c was previously used to denote clean data, but here it is described as a predictive feature. Also, the subscript on x was previously used to denote the sample index i.
- Eq 4: $x = (x_c , x^t_s)$ <= The right side is later described as being predictive and non-predictive features, but $x$ is the input in the image space. Why are they being introduced as a paired element? Also, what is $t$?
- $D$ overloaded: In Figure 1 and Algorithm, $D$ denotes the decoder. In Proposition 2, D is the dimension of the Gaussian. In Equation, we have $D_{KL}$ for KL-Divergence (in contrast to KLD in Eq 3+14). In Section 3.5, D is used to refer to a poisoned dataset, as well as individual images that the input is subtracted from.
- What is the notation for the clean and poisoned dataset? In Equation 1, it appears to be $\mathcal D$ and $\mathcal T$, but in Section 4.2 it’s $C$ and $D_p$. Algorithm 1 also uses its own notation.

# W4. Writing
I encourage the authors to thoroughly revise the writing. Many sections are difficult to read smoothly, and I frequently had to re-read paragraphs multiple times to understand the intended meaning. While some of this is due to minor grammatical or idiomatic errors, or typos (see Miscellaneous for a few non-exhaustive examples), the primary issue is the way concepts are introduced. For example, the paper's specific focus within the broader field of adversarial examples is not clear until well into the Introduction, and my understanding of whether the paper was discussing a malicious method fluctuated several times.

### Questions
Q1. Instead of a VAE, how well does a non-variational auto-encoder work? Such models still have an information bottleneck, and are also trained with reconstruction loss.\
Q2. Why separately decode the perturbation and the reconstructed image? If the input $x$ is $x_c + p$, then knowing either $x_c$ or $p$ should yield the other, since $x$ is given.\
Q3. What percent of the data is poisoned in the main experiments in Tables 2-5?\
Q4. For the Gray and JPEG baselines, are similar transformations applied to the test images during evaluation? Otherwise, these approaches are likely at a disadvantage due to a domain gap.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a defense mechanism against unlearnable examples, a type of attack that aims to decrease the overall utility of a dataset by performing perturbation on the entire dataset. The authors discover that VAEs are capable of removing the perturbations and provide theoretical analysis for justification. The experimental results show SOTA results compared with other baseline defenses against several unlearnable example methods.

### Strengths
Defense against unlearnable examples is a difficult problem, e.g., existing data sanitization techniques cannot be applied as the entire dataset is perturbed. This paper proposes a novel solution for data purification by using generative models (in particular, VAE) to disentangle the perturbation and clean data. The approach seems promising both theoretically and empirically.

### Weaknesses
When studying unlearnable examples, it seems that nowadays people are using three terms: "unlearnable examples", "availability attacks" and "indiscriminate attacks" interchangeably. I am not totally against it, but I think the authors need to be extra careful when specifying the threat model they are considering. 

To illustrate more, availability attack is a generally broader definition. For example, in Biggio et al., 2012 and the following works, availability attacks refer to data poisoning attacks that aim to decrease the model performance overall. Specifically, an attacker usually injects poisoned points into the clean training set to achieve such a goal. Later, Huang et al., 2021 propose another type of availability attack that perturbs the entire training set, which is a data protection technique, also known as unlearnable examples. Obviously, these two types of attacks are very different in terms of the attack budget and attack purpose. I guess "perturbation availability poison" (in the title) seems to be a good definition, but I suggest the authors use a similar explicit definition throughout the paper.

In summary, I encourage the authors to revisit the literature on availability attacks, explicitly identify the threat model they are considering, and specify it in Section 2 while respectively discussing other works (e.g., other data poisoning attacks: targeted attacks, backdoor attacks, and especially indiscriminate attacks). Specifically, sentences like the following one need to be rewritten to reflect the true progress of this field:
> In the realm of DNNs, the majority of existing research
has primarily concentrated on backdoor attacks. However, there has been a growing interest in
availability attacks, also named unlearnable examples, prompting the exploration to prevent unauthorized model training. 

Here, the claim is not supported by any reference and is simply not true: there are numerous other poisoning attacks considering DNNs. Also, the second sentence is not accurate, see my arguments above.

(1) The authors mention that:
> Typically, poisoned samples are notably modified or replaced with newly
generated samples, and take only a fraction of the entire dataset.

This statement is not accurate namely that for such attacks, the attacker cannot "modify" or "replace" any clean training data as the assumption would be too strong (of course, there exists replacing attacks in the literature, but is not considered here). The author should be aware that this specific threat model only considers **adding** poisoned data on top of clean data.

(2) Next the authors write:
> However, these methods often fail to sufficiently degrade model performance
(e.g., only a 16% drop on CIFAR-10), and the poisoned samples are easily distinguishable.

These statements are not entirely wrong but I don't think they are good motivations to study unlearnable examples as the attack budgets are very different. To illustrate more, e.g., Koh & Liang consider adding only 3% of poisoned data while UE considers modifying 100% of the clean set. Thus considering the much lower poisoning fraction, a 16% accuracy drop is probably not tiny.

As a result, as it is not a fair comparison, I would suggest the authors introduce these two methods in parallel as separate categories, one as an attack method, and one as a protection technique.

### Questions
(1) The auxiliary decoder is not very clear to me, and I expect the authors to illustrate more regarding the following aspects:
- What is $u_c$? The authors mention that this is a trainable class-wise embedding, but it is not clear how it is initialized, how it is trained, and why it helps the decoder $D_{\theta_p}$ to generate the disentangled perturbation.
- How do you optimize $\theta_p$? Normally, to train a VAE model, one aims to reconstruct images, in this case, the perturbation $p$. However, to my understanding, a defender should not have access to the perturbations, then how do you construct the loss for $\theta_p$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors uncover and theoretically explain that D-VAE can effectively purify poison patterns. Based on this insight, the authors propose a two-stage purification approach with learnable class-wise embeddings.

### Strengths
The authors show that perturbations tend to have a larger inter-class distance and a smaller intra-class variance.

The pre-training processing shows the potential for effective and efficient defence against poison perturbations.

### Weaknesses
Concern regarding pseudo-robustness. If we design an adaptive poison pattern, that uses a white-box attack (e.g. PGD) to end-to-end (treat VAE and classifier as a whole) generate perturbations, can this method also be used for effective purification?

Concern regarding generalization capacity. If we use a new type of poisoning attack that has not been seen in class-wise embedding (out of the training poisoning attacks), can this method still effectively purify it?

Concern regarding training and inference costs. Does the training set of this method include all poisoning attacks? What is the cost of training? Three additional forward propagations are required in the algorithm, what is the inference time?

### Questions
Please refer to the questions in the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
