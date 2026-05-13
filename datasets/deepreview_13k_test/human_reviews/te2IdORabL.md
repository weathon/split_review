# JPEG Inspired Deep Learning

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Although it is traditionally believed that lossy image compression, such as JPEG compression, has a negative impact on the performance of deep neural networks (DNNs), it is shown by recent works that well-crafted JPEG compression can actually improve the performance of deep learning (DL). Inspired by this, we propose JPEG-DL, a novel DL framework that prepends any underlying DNN architecture with a trainable JPEG compression layer. To make the quantization operation in JPEG compression trainable, a new differentiable soft quantizer is employed at the JPEG layer, and then the quantization operation and underlying DNN are jointly trained. Extensive experiments show that in comparison with the standard DL,  JPEG-DL delivers significant accuracy improvements across various datasets and model architectures while enhancing robustness against adversarial attacks. Particularly, on some fine-grained image classification datasets, JPEG-DL can increase prediction accuracy by as much as 20.9\%.git}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors study the impact of JPEG compression to the performance of deep learning, and propose a JPEG-inspired deep learning framework. For that, they present a differentiable soft quantizer to train the JPEG layer. Experiments show that the proposed method increases the accuracy by almost 21%.

### Strengths
1. Overall, the paper is written clearly, and can be easily understood.
2. A variety of experiments are conducted to verify the effectiveness.
3. The used technique seems sound, although I don’t check it in detail.

### Weaknesses
1. I don’t think the problem studied in this paper is very important in the community. Usually, the images fed into deep learning have been precessed by the fixed JPGE compressor, and we don’t have the chance to modify the process like that in this pager, so the actual application value is limited. In addition, I see the paper is an improvement for the method in Yang 2021 (Entropy), which is not followed by many researchers.  
2. Now lots of papers have shown the vision transformer and large model are effective in many computer vision tasks, I don’t know whether the proposed method can adapt to these new networks. The authors should discuss that. 
3. Although a variety of experiments are conducted, the compared method is only one baseline, which can not show the effectiveness.

### Questions
please see the weakness

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
2

### Summary
This paper proposes jointly optimizing both JPEG quantization operation and a DNN to achieve greater effectiveness. A trainable JPEG compression layer with a novel differentiable soft quantizer are proposed. Extensive experiments validate the effectiveness of the proposed method.

### Strengths
1. To make JPEG trainable, a differentiable soft quantizer is proposed. It works well with JPEG. Overall, this paper makes JPEG trainable which is significant contribution. Because many frameworks equipped with JPEG can be trained by the differentiable soft quantizer.
2. A novel DL framework that prepends any underlying DNN architecture with a trainable JPEG compression layer is proposed. Experiments show it can improve the accuracy significantly with only 128 parameters.
3. This paper enjoys a good writing.

### Weaknesses
1. It is better to make a comparison for the latency. The speed of the model is also important to report.
2. Only image classification is considered. The proposed method is better to be validated on more tasks, such as object detection and segementation. 
3. Hyperparameters are tuned differently on different datasets.

### Questions
1. How to conduct datasets for experiments? For ImageNet-1k, the images are already compressed by JPEG. In traditional deep learning framework, the images are loaded and decoded by JPEG. How to insert the encoding operation in this framework?

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
4

### Summary
This work proposes a new training framework for deep learning models, JPEG-DL, utilizing an image compression module to improve the model performance. To this end, a learnable JPEG-based image compression layer is introduced with a differentiable soft quantization method and is trained jointly with a main model. At test time, a compressed image from the compression layer is fed into the model. The experimental results show consistent performance improvements of existing classification models on various benchmarks with higher robustness on adversarial attacks.

### Strengths
- The approach of leveraging image compression to improve pure performance of a model is interesting.
- The paper is well-written and it is easy to follow.
- A variety of network architectures and datasets are used in the experiments.

### Weaknesses
Major concerns:
- A comparison to training with JPEG-based data augmentation is required to validate that the proposed method provides benefits beyond simple data augmentation using JPEG. 
- There is no baseline for the differentiable quantizer. For example, comparisons could be made with methods such as the straight-through estimator (i.e., using the identity function as a gradient function) or additive uniform noise [1].
- The baseline for the image preprocessing method for training is insufficient; only comparison results with the vanilla models are presented. For stronger persuasiveness, comparison results with other learnable or non-learnable preprocessing modules are needed.
- In L199, it is mentioned that the differentiable soft quantizer is adapted from Yang & Hamidi (2024), but it seems unclear what that exact referenced paper is. Is the patent (https://patents.google.com/patent/US11461646B2/en) the correct source?
- The analysis on the significant difference between performance improvements across different datasets is needed. For instance, in Table 2, what accounts for the notable performance improvement in fine-grained tasks (especially the Flowers dataset)? Additionally, why is there few performance gain in the ImageNet results in Table 3?

Minor concerns:
- The empirical study is limited to classification tasks. 
- In Table 4, the bits per pixel (bpp) is excessively high, making it incomparable to typical lossy compression methods. While empirically showing the possibility of compression, it does not seem particularly convincing.
- The proposed method requires additional computation for encoding and decoding of an image, but the time complexity is not investigated.
- A typo in L292 "we fixe".

[1] Ballé et al., End-to-end Optimized Image Compression, ICLR 2017.

### Questions
- Is the target of the adversarial attack in Figure 3 the whole model including the JPEG layer?
- There appears to be more room for exploration regarding preprocessing modules for performance enhancement. For example, what if deep learning-based image compression models were used? What about a simple autoencoder?

### Soundness
2

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
The paper introduces a trainable JPEG inspired layer to neural networks. The new layer performs the linear JPEG steps of RGB to YCbCr and DCT with the non-differentiable quantization step replaced with a learnable quantization proxy finishing with the linear IDCT and YCbCr to RGB.  The learnable quantization proxy uses a soft-max with a tunable parameter which controls how close the proxy matches true quantization. The quantization step size is a learnable parameter in this layer. The paper shows how including this layer as the first layer of neural network architectures can improve their accuracy on different tasks.

### Strengths
Overall this is a very interesting paper with an unintuitive result. As the authors point out (ln 30) the conventional wisdom is that JPEG compression removes information from an image and should only hurt neural network accuracy. However as this paper, and some prior works, show that is not necessarily the case. This paper builds significantly on prior works by showing not only that JPEG compression can be mitigated, but that it can actually be a large component of a neural networks success and proposing a method for achieving this. The differential soft quantizer is something which may be useful in many different applications, potentially being a better option that the addition of noise or a straight-through gradient as it more accurately models the information loss. Finally, the results show a clear improvement when incorporating the method.

### Weaknesses
While the appendix was fairly comprehensive with additional results there are a few additional things that I would have liked to see. The first is that the paper only tests the JPEG layer as the first layer of the architecture, there could have been more experiments in layer placement that would have been really interesting to see. It also wasn't immediately clear to me how $\alpha$ was being set in experiments, I understand that there is a derivation of $\frac{\partial}{\partial\alpha}$ but is that parameter actually trained and if so how was the gradient magnitude controlled? There is some discussion of this from ln 689 but it was a little unclear if $\alpha$ was fixed or not. One thing missing from the JPEG step was chroma subsampling: another non-linearity. Was this considered? It would be fascinating to see if neural networks respond to missing color information similarly to humans.

Lastly, and maybe most importantly, there was little discussion of *why this couterintuitive results holds*. While many view JPEG as something incidental the core idea of JPEG to isolate important information based on frequency bands. My take on the results presented here is that the learnable layer is essentially filtering out information which is irrelevant for the networks task, but I would love to hear the authors take on it. Perhaps such analysis could lead to a more direct approach? (For example: a layer which only filters frequencies or which alters the color channels, etc.)

### Questions
* Could we see even better results if the JPEG layer was included periodically? 
    * What if *all* nonlinearity was replaced with the JPEG layer?
* Please clarify how $\alpha$ was used in experiments
* What about chroma subsampling?
* Why do the authors think this layer helps?

## Update After Discussion

After discussion with the authors I am raising my rating

The authors did a great job responding to the concerns of myself and fellow reviews and went above and beyond on additional experiments which strengthen the case for this paper quite a bit. I specifically have to call out the layer 1 non-linearity experiments that the authors conducted on a very short turnaround that shows additional gains for the JPEG layer. Given the impact of this result I have to conclude that there is indeed something fundamental about using a JPEG inspired layer as a non-linearity which could have repercussions on the broader field. As I stated in a comment, many view JPEG as something incidental; a specific way of storing images. But the core idea of JPEG is to re-weight frequency bands based on their importance. We know from several studies (Maiya et al. [1] for example) that such re-weighting affects neural networks much as it does humans and this paper gives an actionable method for capturing this phenomenon.

1. Maiya, Shishira R., et al. "Unifying the Harmonic Analysis of Adversarial Attacks and Robustness." BMVC. 2023.

### Soundness
3

### Presentation
3

### Contribution
3
