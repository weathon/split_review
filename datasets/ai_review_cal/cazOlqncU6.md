- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper formalizes the Trustworthy Dataset Proof (TDP) problem — verifying that a model was trained on the *entire* claimed dataset, not just a distributionally similar one or one containing specific watermarked samples. It proposes a Data-Probe technique: a small subset of training samples is selected via a keyed hash of the full dataset; during training, these probe samples are given a subtle statistical signature (e.g., higher confidence, poisoned labels); at verification time, the verifier recomputes the probe from the claimed dataset and checks whether the model's outputs on probe vs. non-probe samples differ significantly. Any modification to the dataset changes the hash, selects different probes, and causes verification to fail. Four probe variants (PP, AP, UP, TP) are designed and evaluated across four datasets and four architectures.

## Strengths

1. **First formalization of the TDP problem with a clear threat model and goals (G1–G4).**  
   The paper precisely defines the two roles (trainer and verifier), the formal functions T-Train and Verify, and the defender's fidelity, low-invasiveness, harmlessness, and efficiency goals (Section 3). This framing cleanly distinguishes TDP from prior work on ownership verification, dataset inference, and PoTD, which target related but different objectives.

2. **Novel Data Probe concept with a principled integrity-binding mechanism.**  
   The Data Probe relaxes watermarking's requirement for a directed (targeted) output — it only requires a detectable distributional difference between probe and non-probe samples (Definition 3, Section 4.2). The keyed-hash probe selection (Algorithm 1, Lines 3–4) binds dataset integrity to probe detectability: any change to $\mathcal{D}$ changes the hash, changes the probe selection, and causes verification to fail. This is the paper's core technical insight and is cleanly motivated.

3. **Extensive empirical evaluation across multiple dimensions.**  
   The paper evaluates four probe types across four datasets (CIFAR-10/100, SVHN, Tiny-ImageNet), four architectures (ResNet18, MobileNet, ShuffleNet, DenseNet), multiple scoring methods (Conf, Loss, Entr, Mentr), probe quantities (0.1%–2%), and adaptive attacks (RQ4). Table 2 reports 128 combinations of settings, making this a thorough exploration of the design space.

4. **Negligible impact on model accuracy.**  
   Accuracy deviations from the unmodified model are consistently within ±1% across all settings (Table 2). This satisfies the harmlessness goal (G3) and is backed by five repeated runs.

5. **Systematic evaluation of adaptive attacks.**  
   RQ4 (Section 6.2, Table 3) tests the worst-case scenario where the attacker knows both the key **k** and the probe type, replicating the probe from the claimed dataset $\mathcal{D}$ and attempting to forge it into a model trained on a different $\mathcal{D}^*$. Results show that AP, UP, and TP maintain Attack Success Rates below 20% across 100 trials per attack, demonstrating non-trivial robustness even in the most challenging setting.

## Weaknesses

### Fatal
None.

### Major

1. **The threat model contains a tension the paper identifies but does not resolve.**  
   The protocol requires the trainer (who is the potential attacker in the threat model) to know the key **k** in order to compute `ProbeSelect(D, k)` during training and embed the probe. Since the attacker knows **k**, they can replicate the exact probe set corresponding to $\mathcal{D}$ and attempt to forge it into a model trained on a different dataset. The paper acknowledges this (RQ4 discussion, line 246: "keeping the user's key k hidden from the users, such as by implementing it through a server API, might be a solution") but does not implement or evaluate any concrete mitigation. While the empirical results in RQ4 show reasonable robustness for AP/UP/TP (ASR < 20%), this is an empirical finding without a formal security bound, and the structural flaw means the scheme's security guarantee is weaker than the paper's framing suggests. Readers need a clearer characterization of what the scheme guarantees and under what assumptions.

2. **Incomplete analysis of false positives in the mismatch setting.**  
   Table 2 reports mismatch metrics (PSA*, pV*) where the verifier computes the probe from the claimed dataset $\mathcal{D}$ while the model was trained on a different $\mathcal{D}^*$. Ideally these should cluster near PSA = 0.5 and pV > 0.1, indicating no separation. The paper's own description says some values deviate from this ideal (line 177: "most probes meet the aforementioned requirements" — implying some do not). However, the paper does not report standard deviations, set explicit detection thresholds with false-positive rates, or analyze *why* certain mismatch cases yield high PSA values. Without this analysis, the reliability of the method in practice — especially for distinguishing a modified dataset from an unmodified one — is incompletely characterized.

### Minor

3. **The case study's baseline comparison is informative but the paper overstates its force.**  
   Section 7 compares Data-Probe (DP) against off-the-shelf Watermarking (WM) and Dataset Inference (DI) on the task of rejecting modified datasets. WM and DI were designed for ownership verification, not TDP, so their failure to reject modified datasets is expected and confirms the paper's own prior analysis (Challenge 1, Section 4.1). The paper frames this as "only DP successfully denied verification" (line 269), which could give a misleading impression of a head-to-head competition. A more informative comparison would adapt these baselines to the TDP setting (e.g., by making them use dataset-derived triggers for WM or distribution-rejection rules for DI). This does not invalidate the results, but it limits what the comparison demonstrates.

4. **Implementation details for PP and AP weighting are insufficiently specified.**  
   The paper describes PP as "assigning a higher weight to the $\mathbf{x}_p$" and AP as "setting the probe weight to 0" (Section 5), but does not specify the exact weighting mechanism, the sampling strategy in the data loader, or the numerical weight values. These details are necessary for reproducibility and for understanding potential interactions with different training frameworks.

### Trivial
None.

## Nice-to-Haves

- A formal security analysis (even a heuristic bounding argument) for why the probe is hard to forge given knowledge of **k** would significantly strengthen the paper.
- An analysis of computational overhead for `ProbeScore` (which queries the model on all non-probe samples) would help practitioners assess scalability to very large datasets.
- Testing on non-standard architectures (transformers, multimodal models) would broaden the claim of model-agnosticity.

## Removed Points

These points from the original reviews were considered and removed:

- **"The case study does not test the most dangerous attacker"** — removed because the case study tests a *different* scenario (dataset modifications that change the hash). The adaptive attacker scenario is tested separately in RQ4. The paper separates these two threat models and evaluates both. The criticism conflates two distinct experimental designs.
- **"Table 3 shows the attack nearly succeeds (UP: PSA drops from 79.68 to 53.14)"** — weakened to Major weakness #1 above. The numbers cited appear plausible from the table image, but the paper's own ASR metric tells a more nuanced story: ASR < 20% for AP/UP/TP. The critic's framing ("nearly succeeds") overstates the results; a PSA of ~53 with a set threshold of 0.51 means the attack barely crosses detection threshold on average, and the ASR captures the actual failure rate.
- **"No discussion of computational overhead for ProbeScore"** — demoted to Nice-to-Have. The paper does report runtime comparisons in Table 4 which show DP is faster than WM and DI, partially addressing efficiency.
- **"No ablation on hashing algorithm or key size"** — demoted to Nice-to-Have. The security of the keyed hash is a standard cryptographic assumption; the paper's contribution does not depend on novel hashing.
- **"The paper claims the method is model-agnostic but only tests standard classifiers"** — this is a fair limitation note but is standard scope for an empirical paper. Moved to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions. The reviewing process surfaced the tension between the trainer needing to know **k** and the security model treating the trainer as a potential attacker, which is an insightful observation about the scheme's design limitations. However, the paper itself acknowledges this tension, so it is not a novel finding from the reviews.

## Suggestions

1. **Address the key-knowledge tension explicitly.** Either: (a) treat the protocol as having two security regimes — the non-adaptive case (dataset modifications) where guarantees are strong, and the adaptive case (attacker knows k) where guarantees are empirical and weaker; or (b) propose and evaluate a concrete mitigation (e.g., the verifier pre-computes the probe indices via a trusted third-party API without revealing **k** to the trainer, or uses a secure two-party computation to select probes without disclosing the key).

2. **Add a false-positive analysis.** Report the distribution of PSA and pV values under the null (mismatch) case, propose a concrete decision threshold with its associated false-positive rate, and discuss the cases where mismatch yields high separation (e.g., PP on CIFAR-100 ResNet18 in Table 2).

3. **Provide standard deviations for Table 2**, or at minimum for the mismatch columns where variability is most informative for assessing reliability.

4. **Specify the weighting mechanism for PP and AP.** Clarify the exact data-loader configuration (e.g., sample weights in PyTorch `WeightedRandomSampler`, exact weight values used, repetition counts) to enable reproduction.

5. **Clarify the scope of the baseline comparison.** Acknowledge that WM and DI are not designed for TDP and that the comparison illustrates their limitations rather than being a direct competition over a shared task.
