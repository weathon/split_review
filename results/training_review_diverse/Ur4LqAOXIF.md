Now I have a thorough understanding of the paper and all the claims. Let me write the consolidated review.

## Summary

The paper formalizes an online OOD detection problem where the detector can continuously adapt to a stream of environment data, proposes the SODA algorithm that updates a classifier and OOD detector via online gradient descent using per-sample environmental feedback, provides a regret bound under online convex optimization assumptions, and demonstrates empirical results on CIFAR-10 and ImageNet-1k.

**Paper type**: New-method paper with theoretical analysis and empirical validation.

---

## Strengths

1. **Formalization of a novel online OOD detection problem with non-stationary OOD**. The paper provides the first rigorous problem statement (Section 2.1) where the environment distribution Q_t^env = (1-π_t)P^in + π_t P_t^out allows OOD to change over time, generalizing prior stationary in-the-wild formulations (Katz-Samuels et al., 2022). This framing is underexplored in the literature and opens a genuine new direction for OOD detection research.

2. **Theoretical regret guarantee**. Theorem 3.1 provides an O(√T) regret bound under standard online convex optimization conditions, establishing that the online detector converges to the optimal detector at a sub-linear rate. This type of convergence guarantee is absent from all prior offline OOD detection methods and is a meaningful theoretical contribution for the proposed setting.

3. **Demonstrated adaptability to non-stationary environments**. Figure 1b shows that SODA recovers from distribution shifts (spikes in regret when OOD switches every Δ=4,800 timesteps) and maintains an overall sub-linear regret trend. This capability—adapting to ever-changing OOD distributions—is validated empirically and is a genuine advantage over static offline detectors.

4. **Flexibility across OOD scoring functions**. Section 4.3 demonstrates that SODA can be instantiated with MSP, ODIN, and Energy scoring functions by modifying L_t^id and L_t^ood, achieving competitive results across instantiations. This makes the framework a general recipe rather than a single-purpose algorithm.

5. **Improved performance over WOODS, a method that also uses environment data**. On ImageNet-1k, SODA reduces FPR95 by 18.54% compared to WOODS (Katz-Samuels et al., 2022), which also sees OOD mixture data but trains offline. This provides a meaningful (though imperfect — see Weaknesses) comparison showing the benefit of online adaptation.

---

## Weaknesses

### Fatal
None.

### Major

1. **The paper compares SODA against offline methods that never see OOD data, then cites the gap as evidence of superiority — but the asymmetry is not controlled.**  
   Offline baselines (MSP, ODIN, Energy, KNN+, etc.) in Table 1 are static detectors derived from a pre-trained ID classifier with zero exposure to OOD samples. SODA, by contrast, receives per-sample OOD labels (and ID class labels) during deployment and continuously trains on them. The large performance gap is therefore expected — any method that receives labeled OOD data will trivially outperform methods that do not. The paper acknowledges this asymmetry only for the WOODS comparison (Section 4.2, "Comparison with Method Using Offline Environment Data") but still headlines "significantly outperforms offline counterparts." The proper baselines would be methods that also receive the same labeled stream data — e.g., retraining on all accumulated labeled data at each timestep, or a dynamic support-set approach. Without such controlled comparisons, the empirical contribution is weakened.

2. **The paper's scope is narrower than its framing suggests: it requires per-sample oracle feedback (both OOD labels and ID class labels) during deployment, a strong assumption that is not clearly scoped.**  
   Algorithm 1 and the full SODA algorithm assume the environment provides feedback on every sample: whether it is OOD and, if ID, its class label. In real-world OOD detection, such feedback is typically unavailable — the entire challenge is detecting unknowns without labels. The paper mentions "a straightforward unsupervised extension" in one sentence (line 18) but provides zero description, zero experiments, and zero analysis of it. The self-driving car example (line 12) does not naturally motivate the availability of per-sample ground-truth labels. The paper would be significantly stronger if it either (a) clearly scoped itself as "online OOD detection with environmental feedback" (a valid but narrower setting, e.g., human-in-the-loop or active learning scenarios) and removed the unsupervised extension claim, or (b) actually implemented and evaluated the unsupervised variant.

3. **The regret analysis assumes convex optimization but SODA optimizes deep neural networks, and the bound contains unmeasured quantities.**  
   Theorem 3.1 cites "conditions commonly found in online convex optimization" (line 93), but SODA optimizes deep neural networks, which are non-convex. No argument bridges this gap. Furthermore, the bound depends on unknown quantities — sup_{x~P^in} ||x||_2, sup_{x~P^out} ||x||_2, the empirical mixture ratio π̃, and constant β — none of which are estimated or bounded in the experiments. Without grounding these quantities, it is unclear whether the bound is empirically meaningful. The claim "linear probing" (line 109) is mentioned as a practical connection, but linear probing is not what is evaluated in the main results.

### Minor

1. **The regret plots (Figure 1) lack a clear definition of what is plotted.**  
   The y-axis is labeled "Regret" and the paper defines cumulative regret in Section 3.2, which must be non-decreasing. However, the description of non-stationary environments mentions regret "spiking" and then "converging," which is consistent with cumulative regret (an increase followed by slower growth). If the curves are cumulative, they should be monotonic. The paper should explicitly state whether the plots show cumulative regret, per-round regret, or a smoothed variant, and ensure the plot format matches the claimed sub-linear convergence.

2. **No online baselines** are compared against. There are no comparisons with simple online learning baselines — e.g., training on all previously seen labeled samples via SGD each round, or fine-tuning only on OOD samples — that would isolate whether SODA's specific loss formulation matters or whether any online update suffices.

3. **No discussion of computational cost.** Updating a deep network every timestep (T=30,000 rounds) is expensive, but the paper reports neither wall-clock time, number of gradient steps per round, nor learning rate schedules.

### Trivial
- The paper refers to "offilne" (typo for "offline") in multiple places (lines 136, 141, 143).
- The word "lim_{T→∞} regret T = 0" in line 89 is missing a division sign — should be lim_{T→∞} regret/T = 0 for average regret convergence.

---

## Nice-to-Haves

- A comparison with offline methods that are retrained on the same labeled stream data (even periodically) would isolate the value of online gradient updates vs. recomputation.
- Estimating or upper-bounding the sup-norm quantities in the regret bound would make the theory more grounded.
- An experiment or discussion of how the framework would work in a setting where only a fraction of samples receive feedback (sparse or delayed feedback) would broaden applicability.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the loss functions L_t^id and L_t^ood are not defined.** The extracted text omits equations between lines 76–79 (the "Out-of-Distribution Loss Function" subsection), likely a PDF parsing artifact — these equations exist in the original submission. The Energy-based loss functions are fully defined in Section 4.3 (lines 166–168). The paper also describes the losses textually ("penalizes overconfidence when observing OOD samples"). This criticism is a parser artifact and does not reflect an author error.

- **Criticism about missing appendix content.** The paper does not reference an appendix, so this does not apply.

---

## Novel Insights

The harsh critic correctly observes a structural tension between the paper's framing (general OOD detection for open environments) and its actual setting (supervised online learning with oracle feedback). This tension is not merely a presentation issue — it cuts across the problem formulation, the experimental design (unfair baselines), and the practical motivation. The strength finder correctly identifies the formalization and regret analysis as genuine contributions. The novel synthesis from these two perspectives is: *the paper introduces a promising online OOD detection framework with theoretical guarantees, but its empirical demonstration and problem framing need to be reconciled with the strong feedback assumption before the claimed advantages over offline methods can be taken at face value.* The most actionable path forward would be for the authors to clearly commit to the supervised-feedback setting (dropping the unsupervised pretense) and add controlled baselines that receive identical labeled data.

---

## Suggestions

1. Reframe the contribution as "Online OOD Detection with Environmental Feedback" — a valid but specific setting. Remove or defer the unsupervised extension claim to future work.
2. Add baselines that receive the same labeled stream data (e.g., periodic full retraining, or a fixed model fine-tuned only on OOD samples) to isolate the benefit of the online gradient update.
3. Clarify whether Figure 1 shows cumulative or per-round regret; if cumulative, ensure monotonicity of the plotted curves.
4. Address the convex-to-non-convex gap in the theory, or at minimum discuss it as a limitation.
5. Report computational cost (wall-clock time, update steps per round) to help practitioners evaluate deployment feasibility.

---

## Score and Decision

**Originality**: Good — the online OOD detection formulation is novel. **Importance**: Moderate — the problem is relevant but the feedback assumption limits applicability. **Claims**: Overclaimed relative to what is demonstrated — the unfair baseline comparisons inflate the empirical claims. **Soundness**: Moderate — the theory is standard online learning theory applied to a new problem but with a convex-to-non-convex gap; the experiments show real improvements but over controlled baselines are absent. **Clarity**: Fair — the framing conflates two settings (with and without feedback). **Value to community**: Moderate — the formalization and regret framework are useful starting points for future work in this direction.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>