# Confidential-DPproof: Confidential Proof of Differentially Private Training

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
Post hoc privacy auditing techniques can be used to test the privacy guarantees of a model, but come with several limitations: (i) they can only establish lower bounds on the privacy loss, (ii) the intermediate model updates and some data must be shared with the auditor to get a better approximation of the privacy loss, and (iii) the auditor typically faces a steep computational cost to run a large number of attacks. In this paper, we propose to proactively generate a cryptographic certificate of privacy during training to forego such auditing limitations. We introduce Confidential-DPproof , a framework for Confidential Proof of Differentially Private Training, which enhances training with a certificate of the $(\varepsilon,\delta)$-DP guarantee achieved. To obtain this certificate without revealing information about the training data or model, we design a customized zero-knowledge proof protocol tailored to the requirements introduced by differentially private training, including random noise addition and privacy amplification by subsampling. In experiments on CIFAR-10, Confidential-DPproof trains a model achieving state-of-the-art $91$% test accuracy with a certified privacy guarantee of $(\varepsilon=0.55,\delta=10^{-5})$-DP in approximately 100 hours.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies important problem in data privacy research, the privacy auditing problem. The main approach is a zero-knowledge proof protocol for differential private machine learning.

### Strengths
The paper seems well-written.

### Weaknesses
Due to my lack background of zero-knowledge proof, it's difficult to evaluate the contribution.



### Questions
1. How this framework to give guidance to correct DP-SGD implementation if the algorithm did not pass the privacy auditing?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a protocol for auditing DP-SGD. The approach is based on zero-knowledge proof and does not require the auditor to access the model and raw data.

### Strengths
1. The problem of verifying privacy claims of algorithms is very important practically.
2. The proposed protocol based on zero-knowledge proofs does not require the auditor to access model parameters, data, and intermediate updates. 
3. The authors take into account malicious auditors and dishonest provers in various aspects of the protocol such as random seed generation and

### Weaknesses
1. The auditor needs to know many implementation details, e.g. clip threshold, and number of iterations. Also, the protocol is specifically designed for DP-SGD. It seems that we need to design different protocols for different algorithms, even if we only make minor adjustments to the algorithm. 
2. Many steps in the DP-SGD algorithm need to be proved in Phase 3. If one step is missing, for example, the auditor forgets to let the prover verify step vi, the total number of iterations, how would it affect validity of the privacy audit claims made by the auditor?
3. The proposed cryptographic approach does not scale to large models trained with DP-SGD.
4. It seems to me that the protocol only attempts to verify that every step of the DP-SGD algorithm is executed correctly as claimed, and the certified privacy parameters are simply derived based on the verified $\sigma$ and subsampling level, which is an upper bound on the actual privacy guarantee (as stated in the conclusion). Thus, when the certified upper bound exceeds the claimed value, we do not know whether there is a privacy failure. Note that even with 100% correct execution of DP-SGD, privacy failure may still exist due to other issues like finite precision computation of floats [1]. Thus, verifying all steps are executed correctly is not sufficient to audit privacy claims, and a privacy lower bound should still be necessary.
5. How does the approach compare to the recent work of [2]?
6. I have questions regarding the experiment setup. See the question section.

Typos:
1. Page 5, line 10 (the description of phase 2): "Next, the auditor generates... and sends.. to the auditor". The second "auditor" should be "prover"?
2. Page 6, line 2: we first generates -> generate

### Questions
1. What are the hyper-parameters: $C, \sigma, T$ in your experiments, and what are the corresponding theoretical upper bounds on $\epsilon, \delta$?
2. Compared to the privacy upper bound provided for the chosen $\sigma$, how accurate are the certified privacy guarantees?
3. The results do not show certified level of $\delta$.
4. The running time may vary across different machines and may not be a consistent measure of computational cost.

## Update
Increase my score to 6 after the authors quickly implemented ZKP for DP-FTRL.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a zero-knowledge proof (ZKP) protocol, dubbed Confidential-DPproof, for an auditor to verify that a company (prover) has trained a ML model using DP-SGG at a certain privacy level, on a fixed private dataset (which should not be revealed to the auditor). Their method has three desirable properties:

1. An honest prover can convince an honest auditor that they have correctly implemented DP-SGD (and therefore that the resulting model is differentially private at a certain level, known to both parties);
2. A dishonest prover cannot convince an honest auditor that the trained model satisfies DP when it in fact does not; and
3. A dishonest auditor cannot bias the computations of an honest prover. In particular, a dishonest auditor cannot gain additional information about the training data, beyond what they would know from observing the output of a DP algorithm trained on the private data.

Experiments with Confidential-DPproof show that the ZKP mechanisms still allow for practically feasible runtimes for model training. The authors obtain strong model utility on CIFAR-10 and MNIST, while still enforcing strong DP guarantees ($\epsilon < 1$).

### Strengths
Confidential-DPproof provides a strong alternative to current methods for privacy auditing, which require instantiating membership inference adversaries to exploit the output of allegedly DP algorithms, thereby providing a lower bound on the privacy leakage. Unless the adversary can be shown to be optimal, however, this approach cannot provide an _upper_ bound on the privacy leakage. In general, implementing such attacks is also computationally difficult, and optimal adversaries are often intractable.

By approaching the problem from a different angle, the authors completely sidestep the need for optimal adversaries for verifying privacy guarantees. This is especially impressive because many of the strongest membership inference attacks require access to the private data in order to be trained (or at least a very good proxy), but this is unrealistic in practical scenarios requiring privacy. In contrast, their method does not require the auditor to have access to any private training data. As such, I believe this to be an exciting, non-incremental contribution, one which has the potential to change the paradigm for privacy auditing moving forward.

### Weaknesses
As ICLR is not primarily a security conference, it is likely that many readers will be unfamiliar with the terms and methodology used. As such, more discussion of the cryptographic primitives used would be helpful in improving the clarity of the paper. (See the "Questions" section below.)

Due to the additional computational overhead imposed by both DP-SGD itself, and the need to represent the steps of the algorithm in circuits which can be integrated with existing ZKP systems, the authors cannot train full neural networks. Instead, they rely on fixed feature extraction methods trained on public data or using other methods independent of the private training data, then train a logistic classifier on top of these representations. Even with these simplifications, gradient computation + clipping can still take over a second per sample in higher feature dimensions. This limitation significantly restricts the applicability of the proposed method to more complex models and datasets. Furthermore, the paper does not fully explore the trade-offs between the level of privacy (epsilon value), model utility, and the computational cost of the ZKP. A more detailed analysis of these trade-offs would be beneficial for understanding the practical limitations of the approach. Finally, while the authors address the issue of unbiased randomness, the paper could benefit from a more rigorous discussion of the security assumptions underlying the cryptographic primitives used, particularly in the context of potential attacks on the ZKP system.

### Questions
I do not have extensive background with ZKPs, so I would like to make sure my understanding of the paper is correct. Can the authors confirm if the following statements are true?

**Unbiased random seed generation:** From the honest prover's perspective, since $k$ was chosen uniformly at random and the auditor only knows $[[k]]$ (but nothing about $k$ itself), the random seed $s=k\oplus r$ is still uniformly random. From the honest auditor's perspective, since $r$ was chosen uniformly at random _after_ $k$ was fixed, $s$ must be uniformly random.

**Dataset commitment:** For verifying that the computations were performed on the committed dataset, we can think of it as follows. The data commitment is another key $K$ which depends on the dataset $\mathcal{D}$, but which gives the auditor no information about $\mathcal{D}$ (since it was an XOR with a private random quantity $M$ known only to the prover; this is similar to the relationship between $k$ and $[[k]]$ above). However, for each circuit $\mathcal{C}$ making up a step of the DP-SGD procedure, the prover can verify that the output of this step was computed on $\mathcal{D}$ using the agreed upon random seed, and this verification _only requires knowledge of $K$_, not $\mathcal{D}$ itself.

**DP-SGD privacy accounting:** This leads to my final question. It seems that the ZKP building blocks allow you to generate a proof for each iteration in DP-SGD, then the proof for the whole procedure is just the AND of all of these steps. In particular, this means that the auditor actually will see all of the intermediate models during the DP-SGD training procedure. There has been some recent work on improving the privacy guarantees of DP-SGD under the assumption that the algorithm output is only the _final_ model parameters $W^T$, rather than the entire trajectory [1]. Confidential-DPproof would be incompatible with this analysis, since there isn't a ZKP protocol (yet) which encodes the entire model training procedure, rather than just the individual steps.

Reference:
[1] Ye, Jiayuan, and Reza Shokri. "Differentially private learning needs hidden state (or much faster convergence)." Advances in Neural Information Processing Systems 35 (2022): 703-715.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
