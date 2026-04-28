# Coordinate-Aware Modulation for Neural Fields

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Neural fields, mapping low-dimensional input coordinates to corresponding signals, have shown promising results in representing various signals.
Numerous methodologies have been proposed, and techniques employing MLPs and grid representations have achieved substantial success.
MLPs allow compact and high expressibility, yet often suffer from spectral bias and slow convergence speed.
On the other hand, methods using grids are free from spectral bias and achieve fast training speed, however, at the expense of high spatial complexity.
In this work, we propose a novel way for exploiting both MLPs and grid representations in neural fields. 
Unlike the prevalent methods that combine them sequentially (extract features from the grids first and feed them to the MLP), we inject spectral bias-free grid representations into the intermediate features in the MLP.
More specifically, we suggest a Coordinate-Aware Modulation (CAM), which modulates the intermediate features using scale and shift parameters extracted from the grid representations.
This can maintain the strengths of MLPs while mitigating any remaining potential biases, facilitating the rapid learning of high-frequency components. 	
In addition, we empirically found that the feature normalizations, which have not been successful in neural filed literature, proved to be effective when applied in conjunction with the proposed CAM.
Experimental results demonstrate that CAM enhances the performance of neural representation and improves learning stability across a range of signals. 
Especially in the novel view synthesis task, we achieved state-of-the-art performance with the least number of parameters and fast training speed for dynamic scenes and the best performance under 1MB memory for static scenes. 
CAM also outperforms the best-performing video compression methods using neural fields by a large margin. The project page is available at \href{https://maincold2.io/cam/}{https://maincold2.io/cam/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a new architecture for neural fields, i.e mapping low-dimensional input co-ordinates to the signal values, called CAM (co-ordinate aware modulation). The main idea is to modulate intermediate features using scale and shift parameters which are inferred from the low-dimensional input co-ordinates. Authors show that, while regular a regular MLP shows heavy spectral bias, and just grid representation is computationally very expensive, CAM can mitigate the spectral bias learning high frequency components, while also being compact. In addition, CAM facilitates adding normalization layers which improves training stability. Authors empirically show that CAM achieves competitive results image representation, novel view synthesis, and video representation tasks, while being fast and very stable to train.

### Strengths
+ Authors are tackling a very relevant problem, with wide interest to practitioners. 
+ Paper is well written and easy to follow. 
+ Claims in the paper are sounds. I particularly like that the argument about spectral bias and not learning high frequency components is verified empirically in Section 4.3 
+ Experiments are sound and covers a wide range of tasks. Results are strong with performance comparable or exceeding the state of the art.

### Weaknesses
 + While the paper is generally strong, I believe that it lacks certain references which can put the work in a better context. There is a long history of using feature modulation in deep learning. A good example is [FiLM](https://arxiv.org/abs/1709.07871). This is also used for image generation/reconstruction tasks like in [generation](https://arxiv.org/abs/1810.01365), [denoising](https://arxiv.org/pdf/2107.12815.pdf), [image restoration](https://arxiv.org/abs/1904.08118) and [style transfer](https://arxiv.org/abs/1705.06830). Adding these references, and including a discussion around it can put feature modulation in a better context. 

+ Can authors include inference speed/inference memory requirements to put regular MLP methods, grid based method, and CAM in prospective? 

+ The choice of not using the all lower dimensional inputs to infer the scale and shift parameters, but a subset based on the problem is interesting. Have you conducted ablation studies that this is in some way beneficial? 

A bit tangential but:
+ Do you think CAM can benefit decoder MLP for a triplane based representation as well? It would be cool to see some experiments and demonstrate the generality here. 
+ In addition, I think text to 3D is one another domain where the speed and training stability of CAM can benefit quite a lot. If authors can demonstrate a couple of results comparing the training stability and speed using CAM augmented MLP in DreamFusion, that would be a great additon to the paper.

### Questions
See above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduced a coordinate-aware modulation module that combines MLP features and grid representations for neural fields. Unlike the popular methods that chain the features, this new method not only preserves the strengths of MLP but also mitigates the bias problem by leveraging grid-based representation. The authors conducted experiments on tasks in multiple domains and the results demonstrate its capability of modeling high-frequency components and advantages over prevalent neural field features.

### Strengths
- The motivation of the paper was clearly stated 
- The proposed approach is simple yet effective
- The paper is well structured and the idea is easy to follow 
- Experiments are comprehensive. It covers various domains such as images, videos, etc.

### Weaknesses
 - The numbers of the baseline models seem to be from the authors' own implementation, which makes it less appealing

### Questions
- Could you answer the first question I posted in the "Weaknesses" section?

### Soundness
3 good

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
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This work proposes combining grid input and MLP structure at intermediate features level for Neural fields application. This naturally extends MLP-only or grid-only methods, which despite its competitive performance have had downsides, such as not being able to represent high-frequency content or being computationally intensive.

### Strengths
- The biggest strength of CAM is its simplicity and its plug-and-play nature. I believe this will have much far-reaching impact in the Neural fields literature, compared to other highly sophisticated & implementation-heavy frameworks designed to maximize PSNR value at all costs. Similar to how widely Batch/layer-normalization has been used by the entire field.
- Extensive experimentation on diverse tasks and against different baselines add to the credibility of the work.

### Weaknesses
 - While there are no specific weaknesses to point out, I don't think Figure 1 or Figure 2 convey the idea that well. Figure 1 probably will be better served by displaying more detailed mechanism (exammple of x, example of the values for \Gamma, etc.).
- Also giving a brief description of what functional form \Gamma and B take would be informative for readers.

### Questions
Don't have specific questions

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This main contribution of this paper is to use a grid-based approach to provide a scale and bias for the features generated at each layer of an implicit neural network, an approach used to encode any kind of signal. This is in contrast to the typical approach where the grid-based approach provides an input to the implicit neural network. In other words, the proposed approach is: a) use the input coordinate to recover the scale and bias for all layers of the MLP, b) recursively apply each layer of the network, normalize features, apply scale and bias for the appropriate layer. The authors also discuss which subset of input coordinates should be used to define the grid. Other contributions of the paper include the use of the aforementioned feature normalization in implicit neural representation and a comparison to various benchmarks on image encoding and generalization, novel view synthesis in static and dynamic NERF and video compression.

### Strengths
Originality:
* As far as I know, use a grid-based approach for scale/bias in implicit neural representation is new.

Quality:
* Evaluation is performed on several different tasks, with good results, thus I believe the strength of the method is demonstrated.
* The baselines used are generally competitive and recent.

Clarity:
* The paper is well written.

Significance:
* good results on multiple tasks, state-of-the-art in some.

### Weaknesses
Quality:
* I find the use of FFN (Tancik, 2020) as the only baseline in the image task disappointing. While not the most significant experiment of the paper, I think the use of more recent baselines and in particular of other grid-based approaches, for example at least instant-NGP, would make the comparison on images more significant. I also want to add that I find the baselines in the video experiment to be adequate, and arguably the video experiment is more important.

Clarity:
* I might have missed it, but for me, the paper does not sufficiently discuss/explain the reasoning behind the choice of coordinates that are used in the grid to select a scale and bias. For example, the scale/bias depends on the pixel coordinates only for a picture. As far as I understand, scale/bias are thus the same for each channel. But for the video, the scale/bias depend on pixel coordinates, time and channel. I do not understand why the channel becomes important for the video. I noticed the ablation study (Table 6), but it only covers the NERF experiments. This ablation study also does not discuss making the scale/bias depend on both direction and time.
* I do not understand what is the variance represented in Figure 8. Is it the variance between the elements of the input of the last layer of the MLP? 
* I find the notation in equation 1 and subsequent equations a bit confusing. Both $\gamma_n$ and $\beta_n$ takes as input the full batch $X$. This suggests that any element of the vectors $\gamma$ and $\beta$ may depend on the full batch $X$. I suspect this is not the case due to how grid based approaches typically work but I am not sure. Would it make sense to change the notation to $\gamma(X_n;\Gamma)$ or  $\gamma(X^{(n)};\Gamma)$, to be closer to the notation already used in equation 4?

### Questions
* On page 8, the paper states that HM decodes at 10fps using a GPU. I was very surprised, because, as far as I know, HM does not use a GPU. I also could not find a mention of this fact in (Hu et al., 2023). While it is common to compare decoding speed on different hardware (CPU for traditional codec, GPU for ML methods), I think it is misleading to state that HM uses GPU. Could you please comment on/clarify this?
* Could you please comment on the choice of coordinates used in the grid to define scale/bias?
* Could you please provide further explanation about Figure 8?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
