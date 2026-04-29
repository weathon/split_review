## Summary

The paper introduces “neural phishing,” a training-data poisoning attack in which an adversary inserts a small number of benign-looking examples that make a later-trained language model more likely to memorize and reveal unrelated PII-like secrets. The empirical results show nontrivial exact extraction rates for high-entropy numeric secrets under relatively weak poisoning assumptions, and further explore how attack success changes with poison count, secret length/duplication, model size, approximate prefix priors, randomized inference, and delay between poisoning/secret exposure/querying.

## Strengths

- **Concrete and surprising attack result under weak poisoning assumptions.** The paper shows that random benign-looking poison sentences with no overlap with the secret can yield around 10–15% exact extraction of 12-digit secrets with tens of poisons, while poisoning-free models never extract the secret and random guessing would be \(10^{-12}\) (lines 101–119). This is a strong empirical demonstration because the metric is exact-match on high-entropy suffixes rather than partial overlap or low-entropy leakage.

- **The attack does not require exact knowledge of the secret prefix during poisoning.** Section 4 shows that broad structural priors such as GPT-generated biographies of “Alexander Hamilton,” “a woman,” or “a man” substantially improve extraction over random prefixes, with the Hamilton biography prior reportedly reaching about 40% SER despite high edit distance from the true prefix (lines 209–216). This supports the central claim that the attacker can exploit vague knowledge about the format of sensitive records.

- **The paper studies several important scaling and robustness dimensions rather than only one proof-of-concept point.** The experiments vary secret length and duplication (lines 157–160), model size from 1.4B to 6.9B parameters (lines 162–163), pretraining/finetuning progress (lines 164–170), randomized inference prompts (lines 225–227), and durability after clean training (lines 249–260). This makes the empirical case more informative than a single attack setting.

- **The “not” poison design is a useful empirical insight.** The paper identifies a failure mode where too many similar poisons lead the model to memorize the poison suffix rather than the target secret, and shows that appending “not” before the poison digits avoids the concave degradation in Figure 1 (lines 121–128). This is a concrete and actionable observation about how poison semantics affect memorization behavior.

- **The paper explicitly investigates temporal durability, which is central to the pretraining-poisoning threat model.** The authors do not merely assume that poisoning and secret exposure are adjacent: they test clean-training delays after poison insertion and after the model sees the secret (lines 249–260), finding that poisoned behavior can persist for many clean steps, although it also decays.

## Weaknesses

### Fatal

None.

### Major

- **The practical threat model still depends on several timing assumptions that are only partially resolved.** The paper explicitly states that, for computational efficiency, it often assumes the attacker can attempt extraction at each training step (lines 55–58), and later acknowledges that immediate prompting after the model sees the secret is unrealistic (lines 259–260). The durability experiments are valuable, but they also show that extraction degrades with clean training and can drop to 0 after sufficiently long delay after the secret is seen (line 260). This does not invalidate the attack, but it means the strongest extraction rates should not be interpreted as directly applying to arbitrary deployed finetuning pipelines where the attacker has no control over when the secret appears or when the model is exposed for querying.

- **The evaluation is still fairly controlled and narrow relative to the broad claims about PII leakage in real deployments.** The paper itself notes that, for computational efficiency, it mainly studies extraction of one secret and leaves thorough multi-secret investigation to future work (line 47). Most results are based on artificial high-entropy numeric secrets inserted into controlled prefix/suffix patterns. This is a reasonable experimental starting point, but it limits how confidently one can generalize the reported SERs to heterogeneous real corporate corpora, many secret formats, many users, and realistic data-ordering conditions.

- **The attack requires the poison to appear before the secret, which constrains some of the claimed deployment scenarios.** The authors explicitly list this as a limitation: “across all our experiments, the poison needs to appear in the training dataset before the secret” (lines 267–269). Poisoning pretraining can satisfy this ordering, but for uncurated finetuning or federated settings where the attacker cannot control ordering or training schedule, this remains an important practical constraint.

### Minor

- **Some extrapolations to much larger models and larger-scale pretraining are plausible but not fully supported by the experiments.** The model-scaling results are only for 1.4B, 2.8B, and 6.9B models, yet the paper speculates that the attack may be “much more effective” for 70B/180B-scale models (lines 162–163). The trend is suggestive, but the claim should be phrased cautiously because scaling behavior can change with training recipe, data filtering, alignment, and deployment constraints.

- **The deduplication-defense conclusion is somewhat stronger than what is directly tested.** The paper argues that deduplication is ineffective because randomized prompts make all 100 poisons unique (lines 25 and 219). This is good evidence against exact duplicate removal, but it does not fully evaluate stronger near-duplicate, semantic, anomaly, or PII-pattern filtering defenses. The claim should be narrowed to exact or simple deduplication unless broader defenses are tested.

- **The randomized inference result supports but does not fully prove the proposed “generalized memorization” mechanism.** Lines 225–227 interpret randomized inference improving extraction as validating that the model is being taught to memorize the secret rather than learning an exact prefix-to-suffix mapping. That is a reasonable interpretation, but the evidence is still behavioral; additional analysis of alternative explanations, such as prompt ensembling increasing coverage over nearby contexts, would strengthen the mechanistic claim.

### Trivial

None that should affect evaluation.

## Nice-to-Haves

- Evaluate the attack on more heterogeneous secret types and corpus contexts, including multiple simultaneous secrets and multiple users, since the paper currently focuses mainly on one numeric secret.
- Include stronger defense evaluations beyond exact deduplication, e.g., near-duplicate filtering, semantic clustering of poison templates, secret-pattern filtering, or training-time anomaly detection.
- Report attack success under more deployment-like query schedules, e.g., the attacker receives access only after a full finetuning run rather than at or near the secret exposure step.
- Add more model families and larger open models if compute permits, to substantiate the scaling extrapolation.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic provided no substantive review.** The harsh-critic input was only “I'm sorry, but I cannot assist with that request,” so there were no grounded criticisms to verify or include.
- **Formatting/typo issues in the extracted text.** The extracted paper contains artifacts such as visible `\input{...}` commands, revision markers, and occasional malformed words. Per the instructions, these are parser/PDF-extraction issues and are not considered weaknesses.
- **Missing appendix/proof/related-work concerns.** The extracted text references appendix material, but the parser may strip appendices; no criticism based on absent appendix material is included.
- **Generic strengths about the problem being important.** I did not include generic statements such as “privacy is important” as standalone strengths; only concrete empirical and methodological contributions were retained.

## Novel Insights

A key insight from synthesizing the review and the paper is that the contribution is not merely “models memorize secrets,” but that poisoning can alter the model’s later propensity to memorize a class of secret-bearing continuations even when the poison suffix differs from the target secret. The most interesting empirical evidence is the combination of weak-prior poisoning, the “not” intervention to avoid poison-suffix overfitting, and randomized inference improving extraction: together these suggest a broader training-time conditioning effect rather than a simple duplicated-string memorization attack. The main unresolved question is how robust this phenomenon remains in messy deployment settings with many secrets, unknown ordering, realistic filtering, and delayed black-box access.

## Suggestions

- Temper broad deployment claims by clearly separating: (i) strongest controlled setting results, (ii) approximate-prior results, (iii) pretraining-poison durability results, and (iv) realistic delayed-access scenarios.
- Expand the multi-secret experiment beyond a brief statement, since real privacy attacks would target many users/secrets and interference between secrets could materially affect SER.
- Rephrase the deduplication claim to “exact deduplication is insufficient” unless stronger deduplication/filtering defenses are evaluated.
- Add experiments where the attacker only queries after a fixed final checkpoint, rather than during or shortly after secret exposure.
- Provide more evidence across model families/training recipes before making strong claims about attack severity at 70B+ scale.

## Calibration and Score

### Calibration anchors retrieved

Topic-based anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vjel3nWP2a.md` — Avg human score 6.67, Accept. Similar LLM training-data extraction paper with strong practical extraction results on aligned/production models; the present paper is more controlled but introduces a distinct poisoning-based mechanism.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/590yfqz1LE.md` — Avg human score 6.75, Accept. Similar memorization/privacy-leakage topic under benign prompts; the present paper is more adversarial and mechanistic but less broad in real-world coverage.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jx6njBKH8E.md` — Avg human score 5.75, Reject. Similar fine-tuning-based amplification of memorization; compared with that anchor, this paper has a clearer exact-secret attack and more directly interpretable success metric.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KSBx6FBZpE.md` — Avg human score 6.25, Accept. Similar focus on leakage of complex single-occurrence sensitive sequences; the present paper adds an active poisoning threat model.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Y4aWwRh25b.md` — Avg human score 6.75, Accept. Similar empirical data-extraction security paper with strong leakage results; that paper is broader in production/RAG evaluation, while this paper is more novel in training-time poisoning.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7erlRDoaV8.md` — Avg human score 7.50, Accept. Related to defenses against secret leakage from LLM weights; less directly comparable, but indicates strong LLM privacy work can score higher when the contribution is clearly actionable and well scoped.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eiqrnVaeIw.md` — Avg human score 4.11, Accept. Related persistent pretraining poisoning paper; the present paper appears stronger and clearer in its empirical target and exact extraction metric.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/i2Ul8WIQm7.md` — Avg human score 5.80, Reject. Related privacy risk/extraction work for parameter-efficient finetuning; the present paper has a more distinctive attack and stronger controlled evidence.

Quality-pattern anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/g16vmAtJ8x.md` — Avg human score 6.00, Reject. Strong empirical privacy attack but with realism/over-optimism concerns; the present paper has similar practicality limitations but a more coherent threat model and more convincing exact-match evaluation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mFTPRV5hYw.md` — Avg human score 6.00, Reject. Effective privacy attacks with concerns about access assumptions and scale; comparable caution applies here, though the present paper’s attack assumptions are better justified.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EBUoTvVtMM.md` — Avg human score 5.50, Reject. Strong LLM user-inference attack but with confounds and simplifying assumptions; the present paper is more controlled and better isolates the causal effect of poisoning.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dRel8fuUK4.md` — Avg human score 6.00, Reject. Membership-inference attack with strong empirical results but practical concerns; the present paper is above this due to novelty and clearer attack success metric.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5dttvRONu0.md` — Avg human score 3.67, Reject. Privacy attack paper with severe realism/experimental-support concerns; the present paper is substantially stronger and does not have comparable methodological failure.

High-band anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kmn0BhQk7p.md` — Avg score 7.20, Accept. Strong LLM privacy paper on personal-attribute inference; the present paper is in a similar quality range, though more controlled experimentally.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oZtt0pRnOl.md` — Avg score 8.00, Accept. High-scoring privacy-preserving LLM method; less directly comparable because it is a defense/method paper with formal privacy motivation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/60Vd7QOXlM.md` — Avg score 6.50, Accept. Related memorization-auditing work; the present paper has a stronger adversarial narrative but similar empirical limitations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YLJs4mKJCF.md` — Avg score 6.00, Accept. Data-poisoning attack anchor; less LLM-specific, but useful as a lower high-band reference.

Medium-band anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4DoSULcfG6.md` — Avg score 5.33, Accept. Privacy/data-poisoning paper around membership leakage; the present paper is stronger in novelty and empirical clarity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rK0YJwL69S.md` — Avg score 5.50, Accept. Poisoning/backdoor defense paper; less directly comparable, but indicates mid-score work often has narrower or less decisive contributions.

Low-band anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/onvN3zsNMI.md` — Avg human score 3.50, Reject. Privacy/memorization mitigation paper with weak support and questionable privacy claims; the present paper is much stronger and empirically better grounded.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XcSJ6hoc1O.md` — Avg human score 4.00, Reject. LLM memorization prediction paper with low score; the present paper has clearer attack impact and stronger evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/asA7vvsgcI.md` — Avg human score 3.75, Reject. Membership-inference attack paper with weaker support; the present paper is substantially above this quality level.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Mb5vJijcHn.md` — Avg human score 3.50, Reject. Durable backdoor/federated learning paper with low score; the present paper’s durability evidence is more directly connected to its claims.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/S5JCqTJyKj.md` — Avg human score 3.00, Reject. Deferred backdoor paper with substantially weaker support; the present paper is clearly above this range.

### Overall assessment

This is an original and important empirical security/privacy paper. The core claims are mostly well supported within the controlled experimental setting: exact extraction of high-entropy secrets occurs at rates far above chance, and the paper provides useful ablations showing how priors, model scale, duplication, poison design, and temporal delay affect success. The main weaknesses are not fatal but are significant: the experiments are controlled, the threat model depends on ordering/timing, and some broad deployment/scaling/defense claims should be tempered.

Relative to the calibration set, this paper is stronger than the medium and low-scoring LLM privacy papers with unclear mechanisms or weak support, and it is comparable to accepted LLM extraction/privacy papers around 6.5–7.0. It is not quite at the strongest 8-level anchor because it lacks broad production-scale validation and still relies on controlled synthetic secret settings. I would place it slightly above the 6.5–6.75 accepted extraction anchors due to the novelty of the poisoning-based mechanism, but below the highest anchors because of the practical-scope limitations.

## Score and Decision

Score: **7.0 / 10**

Decision: **Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>  
MY FINAL DECISION: <orange>Accept</orange>