# Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
The Mixture of Experts (MoE) architecture reduces the training and inference cost significantly compared to a dense model of equivalent capacity. Upcycling is an approach that initializes and trains an MoE model using a pre-trained dense model. While upcycling leads to initial performance gains, the training progresses slower than when trained from scratch, leading to suboptimal performance in the long term. We propose Drop-Upcycling - a method that effectively addresses this problem. Drop-Upcycling combines two seemingly contradictory approaches: utilizing the knowledge of pre-trained dense models while statistically re-initializing some parts of the weights. This approach strategically promotes expert specialization, significantly enhancing the MoE model's efficiency in knowledge acquisition. 
Extensive large-scale experiments demonstrate that Drop-Upcycling significantly outperforms previous MoE construction methods in the long term, specifically when training on hundreds of billions of tokens or more.
As a result, our MoE model with 5.9B active parameters achieves comparable performance to a 13B dense model in the same model family, while requiring approximately 1/4 of the training FLOPs.
All experimental resources, including source code, training data, model checkpoints and logs, are publicly available to promote reproducibility and future research on MoE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Drop-Upcycling for MoE training utilizing the knowledge of pre-trained dense models while statistically re-initializing
some parts of the weights. The proposed method promotes expert specialization (which is often a bottleneck in traditional upcycling), significantly enhancing the MoE model’s efficiency in knowledge acquisition.

### Strengths
- The paper is well written and easy to follow.
- The idea of drop-upcycling is interesting although not new (see weaknesses section).
- Extensive experiments and release of all the relevant materials for reproducibility.

### Weaknesses
 - How is the proposed upcycling method different from the upcycling used in Qwen2: https://arxiv.org/pdf/2407.10671? Qwen2 shuffles parameters along the intermediate dimension to promote diversity which I think is very similar to the current method. They also randomly initialize 50% of the parameters. I would suggest the authors to discuss the differences with experiments.
- What are the benefits of upcycling over training from scratch? I think changing architectural components are often difficult as upcycling is often constrained by the dense model architecture.
- Will the current method going to be scalable to very large MoEs, say 100B+ parameter models? What additional challenges author think to encounter in training large MoEs with upcycling? 
- Can upcycling going to help in continual learning? E.g., can we add new experts to an existing MoE using dropupcycling?

### Questions
I think the identified problem is important but I’d like to rate the current submission below the acceptance threshold (included towards reject) due to limited technical contributions, mainly similarity with existing upcycling methods like the one used in Qwen2.

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
4

### Summary
This paper proposes "Drop-Upcycling",  a method that enables an improved initialization scheme for expert parameters based on the weights of a pre-trained dense model. The approach addresses the lack of diversity in expert weights, a limitation of the standard Upcycling method where expert weights are simply cloned from the FFN in the dense model. 

Drop-Upcycling randomly samples indices from the intermediate dimension of the FFNs. The weights corresponding to these indices from $W_{up}$, $W_{gate}$, and $W_{down}$ matrices are dropped and reinitialized using the statistics of the dropped weights. The parameter $ r $ controls the proportion of indices sampled, with $ r = 1 $ representing full random initialization and $ r = 0 $ corresponding to naive upcycling.

The authors performed thorough experiments with an overall 200k plus GPU hours. A key insight is that the advantages of the approach is mainly in long-term training scenarios (>100B tokens).

### Strengths
- The empirical evaluation section and the number of large-scale training conducted are impressive.
- The proposed method is very simple and the parameter $r$ intuitively controls the trade-off between knowledge retention from the dense network and incorporating diversity.
- The authors implement their drop-upcycling on different parameter scale regimes from ~400M all the way to 18B parameters.
- The authors provide the source code which is great for reproducibility

### Weaknesses
 - Although the empirical evaluation is thorough and the results are promising, the paper has rather limited novelty. The paper would have become stronger if the authors could handle more challenging cases appearing in recent MoE literature such as fine-grained MoEs, or experimenting with a shared expert design. It would be beneficial to report the result of some other intuitive baselines such as adding random noise to the channels of the upcycled experts.

- The way the load-balancing loss is applied seems ineffective. Could you elaborate why the loss was not applied layer-wise as that should prevent expert collapse. Even the model trained with Drop-upcycling shows half of the experts in layer 23 are not used by any of the domains.

- The authors mention that the proposed method outperforms other upcycling approaches in long-term training scenarios. It seems in the very long-term training setting, training from scratch may outperform all methods and in the very short-term training (e.g. <50B tokens) the Branch-Train-Mix upcycling achieves the lowest loss. It would be best if the authors could explain this angle better and also study effect of model parameter size. For example at r=0.5, it takes around 70B Tokens to surpass Branch-Train-Mix for the $8\times 152M$ model, while ~130B tokens are required for surpassing it for the $8\times 1.5B$ Tokens.

### Questions
- As the authors highlighted, the Qwen1.5-2.7B-MoE model seems to follow a similar initialization strategy as Drop-Upcycling. It would be interesting to see how this initialization strategy could be extended for fine-grained MoEs with Granularity >1. Do the authors have thought on how they could extend their method accordingly?

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
3

### Summary
This paper introduces Drop-Upcycling, a novel method for initializing Mixture of Experts (MoE) models from pre-trained dense models. The key innovation is selectively re-initializing parameters of expert feedforward networks while preserving some knowledge from the pre-trained model. Through extensive experiments, the authors demonstrate that Drop-Upcycling outperforms existing initialization methods like naive Upcycling and Branch-Train-MiX, achieving better performance with reduced training costs. Their best MoE model with 5.9B active parameters matches the performance of a 13B dense model while requiring only 1/4 of the training FLOPs.

### Strengths
1. The paper presents a clear technical contribution with Drop-Upcycling that addresses a fundamental challenge in MoE training - balancing knowledge transfer and expert specialization. This is demonstrated through comprehensive empirical results.
2. The experimental evaluation is thorough and well-designed, including ablation studies on re-initialization ratios, detailed analysis of expert routing patterns, and large-scale experiments across multiple model sizes (152M to 3.7B).
3. The work demonstrates significant practical impact by achieving comparable performance to larger dense models with substantially reduced computational costs, which is particularly relevant given the increasing focus on efficient training of large language models.

### Weaknesses
1. While the paper shows Drop-Upcycling works well for decoder-only transformers with MoE in FFN layers, there's limited discussion or analysis of how the method might generalize to other architectures (e.g., encoder-decoder models) or different MoE configurations (e.g., attention-based MoE layers). Specifically, the paper lacks experiments or even a discussion on how the partial re-initialization strategy would interact with different architectural choices, such as the placement of MoE layers within the encoder or decoder stacks, or the use of different gating mechanisms. The current scope is too narrow to confidently claim broad applicability.
2. The theoretical analysis in Section 3.2.2 is relatively brief and could benefit from a bit more substance. The approximations used in equation (5), particularly regarding the assumption of parameter independence during re-initialization, are not rigorously justified. The analysis would benefit from a more detailed exploration of the conditions under which these approximations hold, and perhaps some empirical validation to support the theoretical claims. A more thorough treatment of the mathematical underpinnings is needed to strengthen the theoretical contribution.
3. The paper uses a fixed re-initialization ratio (r=0.5) across all layers and experts. Given that different layers in transformer models are known to learn different types of features, a more adaptive approach to setting the re-initialization ratio based on layer position or expert functionality might yield better results. For example, earlier layers might benefit from a lower re-initialization ratio to preserve more general features, while later layers could use a higher ratio to encourage specialization. The authors don't explore this possibility or justify why a uniform ratio is optimal, potentially missing out on performance gains.

### Questions
1. As a suggestion, the authors could consider expanding the theoretical analysis section with formal proofs or empirical validation of the approximations used. This would strengthen the paper's theoretical foundations.
2. It would be valuable to include experiments or discussions on how Drop-Upcycling performs with different MoE architectures or configurations beyond the standard setup used in the paper.
3. Despite the Qwen2 report being brief, the authors could provide a little more detailed analysis comparing their method with Qwen2-MoE,  highlighting any technical differences and their implications. This would be important given that the authors themselves point out the similarity in the two papers. In any case, I appreciate the "open investigation" into this kind of approach.
4. It would be interesting to investigate whether using different re-initialization ratios for different layers (e.g., lower ratios in early layers and higher ratios in later layers) could improve performance. The authors could conduct experiments with layer-wise adaptive ratios or provide an analysis justifying why a uniform ratio is sufficient.
5. It would also be great to see an analysis of the computational overhead introduced by the re-initialization process compared to naive Upcycling.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Drop-upcycling, which aims to boost the effectiveness of upcycling method by selectively re-initializing parameters to achieve the trade-off between expert diversity and knowledge transfers. Besides, this work provides a detailed introduction of employing upcycling for the initialization of MoE models, with good readability. The experiments are designed using two dense models such as Llama and Mixtral, and this work includes extensive experimental evaluation across seven types of tasks from both Japanese and English.

### Strengths
- 1) This paper is well-written and the Method Section is well-organized, thoroughly demonstrating the authors' understanding of the upcycling methods for MoE models. After reading the Method Section, readers gain valuable insights and can quickly follow the authors' motivation.

- 2) The Drop-upcycling proposed in this paper to enhance the specialization of experts in MoE models is very straightforward, and it includes a hyperparameter that can control the degree of expert specialization and knowledge transfer.

- 3) The experiments in this work are comprehensive, and the Experiment Section provides relatively analyses of the observed phenomena.

### Weaknesses
 - 1) In Table 1, the training costs of different MoE initialization methods vary. It is recommended to add a comparison of training times for different models, including wall-clock time and GPU utilization, to demonstrate the advantages of your proposed method. The current presentation only shows FLOPs, which is an incomplete picture of the actual computational cost.

- 2) In line 428, the author uses Model 1, Models 2 and 3, etc., to describe the performance comparison of different baseline models. However, it is unclear which model each number represents. It is recommended to add a "Baseline Models" section to introduce the names, architectures, and training procedures of different baseline models. The same issue also appears in line 411. This lack of clarity makes it difficult to assess the significance of the reported results.

- 3) There are many ways to enhance the specialization of each expert in MoE models. For example, the Branch-Train-MiX (BTX) [Ref A] ensures expert diversity and specialization by feeding each expert different data distributions. In contrast, this work proposes a hyperparameter $r$ to control the initialization density of the FFN layer to ensure specialization. While the paper claims this approach is more efficient, a more detailed discussion is needed on the trade-offs between the two approaches, including the potential impact on the diversity of learned representations and the sensitivity to the choice of $r$. It is not clear if the proposed method can achieve the same level of specialization as BTX.

### Questions
- 1) In the caption of Figure 2, please add the definition of $S$ to ensure self-containment.

### Soundness
3

### Presentation
3

### Contribution
3
