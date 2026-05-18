Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper proposes FTA, a generator-assisted backdoor attack against federated learning that produces imperceptible, sample-specific triggers. The key idea is to train a generative trigger function that makes poisoned samples share similar hidden features with benign samples of the target label, thereby reducing the parameter-level anomalies (P1–P2) that prior universal-trigger attacks exhibit. The generator is continuously trained across FL rounds to adapt to the changing global model. Experiments on four datasets compare FTA against DBA, Neurotoxin, Edge-case, and a baseline attack under multiple FL defenses.

## Strengths

- **Well-motivated problem decomposition (P1–P3).** The paper identifies three concrete failure modes of prior FL backdoor triggers — abnormal feature extraction, abnormal backdoor routing, and perceptible triggers — and uses these to motivate the generator-based approach. This problem analysis is clear and provides a principled framework for understanding why prior attacks fail against defenses.

- **t-SNE visualization provides direct evidence for the claimed mechanism.** Figure 5(a)–(b) shows that under FTA the hidden features of poisoned samples overlap with benign target-label samples, whereas under the baseline attack they form a separate cluster. This directly supports the argument that FTA addresses the abnormality of feature extraction (P1) and enables reuse of benign routing (P2).

- **Empirical resistance to FLAME and norm clipping is demonstrated across multiple datasets.** Figure 4 shows FTA achieving high backdoor accuracy on CIFAR-10 and Tiny-ImageNet under both norm clipping and FLAME, where baseline attacks (DBA, Neurotoxin, Edge-case) remain near zero. These results are the strongest concrete evidence that FTA's parameter similarity to benign updates provides a practical advantage.

- **Imperceptibility of triggers is qualitatively demonstrated.** Figure 2 (trigger visualization) and the residual maps show that FTA's triggers are visually imperceptible compared to the patch-based triggers of baselines, addressing P3.

## Weaknesses

### Major

- **All performance and defense results are presented as coarse figures with no numerical tables.** The abstract claims "above 98% attack success rate" and Section 4.2 claims "above 97% accuracy on average," but the figures show substantial variability (e.g., CIFAR-10 fixed-frequency at ~83% BA after 50 rounds). There are no reported means, standard deviations, or confidence intervals over multiple runs. The defense curves (FLAME on Fashion-MNIST in Figure 4(e)) appear to plateau well below what the text's "<20% degradation" claim implies. The CIFAR-10 claim of "nearly 83% BA after 50 rounds which is 60% higher than other attacks on average" cannot be verified from the figure alone because the y-axis range and precise values are not given. Without numerical precision, the stated effect sizes are unverifiable. This is the single most consequential weakness — it prevents the paper from substantiating its headline quantitative claims.

- **No evaluation against the trigger-inversion defense (FLIP) that the paper centrally claims to evade.** The introduction and Section 2 (v.s. Trigger generators → Defenses) explicitly state that "FLIP is effective in removing prior backdoors with patch-based triggers whereas our attack can naturally evade this SOTA defense." Yet the empirical section never tests FTA against FLIP. The paper evaluates 8 defenses (norm clipping, FLAME, Multi-Krum, Trimmed-mean, RFA, SignSGD, Foolsgold, SparseFed) but FLIP is not among them. Since evasion of FLIP is explicitly invoked as a key advantage, its absence from the experiments leaves a central claim untested.

- **No ablation of the adaptive generator-across-rounds mechanism.** A core design element is that the trigger generator is continuously trained across FL rounds to adapt to the changing global model (Section 4.3). Yet no experiment compares: (a) training a fresh generator each round, (b) using a fixed pre-trained generator across all rounds, and (c) the proposed adaptive re-training. Without this ablation, it is unclear whether the adaptivity contributes to performance or whether a simpler one-time generator training would suffice.

- **No adapted imperceptible-trigger baseline from centralized work.** The paper explicitly contrasts its approach with centralized generator-based backdoor attacks (LIRA, IBA) in Section 2, arguing they cannot ensure absence of backdoor routing and do not adapt to the changing global model. However, it never implements or evaluates any adapted version of these methods as a FL baseline. This makes the "state-of-the-art stealthiness" claim unsubstantiated against the most competitive comparator class — generator-based invisible triggers adapted to the FL setting.

- **Results for six of the eight defenses are referenced only to the missing appendix.** The main paper shows only norm clipping and FLAME curves. Multi-Krum, Trimmed-mean, RFA, SignSGD, Foolsgold, and SparseFed are mentioned but their results are all in the appendix (which is not present in the submission). Similarly, few-shot durability experiments, SSIM/LPIPS stealthiness results, and key details about tasks, models, and hyperparameters are appendix-only. A paper should present sufficient evidence in the main text to support its core claims.

### Minor

- **t-SNE caption/text inconsistency.** The caption of Figure 5 says "Fashion-MNIST" but the text in Section 4.4 says "We use t-SNE visualization result on CIFAR-10." This minor inconsistency suggests careless editing and makes it unclear which dataset was actually used.

- **Bi-level optimization framing is not reflected in the algorithm.** Equation (1) formulates the problem as a bi-level, non-convex, constrained optimization, but Algorithm 1 is a straightforward two-stage heuristic: fix the model and train the generator, then fix the generator and train the model. The paper acknowledges this ("we consider two steps... not alternately"), but the framing as bi-level optimization is somewhat misleading. This is a minor presentational issue.

- **No analysis of the norm values of malicious vs. benign updates.** The paper argues that FTA evades norm clipping because it requires "a much smaller norm to effectively fool the global model" (Section 4.3.1), but never reports the actual norm magnitudes across rounds. This would add mechanistic insight to the claim.

### Trivial

- None.

## Nice-to-Haves

- The sensitivity to the number of malicious agents (e.g., 1%, 5%, 10%) would strengthen the paper, since the threat model claims <1% attacker fraction.
- A comparison of FTA's computational overhead in more detail (training time, memory) would help assess practicality.
- Testing against adaptive defenses that analyze hidden-feature distributions (e.g., activation clustering on the server) would be a natural next step.

## Removed Points

These points were flagged to be removed; treat them with caution.

- **Harsh critic's claim about <1% vs. 10% attacker proportion discrepancy.** The paper states the attacker compromises <1% of *all agents* and the experiment selects 10 agents per round out of a larger pool (total pool size unspecified). With a sufficiently large total pool, 1 malicious agent per round can be <1%. The harsh critic incorrectly assumed the 10 selected agents are the entire population. Removed as factually wrong.

- **Harsh critic's criticism that the bi-level optimization framing is incorrect.** The paper acknowledges the decoupled two-phase approach is a practical solution ("not alternately"). This is a reasonable engineering approximation for a challenging optimization problem; labeling it a "heuristic" rather than true bi-level is a presentation choice, not a flaw.

- **Strength Finder's generic strengths about "addressing important problems."** Strengths like "backdoor attacks is still a relevant issue" and "the problem is important" are generic and add no specific information about this paper's quality.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add numerical tables for all main results.** Provide at minimum a table reporting mean BA ± std across multiple seeds for all four datasets under FedAvg (fixed-frequency), and a table for defense evaluation (norm clipping and FLAME) with both backdoor accuracy and benign accuracy. The abstract's "98%" and "97%" claims must be backed by precise numbers.

2. **Run and report the FLIP defense experiment.** Without this, the paper's signature claim of trigger-inversion evasion is unsubstantiated.

3. **Ablate the adaptive generator.** Compare: (i) fresh generator each round, (ii) fixed generator from round 1, (iii) proposed adaptive re-training. This directly tests whether the "adaptive" component provides measurable benefit.

4. **Add an imperceptible-trigger baseline.** Adapt LIRA or IBA to FL and evaluate under the same conditions. Use the same generator architecture and norm constraints, without FTA's hidden-feature-to-target-label similarity. This isolates the value of FTA's specific design choices.

5. **Move at least one result table for the "other six defenses" into the main paper.** Even a single table summarizing all 8 defenses on at least one dataset would significantly strengthen the main-text evidence.

## Score and Decision

**Calibration anchors:**
| Anchor | Avg Score | Comparison to FTA |
|--------|-----------|-------------------|
| `Mb5vJijcHn` (EDBA, Reject) | 3.50 | FTA has a clearer problem motivation and better methodology but falls short of the experimental rigor needed for acceptance. |
| `0rS9o1uKqu` (TLDR, Reject) | 2.50 | FTA is substantially stronger — it has a clear method, some experimental evidence, and a well-motivated contribution. |
| `Dc6dgTq2UZ` (DBA-DFL, Reject) | 5.25 | Similar profile: good idea with missing ablations and defenses evaluation. FTA's problem analysis is sharper but experimental gaps are similar. |
| `79nO2DPjVX` (Bad-PFL, Accept) | 6.00 | Both use generator-based triggers, but Bad-PFL provides more thorough experiments with numerical tables. FTA is weaker on evidential rigor. |
| `s8lj3C39Ow` (SuDA, Reject) | 4.50 | Both have clear motivation but insufficient evidence. FTA has a more original attack contribution; SuDA is a defense paper. |
| `RXVYOCGO7g` (Nira, Reject) | 5.00 | Defense paper, not directly comparable. FTA is in a similar quality band. |
| `nTNgkEIfeb` (FedInverse, Accept) | 7.00 | FedInverse provides thorough numerical evaluation (tables, metrics, multiple seeds). FTA lacks this rigor. |

FTA is a good idea paper that identifies real problems (P1–P3) with prior backdoor triggers and proposes a reasonable solution. The t-SNE visualization and FLAME/norm-clipping results provide initial support. However, the experimental validation does not rise to the level required to support the strong quantitative claims made in the abstract and conclusions. The absence of numerical tables, the missing FLIP evaluation, the lack of an imperceptible-trigger baseline, and the unablated adaptive generator are significant gaps that prevent the paper from establishing its contribution convincingly.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>