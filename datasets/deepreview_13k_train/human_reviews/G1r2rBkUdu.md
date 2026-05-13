# Synergy Between Sufficient Changes and Sparse Mixing Procedure for Disentangled Representation Learning

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Disentangled representation learning aims to uncover the latent variables underlying observed data, yet identifying these variables under mild assumptions remains challenging. Some methods rely on sufficient changes in the distribution of latent variables indicated by auxiliary variables, such as domain indices, but acquiring enough domains is often impractical. Alternative approaches exploit the structural sparsity assumption on mixing processes, but this constraint may not hold in practice. Interestingly, we find that these two seemingly unrelated assumptions can actually complement each other. Specifically, when conditioned on auxiliary variables, the sparse mixing process induces independence between latent and observed variables, which simplifies the mapping from estimated to true latent variables and hence compensates for deficiencies of auxiliary variables. Building on this insight, we propose an identifiability theory with less restrictive constraints regarding the auxiliary variables and the sparse mixing process, enhancing applicability to real-world scenarios. Additionally, we develop a generative model framework incorporating a domain encoding network and a sparse mixing constraint and provide two implementations based on variational autoencoders and generative adversarial networks. Experiment results on synthetic and real-world datasets support our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
A disentangled representation learning framework with two types of identifiability guarantees has been proposed. By forcing a sparse mixing procedure, the subspace identifiability is ensured, while sufficient changes in the distribution of latent variables promote componentwise identifiability of latent variables.

### Strengths
- Theoretical understanding of identifiability issue in the disentangled representation
- Proposing two generative implementations based on VAE and GAN using a domain encoding network and sparse mixing constraints
- Synthetic and real-world experiments

### Weaknesses
The notations are heavy and hard to follow. Please provide a comprehensive notation table at the beginning of the paper. and explicitly define each symbol when it's first introduced. For example, 
- In equation (2), what is the meaning of two subscripts of $\mathbf{x}_{k, (1)}$. 
- Other notation also needs to be defined carefully, $\backslash k$ (all index but $k$) ?
- In equation (6), it seems there is a missing integral (the second integral has been omitted). 

There are English typos and errors, e.g., line 157 (contributions --> contribute)

In synthetic experiments, there is no comparison with any nonlinear ICA methods. Comparing the CG-VAE, and CG-GAn with one or two relevant nonlinear ICA methods can be beneficial for readers to understand the advantages of incorporating domain encoding network and sparse mixing constraints in the disentangled representation.

### Questions
- In line 220, the index in $\mathbf{z}_{o1}$ should be $o_1$ ?
- Can you provide some intuition why Sufficient Changes for Component-wise Identification require the second derivative assumption, while this is not the case for the subspace Identification? This could help readers better understand the theoretical foundations of the proposed method.

### Soundness
3

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
In this paper, the authors investigated disentangled representation learning and proposed a new framework by combining two existing methods: sufficient changes and sparse mixing procedures. This framework can guarantee identifiability of the models, because the sparse mixing procedure can induce conditional independence between latent variables , which can simplify the mapping from estimated latent to ground truth. On the other hand, sufficient changes can further improve component-wise identifiability of latent variables. They implemented this framework for two types of deep generative models: VAEs and GANs. They evaluated on multiple datasets and show that their approach can result in better disentangled representations.

### Strengths
Quality and Clarity: In general this paper is in good quality. The paper is well structured and the motivation is significant, and the writing is clear. The authors provide very detailed math derivations for the framework, and to my best knowledge, the derivations are sound. 

Originality: While the paper leverages two existing methods for disentangled representation learning, it is interesting that they explore a framework that combines them in a compatible way, and this framework will also guarantee the identifiability of representation learning.

### Weaknesses
While they validated their framework on multiple datasets, they only provided qualitative results in terms of the disentanglement of learned representations. I would hope that they can evaluated the results more quantitatively and make comparison based on metrics of disentanglement, e.g. the metrics used in [1] and [2]. I guess the reason I want to see this is it is difficult to see the disentanglement only based on t-SNE plots, because t-SNE itself will employ an algorithm that perform dimension reduction into 2D space, so it is likely that this algorithm introduces certain level of disentanglement.



### Questions
What is the reason that the authors choose VAEs and GANs as the two specific types of models that they want to implement the framework with? I mean my main concern is that, since disentangled representation learning has been studied for almost ten years from now, there have been a lot of variants of VAEs that were developed for learning disentangled representations. So I wonder 1) whether their framework can be applied to those variants of VAEs, and 2) if it is possible to compare against those models, such as TC-VAE[3], FactorVAE[4], and HFVAE[5]


[3] Chen, Ricky TQ, et al. "Isolating sources of disentanglement in variational autoencoders." Advances in neural information processing systems 31 (2018).

[4] Kim, Hyunjik, and Andriy Mnih. "Disentangling by factorising." International conference on machine learning. PMLR, 2018.

[5] Esmaeili, Babak, et al. "Structured disentangled representations." The 22nd International Conference on Artificial Intelligence and Statistics. PMLR, 2019.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, authors combine two assumptions for disentangling latent variables (latent identifiability). Thew whole work is based on non-linear ICA (identifiable VAE) with auxiliary variables $u$. Authors show that sufficient changes on the distribution of latent variables and exploiting structural sparsity assumptions on the mixing procedure can be complement each other to achieve better identifiability. Theorems are illustrated and proved in this paper. With both synthetic and real-world experiments, authors show that there proposed approach based on VAE and GAN can achieve good latent indentifiability.

### Strengths
* The theories in this paper is presented and illustrated in a clear way. The schematic graphical model is good. Besides, there are solid prooves of those theorems.
* The contribution is good, I can visually understand the usefulness of the proposed method.
* There are both synthetic results validating the method, and real-world applications to show that the new method is useful.

### Weaknesses
 * The sentence of Theorem A3 is a bit confusing. It is a bit hard to read that long sentence.
* Line 158, why $x_k$ contribute $z_j$? And the derivative $\frac{\partial z_j}{\partial x_k}$. Could the author explain why the relationship is not $z_j$ contribute $x_k$.
* Line 349, "$q(z|x)$  is the an encoder"
* Eq. 9, why loss $L_s$ is chosen to be the absolute sum rather than the squared sum? Will a squared sum be easier to train and more stable? Any reason or trade-off analysis on this choice?
Or does absolute sum have sparsity?
* What is CG-VAE-S? It seems like it was used before it was introduced.
* For synthetic results, why not apply CG-GAN? Also, there are no other baseline methods for comparison.
* It is also very common to compare the generated image with the true by MSE, $R^2$, or cross-entropy (log-likelihood). They are intuitive metrics that are worth seeing.
* Same for the real-world, why not try CG-VAE. If there is some simple reason, authors should state in one sentence why VAE is not suitable for real-world datasets. Also, are there any other alternative methods for real-world, since all four methods are actually some method combinations? Please correct me if my understanding is wrong.
* To me, it would be better to have more experimental results in the main content. The current experiment section is a bit simple. I'd like to see for example, more comprehensive comparison.

### Questions
/

### Soundness
2

### Presentation
2

### Contribution
3
