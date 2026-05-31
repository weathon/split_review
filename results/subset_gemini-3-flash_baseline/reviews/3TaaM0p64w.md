## Summary
The paper introduces Fed-MADS (Federated Minimax Active Data Selection), a framework designed for Federated Active Learning (FAL) in the context of explainable models. The core contribution is a data selection strategy derived from the Information Bottleneck (IB) principle. By treating the global model as a variational distribution for the local model's training dynamics, the authors derive a minimax objective that selects unlabeled samples exhibiting the highest divergence between local and global models in both latent representations (KL-divergence) and final predictions (cross-entropy). Experiments on four datasets using the LR-XFL framework show improvements in model accuracy and rule-based explainability metrics.

## Strengths
- **Theoretical Grounding:** The derivation of the data selection score from the Information Bottleneck principle is elegant. It provides a formal justification for using the global model as a reference point to measure the "informativeness" of local data.
- **Focus on Explainability:** Unlike most FAL papers that focus solely on accuracy, this work specifically targets Explainable Federated Learning (XFL). It evaluates "rule accuracy" and "rule fidelity," which are critical for high-stakes domains like medical (MIMIC-II) or financial (Credit Card) applications.
- **Efficiency:** The proposed selection score ($s_1 + \beta s_2$) is computationally lightweight, requiring only forward passes through the local and global models, making it practical for resource-constrained federated clients.
- **Strong Empirical Results:** The method consistently outperforms several baselines (FedAL, LoGo, KSAS) across diverse datasets, particularly in the low-budget regime (0–250 queries).

## Weaknesses
### Fatal
None.

### Major
- **Assumption of I.I.D. Data:** The paper explicitly states in Section 3.1 that it focuses on "horizontal FL scenarios with i.i.d. data." However, the primary challenge and motivation for most Federated Active Learning research is the Non-I.I.D. (heterogeneous) nature of decentralized data. In an I.I.D. setting, the global model is a very strong proxy for the local distribution, which simplifies the problem significantly. The paper would be much stronger if it addressed how Fed-MADS handles label or feature skew.
- **Baseline Performance:** In Figure 2, the "Random" baseline performs surprisingly well, often outperforming specialized FAL methods like LoGo and KSAS, and staying close to Fed-MADS in some cases (e.g., MIMIC-II). This raises questions about the difficulty of the active learning task in the chosen experimental setup or the tuning of the baseline methods.

### Minor
- **Sensitivity to $\beta$:** While the ablation study shows robustness, the optimal $\beta$ varies across datasets. The paper suggests selecting $\beta$ via a validation set, but in many FL/AL scenarios, the validation set is extremely small or non-existent at the start of training.
- **Global Model Dependency:** As noted in the conclusion, the method relies on the global model being somewhat "mature." In early rounds of FAL, the global model might be poor, potentially leading the KL-divergence term to select noise or outliers rather than informative samples.

### Trivial
- The term "Minimax" is used to describe the selection of samples that maximize the loss/objective, which is standard in AL, but the "mini" part (model training) is kept standard. The "unification" claimed is more of a conceptual alignment than a joint optimization.

## Nice-to-Haves
- An evaluation under Non-I.I.D. settings (e.g., Dirichlet distribution for label skew) to see if the divergence between local and global models remains a reliable signal for informativeness when distributions differ inherently.
- A comparison of communication overhead (though the authors claim it is zero for selection, the frequency of global model downloads for AL purposes could be discussed).

## Novel Insights
The most significant insight is the application of the Information Bottleneck principle to derive a dual-level selection criterion for FAL. Specifically, the paper demonstrates that informativeness in an explainable model is not just about label uncertainty (output layer), but also about "representation uncertainty" (latent layer). By using the global model as the variational target $Q$, the authors transform a theoretical information-theoretic bound into a practical distance metric between local and global model states.

## Suggestions
- Conduct a small experiment with Non-I.I.D. data to demonstrate the limits or robustness of the "divergence from global model" logic.
- Clarify if the global model used for scoring is the one from the *previous* round or if there is an additional synchronization step before selection.

## Score and Decision
The paper is well-motivated and technically sound. The use of IB to bridge FAL and XFL is a novel and successful contribution. While the I.I.D. assumption is a limitation, the empirical results on explainability metrics provide sufficient value to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>