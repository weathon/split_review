Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies privacy-preserving parameter-efficient fine-tuning (PEFT) over APIs. It analyzes label leakage in standard PEFT and proposes P³EFT, a two-party split-learning protocol with two components: (1) gradient obfuscation via additive secret sharing exploiting the linearity of backpropagation, and (2) activation obfuscation via training multiple adapter copies with random mixing weights and an adversarial regularizer. The method is evaluated on DeBERTa-v2-XXLarge and Flan-T5-Large on SST-2 and MRPC.

## Strengths

- **Clean exploitation of backprop linearity for gradient protection.** Section 3.2 formally observes that backprop is linear in output gradients (Eq. 1). This enables an additive secret-sharing scheme (Algorithm 1) where the client sends noisy gradient vectors to different servers and recovers the exact true gradient as a linear combination of the results, introducing zero degradation to training dynamics — a meaningful advantage over methods that modify the loss or architecture.

- **Effective empirical demonstration of label leakage in standard PEFT and gradient obfuscation.** Figure 1 shows that k-means clustering on gradients or activations from standard LoRA fine-tuning recovers training labels. After applying the privacy-preserving backpropagation, an XGBoost classifier achieves at most 50.4% accuracy on a balanced test set (Section 4.1, line 187), confirming that the gradient-level obfuscation erases useful label information from individual servers.

- **Creative use of PEFT's parameter efficiency for activation protection.** The multiple-adapter strategy with mixing weights (Section 3.3) is a novel idea that exploits PEFT's compact parameter footprint — maintaining multiple adapter copies is practical precisely because they are small. The construction of mixing weights (Eq. 3-4) guarantees that the combined model initially equals the average of adapter outputs, preventing early label leakage from activations.

- **Evaluation on realistic-scale models and standard NLP benchmarks.** The experiments use DeBERTa-v2-XXLarge (900M+ parameters) and Flan-T5-Large on GLUE tasks, going beyond the smaller-scale settings common in prior split-learning work and demonstrating practical viability for real-world API fine-tuning.

- **Multi-metric privacy evaluation with a strong baseline.** The paper reports three complementary privacy measures (spectral attack AUC, norm attack AUC, logistic regression accuracy) and compares against the Distance Correlation defense (Sun et al., 2022), a legitimate prior method. The sensitivity analysis (Figure 5) varies regularizer coefficients to explore the accuracy-privacy Pareto frontier.

## Weaknesses

### Fatal
None.

### Major

- **Threat-model tension with the primary motivated use case.** The paper's privacy guarantees rely on servers being independent and non-colluding ("we assume that servers are independent and do not communicate client's data between each other," line 83). However, the introduction motivates the work primarily through centralized APIs such as OpenAI, Hugging Face, and OctoAI (line 21), where all API calls go to a single organization that can trivially correlate queries. The paper acknowledges this ("If both requests are processed by the same server, it can obviously recover $g_h$," line 119) and suggests TEEs as an alternative (line 128), but TEEs are not evaluated, their security assumptions are fundamentally different, and they are not universally available. This gap means the protocol's strongest privacy guarantees apply cleanly only to decentralized settings (e.g., Petals), while the centralized-API scenario — which the paper repeatedly invokes — is not adequately addressed.

- **Unsubstantiated claim about the adversarial regularizer.** Section 3.3 states that the adversarial regularizer "ensures that it is impossible to predict labels from individual adapters $h(x,\theta_i)$" (line 163). This is presented as a definitive guarantee, but no formal proof, convergence analysis, or rigorous empirical validation of this impossibility is provided. The regularizer is a heuristic inspired by Ganin & Lempitsky (2015); the paper provides no evidence that it drives individual adapter activations to become label-independent in any measurable sense beyond the specific attacks tested. The claim should be softened to reflect the empirical nature of the defense.

- **Missing ablation isolating the contribution of the adapter mixing defense.** The multiple-adapter strategy with mixing weights and the adversarial regularizer is the paper's main novel contribution for activation protection, yet no ablation study separates the effects of: (a) the mixing weights alone, (b) the adversarial regularizer alone, (c) training multiple adapters without either. The sensitivity analysis (Figure 5) varies the regularizer coefficient, which partially addresses how the regularizer strength affects the trade-off, but does not isolate whether the privacy gains come from the mixing weights, the regularizer, or simply from training multiple weak adapters.

- **No evaluation against a stronger attacker with access to all adapters' activations.** The paper tests attacks on individual servers' views (gradients from one server, activations from individual adapters). However, the most dangerous attacker for the activation-protection component would have access to the concatenated activations of all $n$ adapters simultaneously (as a single malicious server could, or multiple colluding servers). The mixing weights protect against this only if their randomness is unknown to the attacker, but the paper does not test whether an end-to-end neural network trained on all adapter activations can predict labels. This is a critical missing stress test.

### Minor

- **Key quantitative results reported only in figures without numeric tables.** The main results (Figures 4 and 5) are presented visually without accompanying numeric tables, and trade-offs are described qualitatively ("slightly better trade-offs," line 207). This makes it difficult to assess the statistical significance of differences or to reproduce exact values.

- **No comparison against standard gradient perturbation defenses.** The baselines include Distance Correlation (a related defense) and unregularized training, but not straightforward gradient-noise or gradient-clipping baselines (e.g., adding calibrated Gaussian noise to gradients, which is standard in privacy literature). Such comparisons would help establish whether the complexity of the proposed protocol is justified over simpler alternatives that also work in the single-server setting.

- **Limited discussion of protocol limitations and overhead.** The conclusion (Section 5) is brief and does not discuss key limitations: the server-collusion issue, the computational/communication overhead ($m \times n$ more API calls per step), the dependence on the non-collusion assumption, or the lack of formal privacy guarantees. The paper also does not report actual training times or cost implications of multiplying API calls.

### Trivial
- The discussion of differential privacy (line 53) oversimplifies by claiming it is "not applicable" because the server knows example participation. Per-sample DP guarantees remain meaningful even when participation is known. This does not affect the paper's core contribution, which does not rely on DP.

## Nice-to-Haves
- A case study visualizing the mixing weights' effect on adapter outputs (e.g., PCA of individual adapter activations vs. the combined output) would help illustrate whether the approach actually decorrelates individual adapters from labels.
- A formal discussion of what an attacker can and cannot infer given the information available at each server (gradient shares, individual adapter activations, parameter updates across steps) would strengthen the paper's framing.

## Removed Points
These points from the original reviews are flagged to be removed — treat them with caution:

- **Point about re-identification from model outputs / membership inference**: This concern did not appear in any review as a primary weakness; included for completeness.
- **Critique that "after one step, adapters diverge, and the mixing weights no longer preserve any simple property"** — This is a misunderstanding: the mixing weights are not designed to preserve a specific functional property after divergence; they are designed to obfuscate individual adapter outputs, and the paper explicitly states that after the first step $h'$ becomes an average of adapter predictions. This is by design, not a flaw.
- **Critique that "provably obfuscate the gradients" is misleading** — The "provably" qualifier specifically modifies "obfuscate the gradients communicated during fine-tuning" (line 32). The gradient obfuscation in Section 3.2 is provably correct (linearity of backprop ensures exact recovery of $g_\theta$ while each server sees only noise). The claim does not extend to activation obfuscation. This reading is consistent with the paper's structure.
- **Critique questioning the XGBoost experiment** — The reviewer called 50.4% accuracy "essentially random guessing" and said this is "the easy case." The XGBoost result is presented to validate the gradient obfuscation mechanism, which is a necessary building block of the full protocol. The activation protection (the harder case) is separately addressed in Section 3.3 and evaluated via the three privacy metrics in Section 4.2.
- **Claims that baselines are not fairly compared** — "Training w/o LoRA adapters" is presented as a reference lower bound for accuracy, not as a comparable privacy defense. The paper is transparent about what this baseline represents.

## Novel Insights
None beyond the paper's own contributions. The review process does not surface a fundamentally new observation about the paper's approach that is not already articulated by the authors.

## Suggestions

1. **Address the threat-model gap explicitly.** Either (a) reframe the paper's target setting as decentralized fine-tuning (Petals-like systems) where the non-collusion assumption holds naturally, and relegate centralized APIs to future work with TEEs, or (b) evaluate the protocol under a TEE-based implementation and discuss its limitations. The current framing creates an expectation the protocol cannot meet.

2. **Add ablation experiments.** Isolate the effect of: (a) training multiple adapters without mixing weights, (b) mixing weights without adversarial regularizer, (c) adversarial regularizer without mixing weights. This is essential to attribute privacy gains to the right component.

3. **Test a stronger attacker.** Evaluate an attacker that has access to the concatenated activations (or gradients) from all adapters simultaneously, e.g., a neural network trained to predict labels from the union of all adapter outputs. This directly tests whether the mixing weights provide meaningful protection when servers collude or when a single server hosts all adapters.

4. **Provide numeric tables for key results.** The main results (Figures 4, 5) should be accompanied by tables with exact accuracy/F1 and privacy metric values to improve reproducibility and allow precise comparison.

5. **Soften the claim about the adversarial regularizer.** Replace "ensures it is impossible" with "aims to prevent" or "empirically reduces the ability to predict," and acknowledge the lack of formal guarantees.

6. **Report training time and API call overhead.** For the $m=n=2$ case, the protocol makes 4× the API calls per step. Reporting wall-clock time and cost implications would help practitioners assess practicality.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>