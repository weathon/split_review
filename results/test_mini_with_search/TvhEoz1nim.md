## Summary

This paper proposes DDMI (Diffusion Distillation Model Inversion), a framework that replaces GAN generators in generative model inversion attacks (MIAs) with single-step generators distilled from pretrained diffusion models via Score identity Distillation (SiD). The authors argue that GAN-based MIAs suffer from optimization instability and low reconstruction fidelity, that multi-step diffusion models are unsuitable due to computational/memory overhead and numerical error accumulation, and that distilled single-step diffusion models offer a superior alternative. They further extend generative MIAs to CLIP models for the first time. Experiments on classifier inversion (64×64 face datasets) show substantial improvements over GAN-based baselines, while CLIP inversion results demonstrate the feasibility of reconstructing facial features from multimodal models.

## Strengths

1. **Strong classifier inversion results support the core claim.** Table 1 (embedded image) shows that SDM-based DDMI consistently outperforms GAN-based baselines (GMI, LOMMA, PLG-MI) on Acc@1, KNN Dist, and FID at 64×64 resolution, including under distribution shift between public (FFHQ) and private (CelebA) datasets. The improvement is substantial enough to validate the main technical thesis.

2. **First generative MIA on CLIP models.** The paper extends the generative MIA formulation to CLIP by maximizing cosine similarity between generated image features and text-prompt features (Eq. 3). Table 2 (embedded image) reports quantitative improvements over the input-space CLIPInversion baseline across multiple CLIP encoders (ViT-B/16, ViT-B/32, ViT-L/14), and Figure 3 shows qualitative reconstructions of well-known figures. This opens a new direction for privacy auditing of multimodal models.

3. **Principled analysis of multi-step diffusion incompatibility (Section 3.2).** The paper identifies two concrete obstacles — high NFEs (e.g., 79 for EDM on 64×64 FFHQ) with memory-intensive gradient backpropagation, and accumulation of numerical errors from multi-step ODE solvers — that motivate the single-step distillation approach. This reasoning is clearly articulated and distinguishes the paper from naive DM-based baselines.

4. **Honest evaluation of limitations.** Section 4.2.2 transparently reports that SDM (FID 3.85) underperforms StyleGAN (FID 2.84) for CLIP inversion at 256×256+ resolution and discusses the resolution dependency. The paper also notes a mismatch between high metric scores and visual quality (Section 4.2.1), demonstrating intellectual honesty.

5. **Ablation studies quantify design choices.** Figure 4 examines the effect of the prior loss (adding it increases KNN distance, explained by label mismatch between public and private data) and the impact of more detailed prompts (reduces KNN distance for CLIP inversion), providing actionable guidance.

## Weaknesses

### Fatal
None.

### Major
None. The core claims (classifier inversion improvement at low resolution, first generative CLIP MIA) are supported by evidence in the paper. The acknowledged limitations are real but do not invalidate the contribution.

### Minor

1. **The inversion-specific distillation step is underspecified.** The paper claims novelty in "combining the diffusion distillation loss with the identity loss" (Section 4.2.1) for PLG-MI-style setups, but Section 3.3 — which should present the full framework — is truncated in the parsed text, and the main paper does not provide the joint objective function, loss balancing hyperparameters, or training procedure for this step. Without these details or an ablation isolating (a) frozen SiD generator vs. (b) SiD fine-tuned with identity loss, it is unclear how much the "inversion-specific distillation" contributes beyond using a better generator.

2. **The instability motivation (Figure 1a) is supported by only a single anecdotal trace.** Figure 1(a) shows fluctuations in attack accuracy over iterations for one method, with no error bars, no multiple runs, and crucially no comparison with DDMI's own stability. While this is a motivation point rather than a core technical claim, the paper's framing ("key limitations in GAN-based generative MIAs... instability") would be strengthened by quantitative evidence (e.g., variance across seeds, smoother convergence curves for DDMI).

3. **The comparative claim is broader than the evidence supports.** The abstract states that "single-step diffusion models-based MIAs significantly outperform their GAN-based counterparts" without specifying the resolution constraint. The paper itself shows that StyleGAN outperforms SDM for CLIP inversion at higher resolutions (Section 4.2.2). The dominance is clear at 64×64 classifier inversion but not universal. Scoping this claim more precisely in the abstract and conclusion would better align the paper's narrative with its evidence.

4. **Black-box and defense results are deferred entirely to the appendix.** The introduction claims superiority "in both white-box and black-box settings," but all main-paper results are white-box. While deferring to appendix is common practice, given that the claim is stated as a contribution, a brief summary table or bullet point for the black-box setting in the main paper would strengthen credibility.

### Trivial
None significant.

## Nice-to-Haves
- An ablation comparing (a) frozen SiD generator, (b) SiD generator fine-tuned with identity loss, and (c) full DDMI, to isolate the contribution of inversion-specific distillation.
- A small-scale comparison of a multi-step diffusion model (e.g., EDM with 10–20 steps) in the MIA pipeline to empirically validate Challenge-2 (accumulation of numerical errors).

## Removed Points
- **"CLIP inversion results are unverifiable because Table 2 was not rendered in the parsed text."** *Reason:* The table exists in the original submission as an embedded image. The parsed text's inability to read image-embedded numbers is a parser artifact, not an author error. The paper references and discusses the table's results in the body text.
- **"Missing black-box/defense results in the main paper is a significant weakness."** *Reason:* Deferring extensive results to the appendix is standard practice in ML venues. The claim is weakened to a Minor point 4 above (scope of introductory claim).
- **"Section 3.3 is truncated/underspecified"** is retained as Minor weakness 1, trimmed to emphasize the specific missing details rather than the truncation itself (parser artifact).
- **"FID computation is unreliable due to small sample size"** — *Reason:* Speculative; the paper does not specify sample sizes that would confirm this concern, and FID on reconstructed samples (not generator samples) follows standard practice in the MIA literature.
- **General scope-creep criticisms** (e.g., "no discussion of non-face domains," "no human evaluation") — *Reason:* The paper explicitly scopes itself to facial recognition and CLIP models; demanding evaluation on unrelated domains is outside scope.
- **Strength Finder strengths about "addressing an important problem"** — *Reason:* Generic; removed per filtering rules. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

The reviews surface an important nuance about the paper's scope that is underemphasized in the authors' own presentation: the advantage of single-step diffusion models over GANs for MIAs appears to be resolution-dependent. The strongest evidence is at 64×64 classifier inversion, while at 256×256+ resolutions (CLIP setting), StyleGAN still leads. This suggests the paper's core claim is not about the universal superiority of SDMs but about their specific suitability for low-resolution generative MIAs, where GANs' instability and mode-coverage limitations are most acute. The CLIP contribution stands on its own as a novel application regardless of whether SDM or StyleGAN is the better prior for that setting. A more precise scope statement would strengthen rather than weaken the paper.

## Suggestions
1. **Specify the inversion-specific distillation.** Provide the full joint objective, hyperparameters for loss balancing, and ideally an ablation isolating the distillation fine-tuning from the frozen generator baseline.
2. **Add variance/error bars to the instability motivation** (Figure 1a) across multiple seeds, and optionally show DDMI's own convergence trace for comparison.
3. **Scope the abstract's comparative claim** to low-resolution classifier inversion, and treat the CLIP contribution as a separate (novel but preliminary) finding with its own scope.
4. **Include a brief black-box summary** (one bullet or mini-table) in the main paper if space permits, to directly support the scope claimed in the contributions.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `Xv9lUIwPay.md` — Face privacy protection | 2.67 | 1 | Much weaker; the paper under review has concrete attack results and a clear contribution |
| `4eiydaPgEA.md` — FL gradient inversion | 3.00 | 1 | Weaker; less novel methodology, narrower focus |
| `lddpNkrgXV.md` — Revisiting MI evaluation | 4.00 | 1,2 | Similar score but different contribution (meta-analysis vs. new method); DDMI has stronger experimental substance |
| `n9Ps1SFOlE.md` — GradCFG | 4.50 | 1,2 | Comparable; both propose new inversion methods with some specification gaps. DDMI's results are more complete for the primary setting |
| `1mj4z3ZUeZ.md` — Trigger embeddings | 4.00 | 2 | Less directly comparable; DDMI has broader scope (classifier + CLIP) |
| `roYDAg8Hve.md` — Diffusion privacy analysis | 4.00 | 2 | More theoretical; DDMI has stronger empirical contribution |
| `ehgFLHihTw.md` — Score-based MIA on DMs | 4.00 | 2 | Different task (membership inference vs. reconstruction); DDMI is more novel in application |
| `rlq9aKsY7T.md` — GIT gradient inversion | 4.40 | 2 | Comparable technical level but different setting (gradient inversion); DDMI is better scoped |
| `wKi4Jeqqrb.md` — ReTrace unlearning attack | 5.00 | 2 | Comparable innovation level; both accepted as poster. DDMI has stronger quantitative wins in its primary setting |
| `7wjFjOzCtB.md` — No Prior, No Leakage | 5.20 | 2 | Stronger theoretical contribution but narrower empirical scope; DDMI is comparable overall |
| `uWvLZqxjmx.md` — NatADiff | 5.50 | 2 | Higher quality; cleaner evaluation and more thorough ablations. DDMI is slightly below this bar |
| `lL6htAaolp.md` — Why adversarially train DMs? | 6.00 | 2 | Cleaner formulation and more complete evaluation; DDMI has more scope issues |

**Round-1 bracket:** [4, 6]  
**Round-2 narrowing:** Compared to the 4.0–5.5 anchors (directly relevant to model inversion), the paper under review has solid experimental results and a clear motivating analysis, but the underspecified method detail and scope overclaim hold it back from being a clear accept. It sits below the 5.5+ anchors (NatADiff, etc.) which have cleaner evaluations and more thorough methodological specification, but above the 4.0 anchors which have either thinner contributions or more serious flaws.

**Final judgment:** The paper makes a genuine contribution to generative MIAs — strong empirical evidence at low resolution and a novel CLIP extension. The weaknesses are real but addressable: method specification, scoping, and supporting evidence for the instability motivation. None are fatal.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept (Poster)</decision>