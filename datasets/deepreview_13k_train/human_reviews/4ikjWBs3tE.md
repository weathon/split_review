# Transformers Learn Low Sensitivity Functions: Investigations and Implications

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Transformers achieve state-of-the-art accuracy and robustness across many tasks, but an understanding of their inductive biases and how those biases differ from other neural network architectures remains elusive. In this work, we identify the sensitivity of the model to token-wise random perturbations in the input as a unified metric which explains the inductive bias of transformers across different data modalities and distinguishes them from other architectures. We show that transformers have lower sensitivity than MLPs,  CNNs, ConvMixers and LSTMs, across both vision and language tasks. We also show that this low-sensitivity bias has important implications: i) lower sensitivity correlates with improved robustness; it can also be used as an efficient intervention to further improve the robustness of transformers; ii) it corresponds to flatter minima in the loss landscape; and iii) it can serve as a progress measure for grokking. We support these findings with theoretical results showing (weak) spectral bias of transformers in the NTK regime, and improved robustness due to the lower sensitivity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper considers implicit biases for the transformer architecture. They describe sensitivity of a function as the change in the function value averaged over all possible element-wise changes to the function input, averaged or maxed over all inputs on a hypercube. Such functions can be described using polynomials with the sensitivity connected to the degree of the polynomial. The paper proves that a linear attention transformer is biased (in the eigenvalue of the NTK sense) toward low-sensitivity functions characterized by the degree. Then they go on to generalize the notion of sensitivity for neighborhoods of general (non-boolean) inputs.

### Strengths
- Useful formalization of sensitivity 
- Interesting findings about low sensitivity, robustness, and sensitivity to different parts of the input (like last token in a sequence)
- variety of tasks for better understanding of where architecture properties come from
- connecting between grokking and sensitivity provides a new lens into understanding and improving DNN training.

### Weaknesses
 - On line 141, "where the eigenvalues are non-decreasing with the degree of the multi-linear monomials" would be easier if it said "eigenvalues do not decrease as the degree increases."


### Questions
- What's the difference between sensitivity and adversarial/robustness that looks at neighborhoods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work builds on the theoretical notion of boolean sensitivity, extending it to an empirically measurable quantity and studying it for the case of transformers. It finds that transformers have lower input sensitivity on the training data, compared to other architectures, and that this is correlated with other phenomena such as test-time robustness, sharpness of minima, and grokking.

### Strengths
The study in the paper is quite intriguing. A few things I liked:
 * Provides a new lens on what is different about transformers
 * Demonstrates phenomena consistently across many datasets
 * Provides a new lens on grokking not captured by the weight norm

### Weaknesses
There were a few key places where I felt the paper overclaimed or made dubious claims, which are enough for me to not favor acceptance. In particular:
 * Lower sensitivity leads to robustness: this is basically a restatement of the claim that Gaussian data augmentation improves robustness. This is a very well-known result, the authors do say that it is in line with other results in the literature, but I feel they are understating the extent to which this is well-trodden ground (for instance, Hendrycks, one of the authors of CIFAR-10-C, has published an entire line of work on data augmentation methods for improving robustness; Gaussian noise is the simplest of these and many others work far better).
 * Perhaps more importantly, this sentence does not seem merited: "Together, these results indicate that the inductive bias of transformers to learn functions of lower sensitivity *explains* the improved robustness (to common corruptions) compared to CNNs." I am not sure what "explains" means, but there are many other interventions that improve robustness (such as the data augmentation methods mentioned above), and some of those might have better explanatory power.
 * It is not entirely clear whether input sensitivity is a *different* phenomena than test-time robustness to perturbations. The main difference is it is computed on the training set instead of the test set --- but are there cases where these come apart, or is test-time and train-time input sensitivity always highly correlated?
    * I think the results could be interesting either way -- but if they are the same, then this is interesting mainly because it is a proxy for robustness that can be computed at training time; if they are different, then understanding the differences would be interesting.

### Questions
Have you compared input sensitivity and perturbation robustness at test time? When if ever do they behave differently?

### Soundness
1

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores the inductive biases of transformers, particularly their tendency to learn low-sensitivity functions. It introduces sensitivity as a measure of how model predictions respond to token-wise perturbations in the input. By comparing transformers to other architectures like MLPs, CNNs, ConvMixers, and LSTMs across both vision and language tasks, the paper shows that transformers consistently exhibit lower sensitivity. This low-sensitivity bias is linked to improved robustness, flatter minima in the loss landscape, and hence better generalization. Additionally, the authors propose that sensitivity could act as a progress measure in training, and is linked to grokking.

### Strengths
**Key strength:** In addition to the general importance of developing rigorous understanding of how transformers work and why they show such remarkable properties, this paper proposes a novel perspective by looking into sensitivity. They rigorously define sensitivity and provide strong arguments on how it links to other important properties, such as robustness and generalization. They also show that it can track progress when grokking happens, which I think is an important finding and could potentially enable a series of future studies on grokking.

**Other strengths:** Here are a list of other points that I commend the authors for:
- The introduction is quite well written and motivates the main question quite well (thought it could be improved; see weaknesses). Similarly, the contributions are well explained at the end of the introduction.
- The presentation of the paper is strong, and maintains a good balance between accessibility and rigor.
- Propositions 2.1. And 2.2 are really interesting results on the spectral bias and sensitivity of transformers. 
- The authors explain the implications of their theory quite well.
- The experimental design is thorough and well-tailored to validating the theory.
- While I consider this a theoretical paper, the experiments are quite strong and cover various aspects of the paper’s main questions.

### Weaknesses
I do not see any major weakness. But there could be some improvements. See my suggestions for improvement, below.
1. While the paper clearly explains that lower sensitivity is linked to higher robustness, trade-off/connection with expressivity and performance are not discussed. There is a well-established trade-off in various contexts (see, e.g., [1-2]), and it would further strengthen the paper to discuss this.

2. Though I think the introduction is quite well-written, I think it under-emphasizes the findings of the paper on the role of sensitivity analysis. The authors conduct a rigorous analysis of the transformers sensitivity and use that to clarifies some of the important properties of transformers as I mentioned for the strengths, but while doing so, they also show, quite rigorously with strong theory and experiments, how sensitivity analysis could be used to understand generalization, grokking, etc. Near the end of the paper this realization caught my attention, and the authors actually do point this out more clearly in the Conclusion, but I think this can be better emphasized in the Introduction.

3. I suggest the authors bring the Limitation section from the appendix to the main paper. The limitations are not discussed in the main paper, while it is always important to discuss them.

4. This is a rather minor point and it might be a matter of taste: Do sections 5 and 6 really need to be separate sections? It seems like the findings are generally similar, and they could be merged in one section of empirical analysis of vision and language models.

### Questions
1. Related to weakness 1, how do you think the sensitivity and robustness relate to expressivity and performance in transformers?

2. Lines 310-311 mention generalization capabilities of different models as a reason to investigate sensitivity during training. This made me curious, what do you think the connection between generalizability in representation learning or classification relates to generalizability in sensitivity (I think one direction of it is clear, but the other direction is not)?

3. In line 394, you mention that use the same number of layers for LSTM and RoBERTa for fair comparison. How about the model size in terms of number of parameters? How many parameters in each model? And how do you think changing this could impact your results?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies the sentitivity of functions defined by different deep learning architectures, comparing the specific case of Transformers with CNNs and Mixers. The work stems from previous work tha has studied sensitivity with Boolean inputs, and derives a formulation for token-based models. The authors make a connection between sensitivity and robustness, show how ViTs are less sensitive than other architectures and also show how sensitivity can be used for grokking analysis.
Experiments on synthetic data are provided, as well as experiments using ViT on small datasets (CIFAR, SVHN, ImageNet) and LLMs on 2 datasets (MRPC and QQP).

### Strengths
**Originality:**

Focusing on sensitivity starting from the Boolean formulation is original. I also found the experiment on a synthetic vocabulary (3.1) original.

**Clarity:**

The paper is well written, with clear language. The mathematical notation and formulation is also easy to read.

**Significance:**

The study of sensitivity in current models is important for interpretability as well as to design better training strategies.

### Weaknesses
 **Originality:**

While sensitivity study has its originality, many previous works have studied sensitivity in many ways, for example by understanding the effects of image augmentations (see contrastive learning literature).

**Quality:**

The experiments provided are either synthetic or use small models/datasets. This makes the claims in the paper weaker in my opinion. For example:
* Results in Section 3 use synthetic data and a single attention layer. I would argue that, while still interesting, these experiments might not transfer to full models with several layers and multiple attention heads.
  * Related to this experiment, other research has been carried out analyzing spurious correlations. For example, the work by Robert Geirhos (among others) has already shown that CNNs tend to learn from the easiest cues available. In the experiments in Section 3.1, these "easy" cues would be the sparse tokens. Once they become uninformative, the next available (but harder) cue are the frequent tokens.

> Geirhos, Robert, et al. "Shortcut learning in deep neural networks." Nature Machine Intelligence 2.11 (2020): 665-673.

> Geirhos, Robert, et al. "ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness." arXiv preprint arXiv:1811.12231 (2018).

* Results in Section 4 use small datasets (CIFAR, SVHN) and arguably a medium size dataset nowadays (ImageNet). The models used (Vit-simple/small) are far from real scenarios nowadays, and the compared architectures are also small (3-layer CNN in for example).

* Results in Section 5 use a Roberta model (2019) which does not have the same properties as current LLMs. Also, this model is trained from scratch on small tasks, which also does not transfer to current abilities of LLMs.

In several cases, bold conclusions are extracted from a single model / single dataset experiment, with which I cannot agree. For example, the claim in L357 *"Thus, transformers learn lower sensitivity functions compared to MLPs, ConvMixers, and CNNs"* is validated with a 3-layer CNN on a small dataset like SVHN.

**Clarity:**

* It is not clear how the noising strategy is performed. The text mentions that _tokens_ are polluted with noise, however Fig 1 shows the noise applied to the pixel patch and says *" the original image and the corrupted image are fed into the same neural network"* (which implies that noise is applied at pixel level). The authors should clarify this important aspect.

* It is also not clear how noising is applied to CNNs (which are not patch/token based).

* Proposition 2.1 is harder to parse than the rest of the text, and it is hard to understand why it is important for the paper.

**Significance:**

While the objective of the paper is significant, the results provided and the size of the experiments laregly diminish the impact of this work.

### Questions
* Following up on my previous comment, the authors should clarify if the noising procedure is applied on patches (pixels) or token representations. Fig. 1 contradicts the text.
  * Also, how is noising applied on CNNs?

* How is $\sigma$ important, and why were different $\sigma$ chosen for the experiments in Section 4. I personally find it a drawback that one needs to find a right $\sigma$, and that using different ones the conclusions might change. Also, bold claims are provided with a single (different) sigma per dataset, which raises some questions.

* ViT/LLMs might produce different token scales, but $\sigma$ is kept fixed. This can impact strongly some tokens and leave others almost noise-less. I find this also a negative point of this algorithm, since some "topics" might by-pass the noising.

* How is a single attention representative of a large Transfomer in Section 3.1. I would ask the authors to elaborate on this.
  * Additionally, why have a linear layer $U$ after another linear layer $W_v$, since the composition of both is already a linear layer?

* In Fig. 4, only the training accuracy is provided. What about the test accuracies? It is known that models achieve perfect train accuracy, but the test accuracy might be very different though. Does the test accuracy correlate with the sensitivity (measured on train data as you already do)?

* About the claim in L347 *_"This shows that the observations on small-scale models studied in this section transfer to large-scale pretrained models."_*. By increasing scale, the sensitivity of a conv model has gone down to 0.0342, which is much lower than 0.0829 for ResNet-18. Also, ViT went up from 0.0014 to 0.0191. It would be fair to conclude that scaling up brings sensitivities closer, which would mean that small-scale does not transfer to large-scale. Also, one could go much larger in scale (larger ViT, larger datasets) and see if the trend is still maintained or sensitivities are even closer. 

* Claims in Section 5 are obtained with one Language model (Roberta) and one LSTM on 2 small datasets. I cannot agree with the claims being generic for *Language Tasks* with this setup. Moreover knowing that current LLMs have much different properties than LMs used in 2019 (Roberta).

### Soundness
2

### Presentation
3

### Contribution
2
