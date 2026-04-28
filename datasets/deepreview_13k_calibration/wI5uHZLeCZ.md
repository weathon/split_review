# Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
Large language models (LLMs) can often be made to behave in undesirable ways that they are explicitly fine-tuned not to. 
For example, the LLM red-teaming literature has produced a wide variety of `jailbreaking' techniques to elicit harmful text from models that were fine-tuned to be harmless.
Recent work on red-teaming, model editing, and interpretability suggests that this challenge stems from how (adversarial) fine-tuning largely serves to suppress rather than remove undesirable capabilities from LLMs. 
Prior work has introduced latent adversarial training (LAT) as a way to improve robustness to broad classes of failures.
These prior works have considered \emph{untargeted} latent space attacks where the adversary perturbs latent activations to maximize loss on examples of desirable behavior. 
Untargeted LAT can provide a generic type of robustness but does not leverage information about specific failure modes. 
Here, we experiment with \emph{targeted} LAT where the adversary seeks to minimize loss on a specific competing task.
We find that it can augment a wide variety of state-of-the-art methods.
First, we use targeted LAT to improve robustness to jailbreaks, outperforming a strong R2D2 baseline with orders of magnitude less compute. 
Second, we use it to more effectively remove backdoors with no knowledge of the trigger. 
Finally, we use it to more effectively unlearn knowledge for specific undesirable tasks in a way that is also more robust to re-learning.
Overall, our results suggest that targeted LAT can be an effective tool for defending against harmful behaviors from LLMs. Models are available at \href{https://huggingface.co/LLM-LAT}{huggingface.co/LLM-LAT}. Chat with our jailbreaking robust model at \href{http://www.abhayesian.}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces targeted latent adversarial training (LAT) as a technique to improve robustness to persistent harmful behaviors in large language models (LLMs). The authors demonstrate LAT's effectiveness in three key applications: (1) improving resistance to jailbreaking attacks while maintaining model performance, (2) removing backdoors without knowledge of the trigger, and (3) enhancing unlearning of undesirable knowledge. The core idea is to perturb latent activations to elicit specific undesirable behaviors during training, then optimize the model to be robust against such perturbations. The authors show LAT can augment existing techniques like refusal training, DPO, and machine unlearning methods to achieve better results with minimal computational overhead.

### Strengths
Pros:
- I believe targeted LAT *can be* a useful attack-agnostic defense, although the current evaluation lacks depth (see below).
- The breadth of evaluation is appealing. It’s nice to see a method that potentially improves on safety/alignment across multiple diverse tasks.

### Weaknesses
Weaknesses:
- The attacks used for the evaluation in the main table (Table 2) are quite weak: the best attack success rate is 27.7% on Llama-3-8B Instruct, although it’s possible to achieve ~100% ASR on this model (e.g., as reported in [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://arxiv.org/abs/2404.02151) but with a different judge). Without strong enough attacks, it’s hard to conclude that the defense is effective enough, especially given the anecdotal evidence that there are some simple breaks like the one mentioned in the paragraph “Manual red-teaming and research demo”. The fact that the attacks are not adaptive limits the conclusions that can be drawn about the method's robustness in real-world scenarios. The reported success rates are not indicative of a strong defense against determined adversaries.
- It’s not clear to me why the proposed targeted formulation should be better than the existing LAT methods, such as Embedding-Space Adversarial Training (Xhonneux et al., NeurIPS 2024) or Defending against unforeseen failure modes with latent adversarial training (Casper et al., 2024b). There are some explanations in the introduction but they seem quite handwavy. Also, the only comparison between RT-EAT and RT-EAT-LAT suggests a small difference: 4.3% vs. 2.9% prefilling ASR while 6.22 vs. 5.86 MT-Bench score - so it’s not even clear which model is really better. The lack of a more rigorous ablation study makes it difficult to isolate the specific contributions of the targeted formulation versus other LAT approaches. The performance differences are marginal, and it's unclear if they are statistically significant.
- MMLU and MT-Bench may be too easy as an over-refusal evaluation since those questions are completely harmless. Adding something like [XS-Test](https://arxiv.org/abs/2308.01263) or [OR-Bench](https://arxiv.org/abs/2405.20947) would make the evaluation stronger. The current evaluation does not adequately assess the model's ability to handle more nuanced or adversarial queries that might require a more sophisticated understanding of safety boundaries. The use of only benign datasets limits the generalizability of the findings.
- R2D2 and RT-EAT should also be added for Llama-3 as baselines. The absence of these baselines makes it difficult to contextualize the performance of the proposed method against established techniques, especially given the availability of Llama-3 models. This limits the ability to make a definitive claim about the superiority of the proposed method.
- Since there are no other baselines except DPO for backdoor removal included in Table 3, it’s unclear whether LAT is really necessary there or basically any algorithm that would *somehow* perturb the weights in the optimization process would work as well. The lack of diverse baselines for backdoor removal makes it difficult to ascertain whether the observed improvements are due to the specific properties of LAT or simply a consequence of any weight perturbation. This raises questions about the necessity of the proposed method for this specific task.
- For the unlearning part, it’s not clear to me whether WHP-C-LAT pushes the Pareto frontier compared to WHP-C. WHP-C-LAT has a noticeably worse MMLU score (43.9% vs. 45.6%) although with a better unlearning performance. Also, the unlearning part should have more baselines (there are plenty of unlearning methods that exist in the literature). The trade-off between unlearning performance and general performance is not clearly addressed, and the lack of comparison with other unlearning methods makes it difficult to evaluate the effectiveness of the proposed method in this context. The performance drop on MMLU raises concerns about the overall utility of the method.
- The choice of the L2 norm for layerwise perturbations looks a bit arbitrary. It would be nice to elaborate why it can make sense.

### Questions
General suggestions:
- Table 2 is too wide. Also, the figures above Table 2 should have a separate caption. Also, all table captions should be above tables, not below. Also \citet vs. \citep should be used correctly throughout the paper (e.g., double check the “Future work” paragraph).
- The Future Work paragraph: an introductory sentence would improve the reading flow.
- “Direct preference optimization: Your language model is secretly a reward model. Advances
in Neural Information Processing Systems, 36, 2024.” - should be 2023, not 2024.
- “prefilling attacks (Haizelabs)” doesn’t seem to be the right reference for the prefilling attack, since it wasn’t introduced there.
- In addition to MMLU, it would be also good to add the MT-Bench score for the DPO-LAT models in Table 8.


**Update after the rebuttal: The paper still feels quite rushed to me, primarily in terms of the experiments. Overall, I feel like Targeted LAT might be a promising method to improve multiple dimensions of safety. However, this is still unclear from this version of the paper. I will keep my original score 5/10. I think the approach might be promising but requires much more systematic experiments. I think extending this work and resubmitting it would be the best option.**

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Large language models (LLMs) often exhibit undesirable behaviors despite fine-tuning efforts to remove them. This paper addresses this issue using targeted Latent Adversarial Training (LAT), which enhances robustness by leveraging latent-space perturbations to target specific failure modes. The approach contrasts with traditional adversarial training, focusing on hidden activations rather than inputs. Targeted LAT improving resistance to jailbreaks, removing backdoors, and unlearning undesirable tasks with little computational cost. Extensive experiments validate the method's efficacy, showcasing its potential as a robust tool for mitigating harmful behaviors in LLMs.

### Strengths
- The paper introduces targeted Latent Adversarial Training (LAT). This computationally efficient approach enhances the robustness of LLMs by specifically targeting latent activations.
- Extensive experiments have been conducted to provide a good insight into the components of the proposed method.
- The paper is generally well-written. With clear illustrations and tables.

### Weaknesses
 - This paper follows a general adversarial training pipeline, which requires maximizing the adversarial loss while minimizing the "safety loss." The framework itself is familiar for adversarial training, which might hinder the contribution of the paper.
- As the proposed method shares similarities to the latent adversarial training (LAT), the paper needs to discuss the difference between the proposed method and the previous LAT. In addition, as the LAT perturbed the layer's activation,  choosing which layers to perturb needs to be better discussed and empirically verified.
- Despite its effectiveness in defense of jailbreak, the DPO setting with the backdoor trigger is impractical, as most training datasets are carefully constructed.

### Questions
1. The attack success rate for GCG's Llama-2 and Llama-3 is relatively low compared to the original paper; could you explain this? 
2. The Llama is famous for its safety. Could you provide a discussion or experiment on a model like Vicuna (easier to jailbreak) to see further performance?
3. The DPO setting with the backdoor trigger is impractical; could you discuss its real-world application more?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the Targeted Latent Adversarial Training (t-TLA) technique that can be added on top of existing algorithms to (1) safeguard LLMs from jailbreak attacks (2) erase backdoor behaviors from LLMs (3) remove knowledge from the models. The authors conducted experiments on each task and observed promising performance.

### Strengths
(1) The t-LAT algorithm seems effective across a wide range of tasks and is flexible enough to be combined with many optimization objectives without adding much overhead.

(2) The authors provide necessary implementation guidelines such as adding additional SFT loss or KL divergence.

### Weaknesses
 **Major**

(1) Section 4.1: The attacks considered are not strong enough with most of them achieving ASR < 20% against the base model, making it questionable whether the proposed technique will bring improvement when faced with more advanced jailbreak attacks like [1], [2] and [3]. Also, both Llama-2 and Llama-3 are very safe models. I think the authors should experiment with weaker models like Vicuna-7B. An improvement of 2% in ASR is still somewhat marginal for me. (Also, I encourage the authors to experiment with larger models if computational resources permit.) The evaluation dataset is also not clearly defined. It is unclear if the test set overlaps with the training data, which could inflate the results. The authors should clarify the source of the evaluation data and conduct experiments to measure any potential overlap.

(2) Section 4.2: It is good to see that DPO-LAT surpasses DPO, but how does it perform when compared with other algorithms designed to remove backdoors from LLMs? The authors should provide a more comprehensive comparison against existing backdoor removal techniques to better contextualize the performance of their method.

(3) Section 4.3: The improvement in WHP dataset is too little to be noticed and only one algorithm and one model are considered. What is the key difference between section 4.3.1 and section 4.3.2. It is not clear to me why they should be separated. The authors should clarify the distinction between these sections and provide a more thorough analysis with additional models and algorithms.

(4) Some important experimental details are left out, especially those related to the hyperparameter of the proposed algorithm and the baseline algorithms (i.e. the $\beta$ for DPO, GCG steps, the examples for MSJ, etc.). It is necessary for me to specify the details of the experiments to make the comparison fair and the experiments reproducible/reliable. The lack of these details makes it difficult to verify the results and reproduce the experiments.

(5) There is no ablation study about the choice of $epsilon$, updated layers, additional SFT loss, and etc, The choice of constraint budget and the additional SFT loss is not consistent across different sections.

**Minor**

(1) It occurred to me occasionally while reading that the paper was written in an extreme rush. There are typo errors (line 220), tables exceeding the width limit (line 233-243, line 1188-1208), one line of equation occupying a full page (line 1107), figures without a caption (217-232), and broken citation links. All these errors can be spotted with a 10-min proof-reading.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors apply latent space adversarial training to three different security problems in large language modeling. They show that adversarial training in deeper layers of the network can additionally improve robustness. Further, they demonstrate that beyond jailbreaks, adversarial training can improve robustness against backdoor attacks and robustness against information leaks in the context of unlearning.

### Strengths
* The authors provide code, models, and even user-friendly tools to evaluate their models (after submission). Given the long history of ineffective defenses, this is an important part of a defense contribution
* To the best of my knowledge the results on sleeper agents and unlearning are novel and demonstrate a broad applicability of adversarial  training to different security issues in LLMs. 
* The authors ablate performing adversarial training in different latent layers of a network, which seems to improve robustness

### Weaknesses
 * The framing of the paper could be improved, in my opinion, but I am open to discussions. The authors highlight efficiency improvements upon prior work that explores discrete adv. training (e.g., 281). However, alternative methods exist that are much closer to the algorithm proposed here and are also efficient (Xhonneux et al., 2024, Yu 2024). I believe the authors should highlight the differences to more closely related prior works and focus the discussions on these differences. As far as I can see this includes: 1) New threat models, 2) Exploring different latent layers. This also includes the introduction, which should highlight unique limitations resolved in this paper (and not those already addressed by other works). Note that I do not consider Yu 2024 in terms of my rating as it was released shortly before the submission deadline. 
* The utility datasets used to evaluate model capabilities are insufficient. Both MMLU and MT-bench suffer from assigning high scores to models that refuse every request. The compliance dataset gives a high score to R2D2, which is known for over-refusal, which makes me skeptical about the result. I would recommend OR-bench to evaluate if latent adv. training has a negative impact on over-refusal (Cui et al., 2024). 
* Comparisons between papers would be easier if the authors used the original method name provided in the respective paper (i.e., RT-EAT vs CAT) 
* Table 2 should be fixed for the camera ready. 
* I found 6 occurrences of missing \ref{} and \cite{} commands: 1009, 1286, 1295, 1313, 1336, 1378
* I was not able to find any concrete hyperparameters for any method except for RT-EAT-LAT. A direct comparison between two methods without stating the hyperparameter search procedure appears to be insufficient. It's unclear if the benefit from RT-EAT-LAT comes from the choice to train in deep latent layers or from better hyperparameter tuning.

### Questions
* The RT-EAT method of Xhonneux et al 2024 appears to be equivalent to the proposed method if adversarial training is conducted only in the first latent layer of a model. Could the authors comment on that? If this is true, the connection should be highlighted to provide better context on how these different methods relate. 
* Can the authors explain how hyperparameters were optimized for the different methods and a table of the final hyperparameters used in the experiments
* Can the authors provide an argument for the sufficiency of the used utility benchmarks in Table 2 (or new results) 

Without further changes, I would recommend to reject this paper. However, I believe many of my concerns can be addressed in a rebuttal, and I am willing to change my score to accept.

Since there are still trivial errors in the paper (such as those remarked by myself or reviewer EUWJ) I decided to reduce my score. In its current state, the paper should not be accepted. 
All in all I believe this could be a valuable contribution and I strongly encourage the authors to submit a revised manuscript. For me, a score of 8 would have been achievable with a convincing rebuttal.

### Soundness
3

### Presentation
2

### Contribution
3
