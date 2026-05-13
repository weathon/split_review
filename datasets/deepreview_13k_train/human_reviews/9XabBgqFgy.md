# Unveiling the Backbone-Optimizer Coupling Bias in Visual Representation Learning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
This paper delves into the interplay between vision backbones and optimizers, unvealing an inter-dependent phenomenon termed \textit{\textbf{b}ackbone-\textbf{o}ptimizer \textbf{c}oupling \textbf{b}ias} (BOCB).
We observe that canonical CNNs, such as VGG and ResNet, exhibit a marked co-dependency with SGD families, while recent architectures like ViTs and ConvNeXt share a tight coupling with the adaptive learning rate ones. We further show that BOCB can be introduced by both optimizers and certain backbone designs and may significantly impact the pre-training and downstream fine-tuning of vision models.
Through in-depth empirical analysis, we summarize takeaways on recommended optimizers and insights into robust vision backbone architectures.
We hope this work can inspire the community to question long-held assumptions on backbones and optimizers, stimulate further explorations, and thereby contribute to more robust vision systems.
The source code and models are publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the interaction between popular optimizers and vision backbone architectures. The experiments are conducted over the product of 16 architectures and 20 optimizers on CIFAR-100, ImageNet-1K and COCO.

The authors find that there are notable patterns characterising  which combinations of optimizers + architectures work well together, where some architectures are more sensitive to the choice of optimizer -- which they refer to as “Backbone Optimize Coupling Bias” (BOCB).
From this perspective, the authors thoroughly discuss the various popular vision architectures, based on the design of their components as well as their overall architecture.

### Strengths
* The motivation of the paper is clear, it's important to understand the relationship between vision backbones and optimizers.
* The authors have conducted extensive experiments across a large range of optimizers and vision backbones.
* The experiments reveal many interesting observations about how different architectures perform under different optimizers.
* The authors are releasing the benchmarking results and code, which could allow for further analysis by the community.

### Weaknesses
 * There is no discussion or references to related works studying optimizers for vision backbones and/or transformers. A brief search finds a couple of relevant papers:
- Scaling Vision Transformers, https://arxiv.org/pdf/2106.04560 which discusses e.g. how to adapt Adafactor for ViTs
- How to Fine-Tune Vision Models with SGD, https://arxiv.org/pdf/2211.09359 which studies SGD vs AdamW for finetuning.
- Since most vision backbones are transformer based, other transformer optimizer literature is also relevant -- such as https://arxiv.org/pdf/2002.04745



* In L 197 the authors write "Generally speaking, it is assumed that backbones and optimizers should be unbiased and generalized
components that can be combined freely without significant interdependence". But I don't believe anyone thinks this is the case -- it's well known that optimizer details very often need to adjusted for new architectures.  Furthermore, there are other factors such as model size and overfitting that come to play:
i) a new improved optimizer applied on a an overparameterized architecture may cause it to overfit and hence hurt performance. Why only look at top-1 accuracy but not also training loss?
ii) An architecture may be designed taking an improved optimizer for granted, so why should we expect it to work well with plain old SGD?
ii) A lot of gains can be had from tuning hparams. The authors use the NNI toolbox to pick hparams -- but why not also look at the hparams the authors themselves have proposed for each architecture?

* All of the analysis is of the form "this group of optimizers is working well/poorly for this method or group of methods" but does not really go deeper to explain actually why they perform so differently. E.g. in L260 just tell us that SGD + DeiT-S performs poorly but why? Is it consistent with other findings in the literature? etc

* Some claims made in the paper do not seem to be clearly justified. E.g. 
in L376 the write "The trajectory of vision backbone macro design has significantly sculpted the optimization landscape, progressing through distinct phases that reflect the intricate relationship between network architectural complexity and training challenges  (as illustrated in Figure 1)". I am not sure what exactly the authors are trying to claim here but surely Figure 1 does not illustrate it.
- in L417 they write: "This innovative macro design [of MetaFormer] refines the optimization landscape by harmonizing with
optimizers, leading to reduced BOCB and enhanced performance." How does it "refine the optimization landscape by harmonizing with optimizer"?
- in L445 they write "AttenFormer effectively mitigates BOCB due to its MetaFormer architecture, which incorporates balanced structural designs and residual scaling across stages, enhancing optimization and generalization." How is the "balanced structural design and residual scaling" "enhancing optimization and generalization" here?
- In L456 they write "BOCB in CNNs is often linked to the design of FFN blocks, which are pivotal in models like ConvNeXt" without pointing to any section/table justifying the claim.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work provides an empirical study of the interplay between vision backbones and optimizers. It experiments on common vision datasets like CIFAR-100, ImageNet-1K, and COCO, to document the performance of different architectures (CNN, transformer, etc) and optimizers (SGD-based with momentum, Adam, RMSProp, etc).

### Strengths
* The paper seems to tackle a less discussed aspect about the interplay of different optimizers and architectures
* A comprehensive study on the impact of many hyperparameters
* Great summary of existing architectures and optimizers

### Weaknesses
 * Overall I am not sure the significance of the contribution of this paper is for a conference paper. In my humble opinion, it leans toward a workshop technical report -- certainly empirical study is valuable but I did not find much insights from there.
* The claims and explanations about BOCB are basically hand-waving like section 4; more rigorous derivations of the inductive bias will greatly improve
* All reasoning is empirical and narrows down to the impact of the accuracy. It is not very convincing to get a clear conclusion from such a study. Section 4 is more like reverse-reasoning from the empirical study from the previous sections. This may be acceptable for a paper that proposes a new method that shows better performance and leaves the community to figure out the true reasons. Still, I am not confident about it for a study paper, which I would expect some theoretical induction or in-depth analysis to make it more convincing.

### Questions
What are the authors' thoughts about each of the specific update steps in section 2.2 affecting the performance of different architectures?

### Soundness
3

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
3

### Summary
This paper introduces the concept of Backbone-Optimizer Coupling Bias (BOCB) -- i.e., strong dependencies between neural network backbones and specific optimizers -- which affects performance and generalization. To demonstrate this, a comprehensive benchmark is provided, evaluating various vision backbones and popular optimizers across different tasks.

### Strengths
* I believe the problem statement of the paper is promising. Even though it is known that some modern architectures need specific optimizers to achieve high performance (e.g., ViTs use AdamW by default these days), there are only a few comprehensive studies on the relationship between architectures and optimizers.
* This paper provides results using a wide range of optimizers and architectures, and it reports the average performance over three runs.
* This paper not only reports the phenomenon but also tries to reveal the underlying causes.

### Weaknesses
 * One of the major weaknesses is soundness. I am not fully convinced by some statements in the introduction, as they seem somewhat overstated. As a result, the contributions are somewhat limited.
  * The results suggest that the backbone is not necessarily dependent on a specific optimizer, but rather that certain types of optimizers tend to be generally effective. For example, Table 1, which is one of the main results, seems to simply show that Adam-like optimizers are generally effective. AdaGrad-like optimizers consistently achieve poor results.
  * Likewise, I don’t believe we could derive strong and consistent results from Figures 3 and 4. In these figures, I don’t find significant differences in the variances, except in a few cases. The violin plots and box plots do not show clear separations between different architectures, making it difficult to draw strong conclusions about the coupling bias.
  * In Figure 5, even though AdamW and LAMB show favorable robustness, this may simply indicate that they are inherently robust optimizers, and we cannot strongly conclude that Adam-like optimizers are robust since other optimizers do not achieve significantly good robustness. Also, I am not convinced that Adagrad-like optimizers have heavy BOCB (L371), as RMSProp achieves good BOCB even though it yields poor performance. The claim that Adagrad-like optimizers have heavy BOCB is not well-supported by the data, especially considering the performance of RMSProp.
  * Clarifying the optimizer and backbone design recommendation rules might strengthen the paper. As I mentioned before, the takeaway from the results would be choosing a good optimizer (e.g., AdamW) and a modern backbone, which is a straightforward conclusion.

* The paper does not provide a comprehensive analysis of the architectural components introduced in Section 2 and Figure 1. For example, I would expect a thorough analysis of the influence of architectural choices (e.g., block designs and isotropic vs. hierarchical structures). The discussions in Section 4.1 are useful, but more in-depth analysis would improve the paper. The analysis should delve deeper into how specific architectural choices impact the observed coupling bias, rather than just a general overview.

* I understand conducting experiments on ImageNet might not be easy, but I am not fully convinced that the conclusions would hold on larger datasets. This is because the performance of ViT families highly depends on the training datasets. It is acceptable if we analyze just the behaviors and properties of ViTs on smaller datasets like CIFAR, but the main results depend on the classification accuracy and variances. For example, the problem mentioned in L266 might be resolved in large data regimes. The reliance on smaller datasets raises concerns about the generalizability of the findings to more complex and larger-scale datasets, which are more representative of real-world applications.

* In L322, the paper claims that “while weaker coupling offers more user-friendliness, stronger coupling can potentially lead to better performance and generalization.” However, I couldn’t find strong evidence. I am not convinced that strong coupling is a direct reason for better performance and generalization. The connection between coupling strength and performance is not clearly established, and the claim seems speculative without sufficient empirical support.

* Similarly, in L354, “stage-wise hierarchical and attention mechanisms can more effectively navigate complex optimization landscapes, unlocking superior performance and generalization capabilities.” However, I feel this claim is somewhat contrary to the observation that modern architectures, including attention mechanisms, have BOCB, as it implies that they require specific optimizers to navigate optimization landscapes. Some research, e.g., Park, Namuk, and Songkuk Kim. "How do vision transformers work?" arXiv preprint arXiv:2202.06709 (2022), claims that ViTs have many non-convex points that lead to poor optimization properties. The claim about hierarchical and attention mechanisms is not well-aligned with the observed BOCB, and the paper should address the potential contradictions with existing literature.

In summary, I believe the questions this paper raises are meaningful. However, some statements lack strong evidence, and the novelty is limited as the takeaways are straightforward. Therefore, I lean toward rejecting this manuscript.

* Minor: I couldn’t find Table 3 for a while. Improving the table layout would enhance readability. Also, a more comprehensive analysis of training dynamics would strengthen the paper. It seems that the transfer learning experiments are among the key results, but they are in the appendix.

### Questions
Please refer to the weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
