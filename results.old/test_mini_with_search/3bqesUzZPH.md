## Summary

This paper proposes FTA, a generator-assisted backdoor attack against federated learning. The key idea is to train a trigger generator that produces sample-specific, imperceptible perturbations, and to continuously adapt this generator across FL rounds as the global model changes. This addresses three stealthiness problems (P1–P3): eliminating abnormal hidden features, reducing anomalous backdoor routing, and producing naturally imperceptible triggers during inference. The evaluation is thorough: four datasets (Fashion-MNIST, FEMNIST, CIFAR-10, Tiny-ImageNet), three model architectures, comparisons with three SOTA attacks (DBA, Neurotoxin, Edge-case) plus a baseline, and testing against eight defenses. Results consistently show high attack success rates (often >98%) while maintaining imperceptibility and evading detection.

## Strengths

- **Novel adaptive trigger generation for FL.** The paper introduces a generator $g_\xi$ that produces sample-specific, imperceptible triggers, and crucially updates this generator across FL rounds to adapt to the changing global model (Algorithm 1, Eq. 1). This is the first attack in FL to simultaneously achieve sample-specific flexibility and round-level adaptivity. Unlike prior FL backdoor attacks that use static universal triggers (DBA, Neurotoxin), FTA's triggers are different for each sample and each round, which is a meaningful extension of generator-based attacks from centralized settings to the decentralized, dynamic FL scenario.

- **Comprehensive and convincing empirical evaluation.** The paper evaluates against 8 defenses (norm clipping variant, FLAME, Multi-Krum, Trimmed-mean, RFA, SignSGD, Foolsgold, SparseFed) across 4 datasets. The results are striking: under FLAME, FTA achieves >99% BA on CIFAR-10 and Tiny-ImageNet while prior attacks drop to near 0% (Figure 3e–h). The t-SNE visualization (Figure 5a–b) provides mechanistic evidence that FTA's poisoned samples overlap with benign target-label features, explaining why cluster-based defenses fail.

- **Ablation study on trigger size.** The paper includes a clear ablation showing how the $l_2$-norm bound of the trigger (controlling imperceptibility vs. effectiveness) trades off, with direct visual evidence. This provides practical guidance for deploying the attack.

- **Well-motivated problem decomposition.** The paper clearly identifies three concrete stealthiness problems (P1: feature extraction abnormality, P2: backdoor routing abnormality, P3: perceptible triggers) and shows how each is addressed by the proposed approach. The bilevel optimization formulation (Eq. 1) is cleanly stated.

## Weaknesses

### Fatal
None.

### Major
- **t-SNE dataset inconsistency (Figure 4 / Section 5.3).** The figure caption (line 458) states "T-SNE visualization of hidden features of input samples in Fashion-MNIST" while the surrounding text (line 462) says "We use t-SNE visualization result on CIFAR-10." This is a factual error that must be corrected — one of the two is wrong. Since the figure shows label "7" (which exists in both datasets), the reader cannot determine which dataset was actually used. This undermines credibility of an otherwise informative visualization.

### Minor

- **Duplicated subsections (5.5 and 5.7).** The paper contains two "\subsection{Ablation Study in FTA Attack}" sections (lines 472 and 534). The first has full content (trigger size with figure, poison fraction text, dataset size text). The second is a stub that simply points to the appendix. This appears to be a drafting error and should be cleaned up.

- **Overclaimed novelty language.** Lines 6 and 79 use "for the first time" phrasing (e.g., "for the first time make the generated trigger to be stealthy, flexible and adaptive in FL setups"). Given that generator-based invisible backdoor attacks exist in centralized settings (Doan et al. 2021, Zhao et al. 2022, IBA) and are cited in Section 2.2, the novelty is specifically in adapting generator-based triggers to the FL scenario — not in the concept of a generator itself. The paper already makes this distinction in Section 2.2, so the "for the first time" inflation is unnecessary and risks triggering skepticism. Easy to fix.

- **Custom norm clipping variant lacks standard baseline.** The paper uses a variant of norm clipping (filtering extreme updates, computing adaptive norm bound) and cites FLAME for inspiration (line 409). The rationale is provided (unstable benign norms make fixed bounds ineffective). However, the paper does not compare against standard norm clipping (fixed threshold). While the variant is not obviously unfair to FTA, adding a comparison would eliminate this concern.

- **Missing variance/uncertainty in key results.** Figures 2 and 3 show single curves per attack without error bars or standard deviations. FL results are inherently stochastic due to random client selection; reporting variance across runs (e.g., shaded regions) would strengthen the evidence.

- **Computational cost deferred to appendix.** The main text only states "Our attack does not significantly increase the computational and time cost" (line 342) and references an appendix section. Because the attacker must train an additional neural network each round, a brief overhead estimate (parameters, seconds per round) in the main text would strengthen the practicality claim.

### Trivial

- The distance function $d$ in Eq. 1 is defined as L2 in the text (line 185, line 207) but not in the equation itself. Adding "$d(\cdot,\cdot)=\|\cdot-\cdot\|_2$" to the equation would improve clarity.

- The baseline attack from [pmlr-v162-zhang22w] is not given an explicit name in the comparison list (line 292), though it is clearly described as "baseline attack method" in context.

## Nice-to-Haves

- The paper could discuss whether the generator adaptation works when the server modifies updates via defenses (e.g., clipping, filtering). The threat model states the attacker does not know aggregation rules, but the implicit assumption is that the attacker can still observe the resulting global model and adapt. A brief note acknowledging this would strengthen the threat analysis.

- Including a brief summary of the SSIM/LPIPS values (currently only in the appendix) in the main paper's Section 5.6 would directly support the P3 (natural stealthiness) claim without requiring readers to consult the appendix.

## Removed Points

These points were reviewed and removed for reasons noted:
- **"Abstract 98% claim is overprecise"** — REMOVED. The paper reports "above 97% on average" (line 332) and 100% for Tiny-ImageNet. The abstract's "above 98%" is consistent with these results.
- **"Baseline attack not named"** — REMOVED. The paper cites the specific publication describing the baseline attack. This is standard practice.
- **"Missing generator architecture details"** — REMOVED. The paper states it uses the same architecture as [Doan et al. 2021] (autoencoder/U-Net). This is sufficient with the citation.
- **"Section 2.2 learning argument is vague"** — REMOVED. The paper provides a clear reasoning chain about why centralized generators fail in FL due to changing global models.
- **"Only 2 defenses shown in main paper"** — REMOVED. The critic acknowledged this is acceptable. The main text mentions 8 defenses and defers results to the appendix, which is standard.
- **"Test-time stealthiness needs user study"** — REMOVED. SSIM/LPIPS are the standard metrics for imperceptibility in this literature. A user study would be beyond scope.
- **"Generality to non-image domains"** — REMOVED. The paper is scoped to image classification, which is the primary FL backdoor attack setting. Scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviews largely corroborate the paper's claims rather than generating new observations. The one exception: the mechanism behind FTA's evasion of cluster-based filtering (t-SNE showing feature overlap) is well-explained by the paper itself and confirmed as a genuine strength by both the harsh critic and strength finder.

## Suggestions

1. **Correct the t-SNE dataset inconsistency.** This is the most critical fix — determine whether the figure is Fashion-MNIST or CIFAR-10 and make the text and caption consistent.
2. **Remove the duplicated Section 5.7** and integrate a brief summary of poison fraction and SSIM/LPIPS results from the appendix into the main text.
3. **Tone down "for the first time" language** to accurately reflect the contribution: adapting generator-based triggers to the FL setting rather than claiming the generator concept itself is novel.
4. **Add a comparison with standard (fixed-threshold) norm clipping** or explicitly justify why the adaptive variant is the appropriate baseline.
5. **Add variance information** (error bars or standard deviations) to the main results in Figures 2 and 3.

## Score and Decision

### Calibration Report

**Round 1 — Bracket:** Searched the human-review corpus for FL backdoor attack papers in three bands. The [0–3] band returned CABA (avg 3.00, Withdrawn), a reconstruction attack (3.00), and a label-flipping attack (3.00) — all clearly weaker than FTA in scope and evidence. The [4–7] band returned BAPFL (4.50, Reject) and POLAR (4.00, Reject). The [8–10] band returned papers unrelated to FL security (multimodal reasoning, quantum computing, 3D generation) — no high-scoring FL backdoor attack anchors exist in the corpus. Round 1 bracket: **[5, 7]**.

**Round 2 — Narrowing:** Searched within the [4.5–7.5] range. Retrieved AUPF (4.67, Reject — FL defense paper), BAPFL (4.50, Reject), a graph poisoning attack (5.00, Reject), and several robust aggregation/defense papers (5.50–6.00, Accept Poster). FTA is stronger than BAPFL (4.50) — BAPFL's main weaknesses (not evaluating against SOTA defenses like FLAME, non-standard FL setup) are weaknesses FTA does not share. FTA is stronger than POLAR (4.00), which has limited datasets, incremental novelty, and missing runtime analysis. FTA is stronger than AUPF (4.67), which was rejected for lacking novelty beyond repackaging existing components. FTA compares favorably to SABRE-FL (5.00, Accept Poster), though that is a defense paper in a different subproblem.

**Final score: 6.0.** FTA has a clear methodological contribution, the most comprehensive defense evaluation among comparable FL backdoor attack papers, and well-supported claims. The main issues are presentation-level (duplicated section, dataset inconsistency in one figure, overclaimed novelty language) rather than structural. These are all fixable and do not threaten the core claims.

### Anchors Considered

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| CABA | Vogxs8BzJS.md | 3.00 | R1 | Weaker — less thorough evaluation |
| Gradient reconstruction | 4eiydaPgEA.md | 3.00 | R1 | Different problem, weaker |
| Label flipping | KezVIhjQuu.md | 3.00 | R1 | Weaker in scope |
| Backdoor detection | PluWBC86I4.md | 1.50 | R1 | Irrelevant (detection, not attack) |
| BAPFL | bPN1c10U3P.md | 4.50 | R1/R2 | Weaker — lacks defense evaluation, non-standard setup |
| POLAR | NgGsjZ1G92.md | 4.00 | R1 | Weaker — limited datasets, incremental novelty |
| SABRE-FL | n1HBsszaY6.md | 5.00 | R1 | Defense paper; FTA is stronger in its category |
| AUPF | WZWLnivZAj.md | 4.67 | R2 | Weaker — defense paper, lacked novelty |
| Graph poisoning | 4bdCugosNW.md | 5.00 | R2 | Different problem domain |
| Robust FL (various) | gs6zKwv1gL.md, 1GMw3IwEHW.md, 47eKYCaBIV.md, lXSrulux48.md | 5.50–6.00 | R2 | Different subproblem (defense, not attack) |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>