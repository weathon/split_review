## Summary
FTA proposes a backdoor attack on federated learning that uses a generative trigger function (trained via a generator network) to produce sample-specific, imperceptible triggers that are adaptive across FL rounds. The core mechanism — aligning poisoned samples' latent features with those of benign target-label samples — is well-motivated by three identified failure modes (P1–P3) of prior fixed-trigger attacks. The method is clearly presented, and the mechanistic evidence (t-SNE visualization, update-similarity metrics) provides credible support that FTA indeed produces more natural-looking malicious updates than fixed-trigger baselines.

However, the paper oversells its claims relative to the evidence. The most significant gap is the repeated assertion that FTA evades the FLIP trigger-inversion defense — presented as a key advantage over prior work — with zero experimental evaluation of FLIP anywhere in the paper. Additionally, the paper claims "state-of-the-art" performance but compares only against fixed-trigger attacks (DBA, Neurotoxin, Edge-case, baseline), omitting the most relevant competitors: generator-based attacks (e.g., LIRA, IBA) that are discussed qualitatively in Section 2.2. The defense evaluation is also narrower in the main body than advertised: only 2 of 8 claimed defenses are shown in the main paper; the rest are appendix-referenced.

## Strengths
- **Feature-alignment mechanism with concrete visualization evidence.** The t-SNE analysis (Figure 5a–5b) directly demonstrates that FTA's poisoned samples' feature representations overlap with benign samples of the target label, whereas the baseline attack's poisoned features form a separate cluster. This provides clear mechanistic evidence for why FTA reduces the feature-extraction anomaly (P1) and backdoor-routing abnormality (P2). The update-similarity metrics (Figures 5c–5d, Euclidean distances and cosine similarity) further corroborate that FTA's malicious updates more closely resemble benign ones.

- **Strong attack effectiveness on FedAvg and against two well-tested defenses.** Under standard FedAvg (Figure 3), FTA converges faster and achieves higher backdoor accuracy than all baselines across four datasets. Under norm clipping (Figures 4a–4d) and FLAME (Figures 4e–4h), FTA maintains high BA (e.g., >99% on CIFAR-10 and Tiny-ImageNet under FLAME) where prior attacks are substantially suppressed. These results are well-presented and support the method's practical effectiveness.

- **Clean bi-level optimization design with practical two-phase training.** The separation of generator training (Stage I) and malicious classifier training (Stage II) within each local epoch (Algorithm 1, Section 3.3) is sensible and addresses the instability of naive alternate updating. The justification that the generator remains effective across rounds because the model changes little during the small number of poisoning epochs is plausible and practically motivated.

## Weaknesses
### Fatal
None.

### Major

- **No experimental evaluation against FLIP despite repeatedly claiming FLIP evasion as a key advantage.** The paper mentions FLIP four times (Abstract, Introduction line 53, Section 2.2 lines 153–154, Conclusion framing) as a defense that FTA "naturally evades" — yet presents no experimental results against FLIP. The argument is purely qualitative (FLIP inverts universal triggers; FTA uses per‑sample triggers, so FLIP is ineffective). This is a logical claim, but it is presented as an empirical advantage and would benefit from at least a simple experimental validation. Without it, a central advertised selling point of the method is unsupported.

- **No comparison with generator-based or imperceptible-trigger attacks (LIRA, IBA, etc.).** Section 2.2 ("v.s. Trigger generators in centralized setting") discusses these methods extensively and argues why they are insufficient for FL. Yet the experiments compare FTA only against DBA, Neurotoxin, Edge-case, and a baseline — all fixed-trigger attacks. The "state-of-the-art" claim is unsubstantiated against the most relevant family of competitors. At minimum, a generator-based attack adapted to the FL setting should be included as a baseline.

### Minor

- **t-SNE caption/text contradiction.** The figure caption (line 458) states "T-SNE visualization of hidden features of input samples in **Fashion-MNIST**," but the accompanying text (line 462) says "We use t-SNE visualization result on **CIFAR-10**." This is a factual error that must be corrected.

- **Defense evaluation in the main paper does not fully support the "eight defenses" claim.** The paper claims effectiveness against "eight well-studied defenses" (Abstract, line 98) and "8 SOTA robust FL defenses" (line 344), but the main body provides quantitative results for only two: norm clipping and FLAME. The remaining six (Multi-Krum, Trimmed-mean, RFA, SignSGD, Foolsgold, SparseFed) are listed and referenced to the appendix (lines 347–349), but no summary table or aggregated visualization appears in the main paper. While appendix results likely exist (the parser strips appendix content), a main paper claiming breadth should include a compact summary table.

- **Unqualified statement about malicious update magnitudes.** Line 151 states "the magnitude of malicious updates is usually larger than that of benign updates under FL setups" without citation. This is not universally true (e.g., Neurotoxin deliberately produces small-magnitude updates) and should be qualified or cited.

### Trivial
- Duplicate "Ablation Study in FTA Attack" heading at lines 472 and 534.

## Suggestions
1. **Add a FLIP experiment.** Even a simple evaluation showing backdoor accuracy after FLIP-based sanitization would substantiate the paper's most prominent claimed advantage. This is the single highest-leverage improvement.

2. **Include at least one generator-based attack baseline.** Adapt LIRA or IBA to the FL setting, or construct a version of FTA with a static (non-adaptive) generator to isolate the benefit of adaptivity.

3. **Add a consolidated defense summary table in the main paper.** A table reporting BA at a fixed round (e.g., round 200) under each of the eight defenses across all attacks would make the "eight defenses" claim verifiable without requiring the reader to consult the appendix.

4. **Fix the t-SNE dataset contradiction** between the figure caption (Fashion-MNIST) and the main text (CIFAR-10).

5. **Qualify or cite the claim** about malicious updates having larger magnitudes than benign updates (line 151).

## Score and Decision

The paper presents a novel and well-motivated attack mechanism with solid preliminary evidence. However, the gap between claims and evidence is significant: the method is advertised as evading FLIP with no experimental support, and the "state-of-the-art" claim rests on comparisons that exclude the most relevant baseline family. These gaps are addressable in revision but make the paper unsuitable for acceptance in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
