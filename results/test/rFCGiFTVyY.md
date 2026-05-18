Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes FedSKU, a fine-grained backdoor defense for Federated Learning that goes beyond coarse-grained detection-and-discard approaches. Rather than simply removing identified malicious models, FedSKU uses trigger recovery (via MESA with a pre-aggregation trick) followed by a dual-distillation process: a "clean teacher" (previous-round global model) teaches the surrogate to ignore trigger patterns on poisoned data, while the backdoored model itself teaches the surrogate to retain benign knowledge on clean data. Experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet under Constrain-and-scale and DBA attacks show that FedSKU improves GACC by up to 6.1% over FLAME with low ASR, and outperforms naive extensions of NAD and BAERASER to the FL setting.

## Strengths

- **Novel framing of backdoor defense as selective knowledge utilization rather than coarse-grained removal.** The paper identifies a genuine limitation of existing FL backdoor defenses (they discard useful information along with the backdoor) and proposes a method to salvage benign knowledge from poisoned models. This directional contribution is articulated clearly in Section 1 and Figure 1.

- **Dual-distillation architecture with a principled loss design.** The method uses two distinct teachers to achieve selective unlearning in Eq. 2-4: one teacher (previous global model) suppresses trigger behavior on poisoned inputs, while the other (backdoored model) transfers benign knowledge on clean inputs. The ablation study (Table 3) verifies that the previous-global-model initialization is critical for maintaining high GACC compared to random or backdoored initialization.

- **Pre-aggregation trick for trigger recovery efficiency.** Recognizing that colluding attackers share a common malicious objective, FedSKU pre-aggregates backdoored models before trigger recovery (Section 4.2), reducing per-client overhead. This is a practical concern not addressed by methods like BAERASER.

- **Consistent GACC improvement across settings.** The paper demonstrates that FedSKU improves accuracy over FLAME and Krum across multiple datasets (CIFAR-10, CIFAR-100), attack types (Constrain-and-scale, DBA, Badnets), and non-IID degrees (Table 4), while maintaining low ASR. The trend of improvement is consistent and sustained across malicious ratios from 0.1 to 0.4 (Figure 4).

- **Demonstrates that existing unlearning/distillation methods (NAD, BAERASER) fail when naively extended to FL.** Table 1 shows these methods exhibit high ASR in FL scenarios (e.g., >95% on CIFAR-10), while FedSKU's FL-specific designs achieve both low ASR and high GACC.

## Weaknesses

### Major

- **The "clean teacher" can be contaminated, creating an unacknowledged circular dependency.** The distillation framework in Section 4.3 uses the previous-round global model $T(x)$ as the "clean teacher," described as "a clean model" (line 123). However, in a running FL backdoor attack, the global model becomes progressively poisoned over rounds if any attacks evade detection. The paper never discusses this possibility, tests its impact, or specifies the round at which FedSKU is applied. This is not an edge case — it is the primary threat model for FL backdoors. If the global model already encodes trigger behaviors, Eq. 2 may reinforce rather than erase the backdoor. The experimental results in favorable settings (where the global model likely stays clean due to strong base defenses) may not generalize to later rounds or stronger attacks.

- **Trigger recovery quality is never evaluated, yet the method depends on it entirely.** Section 4.2 adapts MESA for trigger recovery with a pre-aggregation trick, but the paper reports zero metrics on recovery fidelity — no cosine similarity between recovered and true triggers, no attack success rate when the recovered trigger is inserted into a clean model, no ablation comparing FedSKU's performance with a known ground-truth trigger versus the recovered trigger. Since the distillation loss in Eq. 2 directly conditions on the recovered trigger distribution $G(z)$, an inaccurate or incomplete trigger could mean the unlearning targets the wrong distribution, making the defense's success hinge on an unvalidated component.

- **No direct evidence that FedSKU preserves genuinely client-specific knowledge beyond what the global model already provides.** The paper claims FedSKU "extracts the clean knowledge of the backdoored model for later aggregation," but the dual distillation uses the previous global model as both the initialization and one of the two teachers. The natural question is: what unique knowledge does the backdoored model contribute that the global model does not already contain? The non-IID experiments (Table 4) show that in high non-IID settings (where client-specific data is most valuable), FedSKU's GACC advantage over FLAME actually shrinks — a pattern consistent with the surrogate model inheriting mostly global model knowledge. The paper should compare against a detection+discard baseline with equal computation budget to isolate the value of the "salvaged" knowledge.

- **The central framing oversells "decomposition" when the actual mechanism is a heuristic distillation.** The paper presents itself as decomposing the model into $M_{att}^{tri}$ and $M_{att}^{use}$ (Definition 3.1) — a framing that implies parameter-level separation. The actual method is a dual-distillation process that produces a surrogate model with clean behavior. This is a reasonable heuristic, but the paper provides no analysis showing that the distillation actually "isolates" or "extracts" anything specific. The language of decomposition implies a precision the method does not deliver, and the paper should clearly describe what the method does (produce a model that behaves cleanly via distillation) rather than what it metaphorically aims to do (decompose parameters).

### Minor

- **Inconsistent ASR increase claim.** The abstract states "negligible ASR increase (<0.01%)" (line 25), while Section 5.2 states "neglectable ASR increase (<1%)" (line 175). These differ by two orders of magnitude. The authors should verify which number is correct and ensure consistency.

- **Architecture mismatch across baselines in Table 1.** As the paper itself acknowledges (line 143), FLAME uses ResNet-18 while Krum/NAD/BAERASER use WideResNet. The key comparisons (FedSKU+FLAME vs FLAME, FedSKU+Krum vs Krum) are within-architecture and valid, but presenting all methods in a single leaderboard-style table is misleading. At minimum, the paper should report one setting with a unified backbone across all methods.

- **Adaptation of NAD and BAERASER to FL is not described.** Section 5.1 says these methods are "extended to the FL scenario" (line 161) but provides no detail on how this was done. The poor ASR of these baselines could result from a naive adaptation rather than a fundamental limitation, making the comparison uninformative. The paper should describe the adaptation or cite a source.

- **Citation swap in Section 4.1.** Line 83 attributes FLAME to "(Blanchard et al., 2017)" and Krum to "(Nguyen et al., 2022)" — the reverse of the correct attribution (FLAME = Nguyen et al., 2022; Krum = Blanchard et al., 2017). The correct citations appear earlier in Section 2.1 (line 39).

- **Trigger recovery changes from MESA are underspecified.** Section 4.2 describes the loss function borrowed from MESA (Eq. 1) and the conceptual idea of pre-aggregation, but does not explain how the FL-specific pre-aggregation modifies the original MESA algorithm mathematically. It is unclear whether the sub-models $G_1, ..., G_N$ operate on the pre-aggregated model or retain per-client granularity.

### Trivial

- The paper uses "neglectable" (line 175) where standard English uses "negligible."

## Nice-to-Haves

- **Computational cost analysis.** FedSKU requires trigger recovery (training multiple sub-models) plus dual distillation for each surrogate model. With many malicious clients, this could dominate server-side computation. A complexity analysis or wall-clock comparison with Krum/FLAME would help assess practical deployability.
- **Test the circular dependency explicitly.** Run an experiment where the global model is partially poisoned before FedSKU is applied (e.g., attack starts at round 5, defense at round 10) and compare ASR trajectories.
- **Replace trigger recovery with ground-truth trigger in one ablation** to measure how much of the defense's effectiveness depends on recovery accuracy versus the distillation design itself.

## Removed Points

- **"Malformed citation '(?Cao et al., 2019)' in Section 2.1."** This is a parser artifact from the PDF extraction; the original submission does not contain this formatting issue. Per hard rules, parser artifacts are not author errors.
- **"Citation placement swap between FLAME and Krum"** (the specific criticism about Section 4.1 references being swapped) — actually verified as a real error in the paper and moved to Minor weaknesses above. The removed point here is the malformed citation, which remains a parser artifact.
- **"Figure references in the text point to images that were stripped... the method description is incomplete without them."** The parser strips figures from all papers; this is a property of the review format, not a flaw in the paper itself.
- **"The paper's own textual summary says 'up to 6.1%' accuracy gain with 'neglectable ASR increase (<1%)', which contradicts the abstract's claim of <0.01%."** This is a real inconsistency and is kept in Minor weaknesses above.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface methodological gaps and missing evaluations rather than offering new analytical angles on the problem.

## Suggestions

1. **Reconcile the ASR claim.** Choose one number (0.01% or 1%) that matches the actual experimental results and use it consistently throughout.
2. **Add a trigger recovery quality evaluation.** Report at minimum: (a) similarity between recovered and ground-truth triggers, (b) an ablation where FedSKU uses the ground-truth trigger instead of the recovered one, so the reader can assess how much performance depends on recovery accuracy.
3. **Address the clean-teacher circularity directly.** Add an experiment where the global model is partially poisoned before FedSKU is applied, or at minimum discuss why the setup avoids this dependency (e.g., FedSKU runs on top of a base defense that keeps the global model clean).
4. **Add a detection+discard baseline.** Compare FedSKU against simply omitting backdoored models with equal computation budget to isolate whether the knowledge salvage actually adds value.
5. **Describe the NAD/BAERASER extension to FL in more detail.**
6. **Fix the swapped citations** in Section 4.1.
7. **Use a unified backbone for at least one experimental setting** to enable clean head-to-head comparison across all methods.

## Score and Decision

This paper tackles a genuine limitation of existing FL backdoor defenses and proposes a novel, intuitively appealing approach. The core idea — selectively unlearning triggers while preserving benign knowledge — is timely and the experimental results show consistent accuracy improvements. However, the paper has several significant gaps that prevent acceptance in its current form: the "clean teacher" circular dependency is unexamined, trigger recovery quality is never validated, the central "decomposition" framing oversells what the method actually does, and there is an inconsistent ASR claim between the abstract (<0.01%) and the main text (<1%). These issues are addressable through additional experiments and analysis, but in their current form they leave the paper's contribution incompletely supported.

I recommend rejection in the current form, with the suggestion that the authors address the major weaknesses through additional experiments (trigger recovery validation, clean-teacher contamination test, detection+discard baseline) and resubmit.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>