Now I have enough information from the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

DeTrans is a dual-protection framework for on-device DNN model IP protection, addressing for the first time the joint problem of (1) preventing unauthorized inference on the source domain and (2) preventing cross-domain transfer of the extracted model. The method selectively modifies the weights of the highest-transferability filter per convolutional layer using bi-level optimization, and stores the original weight values in TEE secure memory to restore functionality for authorized users. Experiments show DeTrans degrades source-domain accuracy to ~10% (random guessing) while reducing target-domain transferability by up to 81.23%.

---

## Strengths

- **Genuine, novel dual-protection problem formulation**: The paper is the first to simultaneously address unauthorized inference and cross-domain transfer. The observation (validated by Table 2) that NNSplitter reduces source accuracy to ~10% yet achieves only 0.46%/0.39% transferability reduction is a strong, concrete negative result that clearly motivates why a new approach is needed — degrading source accuracy is insufficient for transfer prevention.

- **Bi-level optimization is empirically demonstrated as necessary**: Table 3 contrasts the naive alternating optimization (1.3% accuracy drop, even with full target-domain knowledge) against bi-level optimization (80%+ drop). This ablation concretely establishes the necessity of the bi-level formulation. Combined with the NNSplitter comparison, which shows simple source-accuracy degradation leaves transferability intact, the evidence is consistent that the bi-level component is doing real work.

- **Practical TEE integration is carefully analyzed**: The modification of only 0.07–0.18% of parameters, yielding 79–122 KB of secure storage, is a concrete result showing the authors genuinely evaluated hardware feasibility rather than treating TEE as a black box. This distinguishes DeTrans from methods that propose TEE integration only in principle.

- **Post-processing applicability**: Unlike NTL and CUTI (which train from scratch and inherently sacrifice model owners' own transferability), DeTrans operates as a post-processing step on any pre-trained model — a practically significant advantage, well justified in Sec. 2.4.

---

## Weaknesses

### Fatal
- None.

### Major

- **Missing "basic protection only" ablation for transfer prevention (partially addressed, but gap remains)**: The paper's central technical claim is that bi-level optimization is the key mechanism for dual protection. The ablation in Table 3 compares bi-level vs. naive alternating optimization (where the defender has direct target-domain knowledge), but does not test the simpler baseline: apply Eq. (4) alone (maximize source-domain loss, no bi-level) and then measure target-domain accuracy after attacker fine-tuning. The NNSplitter comparison partially fills this gap — NNSplitter achieves random-guessing source accuracy but negligible transfer reduction — providing indirect evidence that source degradation alone is insufficient. However, NNSplitter uses RL-based masking on a different subset of weights than Eq. (4), so the comparison is not exact. A direct Eq. (4)-only baseline tested on transfer would conclusively attribute the transfer-prevention effect to the bi-level formulation and not to the particular set of filters modified or to general model brokenness.

- **The claim that DeTrans achieves "comparable protection as SOTA works (NTL, CUTI) on transferability reduction, with difference less than 4%" conflates fundamentally different starting conditions**: NTL and CUTI preserve source accuracy (by design, for MLaaS); an attacker who obtains their model fine-tunes from a 80–90% accurate, well-learned representation. An attacker who obtains DeTrans's model fine-tunes from a random-guessing initialization. These are categorically different starting points for fine-tuning. The observed transferability reduction numbers are not on a level playing field. The paper should reframe this comparison more carefully — DeTrans's transfer prevention cannot be meaningfully claimed to be "comparable" to NTL/CUTI given the different initial attacker conditions.

### Minor

- **Fixed attacker data budget (5%) is the sole operating point**: All transfer experiments use 5% of target-domain data. As the paper itself notes, the defense is specifically designed to be robust to limited-data fine-tuning, so the boundary conditions — what happens at 10%, 20%, or 50%? — are unknown. At sufficient data, the defense might simply become training from scratch and lose relevance. This experiment would bound the threat model's practical scope.

- **Threat model is restricted to close target domains but only tested in the most favorable regime**: The paper explicitly scopes to target domains "close to the source domain, while sharing the same label space" (Sec. 2.1) and acknowledges this as a limitation. However, all experiments (MNIST↔USPS↔SVHN; CIFAR10↔STL10) are the maximally favorable instances of this assumption — semantically similar, same label taxonomy. Where the assumption begins to break down is not probed, leaving the effective protection boundary unknown.

- **ResNet-50 results are thin**: Table 5 presents a single CF10→? transfer result with no NTL/CUTI comparison, yet the claim in Sec. 5.2 that DeTrans "outperforms SOTA in reducing transferability" is made without those baselines in view. This claim should be qualified or the baselines included.

### Trivial

- The label in Eq. (1) notation (`Q(x|\bar{z})` for the encoder) is unconventional — standard WAE/CVAE notation would write `Q(z|x)`. While likely a parser artifact, the encoder/decoder labeling should be clarified in any revision.

---

## Nice-to-Haves

- A feature-space visualization (t-SNE/UMAP) showing that protected-filter activations become uninformative across domains would strengthen the mechanistic story beyond accuracy numbers.
- Testing a moderately distant target domain (different imaging modality or sensor type) would bound the threat model's practical range and clarify when the auxiliary-domain approximation fails.
- Analysis of an adaptive attacker who knows DeTrans is deployed and regularizes fine-tuning toward original weights (the perturbation is small enough for TEE, which may also mean it is small enough to partially reverse).

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Critic concern about TEE side-channel security**: The paper cites prior TEE work and states TEE effectiveness is established. The harsh critic calls this "an overstatement." However, the paper is scoped to the specific use case of storing small weight differences in TEE, and the standard academic practice in this field is to cite TEE as an established primitive. This concern is out of scope.

- **Criticism of Eq. (2) as "dimensionally odd"**: The metric in Eq. (2) is cited from Wang et al. (2019a) and adopted as-is. Criticizing the metric in the context of this paper without formal proof that it fails here is speculative and represents a paper-external concern. The ablation (Fig. 3) shows empirically that the metric outperforms random selection by 14.95% on average, which is practical validation.

- **Concern that DeTrans's transferability reduction is entirely due to model degradation ("random-guessing initialization")**: This is substantially undermined by the NNSplitter result. NNSplitter also achieves random-guessing source accuracy, yet shows 0.46% transferability reduction. DeTrans achieves 81.23%. The 80%+ gap cannot be explained by the initialization quality alone — something beyond mere model brokenness is at work. The harsh critic's null hypothesis is disproven by the existing experiment.

- **Criticism of NNSplitter as a "straw-man" in Sec. 4.3**: The paper correctly notes NNSplitter was not designed for transfer reduction. Using it as a comparison is a fair choice — it represents what source-accuracy-only protection achieves on the transfer axis. Labeling this "misleading" is itself a misread.

- **Concern about 10 auxiliary domains being insufficient**: Whether 10 WAE-generated domains are adequate is an empirical question answered by the transfer results. The paper demonstrates effectiveness empirically; demanding a theoretical coverage guarantee is not standard in this field.

- **Strength Finder's generic claim that "the paper addresses an important problem"**: Removed per rules — generic.

---

## Novel Insights

The most genuinely novel observation synthesized across reviews is that the NNSplitter comparison functions as an *implicit "basic protection only" baseline for transfer prevention*: NNSplitter degrades source accuracy to the same random-guessing level as DeTrans, yet leaves transferability essentially intact (0.46% drop). This nearly eliminates the harsh critic's primary null hypothesis that model degradation alone explains DeTrans's transfer prevention, and makes the bi-level optimization's contribution more empirically credible than the critic acknowledges. However, the test remains indirect, and the "basic protection (Eq. 4) → transfer" experiment would close this gap definitively.

---

## Score and Decision

**Calibration Anchors** (all returned from batch search):

| Path | Avg Human Score | Comparison to this paper |
|---|---|---|
| `029hDSVoXK.md` | 6.80 (Accept) | Model extraction defense via dynamic early-exit; stronger and more comprehensive experiments, more ablations, accepted. Higher bar than DeTrans. |
| `f8S3aLm0Vp.md` | 6.50 (Accept) | IP protection for diffusion models; similarly novel problem framing with solid experiments. Comparable level of novelty. |
| `K7xpl3LZQp.md` | 6.25 (Accept) | Copyright tracking for VLMs via adversarial attacks; similar scope of IP protection experiments; arguably comparable to DeTrans in contribution depth. |
| `gjFgBfbP2C.md` | 5.25 (Reject) | NeuralMark watermarking; comparable scope but limited contribution and novelty beyond existing work. |
| `oxjeePpgSP.md` | 5.75 (Accept) | Bi-level trigger optimization for backdoor contrastive learning; similar use of bi-level formulation, accepted with similar experimental depth. |
| `OQccFglTb5.md` | 3.75 (Reject) | FT-Shield watermarking; weaker contribution and more critical flaws than DeTrans. |
| `sruGNQHd7t.md` | 3.00 (Reject) | Privacy-preserving domain shifting; clearly weaker and less principled than DeTrans. |
| `ywGSgEmOYb.md` | 4.40 (Reject) | Fine-tuning for backdoor mitigation; comparable experimental thinness, rejected partly for missing ablations. |
| `PCm1oT8pZI.md` | 5.75 (Accept) | OoD-image watermark injection; similar IP protection scope and experimental quality. |
| `RacYdzHxcz.md` | 3.50 (Reject) | Human-producible adversarial examples; clearly weaker contribution. |

**Calibration reasoning**: DeTrans sits above NeuralMark (5.25) and FT-Shield (3.75) on problem novelty and rigor, but below DNF (6.80) and DIAGNOSIS (6.50) on experimental completeness. The major missing ablation (Eq. 4-only baseline for transfer) is partially mitigated by the NNSplitter proxy result, but the misleading NTL/CUTI comparison and single data budget are real weaknesses. The score of papers accepted in this space with similar experimental scope clusters around 5.75–6.25. The structural comparison issue and single attacker data budget pull DeTrans below that range. Score: **5.0** — borderline, leaning toward weak reject absent revision of the NTL/CUTI comparison framing and addition of the Eq. (4)-only baseline experiment.

**Axis evaluation:**
- *Originality*: High — genuinely first to address dual protection jointly.
- *Importance of research question*: High — model IP protection is practically relevant.
- *Claims well supported*: Moderate — core claim is mostly supported, but the ablation for bi-level's transfer role is indirect and the NTL/CUTI comparison is misleading.
- *Soundness of experiments*: Moderate — single attacker data budget, only close-domain pairs, thin ResNet-50 section.
- *Clarity of writing*: Adequate — framework is well-described, related work positioning is clear.
- *Value to community*: Moderate-high — the NNSplitter negative result alone is useful.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>