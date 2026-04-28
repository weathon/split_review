# Sparling: Learning Latent Representations With Extremely Sparse Activations

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 1, 3

## Abstract
Real-world processes often contain intermediate state that can be modeled as an extremely sparse tensor. We introduce \technique{}, a technique that allows you to learn models with intermediate layers that match this state from only end-to-end labeled examples (i.e., no supervision on the intermediate state).
\technique{} uses a new kind of informational bottleneck that enforces levels of activation sparsity unachievable using other techniques. 
We find that extreme sparsity is necessary to achieve good intermediate state modeling. On our synthetic \digitcircle{} domain as well as the \latexocr{} and \audiomnist{} domains, we are able to precisely localize the intermediate states up to feature permutation with $>90\%$ accuracy, even though we only train end-to-end.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an algorithm to learn sparse intermediate representations through constraining activations to be sparse. The proposed algorithm relies on a combination of a ``Spatial Sparsity layer'' and ``adaptive sparse training". The spatial sparsity layer leverages a parametric form of ReLU to control sparsity. The adaptive sparse training anneals the sparsity parameter to encourage learning. The algorithm is evaluated on motif prediction and localization on three datasets.

### Strengths
1. Sparling achieves extreme activation sparsity and promotes learning interpretable representations.
2. The algorithm shows good localization performance on the provided evaluation datasets.
3. The idea of using activation sparsity to maintain representation capacity while allowing for sparse interpretable representations is interesting and could be an interesting direction to study for other models.

### Weaknesses
1. The requirement of $g^*$ being necessary for the final prediction is quite harsh for general settings. While this might be suitable for OCR, it is fairly rare to have localized and independent predictive features in an input. The assumption that the intermediate representation $g^*$ must be a sparse set of localized features that are individually predictive is a strong constraint that limits the applicability of the method to tasks where such a representation is naturally present. This is particularly concerning for tasks where features are highly distributed and entangled, such as in natural images or complex audio signals.

2. The evaluations are limited to OCR style tasks, and audio detection. However, the paper is missing comparisons with other general OCR methods, including Deng (2016) which has been referred to as inspiring several design choices. In addition, the paper suggests several possible applications and downstream tasks, but does not tackle them. The lack of comparison with existing OCR methods, especially those that have inspired the architecture, makes it difficult to assess the practical utility of the proposed approach. The absence of end-to-end evaluations on tasks like im2Latex, or other downstream tasks such as neural attribution, further limits the scope of the evaluation and the potential impact of the work. The paper needs to demonstrate that the proposed method does not sacrifice performance for sparsity, and that it can be useful in more complex settings.

3. The writing (especially figure captions) can be made more clear.

### Questions
Could you elaborate Fig 2? Do the letters represent specific shapes or the digits themselves?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a technique to learn extremely-sparse intermediate representations without any additional supervision on the representation. The proposed method is to set activations below an annealed threshold value to 0 during training. The paper shows via experiments on 3 datasets that Sparling is able to learn sparse representations without meaningful decrease in task error, unlike considered benchmarks. Learned representations are reliably linkable to known motifs that are present in each of the considered datasets.

### Strengths
* The problem of effectively learning sparse representations is important and the proposed approach is effective and novel to my knowledge.
* The empirical results presented on selected datasets are impressive, especially compared to baselines shown.
* The proposed method is extremely simple, and does not require any additional supervision on the representation.

### Weaknesses
 * The experiments in the paper are limited to settings where strong locality priors may be used. It is unclear if the method works in more general settings, and this limits how significant it is. Can Sparling be applied in standard image classification tasks to learn sparse but predictive features?
* The baselines considered are not totally fair. While the Sparling coefficient $t$ is annealed during the training process to alleviate optimization challenges, the coefficient used for L1 loss is set only once, likely preventing L1 loss from learning sparse representations due to the same optimization challenges. Could we see ablations where the L1 coefficient is also annealed similar to the Sparling coefficient? In particular, is the improved sparsity a result of the spatial sparsity layer, or just the annealing scheme?

### Questions
* Does Sparling work for non-convolutional architectures (e.g. MLP)?
* In Figure 6, the retrained $\hat{h}$ outperforms the end-to-end non sparse network. How is this the case? Why is the performance different at all from the Sparling network which trains the motif model and prediction head end-to-end?
* What is the motivation for computing the spatial sparsity layer channelwise?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces SPARLING, a technique that allows to learn models capable of sparsely identifying structure of data without direct supervision. To do so, the paper formulates the problem of learning sparse tensors with an information bottleneck objective. SPARLING is validated on both synthetic data and visual/audio domains.

### Strengths
1. The proposed method is designed to be capable of inducing sparse representations without any direct supervision 
2. The evaluation of the proposed algorithm has been conducted on multiple benchmarks from different modalities (providing good clues of the general applicability of the proposed idea).

### Weaknesses
1. **(Clarity of the work)**. The paper is meandering and very hard to read. It introduces a lot of quantities that are poorly motivated without properly formalizing their definition and without even providing enough intuitions to justify their necessity. For instance, the introduction of the function 'g' and 'h' lacks clear motivation, and their roles in the overall framework are not immediately apparent. The paper would greatly benefit from a more structured presentation, starting with a clear problem statement and then building up the method step-by-step, providing clear definitions and motivations for each component. While the experimental section is more linear and easier to understand and interpret, the previous 2 sections (3 and 4) are the weakest part of the paper. I’d suggest the authors to revise the whole paper and make the hypothesis being tested clearer, as well as the main ideas that lead to the proposed method and the necessity of each design choice.
2. **(Identifiability of the latent factors of variation)**. Not having any guarantees on the identifiability of the latent variables jeopardizes the proposed method, which seeks to find meaningful/interpretable latent variables without any explicit supervision. The paper does not address the fundamental question of when the learned sparse representations actually correspond to the true underlying factors of variation. The method could potentially learn arbitrary sparse representations that do not capture the actual structure of the data. When is a given amount of data enough to guarantee that the proposed method can recover all the latent factors? And, are there any other specific requirements needed to have disentangled factor of variations as discussed in [2]? The lack of theoretical guarantees makes it difficult to assess the reliability of the method. 
    - Since no theoretical guarantee is provided, it would be good to contextualize more the empirical claim on the motif identifiability which in turn, will justify the use of the proposed method.

### Questions
- Can the authors comment more the sparsity assumption on g^* presented in Section 3.1? 
- Section 3.3 is hard to parse and does not clearly highlight the connection between the information bound and SPARLING. 



Minor: 
- The paper contains some typos, I suggest the authors to proofread the manuscript.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper looks into the problem of learning sparse intermediate activations that preserve spatial information, which can help interpret the intermediate outcomes better and be useful for certain tasks. The paper argues that existing methods based on regularization, such as L1 norm on activations, have drawbacks of either low sparsity rate or low accuracy. To overcome this, the paper introduces optimizations such as an extra spatial sparsity layer normalization layer before the activation and iteratively induces a higher sparsity rate during training. The paper evaluates the proposed method on three tasks DIGITCIRCLE, LATEX-OCR, AUDIOMNISTSEQUENCE and shows that it can achieve higher sparsity and higher accuracy than several baselines.

### Strengths
- The proposed spatial sparsify layer together with the adaptive sparsifying method seems to induce a very high sparsity ratio in activations in the tested tasks. 

- The spatial sparsify layer, to the reviewer's best knowledge, seems to be novel.

### Weaknesses
1. The work is a bit under-motivated. While the interpretability of deep neural networks is crucial, the paper looks into the problem from the angle of changing the model architecture and training method to obtain more interpretable representations. As such, it is less clear how the proposed method can impact state-of-the-art deep neural networks that have been used in practice. It would be more helpful if the authors could add some real applications where sparse activations are useful.

2. Related to the motivation issue, the datasets the paper uses for evaluation seem to be a bit artificial and at a tiny scale. It would be helpful if the authors could elaborate a bit more on how the tasks/domains can interact with real-world applications. Also, given the small scale of the datasets, it raises questions on how well the proposed methods can generalize to larger and more complex data.

3. The paper introduces many additional hyperparameters, such as M, d_T, /delta_update. However, the paper does not explain how these hyperparameters are selected, such as the search space and the sensitivity of each hyperparameter.

4. The paper claims that the adaptive sparsity training technique is novel, but it seems to be similar to the iterative pruning method proposed in the lottery ticket hypothesis paper, except that the paper applies it to the activation and via the parameter in the spacial sparsify layer. The paper should better clarify the differences.

### Questions
Can the authors add some real applications or scenarios where sparse activations are useful?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
