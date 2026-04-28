# Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
The Sparse Mixture of Experts (SMoE) has been widely employed to enhance the efficiency of training and inference for Transformer-based foundational models, yielding promising results.
  However, the performance of SMoE heavily depends on the choice of hyper-parameters, such as the number of experts and the number of experts to be activated (referred to as top-$k$), resulting in significant computational overhead due to the extensive model training by searching over various hyper-parameter configurations.
  As a remedy, we introduce the \algmoe (\algabbr) technique.
  \algabbr incorporates (1) a novel gating method that enables each token to automatically determine the number of experts to activate.
  (2) An adaptive process automatically adjusts the number of experts during training.
  Extensive numerical results across Vision, Language, and Vision-Language tasks demonstrate the effectiveness of our approach to achieve competitive performance compared to GMoE for vision and language tasks, and MoE-LLaVA for vision-language tasks, while maintaining efficiency by activating fewer parameters.
  \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents DynMoE a mixture-of-experts approach which uses 2 mechanisms:

  * Top-any routing which computes a score for each token-expert pair and a learnable threshold per expert, therefore allowing a rather dynamic use of tokens/expert computations.
  *  keeping track of expert utilisation to grow/shrink throughout the training, and initialising the new experts routing based on the non-routed tokens.

It shows results in vision, language, and vision-language tasks and shows it comparable to training with a fixed (but sweeped) number of K experts and top-k tokens routed.

### Strengths
Together, the two proposed mechanisms achieve an expert architecture which automatically decides the number of expert activations and the total number of experts throughout the training. Those are two problems that if addressed correctly can make MoE simpler to use by not having to fix them ahead of time.

### Weaknesses
In my understanding, early design of MoEs [Shazeer et al., 2017] had many engineering challenges in consideration such as efficient use of compute units and network, which led to many of the fixed top-k routing decisions (e.g. why should the compute unit that processes expert A process only 10 tokens.. if it has to wait for another compute unit that has to process 100 tokens?) which is also similar to the concerns of equal utilisation of experts with the purpose to efficiently utilise hardware. With that in mind I find it hard to understand from the text in this paper: (a) why those concerns don’t apply here, (b) how has hardware changed overtime such they are no longer important, (c) if the approach here would not scale to utilise hardware as efficiently as a fixed top-k routing as one scales the method.

Unclear on what mechanisms are at play to optimise the gating mechanisms. In particular it appears to this reviewer that the only gradient to the gating and gating thresholds is via the (1/k) factor of eq (6).. If so one can tend to understand that no per-expert specific gradient is observed.. By that I mean, for a token, all of the params used to compute its gating values will observe similar gradient directions regardless of which expert they refer to.

### Questions
My main questions are highlighted on the main weaknesses above.


After rebuttal from authors with added experiments on (1) Included a load-balance loss in our model; (2) Introduced an efficiency loss to enforce sparsity, as suggested in [2]. I have raised my score from below acceptance to accept.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work proposess DynMoE, an enhanced version of the Mixture of Experts layer. The method enables top-any gating, allowing for the execution of different number of experts for each token. In the proposed method experts that are unused for a predefined period of training time are discarded, and new experts are added if there are tokens that do not activate any experts.

The proposed method is relatively simple and appears to achieve its intended effect of reducing the hyperparameter tuning burden associated with MoE layers. However, the method is compared to only a single variant of MoE, and improvements are visible on only a subset of the results. There are several other issues, with not adequately detailed description of the method being one of them. As of right now, I recommend rejection of this work, but I am willing to increase the score if the authors properly address my concerns.

### Strengths
- Elimination of hyperparameters introduced by MoE, which was the motivation of the paper, is practical and useful, and thus the work could be of interest to the community. The method is also relatively simple, which may be regarded as an advantage.
- The main evaluation is relatively thorough in terms of number of datasets and models. The authors evaluate their method on three different setups, with one being a multimodal task.

### Weaknesses
 - **Limited novelty and lack of proper attribution:** While the authors demonstrate some improvement over standard MoE layers, the idea of dynamically selecting the number of executed experts on a per-token basis is not new [1,2,3,4]. Moreover, none of these are mentioned in the related work section. The authors should properly discuss these works and highlight the differences of the proposed method.
- **Lack of comparison to existing MoE methods from the literature:** Given the above, does the proposed method provide any advantages over the existing top-any literature? An empirical comparison with these methods would strengthen the contribution. As of right now, the authors compare their method with only a single baseline (one of the top-k MoE variants), which is an extremely low number for an empirical-only work. Would the benefits of the proposed method hold even when stacked against alternative top-k MoE variants? Some of these variants also allow for an effectively different number of experts executed per token in inference [5].
- **Unconvincing real latency/throughput evaluation:** A major flaw of the work is that authors only briefly mention the actual speedup that the method supposedly provides. The authors write (line 488): "To ensure a fair evaluation, MoE-LLaVA employs the expert dispatching implementation from DynMoE by fixing the top-k values.". This statement is unclear, and for me it suggests the opposite of a fair evaluation, as the alternative implementation may significantly slow down the original MoE-LLaVA. The readers should be aware of any overhead stemming from the introduction of top-any routing. I would at least expect a non-negligible overhead stemming from the non-constant number of token-expert executions. Finally, to provide a complete picture, the authors should also measure and report the throughput of dense models for comparison.
- **No from-scratch training experiments:** All experiments are conducted on pre-trained models, which are then converted to sparse MoE models during the fine-tuning. Mixture-of-Experts layer was originally proposed to scale up the number of parameters without slowing down from-scratch training. Although the pre-trained setup is as important, demonstrating that the proposed method is also appropriate for the from-scratch setup would strengthen the paper.
- **Standard deviations not being reported:** The authors do not report standard deviations of the results in any of the experiments. This is particularly surprising as the authors write in the appendix that the scores are averaged over three random seeds. Without standard deviations it is hard to estimate the significance of the results, especially since some of the scores in Tables 1, 2, 3, and Figure 4 are really close. The authors also do not present any evidence that training of the proposed DynMoE is stable in any separate experiment.
- **Method description and experimental setup not being adequately explained:** After multiple passes through the text some crucial aspects are still unclear to me - see the questions section below.
- **Readability:** I would recommend to do a pass through the paper to improve grammar and readability (e.g. "and uses an additional gating network g to predict the scores that the input token embedding assigned to each expert." or "To promising efficiency and avoiding burden communication, we only check if experts required to be added add or removed.").

### Questions
- How are experts initialized at the start given a pre-trained model? Are parameters of experts that are added during training initialized randomly, or are the weights of the most recently discarded expert re-used?
- Are the auxiliarry losses somehow weighted? If yes, why is it not reported in the paper?
- Is the MoE implementation used in this work dropless [6], i.e. does it drop tokens if the predefined capacity of an expert is exceeded? If it is not dropless, how often are tokens dropped and how does DynMoE compare to standard MoE in terms of load balance?
- In the appendix the authors write: "For each epoch, we begin recording routing at 1/3 of the epoch and complete recording routing and execute the adaptive process at 2/3 of the epoch." Can the authors clarify why is this needed?
- Currently the method relies on a linear router. However, some works assume a deeper router [7,8]. Can the method be extended to non-linear routers?
- Remark 3.1 is not fully convincing to me. Can the authors explain more in detail why different ranges of expert scores are supposed to be undesirable? 

#### References:
[6] Gale, Trevor, et al. "Megablocks: Efficient sparse training with mixture-of-experts." Proceedings of Machine Learning and Systems 5 (2023): 288-304.

[7] Zhang, Zhengyan, et al. "MoEfication: Transformer Feed-forward Layers are Mixtures of Experts." Findings of the Association for Computational Linguistics: ACL 2022. 2022.

[8] Chi, Zewen, et al. "On the representation collapse of sparse mixture of experts." Advances in Neural Information Processing Systems 35 (2022): 34600-34613.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the DYNMOE, an algorithm that automatically determines the number of experts activated for each token, addressing the dependency on hyperparameters (such as the number of experts and the number of activated experts) in SMoE models. DYNMOE uses an innovative top-any gating method and an adaptive training process to dynamically adjust the number of experts, while incorporating auxiliary loss functions to ensure sparsity and diversity among experts, improving training and inference efficiency. Experiments demonstrate that DYNMOE achieves comparable or superior performance and efficiency to well-tuned MoE configurations across vision, language, and vision-language tasks.

### Strengths
1 The paper clearly analyzes existing issues in MoE, particularly how the fixed top-k approach may not be optimal.

2 The authors consider the extreme case of activating all experts in the top-any scenario and design a regularization loss to address this.

3 The writing logic is clear.

### Weaknesses
1 In the top-any routing, is G a hyperparameter that needs to be predefined? Would this lead to cumbersome tuning?

2 In the top-any routing, the selected k experts considered equally important by default. Would introducing varying importance levels for different experts yield better results? Although the authors mention related content in Remark 3.1, ablation experiments seem necessary.

3 Why top-any MoE training strategy dones't lead to increased training time?

4 The author could further elaborate on how the diversity loss in the auxiliary loss prevents activating all experts simultaneously.

5 How exactly does DYNMOE remove experts? For example, if the interval for adding/removing experts is set to 300 steps and expert x is activated in the first 299 steps but not in the 300th step, will it be removed? Alternatively, if expert x is activated in the first step but not for the remaining 299 steps, will it be removed?

6 For new experts added in DYNMOE, Would averaging the weights of other experts to initialize the new expert’s weights lead to better results? Or would random initialization yield better performance?

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript proposes an MoE framework in which the activated expert numbers could be learned, and each expert can be removed or added during the training phase. This framework removes the hand-design requirements for expert numbers, and outperform the hand-designed MoEs in vision, language and multi-modal tasks.

### Strengths
- The studied problem is interesting and well-motivated, as the design of MoE have been adjusted by hand in previous studies;
- The proposed method is novel and reasonable;
- Empirical evaluation is relatively comprehensive to support the claims, and the observations provide useful insights for researchers in the field;
- Good readability, which helps readers clearly understand the contribution and advantages.

### Weaknesses
 Overall, this is a novel and solid work. I have some kind suggestions for further improving it:

- Experiments
  - For vision tasks, why not conduct experiments on the well-known ImageNet dataset? To my understanding, MoE is designed for larger-scaled data and model sizes. Experiments with larger backbones on ImageNet would make the method more convincing.
  - Comparison with existing MoE models would strengthen the proposed approach, such as Swin-MoE [1], VoE [2] (on vision) and Switch Transformer [3], Mistral MoE [4], DeepSeek-MoE [5] (on language).
  - Maybe it is useful to discuss the advatanges of this well designed MoE over those conventional backbones at the same computation budgets.

- Literature review. To my understanding, the proposed method lies in the field of dynamic neural networks [6]. It is encouraged to discuss more about the relationship to other dynamic paradigms, such as layer skipping [7]. When it allows a token to select 0 expert, the proposed framework would naturally allows layer skipping.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
