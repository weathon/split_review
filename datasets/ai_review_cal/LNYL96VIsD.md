- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper identifies a phenomenon called the "curse of singularities"—where parametric singularities (low stable rank) in weight matrices interact with concentrated Jacobian energy (SJE) to create a vicious cycle leading to training instability under large learning rates. The authors propose Parametric Singularity Smoothing (PSS), a lightweight method that detects impending instability via gradient norm ratios and smooths the singular spectrum of weight matrices. Experiments on BERT and GPT-2 models show that PSS expands the usable LR range by 5–10× with negligible overhead (≈0.21% of training time).

## Strengths

- **PSS demonstrably expands the usable LR range.** Table 1 and Figure 4(b) report that PSS achieves stable training on BERT-base at LRs up to 2e-3 (vs. 1e-4 for baseline) and on GPT-2-Medium proportionally, while Gradient Clipping and Orthogonal Regularization fail at these LRs. The effect holds across larger models (BERT-large, GPT-2-Large, GPT-2-XL) at up to 5× LR increase.

- **Computational overhead is genuinely negligible.** Table 2 shows the total additional overhead amounts to only 0.21% of baseline training time for BERT-base. The protection step triggers fewer than 10 times in most cases (<0.1% of steps even at extreme LRs), making the method practical for large-scale training.

- **Robustness to instability timing and smoothing policy.** Figure 5(a) demonstrates that PSS restores stable training even after the loss has fully diverged—a scenario where standard methods require restarts from checkpoints. Figure 5(b) confirms that multiple smoothing functions (clipping, softplus, etc.) all prevent instability, indicating the method does not depend on a fragile design choice.

- **The SR-SJE cycle analysis provides a plausible mechanistic link** between singularities and training instability, moving beyond correlational observations to describe a specific feedback loop (singularity → rank-deficient representations → increased SJE → further singularity).

## Weaknesses

### Major

- **Missing comparison against spectral normalization.** The paper compares PSS only against Gradient Clipping and Orthogonal Regularization. Spectral normalization (Miyato et al., 2018) is the most natural competitor: it directly constrains the spectral norm of weight matrices, operates in the same conceptual space as PSS, and is cited in the paper's own related work section. Without this baseline, the reader cannot assess whether PSS offers a genuine advantage over a simpler, well-established method that also manipulates singular values. The paper's central claim—that PSS is superior for enabling large LRs—is incompletely supported. *This is verifiable from the paper: Section 4.1 lists only GC and OR as baselines; spectral normalization is mentioned only in the related work (line 212).*

- **Detection mechanism is conceptually disconnected from the analysis.** The analysis (Section 2.2) uses SJE—the *distribution* of Jacobian energy on singular vectors within the stable rank—to explain the vicious cycle driving instability. The detection mechanism uses the *magnitude* of gradient norms (‖g‖_F). The paper never demonstrates that gradient norm spikes reliably correlate with SJE increases or are a faithful proxy for the singularity-driven cycle. Figure 3 shows a gradient norm spike in one explosion case, but this is a single example. If the cycle is driven by changing *distribution* of Jacobian energy, the detection choice (gradient norm magnitude) appears driven by computational convenience rather than flowing naturally from the analysis. This weakens internal coherence. *The paper states (line 109): "The curse of singularities is observed to constantly befall with gradients of significantly increasing magnitudes"—asserted but not quantitatively supported.*

- **No ablation separating detection from protection.** PSS has two components: (a) detection via gradient norm ratio, and (b) protection via SVD-based smoothing. The paper does not ablate detection—for example, by applying protection at a fixed interval without detection, or by always applying it. Figure 5(a) shows that PSS works even after full divergence, so detection may not be necessary for stability; it may only avoid short loss spikes. The paper mentions no experiment to isolate this. *Confirmed: search for "ablat" returns no matches in the paper.*

### Minor

- **The central empirical phenomenon ("curse of singularities") is supported by only one illustrative example.** Section 2.2 presents figures from a single BERT-base run on Wikitext. The paper asserts (line 79) "the observations are prevalent across networks and datasets" but provides no quantitative evidence—no statistics across seeds, architectures, or datasets for the SR/SJE trajectories. Figure 3 shows one explosion case (blue) and one stable case (red). The motivation for the method rests on this pattern; without replication, the reader cannot assess whether it is a robust precursor to instability or a coincidental correlation. *This is a weakness in the scientific claim about the phenomenon, though the method's effectiveness is validated separately through the main results.*

- **Loss explosion is never explicitly defined.** The paper tracks "frequency of loss explosions" in Table 1 and Figure 4(a) but never specifies the criterion used—whether it is loss exceeding a threshold, perplexity becoming NaN/inf, or some other condition. This hurts reproducibility. *No definition found in Sections 4.1 or 4.2.*

- **The smoothing function f_smooth used in the main experiments is not specified.** The paper lists several options (Logarithmic with Scaling, Softplus, Softmax, convolution, clipping) but does not state which one is used for the results in Table 1, Figure 4, or Table 2. This under-specifies the method. *Lines 139–140 list options but never identify which was used.*

- **The 2.40× per-step overhead conflicts with the claim that "DDD's cost is comparable to a forward-backward step."** The paper states DDD's complexity is O(mn log k) vs. forward-backward O(mnb), and "comparable" (line 181). Yet a single PSS invocation costs 2.40× the baseline step. The discrepancy likely arises because the protection step includes power iteration, DDD, smoothing, and reparameterization across all modules, but this is not explained. *Line 183 reports the 2.40× figure; line 181 claims DDD cost is "comparable." Clarification needed.*

### Trivial

- The abstract and list of contributions claim "5-10× increase," while Figure 4(b) reports 20× for BERT-base (1e-4→2e-3, a 20× increase over baseline, 10× over best baseline at 2e-4). The range in the abstract is reasonable but the individual numbers could be stated more precisely to avoid confusion with what is 5×, 10×, or 20× in different settings.

## Nice-to-Haves

- **Sensitivity analysis for τ.** The detection threshold τ=2.5 is used throughout; a brief ablation (e.g., τ∈{1.5, 2.0, 2.5, 3.0, 5.0}) would strengthen the claim that the choice is robust (currently asserted but not demonstrated).
- **Specification of α** (the smoothing coefficient for the gradient moving average). The paper says "typically 0<α≤1" but does not give the value used.

## Removed Points

These points were raised by the harsh critic but removed or downgraded based on verification against the paper:

- **"Table 1 only goes up to 8e-4; 2e-3 claim unsupported"** — The 2e-3 claim is supported by Fig. 4(b) (test loss across LRs), not Table 1. The paper presents evidence; the critic misread which figure supports the claim. However, the paper would benefit from showing explicit stability counts at 2e-3, so this concern is demoted to the minor weakness about missing stability data at the stated LR limit.

- **"Missing comparison to spectral normalization in related work"** — Per the rules, missing related work criticisms are excluded. The baseline omission is already noted as a major weakness.

- **"Single-run figures need error bars"** — The paper reports 3 seeds for stability tests (Table 1). The analysis plots (Figures 1-3, 6) are illustrative; this is standard for observational analyses. Requesting error bars for every qualitative figure would be excessive. This is covered adequately by noting the lack of statistical replication for the phenomenon claim.

- **"NTK λ_max computation not defined"** — The paper describes it adequately: "the principal eigenvalue of a modified Neural Tangent Kernel (NTK) matrix (Jacot et al., 2018), where each element captures the dot product of normalized gradients between pairs of data points" (line 100). This is sufficient for an empirical paper.

- **"The 5-10× claim vs 20× discrepancy is inconsistent"** — The paper states "5-10× increase" in the abstract and "10-fold improvement" (over the baseline's best range) for BERT-base. For larger models it says "up to 5 times." The abstract's range covers all experiments. This is a minor precision issue, not an inconsistency. Demoted from the harsh critic's "erodes trust" framing.

- Various minor reproducibility/specification nitpicks (DDD accuracy, energy-based detection alternative) that are not central to the paper's validity.

## Novel Insights

Reviewers noted the conceptual disconnect between the SJE-based analysis (distribution of Jacobian energy) and the gradient-norm-magnitude detection mechanism as an under-explored tension. If the vicious cycle is fundamentally about the *distribution* of Jacobian energy concentrating on dominant directions, then detecting instability via gradient *magnitude* is an indirect proxy. The paper could have detected via SJE directly (at higher cost) but chose not to, and provides no evidence that the proxy is faithful. This points to a potential design alternative that could either strengthen or simplify the method: using direct spectral metrics for detection, or abandoning the SJE framework as an explanatory model if gradient magnitude is sufficient.

## Suggestions

1. **Add spectral normalization as a baseline** — This is essential. Compare the maximum stable LR, final perplexity, and computational cost of PSS against spectral normalization (and ideally its adaptive variants). If PSS matches spectral normalization, the contribution shifts to the analysis of *when* instability occurs; if PSS outperforms it, the method's advantage is established.

2. **Ablate detection** — Run PSS with detection removed (apply smoothing at a fixed interval, e.g., every N steps, or always-on) and report the trade-off between loss spikes, overhead, and stability. This clarifies whether the gradient-ratio detection mechanism adds value beyond periodic smoothing.

3. **Quantify the curse-of-singularities pattern across runs** — Report statistics (mean and variance of SR at steps t−{10,5,3,1} before explosion across multiple seeds) to turn the single qualitative example into a robust empirical finding.

4. **Specify f_smooth and define "loss explosion"** — State which smoothing function was used in the main experiments and specify the explosion criterion (e.g., loss > threshold, perplexity = NaN, or gradient norm > threshold). These are small fixes that significantly improve reproducibility.
