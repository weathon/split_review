## Summary

This paper introduces NARCISSUS, an unsupervised anomaly detection method that exploits the observation that models trained on unlabeled data containing a mix of normal and anomalous samples converge on normal patterns first. The method combines a tailored early stopping scheme (VES) with a lightweight ensemble (RVES) to detect anomalies without requiring any labels. Evaluated across time series (7 base models, 6 datasets), images (MVTec2D, MNIST), and graphs (UCI Message, Digg), the method achieves F1 and AUC scores within 0.02–0.04 of semi-supervised counterparts trained on clean normal data, directly supporting the central claim of semi-supervised-comparable accuracy without labels.

## Strengths

- **Clear and practically useful insight, empirically grounded.** The core idea — that models fit normal data before anomalous data when trained on a mixed unlabeled set — is genuinely novel in the anomaly detection context. Figure 1 provides direct empirical evidence of this phenomenon, and the method's success across 7+ base models confirms its generality.

- **Strong empirical support for the main claim (semi-supervised comparability).** Table 2 directly compares NARCISSUS-trained models against the same models trained on clean normal data across six time series datasets. The F1 difference is within 0.04 in all cases except the acknowledged MTAD-GAT/NAB failure, and NARCISSUS sometimes *outperforms* the semi-supervised version (e.g., SMAP). This is the right comparison for the paper's headline claim and it holds up well.

- **Ablation cleanly isolates the contribution of each component.** Section 5.4 shows that bootstrapping alone yields F1 scores ranging from 0.43 to 0.97 on MBA (high variance), while NARCISSUS stabilizes performance. The paper also reports (in the appendix) that removing RVES degrades performance, confirming both components are necessary.

- **Demonstrated breadth of applicability.** NARCISSUS is applied to LSTM-NDT, OmniAnomaly, USAD, MTAD-GAT, GDN, TranAD, NPSR (time series), PatchCore and AnoGAN (images), and AddGraph (graphs) without architectural modification, validating model-agnostic applicability within the stated scope of semi-supervised detectors.

## Weaknesses

### Major

1. **Theorem 4.2 does not establish the temporal ordering it claims.** The theorem states that if \(N_n\cdot\delta_n \gg N_a\cdot\delta_a\), SGD converges toward fitting normal data. But this condition is essentially a restatement of the sparsity assumption on aggregate gradient contributions — it bounds one iteration's gradient, not the *per-sample convergence rates* or *temporal ordering* that the method's justification requires. The key corollary (Corollary 4.3) — that "the first converged data are more likely to be normal" — requires a dynamic argument about optimization over time, not a static bound on a single iteration. The "Proof" writes down gradient bounds, asserts the condition, and concludes convergence, but never actually proves convergence rates differ between normal and anomalous data. The paper's empirical evidence (Figure 1) is more compelling than the theorem. Presenting this as a formal theorem with a proof that doesn't prove what it claims is an overreach that may undermine reviewer trust. The paper would be better served by framing this as a heuristic observation backed by Figure 1 and prior work (Paul et al., 2021).

2. **The VES algorithm's \(\eta\) parameter undercuts the "unsupervised" characterization.** Algorithm 1 filters out the top \(\eta\%\) of validation subsets based on loss, where \(\eta\%\) is "the upper bound of the portion of anomalous data." In a truly unsupervised setting, this proportion is unknown by definition. The paper says "empirically we can choose a large \(\eta\) to ensure most of the considered validation data are normal," but provides no principled way to set \(\eta\) without label information. Setting \(\eta\) too large risks discarding normal data (especially if normal-data loss is not uniformly low early in training); setting it too small risks retaining anomalous subsets. The paper does not analyze sensitivity to \(\eta\) or provide an automated estimation procedure. This is the method's most significant practical limitation.

### Minor

3. **Unsupervised baselines are dated relative to the secondary claim.** The paper claims NARCISSUS "significantly outperforms all unsupervised detection methods" (Table 1), but the unsupervised baselines (DAGMM 2018, MSCRED 2019, Merlin 2020) are several years old. More recent unsupervised deep AD methods (e.g., DeepSVDD — which the paper cites in related work — GOAD, NeuTraL) are not included. The *primary* claim (semi-supervised comparability) is well-supported by Table 2, but the secondary claim about outperforming unsupervised methods rests on a weaker comparison set.

4. **Image and graph evaluations are thin relative to the claim of "comprehensive evaluations."** Only two image datasets are tested (MVTec2D, MNIST), and the MNIST setup uses synthetic anomaly scenarios (digits vs. digits). Only two small graph datasets are tested. The paper acknowledges this limitation in its Discussion section, but the abstract's phrase "comprehensive evaluations using time series, image and graph datasets" overstates the breadth. The evidence for cross-domain generalizability is suggestive but preliminary.

5. **No systematic analysis of failure conditions.** The paper notes one failure case (MTAD-GAT on NAB, attributed to small dataset size) and states NARCISSUS "requires a relatively large dataset." But there is no analysis of *when* the method breaks — e.g., at what anomaly proportion the convergence gap collapses, or what structural similarity between normal and anomalous patterns causes loss trajectories to coincide. Understanding these boundaries would substantially strengthen the contribution.

6. **The formal optimization problem (Eq. 3) is not actually optimized by the algorithm.** The paper formulates Eq. 3 as an optimization over pseudo-anomalous subsets, then mentions that VES convergence "meets the constraint in Eq. 3." But the algorithm does not search over subsets to maximize the stated objective — it uses a heuristic early-stopping rule on randomly selected validation subsets. The formal setup and the implemented algorithm operate at different levels of abstraction without a clear bridge.

### Trivial

- None.

## Nice-to-Haves

- A sensitivity analysis of \(\eta\) across datasets with known anomaly proportions, demonstrating a default value (e.g., 5–10%) that works robustly.
- A comparison against self-supervised pseudo-labeling methods on at least one dataset would make the comparison more complete, even if the paper's rationale for excluding them is defensible.
- A controlled experiment where anomaly proportion is systematically varied (e.g., 1%, 5%, 10%, 20%) to map the method's operational regime.

## Removed Points

- **"Model-agnostic is misleading."** Removed. The paper clearly scopes this to semi-supervised models (abstract: "make use of even a semi-supervised anomaly detection model underneath"). The critic's demand that it work with kernel density estimators or isolation forests is outside the paper's stated scope.
- **"Bootstrapping baseline is not representative."** Removed. The bootstrapping comparison is an ablation design intended to show that VES/RVES improve over naive random selection. This is a valid and standard use of a weak baseline in an ablation.
- **"Lemma 4.1 proof is in the missing appendix / Lemma is too trivial."** Removed. The appendix reference is a parser artifact. The lemma itself (existence guarantee) is simple but one trivial lemma is not a paper weakness worth reporting.
- **"No comparison against self-supervised pseudo-label methods."** Removed. The paper provides a clear rationale (line 185–186): NARCISSUS would boost such methods anyway, and NARCISSUS already matches semi-supervised performance, making the extra complexity unnecessary. This is a defensible methodological choice.
- **"Key parameters unspecified."** Removed. The paper references §A.3, §A.4, §A.7 for these details; the appendix was stripped by the parser, so the reviewer cannot evaluate what is or is not specified.
- **"Synthetic MNIST anomalies are not representative."** Removed. The paper itself acknowledges MNIST's "synthetic nature" and the authors treat these results as suggestive rather than definitive. The critic restates a known limitation the authors are already upfront about.

## Novel Insights

None beyond the paper's own contributions. The most insightful observation in the reviews — that the η parameter creates a tension with the "unsupervised" framing — is already implicit in the paper's own description of η as an "upper bound" that the user must supply.

## Suggestions

1. **Reframe or remove Theorem 4.2.** Either (a) replace it with an empirical characterization showing that the loss gap between normal and anomalous data widens over training iterations, with measurements across multiple base models and datasets; or (b) explicitly state it as a heuristic motivation (supported by Figure 1 and prior work) rather than claiming a formal proof. The current presentation overclaims and invites justified skepticism.

2. **Address the η dependency.** Provide either (a) an automated estimation procedure (e.g., use the loss distribution across the RVES ensemble to estimate the anomaly proportion), or (b) an empirical analysis showing that performance is stable across a wide range of η values (e.g., 1%, 5%, 10%, 20%) on multiple datasets. Without this, the method is not reproducible as a fully unsupervised algorithm.

3. **Add at least one modern unsupervised baseline** (e.g., DeepSVDD, which is already cited in the paper) to Table 1 to substantiate the secondary claim about outperforming unsupervised methods.

## Score and Decision

The paper has a genuine empirical contribution: a novel, well-motivated method for unsupervised anomaly detection that convincingly achieves semi-supervised-comparable accuracy on time series data. The evaluations are thorough for the primary claim. However, the paper weakens itself in two ways that would give reviewers at a strong venue pause: (1) it presents Theorem 4.2 as a formal proof when it is at best a heuristic motivation, inviting deserved pushback; and (2) the η parameter's dependence on (unknown) anomaly proportion undercuts the method's claim to be unsupervised, and this is not adequately addressed. These are fixable issues, but they are real in the current submission.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>