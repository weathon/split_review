Here is my final consolidated review:

---

## Summary

The paper proposes Zer0-Jack, a method for directly jailbreaking black-box Multi-modal Large Language Models (MLLMs) by optimizing image inputs using zeroth-order optimization (SPSA) with a patch-coordinate descent strategy (SPSA-P). Unlike prior work that relies on transfer attacks from white-box models, Zer0-Jack estimates gradients using only output logits, enabling direct black-box optimization. Experiments across MiniGPT-4, LLaVA1.5, and INF-MLLM1 show ASR of 88–98%, surpassing transfer-based baselines and approaching white-box performance, while using substantially less GPU memory (e.g., 10G vs. 15G for MiniGPT-4 7B).

## Strengths

- **First direct black-box jailbreak for MLLMs via zeroth-order optimization**: The paper introduces a genuinely novel approach for attacking black-box MLLMs without model access or transfer attacks. This fills an underexplored gap where prior black-box methods were limited to transfer attacks or handcrafted prompts.

- **Clear and substantial memory reduction validated across model sizes**: Table 1 reports concrete GPU memory figures showing Zer0-Jack uses 10G vs. 15G (MiniGPT-4 7B), 22G vs. 39G (13B), and successfully runs the 70B variant on a single A100 (63G) where the white-box baseline OOMs. This directly supports the memory-efficiency claim.

- **High ASR comparable to white-box attacks and dramatically exceeding transfer methods**: On the Harmful Behaviors dataset (Table 2), Zer0-Jack achieves 95% (MiniGPT-4), 90% (LLaVA1.5), and 88% (INF-MLLM1) — matching or exceeding the white-box baseline (93%, 91%, 86%) while all transfer-based baselines score ≤22%. On MM-SafetyBench-T (Table 3), the pattern is similar (98.2%, 95.8%, 96.4% vs. white-box 96.4%, 95.2%, 97.6%).

- **Patch-coordinate descent is a principled solution to high-dimensional gradient estimation error**: The method reduces the effective optimization dimension to ~0.02% of the full image (32×32 patches on 224×224 images), directly addressing the known weakness of zeroth-order methods in high dimensions.

- **Demonstration of feasibility on GPT-4o**: Section 3.6 shows a clever use of the `logit_bias` API feature to obtain log-probabilities for target tokens, successfully jailbreaking GPT-4o in a single showcase at ~$0.70 cost.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No direct black-box image-optimization baseline to isolate the patch mechanism's benefit**: The paper compares against transfer-based image baselines (A-Image) and text-based methods, but never includes a simple direct black-box image-optimization baseline such as SPSA on the full image, random search on patches, or coordinate-wise finite differences. Without this, the reader cannot tell whether the improvement attributed to SPSA-P comes from the patch coordinate descent specifically, or simply from applying zeroth-order optimization to the image at all. The paper's core contribution (SPSA-P) is not ablated against simpler alternatives.

- **No statistical variance reported for any ASR result**: All numbers in Tables 1–3 and Figure 2 are single values with no confidence intervals, standard deviations, or indication of runs/trials. Since SPSA-P involves random sampling of perturbation directions and patch order, the results are stochastic. Without variance estimates, it is impossible to assess whether the differences between methods (e.g., 95% vs. 93% on MiniGPT-4 HB) are meaningful.

- **Memory numbers contain an unexplained discrepancy**: Table 1 reports the white-box (WB) attack memory for MiniGPT-4 7B as 15G. However, Section 4.4 states "image-based optimization techniques such as A-Image and WB Attack, applied to MLLMs like MiniGPT-4, use about 19GB each." This 15G vs. 19G discrepancy is unaddressed. Additionally, the memory comparison mixes text-based methods evaluated on LLaMA2-7B with image-based methods on MiniGPT-4 without clearly noting that the underlying models differ.

- **No total query/forward-pass count**: The paper reports iteration counts (55 iterations) but not the total number of forward passes required per successful attack. Given that SPSA-P uses 2 forward passes per patch per iteration × 49 patches ≈ 98 forward passes per iteration, the total is ~5,390 — but this is never reported, making it harder to assess practical attack cost.

- **Missing hyperparameter values**: The smoothing parameter λ and learning rate α are introduced in the method section but their specific values are never stated. This hurts reproducibility.

- **No ablation of patch size**: The paper uses 32×32 patches for 224×224 images without discussing or ablating this choice. Patch size directly controls the trade-off between gradient estimation accuracy and optimization dimensionality.

- **GPT-4o evaluation limited to a single showcase**: The attack on GPT-4o is demonstrated with one example. While the paper acknowledges this is a "showcase," the claim that "our method can directly attack commercial MLLMs" would benefit from systematic evaluation on even a small set of queries.

- **Transferability evaluation only uses MiniGPT-4 as the source model**: Table 3 tests images optimized on MiniGPT-4 only. To fully characterize transferability, optimization on other source models (LLaVA1.5, INF-MLLM1) should also be tested.

### Trivial
- None beyond the points already listed as Minor.

## Nice-to-Haves
- Testing attack sensitivity to different initial images (e.g., random noise vs. COCO images vs. black image).
- Reporting per-category breakdown for MM-SafetyBench-T (which the paper mentions in Section 4.1 but the appendix is absent).

## Removed Points

These points are flagged to be removed, treat them with caution:

1. *"Missing related works (query-based adversarial attacks for image classifiers / LLMs)"* — Removed per guidelines: missing related works should not be cited without external verification.
2. *"The white-box baseline cannot serve as a baseline for the black-box setting"* — Removed: the paper explicitly states WB is an upper bound reported in the white-box setting, so this is not a flaw but transparency.
3. *"GPT-4 evaluation introduces biases"* — WEAKENED to removal: this is now standard practice in the jailbreak evaluation community; the paper cites the approach from Cai et al. (2024) which validates this methodology.
4. *"The dataset selection is on the smaller side"* — WEAKENED to removal: using 100/500 Harmful Behaviors items is standard for this line of work (many jailbreak papers use subsets), and the paper explains the random selection. The MM-SafetyBench-T dataset is used in full (168 items).

## Novel Insights

The reviews surface an important structural observation that goes beyond the paper's own contribution: while Zer0-Jack convincingly demonstrates that direct black-box jailbreaking of MLLMs is feasible and dramatically outperforms transfer attacks, the evaluation design conflates two distinct questions — "can zeroth-order optimization work for black-box jailbreaking?" (answered: yes) and "does the patch-coordinate descent specifically improve over naive zeroth-order methods?" (not separately tested). This distinction is crucial because it means the paper's specific technical novelty (SPSA-P vs. plain SPSA) is less supported than its high-level finding. Additionally, the GPT-4o logit-bias trick is an insightful practical contribution that could enable follow-up work on API-based attacks.

## Suggestions

1. **Add a simple direct black-box baseline**: Run SPSA on the full image without patch decomposition, or a random search on patches, on at least one model/dataset pair. This directly validates the benefit of the patch mechanism.
2. **Report variance**: Run each configuration 3–5 times with different random seeds and report mean ± std for ASR. This is especially important since SPSA-P involves random sampling.
3. **Reconcile memory numbers**: Clarify why Table 1 shows WB=15G for MiniGPT-4 7B while Section 4.4 says WB uses ~19GB. If these are different settings (image size, batch size, etc.), state this explicitly.
4. **Report total query count**: Add the number of forward passes per successful attack to the efficiency analysis.
5. **Disclose hyperparameters**: State the values of λ and α, even if chosen by simple heuristics.
6. **Ablate patch size**: Show results for at least 16×16, 32×32, 64×64, and full-image SPSA on one model to justify the 32×32 choice.
7. **Expand GPT-4o evaluation**: Test on 10–20 queries and report ASR, or at minimum characterize the cost and success pattern.

## Score and Decision

The paper presents a novel, well-motivated method with compelling empirical results that clearly demonstrate the viability of direct black-box jailbreaking for MLLMs. The weaknesses identified (missing ablation baseline, no variance reporting, memory discrepancies, missing hyperparameters) are all addressable and do not undermine the paper's core contribution — which is that direct zeroth-order optimization of image inputs achieves ASR comparable to white-box attacks while using far less memory. The paper is solid and the claims are largely supported by the evidence presented.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>