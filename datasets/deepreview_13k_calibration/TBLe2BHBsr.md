# Dilated convolution neural operator for multiscale partial differential equations

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
This paper introduces a data-driven operator learning method for multiscale partial differential equations, with a particular emphasis on preserving high-frequency information. Drawing inspiration from the representation of multiscale parameterized solutions as a combination of low-rank global bases (such as low-frequency Fourier modes) and localized bases over coarse patches (analogous to dilated convolution), we propose the Dilated Convolutional Neural Operator (DCNO). The DCNO architecture effectively captures both high-frequency and low-frequency features while maintaining a low computational cost through a combination of convolution and Fourier layers. We conduct experiments to evaluate the performance of DCNO on various datasets, including the multiscale elliptic equation, its inverse problem, Navier-Stokes equation, and Helmholtz equation. We show that DCNO strikes an optimal balance between accuracy and computational cost and offers a promising solution for multiscale operator learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduced DCNO (Dilated Convolution Neural Operator) as an effective approach for learning operators within multiscale partial differential equations (PDEs). The DCNO model adopted an Encode-Process-Decode architecture, starting with an encoder that employed a patch embedding function, which utilized a convolutional neural network (CNN) to elevate the input into a higher-dimensional feature space. The processor section alternated between Fourier layers (F layers) and Convolution layers (C layers), where F layers approximated low-frequency components, and C layers extracted high-frequency features. An ablation study was conducted to analyze the influence of these layers on model performance. Extensive experiments confirmed the effectiveness of DCNO in addressing multiscale PDEs, showcasing its superior performance and potential for various applications.

### Strengths
This practical applicability increases the significance of the research for industries and academic communities.

### Weaknesses
The framework seems to be an extension of a simple encoder-decoder architecture, with its modules combining F layers and C layers.

The contribution of this work lacks clarity, particularly in terms of the proposed decoder, which bears similarities to Cao (2021). It would be valuable for the authors to explicitly articulate the distinctions between these two approaches.

It is worth noting that dilated convolution is a well-established technology, and the novelty of the proposed Dilated Convolution Neural Operator (DCNO) seems somewhat limited. Authors are encouraged to provide a more robust justification for the uniqueness and innovation of their approach.

### Questions
The paper mentions DCNO as a novel architecture, but further clarification is needed to establish its novelty. The authors should explicitly detail how DCNO differs from existing approaches and what specific innovation it brings to the field.

The authors briefly mention similarities between their proposed decoder and a prior work by Cao (2021). It's crucial to provide a comprehensive comparison, highlighting the key differences and improvements in DCNO, to distinguish it from existing methods.

The absence of C layers in the decoder is notable, and the authors should explain this design choice. Providing a clear rationale for this decision would enhance the understanding of the model's architecture.

The inclusion of three convolutional neural networks in the convolution layer should be justified. The authors should elaborate on the reasoning behind this choice and discuss its impact on the model's performance and efficiency.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a neural operator architecture (DNCO), that relies on the combination of fourier layers and dilated convolution layers. The former come from the original FNO architecture with some improvements, while the latter are inspired by works from *Holschneider et al.* and *Stachenfeld et al*. DNCO is compared to different baselines, mainly on the multiscale elliptic equations and the Navier-Stokes equations experiment from *Li et al*. Furthermore, experiments on the Helmholtz equations and a different case of the Navier-Stokes equations are contained in the appendix.

### Strengths
In my opinion, this work has three core strengths:

**S1:** Related work and similar methods are reviewed thoroughly, making it easy to contextualize this work, even for less experienced readers.

**S2:** The overall presentation is clear, easy to follow, and sufficient details are provided, especially in the methodology section.

**S3:** The paper considers a broad range of experiments across physical systems and different baseline architectures. The results are supplemented with additional ablations in the appendix.

In addition, source code is provided for this submission, which should help to improve the reproducibility of the shown results. However, I did neither investigate nor run the source code.

### Weaknesses
Apart from modifications to the FNO architecture, this paper has limited novelty and insights. While improvements of DCNO compared to the baselines appear across cases, it is not clear how well the parameters of each baseline are tuned. Especially so, as neither training details for the baselines and nor descriptions how key parameters were selected are included. In addition, I see the following problems:

### Formatting
The page formatting, page margins and/or the aspect ratio of this paper are clearly different from other submissions. This is especially noticeable due the amount of whitespace under the page number. But since most other formatting aspects are visible reasonable, I am not sure if this counts as a template/formatting violation.

### Evaluations
**E1:**
Why is only DCNO trained with the weighted loss, as it seems to be a highly important aspect in terms of performance (see Appendix B.3.1 and D). In my opinion, a fair evaluation would be to train all baseline methods with the weighted loss as well. Even though DCNO works better than the baselines using a simple L2 loss, this might not be the case for the weighted loss. 

**E2:**
I think one of the core arguments of this paper, that DCNO performs better than previous methods in the high-frequency domain due to the dilated convolution layers, is not supported by the shown results. Fig. 1b only compares to FNO which is known to perform poorly on high frequencies. When considering other methods in Fig. A.1, DCNO only performs on par. To me, Fig. 1c is almost misleading, as the DCNO shown here was trained with the weighted loss that specifically focuses on high frequencies, while FNO in Fig. 1d was not. DCNO without this loss results in a significantly worse frequency behavior, as shown in Fig. C.1. Arguably, other baselines (especially MWT or HANO) even perform slightly better than the shown DCNO result in that figure, as they have smaller errors in the more crucial lower frequencies, indicated by the wider dark-blue area reaching over $10*\pi$. Another point regarding this issue is that a model with no dilations in the convolutions seems to result in a similar performance to DCNO (as shown in Tab. 4). 

In my opinion, performing additional evaluations in this direction would be a highly necessary improvement. One option would be frequency analyses on the Navier-Stokes cases, similar to established techniques from that domain (see e.g. *“Turbulent flows”*, Pope, Cambridge University Press). Such evaluations would clearly show if DCNO exhibits fundamentally better high-frequency behavior compared to the other baselines.

**E3:**
Tab. 4 and Tab. 7 seem to show that models are underparameterized for the investigated learning tasks, as removing layers hurts performance and adding parameters substantially increases performance. To me, this indicates that other baselines such as dilated Resnets could perform better with a higher parameter count as well. As such, it would be nice to see how key parameters for the different baselines were selected, and if the performance could be improved when changing them.

**E4 (less crucial):**
If I interpret Appendix B.1 correctly, all results are computed on test sets that are randomly split from the training data. For PDE simulations, generalization to new parameters and initial conditions is a highly desirable property. Evaluations applying trained models to new parameter ranges, for example different Reynolds numbers in the fluid flow cases would be interesting to see.

**E5 (less crucial):**
As the data samples in the Navier-Stokes case are downsampled from the generation resolution of $256 \times 256$ to $64 \times 64$, does this not average out the effect of using higher Reynolds numbers? To that end it would also be interesting to see visualizations and corresponding predictions at different Reynolds numbers from this data set.

### Presentation:
There are some minor presentation issues listed below, and the structure of the appendix could be improved.

**Minor issues:**
- “allows us to selectively skip” → allows for selectively skipping (3. paragraph of Introduction)
- “convoluted” → convolved (several times in C layers description)
- “which maps the vorticity from time 0 to T0 to the vorticity from time T0 to a later time T” (unclear, Section 4.2)
- “Each convolution layer includes three convolutional neural networks, each” (not very clear, C layers description)
- Several citations lack publication information, e.g. *Cai et al., 2019,* *Freese et al., 2021*, *Liu et al. 2023*
- Citation format is inconsistent, e.g. multiple citations from arxiv are cited differently (arXiv e-prints, ArXiv, CoRR, …)
- Fig. 4.1: add log scaling to colorbar
- Fig. 4.2: add log scaling to plot axis description
- Subplots are plotted inconsistently across figures

### Questions
**Q1:**
Intuitively, dilated convolutions capture non-local, long-range, low frequency components due to the large receptive field that skips directly neighboring values. However, here the authors argue the opposite, which is quite counter-intuitive to me. Is there an intuition to this argumentation? Especially so, as removing dilations seems to result in very similar performance for the DCNO model (see Tab. 4), and the majority of the benefits in the frequency domain appear to come from the weighted loss (see Fig. C.1 as discussed above).

**Q2:**
Why does DCNO(F layers only) in Tab. 5 perform so much better than FNO (from Tab. 1)? Is this just due to better parameter tuning of the FNO layers?

**Q3:**
What is $s=128$, $s=256$, and $s=512$ in Tab. 1? I assume it might be the data resolution, but I did not explicit find a discussion of this aspect.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper targets the solution of PDEs with a modified network architecture. The paper takes a neural operator approach, and builds on existing work, the popular fourier operators and dilated convolutional networks. The authors propose a specifc arrangement of fournier and conv blocks, which, as they claim, increases performance. In addition, a custom loss is introduced that requires a manual balancing of certain frequencies. The results are evaluated on two test sets, Darcy and NS, where the first one (the steady-state Darcy flows) is presented with variations, while the NS case is transient. 

A variety of baselines, from relatively simple nets to more modern attentian based ones, are compared. Unfortunately, the networks seem to be from single training runs and use varying parameter counts, but given this state, the authors claim improvements in accuracy over the best performing baseline architectures.

### Strengths
The paper targets an important goal, namely the accurate and resource-aware prediction of PDE solutions. Handling this in a manner that takes into account multiple scales is an attractive goal, which, however, did not play a central role in the paper despite the title. Most modern architectures (apart maybe from very simple ResNets) inherently work on multiple scales, and the manual scale-separation and weighting in the loss seems to be problem specific.

It's also nice to see that the authors target an inverse problem, in addition to the regular "prediction" tasks.

### Weaknesses
Nonetheless, the datasets and tasks seem relatively simple, and are presented without much detail. E.g., no qualitative evaluations of the Darcy cases are presented, and its left unclear how the averaged MSE quantities influence the obtained solutions. 

A central weakness that I see with this submission is the widely varying parameter count in the comparisons. It is well established that the size, i.e. parameter count, is one of the most influential factors determining NN performance. This is fine for most other networks, e.g., the U-NO network seems to have almost 10x parameters, and still shows a worse performance. Hence, I don't expect this to change much when a similar parameter count is used. It nonetheless would be a fairer comparison -- the large network could show some forms of overfitting. Most importantly, though, the dil-ResNets for some reason are given much fewer weights. I think it would be important to increase the number of features to obtain a parameter count on the level of the DCNO versions. They should do significantly better then, and it's not clear whether they would outperform the proposed approach.

A general question that is left open by the paper is that FNO and dil-ResNet by themselves do worse than the DCNO. Potentially, there could be an ingredient in the combined architecture that yields the "best of both worlds", but the evaluations in the paper leave this point open. If the authors could shed light on where the advantages come from, maybe with a careful ablation or additional analysis, I think this paper would be much more convincing. In combination with the relatively narrow range of experiments and sparse evaluation, I would be hesitant to try out the proposed architecture.

### Questions
- Most importantly, I am wondering how much is to be gained from the proposed architecture. Once the dil-ResNet is given the same number of parameters, and trained with the same loss, how does the performance compare to the proposed architecture?

- How many models were evaluated each time? Training deep nets is inherently stochastic, and the performance of the trained models varies. What are mean and standard deviation across multiple runs?

- As the approach targets multi-scale PDEs, and employs a scale separation in the proposed loss, have the authors evaluated frequency based evaluations and metrics? 

- Where do the time ranges used for the different Reynolds numbers come from? The difficulty seems to "jump" up and down while increasing Re, and details are missing about how these tests were set up. Are these single test sequences, or were results averaged over multiple sequences to obtain stable results?

-----

I want to acknowledge the updates made by the authors and their answers to my questions. I think their work has potential, but for a fairly fundamental architectural advance it's still not fully convincing (judging from my concerns and those of the other reviewers). So I will keep my score and recommendation leaning towards the negative side, but encourage the authors to provide a more thorough "package" that makes clear where (and ideally why) the method works, and potentially also where it stops working.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
