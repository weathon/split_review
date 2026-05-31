## Summary

This paper introduces two methods to simplify and extend classifier-free guidance (CFG) for diffusion models. **Independent Condition Guidance (ICG)** shows that feeding an independent condition (random vector) to a conditional model yields the unconditional score, eliminating the need for auxiliary unconditional training (label-dropping) during training. **Time-Step Guidance (TSG)** perturbs the time-step embedding to create a guidance signal applicable to *any* diffusion model, including unconditional ones. Experiments across DiT, EDM, EDM2, and Stable Diffusion models demonstrate that ICG matches CFG performance, TSG significantly improves unconditional generation quality, and the two methods are complementary.

---

## Strengths

1. **ICG eliminates auxiliary unconditional training with strong empirical evidence** — Figure 3 shows that a purely conditional DiT model guided with ICG achieves consistently better FID across all training checkpoints compared to standard CFG with label-dropping (p=0.1), with ~30% faster convergence and ~20% lower FID at the same iteration count. This directly supports the paper's central practical claim.

2. **TSG is the first method to extend CFG-style benefits to unconditional diffusion models** — Table 3 reports substantial FID improvements on unconditional models: EDM2 from 1.78 to 1.26, unconditional DiT-XL/2 from 10.22 to 2.14. This fills a gap explicitly identified in the paper's motivation (line 12: "there has been no clear way to extend the benefits of classifier-free guidance beyond conditional models to unconditional generation").

3. **ICG quantitatively matches CFG across diverse model architectures** — Tables 1 and 2 show that ICG achieves nearly identical metrics to CFG on DiT-XL/2 (FID 2.23 vs 2.20), Stable Diffusion (FID 18.66 vs 18.43), EDM (1.88 vs 1.87), and EDM2 (2.08 vs 2.07). This consistency across both CFG-trained and non-CFG-trained models is compelling.

4. **Works on pre-trained models not designed for CFG** — Figure 5 shows ICG significantly improves ControlNet image-conditioned generation without any text prompt, and Table 2 successfully applies ICG to EDM/EDM2 models that were never trained with the CFG objective. This demonstrates broad applicability.

5. **ICG and TSG are complementary and can be combined** — Table 4 shows ICG+TSG on DiT-XL/2 achieves FID 1.98, outperforming either method alone (ICG: 2.23, TSG: 2.14) and far exceeding the unguided baseline (10.22).

---

## Weaknesses

### Fatal

None.

### Major

1. **Gap between the theoretical derivation and the network's behavior in ICG** — The derivation in Section 4 (Eq. 6–7) correctly proves that *for the true data distribution*, feeding an independent condition ŷ yields the unconditional score: ∇log p(z_t|ŷ) = ∇log p(z_t). However, the paper then assumes without argument that the *learned neural network* D_θ(z_t, t, ŷ) outputs this quantity for arbitrary ŷ that may be out-of-distribution relative to training (where ŷ was always the *true* condition of the image). The optimal network does indeed minimize toward E[x|z_t, ŷ] — and when ŷ is independent of (x, z_t), this target equals the unconditional denoising target E[x|z_t]. So the gap is not that the theory is wrong, but that the paper does not discuss why the network generalizes correctly to these out-of-distribution condition inputs. The strong empirical evidence (Tables 1, 2, 5) supports that the method *works*, but the paper's framing as a "theoretically motivated method" is slightly overstated without addressing this approximation gap. This is a significant oversight in the theoretical presentation, though the practical contribution remains intact.

### Minor

2. **TSG is not benchmarked against SAG/PAG for unconditional generation** — The paper acknowledges SAG (Hong et al., 2022) and PAG (Ahn et al., 2024) as methods that also improve unconditional UNet-based diffusion model quality (line 19) but positions them as "complementary." While the mechanisms differ (self-attention perturbation vs. time-step perturbation), a quantitative comparison on a common unconditional benchmark (e.g., unconditional DiT or EDM) would help establish TSG's relative effectiveness. Without it, the novelty claim ("first method to extend CFG-like benefits to unconditional models") is somewhat weakened, since SAG/PAG also boost unconditional generation quality through a different mechanism.

3. **The TSG–Langevin dynamics connection is heuristic and the specific scaling (s·t^α) is not derived from it** — Section 5 uses a first-order Taylor expansion to show that the TSG update step "resembles" a Langevin dynamics step. However, the actual implementation (perturbing the time embedding with Gaussian noise scaled by s·t^α and applying it selectively to certain layers) is not derived from this analogy; it is chosen "such that the scale of the noise portion becomes comparable to the scale of the time-step embedding" (line 120). The Langevin connection provides intuitive justification but does not predict or justify the specific design choices. The paper would benefit from either a tighter connection or a more modest framing.

4. **Default TSG hyperparameters for the main results are not explicitly stated** — The ablation (Table 6) explores various values of s, α, and layer indices, but the paper never states which specific configuration was used to produce Tables 3 and 4. The text only says values were chosen "such that the scale of the noise portion becomes comparable to the scale of the time-step embedding" (line 120). Reporting the defaults used in the main experiments is necessary for reproducibility.

### Trivial

5. **Minor presentation: TSG implementation example ("e.g., using t̃_emb for the first 10 layers") is given without specifying how many total layers the network has** — This makes the example harder to interpret.

---

## Nice-to-Haves

- A direct comparison between TSG and CFG on conditional models (e.g., conditional DiT-XL/2). While TSG's primary value is for unconditional models (where CFG cannot apply), such a comparison on conditional models would clarify whether TSG offers any advantage over CFG in settings where both are applicable.
- A brief discussion of failure cases or regimes where TSG degrades quality (the ablation notes that "too much noise hurts image quality" but quantitative evidence of this threshold would be useful).
- The ICG theoretical presentation could be tightened by acknowledging the network generalization gap explicitly and citing the empirical validation as support.

---

## Removed Points

- **"The ICG derivation is invalid / undercuts the paper's main contribution"** — The derivation is mathematically correct for the true distribution and the empirical validation is strong. The gap concerns whether the learned network approximates the correct quantity for out-of-distribution inputs, which is a moderately important subtlety (kept as Major weakness #1) but does *not* invalidate the core contribution.
- **"Statistical significance / confidence intervals"** — Not standard practice in large-scale diffusion benchmarks; single-run FID evaluation is the norm.
- **"Missing related works"** — Per instructions, I cannot independently verify the existence of missing references.
- **"Typos / formatting / garbled characters"** — Parser artifacts, not author errors.
- **Reproducibility nitpicks** about hyperparameters or training details that go beyond what is standard to disclose in a conference paper.

---

## Novel Insights

The two reviewers' perspectives reveal an interesting tension: the harsh critic identifies a genuine theoretical subtlety in ICG's derivation (the gap between the true-distribution identity and the learned network's behavior on out-of-distribution inputs), while the strength finder correctly notes that the empirical evidence is substantial and consistent across multiple architectures. The resolution is that the paper would benefit from a more precise framing of its theoretical contribution — presenting the derivation as a *motivation* rather than a *proof* — but the practical value of ICG is not in doubt. For TSG, neither reviewer fully probes a deeper question: whether the time-step perturbation is effectively performing an implicit ensemble over nearby noise levels, which would connect TSG to a broader literature on inference-time ensembling in diffusion models.

---

## Suggestions

1. **Acknowledge the ICG theoretical gap explicitly**: Add a sentence or paragraph noting that the derivation holds for the true data distribution, and that the empirical results confirm the network generalizes to independent-condition inputs despite the distribution shift during training. This would make the framing more precise without diminishing the contribution.

2. **Report the exact TSG hyperparameters** (s, α, layer range) used for each main result in Tables 3 and 4, either in the experiment setup or as a footnote.

3. **Add a brief quantitative comparison** between TSG and SAG/PAG on at least one shared unconditional benchmark (e.g., unconditional ImageNet 64×64 with a DiT or UNet backbone). Even a single row in a table would clarify the relative landscape.

---

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>