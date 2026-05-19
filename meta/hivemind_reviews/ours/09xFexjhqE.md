## Summary
AutoLoRa proposes disentangling the optimization of natural and adversarial objectives in robust fine-tuning (RFT) by routing the natural objective through a LoRA branch while keeping the feature extractor for the adversarial objective. This architectural separation directly addresses the problem of divergent gradient directions between the two objectives, which the paper empirically documents. Additionally, AutoLoRa introduces heuristic schedulers for learning rate and loss-balancing scalars to reduce hyperparameter tuning. The method is evaluated across six downstream tasks with ResNet-18/50 backbones, reporting consistent improvements over vanilla RFT and TWINS.

## Strengths
1. **Well-motivated architectural fix for a documented problem**: Section 3.2 defines gradient similarity (GS) and shows empirically that vanilla RFT and TWINS produce near-orthogonal gradient directions between natural and adversarial objectives (Figure 1a). The paper then designs a targeted solution — routing natural-objective gradients through a LoRA branch to prevent them from conflicting with adversarial-objective gradients in the feature extractor. The motivation is clear and the intervention is directly responsive to the identified problem.

2. **Consistent empirical gains across diverse settings**: Tables 1–2 show AutoLoRa outperforming vanilla RFT and TWINS on all six downstream tasks (CIFAR-10/100, DTD-57, DOG-120, CUB200, Caltech-256) with both ResNet-18 and ResNet-50 backbones, under both PGD-10 and AutoAttack evaluation. The improvements are consistent (e.g., +2.03% on CIFAR-100 with ResNet-18, +3.03% on DOG-120 with ResNet-50), and statistical tests (Table 7, referenced) were conducted across three runs.

3. **Parameter-efficient and inference-overhead-free**: The LoRA branch introduces <5% additional parameters relative to the feature extractor (Table 4) and is dropped at inference time, making the method practical for deployment.

4. **Ablation studies on key design choices**: The paper investigates rank $r_{\text{nat}}$, the sharpening parameter $\alpha$, pre-training budget $\epsilon_{\text{pt}}$, and vision transformer backbones (ViT, DeiT), providing insight into how these factors affect performance.

## Weaknesses
### Fatal
None.

### Major

1. **Insufficiently specified baseline configuration**: The paper states it follows the settings of TWINS (Liu et al., 2023) for training epoch count ($E=60$) and pre-trained model budget, and describes shared optimizer/weight-decay settings. However, it does not explicitly state whether the baseline methods (vanilla RFT and TWINS) were configured with their *optimal* hyperparameters (e.g., the per-dataset grid-search results from the original TWINS paper) or whether they were simply given the same fixed hyperparameters as AutoLoRa. Since TWINS originally required per-task tuning to achieve its reported results, this ambiguity makes it impossible to determine whether the reported gains reflect genuine architectural improvement or partially under-tuned baselines. The paper would be substantially strengthened by stating: (a) whether published best hyperparameters from the original papers were used for each dataset, or (b) whether a hyperparameter search was conducted for baselines, and (c) if neither, acknowledgment that the comparison favors AutoLoRa.

### Minor

1. **Undefined notation $\bar{\theta}_1$ in Eq. (5)**: The notation $\bar{\theta}_1$ appears in the natural objective of Eq. (5) (line 107) without being redefined in the context of the proposed method. It was originally introduced in §3.1 for TWINS, where $\bar{\theta}$ has frozen BN statistics. For AutoLoRa, the surrounding text clarifies that "the FE parameters $\theta_1$ are updated only by the adversarial objective" (line 110), which implies $\bar{\theta}_1$ is a detached/frozen copy. This interpretation is recoverable but the paper should explicitly restate the definition for Eq. (5) to avoid ambiguity.

2. **Missing ablation: AutoLoRa without the automated LR scheduler**: Table 9 shows that TWINS benefits from the automated LR scheduler, but the paper does not ablate AutoLoRa itself by removing the automated LR scheduler. Since the scheduler is part of the full AutoLoRa method, it is unclear how much of the gain comes from the LR schedule versus the disentanglement structure itself. An ablation run (AutoLoRa with a fixed LR schedule) would disentangle these contributions.

### Trivial
None.

## Suggestions
1. **Clarify baseline setup explicitly**: State in §5 whether TWINS and vanilla RFT used hyperparameters from the original papers' grid-search results (per dataset), or whether they were run with the same fixed defaults as AutoLoRa. If the latter, acknowledge that this may disadvantage the baselines.

2. **Redefine $\bar{\theta}_1$ in §4.1**: Add a short sentence: "Here, $\bar{\theta}_1$ is a frozen copy of $\theta_1$ (no gradients flow to $\theta_1$ from the natural objective), so only the LoRA branch parameters $A,B$ receive gradients from the CE term in Eq. (5)."

3. **Add an ablation of AutoLoRa without the automated LR scheduler**: Run AutoLoRa with a fixed Cosine annealing or step-decay LR schedule and report the result alongside Table 1. This cleanly separates the contribution of the disentanglement from the contribution of the scheduler.

4. **Provide the explicit update rule for $\lambda_1, \lambda_2$**: Even a simple rule such as $\lambda_1 = 1 - \text{acc}_{\text{std}}$, $\lambda_2 = \lambda_2^{\text{max}} \cdot \text{acc}_{\text{std}}$ (with a minimum floor) would make the method reproducible from the main paper alone.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
