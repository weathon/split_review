Now let me do the calibration search to determine the paper's score range.Now let me do the round-2 narrowing search within my initial bracket of 4-6:Now I have enough information to write the complete review. Let me synthesize everything.

---

## Summary

This paper studies federated learning under "openset" noisy labels, where each client observes only a subset of the global label space under noisy conditions. The authors first formally define this problem and convincingly demonstrate that existing transition-matrix-based loss correction methods fail in this setting. They then propose FedDPCont, which aggregates a DP-protected global label distribution and uses it as a contrastive signal to prevent local overfitting to openset noise. Two theoretical results are provided — a labelDP guarantee (Theorem 1) and a federated-to-centralized update equivalence (Theorem 2) — along with empirical evaluation on CIFAR-10/100, CIFAR-N, and Clothing-1M.

---

## Strengths

- **Compelling motivating failure analysis (Section 3.1):** The concrete 3-class transition-matrix example showing that $T_{\text{OptEst}} \neq T_{\text{real}}$ under openset observation is precise and practically compelling; it directly grounds the need for a T-free approach.

- **Formal labelDP guarantee (Theorem 1):** The label-sharing mechanism using the symmetric randomized response matrix $T_{\text{DP}}$ is rigorously shown to satisfy ε-labelDP, addressing a genuine privacy concern in FL label communication.

- **Federated-to-centralized equivalence (Theorem 2):** The paper proves that $\sum_{c \in [C]} \mathbb{P}(\mathcal{D}_c | \mathcal{D}) \cdot \Delta_c^{(r)} = \Delta^{(r)}$, linking the FedDPCont aggregated update to the centralized gradient, which is a meaningful theoretical contribution for the method's calibration.

- **Multi-dataset empirical validation:** The approach is evaluated across CIFAR-10, CIFAR-100, CIFAR-N (human-annotated), and Clothing-1M, including under symmetric noise, random noise, and real-world noise, against eight baselines including FedAvg, FedProx, FedBN, FedDyn, Scaffold, and standard noisy-label methods (loss correction, T-revision, co-teaching). FedDPCont consistently achieves the highest test accuracy.

---

## Weaknesses

### Fatal
None.

### Major

- **Noise-robustness proof is asserted, not demonstrated.** The paper's most consequential theoretical claim is that $\ell_{\text{PL}}$ is robust to label noise in the federated openset setting. The paper states: *"Given Theorem 2, we can further show $\ell_{\text{PL}}$ is robust to label noise as what has been done for centralized training (Liu & Guo, 2020)."* This "further show" never materializes. The centralized robustness result in Liu & Guo (2020) was established under specific assumptions (e.g., the contrastive label drawn independently from features) that may not hold when the contrastive label is sampled from a globally aggregated, DP-corrupted, openset-biased distribution. The conclusion then overstates: *"we have proved that FedDPCont is able to approximate a centralized solution with strong theoretical guarantees"* — but what is actually proved is an expectation-level equivalence (Theorem 2), which the paper itself acknowledges holds only under infinite data. As written, the theoretical framework supports only the privacy and federated-to-centralized calibration properties; the noise-robustness claim that anchors the paper's title contribution is not proved.

- **Critical ablation absent: local vs. global contrastive label distribution.** FedDPCont's specific novelty over generic contrastive regularization is the use of a *globally shared*, DP-aggregated label distribution rather than a local one. The paper's own motivation (Section 3.2) explicitly argues: *"the 'new' label has to be sampled globally; otherwise, the global information is missing and the negative effect of local openset label noise would induce performance degradation."* Despite this claim being central, no experiment compares FedDPCont against a variant that samples the contrastive label from the *local* distribution. Without this baseline, it is not possible to attribute the empirical gains to the proposed label communication mechanism rather than to the general benefit of contrastive regularization (which existing works already provide).

### Minor

- **Definition 1 is formally too broad.** The stated definition — openset noise holds if $\tilde{\mathcal{D}}_c \neq \tilde{\mathcal{D}}$ — is satisfied by virtually any non-IID FL setting and does not specifically capture the missing-class structure that drives the paper's analysis. The informal description (some label classes absent from a client's observed label space) is more precise. Because the theoretical results are ostensibly proved under the formal definition, the mismatch between formal and informal conditions weakens the grounding of the theory.

- **Theorem 2's expectation-level scope is understated.** The paper acknowledges in one sentence that the theorem is "in the expectation level (infinite data size)" but does not further address the finite-sample regime — which is precisely the regime where FL clients operate (small, imbalanced, heterogeneous local datasets). The conclusion's framing of "strong theoretical guarantees" goes beyond what Theorem 2 establishes.

- **Privacy analysis for the recovered label distribution is incomplete.** Algorithm 1 Line 9 broadcasts $(T_{\text{DP}}^\top)^{-1}\check{p}$ — a post-inversion of the DP mechanism applied to the aggregate — to all clients. The paper dismisses the privacy concern with: *"there is no direct evidence of the harm of leaking an imperfect label distribution to the best of our knowledge."* This is not a formal privacy analysis. Theorem 1 covers the per-label DP guarantee but does not cover the privacy properties of this aggregated and inverted quantity. In small-client, few-class settings, the aggregate distribution may be informative about per-client label frequencies.

- **DP stability analysis limited to one dataset/setting.** Section 5.4 studies the effect of ε only on CIFAR-10 with random noise at ratio 0.4. The generalization of this stability finding to CIFAR-100 — where K is 10× larger and ε values are significantly different — is not supported experimentally.

### Trivial

- The conclusion slightly overstates the theoretical contribution by using the phrase "strong theoretical guarantees" for results that are (a) expectation-level only and (b) partially deferred to prior work on centralized noise robustness.

---

## Nice-to-Haves

- Extend the noise-robustness argument even informally: bound the bias introduced by DP corruption in the contrastive term as a function of ε, N, and K. This would help the reader understand when the DP mechanism is sufficiently mild to be practically useful.
- Analyze how closely $(T_{\text{DP}}^\top)^{-1}\check{p}$ approximates the true global label distribution as a function of ε, N, and C. This would justify the specific ε values used in the experiments.
- The contrastive label $\check{y}_{n'}$ has a probability proportional to class frequency of equaling the true class of $x_n$, which causes the second loss term to penalize the correct class. For CIFAR-10 this happens ~10% of the time. While the method works empirically and this mechanism is inherited from prior centralized work, a brief discussion or bound would strengthen the paper.

---

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Section 5.2 body text "missing":** The harsh critic notes the section is empty. This is a PDF/parser extraction artifact (the results table was in image format). Per policy, this is not an author error and is removed.

- **E=5 local update steps undermining Theorem 2:** The critic argues Theorem 2 implicitly requires E=1. However, the paper defines $\Delta_c^{(r)}$ as the "variation of model parameters in the r-th round of local training in client c" — inclusive of all E local steps. Whether the theorem proof is valid for E>1 cannot be determined without seeing the proof itself (which the parser strips). This is speculative given available information and is removed.

- **"Contrastive mechanism failure mode" as fatal:** The critic flags that with probability 1/K the contrastive label equals the correct class, causing the loss to penalize the correct answer. While this is a real (minor) issue, it is not a novel concern — it applies to the entire family of contrastive/negative-label approaches (including Liu & Guo 2020, the paper's basis). The low base rate (10% for CIFAR-10, 1% for CIFAR-100) and consistent empirical success suggest this does not meaningfully undermine the approach. Demoted from major to nice-to-have.

- **Strength: "Formal definition of openset label noise"** — retained as a strength, but weakened by the noted mismatch between Definition 1 and the informal description.

- **Strength: "Robustness to DP level is supported"** — limited scope (CIFAR-10 only, one noise type) prevents this from being a strong supporting strength; kept as minor positive.

---

## Novel Insights

The paper's most incisive contribution is the identification that openset noise in FL creates a systematic bias in transition matrix estimation that cannot be resolved locally, even with access to clean labels — demonstrated analytically in Section 3.1 with the $T_{\text{OptEst}}$ example. The proposed solution of using DP-protected global label statistics contrastively (rather than trying to estimate or correct the local transition matrix) is a genuine reframing of the problem. The result that simply knowing the approximate marginal distribution of labels globally is sufficient to regularize against local openset noise — without needing to estimate client-specific noise matrices — is a practically useful insight even if the theoretical treatment is incomplete.

---

## Suggestions

1. Prove (or formally sketch) the noise-robustness of $\ell_{\text{PL}}$ under the DP-corrupted, openset-aggregated contrastive distribution. At minimum, show how the DP corruption of the contrastive distribution affects the robustness argument from Liu & Guo (2020).
2. Add a "local contrastive" baseline that samples $\check{y}$ from the client's *local* label distribution instead of the global one. This is the single most decisive experiment for validating the method's specific novelty.
3. Tighten Definition 1 to formally reflect the missing-class structure: e.g., $\mathcal{V}_c \subsetneq \mathcal{V}$ or $\text{supp}(\tilde{\mathcal{D}}_c^Y) \subsetneq \text{supp}(\tilde{\mathcal{D}}^Y)$.
4. Extend DP stability analysis to CIFAR-100 to support the generalization claim.

---

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DFL with Noisy Labels (DFLMV) | t8hMqAn8ZG.md | 4.0 | R1/R2 | Most topically similar; also FL+noisy labels; similar theoretical gap issues; paper under review has more formal problem setup and broader empirical scope — slightly stronger |
| DP Clustered FL | rBAnJed1iY.md | 5.0 | R1 | FL+DP, comparable scope; paper under review has less complete theory but more novel problem framing |
| Label Shift in FL (FedPALS) | nwETBpOPiC.md | 4.0 | R2 | FL label distribution issues; paper under review has cleaner motivation and more empirical breadth |
| CONTROL (Open-world SSL + contrastive) | 0Qyxw0cCuu.md | 5.0 | R2 | Open-world + contrastive learning; similar theoretical-gap profile; paper under review comparable in quality |
| FLAIR (FL heterogeneous data) | C7XoUdJ5ZC.md | 3.0 | R1 | Much weaker contribution; paper under review is clearly stronger |
| pFedPLL (Partial label FL) | ehlZFDxwJo.md | 3.0 | R1 | Weaker problem motivation and theory; paper under review is stronger |
| Candidate Label Set Pruning | Fk5IzauJ7F.md | 8.0 | R1 | Accepted strong paper; paper under review is substantially weaker (missing proof, missing ablation) |

**Round-1 bracket:** 4–6.
**Round-2 anchor comparison:**
- Compared to t8hMqAn8ZG (4.0): The paper under review is stronger in problem novelty and empirical scope, placing it above 4.
- Compared to CONTROL/rBAnJed1iY (5.0): Comparable theoretical-gap and missing-ablation profile.
- The missing noise-robustness proof and the absence of the critical local vs. global ablation are genuine major weaknesses that keep the paper from the 6+ range.

**Evaluation on axes:**
- *Originality*: Moderate-high — the specific combination of openset noise + FL + DP contrastive mechanism is novel and not directly addressed in prior work.
- *Importance of research question*: High — openset label noise in FL is practically relevant and underexplored.
- *Claims well-supported*: Moderate — the labelDP and calibration claims are supported; the headline noise-robustness claim is not proved; the empirical improvement claim is shown but without the critical ablation.
- *Soundness of experiments*: Moderate — multi-dataset, multiple baselines, but only 3 seeds, results in image tables, missing the decisive local vs. global ablation.
- *Clarity of writing*: Fair — the motivating example is clear, but Definition 1 is imprecise and some theoretical claims are loosely stated.
- *Value to research community*: Moderate — the problem framing and contrastive approach offer a useful perspective even if the theoretical treatment is incomplete.

**Final score: 5.0 — Reject.** The paper is a borderline contribution with a genuinely useful problem framing and partial theoretical support. The two major weaknesses — the unproved noise-robustness guarantee and the absent local-vs-global ablation — together mean the paper's central claim (that FedDPCont is theoretically and empirically superior due to its globally-shared DP label distribution) is unsubstantiated on the dimensions that matter most. These are fixable in principle but constitute a substantive revision, not a minor clarification.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>