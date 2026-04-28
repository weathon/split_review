# Improving Generalization and Robustness in SNNs Through Signed Rate Encoding and Sparse Encoding Attacks

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
Rate-encoded spiking neural networks (SNNs) are known to offer superior adversarial robustness compared to direct-encoded SNNs but have relatively poor generalization on clean input. While the latter offers good generalization on clean input it suffers poor adversarial robustness under standard training. A key reason for this behaviour is the input noise introduced by the rate encoding, which encodes a pixel intensity with $T$ independent Bernoulli samples. To improve the generalization of rate-encoded SNNs, we propose the *signed rate encoding* (sRATE) that allows mean centering of the input and helps reduce the randomness introduced by the encoding, resulting in improved clean accuracy. In contrast to rate encoding where input restricted to $[0,1]^d$ is encoded in $\\{0,1\\}^{d\times T}$, the signed rate encoding allows input in $[-1,1]^d$ to be encoded with spikes in $\\{-1,0,1\\}^{d\times T}$, where positive (negative) inputs are encoded with positive (negative) spikes. We further construct efficient *Sparse Encoding Attack* (SEA) on standard and signed rate encoded input, which performs $l_0$-norm restricted adversarial attack in the discrete encoding space. We prove the theoretical optimality of the attack under the first-order approximation of the loss and compare it empirically with the existing attacks on the input space. Adversarial training performed with SEA, under signed rate encoding, offers superior adversarial robustness to the existing attacks and itself. Experiments conducted on standard datasets show the effectiveness of sign rate encoding in improving accuracy across all settings including adversarial robustness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper aims to explore an input encoding that balances the robustness and generalization on clean input of the model. The authors propose the signed rate encoding (SRATE) method that improves the accuracy of the model. In addition, they also introduce the sparse encoding attack on the SRATE input. Through theoretical analysis and experiments on datasets like CIFAR-10 and CIFAR-100, the authors demonstrate that SRATE improves generalization, while adversarial training with SEA offers superior robustness compared to traditional methods.

### Strengths
The proposed method utilizes the rate-coding input, which is not only more bio-plausible but also provides inherent advantages in robustness and sparsity, distinguishing it from models that rely on constant input encoding methods.

The authors provide a solid theoretical basis for the SRATE, demonstrating that it preserves the essential characteristics of Poisson input encoding while effectively reducing randomness. 

The authors proposed a novel attack method, offering a solution for finding optimal adversarial examples under binary and sparsity constraints.

### Weaknesses
One drawback of this method is its relatively low accuracy on clean inputs, with even the non-adversarially trained model achieving only ~55% accuracy on the CIFAR-100 dataset. The significant drop in clean accuracy may not justify the robustness gains, which raises the questions about the effectiveness of this approach, particularly when other methods (e.g. adversarial training) may offer a better balance between performance and robustness.



### Questions
Sparsity is a critical feature in neural systems, offering benefits in terms of computational efficiency and reduced energy consumption. Given that this model is based on rate encoding, I wonder whether the model with SRATE encoding also leverages these advantages? 

It would be valuable to know if the authors considered using the Expectation Over Transformations (EOT) method for adversarial attacks, especially since EOT is an effective approach to deal with models that incorporate randomness.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a signed rate encoding (SRATE) method that enables mean-centering of the input, reducing the randomness introduced by traditional rate encoding. This approach improves clean accuracy and enhances the generalization of rate-encoded spiking neural networks (SNNs).

### Strengths
The paper is well-structured and easy to follow.
The performance results show improvement with the proposed method.

### Weaknesses
Some details require further clarification. Specifically, the description of the signed rate encoding (SRATE) method lacks sufficient detail regarding its implementation. It is unclear how the mean-centering is precisely achieved in practice, especially concerning the temporal dynamics of the spike trains. The paper mentions that the encoding reduces randomness, but a more quantitative analysis of this reduction would be beneficial. Additionally, the explanation of how the adversarial attacks are adapted for rate-based models is somewhat vague. While the authors mention the use of the Straight-Through Estimator, they do not provide enough detail on how this is applied to the specific stochastic spiking neurons used in the network. The inconsistent notation for attacks (lowercase) and models (uppercase) in Figure 4 and Table 5, while explained, is still confusing and could be a source of misinterpretation.

### Questions
In the method section, is the encoding applied only to convert images to spike inputs, or does it also occur within spiking neurons in the network?

How could this technique be adapted for use with event-based datasets?

In Section 4.1, why does the attack rely on a first-order approximation rather than directly using the loss? What would happen if the direct loss were used instead?

In Figure 4 and Table 5, there are inconsistent notations (e.g., lowercase "fgsm" and uppercase "FGSM," similarly for "pgd" and "PGD"). Do these represent different methods, or is this just a formatting inconsistency?

How are FGSM and PGD applied to rate-based models in this study?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new encoding method for SNN input, called Signed Rate Encoding (sRATE), which is experimentally shown to reduce the randomness of encoded inputs through statistical analysis. Additionally, the paper introduces a Sparse Encoding Attack (SEA).

### Strengths
S1. The sRATE is newly proposed and the analysis from randomness reduction is good.

S2. Authors conduct extensive experiments in evaluating the difference between RATE and sRATE SNNs, including adversarial training with various attacks.

### Weaknesses
W1. The theoretical analysis needs improvement. From the current analysis, it is unclear why sRATE (Eq. 12) reduces randomness compared to RATE (Eq. 9). Both $x$ and $|x-\mu|$ (I believe the $x$ in Eq. 12 is actually $x-\mu$, though this is not explicitly stated in Section 3.2) belongs to [0,1], meaning that the actual ranges of $k1$ and $k2$ are the same. The core issue is that the paper does not provide a formal proof or derivation showing that the proposed sRATE encoding provably reduces randomness. Instead, the argument relies on the empirical observation that $k_2$ is smaller than $k_1$ in Table 1, which is insufficient to establish a general principle. The paper needs to rigorously demonstrate why the transformation from $x$ to $|x-\mu|$ leads to a reduction in randomness, rather than simply observing it in experiments. The lack of a theoretical foundation weakens the motivation for using sRATE. 

W2. The novelty of the proposed SEA method seems limited. If I understand correctly, the solution in Eq. (16) appears to be a straightforward application of the FGSM attack to RATE/sRATE encoded inputs. The idea of selecting $k$ elements based on the top $k$ gradients in the SEA method is fairly straightforward. I am also somewhat confused by the results—since the perturbations generated by SEA can be considered a subset of those generated by FGSM (with SEA essentially removing some of the perturbations from the FGSM attack), it is unclear why SEA outperforms FGSM, as shown in Table 5. The paper does not adequately explain why restricting the perturbation to a subset of the gradients would lead to a more effective attack than using all gradients, especially given that FGSM is known to be a strong attack method. A more detailed analysis of the differences between the two methods and their impact on the SNN is needed.

W3. The writing could be improved. In my view, Lemma 1 and Theorem 2 present concepts that are fairly straightforward, and it may not be necessary to dedicate much space to them in the main text. Other writing-related comments (which do not affect my overall rating) are summarized in the Questions section.

### Questions
My primary concerns are outlined in the Weakness section. The following points are related to writing improvements and do not affect my overall rating.

Q1. As mentioned in W1, I believe the $x$ in Section 3.2 should actually be $x-\mu$, since $x$ could otherwise be negative. However, the authors did not clarify this point.

Q2. It seems unnecessary to define 'the positive and negative part' of a real number (Lines 197-199). For the sake of simplicity and readability, I believe it would be clearer to directly use piecewise linear functions instead, as this would make the formulation easier to follow.

Q3. The use of the same notation $k$ for different concepts is somewhat confusing. For instance, $k$ is used to represent randomness in Section 3, but it also denotes the sparsity of perturbations in Section 4.2 and the experiments.

Q4. The legend in Figure 4 is unclear, as it is difficult to distingusih between the dashed and solid lines in the legend.

### Soundness
2

### Presentation
2

### Contribution
2
