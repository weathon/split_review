# Neuroexplicit Diffusion Models for Inpainting of Optical Flow Fields

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Deep learning has revolutionized the field of computer vision by introducing large scale neural networks with millions of parameters. 
Training these networks requires massive datasets and leads to intransparent models that can fail to generalize.
At the other extreme, models designed from partial differential equations (PDEs) embed specialized domain knowledge into mathematical equations and usually rely on few manually chosen hyperparameters.
This makes them transparent by construction and if designed and calibrated carefully, they can generalize well to unseen scenarios. In this paper, we show how to bring model- and data-driven approaches together by combining the explicit PDE-based approaches with convolutional neural networks to obtain the best of both worlds. 
We illustrate a joint architecture for the task of inpainting optical flow fields and show that the combination of model- and data-driven modeling leads to an effective architecture.
Our model outperforms both fully explicit and fully data-driven baselines in terms of reconstruction quality, robustness and amount of required training data. 
Averaging the endpoint error across different mask densities, our method outperforms the explicit baselines by $11-27\%$, the GAN baseline by $47\%$ and the Probabilisitic Diffusion  baseline by $42\%$. With that, our method sets a new state of the art for inpainting of optical flow fields from random masks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new approach that combines model-driven and data-driven methods to achieve improved inpainting of optical flow fields. The authors propose a joint architecture that integrates explicit partial differential equation (PDE)-based approaches with convolutional neural networks (CNNs). The paper demonstrates that their model outperforms both fully explicit and fully data-driven baselines in terms of reconstruction quality, robustness, and amount of required training data.

### Strengths
1. The paper successfully combines the strengths of explicit PDE-based models and CNNs, leveraging the interpretability and generalization capabilities of the former and the learning power of the latter. This integration provides an effective architecture for inpainting optical flow fields.

2. The proposed model achieves superior results compared to both explicit and data-driven baselines. The evaluation demonstrates higher reconstruction quality, robustness, and generalization capabilities, making it an advancement in the field.

2. The neuroexplicit diffusion model requires comparatively fewer learnable parameters and can be trained with significantly less data while still outperforming baselines trained on the full dataset. This aspect addresses the dependency on large-scale datasets, making the model more practical and efficient.

### Weaknesses
1. Although the paper compares the proposed model with explicit and data-driven baselines, it would be beneficial to include a comparison with other recent state-of-the-art methods in inpainting for optical flow fields. This would provide a more comprehensive evaluation and enhance the paper's contribution.

2. The paper assumes prior knowledge of diffusion processes and their application in inpainting. I wonder why diffusion-based inpainting is suitable for flow inpainting? Are there any theoretical explanations for this?
There are also many other traditional inpainting methods, are they also suitable in this task and do they work well with neural networks? Why or why not?

3. In the ablation study part, I wonder is coarse-to-fine approach important in this method? And is it possible to substitute Diffusion Tensor module with other parameter-free inpainting or propagation methods, to see which one best suits this task?

### Questions
Please address the questions in weakness part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an end-to-end pipeline for inpainting values of a diffusion process. The model is a hybrid of explicit (solutions to partial differential equations) and neural (U-net) components, where the evolution of the diffusion process is explicitly computed, but guided by learned parameters. The method is demonstrated on inpainting of optical flow fields, where it bests several chosen baselines that are explicit, neural, and neruoexplicit.

### Strengths
The particular combination of learned and explicit diffusion computation is novel.
The metrics demonstrate accuracy superior to the baselines.
The ablation study in Section 4.3 is informative.

### Weaknesses
The approach has only been demonstrated on one niche application -- optical flow. The paper does mention sparse mask inpainting of images several times, which could be another use case to strengthen the paper.  More results would be appreciated too, perhaps on some real-world datasets such as KITTI.

Figure 1 would be more readable with larger fonts and more separation between the UNet and the D,a arrows. What is the difference between yellow and orange layers in the encoder? The inpainting boxes could be more fleshed out to visualize what they are actually doing (are they solving equation 8?). Where do the iterations come into play?

How does the diffusion tensor D connect to equation 8.

Section 3.1 mentions using average pooling to obtain the coarse version of the sparse flow field. Won't that grossly underestimate the flow field due to all the 0 values? Are those ignored somehow? Are the flow values also scaled down by 2 in each downsampling step, so that they are valid offsets for the coarser image size (similar for upsampling)?

Table 1 could be augmented with train/inference timings, parameter count, and number of iterations. The Figure 3 could be removed and that space used for additional results.

In Figure 2 left, it would be helpful to put the x axis ticks exactly where the samples are. There are only 4 sample sizes, and marking e.g. 0 on the x axis is really not informative.

In Figure 2 right, what does the vertical line down the middle indicate? Is that some ideal mask density threshold?

This sentence is hard to parse: "When evaluated on a density of 10%, the network trained on 5% density can even reach a very close EPE on to the network that was optimized on this density (0.28 vs. 0.29)." Does this intend to state that the network trained on 5% density has EPE of 0.29, while the network trained on 10% density has EPE of 0.28, when both are evaluated on 10% density dataset?

### Questions
Figure 1 would be more readable with larger fonts and more separation between the UNet and the D,a arrows. What is the difference between yellow and orange layers in the encoder? The inpainting boxes could be more fleshed out to visualize what they are actually doing (are they solving equation 8?). Where do the iterations come into play?

How does the diffusion tensor D connect to equation 8.

Section 3.1 mentions using average pooling to obtain the coarse version of the sparse flow field. Won't that grossly underestimate the flow field due to all the 0 values? Are those ignored somehow? Are the flow values also scaled down by 2 in each downsampling step, so that they are valid offsets for the coarser image size (similar for upsampling)?

Table 1 could be augmented with train/inference timings, parameter count, and number of iterations. The Figure 3 could be removed and that space used for additional results.

In Figure 2 left, it would be helpful to put the x axis ticks exactly where the samples are. There are only 4 sample sizes, and marking e.g. 0 on the x axis is really not informative.

In Figure 2 right, what does the vertical line down the middle indicate? Is that some ideal mask density threshold?

This sentence is hard to parse: "When evaluated on a density of 10%, the network trained on 5% density can even reach a very close EPE on to the network that was optimized on this density (0.28 vs. 0.29)." Does this intend to state that the network trained on 5% density has EPE of 0.29, while the network trained on 10% density has EPE of 0.28, when both are evaluated on 10% density dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a neuroexplicit diffusion model for the optical flow inpainting task. The method combines domain knowledge (explicit PDE-based formulation) with CNN for the task and demonstrates outperforming other baselines such as CNN-based, GAN-based, and probabilistic diffusion baselines.

### Strengths
- Good clarity

  The paper includes sufficient details for understanding the main methods (equations, network architecture details, and implementation details). This helps the reproduction of the method.

- Better accuracy over baselines

  The paper compares its method with several baselines (FlowNetS, WGAIN, EED, and PD) and achieves better accuracy than them.

### Weaknesses
 - Limited evaluation

  The paper evaluates the method only on one synthetic dataset, Sintel. To ensure the method also works on real-world domains, it would be great to evaluate the method on other datasets such as KITTI, Middlebury, etc. Furthermore, the paper doesn't compare with any previous optical flow inpainting methods (eg., Raad et al, "On Anisotropic Optical Flow Inpainting Algorithms"). Achieving better accuracy than baselines is great, but a comparison with previous work would be also necessary to see where the methods stand among the previous works.

  One could also adopt baselines from the depth completion tasks (https://www.cvlibs.net/datasets/kitti/eval_depth.php?benchmark=depth_completion), train their models on the optical flow tasks, and compare with them.

  The method sounds okay, but due to the limited evaluation, it's difficult to judge if the method is really valuable for the community.


- Other applications

  Despite that the proposed method could be generic, the paper demonstrates only optical flow inpainting as an application. Can this method also be applied to other tasks such as depth completion or semantic scene completion? If the paper showed its applicability to such tasks, it could have demonstrated better impact.

### Questions
- Transparency?

  What's the meaning of the transparency of the model in the abstract?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
