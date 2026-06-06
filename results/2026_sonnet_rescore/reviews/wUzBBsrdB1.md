## Summary

This paper investigates how the sparsity hyperparameter L0 in Sparse Autoencoders (SAEs) affects feature quality, arguing that L0 is not a free "tradeoff knob" but has a data-determined correct value. Using controlled toy model experiments with known ground-truth features, the paper demonstrates that both too-low and too-high L0 cause feature mixing, that MSE loss actively incentivizes incorrect features when L0 is too low, and that standard sparsity-reconstruction tradeoff plots are therefore misleading. The authors propose a practical diagnostic metric — decoder pairwise cosine similarity (c_dec) — which is minimized at the true L0 in toy models and aligns with peak sparse probing performance in Gemma-2-2b and Llama-3.2-1b LLM SAEs.

---

## Strengths

- **Toy model ground-truth validation is clean and decisive.** Sections 3.1–3.2 and Figure 1 use a 50-feature toy model with orthogonal true features and a known correlation structure. At the true L0 of 11, the SAE exactly recovers all ground-truth features; at L0=5, every latent mixes correlated components; at L0=18, many are corrupted. This controlled setup constitutes strong, direct evidence for the core claim.

- **Concrete quantitative refutation of MSE as a quality signal (Section 3.3, Figure 4).** The paper shows that a trained SAE with incorrect, polysemantic latents achieves MSE 2.73 while the ground-truth SAE achieves MSE 4.88 at the same low L0. Figure 4 extends this across a range of L0 values below the true L0, demonstrating that trained SAEs systematically outperform the correct ground-truth SAE on the standard evaluation metric. This is the strongest piece of evidence in the paper.

- **c_dec metric is practical and well-validated in toy models.** Figure 6 shows a clean global minimum at the true L0 of 11 across 5 random seeds. The metric is simple to compute (a pairwise average of absolute decoder cosine similarities), has an intuitive motivation, and comes with code (Appendix A.17) and theoretical justification (Appendix A.6).

- **Cross-architecture replication (Section 3.6, Figure 7).** JumpReLU SAEs also minimize c_dec at the true L0, confirming that the phenomenon is not an artifact of BatchTopK. The "sticking" observation — that JumpReLU training naturally resists straying far from the correct L0 over a wide range of λ_s — is a meaningful, practical insight.

- **LLM validation across multiple models and layers (Figure 8, Figure 9).** The paper trains SAEs on Gemma-2-2b (layers 5 and 12) and Llama-3.2-1b (layer 7), covering both BatchTopK and JumpReLU architectures, with 3 seeds per L0. The c_dec elbow aligns with peak sparse probing F1 in all examined cases.

- **Decoder projection histograms reveal inhomogeneous failure modes (Section 4.2, Figure 9 right).** At L0=750, the projection distribution shows a narrow central peak plus a heavy positive tail, suggesting some latents are over-saturated while others are under-triggered simultaneously. This is a genuinely novel diagnostic observation.

---

## Weaknesses

### Fatal
None.

### Major

- **The c_dec metric's behavior in LLMs is significantly messier than in toy models, and the guidance shifts in a way that is underspecified.** In toy models (Figure 6), c_dec has a clean global minimum at the true L0 — unambiguous and programmatically actionable. In LLMs (Figure 8, top-left), Gemma-2-2b layer 5 shows a sharp early drop followed by a long flat region, with the global minimum inside the flat zone; the paper then shifts the prescription from "use the minimum" to "use the elbow just before c_dec jumps due to low L0." The paper acknowledges this directly in Section 6 ("the metric can sometimes remain nearly flat for a wide range of L0") but provides no mechanistic explanation for why the clean toy-model behavior does not transfer, and no reliable operationalization of "elbow finding." For practitioners who need to apply this in new settings, the practical guidance is currently underspecified. The paper should either provide a concrete heuristic for elbow detection (with evaluation of its reliability across the three layer/model instances where results exist) or more explicitly scope the metric as an "avoid clearly-too-low L0" guard rather than an L0 selection procedure.

- **Validating c_dec against sparse probing introduces a proxy-on-proxy concern.** In LLMs there are no ground-truth features, so c_dec is validated by checking that its elbow aligns with peak k-sparse probing F1 (Kantamneni et al., 2025). This is a meaningful and widely-used evaluation, but sparse probing measures whether SAE features are linearly useful for predicting downstream properties — it is not a direct measure of whether SAE latents correspond to the underlying true features of the LLM. If both c_dec and sparse probing peak at the same L0 but neither is directly measuring "correctness," their alignment demonstrates consistency between two proxies. The paper should be explicit that the LLM evidence establishes consistency between c_dec and a useful downstream metric, rather than direct validation against ground truth.

### Minor

- **The high-L0 degradation mechanism is underexplained relative to the low-L0 case.** Section 3.3 provides a clear, quantitative, mechanistic account of why MSE incentivizes feature mixing at low L0. The high-L0 case (Section 3.2, Figure 1 right) shows degenerate solutions but does not explain what drives them. Section 4.2's explanation ("some latents fire too much while others fire too little") is explicitly framed as a suspicion rather than a demonstrated mechanism. Given that high-L0 failure appears in the abstract, Figure 1, and Section 3.2, the asymmetric treatment is a gap.

- **The headline claim "most commonly used SAEs have an L0 that is too low" is stronger than the evidence strictly warrants.** This claim is based on (a) a survey of Neuronpedia entries showing L0 < 100 is common, and (b) LLM experiments across two models and a handful of layers suggesting optimal L0 is ~200. The inference is plausible, but optimal L0 likely varies significantly by model scale, layer, and data distribution — variation the paper acknowledges only in passing (Figure 8 caption: "the shapes of the c_dec plots vary"). Softening this to "we find suggestive evidence that widely deployed SAEs may have too-low L0" would be more accurate.

### Trivial

None beyond the above.

---

## Nice-to-Haves

- **Characterizing what data-distribution properties determine the true L0.** The toy model gives full control over firing probabilities and feature correlations. Showing how the c_dec minimum shifts as a function of these parameters would deepen the theoretical picture and help practitioners estimate appropriate L0 ranges before training — particularly relevant since different LLM layers likely have very different activation statistics.

- **The SAE width × L0 interaction is absent.** If width is doubled, does optimal L0 scale proportionally? This is practically important for anyone sweeping both hyperparameters. Even a brief toy-model ablation would add value.

- **The JumpReLU "sticking" behavior deserves more prominence.** The observation that a wide range of λ_s values cause JumpReLU to converge near the correct L0 is practically important and currently buried in a single paragraph (Section 3.6). It directly addresses the practitioner's question: "how sensitive is JumpReLU to λ_s misspecification?"

- **The possibility of optimizing c_dec during training** is mentioned in Section 6 and Appendix A.11 as future work. Even a brief sketch of the obstacles would help readers understand the difficulty and assess the feasibility.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Absolute-value in c_dec definition.** The harsh critic questions whether signed pairwise cosine similarity might provide additional information, given that positive and negative correlations produce opposite mixing patterns. However, the paper's motivation for |cos| is clear: both types of mixing increase decoder non-orthogonality, and the absolute value makes c_dec sensitive to both simultaneously. This is a design choice that is reasonable on its face; one sentence in the paper would be sufficient to address it but it is not a flaw.

- **Section 3.3 is "too brief" without a derivation.** The critic notes that a derivation of why MSE rewards mixing would strengthen Section 3.3 and that Appendix A.6 "may already provide this." Under our rules, we do not penalize for content known to exist in appendices (which are stripped from the reviewed text). Removed.

- **Request for formal operationalization of elbow detection.** Upgraded to the Major weakness (above) in properly scoped form; the request for "evaluation of how often the heuristic succeeds" is merged there. Removed as a separate item.

- **Coverage of only two models as a weakness.** Characterized more precisely as context for the proxy-on-proxy concern and the overclaiming concern above; removed as a freestanding weakness since it does not independently invalidate the contribution.

---

## Novel Insights

The most genuinely novel and underappreciated contribution is the MSE-as-adversary demonstration in Section 3.3: standard SAE training objectives do not merely fail to enforce correct features when L0 is misspecified — they *actively penalize* an SAE that would produce the correct answer. This reframes the problem from "SAEs are imperfect tools" to "our evaluation and training objectives jointly encode a systematic bias against correctness at low L0." The decoder projection histogram result at L0=750 in Section 4.2 is a secondary but genuinely interesting finding: that a single global L0 target may be simultaneously too high for some latents and too low for others, partially explaining why JumpReLU's per-latent threshold learning yields better high-L0 performance than BatchTopK.

---

## Suggestions

1. **Provide an operational elbow-finding procedure.** Even a heuristic (e.g., largest second derivative, or inflection point detection on a smoothed curve) with a report of how reliably it identifies the peak-probing-F1 L0 across the three layer/model instances in the paper would substantially strengthen the practical contribution.

2. **Add a paragraph to Section 3.2 sketching the high-L0 mechanism.** The toy model gives full ground-truth access — what is the decoder similarity structure at L0=18, and what gradient signal drives it toward mixing? Even an informal account would make the high-L0 treatment comparable in depth to the low-L0 treatment.

3. **Explicitly acknowledge the proxy-on-proxy limitation in LLM results.** A sentence in Section 4 or the Discussion noting that sparse probing alignment validates c_dec as a practical diagnostic but does not constitute ground-truth verification would appropriately scope the LLM evidence.

4. **Temper the "most SAEs are too sparse" claim** to reflect its empirical basis: two models, limited layers, and a Neuronpedia survey of L0 distributions. The underlying claim is plausible and worth highlighting; the framing need only be made more careful.

---

## Evaluation on Core Axes

- **Originality:** The insight that L0 has a correct value (not a tradeoff), the MSE-adversary demonstration, and the c_dec metric are all novel contributions. The connection to feature hedging is acknowledged. 4/5.
- **Importance:** Directly relevant to anyone training or using SAEs for mechanistic interpretability. The field is active and the practical stakes (whether widely used SAEs are systematically misconfigured) are high. 4/5.
- **Claims supported:** Toy model claims are very well supported; LLM claims are supported at the consistency-with-proxy level and are appropriately caveated in most (though not all) places. 3/5.
- **Soundness:** Experimental design is careful; controlled toy models are the right approach; LLM setup (32768-width, 500M–1B tokens, multiple seeds) is reasonable. The c_dec-to-elbow shift is the main soundness gap. 3/5.
- **Clarity:** Well-organized, with clear exposition of toy model → LLM pipeline and honest discussion of limitations. 4/5.
- **Community value:** High — provides actionable guidance (use c_dec to detect clearly-too-low L0) and a critical warning (sparsity-reconstruction tradeoff plots are misleading). The code provision and SAELens integration make it usable. 4/5.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>