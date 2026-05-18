- Decision: Accept
- Scores: 8, 6, 8, 6

## Merged Review

### Summary
This work presents DynMoE, a mixture-of-experts approach with two mechanisms: (1) a top-any gating method that lets each token automatically determine the number of experts to activate via a learnable per-expert threshold, and (2) an adaptive process that grows or shrinks the total number of experts during training by tracking expert utilisation. The method is evaluated on vision, language, and vision-language tasks, and shows comparable performance to well-tuned fixed top-\(k\) MoE configurations while activating fewer parameters. The elimination of hyperparameter tuning for the number of experts and activated experts is the core motivation.

### Strengths
- The two proposed mechanisms together achieve an expert architecture that automatically decides both the number of expert activations per token and the total number of experts, addressing two key burdens in using MoE.
- The method is relatively simple, which may be regarded as an advantage.
- The main evaluation is relatively thorough in terms of number of datasets and models, covering vision, language, and a multimodal (vision-language) setup.
- The paper clearly analyzes issues with fixed top-\(k\) routing, particularly why it may be suboptimal.
- The authors consider the extreme case where all experts could be activated in top-any routing and design a regularization loss to prevent that.
- Writing logic is clear and the paper is readable, helping readers understand the contribution.
- The studied problem is interesting and well-motivated (MoE design has been hand-tuned previously).
- The proposed method is novel and reasonable; empirical evaluation provides useful insights.

### Weaknesses
- **Hardware efficiency concerns**: The paper does not explain why the engineering challenges that led to fixed top-\(k\) routing (e.g., efficient use of compute units, load balancing for hardware utilization) do not apply to top-any routing, how hardware has changed to make these concerns less important, or whether the approach would scale to utilize hardware as efficiently as fixed top-\(k\) routing.
- **Gradient signal clarity**: It is unclear what mechanisms optimize the gating and thresholds; the only gradient appears to come from the \((1/k)\) factor in eq. (6), which may not provide per-expert specific gradient directions.
- **Limited novelty and missing citations**: The idea of dynamically selecting the number of executed experts per token is not new (references [1–4] omitted in the original paper) and these works are not discussed in the related work section.
- **Lack of comparison to existing MoE methods**: Only a single baseline (one top-\(k\) MoE variant) is compared. Empirical comparison with other top-any methods and alternative MoE variants (e.g., Swin-MoE, VoE, Switch Transformer, Mistral MoE, DeepSeek-MoE on language; baseline comparisons also needed for vision tasks) would strengthen the contribution.
- **Unconvincing real latency/throughput evaluation**: The claim about speedup is unclear; the statement that MoE-LLaVA uses the expert dispatching implementation from DynMoE with fixed top-\(k\) suggests an unfair comparison. Overhead from the non-constant number of token-expert executions is not measured, and throughput of dense models is not reported for comparison.
- **No from-scratch training experiments**: All experiments are conducted on pre-trained models converted to MoE during fine-tuning; from-scratch training (the original MoE setup for scaling up parameters) is not demonstrated.
- **Standard deviations not reported**: Scores are said to be averaged over three random seeds, but standard deviations are absent, making significance hard to judge (especially for close results in Tables 1, 2, 3, and Figure 4).
- **Method description and experimental setup inadequately explained**: Several aspects remain unclear (see questions below). Readability and grammar issues also noted (e.g., incomplete sentences).
- **Hyperparameter \(G\)**: In top-any routing, is \(G\) a hyperparameter that must be predefined? Could this lead to cumbersome tuning?
- **Expert importance weighting**: By default, selected experts are considered equally important; whether introducing varying importance levels for different experts would improve results is not ablated.
- **Training time**: Why does the top-any MoE training strategy not increase training time?
- **Diversity loss explanation**: Elaboration is needed on how the diversity loss in the auxiliary loss prevents activating all experts simultaneously.
- **Expert removal criteria**: The exact removal logic is unclear (e.g., if expert \(x\) is activated in the first 299 of 300 steps but not the 300th, is it removed? Or if activated only in the first step, is it removed?).
- **New expert initialization**: For added experts, would averaging the weights of other experts or random initialization yield better results?
- **ImageNet experiments**: For vision tasks, larger backbones on the well-known ImageNet dataset are not used; MoE is designed for larger scales.
- **Discussion of advantages over conventional backbones**: It would be useful to discuss the advantages of this MoE design over conventional backbones at the same computation budgets.
- **Literature review on dynamic networks**: The work relates to dynamic neural networks (e.g., layer skipping when 0 experts selected); this connection is not discussed.
- **Improvement only on subset of results**: Improvements over the baseline are visible only on a subset of the results.
- **Load balance and sparsity**: One reviewer originally had concerns about load balancing and efficiency; after rebuttal the authors added a load-balance loss and an efficiency loss (as suggested), and that reviewer raised their score from below acceptance to accept. (Preserved as evidence of a concern that was later addressed to that reviewer’s satisfaction.)