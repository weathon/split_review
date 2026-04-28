# Sparse-to-Sparse Training of Diffusion Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Diffusion models (DMs) are a powerful type of generative models that have achieved state-of-the-art results in various image synthesis tasks and have shown  potential in other domains, such as natural language processing and temporal data modeling. Despite their stable training dynamics and ability to produce diverse high-quality samples, DMs are notorious for requiring significant computational resources, both in the training and inference stages. Previous work has focused mostly on increasing the efficiency of model inference. This paper introduces, for the first time, the paradigm of sparse-to-sparse training to DMs, with the aim of improving both training and inference efficiency. We focus on unconditional generation and train sparse DMs from scratch (Latent Diffusion and ChiroDiff) on six datasets using three different methods (Static-DM, RigL-DM, and MagRan-DM) to study the effect of sparsity in model performance. Our experiments show that sparse DMs are able to match and sometimes outperform their Dense counterparts, while substantially reducing the number of trainable parameters and FLOPs. We also identify safe and effective values to perform sparse-to-sparse training of DMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes the use of sparse-to-sparse pretraining for diffusion models. These techniques (specifically those known as _unstructured_ sparsity, where the vertices remain fixed but only edges/connections/weights between neurons are taken to be a subset of a dense network) have shown in prior work that they can boost the performance of a wide variety of deep learning models while theoretically resulting in less FLOPs for both training and inference. This paper applies three different sparse-to-sparse pretraining methods to various diffusion models, showing a slight boost in FID scores on various image datasets while reducing the number of FLOPs.

### Strengths
- The paper is well-written and is easy to follow.
- The results presented improve over the dense baselines in the majority of datasets/models chosen for experiments.
- Important explorations are included, such as studying the effect of different percentages of network sparsity and different numbers of denoising steps for inference.
- Experiments are conducted on various models and datasets, improving confidence on the results.

### Weaknesses
The biggest weakness of this paper is that there is virtually nothing new happening. As the paper itself observes in its literature review, prior work has already shown that the sparsity methods explored have already been shown to achieve similar results in generative models, so the results are not surprising either. The contribution in this paper therefore feels very limited: it is showing that using this on diffusion models can result in a small quality boost and (theoretical / hardware-dependent) FLOP reduction. The techniques explored are all from prior work, with seemingly no additional technical challenges on the way to apply them to diffusion models. Please correct me if I am wrong on this (and if so, this would definitely be an important discussion to include in the paper).

It should also be noted that other methods exist where the goal is also FLOP reduction without compromising quality. For example, masked autoencoders (MAE), and more recent work like MicroDiT applying the ideas from MAE to diffusion models, explore dropping out sequence elements entirely from transformer architectures, which can result in immense computational savings in practice _with current hardware_. The paper needs to better motivate why exploring these specific methods is important, given that the motivation and goals are the same as other methods that can better take advantage / live up to the constraints of modern hardware. In particular, sequence dropout has proven to virtually sacrifice no quality with very drastic dropout rates on image and video domains.

While the improvement of FID scores is certainly a strength of the work given that connections are being pruned, this is insufficient to demonstrate the effectiveness of any method: qualitative comparisons are key, given that the connection between FID and sample quality is not a guarantee (especially when differences are very small). This is an easy fix; the authors can provide many more samples, side-by-side with the baseline models. It is even possible to obtain extremely similar samples, simply via deterministic training and sampling with the same random seed to study the actual results more carefully. 

Finally, while the quantity of experiments, datasets and models is appreciated by the reviewer, one less fatal but nonwithstanding a weakness, is that the datasets utilized are of very narrow domain and results may not transfer to larger settings, which are of key interest to the community. One potential way to improve this would be to show positive results on a traditional dataset that is much more diverse and challening, such as ImageNet (as opposed to the much smaller Imagenette used in the paper). It is more typical for positive findings on challenging benchmarks like ImageNet to transfer to larger-scale tasks and models, while it is very common for results in small, narrow datasets like CIFAR10 and the datasets used in this work to not work in more interesting settings.

### Questions
Why are the authors specifically interested in these sparsity methods compared to other existing techniques in the literature that can *actually* reduce FLOP count and properly utilize hardware? The fixation on these specific sparse-to-sparse methods seems very poorly motivated, but I would welcome clarification on this.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper integrated 2 Diffusion Models with 3 Sparse Training methods respectively, with experiments on many datasets to verify the combination of these two things is OK (reducing FLOPs while maintaining good performance, some even outperforming the dense models). This may be helpful for training time, memory, and computational savings of DMs in the future.

### Strengths
1. The combination of Sparse Training and DMs is proven to be effective, which can be used in the future efficient training of regular DMs without affecting other components of training and inference.
2. Experiments are conducted on many datasets together with extensive analysis, making the methods convincing.
3. The writing logic is great from my point of view, making readers easy to follow.
4. The content is rigorous, e.g., good to point out the hardware limitation for sparse matrix operation (Line 56).

### Weaknesses
Majors:
1. The biggest issue is that sparse training and DMs seem not to be coupled: there's no strong desire for me to think the combination of these two is fantastic or compatible naturally, and I also didn't see any apparent problems that would prevent the two from combining easily. It seems like this paper simply uses "Sparse Training + DMs = Sparse DMs",  in which both Sparse Training and DMs are ready-made without innovation and without extra tricks in the combination process. As a result, although the paper has some contributions (of experiments and verification), it has NO core novelty.
2. I don't think the methods take advantage of the unique characteristics of DMs itself. After all, the denoising phase of DMs parameterizes a neural network $p_{\theta}$ to approximate the denoising process $q(x_{t-1} | x_t)$, so the DMs can be regarded as "noising process + network backbone (for fitting denoising process)". The paper uses Sparse Training in denoising backbones, however the backbones may have been verified of the combination with Sparse Training or pruning [1] [2].

Minors:
1. Refs (hyperlinks) can be changed to a different color or use a box, just like most other articles did. It's hard for me to follow the real contents with all the black letters.
2. It seems that the page number of the first page can be incorrectly hyperlinked.
3. More introduction should be made to Latent Diffusion and ChiroDiff.

### Questions
1. Why choose these two DMs? AFAIK, ChiroDiff is not a well-known model. 
2. Have experiments been done on other DMs (backbones) to test the generalization? What affects the combination of the two may not be different datasets or different generative tasks, but different network backbone architecture (e.g., U-Net v.s. Bidirectional GRU encoder). More analysis into this?
3. For Tables 1, 2, and 4, are there criteria or reasons for choosing these specific sparsity ratios $S$? It may be necessary to supplement the ablation study of sparsity ratios $S$ and pruning rate $p$ of the three methods.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To enhance the efficiency of both training and sampling of DMs, the paper employs a sparse-to-sparse training technique to develop a lightweight model backbone that can achieve performance comparable to its denser counterpart. Since previous methods primarily focus on the efficiency of sampling in DMs, this paper demonstrates significant advantages by optimizing the diffusion framework for both fast training and sampling speeds. To achieve this goal, this paper proposes two strategies—static and dynamic training—to optimize two state-of-the-art models. Experimental results demonstrate the effectiveness of the proposed sparse-to-sparse training method.

### Strengths
1. This paper investigates a challenging problem in the diffusion framework, as current state-of-the-art methods all require large model backbones to maintain significant generative performance. Therefore, using a lightweight model to achieve comparable modeling ability is meaningful for the generative community.

2. The experimental results are compelling, as the proposed framework employs a model with small capacity parameters to achieve slightly better performance, highlighting its great potential for reducing sampling latency.

3. The proposed two training strategies are effective for training the lightweight model backbone, as models optimized with these strategies can match or even surpass the performance of their dense counterparts.

4. This paper is easy to follow and the concept idea for the main framework is clearly presented.

### Weaknesses
1. The proposed framework appears to be an incremental application with limited novelty. Furthermore, this paper seems to rely on established sparse-to-sparse strategies for optimization without any careful design. The application of these strategies to diffusion models lacks a clear motivation beyond simply attempting to reduce computational cost. There is no discussion on how the specific properties of diffusion models might interact with the chosen sparsity techniques, such as the impact on the reverse diffusion process or the stability of the training dynamics. The paper does not explore alternative sparse training methods or justify why the chosen methods are the most appropriate for this task.

2. The proposed method is not theoretically guaranteed, which may result in performance variability. The paper lacks any theoretical analysis of the convergence properties of the sparse training methods in the context of diffusion models. It is unclear whether the observed performance gains are consistent across different random seeds or whether they are sensitive to the specific hyperparameters used for training. The absence of theoretical underpinnings makes it difficult to predict the behavior of the method in different settings or with different model architectures.

3. The ablation studies are lacking.  The validity of the model would be better established with more experimental results provided. The paper does not explore the impact of different sparsity levels on the performance of the diffusion models. It is unclear how the performance varies as the sparsity rate is changed, and whether there is an optimal sparsity level for each model. Furthermore, the paper does not investigate the sensitivity of the method to the choice of pruning strategy or the impact of different initialization schemes on the final performance. The lack of these ablation studies makes it difficult to assess the robustness of the proposed framework.

4. It is suggested that the format of the references be made uniform, as there are discrepancies between different sections.

### Questions
1. Is there any explanation regarding the design of the sparsity rates for training diffusion models, which appear to be predefined without any intuitive understanding based on specific concepts related to the models? Is it possible to design an adaptive sparsity schedule?

2. How many GPUs were used in the training process for different DMs? Providing more details about the training settings would greatly enhance the confidence in the proposed framework.

3. For a given DM, how should the decision be made regarding the training strategy—whether to use static sparsity or dynamic sparsity?

4. Can you provide some experimental results on the text-to-image task, which is one of the most important practical applications of diffusion models?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a weight pruning-based sparse-to-sparse Diffusion Model (DM) training method using both **static** and **dynamic** sparse pruning techniques. Through experiments on latent and Chiro Diffusion Models, the paper demonstrates that sparse training can achieve similar or improved performance compared to dense training methods while reducing the number of parameters and FLOPs.

### Strengths
1. The motivation for the paper is very clear: the high computational cost of training DMs, which drives the proposal of a prune-based DM training method.
2. Sparse training is applied across a diverse range of datasets and models, showcasing its versatility.
3. The experimental results are clearly presented, showing how network sparsity and pruning ratio affect the performance, providing valuable insights into hyperparameter tuning.

### Weaknesses
1. Lack of experiments on full dataset training
    - This paper only uses a portion of the CelebA-HQ and LSUN-Bedrooms datasets for the experiments. However, I believe that the performance of sparse training may decrease on larger datasets due to the reduced expressive power of the model caused by pruning. To fully evaluate the effectiveness of sparse training methods, experiments on larger datasets such as the full ImageNet or the entire LSUN-Bedrooms dataset are needed. Although Appendix C presents results from training on the full CelebA-HQ dataset, with only 30,000 images in total, CelebA-HQ is not large enough to alleviate these concerns. The use of subsets raises questions about the generalizability of the findings to more extensive datasets, where the impact of sparsity might be more pronounced due to the increased complexity and diversity of the data.
2. Lack of evaluation metrics
    - The authors have presented the FID score as the evaluation metric, but relying solely on the FID score to evaluate a Diffusion Model (DM) seems risky. It would be better to additionally present metrics such as the Inception Score (IS) proposed in the Latent Diffusion Model paper. The absence of IS makes it difficult to compare the results with other works that use this metric, potentially limiting the impact of the research. Furthermore, relying on a single metric like FID can obscure potential weaknesses in the generated samples that might be captured by other metrics.
3. Dependence on dataset, method, and hyperparameters
    - In Figure 2, only a few methods and sparse rates outperform dense training in CelebA-HQ and Imagenette. Due to the long search time for optimal settings, the reduction in training time mentioned by the authors seems insignificant. The sensitivity to hyperparameters and the limited number of configurations that outperform dense training suggest that the proposed method may not be robust or easily applicable in practice. The need for extensive hyperparameter tuning undermines the practical benefits of the method.
    - Although ChiroDiff shows performance improvements with the QuickDraw dataset, it is hard to say that there are meaningful improvements in performance for KanjiVG and VMNIST. Sparse training lacks robustness across different datasets. The inconsistent performance across different datasets raises concerns about the general applicability of the proposed method. The lack of a clear understanding of why the method works well on some datasets but not others limits its practical use.
4. Lack of analysis
    - In Section 4.1, line 376, it is mentioned that, unlike existing supervised learning and GAN models, the DM using the SST method outperforms the DST method. Additional analysis is needed to explain why this different trend is observed. The lack of a clear explanation for this divergence from established trends in other domains limits the understanding of the underlying mechanisms of the proposed method. This difference could be crucial for further research and development in this area.
    - In Table 2, performance is good for QuickDraw but poor for KanjiVG and VMNIST. An analysis of the reasons behind this discrepancy would be useful. The lack of analysis on the performance discrepancy across datasets leaves the reader with unanswered questions about the method's behavior and limitations.
5. Lack of novelty
    - Without introducing new concepts or ideas, the paper applies the existing sparse-to-sparse training method from supervised learning to Diffusion Models. It would be better to propose a new method optimized for Diffusion Models. The application of existing methods without significant modifications or novel insights reduces the overall impact of the paper. The lack of a novel approach tailored to the unique characteristics of diffusion models limits the contribution of the work.
    - The variance of FID scores in Table 1 is overall too large, and the reduction in FLOPS is not significant for Bedrooms and Imagenette. The high variance in FID scores and the limited reduction in FLOPS raise concerns about the practical benefits of the proposed method. The lack of significant improvements in both performance and efficiency undermines the motivation for using sparse training in diffusion models.
    - The efficiency gained from reducing inference speed via FLOPS reduction is dependent on hardware.
    - Overall, the time taken to search for methods and hyperparameters seems too long compared to the performance improvements. Proposing methods to reduce the search time would be helpful.
    - In Section 4.3, line 515, a speed-up of 0.57x is mentioned, but it is unclear whether GPU inference time is improved.

### Questions
- Is sparse training effective on larger datasets such as the full LSUN-Bedrooms dataset or ImageNet1k, which are larger than CelebA-HQ?
- Is there a specific reason for using only the FID score as the evaluation metric? If not, it would be helpful to also include the Inception Score (IS).
- Could you explain why performance is strong only for QuickDraw in Table 2, but not for KanjiVG and VMNIST? Is there a particular characteristic of the datasets that leads to this?
- Have you tried using structured sparsity, which removes entire layers, to reduce inference time?
- In Section 4.3, line 515, could you clarify whether GPU inference speed actually improves by 0.57x as mentioned? Could you provide papers or resources that demonstrate that reducing FLOPS leads to improved inference speed on hardware?
- For Table 1, would it be possible to conduct experiments that reduce the standard deviation to below 3.0 through hyperparameter tuning on the Bedrooms and Imagenette datasets? The mean + standard deviation for sparse training (for example, 28.79 + 12.65 = 41.44 for Bedrooms Static-DM) is consistently higher than the mean for dense training (31.09 for Bedrooms Dense).
- Do you have any insights on how to effectively tune hyperparameters such as network sparsity, exploration frequency, pruning rate, and sparse method, beyond random search or grid search?

### Soundness
2

### Presentation
3

### Contribution
1
