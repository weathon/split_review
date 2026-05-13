# Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity

- Decision: Accept
- Scores: 5, 8, 6, 8

## Abstract
Architectures such as Linformer and Mamba have recently emerged as competitive linear time replacements for transformers. However, corresponding large pretrained models are often unavailable, especially in non-text domains. To remedy this, we present a Cross-Architecture Layerwise Distillation (CALD) approach that jointly converts a transformer model to a linear time substitute and fine-tunes it to a target task. We also compare several means to guide the fine-tuning to optimally retain the desired inference capability from the original model. The methods differ in their use of the target model and the trajectory of the parameters. In a series of empirical studies on language processing, language modeling, and speech processing, we show that CALD can effectively recover the result of the original model, and that the guiding strategy contributes to the result. Some reasons for the variation are suggested.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the issue of the quadratic computational complexity of standard self-attention in transformer models and proposes a way to convert pre-trained transformer models with quadratic attention to more efficient linear attention, while trying to minimize performance degradation. They call this method Cross-Architecture Layerwise Distillation (CALD), and the core of this approach is the combination of layer-wise distillation with parameter transfer, making the fine-tuning process more efficient, and a few specially designed fine-tuning strategies. 

The authors propose a few strategies to compare with a simple "unguided" approach. They report on language and speech tasks, and show that their proposed methods consistently outperform the unguided approach, and in some cases, some methods can even outperform linear-attention models that are repretrained.

### Strengths
The paper is mostly well-written and the problem it tries to solve is an important one. It does a good job reference related works. Novelty-wise, although the individual components of the proposed method aren't new, it has a fair amount of novelty for combining them and designing different fine-tuning strategies for training. The figure showing the actual trajectory of hidden states is interesting and informative to show how parameters change in those different methods.

### Weaknesses
I'm not fully convinced of the claimed merits of the method. While it seems to be convincing that those proposed methods are better than unguided approach, there are unanswered questions regarding those approaches, because it seems to have different behaviors in different tasks. E.g. in experiments reported in Table 1, unguided's performance significantly lags behind other methods, while in Table 2, the relative difference is much smaller. This might indicate that the unguided hyper-params might not be well-tuned for certain tasks. Also, in Table 1, the "hybrid" approach gives the worst performance among all CALD variants, but it seems to give the best performance in many of the cases in Table 2 and 3. This to me suggests that there might be some other fundamental factors that caused those different behaviors shown in those Tables. 

There are a couple of misreferences in the writing, where the authors wanted to reference Figure 1 but said Figure 3 instead. There's a reference of Figure 4.1 and Figure 4.4 which I believe are typos that point to other Figures in the paper. In section 2.2, there's an incomplete sentence "an example of the direct parameter transfer approach."

It took me a while to fully understand Figure 1, and I think the source of the confusion comes from that the diagram involves both shifts in hidden states and also relapse of time, like the "trajectory/waypoint guided" blue arrow actually "follows" the green arrow as time goes by. I understand the authors might want to show this diagram here to be consistent with Figure 4 shown later in the analysis, but my feeling is this diagram isn't the clearest way to demonstrate the difference between the approaches. I would feel that providing simple pseudo-code instead of this diagram + lots of text in method bullet points might be a better way to accurately represent the methods. 

For ASR tasks, the authors use CTC loss instead of CE. How that does change Equation 4? E.g. do you still compute the CE per-frame or some other computation? Also, since CTC adopts a blank token in its output and we have research works that show a CTC model would predict blanks for most frames, I feel there should be some interactions with this aspect instead of treating blanks and non-blanks equally.

### Questions
Please see the above "weakness" section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a method called Cross-Architecture Layerwise Distillation (CALD). The goal of CALD is to convert existing pre-trained transformer models into linear-complexity models and also fine-tune tje,, making them more computationally efficient without the need for extensive re-pretraining. This approach enables the efficient adaptation of models to different architectures, such as transforming RoBERTa into Linformer for NLP tasks and Wav2Vec2 into Mamba2 for speech processing tasks. CALD combines parameter transfer, where attention layers are replaced with efficient sequence-mixing modules, with knowledge distillation, where the student model learns from the teacher model's behavior. Four distillation modes are presented: Target Guided, Trajectory Guided, Waypoint Guided, and Hybrid.
The paper highlights that CALD effectively minimizes performance loss compared to directly converted models, demonstrating its efficacy across various language and speech processing tasks.

### Strengths
1.) The introduction of the Cross-Architecture Layerwise Distillation (CALD) is noteworthy, as it aims to convert pre-trained transformer models into efficient linear-complexity architectures. This bridges a critical gap by enabling the reuse of existing pre-trained models without the need for resource-intensive pretraining, especially for non-text domains like speech.

2.) The empirical studies are well-structured and cover various conversion tasks from RoBERTa to Linformer for NLP tasks, Wav2Vec2 to Mamba2 for speech tasks, and Pythia to Mamba for language modeling. The detailed experiments provide a strong basis for assessing the effectiveness of CALD, showing that guided approaches outperform unguided ones significantly.

3.) The paper does a thorough job of comparing the proposed method with existing approaches, including both guided and unguided methods. The results highlight that CALD, especially with trajectory-guided or waypoint-guided distillation, can effectively maintain or improve performance close to standard transformer models.

4.) The inclusion of diverse benchmarks (e.g., QNLI, QQP, TED-LIUM, SLURP, VoxCeleb1) and the report of performance improvements in areas like word error rate (WER) and accuracy provide strong evidence for the robustness of the proposed methodology.

5.) The paper provides a solid theoretical explanation for why trajectory-guided distillation can retain pre-training knowledge and ensure better downstream task performance.

### Weaknesses
Limited Discussion on Limitations: While the results are strong, the paper lacks an in-depth discussion on potential limitations or failure cases of the CALD approach, especially in more complex or resource-constrained real-world scenarios. For instance, the paper does not explore how the performance of CALD might degrade when the target architecture has a significantly different number of parameters or layer structure compared to the teacher model. Furthermore, the paper should discuss the sensitivity of CALD to the choice of hyperparameters, such as the learning rate and the distillation temperature, and how these might need to be tuned differently for different model architectures and tasks. It is also unclear how CALD would perform if the pre-training data of the teacher model is significantly different from the fine-tuning data used for the student model.

Computational Cost Analysis: Although the proposed method is presented as a more efficient alternative, there is insufficient analysis of the actual computational cost savings compared to traditional pre-training or conversion processes. A more detailed breakdown of memory and time requirements would enhance the practical relevance. The paper should include a comparison of the training time and memory consumption of CALD with that of training the target architecture from scratch, as well as with other existing model conversion methods. It would be beneficial to provide a more granular analysis of the computational cost of each distillation mode (Target Guided, Trajectory Guided, Waypoint Guided, and Hybrid) to understand the trade-offs between performance and efficiency. The paper should also discuss the inference time of the converted models and how it compares to the original teacher models.

### Questions
Q1 - How does CALD compare with other recent state-space models in terms of accuracy, inference time, and training stability, particularly for large-scale speech tasks?

Q2 - Have the authors tested CALD in real-world deployment scenarios for speech and language tasks? If so, how does its performance hold up compared to controlled experiments?

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
In this work, a cross architecture layer wise distillation (CALD) approach is proposed, which includes converting a transformer model to a linear time substitute by replacing attention modules and fine-tuning the new model towards the target task. The fine-tuning is enhanced by knowledge distillation at different levels and stages. The proposed method is examined in both language modeling and speech processing tasks. The results show CALD can effectively narrow the gaps between linear time based substitute and original transformer model on the downstream tasks.

### Strengths
- CALD provides an effective and cost-effective approach to build linear complexity based language model by leveraging pre-trained transformer based language model.
- Multiple knowledge distillation methods are proposed and examined.
- The experiments are conducted with different modalities including both speech and text, and different linear complexity transformers. The results show CALD could achieve good results.

### Weaknesses
 - Experimental descriptions could be improved by providing more information. For example,  in section 4.2, "the models are converted from and compared with retrained RoBERTa-base."  But in the following description about Table 1, "In addition, we try to use the target guided approach but initialized from the teacher source parameters, which shows slightly lower results". Are other models are not initialized from RoBERTa-base? 
- More detailed analysis about different distillation methods would be helpful. Specifically, the paper lacks a discussion of how the different distillation losses (e.g., feature-based, output-based) interact with each other and how their relative weights are determined. The impact of these choices on the final performance is unclear.
- The proposed method could be further improved by including the discussion about linear complexity attention module initialization, which could be very important for the final results. The paper does not provide details on how the linear attention mechanisms (e.g., Linformer, Mamba) are initialized, which could significantly affect the training dynamics and final performance. For example, are the projection matrices in Linformer initialized randomly, or with some specific scheme? Similarly, how are the state transition matrices in Mamba initialized?

### Questions
- How do you choose hyper parameters in equ. 7?
- In Table 1, Src. init results are worse, why?
- Hybrid approach is better in Table 2 and 3, but it is worse in Table 1. Any explanation?  The trajectory or waypoint guided approaches are worse than the target Guided method in Table 3 but better in Table 1. Any explanation? Has the model learnt enough from the waypoint model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Latests long-context recurrent models such as Mamba2 have demonstrated performance similar to transformer models, even in large scale scenarios, while being more efficient (no quadratic complexity of attention).
However, they need to be retrained from scratch, which could slow down the adoption of their architecture—especially with so many pre-trained transformer models already available.
Moreover, for non-text modalities such as speech, large scale Mamba 2 models are simply not available yet.
Hence authors propose leveraging off-the-shelf pre-trained (transformer) models and converting them into the target (mamba 2) model with linear complexity.
More specifically, they explore the possibility of converting an existing pre-trained transformer into a linear-complexity model for a specific downstream task; approach proposed is called Cross-Architecture Layerwise Distillation (CALD) and combines parameter transfer and distillation.
Multiple scenarios are explored, including converting RoBERTa to Linformer for NLP tasks, Pythia to Mamba for language modeling, and Wav2Vec2 to Mamba2 for speech tasks; converted models show minimal to no performance loss compared to standard transformers while being of linear (instead of quadratic) complexity.

### Strengths
-new approach to address model conversion/distillation from transformer (quadratic) architectures to mamba 2 (linear) architectures

-not only applied to written language but also to speech with convincing results (3 types of tasks overall: NPL, LM and Speech)

### Weaknesses
 -the obtained model is no longer a general purpose model (converted for a specific downstream task)

-some inference speed evaluations would have been a plus (we know that obtained models with linear complexity should be faster though)

### Questions
Q: the conversion/distillation is made for a particular downstream task, would it be possible to make it for the pre-trained - general purpose - model ?

Q: can we further speed-up inference through quantization (with added benefits)?

### Soundness
4

### Presentation
4

### Contribution
4
