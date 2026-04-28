# Foundation Models Secretly Understand Neural Network Weights: Enhancing Hypernetwork Architectures with Foundation Models

- Decision: Accept
- Avg Score: 5.50
- Scores: 3, 6, 5, 8

## Abstract
Large pre-trained models, or foundation models, have shown impressive performance when adapted to a variety of downstream tasks, often out-performing specialized models. Hypernetworks, neural networks that generate some or all of the parameters of another neural network, have become an increasingly important technique for conditioning and generalizing implicit neural representations (INRs), which represent signals or objects such as audio or 3D shapes using a neural network. However, despite the potential benefits of incorporating foundation models in hypernetwork methods, this research direction has not been investigated, likely due to the dissimilarity of the weight generation task with other visual tasks. To address this gap, we (1) show how foundation models can improve hypernetworks with Transformer-based architectures, (2) provide an empirical analysis of the benefits of foundation models for hypernetworks through the lens of the generalizable INR task, showing that leveraging foundation models improves performance, generalizability, and data efficiency across a variety of algorithms and modalities. We also provide further analysis in examining the design space of foundation model-based hypernetworks, including examining the choice of foundation models, algorithms, and the effect of scaling foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a novel method of using visual foundation models as part of a hyper-network to prediction the weights of an MLP to perform a task. The authors evaluate their method on a novel viewpoint reconstruction task and an audio reconstruction tasks using three methods: random initialization, fine-tuning, and promp-tuning. They demonstrate a small performance improvement using a foundation model and then fine-tuning or prompt-tuning over random initialization.

### Strengths
- The authors have selected and interesting question to investigate and have clearly describe their approach (aside from lacking INR model details)
- This work demonstrates a performance improvement of using foundation model weights over a random baseline.
- The overall architecture proposed is simple and generalizable to any foundation model or task.

### Weaknesses
 - The overall performance improvement is small.
- The authors chose tasks that are very difficult to evaluate and only two tasks were evaluated.
- The paper lacks details about the exact architecture and scale of the INR network which seems like an import parameter that would be interesting to vary.
- The evaluation lacks other baseline methods of training the INR network such as distillation. Although not the goal of this paper, evaluation of other training methods seems important for contextualizing the performance of this method.

### Questions
- What is the exact architecture and number of parameters in the INR network?

- Why did the authors chose generative tasks where the available evaluation metrics such as PSNR, SSIM, LPIPS, and FID are a poor proxy measurement for model performance on the task? Why not use image classification, segmentation, depth prediction, or many other tasks that are easier to evaluate and have more model baselines to compare against?

- How does the performance achieved by the predicted INR weights from this method compare to distilling a foundation model fine-tuned for these tasks into the INR network?

### Soundness
2

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
The paper proposes to leverage pretrained foundation models for enhancing hypernetworks which are trained to generate weights of implicit neural networks, i.e. networks whose parameters are a representation of a single data sample.  The approach leverages transformer based architectures to learn a (modulated) set of weights vectors that will correspond to the implicit representation of each sample. The method is evaluated on mainly on image data, with an additional experiment on audio data, respectively in a novel image synthesis task and audio reconstruction. The experimental section tests varies aspects and benefits of incorporating foundation models from performance, to sample efficiency, generalization to unseen class and parameter efficiency.

### Strengths
- The idea is simple and effective. Leveraging information stored in pretend foudnation models for enhancing implicit neural representations networks is mostly a novel idea to the best of my knowledge and it may benefits future research in the area. 

- The experimental section is quite broad  and comprehensive: it shows the benefits of incorporating foundation models hyper networks to learn implicit representations from the point of view of:  performance, sample complexity, parameter efficiency and multi modality. This seems to suggest that in general pretrained vision models should be incorporated  in learning INRs and pave the way to new applications in this direction. 

- In particular, the results by just finetuning the heads is quite impressive, pointing at the fact that the connection between weights and features should be further inspected in future works. 

- The paper writing is overall clear.

### Weaknesses
 - The architecture and training procedure of the model although it builds on previous work could be explained better in the paper, for See related questions in the question section 

- On the experiment on audio data the model doesn't seem to benefit much form the foundation model. Do the authors have an intuition of why? Could it be related with the complexity of the task or to the fact that audio FM are less expressive in general than Vision ones?

- It would be interesting to see some results on a different task/ dataset on image data. 

- The following work should be included and discussed in the related works section, as it also explores the relation between features extracted and performance of implicit neural networks: 

     - Ye, J., Wang, N., & Wang, X. (2023). Featurenerf: Learning generalizable nerfs by distilling foundation models. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 8962-8973

Similarly, yet fare as line of works the following works which distill information in CLIP embeddings to learn better Implicit representations should be discussed: 

- Wang, Can, et al. "Clip-nerf: Text-and-image driven manipulation of neural radiance fields." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022

- Liao, Guibiao, et al. "Ov-nerf: Open-vocabulary neural radiance fields with vision and language foundation models for 3d semantic understanding." arXiv,  2024


*Minor*

- Visualization quality of Figure 4 could be improved, for example by putting box to zoom on details.

- I spotted the following typos: 

    - Figure 3 caption: "leads generally leads" -> "generally leads"
    - Figure 4 caption: "baselin" -> "baseline" 
    - Line 174: "using of" -> "of using"
    - Lin e 408: "descreased" -> "decreased"

### Questions
- Integration of FM into existing methods :
    -  How is the architecture and training strategy related to the method proposed? Is the model still trained with meta-learning? 
    -  For the experiments in Table 4, again how is the FM included in the methods specifically? Is there any adaptation to the architecture or training strategy? 

- Do the authors have an intuition on why the FID metric seems to grow for foundation models based models in Figure 2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
There are many applications/tasks where large pre-trained (foundation) models can be potentially helpful, but the possibility has not been explored. The authors identify one of these being generalizable INRs using hypernetworks (hypernets).

The paper proposes to use transformer-based foundation models within an architecture based on Trans-INR. The authors show that the model can be trained either through full fine-tuning or through a prompt-tuning-based approach that keeps the foundation model encoder weights frozen. In addition to the input patches as input to the transformer, the authors add learnable weight tokens corresponding to the network weights to be generated at the output.

The authors show that hypernets with foundation model backbones show improved generalization to seen and unseen classes, and improved data and parameter efficiency, compared to hypernets trained from scratch. They note that foundation model choice is important, claiming that models that have learned a good global representation (as opposed to local representations like with MAE) perform better. The authors also show that the scaling benefits of larger foundation models transfer to the generalizable INR task through their incorporation in hypernets. Finally, the authors demonstrate that their idea is robust across two other hypernet algorithms based on Trans-INR and between two modalities (vision and audio).

### Strengths
- The idea is simple and new to the specific task of generalizable INRs using hypernets.
- The authors conduct an extensive empirical evaluation to support their claims and show that the gains are reproduced across algorithms and modalities.
- Most of the paper is easy to follow.

### Weaknesses
Primary:
- The technical contribution of this paper is replacing a transformer component that has previously been trained from scratch with a pre-trained foundation model, which is not original and is now a fairly standard recipe. While the application to hypernetworks is novel, the core idea of leveraging pre-trained models is not, and the paper does not sufficiently explore the nuances of this transfer. The paper lacks a detailed analysis of how the pre-trained representations are adapted to the hypernetwork setting, specifically what properties of the foundation model are beneficial and how the linear head is sufficient to bridge the gap between image/audio representations and network weights. This raises questions about the true novelty of the approach beyond a straightforward application of existing techniques.

Secondary:
- It is confusing that in Table 2, random initialization outperforms foundation models on LPIPS in 2/3 settings, but fine-tuning performs much better on the remaining setting. The paper does not provide an explanation for this inconsistency, nor does it analyze the potential reasons for the random initialization performing better in some cases. This lack of analysis undermines the claims about the superiority of foundation models, as it suggests that the benefits are not consistent across all scenarios and metrics. Further investigation is needed to understand the conditions under which foundation models offer a clear advantage.
- It is not clear what "positional encoding" refers to in Figure 1 and the related discussion. In the context of transformers, this term denotes adding position information to the transformer inputs, which is not the case here. It is also hard to see if the linear heads underneath are labeled positional encodings or the $\gamma(\mathbf{v})$ block to its right. Most likely, this refers to the MLP's output, but there is some ambiguity. The paper should clarify what this term refers to and provide a more detailed explanation of the architecture, including the role of the $\gamma(\mathbf{v})$ block and its relation to the linear heads.
- There is no discussion of training hyperparameters used for the experiments. Are all of these the same as what the base frameworks used? The paper should provide a comprehensive description of the training process, including the specific hyperparameters used for each experiment, and justify the choices made. This information is crucial for reproducibility and for understanding the sensitivity of the results to different training settings.

Minor (no impact on score):
- It is unclear what type of norm is considered around line 140 (context: "normalizes the weights to have norm 1"). It is likely L2-norm based on Trans-INR, but it should be specified here.
- Section 3.1: In the first line, "we experiments" -> "we experiment".
- Around line 175: "Instead using of MSE" -> "Instead using MSE".
- Last sentence in the abstract is too long (the entire point 2).

### Questions
Have you considered deviations from the Trans-INR architecture? Are there any components that become unnecessary or even detrimental with the addition of foundation models (as a motivating example that is not directly related, strong regularization that helps at smaller scales can limit performance gains at larger scales)?

### Soundness
4

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
3

### Summary
This paper investigates the utility of foundation models as backbones for hypernetworks, that is, neural networks which generate the weights for INRs. The authors show that fine-tuning (or freezing and prompt-tuning) foundation models such as DINO and CLIP can indeed lead to hypernetworks that outperform the same architectures trained from scratch.

### Strengths
This paper investigates a logical idea, is clearly written and offers a very thorough analysis, in the sense that many questions one might have about the proposed approach are investigated. For example, the authors investigate different foundation models as backbones, compare different fine-tuning methods and hypernetwork algorithms, as well as different tasks. I can imagine that using foundation models as starting points for training INRs will become the standard procedure in certain visual domains.

### Weaknesses
* As somebody unfamiliar with the NVS task, it would have been nice to not only compare to the (potentially weak?) baseline of training from random initialisation, but also to see the performance of the current state-of-the-art method, as a point of reference. I can see that using the FM backbone is better than the baseline, but is it really good in absolute terms? Looking into Tancik et al 2021, it seems like the average PSNR of their best method is 21.333, while that of Chen and Wang 2022 achieves 22.07 on average. I realize that the numbers are not directly comparable, but why did you choose to train one model on all three tasks instead of training individual models? It would be helpful to understand if the performance drop is due to the multi-task setting or if the method is simply not competitive with the state-of-the-art.
* I wonder about the variance of the performance values in Table 1: Ideally, one would train each model multiple times and give an estimate of the standard deviation of performance. I’m not yet convinced that the model differences are really stable. The same holds for table 2. It's crucial to understand the statistical significance of the reported improvements, as small variations could be due to random initialization or training fluctuations. Without this, it's hard to assess the reliability of the results.
* Finally, I would have liked to see an explicit discussion of limitations and shortcomings of the method. It is important to acknowledge the boundaries of the proposed approach, such as the potential for catastrophic forgetting when fine-tuning the foundation model, or the computational cost of training large hypernetworks. This would help in understanding the practical applicability of the method.

### Questions
## Questions
* Is there really enough data in NVS to justify the training of models with 86M parameters from scratch? 

## Additional Feedback
* Figure 1 could match the text a bit better: In the figure, the linear layers labelled as “Positional Encoding” are called BaseParam in the text (I think? Or are these the heads?) and the Embed layer and Enc are not labelled in the figure. It is still understandable, but would remove any uncertainty to label the elements in the figure better.
* It would be good to motivate and differentiate the four metrics (PSNR, SSIM, LPIPS, FID). 
* Line 141f (“For computational efficiency, each token only helps to generate the weights of a single layer, with the number of tokens r being the total number of parameters in the layer divided by some hyperparameter g.”) is unclear to me, is BaseParam_k a sparse matrix?
* I think that “Enhancing Hypernetwork architectures with foundation models” would have been a fine title on its own, but that might just be preference (and will not affect my rating of the paper)

## Other thoughts 
(going beyond what would be reasonable to do within the rebuttal period)

In addition to the three training settings you investigate (starting in line 180), have you considered training LoRA adapters as a middle ground between freezing the FM and fine-tuning it completely? Maybe this could help with the issue of catastrophic forgetting mentioned in line 230.

## Nitpicks
* Line 323 "seems to plateau"
* Line 407 "decreased"
* Line 416 "is persists"

### Soundness
3

### Presentation
4

### Contribution
3
