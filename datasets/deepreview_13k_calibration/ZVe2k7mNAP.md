# MQ-VAE: Training Vector-Quantized Networks via Meta Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Deep neural networks with discrete latent variables are particularly well-suited for tasks that naturally involve sequences of discrete symbols.
The vector-quantized variational auto-encoder (VQ-VAE) has made significant progress in this area by leveraging vector quantization.
However, while much effort has been put into maximizing codebook utilization, this does not always result in better performance.
Additional challenges include quantization errors in the VQ layer and the lack of direct integration of task loss into the codebook objective.
To address these issues, we propose Meta-Quantized Variational Auto-Encoder (MQ-VAE), a bi-level optimization-based vector quantization framework inspired by meta-learning.
In MQ-VAE, the codebook and encoder-decoder pair are optimized at different levels, with the codebook treated as hyperparameters optimized via hyper-gradient descent.
This approach effectively tackles these challenges within a unified framework.
The evaluation of MQ-VAE on two computer vision tasks demonstrates its superiority over existing methods and ablation baselines.
Code is available at https://anonymous.4open.science/r/MQVAE-B52C.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to use meta learning to improve training of VQ-VAEs, which are hard to optimize due to the non-differentiability of the vector quantization operation. More specifically the authors propose to optimize the encoder and decoder parameters in the inner loop, and the codebook in the outer loop. The advantage of this approach is that the codebook gets direct feedback from the reconstruction loss, and not indirect feedback as in the original formulation. Different variants of the proposed meta learning algorithm and baselines are compared on CIFAR100 and FashionMNIST reconstruction and image generation. The authors further present results for applying their method to the feature maps of a ResNet.

### Strengths
To my knowledge, the application of meta learning to training VQ-VAEs is new. The proposed algorithm is clearly explained, and the paper also proposes some sound tweaks of the algorithm. At a high level, the experiment design makes sense.

### Weaknesses
- The experimental results on image reconstruction/generation are not very convincing. The method is only applied to very low resolution, small data sets, and the tasks are quite simple (CIFAR100, FashionMNIST), so it’s unclear how and whether the method generalizes to more modern VQ-VAE designs involving perceptual losses such as VQGAN [1]. The lack of experiments on more complex datasets and higher resolutions makes it difficult to assess the practical impact of the proposed method. Specifically, the absence of results on datasets like ImageNet or even larger-scale datasets with more complex image structures raises concerns about the scalability and generalizability of the approach.
- I appreciate that the authors address computational cost in Section 5.5, showing that MQ-VAE requires roughly 4x the compute of the baseline. However, the fair comparison would be to train VQ-VAE 4x longer, but MQ-VAE and VQ-VAE are only compared when trained for the same number of iterations (e.g. Figure 4). In particular it seems that the cheaper alternating optimization and/or synced codebook updates come close to the proposed method (Table 2), so they might match or outperform it in a compute matched comparison. The fact that the proposed method requires significantly more computation without a clear demonstration of superior performance when accounting for compute, raises questions about its practical utility. The ablation studies also suggest that simpler methods may achieve comparable results with less computational overhead.
- It is somewhat unclear whether the FID and IS metrics provided in Table 1 and 3 are reconstruction or generation metrics. Generally the text seems to make not always a clear distinction between the two. This ambiguity makes it difficult to interpret the results and understand the true capabilities of the proposed method. Clearer labeling and explanations are needed to differentiate between reconstruction and generation performance.
- Some of the methods are “+group” variants. This is not explained as far as I could see, nor is a reference provided. The lack of explanation for these variants makes it difficult to understand the experimental setup and the specific configurations being compared. This lack of clarity hinders the reproducibility and interpretability of the results.

Minor:
- The authors provided code, which is great. Nevertheless, it would be good to provide some details about the model architectures (both VAE and PixelCNN) and optimizers in the paper.

### Questions
- All the models have their codebook initialized with k-means. This is not novel, but is usually not required for VQ-VAEs to work reasonably well. Did the authors observe optimization issues when randomly initializing the codebook?
- Some recent works [2, 3] do not use an explicit codebook, but rather just scalar-quantize feature maps. These methods do not suffer from a “task-unaware codebook” since all parameters get gradients from the task loss. Could the authors comment on this?

\
[2] Yu et al. "Language Model Beats Diffusion--Tokenizer is Key to Visual Generation." ICLR 2024
[3] Mentzer et al. "Finite scalar quantization: Vq-vae made simple." ICLR 2024

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new training algorithm for learning vector-quantized variational autoencoders (VQ-VAEs). The proposed method interprets the training of VQ-VAE as a bi-level optimization and applies a meta-learning-inspired technique to solve the optimization. The idea seems novel and straightforward, and the experimental results look promising.

### Strengths
* The bi-level optimization view of VQ-VAE training is persuasive and seems novel. 
* The proposed algorithm is straightforward and achieves strong performance.
* The related works and the background information are carefully covered.

### Weaknesses
 * An obvious drawback of the proposed method is additional compute overhead and implementation complexity. However, this point is honestly described in Section 5.5 and Table 4. The improvement in various task performance metrics justifies the additional overhead of the algorithm.
* The scale and the diversity of experiments are relatively small compared to modern standards. Including a larger-scale image dataset (e.g., image of size 64x64 or larger) or experiments on a non-image dataset (e.g., medical, audio, time-series, etc.) would greatly enrich the paper.

### Questions
* FID evaluation protocol is known to be highly sensitive to implementation details. It would be beneficial in terms of reproducibility to state the detailed procedure involved in FID computation, such as which software package is used and how images are preprocessed.
* Could you include some examples of generated images in the supplementary material so readers can qualitatively appreciate the improvement in generation quality?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This submission proposed to conduct quantization for hidden emebeddings / vectors / codebook in VAE (Variational Auto-Encoder). Specially, it designed a bi-level optimization framework to update encoder/decoder (full-precision parameters) and quantized hidden embeddings alternatively: Normal gradient descent is used in encoder/decoder optimization while the codebook is optimized using a hyper-gradient.

### Strengths
- The method proposed is straightforward and writing is easy to understand.

### Weaknesses
 - My main concern of the submission is the motivation and necessity of hyper-gradient used in codebook optimization. Though author claimed that traditional optimization with STE is task-unaware, the reason behind the claim is not explained. STE is widely used in quantization training while I have not seen it is challenged for unable of catching task information. 
- Besides, hyper-gradient is proposed to solve the problem in the bi-level optimization. My understanding towards the problem lie at: the update of lower/upper part is based on an imperfect update of the counterpart. Hyper-gradient is able to perceive the interaction between the two levels. My question is: why hyper-gradient is used in update of quantized codebook instead of encoder/decoder, or why it is not used in both side?

### Questions
- To prove the necessity of hyper-gradient, author should provide analytical and empirical experiments. Which baseline in Section 5 is using normal gradient descent in both level?
- Please clarify the motivation of hyper-gradient.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
**Background**: Gradient-based meta-learning (GBML) aims to updated a models' parameters $\theta$ such that, after only several gradient updates with respect to a class in the support set, the loss on this task is minimized. Intuitively, it tries to find a good set of model parameters that can be quickly adapted (after a couple finetuning steps) to a downstream distribution. 

**This work.** This paper proposes to adapt gradient-based meta-learning (GBML) from the typical few-shot learning setting into the training of a VQ-VAE. 

Specifically, the encoder parameters $\phi$ and decoder parameters $\theta$ are trained with a fixed codebook for several steps, the loss is computed with the updated encoder/decoder parameters, and the codebook is updated with respect to this loss. As in GBML, the encoder/decoder parameter updates are undone; however unlike the typical GBML algorithm, the loss is computed again with the updated codebook vectors, and one step of gradient descent is performed to update the encoder / decoder parameters [keeping the codebook now fixed]. This process is repeated until convergence.

Intuitively, this approach tries to find a good set of codebook vectors by looking-ahead to see how the Encoders'/Decoders' parameters will drift. The authors

### Strengths
I really enjoyed reading this paper. I see its strengths as:

1. Very well written and easy to understand. A reader with familiarity of gradient-based meta-learning can read a couple paragraphs in the introduction, look at Figure 1, and immediately understand the proposed approach.
2. Comparison to Huh et al. 2023: I was looking for this comparison after reading the introduction, and I appreciate the thorough discourse comparing to a very close method.
3. Finite difference approximation: this isn't new, but it's quite the nice touch to make differentiating through multiple encoder/decoder updates practical.
4. Section 4.3 is also quite good: I've seen very few mentions of the *indirect* gradients that appear during meta-learning (or other transfer learning techniques) that appear when you differentiate through a prior parameter update.

### Weaknesses
This paper also presents several weaknesses:

0. Novelty: this paper applies an existing technique (gradient-based meta-learning) to a new setting (VQ-VAE training). That's not an issue in itself -- the ViT paper was incredible even though it applied an existing technique (attention) to a new setting (computer vision). But ViTs were very practical to train and seemed to work really well on computer vision benchmarks. This leads me to my second point:

1. I don't think this method is practical; it is difficult to imagine a researcher or engineer implementing it as they chase sota performance. Implementing a bi-level optimization loop is quite difficult, and many things can go wrong. Even in the meta-learning community, we try to stay away from this as much as possible. Running a bi-level optimization to train a VQ-VAE would be very difficult for real applications. Even with new frameworks like Betty that make it a bit easier, my understanding is that still very difficult and popular training settings like distributed data parallel would not be supported.

 2. The contribution of Huh et al. 2023 in last years ICLR weakens this paper's contribution. I found many of the ideas in that work highly engaging, and while this work advances them in the direction of meta-learning, my sense is that the results / ideas in this paper are less new in the backdrop of Huh et al. 2023.

3. The authors highlight the significance of indirect gradients in red throughout their paper (especially Figure 1 and Section 4.3). When I looked at these for a different application (in meta-learning), it seemed as their gradient norms were **many orders of magnitude less** then the direct gradients. In this context, my prior is that $||\frac{\partial \mathcal{L'}}{\partial \mathcal{C}}|| >>> ||\frac{\partial \phi'}{\partial \mathcal{C}} \frac{\partial \mathcal{L}'}{\partial \phi '}||$ and $||\frac{\partial \mathcal{L'}}{\partial \mathcal{C}}|| >>> ||\frac{\partial \theta'}{\partial \mathcal{C}} \frac{\partial \mathcal{L}'}{\partial \theta '}||$, therefore the effect of the indirect gradients would be almost nothing. I think it is a weakness to not have explored the dynamics of these effects.

4. The experimental results are limited and evaluated on non-realistic datasets. I'm very empathetic to limited computational resources, but evaluating on two small datasets (FashionMNIST and CIFAR100) with a 2017-style VQ-VAE does not convey to me that this would work for a more recent VQ-VAE architecture (such as a VQGAN).

5. The experimental results section seem inconsistent with Huh et al. 2023 -- specifically Table 3 where VQ-VAE + alt + sync is strictly worse than the default VQ-VAE? Is the training setting unstable, or are you reporting that these two techniques actually result in worse performance than the default model for FashionMNIST? 

6. The claim that "MQ-VAE can learn a superior codebook" seems unsupported by the analysis and should be contextualized in the backdrop of recent methods that find not learning the codebook at all can substantively improve performance [1, 2].

### Questions
Please see weaknesses. In particular, addressing:

1. The practicality of this method when implementing a very strong VQ-VAE, and if you believe the results you present on the datasets and architectures that you've chosen provide sufficient evidence to support this claim: "We demonstrate the superiority of MQ-VAE with two computer vision tasks. MQ-VAE significantly outperforms several comparison baselines and ablation methods, highlighting its effectiveness."

2. Inconsistency between Huh et al. 2023 and the results reported on FashionMNIST.

3. Comparison of the magnitude of indirect gradients to the direct ones. If you 0-out the indirect gradients, will the model still perform well? This study would support your assertions that these indirect gradients are crucial for the performance of your approach.

4. The importance of learning a better codebook when recent work has shown that not learning the codebook is actually quite good.

### Soundness
3

### Presentation
3

### Contribution
2
