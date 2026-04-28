# ExPLoRA: Parameter-Efficient Extended Pre-Training to Adapt Vision Transformers under Domain Shifts

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 5, 8, 5, 6

## Abstract
Parameter-efficient fine-tuning (PEFT) techniques such as low-rank adaptation (LoRA) can effectively adapt large pre-trained foundation models to downstream tasks using only a small fraction (0.1\%-10\%) of the original trainable weights. 
  An under-explored question of PEFT is in extending the pre-training phase without supervised labels; that is, can we adapt a pre-trained foundation model to a new domain via efficient self-supervised pre-training on this new domain? 
  In this work, we introduce \model{}, a 
  highly effective technique to improve transfer learning 
  of pre-trained vision transformers (ViTs) under domain shifts.
  Initializing a ViT with pre-trained weights on large, natural-image datasets such as from DinoV2 or MAE, \model{} continues the unsupervised pre-training objective on a new domain, unfreezing 1-2 pre-trained ViT blocks and tuning all other layers with LoRA.
  We then fine-tune the resulting model only with LoRA on this new domain for supervised learning. 
  Our experiments demonstrate state-of-the-art results on satellite imagery, even outperforming fully pre-training and fine-tuning ViTs. 
  Using the DinoV2 training objective, we demonstrate up to 7.5\% improvement in linear probing top-1 accuracy on downstream tasks while using <10\% of the number of parameters that are used in prior fully-tuned state-of-the art approaches. 
  Our ablation studies confirm the efficacy of our approach over other baselines, including PEFT and unfreezing more ViT blocks. 
  Code is available on the project website: \url{https://samar-khanna.io/ExPLoRA/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work presents ExPLoRA, which initializes a ViT with pre-trained weights, selectively unfreezes 1 - 2 blocks, tunes remaining weights with LoRA, and continues unsupervised pre-training on a new domain. Then fine-tunes the model on the new domain for supervised learning. This work demonstrates state-of-the-art results on satellite imagery and generalizes to different domains like wildlife, medical, and agricultural imagery.

### Strengths
-	The introduction of ExPLoRA, a new parameter-efficient method to extend unsupervised pretraining on target domains. 

-	Conducting comprehensive experiments on various datasets, and showcasing improvements in linear probing top-1 accuracy and outperforming existing techniques on datasets like fMoW. 

-	The authors show the effectiveness of ExPLoRA and analyze the differences in local and global information encoded in the patch representations output by each ViT block.

### Weaknesses
 - The authors argue that they selectively unfreeze 1 - 2 blocks, tunes remaining weights with LoRA. But specifically, it is very difficult to evaluate the number of layers to be tuned and which layers to be tuned. Although the authors have shown that the method of tuning 1 - 2 layers is feasible, it is not known whether the number of layers and the specifically selected layers are sensitive for different domains. In other words, the authors‘ method might not be optimal for different domains or datasets.
- The authors may have missed two baselines. For example, in Table 1, the author only gives a result of using their own method for finetuning. However, one baseline is to use the LoRA method in the pre-training phase, and the author should compare the effect of their method with this baseline. The second baseline is to use the pre-trained MAE for full finetuning directly on the downstream task. Intuitively, it is still unknown whether further pre-training on the downstream task is necessary. This baseline will complete the integrity of the experiment. 
- In addition to LoRA, the authors lack a comparison of some related PEFT methods [1,2,3,4,5]. It is better to be able to discuss the related methods. Furthermore, as mentioned in the paper, it is also better for the author to be able to give some results on detection and segmentation tasks.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents ExPLoRA, a method for efficiently adapting pre-trained vision transformers (ViTs) to new domains using parameter-efficient fine-tuning (PEFT) techniques, utilizing LoRA (Low-Rank Adaptation). 
By continuing unsupervised pre-training on the target domain and only unfreezing select model layers, ExPLoRA enables adaptation with minimal computational overhead. 
This approach leverages pre-trained models on natural image datasets like DinoV2, achieving notable performance gains, particularly in challenging domains like satellite imagery. 
For instance, ExPLoRA outperforms fully pre-trained models on satellite classification tasks while using fewer parameters, highlighting its efficiency. 
Beyond satellite data, ExPLoRA generalizes well to other domains, including medical and wildlife imagery, as tested on the WILDS benchmark.

### Strengths
1: ExPLoRA excels at adapting large vision transformers to new domains without requiring full re-training, instead leveraging low-rank adaptation. This parameter-efficient approach significantly reduces computational costs, making it suitable for resource-constrained environments.

2: The proposed method is simple yet effective. The ExPLoRA can directly use the well-trained vision foundation models. This compatibility also simplifies its integration with established models.

3: Extensive experiments on RGB satellite images show the proposed methods' effectiveness compared with previous state-of-the-art works.

### Weaknesses
1: Analysis of the effect of total training cost. From my understanding, this work's main contribution (claim) is to adapt continuing unsupervised pre-training before supervised training on downstream domains (I don't regard using LoRA fine-tuning and unfreezing the last ViT blocks as this work's contribution, and feel free to point my misunderstanding if it is). It is a two-stage. Therefore, it's important to consider the computational cost of these two stages simultaneously. I have seen Figure 7 which analyzes the effect of pre-training iterations. How about simply putting the equivalent computational cost on the supervised fine-tuning stage? Will unsupervised pre-training speed up the convergence of supervised fine-tuning? If the computational budget is fixed, how should we allocate it across the two different stages?

2: The effect of the "extend unsupervised pre-training stage". Current ablation studies mainly focus on the settings of learnable parameters (unfrozen blocks and LoRA). I hold the perspective that the main claim of this paper is the importance of "extend pertaining" for downstream domain transfer. Therefore, the authors are encouraged to verify the necessity of this stage further. For example, supervised fine-tuning can be performed directly with the current optimal setting of LoRA and unfrozen blocks for transferring.

3: Extending the model to multi-modal models like CLIP and zero-shot settings like using natural language for zero-shot understanding in downstream tasks. The authors could follow the setting of the CLIP paper (the downstream validation dataset).


4: (An open question). How about changing unsupervised training objectives in the extended pertaining stage? Lare-scale pre-trained DinoV2 and MAE both have their advantages. The unsupervised training stage is not limited to the corresponding original training objective. Can the model combine different advantages using different training objectives in this stage?

### Questions
Potential limitations of the proposed extended pre-training. Can this stage only benefit the domain shits or also work in general scenarios (like general classification and general object detection)? I also did some experiments before and I failed. I would appreciate it if the authors' pipeline works in such scenarios, but I also understand this part is out of the scope of this paper's claim.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces ExPLoRA, a novel parameter-efficient method for adapting pre-trained vision transformers (ViTs) to new domains through extended unsupervised pre-training. ExPLoRA initializes ViTs with weights from natural-image datasets and continues pre-training on new domains with LoRA. The model is then fine-tuned on the new domain for supervised learning, achieving impressive results on satellite imagery and generalizing to various domains like wildlife, medical, and agricultural imagery. ExPLoRA outperforms fully pre-trained and fine-tuned techniques while using significantly fewer parameters.

### Strengths
1. The writing of the article is quite good and the article is logical.
2. Supplementary materials are substantial.
3. The use of PEFT for post-pretraining in the visual domain is innovative.
4. The experiments in the domain migration section are ample and sensible.

### Weaknesses
1. Figure 1 seems to express the difference between full fine-tuning and PEFT in a more accurate form.
2. The idea of using PEFT for post-pretraining is a good one. loRA was proposed a few years ago, and there are more efficient PEFT methods in the visual field. Maybe the authors can try to compare with LoRA with newer methods [1-3].
[1] 1% vs 100%: Parameter-efficient low rank adapter for dense predictions.
[2] Pro-tuning: Unified prompt tuning for vision tasks.
[3] Adapter is all you need for tuning visual tasks.

3. The method section is more like a solution derived through experience. It is recommended to analyse whether LoRA has limitations in coping with visual post-pretraining tasks, and optimise based on the analysis to propose your own PEFT method.
4. The whole article seems to be like a technical report, and it is recommended to add some in-depth theoretical analyses and technical innovations for visual features.

### Questions
See above.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors introduce ExPLoRA to improve transfer learning of pre-trained vision transformers (ViTs) under domain shifts. It initializes a ViT with pre-trained weights and continues unsupervised pre-training on a new domain with some blocks unfrozen and LoRA for other layers. Then it fine-tunes with LoRA for supervised learning. Experiments show state-of-the-art results on satellite imagery. It improves linear probing top-1 accuracy and ablation studies confirm its efficacy over other baselines

### Strengths
1. The paper is well organized, the figures are readable and understandable.

2. The proposed method looks logical and technically sound.

3. The experimental results are strong. Consistent improvements have been shown over different baselines.

### Weaknesses
1. Concerns about the novelty: The proposed ExPLoRA seems does not have essential differences with the conventional LoRA. What are the differences from LoRA? This paper is more like a technical report than a research paper. The method appears to be a straightforward combination of existing techniques, specifically LoRA and selective layer unfreezing. The authors do not provide a compelling argument for why this particular combination is novel or leads to non-obvious performance gains. The core idea of applying LoRA to certain layers while unfreezing others lacks a strong theoretical justification, making the contribution seem incremental rather than groundbreaking.

2. Many important experimental comparison results are missing. 1) The authors should compare their proposed method with the recent SOTA ViT-based domain adaptation [1-6] in the same setting. The lack of direct comparisons with state-of-the-art domain adaptation methods for ViTs is a significant oversight. The paper should include results against methods that explicitly address domain shift in ViTs, not just general pre-training techniques. 2) Many PEFT methods besides LoRA, [7-8] should be compared. The reviewer wonders whether ExPLoRA outperforms these types of methods? The experimental section needs to be expanded to include a wider range of parameter-efficient fine-tuning methods, including those that use adapters, prompt tuning, or other low-rank approaches. Without these comparisons, it is difficult to assess the true value of ExPLoRA. 3) The results on the widely-used UDA benchmarks like Office-Home, Office-31, VisDA are missing. The absence of results on standard domain adaptation benchmarks makes it hard to evaluate the method's generalizability and effectiveness in typical domain adaptation scenarios.

[1]. TVT: Transferable Vision Transformer for Unsupervised Domain Adaptation, WACV 2023;

[2]. Safe Self-Refinement for Transformer-based Domain Adaptation, CVPR 2022;

[3]. CDTRANS: CROSS-DOMAIN TRANSFORMER FOR UNSUPERVISED DOMAIN ADAPTATION, ICLR 2022;

[4]. Patch-Mix Transformer for Unsupervised Domain Adaptation: A Game Perspective, CVPR 2023;

[5]. Towards Unsupervised Domain Adaptation via Domain-Transformer, IJCV 2024;

[6]. Making The Best of Both Worlds: A Domain-Oriented Transformer for Unsupervised Domain Adaptation, ACM MM 2022;

[7].Low-Rank Few-Shot Adaptation of Vision-Language Models, CVPR 2024;

[8]. Quantized Prompt for Efficient Generalization of Vision-Language Models, ECCV 2024;

3. Many important references of domain adaptation and PEFT [1-8] are missing. These works should be briefly reviewed in the related work section. The related work section is incomplete, lacking discussion of key papers in both domain adaptation and parameter-efficient fine-tuning. The absence of these references makes it difficult to contextualize the proposed method within the existing literature.

### Questions
1. What are the differences between ExPLoRA and LoRA?
2. Does the presented method outperform the state-of-the-art DA and PEFT methods in the same setting?
3. What are the results on the widely-used UDA benchmarks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents an approach for parameter-efficient continual pretraining and fine-tuning of visual foundation models addressing domain shift of the underlying data distribution. To accomplish this, the authors propose to use LoRA during continual pretraining and subsequent fine-tuning.

The domain shift covered in this submission put a major focus on remote sensing imagery as covered by a large part of the experimental section. Nevertheless, the submission also covers some minor experiments including domain shifts of datasets about cell tissue images, wheat images, and animal images.

For all datasets, the authors were able to demonstrate the efficiency of their approach in continual pretraining and fine-tuning up to results able to outperform fine-tuned visual foundation models.

I very much appreciate the work in this area - especially because not everybody has the resources to train visual foundation models and therefore approaches like the one presented are much appreciated. However, overall I see this submission providing only marginal contribution as it combines known methods such as continual pretraining ([mendieta2023towards] proposed it for remote sensing) and low-rank adaptation ([scheibenreif2024parameter] proposed it for remote sensing) together.

Also and since the majority of the experimental section focuses on remote sensing, in times of geo-spatial foundation models such as ScaleMAE, SatMAE, or GMF, I have trouble to see that the first step of training such models is to take a visual foundation models being trained on natural images only.

---
```
@inproceedings{mendieta2023towards,
  title={Towards geospatial foundation models via continual pretraining},
  author={Mendieta, Mat{\'\i}as and Han, Boran and Shi, Xingjian and Zhu, Yi and Chen, Chen},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={16806--16816},
  year={2023}
}
@inproceedings{scheibenreif2024parameter,
    title     = {Parameter Efficient Self-Supervised Geospatial Domain Adaptation},
    author    = {Scheibenreif, Linus and Mommert, Michael and Borth, Damian},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2024},
    pages     = {27841-27851}
}
```

### Strengths
**(S1)**: this work covers an important aspect of foundation model training.

**(S2)**: this work provides vast amount of experimental results showing the capabilities of the proposed approach.

**(S3)**: the presented ablation study of the paper provide valuable insights into parameter-efficient domain adaptation of remote sensing imagery.

### Weaknesses
 **(W1)**: this submission rather combines known approaches than presents methodological or algorithmic novelty. This can be of great value for the research community. However, I think the insights provided in this work might be limited to the ICLR research community.

**(W2)**: given previous work in this area, I miss baseline evaluations against non-LoRA continual pretraining (-> mendieta2023towards) and against pure LoRA (-> scheibenreif2024parameter). Such experiments would provide the opportunity to highlight the capabilities of the proposed approach much more and compare it against previous work.

### Questions
**(Q1)**: In section 4 Problem Setup, the target domain data comes from p_{D_T}(x) where D_T is a set of domains, being a subset of all domains. What is then the difference between  p_{D_T}(x) and p_{d_T}(x, y) coming from d_T ∈ D_T? Is this just the formulation that *some* of the domains of p_{D_T}(x) might provide labels (i.e., p_{d_T}(x, y)) and some not? And if yes, is there a significant change in distributions between these? Can we assume that these distributions (p_{D_T}(x) and p_{d_T}(x, y)) are similar with respect to the distribution of x?

**(Q2)**: Is there a reason why for some experiments you do compare against ScaleMAE and in some you do not? For Table 1, the ScaleMAE in its LoRA-r8 version is missing (while SatMEA is provided). It would be interesting to see ScaleMAE performance as 0.8M fine-tuned parameter model. In Table 4 and Table 5 ScaleMAE is entirely missing. Table 6 is listing ScaleMAE as baseline. Is there a rationale behind this?

**(Q3)**: In Table 3, the ablation study, there is an experiment showing [All], which adapts not only the attention matrices but also the MLP matrices. This is great, have you also run experiments showing how MLP adaptation without attention adaptation would perform?

**(Q4)**: In Fig. 2, where can I find U in the figure, which is described in the image caption.

### Soundness
3

### Presentation
4

### Contribution
3
