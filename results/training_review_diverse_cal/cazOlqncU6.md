Now I have a thorough understanding of the paper and the validity of each reviewer claim. Let me produce the consolidated review.

## Summary

This paper formalizes the Trustworthy Dataset Proof (TDP) problem — verifying that a model was trained on the *complete* declared dataset — and proposes the Data Probe technique as a solution. The key idea is to use a keyed hash of the full dataset to pseudo-randomly select a small "probe" subset, then minimally modify those probe samples (via oversampling, label reassignment, etc.) so the trained model exhibits a detectable distributional difference between probe and non-probe outputs. Any modification to the training dataset changes the hash, altering the probe selection and causing verification to fail. Experiments across four datasets and architectures show the approach preserves model accuracy within ±1% while detecting mismatched datasets.

## Strengths

1. **Novel problem formalization.** The paper is the first to clearly distinguish the TDP problem (verifying the *complete and authentic* use of a dataset) from ownership-focused dataset provenance (watermarking, dataset inference, PoTD). The threat model in Section 3, including the fidelity (G1), low-invasiveness (G2), harmlessness (G3), and efficiency (G4) goals, cleanly exposes a previously unaddressed gap.

2. **Elegant integrity-binding via keyed hash.** The probe selection mechanism (Section 5) binds dataset integrity to probe identity: a keyed hash over the full dataset seeds probe selection, so any modification to the training data — even a single-sample duplication (0.01%) — changes the hash, causing the implanted probe to differ from the verifier-computed probe. Table 2 shows that matched probes yield high PSA and low pV while mismatched probes yield near-random metrics (PSA ≈ 0.5, high pV), and the case study (Table 4, Figure 6) confirms verification is blocked for tiny modifications.

3. **Minimal invasiveness.** The approach only requires data-level operations (oversampling weights, label reassignment) and black-box query access for verification. Accuracy degradation is consistently < ±1% across all tested configurations (Table 2), satisfying G3. The runtime comparison in Table 4 shows Data Probe (0.21s) is substantially faster than Dataset Inference (23.37s) and safer than watermarking (no backdoor exploit risk).

4. **Systematic exploration of design space.** Four probe types (PP, AP, UP, TP), four scoring methods (Conf, Loss, Entr, Mentr), and two detection metrics (PSA, pV) are evaluated, with Mentr identified as the most generally applicable. This gives practitioners a principled toolkit.

## Weaknesses

### Fatal
None.

### Major

1. **The "authentic use" framing is imprecise and risks misleading readers.** The protocol forces the trainer to alter the training data (oversampling, relabeling, or excluding probe samples) as part of operation `O`. The paper repeatedly claims to certify "the authentic use of a trustworthy dataset" (abstract, introduction), but the trainer never uses dataset `D` unmodified — they use `D` with probe-specific perturbations applied. The hash-binding ensures the trainer must start from `D`, which *partially* addresses this, but the paper never explicitly reconciles the framing with the protocol's reality. A reader expecting verification of `D` *as-is* will find this misleading. The paper should clearly state that what is certified is the use of `D` augmented with controlled probe modifications, and argue why this suffices for trustworthiness in practice.

2. **Adaptive attack vulnerability of PP is significant.** Table 3 shows that when the attacker knows the key, the PP (Prominent Probe) scheme is defeated with 95% ASR under Mentr scoring. The paper suggests hiding the key via a server API, but this introduces a trusted third-party dependency that should be discussed upfront in the threat model (Section 3) rather than as an afterthought in Section 6.2. The robustness claims in the abstract and conclusion should be qualified to reflect that PP is not robust against knowledgeable adversaries.

### Minor

1. **Verification cost reporting lacks transparency.** Table 4 reports Data Probe runtime as "0.21s" but does not state how many probe and non-probe samples were queried, nor the number of model forward passes this corresponds to. Without this breakdown, the efficiency claim (G4) cannot be independently assessed or compared across settings. The paper should report: number of probe samples, number of non-probe samples, and total query count for each dataset.

2. **Near-miss evaluation is incomplete.** The paper's main mismatched-dataset evaluation (Table 2, gray rows) tests only entirely different dataset pairs (CIFAR-10 vs. SVHN, etc.). The case study (Section 7) partially fills this gap by testing duplication (0.01%–1%) and backdoor embedding, which are near-miss modifications. However, it does not test other natural near-miss scenarios such as dropping a small fraction of samples, replacing a few samples, or adding novel samples from a similar distribution. While the hash-based mechanism theoretically catches all modifications, direct empirical validation of these specific scenarios would strengthen the fidelity claim (G1). The paper's current scope is sufficient for publication, but this is a clear area for improvement.

3. **PP probe's verification success on CIFAR-100/ShuffleNet is borderline in Table 2.** The PSA for PP on CIFAR-100 with ShuffleNet is not obviously above 0.5 in the table (the image is hard to read precisely), and some probe-type/dataset/architecture combinations show weaker separation. The paper notes that "most probes meet the aforementioned requirements" (Section 6.2), which hedges appropriately, but the limitations of specific probe-type choices could be discussed more explicitly.

### Trivial

- The PSA threshold of 0.51 used for ASR computation in the adaptive attack evaluation (Section 6.2) is briefly mentioned without justification. While a threshold slightly above 0.5 is reasonable for a decision rule, a brief justification would improve practical credibility.

## Nice-to-Haves

- A discussion of false positive rates for the PSA and pV metrics at different thresholds would strengthen practical credibility.
- Testing probe detectability when the probe set overlaps with backdoor triggers or other intentional modifications would strengthen the robustness analysis.
- An ablation showing why Mentr outperforms other scoring methods for specific probe types (beyond the TP label-dependence explanation) would deepen understanding.

## Removed Points

The following criticisms from the reviewer are removed for the stated reasons:

- **"Duplication results unexplained/appear to contradict the method's design"** — This criticism fundamentally misunderstands the hash-binding mechanism. The paper explicitly states (Section 5, Figure 6 caption) that *any modification to D* changes the hash value, which changes probe selection. Duplication adds samples to D, creating D* with a different hash, so probe selection differs at training time vs. verification time. The 0% verification success is the *intended and explained* behavior. The paper's Figure 6 caption directly notes "HASH(train) shows the hash value computed on the tampered dataset during probe implantation, which differs from the HASH(test) obtained on the declared untampered dataset (CIFAR-10) during testing."

- **"Near-miss evaluation considers only large unrelated dataset pairs"** — This is factually incorrect. The case study (Section 7, Table 4) explicitly tests near-miss modifications: duplication of 0.01%–1% of samples and backdoor embedding with minimal noise (l∞=8/255). These are precisely near-miss scenarios. The criticism is downgraded to a minor point about completeness (testing dropping/replacing in addition to duplicating/backdooring).

- **"Empty probe set / overlapping probe and non-probe sets"** — The probe set is never empty by construction (Algorithm 1 selects probes from D). The concern about original versions of probe samples being in the non-probe set is an edge case that does not affect the method's validity, as the probe samples are modified (oversampled/relabeled) before training, making them distinct from their original versions.

## Novel Insights

The key insight that emerges from reading the reviews against the paper is that this work sits at an intersection of security, trust, and dataset provenance where the framing matters enormously. The core technical contribution (keyed-hash-bound probe selection + distributional detection) is sound and clever, but it inherits a fundamental tension: to certify "authentic use" of a dataset, you must first modify it. This is structurally similar to how watermarking works (you mark data to prove it was used), but the paper's framing as "trustworthy dataset proof" rather than "dataset usage certification" sets up expectations the protocol cannot quite meet — namely, that the verifier checks the unmodified dataset. The reviews' fixation on this framing gap, even when overstated, signals that clearer epistemological positioning would significantly strengthen the paper's reception.

## Suggestions

1. Rename or reframe the contribution from "certifying authentic use" to "certifying complete and correct dataset provenance" or similar, and add a paragraph explicitly addressing why embedding probe operations does not violate the spirit of verifying dataset `D` (e.g., the operations are minimal, controlled, and the hash-binding ensures `D` cannot be substituted).

2. Add the PP adaptive-attack vulnerability to the threat model discussion in Section 3, and qualify robustness claims accordingly.

3. Report verification cost transparently: state the number of forward passes (probe + non-probe samples used) corresponding to the reported runtime.

4. Add one experiment showing verification success/failure for a "drop 0.1% of samples" scenario and a "replace 0.1% of samples with similar ones" scenario.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>