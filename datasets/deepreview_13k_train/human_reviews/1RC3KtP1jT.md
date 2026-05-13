# Archilles' Heel in Semi-open LLMs: Hiding Bottom against Recovery Attacks

- Decision: Reject
- Scores: 5, 3, 6, 8

## Abstract
Closed-source large language models deliver strong performance but have limited downstream customizability. Semi-open models, combining both closed-source and public layers, were introduced to improve customizability. However, parameters in the closed-source layers are found vulnerable to recovery attacks. In this paper, we explore the design of semi-open models with fewer closed-source layers, aiming to increase customizability while ensuring resilience to recovery attacks. We analyze the contribution of closed-source layer to the overall resilience and theoretically prove that in a deep transformer-based model, there exists a transition layer such that even small recovery errors in layers before this layer can lead to recovery failure. SCARA employs a fine-tuning-free metric to estimate the maximum number of layers that can be publicly accessible for customization. We apply it to five models (1.3B to 70B parameters) to construct semi-open models, validating their customizability on six downstream tasks and assessing their resilience against various recovery attacks on sixteen benchmarks. We compare SCARA to baselines and observe that it generally improves downstream customization performance and offers similar resilience with over \textbf{10} times fewer closed-source parameters. We empirically investigate the existence of transition layers, analyze the effectiveness of our scheme and finally discuss its limitations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SCARA, a selective closed-sourcing approach for designing semi-open large language models (LLMs) that enhance customizability while maintaining resilience against recovery attacks. The authors develop an algorithm that strategically keeps only a few bottom layers closed-source, ensuring model flexibility without compromising security. They theoretically demonstrate a "transition layer" within deep transformer models, showing that recovery errors in layers before this point lead to recovery failure, while errors in later layers have a limited impact. SCARA estimates the optimal number of layers to hide using a novel metric based on initial recovery loss, bypassing the need for fine-tuning. The method is applied to five models ranging from 1.3B to 70B parameters, tested across six downstream tasks and sixteen recovery benchmarks. Results show that SCARA improves downstream performance while requiring over ten times fewer closed-source parameters than baselines, achieving improvements, especially in domain-specific tasks like Financial, with 30% higher performance on Llama2-70B. SCARA maintains comparable resilience against recovery attacks.

### Strengths
1. The paper introduces SCARA, a method that selectively closes only the bottom layers of semi-open large language models (LLMs) to enhance customizability while maintaining resilience against recovery attacks.
2. It provides a theoretical analysis of the existence of a transition layer in transformer-based models.

### Weaknesses
1. **Unclear Motivation for Semi-Open Models:** The market is dominated by closed-source models and fully open-source models. If customization needs are already addressed by existing fine-tuning services provided for closed-source models (e.g., API-based fine-tuning on closed models like GPT-4), it would be insightful to understand the specific motivations and advantages driving the development of a semi-open architecture. The paper does not adequately address why a user would prefer a semi-open model over fine-tuning a closed-source model or using a fully open-source model, especially considering the added complexity of managing a partially closed system. The value proposition for this approach is not clearly established, particularly when considering the existing landscape of LLM deployment and customization.
2. **The threat model is not clear.** The threat model concerning recovery attacks on semi-open LLMs is insufficiently defined. The paper does not clearly specify the adversary's capabilities, such as the extent of access to the model's architecture, parameters, or outputs. It is unclear whether the adversary has white-box access to the open-source layers, or if they only have black-box access through API calls. The paper also does not specify what constitutes a successful recovery attack. This lack of clarity makes it challenging to assess the effectiveness of the proposed SCARA method in mitigating such threats. A more rigorous definition of the adversary's capabilities and goals is needed to properly evaluate the security claims.
3. **Insufficient Details on SCARA's Implementation:** The description of SCARA's methodology is vague, particularly regarding the fine-tuning-free metric used to determine which layers to keep closed-source. The paper does not provide a clear explanation of how this metric is calculated, the data required, or the computational resources involved. Specifically, the paper lacks details on the composition of the dataset used for evaluating the recovery difficulty, the specific loss function used, and the method for approximating the expectation over random initializations. Without these details, it is difficult to reproduce or validate the results. The paper also lacks a discussion on the sensitivity of the metric to different datasets or initialization schemes.
4. **Evaluation minors:** While the authors present experimental results across multiple models and tasks, the evaluation lacks depth. The paper does not offer a comprehensive analysis of SCARA's performance compared to existing methods, nor does it explore potential trade-offs between customizability and security. The evaluation does not include comparisons with other methods for model partitioning or selective parameter updates. Furthermore, the paper does not analyze the impact of the number of closed-source layers on downstream performance and recovery resilience. A more thorough exploration of these aspects is needed to fully understand the strengths and limitations of SCARA.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a method for identifying which layers in the model that, if recovered by an adversary in an iterative layer recovery process, will make subsequent layers easier to recover.

### Strengths
The evaluation seems comprehensive. It was easy to follow the problem setup and the method.

### Weaknesses
I question the threat model that the authors are introducing. I don't think there's any chance of stealing an LLM through any method that exists no matter how semi-closed/semi-open it is. The only methods that have been proposed that can do something like this specifically target the embedding layer.

It seems like the main insight of the paper, that hiding the earlier layers in the model is more impactful than hiding later layers because if an attacker wants to recover the model they'll pay an accuracy error scaling in the depth of the model past the layer they haven't yet recovered, is trivial. If you asked someone who had never heard anything about this literature of hiding layers, whether they should hide the first block or the last block, I'm certain everyone would choose to hide the first block. There's plenty of work already showing that later layers are more or less redundant and don't learn anything new. This is because attention heads in block N have the ability to learn Nth order interactions, but for N > 2, these interactions typically don't get learned and the attention heads just degenerate [1].

The actual implementation of the method is not sophisticated. It just takes this straightforward insight and turns it into a metric. But that metric is itself just "what happened if I closed the first N layers of the model" and then returns the first one that passes some threshold of difficulty.

It doesn't seem like the evaluation is really fair. The authors evaluate against SEM. But SEM just wants to recover the embedding and the authors are trying to show what happens if they hide the early parts of the network. This seems like an indication that this isn't a particularly realistic threat model.

### Questions
n/a

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of how to design semi-open models (i.e., models whose weights are only partially open-sourced) that can simultaneously also be resilient to recovery attacks. The paper finds that a transition layer exists, such that even small recovery errors in layers before this layer can lead to recovery failure. Building on these insights, the paper proposes an approach called SCARA that keeps only a few bottom layers as closed-source. With this new approach, the paper shows that it is possible to improve downstream customization performance while maintaining similar resilience.

### Strengths
1. The paper is well-written, and the presentation is clear and clean. 

2. The approach is well motivated --- it first starts from an empirical observation that closed-sourcing the first two layers offers significantly greater resilience than the last two, while the model shares similar customizability under the two cases. This implies that close sourcing the later layers may be the optimal solution for keeping the resistance to recovery attacks. The paper subsequently further formally establishes this finding with rigorous theoretical analysis, showing the existence of a transition layer such that even small recovery errors in layers before this layer can lead to recovery failure. This also intuitively makes sense --- when the attacker is asked to recover the earlier layers as opposed to the later layers, the errors in early layers will be amplified by later layers. This asymmetry is natural. 

3. Based on this insight, the paper also proposes an effective approach for the selectively closed-sourcing model to defend against recovery attacks. The experiment results support the effectiveness of the approach. 

Overall, the paper is nicely done.

### Weaknesses
One outstanding weakness of this paper is that the threat model considered may not be practically relevant. It seems the authors coined the semi-open model's scenario, that seems not really exist in the real world.

Currently, the most common setups are either open-source or closed-source. For close-source context, when developers do want their users to customize their models, the standard practice is to deploy fine-tuning APIs (e.g., https://platform.openai.com/docs/guides/fine-tuning) rather than partially open-source a part of the model. It seems to make no sense to only open-source the first few layers of a model to enable customization. Because the customization anyway still needs the involvement of the closed-source developers --- so they can fine-tune and connect the first few layers and the later layers to really deploy the model. Then, why not just close-source all weights and directly ask the users to upload custom data, and then the closed-source developers fine-tune and deploy the model for the users, like what is being done in fine-tuning APIs?

I worry that if not developers will do the partial open-sourcing like the authors of this paper consider, then the problem itself may not hold.

### Questions
Can the authors explain and clarify why the semi-open models are practically relevant?

### Soundness
3

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
4

### Summary
This paper presents SCARA, a method to identify decoder layers to hide in decoder-only LLMs. The authors provide theoretical proof of transition layers, where early errors are amplified in subsequent layers. They introduce RD to assess post-recovery performance when specific layers are hidden. Experiments show that SCARA, by hiding only a few layers, achieves a recovery ratio close to baselines while maintaining customization performance similar to fully open approach. The experiments also confirm the existence of transition layers in the models.

### Strengths
1. The paper is well-written, featuring thorough experiments and clear explanations from both theoretical and empirical perspectives.
2. The overall layout is visually pleasing, and the figures are diverse and effectively illustrate the content, aiding readers' understanding.
3. It proposes a straightforward and effective method for constructing a semi-open model by hiding only a few layers, while achieving baseline-level resilience and customization performance comparable to the fully open setting.
4. The insight regarding the existence of a transition layer contributing to resilience is particularly compelling, with a detailed theoretical explanation that enhances understanding.
5. The authors provide comprehensive empirical validation across multiple architectures and benchmarks, covering models of various sizes (1.3B-70B), and testing customizability and recovery performance on several benchmarks. They also conducted experiments on recovery datasets of different sizes, demonstrating sufficient experimental rigor.
6. The authors proposed additional enhancements to the original baseline, strengthening the protection of baseline SAP and highlighting SCARA’s effectiveness in preserving resilience.
7. The authors empirically validated their theory of the transition layer’s existence and pointed out that smaller models exhibit transition layers earlier than larger models.
8. The authors clearly identified the limitations of the SCARA method, noting its ineffectiveness on small models (OPT-350M) and its inability to defend against other adversary attacks.
9. The proposed SCARA algorithm has clear practical applications, offering a viable solution for enhancing the customizability of semi-open models while preserving comparable resilience.

### Weaknesses
1. One mathematical notation in Section 4.2 is unclear. The loss function $\ell$ for RD(I) is not specified, making it confusing. Specifically, the paper introduces RD as a measure of recovery difficulty but does not define the loss function used to calculate it. This lack of clarity makes it difficult to understand how the recovery difficulty is actually quantified and how it relates to the model's performance. The paper should explicitly state whether the loss function is cross-entropy, mean squared error, or another type of loss, and provide justification for the choice.
2. Figures 1 and 2 have minimal captions and small text, reducing readability and limiting their ability to convey insights. The figures lack sufficient context, making it challenging for the reader to grasp the key takeaways without referring extensively to the main text. For instance, Figure 1 should clearly label the axes and explain the significance of the different curves. Similarly, Figure 2 needs more detailed captions to explain the experimental setup and the implications of the results shown. The small text size further exacerbates the issue, making it difficult to read the labels and annotations.

### Questions
1. Is the "attack datasets" mentioned in Figure 2 the same as the "recovery datasets" discussed later in the paper?
2. Could you clarify the formula and the loss function used for RD(I)?
3. Could you clarify how fully-closed and semi-open models differ in practice?
4. Could you explain more about the distinctions between FT-all, FT-closed, and SEM in Section 5.1?
5. Can the row and column headers in the tables be made clearer by avoiding abbreviations?
6. Could you explain more about potential future work that could be included in the paper?
7. Could the authors clarify what the value 0.00 represents in Table 1 and Table 2?
8. The authors discussed the impact of datasets of different lengths on the effectiveness of SCARA in the experimental section, but these datasets did not appear in the setup. Could the authors provide a detailed introduction to the composition of these datasets?

### Soundness
3

### Presentation
3

### Contribution
4
