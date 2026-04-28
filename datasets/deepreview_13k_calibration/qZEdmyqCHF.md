# Decoupled Finetuning for Domain Generalizable Semantic Segmentation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Joint finetuning of a pretrained encoder and a randomly initialized decoder has been the de facto standard in semantic segmentation, but the vulnerability of this approach to domain shift has not been studied. We investigate the vulnerability issue of joint finetuning, and propose a novel finetuning framework called Decoupled FineTuning for domain generalization (DeFT) as a solution. DeFT operates in two stages. Its first stage warms up the decoder with the frozen, pretrained encoder so that the decoder learns task-relevant knowledge while the encoder preserves its generalizable features. In the second stage, it decouples finetuning of the encoder and decoder into two pathways, each of which concatenates a usual component (UC) and generalized component (GC); each of the encoder and decoder plays a different role between UC and GC in different pathways. UCs are updated by gradients of the loss on the source domain, while GCs are updated by exponential moving average biased toward their initialization to retain their generalization capability. By the two separate optimization pathways with opposite UC-GC configurations, DeFT reduces the number of learnable parameters virtually, and decreases the distance between learned parameters and their initialization, leading to improved generalization capability. DeFT significantly outperformed existing methods in various domain shift scenarios, and its performance could be further boosted by incorporating a simple distance regularization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the vulnerability issue of joint finetuning, and proposes a novel finetuning framework called Decoupled FineTuning for domain generalization (DeFT) as a solution. DeFT operates in two stages. Its first stage warms up the decoder with the frozen, pretrained encoder so that the decoder learns task-relevant knowledge while the encoder preserves its generalizable features. In the second stage, it decouples finetuning of the encoder and decoder into two pathways, each of which concatenates a usual component (UC) and generalized component (GC); each of the encoder and decoder plays a different role between UC and GC in different pathways. DeFT significantly outperformed existing methods in various domain shift scenarios, and its performance could be further boosted by incorporating a simple distance regularization.

### Strengths
1. A  new finetuning framework dubbed Decoupled FineTuning (DeFT) is proposed for domain generalization. Overall, it is a simple and universal solution for DG tasks.

2. The experimental details are sufficient, the reproducibility is good, and the experimental results are convincing.

### Weaknesses
1. While the approach presented in this paper is quite straightforward, my primary concern is that its framework demonstrates effectiveness solely in practical applications. The authors provide an analysis based on parameter distance, yet they lack a more profound theoretical exploration. Given the standards of an ICLR paper, I believe a rigorous theoretical analysis is essential.

2. The paper exclusively utilizes convolutional backbones, such as ResNet-50, without any experiments on more advanced transformer-based backbones [1-2]. The absence of results with these state-of-the-art encoder-decoder frameworks limits the generalizability and relevance of the proposed method.

### Questions
What are the performance comparisons on Transformer-based backbones?

A more rigorous theoretical analysis is essential.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work the authors propose a fine tuning strategy for encoder-decoder networks to improve domain generalization. The idea is to decouple the fine tuning of encoder and decoder by keeping a frozen copy of the decoder (encoder) when fine tuning the encoder (decoder), and then combine the encoder and decoder with their frozen copies via exponential moving averages. This seems to result in more robustness to overfitting and better generalization, showing improved performance in semantic segmentation scenarios.

### Strengths
- The idea is sound and well motivated.
- Comprehensive experiments that show a notable improvement in the generalization capabilities of the model

### Weaknesses
 - The contribution of decoupling encoder and decoder learning, and the contribution of averaging with earlier frozen models, in my view, should be differentiated and ablated properly. In particular, I suggest to evaluate some baseline without decoupling but that averages the joint encoder-decoder model with earlier clones.
- The method is presented in an overcomplicated and confusing way, and be described in a simpler way. In particular the terminology usual component (UC) and generalized component (GC) to refer to the model and its frozen earlier clone is more confusing than clarifying. 
- There is no theoretical analysis (even preliminary) of why the proposed approach improves generalization (the authors leave it to future work).
- There is no analysis of the additional computational and memory costs of the proposed approach.

### Questions
Please address the comments in the weakenesses section.

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
This paper introduces Decoupled FineTuning (DeFT), a novel framework designed to improve domain generalization in semantic segmentation tasks, where models often perform poorly when exposed to domain shifts. The traditional joint fine-tuning of encoder and decoder networks can lead to overfitting on source domains, reducing generalizability to new, unseen domains.

The paper have three contributions:(1)By separating the fine-tuning of encoder and decoder components, DeFT avoids overfitting and improves the model's ability to generalize across domains.(2)Using EMA updates for GCs allows the model to retain initialization-based generalization properties, enhancing the robustness of learned representations.(3)DeFT is validated on five datasets (e.g., Cityscapes, BDD-100K, Mapillary), showing substantial improvements over state-of-the-art methods across diverse domain shift scenarios.

These contributions position DeFT as an effective framework for domain-generalizable semantic segmentation.

### Strengths
Originality:Rather than jointly fine-tuning encoder and decoder components, the paper innovates with a decoupled strategy. This approach uniquely assigns the encoder and decoder to two different components—Usual Components (UC) and Generalized Components (GC)—which are updated in parallel but through distinct pathways. This structure is particularly inventive in preventing overfitting to the source domain while preserving generalizable features,I think this is a very clever and useful method,At the same time, the author uses EMA to update GC and maintain its generalization ability in the fine-tuning process,This method is also very unique, different from the traditional method.

Quality:In this paper, five different data sets (such as Cityscapes, BDD-100K, GTAV, etc.) and a variety of domain offsets are comprehensively tested, and other methods (such as WildNet, SHADE, BlindNet, etc.) are compared.

Clarity:This paper clearly expounds each stage from the initialization of the decoder to the decoupling fine tuning, provides the pseudo-code of the algorithm, and effectively conveys the architecture and ablation experimental results by using diagrams and tables. I think this makes me clearly understand the whole algorithm process and the advantages of the algorithm.

Significance:This paper solves a key problem of domain generalization of semantic segmentation, and I think it plays a important role.

### Weaknesses
limitation:While the empirical results support the DeFT framework, the theoretical grounding behind the decoupling strategy (specifically the benefits of separating encoder and decoder updates into Usual and Generalized Components) is limited. Strengthening this theoretical component would help clarify why the decoupling approach reduces overfitting and improves generalization.

Suggestion:Consider providing a more detailed theoretical analysis or explanation, possibly referencing or building upon works in model fine-tuning and parameter space regularization.Your overview map is very brief, please enrich it if you can.

### Questions
1.Can you clarify why you chose specific datasets and domain shifts for evaluating DeFT?
2.Have you conducted ablation experiments on the updated method? For example, if you use EMA-based updates only for the encoder or only for the decoder, how will DeFT behave?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper, titled Decoupled Finetuning for Domain Generalizable Semantic Segmentation, introduces a novel approach called DeFT. Traditional joint finetuning of an encoder and decoder often leads to overfitting to the source domain, which degrades generalization capabilities on unseen domains. To address this, DeFT proposes a two-stage framework: (1) warming up the decoder while keeping the pretrained encoder frozen to preserve its generalizable features, and (2) decoupling the finetuning of the encoder and decoder into two pathways, each involving a usual component (UC) and a generalized component (GC) updated by an exponential moving average. This decoupling helps retain initial generalizable knowledge while improving task-specific learning. The method significantly outperformed existing state-of-the-art domain generalization techniques across various domain shift scenarios.

### Strengths
1. Originality: DeFT introduces a unique decoupling strategy for finetuning the encoder and decoder, setting it apart from prior methods that only optimize them jointly. The method's use of an exponential moving average for GC updates further enhances its originality.
2. Quality: The paper is well-structured, providing comprehensive empirical evidence through experiments across five datasets. Ablation studies and comparisons with state-of-the-art methods reinforce the robustness of DeFT.
3. Clarity: The description of DeFT, supported by visual diagrams, pseudocode, and detailed explanations, is clear and facilitates understanding of the training process.

### Weaknesses
1. Complexity of Implementation: The decoupled pathway design and maintaining separate UC and GC pathways may introduce additional implementation complexity that is not addressed in terms of potential computational overhead. That is, there is no relevant model complexity analysis. Specifically, the paper lacks a detailed analysis of the computational cost associated with maintaining two separate pathways during training, including the memory footprint and the time required for each update step. This is crucial for practical applications, especially when deploying the model on resource-constrained devices or with large datasets. The absence of a comparison against standard joint finetuning in terms of training time and memory usage makes it difficult to assess the practical trade-offs of the proposed method.
2. Sensitivity analysis experiments for the main parameters are not available. The paper does not provide a comprehensive sensitivity analysis for the key hyperparameters, such as the exponential moving average (EMA) update rate and the regularization parameter. Without a thorough analysis on how these parameters affect the model's performance, it is difficult to determine the optimal configuration for different datasets or tasks. The lack of such analysis raises concerns about the robustness and generalizability of the proposed method.
3.The experimental equipment is not described in sec.4 EXPERIMENTS.

### Questions
1. How does the complexity of implementing DeFT, with its two separate pathways, impact training time and computational resources compared to standard joint finetuning methods?
2. Have the authors explored other update schemes for the GCs besides the exponential moving average? If so, what were the results, and how did they compare?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
**Motivation**
The paper identifies a critical gap in the semantic segmentation field, where the standard practice of joint fine-tuning pre-trained encoders with randomly initialized decoders has not been adequately examined regarding its vulnerability to domain shift. This lack of investigation highlights a potential risk to domain generalization, motivating the need for a new approach to fine-tuning that can better address these challenges.

**Method**
The authors propose the Decoupled Fine-Tuning (DeFT) framework, which consists of two key stages:

Stage One: A frozen pre-trained encoder is used to preheat the decoder. This allows the decoder to learn task-relevant knowledge while keeping the encoder's generalization ability intact.
Stage Two: The fine-tuning process for the encoder and decoder is decoupled into two separate paths. Each path includes:
A Conventional Component (UC) that updates based on the loss gradient from the source domain.
A Generalization Component (GC) that updates through an exponential moving average biased towards its initialization, thus retaining its generalization capability.

**Contribution**
The introduction of the **DeFT** framework, which explicitly addresses the negative impact of joint fine-tuning on domain generalization in semantic segmentation tasks.
The provision of a novel approach to decouple the fine-tuning of encoders and decoders, leading to improved performance and robustness against domain shifts compared to existing methods that primarily focus on data or feature augmentation.

### Strengths
1. A novel training method, DeFT has been proposed, abandoning the previous joint fine-tuning approach and demonstrating its effectiveness through experiments. 
2. Extensive experimental analyses have been conducted to validate the effectiveness of the experiments and assess the sensitivity to parameters, proving the efficacy of DeFT. 
3. This method can be applied to multiple domains and provides ideas for future research.

### Weaknesses
 1. I am worried that this method may significantly reduce computational speed because the introduction of two EMAs could have a considerable impact on training speed, even if it does not significantly affect inference speed. 
 2. There is a lack of insightful analysis regarding the performance loss associated with joint fine-tuning, making the motivation less compelling.

### Questions
1. I would like to know the impact of the two EMA updates in DeFT on training speed. Specifically, how much slower is it compared to the baseline? Could you provide detailed data on this?

2. In Table 8, I noticed that the EMA update ratio (β) has a significant impact on the experimental results, even with slight variations in this parameter. Could you provide a further analysis of the reasons behind this?

3. In Figure 1, the issue of target loss fluctuations is raised. Does DeFT address this problem? Could further experiments be conducted to investigate this?

### Soundness
4

### Presentation
4

### Contribution
3
