Now I have all the calibration anchors I need. Let me compile the final review.

## Summary

The paper studies a "data collection" paradigm under shuffled differential privacy, where uncommitted end users contribute a single labeled data point. It presents a novel theoretical reduction from shuffled DP kernel density estimation (KDE) to binary summation (bitsum) protocols (Theorem 3.2), achieving accuracy that matches central DP rates. Using this reduction, the paper builds a per-class KDE-based classifier (HDC) and demonstrates private class decoding — recovering semantic vocabulary terms from the learned density functions. Experiments on four datasets (DBPedia-14, AG News, SST2, CIFAR-10) with two kernels and three bitsum protocols show classification accuracy approaching central DP and non-private baselines, with qualitative evidence of semantic preservation.

## Strengths

- **Novel theoretical reduction from shuffled DP KDE to bitsum (Theorem 3.2).** The reduction is technically sound, explicitly accounts for LSQ properties and bit-width, and provides a clean path for practitioners to plug in any bitsum protocol. The concrete instantiation for the Gaussian kernel (Theorem 3.3) achieves supRMSE scaling as $O(\sqrt{\log(1/\delta)}/(\varepsilon n))$, matching the central DP rate. This is a genuine theoretical contribution to the shuffled DP literature.

- **Clear and well-motivated framing of the data collection scenario.** The paper correctly distinguishes one-shot private data collection from the multi-round iterative distributed/federated training that dominates prior shuffled DP ML work (Section 2.4). This is an important practical distinction that is often overlooked.

- **Thoughtful treatment of practical deployment considerations.** Section 3.1 explicitly addresses user-count estimation (the chicken-and-egg problem with shuffled DP), distinguishes between communication-threat and model-threat models, and accounts for bit-width and discretization. These details ground the theoretical protocol in realistic constraints.

- **Demonstration of private class decoding.** Table 1 qualitatively shows that the privately learned KDE functions recover semantically meaningful vocabulary terms (e.g., "band", "album", "song" for "artist" class), going beyond classification accuracy and showing that intra-class similarity structure is preserved despite never observing unprotected examples.

## Weaknesses

### Fatal
None.

### Major

- **Privacy accounting in Corollary 3.4 is incomplete.** The paper claims the learning protocol is $(\varepsilon,\delta)$-DP in the model-threat model. However, the learning protocol publishes per-class user counts $\tilde{n}_c$ derived from the $\varepsilon_{\text{lbl}}$-DP label perturbation round (the paper says they are "published"). If these counts are part of what the model-threat adversary can access (they are public), then by basic composition the guarantee should be $(\varepsilon+\varepsilon_{\text{lbl}},\delta)$ — matching the communication-threat model's guarantee. The paper acknowledges the counts are $\varepsilon_{\text{lbl}}$-DP but then omits them from the model-threat accounting. This needs correction: either (a) explain why the counts are not part of the released "model" in the model-threat definition and make that explicit, or (b) correct the guarantee to $(\varepsilon+\varepsilon_{\text{lbl}},\delta)$. This is a significant oversight even though the theory of Theorem 3.2 is unaffected.

- **Missing local DP baseline in experiments.** The paper's motivation hinges on shuffled DP being superior to local DP, yet the experiments include only central DP and non-private baselines. Without a local DP baseline (e.g., local DP KDE with randomized response, or a local DP kNN), the claimed practical advantage of shuffling over local DP is unsubstantiated empirically. The preliminary local DP round for label counts is not a substitute for an end-to-end local DP baseline. This is the most significant empirical gap.

- **Gap between theory and practice: use of noisy group counts.** Theorem 3.2 assumes the true number of users $n$ is known. In the learning protocol, $n$ per class is replaced by the noisy count $\tilde{n}_c$ from the local DP label perturbation. The paper does not analyze how errors in the estimated group counts affect the KDE accuracy (supRMSE) or whether the shuffled KDE protocol's privacy guarantee holds unmodified when the group size is itself a random variable. While the privacy of the counts is separately handled ($\varepsilon_{\text{lbl}}$-DP), the accuracy implications are unexamined. The paper acknowledges the practical concern in Section 3.1 but never bridges it to the theory.

### Minor

- **No error bars or confidence intervals in experiments.** The classification accuracy results (Figure 1) and KDE error results (Figure 3) are reported as single runs. Given the inherent randomness in DP mechanisms, it is unclear whether the observed trends are reproducible. This is standard for many DP benchmarking setups, but the paper should at least acknowledge the limitation or provide some variance estimate.

- **Class decoding is evaluated only qualitatively.** Table 1 is interesting and suggestive, but the paper makes no attempt to quantify correctness (e.g., precision@k on a held-out vocabulary, rank correlation, or comparison against a non-private decoding baseline). The paper acknowledges this ("semantic relatedness is inherently somewhat subjective"), which is reasonable, but the claim that "the class representations... capture the semantic meaning of the classes" remains supported only by anecdote.

- **Figure 1 lacks numerical markers/values.** The accuracy curves are line charts without marked data points or numerical callouts, making it difficult to compare specific values across methods at a glance.

### Trivial

- **Communication cost for the Pure protocol is not shown in Figure 2.** The paper states Pure sends "orders of magnitude more messages" and "cannot fit on the same plots." This is a reasonable justification, but providing a separate figure or a table would be more informative.

- **The paper mentions variants in Theorem 3.2's proof and "additional variants" (line 98) but defers them to appendices that were not available for review.**

## Nice-to-Haves

- A sensitivity analysis varying $\varepsilon_{\text{lbl}}$ to measure impact on classification accuracy (currently all experiments use $\varepsilon_{\text{lbl}}=5$).
- Visualizing the true vs. privately estimated KDE curves for one class to illustrate what the protocol preserves.
- Extending the privacy analysis and theoretical bounds to the setting where the group size used in Algorithm 1 is a random variable (the noisy count).

## Removed Points

- **Criticism about model availability / reproducibility concerns (e.g., "no code released")**: The paper states code is in supplementary material. The critic's concern about reproducibility via undisclosed implementation details is standard for conference submissions.
- **Criticism about missing appendices / proofs deferred to appendices**: The parser strips these; they exist in the original submission.
- **Claim that Corollary 3.4 is "wrong" rather than "incomplete"**: The paper's model-threat definition ("adversary sees only the trained model") could be argued to exclude the intermediate counts. However, the paper says the counts are "published," creating ambiguity. The weakness as stated above is accurate — it needs clarification or correction.
- **"The paper would also need to address the noisy-counts issue and provide a more rigorous evaluation" as a basis for rejection**: This overstates severity; the theoretical core stands. The noisy-counts issue is a gap between theory and experiments, not a theoretical flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension that the paper itself does not fully confront: Theorem 3.2 is a clean theoretical reduction that works when $n$ is known, but the end-to-end learning protocol requires estimating $n$ per class, creating a discontinuity between the theory (which assumes exact $n$) and the practice (which uses noisy counts from local DP). The paper treats the two as independent concerns, but in practice they interact — the error in the per-class counts propagates into the KDE protocol, and this propagation is unanalyzed. The privacy accounting issue with Corollary 3.4 further compounds this. The paper's strongest contribution (the KDE-to-bitsum reduction) is somewhat isolated from its practical deployment story.

## Suggestions

1. **Fix the privacy accounting in Corollary 3.4.** Either explicitly clarify that the noisy counts are not part of the "trained model" in the model-threat definition (and explain why they can be considered separate), or correct the guarantee to $(\varepsilon+\varepsilon_{\text{lbl}},\delta)$ for that threat model as well.

2. **Add at least one local DP baseline to the experiments.** A simple baseline (e.g., local DP KDE using randomized response on features, or local DP kNN) would significantly strengthen the paper's central claim that shuffling provides accuracy benefits over local DP.

3. **Provide a theoretical or empirical analysis of how noisy group counts affect the KDE accuracy.** At minimum, bound the additional error introduced by replacing $n$ with $\tilde{n}_c$, or run an ablation study varying $\varepsilon_{\text{lbl}}$ to measure the impact.

4. **Add error bars or confidence intervals** for the main experimental results, or clearly state that the single-run results should be treated as preliminary.

5. **Quantify class decoding** with at minimum a precision@k metric or a comparison against a non-private KDE baseline, to strengthen the claim that semantic content is preserved.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HMe5CJv9dQ.md` (Efficiently Computing Similarities to Private Datasets) | 7.50 | Similar KDE topic but cleaner theory-to-experiment mapping; fewer experimental gaps. Current paper has weaker empirical validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/txV4dNeusx.md` (Near-Exact Privacy Amplification for Matrix Mechanisms) | 6.25 | Clean privacy accounting with solid experimental support. Current paper has a privacy accounting error and less complete experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hkSjjs4o5d.md` (DP Clustering for Well-Clustered Graphs) | 6.50 | Strong theory paper with careful presentation. Current paper has a novel reduction but weaker presentation and an accounting issue. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gVVoZtiQlt.md` (Phase Transition of Shuffled Regression) | 5.00 | Both study shuffled settings with theoretical contributions; current paper has cleaner theory but similar experimental limitations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/S6Dn3uyM2p.md` (DP One Permutation Hashing) | 4.60 | Both have a combination of theory and experiments; current paper has stronger theoretical novelty but the hashing paper has more thorough experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FNCFiXKYoq.md` (MAAD Private) | 3.00 | Straightforward combination of existing techniques. Current paper has substantially more technical novelty and a novel reduction. |

The paper's theoretical contribution (Theorem 3.2) is genuine and places it above purely incremental work. However, the privacy accounting error in Corollary 3.4, the missing local DP baseline, and the unanalyzed noisy-counts gap together prevent the paper from reaching a strong acceptance level. These issues are fixable in revision but weigh against acceptance in the current form.

MY FINAL SCORE: 4.5
MY FINAL DECISION: Reject