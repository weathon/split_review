Now let me write the consolidated review.

## Summary

This paper defines a novel and practically motivated problem: federated learning with *openset* noisy labels, where each client's observed label space is a proper subset of the full label space *and* the observed labels are noisy. The authors propose FedDPCont, which uses label differential privacy (DP) to share globally aggregated labels among clients, then subtracts a sampled "contrastive label" from the local loss to prevent overfitting to openset noise patterns. The paper includes formal definitions of the openset noise problem, a theoretical claim about centralized-equivalent updates (Theorem 2), and experiments on CIFAR-10/100, CIFAR-N, and Clothing-1M.

## Strengths

1. **Novel problem formulation (Section 3.1, Definition 1):** The paper formally defines openset noisy labels in FL, where each client's noisy label space differs from the global one and is a proper subset. The generation process (uniform/non-uniform allocation via indicator variables and Dirichlet sampling) is clearly specified, and the 3-class example with transition matrices concretely demonstrates why standard loss correction fails under openset conditions. This is a genuine contribution that extends beyond prior FL+noisy-label works (Yang et al. 2022, Xu et al. 2022) which assume identical label spaces across clients.

2. **Creative use of DP-protected label sharing with contrastive loss (Sections 3.2, 4.1, Equation 3):** The core idea — sharing globally aggregated labels under DP guarantees and using them as a contrastive term (ℓ(f(x), ỹ) − ℓ(f(x), y′)) to penalize overfitting to local openset noise — is original and well-motivated. The paper correctly identifies that a locally sampled contrastive label would fail because it lacks global information. The use of label DP (via random response with T_DP and matrix inversion for debiasing) is technically sound and follows established methodology (Ghazi et al., 2021).

3. **Consistent empirical advantage across benchmarks (Table 1, Sections 5.2–5.3):** The paper reports that FedDPCont outperforms FedAvg, FedProx, Co-teaching, T-revision, FedBN, FedDyn, Scaffold, and loss correction across CIFAR-10, CIFAR-100, CIFAR-N, and Clothing-1M under multiple noise settings. While I cannot independently verify the exact numeric values (tables are in image format), the breadth of baselines and datasets is reasonable for a new problem formulation with no existing dedicated methods.

4. **Stability analysis w.r.t. DP privacy level (Section 5.4):** The paper investigates performance across different ϵ values and shows stability, which supports the practical viability of the privacy-utility trade-off.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 2 is insufficiently specified, undermining the paper's central theoretical claim.** The theorem states: "The aggregated model update of FedDPCont is the same as the corresponding centralized model update, i.e., Σ ℙ(𝒟_c|𝒟)·Δ_c^{(r)} = Δ^{(r)}." Here, Δ^{(r)} is defined as "the variation of model parameters in the r-th round of the corresponding global gradient descent update *assuming the local data are collected to a central server*" (line 136), but **what loss function that centralized update minimizes is never stated.** This matters critically because the local updates Δ_c^{(r)} use the contrastive loss ℓ_PL = ℓ(f(x), ỹ) − ℓ(f(x), y′), which includes a negative term not present in standard cross-entropy. The theorem cannot be evaluated without knowing the centralized loss: if it is standard CE, the contrastive term would break the equality; if it also includes a contrastive term, the claim becomes a tautology requiring separate justification. As written, this is a placeholder for a theorem, not an actionable result. The paper relies on this claim to argue that openset noise is "theoretically resolved" (Strength Finder), which is not supported by the text as presented.

2. **The description of the DP mechanism is internally inconsistent, creating ambiguity about the actual privacy parameters used.** The paper states (line 206) that ϵ = 3.58, 5.98, and 3.95 for CIFAR-10 (K=10), CIFAR-100 (K=100), and Clothing-1M (K≈14) respectively, "to keep e^ϵ/(e^ϵ+K−1) = 0.2." However, plugging these values into e^ϵ/(e^ϵ+K−1) yields ≈0.8 for all three datasets, not 0.2. These ϵ values *are* consistent with (K−1)/(e^ϵ+K−1) = 0.2 (total flip probability = 0.2), meaning either the formula is mis-specified or the verbal description "keep ... 0.2" refers to the flip probability rather than the keep probability. Either way, the paper as presented contains a concrete numerical inconsistency that prevents a reader from determining what flip probability was actually used. This is not a fatal methodological error (the values are self-consistent under a different interpretation), but it is a significant clarity failure for the paper's privacy claims.

3. **No ablation isolating the effect of the contrastive term.** The core novelty of FedDPCont is subtracting a globally sampled contrastive label from the loss. Yet the experiments never compare against a version of FedDPCont that uses only the noisy-label loss ℓ(f(x), ỹ) without the contrastive term −ℓ(f(x), y′). Such an ablation would directly test whether the contrastive labels are responsible for the improvement, versus the improvement coming from other aspects of the method (e.g., the label communication protocol reducing ambiguity about the global label distribution). Without this, the paper cannot attribute its gains to the claimed mechanism.

### Minor

4. **Limited statistical rigor in main experiments.** The main results (Table 1) report only "the best accuracy" from 3 random seeds (line 206), without standard deviations visible in the extracted text (the table is an image). Three seeds is on the low end for problems with high stochasticity (noise generation, client sampling, DP flipping, contrastive label sampling). The DP ablation in Section 5.4 does use 10 seeds, which is better, but the main benchmark results would benefit from additional runs and reported variance.

5. **No variation of openset severity.** The experiments vary noise ratios but do not systematically vary the *openset severity* — e.g., the average fraction of classes missing per client. Since "openset" is the paper's defining new dimension, ablating this parameter (e.g., clients with 20%, 50%, 80% of classes) would directly test whether the method addresses the openset aspect or just general noisy-label robustness.

6. **The contrastive loss's behavior is not analyzed.** The loss ℓ(f(x), ỹ) − ℓ(f(x), y′) uses cross-entropy, so the negative term is unbounded below (since ℓ(f(x), y′) can be arbitrarily large as the predicted probability for class y′ approaches zero). While this does not necessarily cause failure in practice, the paper provides no analysis of the loss landscape, boundedness, or convergence properties. The reference to prior contrastive label works (Liu & Guo 2020, Wei et al. 2022a, Cheng et al. 2020) is useful but those works use different formulations; the specific form here is novel and merits its own discussion.

7. **Algorithmic detail about contrastive label sampling frequency is missing.** Algorithm 2, lines 11–14, specifies that a contrastive label (y_c^n)′ is sampled for each data point, but does not state whether this sampling happens once per round, once per epoch, or once per mini-batch. The loss L_c is defined as a sum over the local dataset, but the model is updated per mini-batch; this ambiguity affects reproducibility.

### Trivial
- Line 206: The expression "$e^{\epsilon}/(\bar{e}^{\epsilon+K-1})$" contains a typographical artifact (the bar over e). In the original submission this is likely a formatting issue.
- The privacy discussion (line 186) references "Table 3" but the extracted text does not contain visible Table 3 content (likely an image).

## Nice-to-Haves
- Comparing against an oracle version of FedDPCont that shares true labels (without DP) would quantify the privacy cost concretely.
- Including FL+noisy-label baselines (Yang et al. 2022, Xu et al. 2022), even if they fail under openset assumptions, would make the comparison more informative.
- Testing the effect of the number of clients on the accuracy of the debiased label distribution (finite-sample accuracy of the inverted estimator) would strengthen the analysis of the label communication protocol.

## Removed Points

These points were raised in the reviews but are removed or demoted for the following reasons:

- **"Baselines are straw men" (Harsh Critic Critical Issue 2):** Partially removed. The critic claimed LC is a straw man because it requires a noise transition matrix. The paper acknowledges this and uses LC precisely to *demonstrate* that centralized loss-correction fails under openset noise — this is informative, not a straw man. However, the omission of FL-specific noisy-label baselines (Yang et al. 2022, Xu et al. 2022) is a real point and is retained as a nice-to-have. The claim that Co-teaching/T-revision are "straw men" is unsubstantiated — they are standard noisy-label baselines and their failure under openset FL is a valid result.

- **"Only 3 seeds is insufficient" framed as a critical weakness:** Demoted from major to minor. Three seeds with reported best accuracy is below ideal but not unusual for FL papers. The paper does report 10 seeds for the DP ablation. This is a minor rigor concern, not a fatal or critical one.

- **"Theorem 2 is vacuous" / "ill-posed":** Substantially retained but re-framed. The theorem is not "vacuous" — the concept of centralized-equivalent updates is meaningful. However, the centralized loss is indeed undefined, making the claim unverifiable. This is re-categorized as a major weakness (not fatal) because the paper could clarify the intended centralized objective in revision.

- **"Contrastive loss can be arbitrarily negative → fatal":** Demoted to minor. While technically true that the loss is unbounded below, this is a common property of many contrastive/negative-learning losses used in practice. The paper would benefit from analysis but the absence is not fatal.

- **"No comparison with methods designed for FL with noisy labels" (Strengthening Suggestion 4):** Moved to nice-to-have. The paper acknowledges these methods assume identical label spaces (violated by openset). Including them would strengthen completeness but their failure is predictable.

- **"The paper should test with real-world FL data partitions" (from Conclusion):** Moved to nice-to-have. The paper already acknowledges this limitation (line 232). Testing real-world partitions is future work, not a flaw in the presented experiments.

- **Strength Finder Strength 2 (Theorem 2 supports core claim):** Weakened in wording. Given the theorem's central ambiguity, it does not robustly support the core claim as currently written. The strength is retained but the caveat is now reflected in the weaknesses section.

- **Generic strengths from Strength Finder about "important problem" / "interesting question":** Removed. These are generic and not specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's theoretical centerpiece (Theorem 2) is too vaguely specified to do the work asked of it, and the empirical support is thinner than desirable given the novelty of the problem. The core idea — DP-shared global contrastive labels for openset FL — remains interesting and underexplored, but neither the reviews nor a close reading of the paper yield a fresh perspective beyond what the paper itself provides.

## Suggestions

1. **Precisely define the centralized loss in Theorem 2.** State explicitly whether it is the standard CE loss on pooled data or a modified loss that also includes a global contrastive term. If the latter, provide justification for why that centralized loss is itself robust to openset noise. Without this, the theorem is uninterpretable.

2. **Clarify the DP parameter description.** Ensure the formula and reported ϵ values are consistent. If the intended flip probability is 0.2, state that directly and verify the formula matches: either (K−1)/(e^ϵ+K−1) = 0.2, or equivalently P(keep) = e^ϵ/(e^ϵ+K−1) = 0.8.

3. **Add an ablation removing the contrastive term** (i.e., using only ℓ(f(x), ỹ) without −ℓ(f(x), y′)) to isolate its contribution. This is the single most informative experiment missing from the paper.

4. **Increase the number of random seeds** for main experiments to at least 5 and report standard deviations. For a new problem formulation, reproducibility across runs is important.

5. **Vary openset severity** (e.g., fraction of classes missing per client) to demonstrate that the method specifically addresses the openset dimension of the problem.

6. **Specify the contrastive label sampling frequency** in Algorithm 2 (per mini-batch, per epoch, or per round).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| FedOpenMatch (5UrPAW3uI1) | 5.50 | R1 | Defines a novel OSSFL problem, thorough experiments. This paper defines a novel problem but has weaker experiments and vague theory. **Weaker.** |
| FedGR (BtpXep9qxC) | 4.67 | R1 | FL+noisy labels with incremental contributions and limited theory. Similar level: both define new problem variants but have theory/rigor gaps. **Comparable.** |
| FedCova (ZzhfTlqnyp) | 4.00 | R1 | FL+noisy labels via covariance, rejected with missing baselines. This paper's problem definition is more novel. **Slightly stronger.** |
| Noisy FL (Ps7bqlodWu) | 2.00 | R1 | Weak, withdrawn paper. This paper is clearly stronger. |
| UFL (PSGBG2rBbg) | 2.50 | R1 | Weak, withdrawn. This paper is clearly stronger. |

**Round 1 bracket statement:** The paper sits between 4.0 and 5.5.

**Round 2 — Narrowing:**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| FedOpenMatch (5UrPAW3uI1) | 5.50 | R2 | Same anchor. FedOpenMatch has cleaner theory and more thorough experiments. This paper has a more novel problem but weaker execution. **Clearly weaker.** |
| FedGR (BtpXep9qxC) | 4.67 | R2 | Both define new problem sub-variants in FL+noisy labels and have theory gaps. FedGR's experiments are more thorough (more seeds, more ablations). **Slightly weaker.** |
| FedCova (ZzhfTlqnyp) | 4.00 | R2 | FedCova had stronger theoretical framing (mutual information) but also missing baselines. This paper has a more novel problem definition. **Slightly stronger.** |
| DP+FL (7Zbe5ad3eX) | 6.00 | R2 | Strong theoretical DP analysis paper. This paper's theoretical contribution is much weaker. **Clearly weaker.** |
| OOD+Noise (yk3QBsB43u) | 5.00 | R2 | Had a well-defined problem with clear experimental validation but scattered scores (8,2,4,6). Comparable in overall quality. **Comparable.** |

**Final score determination:** The paper is weaker than FedOpenMatch (5.50, accepted) but comparable to or slightly better than FedGR (4.67, rejected) and slightly stronger than FedCova (4.00, rejected). The paper's main liability is a vague central theoretical claim (Theorem 2), an inconsistent DP parameter description, and insufficiently rigorous experiments (3 seeds, no contrastive ablation). These are real but not fatal issues; the problem definition and core idea have genuine novelty. I position this paper at 4.5 — promising but needing substantial revision.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>