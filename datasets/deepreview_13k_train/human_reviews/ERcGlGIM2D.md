# BLIPEE:  Fast and Robust BLIP with Adversarially Trained Early Exits

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
In recent years, Vision-Language Models (VLMs) have shown remarkable performance improvements in vision-language tasks. However, their large size poses challenges for real-world applications where inference latency is a concern. To tackle this issue, we propose employing Early Exit (EE) strategies in VLM. However, training exit classifiers in VLMs is challenging, particularly with limited labeled training data. To address this, we introduce BLIPEE, an adversarial training approach within a GAN-based framework. Here, each exit consists of a transformer layer and a classifier, and the transformer layer is adversarially trained to produce feature representations similar to the final layer, while a feature classifier serves as the discriminator. Our method focuses on performing input-adaptive inference that mitigates the overthinking issue and increases inference speed. Experimental results demonstrate the effectiveness of our approach in enhancing accuracy and model robustness by mitigating overthinking and the phenomenon of mid-crisis that we highlight. The anonymized source code is available at https://anonymous.4open.science/status/BLIPEE-3ED3.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a very interesting issue of early exists on existing VLM models. To achieve this goal, it introduces an adversarial training approach within a GAN-based framework. Specifically, a transformer layer is utilized to mimic the output features of original VLM, and a classifier is utilized to determine when to exist. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The motivation of this paper is valuable.

2. This paper is easy to read and well-written.

3. The proposed components are reasonable.

### Weaknesses
1. The topic is too limited. The early exits issue is a good question for the existing VLM models, especially for large VLM models. The authors just implement the early exits strategy on a single BLIP model, limiting its scalability. The lack of exploration across diverse VLM architectures raises concerns about the generalizability of the proposed method. It remains unclear how the proposed early exit strategy would perform with different encoder-decoder combinations or with models employing different attention mechanisms.

2. The illustrations of the proposed components are not clear. The authors should re-organize the method section for better presentation. A more detailed explanation of how the transformer layer mimics the output features of the original VLM is needed. The specific loss functions used for training the adversarial network and the exit classifier should be explicitly stated. A clear algorithmic pseudo-code of the entire process should also be provided, detailing the data flow and the training procedure.

3. The experiments are insufficient. The authors compare the efficiency of their BLIPEE with other large VLM like Flamingo, however, the authors do not apply their EE strategy to Flamingo for “plug-and-play” comparison. This makes it difficult to assess the true potential of the proposed method. The comparison should include the performance of the proposed method when applied to other VLM models, not just a comparison against their inference speed. The lack of ablation studies on the impact of different components of the proposed method also limits the understanding of its effectiveness.

4. Since the proposed method relies on additional transformer and classify layers, the authors should provide the comparison on model complexity. The authors should provide a detailed analysis of the parameter overhead introduced by the additional transformer and classifier layers. It is important to understand the trade-off between the speedup achieved by early exits and the increase in model size and computational cost due to these additional components. A comparison of the number of parameters and FLOPs with and without the early exit strategy should be included.

### Questions
1. The topic is too limited. The early exits issue is a good question for the existing VLM models, especially for large VLM models. The authors just implement the early exits strategy on a single BLIP model, limiting its scalability.

2. The illustrations of the proposed components are not clear. The authors should re-organize the method section for better presentation. A algorithmic pseudo-code of the entire process should also be provided.

3. The experiments are insufficient. The authors compare the efficiency of their BLIPEE with other large VLM like Flamingo, however, the authors do not apply their EE strategy to Flamingo for “plug-and-play” comparison.

4. Since the proposed method relies on additional transformer and classify layers, the authors should provide the comparison on model complexity.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an early exit strategy for training VLMs. The key idea is to attach exits across different language model layers, with each exit consisting of a transformer layer and a classifier. The transformer layers and the classifiers are trained through a GAN-based framework such that the transformer layers generate feature representations similar to the last layer. Training consists of (1) backbone fine-tuning and (2) exit training. For exit training, a semi-supervised setup and an unsupervised setup are discussed to train the transformer layer to generate features similar to the final layers. During inference, captions are generated in an autoregressive manner. Experimental results show that the proposed method outperforms prior early exit methods with less computational cost.

### Strengths
* The motivation is clear; the mid-crisis and overthinking phenomenon is intriguing.
* Early exit could also provide some insights into the reasoning mechanisms of LLMs, as shown in Figure 3.
* The idea is novel; using a GAN-based method for early exit is interesting and seems effective.

### Weaknesses
 * The motivation for backbone fine-tuning is unclear and not explained. Why not use a pre-trained backbone? Does it help early exit?
* Most of the baselines come from earlier works. The baseline from recent VLM works, such as LLaVA, miniGPT-4, etc. are missing.
* According to Tables 1 and 2, the performance improvement seems incremental. Instead of the speedup calculated from L323, what is the speedup on the hardware specify in the paper? Does actual speedup align with this calculation?

Minor issue: Citations within the text are strange, check the formatting instruction.

### Questions
1. What is the speedup on hardware? Does early exit also speedup the causal self-attention (autoregressive) model?
2. What is $w_i$ in L342?
3. In Eqn (2), the last $y*$ should be $y*_{1:t-1}$?
4. Does other GAN-framework work? Such as WGAN?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
An EE strategy BLIPEE for VLMs to effectively mitigate inference latency by reducing unnecessary computations. BLIPEE emulate the behaviour of the final layer at the exits through adversarial learning. Experimental results demonstrate the effectiveness of this approach in enhancing accuracy and model robustness by mitigating overthinking and the phenomenon of mid-crisis that we highlight.

### Strengths
The key differences in this work are clear: 1) We employ adversarial training for efficient learning of EE models. 2) Our method can work under both semi-supervised and unsupervised setups by utilizing the zero-shot capabilities of the BLIP-2, while previous methods require a good amount of high-quality labeled training data, thus reducing size of training data.

### Weaknesses
1、Confusing symbols in fig1, why Classifier N, what’s meaning of D1/D2?
2、Missing some improtant references:
[1] NEO-KD: Knowledge-Distillation-Based Adversarial Training for Robust Multi-Exit Neural Networks
[2] L. Qendro and C. Mascolo, "Towards Adversarial Robustness with Early Exit Ensembles," 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Glasgow, Scotland, United Kingdom, 2022, pp. 313-316, doi: 10.1109/EMBC48229.2022.9871347.
3. Unsupervised manner is not novel, just self-labeling, but their pseudo labels are not accurate enough in general.
4. Ablation study is not enough, whether or not the proposed adversarial training is necessary?
5. Technical contributions are not enough, no matter of adversarial training or knowledge distillation are very commonly-used skills, no more new techniques are founded.

### Questions
1. The proposed early exit method was only tested on blip2, and other models were not tested, so the generalization abilty of the method cannot be confirmed. At the same time, the section 3.1 mentioned that the problem discussed in this paper is because Q-former generates image-grounded text embeddings. However, in the case that most VLMs do not use Q-former nowadays, is this method still applicable?
2. The paper tested VQA and caption tasks, and blip2 also tested the retrieval task. How does the method in this paper performs on the retrieval task?
3. The speedup in the article is calculated based on the number of parameters. Can it be calculated based on the actual inference time?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an early exit strategy to reduce the inference latency in Vision-Language Models. An adversarial training network within a GAN-based framework BLIPEE is utilized to reduce the negative impact of limited labeled training data. In the BLIPEE network, each exit contains a transformer layer and a classifier. The used input-adaptive inference mitigates the overthinking issue and increases inference speed. Experimental results show the effectiveness of the proposed BLIPEE. Authors provide anonymized source codes.

### Strengths
Some codes are provided to increase credibility of the BLIPEE network. 

Various results show the effectiveness of the BLIPEE network. The designed method can improve the inference speed while yielding high-quality outputs.

Tables and figures are clear. I can understand them easily.

Limitation section is provided to present the work comprehensively.

### Weaknesses
The compared methods are not state-of-the-art. The newest compared methods (OFA and Flamingo) are published in 2022. Some state-of-the-art works are required for comparison.

In Table 2, BLIPEE-V-O and BLIPEE-V-F contain more Train Params than BLIP-2 V-O and BLIP-2 V-F. Why BLIPEE-V-O and BLIPEE-V-F have higher Spd than BLIP-2 V-O and BLIP-2 V-F?

In Figure 2, "Layers" should be "Layer number".

Some references needs to be revised, such as Li et al. (2020) in Line 634-642.

Some grammatical errors, such as "P_N denote the probability score ..." in Line 215.

About "Our objective is to fasten the existing BLIP-2 VLM model", the objective is not enough for ICLR since the work is only used to fasten the specific model. At first, I thought this paper reconstructed BLIP-2 VLM model. Besides, I agree with Reviewer g7un: "the novelty for combining them in a unique way" is not enough for ICLR.

About Ans-2, as shown in the tables, the speed increase is not amazing, which means that the early exit mechanism is not suitable for most cases.

Thus, I concern that this presented method can only handle a small number of cases.

### Questions
Please address the weakness.

### Soundness
2

### Presentation
3

### Contribution
2
