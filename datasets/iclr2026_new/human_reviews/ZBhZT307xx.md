## Human Reviewer 1

### Summary
This paper analyzes the reliability of rule-based vs. model-based verifiers in reinforcement learning with verifiable reward (RLVR), focusing on mathematical reasoning tasks. Experimental results demonstrate that Rule-based verifiers achieve near-perfect precision but poor recall, increasingly misclassifying correct answers from stronger models. Model-based verifiers can offer higher recall and better flexibility across datasets, but are prone to reward hacking during RL training.

### Strengths
1. The paper is clearly written and easy to follow, with a logical structure and clear presentation of results.
2. It addresses an important and timely question about the reliability of verifiers in RL-based fine-tuning.
3. The work provides a detailed and systematic statistical analysis comparing rule-based and model-based verifiers across multiple benchmarks.

### Weaknesses
1. The paper is mostly empirical and lacks a formal analysis of why RL dynamics amplify verifier brittleness. 
2. The study focuses almost exclusively on mathematical reasoning; generalization to other domains is less mentioned.
3. Reported gains in RL experiments are small and may not exceed noise given limited sampling. Statistical uncertainty isn’t reported.
4. The paper lacks a clear concluding message or actionable suggestion. While it identifies the limitations of both rule-based and model-based verifiers, it does not provide concrete guidance or a principled framework for designing more robust evaluation systems.
5. Section 6 feels unconvincing to me. The probing study on “hacking patterns” appears artificial and disconnected from realistic training dynamics. In practical RL settings, it is unclear how likely policy models are to autonomously discover and exploit such handcrafted adversarial patterns.

### Questions
1. Have the authors considered evaluating the findings on more general or non-mathematical reasoning tasks to test cross-domain robustness?
2. I am quite intersted in what mechanisms cause fine-tuned verifiers to become more vulnerable.
3. Could adversarially trained verifiers (such as through contrastive fine-tuning on generated hacking examples) help improve robustness without sacrificing recall?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper investigates verifier accuracy and its impact on model performance in reinforcement learning with verifiable rewards (RLVR) for mathematical reasoning tasks. Through systematic experiments, the authors show that commonly used rule-based verifiers, while highly precise, suffer from false negatives that lead to suboptimal training outcomes. They further evaluate model-based verifiers and find that, although recall improves, these verifiers are vulnerable to reward hacking during RL training. To mitigate this issue, the paper proposes a hybrid verifier that combines rule-based and model-based verifications, achieving greater stability and performance. Overall, the study underscores the critical role of verifier design in ensuring reliable reward signals and provides some practical guidance for building more robust verifier systems.

### Strengths
- **Originality.** The paper provides a systematic and timely investigation of verifier design in RL with verifiable rewards (RLVR), providing one of the first comprehensive analyses of how verifier accuracy impacts training stability and model performance and exposes limitations in current verification systems.
- **Comprehensive experimentation.** The study conducts extensive experiments comparing rule-based and model-based verifiers, builds dedicated diagnostic datasets, and performs multiple RL training runs with the Qwen2.5-7B model under different verifier configurations.
- **Quality.** The experimental design is sound and rigorous, with consistent metrics and well-documented procedures. The reported improvements are clear and no apparent flaws are evident in the setup and evaluation process.

### Weaknesses
- **[Significance]** While the paper presents systematic experiments and insightful analyses, many of its findings confirm known issues rather than reveal fundamentally new phenomena. Specifically, (1) the false-negative problem of rule-based verifiers has been discussed in prior work on mathematical expression evaluation (e.g., [1], [2]); and (2) the vulnerability of LLM-based verifiers to reward hacking aligns with broader findings on LLM-as-a-judge robustness and the reward hacking in RLHF (e.g., [3], [4]). Although this paper is among the first to document such hacking behaviors in verifier-based RL, the results are largely predictable. The proposed hybrid strategy, which combines rule-based and model-based verifiers, is practical but conceptually straightforward, as both components are adapted from existing methods.
- **[Experiment]** The RL evaluation primarily uses a single policy model (Qwen2.5-7B). Without additional policy models, it is difficult to assess whether the observed verifier effects generalize across architectures or model scales.
- **[Presentation]** The paper’s presentation is somewhat disorganized, making it easy for readers to lose track of the experimental narrative. Numerous experimental setups are scattered throughout the text, and the analyses are often separated from their corresponding results. For example, Figure 1 is introduced early (page 2) but its related experiment is not discussed until page 6; likewise, the analysis of the hybrid verifier in Section 4.1 refers to results that only appear in the appendix. Additionally, Sections 5.2 and 6 contain overlapping analyses on the reward hacking patterns. Overall, this fragmented structure reduces readability and weakens the logical flow of the paper.

[1] Non-Autoregressive Math Word Problem Solver with Unified Tree Structure. EMNLP 2023.

[2] TinyV: Reducing False Negatives in Verification Improves RL for LLM Reasoning. Arxiv 2025.

[3] Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment. EMNLP 2024.

[4] ODIN: Disentangled Reward Mitigates Hacking in RLHF. ICML 2024.

### Questions
- How do the authors interpret the noise in rule-based verifiers? Do such negative samples represent a fundamental limitation for developing better reasoning models, or could they instead be viewed as tolerable label noise—given that neural networks are often robust to noisy supervision [1, 2]? Moreover, since hybrid verification introduces additional training cost, why not explore simpler scaling strategies, such as increasing data volume or training steps, to mitigate the noise effect?
- A potentially insightful extension would be to quantify verifier noise tolerance in RLVR, i.e., how much noise the training can tolerate before noticeable performance degradation or collapse occurs. Do the authors have any empirical observations or insights on this aspect?

[1] Deep learning is robust to massive label noise. Arxiv 2017.

[2] Spurious Rewards: Rethinking Training Signals in RLVR. Arxiv 2025.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper analyzes the verifier component of RLVR in mathematical reasoning tasks. The authors point out that commonly used rule-based verifiers buffer from high precision but low recall, as they perform well only on responses following specific patterns. To mitigate this limitation, LLMs are utilized as a model-based verifier based on its reasoning skills. 
Furthermore, the authors proposed a hybrid verifier and also analyzed the reward hacking  problem in using trained model-based verifiers.

### Strengths
* The paper attempts to clarify and analyze key issues often overlooked in RLHF and RLVR research, particularly the limitations of rule-based versus model-based verifiers. This focus addresses an important and timely problem in the field.

* The discussion on potential reward hacking and robustness issues arising from the use of model-based verifiers is interesting, providing new perspectives on challenges that are often underexplored in current research.

### Weaknesses
**\[W1\] Insufficient Analysis**  
The paper's main motivation is that the impact of verifier types on RLVR is poorly understood, yet it lacks in-depth analysis on this topic. There is no error case analysis explaining why rule- and model-based verifiers fail, nor any examination of how these failures influence policy behavior. Without these critical components, the paper lacks the insights necessary to address its core motivation.

**\[W2\] Low Readability**  
The overall organization of the paper lacks clarity, which makes it difficult to follow the intended narrative. In the abstract and introduction, the authors state that the paper focuses on a comparative analysis between rule-based verifiers and model-based verifiers. However, there is no mention of hybrid verifiers in these sections. Starting from Section 3.3, the paper significantly discusses hybrid verifiers, but the motivation for introducing this concept and its role within the paper’s main objective are not clearly explained. As a result, the overall flow of the paper becomes confusing, and readers may struggle to understand how each section contributes to the central argument.

In addition, the placement of figures and tables often lacks alignment with the corresponding text. Some figures (e.g., Figure 1\) combine content drawn from multiple sections, which makes cross-checking difficult.

**\[W3\] Limited Diversity of Verifiers and Policy Models**  
The hybrid setting is tested with only three model-based verifiers, leaving unclear whether the reported vulnerabilities generalize across architectures or scales. Moreover, RL training uses a single policy (Qwen 2.5 7B), which restricts analysis of verifier–policy interactions. Broader experiments with different verifier families and policy sizes would provide stronger evidence for the claimed trends.

### Questions
**\[Q1\]** Lines 398-399: What explains the instability observed in trained verifier models compared to untrained verifiers and rule-based verifiers? It seems counterintuitive that untrained model-based verifiers don't exhibit the same instability as their trained counterparts.

**\[Q2\]** Given that GPT-4o was utilized as the oracle reward, what performance metrics would this model achieve if implemented directly as a model-based verifier? If it demonstrates high precision and recall, wouldn't this suggest that employing LLMs with superior reasoning capabilities is a more direct solution?

**\[Q3\]** Are models with strong reasoning capabilities like GPT-4o also susceptible to reward hacking? This question has implications for the fundamental approach proposed in the paper.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper investigates the reliability of verifiers: rule-based v.s. model-based in RLVR for mathematical reasoning. The authors evaluate existing rule-based verifiers across different training datasets, finding that their recall could drop compared with rigid equivalence checks. Thus the authors propose model-based and hybrid verifiers that combine rule-based precision with LLM-based flexibility. The authors also show that model-based verifiers yield +2–3 point gains in RL performance, but they introduce reward hacking challenging: policy models exploit verifier weaknesses to gain inflated rewards.

### Strengths
1. Verifier reliability is practically and conceptually important in RL.

2. The static and dynamic analyses span multiple open-source verifiers and datasets, revealing concrete recall-precision trade-offs.

3. The paper goes beyond accuracy metrics, exposing vulnerabilities of fine-tuned verifiers and proposing reward hacks.

### Weaknesses
1. In Figure 1, the differences among rule-based, verifier-based, and oracle reward curves are relatively minor. Table 2 further shows that the hybrid or model-based verifiers yield only about +2 points over the baseline. It is unclear whether such modest gains justify the additional computational and implementation overhead of integrating verifiers into the RL loop.

2. The curves labeled as verifier-hacked and non-hacked in Figure 1 are almost overlapping except at the very last step. This makes it difficult to attribute the observed performance drop to reward hacking rather than to stochastic variation in RL training. It is hard to see obvious performance effects of reward hacking to the RL training.

3. All experiments are conducted on Qwen-based models. The absence of results on other models limits the generality of the conclusions about verifier reliability and reward-hacking behavior.

4. Unclear value proposition of verifiers. The paper claims that introducing verifiers improves reward reliability, yet it simultaneously shows that verifiers increase the risk of reward hacking. Without a clear demonstration that the verifier cost is outweighed by significant performance improvements, it is hard to be convinced that verifiers “deserve” the added overheads. A more compelling storyline might instead argue that naive verifier design will be easily hacked, and then propose a new, more robust verifier design to tackle with this new challenging.

### Questions
1. Could the authors provide a cost–benefit analysis to quantify the extra cost of hybrid or model-based verifiers versus the performance gain reported in Table 2?

2. Do similar verifier behaviors hold for non-Qwen models?

3. Since verifiers can both improve reward recall and introduce hacking risk, could the authors propose a design principle that preserves reward reliability without exposing new vulnerabilities? This would make the paper more convincing and complete.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4
