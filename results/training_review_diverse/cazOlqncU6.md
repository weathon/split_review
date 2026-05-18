Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces the Trustworthy Dataset Proof (TDP) problem — verifying that a model was trained on the exact claimed dataset, not a modified version — and proposes a "Data Probe" technique. The core idea is to use a keyed hash of the full dataset to pseudo-randomly select a small probe subset, apply data-level modifications to it (e.g., oversampling, label perturbation), and then detect the probe's effect on model outputs during verification. Any change to the dataset would change the hash and thus the selected probe, causing verification to fail. The paper formalizes the problem, evaluates four probe types and four scoring methods across four datasets and four architectures, and compares against watermarking and dataset inference in case studies including a Witches' Brew backdoor attack.

## Strengths

- **First formalization of the TDP problem with a clear threat model.** The paper defines TDP as distinct from ownership verification (which existing watermarking, membership inference, and dataset inference address), introducing explicit defender goals (fidelity, low-invasiveness, harmlessness, efficiency) and attacker capabilities (Section 3). This provides a useful conceptual foundation regardless of the specific implementation.

- **Hash-bound probe selection ties integrity to the claimed dataset.** The probe selection mechanism uses a keyed hash of the entire dataset as a random seed, so any modification to the training data during training changes the hash and thus the probe set, causing verification to fail. The case studies (Section 7, Table 4) demonstrate this convincingly against both simulated modifications and a Witches' Brew backdoor attack, where Data Probe succeeds while watermarking and dataset inference fail.

- **Model-agnostic and minimally invasive design.** The probe implantation operates entirely at the data level (weighted sampling, label perturbation) and does not require access to model architecture, training hyperparameters, or white-box model access (Section 5). This directly addresses usability challenges that the paper identifies in prior work.

- **Comprehensive empirical evaluation.** Experiments span four datasets (CIFAR-10, SVHN, CIFAR-100, Tiny-ImageNet-200), four architectures (ResNet18, MobileNet, ShuffleNet, DenseNet), four probe types, and four scoring methods (Section 6). Results are reported with means over five runs, including mismatched-dataset baselines and standard deviations. The finding that most probes harm accuracy by <1% supports the harmlessness goal.

- **Demonstrated advantage over existing methods in realistic attack scenarios.** The case study using Witches' Brew (Section 7, Figure 6) shows that Data Probe is the only method among watermarking, Dataset Inference, and Data Probe that consistently detects dataset tampering while maintaining low overhead and minimal security risk (Table 4).

## Weaknesses

### Fatal

None.

### Major

- **The key-secrecy tension weakens the integrity guarantee against a dishonest trainer.** The protocol (Algorithm 1) requires the trainer to know the key *k* to select and implant probes during T-Train_DP. A dishonest trainer who knows *k* can: train on a different dataset D', compute the correct probe set for the *claimed* dataset D using *k*, then fine-tune the model on that small probe set to implant the expected output difference, and pass verification. The paper evaluates this exact scenario in RQ4 (Table 3) and finds that some probe types (especially PP) have non-trivial Attack Success Rates. The paper acknowledges this and suggests "keeping the user's key k hidden from the users...through a server API" (Section 6.2), but this suggestion is not developed or evaluated. If the key is hidden from the trainer, how does the trainer compute the probe set for their specific dataset? The paper does not resolve this tension, which directly impacts the fidelity goal (G1). This is a structural limitation of the current protocol, not a minor implementation detail.

- **The paper's core claim — "only permits probe detection when the entire claimed dataset is utilized in training" — is not fully supported under active attacks.** While the hash binding ensures that any modification *during training* changes the probe, the adaptive attack scenario (train on D', then post-hoc implant probe from D) is only partially mitigated. The paper reports that "all probe schemes, except for PP, exhibit a certain degree of robustness" (Section 6.2), but "a certain degree" means some probes are vulnerable and the paper does not provide a formal security argument or bound on the attacker's success probability.

### Minor

- **The p-value threshold of 0.1 implies a 10% false positive rate, which is not adequately analyzed for a trust-enhancement application.** In a setting where the verifier is deciding whether a model was trained on compliant data, a 10% false alarm rate is substantial. The paper does not report ROC curves, discuss the trade-off between false positives and false negatives, or analyze how different thresholds would affect reliability. While the PSA metric (>0.5) is also used, its calibration is not characterized either. Some results in Table 2 (e.g., AP on SVHN: PSA 52.1, pV 0.18) are borderline even for honest trainers, raising questions about decision reliability in practice.

- **No formal security definition or security game.** The threat model (Section 3.2) defines attacker goals and defender goals qualitatively, but there is no formal cryptographic game (specifying oracle access, success conditions, security parameter) that would clarify exactly what guarantees the scheme can and cannot provide. This makes it harder to assess whether the protocol's security is adequate or where it falls short.

### Trivial

- The term "data-drobe" appears once in Section 1 (line 4 of the abstract section) — possibly a rendering artifact, but should be checked.
- Some figure references (e.g., "Fig. 9" mentioned but may not be present in the main body) could be clarified.

## Nice-to-Haves

- A detailed protocol resolving the key-secrecy tension would significantly strengthen the paper. Options include: (a) a commitment-based protocol where the trainer commits (hashes) the dataset before receiving the probe set from a verifier-run service, (b) a trusted execution environment approach, or (c) a security analysis that formally characterizes what guarantees remain even when the attacker knows *k*.
- ROC curves or an operating-characteristic analysis for probe detection at multiple thresholds, clarifying the false-positive/false-negative trade-off.

## Removed Points

- **Mechanical issues/typos** ("intergrity," "data-drobe," "generdetected"): Removed per instructions — these are parser artifacts from PDF extraction, not author errors.
- **Criticism that "the integrity guarantee collapses" entirely**: Removed as an overstatement. The paper explicitly tests adaptive attacks (RQ4, Table 3), reports varying ASR values, acknowledges the limitation, and suggests mitigations. The integrity guarantee is weakened but does not "collapse" for all probe types.
- **Criticism about missing appendix content**: Removed per instructions — appendix content is stripped by the parser and exists in the original submission.
- **Complaint that key-secrecy "undermines G2 (low-invasiveness)"**: This is the same underlying issue as the first major weakness, not a separate structural problem. It's addressed by the major weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's framing (TDP as a new problem) and its empirical strengths, while the main disagreement is about the severity of the key-secrecy tension — the harsh critic views it as fatal, while a more measured assessment sees it as a significant but addressable gap that does not invalidate the paper's broader contribution.

## Suggestions

- **Resolve the key-secrecy tension explicitly** in the next revision by proposing and evaluating a concrete protocol that either: (1) uses a commitment scheme where the trainer hashes D and sends the hash to a verifier-run service, receives the probe set in return, and the verifier stores the key; or (2) formally analyzes what security remains when the attacker knows *k*, with bounds on ASR. Without this, the protocol is best described as a *heuristic deterrent* against dataset modification rather than a rigorous integrity guarantee.

- **Add an operating-characteristic analysis** for probe detection, reporting false positive and false negative rates across a range of PSA and pV thresholds. This is essential for any trust-enhancement application where the consequences of false alarms are significant.

- **Clarify the threat model** by formally defining which secrets the attacker has access to (the key *k*, the claimed dataset D, the probe type, the scoring method) and which operations the attacker can perform (post-hoc fine-tuning, full retraining, etc.). The current adaptive attack evaluation (RQ4) is a good start, but a game-based security definition would make the assumptions and guarantees precise.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>