# Decoupling Angles and Strength in Low-rank Adaptation

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Parameter Efficient FineTuning (PEFT) methods have recently gained extreme popularity thanks to the vast availability of large-scale models, allowing to quickly adapt pretrained models to downstream tasks with minimal computational costs. However, current additive finetuning methods such as LoRA show low robustness to prolonged training and hyperparameter choices, not allowing for optimal out-of-the-box usage. On the other hand, multiplicative and bounded approaches such as ETHER, even if providing higher robustness, only allow for extremely low-rank adaptations and are limited to a fixed-strength transformation, hindering the expressive power of the adaptation. In this work, we propose the DeLoRA finetuning method that first normalizes and then scales the learnable low-rank matrices, thus effectively bounding the transformation strength, which leads to increased hyperparameter robustness at no cost in performance. We show that this proposed approach effectively and consistently improves over popular PEFT methods by evaluating our method on two finetuning tasks, subject-driven image generation and LLM instruction tuning. Code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Two existing fine-tuning methods, LoRA and ETHER, have shown widespread success across the field, especially the former. However, some issues with LoRA from hyperparameter tuning and length of fine-tuning arise, leading to degradation in performance. The proposed method, DeLoRA, separates the magnitude and direction of the weight updates from LoRA. This is reminiscent of multiplicative weight updates such as ETHER and OFT with constrained magnitudes. DeLoRA is shown empirically to frequently achieve better accuracy than either LoRA or ETHER.

### Strengths
- The ablation studies provide a convincing argument that somewhere in the continuum between LoRA and ETHER+ is a more powerful method. The experiments showing that different settings have different optimal locations in this continuum show that there are some directions forward with regard to which settings require different method choices, as well as defend that this continuum often contains a better method than the extremes.

- DeLoRA shows promise in having strong robustness similar to ETHER with explicit weight constraints, even when learning rates are high.

### Weaknesses
 - It took some time to figure out what exactly the DeLoRA method is. For clarity, what DeLoRA is could be written in its own dedicated section, not just embedded in Figure 1 without explaining the parameters or at the end of Section 2.2.1, since the two equations describing the method seem like all the others in the derivation at first glance. 

 - It's mentioned in the introduction that one downside to LoRA is performance degradation during extended fine-tuning. This reads as though DeLoRA will overcome this issue, however, the top right of Figure 3 seems to show DeLoRA having the same issue. Are there other instances that can be added to show that DeLoRA does robustly train over many iterations?

 - Figure 3 could use some repetitions. The single training run makes some of the training dynamics, especially DoRA's, hard to trust that they weren't due to randomness.

 - In the derivations section, the LoRA and ETHER derivations seem to create different methods. This may come from the step of changing the ETHER derivation from a multiplicative adaptation to an additive one, but how this is achieved is not clear. Adding at least a few more steps to bridge between the two would be appreciated.

Small things:
- "Figure 5: Average..." instead of "Figure 5: Avergae..."

### Questions
- In the derivations section, the LoRA and ETHER derivations seem to create different methods. This may come from the step of changing the ETHER derivation from a multiplicative adaptation to an additive one, but how this is achieved is not clear. Adding at least a few more steps to bridge between the two would be appreciated. 

Small things:
- "Figure 5: Average..." instead of "Figure 5: Avergae..."

### Soundness
3

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
3

### Summary
This paper proposes a new PEFT method based on LoRA called DeLoRA. 
In specific, the authors propose to decompose the learned low-rank update in LoRA into a learnable low-rank matrix with a unit norm, and a learnable magnitude.
The authors also draw a connection between the proposed DeLoRA and multiplicative ETHER which learns low-rank matrices to be *multiplied* instead of *added to* the original frozen parameters. 
The authors evaluated the proposed method on a variety of language and vision tasks and demonstrated fine-tuning performance improvement from DeLoRA.

### Strengths
1. The writing of this paper is good and it is pleasant to read. 
 
2. The proposed method is well-presented. The connection to existing methods ETHER and DoRA is also amenable. 

3. The experiments look sufficient to me.

### Weaknesses
After reading through the paper, my main concerns lie in the concept of DeLoRA. Namely, 

1. While an original main motivation of DeLoRA, as presented in Introduction, is to "introduce a boundary on the weight updates" to LoRA, the addition of *learnable* parameter $\lambda$ (without any regularization/constraint, if I read the paper correctly) removes this guarantee. Specifically, the learnable $\lambda$ allows the magnitude of the update to grow unboundedly, effectively negating the intended boundary. This makes the DeLoRA solution a strict subset of LoRA's, where the proposed parameterization introduces an inductive bias that is not fully explained by the presented motivation. The rationale for this specific parameterization and its implications on the optimization landscape remain unclear. 

2. On the other hand, as the idea of decomposing the learning into magnitude and direction has already been proposed in DoRA, I feel that how different DeLoRA really is from DoRA, e.g., if they are in fact equivalent, needs more elaboration and careful discussion. Currently the authors only provide a equation-by-equation comparison, but no insights is provided in this form. For instance, a more detailed analysis of the optimization dynamics and the resulting weight distributions would be beneficial. It is not clear if the different parameterization leads to different solutions or if it is just a reparameterization of the same underlying optimization problem. In addition, I think this difference should be highlighted in Introduction and Method, instead of just in Related Work.

### Questions
Besides above questions in Weakness, I also wonder:

1. In Table 1,2 how was controllable boundary combined with LoRA? 

2. In Fig 3, DeLoRA's distance to initialization was in fact decreased, how was this happened? 

3. Can you elaborate more on Fig 4? I didn't find any discussion in the main body. 

4. Can you test the proposed method on more language tasks, such as math reasoning?  

I am willing to adjust my score if these questions can be addressed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses some limitations in current parameter-efficient fine-tuning (PEFT) methods, particularly the robustness and flexibility challenges faced by additive methods like LoRA and multiplicative approaches like ETHER. The authors introduce DeLoRA, a fine-tuning method that normalizes and scales learnable low-rank matrices to improve hyperparameter robustness without sacrificing performance. Through evaluations on subject-driven image generation and large language model (LLM) instruction tuning tasks, DeLoRA demonstrates consistent improvements over existing PEFT methods, offering a balanced solution that enhances adaptability and performance in fine-tuning applications.

### Strengths
1.	Overall, this paper is well-written and presents its ideas in a clear, accessible manner, making it easy to follow.
2.	The authors provide insightful reviews of two primary categories of fine-tuning methods: additive techniques such as LoRA and multiplicative approaches like ETHER, effectively highlighting the limitations inherent to each approach.
3.	The bounded approach constrains the updating scheme within a Frobenius norm ball, promoting a more robust selection of learning rates and potentially enhancing stability across different training settings.

### Weaknesses
Overall, the contribution of this paper appears somewhat incremental, as it focuses on constraining weight updates within a restricted range—a concept that has also been examined in the DoRA paper. Additionally, the performance comparison with LoRA and DoRA is challenging to assess directly, as the experiments were conducted on different datasets.

1.	[Key Issue] The concept of decoupling the angles and scales in LoRA has been explored extensively in the DoRA method. Consequently, the contribution of this paper feels somewhat incremental in comparison to DoRA. Similar to DeLoRA, DoRA can limit its scale term within a fixed range, thereby preventing over-drifting in downstream adaptations. Would this lead to the same robustness effect?
2.	[key issue] LoRA and DoRA algorithms are typically evaluated on well-established NLP and NLU tasks, such as the GLUE benchmarks and Commonsense Reasoning, where their performance characteristics are widely understood. Thus, a fairer performance comparison would be achievable if DeLoRA were also tested on these datasets.
3.	In Eq (13), the updating is limited to |H-I| <= r, effectively limiting weight changes to within a Frobenius norm ball. Then it is not surprising that the algorithm is not sensitive to the change of learning rates. But a fundamental question is: is this restriction always necessary? For instance, in cases where the pretrained model diverges significantly from the target task, imposing a strict parameter update range might inadvertently hamper overall performance.
4.	In line 172, the authors state that 'multiplicative fine-tuning methods show stronger performance in generative models.' However, the results in Table 2 suggest that additive methods like LoRA and DoRA outperform OFT approaches, which appears contradictory and requires clarification.
5.	In Table 2, the performance improvement over DoRA appears marginal. Could the authors clarify if DoRA was evaluated with r=16? To ensure statistical reliability, it would be beneficial to repeat this experiment multiple times and report the standard deviation, as the observed improvement may fall within the range of experimental error.

### Questions
See the above "weakness".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Motivated by the lack of robustness of LoRA fine-tuning with respect to hyperparameter choice and catastrophic forgetting phenomena, the authors propose a novel PEFT method trying to tackle these problems. Their proposal merges the advantages of LoRA and ETHER, being able thus to control rank and maximal distance between fine-tuned and frozen weights.

### Strengths
The paper is well presented and the proposed methods is both efficient and easy to implement.

### Weaknesses
While I find no evident weakness in the manuscript and its content, I believe a broader experimental setting should be proposed to test the method (see questions for more details). Moreover, given the motivation of the work, I encourage the authors to include additional evidence concerning the robustness of their proposed method with respect to hyperparameters (and maybe something more about the avoidance of forgetting phenomena).

### Questions
I leave here some questions/comments concerning the work:
1) Would it be possible to test the method on other common benchmarks (e.g. GLUE Deberta V3)?
2) The only concern I have about the new parametrization is that if a column of $A$ and $B$ is driven towards zero during training, normalization may cause instabilities. Did the authors ever observe this in practice? I would be worried of this phenomenon happening especially when choosing a high rank for the correction.

### Soundness
2

### Presentation
3

### Contribution
2
